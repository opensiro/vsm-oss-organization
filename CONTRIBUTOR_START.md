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

Examples:

- change the definition of S3* → `vsm-harness-profile`;
- change the assessment procedure → `vsm-harness-skills`;
- reassess one harness → `vsm-harness-index`;
- change Awesome curation → `awesome-vsm-harness`;
- decide how contributors escalate a conflict spanning Index and Skills → `vsm-oss-organization`;
- change authority boundaries or shared contributor workflow across the in-scope repositories → `vsm-oss-organization`.

Public repositories such as `arctic-0`, `terminal-bench-vsm`, and `opensiro.com` are outside this bounded VSM Harness OSS system unless the canonical scope is explicitly changed. They are not subjects of this routing invariant.
