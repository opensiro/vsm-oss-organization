# OSM Roadmap

This roadmap grows contributor autonomy bottom-up across the public OpenSiro OSS scope defined in [README.md](README.md). It follows the VSM Harness Profile rule: map the organizational function first, then identify the decisive decision/feedback right, its owner, supporting enforcement, and closure.

The current system-in-focus starts with three declared operational S1 domains — Index, Skills, and Awesome — while Profile remains the normative semantic source and `vsm-oss-organization` is the metasystem/control construction surface.

The vectors below are milestone targets, not automatic grades. A milestone is complete only when the stated function and closure exist in the reference organization.

The sequence is specific to this reference organization. It is not a universal VSM installation order, and `A`, `C`, and `P` are not maturity levels. They describe different ownership arrangements.

## GitHub milestone correspondence

The roadmap milestone identifier is also the canonical GitHub Milestone identifier for this repository. Each tracker issue belongs to the matching milestone; milestone titles may contain descriptive text, but the `M0`–`M5` identifier must not drift.

| GitHub milestone | Tracker issue | Target vector | Scope introduced |
| --- | --- | --- | --- |
| `M0` — Autonomous operation | #2 | `A — — — — —` | Autonomous local operation across the three declared S1 domains. |
| `M1` — Independent audit + control surface | #3 | `A — C A — —` | Complementary S3* audit plus a composable S3 intervention path. |
| `M2` — Parent-governed identity boundary | #4 | `A — C A — P` | Parent-governed S5 closure and explicit delegated policy envelope. |
| `M3` — Autonomous current control | #5 | `A — A A — P` | Autonomous S3 current regulation inside the S5 envelope. |
| `M4` — Cross-S1 coordination | #6 | `A A A A — P` | Autonomous S2 over concrete interference among existing S1 domains. |
| `M5` — External adaptation | #7 | `A A A A A P` | Autonomous S4 outside-and-then adaptation; deliberately last. |

The tracker issue defines the milestone's construction/exit contract. The GitHub Milestone groups the work required to satisfy that contract. Neither is a separate source of VSM semantics.

## Milestone sequence

| Milestone | Target vector | Why it exists |
| --- | --- | --- |
| M0 — Autonomous operation | `A — — — — —` | Establish repeatable autonomous local operation for Index, Skills, and Awesome while keeping residual variety explicit. |
| M1 — Independent audit + control surface | `A — C A — —` | Add complementary audit and an explicit S3 intervention path without yet making S3 autonomous. |
| M2 — Parent-governed identity boundary | `A — C A — P` | Establish genuine S5 escalation and return so later autonomy grows inside an explicit parent-governed policy envelope. |
| M3 — Autonomous current control | `A — A A — P` | Give an agent whole-system current view and bounded intervention authority when S1 domains can no longer absorb all current exceptions locally. |
| M4 — Cross-S1 coordination | `A A A A — P` | Add autonomous S2 only after the already-existing S1 domains exhibit concrete interference that requires coordination. |
| M5 — External adaptation | `A A A A A P` | Add S4 only when the organization must model external/future change and feed adaptation options back into current capability. |

## M0 — Autonomous operation

Target: `A — — — — —`

### Operational plane

M0 declares three S1 domains from the start:

- **Index** — `opensiro/vsm-harness-index`;
- **Skills** — `opensiro/vsm-harness-skills`;
- **Awesome** — `opensiro/awesome-vsm-harness`.

Profile and Organization are not operational S1 domains in this system-in-focus. Profile supplies normative semantics; Organization is the metasystem/control construction surface.

A bounded reference run operates inside exactly one declared S1 domain:

```text
bounded local work item
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

The contributor owns model choice, scheduler, runtime, credentials, budget, sandbox, and launch cadence. These are supporting mechanisms and constraints; they do not own the S1 organizational decisions.

### Requisite-variety rule

Local variety should remain with the S1 domain that has the requisite information and delegated authority. Only residual variety that cannot be safely closed locally should motivate later metasystem functions.

The metasystem must therefore avoid duplicating ordinary Index, Skills, or Awesome decisions merely to centralize control.

### Exit criteria

- the three operational S1 domains and their local outcomes/environments are explicit;
- each domain has a bounded admission/execution/validation/recovery/closure path;
- ordinary local decisions remain inside the relevant S1 authority envelope;
- routine failure recovery does not require human step-by-step control;
- work that actually changes normative/metasystem authority is non-admitted or escalated rather than silently treated as S1;
- internal helper agents are not counted as additional S1 units merely because they are separate processes;
- residual variety is preserved as evidence for later functions rather than hidden by central intervention.

Formal `S1=A` remains an evidence claim under the selected Methodology. The deferred distinct-executor identity work is tracked separately for Parent-assisted M2.

## M1 — Independent audit + control surface

Target: `A — C A — —`

Introduce S3* when routine S1 reporting is insufficient to trust a material operational claim. The S3* path must use materially complementary access to operational reality, for example raw diffs, tests, pinned primary evidence, replay, or other evidence not controlled solely by the producing S1.

S3 remains `C`: the repository exposes a first-party current-control/intervention path, but no default autonomous S3 regulator owns it yet. The path must be specific enough to carry a real whole-system current-control decision back into affected operation.

An algedonic signal is not itself S3* or S3.

Exit criteria:

- an independent agent owns the audit judgment and can emit a material finding;
- the finding can enter a defined current-control/intervention path;
- the intervention result can return to subsequent S1 operation;
- S3 is not claimed `A` until an autonomous agent owns the decisive current-control discretion.

## M2 — Parent-governed identity boundary

Target: `A — C A — P`

Introduce parent-governed S5 before increasing metasystem autonomy further. The purpose is to make the legitimate identity/policy boundary explicit.

Do not award `P` because a human approves ordinary work. A genuine identity/ultimate-policy issue must reach the legitimate parent authority, the parent must decide, and the decision must return to govern subsequent operation.

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

- the delegated local autonomy envelope distinguishes ordinary operational choices from identity/ultimate-policy questions;
- a genuine identity/policy exception can reach the legitimate parent authority;
- the parent decision returns into the running organization;
- subsequent operation is governed by that returned decision;
- ordinary PR approval, permission prompts, or task-level confirmations are not misclassified as S5.

## M3 — Autonomous current control

Target: `A — A A — P`

Add autonomous S3 only when observed current operational variety across the organization exceeds what the S1 domains should absorb locally.

Typical triggers include repeated stalled work, budget/retry trade-offs, current commitment conflicts, or exception-based intervention across the active operational scope.

Exit criteria:

- S3 has a whole-system view of current operations at the declared boundary;
- an agent owns bounded decisions over relevant current priorities/resources/commitments/constraints;
- deterministic schedulers, gates, budgets, or kill switches only enforce those decisions;
- S3* findings can change S3 decisions and subsequent S1 behaviour;
- S3 remains inside the S5 policy envelope established at M2.

## M4 — Cross-S1 coordination

Target: `A A A A — P`

The organization already has three operational S1 domains from M0. M4 therefore does **not** create multi-S1 operation. It introduces autonomous S2 only when concrete interference among those existing S1 domains requires an explicit coordination function.

Examples that can justify S2:

- Index and Skills concurrently changing assumptions about the selected assessment procedure;
- Awesome depending on Index state that is being concurrently regenerated or corrected;
- duplicated or conflicting cross-domain work;
- shared-resource or scheduling contention;
- oscillatory corrections where one S1 repeatedly invalidates another's local assumptions.

Before claiming positive S2, establish:

1. the distinct S1 domains involved;
2. a **specific actual or structurally evidenced** interference, conflict, or oscillation arising from their interaction;
3. a coordination relation specifically capable of attenuating that disturbance;
4. feedback or closure that changes subsequent S1 behaviour.

Generic mailboxes, queues, routing, shared task state, dependency fields, or task sequencing count only when evidence ties them to the identified inter-S1 disturbance.

For `S2=A`, the decisive coordination discretion must be agent-owned. Deterministic locks, schedulers, reservations, merge queues, or branch rules may support/enforce the coordination result without owning that discretion.

## M5 — External adaptation

Target: `A A A A A P`

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

A future separate pipeline may derive reusable skills or methodology artifacts from those histories, but that pipeline is planned only and is not part of the current roadmap architecture.

## Rule for adding anything

Before adding an agent, state file, queue, protocol, or role, answer:

1. Which organizational variety cannot the current design absorb?
2. Which VSM function regulates that variety?
3. What is the decisive decision or feedback right?
4. Who owns it?
5. What machinery merely transports or enforces it?
6. How does the result close back into later operation?

If those questions do not identify a missing function, do not add the entity.