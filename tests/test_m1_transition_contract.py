from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class M1TransitionContractTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_active_milestone_state_is_owned_by_planning_surfaces(self) -> None:
        readme = self.read("README.md")
        roadmap = self.read("docs/ROADMAP.md")
        s3star = self.read("contracts/s3star/audit.md")
        s3 = self.read("contracts/s3/current-control.md")
        self.assertIn("M0–M2 have completed", readme)
        self.assertIn("M3", readme)
        self.assertIn("## M2 — Parent-governed identity boundary", roadmap)
        self.assertIn("M1 is formally complete", roadmap)
        self.assertIn("M1", roadmap)
        self.assertNotIn("active formal roadmap milestone", s3star.lower())
        self.assertNotIn("active formal roadmap milestone", s3.lower())

    def test_m1_target_is_s3_and_s3star_constructor(self) -> None:
        readme = self.read("README.md")
        roadmap = self.read("docs/ROADMAP.md")
        s3star = self.read("contracts/s3star/audit.md")
        s3 = self.read("contracts/s3/current-control.md")
        self.assertIn("A   —   C   C   —   P", readme)
        self.assertIn("Target: `A — C C — —`", roadmap)
        self.assertIn("source-first", readme.lower())
        self.assertIn("Target: `A — C C — —`", roadmap)
        self.assertIn("current constructor target is `S3*=C`", s3star)
        self.assertIn("does **not** establish `S3=C` or `S3=A`", s3)

    def test_s3_c_methodology_threshold_is_not_identical_to_local_m1_exit(self) -> None:
        s3 = self.read("contracts/s3/current-control.md")
        roadmap = self.read("docs/ROADMAP.md")
        review = self.read("docs/reviews/2026-10-13-s3-c-threshold.md")
        self.assertIn("not a universal Methodology prerequisite", s3)
        self.assertIn("local M1 exit", s3)
        self.assertIn("not a universal Skills Methodology prerequisite", roadmap)
        self.assertIn("LOCAL_M1_THRESHOLD_CONFLATION_CONFIRMED", review)
        self.assertIn("S3_POSITIVE_NOT_ADJUDICATED", review)
        self.assertIn("issue #39", roadmap + s3 + review)
        self.assertIn("whole-system S3 function", s3)
        self.assertIn("first-party", s3)
        self.assertIn("S3=A", s3)
        self.assertIn("S3=C", s3)
        self.assertIn("no profile or skills release", review.lower())

    def test_approved_m1_exit_preserves_positive_function_threshold(self) -> None:
        roadmap = self.read("docs/ROADMAP.md")
        s3 = self.read("contracts/s3/current-control.md")
        self.assertIn("approved source-first alternative", roadmap)
        self.assertIn("approved **Organization M1 exit gate**", s3)
        self.assertIn("genuine S3 whole-system current-control function", roadmap)
        self.assertIn("legitimate decisive", roadmap)
        self.assertIn("boundary-reachable", roadmap)
        self.assertIn("### Exit criteria", roadmap)
        self.assertIn("optional", s3)
        self.assertIn("first-party", s3)
        self.assertIn("not a universal Methodology prerequisite", s3)

    def test_accepted_operator_option_b_is_not_a_grade(self) -> None:
        roadmap = self.read("docs/ROADMAP.md")
        s3 = self.read("contracts/s3/current-control.md")
        decision = self.read("docs/proposals/2026-10-13-m1-s3-c-alternate-acceptance.md")
        self.assertIn("effective", roadmap.lower())
        self.assertIn("source-first", roadmap)
        self.assertIn("S3=C NOT ESTABLISHED", decision)
        self.assertIn("OPTION_B_APPROVED", decision)
        self.assertIn("Mere naming, templates", s3)
        self.assertIn("no present grade changes", s3)
        self.assertIn("### Exit criteria", roadmap)

    def test_s3_constructor_has_canonical_s1_return_hook(self) -> None:
        s1 = self.read("roles/S1.md")
        s3 = self.read("contracts/s3/current-control.md")
        prompt = self.read("prompts/apply-s3-control.md")
        self.assertIn("## Returned S3 current control", s1)
        self.assertIn("contracts/s3/current-control.md", s1)
        self.assertIn("The S1-side adapter", s3)
        self.assertIn("Apply one returned S3 current-control decision to S1", prompt)

    def test_pre_admission_s3_operator_intake_keeps_decision_and_review_gates(self) -> None:
        role = self.read("roles/S3.md")
        intake = self.read("prompts/intake-s3-current-control.md")
        index = self.read("docs/README.md")
        self.assertIn("prompts/intake-s3-current-control.md", role)
        self.assertIn("prompts/intake-s3-current-control.md", index)
        for clause in (
            "existing S1 work",
            "whole-system current view",
            "legitimate decision owner",
            "S1 return target",
            "prompts/apply-s3-control.md",
            "S1, S2, S4 or S5",
            "no S3 transaction",
            "not evidence of `S3=C`",
            "generic `continue`",
        ):
            self.assertIn(clause, intake)

    def test_s3star_constructor_contract_is_function_specific(self) -> None:
        roadmap = self.read("docs/ROADMAP.md")
        s3star = self.read("contracts/s3star/audit.md")
        audit_role = self.read("roles/S3STAR.md")
        audit_prompt = self.read("prompts/audit-s1-work.md")
        audit_record = self.read("templates/s3star-audit-record.md")
        self.assertIn("S3*=C — complementary-audit constructor", roadmap)
        for outcome in ("`PASS`", "`FINDING`", "`INSUFFICIENT`"):
            self.assertIn(outcome, s3star)
        self.assertIn("actor adapter", audit_role)
        self.assertIn("autonomous verifier or a second agent", audit_prompt)
        self.assertIn("Auditor / composed actor:", audit_record)
        self.assertIn("M1 constructor check", audit_record)


if __name__ == "__main__":
    unittest.main()
