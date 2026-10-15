#!/usr/bin/env python3
"""S3 current-commitment regulation constructor, not a validator or autonomous S3 owner.

Observe currently binding cross-domain facts, reject local/S5 matters, and
prepare bounded *unselected* owner options only for evidence-linked nonlocal
cases. Never performs or attributes an S3 decision or changes S1 work.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

DOMAINS = {
    "Index": "vsm-harness-index",
    "Skills": "vsm-harness-skills",
    "Awesome": "awesome-vsm-harness",
}
SOURCE_REF = re.compile(
    r"https://github[.]com/opensiro/[A-Za-z0-9_.-]+/(?:issues|pull|commit|blob|tree)/[^\s<>]+\Z"
)
ISSUE_RE = re.compile(
    r"https://github[.]com/opensiro/(vsm-harness-index|vsm-harness-skills|awesome-vsm-harness)/issues/[1-9][0-9]*\Z"
)


class RegulationError(ValueError):
    pass


def need(condition: bool, reason: str) -> None:
    if not condition:
        raise RegulationError(reason)


def text(value: object, name: str) -> str:
    need(isinstance(value, str) and value.strip() != "" and "<" not in value and
         len(value) <= 1500, f"{name}: real non-placeholder text required")
    return value.strip()


def read_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    need(type(data) is dict, f"{path}: JSON object required")
    return data


def source(ref: object, name: str) -> str:
    value = text(ref, name)
    need(bool(SOURCE_REF.fullmatch(value)), f"{name}: needs first-party GitHub source")
    return value


def observe(root: Path, index: Path, skills: Path, awesome: Path) -> dict:
    """Observe real standing commitments without confusing deterministic checks with S3."""
    selected = read_json(root / "UPSTREAM_CONTRACT.json")
    reg = read_json(root / "control" / "s3-standing-commitments.json")
    need(reg.get("version") == 1 and reg.get("system_in_focus") == "opensiro-bounded-oss",
         "standing S3 commitments: unsupported source or version")
    entries = reg.get("standing_commitments")
    need(isinstance(entries, list) and len(entries) == 2 and
         {e["id"] for e in entries} == {
             "selected-methodology-continuity", "canonical-publication-continuity"
         }, "standing commitments: expected two bounded real operating obligations")
    grant = (root / reg["grant_source"]).read_text(encoding="utf-8")
    need("CONTINUE" in grant and "SET_CONSTRAINT" in grant and
         "REQUIRE_REPAIR" in grant and "xLagerFeuer" in grant,
         "published G1 source/response class missing")
    p = selected["profile"]["version"]
    m = selected["methodology"]["version"]
    index_rows = (index / "data" / "active-contract.psv").read_text(encoding="utf-8").strip().splitlines()
    need(len(index_rows) == 2 and index_rows[0] == "profile_version|methodology_version",
         "Index active contract: missing or malformed")
    pair = index_rows[1].split("|")
    need(len(pair) == 2, "Index active contract: malformed versions")
    skills_version = (skills / "skills" / "assess-vsm-harness" / "VERSION").read_text(encoding="utf-8").strip()
    workflow = (awesome / ".github" / "workflows" / "index-consistency.yml").read_text(encoding="utf-8")
    awesome_reads_index = "repository: opensiro/vsm-harness-index" in workflow and "validate_index_consistency.py" in workflow
    need(awesome_reads_index, "Awesome canonical Index consumption not evidenced")
    need(skills_version == m, "provided Skills checkout is not selected Methodology release")
    status = "CURRENT_SHARED_CONTRACT_ALIGNED" if pair == [p, m] else "CURRENT_SHARED_CONTRACT_DRIFT"
    return {
        "system_in_focus": "Index / Skills / Awesome",
        "current_contract_state": status,
        "selected_profile": p,
        "selected_methodology": m,
        "index_active_contract": dict(zip(("profile", "methodology"), pair)),
        "awesome_consumes_canonical_index": True,
        "standing_commitments": entries,
        "decision_owner": "G1 human S3 holder xLagerFeuer; each case requires separate authenticated choice",
        "authority_envelope": reg["granted_classes"],
        "assessment_boundary": "CURRENT_RULES_AND_SUPPORT_NOT_S3_C_GRADE_OR_S3_TRANSACTION",
    }


def candidate_packet(view: dict, case: dict) -> dict:
    """Build only a source-required choice envelope; cannot admit a case or select owner action."""
    need(case.get("schema_version") == 1, "case: schema_version must be 1")
    kind = case.get("kind")
    need(kind in {"local_s1_repair", "s5_contract_selection",
                  "nonlocal_current_commitment"}, "case: unknown kind")
    basis = {"system_in_focus": view["system_in_focus"], "case_kind": kind,
             "current_contract_state": view["current_contract_state"],
             "owner": view["decision_owner"]}
    if kind == "local_s1_repair":
        return {**basis, "disposition": "ROUTE_LOCAL_S1",
                "reason": "Local source/assessment/curation repairs cannot become S3 by routing."}
    if kind == "s5_contract_selection":
        return {**basis, "disposition": "ROUTE_S5_POLICY",
                "reason": "Changing selected Profile/Methodology is outside G1 current-control rights."}
    commitment_id = case.get("commitment_id")
    match = [e for e in view["standing_commitments"] if e["id"] == commitment_id]
    need(len(match) == 1, "case: current shared commitment unknown")
    commitment = match[0]
    work = case.get("active_s1_work")
    need(isinstance(work, list) and len(work) >= 1, "case: require at least one current S1 work record")
    domains = set()
    refs = set()
    for i, item in enumerate(work):
        need(type(item) is dict and set(item) == {"domain", "work_ref", "admission_ref", "commitment"},
             f"case.work[{i}]: exact fields required")
        domain = item["domain"]
        need(domain in commitment["affected_s1"] and domain not in domains,
             f"case.work[{i}]: domain outside commitment or repeated")
        domains.add(domain)
        expected_repo = DOMAINS[domain]
        ref = text(item["work_ref"], "work_ref")
        need(bool(ISSUE_RE.fullmatch(ref)) and f"/{expected_repo}/issues/" in ref,
             f"case.work[{i}]: S1 owning issue required")
        need(ref not in refs, "case: repeated work ref")
        refs.add(ref)
        source(item["admission_ref"], "admission_ref")
        text(item["commitment"], "work commitment")
    evidence = case.get("nonlocal_evidence_refs")
    need(isinstance(evidence, list) and len(evidence) >= 2,
         "case: material whole-system decision must have multiple source refs")
    source_domains = set()
    for i, ref in enumerate(evidence):
        url = source(ref, f"nonlocal_evidence_refs[{i}]")
        for domain, name in DOMAINS.items():
            if f"/opensiro/{name}/" in url:
                source_domains.add(domain)
    need(len(source_domains.intersection(commitment["affected_s1"])) >= 2,
         "case: evidence must identify the current shared obligation across two S1 domains")
    need(domains.issubset(source_domains),
         "case: primary evidence must cover each named affected S1")
    text(case.get("shared_current_constraint"), "shared_current_constraint")
    text(case.get("why_s1_s2_cannot_decide"), "why_s1_s2_cannot_decide")
    target = text(case.get("return_target"), "return_target")
    need(target in refs, "case: S1 return must target a current named work item")
    text(case.get("rollback_condition"), "rollback_condition")
    need(case.get("requires_owner_confirmation") is True,
         "case: cannot pre-approve or impersonate the G1 owner")
    options = [
        {"class": "CONTINUE", "effect": "Preserve local S1 work while verifying the exact shared constraint; no grade or authority change."},
        {"class": "REQUIRE_REPAIR", "effect": "Return a narrowly specified current shared-commitment repair to the named S1; S1 chooses its technical resolution."},
        {"class": "SET_CONSTRAINT", "effect": "Propose a time-limited constraint solely on the named S1 work and recorded shared commitment; holder sets precise scope and expiry."},
    ]
    return {**basis, "disposition": "UNADMITTED_G1_HUMAN_OPTION_PACKET",
            "commitment_id": commitment_id, "current_shared_rule": commitment["regulates"],
            "candidate_current_view": work, "candidate_evidence_refs": evidence,
            "return_target": target, "rollback_condition": case["rollback_condition"],
            "options": options, "chosen_option": None, "decision_ref": None,
            "S1_application_ref": None,
            "conditions_before_choice": [
                "Reverify each S1 admission and effective current work on its owning GitHub source",
                "Demonstrate shared present right above ordinary S1/S2 and not S5 policy",
                "Reverify published G1 effective date, expiry, revocation and holder identity",
                "Human G1 holder must choose; separately instantiate a real S3 transaction",
                "Use existing S3→S1 return procedure only after attributable choice",
            ], "warning": "An option packet does not itself admit a case, decide, constrain S1, or prove S3=C."}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--index-root", type=Path, required=True)
    parser.add_argument("--skills-root", type=Path, required=True)
    parser.add_argument("--awesome-root", type=Path, required=True)
    parser.add_argument("--case", type=Path, help="explicit candidate facts; no case means inspect standing obligations")
    parser.add_argument("--output", type=Path, help="write source view/packet without taking any action")
    args = parser.parse_args(argv)
    try:
        view = observe(args.root, args.index_root, args.skills_root, args.awesome_root)
        report = candidate_packet(view, read_json(args.case)) if args.case else view
        result = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
        if args.output:
            args.output.write_text(result, encoding="utf-8")
        else:
            print(result, end="")
    except (RegulationError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"NO_S3_ACTION: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
