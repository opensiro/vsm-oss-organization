from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class M1TransitionContractTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_active_milestone_surfaces_are_m1(self) -> None:
        readme = self.read("README.md")
        s3star = self.read("S3STAR_AUDIT.md")
        s3 = self.read("S3_CONTROL_SURFACE.md")

        self.assertIn("Active formal work is M1", readme)
        self.assertIn("active formal roadmap milestone is M1", s3star)
        self.assertIn("active formal roadmap milestone is M1", s3)
        self.assertNotIn("active roadmap milestone remains M0", s3star)
        self.assertNotIn("active roadmap milestone remains M0", s3)

    def test_m1_target_is_s3_and_s3star_constructor(self) -> None:
        readme = self.read("README.md")
        roadmap = self.read("ROADMAP.md")
        s3star = self.read("S3STAR_AUDIT.md")

        self.assertIn("A   —   C   C   —   —", readme)
        self.assertIn("Target: `A — C C — —`", roadmap)
        self.assertIn("Its S3* target is constructor state `C`, not autonomous state `A`", s3star)
        self.assertIn("An autonomous verifier is **not** an M1 requirement", s3star)

    def test_s3_constructor_has_canonical_s1_return_hook(self) -> None:
        s1 = self.read("roles/S1.md")
        s3 = self.read("S3_CONTROL_SURFACE.md")
        prompt = self.read("prompts/apply-s3-control.md")

        self.assertIn("## M1 current-control return hook", s1)
        self.assertIn("S3_CONTROL_SURFACE.md", s1)
        self.assertIn("The S1 role contains the M1 return-hook rules", s3)
        self.assertIn("Apply one returned S3 current-control decision to S1", prompt)

    def test_s3star_constructor_contract_is_function_specific(self) -> None:
        roadmap = self.read("ROADMAP.md")
        s3star = self.read("S3STAR_AUDIT.md")
        audit_role = self.read("roles/S3STAR.md")
        audit_prompt = self.read("prompts/audit-s1-work.md")
        audit_record = self.read("templates/s3star-audit-record.md")

        self.assertIn("S3*=C — complementary-audit constructor", roadmap)
        for outcome in ("`PASS`", "`FINDING`", "`INSUFFICIENT`"):
            self.assertIn(outcome, s3star)
        self.assertIn("first-party S3*-specific path", audit_role)
        self.assertIn("M1 does not require an autonomous verifier or a second agent", audit_prompt)
        self.assertIn("Auditor / composed actor:", audit_record)
        self.assertIn("M1 constructor check", audit_record)


if __name__ == "__main__":
    unittest.main()
