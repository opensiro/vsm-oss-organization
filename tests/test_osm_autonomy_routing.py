"""Guard OSM-aware routing without treating draft mandates as active authority."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OSMRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bootstrap = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
        cls.control = (ROOT / "docs" / "AGENT_CONTROL_PLANE.md").read_text(
            encoding="utf-8"
        )
        cls.bootstrap_section = cls.bootstrap.split(
            "## OSM-aware autonomy and delegation routing", 1
        )[1].split("## First-contact control plane", 1)[0]
        cls.control_section = cls.control.split(
            "## OSM-aware delegation and authority transfer", 1
        )[1].split("## Parent S5 decision before assessment", 1)[0]

    def test_bootstrap_is_conditional_and_preserves_authoritative_chain(self):
        for phrase in ("docs/ECOSYSTEM.md", "owning repository @ current default branch",
                       "exact issue / PR / release / pinned artifact"):
            self.assertIn(phrase, self.bootstrap)
        for phrase in ("requests about **transferring decisions",
                       "OSM Roadmap", "S1 domain contracts",
                       "S5 parent authority", "owning issue/PR",
                       "Do not", "grant"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.bootstrap_section)

    def test_owner_first_with_local_discretion_and_residual_escalation(self):
        for phrase in ("function-first", "Local variety/outcome",
                       "Decisive right and owner", "Decide at the correct recursion",
                       "Bounded execution", "Feedback and autonomy evidence",
                       "effective", "current owner"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.control_section)

    def test_no_silent_upstream_admission_or_live_authorization(self):
        for phrase in ("Organization #274", "PROPOSED / NOT ADMITTED",
                       "Upstream #6", "external PR publication decision",
                       "no code/doc change", "stage-specific live authorization"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.control_section.lower())
        for phrase in ("authorize=True", "GitHub login", "proposal digest"):
            self.assertIn(phrase, self.control_section)
        self.assertIn("into an S5 grant", self.bootstrap_section)


if __name__ == "__main__":
    unittest.main()
