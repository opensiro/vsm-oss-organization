"""Guard the read-only VSM ownership-improvement intake route."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MENU = ROOT / "docs" / "AGENT_CONTROL_PLANE.md"
ROUTE = ROOT / "docs" / "BATCH_UPGRADE.md"
CONTROL = ROOT / "docs" / "CONTROL_PLANE.md"


class BatchUpgradeCommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menu = MENU.read_text(encoding="utf-8")
        cls.route = ROUTE.read_text(encoding="utf-8")
        cls.control = CONTROL.read_text(encoding="utf-8")
        cls.dispatch = cls.menu.split(
            "### Batch Upgrade — function and ownership improvement intake", 1
        )[1].split("### S1 function test — Upstream Contributions", 1)[0]

    def test_command_is_discoverable_and_distinct(self):
        self.assertIn("| **Batch Upgrade** | `batch upgrade` |", self.menu)
        self.assertIn("| `batch upgrade` |", self.menu)
        self.assertIn("**Command:** `batch upgrade`", self.dispatch)
        self.assertIn("BATCH_UPGRADE.md", self.menu)
        self.assertIn("BATCH_UPGRADE.md", self.control)
        self.assertIn("`batch upstream`", self.dispatch)
        self.assertIn("`start a batch assessment`", self.route)

    def test_intake_is_not_an_implicit_executor(self):
        for phrase in (
            "read-only",
            "separately reviewed Upstream-owned contract",
            "does not implement, allocate or publish",
            "parallel operators",
            "a scheduler item",
            "TODO.md",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.route)

    def test_grade_remains_an_independent_ownership_observation(self):
        for phrase in (
            "Neither state is a maturity rank or performance score",
            "first-party decision owner",
            "feedback closure",
            "decisive function-specific right",
            "C → A",
            "A` is not presumed",
            "new source ref",
            "edit historical frozen vectors",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.route)

    def test_sources_and_negative_outcomes_are_explicit(self):
        for phrase in (
            "exact Index SHA",
            "review_ref",
            "need",
            "mechanism",
            "counterfactual",
            "scope",
            "UPGRADE_PROPOSAL",
            "NOT_PRODUCT_FIT",
            "BLOCKED_EVIDENCE",
            "NO_ELIGIBLE_ASSESSMENT_CANDIDATE",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.route)

    def test_rights_native_validation_and_ownership_boundaries(self):
        for phrase in (
            "Upstream #56",
            "Skills autonomy states",
            "Index",
            "native-only",
            "deterministic tests",
            "external publication mandate",
            "external repository's maintainer",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.route)


if __name__ == "__main__":
    unittest.main()
