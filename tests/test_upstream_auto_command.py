"""Upstream Auto must not be mistaken for the Organization S2 scheduler."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MENU = (ROOT / "docs" / "AGENT_CONTROL_PLANE.md").read_text(encoding="utf-8")


class UpstreamAutoCommandTests(unittest.TestCase):
    def test_operator_namespace_and_owner(self):
        for phrase in (
            "| **Upstream Auto** | `upstream auto` |",
            "| `upstream auto status` | — |",
            "| `upstream auto` / `upstream auto resume` | — |",
            "https://github.com/opensiro/upstream/issues/161",
            "docs/UPSTREAM_AUTO.md",
            "scripts/upstream_auto.py",
            "| **Upstream Auto Batch** | `upstream auto batch` |",
            "| `upstream auto batch` | — |",
            "| `upstream auto batch` | Apply the **same** live Upstream #161",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, MENU)

    def test_no_implicit_s2_or_executor_rights(self):
        for phrase in (
            "one bounded agent-coupled task",
            "dedicated Upstream CAS ref",
            "stale claims are not stolen",
            "Organization M4 `S2=A`",
            "read-only preview",
            "effective reservation/authentication mechanism",
            "task-specific S1 admission",
            "`PARTIAL` is a valid outcome",
            "atomic multi-task Git CAS",
            "each actor's own claim",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, MENU)


if __name__ == "__main__":
    unittest.main()
