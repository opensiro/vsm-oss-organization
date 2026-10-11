# Prospective source-first Index semantic-review handoff

Owner: [Organization #189](https://github.com/opensiro/vsm-oss-organization/issues/189). Related but disjoint: [#188](https://github.com/opensiro/vsm-oss-organization/issues/188) (complementary S3* batch audit) and [#194](https://github.com/opensiro/vsm-oss-organization/issues/194) (audit-slot claims). This is an **Organization-to-Index governance handoff**, not a second Index admission protocol or Profile/Skills semantic definition.

## Why this exists

An Index S1 assessment author can produce a proposed assessment and successful exact-head CI without having supplied a separately attributable semantic reviewer verdict. The owner must be able to invoke a **different actual human or agent execution context**, record what that reviewer concluded from primary sources *before* showing the proposed classification, and route the evidence to the ordinary Index PR process.

Do not equate the following: complementary Organization S3* audit verdict; independent source-first semantic reviewer verdict; a formal GitHub approving Review; an authorized Index admission. Each is a separate fact with a separate owner.

## Bounded prospective workflow

1. **REQUESTED.** Index owning lane provides frozen upstream source repository and 40-hex source SHA, active Profile/Skills refs, Index issue URL, proposed PR URL/head *to the coordinator only*, and an actually distinct reviewer execution identity. Prepare an isolated **source input list** for the reviewer that excludes the producer vector, author rationale, assessment file, PR description and preferred conclusion. A prompt/persona switch inside the author's context does not satisfy actor separation.
2. **SOURCE_VERDICT_RECORDED.** Reviewer independently checks shipped first-party boundaries, reachable modes, S1-S5 closure rights, counterexamples and bounded absence/uncertainty. Publish a source-first receipt with six per-function source-derived conclusions, adverse paths, primary permalinks, and a timestamp, all before proposal exposure. If source access, context separation or blinding cannot be established, publish **INSUFFICIENT** and stop rather than claiming a blind independent verdict.
3. **RECONCILED.** Only after preserving the immutable source-first record, reveal the author's proposal and compare at the exact PR head. Return a review handoff result PASS / FINDING / INSUFFICIENT to the owning Index lane. Identify disagreement and specific primary evidence. Re-run from new head after any author correction; no stale receipt may silently unlock a changed head.
4. **INDEX_GATE (Index-owned).** Index alone adjudicates the semantic findings, resolves its own review, produces the *separate* admission/exclusion PR, obeys GitHub permissions and exact-head CI, merges through delegated authority, verifies live main and advances the serial board. A source-first PASS is not formal GitHub APPROVED, branch-rule compliance, or automatic canonical admission.
5. **OPTIONAL S3* CONSUMPTION.** A complementary Organization S3* finding may be cited, but it neither creates a blind first verdict nor authorizes repair or S3 current-control escalation by itself. A real S3 issue must meet its separate whole-system admission rule.

## Source-first receipt and validation

The standalone [source-first validator](../../scripts/check_index_reviewer_handoff.py) validates a prospective JSON record with phases REQUESTED / SOURCE_VERDICT_RECORDED / RECONCILED, actual context identifiers, exact-source-SHA-pinned input links, a public independent-execution reference, exactly six function entries, an evidence-first timestamp and a later comparison. It deliberately **cannot** prove that two contexts were truly isolated, that primary citations support the result, that branch rules were met, or that a GitHub approval occurred. Treat a successful structural check as a necessary consistency check, **never** sufficient independent semantic evidence.

Run:

    python scripts/check_index_reviewer_handoff.py path/to/record.json
    python -m unittest tests.test_index_reviewer_handoff -v

A record may be submitted as evidence to an Index issue/PR only under its own authorizations. This Organization artifact may not rewrite Index assessments, issue boards, Profile/Skills definitions, historic W001/W002 receipts, or the selected current-work scheduler.

## Explicit negative gates

- same producer/reviewer context, fabricated context identifier or absent independently checkable execution trace: **INSUFFICIENT**, never claim independently conducted review;
- a reviewer source input containing the producer PR, proposed vector, assessment file or proposed outcome: **contaminated**; no blind first-verdict claim;
- missing original frozen source, an exact-SHA primary source link, source refs, six source-derived claims, adverse/uncertain paths, primary links: **INSUFFICIENT**;
- source verdict timestamp later than proposal exposure, or subsequent PR head changed: **stale/contaminated**, request a new scoped review;
- unavailable eligible GitHub reviewer, pending/failed checks, or absent actual Index authority: **Index gate remains unresolved**; never spoof another GitHub user or self-approve.

## Completion boundary

This PR provides **prospective policy and deterministic negative checks only**. It does not instantiate a different agent context, create a live source-first verdict, resolve #189 acceptance, prove Organization S3*=A, or change S1 autonomy classifications. A separate real invocation and owner-authorized Index handoff remain required.
