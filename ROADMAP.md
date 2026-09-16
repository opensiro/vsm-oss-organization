# OSM Roadmap

This roadmap grows contributor autonomy bottom-up across the public OpenSiro OSS scope defined in [README.md](README.md). It follows the VSM Harness Profile rule: map the organizational function first, then identify the decisive decision/feedback right, its owner, supporting enforcement, and closure.

The vectors below are milestone targets, not automatic grades. A milestone is complete only when the stated function and closure exist in the reference contribution setup.

The sequence is specific to this reference organization. It is not a universal VSM installation order, and `A`, `C`, and `P` are not maturity levels. They describe different ownership arrangements. In particular, the local `S3=C → S3=A` transition means this design intends to close a specific constructor/control path with an autonomous owner; it does not define a general ordering `C < A`. Likewise, `S5=P` is the intended parent-governed identity topology, not an incomplete step toward `S5=A`.

## GitHub milestone correspondence

The roadmap milestone identifier is also the canonical GitHub Milestone identifier for this repository. Each tracker issue belongs to the matching milestone; milestone titles may contain descriptive text, but the `M0`–`M5` identifier must not drift.

| GitHub milestone | Tracker issue | Target vector | Scope introduced |
| --- | --- | --- | --- |
| `M0` — Autonomous operation | #2 | `A — — — — —` | One bounded autonomous OSS contribution S1. |
| `M1` — Independent audit + control surface | #3 | `A — C A — —` | Complementary S3* audit plus a composable S3 intervention path. |
| `M2` — Parent-governed identity boundary | #4 | `A — C A — P` | Parent-governed S5 closure and explicit delegated policy envelope. |
| `M3` — Autonomous current control | #5 | `A — A A — P` | Autonomous S3 current regulation inside the S5 envelope. |
| `M4` — Multi-S1 coordination | #6 | `A A A A — P` | Autonomous S2 only after real inter-S1 interference appears. |
| `M5` — External adaptation | #7 | `A A A A A P` | Autonomous S4 outside-and-then adaptation; deliberately last. |

The tracker issue defines the milestone's construction/exit contract. The GitHub Milestone groups the work required to satisfy that contract. Neither is a separate source of VSM semantics.

## Milestone sequence

| Milestone | Target vector | Why it exists |
| --- | --- | --- |
| M0 — Autonomous operation | `A — — — — —` | Establish one bounded autonomous S1 contribution loop. |
| M1 — Independent audit + control surface | `A — C A — —` | Add complementary audit and an explicit S3 intervention path without yet making S3 autonomous. |
| M2 — Parent-governed identity boundary | `A — C A — P` | Establish genuine S5 escalation and return early, so later autonomy grows inside an explicit parent-governed policy envelope. |
| M3 — Autonomous current control | `A — A A — P` | Give an agent whole-system current view and bounded intervention authority when S1 can no longer absorb all operational exceptions locally. |
| M4 — Multi-S1 coordination | `A A A A — P` | Add S2 only after multiple independent S1 units create real interference that cannot be safely absorbed locally. |
| M5 — External adaptation | `A A A A A P` | Add S4 last, only when the contributor organization must model external/future change and feed adaptation options back into current capability. |

## M0 — Autonomous operation

Target: `A — — — — —`

System-in-focus: one contributor-owned autonomous contribution cell.

Reference closure:

```text
bounded work item
        ↓
agent interprets repository and issue state
        ↓
agent chooses and executes local actions
        ↓
agent checks evidence/tests and repairs failures
        ↓
reviewable Issue artifact or Pull Request
```

The contributor owns model choice, scheduler, runtime, credentials, budget, sandbox, and launch cadence. These are supporting mechanisms and constraints; they do not own the S1 organizational decisions.

Exit criteria:

- one work item has one explicit outcome and repository boundary;
- the agent owns local implementation/research decisions inside that boundary;
- routine failure recovery does not require human step-by-step control;
- the loop produces a reviewable GitHub artifact;
- internal helper agents are not counted as separate S1 units unless they have their own durable outcome/environment/autonomy.

## M1 — Independent audit + control surface

Target: `A — C A — —`

Introduce S3* because routine S1 reporting may be insufficient to trust completion. The S3* path must use materially complementary access to operational reality, for example raw diffs, tests, pinned primary evidence, replay, or other evidence not controlled solely by the producing S1.

S3 remains `C`: the repository exposes a first-party current-control/intervention path, but no default autonomous S3 regulator owns it yet. The path must be specific enough to carry a real S3 decision such as stop/continue, retry budget, current priority, constraint, or required repair back into operation.

An algedonic signal is not itself S3* or S3. S3* may discover exceptional pain/opportunity and originate such a signal, but the algedonic channel is the exceptional communication path to an authority able to act.

Exit criteria:

- an independent agent owns the audit judgment and can emit a material finding;
- the finding can enter a defined current-control/intervention path;
- the intervention result can return to subsequent S1 operation;
- S3 is not claimed `A` until an autonomous agent owns the decisive current-control discretion.

## M2 — Parent-governed identity boundary

Target: `A — C A — P`

Introduce parent-governed S5 before increasing operational autonomy further. The purpose is to make the legitimate identity/policy boundary explicit while S3 is still only composable and before multi-S1 coordination or external adaptation are added.

Do not award `P` because a human approves ordinary work. The runtime must detect or formulate a genuine identity/ultimate-policy issue, transfer it to the legitimate parent authority, receive an authoritative decision, and continue under that returned decision.

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

Minor operational choices should remain below S5. Questions outside the contributor's delegated identity/policy envelope escalate to the higher OpenSiro parent.

Exit criteria:

- the delegated local autonomy envelope is explicit enough to distinguish ordinary operational choices from identity/ultimate-policy questions;
- a genuine identity/policy exception can reach the legitimate parent authority;
- the parent decision returns into the running organization;
- subsequent operation is governed by that returned decision;
- ordinary PR approval, permission prompts, or task-level confirmations are not misclassified as S5.

## M3 — Autonomous current control

Target: `A — A A — P`

Add autonomous S3 only when observed operational variety exceeds what S1 should absorb locally. Typical triggers include repeated stalled work, budget/retry trade-offs, current commitment conflicts, or the need for exception-based intervention across the active operational scope.

Exit criteria:

- S3 has a whole-system view of current operations at the declared boundary;
- an agent owns bounded decisions over relevant current priorities/resources/commitments/constraints;
- deterministic schedulers, gates, budgets, or kill switches only enforce those decisions;
- S3* findings can change S3 decisions and subsequent S1 behaviour;
- S3 remains inside the S5 policy envelope established at M2.

## M4 — Multi-S1 coordination

Target: `A A A A — P`

Do not add S2 merely because more processes or workers exist. Introduce multiple independent S1 units intentionally, then identify the concrete interference they create.

Examples that can justify S2:

- shared-resource contention;
- incompatible concurrent edits or interfaces;
- duplicated work;
- scheduling collisions;
- oscillatory mutual reactions;
- one S1 repeatedly invalidating another's assumptions.

Profile `0.2.1` now makes the S2 witness mechanically explicit. Before claiming positive S2, establish:

1. distinct S1 units at the declared recursion level;
2. a **specific actual or structurally evidenced** interference, conflict, or oscillation arising from their interaction;
3. a coordination relation specifically capable of attenuating that disturbance;
4. feedback or closure that changes subsequent S1 behaviour.

Merely saying that several agents could potentially disagree is insufficient. Generic mailboxes, queues, routing, shared task state, dependency fields, speaker selection, or task sequencing count only when evidence ties them to the identified inter-S1 disturbance.

For `S2=A`, the decisive coordination discretion must be agent-owned. A deterministic merge queue, lock, scheduler, reservation, or branch rule may support/enforce the coordination result without owning that discretion.

## M5 — External adaptation

Target: `A A A A A P`

S4 is deliberately last. Generic self-improvement, backlog ordering, internal planning, memory consolidation, or reacting to a single upstream event is not enough.

Introduce S4 only when the contributor organization genuinely needs to model relevant external/future change, develop adaptation options, and place those options in a two-way conversation with S3 current capability.

Examples may include sustained changes in upstream harness architecture, dependency ecosystems, contributor behaviour, standards, user needs, or research directions when those distinctions should alter how the organization operates.

Exit criteria:

- the system distinguishes relevant external/future change from present operational state;
- an agent develops adaptation options rather than merely summarizing signals;
- those options enter a two-way conversation with autonomous S3 current capability;
- accepted adaptations change subsequent operation while remaining inside the parent-governed S5 identity/policy envelope.

## Rule for adding anything

Before adding an agent, state file, queue, protocol, or role, answer:

1. Which organizational variety cannot the current design absorb?
2. Which VSM function regulates that variety?
3. What is the decisive decision or feedback right?
4. Who owns it?
5. What machinery merely transports or enforces it?
6. How does the result close back into later operation?

If those questions do not identify a missing function, do not add the entity.