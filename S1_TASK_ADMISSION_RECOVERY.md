# S1 task admission and routine recovery

This document defines the runtime-neutral operational contract used to decide whether a presented work item may enter one bounded S1 contribution loop and how that loop handles routine disturbances after admission.

It is a local organizational contract for this repository. It does **not** redefine VSM semantics, autonomy states, or assessment procedure. Those remain owned by the released VSM Harness Profile and VSM Harness Methodology identified in `CONTROL_PLANE.md` (currently Profile `0.2.1` / Methodology `0.2.3`). Frozen work keeps its declared contract.

The governing rule is:

```text
presented work item
        ↓
ADMIT as bounded S1 work
or
NON-ADMIT / ESCALATE with evidence
```

There is no third path in which a human silently supplies ordinary operational decisions while the run continues to be described as autonomous S1 work.

This contract does not solve executor provenance or repository-specific validation coverage. It defines the admission/recovery interface those mechanisms may later support.

## 1. Admission verdict

Before implementation, research, mutation, or other task execution begins, record one explicit verdict:

- `ADMIT` — the item is sufficiently bounded and the ordinary local decision rights needed to close it are delegated to the S1;
- `NON-ADMIT` — the item cannot safely enter the S1 loop under the available authority/evidence; preserve the reason and escalation evidence instead of beginning ordinary execution.

Reading current repository state and primary evidence in order to make this verdict is admission analysis, not execution of the requested change.

### Admission checklist

An item may be admitted only when all applicable questions have a sufficiently concrete answer.

1. **System-in-focus** — which repository/system boundary is being operated on?
2. **Work boundary** — what exact problem or contribution is inside this run, and what adjacent work is outside it?
3. **Bounded outcome** — what reviewable terminal result closes the run: PR, Issue artifact, evidence report, or legitimate no-change result?
4. **Governing contract** — which released or explicitly frozen Profile/Methodology/repository contract applies?
5. **Primary evidence** — what current repository state, issue/PR state, upstream source, or other primary evidence is required before decisions are made?
6. **Authority envelope** — which ordinary implementation, research, evidence-selection, repair, and validation decisions may the S1 make locally?
7. **Forbidden decisions** — which semantic, policy, scope, licensing, integration, risk, or other decisions are not delegated?
8. **Validation expectation** — what evidence or checks can distinguish a closed result from a plausible-looking result?
9. **Escalation conditions** — what observable events require the S1 to stop deciding locally?
10. **Evidence sufficiency** — is the evidence strong enough to make the admission classification without guessing?

If a required item cannot be established, the default is `NON-ADMIT`, not an inferred authority grant.

## 2. Work-class boundary

Admission follows the actual decision rights required by the work, not the repository name or task label.

| Work class | Ordinary S1 admission |
| --- | --- |
| **Ordinary bounded contribution** — implementation, documentation, evidence-backed maintenance, correction, deterministic regeneration, or other repository work under an already-established contract | May be `ADMIT` when the checklist is satisfied and the needed local discretion is delegated. |
| **Normative Profile or Methodology decision** — deciding new VSM meaning/boundary or changing assessment/autonomy/synthesis procedure | `NON-ADMIT` as ordinary S1 work. Escalate to the source-of-truth change process. Implementation of an already-authorized, frozen normative decision may be separately admitted only when no undelegated semantic/procedure choice remains. |
| **Organization identity, scope, or ultimate-policy decision** — changing what this viable system is, what repositories/work it governs, or its ultimate policy/authority topology | `NON-ADMIT` as ordinary S1 work unless that authority has been explicitly delegated by the legitimate owner. Preserve the decision needed and escalate. |
| **Insufficient-evidence work** — the requested claim, classification, repair, or mutation cannot be justified from available primary evidence | `NON-ADMIT`, or stop an already-admitted run when the gap is discovered. Do not guess the missing fact. |

Not all public OSS work is therefore S1 work for this organization.

### Merge and integration

Producing a reviewable PR may close an S1 contribution without granting the S1 authority to merge it.

Merge/integration is a separate decision right. Treat it as outside the S1 envelope unless the work item or repository contract explicitly delegates it. A human review or merge boundary does not by itself establish a new VSM function.

## 3. Routine recovery

After `ADMIT`, the S1 should absorb ordinary local disturbances without step-by-step human direction when all of the following remain true:

- the bounded outcome is unchanged;
- the system/repository boundary is unchanged;
- the recovery uses decision rights already inside the authority envelope;
- no new normative, identity, scope, ultimate-policy, or integration decision is required;
- available evidence remains sufficient to justify the repair;
- the expected validation can still establish closure.

If one of these conditions stops holding, local recovery becomes escalation.

### Recovery table

| Disturbance | Local recovery | Escalate when |
| --- | --- | --- |
| **Stale base / concurrent change** | Refresh current state; rebase, rebuild, or replay the bounded change; repeat applicable validation. Preserve the new base revision. | The concurrent change alters requirements, authority, semantics, frozen provenance, or creates a conflict whose resolution requires a non-delegated decision. |
| **Validation failure** | Diagnose from observable evidence, repair inside the work boundary, and rerun the relevant checks. | Passing validation requires changing the acceptance contract, suppressing a legitimate failure, or making a decision outside delegated authority. |
| **Broken reference** | Locate a stable primary replacement or correct a clearly moved/renamed reference when equivalence can be established. | The replacement changes the substantive claim, provenance cannot be reconstructed, or multiple plausible sources require an authority-level interpretation. |
| **Generated-file drift** | Re-run the canonical deterministic generator and verify source/generated consistency when the source contract is unchanged. | Repair requires changing generator semantics, canonical source data, or another repository-owned contract rather than regenerating it. |
| **Evidence gap** | Search the declared primary evidence surfaces and narrow the claim to what is actually supported. | A material claim/decision still depends on missing, contradictory, or unresolvable evidence. Stop rather than invent evidence. |
| **Legitimate no-change result** | Close with evidence showing the current state already satisfies the bounded outcome or that no justified mutation exists. | The absence of a change cannot itself be established, or the requester must decide a new policy/semantic preference before closure is possible. |

Do not manufacture a failure solely to demonstrate recovery.

## 4. Escalation categories

Escalation identifies the missing decision or evidence; it does not imply a particular future VSM role.

Use the smallest applicable category:

- `BOUNDARY_AMBIGUOUS` — system/work boundary cannot be established without an external decision;
- `AUTHORITY_NORMATIVE` — Profile/Methodology semantics or procedure must be decided;
- `AUTHORITY_IDENTITY_POLICY` — organization identity, scope, ultimate policy, or equivalent governing authority must be decided;
- `AUTHORITY_INTEGRATION` — merge/integration or shared-state mutation is required but not delegated;
- `EVIDENCE_INSUFFICIENT` — primary evidence cannot support the required decision or claim;
- `VALIDATION_INSUFFICIENT` — no available completion evidence can distinguish correct closure from an unsupported result;
- `CONCURRENT_CHANGE_OUT_OF_BOUNDARY` — a stale base or concurrent change has changed the problem beyond the admitted envelope;
- `OTHER_FORBIDDEN_DECISION` — another explicitly forbidden decision is required; name it precisely.

A repository may use more specific local labels, but they should map back to the reason the S1 cannot continue autonomously.

## 5. Evidence preserved on non-admission or escalation

A rejection or escalation is itself a reviewable outcome when it preserves enough evidence for another reviewer to reconstruct why execution stopped.

Record:

```text
work item / requested outcome
system-in-focus and repository revision(s) inspected
governing released or frozen contract
primary evidence inspected
authority envelope considered
failed admission criterion or observed escalation condition
escalation category
local recovery attempted, if any
exact decision/evidence still required
safe next step or owning source-of-truth process, when known
```

Record observable decisions and evidence, not hidden chain-of-thought.

Do not convert `NON-ADMIT` into `ADMIT` merely because a human supplies the next ordinary implementation choice interactively. Either the authority/evidence envelope is explicitly re-established as a new admission decision, or the work remains escalated.

## 6. Closure states

An admitted S1 run ends in one of these observable states:

- `CLOSED_CHANGE` — bounded change produced and required validation/evidence completed;
- `CLOSED_NO_CHANGE` — primary evidence establishes that no justified mutation is required;
- `ESCALATED` — a previously admitted run encountered a condition outside local authority/evidence and preserved the escalation record.

A presented item that never passes the admission gate ends as `NON_ADMITTED`.

These are operational record states for this organization, not VSM autonomy states.

## 7. M0 evidence boundary

Using this contract does not by itself establish `S1=A`.

For a positive autonomy claim, the released Methodology still requires the organizational function, decisive decision right, owner, supporting/enforcement machinery, and closure to be independently reconstructable from primary evidence. Executor/owner provenance is a separate M0 workstream, and repository-specific completion oracles remain separate validation workstreams.
