import importlib.util
import json
import os
import subprocess
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
publication:
  aggregate_productivity_score: forbidden
"""


def run_git(root: Path, *args: str, env=None):
    subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def commit_all(root: Path, when: str, message: str):
    run_git(root, "add", ".")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = when
    env["GIT_COMMITTER_DATE"] = when
    run_git(root, "commit", "-m", message, env=env)


class CollectorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        base = Path(self.temp.name)
        self.roots = {key: base / key for key in collector.REPOSITORIES}
        for root in self.roots.values():
            root.mkdir(parents=True)
            run_git(root, "init", "-q")
            run_git(root, "config", "user.email", "test@example.com")
            run_git(root, "config", "user.name", "Test")

        (self.roots["organization"] / "metrics.yaml").write_text(
            CONTRACT, encoding="utf-8"
        )
        commit_all(self.roots["organization"], "2026-08-01T12:00:00Z", "contract")

        (self.roots["profile"] / "VERSION").write_text("0.2.3\n", encoding="utf-8")
        commit_all(self.roots["profile"], "2026-08-01T12:00:00Z", "profile 0.2.3")
        (self.roots["profile"] / "VERSION").write_text("0.2.4\n", encoding="utf-8")
        commit_all(self.roots["profile"], "2026-09-20T12:00:00Z", "profile 0.2.4")

        version = self.roots["skills"] / "skills" / "assess-vsm-harness" / "VERSION"
        version.parent.mkdir(parents=True)
        version.write_text("0.3.5\n", encoding="utf-8")
        (self.roots["skills"] / "README.md").write_text(
            "# Skills\n\n## Skill catalog\n\n| Skill | Purpose |\n| --- | --- |\n"
            "| [assess-vsm-harness](skills/assess-vsm-harness/SKILL.md) | Assess |\n",
            encoding="utf-8",
        )
        commit_all(self.roots["skills"], "2026-08-01T12:00:00Z", "skills old")
        version.write_text("0.3.6\n", encoding="utf-8")
        (self.roots["skills"] / "README.md").write_text(
            "# Skills\n\n## Skill catalog\n\n| Skill | Purpose |\n| --- | --- |\n"
            "| [assess-vsm-harness](skills/assess-vsm-harness/SKILL.md) | Assess |\n"
            "| [second](skills/second/SKILL.md) | Second |\n",
            encoding="utf-8",
        )
        commit_all(self.roots["skills"], "2026-09-18T12:00:00Z", "skills new")

        data = self.roots["index"] / "data"
        data.mkdir()
        for when, included, catalog, reassess in [
            ("2026-08-01T12:00:00Z", 1, 2, 1),
            ("2026-08-30T12:00:00Z", 2, 3, 2),
            ("2026-09-18T12:00:00Z", 3, 4, 4),
            ("2026-09-22T12:00:00Z", 4, 5, 7),
        ]:
            (data / "metrics.json").write_text(
                json.dumps(
                    {
                        "corpus": {
                            "included_assessments": included,
                            "catalog_entries": catalog,
                            "reassessment_events": reassess,
                        },
                        "active_contract": {
                            "profile_version": "0.2.4",
                            "methodology_version": "0.3.6",
                        },
                    }
                ),
                encoding="utf-8",
            )
            commit_all(self.roots["index"], when, f"index {included}")

        readme = self.roots["awesome"] / "README.md"
        readme.write_text(
            "[Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/alpha.md)\n",
            encoding="utf-8",
        )
        commit_all(self.roots["awesome"], "2026-08-01T12:00:00Z", "awesome 1")
        readme.write_text(
            "[Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/alpha.md)\n"
            "[Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/beta.md)\n",
            encoding="utf-8",
        )
        commit_all(self.roots["awesome"], "2026-09-18T12:00:00Z", "awesome 2")

        self.activity = {
            repo: {
                "classification": "secondary_non_kpi",
                "commits_24h": 10,
                "commits_7d": 40,
                "commits_30d": 100,
            }
            for repo in collector.REPOSITORIES.values()
        }
        self.now = datetime(2026, 9, 22, 18, 0, tzinfo=timezone.utc)

    def tearDown(self):
        self.temp.cleanup()

    def snapshot(self):
        return collector.collect_snapshot(
            self.roots,
            collected_at=self.now,
            activity=self.activity,
        )

    def test_index_uses_repo_owned_metrics_without_reparsing_assessments(self):
        snapshot = self.snapshot()
        metric = snapshot["repositories"]["opensiro/vsm-harness-index"]["metrics"][
            "included_assessments"
        ]
        self.assertEqual(metric["value"], 4)
        self.assertEqual(
            metric["source"], "data/metrics.json#/corpus/included_assessments"
        )
        self.assertEqual(metric["window_change"]["24h"]["value"], 1)
        self.assertEqual(metric["window_change"]["7d"]["value"], 2)
        self.assertEqual(metric["window_change"]["30d"]["value"], 3)
        self.assertNotIn("raw", snapshot["repositories"]["opensiro/vsm-harness-index"])

    def test_window_change_is_net_state_change_not_gross_flow(self):
        snapshot = self.snapshot()
        self.assertEqual(
            snapshot["publication"]["window_change_semantics"],
            "net canonical state change, not gross event count",
        )
        reassess = snapshot["repositories"]["opensiro/vsm-harness-index"]["metrics"][
            "reassessment_events"
        ]["window_change"]
        self.assertEqual(reassess["24h"]["value"], 3)
        self.assertEqual(reassess["7d"]["value"], 5)
        self.assertEqual(reassess["30d"]["value"], 6)

    def test_profile_and_skills_compare_same_repo_owned_state_across_windows(self):
        snapshot = self.snapshot()
        profile = snapshot["repositories"]["opensiro/vsm-harness-profile"]["metrics"][
            "current_validated_profile_release"
        ]["window_change"]
        self.assertFalse(profile["24h"]["changed"])
        self.assertTrue(profile["7d"]["changed"])
        self.assertTrue(profile["30d"]["changed"])

        skills = snapshot["repositories"]["opensiro/vsm-harness-skills"]["metrics"]
        self.assertEqual(
            skills["skill_catalog_entries"]["window_change"]["24h"]["value"], 0
        )
        self.assertEqual(
            skills["skill_catalog_entries"]["window_change"]["7d"]["value"], 1
        )

    def test_semantic_metrics_remain_unclaimed_for_all_windows(self):
        snapshot = self.snapshot()
        metric = snapshot["repositories"]["opensiro/vsm-oss-organization"]["metrics"][
            "current_formal_construction_milestone"
        ]
        self.assertIsNone(metric["value"])
        for label in ("24h", "7d", "30d"):
            self.assertEqual(
                metric["window_change"][label]["status"],
                "unclaimed_semantic_evidence",
            )

    def test_activity_is_separate_and_has_30d(self):
        snapshot = self.snapshot()
        repo = snapshot["repositories"]["opensiro/vsm-harness-index"]
        self.assertNotIn("commits_24h", repo["metrics"])
        self.assertEqual(
            repo["engineering_activity"]["classification"], "secondary_non_kpi"
        )
        self.assertEqual(repo["engineering_activity"]["commits_30d"], 100)
        self.assertEqual(snapshot["windows"], ["24h", "7d", "30d"])

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
