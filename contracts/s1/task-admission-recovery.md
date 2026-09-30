# S1 task admission and routine recovery

This runtime-neutral organizational contract decides whether a presented work item may enter one bounded S1 contribution loop and how that loop handles ordinary disturbances after admission.

It does **not** redefine VSM semantics, autonomy states, or assessment procedure. Those remain owned by the selected upstream Profile/Methodology or by an explicitly frozen historical contract declared by the work item.

The governing rule is:

```text
presented work item
        ↓
ADMIT as bounded S1 work
or
NON-ADMIT / ESCALATE with evidence
```

Human intervention is allowed but must remain visible and attributed to the human for the affected decision.

## Admission

Before ordinary execution begins, record one verdict:

- `ADMIT` — the work is sufficiently bounded and the ordinary local decision rights needed to close it are delegated to S1;
- `NON-ADMIT` — available authority/evidence is insufficient for safe S1 execution.

Admission analysis may inspect current state and primary evidence before mutation.

A work item should establish at least:

1. system-in-focus;
2. exact work boundary;
3. bounded reviewable outcome;
4. governing contract;
5. primary evidence;
6. delegated local authority envelope;
7. forbidden decisions;
8. validation expectation;
9. escalation conditions;
10. evidence sufficiency.

If a material item cannot be established without guessing, default to `NON-ADMIT`.

## Work-class boundary

Admission follows the decision rights required by the work, not repository name or task label.

- ordinary bounded contribution work may be admitted when the contract is satisfied;
- normative Profile/Methodology authority changes are not ordinary S1 work, although implementation of an already-authorized decision may be;
- identity/scope/ultimate-policy decisions are not ordinary S1 work unless separately delegated;
- insufficient-evidence work must remain non-admitted or stop/escalate when the gap becomes visible.

Not all OSS work is therefore S1 work for this organization.

## Merge and integration

Producing a reviewable PR may close S1 contribution work without granting merge authority. Integration/default-branch mutation is a separate decision right unless explicitly delegated. A human review/merge boundary does not by itself establish another VSM function.

## Routine recovery

After admission, S1 should absorb ordinary local disturbances while the outcome, boundary, governing contract, authority envelope, evidence sufficiency, and validation expectation remain intact.

Typical local recovery includes stale bases, validation failures, broken references, generated drift, task-local tool failure, resolvable evidence gaps, and justified no-change outcomes.

Do not manufacture failure merely to demonstrate recovery. If repair requires a new decision outside the admitted authority/evidence boundary, escalate.

## Human intervention

When a human intervenes:

1. record the intervention;
2. attribute it to the human;
3. identify the affected decision/right;
4. record whether the human selected, constrained, overrode, stopped, or supplied information for that decision;
5. do not count that specific decision as agent-owned evidence;
6. record whether S1 resumed autonomous operation;
7. re-establish admission if the boundary, governing contract, or delegated authority changed.

Repeated or standard-path human selection of ordinary decisive S1 decisions is evidence that those rights may remain human-owned.

## Escalation

Escalation identifies missing authority or evidence; it does not imply a particular future VSM role. Useful local categories may include boundary ambiguity, normative authority, identity/policy authority, integration authority, insufficient evidence/validation, out-of-bound concurrent change, or another forbidden decision.

## Evidence preserved

For admission, non-admission, escalation, recovery, or intervention preserve enough observable evidence for another reviewer to reconstruct the work boundary, governing contract, evidence inspected, authority envelope, decision ownership, disturbances/recovery, validation, and closure.

Do not preserve hidden chain-of-thought.

## Terminal states

An S1 run ends in one of:

- `CLOSED_CHANGE`;
- `CLOSED_NO_CHANGE`;
- `ESCALATED`;
- `NON_ADMITTED`.

Human intervention is an event attribute rather than a separate terminal state.

## Assessment evidence boundary

Using this contract does not establish `S1=A` by itself. A positive autonomy claim still requires the governing Methodology's function, decisive right, owner, support/enforcement, boundary reachability, and closure evidence. If the decisive closure used as evidence was actually selected by a human, that run is not sufficient by itself to establish autonomous ownership.
