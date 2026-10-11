"""Negative cases for prospective Index source-first reviewer handoff (#189)."""
from __future__ import annotations
import copy
import importlib.util
import unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_index_reviewer_handoff.py"
SPEC = importlib.util.spec_from_file_location("review_handoff", PATH)
assert SPEC and SPEC.loader
s = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(s)

def fixture():
    src = "https://github.com/acme/code/blob/" + "a" * 40 + "/agent.py"
    return {
        "version": 1, "phase": "RECONCILED",
        "index_issue": "https://github.com/opensiro/vsm-harness-index/issues/1000",
        "proposal_pr": "https://github.com/opensiro/vsm-harness-index/pull/1001",
        "reviewed_head": "b" * 40, "source_repository": "acme/code",
        "source_sha": "a" * 40,
        "profile_ref": "https://github.com/opensiro/vsm-harness-profile/commit/" + "c" * 40,
        "skills_ref": "https://github.com/opensiro/vsm-harness-skills/commit/" + "d" * 40,
        "producer_context": "author-execution-1", "reviewer_context": "reviewer-execution-2",
        "reviewer_input_refs": [src],
        "reviewer_execution_ref": "https://github.com/opensiro/vsm-oss-organization/issues/189#issuecomment-1",
        "source_verdict": {
            "recorded_at": "2026-10-11T09:00:00Z",
            "receipt_url": "https://github.com/opensiro/vsm-oss-organization/issues/189#issuecomment-2",
            "functions": [
                {"function": f, "judgment": "source-derived uncertainty", "primary_refs": [src],
                 "counterevidence": "inspected negative and positive paths"}
                for f in ("S1", "S2", "S3", "S3*", "S4", "S5")
            ]
        },
        "comparison": {
            "proposal_revealed_at": "2026-10-11T09:20:00Z",
            "receipt_url": "https://github.com/opensiro/vsm-harness-index/issues/1000#issuecomment-3",
            "pr_head": "b" * 40, "outcome": "FINDING", "difference_summary": "bounded difference"
        }
    }

class ReviewHandoffTests(unittest.TestCase):
    def test_valid_structure_not_proof_of_execution(self):
        self.assertEqual(s.validate(fixture()), [])
    def test_requested_has_no_verdict(self):
        r = fixture()
        r.update(phase="REQUESTED", source_verdict=None, comparison=None, reviewer_execution_ref=None)
        self.assertEqual(s.validate(r), [])
    def test_requested_unassigned_does_not_invent_reviewer(self):
        r = fixture()
        r.update(phase="REQUESTED", reviewer_context=None, reviewer_execution_ref=None,
                 source_verdict=None, comparison=None)
        self.assertEqual(s.validate(r), [])

    def test_requested_without_either_known_context_is_pending(self):
        r = fixture()
        r.update(phase="REQUESTED", producer_context=None, reviewer_context=None,
                 reviewer_execution_ref=None, source_verdict=None, comparison=None)
        self.assertEqual(s.validate(r), [])

    def test_requested_same_predeclared_context_fails(self):
        r = fixture()
        r.update(phase="REQUESTED", reviewer_context=r["producer_context"],
                 reviewer_execution_ref=None, source_verdict=None, comparison=None)
        self.assertTrue(s.validate(r))

    def test_source_verdict_requires_real_reviewer_context(self):
        r = fixture()
        r.update(phase="SOURCE_VERDICT_RECORDED", reviewer_context=None,
                 comparison=None)
        self.assertTrue(s.validate(r))

    def test_reconciled_requires_real_producer_context(self):
        r = fixture()
        r["producer_context"] = None
        self.assertTrue(s.validate(r))

    def test_source_only_has_no_comparison(self):
        r = fixture()
        r.update(phase="SOURCE_VERDICT_RECORDED", comparison=None)
        self.assertEqual(s.validate(r), [])
    def test_same_context_rejected(self):
        r = fixture()
        r["reviewer_context"] = r["producer_context"]
        self.assertTrue(s.validate(r))
    def test_proposal_contamination_rejected(self):
        r = fixture()
        r["reviewer_input_refs"].append(r["proposal_pr"])
        self.assertTrue(s.validate(r))
    def test_single_good_input_does_not_hide_exposed_author_issue(self):
        r = fixture()
        r["reviewer_input_refs"].append(
            "https://github.com/opensiro/vsm-harness-index/issues/1387")
        self.assertTrue(s.validate(r))

    def test_single_good_input_does_not_hide_other_source(self):
        r = fixture()
        r["reviewer_input_refs"].append(
            "https://github.com/another/source/blob/" + "a" * 40 + "/file.py")
        self.assertTrue(s.validate(r))

    def test_source_first_allows_exact_contract_refs(self):
        r = fixture()
        r["reviewer_input_refs"].extend([r["profile_ref"], r["skills_ref"]])
        self.assertEqual(s.validate(r), [])

    def test_normative_ref_on_floating_branch_rejected(self):
        r = fixture()
        r["profile_ref"] = "https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md"
        self.assertTrue(s.validate(r))

    def test_primary_ref_to_author_pr_rejected(self):
        r = fixture()
        r["source_verdict"]["functions"][3]["primary_refs"] = [
            "https://github.com/opensiro/vsm-harness-index/pull/1388"]
        self.assertTrue(s.validate(r))

    def test_primary_ref_to_unpinned_other_repo_rejected(self):
        r = fixture()
        r["source_verdict"]["functions"][3]["primary_refs"] = [
            "https://github.com/get-bb/bb/blob/main/src/file.py"]
        self.assertTrue(s.validate(r))

    def test_primary_ref_to_wrong_upstream_sha_rejected(self):
        r = fixture()
        r["source_verdict"]["functions"][3]["primary_refs"] = [
            "https://github.com/acme/code/blob/" + "f" * 40 + "/agent.py"]
        self.assertTrue(s.validate(r))

    def test_exact_sha_line_anchor_is_permitted(self):
        r = fixture()
        r["source_verdict"]["functions"][3]["primary_refs"] = [
            "https://github.com/acme/code/blob/" + "a" * 40 + "/agent.py#L10-L20"]
        self.assertEqual(s.validate(r), [])

    def test_input_branch_not_pinned(self):
        r = fixture()
        r["reviewer_input_refs"] = ["https://github.com/acme/code/blob/main/agent.py"]
        self.assertTrue(s.validate(r))
    def test_input_wrong_frozen_sha(self):
        r = fixture()
        r["reviewer_input_refs"] = ["https://github.com/acme/code/blob/" + "f" * 40 + "/agent.py"]
        self.assertTrue(s.validate(r))
    def test_unpinned_source_rejected(self):
        r = fixture()
        r["source_sha"] = "main"
        self.assertTrue(s.validate(r))
    def test_pr_head_drift_rejected(self):
        r = fixture()
        r["comparison"]["pr_head"] = "f" * 40
        self.assertTrue(s.validate(r))
    def test_source_verdict_after_reveal_rejected(self):
        r = fixture()
        r["comparison"]["proposal_revealed_at"] = "2026-10-11T08:50:00Z"
        self.assertTrue(s.validate(r))
    def test_missing_s3star_evidence_rejected(self):
        r = fixture()
        r["source_verdict"]["functions"][3]["primary_refs"] = []
        self.assertTrue(s.validate(r))
    def test_missing_executor_trace_rejected(self):
        r = fixture()
        r["reviewer_execution_ref"] = None
        self.assertTrue(s.validate(r))
    def test_extra_approval_claim_rejected(self):
        r = fixture()
        r["github_approved"] = True
        self.assertTrue(s.validate(r))
    def test_incomplete_functional_set_rejected(self):
        r = fixture()
        r["source_verdict"]["functions"][0]["function"] = "S2"
        self.assertTrue(s.validate(r))
    def test_proposal_exposed_in_source_only_rejected(self):
        r = fixture()
        r.update(phase="SOURCE_VERDICT_RECORDED")
        self.assertTrue(s.validate(r))

if __name__ == "__main__":
    unittest.main()
