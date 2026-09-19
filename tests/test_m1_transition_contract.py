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

    def test_s3_constructor_has_canonical_s1_return_hook(self) -> None:
        s1 = self.read("roles/S1.md")
        s3 = self.read("S3_CONTROL_SURFACE.md")
        prompt = self.read("prompts/apply-s3-control.md")

        self.assertIn("## M1 current-control return hook", s1)
        self.assertIn("S3_CONTROL_SURFACE.md", s1)
        self.assertIn("The S1 role contains the M1 return-hook rules", s3)
        self.assertIn("Apply one returned S3 current-control decision to S1", prompt)

    def test_m1_does_not_require_executor_identity_proof(self) -> None:
        readme = self.read("README.md")
        roadmap = self.read("ROADMAP.md")
        domain_contracts = self.read("S1_DOMAIN_CONTRACTS.md")
        coverage = self.read("S1_AUTONOMY_COVERAGE.md")
        s1 = self.read("roles/S1.md")

        for text in (readme, roadmap, domain_contracts, coverage, s1):
            self.assertNotIn("#35", text)
            self.assertNotIn("GITHUB_APP_EXECUTOR", text)
            self.assertNotIn("EXECUTOR_PROVENANCE", text)

        self.assertIn("independent S3* audit", readme)
        self.assertIn("independent second agent", roadmap)


if __name__ == "__main__":
    unittest.main()
