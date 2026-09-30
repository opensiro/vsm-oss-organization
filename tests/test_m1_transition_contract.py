from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class M1TransitionContractTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_active_milestone_state_is_owned_by_planning_surfaces(self) -> None:
        readme = self.read("README.md")
        roadmap = self.read("ROADMAP.md")
        s3star = self.read("contracts/s3star/audit.md")
        s3 = self.read("contracts/s3/current-control.md")

        self.assertIn("Active formal work is M1", readme)
        self.assertIn("M1", roadmap)
        self.assertNotIn("active formal roadmap milestone", s3star.lower())
        self.assertNotIn("active formal roadmap milestone", s3.lower())

    def test_m1_target_is_s3_and_s3star_constructor(self) -> None:
        readme = self.read("README.md")
        roadmap = self.read("ROADMAP.md")
        s3star = self.read("contracts/s3star/audit.md")
        s3 = self.read("contracts/s3/current-control.md")

        self.assertIn("A   —   C   C   —   —", readme)
        self.assertIn("Target: `A — C C — —`", roadmap)
        self.assertIn("current constructor target is `S3*=C`", s3star)
        self.assertIn("does **not** establish `S3=C` or `S3=A`", s3)

    def test_s3_constructor_has_canonical_s1_return_hook(self) -> None:
        s1 = self.read("roles/S1.md")
        s3 = self.read("contracts/s3/current-control.md")
        prompt = self.read("prompts/apply-s3-control.md")

        self.assertIn("## Returned S3 current control", s1)
        self.assertIn("contracts/s3/current-control.md", s1)
        self.assertIn("The S1-side adapter", s3)
        self.assertIn("Apply one returned S3 current-control decision to S1", prompt)

    def test_s3star_constructor_contract_is_function_specific(self) -> None:
        roadmap = self.read("ROADMAP.md")
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

    def test_root_m1_contract_names_are_compatibility_pointers_only(self) -> None:
        self.assertIn(
            "Canonical contract: [`contracts/s3/current-control.md`]",
            self.read("S3_CONTROL_SURFACE.md"),
        )
        self.assertIn(
            "Canonical contract: [`contracts/s3star/audit.md`]",
            self.read("S3STAR_AUDIT.md"),
        )


if __name__ == "__main__":
    unittest.main()
