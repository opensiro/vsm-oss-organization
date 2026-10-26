"""Upstream admission never activates the exact-stage write handoff."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "docs" / "AGENT_CONTROL_PLANE.md"
BOUNDARY = ROOT / "docs" / "CONTROL_PLANE.md"
GUIDE = ROOT / "CONTRIBUTE_WITH_AI.md"


class UpstreamControlPlaneHandoffTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.control = CONTROL.read_text(encoding="utf-8")
        cls.boundary = BOUNDARY.read_text(encoding="utf-8")
        cls.guide = GUIDE.read_text(encoding="utf-8")
        cls.handoff = cls.control.split(
            "### Control Plane → Upstream preparation handoff (one stage, read-only)", 1
        )[1].split("### Selected contribution execution and outcome", 1)[0]

    def test_menu_and_command_route_to_existing_control_plane(self):
        self.assertIn("| **Prepare Upstream Change** | `prepare upstream contribution` |", self.control)
        self.assertIn("| `prepare upstream contribution` / `prepare upstream contribution <source/issue>` |",
                      self.control)
        self.assertIn("## External upstream contributions", self.control)
        self.assertIn("prepare upstream contribution", self.guide)

    def test_repository_ownership_remains_with_upstream(self):
        for path in ("docs/CONTROL_PLANE_HANDOFF.md", "scripts/control_plane_handoff.py",
                     "scripts/connected_stage_adapter.py", "scripts/batch_proposals.py"):
            with self.subTest(path=path):
                self.assertIn("https://github.com/opensiro/upstream/blob/main/" + path,
                              self.handoff)
        self.assertIn("Upstream #6", self.handoff)
        self.assertIn("Organization #274", self.boundary)

    def test_no_automatic_approval_from_conversation_or_proposal(self):
        for phrase in ("ACTION_PREPARED_NOT_AUTHORIZED", "NOT", "BLOCKED",
                       "Generic `продолжай`", "current-session",
                       "content SHA-256", "selected ID", "not host-connected"):
            with self.subTest(phrase=phrase):
                if phrase == "not host-connected":
                    self.assertIn("not host-connected", self.handoff.lower())
                else:
                    self.assertIn(phrase, self.handoff)
        self.assertIn("No staged permission carries into another stage", self.handoff)
        self.assertIn("before any write", self.handoff)

    def test_stage_limited_and_unavailable_actions_still_stop(self):
        for term in ("prepare_contribution", "create_public_fork",
                     "submit_external_pr", "UPSTREAM_FORK_TOKEN", "create_fork.py --execute",
                     "matching fork and push rights", "40-hex base SHA"):
            with self.subTest(term=term):
                self.assertIn(term, self.handoff)
        self.assertIn("current", self.handoff)
        self.assertIn("does not activate this live write stage", self.handoff)
        self.assertNotIn("active writer", self.boundary.lower())

    def test_source_of_truth_not_duplicated_as_local_executor(self):
        self.assertIn("no external execution permission", self.boundary)
        self.assertIn("Upstream #6 owns", self.boundary)
        self.assertIn("Organization #274", self.boundary)
        self.assertIn("not a second interface", self.handoff.lower())


if __name__ == "__main__":
    unittest.main()
