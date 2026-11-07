"""Upstream S1 commands stay discoverable and distinct from adjacent owners."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "docs" / "AGENT_CONTROL_PLANE.md"
GUIDE = ROOT / "CONTRIBUTE_WITH_AI.md"


class UpstreamCommandNamespaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.control = CONTROL.read_text(encoding="utf-8")
        cls.guide = GUIDE.read_text(encoding="utf-8")

    def test_preferred_commands_are_routed_to_existing_upstream_owners(self):
        for preferred, legacy in (
            ("upstream discover", "contribute to other harnesses"),
            ("upstream prepare", "prepare upstream contribution"),
            ("upstream batch", "batch upstream"),
            ("upstream status", "show harness contribution status"),
            ("upstream outcomes", "verify upstream outcomes"),
            ("upstream s1 test", "test S1 function: upstream contributions"),
        ):
            with self.subTest(preferred=preferred):
                self.assertIn(f"| `{preferred}` | `{legacy}` |", self.control)
                if preferred == "upstream discover":
                    self.assertIn("\nupstream discover\n", self.guide)
                else:
                    self.assertIn(f"`{preferred}`", self.guide)

    def test_namespace_does_not_reassign_organization_or_index_work(self):
        self.assertIn("**Upstream S1 command namespace.**", self.control)
        self.assertIn("not new technical authority or a new", self.control)
        self.assertIn("**Adjacent, not Upstream S1 execution:** `batch upgrade`", self.control)
        self.assertIn("Index `batch status`/`batch reconcile`", self.control)
        self.assertIn("`upstream outcomes`", self.control)
        self.assertIn("`batch upgrade` command is an Organization-owned", self.guide)

    def test_no_external_publication_right_or_automatic_kpi(self):
        self.assertIn("External publication remains separately authorized", self.control)
        self.assertIn("not an automatic Organization KPI", self.control)
        self.assertIn("no branch, fork, PR or human approval implied", self.control)
        self.assertIn("Tracking is **off by default**", self.guide)


if __name__ == "__main__":
    unittest.main()
