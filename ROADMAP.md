# OSM Roadmap

This roadmap grows contributor autonomy bottom-up. It follows the VSM Harness Profile rule: map the organizational function first, then identify the decisive decision/feedback right, its owner, supporting enforcement, and closure.

The vectors below are milestone targets, not automatic grades. A milestone is complete only when the stated function and closure exist in the reference contribution setup.

| Milestone | Target vector | Why it exists |
| --- | --- | --- |
| M0 — Autonomous operation | `A — — — — —` | Establish one bounded autonomous S1 contribution loop. |
| M1 — Independent audit + control surface | `A — C A — —` | Add complementary audit and an explicit S3 intervention path without yet making S3 autonomous. |
| M2 — Autonomous current control | `A — A A — —` | Give an agent whole-system current view and bounded intervention authority when S1 can no longer absorb all operational exceptions locally. |
| M3 — Multi-S1 coordination | `A A A A — —` | Add S2 only after multiple independent S1 units create real interference that cannot be safely absorbed locally. |
| M4 — External adaptation | `A A A A A —` | Add S4 only when the contributor organization must model external/future change and feed adaptation options back into current capability. |
| M5 — Parent-governed identity | `A A A A A P` | Close genuine identity/ultimate-policy questions through a legitimate parent authority and return the decision into operation. |

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

## M2 — Autonomous current control

Target: `A — A A — —`

Add autonomous S3 only when observed operational variety exceeds what S1 should absorb locally. Typical triggers include repeated stalled work, budget/retry trade-offs, current commitment conflicts, or the need for exception-based intervention across the active operational scope.

Exit criteria:

- S3 has a whole-system view of current operations at the declared boundary;
- an agent owns bounded decisions over relevant current priorities/resources/commitments/constraints;
- deterministic schedulers, gates, budgets, or kill switches only enforce those decisions;
- S3* findings can change S3 decisions and subsequent S1 behaviour.

## M3 — Multi-S1 coordination

Target: `A A A A — —`

Do not add S2 merely because more processes or workers exist. Introduce multiple independent S1 units intentionally, then identify the concrete interference they create.

Examples that can justify S2:

- shared-resource contention;
- incompatible concurrent edits or interfaces;
- duplicated work;
- scheduling collisions;
- oscillatory mutual reactions;
- one S1 repeatedly invalidating another's assumptions.

A positive S2 mapping requires distinct S1 units, concrete interference/oscillation, an attenuation path, and closure that changes subsequent S1 behaviour. Mutex/reservations can be strong evidence for one class of S2 disturbance, but they are not the definition of S2.

For `S2=A`, the decisive coordination discretion must be agent-owned. A deterministic merge queue, lock, scheduler, or branch rule alone is enforcement/support.

See the related Profile discussion: https://github.com/opensiro/vsm-harness-profile/issues/7

## M4 — External adaptation

Target: `A A A A A —`

S4 is deliberately deferred. Generic self-improvement, backlog ordering, internal planning, memory consolidation, or reacting to a single upstream event is not enough.

Introduce S4 when the contributor organization genuinely needs to model relevant external/future change, develop adaptation options, and place those options in a two-way conversation with S3 current capability.

Examples may include sustained changes in upstream harness architecture, dependency ecosystems, contributor behaviour, standards, user needs, or research directions when those distinctions should alter how the organization operates.

## M5 — Parent-governed identity

Target: `A A A A A P`

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

## Rule for adding anything

Before adding an agent, state file, queue, protocol, or role, answer:

1. Which organizational variety cannot the current design absorb?
2. Which VSM function regulates that variety?
3. What is the decisive decision or feedback right?
4. Who owns it?
5. What machinery merely transports or enforces it?
6. How does the result close back into later operation?

If those questions do not identify a missing function, do not add the entity.
