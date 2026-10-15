#!/usr/bin/env python3
"""Strict offline preflight for the autonomous S3 D1-A grant.

Never outputs an authority token. Even positive structural output requires
separate live owner/publication/revocation checks and a real S3 case.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys

ALLOWED = {"CONTINUE", "REQUIRE_REPAIR"}
REPOS = {"Index", "Skills", "Awesome"}
COMMITMENTS = {"selected-methodology-continuity", "canonical-publication-continuity"}
OWNER_REF = re.compile(r"https://github\.com/opensiro/vsm-oss-organization/issues/[1-9][0-9]*#issuecomment-[1-9][0-9]*$")
SHA = re.compile(r"[0-9a-f]{40}$")


class GateError(ValueError):
    pass


def check(data: dict, *, agent_id: str, now: datetime | None = None) -> str:
    if not isinstance(data, dict):
        raise GateError("invalid grant object")
    if data.get("status") != "ACTIVE":
        raise GateError("NO_AUTHORITY: D1-A pending separately attributable S5 grant")
    if data.get("grant_version") != "d1a-v1" or data.get("system_in_focus") != "opensiro-bounded-oss":
        raise GateError("grant identity or boundary mismatch")
    if data.get("parent_github_holder") != "xLagerFeuer" or data.get("parent_role") != "S5":
        raise GateError("unknown delegated parent role")
    identity = data.get("recipient_execution_identity")
    if not isinstance(identity, str) or len(identity.strip()) < 12 or identity != agent_id:
        raise GateError("unattested or mismatched agent execution identity")
    if set(data.get("allowed_classes") or []) != ALLOWED:
        raise GateError("unauthorized S3 decision class")
    if set(data.get("allowed_standing_commitments") or []) != COMMITMENTS:
        raise GateError("unauthorized organizational commitment scope")
    if set(data.get("s1_domains") or []) != REPOS:
        raise GateError("scope outside declared S1")
    ref = data.get("owner_attestation_url")
    if not isinstance(ref, str) or not OWNER_REF.fullmatch(ref):
        raise GateError("no canonical S5 owner decision reference")
    merged = data.get("grant_publication_commit")
    if not isinstance(merged, str) or not SHA.fullmatch(merged):
        raise GateError("no pinned public merge commit")
    try:
        start = datetime.fromisoformat(data["effective_from_utc"].replace("Z","+00:00"))
        until = datetime.fromisoformat(data["expires_at_utc"].replace("Z","+00:00"))
    except (KeyError, AttributeError, ValueError) as exc:
        raise GateError("invalid explicit grant term") from exc
    now = now or datetime.now(timezone.utc)
    if any(dt.utcoffset() is None for dt in (start, until, now)):
        raise GateError("timezone-aware grant term required")
    if not (start <= now < until) or not (start < until <= start.replace(year=start.year+1)):
        raise GateError("expired, future or invalid grant term")
    if (until - start).total_seconds() > 30 * 86400:
        raise GateError("D1-A term exceeds 30 days")
    if data.get("requires_live_authority_checks") is not True:
        raise GateError("live authority checks must not be disabled")
    return "STRUCTURAL_READY_LIVE_AUTHORITY_STILL_REQUIRED"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("grant", type=Path)
    parser.add_argument("--agent-id", required=True, help="attested actual runtime identity")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.grant.read_text(encoding="utf-8"))
        print(check(data, agent_id=args.agent_id))
    except (GateError, OSError, ValueError, TypeError) as exc:
        print(f"NO_S3_AGENT_DECISION: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
