# VSM OSS Organization

# I'm human

Choose the way you want to enter this repository:

- **Repository web:** [opensiro/vsm-oss-organization](https://github.com/opensiro/vsm-oss-organization)
- **Independent repository statistics:** [Star History](https://www.star-history.com/#opensiro/vsm-oss-organization&Date)
- **How do I contribute?** [Contribute to OpenSiro with AI](CONTRIBUTE_WITH_AI.md)

You do not need to reconstruct the whole VSM/OSM organization before contributing. The human contribution guide gives you a copy-paste prompt that lets an AI agent discover the current public operating context and route the work correctly.

# I'm AI

Start from the current public [`START_HERE.md`](START_HERE.md). It is the machine-facing bootstrap contract for re-grounding in current GitHub state before routing into the owning repository and exact task artifact.

- For already tracked current work, use [`TODO.md`](TODO.md), then return to the linked owning repository/issue.
- For new, unclassified, cross-repository, or authority-sensitive work, use [`CONTRIBUTOR_START.md`](CONTRIBUTOR_START.md).
- Repository-local facts remain authoritative in their owning repository; this repository owns the bounded cross-repository organization/control construction.

A minimal organizational profile for autonomous OpenSiro OSS contributors.

This repository applies, but does not redefine, the public [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile). It is built bottom-up using an OSM-style elimination method: add an organizational function only when concrete residual variety cannot be absorbed by the functions already present.

> Cross-repository architecture, including the **experimental** `vsm-harness-capability` layer and future domain-specific capability repositories, is documented in [ECOSYSTEM.md](ECOSYSTEM.md). That note does not expand the current bounded organization or its operational S1 domains.

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

See [ORGANIZATION.md](ORGANIZATION.md) for the system boundary and viability criterion, [S1_DOMAIN_CONTRACTS.md](S1_DOMAIN_CONTRACTS.md) for the canonical local S1 envelopes, and [S1_AUTONOMY_COVERAGE.md](S1_AUTONOMY_COVERAGE.md) for operational evidence.

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

## Public outcome metrics

[`METRICS.md`](METRICS.md) defines the shared observability contract for these five public in-scope repositories, with a machine-readable projection in [`metrics.yaml`](metrics.yaml).

The rule is intentionally outcome-oriented: **count accepted repository-owned state transitions, not edits**. Commits, lines changed, PRs, issues, and workflow runs may be exposed as secondary engineering telemetry, but they are not productivity or verified-output KPIs.

## FOR CONTRIBUTORS

For **current tracked work across the bounded VSM Harness OSS group**, start with [`TODO.md`](TODO.md). It is the Git-native scheduler and owns only current selection/order through `NOW`, `NEXT`, and `BLOCKED`. The linked issue and repository remain authoritative for task scope, evidence, acceptance, and canonical artifacts.

The linked organization-level GitHub Project may remain available as an optional human visual projection, but it is not the canonical current-work source and is not required for autonomous correctness.

If you instead need to decide **where a new or unclassified piece of work belongs**, start with [CONTRIBUTOR_START.md](CONTRIBUTOR_START.md). This routing surface follows the declared scope above and does not expand it.

The work-lifecycle ownership map is defined once in [CONTROL_PLANE.md](CONTROL_PLANE.md): GitHub milestones own planned destinations, issues own durable work contracts, `TODO.md` owns current scheduling, and existing S1/metasystem contracts own admission, execution, escalation and closure.

You do not need to implement a VSM runtime to start contributing. Use the prompts as portable entry points with your own agent/runtime:

1. **New to the VSM Harness OSS group:** [prompts/learn-ecosystem.md](prompts/learn-ecosystem.md) — map repositories, authority boundaries, current milestone, and open work.
2. **Ready to work in an operational domain:** [prompts/contribute.md](prompts/contribute.md) — select Index, Skills, or Awesome, load its contract from `S1_DOMAIN_CONTRACTS.md`, and execute one bounded S1 contribution.
3. **Need the parent-governed identity/policy boundary:** [prompts/parent-control-plane.md](prompts/parent-control-plane.md) — apply the current S5 parent-authority, delegated-envelope, escalation, decision, and return contract. Ordinary approvals or tool permissions are not S5 by themselves.
4. **Using the M1 complementary-audit constructor:** [prompts/audit-s1-work.md](prompts/audit-s1-work.md) — exercise the first-party S3* path with a composed auditor; M1 does not require a permanent autonomous verifier.
5. **Applying a returned M1 current-control decision:** [prompts/apply-s3-control.md](prompts/apply-s3-control.md) — arbitrary comments/approvals are not treated as S3 input.

Repository-local contributions still belong in the repository that owns the relevant source of truth. Use this repository for organization-wide questions: contributor roles, authority boundaries, cross-repository control/coordination, escalation, milestone sequencing, shared current-work selection, and evolution of the shared contribution control plane.

The prompt pack and current-work routing surface are operational guidance/control surfaces, not additional VSM semantics and not evidence that a future milestone is complete.

## Source boundary

[`UPSTREAM_CONTRACT.json`](UPSTREAM_CONTRACT.json) is the single machine-readable selection of the upstream Profile, Methodology, and Index contract surfaces consumed by this organization.

- Normative VSM semantics remain owned by `opensiro/vsm-harness-profile`.
- Assessment procedure/autonomy publication conventions remain owned by `opensiro/vsm-harness-skills` under the selected source/provenance contract; local implementation work does not silently gain authority to redefine the Profile.
- Canonical assessment facts remain owned by `opensiro/vsm-harness-index`.
- Historical/frozen work keeps its original provenance; later compatible releases do not rewrite the contract under which an older artifact was produced.
- This repository operationalizes organization/control for the bounded OSS group; it does not redefine S1–S5.

See [CONTROL_PLANE.md](CONTROL_PLANE.md) for compatibility gates, frozen-work boundaries, cross-repository validation, merge gates, work-lifecycle ownership, and maintainer decision points.

## Contribution model

OpenSiro defines organizational roles and GitHub contribution boundaries. Contributors own their runtime:

```text
Organization TODO.md
        ↓
linked owning repository / issue
        ↓
contributor-owned scheduler / harness / credentials / budget
        ↓
select one S1 domain contract when applicable
        ↓
S1 role executes bounded local work
        ↓
Issue / Pull Request / no-change / escalation
```

A contributor may use one agent or many internal workers. Internal workers are not separate S1 units merely because they are separate processes or prompts.

Local variety should remain in the relevant operational domain when that domain has the requisite information and delegated authority. Only residual variety should move into later metasystem functions.

A scheduler state such as `BLOCKED` is not itself an algedonic signal or metasystem decision. Exceptional escalation remains governed by the selected Profile and the owning execution contract.

## OSM roadmap

Roadmap, work-contract, and live-scheduling state are intentionally separate:

- [`ROADMAP.md`](ROADMAP.md) owns the durable OSM milestone sequence, construction targets, and evidence-state narrative;
- the corresponding GitHub milestone/tracker issue owns the exact milestone exit contract and reviewable completion history;
- [`TODO.md`](TODO.md) owns only which already-existing issues are currently selected as `NOW`, `NEXT`, or `BLOCKED`.

The root README is therefore **not a live milestone-status or work-scheduling surface**. For current construction state, read `ROADMAP.md` and the applicable tracker; for current selected work, read `TODO.md` and then return to the linked owning issue/repository.

The roadmap is specific to this reference organization. Its target vectors are design/construction targets, not independently published assessment states, and `A`, `C`, and `P` are ownership arrangements rather than maturity scores. See [`ROADMAP.md`](ROADMAP.md) for the current milestone, evidence state, sequencing, and long-term reference target.

<!-- ROADMAP VALIDATOR PROJECTION:START
Derived compatibility projection for scripts/validate_contract.py. ROADMAP.md remains authoritative; this block is not a human-facing status or scheduling surface.

Active formal work is M1.

Current milestone target:

```text
S1  S2  S3  S3* S4  S5
A   —   C   C   —   —
```

Long-term reference target:

```text
S1  S2  S3  S3* S4  S5
A   A   A   C   A   P
```
ROADMAP VALIDATOR PROJECTION:END -->

## Construction roles

Role and constructor surfaces are introduced and interpreted under [`ROADMAP.md`](ROADMAP.md), the selected Profile, and their owning contracts. Their mere presence in this repository is not evidence that a milestone or autonomy state has been achieved.

The S1 construction uses [roles/S1.md](roles/S1.md) together with [S1_DOMAIN_CONTRACTS.md](S1_DOMAIN_CONTRACTS.md). A run must declare Index, Skills, or Awesome as its operational domain.

The complementary-audit constructor contract is defined in [S3STAR_AUDIT.md](S3STAR_AUDIT.md), with composition guidance in [roles/S3STAR.md](roles/S3STAR.md). The actual audit judgment owner is recorded per qualifying run rather than inferred from the existence of the role document.

The S3 current-control ownership contract is defined in [roles/S3.md](roles/S3.md). Its use, evidence status, and any later autonomous-agent mode are governed by the applicable roadmap milestone and contract rather than by README prose.

For the current milestone/evidence state, consult `ROADMAP.md` and its tracker. For selected executable work, consult `TODO.md`. Further roles are added only when concrete residual variety establishes the organizational need; VSM functions are responsibilities and relationships, not a checklist of permanent agent processes.

## Supplementary development evidence

The files under `supplementary/`, especially [supplementary/evolution-log.md](supplementary/evolution-log.md), preserve empirical development history and design reasoning.

They are **side artifacts of building and studying the organization, not primary operational products and not additional S1 domains**.

Their primary downstream purpose is an evidence-backed article/case study testing where applying VSM/OSM exposed organizational problems earlier, reduced rework/coordination cost, or otherwise improved development relative to plausible organically evolved alternatives — including negative cases where no such advantage is supported. A future pipeline may also derive reusable skills or methodology material, but that is a secondary planned use and not part of the current architecture.

See [supplementary/design-reasoning.md](supplementary/design-reasoning.md) for worked reasoning and [supplementary/evolution-log.md](supplementary/evolution-log.md) for the chronological development record.

## License

Repository code, prompts, configuration, and original documentation are licensed under the [Apache License 2.0](LICENSE). Third-party material, if added later, must retain its own stated license and attribution rather than being silently relicensed by this repository.
