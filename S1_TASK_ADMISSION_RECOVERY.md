# S1 task admission and routine recovery

This document defines the runtime-neutral operational contract used to decide whether a presented work item may enter one bounded S1 contribution loop and how that loop handles routine disturbances after admission.

It is a local organizational contract for this repository. It does **not** redefine VSM semantics, autonomy states, or assessment procedure. Those remain owned by the upstream VSM Harness Profile and VSM Harness Methodology selected through `UPSTREAM_CONTRACT.json`, or by an explicitly frozen historical contract when the work item declares one.

The governing admission rule is:

```text
presented work item
        ↓
ADMIT as bounded S1 work
or
NON-ADMIT / ESCALATE with evidence
```

Human intervention after admission is allowed. It must be visible, attributed, and treated as human-owned for the affected decision rather than silently counted as agent-owned discretion.

## 1. Admission verdict

Before implementation, research, mutation, or other task execution begins, record one explicit verdict:

- `ADMIT` — the item is sufficiently bounded and the ordinary local decision rights needed to close it are delegated to the S1;
- `NON-ADMIT` — the item cannot safely enter the S1 loop under the available authority/evidence; preserve the reason and escalation evidence instead of beginning ordinary execution.

Reading current repository state and primary evidence in order to make this verdict is admission analysis, not execution of the requested change.

### Admission checklist

An item may be admitted only when all applicable questions have a sufficiently concrete answer.

1. **System-in-focus** — which repository/system boundary is being operated on?
2. **Work boundary** — what exact problem or contribution is inside this run, and what adjacent work is outside it?
3. **Bounded outcome** — what reviewable terminal result closes the run?
4. **Governing contract** — which Organization-selected upstream contract, or which explicitly frozen historical contract, applies?
5. **Primary evidence** — what evidence must be inspected before decisions are made?
6. **Authority envelope** — which ordinary implementation, research, evidence-selection, repair, and validation decisions may the S1 make locally?
7. **Forbidden decisions** — which semantic, policy, scope, licensing, integration, risk, or other decisions are not delegated?
8. **Validation expectation** — what evidence/checks distinguish closure from a plausible-looking result?
9. **Escalation conditions** — what observable events exceed local authority/evidence?
10. **Evidence sufficiency** — is the admission classification supportable without guessing?

If a required item cannot be established, the default is `NON-ADMIT`.

## 2. Work-class boundary

Admission follows the actual decision rights required by the work, not the repository name or task label.

| Work class | Ordinary S1 admission |
| --- | --- |
| **Ordinary bounded contribution** | May be `ADMIT` when the checklist is satisfied and the needed local discretion is delegated. |
| **Normative Profile or Methodology decision** | `NON-ADMIT` as ordinary S1 work. Implementation of an already-authorized selected/frozen decision may be separately admitted when no undelegated semantic/procedure discretion remains. |
| **Organization identity, scope, or ultimate-policy decision** | `NON-ADMIT` as ordinary S1 work unless that authority has been explicitly delegated by the legitimate owner/process. |
| **Insufficient-evidence work** | `NON-ADMIT`, or stop an already-admitted run when the gap is discovered. Do not invent missing evidence. |

Not all OSS work is therefore S1 work for this organization.

### Merge and integration

Producing a reviewable PR may close an S1 contribution without granting the S1 authority to merge it.

Merge/integration is a separate decision right unless explicitly delegated. A human review or merge boundary does not by itself establish a new VSM function.

## 3. Routine recovery

After `ADMIT`, the S1 should absorb ordinary local disturbances itself when the outcome, boundary, governing contract, authority envelope, evidence sufficiency, and validation expectation remain intact.

Typical local recovery includes stale bases, validation failures, broken references, generated-file drift, evidence gaps, and legitimate no-change results.

Do not manufacture failures merely to demonstrate recovery.

If recovery requires a decision outside the admitted authority/evidence boundary, record an escalation.

## 4. Human intervention

Human intervention is a normal possible event in a viable system, not an automatic failure state.

When a human intervenes after admission:

1. record that an intervention occurred;
2. attribute the intervention to the human;
3. identify the decision/right it affected;
4. record whether the human selected, constrained, overrode, stopped, or supplied information for the decision;
5. do not count that specific human-selected decision as agent-owned evidence;
6. record whether the S1 resumed autonomous operation afterward;
7. if the intervention changes the work boundary, governing contract, or delegated authority, re-establish admission or escalate before continuing.

An isolated intervention does not automatically invalidate the whole S1 arrangement. The evidence question is whether the relevant decisive organizational discretion is ordinarily agent-owned and operationally closed.

Repeated or standard-path human selection of ordinary decisive S1 decisions is evidence that those rights may actually remain human-owned.

The organization should therefore optimize for **visible intervention and decreasing avoidable intervention/loss**, not for pretending that intervention never occurs.

Useful observations include intervention frequency, cause, affected decision right, recovery outcome, and whether the same intervention class recurs.

## 5. Escalation

Escalation identifies a missing decision or evidence; it does not imply a particular future VSM role.

Useful categories include:

- `BOUNDARY_AMBIGUOUS`;
- `AUTHORITY_NORMATIVE`;
- `AUTHORITY_IDENTITY_POLICY`;
- `AUTHORITY_INTEGRATION`;
- `EVIDENCE_INSUFFICIENT`;
- `VALIDATION_INSUFFICIENT`;
- `CONCURRENT_CHANGE_OUT_OF_BOUNDARY`;
- `OTHER_FORBIDDEN_DECISION`.

A human response to escalation is attributed to the human/parent for that external decision. Subsequent in-boundary discretion may return to S1.

## 6. Evidence preserved

For non-admission, escalation, recovery, or intervention, preserve enough evidence for another reviewer to reconstruct what happened:

```text
work item / requested outcome
system-in-focus and repository revision(s)
governing contract
primary evidence inspected
authority envelope
admission verdict
natural disturbances and recovery actions
human interventions, if any
which decision/right each intervention affected
escalations, if any
validation / closure evidence
```

Record observable decisions and evidence, not hidden chain-of-thought.

## 7. Closure states

An admitted S1 run ends in one of these operational states:

- `CLOSED_CHANGE` — bounded change produced and validation/evidence completed;
- `CLOSED_NO_CHANGE` — evidence establishes no justified mutation is required;
- `ESCALATED` — the run crossed its current authority/evidence boundary;
- `NON_ADMITTED` — the item never passed the admission gate.

Human intervention is an **attribute of the run/event record**, not a separate failure terminal state. A run may be `CLOSED_CHANGE` with one or more reported interventions.

These are operational record states, not VSM autonomy states.

## 8. M0 evidence boundary

Using this contract does not by itself establish `S1=A`.

For a positive autonomy claim, the governing Methodology still requires function, decisive decision right, owner, supporting/enforcement machinery, and closure to be reconstructable from primary evidence.

A human intervention does not automatically negate `A`; however, any human-owned decision must remain attributed to the human. If the decisive closure used as evidence for `S1=A` was actually supplied by the human, that run is not sufficient by itself to establish agent ownership of that decisive loop.
