# Proposal: Upstream Contributions as an operational S1 domain

> **Status: PROPOSED / NOT ADMITTED.** This is a prospective, non-operative domain envelope for [Organization #274](https://github.com/opensiro/vsm-oss-organization/issues/274). It does not amend the current [canonical in-scope repository set](../../README.md), grant an S1 runtime autonomy state, authorize third-party upstream submissions, or transfer ownership of the experimental fit ledger. Its adoption requires an explicit parent S5 system-boundary decision and a separately validated application PR.

## 1. System boundary and operating purpose

**System-in-focus:** the current bounded public OpenSiro VSM Harness OSS organization at its existing recursion. **Candidate additional S1 domain:** `Upstream Contributions`, with `opensiro/upstream` as its portfolio/registry owner.

The other current operational domains retain their own products and closure rights:

| Domain | Owns | Does not own |
| --- | --- | --- |
| Index | canonical evidence-backed general assessment corpus, provenance, accepted assessments | external OSS PR acceptance or portfolio lifecycle |
| Skills | reusable assessment methodology, procedures, references and tools | decisions about an external project's product roadmap |
| Awesome | curated representative forms tied to canonical Index | external contribution outcomes |
| **Upstream (candidate)** | public intervention portfolio, OpenSiro-owned fork contribution lifecycle, documented upstream-native changes and attributed outcomes | canonical assessments, normative Profile, external maintainer decisions |

Profile remains normative semantic authority and Organization remains the metasystem/control construction. A contribution to external OSS may use Index evidence, but an Index assessment neither obliges an external project to accept a contribution nor proves upstream-native value.

**Primary transformation:**

```text
public upstream need / maintainer context / optional OpenSiro research
                  ↓
    candidate improvement + native-fit analysis
                  ↓
  authorized working fork / branch + implementation
                  ↓
    validation + reviewable third-party proposal
                  ↓
  externally owned disposition and local maintenance
                  ↓
     public evidence-linked outcome / portfolio
```

This is an operational production loop, not automatically an S4 adaptation loop. Future-oriented whole-system adaptation, if any, must be separately qualified from actual S4-specific decisive ownership and organizational return evidence.

## 2. Environment and durable result

The local environment comprises independently governed external OSS projects, upstream issues and maintainer feedback, contributor rules, APIs/interfaces, source trees, forks, CI, peer review, and change lifecycle. Internal inputs may include accepted Index findings and independently supported research; neither is a prerequisite for all external contributions.

**Durable result:** upstream-native OSS improvements and a truthful, source-backed record of proposed, implemented, submitted, landed, rejected, withdrawn, or still-open work, including OpenSiro-owned fork maintenance. Negative/no-change results must remain observable rather than disappearing from the portfolio.

An output is not automatically successful because a PR was opened or a VSM grade was discussed. A landed external code change is counted as landed only with external upstream merge/integration evidence; accepted ideas implemented independently by maintainers have their own attribution and outcome distinction.

## 3. Prospective delegated S1 decision rights

For one **admitted bounded** contribution, an authorized S1 executor may:

1. Inspect current external primary sources, maintainer issues, local portfolio and relevant Index/research evidence.
2. Decide a task-local research, implementation, repair and validation strategy within the specified contribution scope.
3. Select an upstream-native mechanism supported by primary evidence; reject a speculative change where native need cannot be established.
4. Prepare and validate changes only in authorized repositories/branches with already granted credentials and existing project requirements.
5. Package reviewable code, documentation, or an evidence-backed no-change result.
6. Maintain the `opensiro/upstream` registry, casebook, project profile, contribution-status and fork-lifecycle **facts** when source-backed and inside current local policy; correct stale or misleading links, attribution or dates.
7. Recover from routine task-local errors without silently broadening authority, and preserve an auditable outcome.

**Not delegated by admission:** submission to third-party upstream or contact with maintainers without an applicable specific authorization; merging/approving changes in someone else's repository; archival of forks absent the explicit local archive decision; changes to global organizational boundary, identity, ultimate policy or cross-domain rights; licensing, security or permission expansion; creating a VSM-named control feature in another project against its native scope; assigning new canonical Index grades, Profile meanings or Methodology judgments; managing personal contributor forks by implication.

The third-party maintainer's right to accept, reject, amend or supersede a contribution is external to OpenSiro. A maintainer-authored replacement can preserve contributor attribution without turning the original PR into a merged PR. The S1 runner must obey explicit upstream issue assignment, contribution and contest eligibility rules when relevant.

## 4. Admission, validation, recovery and closure

Use the shared [S1 task admission/recovery contract](../../contracts/s1/task-admission-recovery.md) and [S1 actor adapter](../../roles/S1.md) **only after this domain is admitted**. Each run identifies one domain, issue/target, exact source state, scope, authority, forbidden operations, completion oracle, residual variety and integration owner.

Minimum public evidence for a recorded intervention, where applicable:

- actual external project, public issue/PR/commit links and exact tested source/fork refs;
- source-based upstream need, native mechanism, scope fit and honest counterfactual rationale;
- reproducible validation or stated absence of runnable test surface;
- independent **contribution status**, **fork lifecycle** and (where assessed) **product-native fit**;
- participants and authorship grounded in PR/commit/review evidence, with replacement/landing chains deduplicated;
- date of verification and any missing/inaccessible facts explicitly marked unknown;
- maintenance obligations, recovery actions and final local outcome.

Internal terminal states follow the existing S1 contract: `CLOSED_CHANGE`, `CLOSED_NO_CHANGE`, `ESCALATED`, `NON_ADMITTED`. An upstream PR still awaiting third-party review may coexist with a completed **local** preparation/recording task. Conversely, recording a pending external outcome must not imply that upstream has accepted the change. A response or PR from an external maintainer remains external decision evidence, not OpenSiro S1-owned closure of their repository.

Escalate rather than infer authority when a task requires new system boundaries, policy, unrelated cross-S1 control, external submission permission, copyright/license clarification, credentials, or another unadmitted decision.

## 5. Source ownership and metrics

Current repository-owned fact split is preserved unless a subsequent specific migration is approved:

- **`opensiro/upstream`** owns its [registry and fork lifecycle](https://github.com/opensiro/upstream/blob/main/registry.yaml), [public casebook](https://github.com/opensiro/upstream/blob/main/cases/README.md), [dashboard](https://github.com/opensiro/upstream/blob/main/DASHBOARD.md), and local contribution profiles. This repository is *not* the upstream codebase or a monorepo of forks.
- **`opensiro/vsm-oss-organization`** currently owns the [experimental upstream-intervention-fit source ledger](../../experiments/upstream-intervention-fit/README.md), deduplication, primary fit gates and snapshot. Upstream dashboard presentation consumes a pinned copy; it does not independently assign fit grades.
- **External upstream projects** own external source code, maintainership, issue/PR dispositions and acceptance.
- **Index** owns canonical VSM assessments. The candidate Upstream domain is neither a grade-raising mechanism nor a second assessment corpus.

An optional future outcome metric should count **provenance-qualified outcomes** only under an approved repository-owned identity/event rule. Raw PR volume, commits, lines, opened issues, and dashboard page views are **not** S1 output/quality KPIs. Product-native fit rates must retain their exact denominator, unknown/pending rules, negative observations and as-of timestamps, and must never be reported as merge rate or autonomous-agent productivity.

## 6. Parent decision, implementation and test gate

The legitimate parent [identified in S5 authority](../../contracts/s5/parent-authority.md) must choose:

- **A — ADMIT_WITH_ENVELOPE:** approve a fourth S1 domain prospectively, bounded by this contract; make it operational only after the validated application changes below.
- **B — KEEP_ADJACENT:** continue the externally governed portfolio without broadening the VSM OSS organization scope.

The parent decision and return/application evidence belong to [Organization #274](https://github.com/opensiro/vsm-oss-organization/issues/274) and the [S5 decision procedure](../../contracts/s5/parent-boundary.md); an issue or proposed file alone does not exercise that right.

If **A** is selected, stage reviewable cross-repository implementation:

1. Update canonical Organization `README.md` scope and `docs/ORGANIZATION.md` viable-system identity/operational transformation, cross-repository `docs/ECOSYSTEM.md` ownership, and local S1 domain/role/operating-evidence documents without redefining Profile semantics.
2. Amend contributor routing, current-work eligibility and S1-domain allowlists/fixtures, as appropriate. Verify scripts and docs with hardcoded three-domain or five-repository assumptions.
3. Make the `opensiro/upstream` root README directly discover the Organization [START_HERE](../../START_HERE.md), [contributor route](../../CONTRIBUTOR_START.md) and [current work](../../TODO.md); leave local upstream status, product and contribution policy authoritative in Upstream.
4. Reconcile metrics-contract scope and collection tests before counting Upstream as an in-scope repo; don't silently change the experimental `upstream-intervention-fit` metric into an organization-wide outcome.
5. Validate applicable Organization contracts/tests, the live routing oracle, repository-local portfolio integrity, links, exact diffs, and a source-first bounded S1 reference case.
6. Record S5 returned/application closure, then only claim **domain admission / constructed S1 path**. A formal `S1=A` (or other grade) needs separately sufficient operational ownership evidence under the selected Profile/Methodology.
7. Preserve historical milestone/assessment provenance; do not automatically change M0–M5 closure/targets or select `TODO.md` work.

No third-party submission, unsolicited maintainer contact, external code change, fork archive or new authority grant is initiated by this proposal.

## 7. Operational-readiness evidence checkpoint — 2026-10-25

This is a **dated evidence update**, not an S5 admission decision or a change to the proposed S1 authority envelope. The owning [Upstream operational-readiness review](https://github.com/opensiro/upstream/blob/corrective/reef-19-register-watch/reports/2026-10-25-upstream-operational-readiness.md) is included in the reviewable [Upstream PR #129](https://github.com/opensiro/upstream/pull/129); it must not be mistaken for merged `main` state.

- The fixed 34-case Corrective cohort is **13 externally SUBMITTED / 21 BLOCKED / 0 QUEUED** on PR #129. The 21 blocked records are **not** published external PRs; this finite mandate must not be broadened implicitly. At the checkpoint, the Upstream default branch still had the older **8 SUBMITTED / 26 QUEUED** ledger.
- [PR maintenance #125](https://github.com/opensiro/upstream/issues/125) has a deployed **read-only hourly monitor for 13 PRs**; PR #129 proposes a watchlist of **18**. An 18-target active/default-branch monitor and a completed maintainer-request repair loop are **not yet evidenced**.
- The 18 proposed external targets were directly checked: **16 OPEN / 1 MERGED / 1 CLOSED**; the 13 Corrective PRs were **OPEN / Ready**, with no observed `CHANGES_REQUESTED` review. These are dated observations, not a perpetual count or an autonomous-contribution metric.
- The connected generic executor in [Upstream #6](https://github.com/opensiro/upstream/issues/6) is **inactive**. The strict Index-first [functional-improvement experiment #56](https://github.com/opensiro/upstream/issues/56) lacks a complete externally validated assessment → native before/after → upstream-outcome witness. Corrective submission volume does not supply that missing evidence.
- Consequently, the current evidence supports a sustained **adjacent** operating workstream and prospective S1 proposal, **not** a fourth admitted S1, an `S1=A` declaration, or a new standing external-publishing mandate. Reviewers should use [Organization #274](https://github.com/opensiro/vsm-oss-organization/issues/274) for the explicit S5 choice and apply the separate validation/migration gate in §6 if `ADMIT_WITH_ENVELOPE` is selected.

**Synchronization rule:** Upstream remains the source of truth for publication and watcher facts; this proposal links a dated bounded snapshot and must not duplicate it as a live Organization ledger. Before applying any admission decision, re-read current default-branch Upstream state and any unmerged follow-up PRs.
