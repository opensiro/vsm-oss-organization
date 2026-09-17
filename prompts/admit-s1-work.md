# Admit and execute one S1 work item

Use this prompt when a presented VSM Harness OSS work item must first be classified under the runtime-neutral admission/recovery contract in [`S1_TASK_ADMISSION_RECOVERY.md`](../S1_TASK_ADMISSION_RECOVERY.md).

```text
Evaluate one presented work item for bounded S1 execution.

First inspect the current target-repository state, relevant Issue/PR state, the Organization-selected upstream contract (or an explicitly frozen historical contract when declared), and the primary evidence needed to classify the item.

Before executing the requested work, record exactly one verdict:

ADMIT as bounded S1 work
or
NON-ADMIT / ESCALATE with evidence

For admission, establish:
- system-in-focus, target repository, and exact work boundary;
- bounded terminal outcome, including whether an evidence-backed no-change result can close it;
- governing Organization-selected upstream or explicitly frozen historical contract;
- primary evidence required before decisions are made;
- ordinary implementation/research/evidence/repair decisions delegated locally;
- forbidden decisions outside local authority;
- validation evidence/checks required for closure;
- observable escalation conditions;
- whether merge/integration authority is separately delegated.

Do not assume all OSS work belongs to S1. Do not begin the requested mutation if the boundary, authority, validation expectation, or primary evidence is insufficient.

If admitted, execute autonomously inside that envelope. Recover from natural stale bases, validation failures, broken references, generated-file drift, evidence gaps, and comparable routine disturbances when the repair keeps the same outcome, boundary, authority, semantics, and governing contract. Do not manufacture failures.

Human intervention is allowed. If a human intervenes, record the intervention, attribute the affected decision to the human, state which decision/right was affected, and record whether autonomous S1 operation resumed afterward. Do not hide the intervention or count a human-selected decision as agent-owned evidence.

If an intervention or recovery changes the authority envelope, governing contract, work boundary, or required decision class, re-establish admission or preserve an evidence-backed escalation before continuing.

Do not introduce S2/S3/S3*/S4/S5 merely to route an escalation. Identify the legitimate source-of-truth process or authority when known without inventing a future VSM role.

End in exactly one operational state:
- CLOSED_CHANGE — bounded change plus required evidence/checks;
- CLOSED_NO_CHANGE — evidence establishes no justified mutation is required;
- ESCALATED — an admitted run crossed its current authority/evidence boundary;
- NON_ADMITTED — the item never passed the admission gate.

Human intervention is an attribute of the run, not a separate terminal failure state.

For repository mutation, prefer a normal GitHub PR. A reviewable PR may close S1 work without implying authority to merge it.
```
