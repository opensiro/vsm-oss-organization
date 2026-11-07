"""Upstream Auto must not be mistaken for the Organization S2 scheduler."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MENU = (ROOT / "docs" / "AGENT_CONTROL_PLANE.md").read_text(encoding="utf-8")


class UpstreamAutoCommandTests(unittest.TestCase):
    def test_operator_namespace_and_owner(self):
        for phrase in (
            "| **Upstream Auto (preview)** | `upstream auto status` |",
            "| `upstream auto status` | — |",
            "| `upstream auto` / `upstream auto resume` | — |",
            "https://github.com/opensiro/upstream/issues/161",
            "docs/UPSTREAM_AUTO.md",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, MENU)

    def test_no_implicit_s2_or_executor_rights(self):
        for phrase in (
            "NOT_IMPLEMENTED_EXECUTOR",
            "NOT_IMPLEMENTED_TASK_CLAIM",
            "Local Upstream coordination is not Organization M4 S2",
            "does not assert `S2=C/A`",
            "read-only preview",
            "effective stage grants",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, MENU)


if __name__ == "__main__":
    unittest.main()
