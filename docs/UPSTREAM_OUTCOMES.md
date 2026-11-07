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

The operation has two different loops:

1. **Deterministic GitHub readback** — Upstream's current
   [`scripts/verified_external_outcomes.py`](https://github.com/opensiro/upstream/blob/main/scripts/verified_external_outcomes.py)
   validates the finite source cohort, contribution/fork/merge identity,
   source SHA, pinned native CI receipt and complete post-publication diff
   when needed. Its authoritative specification is
   [`docs/VERIFIED_EXTERNAL_OUTCOMES.md`](https://github.com/opensiro/upstream/blob/main/docs/VERIFIED_EXTERNAL_OUTCOMES.md).
2. **Agent semantic review** — the current agent investigates unresolved
   first-party disposition and contribution attribution using exact external
   PR/commit/review/issue-event sources. It produces a reviewable evidence
   dossier, not its own accepted outcome ledger or an independent audit.

## Invocation protocol

1. **Bootstrap and admission.** Read the current Organization
   [`START_HERE.md`](../START_HERE.md), owner map and S1 admission contract;
   then current Upstream `main`, its [#159](https://github.com/opensiro/upstream/issues/159),
   `UPSTREAMING.md`, `docs/VERIFIED_EXTERNAL_OUTCOMES.md` and the exact
   source ledgers. Check for concurrent operators/PRs for a candidate before
   proposing a write. A closed #159 or changed cohort is not permission to
   silently invent a successor task or alter the metric.
2. **Obtain current evidence.** Run `python3 scripts/verified_external_outcomes.py --validate-only`
   on current Upstream source. With an authorized read-only GitHub token run
   `--report --output-json <local-output-path>`; otherwise read the **latest verified live**
   workflow artifact via an available GitHub connector. Verify timestamp,
   source SHA256 and cohort fingerprint against the current owner state. If
   no full live readback is available, report `LIVE_EVIDENCE_UNAVAILABLE`;
   offline passing tests are not a substitute. Never quietly use an expired
   or old cohort artifact.
3. **Keep four source statuses intact.** `VERIFIED` is a machine-checked
   **candidate**, not an Organization-accepted stock item.
   `PENDING_REVIEW` calls for semantic attribution; `INSUFFICIENT_EVIDENCE`
   means the gate has not completed; `UNVERIFIABLE` remains explicitly
   unavailable. A missing result is not a zero or a rejection.
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
5. **Return a reconstructable dossier.** Use the [review template](../prompts/upstream-outcome-review.md)
   with the exact intervention ID, source digests, observed event and its
   actor, contribution/commit link, native test receipt, alternative
   interpretations, reasons for the proposed verdict, limitations and the
   specific owning decision still required. An unattributable or ambiguous
   result stays unclaimed; do not prompt the maintainer to choose an outcome
   merely because the evidence is inconvenient.
6. **Propose, do not self-certify.** If the specific Upstream task admits the
   change and GitHub rights permit it, prepare a reviewable **internal
   Upstream PR** against an Upstream-owned accepted outcome ledger (once its
   schema is reviewed), with source-pinned receipts and duplicate/CI checks.
   Until that owner ledger exists, preserve the dossier as a proposal under
   [#159](https://github.com/opensiro/upstream/issues/159); do not create a
   parallel Organization-owned factual ledger. A reviewer may be requested
   for **actual ambiguous/high-risk claims** under existing rules; no
   universal independent S3* gate or fabricated approval is introduced.
7. **Organization integration is a separate gate.** Only after an Upstream
   owner-approved accepted ledger, live validation and a reviewable
   Organization collector change can `verified_external_outcomes` transition
   from `unclaimed_semantic_evidence` to an official stock value.
   [Product-native fit is deprecated](METRICS.md) and must not be reactivated.
   Raw PR acceptance and first-party technical tests are separate metrics.

## Required result

Return a compact `DONE / NOW / BLOCKED / NEXT / NEED YOU` summary containing:

- verification timestamp, Upstream source commit and evidence/artifact URL;
- source cohort identity and **intervention** count versus PR URL count;
- machine `VERIFIED` candidates, `PENDING_REVIEW`, `INSUFFICIENT_EVIDENCE`,
  `UNVERIFIABLE` separately, with no implicit zero for inaccessible cases;
- semantic-review dossiers and exact PR/issue links, including negative results;
- accepted Upstream ledger status and **independent** Organization metric
  claim status (`unclaimed` until its completion gate is actually met);
- any current tool, third-party authority, test or integration blocker.

The command does **not** automatically publish external PRs, approve/merge
third-party changes, approve its own review, archive forks, update `TODO.md`,
rewrite historical fit, claim deployed user benefit, or create background
agent infrastructure. Stop and escalate only the real residual authority
gap; routine S1 source analysis stays with Upstream.
