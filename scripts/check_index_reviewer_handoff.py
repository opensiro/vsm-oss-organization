#!/usr/bin/env python3
"""Conservative, offline structural check for a prospective Index review handoff.

Not an independence, semantic, GitHub permission or PR approval oracle.
"""
from __future__ import annotations
import datetime as dt
import json
import re
import sys
from pathlib import Path

HEX40 = re.compile(r"^[0-9a-f]{40}$")
FUNCTIONS = {"S1", "S2", "S3", "S3*", "S4", "S5"}
PHASES = {"REQUESTED", "SOURCE_VERDICT_RECORDED", "RECONCILED"}
URL = re.compile(r"^https://github\.com/[^/ ]+/[^/ ]+/(?:blob|tree|issues|pull|commit)/[^ ]+$")
CONTAMINATING = ("/pull/", "/assessments/", "proposed_vector", "author_rationale", "preferred_outcome")


def _pinned_upstream_link(url: object, repository: object, sha: object) -> bool:
    """Only a frozen upstream tree/file can count as primary source evidence."""
    if not isinstance(url, str) or not isinstance(repository, str) or not isinstance(sha, str):
        return False
    if not HEX40.fullmatch(sha) or not re.fullmatch(r"[^/ ]+/[^/ ]+", repository):
        return False
    base = re.escape(f"https://github.com/{repository}")
    tree = rf"/tree/{sha}(?:/[^?# ]+)?"
    blob = rf"/blob/{sha}/[^?# ]+"
    lines = r"(?:#L[0-9]+(?:-L[0-9]+)?)?"
    return bool(re.fullmatch(rf"{base}(?:{tree}|{blob}){lines}", url))


def _pinned_contract_ref(url: object, repository: str) -> bool:
    """Allow only exact-commit normative references in the reviewer envelope."""
    if not isinstance(url, str):
        return False
    base = re.escape(f"https://github.com/{repository}")
    tail = r"(?:commit/[0-9a-f]{40}|blob/[0-9a-f]{40}/[^?# ]+|tree/[0-9a-f]{40}(?:/[^?# ]+)?)"
    return bool(re.fullmatch(rf"{base}/{tail}(?:#L[0-9]+(?:-L[0-9]+)?)?", url))


def _allowed_source_first_input(url: object, record: dict) -> bool:
    if _pinned_upstream_link(url, record["source_repository"], record["source_sha"]):
        return True
    return (
        (url == record["profile_ref"] and _pinned_contract_ref(url, "opensiro/vsm-harness-profile"))
        or (url == record["skills_ref"] and _pinned_contract_ref(url, "opensiro/vsm-harness-skills"))
    )

def _date(value: object, where: str, errors: list[str]) -> dt.datetime | None:
    try:
        if not isinstance(value, str):
            raise ValueError("not string")
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("must have timezone")
        return parsed
    except ValueError:
        errors.append(where + ": invalid offset-aware timestamp")
        return None

def _url(value: object) -> bool:
    return isinstance(value, str) and bool(URL.fullmatch(value))

def validate(record: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return ["record: expected object"]
    required = {"version", "phase", "index_issue", "proposal_pr", "reviewed_head",
                "source_repository", "source_sha", "profile_ref", "skills_ref",
                "producer_context", "reviewer_context", "reviewer_input_refs",
                "reviewer_execution_ref", "source_verdict", "comparison"}
    errors.extend("missing " + k for k in sorted(required - record.keys()))
    errors.extend("unexpected " + k for k in sorted(record.keys() - required))
    if errors:
        return errors
    if record["version"] != 1 or not isinstance(record["phase"], str) or record["phase"] not in PHASES:
        errors.append("invalid version or phase")
    for key in ("source_sha", "reviewed_head"):
        if not isinstance(record[key], str) or not HEX40.fullmatch(record[key]):
            errors.append(key + ": expected exact full SHA")
    for key in ("index_issue", "proposal_pr"):
        if not _url(record[key]):
            errors.append(key + ": expected public GitHub reference")
    for key, repo in (("profile_ref", "opensiro/vsm-harness-profile"),
                      ("skills_ref", "opensiro/vsm-harness-skills")):
        if not _pinned_contract_ref(record[key], repo):
            errors.append(key + ": must pin the correct normative repository to exact commit SHA")
    if "/issues/" not in str(record["index_issue"]) or "/pull/" not in str(record["proposal_pr"]):
        errors.append("Index issue / PR URLs must identify correct resource types")
    if not isinstance(record["source_repository"], str) or not re.fullmatch(r"[^/ ]+/[^/ ]+", record["source_repository"]):
        errors.append("source_repository must be owner/repo")
    # A REQUESTED/UNASSIGNED record is pending, not a reviewer execution.
    # Do not require invented actor or execution-context IDs before admission.
    pending = record["phase"] == "REQUESTED"
    for key in ("producer_context", "reviewer_context"):
        value = record[key]
        if pending and value is None:
            continue
        if not isinstance(value, str) or len(value.strip()) < 3:
            errors.append(key + ": missing actual context identifier")
    if (isinstance(record["producer_context"], str)
            and isinstance(record["reviewer_context"], str)
            and record["producer_context"] == record["reviewer_context"]):
        errors.append("same producer and reviewer context: no independent handoff")
    inputs = record["reviewer_input_refs"]
    if not isinstance(inputs, list) or not inputs:
        errors.append("reviewer_input_refs must contain frozen upstream primary sources")
    else:
        if not any(_pinned_upstream_link(x, record["source_repository"], record["source_sha"]) for x in inputs):
            errors.append("no exact frozen primary upstream source link in reviewer inputs")
        # Merely having one good source URL is NOT enough: one additional
        # author issue or unpinned source contaminates a blind reviewer.
        for url in inputs:
            if not _allowed_source_first_input(url, record):
                errors.append("source-first input includes non-primary or non-pinned material")
                break
    verdict = record["source_verdict"]
    comparison = record["comparison"]
    if record["phase"] == "REQUESTED":
        if verdict is not None or comparison is not None or record["reviewer_execution_ref"] is not None:
            errors.append("REQUESTED must not fabricate execution/verdict/comparison")
        return errors
    if not _url(record["reviewer_execution_ref"]):
        errors.append("source-first verdict needs attributable execution reference")
    if not isinstance(verdict, dict) or set(verdict) != {"recorded_at", "receipt_url", "functions"}:
        errors.append("source_verdict missing required fields")
        return errors
    first_time = _date(verdict["recorded_at"], "source_verdict.recorded_at", errors)
    if not _url(verdict["receipt_url"]):
        errors.append("source_verdict: missing public attributable receipt reference")
    items = verdict["functions"]
    if not isinstance(items, list) or len(items) != 6 or not all(isinstance(x, dict) for x in items):
        errors.append("source_verdict: six function judgments required")
    else:
        labels = [x.get("function") for x in items]
        if set(labels) != FUNCTIONS or len(set(labels)) != 6:
            errors.append("source_verdict: exact S1/S2/S3/S3*/S4/S5 coverage required")
        for item in items:
            if set(item) != {"function", "judgment", "primary_refs", "counterevidence"}:
                errors.append("source_verdict: incomplete per-function evidence map")
                break
            if not isinstance(item["judgment"], str) or not item["judgment"].strip():
                errors.append("empty source-derived judgment")
            if (not isinstance(item["primary_refs"], list) or not item["primary_refs"]
                    or any(not _pinned_upstream_link(u, record["source_repository"], record["source_sha"])
                           for u in item["primary_refs"])):
                errors.append("per-function primary refs must be original exact-SHA upstream tree/file links")
            if not isinstance(item["counterevidence"], str) or not item["counterevidence"].strip():
                errors.append("missing counterevidence/absence/uncertainty check")
    if record["phase"] == "SOURCE_VERDICT_RECORDED":
        if comparison is not None:
            errors.append("source-first phase must not expose proposal comparison")
        return errors
    if not isinstance(comparison, dict) or set(comparison) != {"proposal_revealed_at", "receipt_url", "pr_head", "outcome", "difference_summary"}:
        errors.append("reconciliation missing exact required fields")
        return errors
    reveal = _date(comparison["proposal_revealed_at"], "comparison.proposal_revealed_at", errors)
    if first_time and reveal and first_time >= reveal:
        errors.append("no proven chronological source-first verdict")
    if comparison["pr_head"] != record["reviewed_head"]:
        errors.append("PR head changed: fail closed")
    if comparison["outcome"] not in {"PASS", "FINDING", "INSUFFICIENT"}:
        errors.append("invalid bounded local outcome")
    if not _url(comparison["receipt_url"]) or not isinstance(comparison["difference_summary"], str) or not comparison["difference_summary"].strip():
        errors.append("reconciliation missing attributable evidence/differences")
    return errors

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_index_reviewer_handoff.py RECORD.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("BLOCKED:", exc, file=sys.stderr)
        return 2
    problems = validate(data)
    for problem in problems:
        print("BLOCKED: " + problem, file=sys.stderr)
    if problems:
        return 2
    print("STRUCTURAL PASS ONLY: no independent reviewer or Index admission inferred")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
