# Contributing

This repository defines a VSM-based contribution contract for OpenSiro OSS. Contributors may use any local runtime, scheduler, model provider, or agent harness. OpenSiro standardizes organizational responsibilities and GitHub boundaries, not execution technology.

## Current milestone: M1

The current formal milestone is M1, targeting `A — C C — —`.

Current evidence state:

- `S1=A` is established from M0;
- `S3*=C` is established by the current complementary-audit constructor and real witness;
- `S3=C` remains open until one naturally qualifying current-control transaction closes #39;
- M2-specific `S5=P` evidence already exists, but formal M2 completion remains sequentially blocked on M1.

Do not manufacture an S3 disturbance merely to complete the milestone. Ordinary repository-local work remains with the S1 domain that has the requisite information and delegated authority.

The reference contribution unit remains one bounded autonomous S1 loop unless the work item genuinely crosses a higher-level organizational boundary:

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

## Escalation and parent-governed S5

Start with [`CONTRIBUTOR_START.md`](CONTRIBUTOR_START.md) for repository ownership and organization-wide routing.

A contributor may operate the parent-governed S5 admission process described in [`prompts/parent-control-plane.md`](prompts/parent-control-plane.md): gather evidence, prepare options, record/apply a returned decision, and verify closure. Running that process does **not** transfer the unresolved S5 decisive right to the contributor.

Use the shorthand only as an admission request:

```text
S5: рассмотреть <matter>
S5: consider <matter>
```

Existing returned parent policy may be applied by a contributor without creating a new S5 event. A genuinely unresolved identity / ultimate-policy choice must reach the legitimate parent declared by [`S5_PARENT_AUTHORITY.md`](S5_PARENT_AUTHORITY.md). Ordinary S1 work, S3 current-control, S3* audit, PR review, CI repair, or routine tool use must not be promoted into S5 merely because the matter is important.

## GitHub boundary

Prefer one claimed work item → one reviewable PR unless the work item explicitly defines another artifact.

Do not mutate shared canonical state merely to prove autonomy. Use normal GitHub review/integration boundaries. Whether those boundaries later participate in S2 is a functional question at the relevant recursion level; PRs are not defined as either S2 or non-S2 by name.

## Autonomous progress and owner observability

Autonomous execution is useful only when the project owner can cheaply recover the state of work. A contributor or agent should therefore optimize for both **completion** and **owner observability**.

### Run boundary

For an ordinary autonomous run:

1. complete the explicitly requested work item;
2. complete at most **one or two obvious downstream steps** that are directly implied by that work and remain inside the same authority/evidence boundary;
3. finish an already-started atomic delivery chain such as `branch → PR → CI → fix → merge` rather than stopping in the middle;
4. stop before opening a new independent research/program of work merely because another useful idea is visible.

This is a default stop rule, not a prohibition on larger explicitly assigned work. A work item may define a broader bounded sequence in advance.

### Owner-facing snapshot

At the end of a meaningful autonomous run, provide one compact control-plane snapshot that lets the owner recover context without reading every intermediate update:

```text
OpenSiro status

DONE
- up to three durable results

NOW
- current milestone / work-state change

BLOCKED
- none, or the concrete blocker and where it lives

NEXT
- one next step and why it is next

NEED YOU
- none, or the exact owner decision/input required
```

Use issue/PR/commit identifiers as supporting provenance, not as the primary narrative. Routine green CI, intermediate branch mechanics, and low-level tool activity should normally be omitted unless they failed or materially changed the result.

If `NEED YOU = none`, do not manufacture an approval request merely to force interaction. The snapshot should still make the next autonomous continuation obvious.

### Boundary

This reporting convention is an **observability/interface rule for contributors**. It does not establish S2, S3, S3*, S4, S5, an autonomy state, or a new decision owner by itself. Function and ownership claims still require the normal Profile/Methodology evidence.

## Milestone discipline

Do not add permanent S2/S3/S3*/S4/S5 agents pre-emptively. New role prompts and control surfaces count only when the relevant organizational function, decisive right, owner, boundary reachability, and closure evidence are established under the active Profile/Methodology.

The current roadmap target is:

```text
M0  A — — — — —
M1  A — C C — —
M2  A — C C — P
M3  A — A C — P
M4  A A A C — P
M5  A A A C A P
```

The long-term reference target is therefore `A A A C A P`. Present autonomy claims must follow actual function, ownership, and closure evidence; `A`, `C`, and `P` are ownership arrangements, not a maturity ladder.
