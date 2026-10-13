"""Contract smoke test for the source-first S3 Control Plane menu action."""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MENU = ROOT / "docs" / "AGENT_CONTROL_PLANE.md"
INTAKE = ROOT / "prompts" / "intake-s3-current-control.md"
RECORD = ROOT / "templates" / "s3-control-record.md"
TRANSACTION = ROOT / "control" / "s3-current-control-v1.template.json"


class S3ControlPlaneMenuTests(unittest.TestCase):
    def test_menu_action_and_command_match_canonical_intake(self):
        menu = MENU.read_text(encoding="utf-8")
        intake = INTAKE.read_text(encoding="utf-8")
        self.assertIn("| **Current Control (S3)** | `S3: inspect current control` |", menu)
        self.assertIn("## S3 current-control intake (M1)", menu)
        self.assertIn("S3: consider <present choice>", menu)
        self.assertIn("S3: inspect current control", intake)
        self.assertIn("S3: consider <present Organization-wide choice / existing S1 work refs>", intake)

    def test_authority_and_witness_boundaries_stay_explicit(self):
        menu = MENU.read_text(encoding="utf-8")
        section = menu.split("## S3 current-control intake (M1)", 1)[1].split(
            "## External upstream contributions", 1
        )[0]
        for text in (
            "read-only",
            "no S3 transaction",
            "legitimate authority",
            "S1 return targets",
            "The actual owner must make the decision",
            "no `S3=C` promotion",
            "S3* Audit",
            "M1 #39",
        ):
            self.assertIn(text, section)
        self.assertNotIn("auto-admit", section)


    def test_s3_record_references_live_authority(self):
        record = RECORD.read_text(encoding="utf-8")
        self.assertNotIn("S3_CONTROL_SURFACE.md", record)
        for relative in (
            "../contracts/s3/current-control.md",
            "../control/s3-current-control-v1.template.json",
        ):
            with self.subTest(relative=relative):
                self.assertIn(f"]({relative})", record)
                self.assertTrue((RECORD.parent / relative).is_file())



    def test_requested_s3_template_has_no_decision_or_closure(self):
        transaction = json.loads(TRANSACTION.read_text(encoding="utf-8"))
        self.assertEqual("REQUESTED", transaction["status"])
        self.assertIsNone(transaction["decision"]["class"])
        self.assertIsNone(transaction["decision"]["instruction"])
        self.assertEqual([], transaction["decision"]["evidence_refs"])
        self.assertIsNone(transaction["return_to_s1"]["acknowledgement_ref"])
        self.assertIsNone(transaction["return_to_s1"]["application_summary"])
        self.assertEqual([], transaction["return_to_s1"]["effect_refs"])
        self.assertIsNone(transaction["closure"]["final_status"])
        self.assertIsNone(transaction["closure"]["summary"])
        self.assertEqual([], transaction["closure"]["evidence_refs"])



if __name__ == "__main__":
    unittest.main()
