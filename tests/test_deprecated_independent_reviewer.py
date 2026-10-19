"""Regression boundary for deprecated Independent Reviewer prototypes.

Only the active navigation/placement policy is tested. Archived snapshot scripts are
historical data and intentionally not imported or executed.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "deprecated" / "independent-reviewer"


class DeprecatedReviewerPlacementTest(unittest.TestCase):
    def test_archive_is_explicit(self):
        readme = (ARCHIVE / "README.md").read_text(encoding="utf-8")
        self.assertIn("DEPRECATED", readme)
        self.assertIn("NOT DEPLOYED", readme)
        self.assertIn("not silently satisfied", readme)

    def test_proposals_preserved_but_not_activated(self):
        snapshots = (
            "pr-198/contracts/s3star/index-review-handoff.md",
            "pr-198/scripts/check_index_reviewer_handoff.py",
            "pr-198/tests/test_index_reviewer_handoff.py",
            "pr-215/docs/INDEPENDENT_REVIEWER_BATCH_HYPOTHESIS.md.txt",
        )
        for item in snapshots:
            with self.subTest(item=item):
                self.assertTrue((ARCHIVE / item).is_file())
        active = (
            "contracts/s3star/index-review-handoff.md",
            "scripts/check_index_reviewer_handoff.py",
            "tests/test_index_reviewer_handoff.py",
            "docs/INDEPENDENT_REVIEWER_BATCH_HYPOTHESIS.md",
        )
        for item in active:
            with self.subTest(item=item):
                self.assertFalse((ROOT / item).exists())

    def test_current_control_plane_distinguishes_audit(self):
        text = (ROOT / "docs/AGENT_CONTROL_PLANE.md").read_text(encoding="utf-8")
        self.assertIn("## Deprecated Independent Reviewer experiment", text)
        self.assertIn("No second GitHub account", text)
        self.assertIn("not deprecated", text.lower())


if __name__ == "__main__":
    unittest.main()
