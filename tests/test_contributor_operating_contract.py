from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ContributorOperatingContractTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_contributing_defines_bounded_autonomous_run(self) -> None:
        contributing = self.read("CONTRIBUTING.md")

        self.assertIn("## Autonomous progress and owner observability", contributing)
        self.assertIn("one or two obvious downstream steps", contributing)
        self.assertIn("branch → PR → CI → fix → merge", contributing)
        self.assertIn("stop before opening a new independent research/program of work", contributing)

    def test_owner_snapshot_is_explicit_and_non_blocking(self) -> None:
        contributing = self.read("CONTRIBUTING.md")

        for marker in ("DONE", "NOW", "BLOCKED", "NEXT", "NEED YOU"):
            self.assertIn(marker, contributing)

        self.assertIn("If `NEED YOU = none`", contributing)
        self.assertIn("do not manufacture an approval request", contributing)

    def test_observability_contract_does_not_create_vsm_evidence(self) -> None:
        contributing = self.read("CONTRIBUTING.md")
        entry = self.read("CONTRIBUTOR_START.md")

        self.assertIn("does not establish S2, S3, S3*, S4, S5", contributing)
        self.assertIn("This is a contributor observability convention", entry)
        self.assertIn("Autonomous progress and owner observability", entry)
        self.assertIn("NEED YOU", entry)


if __name__ == "__main__":
    unittest.main()
