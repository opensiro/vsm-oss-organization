# VSM Harness OSS contributor routing

This file is the common **routing** entry point for contributors and agents that arrive through one of the repositories in the bounded **OpenSiro VSM Harness OSS group** and need to determine where work belongs.

For already tracked work, the single current-work entry point is [`TODO.md`](TODO.md). Use this file when the work is new, unclassified, cross-repository, or needs an authority/routing decision.

The canonical membership of that group is the `Current in-scope public repositories:` block in [README.md](README.md). This file does not expand that set.

The work-lifecycle ownership map is defined in [`CONTROL_PLANE.md`](CONTROL_PLANE.md). Do not duplicate it here: milestones plan destinations, issues own durable work contracts, `TODO.md` schedules current issues, and existing organizational contracts own admission/execution/escalation/closure.

## Current tracked work

Start with [`TODO.md`](TODO.md) when the goal is to pick up existing work.

`TODO.md` owns only cross-repository current selection and ordering through `NOW`, `NEXT`, and `BLOCKED`. The linked repository and issue remain authoritative for scope, evidence, frozen refs, validation and acceptance.

Do not scrape every open issue and treat it as equally current. An open issue may be a frozen batch, durable source tracker, watchlist, future trigger, milestone evidence record, or executable work that simply has not been selected into the current scheduler.

The linked organization-level GitHub Project may be used as an optional human visual projection, but autonomous correctness must not depend on Project fields/items and the Project must not become a second current-work source of truth.

## New to OpenSiro?

For a plain-language and visual introduction to why this work exists, start with **[opensiro.com](https://opensiro.com)** and the **[VSMLite / VSM poster](https://opensiro.com/vsm.html)**. The poster introduces the harness-normalization problem and the organizational relationships that motivate the VSM coordinate system.

This orientation is optional and non-normative. `opensiro.com` is a presentation layer outside the bounded VSM Harness OSS system. Return to the owning GitHub repositories for canonical semantics, assessment procedure, evidence-backed findings, contributor authority, and work acceptance.

## Routing rule

**Repository-local work stays in the repository that owns the relevant source of truth.**

Use `opensiro/vsm-oss-organization` when the question is organization-wide within the declared VSM Harness OSS group: contributor roles, authority boundaries, escalation, cross-repository coordination, shared current-work selection, milestone sequencing, or evolution of the shared contribution control plane.

Repositories and research tracks outside the declared scope are not governed by this routing contract merely because they are public or live under the `opensiro` organization.

## Autonomous work reporting

For substantial multi-step autonomous work, follow [`AUTONOMOUS_WORK_REPORTING.md`](AUTONOMOUS_WORK_REPORTING.md).

The contributor should keep owner attention cheap: complete the requested work, finish any already-started atomic integration chain, take at most one or two obvious downstream closure/validation steps by default, then emit the compact owner-facing snapshot:

```text
DONE
NOW
BLOCKED
NEXT
NEED YOU
```

When the run is executing tracked work, `NOW`, `BLOCKED`, and `NEXT` should reconcile with `TODO.md` rather than creating a parallel backlog in status prose.

Use `NEED YOU = none` when no real owner decision is required. This is a reporting/observability contract only; it does not create a VSM function, autonomy state, scheduling decision, or decision owner.

A `BLOCKED` scheduler/reporting state is not itself an algedonic signal. Exceptional escalation remains governed by the selected Profile semantics and the owning execution contract.

## Parent-governed S5 entry

Any contributor working inside this bounded Organization may request admission to the existing parent-governed S5 process with:

```text
S5: рассмотреть <matter>
S5: consider <matter>
```

The canonical operating prompt is [`prompts/parent-control-plane.md`](prompts/parent-control-plane.md).

The prefix is a request to **classify and route** the matter, not permission for the caller to exercise S5 authority. The process distinguishes:

- `S5_ADMITTED` — a genuinely unresolved identity / ultimate-policy matter that must reach the legitimate parent;
- `POLICY_ALREADY_GOVERNS` — an existing returned parent policy already determines the case, so the contributor may apply that policy without creating a new S5 event;
- `NOT_S5` — the matter belongs to an already-delegated lower function and must stay there;
- `INSUFFICIENT_AUTHORITY` — the matter may be S5-level but legitimate parent ownership cannot be reconstructed.

A contributor may gather evidence, prepare options, write the decision record, implement a returned decision, and verify closure. Those activities do **not** transfer the unresolved S5 decisive right to the contributor. Under the current authority declaration, a genuinely new identity / ultimate-policy choice is escalated to the legitimate parent defined by [`S5_PARENT_AUTHORITY.md`](S5_PARENT_AUTHORITY.md).

Do not route ordinary S1 work, S3 current-control, S3* audit, PR review, CI repair, or routine tool use into S5 merely because the matter is important or because a maintainer is involved.

## Routing conformance

Every repository in the canonical in-scope set must expose the Organization boundary directly from its root README and must expose the shared [`TODO.md`](TODO.md) route for already tracked work.

The routing outcome remains:

- repository-local work remains in the repository that owns the source of truth;
- organization-wide contributor roles, authority, escalation, cross-repository coordination, shared work ordering, milestone sequencing, or organizational evolution route to `opensiro/vsm-oss-organization`;
- tracked work selection starts at `TODO.md`, then returns to the owning repository/issue for execution.

Equivalent wording is allowed when a repository needs to preserve a domain-specific boundary, but the route itself must remain directly discoverable from the repository root.

See [ROUTING_CONFORMANCE.md](ROUTING_CONFORMANCE.md) for the scoped cross-repository oracle, evidence boundary, and blind-agent trial protocol.

## In-scope repository map

| Repository | Repository-local responsibility | Relationship to this control plane |
| --- | --- | --- |
| `opensiro/vsm-harness-profile` | Normative VSM Harness semantics | In-scope normative authority; local semantic changes stay in Profile |
| `opensiro/vsm-harness-skills` | Assessment methodology, skills, validation tooling | In-scope operational domain; local procedure changes stay in Skills |
| `opensiro/vsm-harness-index` | Evidence-backed assessments, catalog/provenance, generated views | In-scope operational domain; local assessment work stays in Index |
| `opensiro/awesome-vsm-harness` | Curated downstream organizational examples | In-scope operational domain; local curation stays in Awesome |
| `opensiro/vsm-oss-organization` | Contributor roles, authority, escalation, cross-repository control, work selection and organizational evolution | Organizational/metasystem construction surface and routing/current-work entry point |

The table above is explanatory. Canonical membership remains the README scope block and is mechanically checked against the Organization contracts.

## Agent decision procedure

When starting from an in-scope repository:

1. If you are looking for **existing tracked work**, open [`TODO.md`](TODO.md), choose the applicable current issue, then return to its owning repository/issue.
2. Otherwise read the starting repository's README and identify its local source-of-truth responsibility.
3. If the requested change is local to that responsibility, stay in that repository.
4. If the requested change concerns contributor authority, escalation, multiple in-scope repositories, current-work ordering, milestone sequencing, or the shared contribution control plane, continue here.
5. From here, route domain-specific work back to the owning repository rather than duplicating its facts or semantics.
6. If the unresolved question is specifically about identity, ultimate policy, system boundary, legitimate authority, or the delegated autonomy envelope, use the parent-governed S5 entry above; otherwise do not invoke S5.

Examples:

- pick up the current Index assessment → `TODO.md` → owning Index issue;
- change the definition of S3* → `vsm-harness-profile`;
- change the assessment procedure → `vsm-harness-skills`;
- reassess one harness → `vsm-harness-index`;
- change Awesome curation → `awesome-vsm-harness`;
- decide how contributors escalate a conflict spanning Index and Skills → `vsm-oss-organization`;
- change authority boundaries or shared contributor workflow across the in-scope repositories → `vsm-oss-organization`;
- propose changing the declared system boundary or ultimate policy authority → Organization S5 admission via `prompts/parent-control-plane.md`.

Public repositories such as `arctic-0`, `terminal-bench-vsm`, and `opensiro.com` are outside this bounded VSM Harness OSS system unless the canonical scope is explicitly changed. They are not subjects of this routing invariant.
