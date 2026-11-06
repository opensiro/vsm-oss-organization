"""Contract checks for the owner-routed read-only Upstream status command."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "AGENT_CONTROL_PLANE.md"


class UpstreamStatusCommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = DOC.read_text(encoding="utf-8")

    def test_first_contact_menu_and_typed_route(self):
        self.assertIn("| **Upstream Status** | `upstream status` |", self.content)
        self.assertIn("| `upstream status` / `show harness contribution status` |", self.content)
        self.assertIn("### Upstream status — joined harness/intervention/PR inventory", self.content)

    def test_owner_and_non_authorizing_boundary(self):
        self.assertIn("opensiro/upstream/blob/main/HARNESS_STATUS.md", self.content)
        self.assertIn("python3 scripts/harness_status.py --check", self.content)
        self.assertIn("harness → independent intervention → external PR(s)", self.content)
        self.assertIn("does not publish third-party PRs", self.content)


if __name__ == "__main__":
    unittest.main()
