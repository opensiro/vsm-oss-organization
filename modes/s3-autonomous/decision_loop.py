#!/usr/bin/env python3
"""First-party D1-A decision/return orchestration.

A model-backed agent adapter *owns* the choice; these gates merely constrain
and transport it. No default model, authority provider, S1 admission provider
or S1 transport is silently trusted. The shipped inactive D1-A grant blocks
all decision callbacks before their invocation.
"""
from __future__ import annotations

from datetime import datetime, timezone
import importlib.util
from pathlib import Path
import re
from typing import Callable

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "s3_d1a_grant_gate", ROOT / "scripts" / "check_s3_d1a_gate.py"
)
assert SPEC is not None and SPEC.loader is not None
_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(_gate)

S1_ISSUE = re.compile(
    r"https://github\.com/opensiro/(?:vsm-harness-index|vsm-harness-skills|awesome-vsm-harness)/issues/[1-9][0-9]*$"
)
SOURCE = re.compile(
    r"https://github\.com/opensiro/[A-Za-z0-9_.-]+/(?:issues|pull|commit|blob|tree)/[^\s<>]+$"
)
ALLOWED = frozenset({"CONTINUE", "REQUIRE_REPAIR"})
COMMITMENTS = frozenset({
    "selected-methodology-continuity", "canonical-publication-continuity"
})


class DecisionBlocked(ValueError):
    """Authorization, admission, response, or transport is not demonstrated."""


def require(condition: bool, explanation: str) -> None:
    if not condition:
        raise DecisionBlocked(explanation)


def nonempty(value: object, name: str, limit: int = 1500) -> str:
    require(isinstance(value, str) and 0 < len(value.strip()) <= limit and
            "<" not in value, f"{name}: bounded concrete text required")
    return value.strip()


def admitted_case_shape(case: dict) -> dict:
    """Structural check; not a substitute for verifying real current admission."""
    require(type(case) is dict, "admission: concrete case object required")
    require(case.get("kind") == "nonlocal_current_commitment",
            "admission: local S1/S2/S5 issue must not become S3")
    require(case.get("commitment_id") in COMMITMENTS,
            "admission: not a delegated standing shared commitment")
    ref = nonempty(case.get("return_target"), "return_target")
    require(bool(S1_ISSUE.fullmatch(ref)), "admission: named existing owning-S1 issue required")
    refs = case.get("nonlocal_evidence_refs")
    require(type(refs) is list and len(refs) >= 2 and
            all(isinstance(x, str) and SOURCE.fullmatch(x) for x in refs),
            "admission: multi-source first-party primary evidence required")
    domains = {u.split("/opensiro/", 1)[1].split("/", 1)[0] for u in refs}
    require(len(domains.intersection({"vsm-harness-index", "vsm-harness-skills",
                                      "awesome-vsm-harness"})) >= 2,
            "admission: source refs must cover two distinct S1 domains")
    nonempty(case.get("shared_current_constraint"), "shared_current_constraint")
    nonempty(case.get("why_s1_s2_cannot_decide"), "why_s1_s2_cannot_decide")
    nonempty(case.get("rollback_condition"), "rollback_condition")
    return case


def run_decision(
    *,
    grant: dict,
    runtime_actor_id: str,
    case: dict,
    check_live_authority: Callable[[dict, str], object],
    check_current_admission: Callable[[dict], object],
    agent_decide: Callable[[dict], object],
    return_to_s1: Callable[[dict], object],
    now: datetime | None = None,
) -> dict:
    """Operate only after *separate trusted* authority and S1-admission checks.

    All four adapters are explicit, injected by the first-party host:
      check_live_authority - independent CURRENT GitHub S5 publication/revocation
      check_current_admission - independently verified actual S1 active work
      agent_decide - REAL agent-owned nondeterministic choice, never a fixed rule
      return_to_s1 - authorized write transport to the named actual S1 issue

    Tests may inject fakes but never constitute a live autonomous S3 witness.
    A transport receipt is not an S1 acknowledgement or operational effect.
    """
    try:
        _gate.check(grant, agent_id=runtime_actor_id,
                    now=now or datetime.now(timezone.utc))
    except _gate.GateError as exc:
        raise DecisionBlocked(f"NO_AUTHORITY: {exc}") from exc
    require(all(callable(f) for f in (
        check_live_authority, check_current_admission, agent_decide, return_to_s1
    )), "runtime: complete trusted adapters are required")
    shape = admitted_case_shape(case)

    live = check_live_authority(grant, runtime_actor_id)
    require(type(live) is dict and live.get("authorized") is True and
            live.get("revocation_checked") is True and
            live.get("attested_actor") == runtime_actor_id and
            live.get("owner_comment_url") == grant["owner_attestation_url"] and
            live.get("published_grant_sha") == grant["grant_publication_commit"],
            "NO_AUTHORITY: actual owner/publication/revocation attestation unavailable")

    actual = check_current_admission(shape)
    require(type(actual) is dict and actual.get("admitted") is True and
            actual.get("return_target") == shape["return_target"] and
            actual.get("commitment_id") == shape["commitment_id"] and
            actual.get("nonlocal_right_verified") is True and
            actual.get("s1_s2_s5_falsifiers_checked") is True,
            "NOT_ADMITTED: source URLs alone are not a verified S3 case")

    context = {
        "actor": runtime_actor_id,
        "source_case": shape,
        "allowed_classes": sorted(ALLOWED),
        "authority": "distinct D1-A agent S3, not human G1 or parent S5",
        "no_index_grade_or_s5_policy_power": True,
        "must_choose_own_class": True,
    }
    chosen = agent_decide(context)
    require(type(chosen) is dict and set(chosen) == {
        "class", "instruction", "evidence_refs", "decision_summary"
    }, "decision: agent adapter must return exactly the bounded decision fields")
    label = chosen.get("class")
    require(label in ALLOWED, "decision: class outside active D1-A envelope")
    instruction = nonempty(chosen.get("instruction"), "instruction", limit=900)
    summary = nonempty(chosen.get("decision_summary"), "decision_summary")
    evidence = chosen.get("evidence_refs")
    require(type(evidence) is list and len(evidence) >= 1 and all(
        isinstance(x, str) and x in shape["nonlocal_evidence_refs"] for x in evidence
    ), "decision: must cite frozen case evidence, not an unsupported assertion")
    forbidden = (
        "SET_CONSTRAINT", "SET_RETRY_BUDGET", "STOP", "override grade",
        "regrade", "methodology selection", "disable permission",
        "freeze all", "delegate authority"
    )
    require(not any(bad.lower() in instruction.lower() for bad in forbidden),
            "decision: instruction attempts forbidden S1/S5 change")
    action = {
        "status": "AGENT_DECIDED_AWAITING_S1_ACK",
        "owner_class": "agent",
        "actor_execution_id": runtime_actor_id,
        "grant_owner_receipt": grant["owner_attestation_url"],
        "selected_class": label,
        "instruction": instruction,
        "summary": summary,
        "evidence_refs": evidence,
        "return_target": shape["return_target"],
        "commitment_id": shape["commitment_id"],
        "rollback_condition": shape["rollback_condition"],
        "S1_acknowledgement_ref": None,
        "S1_effect_refs": [],
        "closed": False,
    }
    receipt = return_to_s1(action)
    require(type(receipt) is dict and
            receipt.get("target_issue") == action["return_target"] and
            isinstance(receipt.get("transport_url"), str) and
            re.fullmatch(re.escape(action["return_target"]) + r"#issuecomment-[1-9][0-9]*",
                         receipt["transport_url"]),
            "transport: no verifiable bounded S1 delivery receipt")
    # Receipt proves only sending. No agent-side S1 success/closure claim.
    return {**action,
            "transport_url": receipt["transport_url"],
            "status": "S1_RETURN_SENT_EFFECT_UNVERIFIED",
            "S1_acknowledgement_ref": None,
            "S1_effect_refs": [],
            "closed": False}
