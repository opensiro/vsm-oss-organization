from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class M2ParentBoundaryTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_parent_contract_is_preparatory_not_positive_claim(self) -> None:
        contract = self.read("S5_PARENT_BOUNDARY.md")

        self.assertIn("does **not** establish `S5=P`", contract)
        self.assertIn("The active formal roadmap milestone remains M1", contract)
        self.assertIn("Repository authorship, maintainer status, merge capability", contract)

    def test_parent_contract_requires_function_and_return(self) -> None:
        contract = self.read("S5_PARENT_BOUNDARY.md")

        for marker in (
            "## Delegated local envelope",
            "## Reserved S5 matters",
            "## Legitimate parent",
            "## Escalation admission",
            "## Return and closure",
            "## Support and enforcement boundary",
        ):
            self.assertIn(marker, contract)

        self.assertIn("identity / ultimate-policy", contract)
        self.assertIn("subsequent operation governed by returned decision", contract)

    def test_current_parent_authority_is_explicit(self) -> None:
        authority = self.read("S5_PARENT_AUTHORITY.md")

        self.assertIn("**OpenSiro organization owner**", authority)
        self.assertIn("GitHub identity: `xLagerFeuer`", authority)
        self.assertIn("authority recorded here comes from this explicit Organization governance declaration", authority)
        self.assertIn("Continuity for the routing-scope decision", authority)
        self.assertIn("issue #59 / PR #62", authority)
        self.assertIn("Changing the legitimate parent role", authority)

    def test_parent_record_separates_owner_support_and_closure(self) -> None:
        record = self.read("templates/s5-parent-decision-record.md")

        for marker in (
            "legitimate parent role:",
            "concrete decision owner:",
            "primary evidence of parent legitimacy:",
            "decisive S5 right:",
            "## Support / enforcement",
            "## Return into Organization",
            "## Closure",
        ):
            self.assertIn(marker, record)

        self.assertIn("INSUFFICIENT_AUTHORITY", record)

    def test_first_reconstructed_witness_preserves_boundary(self) -> None:
        witness = self.read("records/s5/2026-09-18-routing-scope-correction.md")

        self.assertIn("decision / work item id: `S5-P-001`", witness)
        self.assertIn("concrete decision owner: `xLagerFeuer`", witness)
        self.assertIn("does this record support a positive `S5=P` witness? `YES`", witness)
        self.assertIn("retrospective reconstruction", witness)
        self.assertIn("does **not** formally complete M2 while M1 remains open", witness)

    def test_parent_prompt_rejects_shortcuts_and_supports_contributor_invocation(self) -> None:
        prompt = self.read("prompts/parent-control-plane.md")

        self.assertIn("S5: рассмотреть <matter>", prompt)
        self.assertIn("S5: consider <matter>", prompt)
        self.assertIn("Any contributor may initiate S5 admission/review", prompt)
        self.assertIn("S5_ADMITTED", prompt)
        self.assertIn("POLICY_ALREADY_GOVERNS", prompt)
        self.assertIn("NOT_S5", prompt)
        self.assertIn("INSUFFICIENT_AUTHORITY", prompt)
        self.assertIn("not a transfer of S5 ownership to the contributor invoking it", prompt)
        self.assertIn("Do not manufacture a new S5 event", prompt)
        self.assertIn("Apply function first, ownership second", prompt)
        self.assertIn("If ordinary S1, S3, or S3* authority can safely close the matter", prompt)
        self.assertIn("must not exercise unresolved s5 discretion", prompt.lower())
        self.assertIn("do not infer a new s5 witness merely because this prompt was invoked", prompt.lower())


if __name__ == "__main__":
    unittest.main()
