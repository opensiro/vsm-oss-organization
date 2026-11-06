"""Keep prospective M4/S2 design separated from deployed Organization work."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class S2CandidateDocumentTests(unittest.TestCase):
    def test_prospective_status_and_authority_boundary(self):
        s = (ROOT / "docs/S2_CROSS_S1_CONSISTENCY_COORDINATOR.md").read_text(encoding="utf-8")
        for phrase in ("NOT DEPLOYED", "NOT S2 EVIDENCE", "Index S1", "Awesome S1",
                       "S3", "S5", "TODO.md", "M3", "NOT_QUALIFIED_LOCAL", "INSUFFICIENT"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, s)

    def test_template_not_a_runtime_receipt(self):
        s = (ROOT / "templates/s2-cross-s1-collision.md").read_text(encoding="utf-8")
        for phrase in ("TEMPLATE ONLY", "NOT S2 EVIDENCE", "Index", "Awesome", "head SHA",
                       "Decision owner", "Return", "INSUFFICIENT"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, s)

    def test_roadmap_and_docs_link_candidate(self):
        for path in ("docs/ROADMAP.md", "docs/README.md"):
            with self.subTest(path=path):
                self.assertIn("S2_CROSS_S1_CONSISTENCY_COORDINATOR.md",
                              (ROOT / path).read_text(encoding="utf-8"))

    def test_current_work_not_changed(self):
        current = (ROOT / "TODO.md").read_text(encoding="utf-8")
        self.assertNotIn("S2_CROSS_S1_CONSISTENCY_COORDINATOR", current)

if __name__ == "__main__":
    unittest.main()
