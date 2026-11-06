# Cross-S1 Consistency Coordinator — prospective M4/S2 candidate

**Status:** PROPOSED / READ-ONLY DESIGN / NOT DEPLOYED / NOT S2 EVIDENCE (2026-10-13).

**Governing authority:** [Organization M4 #6](https://github.com/opensiro/vsm-oss-organization/issues/6) and [selected Profile §6](https://github.com/opensiro/vsm-harness-profile/blob/v0.2.4/PROFILE.md). This RFC does not redefine the Profile, grant S2 decision rights, schedule M4, or establish `S2=A`. Formal M4 follows M3. For actual work selection, read [`TODO.md`](../TODO.md); its NOW/NEXT are unchanged.

## Objective: automate coordination around assessments, not reassess each harness

The assessment itself stays with **Index S1**: source-first inspection, classification, evidence, correction and canonical admission. **Skills S1** owns the assessment Methodology; **Awesome S1** owns downstream representative curation. S2's candidate contribution is to reduce **cross-S1 interference affecting these assessment operations** (incompatible change order, repeated invalidation, conflicting assumptions), without taking the underlying S1 decisions.

At a *lower recursion inside Index*, coordinating many assessment workers may be another S2 question, but multiple Index workers are not multiple **Organization S1 domains**. A Reviewer Batch, a reviewer queue, another assessment, PR review, source-first reassessment, generic workflow scheduler, or a second GitHub account does not establish Organization S2. The undeployed Independent Reviewer experiments were paused under [archive PR #223](https://github.com/opensiro/vsm-oss-organization/pull/223); this RFC neither reactivates them nor imposes an independent-review gate.

## Initial domain pair: Index ↔ Awesome

Current first-party supporting evidence:

- [Awesome consistency validator](https://github.com/opensiro/awesome-vsm-harness/blob/main/scripts/validate_index_consistency.py) checks references from curated Awesome entries against Index's canonical assessment identities, links, anchors and expected source repositories.
- [Awesome Index-consistency CI](https://github.com/opensiro/awesome-vsm-harness/blob/main/.github/workflows/index-consistency.yml) checks the Awesome worktree against Index `main`.
- [Organization S1 domain contracts](../contracts/s1/domain-contracts.md) assign Index canonical assessment decisions and Awesome curated publication to distinct S1s.

These prove a dependency and an existing deterministic check, **not an observed S2 disturbance or an agent-owned coordination path**.

**Candidate collision to investigate:** a valid, in-flight Index assessment identity/anchor correction and a valid, in-flight Awesome curated-entry update overlap on the same source relationship. Their independent actions conflict in an order-sensitive way, cannot be resolved by one S1 locally under existing rights, and risk repeated invalidation or publication instability. A simple stale Awesome link and its local repair is **Awesome S1**, not S2. A hypothetical race without concrete interacting changes is **not** positive evidence.

A separate later candidate, **Skills ↔ Index Methodology transition**, must earn its own live disturbance evidence; ordinary planned Methodology uptake is not automatically S2.

## Preliminary qualification gate

Before designing a runtime or asserting a coordination event, identify:

1. Two **different** Organization S1 domains, their independently admitted current tasks and immutable issue/PR refs.
2. Exact source bases/heads/selected contracts and a specific overlapping assumption or relationship.
3. An actual or **structurally evidenced** interference/conflict/oscillation **caused by their interaction**; not merely the existence of dependency, shared CI or normal local failure.
4. Why the already authorized S1 local remedies and deterministic gates are insufficient to settle the cross-S1 interference.
5. An explicitly authorized **bounded cross-S1 coordination right**, an agent to exercise actual discretion, and separately identified S1 decision owners.
6. Two-S1 return/acknowledgement and a post-decision oracle proving subsequent operations changed to attenuate the identified interference.

Stop as `NOT_QUALIFIED_LOCAL` or `INSUFFICIENT` without opening an S2 transaction when any of these are missing. Do not manufacture concurrent PRs or break CI to force a qualifying case.

## Proposed decision and feedback loop (NOT ACTIVATED)

1. **OBSERVE:** check already-authorized live Index/Awesome work, CI and immutable Git refs; record a possible collision with both source links.
2. **QUALIFY:** distinguish cross-S1 interaction disturbance from local S1 errors and normal dependency checks.
3. **FREEZE:** record evidence before discretion, actor/context identity, actual allowed response types and existing authority, using the [prospective receipt template](../templates/s2-cross-s1-collision.md).
4. **DECIDE:** if *and only if* an agent has a prospective delegation, choose a justified bounded compatibility/sequence response (`INDEX_FIRST`, `AWESOME_FIRST`, `REQUEST_MUTUAL_ADJUSTMENT`) or `ESCALATE` where insufficient. It must decide a real coordination tradeoff, not just run a fixed ordering rule.
5. **RETURN:** route the choice to **both** source-of-truth S1 owners and capture each acknowledgement/outcome. Neither S1's assessment/curation rights nor GitHub merge/CI permissions are transferred.
6. **VERIFY:** inspect subsequent exact refs/operations and consistency evidence; document actual prevention, bounded invalidation or reduced oscillation. A completed workflow, green check, static queue or a unilateral comment is not proof of S2 closure.

The agent may **recommend** pauses or aligned sequencing; it cannot impose them without established authority. A global resource/priorities decision belongs to **S3**; Organization identity/policy is **S5**; S3* complementary audit remains separate. Support mechanisms (locks, CI, validators, GitHub APIs, receipts, queues) cannot claim the S2 discretionary owner role.

## Decision table and negative cases

| Evidence | Appropriate classification |
| --- | --- |
| Single Awesome link stale after a finished Index change; Awesome fixes it | Awesome S1 local work |
| Only `Index main` and Awesome's validator disagree; deterministic repair suffices | S1 / existing CI support, **not** S2 |
| Two S1 operations exhibit a real/structurally pinned interaction conflict but no authorized agent decision | Candidate only, **not** `S2=A` |
| Coordinating agent with delegated discretion chooses a cross-S1 response; both S1s acknowledge and later effects attenuate conflict | Prospective **S2 functional evidence**, subject to M4 evaluation |
| Scheduler always processes Index before Awesome with no agent-owned choice | Mechanical support; **not** `S2=A` |
| Coordinator allocates organization-wide token budget or overrides canonical grade | S3 / out of scope, **not** S2 |
| Missing frozen refs, conflict proof, decisive owner, S1 return or measured effect | `INSUFFICIENT` |

## Admission, authority and stop rules

This RFC is a **design candidate only**; no standing observer, agent, queue, cross-repo execution, or claims of S2 autonomy are implemented. A future M4 execution issue must re-read [M4 #6](https://github.com/opensiro/vsm-oss-organization/issues/6), live Profile/Skills contracts, M3 completion and actual S1 work; freeze one naturally occurring qualified collision and its separately delegated rights **before** any S2 decision. If none exists, stop without an invented trial. No extra GitHub identity or independent reviewer is presumed.

No changes to Index/Skills/Awesome implementation, Index classification or assessments, `TODO.md`, M1/M2/M3 state, active S3/S3*/S5 constructors, branch rules or GitHub review requirements.
