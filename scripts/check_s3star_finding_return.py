#!/usr/bin/env python3
"""Offline structural guard for derived S3* -> Index S1 finding-return snapshots.

Checks internal evidence shape only; it cannot independently establish source
correctness, actor separation, GitHub identity/permissions, or a live closure.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

SHA = re.compile(r"^[0-9a-f]{40}$")
REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
INDEX_ISSUE = re.compile(r"^https://github\.com/opensiro/vsm-harness-index/issues/[0-9]+$")
INDEX_PR = re.compile(r"^https://github\.com/opensiro/vsm-harness-index/pull/[0-9]+(?:[#/][A-Za-z0-9_-]+)?$")
INDEX_COMMENT = re.compile(r"^https://github\.com/opensiro/vsm-harness-index/issues/[0-9]+#issuecomment-[0-9]+$")
ORG_REF = re.compile(r"^https://github\.com/opensiro/vsm-oss-organization/(?:issues|pull)/[0-9]+(?:[#/][A-Za-z0-9_-]+)?$")
FIELDS = {
    "id", "wave", "index_batch", "row", "source_repository", "source_sha",
    "audited_function", "scope", "original_audit_ref", "index_owner_issue",
    "routed_ref", "original_outcome", "disposition", "owner_decision",
    "verification",
}
ROOT = {
    "schema_version", "view_kind", "snapshot_date_utc", "authority_issue",
    "organization_main_sha", "index_main_sha", "findings",
}
DECISION = {
    "outcome", "owner_actor", "decided_at_utc", "index_reference",
    "index_main_sha", "reason",
}
VERIFICATION = {
    "effect", "verifier_actor", "verified_at_utc", "verification_ref",
    "index_main_sha", "result_pr_ref",
}
FUNCTIONS = {"S1", "S2", "S3", "S3*", "S4", "S5"}

# The initial four-finding cut is a derived historical anchor, not a new
# source of semantic authority. A digest guards against quietly rewriting it.
FROZEN_BASELINE = (
    Path(__file__).resolve().parents[1]
    / "records/s3star/finding-return/2026-10-11-index-open.json"
)
FROZEN_BASELINE_SHA256 = "4769a04cacecc06d37a979476b010c63150c73e05e63282f8c5b80ff21ae896d"
FROZEN_FIELDS = (
    "id", "wave", "index_batch", "row", "source_repository", "source_sha",
    "audited_function", "scope", "original_audit_ref", "index_owner_issue",
    "routed_ref", "original_outcome",
)


def frozen_findings() -> dict[str, dict]:
    """Load the fixed #200 population only after verifying its original bytes."""
    original = FROZEN_BASELINE.read_bytes()
    if hashlib.sha256(original).hexdigest() != FROZEN_BASELINE_SHA256:
        raise ValueError("historical four-finding baseline digest mismatch")
    rows = json.loads(original)["findings"]
    return {f["id"]: {field: f[field] for field in FROZEN_FIELDS} for f in rows}


def date(value: object) -> dt.date | None:
    try:
        return dt.date.fromisoformat(value) if isinstance(value, str) else None
    except ValueError:
        return None


def sha(value: object) -> bool:
    return isinstance(value, str) and bool(SHA.fullmatch(value))


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def timestamp(value: object) -> dt.datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed if parsed.utcoffset() is not None else None
    except ValueError:
        return None


def validate(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["root must be object"]
    if set(data) != ROOT:
        return ["root fields mismatch"]
    if data["schema_version"] != "s3star-index-finding-return-v1":
        errors.append("schema version mismatch")
    if data["view_kind"] != "DERIVED_READ_ONLY":
        errors.append("must explicitly be derived read-only")
    snapshot_day = date(data["snapshot_date_utc"])
    if snapshot_day is None:
        errors.append("snapshot date invalid")
    if data["authority_issue"] != "https://github.com/opensiro/vsm-oss-organization/issues/200":
        errors.append("wrong authority issue")
    for k in ("organization_main_sha", "index_main_sha"):
        if not sha(data[k]):
            errors.append(k + " must be full SHA")
    findings = data["findings"]
    if not isinstance(findings, list) or not findings:
        return errors + ["nonempty findings required"]
    try:
        frozen = frozen_findings()
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        return errors + ["frozen baseline unavailable or changed: " + str(exc)]
    if len(findings) != len(frozen):
        errors.append("exactly four frozen #200 findings required")
    seen: set[tuple[str, int, int]] = set()
    ids: set[str] = set()
    for pos, f in enumerate(findings):
        at = f"findings[{pos}]"
        if not isinstance(f, dict) or set(f) != FIELDS:
            errors.append(at + ": wrong fields")
            continue
        expected = frozen.get(f["id"]) if isinstance(f["id"], str) else None
        if expected is None:
            errors.append(at + ": finding identity not in frozen #200 population")
        else:
            for field in FROZEN_FIELDS:
                if f[field] != expected[field]:
                    errors.append(at + ": frozen " + field + " altered")
        wave, batch, row = f["wave"], f["index_batch"], f["row"]
        if not isinstance(wave, str) or wave not in {"W001", "W002"} or type(batch) is not int or batch <= 0 or type(row) is not int or row <= 0:
            errors.append(at + ": invalid frozen row identity")
        else:
            key = wave, batch, row
            if key in seen:
                errors.append(at + ": duplicate frozen row")
            seen.add(key)
        if not nonempty(f["id"]) or f["id"] in ids:
            errors.append(at + ": missing/duplicate finding ID")
        else:
            ids.add(f["id"])
        if not isinstance(f["source_repository"], str) or not REPO.fullmatch(f["source_repository"]):
            errors.append(at + ": invalid frozen upstream repository")
        if not sha(f["source_sha"]):
            errors.append(at + ": invalid frozen source SHA")
        if not isinstance(f["audited_function"], str) or f["audited_function"] not in FUNCTIONS or not nonempty(f["scope"]):
            errors.append(at + ": missing audited claim scope")
        if not isinstance(f["original_audit_ref"], str) or not ORG_REF.fullmatch(f["original_audit_ref"]):
            errors.append(at + ": invalid original Organization evidence reference")
        owner = f["index_owner_issue"]
        routed = f["routed_ref"]
        if not isinstance(owner, str) or not INDEX_ISSUE.fullmatch(owner):
            errors.append(at + ": Index owner must be exact owning issue")
        if not isinstance(routed, str) or (routed != owner and not (routed.startswith(str(owner) + "#issuecomment-") and INDEX_COMMENT.fullmatch(routed))):
            errors.append(at + ": routed ref must point to exact owning Index issue/comment")
        if f["original_outcome"] != "FINDING":
            errors.append(at + ": historical audit outcome must stay FINDING")
        disposition, decision, verification = f["disposition"], f["owner_decision"], f["verification"]
        if not isinstance(disposition, str) or disposition not in {"ROUTED_OPEN", "ADJUDICATED", "VERIFIED"}:
            errors.append(at + ": invalid disposition")
            continue
        if disposition == "ROUTED_OPEN":
            if decision is not None or verification is not None:
                errors.append(at + ": routed finding must not invent owner decision / closure")
            continue
        if not isinstance(decision, dict) or set(decision) != DECISION:
            errors.append(at + ": adjudication requires complete Index owner evidence")
            continue
        outcome = decision["outcome"]
        if not isinstance(outcome, str) or outcome not in {"CORRECTION_REQUIRED", "NO_CHANGE_EVIDENCED", "INSUFFICIENT_EVIDENCE"}:
            errors.append(at + ": invalid owner disposition")
        if not nonempty(decision["owner_actor"]) or not nonempty(decision["reason"]):
            errors.append(at + ": owner identity/reason missing")
        decided = timestamp(decision["decided_at_utc"])
        if decided is None:
            errors.append(at + ": owner decision timestamp invalid")
        elif snapshot_day is not None and decided.astimezone(dt.timezone.utc).date() > snapshot_day:
            errors.append(at + ": owner decision occurs after dated snapshot")
        if not sha(decision["index_main_sha"]):
            errors.append(at + ": owner decision Index main SHA absent")
        decision_ref = decision["index_reference"]
        if not isinstance(decision_ref, str) or not (INDEX_COMMENT.fullmatch(decision_ref) and decision_ref.startswith(str(owner) + "#issuecomment-") or INDEX_PR.fullmatch(decision_ref)):
            errors.append(at + ": decision must cite owning Index comment or PR")
        if disposition == "ADJUDICATED":
            if verification is not None:
                errors.append(at + ": adjudication cannot claim verification without VERIFIED status")
            continue
        if outcome == "INSUFFICIENT_EVIDENCE":
            errors.append(at + ": insufficient evidence cannot be VERIFIED")
        if not isinstance(verification, dict) or set(verification) != VERIFICATION:
            errors.append(at + ": VERIFIED requires independent verification receipt")
            continue
        if not nonempty(verification["verifier_actor"]) or verification["verifier_actor"] == decision["owner_actor"]:
            errors.append(at + ": verifier must be separately attributed from owner")
        verified = timestamp(verification["verified_at_utc"])
        if verified is None or (decided is not None and verified <= decided):
            errors.append(at + ": verification must be dated after owner decision")
        if verified is not None and snapshot_day is not None and verified.astimezone(dt.timezone.utc).date() > snapshot_day:
            errors.append(at + ": verification occurs after dated snapshot")
        if not sha(verification["index_main_sha"]):
            errors.append(at + ": verified Index main SHA absent")
        if not isinstance(verification["verification_ref"], str) or not ORG_REF.fullmatch(verification["verification_ref"]):
            errors.append(at + ": independent verification must be linked to Organization receipt")
        if outcome == "CORRECTION_REQUIRED":
            if verification["effect"] != "CORRECTION_MERGED" or not isinstance(verification["result_pr_ref"], str) or not INDEX_PR.fullmatch(verification["result_pr_ref"]):
                errors.append(at + ": accepted correction requires actual Index PR and merged-result witness")
        elif outcome == "NO_CHANGE_EVIDENCED":
            if verification["effect"] != "JUSTIFIED_NO_CHANGE" or verification["result_pr_ref"] is not None:
                errors.append(at + ": reasoned no-change must not claim merged correction")
    if ids != set(frozen):
        errors.append("missing or extra frozen finding IDs")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_s3star_finding_return.py SNAPSHOT.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("BLOCKED: " + str(exc), file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        for error in errors:
            print("BLOCKED: " + error, file=sys.stderr)
        return 2
    print("STRUCTURAL PASS ONLY: inspect Index owner and independent verification sources live")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())