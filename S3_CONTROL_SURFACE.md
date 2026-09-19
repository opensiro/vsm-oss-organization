# S3 current-control constructor surface

This document defines a repository-local first-party primitive for carrying a bounded S3 current-control decision into subsequent S1 operation during M1 work.

It applies the selected VSM Harness Profile and Methodology through `UPSTREAM_CONTRACT.json`; it does **not** redefine S3, constructor state `C`, or autonomy semantics.

The active formal roadmap milestone is M1. The presence of this surface therefore does **not** establish `S3=C`, `S3=A`, or complete M1 by itself. A positive mapping still requires the S3 function to be established from actual use at the declared system boundary.

## Purpose

The constructor surface exists so a material current-control need can be represented as a first-party request/decision/return transaction rather than as an unstructured comment or ad-hoc human instruction.

Reference flow:

```text
material current exception / S3* finding
        ↓
S3 control request
        ↓
whole-system current context
        ↓
decisive current-control choice
        ↓ owner recorded explicitly
returned control decision
        ↓
S1 acknowledgement / application
        ↓
observable effect on subsequent operation
```

The surface transports and records the decision. It does not own the decision.

## Functional admission

Do not use this surface merely because a task needs approval or correction.

A transaction qualifies for this surface only when the requested decision regulates **current operation on behalf of the whole declared system**, with a relevant whole-system view of present commitments, constraints, resources, priorities, accountability, synergy, or intervention needs.

Before creating a transaction, establish:

1. **System-in-focus** — the current organizational boundary being regulated.
2. **Trigger** — the material finding/exception that cannot be closed as ordinary local S1 variety.
3. **Whole-system current view** — what current operations/commitments/constraints are relevant to the decision.
4. **Decisive current-control right** — what choice must be made.
5. **Allowed response class** — which bounded responses can close this transaction.
6. **Decision owner** — who actually exercises the choice in this run/mode.
7. **Support/enforcement** — what machinery transports or enforces the returned decision.
8. **Return target** — which S1 work item(s) must acknowledge/apply the decision.
9. **Closure evidence** — what proves the returned decision changed or intentionally preserved subsequent operation.

If the matter is only a local implementation choice that S1 can absorb inside its admitted authority, keep it in S1.

If the matter is identity/ultimate-policy level, do not force it through this surface; preserve escalation to the legitimate parent/policy boundary.

## Local decision classes

The following local classes are available when they represent a genuine S3 current-control decision at the declared boundary:

- `CONTINUE` — continue current operation under the returned constraints;
- `STOP` — suspend/stop the affected current operation;
- `REQUIRE_REPAIR` — require a bounded repair before the affected operation may close or proceed;
- `SET_CONSTRAINT` — add/revise a current operating constraint on behalf of the whole;
- `SET_RETRY_BUDGET` — add/revise a current retry/time/attempt envelope where that envelope is a whole-system current-control matter;
- `OTHER_CURRENT_CONTROL` — another explicitly described S3 current-control decision that satisfies the functional admission test.

These are repository-local operational labels, not VSM semantics.

A class name alone does not establish S3. For example, `STOP` on a single local action may still be ordinary S1 recovery or a generic permission boundary.

## Constructor ownership model

This surface targets a constructor path, not an autonomous S3 owner.

A conforming transaction MUST separate:

- the **S3 function** being closed;
- the **decisive current-control right**;
- the **decision owner** in this concrete transaction;
- the **first-party constructor surface** that exposes the request/return path;
- **support/enforcement machinery**;
- the **return/closure path** into S1.

The decision owner may be a human, parent, external actor, or later autonomous S3 agent depending on the run/mode. This file does not assign that ownership.

A JSON record, GitHub issue/comment, branch rule, CI gate, scheduler, queue, or validator may enforce/transport the result without owning the organizational decision.

The corresponding role/ownership contract is [`roles/S3.md`](roles/S3.md). During M1 it preserves explicit transaction-level ownership rather than declaring a permanent autonomous S3 owner; autonomous agent ownership remains gated by the M3 conditions in `ROADMAP.md`.

## Machine-readable transaction

Use `control/s3-current-control-v1.template.json` as the canonical starting shape.

A transaction should include:

- version and transaction id;
- system-in-focus;
- trigger and primary evidence refs;
- whole-system current-view refs/summary;
- requested decisive right and allowed decision classes;
- actual decision owner and actor evidence;
- returned decision and bounded instruction;
- support/enforcement refs;
- S1 return targets;
- S1 acknowledgement/application refs;
- final transaction state.

The JSON representation is a transport/evidence surface, not an autonomous regulator.

## Transaction states

Use these local lifecycle states:

- `REQUESTED` — a qualifying current-control decision is needed;
- `DECIDED` — the decisive owner has returned a bounded decision;
- `APPLIED` — target S1 operation has acknowledged/applied the decision;
- `CLOSED` — the effect/closure is reviewable;
- `ESCALATED` — the matter cannot be closed inside the current S3 decision envelope;
- `CANCELLED` — the trigger became invalid or the transaction was superseded before decision.

These are operational states, not VSM autonomy states.

## S1 return hook

A returned decision changes S1 operation only when all of the following are true:

1. the transaction identifies the affected S1 work item/boundary;
2. the decision is in an allowed class for that transaction;
3. the actual decision owner is recorded;
4. the decision remains inside the declared S3 current-control envelope;
5. the returned instruction is concrete enough for S1 to apply or explicitly reject/escalate;
6. S1 records acknowledgement/application and preserves closure evidence.

Arbitrary comments, chat messages, labels, approval buttons, or human instructions do not become S3 input merely because S1 sees them.

The S1 role contains the M1 return-hook rules in `roles/S1.md`. In the absence of a declared qualifying transaction, ordinary S1 admission/recovery rules remain unchanged.

## S3* relationship

A material S3* `FINDING` may be a trigger for this surface, but S3* and S3 remain distinct:

```text
S3* owns audit judgment
        ↓
finding
S3 decision owner chooses current-control response
        ↓
constructor surface transports/enforces return
```

The auditor does not inherit S3 authority merely because its finding initiated the transaction.

## Human and parent decisions

A human may own the decisive current-control choice in a concrete constructor transaction. Record that ownership honestly.

Do not automatically publish such involvement as S3 parent mode `(P)`. The governing Methodology requires a separately established first-party parent-governed S3 topology and returned closure at the declared recursion. This surface does not make that classification by itself.

## Identity/policy boundary

Do not normalize identity/ultimate-policy questions into current control.

Examples that should normally leave this surface include changes to:

- the organization's identity/purpose;
- ultimate semantic authority;
- repository governance ownership;
- the parent delegation model itself;
- other policy decisions whose legitimacy belongs at S5/parent recursion rather than present operational control.

Record an escalation instead of selecting `OTHER_CURRENT_CONTROL` to bypass the boundary.

## Non-examples

The following do not independently establish S3 or this constructor path:

- ordinary PR approval;
- a generic issue comment asking for changes;
- a static branch rule;
- a task assignment/delegation;
- a retry inside local S1 recovery;
- a queue/mailbox/API with no S3-specific decision semantics;
- a component named manager/controller/orchestrator;
- CI blocking a change under a preselected rule.

## Reference artifacts

- role/ownership contract: `roles/S3.md`;
- machine-readable transaction: `control/s3-current-control-v1.template.json`;
- reviewable record: `templates/s3-control-record.md`;
- S1 return hook: `roles/S1.md`;
- parent work: #38 / #42;
- complementary audit input: `S3STAR_AUDIT.md` / #37;
- end-to-end trial: #39.
