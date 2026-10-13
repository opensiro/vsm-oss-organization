#!/usr/bin/env python3
"""Offline structural guard for one S3 current-control transaction.

This checker does NOT establish S3 function, actual GitHub provenance,
legitimate organizational decision authority, or Methodology state C/A.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

STATES = {"REQUESTED", "DECIDED", "APPLIED", "CLOSED", "ESCALATED", "CANCELLED"}
CLASSES = {
    "CONTINUE", "STOP", "REQUIRE_REPAIR", "SET_CONSTRAINT",
    "SET_RETRY_BUDGET", "OTHER_CURRENT_CONTROL",
}
TRIGGERS = {"s3star_finding", "current_exception", "other_current_control_need"}
OWNERS = {"human", "agent", "parent", "distributed", "unknown"}
S1_REPOS = {"vsm-harness-index", "vsm-harness-skills", "awesome-vsm-harness"}
ISSUE_URL = re.compile(
    r"https://github[.]com/opensiro/("
    + "|".join(sorted(S1_REPOS))
    + r")/(issues|pull)/[1-9][0-9]*(?:#issuecomment-[0-9]+)?\Z"
)
GITHUB_EVIDENCE = re.compile(r"https://github[.]com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/(issues|pull|commit|blob|tree|actions)/.+\Z")
REQUIRED = {
    "control_version", "transaction_id", "system_in_focus", "status",
    "trigger", "current_view", "requested_decision", "decision",
    "support_and_enforcement", "return_to_s1", "closure",
}


class InvalidS3Transaction(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise InvalidS3Transaction(message)


def keys(obj: object, expected: set[str], path: str) -> dict:
    require(type(obj) is dict and set(obj) == expected, f"{path}: missing or unknown fields")
    return obj


def real_text(value: object, path: str) -> str:
    require(
        type(value) is str and bool(value.strip()) and
        "<" not in value and ">" not in value and "|" not in value and
        len(value) <= 4096,
        f"{path}: requires one concrete non-placeholder string",
    )
    return value


def optional_text(value: object, path: str) -> None:
    if value is not None:
        real_text(value, path)


def refs(value: object, path: str, *, require_one: bool = False, s1: bool = False) -> None:
    require(type(value) is list and (not require_one or len(value) > 0), f"{path}: missing reference list")
    for i, ref in enumerate(value):
        v = real_text(ref, f"{path}[{i}]")
        matcher = ISSUE_URL if s1 else GITHUB_EVIDENCE
        require(bool(matcher.fullmatch(v)), f"{path}[{i}]: requires an owning GitHub reference")


def texts(value: object, path: str, *, require_one: bool = False) -> None:
    require(type(value) is list and (not require_one or len(value) > 0), f"{path}: missing list")
    for i, v in enumerate(value):
        real_text(v, f"{path}[{i}]")


def empty_return(ret: dict) -> bool:
    return ret["acknowledgement_ref"] is None and ret["application_summary"] is None and ret["effect_refs"] == []


def empty_closure(closure: dict) -> bool:
    return all(closure[k] is None for k in ("final_status", "summary")) and closure["evidence_refs"] == []


def validate(obj: object) -> str:
    t = keys(obj, REQUIRED, "transaction")
    require(t["control_version"] == "1", "control_version: unsupported")
    real_text(t["transaction_id"], "transaction_id")
    real_text(t["system_in_focus"], "system_in_focus")
    state = t["status"]
    require(type(state) is str and state in STATES, "status: invalid")

    trigger = keys(t["trigger"], {"kind", "summary", "evidence_refs"}, "trigger")
    require(trigger["kind"] in TRIGGERS, "trigger.kind: invalid")
    real_text(trigger["summary"], "trigger.summary")
    refs(trigger["evidence_refs"], "trigger.evidence_refs", require_one=True)

    current = keys(t["current_view"], {
        "active_s1_refs", "commitments", "constraints", "resource_or_priority_context",
    }, "current_view")
    refs(current["active_s1_refs"], "current_view.active_s1_refs", require_one=True, s1=True)
    texts(current["commitments"], "current_view.commitments", require_one=True)
    texts(current["constraints"], "current_view.constraints", require_one=True)
    texts(current["resource_or_priority_context"], "current_view.resource_or_priority_context")

    requested = keys(t["requested_decision"], {
        "decision_right", "allowed_classes", "authority_boundary",
    }, "requested_decision")
    real_text(requested["decision_right"], "requested_decision.decision_right")
    real_text(requested["authority_boundary"], "requested_decision.authority_boundary")
    allowed = requested["allowed_classes"]
    require(type(allowed) is list and bool(allowed) and
            all(type(x) is str and x in CLASSES for x in allowed) and
            len(set(allowed)) == len(allowed), "requested_decision.allowed_classes: invalid")

    decision = keys(t["decision"], {
        "owner_class", "owner_ref", "class", "instruction", "evidence_refs",
    }, "decision")
    require(decision["owner_class"] in OWNERS, "decision.owner_class: invalid")
    if state == "REQUESTED":
        # The initial template may carry an as-yet-unverified owner reference.
        optional_text(decision["owner_ref"], "decision.owner_ref")
        require(decision["class"] is None and decision["instruction"] is None and
                decision["evidence_refs"] == [], "REQUESTED: cannot pre-fill owner decision")
    else:
        require(decision["owner_class"] != "unknown", "decision: unknown owner cannot authorize a later state")
        ref = real_text(decision["owner_ref"], "decision.owner_ref")
        require(bool(GITHUB_EVIDENCE.fullmatch(ref)), "decision.owner_ref: required owning source")
        # Terminal aborts may be pre-decision, but must not masquerade as decided.
        if state in {"ESCALATED", "CANCELLED"} and decision["class"] is None:
            require(decision["instruction"] is None and decision["evidence_refs"] == [],
                    "terminal pre-decision: no fabricated decision")
        else:
            require(decision["class"] in allowed, "decision.class: not admitted")
            real_text(decision["instruction"], "decision.instruction")
            refs(decision["evidence_refs"], "decision.evidence_refs", require_one=True)

    support = t["support_and_enforcement"]
    require(type(support) is list, "support_and_enforcement: expected list")
    for i, item in enumerate(support):
        v = keys(item, {"mechanism", "role", "evidence_ref"}, f"support[{i}]")
        real_text(v["mechanism"], f"support[{i}].mechanism")
        real_text(v["role"], f"support[{i}].role")
        ref = real_text(v["evidence_ref"], f"support[{i}].evidence_ref")
        require(bool(GITHUB_EVIDENCE.fullmatch(ref)), f"support[{i}]: evidence must be sourced")

    ret = keys(t["return_to_s1"], {
        "target_work_refs", "acknowledgement_ref", "application_summary", "effect_refs",
    }, "return_to_s1")
    refs(ret["target_work_refs"], "return_to_s1.target_work_refs", require_one=True, s1=True)
    require(set(ret["target_work_refs"]).issubset(set(current["active_s1_refs"])),
            "return_to_s1: target must occur in whole-system current view")
    closed = keys(t["closure"], {"final_status", "summary", "evidence_refs"}, "closure")

    if state in {"REQUESTED", "DECIDED"}:
        require(empty_return(ret) and empty_closure(closed),
                f"{state}: cannot claim S1 effect or closure")
    elif state == "APPLIED":
        applied(ret)
        require(empty_closure(closed), "APPLIED: no premature closure")
    elif state == "CLOSED":
        applied(ret)
        complete(closed, state)
    elif state in {"ESCALATED", "CANCELLED"}:
        complete(closed, state)
        if not empty_return(ret):
            applied(ret)
    return "STRUCTURALLY_VALID_NOT_S3_FUNCTION_WITNESS"


def applied(ret: dict) -> None:
    ref = real_text(ret["acknowledgement_ref"], "return_to_s1.acknowledgement_ref")
    require(bool(GITHUB_EVIDENCE.fullmatch(ref)), "return_to_s1: acknowledgement source required")
    real_text(ret["application_summary"], "return_to_s1.application_summary")
    refs(ret["effect_refs"], "return_to_s1.effect_refs", require_one=True)


def complete(closure: dict, state: str) -> None:
    require(closure["final_status"] == state, "closure.final_status: must equal terminal state")
    real_text(closure["summary"], "closure.summary")
    refs(closure["evidence_refs"], "closure.evidence_refs", require_one=True)


ALLOWED_TRANSITIONS = {
    "REQUESTED": {"DECIDED", "ESCALATED", "CANCELLED"},
    "DECIDED": {"APPLIED", "ESCALATED", "CANCELLED"},
    "APPLIED": {"CLOSED", "ESCALATED", "CANCELLED"},
    "CLOSED": set(), "ESCALATED": set(), "CANCELLED": set(),
}


def validate_transition(previous: object, current: object) -> str:
    """Check adjacent snapshots, not authenticated provenance or actual GitHub events."""
    validate(previous)
    validate(current)
    old, new = previous, current
    require(new["status"] in ALLOWED_TRANSITIONS[old["status"]],
            "transition: skipped stage, terminal rewrite or invalid status step")
    for field in ("control_version", "transaction_id", "system_in_focus",
                  "trigger", "current_view", "requested_decision"):
        require(old[field] == new[field], f"transition: immutable {field} changed")
    require(old["return_to_s1"]["target_work_refs"] == new["return_to_s1"]["target_work_refs"],
            "transition: S1 return target changed")
    if old["status"] != "REQUESTED":
        require(old["decision"] == new["decision"], "transition: already decided instruction changed")
    if old["status"] == "APPLIED":
        require(old["return_to_s1"] == new["return_to_s1"],
                "transition: already applied S1 outcome changed")
    return "STRUCTURAL_TRANSITION_VALID_NOT_AUTHORITY_OR_S3_WITNESS"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="one instantiated transaction JSON")
    parser.add_argument("--previous", type=Path, help="optional previous snapshot for strict transition check")
    args = parser.parse_args(argv)
    try:
        obj = json.loads(args.path.read_text(encoding="utf-8"))
        result = (validate_transition(json.loads(args.previous.read_text(encoding="utf-8")), obj)
                  if args.previous else validate(obj))
    except (InvalidS3Transaction, json.JSONDecodeError, OSError) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
