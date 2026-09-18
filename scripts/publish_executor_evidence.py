#!/usr/bin/env python3
"""Publish one immutable executor-provenance evidence object through a GitHub App token.

The script is deliberately create-only: an existing evidence path is never
updated. The caller supplies a short-lived GitHub App installation token in an
environment variable and an expected App bot login. After publication the
resulting commit is fetched back and the observed GitHub actor is checked.

This helper is proof transport, not a VSM organizational owner.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

API = "https://api.github.com"
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
RUN_ID_RE = re.compile(r"^[A-Za-z0-9._:-]+$")


class GitHubError(RuntimeError):
    pass


def request_json(
    method: str,
    url: str,
    token: str,
    *,
    payload: dict[str, Any] | None = None,
    allow_404: bool = False,
) -> dict[str, Any] | list[Any] | None:
    data = None
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "opensiro-vsm-executor-provenance",
    }
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            raw = response.read()
    except urllib.error.HTTPError as exc:
        if allow_404 and exc.code == 404:
            return None
        body = exc.read().decode("utf-8", errors="replace")
        raise GitHubError(f"GitHub API {method} {url} failed: HTTP {exc.code}: {body}") from exc
    except urllib.error.URLError as exc:
        raise GitHubError(f"GitHub API {method} {url} failed: {exc}") from exc

    if not raw:
        return None
    return json.loads(raw.decode("utf-8"))


def ensure_branch(repo: str, branch: str, base_ref: str, token: str) -> None:
    branch_url = f"{API}/repos/{repo}/git/ref/heads/{urllib.parse.quote(branch, safe='/')}"
    existing = request_json("GET", branch_url, token, allow_404=True)
    if existing is not None:
        return

    base_url = f"{API}/repos/{repo}/git/ref/heads/{urllib.parse.quote(base_ref, safe='/')}"
    base = request_json("GET", base_url, token)
    if not isinstance(base, dict):
        raise GitHubError("could not resolve base ref")
    sha = base.get("object", {}).get("sha")
    if not isinstance(sha, str):
        raise GitHubError("base ref response did not contain commit SHA")

    created = request_json(
        "POST",
        f"{API}/repos/{repo}/git/refs",
        token,
        payload={"ref": f"refs/heads/{branch}", "sha": sha},
    )
    if not isinstance(created, dict):
        raise GitHubError("GitHub did not return the created branch ref")


def ensure_path_is_new(repo: str, path: str, branch: str, token: str) -> None:
    quoted_path = urllib.parse.quote(path, safe="/")
    url = f"{API}/repos/{repo}/contents/{quoted_path}?ref={urllib.parse.quote(branch, safe='')}"
    existing = request_json("GET", url, token, allow_404=True)
    if existing is not None:
        raise GitHubError(
            f"refusing to overwrite existing evidence path {repo}:{path}@{branch}; "
            "executor evidence publication is create-only"
        )


def publish_file(
    repo: str,
    branch: str,
    path: str,
    content: bytes,
    message: str,
    token: str,
) -> tuple[str, str]:
    quoted_path = urllib.parse.quote(path, safe="/")
    result = request_json(
        "PUT",
        f"{API}/repos/{repo}/contents/{quoted_path}",
        token,
        payload={
            "message": message,
            "content": base64.b64encode(content).decode("ascii"),
            "branch": branch,
        },
    )
    if not isinstance(result, dict):
        raise GitHubError("GitHub did not return a content-publication result")
    commit = result.get("commit")
    if not isinstance(commit, dict):
        raise GitHubError("GitHub response did not include commit metadata")
    sha = commit.get("sha")
    html_url = commit.get("html_url")
    if not isinstance(sha, str) or not isinstance(html_url, str):
        raise GitHubError("GitHub response did not include commit SHA/html_url")
    return sha, html_url


def verify_commit_actor(repo: str, sha: str, token: str, expected_bot_login: str) -> dict[str, str | None]:
    result = request_json("GET", f"{API}/repos/{repo}/commits/{sha}", token)
    if not isinstance(result, dict):
        raise GitHubError("could not fetch published commit")

    author = result.get("author")
    committer = result.get("committer")
    author_login = author.get("login") if isinstance(author, dict) else None
    committer_login = committer.get("login") if isinstance(committer, dict) else None

    observed = {item for item in (author_login, committer_login) if isinstance(item, str)}
    if expected_bot_login not in observed:
        raise GitHubError(
            "published commit is not attributed to the expected GitHub App bot identity: "
            f"expected={expected_bot_login!r}, author={author_login!r}, committer={committer_login!r}"
        )

    return {
        "author_login": author_login,
        "committer_login": committer_login,
    }


def expected_path(run_id: str, kind: str, event_seq: int | None) -> str:
    prefix = f"provenance/runs/{run_id}"
    if kind == "anchor":
        return f"{prefix}/anchor.json"
    if kind == "closure":
        return f"{prefix}/closure.json"
    if kind == "witness":
        return f"{prefix}/witness.json"
    if kind == "event":
        if event_seq is None or event_seq <= 0:
            raise ValueError("--event-seq is required and must be positive for kind=event")
        return f"{prefix}/events/{event_seq:04d}.json"
    raise ValueError(f"unsupported kind: {kind}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="evidence repository in owner/name form")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--kind", required=True, choices=("anchor", "event", "closure", "witness"))
    parser.add_argument("--file", required=True, help="local JSON evidence object to publish")
    parser.add_argument("--event-seq", type=int)
    parser.add_argument("--branch", help="evidence branch; defaults to provenance/<run_id>")
    parser.add_argument("--base-ref", default="main")
    parser.add_argument("--expected-bot-login", required=True)
    parser.add_argument(
        "--token-env",
        default="OPENSIRO_EXECUTOR_GITHUB_TOKEN",
        help="environment variable containing short-lived GitHub App installation token",
    )
    args = parser.parse_args()

    if not REPO_RE.fullmatch(args.repo):
        parser.error("--repo must use owner/name syntax")
    if not RUN_ID_RE.fullmatch(args.run_id):
        parser.error("--run-id contains unsupported characters")
    if not args.expected_bot_login.endswith("[bot]"):
        parser.error("--expected-bot-login must be a GitHub App bot login ending in '[bot]'")

    token = os.environ.get(args.token_env)
    if not token:
        parser.error(f"environment variable {args.token_env!r} is not set")

    source = Path(args.file)
    try:
        content = source.read_bytes()
        parsed = json.loads(content.decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        parser.error(f"--file must be readable UTF-8 JSON: {exc}")
    if not isinstance(parsed, dict):
        parser.error("--file JSON root must be an object")

    embedded_run_id = parsed.get("run_id")
    if embedded_run_id is None and isinstance(parsed.get("run"), dict):
        embedded_run_id = parsed["run"].get("run_id")
    if embedded_run_id is not None and embedded_run_id != args.run_id:
        parser.error(
            f"evidence object run_id {embedded_run_id!r} does not match --run-id {args.run_id!r}"
        )

    try:
        path = expected_path(args.run_id, args.kind, args.event_seq)
    except ValueError as exc:
        parser.error(str(exc))

    branch = args.branch or f"provenance/{args.run_id}"

    try:
        ensure_branch(args.repo, branch, args.base_ref, token)
        ensure_path_is_new(args.repo, path, branch, token)
        sha, html_url = publish_file(
            args.repo,
            branch,
            path,
            content,
            f"provenance({args.run_id}): publish {args.kind}",
            token,
        )
        actors = verify_commit_actor(args.repo, sha, token, args.expected_bot_login)
    except GitHubError as exc:
        print(f"Executor evidence publication FAILED: {exc}", file=sys.stderr)
        return 1

    result = {
        "repository": args.repo,
        "branch": branch,
        "path": path,
        "commit_sha": sha,
        "commit_url": html_url,
        "expected_bot_login": args.expected_bot_login,
        **actors,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
