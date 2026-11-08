#!/usr/bin/env python3
"""Capture a read-only, source-pinned snapshot of the bounded OpenSiro OSS scope.

The output is a reproducibility manifest, not a release or an autonomy claim.
No GitHub writes are performed. Publication is a separate operator action.
"""

from __future__ import annotations

import argparse
import base64
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from validate_contract import repo_block, release_path, parse_index_contract

ORG = "opensiro/vsm-oss-organization"
SHA = re.compile(r"[0-9a-f]{40}\Z")
DISCLAIMER = (
    "Checks establish only selected-source/contract consistency and stable observed "
    "branch heads, not an atomic cross-repository transaction, semantic correctness, "
    "VSM autonomy, or a release."
)


class SnapshotError(Exception):
    """Fail-closed error; no verified snapshot should be emitted."""


class GitHub:
    def __init__(self, token: str | None = None):
        self.token = token

    def get(self, path: str) -> dict:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "opensiro-oss-snapshot",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = Request("https://api.github.com" + path, headers=headers)
        try:
            with urlopen(request, timeout=20) as response:
                data = json.load(response)
        except (HTTPError, URLError, TimeoutError, ValueError) as exc:
            raise SnapshotError(f"GitHub read failed for {path}: {exc}") from exc
        if not isinstance(data, dict):
            raise SnapshotError(f"GitHub returned a non-object for {path}")
        return data


def require_sha(value: object, context: str) -> str:
    if not isinstance(value, str) or not SHA.fullmatch(value):
        raise SnapshotError(f"Invalid commit SHA for {context}")
    return value


def head(client: GitHub, repository: str) -> dict:
    name = quote(repository, safe="/")
    branch = client.get(f"/repos/{name}").get("default_branch")
    if not isinstance(branch, str) or not branch:
        raise SnapshotError(f"Missing default branch for {repository}")
    commit = client.get(f"/repos/{name}/commits/{quote(branch, safe='')}")
    return {"repository": repository, "default_branch": branch,
            "sha": require_sha(commit.get("sha"), repository)}


def contents(client: GitHub, repository: str, path: str, sha: str) -> str:
    name = quote(repository, safe="/")
    result = client.get(
        f"/repos/{name}/contents/{quote(path, safe='/')}?ref={sha}"
    )
    if result.get("encoding") != "base64" or not isinstance(result.get("content"), str):
        raise SnapshotError(f"GitHub did not return pinned base64 content: {repository}/{path}")
    try:
        return base64.b64decode(result["content"], validate=False).decode("utf-8")
    except (ValueError, UnicodeError) as exc:
        raise SnapshotError(f"Invalid pinned content: {repository}/{path}") from exc


def json_contents(client: GitHub, repository: str, path: str, sha: str) -> dict:
    try:
        value = json.loads(contents(client, repository, path, sha))
    except ValueError as exc:
        raise SnapshotError(f"Invalid JSON at {repository}/{path}") from exc
    if not isinstance(value, dict):
        raise SnapshotError(f"Expected JSON object at {repository}/{path}")
    return value


def ref_sha(client: GitHub, repository: str, ref: str) -> str:
    result = client.get(f"/repos/{quote(repository, safe='/')}/commits/{quote(ref, safe='')}")
    return require_sha(result.get("sha"), f"{repository}@{ref}")


def selected_source(client: GitHub, name: str, value: object) -> dict:
    if not isinstance(value, dict):
        raise SnapshotError(f"Missing selected {name} contract")
    repository, ref, kind = (value.get(key) for key in ("repository", "ref", "source_kind"))
    if not all(isinstance(item, str) and item for item in (repository, ref, kind)):
        raise SnapshotError(f"Malformed selected {name} source")
    if kind not in {"release", "commit", "branch"}:
        raise SnapshotError(f"Unknown {name} source kind: {kind}")
    sha = ref_sha(client, repository, ref)
    if kind == "commit" and sha != require_sha(ref, f"{name} selected ref"):
        raise SnapshotError(f"Selected {name} commit ref drift")
    return {"repository": repository, "source_kind": kind, "ref": ref, "sha": sha,
            **({"version": value["version"]} if "version" in value else {})}


def read_heads(client: GitHub, names: list[str]) -> list[dict]:
    with ThreadPoolExecutor(max_workers=min(len(names), 6)) as executor:
        return list(executor.map(lambda name: head(client, name), names))


def capture(client: GitHub, now: datetime | None = None) -> dict:
    # Resolve Organization first; the scope and selection must come from that exact SHA.
    organization = head(client, ORG)
    readme = contents(client, ORG, "README.md", organization["sha"])
    parse_errors: list[str] = []
    scope = repo_block(readme, "Current in-scope public repositories:", parse_errors)
    if parse_errors or ORG not in scope:
        raise SnapshotError(f"Cannot establish bounded scope: {parse_errors}")
    names = sorted(scope)
    observed = read_heads(client, names)
    if next(row for row in observed if row["repository"] == ORG) != organization:
        raise SnapshotError("Organization head changed while resolving the scope")

    manifest = json_contents(client, ORG, "UPSTREAM_CONTRACT.json", organization["sha"])
    if set(manifest) != {"profile", "methodology", "index"}:
        raise SnapshotError("Organization upstream selection has an unexpected shape")
    selected = {key: selected_source(client, key, manifest[key])
                for key in ("profile", "methodology", "index")}

    profile, methodology, index = (manifest[key] for key in ("profile", "methodology", "index"))
    for kind, value in (("profile", profile), ("methodology", methodology)):
        if value.get("source_kind") == "release" and value.get("ref") != f"v{value.get('version')}":
            raise SnapshotError(f"Selected {kind} release ref does not match its version")
        version_path = value.get("version_path")
        if not isinstance(version_path, str) or not version_path:
            raise SnapshotError(f"Missing selected {kind} version path")
        actual = contents(client, selected[kind]["repository"], version_path,
                          selected[kind]["sha"]).strip()
        if actual != value.get("version"):
            raise SnapshotError(f"Selected {kind} version differs from pinned source: {actual!r}")

    contract_path = index.get("active_contract_path")
    if not isinstance(contract_path, str) or not contract_path:
        raise SnapshotError("Missing selected Index active-contract path")
    parsing: list[str] = []
    pair = parse_index_contract(contents(client, selected["index"]["repository"],
                                         contract_path, selected["index"]["sha"]), parsing)
    if parsing or pair is None:
        raise SnapshotError(f"Invalid pinned Index active contract: {parsing}")
    index_profile, index_methodology = pair
    if index_methodology != methodology["version"]:
        raise SnapshotError("Index Methodology differs from Organization selection: "
                            f"{index_methodology} != {methodology['version']}")

    impact_path = profile.get("release_impact_path")
    if not isinstance(impact_path, str) or not impact_path:
        raise SnapshotError("Missing selected Profile release-impact path")
    impact = json_contents(client, selected["profile"]["repository"],
                           impact_path, selected["profile"]["sha"])
    if impact.get("profile") != profile["repository"]:
        raise SnapshotError("Profile release-impact repository identity mismatch")
    releases = impact.get("releases")
    if not isinstance(releases, list) or sum(isinstance(r, dict) and r.get("version") == profile["version"] for r in releases) != 1:
        raise SnapshotError("Selected Profile release has no unique impact entry")
    errors: list[str] = []
    transitions = release_path(impact, index_profile, profile["version"], errors)
    if errors or transitions is None:
        raise SnapshotError(f"Unresolved Profile compatibility path: {errors}")
    for item in transitions:
        if item.get("compatibility") != "compatible" or item.get("assessment_impact") != "none":
            raise SnapshotError(f"Profile transition {item.get('version')} requires explicit review")

    # This is a stable observed vector, not a globally atomic GitHub read.
    if observed != read_heads(client, names):
        raise SnapshotError("At least one default-branch head changed during capture; retry")
    for key, value in selected.items():
        if ref_sha(client, value["repository"], value["ref"]) != value["sha"]:
            raise SnapshotError(f"Selected {key} ref moved during capture; retry")
    timestamp = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    return {
        "schema_version": 1,
        "captured_at": timestamp.isoformat(timespec="seconds").replace("+00:00", "Z"),
        "scope_source": {"repository": ORG, "sha": organization["sha"],
                         "path": "README.md"},
        "repositories": observed,
        "selected_sources": selected,
        "index_active_contract": {"profile_version": index_profile,
                                  "methodology_version": index_methodology},
        "checks": {"head_stability": "PASS", "selected_version_refs": "PASS",
                   "index_methodology_selection": "PASS", "profile_compatibility": "PASS"},
        "result": "CHECKED_DETERMINISTIC_CONTRACT",
        "limitations": DISCLAIMER,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        help="save a JSON manifest to a new local file (never overwrites)")
    args = parser.parse_args(argv)
    client = GitHub(os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN"))
    try:
        result = capture(client)
        content = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
        if args.output:
            with args.output.open("x", encoding="utf-8") as file:
                file.write(content)
            print(f"Snapshot saved locally: {args.output}")
        else:
            print(content, end="")
    except (SnapshotError, OSError) as exc:
        print(f"SNAPSHOT BLOCKED: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
