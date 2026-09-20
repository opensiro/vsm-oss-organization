# VSM Harness OSS contributor routing

This file is the common entry point for contributors and agents that arrive through one of the repositories in the bounded **OpenSiro VSM Harness OSS group** and need to determine where work belongs.

The canonical membership of that group is the `Current in-scope public repositories:` block in [README.md](README.md). This file does not expand that set.

## New to OpenSiro?

For a plain-language and visual introduction to why this work exists, start with **[opensiro.com](https://opensiro.com)** and the **[VSMLite / VSM poster](https://opensiro.com/vsm.html)**. The poster introduces the harness-normalization problem and the organizational relationships that motivate the VSM coordinate system.

This orientation is optional and non-normative. `opensiro.com` is a presentation layer outside the bounded VSM Harness OSS system. Return to the owning GitHub repositories for canonical semantics, assessment procedure, evidence-backed findings, contributor authority, and work acceptance.

## Routing rule

**Repository-local work stays in the repository that owns the relevant source of truth.**

Use `opensiro/vsm-oss-organization` when the question is organization-wide within the declared VSM Harness OSS group: contributor roles, authority boundaries, escalation, cross-repository coordination, milestone sequencing, or evolution of the shared contribution control plane.

Repositories and research tracks outside the declared scope are not governed by this routing contract merely because they are public or live under the `opensiro` organization.

## Autonomous contributor observability

Autonomous contributors should keep the project owner able to recover the current state without following every intermediate action. The default run boundary and owner-facing snapshot contract are defined in [`CONTRIBUTING.md`](CONTRIBUTING.md), under **Autonomous progress and owner observability**.

In short, complete the requested work, finish any already-started atomic delivery chain, take no more than one or two directly implied downstream steps by default, then report:

```text
DONE
NOW
BLOCKED
NEXT
NEED YOU
```

`NEED YOU` should be `none` when no real owner decision is required. This is a contributor observability convention, not evidence of any VSM function or autonomy state.

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

Every repository in the canonical in-scope set must expose this routing boundary directly from its root README, making both outcomes clear:

- repository-local work remains in the repository that owns the source of truth;
- organization-wide contributor roles, authority, escalation, cross-repository coordination, milestone sequencing, or organizational evolution route to `opensiro/vsm-oss-organization` / this contributor entry point.

Equivalent wording is allowed when a repository needs to preserve a domain-specific boundary, but the route itself must remain directly discoverable from the repository root.

See [ROUTING_CONFORMANCE.md](ROUTING_CONFORMANCE.md) for the scoped cross-repository oracle, evidence boundary, and blind-agent trial protocol.

## In-scope repository map

| Repository | Repository-local responsibility | Relationship to this control plane |
| --- | --- | --- |
| `opensiro/vsm-harness-profile` | Normative VSM Harness semantics | In-scope normative authority; local semantic changes stay in Profile |
| `opensiro/vsm-harness-skills` | Assessment methodology, skills, validation tooling | In-scope operational domain; local procedure changes stay in Skills |
| `opensiro/vsm-harness-index` | Evidence-backed assessments, catalog/provenance, generated views | In-scope operational domain; local assessment work stays in Index |
| `opensiro/awesome-vsm-harness` | Curated downstream organizational examples | In-scope operational domain; local curation stays in Awesome |
| `opensiro/vsm-oss-organization` | Contributor roles, authority, escalation, cross-repository control and organizational evolution | Organizational/metasystem construction surface and routing entry point |

The table above is explanatory. Canonical membership remains the README scope block and is mechanically checked against the Organization contracts.

## Agent decision procedure

When starting from an in-scope repository:

1. Read that repository's README and identify its local source-of-truth responsibility.
2. If the requested change is local to that responsibility, stay in that repository.
3. If the requested change concerns contributor authority, escalation, multiple in-scope repositories, milestone sequencing, or the shared contribution control plane, continue here.
4. From here, route domain-specific work back to the owning repository rather than duplicating its facts or semantics.
5. If the unresolved question is specifically about identity, ultimate policy, system boundary, legitimate authority, or the delegated autonomy envelope, use the parent-governed S5 entry above; otherwise do not invoke S5.

Examples:

- change the definition of S3* → `vsm-harness-profile`;
- change the assessment procedure → `vsm-harness-skills`;
- reassess one harness → `vsm-harness-index`;
- change Awesome curation → `awesome-vsm-harness`;
- decide how contributors escalate a conflict spanning Index and Skills → `vsm-oss-organization`;
- change authority boundaries or shared contributor workflow across the in-scope repositories → `vsm-oss-organization`;
- propose changing the declared system boundary or ultimate policy authority → Organization S5 admission via `prompts/parent-control-plane.md`.

Public repositories such as `arctic-0`, `terminal-bench-vsm`, and `opensiro.com` are outside this bounded VSM Harness OSS system unless the canonical scope is explicitly changed. They are not subjects of this routing invariant.
