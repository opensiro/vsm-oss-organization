# OpenSiro public contributor routing

This file is the common entry point for contributors and agents that arrive through any public OpenSiro repository and need to determine where work belongs.

## Routing rule

**Repository-local work stays in the repository that owns the relevant source of truth.**

Use `opensiro/vsm-oss-organization` when the question is organization-wide: contributor roles, authority boundaries, escalation, cross-repository coordination, milestone sequencing, or evolution of the shared public contribution control plane.

Routing here does **not** make every public OpenSiro repository part of one VSM system. The formal VSM Harness system boundary remains defined by this repository's `README.md`, `ORGANIZATION.md`, and `S1_DOMAIN_CONTRACTS.md`.

## Public repository map

| Repository | Repository-local responsibility | Relationship to this control plane |
| --- | --- | --- |
| `opensiro/vsm-harness-profile` | Normative VSM Harness semantics | In-scope normative authority; local semantic changes stay in Profile |
| `opensiro/vsm-harness-skills` | Assessment methodology, skills, validation tooling | In-scope operational domain; local procedure changes stay in Skills |
| `opensiro/vsm-harness-index` | Evidence-backed assessments, catalog/provenance, generated views | In-scope operational domain; local assessment work stays in Index |
| `opensiro/awesome-vsm-harness` | Curated downstream organizational examples | In-scope operational domain; local curation stays in Awesome |
| `opensiro/vsm-oss-organization` | Contributor roles, authority, escalation, cross-repository control and organizational evolution | Common public routing/control entry point |
| `opensiro/terminal-bench-vsm` | Experimental failure-aware coding harness and evaluation/growth environment | Separate experimental track; not part of the VSM Harness S1 plane. Its current license is TBD, so public availability must not be confused with an open-source license |
| `opensiro/arctic-0` | ARCTIC archive, schemas, taxonomy and released tooling | Separate research track; ARCTIC facts remain owned by ARCTIC |
| `opensiro/opensiro.com` | Presentation layer and website implementation | Presentation layer; canonical product/research facts stay in their owning repositories |

Private OpenSiro repositories and private R&D are outside this public routing surface.

## Agent decision procedure

When starting from an arbitrary public OpenSiro repository:

1. Read that repository's README and identify its local source-of-truth responsibility.
2. If the requested change is local to that responsibility, stay in that repository.
3. If the requested change concerns contributor authority, escalation, multiple repositories, milestone sequencing, or the shared contribution control plane, continue here.
4. From here, route domain-specific work back to the owning repository rather than duplicating its facts or semantics.

Examples:

- change the definition of S3* → `vsm-harness-profile`;
- reassess one harness → `vsm-harness-index`;
- change ARCTIC archive/schema/tooling → `arctic-0`;
- change website presentation → `opensiro.com`;
- decide how contributors escalate a conflict spanning Index and Skills → `vsm-oss-organization`;
- change authority boundaries or shared contributor workflow across repositories → `vsm-oss-organization`.
