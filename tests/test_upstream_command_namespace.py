"""Case-first Upstream commands route to existing Organization control, not a new scheduler."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONTROL = (ROOT / "docs" / "AGENT_CONTROL_PLANE.md").read_text(encoding="utf-8")
GUIDE = (ROOT / "CONTRIBUTE_WITH_AI.md").read_text(encoding="utf-8")

class UpstreamCommandNamespaceTests(unittest.TestCase):
    def test_current_operator_commands_are_exactly_case_first(self):
        menu = CONTROL.split("| Visible action |", 1)[1].split("**Current Upstream S1 command namespace.**", 1)[0]
        for label, command in (
            ("Upstream Discover", "upstream discover"),
            ("Upstream Continue", "upstream continue <issue URL>"),
            ("Upstream Status", "upstream status"),
        ):
            with self.subTest(label=label):
                self.assertIn(f"| **{label}** | `{command}` |", menu)
        for old in ("Upstream Batch", "Upstream Upgrade Batch", "Upstream Auto", "Upstream Outcomes"):
            self.assertNotIn(f"| **{old}** |", menu)

    def test_old_routes_keep_real_history_not_new_authority(self):
        self.assertIn("upstream-old/issues/56", CONTROL)
        self.assertIn("upstream-old/issues/161", CONTROL)
        self.assertIn("Predecessor-only documentation", CONTROL)
        self.assertIn("not an installed CLI or background executor", CONTROL)
        self.assertIn("Organization continues to own the global work selection", CONTROL)
        self.assertIn("Index `batch status`", CONTROL)

    def test_no_external_publication_right_or_automatic_kpi(self):
        self.assertIn("current-conversation exact owner consent", CONTROL)
        self.assertIn("the historic accepted-outcomes exporter is", CONTROL.lower())
        self.assertIn("new-source live metrics stay unclaimed", CONTROL)
        self.assertIn("Tracking is **off by default**", GUIDE)

if __name__ == "__main__":
    unittest.main()
