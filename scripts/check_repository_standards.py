#!/usr/bin/env python3
"""Read-only, source-pinned repository standards evidence probe (Organization #288).

This is a deterministic S3/S3* support tool, not an S3 decision or independent
S3* judgment. Only the already-adopted routing invariant is mandatory.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable
from urllib.parse import quote

try:
    from scripts.check_public_routing import (
        DEFAULT_API_BASE,
        RoutingError,
        api_json,
        bootstrap_marker_present,
        decode_readme_payload,
        route_marker_present,
        scope_repositories_from_readme,
        todo_marker_present,
    )
except ModuleNotFoundError:  # python scripts/check_repository_standards.py
    from check_public_routing import (  # type: ignore[no-redef]
        DEFAULT_API_BASE,
        RoutingError,
        api_json,
        bootstrap_marker_present,
        decode_readme_payload,
        route_marker_present,
        scope_repositories_from_readme,
        todo_marker_present,
    )


@dataclass(frozen=True)
class Finding:
    repository: str
    dimension: str
    status: str  # PASS / DRIFT / NON_COMPLIANT / UNKNOWN
    rule: str  # REQUIRED / ADVISORY
    detail: str
    source: str


def _endpoint(repo: str, suffix: str, api_base: str) -> str:
    owner, name = repo.split("/", 1)
    return f"{api_base.rstrip('/')}/repos/{quote(owner)}/{quote(name)}{suffix}"


def _read(
    repo: str,
    suffix: str,
    *,
    api_base: str,
    token: str | None,
    get_json: Callable[[str, str | None], object],
) -> tuple[object | None, str | None, str]:
    url = _endpoint(repo, suffix, api_base)
    try:
        return get_json(url, token), None, url
    except (RoutingError, OSError, ValueError) as exc:
        return None, str(exc), url


def inspect_repository(
    repo: str,
    *,
    in_scope: bool,
    token: str | None = None,
    api_base: str = DEFAULT_API_BASE,
    get_json: Callable[[str, str | None], object] = api_json,
    organization: str = "opensiro",
) -> tuple[str | None, list[Finding]]:
    """Inspect primary GitHub evidence; preserve uncertainty per dimension."""
    findings: list[Finding] = []

    def record(dimension: str, status: str, rule: str, detail: str, source: str) -> None:
        findings.append(Finding(repo, dimension, status, rule, detail, source))

    metadata, error, url = _read(repo, "", api_base=api_base, token=token, get_json=get_json)
    if not isinstance(metadata, dict) or error:
        record("repository_metadata", "UNKNOWN", "REQUIRED" if in_scope else "ADVISORY",
               error or "invalid metadata JSON", url)
        return None, findings
    if metadata.get("full_name") != repo or metadata.get("private") is not False:
        record("repository_metadata", "UNKNOWN", "REQUIRED" if in_scope else "ADVISORY",
               "repository identity/public access could not be verified", url)
        return None, findings
    branch = metadata.get("default_branch")
    if not isinstance(branch, str) or not branch:
        record("default_branch", "UNKNOWN", "ADVISORY", "no default branch in metadata", url)
        return None, findings
    record("default_branch", "PASS" if branch == "main" else "DRIFT", "ADVISORY",
           f"default branch is {branch}; comparison baseline is main", url)
    deletion = metadata.get("delete_branch_on_merge")
    record("delete_branch_on_merge", "PASS" if deletion is True else "DRIFT" if deletion is False else "UNKNOWN",
           "ADVISORY", f"delete_branch_on_merge={deletion!r}; five-repo observed baseline=true", url)

    branch_payload, error, url = _read(
        repo, f"/branches/{quote(branch, safe='')}", api_base=api_base, token=token, get_json=get_json
    )
    head_sha = branch_payload.get("commit", {}).get("sha") if isinstance(branch_payload, dict) else None
    protected = branch_payload.get("protected") if isinstance(branch_payload, dict) else None
    if error or not isinstance(protected, bool):
        record("branch_protected", "UNKNOWN", "ADVISORY", error or "protected not a boolean", url)
    else:
        record("branch_protected", "PASS" if protected else "DRIFT", "ADVISORY",
               f"GitHub branch protected={protected}; check actual rules separately", url)

    # Mutable settings are a point-in-time observation. Root source artifacts,
    # by contrast, must be fetched at one immutable commit or marked unknown.
    pinned = isinstance(head_sha, str) and len(head_sha) == 40

    rulesets, error, url = _read(repo, "/rulesets", api_base=api_base, token=token, get_json=get_json)
    if error or not isinstance(rulesets, list):
        record("protect_main_ruleset", "UNKNOWN", "ADVISORY", error or "rulesets not a list", url)
    else:
        active = [r.get("name") for r in rulesets if isinstance(r, dict) and r.get("enforcement") == "active"]
        found = "Protect main" in active
        record("protect_main_ruleset", "PASS" if found else "DRIFT", "ADVISORY",
               f"active rulesets={active!r}; a protected branch can use legacy protection", url)

    if not pinned:
        pin_url = _endpoint(repo, f"/branches/{quote(branch, safe='')}", api_base)
        record("pinned_head", "UNKNOWN", "REQUIRED" if in_scope else "ADVISORY",
               "immutable default-branch head unavailable; source checks not attempted", pin_url)
        for dimension in ("common_start_here", "organization_route", "shared_todo"):
            record(dimension, "UNKNOWN", "REQUIRED" if in_scope else "ADVISORY",
                   "no immutable revision for README", pin_url)
        for dimension in ("root_license", "workflow_files"):
            record(dimension, "UNKNOWN", "ADVISORY", "no immutable source revision", pin_url)
        return None, findings

    ref = quote(head_sha, safe="")

    readme_payload, error, url = _read(
        repo, f"/readme?ref={ref}", api_base=api_base, token=token, get_json=get_json
    )
    try:
        readme = decode_readme_payload(readme_payload) if not error else None
    except RoutingError as exc:
        readme, error = None, str(exc)
    route_rule = "REQUIRED" if in_scope else "ADVISORY"
    routing = {
        "common_start_here": bootstrap_marker_present,
        "organization_route": route_marker_present,
        "shared_todo": todo_marker_present,
    }
    for dimension, marker in routing.items():
        if readme is None:
            record(dimension, "UNKNOWN", route_rule, error or "no readable README", url)
        else:
            found = marker(repo, readme, organization)
            status = "PASS" if found else "NON_COMPLIANT" if in_scope else "DRIFT"
            record(dimension, status, route_rule,
                   "README entry present" if found else "README entry missing; adjacent comparison is non-binding" if not in_scope else "required README entry missing", url)

    root, error, url = _read(
        repo, f"/contents?ref={ref}", api_base=api_base, token=token, get_json=get_json
    )
    if error or not isinstance(root, list):
        record("root_license", "UNKNOWN", "ADVISORY", error or "root listing unavailable", url)
    else:
        files = {item.get("name", "") for item in root if isinstance(item, dict) and item.get("type") == "file"}
        found = any(name == "LICENSE" or name.startswith("LICENSE.") for name in files)
        record("root_license", "PASS" if found else "DRIFT", "ADVISORY",
               "root LICENSE present" if found else "no root LICENSE file in directory listing", url)

    workflows, error, url = _read(
        repo, f"/contents/.github/workflows?ref={ref}",
        api_base=api_base, token=token, get_json=get_json,
    )
    if error or not isinstance(workflows, list):
        record("workflow_files", "UNKNOWN", "ADVISORY", error or "workflows listing unavailable", url)
    else:
        found = any(item.get("type") == "file" and str(item.get("name", "")).endswith((".yml", ".yaml"))
                    for item in workflows if isinstance(item, dict))
        record("workflow_files", "PASS" if found else "DRIFT", "ADVISORY",
               "GitHub Actions workflow file present" if found else "no YAML workflow file listed", url)

    return head_sha, findings


def build_report(
    scope_readme: str,
    *,
    adjacent: list[str] | None = None,
    get_json: Callable[[str, str | None], object] = api_json,
    token: str | None = None,
    api_base: str = DEFAULT_API_BASE,
    as_of: str | None = None,
) -> dict[str, object]:
    scope = scope_repositories_from_readme(scope_readme)
    extras = list(dict.fromkeys(adjacent or []))
    for repo in extras:
        if not repo.startswith("opensiro/") or repo.count("/") != 1:
            raise RoutingError(f"invalid adjacent repository: {repo!r}")
    repos = list(dict.fromkeys([*scope, *extras]))
    items: list[dict[str, object]] = []
    for repo in repos:
        sha, findings = inspect_repository(repo, in_scope=repo in scope, get_json=get_json,
                                           token=token, api_base=api_base)
        items.append({"repository": repo, "in_scope": repo in scope, "default_head_sha": sha,
                      "findings": [asdict(f) for f in findings]})
    return {"as_of_utc": as_of or datetime.now(timezone.utc).isoformat(),
            "system_in_focus": "opensiro/vsm-oss-organization: current five-repository boundary",
            "classification_note": "A probe supports judgment; it is not an S3 decision or independent S3* audit",
            "repositories": items}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scope-readme", default="README.md")
    parser.add_argument("--compare-adjacent", action="append", default=[])
    parser.add_argument("--api-base", default=DEFAULT_API_BASE)
    parser.add_argument("--format", choices=("json", "summary"), default="summary")
    args = parser.parse_args(argv)
    try:
        scope_text = Path(args.scope_readme).read_text(encoding="utf-8")
        report = build_report(scope_text, adjacent=args.compare_adjacent,
                              token=os.environ.get("GITHUB_TOKEN"), api_base=args.api_base)
    except (OSError, UnicodeDecodeError, RoutingError) as exc:
        print(f"repository standards probe ERROR: {exc}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for item in report["repositories"]:
            print(f"{item['repository']} @ {item['default_head_sha'] or 'UNKNOWN'} "
                  f"({'in-scope' if item['in_scope'] else 'adjacent'})")
            for finding in item["findings"]:
                print(f"  {finding['status']:<14} {finding['dimension']:<25} "
                      f"[{finding['rule']}] {finding['detail']}")
    findings = [f for item in report["repositories"] for f in item["findings"]]
    if any(f["rule"] == "REQUIRED" and f["status"] == "UNKNOWN" for f in findings):
        return 2
    if any(f["rule"] == "REQUIRED" and f["status"] == "NON_COMPLIANT" for f in findings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
