#!/usr/bin/env python3
"""Finalize historical metric windows through repository-owned renderers.

The base collector reads generated owner artifacts at current/historical refs.
When a cutoff predates one of those generated artifacts, this finalizer invokes
the owning repository's current read-only renderer against a detached historical
source tree. Before repository inception, cumulative numeric stock uses zero.
Semantic VSM state is never inferred.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Mapping


OWNER_RENDERERS = {
    "skills": {
        "repository": "opensiro/vsm-harness-skills",
        "metrics": {
            "current_validated_methodology_release": "methodology_version",
            "skill_catalog_entries": "skill_catalog_entries",
        },
    },
    "index": {
        "repository": "opensiro/vsm-harness-index",
        "metrics": {
            "included_assessments": "included_assessments",
            "catalog_entries": "catalog_entries",
        },
    },
    "awesome": {
        "repository": "opensiro/awesome-vsm-harness",
        "metrics": {
            "curated_representative_entries": "curated_representative_entries",
        },
    },
}


class FinalizeError(RuntimeError):
    pass


def owner_core_at_revision(root: Path, revision: str, repository: str) -> dict[str, Any]:
    renderer = root / "scripts" / "render_metrics.py"
    if not renderer.is_file():
        raise FinalizeError(f"missing owner renderer for {repository}: {renderer}")

    with tempfile.TemporaryDirectory(prefix="vsm-oss-owner-metrics-") as temp_dir:
        worktree = Path(temp_dir) / "tree"
        added = False
        try:
            subprocess.run(
                ["git", "-C", str(root), "worktree", "add", "--detach", "--force", str(worktree), revision],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            added = True
            completed = subprocess.run(
                [
                    sys.executable,
                    "-S",
                    str(renderer),
                    "--source-root",
                    str(worktree),
                    "--stdout-core-json",
                ],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            data = json.loads(completed.stdout)
            if not isinstance(data, dict):
                raise FinalizeError(f"owner renderer for {repository} did not return an object")
            return data
        except (subprocess.CalledProcessError, json.JSONDecodeError, ValueError) as exc:
            raise FinalizeError(
                f"owner renderer failed for {repository} historical revision {revision}"
            ) from exc
        finally:
            if added:
                subprocess.run(
                    ["git", "-C", str(root), "worktree", "remove", "--force", str(worktree)],
                    check=False,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )


def finalize_pre_inception(snapshot: dict[str, Any]) -> None:
    for repo in snapshot.get("repositories", {}).values():
        for metric in repo.get("metrics", {}).values():
            changes = metric.get("window_change")
            if not isinstance(changes, dict):
                continue
            for entry in changes.values():
                if not isinstance(entry, dict) or entry.get("status") != "history_unavailable":
                    continue
                current = metric.get("value")
                if isinstance(current, int) and not isinstance(current, bool):
                    entry["baseline"] = 0
                    entry["value"] = current
                    entry["status"] = "derived_pre_inception_net_change"
                elif isinstance(current, str):
                    entry["baseline"] = None
                    entry["changed"] = True
                    entry["status"] = "derived_pre_inception_state"


def apply_owner_renderer_gap(
    metric: dict[str, Any],
    *,
    owner_value: Any,
    repository: str,
) -> None:
    current = metric.get("value")
    if isinstance(current, int) and not isinstance(current, bool):
        baseline = int(owner_value)
        metric_entry_mode = "numeric"
    elif isinstance(current, str):
        baseline = str(owner_value)
        metric_entry_mode = "state"
    else:
        raise FinalizeError(
            f"unsupported owner-rendered metric value for {repository}: {type(current).__name__}"
        )

    for entry in metric.get("window_change", {}).values():
        if entry.get("status") != "source_unavailable_at_baseline":
            continue
        # Caller attaches one renderer result per exact baseline revision.
        if entry.get("_owner_baseline_revision") is None:
            continue
        entry["baseline"] = baseline
        if metric_entry_mode == "numeric":
            entry["value"] = int(current) - baseline
            entry["status"] = "derived_net_change_via_repository_renderer"
        else:
            entry["changed"] = str(current) != baseline
            entry["status"] = "derived_state_change_via_repository_renderer"
        entry["baseline_source"] = f"{repository} scripts/render_metrics.py --stdout-core-json"
        entry.pop("_owner_baseline_revision", None)


def finalize_owner_history(
    snapshot: dict[str, Any],
    roots: Mapping[str, Path],
) -> None:
    for key, config in OWNER_RENDERERS.items():
        repository = str(config["repository"])
        root = roots[key]
        metrics = snapshot["repositories"][repository]["metrics"]
        cache: dict[str, dict[str, Any]] = {}

        # Group gaps by revision first so one historical worktree/query serves all metrics.
        revisions: set[str] = set()
        for metric_name in config["metrics"]:
            metric = metrics.get(metric_name)
            if not isinstance(metric, dict):
                continue
            for entry in metric.get("window_change", {}).values():
                if entry.get("status") == "source_unavailable_at_baseline":
                    revision = entry.get("baseline_revision")
                    if not revision:
                        raise FinalizeError(
                            f"{repository}:{metric_name} gap has no baseline revision"
                        )
                    revisions.add(str(revision))

        for revision in revisions:
            cache[revision] = owner_core_at_revision(root, revision, repository)

        for metric_name, owner_key in config["metrics"].items():
            metric = metrics.get(metric_name)
            if not isinstance(metric, dict):
                continue
            for entry in metric.get("window_change", {}).values():
                if entry.get("status") != "source_unavailable_at_baseline":
                    continue
                revision = str(entry["baseline_revision"])
                owner_data = cache[revision]
                if owner_key not in owner_data:
                    raise FinalizeError(
                        f"owner renderer for {repository} omitted required key {owner_key}"
                    )
                current = metric.get("value")
                baseline = owner_data[owner_key]
                entry["baseline"] = baseline
                if isinstance(current, int) and not isinstance(current, bool):
                    entry["value"] = int(current) - int(baseline)
                    entry["status"] = "derived_net_change_via_repository_renderer"
                elif isinstance(current, str):
                    entry["changed"] = str(current) != str(baseline)
                    entry["status"] = "derived_state_change_via_repository_renderer"
                else:
                    raise FinalizeError(
                        f"unsupported owner metric {repository}:{metric_name}"
                    )
                entry["baseline_source"] = (
                    f"{repository} scripts/render_metrics.py --stdout-core-json"
                )


def finalize(snapshot: dict[str, Any], roots: Mapping[str, Path]) -> dict[str, Any]:
    if snapshot.get("publication", {}).get("window_change_semantics") != (
        "net canonical state change, not gross event count"
    ):
        raise FinalizeError("unexpected or missing window-change semantics")
    missing = set(OWNER_RENDERERS) - set(roots)
    if missing:
        raise FinalizeError(f"missing owner roots: {sorted(missing)}")
    finalize_pre_inception(snapshot)
    finalize_owner_history(snapshot, roots)
    snapshot.setdefault("publication", {})["historical_gap_policy"] = (
        "owning repository renderer when generated owner artifact predates instrumentation; "
        "zero baseline before repository inception"
    )
    return snapshot


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--skills-root", type=Path, required=True)
    parser.add_argument("--index-root", type=Path, required=True)
    parser.add_argument("--awesome-root", type=Path, required=True)
    args = parser.parse_args()
    roots = {
        "skills": args.skills_root,
        "index": args.index_root,
        "awesome": args.awesome_root,
    }
    try:
        snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
        finalized = finalize(snapshot, roots)
    except (OSError, json.JSONDecodeError, FinalizeError, KeyError, TypeError, ValueError) as exc:
        raise SystemExit(f"metrics window finalizer error: {exc}") from exc
    args.snapshot.write_text(
        json.dumps(finalized, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
