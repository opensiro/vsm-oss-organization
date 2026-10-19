# Prospective source-first Index semantic-review handoff

Owner: [Organization #189](https://github.com/opensiro/vsm-oss-organization/issues/189). Related but disjoint: [#188](https://github.com/opensiro/vsm-oss-organization/issues/188) (complementary S3* batch audit) and [#194](https://github.com/opensiro/vsm-oss-organization/issues/194) (audit-slot claims). This is an **Organization-to-Index governance handoff**, not a second Index admission protocol or Profile/Skills semantic definition.

## Why this exists

An Index S1 assessment author can produce a proposed assessment and successful exact-head CI without having supplied a separately attributable semantic reviewer verdict. The owner must be able to invoke a **different actual human or agent execution context**, record what that reviewer concluded from primary sources *before* showing the proposed classification, and route the evidence to the ordinary Index PR process.

Do not equate the following: complementary Organization S3* audit verdict; independent source-first semantic reviewer verdict; a formal GitHub approving Review; an authorized Index admission. Each is a separate fact with a separate owner.

## Bounded prospective workflow

1. **REQUESTED.** Index owning lane provides frozen upstream source repository and 40-hex source SHA, active Profile/Skills refs, Index issue URL and proposed PR URL/head *to the coordinator only*. In an unassigned REQUESTED state, encode reviewer_context, reviewer_execution_ref, source_verdict and comparison as null; producer_context may also be null when its actual execution identity is unknown. A null means **not yet established**, never an inferred different reviewer. Actual nonblank distinct context IDs become mandatory at SOURCE_VERDICT_RECORDED and later phases. Prepare an isolated **source input list** for the reviewer that excludes the producer vector, author rationale, assessment file, PR description and preferred conclusion. A prompt/persona switch inside the author's context does not satisfy actor separation.
2. **SOURCE_VERDICT_RECORDED.** Reviewer independently checks shipped first-party boundaries, reachable modes, S1-S5 closure rights, counterexamples and bounded absence/uncertainty. Publish a source-first receipt with six per-function source-derived conclusions, adverse paths, primary permalinks, and a timestamp, all before proposal exposure. If source access, context separation or blinding cannot be established, publish **INSUFFICIENT** and stop rather than claiming a blind independent verdict.
3. **RECONCILED.** Only after preserving the immutable source-first record, reveal the author's proposal and compare at the exact PR head. Return a review handoff result PASS / FINDING / INSUFFICIENT to the owning Index lane. Identify disagreement and specific primary evidence. Re-run from new head after any author correction; no stale receipt may silently unlock a changed head.
4. **INDEX_GATE (Index-owned).** Index alone adjudicates the semantic findings, resolves its own review, produces the *separate* admission/exclusion PR, obeys GitHub permissions and exact-head CI, merges through delegated authority, verifies live main and advances the serial board. A source-first PASS is not formal GitHub APPROVED, branch-rule compliance, or automatic canonical admission.
5. **OPTIONAL S3* CONSUMPTION.** A complementary Organization S3* finding may be cited, but it neither creates a blind first verdict nor authorizes repair or S3 current-control escalation by itself. A real S3 issue must meet its separate whole-system admission rule.

## Source-first receipt and validation

The standalone [source-first validator](../../scripts/check_index_reviewer_handoff.py) validates a prospective JSON record with phases REQUESTED / SOURCE_VERDICT_RECORDED / RECONCILED, actual context identifiers, exact-source-SHA-pinned input links, a public independent-execution reference, exactly six function entries, an evidence-first timestamp and a later comparison.

**All**, not just one, `reviewer_input_refs` must be either tree/file links pinned to the exact frozen upstream `source_repository@source_sha`, or the already declared Profile/Skills normative references pinned to full commit SHAs in their correct owning repositories. This excludes arbitrary GitHub issues, PRs, branch links and unrelated sources from a purportedly blind stage. Every per-function `source_verdict.functions[].primary_refs` must be pinned to the original upstream SHA, rather than just be a syntactically valid GitHub link; normative documents inform classification but are not substitutes for first-party source evidence. Anchored source line references are permitted. The `index_issue` and `proposal_pr` identifiers must be canonical links in `opensiro/vsm-harness-index`; a link to another repository cannot designate the owning Index gate. Literal actor-context identifiers are compared after trimming incidental surrounding whitespace, but neither textual inequality nor a GitHub account name attests to actual execution separation.

The validator deliberately **cannot** prove that two contexts were truly isolated, that cited source files exist or support the verdict, that branch rules were met, or that a GitHub approval occurred. Treat a successful structural check as a necessary consistency check, **never** sufficient independent semantic evidence.

Run:

    python scripts/check_index_reviewer_handoff.py path/to/record.json
    python -m unittest tests.test_index_reviewer_handoff -v

A record may be submitted as evidence to an Index issue/PR only under its own authorizations. This Organization artifact may not rewrite Index assessments, issue boards, Profile/Skills definitions, historic W001/W002 receipts, or the selected current-work scheduler.

## Early INSUFFICIENT: external fail-closed receipt

The three machine handoff `phase` values document progress **only if that phase actually happened**. An early failure (no separately attributable reviewer, contaminated input, missing pinned sources, inability to preserve a source-first checkpoint, or missing access) may occur **before** any six-function `source_verdict` exists. Do **not** change `phase` to an invented completed state, add placeholder S1–S5 judgments, or create a fake `reviewer_context` / `reviewer_execution_ref`. The validator intentionally does not accept `phase=INSUFFICIENT` or a missing verdict as `SOURCE_VERDICT_RECORDED`.

**External fail-closed receipt path (not the JSON handoff record):**

1. The actual coordinator/observer records a durable, dated **`REVIEW_INSUFFICIENT`** Markdown comment in the **owning Index issue**, with a link from the relevant Index PR when one exists. Cross-link Organization #189 / #207 only as relevant. This is an operational workflow disposition, **not a VSM grade, reviewer verdict, or GitHub approval**. A simply unassigned `REQUESTED` packet remains pending unless an actual bounded attempt is explicitly terminated as insufficient.
2. The comment must identify: the exact Index issue/PR URLs and reviewed PR head (if known); frozen `source_repository@source_sha` and Profile/Skills refs (or state which ones could not be established); observed UTC time; **actual** reporting actor/context (or honestly unknown); observed reason and specific missing evidence/independence/execution capability; whether proposed conclusions were already exposed (yes/no/unknown); and the next permissible remedy or explicit stop. State that **no source-first verdict was recorded** when that is the case. A not-started reviewer has **no** reviewer identity, execution URL or initial verdict; never substitute the reporting actor for the reviewer.
3. Preserve any structurally valid `REQUESTED` JSON packet separately as pending, or record that no JSON packet could be formed. The external comment is linked evidence of a failed attempt, **not** a completed `SOURCE_VERDICT_RECORDED` / `RECONCILED` record and **not** input that can validate as a successful handoff. Reattempt only under a newly verified actor/input/head boundary; preserve the earlier failed receipt rather than overwriting history.
4. The **Index owner** determines the applicable gate: where a task-specific independent-review gate exists, `REVIEW_INSUFFICIENT` **does not satisfy a task-specific independent-review gate** and admission remains blocked. Where no such gate exists, ordinary Index PR/CI policy may proceed with explicitly non-blind provenance; never invent an unconditional reviewer requirement for every assessment. Organization does not decide Index admission or grant GitHub review permissions.

Example comment (values must be observed, not fabricated):

```text
Disposition: REVIEW_INSUFFICIENT (external fail-closed receipt; no review executed)
Index issue / PR / exact head: <actual URLs and SHA, or unknown>
Frozen source / Profile / Skills: <actual pinned refs, or missing>
Recorded at (UTC): <observed timestamp>
Reporter identity/context: <actual coordinator/observer, or unknown>
Reviewer identity/execution: NOT ESTABLISHED
Producer proposal exposure: <yes/no/unknown>
Reason and missing evidence: <concrete observed blocker>
Source-first checkpoint: NONE; no source-first verdict was recorded
Applicable Index gate / next step: <verified gate and remedy or stop>
```

## Explicit negative gates

- same producer/reviewer context, fabricated context identifier or absent independently checkable execution trace: **INSUFFICIENT**, never claim independently conducted review;
- a reviewer source input containing the producer PR, proposed vector, assessment file or proposed outcome: **contaminated**; no blind first-verdict claim;
- missing original frozen source, an exact-SHA primary source link, source refs, six source-derived claims, adverse/uncertain paths, primary links: **INSUFFICIENT**;
- source verdict timestamp later than proposal exposure, or subsequent PR head changed: **stale/contaminated**, request a new scoped review;
- unavailable eligible GitHub reviewer, pending/failed checks, or absent actual Index authority: **Index gate remains unresolved**; never spoof another GitHub user or self-approve.

## Completion boundary

This PR provides **prospective policy and deterministic negative checks only**. It does not instantiate a different agent context, create a live source-first verdict, resolve #189 acceptance, prove Organization S3*=A, or change S1 autonomy classifications. A separate real invocation and owner-authorized Index handoff remain required.
