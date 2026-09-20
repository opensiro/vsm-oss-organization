from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AutonomousWorkReportingTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_reporting_contract_preserves_snapshot_and_stop_rule(self) -> None:
        contract = self.read("AUTONOMOUS_WORK_REPORTING.md")

        for marker in ("DONE", "NOW", "BLOCKED", "NEXT", "NEED YOU"):
            self.assertIn(marker, contract)

        self.assertIn("one or two obvious downstream steps", contract)
        self.assertIn("branch → PR → CI → fix → merge", contract)
        self.assertIn("NEED YOU = none", contract)
        self.assertIn("Do not silently turn a finished task into an indefinitely expanding", contract)

    def test_common_entry_exposes_reporting_contract(self) -> None:
        entry = self.read("CONTRIBUTOR_START.md")

        self.assertIn("## Autonomous work reporting", entry)
        self.assertIn("AUTONOMOUS_WORK_REPORTING.md", entry)
        for marker in ("DONE", "NOW", "BLOCKED", "NEXT", "NEED YOU"):
            self.assertIn(marker, entry)
        self.assertIn("does not create a VSM function", entry)


if __name__ == "__main__":
    unittest.main()
