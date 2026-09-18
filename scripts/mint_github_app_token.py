#!/usr/bin/env python3
"""Mint a narrowed short-lived GitHub App installation token without printing it.

Requires only Python stdlib plus the system `openssl` binary. The App private
key remains local. The installation token is written to an owner-only file.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import stat
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

API = "https://api.github.com"
API_VERSION = "2026-03-10"
ALLOWED_LEVELS = {"read", "write"}


class GitHubError(RuntimeError):
    pass


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def ensure_private_key_permissions(path: Path, allow_insecure: bool) -> None:
    mode = stat.S_IMODE(path.stat().st_mode)
    if os.name == "posix" and mode & (stat.S_IRWXG | stat.S_IRWXO) and not allow_insecure:
        raise ValueError(
            f"private key {path} has group/world permissions {oct(mode)}; use chmod 600 or --allow-insecure-key-permissions"
        )


def sign_rs256(signing_input: bytes, private_key: Path) -> bytes:
    try:
        result = subprocess.run(
            ["openssl", "dgst", "-sha256", "-sign", str(private_key)],
            input=signing_input,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("openssl executable not found") from exc
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
    return result.stdout


def build_app_jwt(app_id: int, private_key: Path, now: int | None = None) -> str:
    current = int(time.time()) if now is None else now
    header = {"alg": "RS256", "typ": "JWT"}
    payload = {"iat": current - 60, "exp": current + 540, "iss": str(app_id)}
    signing_input = f"{b64url(canonical_json(header))}.{b64url(canonical_json(payload))}".encode("ascii")
    signature = sign_rs256(signing_input, private_key)
    return f"{signing_input.decode('ascii')}.{b64url(signature)}"


def request_json(method: str, url: str, bearer: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    body = None
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {bearer}",
        "X-GitHub-Api-Version": API_VERSION,
        "User-Agent": "opensiro-vsm-executor-provenance",
    }
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read()
    except urllib.error.HTTPError as exc:
        error = exc.read().decode("utf-8", errors="replace")
        raise GitHubError(f"GitHub API returned HTTP {exc.code}: {error}") from exc
    except urllib.error.URLError as exc:
        raise GitHubError(f"GitHub API request failed: {exc}") from exc
    data = json.loads(raw.decode("utf-8")) if raw else {}
    if not isinstance(data, dict):
        raise GitHubError("unexpected non-object GitHub API response")
    return data


def parse_permission(spec: str) -> tuple[str, str]:
    if "=" not in spec:
        raise ValueError("permission must use name=read|write syntax")
    name, level = spec.split("=", 1)
    name = name.strip()
    level = level.strip()
    if not name or level not in ALLOWED_LEVELS:
        raise ValueError("permission must use non-empty-name=read|write syntax")
    return name, level


def resolve_installation_id(jwt: str, repository: str) -> int:
    owner, repo = repository.split("/", 1)
    result = request_json("GET", f"{API}/repos/{owner}/{repo}/installation", jwt)
    installation_id = result.get("id")
    if not isinstance(installation_id, int) or installation_id <= 0:
        raise GitHubError("repository installation response did not contain a valid installation id")
    return installation_id


def write_secret(path: Path, value: str) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    fd = os.open(path, flags, 0o600)
    try:
        os.write(fd, value.encode("utf-8"))
        os.write(fd, b"\n")
    finally:
        os.close(fd)
    if os.name == "posix":
        os.chmod(path, 0o600)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app-id", type=int, required=True)
    parser.add_argument("--private-key", type=Path, required=True)
    parser.add_argument("--installation-id", type=int)
    parser.add_argument("--repository", action="append", required=True, help="owner/repository; repeatable")
    parser.add_argument("--permission", action="append", default=[], help="name=read|write; repeatable")
    parser.add_argument("--token-output", type=Path, required=True)
    parser.add_argument("--allow-insecure-key-permissions", action="store_true")
    args = parser.parse_args()

    if args.app_id <= 0:
        parser.error("--app-id must be positive")
    if not args.private_key.is_file():
        parser.error("--private-key must point to an existing PEM file")
    if args.token_output.exists():
        parser.error("--token-output already exists; refusing to overwrite a secret file")
    if any(repo.count("/") != 1 for repo in args.repository):
        parser.error("every --repository must use owner/repository syntax")

    try:
        ensure_private_key_permissions(args.private_key, args.allow_insecure_key_permissions)
        permissions = dict(parse_permission(item) for item in args.permission)
        jwt = build_app_jwt(args.app_id, args.private_key)
        app = request_json("GET", f"{API}/app", jwt)
        observed_app_id = app.get("id")
        if observed_app_id != args.app_id:
            raise GitHubError(f"authenticated App id mismatch: expected {args.app_id}, got {observed_app_id}")
        slug = app.get("slug")
        if not isinstance(slug, str) or not slug:
            raise GitHubError("authenticated App response did not contain a slug")

        installation_id = args.installation_id or resolve_installation_id(jwt, args.repository[0])
        if installation_id <= 0:
            raise ValueError("installation id must be positive")

        body: dict[str, Any] = {"repositories": [repo.split("/", 1)[1] for repo in args.repository]}
        if permissions:
            body["permissions"] = permissions

        token_response = request_json(
            "POST",
            f"{API}/app/installations/{installation_id}/access_tokens",
            jwt,
            payload=body,
        )
        token = token_response.get("token")
        if not isinstance(token, str) or not token:
            raise GitHubError("installation token response did not contain a token")
        write_secret(args.token_output, token)

        repositories = []
        for item in token_response.get("repositories", []):
            if isinstance(item, dict) and isinstance(item.get("full_name"), str):
                repositories.append(item["full_name"])

        metadata = {
            "app_id": observed_app_id,
            "app_slug": slug,
            "bot_login": f"{slug}[bot]",
            "installation_id": installation_id,
            "expires_at": token_response.get("expires_at"),
            "permissions": token_response.get("permissions", permissions),
            "repositories": repositories or args.repository,
            "token_output": str(args.token_output),
            "token_printed": False,
        }
        print(json.dumps(metadata, indent=2, sort_keys=True))
        return 0
    except (ValueError, RuntimeError, GitHubError, OSError) as exc:
        print(f"GitHub App token mint FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
