"""Offline negative tests for the S3 transaction structural guard; not S3 witnesses."""
import copy
import importlib.util
import unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_s3_current_control.py"
SPEC = importlib.util.spec_from_file_location("check_s3_current_control", PATH)
assert SPEC and SPEC.loader
s = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(s)

ORG = "https://github.com/opensiro/vsm-oss-organization/issues/39"
S1 = "https://github.com/opensiro/vsm-harness-index/issues/1450"
S1_ALT = "https://github.com/opensiro/vsm-harness-skills/issues/49"


def packet(state="REQUESTED"):
    return {
        "control_version": "1",
        "transaction_id": "s3-test-only-not-a-real-run",
        "system_in_focus": "bounded Opensiro OSS",
        "status": state,
        "trigger": {"kind": "other_current_control_need", "summary": "test-only structural input",
                    "evidence_refs": [ORG]},
        "current_view": {"active_s1_refs": [S1, S1_ALT], "commitments": ["source-backed obligation"],
                         "constraints": ["concrete current constraint"],
                         "resource_or_priority_context": []},
        "requested_decision": {"decision_right": "test-only bounded organizational decision",
                               "allowed_classes": ["CONTINUE", "STOP"],
                               "authority_boundary": "test-only; not an authorization"},
        "decision": {"owner_class": "unknown", "owner_ref": ORG,
                     "class": None, "instruction": None, "evidence_refs": []},
        "support_and_enforcement": [{"mechanism": "CI", "role": "validator, not decision owner",
                                     "evidence_ref": ORG}],
        "return_to_s1": {"target_work_refs": [S1], "acknowledgement_ref": None,
                         "application_summary": None, "effect_refs": []},
        "closure": {"final_status": None, "summary": None, "evidence_refs": []},
    }


def decided():
    t = packet("DECIDED")
    t["decision"].update(owner_class="human", owner_ref=ORG, **{"class": "CONTINUE"},
                         instruction="test-only instruction", evidence_refs=[ORG])
    return t


def applied():
    t = decided()
    t["status"] = "APPLIED"
    t["return_to_s1"].update(acknowledgement_ref=S1, application_summary="test-only application",
                             effect_refs=[S1])
    return t


def closed():
    t = applied()
    t["status"] = "CLOSED"
    t["closure"] = {"final_status": "CLOSED", "summary": "test-only completion", "evidence_refs": [ORG]}
    return t


class S3StructuralGuardTests(unittest.TestCase):
    def assertBlocked(self, obj):
        with self.assertRaises(s.InvalidS3Transaction):
            s.validate(obj)

    def test_all_four_valid_structural_shapes_are_not_function_witnesses(self):
        for obj in (packet(), decided(), applied(), closed()):
            self.assertEqual("STRUCTURALLY_VALID_NOT_S3_FUNCTION_WITNESS", s.validate(obj))

    def test_current_placeholder_template_is_not_falsely_admitted(self):
        import json
        p = PATH.parents[1] / "control" / "s3-current-control-v1.template.json"
        self.assertBlocked(json.loads(p.read_text(encoding="utf-8")))

    def test_requested_cannot_claim_decision_or_closure(self):
        for change in (
            lambda t: t["decision"].update(**{"class": "STOP"}),
            lambda t: t["return_to_s1"].update(acknowledgement_ref=S1),
            lambda t: t["closure"].update(final_status="CLOSED"),
        ):
            t = packet()
            change(t)
            self.assertBlocked(t)

    def test_decided_cannot_fake_s1_effect_or_lack_owner(self):
        for change in (
            lambda t: t["decision"].update(owner_class="unknown"),
            lambda t: t["decision"].update(evidence_refs=[]),
            lambda t: t["return_to_s1"].update(effect_refs=[S1]),
            lambda t: t["decision"].update(**{"class": "SET_CONSTRAINT"}),
        ):
            t = decided()
            change(t)
            self.assertBlocked(t)

    def test_applied_and_closed_require_real_shape_of_effect_and_closure(self):
        for change in (
            lambda t: t["return_to_s1"].update(effect_refs=[]),
            lambda t: t["closure"].update(final_status="CLOSED"),
            lambda t: t["return_to_s1"].update(acknowledgement_ref=None),
        ):
            t = applied()
            change(t)
            self.assertBlocked(t)
        for change in (
            lambda t: t["closure"].update(final_status="APPLIED"),
            lambda t: t["closure"].update(evidence_refs=[]),
        ):
            t = closed()
            change(t)
            self.assertBlocked(t)

    def test_s1_target_must_be_real_domain_work_in_current_view(self):
        for change in (
            lambda t: t["return_to_s1"].update(target_work_refs=[ORG]),
            lambda t: t["return_to_s1"].update(target_work_refs=[S1_ALT+"-not-in-view"]),
            lambda t: t["current_view"].update(active_s1_refs=[ORG]),
        ):
            t = packet()
            change(t)
            self.assertBlocked(t)

    def test_no_placeholder_or_external_unattributed_references(self):
        for change in (
            lambda t: t.update(transaction_id="<placeholder>"),
            lambda t: t["trigger"].update(evidence_refs=["https://example.org/fake"]),
            lambda t: t["decision"].update(owner_ref="<not-authorized>"),
            lambda t: t["current_view"].update(constraints=[]),
            lambda t: t["requested_decision"].update(allowed_classes=["STOP","STOP"]),
            lambda t: t["support_and_enforcement"][0].update(evidence_ref="main"),
        ):
            t = packet()
            change(t)
            self.assertBlocked(t)

    def test_terminal_abort_without_decision_is_allowed_but_requires_actual_owner_and_receipt(self):
        for state in ("ESCALATED", "CANCELLED"):
            t = packet(state)
            t["decision"]["owner_class"] = "human"
            t["closure"] = {"final_status": state, "summary": "test-only abort", "evidence_refs": [ORG]}
            self.assertEqual("STRUCTURALLY_VALID_NOT_S3_FUNCTION_WITNESS", s.validate(t))
            t["closure"]["evidence_refs"] = []
            self.assertBlocked(t)

    def test_valid_adjacent_transitions(self):
        pairs = [
            (packet(), decided()), (decided(), applied()), (applied(), closed()),
        ]
        for earlier, later in pairs:
            self.assertEqual("STRUCTURAL_TRANSITION_VALID_NOT_AUTHORITY_OR_S3_WITNESS",
                             s.validate_transition(earlier, later))

    def test_skipping_and_terminal_rewrites_fail(self):
        for before, after in (
            (packet(), applied()), (packet(), closed()), (decided(), closed()),
            (closed(), decided()), (closed(), closed()),
        ):
            with self.assertRaises(s.InvalidS3Transaction):
                s.validate_transition(before, after)

    def test_mutating_decision_scope_and_existing_effect_fails(self):
        n = applied()
        n["decision"]["instruction"] = "changed after original decision"
        with self.assertRaisesRegex(s.InvalidS3Transaction, "decided instruction"):
            s.validate_transition(decided(), n)
        n = applied()
        n["return_to_s1"]["application_summary"] = "rewritten"
        n["status"] = "CLOSED"
        n["closure"] = {"final_status": "CLOSED", "summary": "test-only", "evidence_refs": [ORG]}
        with self.assertRaisesRegex(s.InvalidS3Transaction, "already applied"):
            s.validate_transition(applied(), n)
        n = decided()
        n["requested_decision"]["authority_boundary"] = "new scope"
        with self.assertRaisesRegex(s.InvalidS3Transaction, "immutable"):
            s.validate_transition(packet(), n)

    def test_unknown_fields_fail_closed(self):
        t = packet()
        t["decision"]["pretend_s3_a"] = True
        self.assertBlocked(t)


if __name__ == "__main__":
    unittest.main()
