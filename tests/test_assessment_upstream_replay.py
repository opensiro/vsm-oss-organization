"""Static conformance guard for fresh assessment→upstream Control Plane replay.

These source checks deliberately do not pretend to test an agent's independent
discovery, actual GitHub stage authorization or native product benefit.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "docs" / "AGENT_CONTROL_PLANE.md"
PROTOCOL = ROOT / "docs" / "ASSESSMENT_UPSTREAM_REPLAY.md"
RECEIPT = ROOT / "docs" / "reviews" / "2026-10-22-assessment-upstream-prior-case.md"
DOCS_INDEX = ROOT / "docs" / "README.md"
PROMPT = ROOT / "prompts" / "assessment-upstream-fresh-replay.md"


class AssessmentUpstreamReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.control = CONTROL.read_text(encoding="utf-8")
        cls.protocol = PROTOCOL.read_text(encoding="utf-8")
        cls.receipt = RECEIPT.read_text(encoding="utf-8")
        cls.docs = DOCS_INDEX.read_text(encoding="utf-8")
        cls.prompt = PROMPT.read_text(encoding="utf-8")

    def test_fresh_control_plane_command_and_routing(self):
        self.assertIn("test S1 function: upstream contributions", self.control)
        self.assertIn("ASSESSMENT_UPSTREAM_REPLAY.md", self.control)
        self.assertIn("FRESH_INDEX_FIRST", self.control)
        self.assertIn("CONTINUE_PINNED_CASE", self.control)
        self.assertIn("ASSESSMENT_UPSTREAM_REPLAY.md", self.docs)

    def test_fresh_route_does_not_disclose_previous_target(self):
        fresh = self.protocol.split("## FRESH_INDEX_FIRST", 1)[1].split("## CONTINUE_PINNED_CASE", 1)[0]
        for hidden in ("AgentBox", "Agent Code", "HarnessDesk", "Kit #222", "PR #72"):
            with self.subTest(hidden=hidden):
                self.assertNotIn(hidden, fresh)
        for required in ("Selection firewall", "selection_lock", "assessment_path",
                         "review_ref", "counterexample_or_null", "selection_time/source_order",
                         "Index", "need", "mechanism", "counterfactual_value", "scope"):
            with self.subTest(required=required):
                self.assertIn(required, fresh)

    def test_new_chat_prompt_and_generic_route_hide_prior_case_target(self):
        self.assertIn("FRESH_INDEX_FIRST", self.prompt)
        self.assertIn("test S1 function: upstream contributions", self.prompt)
        self.assertIn("selection", self.protocol.lower())
        for text in (self.protocol, self.prompt, self.docs):
            with self.subTest(area=text[:40]):
                self.assertNotIn("Agent" + "Box", text)
                self.assertNotIn("Harness" + "Desk", text)
                self.assertNotIn("PR #72", text)
        self.assertIn("Agent" + "Box", self.receipt)

    def test_replay_is_not_fake_finished_native_intervention(self):
        for required in ("BENEFIT_NOT_MEASURED", "NOT_TESTED", "NO_ELIGIBLE_ASSESSMENT_CANDIDATE",
                         "BLOCKED_EVIDENCE", "native", "before/after", "external", "NULL"):
            with self.subTest(required=required):
                self.assertIn(required.lower(), self.protocol.lower())
        self.assertIn("not real product before/after", self.receipt.lower())
        self.assertIn("20/20 PASS", self.receipt)
        self.assertIn("not merged", self.receipt.lower())
        self.assertIn("unpublished", self.receipt.lower())

    def test_non_admitted_boundary_and_human_decision(self):
        for phrase in ("PROPOSED / NOT ADMITTED", "Organization #274",
                       "Upstream #6", "generic `продолжай`", "no write"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.protocol.lower())
        self.assertIn("not an admitted Organization S1 domain".lower(), self.protocol.lower())

    def test_replay_and_case_history_separate(self):
        self.assertIn("only in explicit", self.receipt)
        self.assertIn("CONTINUE_PINNED_CASE", self.receipt)
        self.assertIn("FRESH_INDEX_FIRST", self.receipt)
        self.assertIn("Upstream case #61", self.receipt)
        self.assertIn("Upstream experiment #56", self.receipt)


if __name__ == "__main__":
    unittest.main()
