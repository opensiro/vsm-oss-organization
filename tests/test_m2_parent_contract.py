from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class M2ParentBoundaryTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_parent_contract_requires_real_witness_not_file_presence(self) -> None:
        contract = self.read("contracts/s5/parent-boundary.md")

        self.assertIn("does **not** establish `S5=P`", contract)
        self.assertIn("a real qualifying decision and returned closure are required", contract)
        self.assertIn("Repository authorship, maintainer status, merge capability", contract)

    def test_parent_contract_requires_function_and_return(self) -> None:
        contract = self.read("contracts/s5/parent-boundary.md")

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
        authority = self.read("contracts/s5/parent-authority.md")

        self.assertIn("**Opensiro organization owner**", authority)
        self.assertIn("GitHub identity: `xLagerFeuer`", authority)
        self.assertIn("explicit governance declaration", authority)
        self.assertIn("Historical continuity", authority)
        self.assertIn("issue #59 / PR #62", authority)
        self.assertIn("parent role and holder applied", authority)

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
        self.assertIn("A contributor may collect evidence", prompt)
        self.assertIn("S5_ADMITTED", prompt)
        self.assertIn("POLICY_ALREADY_GOVERNS", prompt)
        self.assertIn("NOT_S5", prompt)
        self.assertIn("INSUFFICIENT_AUTHORITY", prompt)
        self.assertIn("not a transfer of S5 ownership to the contributor invoking it", prompt)
        self.assertIn("Do not manufacture a new S5 event", prompt)
        self.assertIn("Apply function first, ownership second", prompt)
        self.assertIn("do not transfer unresolved S5 discretion", prompt)
        self.assertIn("does not by itself establish another witness", prompt)

    def test_contributor_entry_exposes_parent_governed_s5_without_transferring_authority(self) -> None:
        entry = self.read("CONTRIBUTOR_START.md")

        self.assertIn("## Parent-governed S5 entry", entry)
        self.assertIn("prompts/parent-control-plane.md", entry)
        self.assertIn("S5_ADMITTED", entry)
        self.assertIn("POLICY_ALREADY_GOVERNS", entry)
        self.assertIn("NOT_S5", entry)
        self.assertIn("INSUFFICIENT_AUTHORITY", entry)
        self.assertIn("do **not** transfer the unresolved S5 decisive right", entry)
        self.assertIn("S3 current-control", entry)

    def test_contributing_routes_live_state_to_its_owners(self) -> None:
        contributing = self.read("CONTRIBUTING.md")

        self.assertIn("GitHub milestones + their tracker issues", contributing)
        self.assertIn("TODO.md", contributing)
        self.assertIn("ROADMAP.md", contributing)
        self.assertIn("not a second planning authority", contributing)
        self.assertIn("Canonical general assessment publication", contributing)
        self.assertIn("Do not silently promote that snapshot into an Index fact", contributing)
        self.assertNotIn("## Current milestone: M1", contributing)
        self.assertNotIn("S1=A` is established from M0", contributing)

    def test_root_s5_names_are_compatibility_pointers_only(self) -> None:
        self.assertIn(
            "Canonical contract: [`contracts/s5/parent-boundary.md`]",
            self.read("S5_PARENT_BOUNDARY.md"),
        )
        self.assertIn(
            "Canonical declaration: [`contracts/s5/parent-authority.md`]",
            self.read("S5_PARENT_AUTHORITY.md"),
        )


if __name__ == "__main__":
    unittest.main()
