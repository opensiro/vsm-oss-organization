"""Contract smoke tests for the external OSS contribution control-plane entry."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "docs" / "AGENT_CONTROL_PLANE.md"
HUMAN = ROOT / "CONTRIBUTE_WITH_AI.md"


class ExternalContributionCommandTests(unittest.TestCase):
    def setUp(self):
        self.control = CONTROL.read_text(encoding="utf-8")
        self.human = HUMAN.read_text(encoding="utf-8")
        self.command = self.control.split("## External upstream contributions", 1)[1].split(
            "## Per-command operating loop", 1
        )[0]

    def test_discovery_command_is_exposed_from_both_entries(self):
        self.assertIn("`contribute to other harnesses`", self.control)
        self.assertIn("contribute to other harnesses", self.human)
        self.assertIn("docs/AGENT_CONTROL_PLANE.md#external-upstream-contributions", self.human)
        for field in ("first-party evidence URL", "existing open PRs", "5-10 eligible harnesses",
                      "CONTRIBUTING", "licensing/CLA", "speculative"):
            self.assertIn(field, self.command)

    def test_tracking_requires_explicit_user_choice_and_is_nonblocking(self):
        for clause in ("**Default: OFF.**", "**One-time scan:**", "**Ongoing monitoring:**",
                       "**Storage and revocation:**", "If declined or unanswered",
                       "separate explicit publication decision"):
            self.assertIn(clause, self.command)
        self.assertIn("Do not infer permission", self.command)
        self.assertIn("requires a separate affirmative choice", self.command)
        self.assertIn("The contributor may provide PR links voluntarily", self.command)

    def test_external_owner_and_experimental_ledger_boundary(self):
        for clause in ("outside the bounded Organization S1 scheduler",
                       "upstream as the **system-in-focus**",
                       "product_native_fit=pass", "observations.json", "snapshot.json",
                       "not an upstream need", "**not required**"):
            self.assertIn(clause, self.command)
        self.assertIn("Do not create forks, branches, PRs", self.command)


if __name__ == "__main__":
    unittest.main()
