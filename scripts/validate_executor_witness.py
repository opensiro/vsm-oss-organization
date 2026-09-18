#!/usr/bin/env python3
"""Validate the GitHub-App executor provenance witness profile.

This validator checks local structural and hash-chain invariants only. It does
not replace independent inspection of the cited GitHub actor/action evidence.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

SHA40_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
RFC3339_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T")

ALLOWED_DOMAINS = {"Index", "Skills", "Awesome"}
ALLOWED_KINDS = {
    "executor_decision",
    "executor_action",
    "human_input",
    "human_intervention",
    "escalation",
    "support",
    "closure",
}
ALLOWED_ACTORS = {"executor", "human", "support"}
ALLOWED_AUTHORITIES = {
    "inside_s1",
    "outside_s1_escalation",
    "human_intervention",
    "support_only",
}
ALLOWED_ACTION_TYPES = {
    "commit",
    "issue_comment",
    "pull_request",
    "file_write",
    "other",
}
ALLOWED_PERMISSION_LEVELS = {"read", "write", "none"}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def canonical_digest(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(value)).hexdigest()


def event_digest(event: dict[str, Any]) -> str:
    payload = copy.deepcopy(event)
    payload.pop("event_digest", None)
    return canonical_digest(payload)


def run_record_digest(events: list[dict[str, Any]]) -> str:
    return canonical_digest({"event_digests": [event["event_digest"] for event in events]})


def final_binding_payload(data: dict[str, Any]) -> dict[str, Any]:
    run = data["run"]
    anchor = data["pre_run_anchor"]
    closure = data["closure"]
    return {
        "run_id": run["run_id"],
        "pre_run_anchor_ref": anchor["immutable_ref"],
        "run_record_digest": closure["run_record_digest"],
        "closure_artifact_refs": closure["closure_artifact_refs"],
        "final_result_revision": closure["final_result_revision"],
        "human_intervention_occurred": closure["human_intervention_occurred"],
        "escalation_occurred": closure["escalation_occurred"],
    }


def final_binding_digest(data: dict[str, Any]) -> str:
    return canonical_digest(final_binding_payload(data))


def _is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _require_dict(parent: dict[str, Any], key: str, context: str, errors: list[str]) -> dict[str, Any]:
    value = parent.get(key)
    if not isinstance(value, dict):
        errors.append(f"{context}.{key}: expected object")
        return {}
    return value


def _require_list(parent: dict[str, Any], key: str, context: str, errors: list[str]) -> list[Any]:
    value = parent.get(key)
    if not isinstance(value, list):
        errors.append(f"{context}.{key}: expected array")
        return []
    return value


def _require_string(parent: dict[str, Any], key: str, context: str, errors: list[str]) -> str:
    value = parent.get(key)
    if not _is_nonempty_string(value):
        errors.append(f"{context}.{key}: expected non-empty string")
        return ""
    return value


def _require_bool(parent: dict[str, Any], key: str, context: str, errors: list[str]) -> bool | None:
    value = parent.get(key)
    if not isinstance(value, bool):
        errors.append(f"{context}.{key}: expected boolean")
        return None
    return value


def validate_witness(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if data.get("provenance_version") != "1":
        errors.append("provenance_version: expected '1'")
    if data.get("profile") != "github_app_v1":
        errors.append("profile: expected 'github_app_v1'")

    run = _require_dict(data, "run", "root", errors)
    run_id = _require_string(run, "run_id", "run", errors)
    _require_string(run, "system_in_focus", "run", errors)
    domain = _require_string(run, "s1_domain", "run", errors)
    if domain and domain not in ALLOWED_DOMAINS:
        errors.append(f"run.s1_domain: expected one of {sorted(ALLOWED_DOMAINS)}")

    repository_boundary = _require_list(run, "repository_boundary", "run", errors)
    if not repository_boundary or any(not _is_nonempty_string(item) or "/" not in item for item in repository_boundary):
        errors.append("run.repository_boundary: expected at least one owner/repository string")

    _require_string(run, "work_item_ref", "run", errors)
    start_revision = _require_string(run, "start_revision", "run", errors)
    if start_revision and not SHA40_RE.fullmatch(start_revision):
        errors.append("run.start_revision: expected lowercase 40-hex commit SHA")

    role = _require_dict(run, "governing_role_or_prompt", "run", errors)
    _require_string(role, "ref", "run.governing_role_or_prompt", errors)
    role_sha = _require_string(role, "sha256", "run.governing_role_or_prompt", errors)
    if role_sha and not HEX64_RE.fullmatch(role_sha):
        errors.append("run.governing_role_or_prompt.sha256: expected lowercase 64-hex SHA-256")

    _require_string(run, "upstream_contract_ref", "run", errors)
    _require_string(run, "pre_start_human_constraints_ref", "run", errors)
    human_channels = _require_list(run, "post_start_human_input_channels", "run", errors)
    if any(not _is_nonempty_string(item) for item in human_channels):
        errors.append("run.post_start_human_input_channels: every item must be a non-empty string")

    declared_humans = _require_list(run, "declared_human_github_logins", "run", errors)
    if any(not _is_nonempty_string(item) for item in declared_humans):
        errors.append("run.declared_human_github_logins: every item must be a non-empty string")
    declared_human_set = {item for item in declared_humans if isinstance(item, str)}

    attester = _require_dict(data, "attester", "root", errors)
    identity = _require_string(attester, "identity", "attester", errors)
    if attester.get("identity_type") != "github_app":
        errors.append("attester.identity_type: expected 'github_app'")
    _require_string(attester, "verification_material_ref", "attester", errors)
    if attester.get("attestation_format") != "github-app-actor+sha256-chain/v1":
        errors.append("attester.attestation_format: expected github-app-actor+sha256-chain/v1")
    _require_string(attester, "trust_basis", "attester", errors)

    app = _require_dict(attester, "github_app", "attester", errors)
    app_slug = _require_string(app, "app_slug", "attester.github_app", errors)
    app_id = app.get("app_id")
    installation_id = app.get("installation_id")
    if not isinstance(app_id, int) or isinstance(app_id, bool) or app_id <= 0:
        errors.append("attester.github_app.app_id: expected positive integer")
    if not isinstance(installation_id, int) or isinstance(installation_id, bool) or installation_id <= 0:
        errors.append("attester.github_app.installation_id: expected positive integer")

    bot_login = _require_string(app, "bot_login", "attester.github_app", errors)
    if bot_login and not bot_login.endswith("[bot]"):
        errors.append("attester.github_app.bot_login: expected GitHub App bot login ending in '[bot]'")
    if identity and bot_login and identity != bot_login:
        errors.append("attester.identity must equal attester.github_app.bot_login")
    if bot_login and bot_login in declared_human_set:
        errors.append("distinct executor identity failed: bot login is also declared as a human GitHub identity")

    if app_slug:
        expected_ref = f"https://github.com/apps/{app_slug}"
        if attester.get("verification_material_ref") != expected_ref:
            errors.append(
                "attester.verification_material_ref must be the public GitHub App reference "
                f"{expected_ref!r}"
            )

    scoped_repositories = _require_list(app, "token_scope_repositories", "attester.github_app", errors)
    if any(not _is_nonempty_string(item) or "/" not in item for item in scoped_repositories):
        errors.append("attester.github_app.token_scope_repositories: expected owner/repository strings")
    boundary_set = {item for item in repository_boundary if isinstance(item, str)}
    scope_set = {item for item in scoped_repositories if isinstance(item, str)}
    if boundary_set and not boundary_set.issubset(scope_set):
        errors.append("attester.github_app.token_scope_repositories must cover run.repository_boundary")

    permissions = _require_dict(app, "token_permissions", "attester.github_app", errors)
    for permission_name, permission_level in permissions.items():
        if not _is_nonempty_string(permission_name) or permission_level not in ALLOWED_PERMISSION_LEVELS:
            errors.append(
                "attester.github_app.token_permissions: permission values must be read/write/none"
            )
            break
    if app.get("token_delivery") != "runtime_only_short_lived_installation_token":
        errors.append(
            "attester.github_app.token_delivery: expected runtime_only_short_lived_installation_token"
        )

    anchor = _require_dict(data, "pre_run_anchor", "root", errors)
    published_at = _require_string(anchor, "published_at", "pre_run_anchor", errors)
    if published_at and not RFC3339_PREFIX_RE.match(published_at):
        errors.append("pre_run_anchor.published_at: expected RFC3339-like timestamp")
    anchor_ref = _require_string(anchor, "immutable_ref", "pre_run_anchor", errors)
    anchor_digest = _require_string(anchor, "payload_digest", "pre_run_anchor", errors)
    if anchor_digest and not SHA256_RE.fullmatch(anchor_digest):
        errors.append("pre_run_anchor.payload_digest: expected sha256:<64-hex>")
    _require_string(anchor, "attestation_ref", "pre_run_anchor", errors)
    anchor_actor = _require_string(anchor, "observed_actor_login", "pre_run_anchor", errors)
    if bot_login and anchor_actor and anchor_actor != bot_login:
        errors.append("pre_run_anchor.observed_actor_login must equal App bot login")

    events_raw = _require_list(data, "events", "root", errors)
    events: list[dict[str, Any]] = []
    if not events_raw:
        errors.append("events: expected at least one material event")
    for index, raw in enumerate(events_raw, start=1):
        context = f"events[{index - 1}]"
        if not isinstance(raw, dict):
            errors.append(f"{context}: expected object")
            continue
        event = raw
        events.append(event)

        if event.get("seq") != index:
            errors.append(f"{context}.seq: expected contiguous sequence value {index}")
        _require_string(event, "event_id", context, errors)
        if event.get("kind") not in ALLOWED_KINDS:
            errors.append(f"{context}.kind: invalid event kind")
        if event.get("actor") not in ALLOWED_ACTORS:
            errors.append(f"{context}.actor: invalid actor class")
        actor_identity = _require_string(event, "actor_identity", context, errors)
        _require_string(event, "observed_at", context, errors)
        _require_string(event, "summary", context, errors)
        if event.get("authority") not in ALLOWED_AUTHORITIES:
            errors.append(f"{context}.authority: invalid authority classification")

        evidence_refs = _require_list(event, "evidence_refs", context, errors)
        if any(not _is_nonempty_string(item) for item in evidence_refs):
            errors.append(f"{context}.evidence_refs: every item must be a non-empty string")

        action_refs = _require_list(event, "action_refs", context, errors)
        for action_index, action in enumerate(action_refs):
            action_context = f"{context}.action_refs[{action_index}]"
            if not isinstance(action, dict):
                errors.append(f"{action_context}: expected object")
                continue
            if action.get("type") not in ALLOWED_ACTION_TYPES:
                errors.append(f"{action_context}.type: invalid action type")
            _require_string(action, "immutable_ref", action_context, errors)
            payload_sha = _require_string(action, "payload_sha256", action_context, errors)
            if payload_sha and not SHA256_RE.fullmatch(payload_sha):
                errors.append(f"{action_context}.payload_sha256: expected sha256:<64-hex>")
            observed_actor = _require_string(action, "observed_actor_login", action_context, errors)
            if event.get("actor") == "executor" and bot_login and observed_actor and observed_actor != bot_login:
                errors.append(
                    f"{action_context}.observed_actor_login: executor action must use declared App bot login"
                )

        if event.get("actor") == "executor" and bot_login and actor_identity and actor_identity != bot_login:
            errors.append(f"{context}.actor_identity: executor event must use declared App bot login")
        if event.get("actor") == "human" and actor_identity and actor_identity not in declared_human_set:
            errors.append(f"{context}.actor_identity: human actor is not in declared_human_github_logins")
        if event.get("kind") == "executor_action" and not action_refs:
            errors.append(f"{context}: executor_action requires at least one action_ref")
        if event.get("kind") == "human_intervention" and event.get("authority") != "human_intervention":
            errors.append(f"{context}: human_intervention event must use human_intervention authority")

        previous = event.get("previous_event_digest")
        if index == 1:
            if previous != "GENESIS":
                errors.append(f"{context}.previous_event_digest: first event must use GENESIS")
        else:
            expected_previous = events[index - 2].get("event_digest")
            if previous != expected_previous:
                errors.append(f"{context}.previous_event_digest: does not match prior event_digest")

        claimed_digest = event.get("event_digest")
        if not isinstance(claimed_digest, str) or not SHA256_RE.fullmatch(claimed_digest):
            errors.append(f"{context}.event_digest: expected sha256:<64-hex>")
        else:
            expected_digest = event_digest(event)
            if claimed_digest != expected_digest:
                errors.append(f"{context}.event_digest: digest mismatch")

    event_ids = [event.get("event_id") for event in events if isinstance(event.get("event_id"), str)]
    if len(event_ids) != len(set(event_ids)):
        errors.append("events: event_id values must be unique within a run")

    accounting = _require_dict(data, "human_intervention_accounting", "root", errors)
    post_start_human_input = _require_bool(
        accounting, "post_start_human_input_occurred", "human_intervention_accounting", errors
    )
    human_intervention = _require_bool(
        accounting, "human_intervention_occurred", "human_intervention_accounting", errors
    )
    intervention_count = accounting.get("intervention_count")
    if not isinstance(intervention_count, int) or isinstance(intervention_count, bool) or intervention_count < 0:
        errors.append("human_intervention_accounting.intervention_count: expected non-negative integer")
        intervention_count = None
    material_attributed = _require_bool(
        accounting, "material_interventions_attributed", "human_intervention_accounting", errors
    )
    _require_bool(
        accounting, "unobserved_material_channel_known", "human_intervention_accounting", errors
    )
    resumed = accounting.get("s1_resumed_autonomously_after_intervention")
    if resumed not in {True, False, "not_applicable"}:
        errors.append(
            "human_intervention_accounting.s1_resumed_autonomously_after_intervention: "
            "expected true/false/'not_applicable'"
        )
    _require_string(accounting, "notes", "human_intervention_accounting", errors)

    intervention_events = sum(event.get("kind") == "human_intervention" for event in events)
    human_input_events = sum(
        event.get("kind") in {"human_input", "human_intervention"} for event in events
    )
    if intervention_count is not None and intervention_count != intervention_events:
        errors.append(
            "human_intervention_accounting.intervention_count does not match human_intervention events"
        )
    if human_intervention is not None and human_intervention != (intervention_events > 0):
        errors.append(
            "human_intervention_accounting.human_intervention_occurred does not match event record"
        )
    if post_start_human_input is not None and post_start_human_input != (human_input_events > 0):
        errors.append(
            "human_intervention_accounting.post_start_human_input_occurred does not match event record"
        )
    if intervention_events > 0 and material_attributed is not True:
        errors.append(
            "human_intervention_accounting.material_interventions_attributed must be true when interventions exist"
        )

    closure = _require_dict(data, "closure", "root", errors)
    closure_refs = _require_list(closure, "closure_artifact_refs", "closure", errors)
    if not closure_refs or any(not _is_nonempty_string(item) for item in closure_refs):
        errors.append("closure.closure_artifact_refs: expected at least one non-empty reference")
    final_revision = closure.get("final_result_revision")
    if final_revision is not None and (not isinstance(final_revision, str) or not SHA40_RE.fullmatch(final_revision)):
        errors.append("closure.final_result_revision: expected lowercase 40-hex SHA or null")
    claimed_run_digest = _require_string(closure, "run_record_digest", "closure", errors)
    if claimed_run_digest and not SHA256_RE.fullmatch(claimed_run_digest):
        errors.append("closure.run_record_digest: expected sha256:<64-hex>")
    elif claimed_run_digest and events and all(
        isinstance(event.get("event_digest"), str) and SHA256_RE.fullmatch(event["event_digest"])
        for event in events
    ):
        expected_run_digest = run_record_digest(events)
        if claimed_run_digest != expected_run_digest:
            errors.append("closure.run_record_digest: digest mismatch")
    if anchor_ref and closure.get("pre_run_anchor_ref") != anchor_ref:
        errors.append("closure.pre_run_anchor_ref must equal pre_run_anchor.immutable_ref")
    closure_escalation = _require_bool(closure, "escalation_occurred", "closure", errors)
    closure_intervention = _require_bool(closure, "human_intervention_occurred", "closure", errors)
    escalation_events = any(event.get("kind") == "escalation" for event in events)
    if closure_escalation is not None and closure_escalation != escalation_events:
        errors.append("closure.escalation_occurred does not match event record")
    if closure_intervention is not None and human_intervention is not None and closure_intervention != human_intervention:
        errors.append("closure.human_intervention_occurred must match human_intervention_accounting")

    final_attestation = _require_dict(data, "final_attestation", "root", errors)
    if bot_login and final_attestation.get("attester_identity") != bot_login:
        errors.append("final_attestation.attester_identity must equal App bot login")
    if bot_login and final_attestation.get("observed_actor_login") != bot_login:
        errors.append("final_attestation.observed_actor_login must equal App bot login")
    final_digest = _require_string(final_attestation, "payload_digest", "final_attestation", errors)
    if final_digest and not SHA256_RE.fullmatch(final_digest):
        errors.append("final_attestation.payload_digest: expected sha256:<64-hex>")
    elif final_digest and run and anchor and closure:
        try:
            expected_final = final_binding_digest(data)
        except KeyError:
            expected_final = None
        if expected_final and final_digest != expected_final:
            errors.append("final_attestation.payload_digest: digest mismatch")
    _require_string(final_attestation, "attestation_ref", "final_attestation", errors)
    _require_string(final_attestation, "verification_instructions_ref", "final_attestation", errors)

    review = _require_dict(data, "review", "root", errors)
    for key in (
        "actor_attribution_verified",
        "action_bindings_verified",
        "human_interventions_accounted_for",
        "event_order_integrity_verified",
    ):
        _require_bool(review, key, "review", errors)
    decisive_loop = review.get("decisive_agent_owned_loop_established")
    if decisive_loop not in {True, False, "insufficient"}:
        errors.append(
            "review.decisive_agent_owned_loop_established: expected true/false/'insufficient'"
        )
    verdict = review.get("provenance_verdict")
    if verdict not in {"PASS", "FAIL", "INSUFFICIENT"}:
        errors.append("review.provenance_verdict: expected PASS/FAIL/INSUFFICIENT")
    _require_string(review, "note", "review", errors)

    if run_id and not re.fullmatch(r"[A-Za-z0-9._:-]+", run_id):
        errors.append("run.run_id: use only letters, digits, dot, underscore, colon, or hyphen")

    return errors


def validate_file(path: Path) -> list[str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: invalid JSON: {exc}"]
    if not isinstance(data, dict):
        return [f"{path}: root must be an object"]
    return [f"{path}: {error}" for error in validate_witness(data)]


def collect_paths(explicit: list[str], directory: str | None) -> list[Path]:
    paths = [Path(item) for item in explicit]
    if directory:
        root = Path(directory)
        if root.is_dir():
            paths.extend(sorted(root.rglob("witness.json")))
    unique: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        resolved = path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(path)
    return unique


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="witness JSON files")
    parser.add_argument(
        "--directory",
        help="recursively validate files named witness.json below this directory",
    )
    parser.add_argument(
        "--allow-empty",
        action="store_true",
        help="succeed when no witness files are present",
    )
    args = parser.parse_args()

    paths = collect_paths(args.paths, args.directory)
    if not paths:
        if args.allow_empty:
            print("No executor witness files present; nothing to validate.")
            return 0
        parser.error("no witness files supplied or discovered")

    errors: list[str] = []
    for path in paths:
        errors.extend(validate_file(path))

    if errors:
        print("Executor provenance witness validation FAILED:")
        for error in errors:
            print(f"- {error}")
        print(
            "Local validation checks structure/hash bindings only; remote GitHub actor evidence "
            "still requires independent inspection."
        )
        return 1

    print(f"Executor provenance witness validation OK ({len(paths)} file(s)).")
    print(
        "This does not establish S1=A or independently verify remote GitHub actor claims; "
        "apply the selected Profile/Methodology and inspect cited primary evidence."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
