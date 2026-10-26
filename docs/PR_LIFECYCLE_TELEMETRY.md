# Public OSS PR lifecycle snapshots (secondary, non-KPI)

**Owner:** `opensiro/vsm-oss-organization` (#208). This document owns the archive/collection mechanics, while `docs/METRICS.md` owns public metric interpretation. The bounded six-repository scope comes from the current Organization README after S5 decision #274. Historical five-repository snapshots retain their original scope.

The source of truth for PR lifecycle events and reviews is the **public GitHub REST API**; no browser or website parsing is involved. Unlike repository-owned *canonical outcome* metrics, this is gross engineering activity, not productivity/quality/verified-output evidence.

## Live collector

```bash
GITHUB_TOKEN=<your-read-token> python3 scripts/collect_pr_activity.py --output /tmp/opensiro-pr-activity.json
```

Use a short-lived read-only token in the environment (or the workflow's standard GitHub token); never commit credentials. Each record includes source URLs, `collected_at`, exact query semantics, sample sizes, a completeness state and API request count. A nonzero exit means some repository did not reach `complete`; inspect JSON even on nonzero exit. Partial review metrics are null and individually marked, while separately complete PR event counts remain usable.

The collector paginates **all current open PRs**, even if old, and all PRs updated since the 30-day cutoff. It paginates each relevant PR's entire submitted review history. API pagination exhaustion, GitHub errors, and unknown actor types fail closed for the *affected metric*, not as zero. The script deliberately does not use the Search API's 1,000-result cap. The current GitHub PR representation only preserves the latest closed state and is not an event-sourced replay of multiple reopen/close transitions. `collected_at` is a collection-start timestamp, not a GitHub-wide atomic snapshot.

## Durable archive

[`.github/workflows/pr-lifecycle-telemetry.yml`](../.github/workflows/pr-lifecycle-telemetry.yml) runs daily and can be invoked manually. It collects using `GITHUB_TOKEN` and commits dated snapshots to the independent repository branch `telemetry/pr-lifecycle`:

```text
refs/heads/telemetry/pr-lifecycle
  data/pr-lifecycle/snapshots/YYYY/MM/DD/<UTC-timestamp>.json
```

This is a Git-backed **append-only observational archive**, so old snapshots remain reviewable by commit SHA. The action never pushes generated data or changes to `main` and does not publish a website. Archive branch updates are serialized. Even a partial/unavailable snapshot is archived with honest status and the run fails visibly afterwards. If the branch or write permissions are unavailable, the workflow reports failure; the PR/review source remains in GitHub but there is **no claim that a snapshot was archived**.

Do not sum repository median hours or extrapolate review latencies from partial histories. Human identity and co-authorship of multi-actor external interventions belong to the separate experimental provenance ledger, not to this six-repo first-party PR-event count.

## Validation

```bash
python3 -m unittest tests.test_pr_activity -v
python3 -m unittest discover -s tests -q
```

For a read-only bounded live sanity check, compare the timestamp/source from any archive record with GitHub's original PR API and sample independently. Site [#28](https://github.com/opensiro/opensiro.com/issues/28) is **deferred** and not a prerequisite for retaining activity records.
