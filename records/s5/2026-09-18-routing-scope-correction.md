# S5 parent decision record — routing scope correction

This record reconstructs a historical decision after the fact using the current parent-authority declaration. It does not claim that this record or `S5_PARENT_AUTHORITY.md` existed on 2026-09-18.

## Decision identity

- decision / work item id: `S5-P-001`
- decision date: 2026-09-18
- reconstruction date: 2026-09-20
- system-in-focus: bounded OpenSiro VSM Harness OSS organization
- governing Organization revision at closure: PR #62 merge commit `f1406f1433269e8b7b676a05df45d5629f6c281f`
- governing Profile / Methodology contract at closure: Profile `v0.2.2`; Methodology `0.3.1` at `01e13e595c101bd526fd1913863bfd8170f08116`; Index contract source `main`

## Matter

- exact identity / ultimate-policy question: whether the Organization's governed/routing population should expand to every public repository under `opensiro`, or remain the explicitly declared five-repository VSM Harness OSS boundary.
- why this is S5-level at the declared recursion: the choice changes the declared system-in-focus / participation boundary, not merely implementation inside an existing operational domain.
- lower-level S1 / S3 / S3* authority considered: Index, Skills, and Awesome may regulate their own operations; S3 may regulate current operation inside an already-selected boundary; S3* may audit claims. None owns the ultimate right to redefine which repositories constitute this viable system.
- why the matter cannot be closed safely inside that delegated envelope: admitting or excluding repositories changes organizational identity/scope for all lower-level functions and conformance evidence.

## Parent authority

- legitimate parent role: OpenSiro organization owner, as declared in `S5_PARENT_AUTHORITY.md`
- concrete decision owner: `xLagerFeuer`
- primary evidence of parent legitimacy: `S5_PARENT_AUTHORITY.md`, including its continuity declaration for issue #59 / PR #62
- decisive S5 right: set the declared system-in-focus / repository participation boundary for this recursion
- authority limits / caveats: the role does not own ordinary S1/S3/S3* decisions merely because the holder can technically merge or administer repositories

## Evidence / options

- primary evidence refs: issue #59; PR #62; PR #62 merge commit `f1406f1433269e8b7b676a05df45d5629f6c281f`; `README.md`; `ORGANIZATION.md`; `ROUTING_CONFORMANCE.md`; `S5_PARENT_AUTHORITY.md`
- relevant prior state: #60's routing oracle had widened the proof population to all public OpenSiro repositories, producing an 8/8 public-repository routing result
- viable options considered:
  - keep all public OpenSiro repositories inside the routing/proof population;
  - restore the Organization to the five repositories explicitly declared in its bounded scope
- consequence of no decision: Organization conformance evidence would continue to mix unrelated research/presentation tracks into the bounded VSM Harness OSS system and misstate the system boundary

## Parent decision

- lifecycle state: `CLOSED`
- authoritative decision: keep the bounded Organization scope at exactly the declared five repositories — `vsm-harness-profile`, `vsm-harness-skills`, `vsm-harness-index`, `awesome-vsm-harness`, and `vsm-oss-organization`
- returned policy / identity constraint: public visibility or membership in the `opensiro` GitHub organization does not itself admit a repository into this viable system; scope changes require an explicit Organization boundary decision
- decision evidence ref: issue #59 + merged PR #62, with current parent-role continuity confirmed by `S5_PARENT_AUTHORITY.md`

## Support / enforcement

Mechanisms that transported/enforced the returned decision without owning it:

- GitHub issue / PR: #59 / #62
- ruleset / permissions: none required for the semantic decision
- plugin / connector: GitHub transport only
- CI / validator: scoped routing workflow and routing-oracle tests
- other support: `README.md`, `CONTRIBUTOR_START.md`, `ROUTING_CONFORMANCE.md`, `scripts/check_public_routing.py`, workflow configuration and tests

## Return into Organization

- return target(s): canonical README scope consumption, contributor routing, routing conformance oracle, workflow target population, blind-trial population
- acknowledgement / application ref(s): PR #62 merged at 2026-09-18T21:33:48Z; merge commit `f1406f1433269e8b7b676a05df45d5629f6c281f`
- expected change or intentional preservation in subsequent operation: only the five declared repositories participate in the Organization routing invariant and proof population; `arctic-0`, `terminal-bench-vsm`, and `opensiro.com` remain outside it unless a later explicit scope decision admits them
- observed effect: routing code/docs/tests/workflow were changed to derive targets from the canonical README scope; the earlier 8/8 all-public result was explicitly superseded as evidence

## Closure

- final state: `CLOSED`
- closure evidence: merged PR #62 plus current scoped routing/conformance surfaces on `main`
- remaining uncertainty: this is a retrospective reconstruction; parent-legitimacy evidence was made explicit on 2026-09-20 rather than contemporaneously on 2026-09-18
- does this record support a positive `S5=P` witness? `YES`
- rationale: a genuine system-boundary decision was owned by the now-explicit legitimate parent, returned through first-party Organization surfaces, and measurably governed subsequent routing/conformance behavior. The parent-role continuity declaration supplies the missing ownership link without treating GitHub merge rights themselves as S5 authority.

## Boundary checks

- [x] matter is genuinely identity / ultimate-policy level;
- [x] legitimate parent role is explicit;
- [x] concrete decision owner is explicit;
- [x] parent legitimacy is evidenced independently of mere technical access;
- [x] decisive right is separated from support/enforcement;
- [x] returned decision reaches Organization operation;
- [x] subsequent operation changes or is intentionally preserved under the returned decision;
- [x] ordinary approval / merge / permission prompt is not being misclassified as S5;
- [x] no unrelated S2 / S3 / S3* / S4 autonomy claim is inferred from this record.

## Milestone interpretation

This record establishes evidence for the `S5=P` function/ownership arrangement. It does **not** formally complete M2 while M1 remains open; milestone sequencing in #4 still requires M1 completion before the M2 target vector is claimed as complete.
