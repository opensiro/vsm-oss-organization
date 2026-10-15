#!/usr/bin/env python3
"""Authorized, deduplicated S3-to-S1 GitHub issue-comment delivery.

This source owns *transport only*, never D1-A authorization or S3 semantic
admission. Require both independently attested inputs before any GitHub POST.
"""
from __future__ import annotations
import hashlib
import json
import re
from typing import Callable

ISSUE = re.compile(r"https://github\.com/opensiro/(vsm-harness-index|vsm-harness-skills|awesome-vsm-harness)/issues/([1-9][0-9]*)$")
CLASS = frozenset(("CONTINUE", "REQUIRE_REPAIR"))
MARKER = "OPENSIRO_S3_D1A_RETURN_V1\n"
USER = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}$")

class S1DeliveryError(ValueError):
    pass

def require(condition, why):
    if not condition:
        raise S1DeliveryError(why)

def deliver(action: dict, *, api: Callable[[str, str, dict | None], object],
            verify_authority: Callable[[dict], dict],
            verify_admission: Callable[[dict], dict],
            transport_login: str) -> dict:
    """Operate with explicit authenticated GitHub GET/POST host.

    api(method,path,json_body) is a host-provided signed GitHub REST client.
    This module cannot forge S1 authorization: callers still must attest
    owner grant and independently established S3 semantic admission.
    """
    require(type(action) is dict and action.get("owner_class") == "agent" and
            action.get("selected_class") in CLASS and action.get("closed") is False and
            action.get("S1_acknowledgement_ref") is None and
            action.get("S1_effect_refs") == [],
            "only one open bounded agent-owned action can be returned")
    target = action.get("return_target")
    m = ISSUE.fullmatch(target) if isinstance(target, str) else None
    require(m is not None, "S1 target outside bounded GitHub issues")
    repo, number = m.groups()
    login = transport_login
    require(isinstance(login, str) and USER.fullmatch(login) and login != "xLagerFeuer",
            "transport identity must be a distinct authenticated non-parent actor")
    require(callable(api) and callable(verify_authority) and callable(verify_admission),
            "missing required live authority/admission/GitHub transport adapters")
    auth = verify_authority(action)
    require(type(auth) is dict and auth.get("authorized") is True and
            auth.get("revocation_checked") is True and
            auth.get("owner_comment_url") == action.get("grant_owner_receipt") and
            auth.get("attested_actor") == action.get("actor_execution_id"),
            "owner's active D1-A grant is not independently verified")
    admitted = verify_admission(action)
    require(type(admitted) is dict and admitted.get("admitted") is True and
            admitted.get("return_target") == target and
            admitted.get("nonlocal_right_verified") is True and
            admitted.get("s1_s2_s5_falsifiers_checked") is True,
            "whole-system S3 right and current S1 admission not proven")
    actor = api("GET", "/user", None)
    require(type(actor) is dict and actor.get("login") == login,
            "current GitHub token identity does not match authorized transport")
    p = api("GET", f"/repos/opensiro/{repo}/collaborators/{login}/permission", None)
    require(type(p) is dict and p.get("permission") in ("write", "maintain", "admin"),
            "transport account has no owning-S1 write capability")
    issue = api("GET", f"/repos/opensiro/{repo}/issues/{number}", None)
    require(type(issue) is dict and issue.get("state") == "open" and
            issue.get("html_url") == target and not issue.get("pull_request"),
            "S1 issue is unavailable or not currently open")
    instruction=action.get("instruction")
    require(isinstance(instruction,str) and 0<len(instruction)<=900,
            "unbounded or missing instruction")
    evidence=action.get("evidence_refs")
    require(type(evidence) is list and evidence and all(
        isinstance(s,str) and s.startswith("https://github.com/opensiro/")
        for s in evidence), "exact frozen first-party evidence refs required")
    record={k:action[k] for k in (
        "actor_execution_id", "grant_owner_receipt", "selected_class",
        "instruction", "evidence_refs", "return_target", "commitment_id")}
    blob=json.dumps(record,sort_keys=True,separators=(",",":"),ensure_ascii=False)
    require(len(blob.encode("utf-8")) <= 6000, "S3 delivery exceeds bounded size")
    digest=hashlib.sha256(blob.encode("utf-8")).hexdigest()
    body=MARKER+json.dumps({"id":"sha256:"+digest,"action":record},
        ensure_ascii=False,sort_keys=True,separators=(",",":"))
    require(len(body.encode("utf-8")) <= 6400, "S3 delivery comment too large")
    # Exhaustive idempotency lookup: refuse to double-send on retry.
    for page in range(1,31):
        comments=api("GET",f"/repos/opensiro/{repo}/issues/{number}/comments?per_page=100&page={page}",None)
        require(type(comments) is list and len(comments)<=100,
                "S1 comment history not fully readable")
        for c in comments:
            require(type(c) is dict,"malformed S1 comment")
            if c.get("body","").startswith(MARKER) and c.get("body") == body:
                require(type(c.get("user")) is dict and c["user"].get("login")==login and
                        re.fullmatch(re.escape(target)+r"#issuecomment-[1-9][0-9]*",
                          str(c.get("html_url"))),
                        "duplicate action found under different transport actor")
                return {"target_issue":target,"transport_url":c["html_url"],
                        "delivery_status":"ALREADY_SENT"}
        if len(comments)<100:break
    else:
        raise S1DeliveryError("S1 history too large to guarantee idempotency")
    posted=api("POST",f"/repos/opensiro/{repo}/issues/{number}/comments",{"body":body})
    require(type(posted) is dict and type(posted.get("user")) is dict and
            posted["user"].get("login")==login and
            re.fullmatch(re.escape(target)+r"#issuecomment-[1-9][0-9]*",
              str(posted.get("html_url"))),
            "GitHub did not confirm delivery on exact named S1 issue")
    return {"target_issue":target,"transport_url":posted["html_url"],
            "delivery_status":"POSTED_S1_EFFECT_UNVERIFIED"}
