# OpenSiro VSM OSS — start here

This is the **common bootstrap entry point** for work on the public OpenSiro VSM Harness ecosystem.

It is intended for humans, persistent ChatGPT Projects such as `opensiro-index-oss`, coding agents, research agents, and other contributor runtimes. Runtime memory and project instructions are working context, not canonical repository state.

## Bootstrap

For substantial OpenSiro work, use this order:

```text
START_HERE.md
        ↓
ECOSYSTEM.md
        ↓
owning repository @ current default branch
        ↓
exact issue / PR / release / pinned artifact governing the task
```

If the goal is to select **already tracked current work**, consult [`TODO.md`](TODO.md) and then return to the linked owning repository/issue. If the work is new, unclassified, or needs an authority/routing decision, use [`CONTRIBUTOR_START.md`](CONTRIBUTOR_START.md).

## Source-of-truth rule

[`ECOSYSTEM.md`](ECOSYSTEM.md) owns the cross-repository responsibility map. Do not maintain a second copy of that map here.

Repository-local facts, semantics, procedures, evidence, and implementation remain authoritative in the repository that owns them.

For current state:

1. inspect the relevant public repository and its current default branch;
2. inspect the exact task artifact when one exists;
3. prefer the owning GitHub source over remembered context;
4. explain material evolution when prior context and current state differ;
5. do not copy fast-changing counts, versions, queues, milestone states, or repository conclusions into durable runtime instructions when they can be re-read from their owner.

## Runtime / persistent-project contract

Persistent workspaces may retain summaries, prior chats, memories, or local instructions for continuity. They must not become a parallel control plane.

```text
GitHub canonical state
        ↓ refreshes
runtime / project working context

runtime memory
        ✕ does not implicitly overwrite
GitHub canonical state
```

Do not silently use private OpenSiro repositories, private R&D context, unpublished internal artifacts, or unrelated personal context. Use another source only when the user explicitly introduces it for the task.

## Task boundaries

Explicit task contracts override continuity assumptions. Preserve any declared:

- fresh or independent context;
- read-only boundary;
- pinned or frozen revision;
- allowed evidence sources;
- first-attempt semantics;
- stop conditions;
- fail-closed behavior;
- prohibited adjacent work;
- exact issue or PR instructions.

Do not import conclusions, repair ideas, expected outcomes, or hidden assumptions from earlier work when the task requires an independent context.

## Execution rule

For a fresh task:

1. identify the system-in-focus;
2. use [`ECOSYSTEM.md`](ECOSYSTEM.md) to identify the owning repository;
3. refresh that repository from its current default branch;
4. read its repository-local README/contracts and the exact governing artifact;
5. keep local work with its owner and route only genuinely cross-repository responsibility/authority questions back here;
6. validate relevant tests, generated artifacts, provenance, and source-of-truth consistency before closure.

For substantial autonomous work, follow [`AUTONOMOUS_WORK_REPORTING.md`](AUTONOMOUS_WORK_REPORTING.md).

## Context drift

Persistent context will become stale as repositories evolve. The control mechanism is **re-grounding**, not perfect memory.

When drift is found, refresh from the owner rather than preserving a stale runtime assumption. Historical assessments, experiments, releases, and frozen research runs keep their exact original provenance.

## Boundary

This file owns only the bootstrap protocol. It does not redefine VSM semantics, assessment methodology, Index facts, Capability methodology, repository admission, or organizational autonomy.

If this file disagrees with an owning repository on a repository-owned fact, the owning repository wins. If the disagreement is about cross-repository responsibility or routing, update `vsm-oss-organization` rather than creating another parallel context document.
