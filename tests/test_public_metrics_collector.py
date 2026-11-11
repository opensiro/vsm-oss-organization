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
    - opensiro/upstream
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
  opensiro/upstream:
    organizational_role: operational_s1
    primary_metric: verified_external_outcomes
    metrics:
      verified_external_outcomes:
        kind: stock
        source:
          mode: semantic_evidence
          paths: [registry.yaml]
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


def write_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


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

        (self.roots["organization"] / "metrics.yaml").write_text(CONTRACT, encoding="utf-8")
        commit_all(self.roots["organization"], "2026-08-01T12:00:00Z", "contract")

        (self.roots["upstream"] / "registry.yaml").write_text("projects: []\n", encoding="utf-8")
        commit_all(self.roots["upstream"], "2026-08-01T12:00:00Z", "upstream fixture")

        (self.roots["profile"] / "VERSION").write_text("0.2.3\n", encoding="utf-8")
        commit_all(self.roots["profile"], "2026-08-01T12:00:00Z", "profile 0.2.3")
        (self.roots["profile"] / "VERSION").write_text("0.2.4\n", encoding="utf-8")
        commit_all(self.roots["profile"], "2026-09-20T12:00:00Z", "profile 0.2.4")

        skills_metrics = self.roots["skills"] / "data" / "metrics.json"
        write_json(skills_metrics, {
            "schema_version": 1,
            "methodology_version": "0.3.5",
            "skill_catalog_entries": 1,
            "skill_ids": ["assess-vsm-harness"],
        })
        commit_all(self.roots["skills"], "2026-08-01T12:00:00Z", "skills old owner metrics")
        write_json(skills_metrics, {
            "schema_version": 1,
            "methodology_version": "0.3.6",
            "skill_catalog_entries": 2,
            "skill_ids": ["assess-vsm-harness", "second"],
        })
        commit_all(self.roots["skills"], "2026-09-18T12:00:00Z", "skills new owner metrics")

        index_metrics = self.roots["index"] / "data" / "metrics.json"
        for when, included, catalog, reassess in [
            ("2026-08-01T12:00:00Z", 1, 2, 1),
            ("2026-08-30T12:00:00Z", 2, 3, 2),
            ("2026-09-18T12:00:00Z", 3, 4, 4),
            ("2026-09-22T12:00:00Z", 4, 5, 7),
        ]:
            write_json(index_metrics, {
                "corpus": {
                    "included_assessments": included,
                    "catalog_entries": catalog,
                    "reassessment_events": reassess,
                },
                "active_contract": {
                    "profile_version": "0.2.4",
                    "methodology_version": "0.3.6",
                },
            })
            commit_all(self.roots["index"], when, f"index {included}")

        awesome_metrics = self.roots["awesome"] / "data" / "metrics.json"
        write_json(awesome_metrics, {
            "schema_version": 1,
            "curated_representative_entries": 1,
            "curated_entry_ids": ["alpha"],
        })
        commit_all(self.roots["awesome"], "2026-08-01T12:00:00Z", "awesome old owner metrics")
        write_json(awesome_metrics, {
            "schema_version": 1,
            "curated_representative_entries": 2,
            "curated_entry_ids": ["alpha", "beta"],
        })
        commit_all(self.roots["awesome"], "2026-09-18T12:00:00Z", "awesome new owner metrics")

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

    def test_consumes_only_owner_artifacts_for_skills_index_and_awesome(self):
        snapshot = self.snapshot()
        skills = snapshot["repositories"]["opensiro/vsm-harness-skills"]["metrics"]
        index = snapshot["repositories"]["opensiro/vsm-harness-index"]["metrics"]
        awesome = snapshot["repositories"]["opensiro/awesome-vsm-harness"]["metrics"]

        self.assertEqual(skills["current_validated_methodology_release"]["value"], "0.3.6")
        self.assertEqual(skills["skill_catalog_entries"]["value"], 2)
        self.assertEqual(skills["skill_catalog_entries"]["source"], "data/metrics.json#/skill_catalog_entries")
        self.assertEqual(index["included_assessments"]["value"], 4)
        self.assertEqual(index["included_assessments"]["source"], "data/metrics.json#/corpus/included_assessments")
        self.assertEqual(awesome["curated_representative_entries"]["value"], 2)
        self.assertEqual(awesome["curated_representative_entries"]["source"], "data/metrics.json#/curated_representative_entries")

        # There are intentionally no Skills/Awesome README fixtures. If central
        # parsing returns, this test suite fails before assertions are reached.
        self.assertFalse((self.roots["skills"] / "README.md").exists())
        self.assertFalse((self.roots["awesome"] / "README.md").exists())

    def test_owner_artifact_growth_is_net_state_change(self):
        snapshot = self.snapshot()
        self.assertEqual(
            snapshot["publication"]["window_change_semantics"],
            "net canonical state change, not gross event count",
        )
        skills = snapshot["repositories"]["opensiro/vsm-harness-skills"]["metrics"]
        awesome = snapshot["repositories"]["opensiro/awesome-vsm-harness"]["metrics"]
        index = snapshot["repositories"]["opensiro/vsm-harness-index"]["metrics"]

        self.assertEqual(skills["skill_catalog_entries"]["window_change"]["24h"]["value"], 0)
        self.assertEqual(skills["skill_catalog_entries"]["window_change"]["7d"]["value"], 1)
        self.assertFalse(skills["current_validated_methodology_release"]["window_change"]["24h"]["changed"])
        self.assertTrue(skills["current_validated_methodology_release"]["window_change"]["7d"]["changed"])
        self.assertEqual(awesome["curated_representative_entries"]["window_change"]["7d"]["value"], 1)
        self.assertEqual(index["included_assessments"]["window_change"]["24h"]["value"], 1)
        self.assertEqual(index["included_assessments"]["window_change"]["7d"]["value"], 2)
        self.assertEqual(index["included_assessments"]["window_change"]["30d"]["value"], 3)

    def test_profile_direct_owner_state_and_semantic_org_boundary(self):
        snapshot = self.snapshot()
        profile = snapshot["repositories"]["opensiro/vsm-harness-profile"]["metrics"]["current_validated_profile_release"]
        self.assertEqual(profile["source"], "VERSION")
        self.assertFalse(profile["window_change"]["24h"]["changed"])
        self.assertTrue(profile["window_change"]["7d"]["changed"])

        org = snapshot["repositories"]["opensiro/vsm-oss-organization"]["metrics"]["current_formal_construction_milestone"]
        self.assertIsNone(org["value"])
        for label in ("24h", "7d", "30d"):
            self.assertEqual(org["window_change"][label]["status"], "unclaimed_semantic_evidence")

    def test_upstream_domain_does_not_fabricate_external_outcome_count(self):
        snapshot = self.snapshot()
        upstream = snapshot["repositories"]["opensiro/upstream"]
        self.assertEqual("operational_s1", upstream["organizational_role"])
        outcomes = upstream["metrics"]["verified_external_outcomes"]
        self.assertIsNone(outcomes["value"])
        self.assertEqual("unclaimed_semantic_evidence", outcomes["claim_status"])
        self.assertFalse(outcomes["completion_gate_evaluated"])
        self.assertEqual(["registry.yaml"], outcomes["evidence_paths"])
        for label in ("24h", "7d", "30d"):
            self.assertEqual("unclaimed_semantic_evidence", outcomes["window_change"][label]["status"])


    def outcome_export(self, *, count=1, status="UPSTREAM_ACCEPTED_SOURCE_ONLY"):
        """The live owner API is tested by Upstream; Organization tests consumption."""
        owner_script = self.roots["upstream"] / "scripts" / "verified_external_outcomes.py"
        owner_script.parent.mkdir(exist_ok=True)
        owner_script.write_text(
            "class Portfolio:\n"
            "    def cohort(self): return []\n"
            "    def cohort_fingerprint(self, value): return 'b' * 64\n"
            "portfolio_reconcile = Portfolio()\n"
            "def digest_sources(): return 'a' * 64\n",
            encoding="utf-8",
        )
        cases = [{
            "intervention_id": "improvement:agent-fleet",
            "external_pr_url": "https://github.com/chankov/agent-fleet/pull/43",
            "merge_commit_sha": "c" * 40,
            "native_receipt": "https://github.com/opensiro/upstream/actions/runs/40093167700",
            "decision": "ACCEPTED_MERGED_CHANGE_ONLY",
            "acceptance_basis": "DETERMINISTIC_VERIFIED_MERGE",
            "benefit_claim": "NOT_MEASURED",
        }] if count else []
        data = {
            "schema_version": 1,
            "source": "opensiro/upstream",
            "metric_status": status,
            "observed_at": self.now.isoformat(),
            "source_sha256": "a" * 64,
            "portfolio_cohort_sha256": "b" * 64,
            "accepted_count": count,
            "accepted": cases,
            "organization_metric_claimed": False,
        }
        path = Path(self.temp.name) / "upstream-export.json"
        write_json(path, data)
        return path, data

    def test_owner_verified_merged_change_can_be_claimed_without_benefit_claim(self):
        path, _ = self.outcome_export()
        result = collector.collect_snapshot(
            self.roots, collected_at=self.now, activity=self.activity,
            upstream_accepted=path,
        )
        claim = result["repositories"]["opensiro/upstream"]["metrics"]["verified_external_outcomes"]
        self.assertEqual(claim["value"], 1)
        self.assertTrue(claim["completion_gate_evaluated"])
        self.assertEqual(claim["claim_status"],
                         "verified_merged_changes_only_not_deployed_benefit")
        self.assertEqual(claim["accepted"][0]["benefit_claim"], "NOT_MEASURED")
        for window in collector.WINDOWS:
            self.assertIsNone(claim["window_change"][window]["value"])
            self.assertEqual(claim["window_change"][window]["status"],
                             "source_unavailable_at_baseline")

    def test_empty_verified_export_stays_unclaimed(self):
        path, _ = self.outcome_export(
            count=0, status="UNCLAIMED_SEMANTIC_EVIDENCE")
        data = collector.collect_snapshot(
            self.roots, collected_at=self.now, activity=self.activity,
            upstream_accepted=path)
        metric = data["repositories"]["opensiro/upstream"]["metrics"]["verified_external_outcomes"]
        self.assertIsNone(metric["value"])
        self.assertEqual(metric["claim_status"], "unclaimed_semantic_evidence")

    def test_stale_or_drifted_owner_export_fails_closed(self):
        path, data = self.outcome_export()
        bad = [
            {"source_sha256": "0" * 64},
            {"portfolio_cohort_sha256": "f" * 64},
            {"accepted_count": 2},
            {"observed_at": "2026-09-20T12:00:00Z"},
            {"organization_metric_claimed": True},
            {"metric_status": "CANDIDATE_ONLY_NOT_ORGANIZATION_CLAIMED"},
        ]
        for edit in bad:
            with self.subTest(edit=edit):
                write_json(path, dict(data, **edit))
                with self.assertRaises(collector.CollectorError):
                    collector.collect_snapshot(
                        self.roots, collected_at=self.now, activity=self.activity,
                        upstream_accepted=path)

    def test_duplicate_and_unpinned_or_false_benefit_fail_closed(self):
        path, data = self.outcome_export()
        for key, value in [
            ("benefit_claim", "DEPLOYED"),
            ("native_receipt", "https://github.com/opensiro/upstream/blob/main/test"),
            ("acceptance_basis", "RAW_MERGE_COUNT"),
        ]:
            with self.subTest(field=key):
                edited = json.loads(json.dumps(data))
                edited["accepted"][0][key] = value
                write_json(path, edited)
                with self.assertRaises(collector.CollectorError):
                    collector.collect_snapshot(
                        self.roots, collected_at=self.now, activity=self.activity,
                        upstream_accepted=path)
        duplicate = json.loads(json.dumps(data))
        duplicate["accepted"].append(dict(duplicate["accepted"][0]))
        duplicate["accepted_count"] = 2
        write_json(path, duplicate)
        with self.assertRaises(collector.CollectorError):
            collector.collect_snapshot(
                self.roots, collected_at=self.now, activity=self.activity,
                upstream_accepted=path)

    def test_activity_is_separate_non_kpi_telemetry(self):
        snapshot = self.snapshot()
        repo = snapshot["repositories"]["opensiro/vsm-harness-index"]
        self.assertNotIn("commits_24h", repo["metrics"])
        self.assertEqual(repo["engineering_activity"]["classification"], "secondary_non_kpi")
        self.assertEqual(repo["engineering_activity"]["commits_30d"], 100)
        self.assertFalse(snapshot["publication"]["engineering_activity_is_productivity_kpi"])
        self.assertEqual(snapshot["windows"], ["24h", "7d", "30d"])

    def test_missing_owner_artifact_fails_closed(self):
        (self.roots["awesome"] / "data" / "metrics.json").unlink()
        with self.assertRaises(collector.CollectorError):
            self.snapshot()

    def test_scope_drift_fails_closed(self):
        contract = CONTRACT.replace(
            "    - opensiro/vsm-oss-organization\n",
            "    - opensiro/vsm-oss-organization\n    - opensiro/not-in-scope\n",
            1,
        )
        (self.roots["organization"] / "metrics.yaml").write_text(contract, encoding="utf-8")
        with self.assertRaises(collector.CollectorError):
            self.snapshot()


if __name__ == "__main__":
    unittest.main()
