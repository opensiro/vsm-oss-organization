#!/usr/bin/env python3
"""Compose the already-shipped D1-A v1 S3 components. No new authority.

One standard first-party entry for a compatible model-backed agent. This
does not provide a parent S5 signature, runtime credentials, or automatically
promote S1 evidence to a whole-system S3 decision.
"""
from __future__ import annotations

from datetime import datetime, timezone
from functools import partial
import json
from pathlib import Path
import sys
from typing import Callable

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import decision_loop
import github_rest
import github_s1_delivery
import github_s1_receipts
import github_s5_authority
import model_owner
import s1_feedback

GRANT_PATH = ROOT / "contracts" / "s3" / "autonomous-d1a.json"


def _ready(grant: dict, actor: str, now: datetime | None) -> None:
    """Fail before opening a token-backed transport or contacting the model."""
    try:
        decision_loop._gate.check(
            grant, agent_id=actor, now=now or datetime.now(timezone.utc)
        )
    except decision_loop._gate.GateError as exc:
        raise decision_loop.DecisionBlocked(
            f"NO_AUTHORITY: {exc}"
        ) from exc


def run_case(
    *,
    actor_id: str,
    case: dict,
    model: str,
    transport_login: str,
    confirm_parent_authorship: Callable[[dict], bool],
    qualify_current_s3_right: Callable[[dict, dict], dict],
    github_token: str | None = None,
    model_api_key: str | None = None,
    now: datetime | None = None,
) -> dict:
    """Execute only when the checked-in ACTIVE D1-A grant has real authority.

    The two explicit host-provided attestations are essential trust boundaries:
    - confirm_parent_authorship is a separate authenticated S5 owner channel.
      A GitHub login, assistant-created issue comment, or lambda True isn't it.
    - qualify_current_s3_right must actually evaluate cross-domain current
      obligations and S1/S2/S5 falsifiers using verified primary evidence.

    Neither callback can be substituted by agent self-assertion for S3=A.
    """
    grant = json.loads(GRANT_PATH.read_text(encoding="utf-8"))
    _ready(grant, actor_id, now)
    if not callable(confirm_parent_authorship) or not callable(qualify_current_s3_right):
        raise decision_loop.DecisionBlocked("Missing trusted parent/S3 case verifier")

    github = github_rest.GitHubREST(token=github_token)
    reader = github_s1_receipts.GitHubS1Reader(fetch=github.get)

    def live_authority(grant_record: dict, runtime: str) -> dict:
        return github_s5_authority.verify_active_grant(
            grant_record,
            runtime,
            github_get=github.get,
            parent_authorship=confirm_parent_authorship,
            now=now,
        )

    def current_admission(presented_case: dict) -> dict:
        factual = reader.read_s1_admission(presented_case)
        semantic = qualify_current_s3_right(presented_case, factual)
        if (type(semantic) is not dict or
            semantic.get("nonlocal_right_verified") is not True or
            semantic.get("s1_s2_s5_falsifiers_checked") is not True):
            raise decision_loop.DecisionBlocked(
                "NOT_ADMITTED: no independently established present whole-system S3 right"
            )
        # Source-backed S1 admission and independently qualified whole-system
        # discretion remain separate; the agent's later choice is not prefilled.
        return {**factual,
                "nonlocal_right_verified": True,
                "s1_s2_s5_falsifiers_checked": True}

    def return_to_s1(action: dict) -> dict:
        return github_s1_delivery.deliver(
            action,
            api=github,
            verify_authority=lambda _: live_authority(grant, actor_id),
            verify_admission=lambda _: current_admission(case),
            transport_login=transport_login,
        )

    return decision_loop.run_decision(
        grant=grant,
        runtime_actor_id=actor_id,
        case=case,
        check_live_authority=live_authority,
        check_current_admission=current_admission,
        agent_decide=partial(
            model_owner.model_decider, model=model, api_key=model_api_key
        ),
        return_to_s1=return_to_s1,
        now=now,
    )


def reconcile_s1(
    action: dict,
    *,
    acknowledgement_ref: str,
    effect_pr_ref: str,
    github_token: str | None = None,
) -> dict:
    """Separate subsequent S1-owner feedback (never closure on delivery alone).

    GitHub checks factual source/actor/merge references, not semantic adequacy
    of the technical fix. That still requires source-first functional review.
    """
    github = github_rest.GitHubREST(token=github_token)
    reader = github_s1_receipts.GitHubS1Reader(fetch=github.get)
    return s1_feedback.reconcile(
        action,
        fetch_verified_s1_result=lambda a: reader.verify_s1_return(
            a,
            acknowledgement_ref=acknowledgement_ref,
            effect_pr_ref=effect_pr_ref,
        ),
    )
