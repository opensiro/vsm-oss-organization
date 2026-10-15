"""D1-A model-decided return pipeline: mocked capability tests, not live S3=A."""
from __future__ import annotations

import copy
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "modes" / "s3-autonomous" / "decision_loop.py"
SPEC = importlib.util.spec_from_file_location("s3_d1a_decision_loop", CODE)
assert SPEC and SPEC.loader
loop = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(loop)
STORED = json.loads((ROOT / "contracts" / "s3" / "autonomous-d1a.json").read_text())
ACTOR = "test-agent-d1a-runtime-001"
AT = datetime(2026, 10, 16, 8, 0, tzinfo=timezone.utc)
OWNER = "https://github.com/opensiro/vsm-oss-organization/issues/5#issuecomment-777"
IDX = "https://github.com/opensiro/vsm-harness-index/issues/1567"
AWESOME = "https://github.com/opensiro/awesome-vsm-harness/issues/7"


def hypothetical_active():
    x = copy.deepcopy(STORED)
    x.update({
        "status":"ACTIVE", "recipient_execution_identity":ACTOR,
        "owner_attestation_url":OWNER,
        "grant_publication_commit":"a" * 40,
        "effective_from_utc":"2026-10-15T13:00:00Z",
        "expires_at_utc":"2026-11-13T12:00:00Z",
    })
    return x


def fixture():
    return {
        "kind":"nonlocal_current_commitment",
        "commitment_id":"canonical-publication-continuity",
        "return_target":AWESOME,
        "nonlocal_evidence_refs":[IDX,AWESOME],
        "shared_current_constraint":"FICTITIOUS_FIXTURE_ONLY: shared current publication discrepancy",
        "why_s1_s2_cannot_decide":"FICTITIOUS_FIXTURE_ONLY: multi-system decision right",
        "rollback_condition":"FICTITIOUS_FIXTURE_ONLY: owner rescinds on new evidence"
    }


def permitted_context(g, actor):
    return {
        "authorized":True, "revocation_checked":True,
        "attested_actor":actor,
        "owner_comment_url":g["owner_attestation_url"],
        "published_grant_sha":g["grant_publication_commit"]
    }


def admitted(c):
    return {
        "admitted":True, "return_target":c["return_target"],
        "commitment_id":c["commitment_id"],
        "nonlocal_right_verified":True,
        "s1_s2_s5_falsifiers_checked":True
    }


def agent_choice(context):
    assert context["must_choose_own_class"] is True
    return {"class":"REQUIRE_REPAIR",
            "instruction":"Return a specific shared-commitment defect to the named S1 without rewriting its grade",
            "decision_summary":"Agent assessed the frozen test fixture",
            "evidence_refs":[AWESOME]}


def transport(action):
    return {
        "target_issue":action["return_target"],
        "transport_url":"https://github.com/opensiro/awesome-vsm-harness/issues/7#issuecomment-777"
    }


class AgentD1AFlow(unittest.TestCase):
    def execute(self, **override):
        kw=dict(grant=hypothetical_active(), runtime_actor_id=ACTOR, case=fixture(),
                check_live_authority=permitted_context,
                check_current_admission=admitted,
                agent_decide=agent_choice, return_to_s1=transport,
                now=AT)
        kw.update(override)
        return loop.run_decision(**kw)

    def test_shipped_grant_blocks_before_any_agent_choice_or_s1_write(self):
        called=[]
        def record(*_args):
            called.append(True)
            raise AssertionError("must not call adapters")
        with self.assertRaisesRegex(loop.DecisionBlocked, "NO_AUTHORITY"):
            self.execute(grant=STORED,check_live_authority=record,
                         check_current_admission=record,
                         agent_decide=record,return_to_s1=record)
        self.assertEqual([],called)

    def test_expired_grant_blocks_before_decision(self):
        with self.assertRaisesRegex(loop.DecisionBlocked, "NO_AUTHORITY"):
            self.execute(now=datetime(2026,11,13,12,0,tzinfo=timezone.utc))

    def test_human_g1_cannot_own_autonomous_choice(self):
        with self.assertRaisesRegex(loop.DecisionBlocked,"NO_AUTHORITY"):
            self.execute(runtime_actor_id="xLagerFeuer")

    def test_explicit_model_choice_and_return_stay_unclosed_without_s1_effect(self):
        result=self.execute()
        self.assertEqual("REQUIRE_REPAIR",result["selected_class"])
        self.assertEqual("agent",result["owner_class"])
        self.assertEqual("S1_RETURN_SENT_EFFECT_UNVERIFIED",result["status"])
        self.assertFalse(result["closed"])
        self.assertIsNone(result["S1_acknowledgement_ref"])
        self.assertEqual([],result["S1_effect_refs"])
        self.assertIn("/awesome-vsm-harness/issues/7",result["transport_url"])

    def test_denied_or_revoked_live_authority_blocks_decision(self):
        for auth in (
            lambda g,a: {"authorized":False},
            lambda g,a: {**permitted_context(g,a),"revocation_checked":False},
            lambda g,a: {**permitted_context(g,a),"attested_actor":"different"}
        ):
            with self.assertRaisesRegex(loop.DecisionBlocked,"NO_AUTHORITY"):
                self.execute(check_live_authority=auth)

    def test_unadmitted_local_or_fictional_current_work_cannot_choose(self):
        for case in (
            {**fixture(),"kind":"local_s1_repair"},
            {**fixture(),"nonlocal_evidence_refs":[AWESOME,AWESOME]},
        ):
            with self.assertRaises(loop.DecisionBlocked):
                self.execute(case=case)
        with self.assertRaisesRegex(loop.DecisionBlocked,"NOT_ADMITTED"):
            self.execute(check_current_admission=lambda c: {"admitted":False})

    def test_model_cannot_invent_forbidden_decision(self):
        for label in ("STOP","SET_CONSTRAINT","SET_RETRY_BUDGET"):
            with self.assertRaisesRegex(loop.DecisionBlocked, "outside active"):
                self.execute(agent_decide=lambda c: {**agent_choice(c),"class":label})
        with self.assertRaisesRegex(loop.DecisionBlocked,"forbidden"):
            self.execute(agent_decide=lambda c: {**agent_choice(c),
                         "instruction":"Override grade in canonical Index"})
        with self.assertRaisesRegex(loop.DecisionBlocked,"frozen"):
            self.execute(agent_decide=lambda c: {**agent_choice(c),
                         "evidence_refs":["https://github.com/opensiro/vsm-harness-index/issues/123456"]})

    def test_transport_cannot_claim_s1_closure(self):
        def dishonest(a):
            return {**transport(a),"closed":True,"S1_acknowledgement_ref":AWESOME}
        obj=self.execute(return_to_s1=dishonest)
        self.assertFalse(obj["closed"])
        self.assertIsNone(obj["S1_acknowledgement_ref"])
        with self.assertRaisesRegex(loop.DecisionBlocked,"transport"):
            self.execute(return_to_s1=lambda a: {"target_issue":IDX})

    def test_missing_runtime_adapters_fail_closed(self):
        with self.assertRaisesRegex(loop.DecisionBlocked,"adapters"):
            self.execute(agent_decide=None)


if __name__=="__main__":
    unittest.main()
