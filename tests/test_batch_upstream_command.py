"""Ensure the Control Plane dispatches a real Upstream batch without granting publication."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "docs" / "AGENT_CONTROL_PLANE.md"


class BatchUpstreamCommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = CONTROL.read_text(encoding="utf-8")
        cls.batch = cls.document.split(
            "### Batch Upstream — assessment-first technical contribution", 1
        )[1].split("### S1 function test — Upstream Contributions", 1)[0]

    def test_menu_and_dispatch_have_distinct_execution_route(self):
        self.assertIn("| **Batch Upstream** | `batch upstream` |", self.document)
        self.assertIn("| `batch upstream` / `start an upstream batch`", self.document)
        self.assertIn("**Command:** `batch upstream`", self.batch)
        for distinct in (
            "contribute to other harnesses",
            "start a batch assessment",
            "test S1 function: upstream contributions",
            "Upstream #56",
        ):
            with self.subTest(distinct=distinct):
                self.assertIn(distinct, self.document)

    def test_frozen_index_and_parallel_process_protection(self):
        for contract in (
            "five distinct included assessment records",
            "pin one exact Index commit",
            "open concurrent batch PRs/branches",
            "occupied sources",
            "serially",
            "need",
            "mechanism",
            "counterfactual",
            "scope",
            "native deterministic first-party tests",
            "scripts/assessment_candidate_batches.py validate",
            "NO_ELIGIBLE_ASSESSMENT_CANDIDATE",
        ):
            with self.subTest(contract=contract):
                self.assertIn(contract, self.batch)

    def test_external_decision_rights_remain_unchanged(self):
        for boundary in (
            "AWAITING_EXTERNAL",
            "BLOCKED_EVIDENCE",
            "CLOSED_NO_CHANGE",
            "effective stage-specific mandates",
            "finite 34-case Corrective publication mandate",
            "not external delivery",
            "Do not silently edit `TODO.md`",
        ):
            with self.subTest(boundary=boundary):
                self.assertIn(boundary, self.batch)


if __name__ == "__main__":
    unittest.main()
