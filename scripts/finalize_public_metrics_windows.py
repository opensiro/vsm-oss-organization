#!/usr/bin/env python3
"""Finalize 24h/7d/30d window change without duplicating repository logic.

The base collector reads canonical repository-owned metric artifacts. This
finalizer only handles two historical edge cases:

1. a metric artifact did not yet exist at a cutoff, but the owning repository
   can evaluate the historical source tree with its current read-only renderer;
2. the repository itself did not yet exist at the cutoff, in which case a
   cumulative numeric stock has a pre-inception baseline of zero.

No semantic VSM state is inferred here.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


INDEX_REPO = "opensiro/vsm-harness-index"
CORE_METRICS = {
    "included_assessments": "included_assessments",
    "catalog_entries": "catalog_entries",
}


class FinalizeError(RuntimeError):
    pass


def index_core_at_revision(index_root: Path, revision: str) -> dict[str, int]:
    renderer = index_root / "scripts" / "render_metrics.py"
    if not renderer.is_file():
        raise FinalizeError(f"missing Index renderer: {renderer}")

    with tempfile.TemporaryDirectory(prefix="vsm-index-metrics-") as temp_dir:
        worktree = Path(temp_dir) / "tree"
        added = False
        try:
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(index_root),
                    "worktree",
                    "add",
                    "--detach",
                    "--force",
                    str(worktree),
                    revision,
                ],
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
            return {
                "included_assessments": int(data["included_assessments"]),
                "catalog_entries": int(data["catalog_entries"]),
            }
        except (subprocess.CalledProcessError, json.JSONDecodeError, KeyError, ValueError) as exc:
            raise FinalizeError(
                f"Index core renderer failed for historical revision {revision}"
            ) from exc
        finally:
            if added:
                subprocess.run(
                    [
                        "git",
                        "-C",
                        str(index_root),
                        "worktree",
                        "remove",
                        "--force",
                        str(worktree),
                    ],
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
                    entry["changed"] = True
                    entry["status"] = "derived_pre_inception_state"


def finalize_index_history(snapshot: dict[str, Any], index_root: Path) -> None:
    repo = snapshot["repositories"][INDEX_REPO]
    metrics = repo["metrics"]
    cache: dict[str, dict[str, int]] = {}

    for metric_name, core_name in CORE_METRICS.items():
        metric = metrics[metric_name]
        current = int(metric["value"])
        for entry in metric.get("window_change", {}).values():
            if entry.get("status") != "source_unavailable_at_baseline":
                continue
            revision = entry.get("baseline_revision")
            if not revision:
                raise FinalizeError(
                    f"{metric_name} historical source missing without baseline revision"
                )
            if revision not in cache:
                cache[revision] = index_core_at_revision(index_root, revision)
            baseline = int(cache[revision][core_name])
            entry["baseline"] = baseline
            entry["value"] = current - baseline
            entry["status"] = "derived_net_change_via_repository_renderer"
            entry["baseline_source"] = "Index scripts/render_metrics.py --stdout-core-json"


def finalize(snapshot: dict[str, Any], index_root: Path) -> dict[str, Any]:
    if snapshot.get("publication", {}).get("window_change_semantics") != (
        "net canonical state change, not gross event count"
    ):
        raise FinalizeError("unexpected or missing window-change semantics")
    finalize_pre_inception(snapshot)
    finalize_index_history(snapshot, index_root)
    snapshot.setdefault("publication", {})["historical_gap_policy"] = (
        "repository renderer when canonical artifact predates instrumentation; "
        "zero baseline before repository inception"
    )
    return snapshot


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--index-root", type=Path, required=True)
    args = parser.parse_args()

    try:
        snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
        finalized = finalize(snapshot, args.index_root)
    except (OSError, json.JSONDecodeError, FinalizeError, KeyError, TypeError, ValueError) as exc:
        raise SystemExit(f"metrics window finalizer error: {exc}") from exc

    args.snapshot.write_text(
        json.dumps(finalized, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
