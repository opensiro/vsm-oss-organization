#!/usr/bin/env python3
"""Non-admitting bridge from a material S3* FINDING into bounded S3 candidates.

No audit record alone confers S3 authority. The receiving S3 agent must still
prove a present whole-system choice and actual S1 admission; unverified audit
source or ordinary local finding cannot enter D1-A autonomous decisions.
"""
from __future__ import annotations

import re

URL = re.compile(r"https://github\.com/opensiro/[A-Za-z0-9_.-]+/(?:issues|pull|commit|blob)/[^\s<>]+$")
S1 = re.compile(r"https://github\.com/opensiro/(vsm-harness-index|vsm-harness-skills|awesome-vsm-harness)/issues/[1-9][0-9]*$")

class AuditBridgeError(ValueError):
    pass


def as_candidate(audit: dict, *, audit_source_verified: bool) -> dict:
    if type(audit) is not dict or audit.get("outcome") != "FINDING":
        raise AuditBridgeError("Only material S3* FINDING can enter S3 candidate intake")
    if audit_source_verified is not True:
        raise AuditBridgeError("Complementary audit outcome/source ownership not verified")
    target = audit.get("return_target")
    if not isinstance(target, str) or not S1.fullmatch(target):
        raise AuditBridgeError("Finding does not name an owning S1 work item")
    refs = audit.get("complementary_evidence_refs")
    if type(refs) is not list or not refs or any(
        not isinstance(u, str) or not URL.fullmatch(u) for u in refs
    ):
        raise AuditBridgeError("Complementary first-party evidence refs missing")
    audit_ref = audit.get("audit_receipt_ref")
    if not isinstance(audit_ref, str) or not URL.fullmatch(audit_ref):
        raise AuditBridgeError("No separately published S3* audit receipt")
    if audit.get("material_whole_system_relevance") is not True:
        raise AuditBridgeError("Ordinary local or unproved consequence remains S1")
    if audit.get("commitment_id") not in (
        "selected-methodology-continuity", "canonical-publication-continuity"
    ):
        raise AuditBridgeError("Audit finding not in D1-A standing commitment scope")
    return {
        "status": "UNADMITTED_S3_CANDIDATE_FROM_S3STAR",
        "trigger": "s3star_finding",
        "audit_ref": audit_ref,
        "return_target": target,
        "commitment_id": audit["commitment_id"],
        "complementary_evidence_refs": refs,
        "selected_class": None,
        "S1_effect_refs": [],
        "reason": "Must independently prove current nonlocal S3 right, active grant and actual S1 admission before any agent decision."
    }
