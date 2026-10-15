#!/usr/bin/env python3
"""Source-backed, read-only S5 D1-A authorization verification.

GitHub login is insufficient to authenticate the *human* S5 holder: the
separate parent_authorship verifier is REQUIRED and must not be an agent-
asserted boolean. A two-phase publication prevents a self-hashing git grant.
No owner decision is created here. Never silently use the human G1 grant.
"""
from __future__ import annotations
import base64
from datetime import datetime, timezone
import importlib.util
from pathlib import Path
import json
import re
from typing import Callable

SPEC=importlib.util.spec_from_file_location("s3_d1a_checked_grant", Path(__file__).resolve().parents[2] / "scripts" / "check_s3_d1a_gate.py")
assert SPEC and SPEC.loader
_gate=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(_gate)

SOURCE = "opensiro/vsm-oss-organization"
GRANT_PATH = "contracts/s3/autonomous-d1a.json"
OWNER = "xLagerFeuer"
ATTEST = "OPENSIRO_S5_D1A_AUTHORIZATION_V1\n"
REVOKE = "OPENSIRO_S5_D1A_REVOCATION_V1\n"
COMMENT = re.compile(r"https://github\.com/opensiro/vsm-oss-organization/issues/([1-9][0-9]*)#issuecomment-([1-9][0-9]*)$")
SHA = re.compile(r"[0-9a-f]{40}$")

class S5AuthorizationError(ValueError):
    pass

def require(cond, msg):
    if not cond:
        raise S5AuthorizationError(msg)

def decode_json_file(doc):
    require(type(doc) is dict and doc.get("encoding") == "base64" and
            isinstance(doc.get("content"), str), "missing GitHub blob content")
    try:
        out = json.loads(base64.b64decode(doc["content"], validate=False))
    except (ValueError, UnicodeError) as exc:
        raise S5AuthorizationError("invalid GitHub grant JSON") from exc
    require(type(out) is dict, "published grant not an object")
    return out

def parse_utc(value):
    require(isinstance(value, str) and value.endswith("Z"), "grant time not UTC")
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise S5AuthorizationError("invalid grant time") from exc

def owner_envelope(comment, grant):
    require(type(comment) is dict and type(comment.get("user")) is dict and
            comment["user"].get("login") == OWNER,
            "GitHub owner login does not match public S5 declaration")
    body = comment.get("body")
    require(isinstance(body, str) and body.startswith(ATTEST), "no explicit S5 decision envelope")
    try:
        obj = json.loads(body[len(ATTEST):])
    except ValueError as exc:
        raise S5AuthorizationError("malformed public S5 authorization") from exc
    require(type(obj) is dict and set(obj) == {
        "decision", "recipient_execution_identity", "allowed_classes",
        "allowed_standing_commitments", "effective_from_utc",
        "expires_at_utc", "grant_publication_commit"},
        "wrong public S5 decision fields")
    require(obj["decision"] == "AUTHORIZE_D1A" and
            obj["recipient_execution_identity"] == grant["recipient_execution_identity"] and
            set(obj["allowed_classes"]) == set(grant["allowed_classes"]) and
            set(obj["allowed_standing_commitments"]) == set(grant["allowed_standing_commitments"]) and
            obj["effective_from_utc"] == grant["effective_from_utc"] and
            obj["expires_at_utc"] == grant["expires_at_utc"] and
            obj["grant_publication_commit"] == grant["grant_publication_commit"],
            "S5 owner decision does not match published active grant")
    return obj

def verify_active_grant(grant: dict, actor_id: str, github_get: Callable[[str], object],
                        parent_authorship: Callable[[dict], bool] | None = None,
                        now: datetime | None = None) -> dict:
    """Resolve current public source and revocations, NOT just a local JSON blob.

    parent_authorship must be a trusted, separately established check of an
    owner-initiated statement. Github tools may post using the user's account,
    so a matching login or comment alone cannot satisfy this requirement.
    """
    require(type(grant) is dict and grant.get("status") == "ACTIVE",
            "D1-A is not active")
    try:
        _gate.check(grant,agent_id=actor_id,now=now or datetime.now(timezone.utc))
    except _gate.GateError as exc:
        raise S5AuthorizationError("Invalid bounded D1-A grant: " + str(exc)) from exc
    require(type(actor_id) is str and actor_id == grant.get("recipient_execution_identity") and len(actor_id) >= 12,
            "wrong active agent runtime")
    ref = grant.get("owner_attestation_url")
    m = COMMENT.fullmatch(ref) if isinstance(ref, str) else None
    require(m is not None and m.group(1) == "5", "owner attestation must link M3 #5")
    base_sha = grant.get("grant_publication_commit")
    require(isinstance(base_sha, str) and SHA.fullmatch(base_sha), "missing frozen grant source commit")
    require(callable(github_get), "authenticated GitHub source reader required")
    branch = github_get("/repos/" + SOURCE + "/branches/main")
    require(type(branch) is dict and type(branch.get("commit")) is dict,
            "current Organization main unavailable")
    head = branch["commit"].get("sha")
    require(isinstance(head, str) and SHA.fullmatch(head), "invalid current main ref")
    compare = github_get("/repos/" + SOURCE + "/compare/" + base_sha + "..." + head)
    require(type(compare) is dict and compare.get("status") in ("ahead", "identical"),
            "frozen grant source is not ancestor of live main")
    def file_at(ref):
        return decode_json_file(github_get(
            "/repos/" + SOURCE + "/contents/" + GRANT_PATH + "?ref=" + ref))
    current = file_at(head)
    require(current == grant, "supplied grant is not current Organization main")
    published = file_at(base_sha)
    # First snapshot cannot cite a later owner comment or its own commit SHA.
    # A distinct later owner statement cites that snapshot; only the second
    # grant commit fills BOTH references without changing the delegated scope.
    require(published.get("status") == "ACTIVE" and
            published.get("owner_attestation_url") is None and
            published.get("grant_publication_commit") is None and
            {k:v for k,v in current.items()
             if k not in ("owner_attestation_url", "grant_publication_commit")} ==
            {k:v for k,v in published.items()
             if k not in ("owner_attestation_url", "grant_publication_commit")},
            "referenced inert grant snapshot does not match active grant")
    comment = github_get("/repos/" + SOURCE + "/issues/comments/" + m.group(2))
    require(type(comment) is dict and comment.get("html_url") == ref,
            "owner attestation comment mismatch")
    owner_envelope(comment, grant)
    require(parse_utc(comment.get("created_at")) <= parse_utc(grant["effective_from_utc"]),
            "owner approval is later than purported authorization start")
    if not callable(parent_authorship) or parent_authorship(comment) is not True:
        raise S5AuthorizationError("GitHub account attribution is not independently authenticated S5 authorship")
    issue = github_get("/repos/" + SOURCE + "/issues/5")
    require(type(issue) is dict and issue.get("number") == 5, "revocation source unavailable")
    # Read ALL current comments, fail closed on truncation. An owner-authored
    # revocation marker invalidates the grant even while local JSON says ACTIVE.
    for page in range(1, 31):
        comments = github_get("/repos/" + SOURCE + "/issues/5/comments?per_page=100&page=" + str(page))
        require(type(comments) is list and len(comments) <= 100,
                "revocation scan failed or paginated incompletely")
        for entry in comments:
            require(type(entry) is dict and type(entry.get("user")) is dict,
                    "malformed revocation source")
            if entry["user"].get("login") != OWNER:
                continue
            body = entry.get("body")
            if not isinstance(body, str) or not body.startswith(REVOKE):
                continue
            try:
                payload = json.loads(body[len(REVOKE):])
            except ValueError as exc:
                raise S5AuthorizationError("ambiguous owner revocation entry") from exc
            require(type(payload) is dict and
                    set(payload) == {"owner_attestation_url"}, "malformed S5 revocation")
            require(payload["owner_attestation_url"] != ref,
                    "D1-A S5 owner revoked this grant")
        if len(comments) < 100:
            break
    else:
        raise S5AuthorizationError("revocation source too large to verify exhaustively")
    moment = now or datetime.now(timezone.utc)
    require(parse_utc(grant["effective_from_utc"]) <= moment <
            parse_utc(grant["expires_at_utc"]), "D1-A term expired or not yet effective")
    return {"authorized":True,"revocation_checked":True,
            "attested_actor":actor_id, "owner_comment_url":ref,
            "published_grant_sha":base_sha,
            "current_main_sha":head,
            "identity_assurance":"independent_parent_authorship_callback"}
