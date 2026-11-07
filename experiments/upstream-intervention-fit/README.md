# Upstream Intervention Fit

Status: **DEPRECATED (2026-11-07)** — historical evidence only; no active metric or new fit scoring.

Issue: #165

This **retired historical experiment** asked whether upstream changes motivated by OpenSiro assessment/research remained independently useful to the upstream project when OpenSiro/VSM/grade pressure was removed from the rationale.

**Deprecation decision:** the maintainer retired the aggregate `product_native_fit_rate` as an active/public outcome metric. Preserve `observations.json`, `metric.json`, `compute.py` and the pinned `snapshot.json` for audit and reproducibility; **do not add new observations, change historic gate outcomes, publish refreshed percentages or use this ratio as a current performance indicator**. Subsequent external PR lifecycle, attribution and intervention records belong to [Upstream Contributions](https://github.com/opensiro/upstream), while the Organization-wide [Verified external outcomes](../../docs/METRICS.md#opensiroupstream) candidate and Upstream's independent [Resolved PR Acceptance](https://github.com/opensiro/upstream/blob/main/docs/RESOLVED_PR_ACCEPTANCE.md) retain their separate contracts. Neither is an automatic numerical replacement for this retired experiment.

Source-native engineering diligence—checking an actual upstream need, compatible mechanisms, independent test evidence and project scope—remains necessary when preparing contributions, **without issuing a four-gate fit grade**.

It is intentionally outside the canonical organization metrics contract. Nothing here changes `METRICS.md`, `metrics.yaml`, VSM semantics, assessment methodology, canonical grades, or organizational authority.

## Unit of observation

One observation is one **upstream intervention identity**: normally an upstream pull request, or a pre-PR branch/issue if no PR exists yet.

Rebases, review-fix commits, force-pushes, and revisions do not create new observations.

## Attribution and PR replacement chains

The durable entry is the **intervention**, not a PR number or a person. A maintainer may rebase or replace a contributor's original PR with a new PR while keeping the contributor's commits; one intervention may therefore have multiple linked PR URLs, but it is still counted once.

The original `pull_request` stays stable. An optional `related_pull_requests` list records each link with its `relation` (`original`, `landed_replacement`, or `related`) and independently observed PR `lifecycle`; when one merged PR is the accepted landing, its URL appears as `landing_pull_request`. The intervention's own `lifecycle` describes the overall accepted outcome. Do not backfill a merged outcome by silently rewriting an original closed-unmerged PR as merged.

Optional `participants` records each public GitHub account once per intervention with `github_login`, `account_type` (`github_user`, `github_bot`, `unknown`), `roles`, and first-party `evidence_urls`. Examples of roles are `original_pr_author`, `source_commit_contributor`, `landing_pr_author`, `merger`, `reviewer`, `review_fix_commit_contributor`. GitHub account classification does **not** certify a natural person or determine a share of impact. Review roles must be backed by an actual GitHub review, not an author comment. A link mentioning OpenSiro is not itself participation evidence.

`as_of` is the date the **ledger was updated**, not proof that every historical PR was rechecked on that day. `last_verified_at` may specify a case actually refreshed. Unverified participant identity and contributions stay unknown; avoid inventing roles or assigning credit by association.

This material remains **deprecated historical research outside** public canonical productivity/outcome metrics. The independent PR lifecycle collector is tracked under [Organization #208](https://github.com/opensiro/vsm-oss-organization/issues/208); it does not activate or refresh the retired ratio.

Historically, every intervention materially initiated or shaped by OpenSiro assessment/research belonged in this log, including rejected, withdrawn, closed-unmerged, and unsuccessful work. New intervention evidence must not be written into this frozen experiment.

## Deprecated primary metric — reproducibility only

`product_native_fit_rate`

```text
completed fit reviews = pass + fail
product_native_fit_rate = pass / completed fit reviews
```

`pending` interventions are reported but excluded from the denominator until the fit review is complete.

The frozen `2026-10-12` result was 3/5 (60%). **It is not a current KPI**, upstream acceptance rate, or VSM-grade-improvement rate.

## Fit gates

An intervention derives `pass` only when **all four** gates are supported by public evidence:

1. **upstream_need** — public upstream evidence or maintainer evidence supports a real upstream-native need, risk, problem, or workflow served by the intervention;
2. **native_mechanism** — the intervention uses or extends an upstream-owned mechanism/pattern rather than adding a VSM-only control surface;
3. **counterfactual_value** — the intervention remains justifiable if all OpenSiro, VSM, assessment, and grade language is removed;
4. **scope_compatibility** — current public upstream scope/direction does not conflict with the intervention.

Gate states are:

- `pass` — evidence supports the gate;
- `fail` — evidence materially contradicts the gate, or a completed negative-evidence review establishes that the required upstream-native basis is absent;
- `unknown` — evidence is incomplete.

Derived fit state:

```text
any gate = fail                  -> fail
all gates = pass                 -> pass
otherwise                        -> pending
```

A maintainer merge/approval is strong evidence but is not required and is not itself the metric. Likewise, a rejected PR is not automatically a fit failure: maintainers may reject a product-native change for implementation, timing, maintenance, or other reasons.

## Evidence discipline

Prefer, in order:

1. explicit maintainer statements or accepted upstream issue/roadmap intent;
2. current first-party upstream documentation and architecture;
3. current first-party implementation/extension points;
4. repository-wide negative-evidence review when a proposed responsibility appears to have no upstream-native basis.

OpenSiro's own assessment or desired grade cannot satisfy any gate.

## Anti-gaming rules

- Log all OpenSiro-shaped upstream interventions, not only successful ones.
- One intervention identity counts once regardless of revisions.
- Never use a grade increase as fit evidence.
- Do not classify `unknown` as `pass` to improve the metric.
- Do not convert merge state into fit state mechanically.
- Preserve closed/withdrawn observations; they remain part of experiment history.
- If evidence changes, update the observation and regenerate the snapshot rather than rewriting history elsewhere.

## Files

- `metric.json` — machine-readable metric and gate contract;
- `observations.json` — intervention log and evidence summaries;
- `compute.py` — deterministic stdlib-only validator/renderer;
- `snapshot.json` — frozen historical projection, reproducible from the original observations.

For archival verification only (no new data collection or publication):

```bash
python experiments/upstream-intervention-fit/compute.py --check
python experiments/upstream-intervention-fit/compute.py --stdout
```

## Initial cohort

The bootstrap cohort records the current interventions around:

- Marveen #1516;
- oh-my-agent #819;
- Scion #2047;
- Headcount #47;
- Henterprise #1.

The initial snapshot intentionally leaves incomplete reviews as `pending` rather than guessing fit.

## Extraction boundary

This directory is designed to move to a dedicated repository later without depending on Organization collectors or canonical metrics machinery.

A future extraction should be able to preserve the experiment contract, observations, computation, and snapshot essentially unchanged. Promotion/extraction is a separate decision; existence here does not admit a new repository into the bounded VSM OSS organization.
