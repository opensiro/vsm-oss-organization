#!/usr/bin/env python3
"""Compute the experimental upstream-intervention-fit snapshot using stdlib only."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OBSERVATIONS = ROOT / "observations.json"
SNAPSHOT = ROOT / "snapshot.json"

GATES = (
    "upstream_need",
    "native_mechanism",
    "counterfactual_value",
    "scope_compatibility",
)
GATE_STATES = {"pass", "fail", "unknown"}
LIFECYCLE_STATES = {"draft", "open", "merged", "closed_unmerged", "withdrawn"}
PR_RELATIONS = {"original", "landed_replacement", "related"}
ACCOUNT_TYPES = {"github_user", "github_bot", "unknown"}
PARTICIPANT_ROLES = {
    "original_pr_author", "source_commit_contributor", "landing_pr_author",
    "merger", "reviewer", "review_fix_commit_contributor",
}
GH_LOGIN = re.compile(r"^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,38})$")
GH_PR = re.compile(r"^https://github\.com/([^/]+)/([^/]+)/pull/([1-9][0-9]*)$")
GH_COMMIT = re.compile(r"^https://github\.com/([^/]+)/([^/]+)/commit/([a-fA-F0-9]{7,40})$")
GH_REVIEW = re.compile(r"^https://github\.com/([^/]+)/([^/]+)/pull/([1-9][0-9]*)#pullrequestreview-[0-9]+$")


def upstream_pr(value: str, repo: str, label: str) -> str:
    match = GH_PR.fullmatch(value) if isinstance(value, str) else None
    if not match or (match.group(1) + "/" + match.group(2)).lower() != repo.lower():
        raise ValueError(f"{label}: PR must be a first-party GitHub upstream PR in {repo}")
    return value


def validate_attribution(item: dict) -> None:
    identity = item["id"]
    repo = item["upstream_repository"]
    source_pr = upstream_pr(item["pull_request"], repo, identity)
    chain = item.get("related_pull_requests")
    landing = item.get("landing_pull_request")

    if chain is not None:
        if not isinstance(chain, list) or not chain:
            raise ValueError(f"{identity}: related_pull_requests must be nonempty")
        seen_prs = set()
        original_count = landing_count = 0
        for link in chain:
            if not isinstance(link, dict) or set(link) != {"url", "relation", "lifecycle"}:
                raise ValueError(f"{identity}: linked PR requires url, relation, lifecycle")
            url = upstream_pr(link["url"], repo, identity)
            if url in seen_prs:
                raise ValueError(f"{identity}: duplicate linked PR {url}")
            seen_prs.add(url)
            if link["relation"] not in PR_RELATIONS or link["lifecycle"] not in LIFECYCLE_STATES:
                raise ValueError(f"{identity}: invalid linked PR relation/lifecycle")
            if link["relation"] == "original":
                original_count += 1
                if url != source_pr:
                    raise ValueError(f"{identity}: original PR must equal stable pull_request")
            if link["relation"] == "landed_replacement":
                landing_count += 1
                if link["lifecycle"] != "merged" or url != landing:
                    raise ValueError(f"{identity}: landing PR must be merged and match landing_pull_request")
        if original_count != 1 or landing_count > 1 or source_pr not in seen_prs:
            raise ValueError(f"{identity}: one original PR and at most one landing replacement required")
        if landing and (landing not in seen_prs or landing_count != 1):
            raise ValueError(f"{identity}: landing_pull_request is absent from replacement chain")
        if landing and item["lifecycle"] != "merged":
            raise ValueError(f"{identity}: merged landing requires intervention lifecycle merged")
    elif landing is not None:
        raise ValueError(f"{identity}: landing_pull_request requires related_pull_requests")

    participants = item.get("participants")
    if participants is None:
        return
    if not isinstance(participants, list) or not participants:
        raise ValueError(f"{identity}: participants must be nonempty")
    seen_accounts = set()
    for actor in participants:
        if not isinstance(actor, dict) or set(actor) != {"github_login", "account_type", "roles", "evidence_urls"}:
            raise ValueError(f"{identity}: participant must contain login/type/roles/evidence_urls")
        login = actor["github_login"]
        if not isinstance(login, str) or not GH_LOGIN.fullmatch(login):
            raise ValueError(f"{identity}: invalid GitHub login")
        if login.lower() in seen_accounts:
            raise ValueError(f"{identity}: duplicate participant {login}")
        seen_accounts.add(login.lower())
        if actor["account_type"] not in ACCOUNT_TYPES:
            raise ValueError(f"{identity}: invalid account type")
        roles = actor["roles"]
        if not isinstance(roles, list) or not roles or len(set(roles)) != len(roles) or not set(roles) <= PARTICIPANT_ROLES:
            raise ValueError(f"{identity}: invalid/duplicate participant roles")
        evidences = actor["evidence_urls"]
        if not isinstance(evidences, list) or not evidences or len(set(evidences)) != len(evidences):
            raise ValueError(f"{identity}: participant evidence URLs must be nonempty and unique")
        for url in evidences:
            if not isinstance(url, str):
                raise ValueError(f"{identity}: invalid participant evidence URL")
            match = GH_PR.fullmatch(url) or GH_COMMIT.fullmatch(url) or GH_REVIEW.fullmatch(url)
            if not match or (match.group(1) + "/" + match.group(2)).lower() != repo.lower():
                raise ValueError(f"{identity}: participant evidence must reference original upstream GitHub")
        if "reviewer" in roles and not any(GH_REVIEW.fullmatch(url) for url in evidences):
            raise ValueError(f"{identity}: reviewer requires submitted GitHub review evidence")
        if "source_commit_contributor" in roles and not any(GH_COMMIT.fullmatch(url) for url in evidences):
            raise ValueError(f"{identity}: source commit contributor requires commit evidence")


def derived_fit(gates: dict[str, str]) -> str:
    values = [gates[name] for name in GATES]
    if "fail" in values:
        return "fail"
    if all(value == "pass" for value in values):
        return "pass"
    return "pending"


def validate_observations(data: dict) -> dict:
    if data.get("schema_version") != 1:
        raise ValueError("observations schema_version must be 1")

    seen: set[str] = set()
    for item in data.get("interventions", []):
        identity = item["id"]
        if identity in seen:
            raise ValueError(f"duplicate intervention id: {identity}")
        seen.add(identity)

        gates = item["gates"]
        if set(gates) != set(GATES):
            raise ValueError(f"{identity}: gates must be exactly {GATES}")
        for gate, value in gates.items():
            if value not in GATE_STATES:
                raise ValueError(f"{identity}: invalid {gate} state {value!r}")

        if item["lifecycle"] not in LIFECYCLE_STATES:
            raise ValueError(f"{identity}: invalid lifecycle {item['lifecycle']!r}")

        evidence = item.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            raise ValueError(f"{identity}: at least one evidence entry is required")
        validate_attribution(item)
    return data


def load_observations() -> dict:
    data = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))
    return validate_observations(data)


def compute(data: dict) -> dict:
    rows = []
    counts = {"pass": 0, "fail": 0, "pending": 0}
    lifecycle_counts: dict[str, int] = {}

    for item in data["interventions"]:
        fit = derived_fit(item["gates"])
        counts[fit] += 1
        lifecycle = item["lifecycle"]
        lifecycle_counts[lifecycle] = lifecycle_counts.get(lifecycle, 0) + 1
        row = {
            "id": item["id"],
            "fit": fit,
            "lifecycle": lifecycle,
            "pull_request": item["pull_request"],
            "upstream_repository": item["upstream_repository"],
        }
        for field in ("last_verified_at", "landing_pull_request", "related_pull_requests", "participants"):
            if field in item:
                row[field] = item[field]
        rows.append(row)

    denominator = counts["pass"] + counts["fail"]
    rate = None if denominator == 0 else round(counts["pass"] / denominator, 4)

    return {
        "schema_version": 1,
        "experiment": data["experiment"],
        "as_of": data["as_of"],
        "primary_metric": {
            "id": "product_native_fit_rate",
            "value": rate,
            "numerator_pass": counts["pass"],
            "denominator_completed_reviews": denominator,
        },
        "fit_counts": counts,
        "lifecycle_counts": dict(sorted(lifecycle_counts.items())),
        "interventions": sorted(rows, key=lambda row: row["id"]),
    }


def rendered_snapshot(data: dict) -> str:
    return json.dumps(compute(data), indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()

    try:
        data = load_observations()
        rendered = rendered_snapshot(data)
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.stdout:
        print(rendered, end="")

    if args.check:
        if not SNAPSHOT.exists():
            print("error: snapshot.json is missing", file=sys.stderr)
            return 1
        current = SNAPSHOT.read_text(encoding="utf-8")
        if current != rendered:
            print("error: snapshot.json is stale; run compute.py", file=sys.stderr)
            return 1
        print("upstream-intervention-fit snapshot is current")
        return 0

    SNAPSHOT.write_text(rendered, encoding="utf-8")
    if not args.stdout:
        print(f"wrote {SNAPSHOT.relative_to(ROOT.parent.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
