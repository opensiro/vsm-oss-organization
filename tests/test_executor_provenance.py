from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

VALIDATOR_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_executor_witness.py"
VALIDATOR_SPEC = importlib.util.spec_from_file_location("validate_executor_witness", VALIDATOR_PATH)
assert VALIDATOR_SPEC and VALIDATOR_SPEC.loader
validator = importlib.util.module_from_spec(VALIDATOR_SPEC)
VALIDATOR_SPEC.loader.exec_module(validator)

PUBLISHER_PATH = Path(__file__).resolve().parents[1] / "scripts" / "publish_executor_evidence.py"
PUBLISHER_SPEC = importlib.util.spec_from_file_location("publish_executor_evidence", PUBLISHER_PATH)
assert PUBLISHER_SPEC and PUBLISHER_SPEC.loader
publisher = importlib.util.module_from_spec(PUBLISHER_SPEC)
PUBLISHER_SPEC.loader.exec_module(publisher)

BOT = "opensiro-executor[bot]"
HUMAN = "xLagerFeuer"


def make_event(
    *,
    seq: int,
    kind: str,
    actor: str,
    actor_identity: str,
    authority: str,
    previous: str,
    action_refs: list[dict] | None = None,
) -> dict:
    event = {
        "seq": seq,
        "event_id": f"run-001:{seq:04d}",
        "kind": kind,
        "actor": actor,
        "actor_identity": actor_identity,
        "observed_at": f"2026-09-19T00:00:{seq:02d}Z",
        "summary": f"observable event {seq}",
        "authority": authority,
        "affected_decision_right": "local execution path",
        "evidence_refs": [f"https://github.com/opensiro/vsm-harness-index/issues/{100 + seq}"],
        "action_refs": action_refs or [],
        "previous_event_digest": previous,
    }
    event["event_digest"] = validator.event_digest(event)
    return event


def valid_witness() -> dict:
    first = make_event(
        seq=1,
        kind="executor_decision",
        actor="executor",
        actor_identity=BOT,
        authority="inside_s1",
        previous="GENESIS",
    )
    second = make_event(
        seq=2,
        kind="executor_action",
        actor="executor",
        actor_identity=BOT,
        authority="inside_s1",
        previous=first["event_digest"],
        action_refs=[
            {
                "type": "commit",
                "immutable_ref": "https://github.com/opensiro/vsm-harness-index/commit/" + "d" * 40,
                "payload_sha256": "sha256:" + "e" * 64,
                "observed_actor_login": BOT,
            }
        ],
    )

    data = {
        "provenance_version": "1",
        "profile": "github_app_v1",
        "run": {
            "run_id": "run-001",
            "system_in_focus": "OpenSiro VSM Harness OSS organization",
            "s1_domain": "Index",
            "repository_boundary": ["opensiro/vsm-harness-index"],
            "work_item_ref": "https://github.com/opensiro/vsm-harness-index/issues/101",
            "start_revision": "a" * 40,
            "governing_role_or_prompt": {
                "ref": "https://github.com/opensiro/vsm-oss-organization/blob/" + "b" * 40 + "/roles/S1.md",
                "sha256": "c" * 64,
            },
            "upstream_contract_ref": "https://github.com/opensiro/vsm-oss-organization/blob/" + "b" * 40 + "/UPSTREAM_CONTRACT.json",
            "pre_start_human_constraints_ref": "sha256:" + "f" * 64,
            "post_start_human_input_channels": ["github-issue-comments"],
            "declared_human_github_logins": [HUMAN],
        },
        "attester": {
            "identity": BOT,
            "identity_type": "github_app",
            "verification_material_ref": "https://github.com/apps/opensiro-executor",
            "attestation_format": "github-app-actor+sha256-chain/v1",
            "trust_basis": "Short-lived installation token delivered only to the declared executor session.",
            "github_app": {
                "app_slug": "opensiro-executor",
                "app_id": 123,
                "installation_id": 456,
                "bot_login": BOT,
                "token_scope_repositories": ["opensiro/vsm-harness-index"],
                "token_permissions": {
                    "contents": "write",
                    "issues": "write",
                    "pull_requests": "write",
                },
                "token_delivery": "runtime_only_short_lived_installation_token",
            },
        },
        "pre_run_anchor": {
            "published_at": "2026-09-19T00:00:00Z",
            "immutable_ref": "https://github.com/opensiro/vsm-oss-organization/commit/" + "1" * 40,
            "payload_digest": "sha256:" + "2" * 64,
            "attestation_ref": "https://github.com/opensiro/vsm-oss-organization/commit/" + "1" * 40,
            "observed_actor_login": BOT,
        },
        "events": [first, second],
        "human_intervention_accounting": {
            "post_start_human_input_occurred": False,
            "human_intervention_occurred": False,
            "intervention_count": 0,
            "material_interventions_attributed": True,
            "s1_resumed_autonomously_after_intervention": "not_applicable",
            "unobserved_material_channel_known": False,
            "notes": "none",
        },
        "closure": {
            "closure_artifact_refs": ["https://github.com/opensiro/vsm-harness-index/pull/999"],
            "final_result_revision": "3" * 40,
            "run_record_digest": validator.run_record_digest([first, second]),
            "pre_run_anchor_ref": "https://github.com/opensiro/vsm-oss-organization/commit/" + "1" * 40,
            "escalation_occurred": False,
            "human_intervention_occurred": False,
        },
        "final_attestation": {
            "attester_identity": BOT,
            "observed_actor_login": BOT,
            "payload_digest": "",
            "attestation_ref": "https://github.com/opensiro/vsm-oss-organization/commit/" + "4" * 40,
            "verification_instructions_ref": "provenance/GITHUB_APP_EXECUTOR.md",
        },
        "review": {
            "actor_attribution_verified": False,
            "action_bindings_verified": False,
            "human_interventions_accounted_for": False,
            "event_order_integrity_verified": False,
            "decisive_agent_owned_loop_established": "insufficient",
            "provenance_verdict": "INSUFFICIENT",
            "note": "Second review not yet performed.",
        },
    }
    data["final_attestation"]["payload_digest"] = validator.final_binding_digest(data)
    return data


class ExecutorProvenanceTests(unittest.TestCase):
    def test_valid_github_app_witness_passes_local_validation(self) -> None:
        self.assertEqual([], validator.validate_witness(valid_witness()))

    def test_contributor_only_identity_is_rejected(self) -> None:
        data = valid_witness()
        data["run"]["declared_human_github_logins"].append(BOT)
        errors = validator.validate_witness(data)
        self.assertTrue(any("distinct executor identity failed" in error for error in errors))

    def test_executor_action_must_be_observed_as_app_actor(self) -> None:
        data = valid_witness()
        data["events"][1]["action_refs"][0]["observed_actor_login"] = HUMAN
        data["events"][1]["event_digest"] = validator.event_digest(data["events"][1])
        data["closure"]["run_record_digest"] = validator.run_record_digest(data["events"])
        data["final_attestation"]["payload_digest"] = validator.final_binding_digest(data)
        errors = validator.validate_witness(data)
        self.assertTrue(any("executor action must use declared App bot login" in error for error in errors))

    def test_broken_event_chain_is_rejected(self) -> None:
        data = valid_witness()
        data["events"][1]["previous_event_digest"] = "sha256:" + "0" * 64
        data["events"][1]["event_digest"] = validator.event_digest(data["events"][1])
        data["closure"]["run_record_digest"] = validator.run_record_digest(data["events"])
        data["final_attestation"]["payload_digest"] = validator.final_binding_digest(data)
        errors = validator.validate_witness(data)
        self.assertTrue(any("does not match prior event_digest" in error for error in errors))

    def test_unaccounted_human_intervention_is_rejected(self) -> None:
        data = valid_witness()
        intervention = make_event(
            seq=3,
            kind="human_intervention",
            actor="human",
            actor_identity=HUMAN,
            authority="human_intervention",
            previous=data["events"][1]["event_digest"],
        )
        data["events"].append(intervention)
        data["closure"]["run_record_digest"] = validator.run_record_digest(data["events"])
        data["final_attestation"]["payload_digest"] = validator.final_binding_digest(data)
        errors = validator.validate_witness(data)
        self.assertTrue(
            any("intervention_count does not match" in error for error in errors)
        )
        self.assertTrue(
            any("human_intervention_occurred does not match" in error for error in errors)
        )

    def test_final_binding_digest_detects_closure_change(self) -> None:
        data = valid_witness()
        original = data["final_attestation"]["payload_digest"]
        data["closure"]["closure_artifact_refs"].append(
            "https://github.com/opensiro/vsm-harness-index/issues/777"
        )
        self.assertNotEqual(original, validator.final_binding_digest(data))
        errors = validator.validate_witness(data)
        self.assertTrue(any("final_attestation.payload_digest: digest mismatch" in error for error in errors))

    def test_publisher_uses_create_only_run_paths(self) -> None:
        self.assertEqual(
            "provenance/runs/run-001/anchor.json",
            publisher.expected_path("run-001", "anchor", None),
        )
        self.assertEqual(
            "provenance/runs/run-001/events/0007.json",
            publisher.expected_path("run-001", "event", 7),
        )
        with self.assertRaises(ValueError):
            publisher.expected_path("run-001", "event", None)


if __name__ == "__main__":
    unittest.main()
