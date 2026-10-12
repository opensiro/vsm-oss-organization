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

## First-contact control plane

When a user supplies this bootstrap URL, asks to `start`, `help`, or `show control plane`, or otherwise requests an **open-ended OpenSiro entry point** without a concrete task, the agent should **present the operator interface**, not stop after listing documentation links or silently begin an execution lane.

1. Follow the bootstrap above. Read [`docs/AGENT_CONTROL_PLANE.md`](docs/AGENT_CONTROL_PLANE.md), the current [`README.md`](README.md) scope, and [`TODO.md`](TODO.md). Resolve any displayed milestone, issue, PR, blocker or available work from its **current owning GitHub source**; label unverified state if live access is unavailable.
2. Display a concise **OpenSiro Control Plane** entry surface: what the bounded OSS system is, a source-linked current-work/status snapshot where verified, and the available actions. Distinguish `TODO.md` selected work from other open issues and distinguish milestone targets from established evidence.
3. Offer an **action menu** using real, native clickable buttons or comparable controls **only when the current chat/client supports them**. Button labels may be localized; each action must map to an exact command in [`docs/AGENT_CONTROL_PLANE.md`](docs/AGENT_CONTROL_PLANE.md). No assumed universal button syntax, HTML/Markdown pseudo-buttons, fake click targets, or unsupported host actions.
4. If clickable controls are unavailable, render the **same choices as a compact numbered text menu with copyable commands** and accept free-form commands or repository/issue URLs. This is a required usable fallback, not a failed startup.
5. Merely displaying the interface is **read-only**. A selection is a new command subject to the normal owner/task/permissions/independence/CI gates, never an automatic scheduling, batch admission, review, GitHub write, approval, merge, or background task. Do not suggest an action is executable if the tool or authority to perform it is missing; expose the limitation and permissible read-only path.

For a **specific actionable request** (for example `continue Index #123` or a named PR), carry out that task under the normal bootstrap and controls **without forcing the introductory menu**. The interface is a discoverability aid, not a modal gate, role assignment, scheduler, or new VSM function. The complete command list, display defaults and acceptance cases live in [`docs/AGENT_CONTROL_PLANE.md`](docs/AGENT_CONTROL_PLANE.md).

## Single-agent operator entry

A maintainer can use one agent conversation for `status`, `continue`, a named issue/PR, or a cross-repository status request. The owner-facing command and gate-handling interface is [`docs/AGENT_CONTROL_PLANE.md`](docs/AGENT_CONTROL_PLANE.md). It **uses** this bootstrap and the owning repository contracts; it is not a new scheduler, an independent reviewer runtime, or an authorization override. The maintainer need not create a new chat by default, but genuine source-first independence cannot be claimed from a contaminated context.

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
