import importlib.util
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "collect_public_metrics.py"
SPEC = importlib.util.spec_from_file_location("collect_public_metrics", SCRIPT)
collector = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(collector)


CONTRACT = """
schema_version: 1
scope:
  repositories:
    - opensiro/vsm-harness-profile
    - opensiro/vsm-harness-skills
    - opensiro/vsm-harness-index
    - opensiro/awesome-vsm-harness
    - opensiro/vsm-oss-organization
repositories:
  opensiro/vsm-harness-profile:
    organizational_role: normative_semantic_authority
    primary_metric: current_validated_profile_release
    metrics: {}
  opensiro/vsm-harness-skills:
    organizational_role: operational_s1
    primary_metric: current_validated_methodology_release
    metrics: {}
  opensiro/vsm-harness-index:
    organizational_role: operational_s1
    primary_metric: included_assessments
    metrics: {}
  opensiro/awesome-vsm-harness:
    organizational_role: operational_s1
    primary_metric: curated_representative_entries
    metrics: {}
  opensiro/vsm-oss-organization:
    organizational_role: metasystem_control_construction
    primary_metric: current_formal_construction_milestone
    metrics:
      current_formal_construction_milestone:
        kind: state
        source:
          mode: semantic_evidence
          paths: [ROADMAP.md, README.md]
      completed_current_control_transactions:
        kind: flow
        source:
          mode: semantic_evidence
          path: CONTROL_PLANE.md
publication:
  aggregate_productivity_score: forbidden
"""


class CollectorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        base = Path(self.temp.name)
        self.roots = {key: base / key for key in collector.REPOSITORIES}
        for root in self.roots.values():
            root.mkdir(parents=True)

        (self.roots["organization"] / "metrics.yaml").write_text(
            CONTRACT, encoding="utf-8"
        )
        (self.roots["profile"] / "VERSION").write_text("0.2.4\n", encoding="utf-8")

        version = self.roots["skills"] / "skills" / "assess-vsm-harness" / "VERSION"
        version.parent.mkdir(parents=True)
        version.write_text("0.3.6\n", encoding="utf-8")
        (self.roots["skills"] / "README.md").write_text(
            """# Skills

## Skill catalog

| Skill | Purpose |
| --- | --- |
| [assess-vsm-harness](skills/assess-vsm-harness/SKILL.md) | Assess |

## Other
""",
            encoding="utf-8",
        )

        data = self.roots["index"] / "data"
        data.mkdir()
        (data / "metrics.json").write_text(
            json.dumps(
                {
                    "corpus": {
                        "included_assessments": 2,
                        "catalog_entries": 3,
                        "reassessment_events": 4,
                    },
                    "active_contract": {
                        "profile_version": "0.2.4",
                        "methodology_version": "0.3.6",
                    },
                }
            ),
            encoding="utf-8",
        )
        (data / "signatures.psv").write_text(
            "catalog_position|harness_id|signature\n"
            "1|alpha|a\n"
            "2|beta|b\n",
            encoding="utf-8",
        )

        (self.roots["awesome"] / "README.md").write_text(
            "- [Alpha](https://example.com/alpha) - A. "
            "[Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/alpha.md) "
            "· [TL;DR](https://example.com) · [Ranking](https://example.com)\n"
            "- [Beta](https://example.com/beta) - B. "
            "[Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/beta.md) "
            "· [TL;DR](https://example.com) · [Ranking](https://example.com)\n"
            "- [Unrelated list](https://example.com)\n",
            encoding="utf-8",
        )

        self.revisions = {
            repo: f"{index:040x}"
            for index, repo in enumerate(collector.REPOSITORIES.values(), 1)
        }
        self.activity = {
            repo: {
                "classification": "secondary_non_kpi",
                "commits_24h": 10,
                "commits_7d": 40,
            }
            for repo in collector.REPOSITORIES.values()
        }
        self.now = datetime(2026, 9, 22, 18, 0, tzinfo=timezone.utc)

    def tearDown(self):
        self.temp.cleanup()

    def snapshot(self, previous=None):
        return collector.collect_snapshot(
            self.roots,
            collected_at=self.now,
            revisions=self.revisions,
            activity=self.activity,
            previous=previous,
        )

    def test_collects_only_declared_outcomes_and_separates_activity(self):
        snapshot = self.snapshot()
        self.assertEqual(snapshot["scope"], list(collector.REPOSITORIES.values()))
        self.assertEqual(
            snapshot["repositories"]["opensiro/vsm-harness-index"]["metrics"][
                "included_assessments"
            ]["value"],
            2,
        )
        self.assertEqual(
            snapshot["repositories"]["opensiro/awesome-vsm-harness"]["metrics"][
                "curated_representative_entries"
            ]["value"],
            2,
        )
        self.assertNotIn("commits_24h", snapshot["repositories"]["opensiro/vsm-harness-index"]["metrics"])
        self.assertEqual(
            snapshot["repositories"]["opensiro/vsm-harness-index"]["engineering_activity"][
                "classification"
            ],
            "secondary_non_kpi",
        )
        self.assertEqual(
            snapshot["publication"]["aggregate_productivity_score"], "forbidden"
        )
        self.assertEqual(snapshot["flows"]["status"], "requires_previous_snapshot")

    def test_semantic_organization_metrics_remain_unclaimed(self):
        snapshot = self.snapshot()
        metrics = snapshot["repositories"]["opensiro/vsm-oss-organization"]["metrics"]
        self.assertIsNone(metrics["current_formal_construction_milestone"]["value"])
        self.assertEqual(
            metrics["current_formal_construction_milestone"]["claim_status"],
            "unclaimed_semantic_evidence",
        )
        self.assertEqual(
            metrics["current_formal_construction_milestone"]["evidence_paths"],
            ["ROADMAP.md", "README.md"],
        )
        self.assertIsNone(metrics["completed_current_control_transactions"]["value"])

    def test_previous_snapshot_uses_identity_sets_for_flows(self):
        previous = self.snapshot()
        index_repo = previous["repositories"]["opensiro/vsm-harness-index"]
        index_repo["raw"]["included_assessment_ids"] = ["alpha"]
        index_repo["metrics"]["included_assessments"]["value"] = 1
        index_repo["metrics"]["reassessment_events"]["value"] = 2

        awesome_repo = previous["repositories"]["opensiro/awesome-vsm-harness"]
        awesome_repo["raw"]["curated_entry_ids"] = ["alpha", "gamma"]
        awesome_repo["metrics"]["curated_representative_entries"]["value"] = 2

        current = self.snapshot(previous=previous)
        index_flow = current["flows"]["opensiro/vsm-harness-index"]
        self.assertEqual(index_flow["assessments_admitted"]["identities"], ["beta"])
        self.assertEqual(index_flow["reassessments_completed"]["value"], 2)

        awesome_flow = current["flows"]["opensiro/awesome-vsm-harness"]
        self.assertEqual(awesome_flow["entries_admitted"]["identities"], ["beta"])
        self.assertEqual(
            awesome_flow["entries_retired_or_replaced"]["identities"], ["gamma"]
        )

    def test_index_identity_count_must_match_canonical_metric(self):
        (self.roots["index"] / "data" / "signatures.psv").write_text(
            "catalog_position|harness_id|signature\n1|alpha|a\n",
            encoding="utf-8",
        )
        with self.assertRaises(collector.CollectorError):
            self.snapshot()

    def test_scope_drift_fails_closed(self):
        contract = CONTRACT.replace(
            "    - opensiro/vsm-oss-organization\n",
            "    - opensiro/vsm-oss-organization\n    - opensiro/not-in-scope\n",
            1,
        )
        (self.roots["organization"] / "metrics.yaml").write_text(
            contract, encoding="utf-8"
        )
        with self.assertRaises(collector.CollectorError):
            self.snapshot()


if __name__ == "__main__":
    unittest.main()
