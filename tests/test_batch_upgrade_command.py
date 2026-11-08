"""Guard two Upstream technical batch commands and the retired Organization intake."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MENU = ROOT / "docs" / "AGENT_CONTROL_PLANE.md"
HISTORY = ROOT / "docs" / "BATCH_UPGRADE.md"
CONTROL = ROOT / "docs" / "CONTROL_PLANE.md"
GUIDE = ROOT / "CONTRIBUTE_WITH_AI.md"


class BatchUpgradeCommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menu = MENU.read_text(encoding="utf-8")
        cls.history = HISTORY.read_text(encoding="utf-8")
        cls.control = CONTROL.read_text(encoding="utf-8")
        cls.guide = GUIDE.read_text(encoding="utf-8")
        cls.dispatch = cls.menu.split(
            "### Upstream Upgrade Batch — strict assessment-derived improvement", 1
        )[1].split("### Upstream status —", 1)[0]

    def test_exactly_two_technical_batch_routes_not_old_third_command(self):
        self.assertIn("| **Upstream Batch** | `upstream batch` |", self.menu)
        self.assertIn("| **Upstream Upgrade Batch** | `upstream upgrade batch` |", self.menu)
        self.assertNotIn("| **Batch Upgrade** | `batch upgrade` |", self.menu)
        self.assertNotIn("| `batch upgrade` |", self.menu)
        self.assertIn("**Command:** `upstream upgrade batch`", self.dispatch)
        self.assertIn("historical rationale", self.control)
        self.assertIn("not a third active command", self.guide)
        self.assertIn("not an active third command", self.history)

    def test_both_modes_find_vsm_hypotheses_but_derived_origin_is_strict(self):
        for phrase in (
            "Both this mode and `upstream batch` search possible",
            "pre-register",
            "before fresh first-party code/issue inspection",
            "ASSESSMENT_DERIVED",
            "ASSESSMENT_INFORMED",
            "need / mechanism / counterfactual / scope",
            "distinct deterministic CI/runner",
            "BLOCKED_INDEPENDENT_EXECUTION",
            "five distinct",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.dispatch.lower())

    def test_no_new_queue_grade_or_publication_authority(self):
        for phrase in (
            "Upstream #56",
            "source-disjoint",
            "NO_ELIGIBLE_ASSESSMENT_CANDIDATE",
            "CLOSED_NO_CHANGE",
            "external publication grants",
            "No Organization",
            "No Organization `TODO.md` scheduler entry",
            "C` function need not become `A`",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.dispatch.lower())
        self.assertIn("original intake rationale", self.history.lower())
        self.assertIn("External publication", self.control)


if __name__ == "__main__":
    unittest.main()
