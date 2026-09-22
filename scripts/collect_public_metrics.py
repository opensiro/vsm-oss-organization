#!/usr/bin/env python3
"""Collect public VSM OSS outcome state and time-window change.

Repository-owned sources define the current metric values. This collector does
not reimplement repository counting logic where a canonical metric artifact
already exists. For 24h/7d/30d change it reads the same source at the most
recent repository revision at or before each cutoff.

Engineering activity is emitted separately as secondary, non-KPI telemetry.
Semantic VSM evidence is never inferred.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Mapping

import yaml


class CollectorError(RuntimeError):
    pass


REPOSITORIES = {
    "profile": "opensiro/vsm-harness-profile",
    "skills": "opensiro/vsm-harness-skills",
    "index": "opensiro/vsm-harness-index",
    "awesome": "opensiro/awesome-vsm-harness",
    "organization": "opensiro/vsm-oss-organization",
}

WINDOWS = {
    "24h": timedelta(hours=24),
    "7d": timedelta(days=7),
    "30d": timedelta(days=30),
}

AWESOME_ASSESSMENT_RE = re.compile(
    r"https://github\.com/opensiro/vsm-harness-index/blob/main/assessments/"
    r"([A-Za-z0-9._-]+)\.md"
)


def parse_instant(value: str | None) -> datetime:
    if value is None:
        return datetime.now(timezone.utc).replace(microsecond=0)
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise CollectorError("collection time must include a timezone")
    return parsed.astimezone(timezone.utc).replace(microsecond=0)


def instant_text(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def read_text(root: Path, relative: str) -> str:
    path = root / relative
    if not path.is_file():
        raise CollectorError(f"missing required source: {path}")
    return path.read_text(encoding="utf-8")


def read_json(root: Path, relative: str) -> Any:
    try:
        return json.loads(read_text(root, relative))
    except json.JSONDecodeError as exc:
        raise CollectorError(f"invalid JSON in {root / relative}: {exc}") from exc


def load_contract(organization_root: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(read_text(organization_root, "metrics.yaml"))
    except yaml.YAMLError as exc:
        raise CollectorError(f"invalid metrics.yaml: {exc}") from exc
    if not isinstance(data, dict):
        raise CollectorError("metrics.yaml must contain a mapping")
    return data


def git_output(root: Path, *args: str, check: bool = True) -> str:
    try:
        completed = subprocess.run(
            ["git", "-C", str(root), *args],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=check,
        )
    except subprocess.CalledProcessError as exc:
        raise CollectorError(f"git {' '.join(args)} failed for {root}") from exc
    return completed.stdout.strip()


def git_revision(root: Path) -> str:
    return git_output(root, "rev-parse", "HEAD")


def git_revision_at_or_before(root: Path, cutoff: datetime) -> str | None:
    value = git_output(
        root,
        "rev-list",
        "-1",
        f"--before={instant_text(cutoff)}",
        "HEAD",
        check=False,
    )
    return value or None


def git_text_at(root: Path, revision: str, relative: str) -> str | None:
    completed = subprocess.run(
        ["git", "-C", str(root), "show", f"{revision}:{relative}"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if completed.returncode != 0:
        return None
    return completed.stdout


def git_json_at(root: Path, revision: str, relative: str) -> Any | None:
    text = git_text_at(root, revision, relative)
    if text is None:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise CollectorError(
            f"invalid historical JSON at {revision}:{relative}"
        ) from exc


def git_commit_count(root: Path, since: datetime, until: datetime) -> int:
    output = git_output(
        root,
        "rev-list",
        "--count",
        f"--since={instant_text(since)}",
        f"--until={instant_text(until)}",
        "HEAD",
    )
    return int(output or "0")


def collect_activity(root: Path, collected_at: datetime) -> dict[str, Any]:
    result: dict[str, Any] = {"classification": "secondary_non_kpi"}
    for label, delta in WINDOWS.items():
        result[f"commits_{label}"] = git_commit_count(
            root, collected_at - delta, collected_at
        )
    return result


def parse_skill_ids_text(text: str) -> list[str]:
    in_section = False
    ids: list[str] = []
    for line in text.splitlines():
        if line.strip() == "## Skill catalog":
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if not in_section:
            continue
        match = re.match(r"^\|\s*\[([^\]]+)\]\([^)]+\)\s*\|", line)
        if match:
            ids.append(match.group(1).strip())
    if len(ids) != len(set(ids)):
        raise CollectorError("duplicate skill identity in README skill catalog")
    return ids


def parse_awesome_ids_text(text: str) -> list[str]:
    ids = AWESOME_ASSESSMENT_RE.findall(text)
    unique = list(dict.fromkeys(ids))
    if len(ids) != len(unique):
        raise CollectorError("duplicate canonical Index assessment link in Awesome README")
    return unique


def metric(
    kind: str,
    value: Any,
    source: str,
    *,
    claim_status: str = "mechanically_derived",
    completion_gate_evaluated: bool = False,
    window_change: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    result = {
        "kind": kind,
        "value": value,
        "source": source,
        "claim_status": claim_status,
        "completion_gate_evaluated": completion_gate_evaluated,
    }
    if window_change is not None:
        result["window_change"] = dict(window_change)
    return result


def historical_text_value(root: Path, revision: str, relative: str) -> str | None:
    text = git_text_at(root, revision, relative)
    return text.strip() if text is not None else None


def semantic_metrics_unclaimed(repo_contract: Mapping[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for name, spec in repo_contract.get("metrics", {}).items():
        source = spec.get("source", {})
        if source.get("mode") != "semantic_evidence":
            continue
        paths: list[str] = []
        if isinstance(source.get("path"), str):
            paths.append(source["path"])
        if isinstance(source.get("paths"), list):
            paths.extend(str(item) for item in source["paths"])
        result[name] = {
            "kind": spec.get("kind"),
            "value": None,
            "claim_status": "unclaimed_semantic_evidence",
            "completion_gate_evaluated": False,
            "evidence_paths": paths,
            "window_change": {
                label: {"status": "unclaimed_semantic_evidence", "value": None}
                for label in WINDOWS
            },
        }
    return result


def window_baselines(
    root: Path,
    collected_at: datetime,
    reader: Callable[[str], Any | None],
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for label, delta in WINDOWS.items():
        cutoff = collected_at - delta
        revision = git_revision_at_or_before(root, cutoff)
        if revision is None:
            result[label] = {
                "status": "history_unavailable",
                "cutoff": instant_text(cutoff),
                "baseline_revision": None,
                "baseline": None,
            }
            continue
        value = reader(revision)
        if value is None:
            result[label] = {
                "status": "source_unavailable_at_baseline",
                "cutoff": instant_text(cutoff),
                "baseline_revision": revision,
                "baseline": None,
            }
            continue
        result[label] = {
            "status": "baseline_available",
            "cutoff": instant_text(cutoff),
            "baseline_revision": revision,
            "baseline": value,
        }
    return result


def numeric_window_change(
    root: Path,
    collected_at: datetime,
    current: int,
    reader: Callable[[str], int | None],
) -> dict[str, Any]:
    baselines = window_baselines(root, collected_at, reader)
    for entry in baselines.values():
        if entry["status"] != "baseline_available":
            entry["value"] = None
            continue
        baseline = int(entry["baseline"])
        entry["value"] = current - baseline
        entry["status"] = "derived_net_change"
    return baselines


def state_window_change(
    root: Path,
    collected_at: datetime,
    current: str,
    reader: Callable[[str], str | None],
) -> dict[str, Any]:
    baselines = window_baselines(root, collected_at, reader)
    for entry in baselines.values():
        if entry["status"] != "baseline_available":
            entry["changed"] = None
            continue
        entry["changed"] = str(entry["baseline"]) != current
        entry["status"] = "derived_state_change"
    return baselines


def collect_snapshot(
    roots: Mapping[str, Path],
    *,
    collected_at: datetime,
    revisions: Mapping[str, str] | None = None,
    activity: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    missing_root_keys = set(REPOSITORIES) - set(roots)
    if missing_root_keys:
        raise CollectorError(f"missing roots: {sorted(missing_root_keys)}")

    organization_root = roots["organization"]
    contract = load_contract(organization_root)
    scope = contract.get("scope", {}).get("repositories")
    if scope != list(REPOSITORIES.values()):
        raise CollectorError(
            "metrics.yaml scope/order differs from the collector adapter boundary"
        )
    contract_repositories = contract.get("repositories", {})
    if set(contract_repositories) != set(REPOSITORIES.values()):
        raise CollectorError("metrics.yaml repository definitions differ from scope")

    revisions_by_repo = {
        full_name: (
            revisions[full_name]
            if revisions is not None
            else git_revision(roots[key])
        )
        for key, full_name in REPOSITORIES.items()
    }
    activity_by_repo = {
        full_name: (
            dict(activity[full_name])
            if activity is not None
            else collect_activity(roots[key], collected_at)
        )
        for key, full_name in REPOSITORIES.items()
    }

    profile_repo = REPOSITORIES["profile"]
    skills_repo = REPOSITORIES["skills"]
    index_repo = REPOSITORIES["index"]
    awesome_repo = REPOSITORIES["awesome"]
    organization_repo = REPOSITORIES["organization"]

    repositories: dict[str, Any] = {}

    def base(repo: str) -> dict[str, Any]:
        repo_contract = contract_repositories[repo]
        return {
            "revision": revisions_by_repo[repo],
            "organizational_role": repo_contract["organizational_role"],
            "primary_metric": repo_contract["primary_metric"],
            "metrics": {},
            "engineering_activity": activity_by_repo[repo],
        }

    profile = base(profile_repo)
    profile_version = read_text(roots["profile"], "VERSION").strip()
    profile["metrics"]["current_validated_profile_release"] = metric(
        "state",
        profile_version,
        "VERSION",
        claim_status="source_observed_completion_gate_not_rechecked",
        window_change=state_window_change(
            roots["profile"],
            collected_at,
            profile_version,
            lambda rev: historical_text_value(roots["profile"], rev, "VERSION"),
        ),
    )
    repositories[profile_repo] = profile

    skills = base(skills_repo)
    skills_version = read_text(
        roots["skills"], "skills/assess-vsm-harness/VERSION"
    ).strip()
    skills["metrics"]["current_validated_methodology_release"] = metric(
        "state",
        skills_version,
        "skills/assess-vsm-harness/VERSION",
        claim_status="source_observed_completion_gate_not_rechecked",
        window_change=state_window_change(
            roots["skills"],
            collected_at,
            skills_version,
            lambda rev: historical_text_value(
                roots["skills"], rev, "skills/assess-vsm-harness/VERSION"
            ),
        ),
    )
    skill_ids = parse_skill_ids_text(read_text(roots["skills"], "README.md"))
    skills["metrics"]["skill_catalog_entries"] = metric(
        "stock",
        len(skill_ids),
        "README.md#skill-catalog",
        window_change=numeric_window_change(
            roots["skills"],
            collected_at,
            len(skill_ids),
            lambda rev: (
                len(parse_skill_ids_text(text))
                if (text := git_text_at(roots["skills"], rev, "README.md")) is not None
                else None
            ),
        ),
    )
    repositories[skills_repo] = skills

    index_data = read_json(roots["index"], "data/metrics.json")
    index = base(index_repo)

    def historical_index_value(revision: str, *keys: str) -> int | None:
        data = git_json_at(roots["index"], revision, "data/metrics.json")
        if data is None:
            return None
        value: Any = data
        for key in keys:
            value = value[key]
        return int(value)

    included = int(index_data["corpus"]["included_assessments"])
    index["metrics"]["included_assessments"] = metric(
        "stock",
        included,
        "data/metrics.json#/corpus/included_assessments",
        window_change=numeric_window_change(
            roots["index"],
            collected_at,
            included,
            lambda rev: historical_index_value(
                rev, "corpus", "included_assessments"
            ),
        ),
    )
    catalog_entries = int(index_data["corpus"]["catalog_entries"])
    index["metrics"]["catalog_entries"] = metric(
        "stock",
        catalog_entries,
        "data/metrics.json#/corpus/catalog_entries",
        window_change=numeric_window_change(
            roots["index"],
            collected_at,
            catalog_entries,
            lambda rev: historical_index_value(rev, "corpus", "catalog_entries"),
        ),
    )
    reassessment_events = int(index_data["corpus"]["reassessment_events"])
    index["metrics"]["reassessment_events"] = metric(
        "stock",
        reassessment_events,
        "data/metrics.json#/corpus/reassessment_events",
        window_change=numeric_window_change(
            roots["index"],
            collected_at,
            reassessment_events,
            lambda rev: historical_index_value(
                rev, "corpus", "reassessment_events"
            ),
        ),
    )
    index["metrics"]["active_contract"] = metric(
        "state",
        {
            "profile_version": index_data["active_contract"]["profile_version"],
            "methodology_version": index_data["active_contract"]["methodology_version"],
        },
        "data/metrics.json#/active_contract",
    )
    repositories[index_repo] = index

    awesome = base(awesome_repo)
    awesome_ids = parse_awesome_ids_text(read_text(roots["awesome"], "README.md"))
    awesome["metrics"]["curated_representative_entries"] = metric(
        "stock",
        len(awesome_ids),
        "README.md canonical Index assessment links",
        window_change=numeric_window_change(
            roots["awesome"],
            collected_at,
            len(awesome_ids),
            lambda rev: (
                len(parse_awesome_ids_text(text))
                if (text := git_text_at(roots["awesome"], rev, "README.md")) is not None
                else None
            ),
        ),
    )
    repositories[awesome_repo] = awesome

    organization = base(organization_repo)
    organization["metrics"].update(
        semantic_metrics_unclaimed(contract_repositories[organization_repo])
    )
    repositories[organization_repo] = organization

    return {
        "schema_version": 2,
        "collected_at": instant_text(collected_at),
        "windows": list(WINDOWS),
        "contract": {
            "repository": organization_repo,
            "revision": revisions_by_repo[organization_repo],
            "path": "metrics.yaml",
        },
        "scope": scope,
        "repositories": repositories,
        "publication": {
            "aggregate_productivity_score": "forbidden",
            "heterogeneous_outputs_may_be_summed": False,
            "engineering_activity_is_productivity_kpi": False,
            "window_change_semantics": "net canonical state change, not gross event count",
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    for key in REPOSITORIES:
        parser.add_argument(
            f"--{key}-root",
            type=Path,
            required=True,
            help=f"checkout root for {REPOSITORIES[key]}",
        )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--collected-at",
        help="ISO-8601 timestamp; defaults to current UTC time",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    roots = {key: getattr(args, f"{key}_root") for key in REPOSITORIES}
    try:
        snapshot = collect_snapshot(
            roots,
            collected_at=parse_instant(args.collected_at),
        )
    except (CollectorError, KeyError, TypeError, ValueError) as exc:
        raise SystemExit(f"metrics collector error: {exc}") from exc

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(snapshot, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
