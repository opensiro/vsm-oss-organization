from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AutonomousWorkReportingTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_reporting_contract_preserves_snapshot_and_stop_rule(self) -> None:
        contract = self.read("docs/AUTONOMOUS_WORK_REPORTING.md")
        for marker in ("DONE", "NOW", "BLOCKED", "NEXT", "NEED YOU"):
            self.assertIn(marker, contract)
        self.assertIn("one or two obvious downstream steps", contract)
        self.assertIn("branch → PR → CI → fix → merge", contract)
        self.assertIn("NEED YOU = none", contract)
        self.assertIn("Do not silently turn a finished task into an indefinitely expanding", contract)
        self.assertIn("TODO.md", contract)
        self.assertIn("Scheduler reconciliation", contract)
        self.assertIn("not by itself an algedonic signal", contract)

    def test_status_command_uses_existing_compact_reporting_without_extra_queue(self) -> None:
        control = self.read("docs/AGENT_CONTROL_PLANE.md")
        reporting = self.read("docs/AUTONOMOUS_WORK_REPORTING.md")
        section = control.split("## Default `status` answer (compact, read-only)", 1)[1].split(
            "## Maintainer commands", 1
        )[0]
        for marker in (
            "NOW / BLOCKED / NEXT",
            "AUTONOMOUS_WORK_REPORTING.md",
            "no current scheduled item",
            "TODO.md",
            "unverified",
            "NEED YOU",
            "DONE",
            "suggestion",
            "no new scheduler",
        ):
            self.assertIn(marker, section)
        for marker in ("DONE", "NOW", "BLOCKED", "NEXT", "NEED YOU"):
            self.assertIn(marker, reporting)
        self.assertIn("#default-status-answer-compact-read-only", control)

    def test_common_entry_exposes_reporting_contract(self) -> None:
        entry = self.read("CONTRIBUTOR_START.md")
        self.assertIn("## Autonomous work reporting", entry)
        self.assertIn("docs/AUTONOMOUS_WORK_REPORTING.md", entry)
        for marker in ("DONE", "NOW", "BLOCKED", "NEXT", "NEED YOU"):
            self.assertIn(marker, entry)
        self.assertIn("does not create a VSM function", entry)
        self.assertIn("TODO.md", entry)

    def test_control_plane_owns_lifecycle_boundary(self) -> None:
        control = self.read("docs/CONTROL_PLANE.md")
        todo = self.read("TODO.md")
        root_readme = self.read("README.md")
        for marker in ("GitHub milestone", "GitHub issue", "TODO.md", "S1 execution", "Metasystem execution", "Optional projection"):
            self.assertIn(marker, control)
        self.assertIn("## NOW", todo)
        self.assertIn("## NEXT", todo)
        self.assertIn("## BLOCKED", todo)
        self.assertNotIn("## WATCH", todo)
        self.assertNotIn("## LATER", todo)
        self.assertIn("Git-native scheduler", root_readme)
        self.assertIn("docs/CONTROL_PLANE.md", root_readme)


if __name__ == "__main__":
    unittest.main()
