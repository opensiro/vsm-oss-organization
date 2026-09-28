#!/usr/bin/env python3
"""Compute the experimental upstream-intervention-fit snapshot using stdlib only."""

from __future__ import annotations

import argparse
import json
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


def derived_fit(gates: dict[str, str]) -> str:
    values = [gates[name] for name in GATES]
    if "fail" in values:
        return "fail"
    if all(value == "pass" for value in values):
        return "pass"
    return "pending"


def load_observations() -> dict:
    data = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))
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
    return data


def compute(data: dict) -> dict:
    rows = []
    counts = {"pass": 0, "fail": 0, "pending": 0}
    lifecycle_counts: dict[str, int] = {}

    for item in data["interventions"]:
        fit = derived_fit(item["gates"])
        counts[fit] += 1
        lifecycle = item["lifecycle"]
        lifecycle_counts[lifecycle] = lifecycle_counts.get(lifecycle, 0) + 1
        rows.append(
            {
                "id": item["id"],
                "fit": fit,
                "lifecycle": lifecycle,
                "pull_request": item["pull_request"],
                "upstream_repository": item["upstream_repository"],
            }
        )

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
