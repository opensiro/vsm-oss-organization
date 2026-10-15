#!/usr/bin/env python3
"""Read-only source inventory of the three in-scope OpenSiro S1 domains.

This is an S3 *support* view, not S3 authority, active S1 admission, an S3
current-control decision, a transaction, or evidence for a VSM grade.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
from typing import Callable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

REPOSITORIES = (
    "opensiro/vsm-harness-index",
    "opensiro/vsm-harness-skills",
    "opensiro/awesome-vsm-harness",
)
API = "https://api.github.com"
ISSUE_LIMIT = 100
MAX_PAGES = 20
BOUNDARY = "CANDIDATES_ONLY_NOT_ACTIVE_S1_OR_S3_EVIDENCE"


class CurrentViewError(RuntimeError):
    pass


def github_get(path: str) -> object:
    if not path.startswith("/repos/opensiro/") or ".." in path:
        raise CurrentViewError("refusing unsupported GitHub API route")
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "opensiro-s3-current-view-readonly",
    }
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    request = Request(API + path, headers=headers)
    try:
        with urlopen(request, timeout=30) as response:  # noqa: S310 - fixed GitHub API
            return json.load(response)
    except (HTTPError, URLError, ValueError, TimeoutError) as exc:
        raise CurrentViewError(f"source read failed: {path}: {type(exc).__name__}") from exc


def required_text(obj: dict, key: str) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        raise CurrentViewError(f"missing source value: {key}")
    return value


def open_items(fetch: Callable[[str], object], repo: str, kind: str) -> list[dict]:
    """Read all pages; do not silently turn a partial inventory into a whole view."""
    result: list[dict] = []
    for page in range(1, MAX_PAGES + 1):
        path = (f"/repos/{repo}/{kind}?state=open&per_page={ISSUE_LIMIT}"
                f"&sort=updated&direction=desc&page={page}")
        items = fetch(path)
        if not isinstance(items, list) or any(not isinstance(item, dict) for item in items):
            raise CurrentViewError(f"{repo}: unavailable or malformed {kind} page {page}")
        result.extend(items)
        if len(items) < ISSUE_LIMIT:
            return result
    raise CurrentViewError(f"{repo}: exceeded pagination limit for {kind}")


def collect(fetch: Callable[[str], object] = github_get, *, observed_at: str | None = None) -> dict:
    observed_at = observed_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
    output: dict = {
        "observed_at_utc": observed_at,
        "system_in_focus": "OpenSiro VSM Harness OSS: Index/Skills/Awesome S1",
        "classification": BOUNDARY,
        "s3_admission": "NOT_ASSESSED",
        "warning": "Open issues/PRs are candidate sources, never proof of executing S1 work, shared constraint, G1 authority or S3 function.",
        "domains": [],
    }
    for repo in REPOSITORIES:
        details = fetch(f"/repos/{repo}")
        if not isinstance(details, dict):
            raise CurrentViewError(f"{repo}: repo metadata unavailable")
        branch = required_text(details, "default_branch")
        # GitHub names are path components. Reject unexpected characters.
        if not branch.replace("-", "").replace("_", "").replace(".", "").isalnum():
            raise CurrentViewError(f"{repo}: unexpected default-branch ref")
        b = fetch(f"/repos/{repo}/branches/{branch}")
        if not isinstance(b, dict) or not isinstance(b.get("commit"), dict):
            raise CurrentViewError(f"{repo}: branch response unavailable")
        sha = required_text(b["commit"], "sha")
        if len(sha) != 40 or any(ch not in "0123456789abcdef" for ch in sha.lower()):
            raise CurrentViewError(f"{repo}: invalid default-branch commit")
        issues = open_items(fetch, repo, "issues")
        pulls = open_items(fetch, repo, "pulls")
        open_issues = []
        for issue in issues:
            if not isinstance(issue, dict):
                raise CurrentViewError(f"{repo}: malformed issue")
            if issue.get("pull_request"):
                continue
            open_issues.append({
                "number": issue["number"],
                "title": required_text(issue, "title"),
                "url": required_text(issue, "html_url"),
                "updated_at": required_text(issue, "updated_at"),
                "work_admitted": "UNKNOWN",
            })
        open_pulls = []
        for pr in pulls:
            if not isinstance(pr, dict) or not isinstance(pr.get("head"), dict):
                raise CurrentViewError(f"{repo}: malformed pull request")
            open_pulls.append({
                "number": pr["number"],
                "title": required_text(pr, "title"),
                "url": required_text(pr, "html_url"),
                "head_sha": required_text(pr["head"], "sha"),
                "draft": pr.get("draft") is True,
                "work_admitted": "UNKNOWN",
            })
        output["domains"].append({
            "repo": repo,
            "source_main": f"https://github.com/{repo}/tree/{sha}",
            "main_sha": sha,
            "open_issues": open_issues,
            "open_pulls": open_pulls,
        })
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="local JSON path; stdout otherwise")
    args = parser.parse_args(argv)
    try:
        report = collect()
        contents = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
        if args.output:
            args.output.write_text(contents, encoding="utf-8")
        else:
            print(contents, end="")
    except (CurrentViewError, OSError, KeyError, TypeError) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
