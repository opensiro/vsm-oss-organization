# OpenSiro VSM OSS — start here

This is the **common bootstrap entry point** for work on the public OpenSiro VSM Harness ecosystem.

It is intended for humans, ChatGPT Projects (including `opensiro-index-oss`), coding agents, research agents, and other contributor runtimes. A runtime may keep its own memory or project instructions, but those are **working context, not a source of truth**.

When beginning a fresh task, recovering context, or resolving disagreement between remembered context and the repositories, start here.

## Bootstrap rule

Use this order:

```text
START_HERE.md
        ↓
ECOSYSTEM.md
        ↓
owning repository + its current main
        ↓
authoritative issue / PR / pinned artifact for the task
        ↓
TODO.md only when selecting already-tracked current work
```

Do not reconstruct current project state from chat history when current public repository state is available.

## Runtime / ChatGPT Project contract

For the ChatGPT Project `opensiro-index-oss` and equivalent persistent workspaces:

1. Treat this file as the common public bootstrap contract.
2. Treat saved project instructions, memories, summaries, and prior chats as **continuity aids only**.
3. Before making a current-state claim or repository change, inspect the relevant public repository on its current default branch.
4. If remembered context conflicts with current GitHub state, **GitHub wins**. Explain the evolution when it matters.
5. Do not copy fast-changing repository facts into the Project context merely to keep them "in sync". Link or re-read the owning source instead.
6. Do not silently use private OpenSiro repositories, private R&D context, or unpublished artifacts.
7. Keep repository responsibilities separate; route changes to the owner of the fact or procedure.
8. For substantial work, preserve the task's explicit issue/PR/frozen-ref boundaries even if broader Project context suggests adjacent work.

This makes synchronization intentionally asymmetric:

```text
GitHub canonical state
        ↓ refreshes
runtime / ChatGPT Project working context

runtime memory
        ✕ does not overwrite
GitHub canonical state
```

A Project may summarize the ecosystem for convenience, but the summary must not become a parallel control plane.

## Source-of-truth map

Read [`ECOSYSTEM.md`](ECOSYSTEM.md) for the full cross-repository architecture. The minimum routing map is:

| Need | Authoritative public source |
| --- | --- |
| VSM semantics: S1–S5, recursion, autonomy, variety, escalation, evidence boundaries | `opensiro/vsm-harness-profile` |
| Assessment procedure and autonomy classification | `opensiro/vsm-harness-skills` |
| Canonical repository-relative assessments, provenance, catalog and deterministic views | `opensiro/vsm-harness-index` |
| General per-function capability evidence | `opensiro/vsm-harness-capability` (**experimental**) |
| Representative curated downstream view | `opensiro/awesome-vsm-harness` |
| Cross-repository architecture, routing, authority, coordination and current-work control | `opensiro/vsm-oss-organization` |

The experimental Capability repository is adjacent to the currently bounded VSM OSS organization; its presence in this routing map does not admit it as an S1 domain or change the organizational boundary.

## Stable architecture invariants

Keep these distinctions unless their owning source changes them:

```text
Beer / cybernetics
        ↓
VSM Harness Profile
        ↓
VSM assessment procedure / skills
        ↓
VSM Harness Index
        ↓
curated downstream views
```

The Profile owns organizational semantics. Skills applies them. The Index owns assessment instances and derived corpus views. Awesome curates representative examples.

For assessment work, map the **organizational function first** and classify autonomy second. Do not infer VSM functions from component names.

Autonomy states are ownership arrangements, not a maturity ladder. Do not interpret `A`, `C`, and `P` as ordinal grades.

Capability evidence is separate from canonical ownership/classification. Benchmark performance does not create a canonical VSM function or autonomy state.

## Task start procedure

For every fresh task:

1. **Identify the system-in-focus.** Which repository or bounded organization is actually being changed or studied?
2. **Identify the owner.** Use the source-of-truth map above and the repository's own README/contracts.
3. **Refresh current state.** Read current `main` and the exact issue, PR, release, pinned revision, or artifact governing the task.
4. **Preserve explicit boundaries.** If the task declares a fresh/independent context, frozen revision, read-only role, first-attempt rule, stop condition, or fail-closed behavior, that contract overrides convenience from prior runtime context.
5. **Execute locally.** Keep repository-local work in its owning repository. Route cross-repository authority/control questions here.
6. **Validate before closure.** Check relevant tests, generated artifacts, provenance, and source-of-truth consistency.
7. **Report compactly.** For substantial autonomous work, follow [`AUTONOMOUS_WORK_REPORTING.md`](AUTONOMOUS_WORK_REPORTING.md).

If selecting **already tracked current work**, use [`TODO.md`](TODO.md). If the work is new, unclassified, or needs routing, use [`CONTRIBUTOR_START.md`](CONTRIBUTOR_START.md).

## Context drift

A persistent runtime will inevitably accumulate stale statements as repositories evolve. That is expected. The control mechanism is not perfect memory; it is **cheap re-grounding in authoritative state**.

When drift is found:

- do not edit history to make it look as if the old context was always correct;
- update the owning repository when the canonical contract itself changed;
- otherwise refresh the runtime summary from the owning repository;
- preserve exact historical provenance for frozen assessments, experiments, releases, and completed research runs.

A useful runtime summary should therefore contain mostly stable routing rules and links, not copied live counts, current issue queues, current versions, or assessment conclusions.

## Boundary

This file is a bootstrap and routing contract. It does not redefine VSM semantics, assessment methodology, Index facts, Capability methodology, repository admission, or organizational autonomy.

If this file disagrees with an owning repository on a repository-owned fact, the owning repository is authoritative. If the disagreement is about cross-repository responsibility or organizational routing, fix this repository rather than creating another parallel context document.
