#!/usr/bin/env python3
"""First-party S3 -> S1 feedback reconciliation.

A transport comment does not mean S1 acknowledged, applied, or effectuated
the decision. Only *independently verified S1 owner* evidence can close it.
This module cannot itself write to S1, forge receipts, or infer independent
authorship from the presence of a GitHub URL.
"""
from __future__ import annotations

import re
from typing import Callable

REPO_ISSUE = re.compile(r"https://github\.com/opensiro/(vsm-harness-index|vsm-harness-skills|awesome-vsm-harness)/issues/[1-9][0-9]*$")
EFFECT = re.compile(r"https://github\.com/opensiro/(vsm-harness-index|vsm-harness-skills|awesome-vsm-harness)/(?:pull/[1-9][0-9]*|commit/[0-9a-f]{40}|issues/[1-9][0-9]*#issuecomment-[1-9][0-9]*)$")


class FeedbackError(ValueError):
    pass


def reconcile(action: dict, *, fetch_verified_s1_result: Callable[[dict], dict]) -> dict:
    """Require independently verified owner acknowledgement AND effect.

    fetch_verified_s1_result must inspect current owning-S1 primary GitHub
    evidence, verify speaker/permission independently of agent D1-A runtime,
    and prove application/effect, not merely URL shape or a self-authored
    assertion. This callable is not supplied by an untrusted model.
    """
    if type(action) is not dict or action.get("status") != "S1_RETURN_SENT_EFFECT_UNVERIFIED":
        raise FeedbackError("Not a pending delivered S3 decision")
    target = action.get("return_target")
    if not isinstance(target, str) or not REPO_ISSUE.fullmatch(target):
        raise FeedbackError("Unknown or non-S1 return target")
    if action.get("closed") is not False or action.get("S1_acknowledgement_ref") is not None:
        raise FeedbackError("Unverified action cannot preload S1 closure")
    if not callable(fetch_verified_s1_result):
        raise FeedbackError("No independent S1 feedback verifier")
    evidence = fetch_verified_s1_result(action)
    if type(evidence) is not dict:
        raise FeedbackError("Missing independent S1 feedback receipt")
    ack = evidence.get("acknowledgement_ref")
    if not isinstance(ack, str) or not re.fullmatch(re.escape(target) + r"#issuecomment-[1-9][0-9]*", ack):
        raise FeedbackError("S1 acknowledgement must belong to exact receiving work")
    refs = evidence.get("effect_refs")
    owning_repo = target.split("/opensiro/", 1)[1].split("/", 1)[0]
    if type(refs) is not list or not refs or any(
        not isinstance(ref, str) or not EFFECT.fullmatch(ref) or
        f"/opensiro/{owning_repo}/" not in ref for ref in refs
    ):
        raise FeedbackError("Independently verified S1 effect refs required")
    if (evidence.get("s1_owner_verified") is not True or
        evidence.get("effect_verified") is not True or
        evidence.get("s1_independent_of_s3_actor") is not True):
        raise FeedbackError("No independently verified owning S1 closure")
    result = {
        **action,
        "status": "S1_RETURNED_EFFECT_VERIFIED",
        "S1_acknowledgement_ref": ack,
        "S1_effect_refs": refs,
        "closed": True
    }
    return result
