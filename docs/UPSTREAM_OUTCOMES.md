# `upstream outcomes` — agent-assisted external outcome reconciliation

**Command:** `upstream outcomes` (alias `verify upstream outcomes`).

**Command owner:** the [Organization agent Control Plane](AGENT_CONTROL_PLANE.md).
**Evidence and case owner:** [`opensiro/upstream`](https://github.com/opensiro/upstream),
S1 Upstream Contributions. **Work owner:** [Upstream #159](https://github.com/opensiro/upstream/issues/159).
**Metric contract owner:** Organization's [metrics contract](METRICS.md) and
[`metrics.yaml`](../metrics.yaml). No further S1 domain, S3/S3* role or S5
delegation is created by this command.

## What actually runs

The command is a **source-first agent session entry**. It is executable in a
maintainer's current assistant context with sufficient public-source tools.
It is **not** a background ChatGPT job, an installed scheduler, an
independently executing S3* reviewer, or an automatically launched LLM in
GitHub Actions. Upstream's existing daily workflow performs deterministic
read-only sensing between agent invocations.

The operation has three distinct stages:

1. **Deterministic GitHub readback** — Upstream's
   [`scripts/verified_external_outcomes.py`](https://github.com/opensiro/upstream/blob/main/scripts/verified_external_outcomes.py)
   validates the finite source cohort, external PR/fork/merge identity, landed
   source delta and pinned native CI evidence.
2. **Automatic accepted-source export** — Upstream's
   [`scripts/accepted_external_outcomes.py`](https://github.com/opensiro/upstream/blob/main/scripts/accepted_external_outcomes.py)
   independently rechecks live GitHub evidence and exports strict
   `VERIFIED` cases as `ACCEPTED_MERGED_CHANGE_ONLY`, with
   `acceptance_basis=DETERMINISTIC_VERIFIED_MERGE`. No per-case owner
   decision, GitHub `APPROVED` review or S3* audit is required. Historical
   owner decisions are optional provenance, not a prerequisite.
3. **Agent semantic review** — only unresolved first-party disposition and
   contribution attribution (`PENDING_REVIEW`) need case-specific source
   examination and a reviewable dossier, not automatic acceptance.

The authoritative current Upstream specification is
[`docs/VERIFIED_EXTERNAL_OUTCOMES.md`](https://github.com/opensiro/upstream/blob/main/docs/VERIFIED_EXTERNAL_OUTCOMES.md).

## Invocation protocol

1. **Bootstrap and admission.** Read the current Organization
   [`START_HERE.md`](../START_HERE.md), owner map and S1 admission contract;
   then current Upstream `main`, its [#159](https://github.com/opensiro/upstream/issues/159),
   `UPSTREAMING.md`, `docs/VERIFIED_EXTERNAL_OUTCOMES.md` and the exact
   source ledgers. Check for concurrent operators/PRs for a candidate before
   proposing a write. A closed #159 or changed cohort is not permission to
   silently invent a successor task or alter the metric.
2. **Obtain current evidence.** Run
   `python3 scripts/verified_external_outcomes.py --validate-only` on
   current Upstream source. With authorized read-only GitHub API access, run
   `--report --output-json <path>`, then
   `scripts/accepted_external_outcomes.py --observation-json <path>`
   (or read both JSON files in the latest successful live workflow artifact).
   Verify source/cohort digests, timestamp, exact external evidence and
   live-revalidated accepted-source output. No complete live readback means
   `LIVE_EVIDENCE_UNAVAILABLE`; offline tests or a stale artifact are not
   substitutes.
3. **Preserve four distinct observation statuses.** A strict machine
   `VERIFIED` result is automatically `ACCEPTED_MERGED_CHANGE_ONLY` in
   Upstream's accepted-source export, with `benefit_claim=NOT_MEASURED`.
   This is **not** an Organization metric claim. `PENDING_REVIEW` requires
   semantic attribution, `INSUFFICIENT_EVIDENCE` has no externally merged
   resolution, and `UNVERIFIABLE` remains unavailable. Missing evidence
   is not a zero or a rejection.
4. **Review bounded ambiguity.** For every eligible `PENDING_REVIEW` record
   chosen within the current admitted task, inspect its original and landing
   PR URL(s), current first-party state, exact commits/diffs, issue closure
   events and maintainer discussion, contributor identity, and pinned
   test/source receipts. Verify whether the upstream maintainer **merged this
   contributor's work**, made a separately attributable replacement, or
   independently implemented a similar idea. Closing actor is not closure
   motive; a duplicate/replacement chain is **one intervention**, never two
   accepted contributions. Do not run live third-party model/agent quality
   experiments as an evidence shortcut.
5. **Return a reconstructable dossier for ambiguity.** Use the
   [review template](../prompts/upstream-outcome-review.md) with exact
   intervention ID, source digests, event/actor, contribution/commit link,
   native receipt, alternatives, limitations and any actually required
   source-owner decision. Do not ask the maintainer to approve a strict
   machine-`VERIFIED` case again.
6. **Correct genuine ambiguity at the owner.** If the governing Upstream
   task admits it and GitHub permissions permit it, propose an **internal
   Upstream PR** with source-pinned evidence, duplicate and CI checks for
   an ambiguous case. Do not append an owner-decision row for every new
   `VERIFIED` case: the accepted-source export is derived automatically.
   Existing historical decisions remain optional provenance. Do not create
   a parallel Organization factual ledger or invent an S3* reviewer gate.
7. **Organization integration is a separate gate.** Even a nonempty,
   live-revalidated export remains `UPSTREAM_ACCEPTED_SOURCE_ONLY` with
   `organization_metric_claimed=false`. An Organization-owned collector
   change, reviewed under its metrics contract, must separately activate
   `verified_external_outcomes`. [Product-native fit is deprecated](METRICS.md)
   and must not be reactivated. Raw external PR counts and native tests
   alone are not this metric.

## Required result

Return a compact `DONE / NOW / BLOCKED / NEXT / NEED YOU` summary containing:

- verification timestamp, Upstream source commit and evidence/artifact URL;
- source cohort identity and **intervention** count versus PR URL count;
- machine `VERIFIED` candidates, `PENDING_REVIEW`, `INSUFFICIENT_EVIDENCE`,
  `UNVERIFIABLE` separately, with no implicit zero for inaccessible cases;
- semantic-review dossiers and exact PR/issue links, including negative results;
- automatic Upstream accepted-source export count/basis versus the **separate**
  Organization metric claim status (`unclaimed` until its own gate passes);
- any current tool, third-party authority, test or integration blocker.

The command does **not** automatically publish external PRs, approve/merge
third-party changes, approve its own review, archive forks, update `TODO.md`,
rewrite historical fit, claim deployed user benefit, or create background
agent infrastructure. Stop and escalate only the real residual authority
gap; routine S1 source analysis stays with Upstream.
