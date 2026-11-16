"""Fork-local Upstream commands route to existing Organization control, not a new scheduler."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONTROL = (ROOT / "docs" / "AGENT_CONTROL_PLANE.md").read_text(encoding="utf-8")
GUIDE = (ROOT / "CONTRIBUTE_WITH_AI.md").read_text(encoding="utf-8")

class UpstreamCommandNamespaceTests(unittest.TestCase):
    def test_current_operator_commands_are_fork_local(self):
        menu = CONTROL.split("| Visible action |", 1)[1].split("**Current Upstream S1 command namespace.**", 1)[0]
        for label, command in (
            ("Upstream Upgrade", "upstream upgrade"),
            ("Upstream Discover", "upstream discover"),
            ("Upstream Continue", "upstream continue <harness>"),
            ("Upstream Status", "upstream status"),
        ):
            with self.subTest(label=label):
                self.assertIn(f"| **{label}** | `{command}` |", menu)
        for old in ("Upstream Batch", "Upstream Upgrade Batch", "Upstream Auto", "Upstream Outcomes"):
            self.assertNotIn(f"| **{old}** |", menu)

    def test_fork_local_human_controls_and_progress_are_visible(self):
        for phrase in (".opensiro/", "opensiro/meta", "PAUSE/STOP/RESUME", "UNKNOWN", "migration"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), CONTROL.lower())
        self.assertIn("upstream continue <harness>", CONTROL)
        self.assertIn("full engineering cycle", CONTROL)
        self.assertIn("never a research-only shortlist", CONTROL)
        self.assertIn("ONE original harness", CONTROL)
        self.assertIn("review PR in `opensiro-contributions`", CONTROL)
        self.assertIn("do not move to another source", CONTROL)
        self.assertIn("separate exact current-conversation owner approval", CONTROL)
        self.assertIn("read-only draft", CONTROL)
        self.assertIn("The later third-party PR has its own consent gate", CONTROL)
        self.assertNotIn("| **Upstream Continue** | `upstream continue <issue URL>` |", CONTROL)

    def test_upgrade_disclosure_requires_five_contributions_links(self):
        for phrase in (
            "Mandatory Upstream Upgrade PR-link preflight",
            "five real clickable links",
            "working repository",
            "product branch",
            "exact implementation commit",
            "existing fork-local review PR",
            "pinned `.opensiro/contributions/<stable-id>.json`",
            "proposed external PR body's AI-assisted disclosure",
            "NOT_CREATED",
            "do not publish a new external PR missing its real review link",
        ):
            self.assertIn(phrase, CONTROL)

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
