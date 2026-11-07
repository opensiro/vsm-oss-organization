"""Guard the retired fit-rate metric without destroying its historical evidence."""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "experiments" / "upstream-intervention-fit"


class DeprecatedUpstreamFitTests(unittest.TestCase):
    def test_metric_is_deprecated_not_replaced_by_unverified_adoption(self):
        metric = json.loads((ARCHIVE / "metric.json").read_text(encoding="utf-8"))
        self.assertEqual(metric["status"], "deprecated")
        self.assertEqual(metric["deprecated_at"], "2026-11-07")
        self.assertIsNone(metric["replacement_metric"])
        self.assertEqual(metric["primary_metric"]["id"], "product_native_fit_rate")

    def test_archived_evidence_and_report_remain_reproducible(self):
        observations = json.loads((ARCHIVE / "observations.json").read_text(encoding="utf-8"))
        snapshot = json.loads((ARCHIVE / "snapshot.json").read_text(encoding="utf-8"))
        self.assertEqual(len(observations["interventions"]), 8)
        self.assertEqual(snapshot["primary_metric"]["value"], 0.6)
        self.assertEqual(snapshot["as_of"], "2026-10-12")

    def test_active_kpis_exclude_retired_fit_rate(self):
        metrics = (ROOT / "metrics.yaml").read_text(encoding="utf-8")
        self.assertNotIn("product_native_fit_rate", metrics)
        self.assertIn("verified_external_outcomes", metrics)
        plane = (ROOT / "docs/AGENT_CONTROL_PLANE.md").read_text(encoding="utf-8")
        self.assertIn("frozen deprecated research", plane)
        self.assertIn("Upstream-native justification", plane)
        readme = (ARCHIVE / "README.md").read_text(encoding="utf-8")
        self.assertIn("DEPRECATED", readme)
        self.assertIn("do not add new observations", readme)


if __name__ == "__main__":
    unittest.main()
