"""Negative evidence fixtures for derived S3* -> Index finding-return tracking."""
from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "scripts" / "check_s3star_finding_return.py"
SPEC = importlib.util.spec_from_file_location("s3star_return", MODULE)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)

def fixture():
    return json.loads((ROOT / "records/s3star/finding-return/2026-10-11-index-open.json").read_text(encoding="utf-8"))

def decision(outcome="CORRECTION_REQUIRED"):
    return {
        "outcome": outcome, "owner_actor": "actual-index-owner-1",
        "decided_at_utc": "2026-10-11T14:00:00Z",
        "index_reference": "https://github.com/opensiro/vsm-harness-index/issues/1381#issuecomment-123",
        "index_main_sha": "f" * 40, "reason": "reasoned public source review",
    }

def verification(effect="CORRECTION_MERGED", pr=True):
    return {
        "effect": effect, "verifier_actor": "separate-check-context-2",
        "verified_at_utc": "2026-10-11T14:30:00Z",
        "verification_ref": "https://github.com/opensiro/vsm-oss-organization/issues/200#issuecomment-222",
        "index_main_sha": "e" * 40,
        "result_pr_ref": "https://github.com/opensiro/vsm-harness-index/pull/1400" if pr else None,
    }

class FindingReturnTests(unittest.TestCase):
    def assertBlocked(self, data):
        self.assertNotEqual(validator.validate(data), [])
    def test_real_four_finding_snapshot_is_only_routed(self):
        f = fixture()
        self.assertEqual(validator.validate(f), [])
        self.assertEqual(len(f["findings"]), 4)
        self.assertTrue(all(x["disposition"] == "ROUTED_OPEN" for x in f["findings"]))
    def test_no_owner_decision_cannot_verify(self):
        f = fixture()
        f["findings"][0]["disposition"] = "VERIFIED"
        self.assertBlocked(f)
    def test_duplicate_row_cannot_count_twice(self):
        f = fixture()
        f["findings"].append(copy.deepcopy(f["findings"][0]))
        f["findings"][-1]["id"] = "different-finding-id"
        self.assertBlocked(f)
    def test_duplicate_identity_cannot_count_twice(self):
        f = fixture()
        f["findings"].append(copy.deepcopy(f["findings"][0]))
        self.assertBlocked(f)
    def test_routed_ref_must_match_owner_issue(self):
        f = fixture()
        f["findings"][0]["routed_ref"] = "https://github.com/opensiro/vsm-harness-index/issues/1011"
        self.assertBlocked(f)
    def test_frozen_source_sha_required(self):
        f = fixture()
        f["findings"][0]["source_sha"] = "main"
        self.assertBlocked(f)
    def test_well_formed_but_wrong_frozen_sha_rejected(self):
        f = fixture()
        f["findings"][0]["source_sha"] = "f" * 40
        self.assertBlocked(f)
    def test_other_valid_index_owner_and_routing_rejected(self):
        f = fixture()
        owner = "https://github.com/opensiro/vsm-harness-index/issues/999999"
        f["findings"][0]["index_owner_issue"] = owner
        f["findings"][0]["routed_ref"] = owner
        self.assertBlocked(f)
    def test_frozen_claim_scope_cannot_silently_change(self):
        f = fixture()
        f["findings"][0]["scope"] = "A newly asserted claim"
        self.assertBlocked(f)
    def test_frozen_audit_origin_cannot_be_repointed(self):
        f = fixture()
        f["findings"][2]["original_audit_ref"] = "https://github.com/opensiro/vsm-oss-organization/issues/188"
        self.assertBlocked(f)
    def test_dropping_frozen_finding_is_rejected(self):
        f = fixture()
        f["findings"].pop()
        self.assertBlocked(f)
    def test_reordering_four_frozen_findings_is_allowed(self):
        f = fixture()
        f["findings"].reverse()
        self.assertEqual(validator.validate(f), [])
    def test_later_derived_snapshot_preserves_frozen_identity(self):
        f = fixture()
        f["snapshot_date_utc"] = "2026-10-12"
        f["organization_main_sha"] = "f" * 40
        f["index_main_sha"] = "e" * 40
        self.assertEqual(validator.validate(f), [])
    def test_unrelated_owner_issue_not_allowed(self):
        f = fixture()
        f["findings"][0]["index_owner_issue"] = "https://github.com/not-index/repo/issues/1"
        self.assertBlocked(f)
    def test_original_outcome_immutable(self):
        f = fixture()
        f["findings"][0]["original_outcome"] = "PASS"
        self.assertBlocked(f)
    def test_routed_row_cannot_claim_decision(self):
        f = fixture()
        f["findings"][0]["owner_decision"] = decision()
        self.assertBlocked(f)
    def test_accepted_owner_adjudication_structural_pass(self):
        f = fixture()
        f["findings"][0]["disposition"] = "ADJUDICATED"
        f["findings"][0]["owner_decision"] = decision()
        self.assertEqual(validator.validate(f), [])
    def test_owner_decision_requires_owner_ref(self):
        f = fixture()
        f["findings"][0]["disposition"] = "ADJUDICATED"
        f["findings"][0]["owner_decision"] = decision()
        f["findings"][0]["owner_decision"]["index_reference"] = "https://github.com/opensiro/vsm-oss-organization/issues/200#issuecomment-222"
        self.assertBlocked(f)
    def test_adjudicated_cannot_attach_verified_receipt(self):
        f = fixture()
        f["findings"][0]["disposition"] = "ADJUDICATED"
        f["findings"][0]["owner_decision"] = decision()
        f["findings"][0]["verification"] = verification()
        self.assertBlocked(f)
    def test_rejected_evidence_cannot_look_verified(self):
        f = fixture()
        f["findings"][0].update(disposition="VERIFIED", owner_decision=decision("INSUFFICIENT_EVIDENCE"), verification=verification())
        self.assertBlocked(f)
    def test_same_owner_and_verifier_context_rejected(self):
        f = fixture()
        f["findings"][0].update(disposition="VERIFIED", owner_decision=decision(), verification=verification())
        f["findings"][0]["verification"]["verifier_actor"] = f["findings"][0]["owner_decision"]["owner_actor"]
        self.assertBlocked(f)
    def test_missing_final_pr_rejected(self):
        f = fixture()
        f["findings"][0].update(disposition="VERIFIED", owner_decision=decision(), verification=verification(pr=False))
        self.assertBlocked(f)
    def test_nochange_cannot_claim_merged_correction(self):
        f = fixture()
        f["findings"][0].update(disposition="VERIFIED", owner_decision=decision("NO_CHANGE_EVIDENCED"), verification=verification())
        self.assertBlocked(f)
    def test_verified_before_adjudicated_rejected(self):
        f = fixture()
        f["findings"][0].update(disposition="VERIFIED", owner_decision=decision(), verification=verification())
        f["findings"][0]["verification"]["verified_at_utc"] = "2026-10-11T13:00:00Z"
        self.assertBlocked(f)
    def test_structural_corrected_case_not_live_proof(self):
        f = fixture()
        f["findings"][0].update(disposition="VERIFIED", owner_decision=decision(), verification=verification())
        self.assertEqual(validator.validate(f), [])
    def test_structural_reasoned_nochange_not_live_proof(self):
        f = fixture()
        f["findings"][0].update(disposition="VERIFIED", owner_decision=decision("NO_CHANGE_EVIDENCED"), verification=verification(effect="JUSTIFIED_NO_CHANGE", pr=False))
        self.assertEqual(validator.validate(f), [])
    def test_wrong_schema_rejected(self):
        f = fixture()
        f["view_kind"] = "CANONICAL_ASSESSMENT"
        self.assertBlocked(f)

if __name__ == "__main__":
    unittest.main()