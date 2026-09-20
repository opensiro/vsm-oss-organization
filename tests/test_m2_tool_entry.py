from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class M2ExternalToolEntryTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def load_json(self, relative: str) -> dict:
        return json.loads(self.read(relative))

    def test_contract_preserves_function_mechanism_boundary(self) -> None:
        contract = self.read("EXTERNAL_TOOL_ENTRY.md")

        self.assertIn("tool does **not** become S1, S2, S3, S3*, S4, or S5", contract)
        self.assertIn("The tool never widens organizational authority on its own", contract)
        self.assertIn("Parent approval of a tool action is **not automatically an S5 event**", contract)
        self.assertIn("## Failure / drift behavior", contract)
        self.assertIn("## Re-entry triggers", contract)

    def test_schema_has_required_entry_surfaces(self) -> None:
        schema = self.load_json("schemas/external-tool-entry.schema.json")
        required = set(schema["required"])

        for marker in (
            "external_boundary",
            "connection_owner",
            "runtime_users",
            "technical_permissions",
            "action_policy",
            "revocation",
            "failure_behavior",
            "reentry_triggers",
            "evidence_retention",
        ):
            self.assertIn(marker, required)

        action_required = set(schema["$defs"]["action"]["required"])
        self.assertEqual(action_required, {"class", "actions", "rationale"})

    def test_github_entry_is_bounded_by_parent_and_scope(self) -> None:
        entry = self.load_json("entries/tools/github-chatgpt.json")

        self.assertEqual(entry["connection_owner"]["role"], "OpenSiro organization owner")
        self.assertEqual(entry["connection_owner"]["authority_ref"], "S5_PARENT_AUTHORITY.md")

        resources = set(entry["external_boundary"]["resources"])
        self.assertEqual(
            resources,
            {
                "opensiro/vsm-harness-profile",
                "opensiro/vsm-harness-skills",
                "opensiro/vsm-harness-index",
                "opensiro/awesome-vsm-harness",
                "opensiro/vsm-oss-organization",
            },
        )

        delegated = entry["action_policy"]["delegated"]
        parent_gated = entry["action_policy"]["parent_gated"]
        forbidden = entry["action_policy"]["forbidden"]

        self.assertTrue(any(item["class"] == "READ_ONLY" for item in delegated))
        self.assertTrue(any(item["class"] == "BOUNDED_MUTATION" for item in delegated))
        self.assertTrue(any(item["class"] == "INTEGRATION_SENSITIVE" for item in parent_gated))
        self.assertTrue(any(item["class"] == "POLICY_SECURITY_SENSITIVE" for item in parent_gated))
        self.assertTrue(any(item["class"] == "FORBIDDEN" for item in forbidden))

    def test_github_entry_fails_closed_on_drift(self) -> None:
        entry = self.load_json("entries/tools/github-chatgpt.json")
        failure_text = " ".join(entry["failure_behavior"])
        reentry_text = " ".join(entry["reentry_triggers"])

        self.assertIn("stop the affected mutation", failure_text)
        self.assertIn("report permission/resource drift explicitly", failure_text)
        self.assertIn("technical permissions materially expand or contract", reentry_text)
        self.assertIn("parent/delegation policy changes", reentry_text)


if __name__ == "__main__":
    unittest.main()
