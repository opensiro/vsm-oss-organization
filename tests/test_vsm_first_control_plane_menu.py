"""Contract checks for VSM-first Control Plane navigation and S1 subgroups."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MENU = ROOT / "docs" / "AGENT_CONTROL_PLANE.md"
BOOTSTRAP = ROOT / "START_HERE.md"


class VsmFirstControlPlaneMenuTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        menu = MENU.read_text(encoding="utf-8")
        cls.hierarchy = menu.split(
            "### VSM-first action-menu hierarchy (presentation only)", 1
        )[1].split("**Exact first-contact command map", 1)[0]
        cls.menu = menu
        cls.bootstrap = BOOTSTRAP.read_text(encoding="utf-8")

    def test_group_order_and_four_explicit_s1_subgroups(self):
        groups = (
            "**System Overview",
            "**S1 · Operations",
            "**S2 · Coordination**",
            "**S3 · Current Control**",
            "**S3* · Complementary Audit**",
            "**S4 · Adaptation**",
            "**S5 · Policy & Identity**",
        )
        positions = [self.hierarchy.index(group) for group in groups]
        self.assertEqual(sorted(positions), positions)

        domains = (
            "**Index** (\`opensiro/vsm-harness-index\`)",
            "**Skills** (\`opensiro/vsm-harness-skills\`)",
            "**Awesome** (\`opensiro/awesome-vsm-harness\`)",
            "**Upstream Contributions** (\`opensiro/upstream\`)",
        )
        for domain in domains:
            with self.subTest(domain=domain):
                self.assertIn(domain.replace("\\`", "`"), self.hierarchy)
        self.assertLess(
            self.hierarchy.index("**Index**"), self.hierarchy.index("**Skills**")
        )
        self.assertLess(
            self.hierarchy.index("**Skills**"), self.hierarchy.index("**Awesome**")
        )
        self.assertLess(
            self.hierarchy.index("**Awesome**"),
            self.hierarchy.index("**Upstream Contributions**"),
        )

    def test_dispatch_preserved_and_missing_subgroup_commands_not_invented(self):
        for command in (
            "start a batch assessment",
            "batch status",
            "batch reconcile",
            "upstream upgrade",
            "upstream discover",
            "upstream continue <harness>",
            "upstream status",
            "check S3* audit status",
            "check repository standards",
            "S3: inspect current control",
            "S5: consider <matter>",
        ):
            with self.subTest(command=command):
                self.assertIn(command, self.hierarchy)
                self.assertIn(command, self.menu)
        self.assertIn("No standalone Skills first-contact command", self.hierarchy)
        self.assertIn("No standalone Awesome first-contact command", self.hierarchy)
        self.assertIn("exact-target entry hint", self.hierarchy)

    def test_function_and_authority_boundaries_not_overclaimed(self):
        for boundary in (
            "navigation taxonomy",
            "not new VSM evidence",
            "without an executable S2 button",
            "without an executable S4 button",
            "not automatically S2",
            "not proof of S4",
            "not a discretionary S3* judgment by itself",
            "not a generic approval button",
            "not Organization S4",
        ):
            with self.subTest(boundary=boundary):
                self.assertIn(boundary, self.hierarchy)
        self.assertIn("Never render literal", self.hierarchy)
        self.assertIn("not misleading buttons", self.hierarchy)
        self.assertIn("existing source-first admission", self.hierarchy.lower())

    def test_bootstrap_requires_nested_menu_and_text_fallback(self):
        self.assertIn("**VSM-first action menu**", self.bootstrap)
        for domain in ("Index", "Skills", "Awesome", "Upstream Contributions"):
            self.assertIn(domain, self.bootstrap)
        self.assertIn("**same VSM groups and four S1 subgroups**", self.bootstrap)
        self.assertIn("request a concrete issue/PR target", self.bootstrap)


if __name__ == "__main__":
    unittest.main()
