"""Legacy Upstream Auto remains historical; it cannot become a second S2 scheduler."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MENU = (ROOT / "docs" / "AGENT_CONTROL_PLANE.md").read_text(encoding="utf-8")

class UpstreamAutoCommandTests(unittest.TestCase):
    def test_legacy_auto_retains_correct_predecessor_owner(self):
        self.assertIn("## Current Upstream v0.12.0", MENU)
        self.assertIn("upstream-old/issues/161", MENU)
        self.assertIn("docs/UPSTREAM_AUTO.md", MENU)
        self.assertIn("scripts/upstream_auto.py", MENU)
        self.assertIn("**Legacy:**", MENU)
        self.assertNotIn("| **Upstream Auto** | `upstream auto` |", MENU)
        self.assertNotIn("| **Upstream Auto Batch** | `upstream auto batch` |", MENU)

    def test_no_implicit_s2_or_executor_rights(self):
        self.assertIn("The Organization continues to own the global work selection", MENU)
        self.assertIn("No new autonomous runtime or S1 grade is implied", MENU)
        self.assertIn("current-conversation exact owner consent", MENU)
        self.assertIn("No Organization", MENU)
        self.assertIn("not a daemon", MENU.lower())

if __name__ == "__main__":
    unittest.main()
