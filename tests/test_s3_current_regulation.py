"""Source-first S3 standing-regulation operating-path tests, not semantic grade tests."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

SRC = Path(__file__).resolve().parents[1] / "scripts" / "s3_current_regulation.py"
SPEC = importlib.util.spec_from_file_location("s3_current_regulation", SRC)
assert SPEC and SPEC.loader
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

REGISTRY = Path(__file__).resolve().parents[1] / "control" / "s3-standing-commitments.json"
GRANT = Path(__file__).resolve().parents[1] / "contracts" / "s3" / "parent-assisted-g1.md"


def temp_inputs(base: Path, *, selected="0.3.7", index_method="0.3.7"):
    org, index, skills, awesome = [base / x for x in ("org", "index", "skills", "awesome")]
    (org / "control").mkdir(parents=True)
    (org / "contracts" / "s3").mkdir(parents=True)
    (index / "data").mkdir(parents=True)
    (skills / "skills" / "assess-vsm-harness").mkdir(parents=True)
    (awesome / ".github" / "workflows").mkdir(parents=True)
    (org / "UPSTREAM_CONTRACT.json").write_text(json.dumps({
        "profile": {"version": "0.2.4"},
        "methodology": {"version": selected},
    }), encoding="utf-8")
    (org / "control" / "s3-standing-commitments.json").write_text(
        REGISTRY.read_text(encoding="utf-8"), encoding="utf-8")
    (org / "contracts" / "s3" / "parent-assisted-g1.md").write_text(
        GRANT.read_text(encoding="utf-8"), encoding="utf-8")
    (index / "data" / "active-contract.psv").write_text(
        "profile_version|methodology_version\n0.2.4|" + index_method + "\n", encoding="utf-8")
    (skills / "skills" / "assess-vsm-harness" / "VERSION").write_text(
        selected + "\n", encoding="utf-8")
    (awesome / ".github" / "workflows" / "index-consistency.yml").write_text(
        "repository: opensiro/vsm-harness-index\n"
        "run: python scripts/validate_index_consistency.py --index-dir ../index\n",
        encoding="utf-8")
    return org, index, skills, awesome


def sample_case():
    return {
        "schema_version": 1,
        "kind": "nonlocal_current_commitment",
        "commitment_id": "canonical-publication-continuity",
        "active_s1_work": [
            {"domain": "Index", "work_ref": "https://github.com/opensiro/vsm-harness-index/issues/1567",
             "admission_ref": "https://github.com/opensiro/vsm-harness-index/issues/1567",
             "commitment": "Canonical evidence remains Index-owned"},
            {"domain": "Awesome", "work_ref": "https://github.com/opensiro/awesome-vsm-harness/issues/7",
             "admission_ref": "https://github.com/opensiro/awesome-vsm-harness/issues/7",
             "commitment": "Curated downstream links remain canonical"},
        ],
        "nonlocal_evidence_refs": [
            "https://github.com/opensiro/vsm-harness-index/issues/1567",
            "https://github.com/opensiro/awesome-vsm-harness/issues/7",
        ],
        "shared_current_constraint": "Hypothetical shared current publication timing tradeoff — fixture only",
        "why_s1_s2_cannot_decide": "Fixture asserts no one S1 can decide both commitments",
        "return_target": "https://github.com/opensiro/awesome-vsm-harness/issues/7",
        "rollback_condition": "Fixture rollback once both owners acknowledge",
        "requires_owner_confirmation": True,
    }


class StandingRegulationTests(unittest.TestCase):
    def test_observes_real_shipped_operating_obligations(self):
        with TemporaryDirectory() as temp:
            view = mod.observe(*temp_inputs(Path(temp)))
        self.assertEqual("CURRENT_SHARED_CONTRACT_ALIGNED", view["current_contract_state"])
        self.assertTrue(view["awesome_consumes_canonical_index"])
        self.assertEqual(2, len(view["standing_commitments"]))
        self.assertEqual("0.3.7", view["selected_methodology"])
        self.assertIn("NOT_S3_C_GRADE", view["assessment_boundary"])

    def test_contract_drift_is_observed_not_auto_s3_decision(self):
        with TemporaryDirectory() as temp:
            view = mod.observe(*temp_inputs(Path(temp), index_method="0.3.6"))
        self.assertEqual("CURRENT_SHARED_CONTRACT_DRIFT", view["current_contract_state"])
        self.assertNotIn("chosen_option", view)

    def test_nonlocal_candidate_prepares_unselected_bounded_return_options(self):
        with TemporaryDirectory() as temp:
            view = mod.observe(*temp_inputs(Path(temp)))
        packet = mod.candidate_packet(view, sample_case())
        self.assertEqual("UNADMITTED_G1_HUMAN_OPTION_PACKET", packet["disposition"])
        self.assertEqual({"CONTINUE", "REQUIRE_REPAIR", "SET_CONSTRAINT"},
                         {o["class"] for o in packet["options"]})
        self.assertIsNone(packet["chosen_option"])
        self.assertIsNone(packet["decision_ref"])
        self.assertIsNone(packet["S1_application_ref"])
        self.assertIn("awesome-vsm-harness/issues/7", packet["return_target"])

    def test_local_work_stays_s1(self):
        with TemporaryDirectory() as temp:
            view = mod.observe(*temp_inputs(Path(temp)))
        obj = mod.candidate_packet(view, {"schema_version": 1, "kind": "local_s1_repair"})
        self.assertEqual("ROUTE_LOCAL_S1", obj["disposition"])
        self.assertNotIn("options", obj)

    def test_contract_selection_is_s5_not_s3(self):
        with TemporaryDirectory() as temp:
            view = mod.observe(*temp_inputs(Path(temp)))
        obj = mod.candidate_packet(view, {"schema_version": 1, "kind": "s5_contract_selection"})
        self.assertEqual("ROUTE_S5_POLICY", obj["disposition"])
        self.assertNotIn("options", obj)

    def test_one_affected_s1_can_receive_truly_nonlocal_regulation(self):
        with TemporaryDirectory() as temp:
            view = mod.observe(*temp_inputs(Path(temp)))
        case = sample_case()
        case["active_s1_work"] = case["active_s1_work"][1:]
        packet = mod.candidate_packet(view, case)
        self.assertEqual("UNADMITTED_G1_HUMAN_OPTION_PACKET", packet["disposition"])
        self.assertEqual(1, len(packet["candidate_current_view"]))

    def test_no_named_current_s1_work_cannot_qualify(self):
        with TemporaryDirectory() as temp:
            view = mod.observe(*temp_inputs(Path(temp)))
        case = sample_case()
        case["active_s1_work"] = []
        with self.assertRaisesRegex(mod.RegulationError, "at least one"):
            mod.candidate_packet(view, case)

    def test_nonlocal_authority_requires_distinct_s1_source_evidence(self):
        with TemporaryDirectory() as temp:
            view = mod.observe(*temp_inputs(Path(temp)))
        case = sample_case()
        case["active_s1_work"] = case["active_s1_work"][1:]
        case["nonlocal_evidence_refs"] = [
            "https://github.com/opensiro/awesome-vsm-harness/issues/7",
            "https://github.com/opensiro/awesome-vsm-harness/issues/5",
        ]
        with self.assertRaisesRegex(mod.RegulationError, "across two S1 domains"):
            mod.candidate_packet(view, case)

    def test_no_unapproved_owner_packet(self):
        with TemporaryDirectory() as temp:
            view = mod.observe(*temp_inputs(Path(temp)))
        case = sample_case()
        case["requires_owner_confirmation"] = False
        with self.assertRaisesRegex(mod.RegulationError, "pre-approve"):
            mod.candidate_packet(view, case)

    def test_no_unscoped_return(self):
        with TemporaryDirectory() as temp:
            view = mod.observe(*temp_inputs(Path(temp)))
        case = sample_case()
        case["return_target"] = "https://github.com/opensiro/vsm-harness-skills/issues/49"
        with self.assertRaisesRegex(mod.RegulationError, "target a current named"):
            mod.candidate_packet(view, case)


if __name__ == "__main__":
    unittest.main()
