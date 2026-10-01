from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AutonomousS1ModeTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_bootstrap_routes_to_supported_s1_mode(self) -> None:
        start = self.read("START_HERE.md")
        contributor = self.read("CONTRIBUTOR_START.md")
        mode = self.read("modes/s1-autonomous/README.md")

        self.assertIn("modes/s1-autonomous/", start)
        self.assertIn("modes/s1-autonomous/README.md", contributor)
        self.assertIn("RUN.md", mode)
        self.assertIn("contracts/s1/domain-contracts.md", mode)
        self.assertIn("roles/S1.md", mode)

    def test_mode_does_not_claim_grade_from_construction(self) -> None:
        mode = self.read("modes/s1-autonomous/README.md")
        run = self.read("modes/s1-autonomous/RUN.md")
        records = self.read("records/s1/runs/README.md")

        self.assertIn("an autonomy grade by itself", mode.lower())
        self.assertIn("Positive `S1=A` interpretation still requires", mode)
        self.assertIn("Do not infer `S1=A` inside the run", run)
        self.assertIn("not autonomy grades", records)

    def test_mode_requires_direct_boundary_reachability(self) -> None:
        mode = self.read("modes/s1-autonomous/README.md")
        run = self.read("modes/s1-autonomous/RUN.md")

        self.assertIn("no developer-specific code, prompt assembly, authority wiring", mode)
        self.assertIn("custom composition", mode)
        self.assertIn("boundary-reachability", run)

    def test_run_separates_decision_ownership_from_support(self) -> None:
        run = self.read("modes/s1-autonomous/RUN.md")
        template = self.read("templates/s1-autonomous-run.md")

        self.assertIn("Separate support from ownership", run)
        self.assertIn("Agent-owned decisions", template)
        self.assertIn("Human interventions", template)
        self.assertIn("Runtime / support machinery", template)

    def test_schema_requires_ownership_intervention_and_terminal_evidence(self) -> None:
        schema = json.loads(self.read("schemas/s1-autonomous-run.schema.json"))
        required = set(schema["required"])

        for field in (
            "boundary_reachability",
            "runtime_support",
            "agent_owned_decisions",
            "human_interventions",
            "disturbances_and_recovery",
            "validation",
            "terminal_state",
            "artifacts",
        ):
            self.assertIn(field, required)

        self.assertEqual(
            set(schema["properties"]["terminal_state"]["enum"]),
            {"CLOSED_CHANGE", "CLOSED_NO_CHANGE", "ESCALATED", "NON_ADMITTED"},
        )
        self.assertEqual(
            set(schema["properties"]["domain"]["enum"]),
            {"Index", "Skills", "Awesome"},
        )

    def test_human_merge_may_remain_separate_from_s1_closure(self) -> None:
        mode = self.read("modes/s1-autonomous/README.md")
        run = self.read("modes/s1-autonomous/RUN.md")

        self.assertIn("Human merge/rejection", mode)
        self.assertIn("Protected/default-branch integration may remain human-owned", run)


if __name__ == "__main__":
    unittest.main()
