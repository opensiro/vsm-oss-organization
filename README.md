# VSM OSS Organization

A minimal organizational profile for autonomous OpenSiro OSS contributors.

This repository applies, but does not redefine, the public [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile). It is built bottom-up using an OSM-style elimination method: add an organizational function only when concrete residual variety cannot be absorbed by the functions already present.

## Viable-system identity

The bounded organization maintained here exists to keep public, current, evidence-backed VSM Harness knowledge available to the open-source community.

The current system separates a normative/metasystem plane from three operational S1 domains:

```text
normative / metasystem plane
├── vsm-harness-profile      authoritative semantics
└── vsm-oss-organization     organizational/control construction

operational S1 plane
├── vsm-harness-index
├── vsm-harness-skills
└── awesome-vsm-harness
```

The operational domains produce different durable outcomes:

- **Index** — canonical evidence-backed corpus, provenance, reassessment history, signatures, and deterministic comparative views;
- **Skills** — reusable VSM Harness assessment procedure/skills/tooling that applies the selected Profile;
- **Awesome** — curated representative downstream view linked to canonical Index facts.

See [ORGANIZATION.md](ORGANIZATION.md) for the system boundary and viability criterion, [S1_DOMAIN_CONTRACTS.md](S1_DOMAIN_CONTRACTS.md) for the canonical local S1 envelopes, and [S1_AUTONOMY_COVERAGE.md](S1_AUTONOMY_COVERAGE.md) for operational evidence and the remaining autonomy-proof boundary.

## Scope

This repository is the organizational/control plane for a bounded **OpenSiro VSM Harness OSS group**. It is not a control plane for every OpenSiro project, account, research track, or private R&D activity.

Current in-scope public repositories:

- `opensiro/vsm-harness-profile`
- `opensiro/vsm-harness-skills`
- `opensiro/vsm-harness-index`
- `opensiro/awesome-vsm-harness`
- `opensiro/vsm-oss-organization`

Scope membership does not mean that all five repositories are operational S1 units. For the current system-in-focus:

- `vsm-harness-index`, `vsm-harness-skills`, and `awesome-vsm-harness` are the declared operational S1 domains;
- `vsm-harness-profile` is the normative semantic authority consumed by the organization;
- `vsm-oss-organization` is the organizational/metasystem construction surface.

Repository location alone does not determine function. In particular, `vsm-harness-skills` may host general-purpose skills outside this viable-system boundary, and a change inside an operational repository may still leave S1 if it actually changes normative, cross-S1, identity, or metasystem authority.

Repositories outside the current in-scope set may consume or present artifacts produced here without becoming governed by this control plane.

## FOR CONTRIBUTORS

You do not need to implement a VSM runtime to start contributing. Use the prompts as portable entry points with your own agent/runtime:

1. **New to the VSM Harness OSS group:** [prompts/learn-ecosystem.md](prompts/learn-ecosystem.md) — map repositories, authority boundaries, current milestone, and open work.
2. **Ready to work in an operational domain:** [prompts/contribute.md](prompts/contribute.md) — select Index, Skills, or Awesome, load its contract from `S1_DOMAIN_CONTRACTS.md`, and execute one bounded S1 contribution.
3. **Want an explicit control plane now:** [prompts/parent-control-plane.md](prompts/parent-control-plane.md) — demo a human-parent autonomy envelope ahead of the full M2 implementation.
4. **Preparing complementary M1 audit work:** [prompts/audit-s1-work.md](prompts/audit-s1-work.md) — preparatory only; its existence is not evidence that M1 or `S3*=A` is established.
5. **Applying a returned preparatory M1 current-control decision:** [prompts/apply-s3-control.md](prompts/apply-s3-control.md) — preparatory only; arbitrary comments/approvals are not treated as S3 input.

The prompt pack is operational guidance, not additional VSM semantics and not evidence that a future milestone is complete.

## Source boundary

[`UPSTREAM_CONTRACT.json`](UPSTREAM_CONTRACT.json) is the single machine-readable selection of the upstream Profile, Methodology, and Index contract surfaces consumed by this organization.

- Normative VSM semantics remain owned by `opensiro/vsm-harness-profile`.
- Assessment procedure/autonomy publication conventions remain owned by `opensiro/vsm-harness-skills` under the selected source/provenance contract; local implementation work does not silently gain authority to redefine the Profile.
- Canonical assessment facts remain owned by `opensiro/vsm-harness-index`.
- Historical/frozen work keeps its original provenance; later compatible releases do not rewrite the contract under which an older artifact was produced.
- This repository operationalizes organization/control for the bounded OSS group; it does not redefine S1–S5.

See [CONTROL_PLANE.md](CONTROL_PLANE.md) for compatibility gates, frozen-work boundaries, cross-repository validation, merge gates, and maintainer decision points.

## Contribution model

OpenSiro defines organizational roles and GitHub contribution boundaries. Contributors own their runtime:

```text
OpenSiro contribution contract
        ↓
contributor-owned scheduler / harness / credentials / budget
        ↓
select one S1 domain contract
        ↓
S1 role executes bounded local work
        ↓
Issue / Pull Request / no-change / escalation
```

A contributor may use one agent or many internal workers. Internal workers are not separate S1 units merely because they are separate processes or prompts.

Local variety should remain in the relevant operational domain when that domain has the requisite information and delegated authority. Only residual variety should move into later metasystem functions.

## OSM roadmap

M0 operational construction is complete: Index, Skills, and Awesome now have explicit local envelopes and real operational evidence paths.

Current milestone target:

```text
S1  S2  S3  S3* S4  S5
A   —   —   —   —   —
```

The vector is a **design/construction target, not an independently proven autonomy-state publication**. Repository attribution still does not independently prove the autonomous executor owned every decisive local S1 choice; that actor-attribution proof debt is explicitly deferred to Parent-assisted work in #35 / M2.

Long-term reference target:

```text
S1  S2  S3  S3* S4  S5
A   A   A   A   A   P
```

`A`, `C`, and `P` are ownership arrangements, not maturity scores. The milestone ordering is specific to this reference organization, not a universal VSM installation order. See [ROADMAP.md](ROADMAP.md).

## Current and preparatory roles

The M0 S1 construction uses [roles/S1.md](roles/S1.md) together with [S1_DOMAIN_CONTRACTS.md](S1_DOMAIN_CONTRACTS.md). A run must declare Index, Skills, or Awesome as its operational domain.

Preparatory M1 artifacts may exist before that milestone is formally achieved. The current S3* audit role and S3 constructor surface remain preparatory; their presence does not establish `S3*=A`, `S3=C`, or an autonomous S3 regulator.

Further roles are added only when concrete residual variety establishes the organizational need. VSM functions are responsibilities and relationships, not a checklist of permanent agent processes.

## Supplementary development evidence

The files under `supplementary/`, especially [supplementary/evolution-log.md](supplementary/evolution-log.md), preserve empirical development history and design reasoning.

They are **side artifacts of building and studying the organization, not primary operational products and not additional S1 domains**.

Their primary downstream purpose is an evidence-backed article/case study testing where applying VSM/OSM exposed organizational problems earlier, reduced rework/coordination cost, or otherwise improved development relative to plausible organically evolved alternatives — including negative cases where no such advantage is supported. A future pipeline may also derive reusable skills or methodology material, but that is a secondary planned use and not part of the current architecture.

See [supplementary/design-reasoning.md](supplementary/design-reasoning.md) for worked reasoning and [supplementary/evolution-log.md](supplementary/evolution-log.md) for the chronological development record.