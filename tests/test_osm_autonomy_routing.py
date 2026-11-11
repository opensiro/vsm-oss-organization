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

    def test_new_standing_publication_still_requires_effective_source_gates(self):
        # Distinct parent decisions: S1 admission did not grant writes; the
        # later publication mandate did, but is not an executor or grade.
        for phrase in ("separately delegated standing external-PR publication",
                       "current Upstream policy", "per-PR owner conversation",
                       "before** exercising new rights", "provider capabilities",
                       "No permission override or autonomy grade"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.control_section.lower())
        for phrase in ("authorize=True", "GitHub login", "proposal digest"):
            self.assertIn(phrase, self.control_section)
        self.assertIn("into an S5 grant", self.bootstrap_section)

    def test_upstream_local_grant_is_distinct_from_s5_domain(self):
        self.assertIn("repository/fork owner", self.control_section)
        self.assertIn("different rights", self.control_section)
        self.assertIn("#274", self.control_section)
        self.assertIn("S1 admission alone", self.control_section)



if __name__ == "__main__":
    unittest.main()
