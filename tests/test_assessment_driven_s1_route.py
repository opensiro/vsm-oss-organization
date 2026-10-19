"""Keep the S1 Upstream test assessment-derived, without widening GitHub authority."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "docs" / "AGENT_CONTROL_PLANE.md"


class AssessmentDrivenS1RouteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = CONTROL.read_text(encoding="utf-8")
        cls.test_route = cls.document.split(
            "### S1 function test — Upstream Contributions (candidate, not admitted)", 1
        )[1].split("### Discovery and the offered list", 1)[0]
        cls.generic = cls.document.split(
            "## External upstream contributions", 1
        )[1].split("### S1 function test", 1)[0]

    def test_menu_keeps_command_mapped_to_assessment_first_route(self):
        self.assertIn(
            "| **S1 Function Test (Upstream)** | `test S1 function: upstream contributions` |",
            self.document,
        )
        self.assertIn("**Assessment-driven**", self.document)
        self.assertIn("docs/ASSESSMENT_DRIVEN_S1_TEST.md", self.document)

    def test_test_originates_in_index_not_arbitrary_upstream_issue(self):
        for phrase in (
            "Its starting point is the assessment", 
            "canonical OpenSiro Index assessments",
            "Index commit SHA",
            "assessment path at exact Index commit SHA", 
            "assessed system identity",
            "Index assessment → harness/finding → evidence → proposed change → tests",
            "NO_ELIGIBLE_ASSESSMENT_CANDIDATE",
            "BLOCKED_EVIDENCE",
            "Do not preselect Cognee",
            "no silent project substitution",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.test_route)

    def test_low_grade_and_non_native_fit_cannot_pass(self):
        for phrase in (
            "does not prove a software bug", 
            "counterfactual",
            "source-backed upstream need", 
            "a low VSM grade", 
            "generic issue hunting",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.test_route.lower())

    def test_test_is_not_live_permission_or_formal_s1_admission(self):
        for phrase in (
            "PROPOSED / NOT ADMITTED",
            "read-only",
            "Upstream #6",
            "Organization #274",
            "old fork does not prove",
            "stage",
            "consent", 
            "No `S1=A`",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.test_route.lower())

    def test_generic_discovery_is_preserved_as_distinct_command(self):
        self.assertIn("`contribute to other harnesses`", self.generic)
        self.assertIn("opt-in contribution-discovery", self.generic)
        self.assertIn("candidate-discovery inputs **only**", self.generic)
        self.assertIn("still provides general OSS discovery", self.test_route)


if __name__ == "__main__":
    unittest.main()
