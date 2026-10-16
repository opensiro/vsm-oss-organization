# VSM OSS Organization

This `README.md` is the common entry point for people and AI runtimes into the bounded OpenSiro VSM Harness OSS organization.

## I'm human

- **Web overview:** [opensiro.com](https://opensiro.com)
- **Public outcome metrics:** [`docs/METRICS.md`](docs/METRICS.md)
- **Contribute with AI:** [`CONTRIBUTE_WITH_AI.md`](CONTRIBUTE_WITH_AI.md)
- **Manage OSS through one agent:** [`docs/AGENT_CONTROL_PLANE.md`](docs/AGENT_CONTROL_PLANE.md)
- **Full documentation index:** [`docs/README.md`](docs/README.md)

## I'm AI

Start with [`START_HERE.md`](START_HERE.md). It is the canonical machine bootstrap for re-grounding in current public GitHub state.

- already tracked current work → [`TODO.md`](TODO.md), then return to the linked owning issue/repository;
- new, unclassified, cross-repository, or authority-sensitive work → [`CONTRIBUTOR_START.md`](CONTRIBUTOR_START.md);
- cross-repository architecture → [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md).

Repository-local facts remain authoritative in their owning repository. This repository owns only the bounded cross-repository organization/control construction.

## Scope

Current in-scope public repositories:

- `opensiro/vsm-harness-profile`
- `opensiro/vsm-harness-skills`
- `opensiro/vsm-harness-index`
- `opensiro/awesome-vsm-harness`
- `opensiro/vsm-oss-organization`

The operational S1 domains are Index, Skills, and Awesome. Profile is the normative semantic authority consumed by the organization. Organization is the metasystem/control-construction surface.

See [`docs/ORGANIZATION.md`](docs/ORGANIZATION.md) for the system boundary and viability criterion.

## Source boundary

[`UPSTREAM_CONTRACT.json`](UPSTREAM_CONTRACT.json) is the single machine-readable selection of the upstream Profile, Methodology, and Index contract surfaces consumed by this organization.

- Profile owns normative VSM semantics.
- Skills owns assessment procedure and methodology.
- Index owns canonical assessment facts.
- Historical/frozen work keeps its original provenance.
- Organization does not redefine S1–S5.

See [`docs/CONTROL_PLANE.md`](docs/CONTROL_PLANE.md) for compatibility gates, work-lifecycle ownership, merge gates, and maintainer decision points.

## Current construction

Planning, work contracts, and current scheduling are separate:

- **GitHub milestones + their tracker issues** own planned destination and exact exit contracts;
- [`docs/ROADMAP.md`](docs/ROADMAP.md) is the readable construction/evidence projection;
- [`TODO.md`](TODO.md) is the **Git-native scheduler** for selected `NOW` / `NEXT` / `BLOCKED` issues only.

**M0–M2 completed their Organization-local construction/assessment milestones.** M2 closure is evidenced in the [source-first parent-return revalidation](docs/reviews/2026-10-15-m2-s5-parent-source-revalidation.md). The `A — C C — P` M2 vector is a local milestone target/outcome, not a new canonical Index general assessment.

Active formal work is M3 — **the next formal construction milestone, not a completed autonomy claim**. First-party D1-A v1 reference code is **source-prepared but inactive**: the [agent-owned decision/return mode](modes/s3-autonomous/RUN.md) composes model selection, authority and S1-source checks, bounded delivery, and subsequent feedback, but its [machine-readable grant](contracts/s3/autonomous-d1a.json) remains `PENDING_S5_PUBLIC_ATTESTATION`. In particular, no independently attributable S5 issuance, concrete authorized agent execution identity, effective term, or positive first-party `S3=A` ownership/closure assessment has been established. **M3 [#5](https://github.com/opensiro/vsm-oss-organization/issues/5) remains open and `S3=A` remains unproven**; the previously supported Organization-local `S3=C` result is unchanged.

**OSS runtime boundary:** OpenSiro provides open contracts, reference code and integration interfaces; an OpenSiro-hosted S3 worker, bot or persistent runtime is **not required** for M3 source-first assessment. Consumers may bring their own runtime. That removes a deployment prerequisite, **not** the need for an effective S5 grant, genuinely agent-owned decisions, and a source-supported S3-to-S1 return path. No synthetic S3 intervention or independent-reviewer deployment is required merely to upgrade a label. See [M3 scope clarification](docs/AGENT_CONTROL_PLANE.md#m3-d1-a-autonomous-s3-source-prepared-not-active) and [merged PR #270](https://github.com/opensiro/vsm-oss-organization/pull/270).

This M3 roadmap selection does **not** add work automatically to `TODO.md`; the shared scheduler still admits only explicitly listed NOW/NEXT/BLOCKED items.

Milestone/evidence distinction:

| Phase | Current Organization-local evidence | Not implied |
| --- | --- | --- |
| M0–M2 | Local S1 autonomy, S3/S3* constructor qualification at `C`, and parent-governed S5 at `P` | A new canonical Index assessment |
| M3 | D1-A code and tests prepared; agent grant remains pending | Effective autonomous S3 or `S3=A` |
| M4–M5 | Planned S2/S4 construction | Demonstrated S2/S4 autonomy |

Current milestone target:

```text
S1  S2  S3  S3* S4  S5
A   —   A   C   —   P
```

Long-term reference target:

```text
S1  S2  S3  S3* S4  S5
A   A   A   C   A   P
```

These are construction targets for this reference organization, not a universal maturity ladder or independently published assessment state.

## Operating surfaces

- S1 domain envelopes: [`contracts/s1/domain-contracts.md`](contracts/s1/domain-contracts.md)
- S1 admission/recovery: [`contracts/s1/task-admission-recovery.md`](contracts/s1/task-admission-recovery.md)
- S1 operational evidence: [`records/s1/autonomy-coverage.md`](records/s1/autonomy-coverage.md)
- supported autonomous S1 mode: [`modes/s1-autonomous/`](modes/s1-autonomous/)
- S3 current control: [`contracts/s3/current-control.md`](contracts/s3/current-control.md)
- S3* complementary audit: [`contracts/s3star/audit.md`](contracts/s3star/audit.md)
- S5 parent boundary and authority: [`contracts/s5/`](contracts/s5/)
- external-tool admission: [`contracts/tools/external-entry.md`](contracts/tools/external-entry.md)
- autonomous work reporting: [`docs/AUTONOMOUS_WORK_REPORTING.md`](docs/AUTONOMOUS_WORK_REPORTING.md)
- routing conformance: [`docs/ROUTING_CONFORMANCE.md`](docs/ROUTING_CONFORMANCE.md)
- fresh contributor conformance: [`docs/CONTRIBUTOR_CONFORMANCE.md`](docs/CONTRIBUTOR_CONFORMANCE.md)

Contracts and role files are construction surfaces, not positive function evidence by file presence alone.

## Repository layout

The root is intentionally limited to entry/control surfaces. Long-form documentation belongs under [`docs/`](docs/README.md); organizational contracts under [`contracts/`](contracts/README.md); actor adapters under `roles/`; concrete evidence under `records/`; prompts under `prompts/`; schemas under `schemas/`; tests under `tests/`.

## License

Repository code, prompts, configuration, and original documentation are licensed under the [Apache License 2.0](LICENSE).
