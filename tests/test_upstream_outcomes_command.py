"""Contract tests for the agent-invoked Upstream outcomes evidence review route."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MENU = ROOT / "docs" / "AGENT_CONTROL_PLANE.md"
CONTRACT = ROOT / "docs" / "UPSTREAM_OUTCOMES.md"
TEMPLATE = ROOT / "prompts" / "upstream-outcome-review.md"
DOC_INDEX = ROOT / "docs" / "README.md"


class UpstreamOutcomesCommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menu = MENU.read_text(encoding="utf-8")
        cls.contract = CONTRACT.read_text(encoding="utf-8")
        cls.template = TEMPLATE.read_text(encoding="utf-8")
        cls.doc_index = DOC_INDEX.read_text(encoding="utf-8")

    def test_command_is_discoverable_in_both_control_plane_menus(self):
        self.assertIn("| **Upstream Outcomes** | `upstream outcomes` |", self.menu)
        self.assertIn("| `upstream outcomes` / `verify upstream outcomes` |", self.menu)
        self.assertIn("### Upstream outcomes — evidence-first agent review", self.menu)
        self.assertIn("UPSTREAM_OUTCOMES.md", self.menu)
        self.assertIn("UPSTREAM_OUTCOMES.md", self.doc_index)
        self.assertIn("upstream outcomes", self.contract)

    def test_routes_to_live_s1_owner_without_s3_claim(self):
        self.assertIn("opensiro/upstream/issues/159", self.menu)
        self.assertIn("opensiro/upstream/issues/159", self.contract)
        self.assertIn("scripts/verified_external_outcomes.py", self.contract)
        self.assertIn("docs/VERIFIED_EXTERNAL_OUTCOMES.md", self.contract)
        self.assertIn("--validate-only", self.contract)
        self.assertIn("--report --output-json", self.contract)
        self.assertIn("source-first agent session entry", self.contract)
        self.assertIn("not an accepted fact, formal S3* audit", self.template)
        self.assertIn("not the deployment of a persistent agent", self.menu)

    def test_verified_source_acceptance_does_not_claim_organization_metric(self):
        for status in (
            "VERIFIED",
            "PENDING_REVIEW",
            "INSUFFICIENT_EVIDENCE",
            "UNVERIFIABLE",
        ):
            with self.subTest(status=status):
                self.assertIn(status, self.contract)
                self.assertIn(status, self.template)
        self.assertIn("ACCEPTED_MERGED_CHANGE_ONLY", self.contract)
        self.assertIn("DETERMINISTIC_VERIFIED_MERGE", self.contract)
        self.assertIn("UPSTREAM_ACCEPTED_SOURCE_ONLY", self.contract)
        self.assertIn("organization_metric_claimed=false", self.contract)
        self.assertIn("Organization metric claim", self.contract)
        self.assertIn("Product-native fit is deprecated", self.contract)

    def test_semantic_attribution_and_no_duplicate_interventions(self):
        self.assertIn("independently implemented a similar idea", self.contract)
        self.assertIn("Closing actor is not closure", self.contract)
        self.assertIn("one intervention", self.contract)
        self.assertIn("original and landing", self.contract)
        self.assertIn("Native test receipt", self.template)
        self.assertIn("Other maintainer PR or independent implementation", self.template)
        self.assertIn("Replacement-chain intervention deduplication", self.template)

    def test_submission_requires_real_owner_and_authority(self):
        self.assertIn("propose an **internal\n   Upstream PR**", self.contract)
        self.assertIn("Do not create\n   a parallel Organization factual ledger", self.contract)
        self.assertIn("does **not** automatically publish external PRs", self.contract)
        self.assertIn("Do not append an owner-decision row for every new", self.contract)
        self.assertIn("source/cohort digests", self.contract)
        self.assertIn("Live observation URL", self.template)


if __name__ == "__main__":
    unittest.main()
