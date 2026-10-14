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
        for marker in ("## Delegated local envelope", "## Reserved S5 matters", "## Legitimate parent", "## Escalation admission", "## Return and closure", "## Support and enforcement boundary"):
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
        for marker in ("legitimate parent role:", "concrete decision owner:", "primary evidence of parent legitimacy:", "decisive S5 right:", "## Support / enforcement", "## Return into Organization", "## Closure"):
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
        for marker in ("S5: рассмотреть <matter>", "S5: consider <matter>", "A contributor may collect evidence", "S5_ADMITTED", "POLICY_ALREADY_GOVERNS", "NOT_S5", "INSUFFICIENT_AUTHORITY", "not a transfer of S5 ownership to the contributor invoking it", "Do not manufacture a new S5 event", "Apply function first, ownership second", "do not transfer unresolved S5 discretion", "does not by itself establish another witness"):
            self.assertIn(marker, prompt)

    def test_contributor_entry_exposes_parent_governed_s5_without_transferring_authority(self) -> None:
        entry = self.read("CONTRIBUTOR_START.md")
        self.assertIn("## Parent-governed S5 entry", entry)
        self.assertIn("prompts/parent-control-plane.md", entry)
        for marker in ("S5_ADMITTED", "POLICY_ALREADY_GOVERNS", "NOT_S5", "INSUFFICIENT_AUTHORITY"):
            self.assertIn(marker, entry)
        self.assertIn("does **not** transfer the unresolved S5 decisive right", entry)
        self.assertIn("S3 current-control", entry)

    def test_parent_governance_is_not_gated_by_s3_assessment(self) -> None:
        """Regression: a lack of S3 evidence may block a grade or case, not a parent choice."""
        authority = self.read("contracts/s5/parent-authority.md")
        boundary = self.read("contracts/s5/parent-boundary.md")
        prompt = self.read("prompts/parent-control-plane.md")
        entry = self.read("CONTRIBUTOR_START.md")
        control = self.read("docs/AGENT_CONTROL_PLANE.md")
        review = self.read("docs/reviews/2026-10-14-s5-s3-assessment-gate-inversion.md")

        self.assertIn("## Reserved decisions while parent-governed", authority)
        self.assertIn("INSUFFICIENT", authority)
        self.assertIn("prospective/conditional S3 authority", authority)
        self.assertIn("## Governance decision is not an assessment admission gate", boundary)
        self.assertIn("blocks that intervention", boundary)
        self.assertIn("blocks only the positive grade claim", boundary)
        self.assertIn("Three decisions must remain separate", prompt)
        self.assertIn("S5 domain-fit and delegation choices belong", entry)
        self.assertIn("## Parent S5 decision before assessment", control)
        self.assertIn("A particular **operational S3 action**", control)
        self.assertIn("Primary root cause", review)
        self.assertIn("VSM evidence assessment", review)
        self.assertIn("Stage-2", review)

    def test_s3_cp_target_and_g1_issued_but_not_grade_or_case(self) -> None:
        """S5 can grant conditional standing S3 rights without inventing C(P) evidence."""
        mandate = self.read("docs/proposals/2026-10-14-s3-parent-assisted-general-mandate.md")
        grant = self.read("contracts/s3/parent-assisted-g1.md")
        parent_record = self.read("records/s5/2026-10-14-s3-g1-parent-assisted-grant.md")
        s3_contract = self.read("contracts/s3/current-control.md")
        self.assertIn("S5 TARGET MODE `C(P)` SELECTED", mandate)
        self.assertIn("## 2A. Selected target mode `C(P)`", mandate)
        self.assertIn("**Base `C`**", mandate)
        self.assertIn("**Parent `P`**", mandate)
        self.assertIn("G1 HOLDER APPOINTED by S5", mandate)
        self.assertIn("NOT YET ESTABLISHED", mandate)
        self.assertIn("## 5. G1 holder and bounded conditional grant", mandate)
        self.assertIn("G1 — HUMAN_S3_HOLDER", mandate)
        self.assertIn("## Grant identity and effective window", grant)
        self.assertIn("GitHub merge-commit UTC timestamp", grant)
        self.assertIn("2026-11-13T12:00:00Z", grant)
        for marker in ("CONTINUE", "SET_CONSTRAINT", "REQUIRE_REPAIR", "STOP", "SET_RETRY_BUDGET", "OTHER_CURRENT_CONTROL"):
            self.assertIn(marker, grant)
        self.assertIn("NO_S3_CASE_OPENED", grant)
        self.assertIn("S5-P-G1-238", parent_record)
        self.assertIn("RETURN_PENDING_PUBLICATION", parent_record)
        self.assertIn("parent-assisted-g1.md", s3_contract)
        self.assertIn("does **not** establish `C(P)`", s3_contract)

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


if __name__ == "__main__":
    unittest.main()
