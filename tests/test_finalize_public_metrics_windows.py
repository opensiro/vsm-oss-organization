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


class FinalizeWindowsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.index = Path(self.temp.name) / "index"
        self.index.mkdir()
        git(self.index, "init", "-q")
        git(self.index, "config", "user.email", "test@example.com")
        git(self.index, "config", "user.name", "Test")

        data = self.index / "data"
        data.mkdir()
        (data / "core_source.json").write_text(
            json.dumps({"included_assessments": 3, "catalog_entries": 4}),
            encoding="utf-8",
        )
        commit(self.index, "2026-09-15T12:00:00Z", "historical source")
        self.baseline_revision = subprocess.check_output(
            ["git", "-C", str(self.index), "rev-parse", "HEAD"], text=True
        ).strip()

        scripts = self.index / "scripts"
        scripts.mkdir()
        (scripts / "render_metrics.py").write_text(
            """#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
p = argparse.ArgumentParser()
p.add_argument('--source-root', type=Path, required=True)
p.add_argument('--stdout-core-json', action='store_true')
a = p.parse_args()
print((a.source_root / 'data' / 'core_source.json').read_text())
""",
            encoding="utf-8",
        )
        (data / "core_source.json").write_text(
            json.dumps({"included_assessments": 4, "catalog_entries": 5}),
            encoding="utf-8",
        )
        commit(self.index, "2026-09-22T12:00:00Z", "current renderer")

    def tearDown(self):
        self.temp.cleanup()

    def snapshot(self):
        gap = {
            "24h": {
                "status": "derived_net_change",
                "baseline": 4,
                "value": 0,
            },
            "7d": {
                "status": "source_unavailable_at_baseline",
                "baseline_revision": self.baseline_revision,
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
        return {
            "publication": {
                "window_change_semantics": "net canonical state change, not gross event count"
            },
            "repositories": {
                "opensiro/vsm-harness-index": {
                    "metrics": {
                        "included_assessments": {
                            "value": 4,
                            "window_change": json.loads(json.dumps(gap)),
                        },
                        "catalog_entries": {
                            "value": 5,
                            "window_change": json.loads(json.dumps(gap)),
                        },
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

    def test_fills_index_gap_with_index_owned_renderer_and_pre_inception_zero(self):
        result = finalizer.finalize(self.snapshot(), self.index)
        index = result["repositories"]["opensiro/vsm-harness-index"]["metrics"]

        included_7d = index["included_assessments"]["window_change"]["7d"]
        self.assertEqual(included_7d["baseline"], 3)
        self.assertEqual(included_7d["value"], 1)
        self.assertEqual(
            included_7d["status"], "derived_net_change_via_repository_renderer"
        )

        included_30d = index["included_assessments"]["window_change"]["30d"]
        self.assertEqual(included_30d["baseline"], 0)
        self.assertEqual(included_30d["value"], 4)
        self.assertEqual(
            included_30d["status"], "derived_pre_inception_net_change"
        )

        catalog_7d = index["catalog_entries"]["window_change"]["7d"]
        self.assertEqual(catalog_7d["baseline"], 4)
        self.assertEqual(catalog_7d["value"], 1)

    def test_pre_inception_state_is_created_not_semantically_inferred(self):
        result = finalizer.finalize(self.snapshot(), self.index)
        profile = result["repositories"]["opensiro/vsm-harness-profile"]["metrics"]
        state = profile["current_validated_profile_release"]["window_change"]["30d"]
        self.assertTrue(state["changed"])
        self.assertEqual(state["status"], "derived_pre_inception_state")

        organization = result["repositories"]["opensiro/vsm-oss-organization"]["metrics"]
        semantic = organization["current_formal_construction_milestone"]["window_change"]["30d"]
        self.assertEqual(semantic["status"], "unclaimed_semantic_evidence")
        self.assertIsNone(semantic["value"])


if __name__ == "__main__":
    unittest.main()
