# Autonomous work reporting

This contract defines the minimum observability surface for contributors or agents that execute substantial OpenSiro OSS work autonomously across multiple steps.

It exists because execution autonomy without concise state visibility creates a control problem for the project owner: work may be correct and productive while still becoming difficult to supervise, interrupt, or resume.

This is an operating/reporting contract. It does **not** redefine VSM functions, autonomy states, repository ownership, milestone evidence, or decision authority.

## Principle

A contributor may work autonomously inside already-delegated authority, but must keep the project owner able to understand the current state without reconstructing every issue, PR, CI run, or intermediate discussion.

The reporting objective is:

> the owner should be able to understand the important state of an autonomous work run in roughly one short status read.

For tracked work in the bounded VSM Harness OSS group, [`TODO.md`](TODO.md) is the shared current-work index. Status reporting should reconcile with that index rather than creating a second backlog in prose.

## Control-plane snapshot

After a meaningful autonomous run, and before continuing far beyond the original task, emit a compact snapshot with these fields:

```text
OpenSiro status

DONE
- completed outcomes that materially changed project state

NOW
- current milestone / workstream state

BLOCKED
- unresolved blockers, or `none`

NEXT
- the next one or two intended actions and why they are next

NEED YOU
- the exact decision/input required from the owner, or `none`
```

Keep this outcome-oriented. PR numbers, workflow runs, commit SHAs, and implementation details are supporting evidence and should be included only when they help reconstruct or review the state.

### TODO reconciliation

When the run participates in work already tracked in [`TODO.md`](TODO.md):

- `NOW` should identify the matching TODO item or explain why the current run temporarily differs;
- a new durable blocker should be reflected in `TODO.md` rather than living only in the status message;
- `NEXT` should normally come from the owning issue plus the TODO ordering, not from an untracked expansion of scope;
- terminal closure should remove/reclassify the TODO entry after the owning repository records the result.

This does not make `TODO.md` a second evidence database. The linked issue/repository remains authoritative for task content, evidence and acceptance.

## Autonomous continuation rule

When `NEED YOU = none`, a contributor may continue without requesting routine confirmation for work already inside the delegated envelope.

Default continuation boundary:

1. complete the requested task;
2. complete at most one or two obvious downstream steps that directly close or validate it;
3. finish an already-started atomic integration chain such as `branch → PR → CI → fix → merge` rather than stopping mid-chain;
4. then emit the control-plane snapshot before opening a substantially new line of work.

This is a default observability boundary, not a hard prohibition. A task explicitly defined as continuous, batched, or multi-stage may proceed further, but should still emit periodic snapshots at meaningful state transitions.

## What counts as a meaningful state transition

Examples include:

- requested work is complete;
- a PR merges or fails in a way that changes the plan;
- a milestone condition becomes established, falsified, or remains intentionally unproven;
- the work crosses from one repository or organizational function into another;
- a new blocker appears;
- a planned next step changes because evidence invalidated the earlier plan;
- a bounded research phase completes;
- owner authority or a higher-level decision is genuinely required.

Do not emit a full snapshot for every low-level tool call or trivial edit.

## Owner attention budget

Autonomous execution should minimize mandatory owner attention, not maximize output volume.

Prefer:

- one concise state summary over a stream of low-level progress messages;
- explicit `NEED YOU = none` when no decision is required;
- one concrete decision request when authority/input is required;
- preserving enough provenance that the owner can inspect details later without having to follow them live.

Do not silently turn a finished task into an indefinitely expanding research or implementation program merely because another useful step is visible.

## Decision and authority boundary

Reporting does not transfer authority.

A contributor may autonomously execute decisions already delegated to the relevant S1/S3/S3*/other function, but must stop and surface `NEED YOU` when the next action requires an owner decision that is not already determined by existing policy or delegated authority.

For parent-governed S5 matters, follow `S5_PARENT_BOUNDARY.md`, `S5_PARENT_AUTHORITY.md`, and `prompts/parent-control-plane.md`. This reporting contract must not be used to bypass S5 admission or to promote ordinary S1/S3/S3* variety into S5.

## Evidence boundary

The snapshot and `TODO.md` are navigation/control artifacts, not second databases.

Canonical facts remain in their owning repositories, issues, PRs, records, tests, and generated artifacts. Do not manually duplicate detailed assessment state, VSM semantics, candidate evidence, or corpus facts merely to make status self-contained.
