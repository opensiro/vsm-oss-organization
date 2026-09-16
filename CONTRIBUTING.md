# Contributing

This repository defines a VSM-based contribution contract for the in-scope OpenSiro VSM Harness OSS group listed in `README.md`. Contributors may use any local runtime, scheduler, model provider, or agent harness. This control plane standardizes organizational responsibilities and GitHub boundaries, not execution technology.

## Current milestone: M0

The current reference contribution unit is one bounded autonomous S1 loop.

```text
Issue / explicit work item
        ↓
claim one bounded contribution
        ↓
contributor-owned agent runtime
        ↓
research / implementation / validation / recovery
        ↓
Issue artifact or Pull Request
```

A contribution should state:

- system-in-focus and repository boundary;
- expected outcome;
- evidence/tests required for completion;
- actions that remain inside local authority;
- escalation conditions that exceed the contribution boundary.

The agent should own ordinary local decisions and failure recovery. The contributor owns the runtime envelope: scheduler, model choice, credentials, budget, sandbox, and launch cadence.

## One S1 does not mean one process

A contributor may use several internal agents or tools. Do not create extra VSM functions from process names alone.

Several workers remain one S1 when they jointly close one durable contribution outcome and do not operate as independently regulated operational units with separate environments and autonomy.

## GitHub boundary

Prefer one claimed work item → one reviewable PR unless the work item explicitly defines another artifact.

Do not mutate shared canonical state merely to prove autonomy. Use normal GitHub review/integration boundaries. Whether those boundaries later participate in S2 is a functional question at the relevant recursion level; PRs are not defined as either S2 or non-S2 by name.

## Future milestones

Do not add permanent S2/S3/S3*/S4/S5 agents pre-emptively. New role prompts and control surfaces are introduced only when [ROADMAP.md](ROADMAP.md) establishes the disturbance they regulate.

The long-term reference target is `A A A A A P`, but present autonomy claims must follow actual function, ownership, and closure evidence.
