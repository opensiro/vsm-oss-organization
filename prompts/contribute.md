# Work on one OpenSiro OSS contribution

Use this prompt for a bounded contribution under the current M0 S1-first organization.

```text
Work on one bounded public OpenSiro OSS contribution.

Use the active S1 role in roles/S1.md and the admission/recovery contract in S1_TASK_ADMISSION_RECOVERY.md.

For the presented work item, execute this action sequence as applicable:

1. INSPECT / OBSERVE
- inspect the current default branch or declared starting revision;
- inspect relevant files, issues/PRs, tests, generated artifacts, governing contract, and primary evidence;
- notice material concurrent changes that may affect the task boundary.

2. BOUND / ADMIT
- identify the system-in-focus and exact work boundary;
- state the reviewable outcome;
- state the local authority and forbidden decisions;
- state the completion evidence and escalation conditions;
- record ADMIT or NON-ADMIT / ESCALATE before ordinary execution.

3. CHOOSE LOCAL EXECUTION
- independently choose the implementation/research/evidence/repair strategy inside the admitted envelope;
- choose task-local files, ordering, helper tools/agents, branch/commit structure, validation, and bounded retry decisions without step-by-step human control.

4. PRODUCE / MUTATE
- perform the actual bounded work: research, edit code/docs/data/config/tests, generate artifacts, or update task-local repository surfaces as justified;
- prefer a normal GitHub branch + PR for repository changes.

5. VALIDATE
- run the applicable tests/validators/generation/provenance/reference checks;
- inspect the actual diff/result against the declared completion evidence;
- accept CLOSED_NO_CHANGE when primary evidence establishes that no mutation is justified.

6. RECOVER
- handle ordinary local failures yourself while the original outcome, authority, contract, and evidence boundary remain intact;
- repair validation failures, stale bases, ordinary conflicts, broken references, generated drift, tool failures, and resolvable evidence gaps;
- escalate instead of making a new undelegated normative/policy/scope/integration/security/licensing decision.

7. PRESERVE EVIDENCE / PACKAGE OUTCOME
- preserve relevant starting refs, evidence, changed surfaces, validation results, recovery/intervention/escalation facts, and final reviewable artifact refs;
- do not record hidden chain-of-thought.

8. CLOSE OR ESCALATE
End with exactly one operational state:
- CLOSED_CHANGE
- CLOSED_NO_CHANGE
- ESCALATED
- NON_ADMITTED

Do not silently change VSM semantics, assessment Methodology, organizational identity/scope/policy, licensing policy, repository security/permissions, or other authority boundaries owned elsewhere.

Merge/integration to a protected/default branch remains separate unless explicitly delegated. Producing a validated reviewable PR can be a complete S1 outcome.

GitHub, plugins/connectors, CI, helper agents, model/runtime, schedulers, and validators are supporting mechanisms. Do not reinterpret them as additional VSM functions merely because they are used during execution.
```