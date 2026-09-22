#!/usr/bin/env python3
"""Check contributor routing for the declared VSM Harness OSS repository scope.

The canonical target set comes from the ``Current in-scope public repositories:``
block in Organization README.md. This live cross-repository check is deliberately
separate from the repository-local deterministic completion oracle in
``validate_contract.py`` because remote default-branch state is temporal.
"""

from __future__ import annotations

import argparse
import base64
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

API_VERSION = "2022-11-28"
DEFAULT_API_BASE = "https://api.github.com"
DEFAULT_ORG = "opensiro"
PROJECT_URL = "https://github.com/orgs/opensiro/projects/1"
SCOPE_MARKER = "Current in-scope public repositories:"
REPO_RE = re.compile(r"`(opensiro/[A-Za-z0-9_.-]+)`")


class RoutingError(RuntimeError):
    """The routing check could not obtain required scope or GitHub evidence."""


@dataclass(frozen=True)
class Repository:
    full_name: str
    default_branch: str


@dataclass(frozen=True)
class CheckResult:
    repository: Repository
    ok: bool
    detail: str


def api_json(url: str, token: str | None = None) -> object:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": API_VERSION,
        "User-Agent": "opensiro-vsm-routing-oracle",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = Request(url, headers=headers)
    try:
        with urlopen(request, timeout=30) as response:  # noqa: S310 - GitHub API by default
            import json

            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise RoutingError(f"GitHub API returned HTTP {exc.code} for {url}") from exc
    except (URLError, UnicodeDecodeError, ValueError) as exc:
        raise RoutingError(f"could not read GitHub API response for {url}: {exc}") from exc


def scope_repositories_from_readme(text: str) -> list[str]:
    pos = text.find(SCOPE_MARKER)
    if pos < 0:
        raise RoutingError(f"Organization README missing scope marker: {SCOPE_MARKER}")

    repositories: list[str] = []
    started = False
    for raw in text[pos + len(SCOPE_MARKER) :].splitlines():
        line = raw.strip()
        if not line and not started:
            continue
        if line.startswith("- "):
            started = True
            match = REPO_RE.search(line)
            if not match:
                raise RoutingError(f"scope bullet does not contain an opensiro repository: {line}")
            repositories.append(match.group(1))
            continue
        if started:
            break

    if not repositories:
        raise RoutingError("Organization README scope block contains no repositories")
    if len(repositories) != len(set(repositories)):
        raise RoutingError("Organization README scope block contains duplicate repositories")
    return repositories


def fetch_repository_metadata(
    full_name: str,
    *,
    token: str | None = None,
    api_base: str = DEFAULT_API_BASE,
    get_json: Callable[[str, str | None], object] = api_json,
) -> Repository:
    owner, name = full_name.split("/", 1)
    url = f"{api_base.rstrip('/')}/repos/{quote(owner)}/{quote(name)}"
    payload = get_json(url, token)
    if not isinstance(payload, dict):
        raise RoutingError(f"repository metadata for {full_name} was not a JSON object")
    if payload.get("private") is not False:
        raise RoutingError(f"in-scope repository {full_name} is not public")
    default_branch = payload.get("default_branch")
    reported_name = payload.get("full_name")
    if reported_name != full_name or not isinstance(default_branch, str):
        raise RoutingError(f"repository metadata mismatch for {full_name}")
    return Repository(full_name, default_branch)


def decode_readme_payload(payload: object) -> str:
    if not isinstance(payload, dict):
        raise RoutingError("README response was not a JSON object")

    content = payload.get("content")
    encoding = payload.get("encoding")
    if not isinstance(content, str):
        raise RoutingError("README response does not contain text content")

    if encoding == "base64":
        try:
            return base64.b64decode(content).decode("utf-8")
        except (ValueError, UnicodeDecodeError) as exc:
            raise RoutingError("README base64 content is not valid UTF-8") from exc
    if encoding in (None, "utf-8"):
        return content

    raise RoutingError(f"unsupported README encoding: {encoding!r}")


def fetch_root_readme(
    repository: Repository,
    *,
    token: str | None = None,
    api_base: str = DEFAULT_API_BASE,
    get_json: Callable[[str, str | None], object] = api_json,
) -> str:
    owner, name = repository.full_name.split("/", 1)
    url = (
        f"{api_base.rstrip('/')}/repos/{quote(owner)}/{quote(name)}/readme"
        f"?ref={quote(repository.default_branch)}"
    )
    return decode_readme_payload(get_json(url, token))


def route_marker_present(full_name: str, readme: str, org: str) -> bool:
    text = readme.casefold()
    organization_repo = f"{org}/vsm-oss-organization".casefold()

    if full_name.casefold() == organization_repo:
        return "contributor_start.md" in text
    return organization_repo in text


def project_marker_present(readme: str) -> bool:
    return PROJECT_URL.casefold() in readme.casefold()


def evaluate_repositories(
    repositories: Iterable[Repository],
    *,
    org: str,
    readme_loader: Callable[[Repository], str],
) -> list[CheckResult]:
    results: list[CheckResult] = []
    for repository in repositories:
        try:
            readme = readme_loader(repository)
        except RoutingError as exc:
            results.append(CheckResult(repository, False, str(exc)))
            continue

        has_route = route_marker_present(repository.full_name, readme, org)
        has_project = project_marker_present(readme)
        if has_route and has_project:
            results.append(
                CheckResult(
                    repository,
                    True,
                    "Organization route and OpenSiro VSM OSS Project are directly discoverable",
                )
            )
            continue

        missing: list[str] = []
        if not has_route:
            missing.append(f"{org}/vsm-oss-organization route")
        if not has_project:
            missing.append("OpenSiro VSM OSS Project")
        results.append(
            CheckResult(
                repository,
                False,
                "root README does not expose " + " and ".join(missing),
            )
        )
    return results


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--org", default=DEFAULT_ORG, help="expected GitHub organization")
    parser.add_argument(
        "--scope-readme",
        default="README.md",
        help="Organization README containing the canonical in-scope repository block",
    )
    parser.add_argument("--api-base", default=DEFAULT_API_BASE, help="GitHub API base URL")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    token = os.environ.get("GITHUB_TOKEN") or None

    try:
        scope_text = Path(args.scope_readme).read_text(encoding="utf-8")
        scoped_names = scope_repositories_from_readme(scope_text)
        wrong_org = [name for name in scoped_names if not name.startswith(f"{args.org}/")]
        if wrong_org:
            raise RoutingError(f"scope contains repositories outside {args.org}: {wrong_org}")
        repositories = [
            fetch_repository_metadata(
                name,
                token=token,
                api_base=args.api_base,
            )
            for name in scoped_names
        ]
    except (OSError, UnicodeDecodeError, RoutingError) as exc:
        print(f"routing conformance ERROR: {exc}", file=sys.stderr)
        return 2

    def load(repository: Repository) -> str:
        return fetch_root_readme(
            repository,
            token=token,
            api_base=args.api_base,
        )

    results = evaluate_repositories(repositories, org=args.org, readme_loader=load)
    passed = sum(result.ok for result in results)

    for result in results:
        status = "PASS" if result.ok else "FAIL"
        print(
            f"{status} {result.repository.full_name}"
            f" @ {result.repository.default_branch}: {result.detail}"
        )

    print(f"routing conformance: {passed}/{len(results)} in-scope repositories passed")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
