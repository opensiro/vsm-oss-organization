# VSM OSS Organization

A minimal organizational profile for autonomous OpenSiro OSS contributors.

This repository applies, but does not redefine, the public [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile). It is built bottom-up using an OSM-style elimination method: add an organizational function only when a concrete variety or disturbance cannot be absorbed by the functions already present.

## Viable-system identity

The bounded organization maintained here exists to keep a public, current, evidence-backed representation of the organizational structure of AI-agent harnesses available to the open-source community through VSM.

Its primary transformation is:

```text
public harness ecosystem evidence
        ↓
VSM semantics + assessment methodology
        ↓
evidence-backed assessments
        ↓
normalized comparative knowledge
        ↓
curated public views for the OSS community
```

See [ORGANIZATION.md](ORGANIZATION.md) for the system identity, operational work domain, repository participation boundary, and viability criterion. See [S1_AUTONOMY_COVERAGE.md](S1_AUTONOMY_COVERAGE.md) for the current operational work classes and the engineering gaps that still block broad S1 autonomy.

## Scope

This repository is the organizational/control plane for a bounded **OpenSiro VSM Harness OSS group**. It is not a control plane for every OpenSiro project, account, research track, or private R&D activity.

Current in-scope public repositories:

- `opensiro/vsm-harness-profile`
- `opensiro/vsm-harness-skills`
- `opensiro/vsm-harness-index`
- `opensiro/awesome-vsm-harness`
- `opensiro/vsm-oss-organization`

The repositories remain separate systems with separate sources of truth. Inclusion here means their **public OSS contribution work that participates in the declared VSM Harness knowledge transformation** may be organized through this contributor/control plane; it does not transfer semantic ownership between repositories.

`opensiro/vsm-harness-skills` is intentionally only partially inside this viable-system boundary. The repository may host reusable skills for more general tasks and for other systems. This control plane governs only those skills/procedures whose work participates in producing or maintaining VSM Harness knowledge; repository location alone does not make every skill part of this organization.

Repositories outside the declared current in-scope set may still consume, demonstrate, experiment with, or present artifacts produced by the in-scope repositories. That dependency alone does not place them under this control plane.

Scope changes are explicit; organization membership, repository naming, or dependency alone is not enough to place work under this control plane.

## FOR CONTRIBUTORS

You do not need to implement a VSM runtime to start contributing. Use the prompts as portable entry points with your own agent/runtime:

1. **New to the VSM Harness OSS group:** [prompts/learn-ecosystem.md](prompts/learn-ecosystem.md) — map the in-scope repositories, authority boundaries, current milestone, and open work before changing anything.
2. **Ready to work:** [prompts/contribute.md](prompts/contribute.md) — execute one bounded contribution under the current S1-first contract.
3. **Want an explicit control plane now:** [prompts/parent-control-plane.md](prompts/parent-control-plane.md) — demo a human-parent autonomy envelope and escalation interface ahead of the full M2 implementation.
4. **Preparing complementary M1 audit work:** [prompts/audit-s1-work.md](prompts/audit-s1-work.md) — challenge one explicit S1 claim through a materially complementary evidence path. This is a preparatory M1 entry point, not a claim that M1 or `S3*=A` is already established.

The prompt pack is operational guidance, not additional VSM semantics and not evidence that a future roadmap milestone is already complete.

## Source boundary

[`UPSTREAM_CONTRACT.json`](UPSTREAM_CONTRACT.json) is the single machine-readable selection of the upstream Profile, Methodology, and Index contract surfaces consumed by this organization.

- Normative VSM semantics remain owned by `opensiro/vsm-harness-profile`; this repository consumes the selected released Profile and its downstream compatibility facade rather than copying S1–S5 definitions.
- Autonomy notation and assessment procedure remain owned by `opensiro/vsm-harness-skills`; the selected Methodology revision is pinned in the manifest with its actual source status.
- The current assessment-contract pair remains owned by `opensiro/vsm-harness-index`; Organization validation reads that upstream contract and checks whether the selected Profile is compatible through the Profile release-impact chain.
- Historical or frozen work keeps its original provenance. A later compatible Profile release does not rewrite the Profile version under which an older assessment or trial was produced.
- This repository is a local operationalization for the in-scope OpenSiro VSM Harness OSS group. It does not redefine S1-S5.

See [CONTROL_PLANE.md](CONTROL_PLANE.md) for the compatibility gate, frozen-work boundary, cross-repository validation model, merge gates, and maintainer decision points. Open semantic proposals are never treated as accepted Profile rules.

## Contribution model

OpenSiro defines organizational roles and GitHub contribution boundaries. Contributors own their runtime:

```text
OpenSiro contribution contract
        ↓
contributor-owned scheduler / harness / credentials / budget
        ↓
VSM role prompt(s)
        ↓
autonomous contribution
        ↓
Issue / Pull Request
```

A contributor may use one agent or many internal workers. Internal workers are not separate S1 units merely because they are separate processes or prompts. The current minimal system-in-focus is one bounded contribution loop with one operational outcome.

## OSM roadmap

The implementation starts from the smallest useful organization and introduces functions only when their disturbance appears.

Current milestone target:

```text
S1  S2  S3  S3* S4  S5
A   —   —   —   —   —
```

This is the M0 **target**, not a current evidence claim. The current strict M0 status is tracked in issue #2; M0 remains open until `S1=A` is established from sufficient primary evidence.

Long-term reference target:

```text
S1  S2  S3  S3* S4  S5
A   A   A   A   A   P
```

The final vector is a design target, not a present assessment claim. `A`, `C`, and `P` are ownership arrangements, not maturity scores; the milestone ordering is the construction sequence for this reference organization rather than a universal VSM installation order. Each milestone has explicit entry and exit conditions in [ROADMAP.md](ROADMAP.md).

## Current and preparatory roles

The only role active in the current M0 milestone is S1: [roles/S1.md](roles/S1.md).

Preparatory M1 work may define future role artifacts before the milestone is formally achieved. The current preparatory S3* audit role is [roles/S3STAR.md](roles/S3STAR.md), governed by [S3STAR_AUDIT.md](S3STAR_AUDIT.md). Its presence does **not** establish `S3*=A`, activate M1, or imply an autonomous S3 regulator.

Further roles are added only when the roadmap establishes a concrete organizational need for them. This is deliberate: VSM functions are organizational responsibilities, not a checklist of permanent agent processes.

## Design rationale

See [supplementary/design-reasoning.md](supplementary/design-reasoning.md) for worked examples from the design discussion, including reasoning that survived re-check and reasoning that was rejected or narrowed after applying the current Profile.
