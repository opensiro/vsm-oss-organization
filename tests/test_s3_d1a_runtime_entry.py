"""Existing D1-A adapters are wired, but inactive grant cannot do work."""
import importlib.util
import json
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

HERE=Path(__file__).resolve().parents[1]
S=HERE/"modes"/"s3-autonomous"/"runtime_entry.py"
spec=importlib.util.spec_from_file_location("d1a_v1_runtime_entry_test",S)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
STORED=json.loads((HERE/"contracts"/"s3"/"autonomous-d1a.json").read_text())
ACTOR="source-test-agent-runtime-id-0001"
AT=__import__("datetime").datetime(2026,10,16,8,tzinfo=__import__("datetime").timezone.utc)
ISSUE="https://github.com/opensiro/awesome-vsm-harness/issues/7"
INDEX="https://github.com/opensiro/vsm-harness-index/issues/1567"

def case():
    return {"kind":"nonlocal_current_commitment",
      "return_target":ISSUE,
      "s1_admission_comment_url":ISSUE+"#issuecomment-17",
      "commitment_id":"canonical-publication-continuity",
      "nonlocal_evidence_refs":[ISSUE,INDEX],
      "shared_current_constraint":"HYPOTHETICAL current shared commitment discrepancy",
      "why_s1_s2_cannot_decide":"HYPOTHETICAL beyond-local present decision",
      "rollback_condition":"If evidence no longer holds"}

def future_grant():
    return {**STORED,"status":"ACTIVE",
      "recipient_execution_identity":ACTOR,
      "owner_attestation_url":
         "https://github.com/opensiro/vsm-oss-organization/issues/5#issuecomment-987",
      "grant_publication_commit":"a"*40,
      "effective_from_utc":"2026-10-15T13:00:00Z",
      "expires_at_utc":"2026-11-12T13:00:00Z"}

class TestD1AV1Runtime(TestCase):
    def execute(self, **kw):
        opts=dict(actor_id=ACTOR,case=case(),model="example-model",
            transport_login="s3-test-bot",
            confirm_parent_authorship=lambda _: True,
            qualify_current_s3_right=lambda *_:{
              "nonlocal_right_verified":True,
              "s1_s2_s5_falsifiers_checked":True},
            now=AT)
        opts.update(kw)
        return m.run_case(**opts)

    def test_checked_in_pending_grant_blocks_before_token_or_model(self):
        with patch.object(m.github_rest,"GitHubREST",
                          side_effect=AssertionError("API must not open")) as network:
            with patch.object(m.model_owner,"model_decider",
                              side_effect=AssertionError("Model must not run")) as model:
                with self.assertRaisesRegex(m.decision_loop.DecisionBlocked,
                                             "NO_AUTHORITY"):
                    self.execute()
            network.assert_not_called()
            model.assert_not_called()

    def test_no_trusted_parent_verifier_does_not_start(self):
        with patch.object(m,"GRANT_PATH") as source:
            source.read_text.return_value=json.dumps(future_grant())
            with patch.object(m.github_rest,"GitHubREST",
                              side_effect=AssertionError("API must not open")):
                with self.assertRaisesRegex(m.decision_loop.DecisionBlocked,
                                             "Missing trusted"):
                    self.execute(confirm_parent_authorship=None)

    def test_bound_existing_components_return_is_pending_not_closed(self):
        refs=[]
        class FakeGithub:
            def __init__(self, **kw):refs.append("github")
            def get(self, path):return {"source":"hypothetical"}
        class FakeS1:
            def __init__(self, **kw): pass
            def read_s1_admission(self, c):
                refs.append("s1facts")
                return {"admitted":True,"return_target":c["return_target"],
                        "commitment_id":c["commitment_id"]}
        def fake_authority(g, a, **kw):
            refs.append("authority")
            return {"authorized":True,"revocation_checked":True,
                "attested_actor":a,"owner_comment_url":g["owner_attestation_url"],
                "published_grant_sha":g["grant_publication_commit"]}
        def fake_choice(ctx,**kw):
            refs.append("model")
            return {"class":"REQUIRE_REPAIR","instruction":"Repair the bounded S1 work",
                "decision_summary":"Hypothetical agent model chose repair",
                "evidence_refs":[INDEX]}
        def fake_delivery(a,**kw):
            refs.append("s1send")
            self.assertEqual("REQUIRE_REPAIR",a["selected_class"])
            return {"target_issue":ISSUE,"transport_url":ISSUE+"#issuecomment-21"}
        with patch.object(m,"GRANT_PATH") as source, \
             patch.object(m.github_rest,"GitHubREST",FakeGithub), \
             patch.object(m.github_s1_receipts,"GitHubS1Reader",FakeS1), \
             patch.object(m.github_s5_authority,"verify_active_grant",fake_authority), \
             patch.object(m.model_owner,"model_decider",fake_choice), \
             patch.object(m.github_s1_delivery,"deliver",fake_delivery):
            source.read_text.return_value=json.dumps(future_grant())
            out=self.execute()
        self.assertFalse(out["closed"])
        self.assertEqual("S1_RETURN_SENT_EFFECT_UNVERIFIED",out["status"])
        self.assertIn("model",refs)
        self.assertIn("s1send",refs)
        self.assertGreater(refs.count("authority"),0)
        self.assertGreater(refs.count("s1facts"),0)

    def test_rejected_nonlocal_claim_blocks_model_and_s1_transport(self):
        with patch.object(m,"GRANT_PATH") as source, \
             patch.object(m.github_rest,"GitHubREST",return_value=object()), \
             patch.object(m.github_s1_receipts,"GitHubS1Reader") as reader, \
             patch.object(m.github_s5_authority,"verify_active_grant") as authority, \
             patch.object(m.model_owner,"model_decider") as model:
            source.read_text.return_value=json.dumps(future_grant())
            reader.return_value.read_s1_admission.return_value={
              "admitted":True,"return_target":ISSUE,
              "commitment_id":"canonical-publication-continuity"}
            authority.return_value={
              "authorized":True,"revocation_checked":True,
              "attested_actor":ACTOR,
              "owner_comment_url":future_grant()["owner_attestation_url"],
              "published_grant_sha":"a"*40}
            with self.assertRaisesRegex(m.decision_loop.DecisionBlocked,
                                         "NOT_ADMITTED"):
                self.execute(qualify_current_s3_right=lambda *_: {
                  "nonlocal_right_verified":False,
                  "s1_s2_s5_falsifiers_checked":False})
            model.assert_not_called()
