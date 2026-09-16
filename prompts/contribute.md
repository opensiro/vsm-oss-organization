# Work on one OpenSiro OSS contribution

Use this prompt for a bounded contribution under the current S1-first organization. The durable admission/recovery contract is [`S1_TASK_ADMISSION_RECOVERY.md`](../S1_TASK_ADMISSION_RECOVERY.md).

```text
Work on one bounded public OpenSiro OSS contribution.

Before execution, perform the S1 admission gate.

Inspect current repository and relevant Issue/PR state, then record exactly one verdict:

ADMIT as bounded S1 work
or
NON-ADMIT / ESCALATE with evidence

For admission, establish:
- system-in-focus, target repository, and exact work boundary;
- expected reviewable outcome, including whether a legitimate no-change result can close the item;
- released or explicitly frozen contract that governs the work;
- primary evidence required before decisions are made;
- ordinary implementation/research/evidence/repair decisions inside local authority;
- forbidden decisions outside local authority;
- evidence/tests required for completion;
- observable escalation conditions;
- whether merge/integration authority is separately delegated.

Do not assume all OSS work is S1 work. Do not begin the requested mutation if the boundary, authority, validation expectation, or primary evidence is insufficient.

If admitted, execute autonomously inside the declared envelope. Handle natural stale bases, validation failures, broken references, generated-file drift, and other routine local disturbances yourself when the repair does not change the outcome, authority, semantics, or governing contract. Do not manufacture failures.

If recovery would require a normative Profile/Methodology decision, organization identity/scope/ultimate-policy decision, undelegated merge/integration decision, unsupported evidence claim, or another forbidden choice, stop and preserve an evidence-backed escalation instead of asking a human for ordinary step-by-step decisions and continuing to call the run autonomous.

Do not silently change VSM semantics, assessment methodology, frozen Index contracts, licensing, project identity/scope, or other authority boundaries owned elsewhere. Escalate those decisions to the legitimate source-of-truth process without inventing a future VSM role merely for routing.

Completion is one observable terminal state:
- CLOSED_CHANGE — bounded change plus required evidence/checks;
- CLOSED_NO_CHANGE — evidence establishes no justified mutation is required;
- ESCALATED — an admitted run crossed its authority/evidence boundary;
- NON_ADMITTED — the item never passed the admission gate.

Prefer a normal GitHub PR for repository mutations. A reviewable PR may close S1 work without implying authority to merge it.
```
