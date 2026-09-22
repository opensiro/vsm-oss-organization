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
        self.assertIn("TODO.md", contract)
        self.assertIn("TODO reconciliation", contract)

    def test_common_entry_exposes_reporting_contract(self) -> None:
        entry = self.read("CONTRIBUTOR_START.md")

        self.assertIn("## Autonomous work reporting", entry)
        self.assertIn("AUTONOMOUS_WORK_REPORTING.md", entry)
        for marker in ("DONE", "NOW", "BLOCKED", "NEXT", "NEED YOU"):
            self.assertIn(marker, entry)
        self.assertIn("does not create a VSM function", entry)

    def test_common_entry_exposes_current_work_bootstrap(self) -> None:
        entry = self.read("CONTRIBUTOR_START.md")
        root_readme = self.read("README.md")
        todo = self.read("TODO.md")

        self.assertIn("TODO.md", entry)
        self.assertIn("TODO.md", root_readme)
        self.assertIn("Temporary bootstrap surface", todo)
        self.assertIn("GitHub Project", todo)
        self.assertIn("#125", todo)
        for state in ("# NOW", "# NEXT", "# BLOCKED", "# WATCH", "# LATER"):
            self.assertIn(state, todo)
        for repository in (
            "opensiro/vsm-harness-profile",
            "opensiro/vsm-harness-skills",
            "opensiro/vsm-harness-index",
            "opensiro/awesome-vsm-harness",
            "opensiro/vsm-oss-organization",
        ):
            self.assertIn(repository, todo)


if __name__ == "__main__":
    unittest.main()
