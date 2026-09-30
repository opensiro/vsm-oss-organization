# Autonomous S1 run protocol

Execute exactly one bounded S1 work item.

This protocol composes the canonical S1 actor adapter and contracts into the supported autonomous operating mode. It does not widen authority and it does not override a stricter issue/PR/frozen-artifact boundary.

## 0. Re-ground

Before acting:

1. start from [`../../START_HERE.md`](../../START_HERE.md) when entering from fresh context;
2. identify the exact owning repository and current/frozen revision;
3. read the exact issue/PR/artifact governing the work when one exists;
4. read [`../../roles/S1.md`](../../roles/S1.md), [`../../contracts/s1/domain-contracts.md`](../../contracts/s1/domain-contracts.md), and [`../../contracts/s1/task-admission-recovery.md`](../../contracts/s1/task-admission-recovery.md);
5. declare exactly one S1 domain: Index, Skills, or Awesome.

Fail closed if the required task boundary, authority, or evidence source cannot be reconstructed.

## 1. Open the run record

Create one evidence record from [`../../templates/s1-autonomous-run.md`](../../templates/s1-autonomous-run.md).

Record at minimum:

- domain;
- work item / request;
- starting revision;
- governing contract/task artifact;
- runtime/support machinery;
- declared system/work boundary;
- boundary-reachability statement for this autonomous mode.

Do not claim autonomy from the identity of the GitHub account or transport used to write the record.

## 2. Admit or reject

Apply the canonical admission contract and record exactly one result:

```text
ADMIT
NON_ADMITTED
ESCALATED
```

For `ADMIT`, record the local outcome, delegated decisions, forbidden decisions, completion evidence, escalation conditions, and integration boundary.

If `NON_ADMITTED` or `ESCALATED`, preserve the reason/evidence and end the run with the matching terminal state. Do not improvise a wider authority envelope.

## 3. Execute autonomous local decisions

For an admitted run, the autonomous actor owns ordinary local discretion inside the declared envelope, including as applicable:

- research/evidence strategy;
- implementation or repair strategy;
- files/surfaces selected inside the task boundary;
- ordering of local steps;
- helper tools/agents;
- validation sequence;
- bounded retries and ordinary recovery;
- `CLOSED_CHANGE` versus `CLOSED_NO_CHANGE` when evidence supports closure.

Do not ask a human to choose ordinary local actions merely to continue the run. If human input is actually required, record the exact intervention and whether it changes ownership/boundary.

## 4. Separate support from ownership

Record runtime and support machinery separately from the agent-owned decisions.

Examples of support machinery include:

- ChatGPT/Codex/other runtime implementation;
- GitHub connector/API;
- CI;
- deterministic validators;
- repository scripts;
- schedulers and queues.

These may transport, execute, validate, persist, or enforce a decision. They do not become the owner of the S1 discretion merely by doing so.

## 5. Validate and recover

Validate the actual result using the strongest applicable repository-native evidence.

When an ordinary local disturbance occurs, recover autonomously while all of the following remain unchanged:

- S1 domain;
- task/outcome boundary;
- governing contract;
- delegated authority;
- evidence boundary.

Record the disturbance and recovery. If recovery would require changing one of those boundaries or exercising an undelegated right, escalate instead.

## 6. Close

End with exactly one terminal state:

```text
CLOSED_CHANGE
CLOSED_NO_CHANGE
ESCALATED
NON_ADMITTED
```

For `CLOSED_CHANGE`, preserve the reviewable branch/commit/PR/artifact and validation evidence.

For `CLOSED_NO_CHANGE`, preserve the evidence showing why no mutation was required.

Protected/default-branch integration may remain human-owned after S1 closure. Record that as a separate right rather than treating merge as necessary for S1 ownership.

## 7. Evidence integrity

Before returning control, verify that another reviewer can reconstruct:

1. what the operational outcome was;
2. which decisions were discretionary;
3. which of those decisions the autonomous actor actually owned;
4. what support machinery merely executed/enforced the decisions;
5. whether a human intervened and exactly where;
6. how disturbances were handled;
7. how the result affected the declared S1 domain;
8. why the actor and closure path were reachable through this first-party mode without custom composition.

Do not infer `S1=A` inside the run. Grade interpretation belongs to a later independent assessment.
