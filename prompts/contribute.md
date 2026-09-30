# Work on one Opensiro OSS contribution

Use this prompt for one bounded contribution inside the current S1-first organization.

```text
Work on one bounded public Opensiro OSS contribution.

Use:
- roles/S1.md for the executable S1 actor/action loop;
- contracts/s1/domain-contracts.md for the local operational envelope;
- contracts/s1/task-admission-recovery.md for admission, recovery, intervention, escalation, and terminal states.

Before admission, declare exactly one current S1 domain:

INDEX
→ opensiro/vsm-harness-index

SKILLS
→ opensiro/vsm-harness-skills

AWESOME
→ opensiro/awesome-vsm-harness

If the requested work is primarily Profile semantics, Organization/metasystem design, cross-S1 authority, identity/policy, or another surface outside those local operational outcomes, do not force it into S1. Return NON-ADMITTED / ESCALATED with evidence.

For the presented work item:

1. INSPECT / OBSERVE
- inspect the current default branch or declared starting revision;
- inspect relevant files, issues/PRs, tests, generated artifacts, governing contract, and primary evidence;
- inspect the selected domain envelope in contracts/s1/domain-contracts.md;
- notice material concurrent changes that may affect the task boundary.

2. BOUND / ADMIT
- state the selected S1 domain;
- identify the system-in-focus and exact work boundary;
- state the reviewable local outcome;
- state local authority and forbidden decisions from the domain envelope;
- state completion evidence and escalation conditions;
- record ADMIT or NON-ADMIT / ESCALATE before ordinary execution.

3. CHOOSE LOCAL EXECUTION
- independently choose implementation/research/evidence/repair strategy inside the admitted envelope;
- choose task-local files, ordering, helper tools/agents, branch/commit structure, validation, and bounded retry decisions without step-by-step human control.

4. PRODUCE / MUTATE
- perform the bounded work of the selected domain;
- prefer a normal GitHub branch + PR for repository changes;
- do not mutate Profile/Organization/metasystem surfaces merely because they are writable.

5. VALIDATE
- use the domain-specific completion evidence in contracts/s1/domain-contracts.md;
- run applicable tests/validators/generation/provenance/reference checks;
- inspect the actual diff/result against declared completion evidence;
- accept CLOSED_NO_CHANGE when primary evidence establishes that no mutation is justified.

6. RECOVER
- handle ordinary local failures yourself while outcome, authority, contract, and evidence boundary remain intact;
- escalate instead of making a new undelegated normative/policy/scope/integration/security/licensing or cross-S1 decision.

7. PRESERVE EVIDENCE / PACKAGE OUTCOME
- preserve domain, starting refs, governing contract, primary evidence, changed surfaces, validation, recovery/intervention/escalation facts, and final artifact refs;
- do not record hidden chain-of-thought.

8. CLOSE OR ESCALATE
End with exactly one operational state:
- CLOSED_CHANGE
- CLOSED_NO_CHANGE
- ESCALATED
- NON_ADMITTED

Merge/integration to a protected/default branch remains separate unless explicitly delegated. Producing a validated reviewable PR can be a complete S1 outcome.

GitHub, plugins/connectors, CI, helper agents, model/runtime, schedulers, and validators are supporting mechanisms. Do not reinterpret them as VSM functions merely because they are used during execution.
```