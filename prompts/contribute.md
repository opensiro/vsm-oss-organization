# Work on one OpenSiro OSS contribution

Use this prompt for one bounded contribution under the current M0 S1-first organization.

```text
Work on one bounded public OpenSiro OSS contribution.

Use:
- roles/S1.md for the common S1 action loop;
- S1_DOMAIN_CONTRACTS.md for the local operational envelope;
- S1_TASK_ADMISSION_RECOVERY.md for admission, recovery, and terminal states.

Before admission, declare exactly one current M0 S1 domain:

INDEX
→ opensiro/vsm-harness-index

SKILLS
→ opensiro/vsm-harness-skills

AWESOME
→ opensiro/awesome-vsm-harness

If the requested work is primarily Profile semantics, Organization/metasystem design, cross-S1 authority, identity/policy, or another surface outside those local operational outcomes, do not force it into S1. Return NON-ADMITTED / ESCALATED with evidence.

For the presented work item, execute this action sequence as applicable:

1. INSPECT / OBSERVE
- inspect the current default branch or declared starting revision;
- inspect relevant files, issues/PRs, tests, generated artifacts, governing contract, and primary evidence;
- inspect the selected domain envelope in S1_DOMAIN_CONTRACTS.md;
- notice material concurrent changes that may affect the task boundary.

2. BOUND / ADMIT
- state the selected S1 domain;
- identify the system-in-focus and exact work boundary;
- state the reviewable local outcome;
- state the local authority and forbidden decisions from the domain envelope;
- state the completion evidence and escalation conditions;
- record ADMIT or NON-ADMIT / ESCALATE before ordinary execution.

3. CHOOSE LOCAL EXECUTION
- independently choose the implementation/research/evidence/repair strategy inside the admitted local envelope;
- choose task-local files, ordering, helper tools/agents, branch/commit structure, validation, and bounded retry decisions without step-by-step human control.

4. PRODUCE / MUTATE
- perform the actual bounded work of the selected domain;
- prefer a normal GitHub branch + PR for repository changes;
- do not mutate Profile/Organization/metasystem surfaces merely because they are writable.

5. VALIDATE
- use the domain-specific completion evidence in S1_DOMAIN_CONTRACTS.md;
- run applicable tests/validators/generation/provenance/reference checks;
- inspect the actual diff/result against the declared completion evidence;
- accept CLOSED_NO_CHANGE when primary evidence establishes that no mutation is justified.

6. RECOVER
- handle ordinary local failures yourself while the original outcome, authority, contract, and evidence boundary remain intact;
- repair validation failures, stale bases, ordinary conflicts, broken references, generated drift, tool failures, and resolvable evidence gaps;
- escalate instead of making a new undelegated normative/policy/scope/integration/security/licensing or cross-S1 decision.

7. PRESERVE EVIDENCE / PACKAGE OUTCOME
- preserve the selected domain, relevant starting refs, governing contract, primary evidence, changed surfaces, validation results, recovery/intervention/escalation facts, and final reviewable artifact refs;
- do not record hidden chain-of-thought.

8. CLOSE OR ESCALATE
End with exactly one operational state:
- CLOSED_CHANGE
- CLOSED_NO_CHANGE
- ESCALATED
- NON_ADMITTED

Do not silently change VSM semantics, system-wide assessment Methodology authority, organizational identity/scope/policy, cross-S1 authority, licensing policy, repository security/permissions, or other authority boundaries owned elsewhere.

Merge/integration to a protected/default branch remains separate unless explicitly delegated. Producing a validated reviewable PR can be a complete S1 outcome.

GitHub, plugins/connectors, CI, helper agents, model/runtime, schedulers, and validators are supporting mechanisms. Do not reinterpret them as additional VSM functions merely because they are used during execution.
```