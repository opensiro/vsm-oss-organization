"""Offline tests for the on-demand, read-only ecosystem snapshot command."""

import base64
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import oss_snapshot as snapshot  # noqa: E402


SCOPE = [
    "opensiro/awesome-vsm-harness",
    "opensiro/upstream",
    "opensiro/vsm-harness-index",
    "opensiro/vsm-harness-profile",
    "opensiro/vsm-harness-skills",
    "opensiro/vsm-oss-organization",
]


class FakeGitHub:
    def __init__(self):
        self.heads = {name: f"{index + 1:040x}" for index, name in enumerate(SCOPE)}
        self.refs = {
            ("opensiro/vsm-harness-profile", "v0.2.4"): "a" * 40,
            ("opensiro/vsm-harness-skills", "v0.3.7"): "b" * 40,
        }
        self.selected = {
            "profile": {"repository": "opensiro/vsm-harness-profile", "source_kind": "release",
                        "ref": "v0.2.4", "version": "0.2.4", "version_path": "VERSION",
                        "release_impact_path": "RELEASE_IMPACT.json"},
            "methodology": {"repository": "opensiro/vsm-harness-skills", "source_kind": "release",
                            "ref": "v0.3.7", "version": "0.3.7",
                            "version_path": "skills/assess-vsm-harness/VERSION"},
            "index": {"repository": "opensiro/vsm-harness-index", "source_kind": "branch",
                      "ref": "main", "active_contract_path": "data/active-contract.psv"},
        }
        self.active_contract = "profile_version|methodology_version\n0.2.4|0.3.7\n"
        self.impact = {"profile": "opensiro/vsm-harness-profile", "releases": [
            {"version": "0.2.4", "previous": "0.2.3", "compatibility": "compatible",
             "assessment_impact": "none"}
        ]}
        self.mutate_during_recheck = False
        self.organization_head_calls = 0

    def get(self, path):
        parsed = urlsplit(path)
        parts = [unquote(part) for part in parsed.path.strip("/").split("/")]
        assert parts[0] == "repos", path
        repo = "/".join(parts[1:3])
        if len(parts) == 3:
            return {"default_branch": "main"}
        if parts[3] == "commits":
            ref = parts[4]
            if ref == "main":
                if repo == snapshot.ORG:
                    self.organization_head_calls += 1
                    if self.mutate_during_recheck and self.organization_head_calls > 2:
                        return {"sha": "f" * 40}
                return {"sha": self.heads[repo]}
            return {"sha": self.refs[(repo, ref)]}
        if parts[3] == "contents":
            content_path = "/".join(parts[4:])
            if repo == snapshot.ORG and content_path == "README.md":
                data = "Current in-scope public repositories:\n\n" + "\n".join(
                    f"- `{name}`" for name in SCOPE
                ) + "\n\nNext section"
            elif repo == snapshot.ORG and content_path == "UPSTREAM_CONTRACT.json":
                data = json.dumps(self.selected)
            elif content_path == "VERSION":
                data = "0.2.4\n"
            elif content_path == "skills/assess-vsm-harness/VERSION":
                data = "0.3.7\n"
            elif content_path == "data/active-contract.psv":
                data = self.active_contract
            elif content_path == "RELEASE_IMPACT.json":
                data = json.dumps(self.impact)
            else:
                raise AssertionError(path)
            return {"encoding": "base64", "content": base64.b64encode(data.encode()).decode()}
        raise AssertionError(path)


class SnapshotTests(unittest.TestCase):
    def test_control_plane_exposes_read_only_command(self):
        menu = (ROOT / "docs" / "AGENT_CONTROL_PLANE.md").read_text(encoding="utf-8")
        guide = (ROOT / "docs" / "OSS_SNAPSHOT.md").read_text(encoding="utf-8")
        self.assertIn("| **OSS Snapshot** | `snapshot` |", menu)
        self.assertIn("| `snapshot` / `OSS snapshot` |", menu)
        self.assertIn("python3 scripts/oss_snapshot.py", guide)
        self.assertIn("no remote writes", guide)

    def test_verified_snapshot_records_all_six_heads_and_selected_release_refs(self):
        client = FakeGitHub()
        result = snapshot.capture(client)
        self.assertEqual(result["result"], "CHECKED_DETERMINISTIC_CONTRACT")
        self.assertEqual([r["repository"] for r in result["repositories"]], SCOPE)
        self.assertEqual(result["selected_sources"]["profile"]["sha"], "a" * 40)
        self.assertNotEqual(result["selected_sources"]["profile"]["sha"],
                            client.heads["opensiro/vsm-harness-profile"])
        self.assertEqual(result["index_active_contract"]["methodology_version"], "0.3.7")

    def test_methodology_drift_fails_closed(self):
        client = FakeGitHub()
        client.active_contract = "profile_version|methodology_version\n0.2.4|0.3.8\n"
        with self.assertRaisesRegex(snapshot.SnapshotError, "differs"):
            snapshot.capture(client)

    def test_nonzero_profile_transition_fails_closed(self):
        client = FakeGitHub()
        client.active_contract = "profile_version|methodology_version\n0.2.3|0.3.7\n"
        client.impact["releases"][0]["assessment_impact"] = "targeted"
        with self.assertRaisesRegex(snapshot.SnapshotError, "explicit review"):
            snapshot.capture(client)

    def test_compatible_profile_transition_is_recorded_without_migration(self):
        client = FakeGitHub()
        client.active_contract = "profile_version|methodology_version\n0.2.3|0.3.7\n"
        result = snapshot.capture(client)
        self.assertEqual(result["index_active_contract"]["profile_version"], "0.2.3")
        self.assertEqual(result["checks"]["profile_compatibility"], "PASS")

    def test_changed_branch_head_fails_closed(self):
        client = FakeGitHub()
        client.mutate_during_recheck = True
        with self.assertRaisesRegex(snapshot.SnapshotError, "head changed"):
            snapshot.capture(client)

    def test_selected_release_must_match_pinned_version(self):
        client = FakeGitHub()
        client.selected["methodology"]["version"] = "0.3.8"
        with self.assertRaisesRegex(snapshot.SnapshotError, "release ref"):
            snapshot.capture(client)


if __name__ == "__main__":
    unittest.main()
