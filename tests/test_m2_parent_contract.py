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

    def test_parent_prompt_rejects_shortcuts(self) -> None:
        prompt = self.read("prompts/parent-control-plane.md")

        self.assertIn("Apply function first, ownership second", prompt)
        self.assertIn("If ordinary S1, S3, or S3* authority can safely close it", prompt)
        self.assertIn("record INSUFFICIENT_AUTHORITY", prompt)
        self.assertIn("do not claim S5=P completion", prompt)


if __name__ == "__main__":
    unittest.main()
