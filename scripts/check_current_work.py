#!/usr/bin/env python3
"""Validate the Git-native current-work scheduler and its live issue references."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from check_public_routing import RoutingError, scope_repositories_from_readme

API_VERSION = "2022-11-28"
DEFAULT_API_BASE = "https://api.github.com"
SECTIONS = ("NOW", "NEXT", "BLOCKED")
ISSUE_RE = re.compile(
    r"^- https://github\.com/(opensiro/[A-Za-z0-9_.-]+)/issues/([1-9][0-9]*)$"
)


@dataclass(frozen=True)
class IssueRef:
    repository: str
    number: int

    @property
    def url(self) -> str:
        return f"https://github.com/{self.repository}/issues/{self.number}"


def api_json(url: str, token: str | None = None) -> object:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": API_VERSION,
        "User-Agent": "opensiro-vsm-current-work-oracle",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    try:
        with urlopen(request, timeout=30) as response:  # noqa: S310 - GitHub API by default
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise RoutingError(f"GitHub API returned HTTP {exc.code} for {url}") from exc
    except (URLError, UnicodeDecodeError, ValueError) as exc:
        raise RoutingError(f"could not read GitHub API response for {url}: {exc}") from exc


def parse_current_work(text: str) -> dict[str, list[IssueRef]]:
    if re.search(r"^## (WATCH|LATER)\s*$", text, re.MULTILINE):
        raise RoutingError("TODO.md must not contain WATCH or LATER scheduler sections")

    heading_matches = list(re.finditer(r"^## ([A-Z][A-Z ]*)\s*$", text, re.MULTILINE))
    headings = [match.group(1) for match in heading_matches]
    if headings != list(SECTIONS):
        raise RoutingError(
            f"TODO.md must contain exactly the scheduler headings {SECTIONS}; found {headings}"
        )

    result: dict[str, list[IssueRef]] = {section: [] for section in SECTIONS}
    seen: set[IssueRef] = set()

    for index, match in enumerate(heading_matches):
        section = match.group(1)
        end = heading_matches[index + 1].start() if index + 1 < len(heading_matches) else len(text)
        body = text[match.end() : end]
        for raw in body.splitlines():
            line = raw.strip()
            if not line:
                continue
            issue_match = ISSUE_RE.fullmatch(line)
            if not issue_match:
                raise RoutingError(
                    f"{section}: scheduler entries must be bare in-scope GitHub issue URLs: {line!r}"
                )
            ref = IssueRef(issue_match.group(1), int(issue_match.group(2)))
            if ref in seen:
                raise RoutingError(f"duplicate scheduler issue: {ref.url}")
            seen.add(ref)
            result[section].append(ref)

    return result


def validate_live_issue(
    ref: IssueRef,
    *,
    token: str | None = None,
    api_base: str = DEFAULT_API_BASE,
    get_json: Callable[[str, str | None], object] = api_json,
) -> None:
    owner, repo = ref.repository.split("/", 1)
    url = f"{api_base.rstrip('/')}/repos/{owner}/{repo}/issues/{ref.number}"
    payload = get_json(url, token)
    if not isinstance(payload, dict):
        raise RoutingError(f"issue response was not a JSON object: {ref.url}")
    if "pull_request" in payload:
        raise RoutingError(f"scheduler entry resolves to a pull request, not an issue: {ref.url}")
    if payload.get("state") != "open":
        raise RoutingError(f"scheduler issue is not open: {ref.url}")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Organization repository root")
    parser.add_argument("--api-base", default=DEFAULT_API_BASE, help="GitHub API base URL")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = Path(args.root)
    token = os.environ.get("GITHUB_TOKEN") or None

    try:
        readme = (root / "README.md").read_text(encoding="utf-8")
        todo = (root / "TODO.md").read_text(encoding="utf-8")
        scope = set(scope_repositories_from_readme(readme))
        sections = parse_current_work(todo)
        refs = [ref for section in SECTIONS for ref in sections[section]]
        outside = [ref.url for ref in refs if ref.repository not in scope]
        if outside:
            raise RoutingError(f"scheduler contains issues outside canonical scope: {outside}")
        for ref in refs:
            validate_live_issue(ref, token=token, api_base=args.api_base)
    except (OSError, UnicodeDecodeError, RoutingError) as exc:
        print(f"current-work conformance ERROR: {exc}", file=sys.stderr)
        return 2

    print(
        "current-work conformance PASS: "
        + ", ".join(f"{section}={len(sections[section])}" for section in SECTIONS)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
