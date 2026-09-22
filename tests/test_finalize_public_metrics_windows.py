import importlib.util
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "finalize_public_metrics_windows.py"
SPEC = importlib.util.spec_from_file_location("finalize_public_metrics_windows", SCRIPT)
finalizer = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(finalizer)


def git(root: Path, *args: str, env=None):
    subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def commit(root: Path, when: str, message: str):
    git(root, "add", ".")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = when
    env["GIT_COMMITTER_DATE"] = when
    git(root, "commit", "-m", message, env=env)


def owner_repo(base: Path, name: str, historical: dict, current: dict) -> tuple[Path, str]:
    root = base / name
    root.mkdir()
    git(root, "init", "-q")
    git(root, "config", "user.email", "test@example.com")
    git(root, "config", "user.name", "Test")
    data = root / "data"
    data.mkdir()
    (data / "core_source.json").write_text(json.dumps(historical), encoding="utf-8")
    commit(root, "2026-09-15T12:00:00Z", "historical owner source")
    historical_revision = subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
    ).strip()

    scripts = root / "scripts"
    scripts.mkdir()
    (scripts / "render_metrics.py").write_text(
        """#!/usr/bin/env python3
import argparse
from pathlib import Path
p = argparse.ArgumentParser()
p.add_argument('--source-root', type=Path, required=True)
p.add_argument('--stdout-core-json', action='store_true')
a = p.parse_args()
print((a.source_root / 'data' / 'core_source.json').read_text())
""",
        encoding="utf-8",
    )
    (data / "core_source.json").write_text(json.dumps(current), encoding="utf-8")
    commit(root, "2026-09-22T12:00:00Z", "current owner renderer")
    return root, historical_revision


class FinalizeWindowsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        base = Path(self.temp.name)
        self.skills, self.skills_rev = owner_repo(
            base,
            "skills",
            {"methodology_version": "0.3.5", "skill_catalog_entries": 1},
            {"methodology_version": "0.3.6", "skill_catalog_entries": 2},
        )
        self.index, self.index_rev = owner_repo(
            base,
            "index",
            {"included_assessments": 3, "catalog_entries": 4},
            {"included_assessments": 4, "catalog_entries": 5},
        )
        self.awesome, self.awesome_rev = owner_repo(
            base,
            "awesome",
            {"curated_representative_entries": 1},
            {"curated_representative_entries": 2},
        )
        self.roots = {
            "skills": self.skills,
            "index": self.index,
            "awesome": self.awesome,
        }

    def tearDown(self):
        self.temp.cleanup()

    @staticmethod
    def gap(revision: str) -> dict:
        return {
            "24h": {"status": "derived_net_change", "baseline": 1, "value": 0},
            "7d": {
                "status": "source_unavailable_at_baseline",
                "baseline_revision": revision,
                "baseline": None,
                "value": None,
            },
            "30d": {
                "status": "history_unavailable",
                "baseline_revision": None,
                "baseline": None,
                "value": None,
            },
        }

    def snapshot(self):
        skill_state = self.gap(self.skills_rev)
        skill_state["24h"].pop("value")
        skill_state["24h"]["changed"] = False
        skill_state["7d"].pop("value")
        skill_state["7d"]["changed"] = None
        skill_state["30d"].pop("value")
        skill_state["30d"]["changed"] = None
        return {
            "publication": {
                "window_change_semantics": "net canonical state change, not gross event count"
            },
            "repositories": {
                "opensiro/vsm-harness-skills": {
                    "metrics": {
                        "current_validated_methodology_release": {
                            "value": "0.3.6",
                            "window_change": skill_state,
                        },
                        "skill_catalog_entries": {
                            "value": 2,
                            "window_change": self.gap(self.skills_rev),
                        },
                    }
                },
                "opensiro/vsm-harness-index": {
                    "metrics": {
                        "included_assessments": {
                            "value": 4,
                            "window_change": self.gap(self.index_rev),
                        },
                        "catalog_entries": {
                            "value": 5,
                            "window_change": self.gap(self.index_rev),
                        },
                    }
                },
                "opensiro/awesome-vsm-harness": {
                    "metrics": {
                        "curated_representative_entries": {
                            "value": 2,
                            "window_change": self.gap(self.awesome_rev),
                        }
                    }
                },
                "opensiro/vsm-harness-profile": {
                    "metrics": {
                        "current_validated_profile_release": {
                            "value": "0.2.4",
                            "window_change": {
                                "30d": {
                                    "status": "history_unavailable",
                                    "baseline": None,
                                    "changed": None,
                                }
                            },
                        }
                    }
                },
                "opensiro/vsm-oss-organization": {
                    "metrics": {
                        "current_formal_construction_milestone": {
                            "value": None,
                            "window_change": {
                                "30d": {
                                    "status": "unclaimed_semantic_evidence",
                                    "value": None,
                                }
                            },
                        }
                    }
                },
            },
        }

    def test_all_preinstrumentation_gaps_use_owning_renderers(self):
        result = finalizer.finalize(self.snapshot(), self.roots)

        skills = result["repositories"]["opensiro/vsm-harness-skills"]["metrics"]
        state_7d = skills["current_validated_methodology_release"]["window_change"]["7d"]
        self.assertEqual(state_7d["baseline"], "0.3.5")
        self.assertTrue(state_7d["changed"])
        self.assertEqual(state_7d["status"], "derived_state_change_via_repository_renderer")
        skill_count = skills["skill_catalog_entries"]["window_change"]["7d"]
        self.assertEqual(skill_count["baseline"], 1)
        self.assertEqual(skill_count["value"], 1)

        index = result["repositories"]["opensiro/vsm-harness-index"]["metrics"]
        self.assertEqual(index["included_assessments"]["window_change"]["7d"]["baseline"], 3)
        self.assertEqual(index["included_assessments"]["window_change"]["7d"]["value"], 1)
        self.assertEqual(index["catalog_entries"]["window_change"]["7d"]["baseline"], 4)

        awesome = result["repositories"]["opensiro/awesome-vsm-harness"]["metrics"]
        curated = awesome["curated_representative_entries"]["window_change"]["7d"]
        self.assertEqual(curated["baseline"], 1)
        self.assertEqual(curated["value"], 1)
        self.assertIn("awesome-vsm-harness", curated["baseline_source"])

    def test_pre_inception_stock_and_state_do_not_infer_semantics(self):
        result = finalizer.finalize(self.snapshot(), self.roots)
        skills = result["repositories"]["opensiro/vsm-harness-skills"]["metrics"]
        self.assertEqual(
            skills["skill_catalog_entries"]["window_change"]["30d"]["status"],
            "derived_pre_inception_net_change",
        )
        self.assertEqual(skills["skill_catalog_entries"]["window_change"]["30d"]["baseline"], 0)

        profile = result["repositories"]["opensiro/vsm-harness-profile"]["metrics"]
        state = profile["current_validated_profile_release"]["window_change"]["30d"]
        self.assertTrue(state["changed"])
        self.assertEqual(state["status"], "derived_pre_inception_state")

        semantic = result["repositories"]["opensiro/vsm-oss-organization"]["metrics"]["current_formal_construction_milestone"]["window_change"]["30d"]
        self.assertEqual(semantic["status"], "unclaimed_semantic_evidence")
        self.assertIsNone(semantic["value"])

    def test_missing_owner_root_fails_closed(self):
        roots = dict(self.roots)
        roots.pop("awesome")
        with self.assertRaises(finalizer.FinalizeError):
            finalizer.finalize(self.snapshot(), roots)


if __name__ == "__main__":
    unittest.main()
