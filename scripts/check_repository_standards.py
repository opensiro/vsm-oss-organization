#!/usr/bin/env python3
"""Read-only, source-pinned repository standards evidence probe (Organization #288).

This is a deterministic S3/S3* support tool, not an S3 decision or independent
S3* judgment. Only the already-adopted routing invariant is mandatory.
"""

from __future__ import annotations

import argparse
import json
import os
import posixpath
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable
from urllib.parse import quote, unquote, urlsplit

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
    rule: str  # REQUIRED / ADVISORY (a comparison is not a policy mandate)
    detail: str
    source: str


_INLINE_MARKDOWN_LINK = re.compile(r"\]\(([^)\s]+)(?:\s+[^)]*)?\)")
_FENCED_CODE = re.compile(r"(?ms)^\s*```[^\n]*\n.*?^\s*```[^\n]*$")


def _readme_local_targets(readme: str) -> tuple[set[str], set[str]]:
    """Extract simple relative Markdown links from a root README.

    This intentionally excludes external URLs, reference-style links and
    cross-file fragments; it is a conservative navigation check, not a full
    Markdown renderer or a GitHub Pages link crawler.
    """
    without_code = _FENCED_CODE.sub("", readme)
    paths: set[str] = set()
    local_fragments: set[str] = set()
    for raw in _INLINE_MARKDOWN_LINK.findall(without_code):
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc or raw.startswith("//"):
            continue
        if not parsed.path and parsed.fragment:
            local_fragments.add(unquote(parsed.fragment).lower())
        elif parsed.path:
            path = posixpath.normpath(unquote(parsed.path))
            if path != ".":
                paths.add(path)
    return paths, local_fragments


def _readme_heading_anchors(readme: str) -> set[str]:
    """GitHub-like slugs for ordinary ATX headings (including duplicates)."""
    without_code = _FENCED_CODE.sub("", readme)
    seen: dict[str, int] = {}
    anchors: set[str] = set()
    for line in without_code.splitlines():
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+)$", line)
        if not match:
            continue
        title = re.sub(r"\s+#+\s*$", "", match.group(1)).strip()
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        if slug:
            suffix = seen.get(slug, 0)
            anchors.add(f"{slug}-{suffix}" if suffix else slug)
            seen[slug] = suffix + 1
    return anchors


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

    def record_unavailable_source(reason: str, source: str) -> None:
        """An unavailable immutable ref cannot silently skip mandatory routing."""
        route_rule = "REQUIRED" if in_scope else "ADVISORY"
        record("pinned_head", "UNKNOWN", route_rule, reason, source)
        for dimension in ("common_start_here", "organization_route", "shared_todo"):
            record(dimension, "UNKNOWN", route_rule,
                   f"source checks not attempted: {reason}", source)
        for dimension in ("root_license", "root_contributing", "workflow_files"):
            record(dimension, "UNKNOWN", "ADVISORY",
                   f"source checks not attempted: {reason}", source)
        record("readme_local_links", "UNKNOWN", "ADVISORY",
               f"source checks not attempted: {reason}", source)

    metadata, error, url = _read(repo, "", api_base=api_base, token=token, get_json=get_json)
    if not isinstance(metadata, dict) or error:
        record("repository_metadata", "UNKNOWN", "REQUIRED" if in_scope else "ADVISORY",
               error or "invalid metadata JSON", url)
        return None, findings
    if metadata.get("full_name") != repo or metadata.get("private") is not False:
        record("repository_metadata", "UNKNOWN", "REQUIRED" if in_scope else "ADVISORY",
               "repository identity/public access could not be verified", url)
        return None, findings
    description = metadata.get("description")
    record("repository_description",
           "PASS" if isinstance(description, str) and description.strip() else
           "DRIFT" if "description" in metadata else "UNKNOWN",
           "ADVISORY", "nonempty public description" if description else
           "no description supplied or field unavailable", url)
    topics = metadata.get("topics")
    record("repository_topics",
           "PASS" if isinstance(topics, list) and topics else
           "DRIFT" if isinstance(topics, list) else "UNKNOWN",
           "ADVISORY", f"public discovery topics={topics!r}; optional metadata", url)
    license_metadata = metadata.get("license")
    license_id = license_metadata.get("spdx_id") if isinstance(license_metadata, dict) else None
    record("github_license_detection",
           "PASS" if isinstance(license_id, str) and license_id not in ("", "NOASSERTION") else
           "DRIFT" if "license" in metadata else "UNKNOWN",
           "ADVISORY", f"GitHub SPDX detection={license_id!r}; a root license may still be valid", url)
    branch = metadata.get("default_branch")
    if not isinstance(branch, str) or not branch:
        record("default_branch", "UNKNOWN", "ADVISORY", "no default branch in metadata", url)
        record_unavailable_source("immutable default-branch head unavailable", url)
        return None, findings
    record("default_branch", "PASS" if branch == "main" else "DRIFT", "ADVISORY",
           f"default branch is {branch}; comparison baseline is main", url)
    deletion = metadata.get("delete_branch_on_merge")
    record("delete_branch_on_merge", "PASS" if deletion is True else "DRIFT" if deletion is False else "UNKNOWN",
           "ADVISORY", f"delete_branch_on_merge={deletion!r}; observed comparison=true, not mandatory policy", url)

    branch_payload, error, url = _read(
        repo, f"/branches/{quote(branch, safe='')}", api_base=api_base, token=token, get_json=get_json
    )
    commit = branch_payload.get("commit") if isinstance(branch_payload, dict) else None
    head_sha = commit.get("sha") if isinstance(commit, dict) else None
    protected = branch_payload.get("protected") if isinstance(branch_payload, dict) else None
    if error or not isinstance(protected, bool):
        record("branch_protected", "UNKNOWN", "ADVISORY", error or "protected not a boolean", url)
    else:
        record("branch_protected", "PASS" if protected else "DRIFT", "ADVISORY",
               f"GitHub branch protected={protected}; check actual rules separately", url)

    # Mutable settings are a point-in-time observation. Root source artifacts,
    # by contrast, must be fetched at one immutable commit or marked unknown.
    pinned = (isinstance(head_sha, str) and len(head_sha) == 40
              and all(char in "0123456789abcdefABCDEF" for char in head_sha))

    rulesets, error, url = _read(repo, "/rulesets", api_base=api_base, token=token, get_json=get_json)
    if error or not isinstance(rulesets, list):
        record("protect_main_ruleset", "UNKNOWN", "ADVISORY", error or "rulesets not a list", url)
    else:
        active = [r.get("name") for r in rulesets if isinstance(r, dict) and r.get("enforcement") == "active"]
        found = "Protect main" in active
        record("protect_main_ruleset", "PASS" if found else "DRIFT", "ADVISORY",
               f"active rulesets={active!r}; a protected branch can use legacy protection", url)
        candidates = [r for r in rulesets if isinstance(r, dict) and
                      r.get("name") == "Protect main" and r.get("enforcement") == "active"]
        ruleset_id = candidates[0].get("id") if candidates else None
        if isinstance(ruleset_id, int) and ruleset_id > 0:
            rules, detail_error, detail_url = _read(
                repo, f"/rulesets/{ruleset_id}", api_base=api_base, token=token, get_json=get_json
            )
            entries = rules.get("rules") if isinstance(rules, dict) else None
            if detail_error or not isinstance(entries, list):
                record("ruleset_gate_evidence", "UNKNOWN", "ADVISORY",
                       detail_error or "ruleset details unavailable", detail_url)
            else:
                pr_rules = [r for r in entries if isinstance(r, dict) and r.get("type") == "pull_request"]
                review_count = (pr_rules[0].get("parameters", {}).get("required_approving_review_count")
                                if pr_rules and isinstance(pr_rules[0].get("parameters"), dict) else None)
                status_check_rule = any(isinstance(r, dict) and r.get("type") == "required_status_checks"
                                        for r in entries)
                record("ruleset_gate_evidence", "PASS", "ADVISORY",
                       f"observed ruleset only: required_approvals={review_count!r}, "
                       f"required_status_checks_rule={status_check_rule}; "
                       "other branch protection controls not attested", detail_url)
        else:
            record("ruleset_gate_evidence", "UNKNOWN", "ADVISORY",
                   "no active named ruleset with an inspectable ID; legacy branch protection may apply", url)

    if not pinned:
        pin_url = _endpoint(repo, f"/branches/{quote(branch, safe='')}", api_base)
        record_unavailable_source("immutable default-branch head unavailable", pin_url)
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
    if readme is None:
        record("readme_overview", "UNKNOWN", "ADVISORY", error or "no readable README", url)
        record("readme_local_links", "UNKNOWN", "ADVISORY", error or "no readable README", url)
    else:
        lines = readme.splitlines()
        headings = [line.strip() for line in lines if line.startswith("#")]
        record("readme_overview", "PASS" if any(line.startswith("# ") for line in lines) else "DRIFT",
               "ADVISORY",
               f"readable README: {len(lines)} lines, {len(headings)} headings; human clarity review still required", url)

        relative_paths, self_fragments = _readme_local_targets(readme)
        tree, tree_error, tree_url = _read(
            repo, f"/git/trees/{ref}?recursive=1",
            api_base=api_base, token=token, get_json=get_json,
        )
        entries = tree.get("tree") if isinstance(tree, dict) else None
        if tree_error or not isinstance(entries, list) or tree.get("truncated") is not False:
            record("readme_local_links", "UNKNOWN", "ADVISORY",
                   tree_error or "complete pinned Git tree unavailable; cannot establish missing links",
                   tree_url)
        else:
            tree_paths = {entry.get("path") for entry in entries
                          if isinstance(entry, dict) and isinstance(entry.get("path"), str)}
            missing_paths = sorted(path for path in relative_paths if path not in tree_paths)
            heading_anchors = _readme_heading_anchors(readme)
            missing_fragments = sorted(anchor for anchor in self_fragments if anchor not in heading_anchors)
            problems = [f"missing paths={missing_paths!r}" if missing_paths else "",
                        f"missing README anchors={missing_fragments!r}" if missing_fragments else ""]
            problems = [problem for problem in problems if problem]
            detail = (f"{len(relative_paths)} relative paths and {len(self_fragments)} README anchors inspected; "
                      + ("; ".join(problems) if problems else "all observed targets exist"))
            record("readme_local_links", "DRIFT" if problems else "PASS", "ADVISORY",
                   detail + "; external and cross-file anchors not checked", tree_url)

    root, error, url = _read(
        repo, f"/contents?ref={ref}", api_base=api_base, token=token, get_json=get_json
    )
    if error or not isinstance(root, list):
        record("root_license", "UNKNOWN", "ADVISORY", error or "root listing unavailable", url)
        record("root_contributing", "UNKNOWN", "ADVISORY", error or "root listing unavailable", url)
    else:
        files = {item.get("name", "") for item in root if isinstance(item, dict) and item.get("type") == "file"}
        found = any(name == "LICENSE" or name.startswith("LICENSE.") for name in files)
        record("root_license", "PASS" if found else "DRIFT", "ADVISORY",
               "root LICENSE present" if found else "no root LICENSE file in directory listing", url)
        contributing = "CONTRIBUTING.md" in files
        record("root_contributing", "PASS" if contributing else "DRIFT", "ADVISORY",
               "root CONTRIBUTING.md present" if contributing else
               "no root CONTRIBUTING.md; shared contributor route may be sufficient", url)

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
    def inspect(repo: str) -> dict[str, object]:
        sha, findings = inspect_repository(repo, in_scope=repo in scope, get_json=get_json,
                                           token=token, api_base=api_base)
        return {"repository": repo, "in_scope": repo in scope, "default_head_sha": sha,
                "findings": [asdict(f) for f in findings]}

    # Independent read-only repository requests run concurrently. map() retains
    # the canonical README order in the report despite network completion order.
    with ThreadPoolExecutor(max_workers=max(1, min(6, len(repos)))) as pool:
        items = list(pool.map(inspect, repos))
    return {"as_of_utc": as_of or datetime.now(timezone.utc).isoformat(),
            "system_in_focus": f"opensiro/vsm-oss-organization: current {len(scope)}-repository boundary",
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
