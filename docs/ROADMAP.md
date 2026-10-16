# OSM Roadmap

This roadmap grows contributor autonomy bottom-up across the public OpenSiro OSS scope defined in [README.md](README.md). It follows the VSM Harness Profile rule: map the organizational function first, then identify the decisive decision/feedback right, its owner, supporting enforcement, and closure.

The current system-in-focus starts with three declared operational S1 domains — Index, Skills, and Awesome — while Profile remains the normative semantic source and `vsm-oss-organization` is the metasystem/control-construction surface.

The vectors below are milestone construction targets, not automatic grades or published assessment states.

The sequence is specific to this reference organization. It is not a universal VSM installation order, and `A`, `C`, and `P` are not maturity levels. They describe different ownership arrangements.

## GitHub milestone correspondence

| GitHub milestone | Tracker issue | Target vector | Scope introduced |
| --- | --- | --- | --- |
| `M0` — Autonomous operation | #2 | `A — — — — —` | Local S1 construction across Index, Skills, and Awesome. |
| `M1` — Audit + control constructors | #3 | `A — C C — —` | Function-specific S3 current-control and S3* complementary-audit construction paths. |
| `M2` — Parent-governed identity boundary | #4 | `A — C C — P` | Parent-governed S5 closure and explicit delegated policy envelope. |
| `M3` — Autonomous current control | #5 | `A — A C — P` | Autonomous S3 current regulation inside the S5 envelope. |
| `M4` — Cross-S1 coordination | #6 | `A A A C — P` | Autonomous S2 over concrete interference among existing S1 domains. |
| `M5` — External adaptation | #7 | `A A A C A P` | Autonomous S4 outside-and-then adaptation. |

The tracker issue defines the milestone's construction/exit contract. Neither the tracker nor this roadmap is a second source of VSM semantics.

## Current evidence state — 2026-10-15

```text
M0  complete
M1  S3*=C established; S3=C positive source-first constructor qualification (#39)
M2  complete: S5=P revalidated against current main and inherited M1
M3  next planned; D1-A v1 source-prepared/inactive, S5 agent grant pending; S3=A not established
M4  blocked on M3
M5  blocked on M4
```

M1 source-first positive evidence: [published S3=C assessment](reviews/2026-10-15-s3-c-standing-commitment-qualification.md) at Organization `5a08fbb18950cb2e424ae62c496cf747a7ea5c74`, built on [PR #254](https://github.com/opensiro/vsm-oss-organization/pull/254), accepted by [assessment PR #255](https://github.com/opensiro/vsm-oss-organization/pull/255). This is an **Organization-local current source-cut constructor outcome**, not a new canonical Index general grade or a claim of `C(P)`, `A` or live G1 execution. Historical 2026-09-30 `S3=?` remains immutable.

This status records construction/evidence progress only. It does not convert milestone target vectors into independent published assessments, and it does not lower any function-specific evidence threshold.

## Milestone sequence

| Milestone | Target vector | Why it exists |
| --- | --- | --- |
| M0 — Autonomous operation | `A — — — — —` | Establish repeatable local S1 operation for Index, Skills, and Awesome while keeping residual variety explicit. |
| M1 — Audit + control constructors | `A — C C — —` | Establish real S3 and S3* functions with first-party construction paths, without yet requiring autonomous owners for either metasystem function. |
| M2 — Parent-governed identity boundary | `A — C C — P` | Establish genuine S5 escalation and return so later autonomy grows inside an explicit parent-governed policy envelope. |
| M3 — Autonomous current control | `A — A C — P` | Build autonomous whole-system current-control ownership in roadmap order, ahead of contributor scaling, while requiring real current decisions and returned S1 effects for evidence. |
| M4 — Cross-S1 coordination | `A A A C — P` | Add autonomous S2 only after the already-existing S1 domains exhibit concrete interference that requires coordination. |
| M5 — External adaptation | `A A A C A P` | Add S4 only when the organization must model external/future change and feed adaptation options back into current capability. |

The current roadmap intentionally leaves S3* at `C`. A future `S3*=A` milestone should be added only if observed audit variety justifies a permanent autonomous audit owner rather than merely because S3* exists in VSM.

## M0 — Autonomous operation

Target: `A — — — — —`

**Construction status: complete.**

M0 completion means the local S1 organization has been constructed and exercised across the three operational domains.

### Operational plane

M0 declares three S1 domains:

- **Index** — `opensiro/vsm-harness-index`;
- **Skills** — `opensiro/vsm-harness-skills`;
- **Awesome** — `opensiro/awesome-vsm-harness`.

Profile and Organization are not operational S1 domains in this system-in-focus. Profile supplies normative semantics; Organization is the metasystem/control-construction surface.

Each M0 run operates inside exactly one domain and consumes the canonical local envelope in [`S1_DOMAIN_CONTRACTS.md`](S1_DOMAIN_CONTRACTS.md):

```text
bounded local work item
        ↓
S1 declares Index / Skills / Awesome
        ↓
S1 inspects current local environment
        ↓
S1 admits or rejects the work
        ↓
S1 chooses and executes local actions
        ↓
S1 validates and repairs ordinary failures
        ↓
reviewable change / no-change / escalation outcome
```

The contributor owns model choice, scheduler, runtime, credentials, budget, sandbox, and launch cadence. These are supporting mechanisms and constraints; they do not own the S1 organizational decisions merely by existing.

### Requisite-variety rule

Local variety should remain with the S1 domain that has the requisite information and delegated authority. Only residual variety that cannot be safely closed locally should motivate later metasystem functions.

The metasystem must therefore avoid duplicating ordinary Index, Skills, or Awesome decisions merely to centralize control.

### Operational evidence

Representative real paths already exist; no synthetic trial is required merely to reproduce them:

- **Index:** `opensiro/vsm-harness-index#114` — real canonical admission, dependent regeneration, completion-oracle defect discovered/repaired, regression coverage and validation;
- **Skills:** `opensiro/vsm-harness-skills#9`, `#11`, `#16` — provenance/validation defects repaired inside the current procedure contract and covered by deterministic tests;
- **Awesome:** `opensiro/awesome-vsm-harness#2`, `#3`, `#4` — real curation, subsequent narrowing/correction, and deterministic Index-consistency validation.

These establish operational paths and local correction/recovery capability. They are evidence for the S1 construction at the declared domain boundaries, while the governing Methodology remains authoritative for any formal autonomy publication.

### Exit criteria

M0 construction is complete when:

- [x] the three operational S1 domains and their local outcomes/environments are explicit;
- [x] each domain has an explicit local authority and escalation envelope;
- [x] each domain has a bounded admission/execution/validation/recovery/closure path;
- [x] each domain has a real operational evidence path;
- [x] ordinary local decisions remain inside the relevant S1 authority envelope;
- [x] work that changes normative/metasystem authority is non-admitted or escalated rather than silently treated as S1;
- [x] helper agents/tools remain supporting machinery unless independently proven as organizational units/functions;
- [x] residual variety is preserved as evidence for later functions rather than hidden by central intervention.

## M1 — Audit + control constructors

Target: `A — C C — —`

**Current evidence status:** `S3*=C` is established by #44 / PR #45; `S3=C` is **source-first positively qualified** for the bounded Organization M1 by [current source-cut assessment](reviews/2026-10-15-s3-c-standing-commitment-qualification.md), after first-party regulation implementation [PR #254](https://github.com/opensiro/vsm-oss-organization/pull/254) and [assessment PR #255](https://github.com/opensiro/vsm-oss-organization/pull/255). This satisfies the **approved local M1 Option B** without inventing an S3 transaction. It does **not** prove `C(P)`, `P`, `A`, or an independent general assessment. The frozen 2026-09-30 [general pre-assessment](../records/assessment-snapshots/2026-09-30-general-preassessment.md) independently recorded `S3=?`; it is not retroactively changed.

M1 establishes **two constructor paths**. It does not require a permanent autonomous S3 regulator or a permanent autonomous S3* verifier.

### S3*=C — complementary-audit constructor

Introduce S3* only where routine S1/S3 reporting is insufficient to trust a material operational claim or risk.

The constructor threshold is:

1. a real complementary-audit function is established at the declared boundary;
2. the ordinary S1/S3 reporting path is explicit;
3. a first-party path exposes materially complementary access to operational reality;
4. the S3*-specific surface can represent the audited claim/risk, evidence boundary, audit judgment, and local outcome (`PASS`, `FINDING`, or `INSUFFICIENT`);
5. a material finding has an explicit route toward subsequent current control;
6. the actual judgment owner is recorded separately from evidence collection, deterministic checking, transport, and downstream S3 control;
7. the constructor path is boundary-reachable and is more specific than a generic reviewer/hook/callback.

For `S3*=C`, the audit judgment owner may be human, agent, or another explicitly composed participant. The autonomous actor, authority, independence, or final closure loop may still require composition. This follows the selected Methodology definition of `C`.

Issue #44 / PR #45 is the first real functional witness: it exercised a complementary evidence path on real work and closed with `PASS` without manufacturing a finding. That evidence supports the S3* function/constructor topology; it does not establish `S3*=A`.

### S3=C — current-control constructor

S3's **current shared-commitment regulation subject and constructor** are implemented and supported by the [2026-10-15 source-first functional qualification](reviews/2026-10-15-s3-c-standing-commitment-qualification.md). The function covers existing selected-methodology and canonical Index→Awesome commitments, a G1-bounded current nonlocal decision right, and a first-party source/owner/S1-return path. The general `C` threshold permits actor/authority/closure composition; a completed live transaction is **not universally required**. An executed S3 case is **not a universal Skills Methodology prerequisite** for the `C` constructor state; a separately sourced positive functional constructor is the approved route. The separate closed parent `(P)` mode remains unproved, and a first-party interface or CI result **alone** would not have supported this positive outcome.

The path must be capable of carrying a real whole-system current-control decision back into affected operation. An actual present-tense allocation, prioritization, commitment, or shared-constraint choice can qualify when its decisive authority belongs to the whole system rather than one S1. A material S3* finding or current exception can also trigger the path, but neither an emergency nor S1 failure is a prerequisite.

Reference flow:

```text
S1 operation
        ↓
real current whole-system control need
(present allocation/commitment/constraint choice,
or a current exception / S3* finding)
        ↓
S3 control request
        ↓
whole-system current context
        ↓
current-control decision
        ↓
S3 constructor return
        ↓
subsequent S1 operation
```

An algedonic signal is not itself S3* or S3.

### M1 S3(C) acceptance — approved source-first alternative (2026-10-13)

**Effective policy:** [M1 #3 owner decision](https://github.com/opensiro/vsm-oss-organization/issues/3#issuecomment-6154518187) and the prospectively updated [#3](https://github.com/opensiro/vsm-oss-organization/issues/3) / [#39](https://github.com/opensiro/vsm-oss-organization/issues/39) permit source-first positive function/constructor qualification, **without requiring completed live S3→S1 execution**.

A source-first `S3=C` acceptance still requires: (1) a **real present whole-system S3 control function**, material current commitments/resources/priorities/constraints and appropriate shared visibility; (2) **legitimate decisive authority** over that variety, separated from CI/transport and ordinary local S1/S2 work; (3) a **specialized first-party, boundary-reachable decision/feedback constructor**, not a generic plugin or task router; (4) a structurally credible **return path to affected S1 work**, with explicit limits where actor, authority or closure requires composition; (5) pinned primary sources, a transparent review context and checks of counterexamples. Documentation names, JSON schemas, unrelated approvals, and this governance amendment alone are insufficient.

An authentic S3→S1 current-control transaction is an equally acceptable witness when it proves these facts, but is **optional integration evidence**, not mandatory for `C`. The separate `A` state still requires an autonomous agent to own decisive S3 discretion and operationally close the loop.

**Current evidence result (2026-10-15):** a separately reviewable [source-first positive `S3=C` qualification](reviews/2026-10-15-s3-c-standing-commitment-qualification.md) is now published for the bounded Organization M1 scope. The result is function/constructor evidence under this already-approved acceptance route, not an executed G1 action; historical `S3=?` remains frozen. The [owner decision packet](proposals/2026-10-13-m1-s3-c-alternate-acceptance.md) records the earlier governing route, not the later functional proof.

### Roadmap-driven reference trial, evidence-driven classification

**Two tests, different authority:** Skills owns the general `C` classification; Organization issues [#3](https://github.com/opensiro/vsm-oss-organization/issues/3) and [#39](https://github.com/opensiro/vsm-oss-organization/issues/39) now allow source-first qualification or a genuine real-work trial. These are different evidence routes, and a `C` constructor cannot be inferred from documentation/API names without a substantiated S3 function, credible whole-system authority and return path.

Milestones select **when to construct and test** S3. They do not require waiting for more contributors, the maintainer becoming unavailable, an outage, or another naturally occurring crisis before attempting M1 or developing the later M3 owner. The intended benefit is to prepare bounded current management before contributor load grows.

For an **optional real-use integration trial**, use **existing, real operational work**:

1. Identify active Index, Skills, and/or Awesome S1 commitments and a substantive current decision over shared capacity, priorities, commitments, constraints, or accountability that an individual S1 is not authorized to settle for the whole.
2. Record the relevant whole-system present-state facts, affected S1 work and exact refs **before** the decision. Keep normal S1 discretion and any S2 coordination distinct from the S3 decision right.
3. Identify the legitimate decision owner. Use the existing S3 constructor/return hook to carry the bounded choice into affected S1 operation; preserve acknowledgement/application and an observable change or justified preservation of subsequent work.
4. Review the actual function, owner/support split, boundary reachability, and closure under the selected Profile/Methodology before asserting `S3=C`. If no substantive whole-system current decision is available, report `INSUFFICIENT` and leave M1 open rather than manufacturing a trade-off.

A milestone, S3 role file, task priority label, TODO reorder, reviewer delay, or ordinary local S1 repair is **not** a functional S3 witness. Do not invent a conflict, budget pressure, blocker, audit finding, or meaningless work change merely to obtain a `C` classification. The frozen [2026-09-30 pre-assessment](../records/assessment-snapshots/2026-09-30-general-preassessment.md) remains historical; a later assessment of new evidence must pin its own source revision and provide its own verdict.

Current S3 function/constructor qualification is **positive for `C`** at the cited 2026-10-15 source cut: implemented standing current commitments plus G1-bounded nonlocal regulatory choices and the first-party S3→S1 return path are source linked and tested. This does **not** attest to an already applied S3 decision, actual current shared-resource shortage, or closed parent mode. Further preparatory validators cannot upgrade this grade to `A` or `C(P)`.

### Exit criteria

M1 closes when:

- the S3* function has a real first-party constructor witness with ordinary vs complementary evidence paths distinguishable and a reviewable audit outcome;
- the S3* constructor exposes a route for material findings into current control without requiring an autonomous verifier;
- a genuine S3 whole-system current-control function and specialized first-party constructor are positively established by source-first review or real-use evidence;
- the S3 decision/feedback return path to affected S1 is established; if a live instruction was issued, its application/effect/closure must be separately evidenced;
- actual decision/judgment owners remain explicit and support/enforcement remains separate;
- neither S3 nor S3* is claimed `A` merely because constructor infrastructure exists.

Do not manufacture a current-control disturbance solely to complete M1. Ordinary Index discovery/assessment concurrency, local Skills repair, and local Awesome curation remain S1 variety unless a real present-tense control choice requires authority on behalf of the whole Organization. A planned trial is allowed; a planned trial without a genuine decision and returned S1 effect is not evidence.

## M2 — Parent-governed identity boundary

Target: `A — C C — P`

**Current evidence and milestone status:** M2 source-first closure **SUPPORTED**, now that inherited M1 (#3, #39) is formally complete. The original `S5=P` witness [`S5-P-001`](../records/s5/2026-09-18-routing-scope-correction.md) from #81/PR #84, together with [S5 authority](../contracts/s5/parent-authority.md), was freshly checked against actual current Organization policy/routing sources and [the M1 `S3=C` functional qualification](reviews/2026-10-15-s3-c-standing-commitment-qualification.md). Full [bounded 2026-10-15 M2 source-first revalidation](reviews/2026-10-15-m2-s5-parent-source-revalidation.md). **No second S5 policy event is claimed or required.** This is the Organization's milestone-level assessment, not a new canonical general Index classification.

Introduce parent-governed S5 before increasing metasystem autonomy further. The purpose is to make the legitimate identity/policy boundary explicit.

Do not award `P` because a human approves ordinary work. A genuine identity/ultimate-policy issue must reach the legitimate parent authority, the parent must decide, and the decision must return to govern subsequent operation.

Current parent arrangement:

- legitimate parent role: **OpenSiro organization owner**;
- current holder: `xLagerFeuer`;
- authority derives from the explicit Organization governance declaration, not from GitHub permissions themselves;
- changing the parent-role/holder arrangement is itself a candidate identity/ultimate-policy matter.

`S5-P-001` reconstructs the 2026-09-18 routing-scope correction as the first positive witness. The decision kept the bounded system at Profile, Skills, Index, Awesome, and Organization rather than every public `opensiro/*` repository, and PR #62 returned that decision into routing/conformance/workflow/trial population. The record preserves that explicit parent-legitimacy attribution was added later, on 2026-09-20, rather than pretending it existed at the earlier timestamp.

Reference recursion:

```text
OpenSiro identity / major policy
        ↓ ultimate authority
OpenSiro owner / designated governance parent
        ↓ delegated envelope
contributor human parent
        ↓ local autonomy envelope
agent organization
```

Exit criteria:

- [x] M1 is formally complete — #3 and #39 closed after source-first #254–#256.
- [x] the delegated local autonomy envelope distinguishes ordinary operational choices from identity/ultimate-policy questions;
- [x] a genuine identity/policy exception can reach the legitimate parent authority;
- [x] the parent decision returns into the running organization;
- [x] subsequent operation is governed by that returned decision;
- [x] consequential external capabilities have explicit parent authorization/scope/intervention/revocation boundaries where needed;
- [x] ordinary PR approval, permission prompts, or task-level confirmations are not misclassified as S5.

Bounded current-main revalidation of inherited M1 evidence and `S5-P-001` is recorded in [M2 closure assessment](reviews/2026-10-15-m2-s5-parent-source-revalidation.md). Under governing [M2 #4](https://github.com/opensiro/vsm-oss-organization/issues/4), the completed M1 inheritance plus retained genuine S5 parent-governed decision and returned organizational effect permit M2 formal closure **without any new S5 intervention**. Later M3 must establish an autonomous S3 decision owner on its own evidence; M2 does not confer or prove it.

## M3 — Autonomous current control

Target: `A — A C — P`

M3 is selected by the roadmap after M2, **not** by reaching a contributor-count threshold or waiting until the maintainer is overloaded. Build and validate an autonomous current-control actor in advance of anticipated growth, while retaining each S1 domain's local discretion and the M2 S5 delegated envelope.

Functional `S3=A` evidence requires an **actually supported, first-party autonomous S3 owner and credible operational closure path**, regulating genuine present whole-system commitments, capacity, priorities or constraints within S5's issued authority. Under the operator's 2026-10-15 assessment-level evidence instruction, a **source-first positive functional assessment is acceptable** for M3 once the agent-owned decisive right and return/closure are demonstrably implemented; a specially created live transaction is **not a universal prerequisite**. An autonomous owner cannot be inferred from a hypothetical choice, source checker, LLM assistant preparing options for G1, standalone prompt, CI pass, or a new grant alone. A legitimate already-occurring real transaction may still be cited when it exists. See [proposed narrow M3 S5 delegation](proposals/2026-10-15-m3-autonomous-s3-boundary.md), [historical preflight](reviews/2026-10-15-m3-s3-a-source-first-preflight.md) and [current post-model source-first reassessment](reviews/2026-10-15-m3-s3-a-post-model-source-first-reassessment.md) and [latest source-first S1 GitHub/S3* check](reviews/2026-10-15-m3-s3-a-post-github-source-first-reassessment.md) and [post-D1-A public-source/transport assessment](reviews/2026-10-15-m3-s3-a-post-live-source-first-reassessment.md). **No autonomous delegation is issued by an assessment instruction.**

Exit criteria:

- S3 has a whole-system view of current operations at the declared boundary;
- an agent owns bounded decisions over relevant current priorities/resources/commitments/constraints;
- deterministic schedulers, gates, budgets, or kill switches only enforce those decisions;
- findings produced through the S3* constructor can change S3 decisions and subsequent S1 behaviour when a composed audit emits a material finding;
- S3 remains inside the S5 policy envelope established at M2.

## M4 — Cross-S1 coordination

Target: `A A A C — P`

The organization already has three operational S1 domains from M0. M4 therefore does **not** create multi-S1 operation. It introduces autonomous S2 only when concrete interference among those existing S1 domains requires an explicit coordination function.

Examples that can justify S2:

- Index and Skills concurrently changing assumptions about the selected assessment procedure;
- Awesome depending on Index state that is being concurrently regenerated or corrected;
- duplicated or conflicting cross-domain work;
- shared-resource or scheduling contention;
- oscillatory corrections where one S1 repeatedly invalidates another's local assumptions.

Before claiming positive S2, establish:

1. the distinct S1 domains involved;
2. a specific actual or structurally evidenced interference, conflict, or oscillation arising from their interaction;
3. a coordination relation specifically capable of attenuating that disturbance;
4. feedback or closure that changes subsequent S1 behaviour.

Generic mailboxes, queues, routing, shared task state, dependency fields, or task sequencing count only when evidence ties them to the identified inter-S1 disturbance.

For `S2=A`, the decisive coordination discretion must be agent-owned. Deterministic locks, schedulers, reservations, merge queues, or branch rules may support/enforce the coordination result without owning that discretion.

## M5 — External adaptation

Target: `A A A C A P`

S4 is deliberately last. Generic self-improvement, backlog ordering, internal planning, memory consolidation, or reacting to a single upstream event is not enough.

Introduce S4 only when the organization genuinely needs to model relevant external/future change, develop adaptation options, and place those options in a two-way conversation with S3 current capability.

Examples may include sustained changes in upstream harness architecture, dependency ecosystems, contributor behaviour, standards, user needs, or research directions when those distinctions should alter how the organization operates.

Exit criteria:

- the system distinguishes relevant external/future change from present operational state;
- an agent develops adaptation options rather than merely summarizing signals;
- those options enter a two-way conversation with autonomous S3 current capability;
- accepted adaptations change subsequent operation while remaining inside the parent-governed S5 identity/policy envelope.

## Supplementary development artifacts

The empirical evolution log, design-reasoning material, and external case studies are supplementary side artifacts of building and studying this organization. They are not primary operational products and do not create another S1 domain.

Their primary downstream use is a future evidence-backed article/case study testing whether VSM/OSM exposed organizational problems earlier, reduced rework/coordination cost, or otherwise improved development relative to plausible organically evolved alternatives. The evidence must also preserve negative cases where no advantage is supported.

A future separate pipeline may derive reusable skills or methodology artifacts from those histories as a secondary use; that pipeline is planned only and is not part of the current roadmap architecture.

## Rule for adding anything

Before adding an agent, state file, queue, protocol, or role, answer:

1. Which organizational variety cannot the current design absorb?
2. Which VSM function regulates that variety?
3. What is the decisive decision or feedback right?
4. Who owns it?
5. What machinery merely transports or enforces it?
6. How does the result close back into later operation?

If those questions do not identify a missing function, do not add the entity.
