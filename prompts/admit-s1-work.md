# Admit and execute one S1 work item

Use this prompt when a presented VSM Harness OSS work item must first be classified under the runtime-neutral admission/recovery contract in [`S1_TASK_ADMISSION_RECOVERY.md`](../S1_TASK_ADMISSION_RECOVERY.md).

```text
Evaluate one presented work item for bounded S1 execution.

First inspect the current target-repository state, relevant Issue/PR state, applicable released or explicitly frozen contract, and the primary evidence needed to classify the item.

Before executing the requested work, record exactly one verdict:

ADMIT as bounded S1 work
or
NON-ADMIT / ESCALATE with evidence

For admission, establish:
- system-in-focus, target repository, and exact work boundary;
- bounded terminal outcome, including whether an evidence-backed no-change result can close it;
- governing released or explicitly frozen contract;
- primary evidence required before decisions are made;
- ordinary implementation/research/evidence/repair decisions delegated locally;
- forbidden decisions outside local authority;
- validation evidence/checks required for closure;
- observable escalation conditions;
- whether merge/integration authority is separately delegated.

Do not assume all OSS work belongs to S1. Do not begin the requested mutation if the boundary, authority, validation expectation, or primary evidence is insufficient.

If admitted, execute autonomously inside that envelope. Recover from natural stale bases, validation failures, broken references, generated-file drift, evidence gaps, and comparable routine disturbances when the repair keeps the same outcome, boundary, authority, semantics, and governing contract. Do not manufacture failures.

If recovery requires a normative Profile/Methodology decision, organization identity/scope/ultimate-policy decision, undelegated merge/integration decision, unsupported evidence claim, or another forbidden choice, stop and preserve an evidence-backed escalation. Do not ask a human to supply ordinary step-by-step decisions and then continue to describe the same run as autonomous.

Do not introduce S2/S3/S3*/S4/S5 merely to route an escalation. Identify the legitimate source-of-truth process or authority when known without inventing a future VSM role.

End in exactly one operational state:
- CLOSED_CHANGE — bounded change plus required evidence/checks;
- CLOSED_NO_CHANGE — evidence establishes no justified mutation is required;
- ESCALATED — an admitted run crossed its authority/evidence boundary;
- NON_ADMITTED — the item never passed the admission gate.

For repository mutation, prefer a normal GitHub PR. A reviewable PR may close S1 work without implying authority to merge it.
```
