# OpenSiro VSM OSS — start here

This is the **canonical bootstrap protocol for contributor runtimes** working on the public OpenSiro VSM Harness ecosystem.

Repository `README.md` files are public handoff surfaces. Runtime memory and project instructions are working context, not canonical repository state.

## Bootstrap

For substantial OpenSiro work, use this order:

```text
repository README.md / AI handoff
        ↓
START_HERE.md
        ↓
docs/ECOSYSTEM.md
        ↓
owning repository @ current default branch
        ↓
exact issue / PR / release / pinned artifact governing the task
```

Cross-repository architecture and ownership routing live in [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md).

For already tracked current work, consult [`TODO.md`](TODO.md) and then return to the linked owning repository/issue. For new, unclassified, or authority-sensitive work, use [`CONTRIBUTOR_START.md`](CONTRIBUTOR_START.md).

## Source-of-truth rule

1. Inspect the relevant public repository and its current default branch.
2. Inspect the exact task artifact when one exists.
3. Prefer the owning GitHub source over remembered context.
4. Preserve frozen historical provenance.
5. Do not copy fast-changing counts, versions, queues, milestone states, or conclusions into durable runtime assumptions when they can be re-read from their owner.

If a repository-owned fact conflicts with this repository, the owning repository wins. Cross-repository responsibility/routing changes belong here.

## Task boundaries

Explicit task contracts override continuity assumptions. Preserve any declared fresh/independent context, read-only boundary, pinned revision, allowed evidence source, first-attempt semantics, stop condition, fail-closed behavior, prohibited adjacent work, and exact issue/PR instructions.

Do not import task-specific conclusions or repair ideas from earlier work when independent execution is required.

## Execution rule

For a fresh task:

1. identify the system-in-focus;
2. use [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md) to identify the owning repository;
3. refresh that repository from its current default branch;
4. read its local README/contracts and exact governing artifact;
5. keep local work with its owner;
6. validate relevant tests, generated artifacts, provenance, and source-of-truth consistency before closure.

When the resolved work is one ordinary bounded S1 contribution in Index, Skills, or Awesome, [`CONTRIBUTOR_START.md`](CONTRIBUTOR_START.md) routes the agent to the supported [`modes/s1-autonomous/`](modes/s1-autonomous/) operating mode. The mode is an execution path, not an autonomy grade.

For substantial autonomous work, follow [`docs/AUTONOMOUS_WORK_REPORTING.md`](docs/AUTONOMOUS_WORK_REPORTING.md).

## Boundary

This file owns only the bootstrap protocol. It does not redefine VSM semantics, assessment methodology, Index facts, Capability methodology, repository admission, or organizational autonomy.
