# Empirical OSS harness case studies

This directory contains comparative empirical artifacts for the `vsm-oss-organization` supplementary empirical track.

Parent workstream: [#30](https://github.com/opensiro/vsm-oss-organization/issues/30).

Case-study tasks:

- first case: [#31](https://github.com/opensiro/vsm-oss-organization/issues/31);
- second case: [#88](https://github.com/opensiro/vsm-oss-organization/issues/88);
- third case: [#98](https://github.com/opensiro/vsm-oss-organization/issues/98);
- fourth case: [#102](https://github.com/opensiro/vsm-oss-organization/issues/102);
- cross-case schema: [#90](https://github.com/opensiro/vsm-oss-organization/issues/90), implemented and later revised in [`COMPARISON_SCHEMA.md`](COMPARISON_SCHEMA.md);
- first bounded three-case synthesis: [#100](https://github.com/opensiro/vsm-oss-organization/issues/100), implemented in [`CROSS_CASE_SYNTHESIS.md`](CROSS_CASE_SYNTHESIS.md);
- second bounded four-case synthesis: [#104](https://github.com/opensiro/vsm-oss-organization/issues/104), implemented in [`CROSS_CASE_SYNTHESIS_V2.md`](CROSS_CASE_SYNTHESIS_V2.md).

These documents are **not VSM Harness Index assessments** and are not a second assessment database. Their purpose is to reconstruct how real OSS harness organizations changed over time so the practical significance of VSM/OSM construction ideas can be tested against independent history.

## Cases

- [`autogen.md`](autogen.md) — AutoGen multimodal coordination pressure, roadmap/epic consolidation, partial repairs, and the later `v0.4` architectural boundary. The case intentionally leaves decisive S2/S4 ownership and causal development-cost claims unproven where the public evidence does not establish them.
- [`openhands-runtime.md`](openhands-runtime.md) — OpenDevin/OpenHands runtime migration from SSH-coupled execution toward EventStreamRuntime, including partial compatibility work, parallel replacement implementation, integration/evaluation gates, preserved validation gaps, and final retirement/default switch. The case does not infer S3/S3*/S4 ownership from runtime, testing, or maintainer vocabulary.
- [`langgraph-interrupt-coordination.md`](langgraph-interrupt-coordination.md) — LangGraph parallel interrupt/resume evolution from ambiguous shared feedback toward explicit interrupt identity, ID-mapped resumes, and rejection of ambiguous scalar feedback, with a later nested-subgraph counterexample showing incomplete recursive coverage. The case treats this as coordination/requisite-variety evidence without inferring S2 autonomy or decision ownership.
- [`pydanticai-prioritization.md`](pydanticai-prioritization.md) — PydanticAI issue/PR overload and the shift from interruption-heavy review toward explicit maintainer-owned prioritization, admission and human review, with `AGENTS.md`, triage/review automation and contributor/champion input kept separate as support. The case provides stronger public decision-owner evidence than the first three without assigning an S3 autonomy state.

## Cross-case synthesis

[`CROSS_CASE_SYNTHESIS.md`](CROSS_CASE_SYNTHESIS.md) is the frozen first synthesis across AutoGen, OpenHands, and LangGraph.

[`CROSS_CASE_SYNTHESIS_V2.md`](CROSS_CASE_SYNTHESIS_V2.md) is the explicit second synthesis that adds PydanticAI without rewriting the provenance of the original three-case snapshot. Its purpose is to retest provisional recurring observations against a deliberately different owner-evidence shape.

The syntheses are deliberately bounded. They separate:

- observations recurring across multiple cases;
- case-specific mechanisms;
- article-safe descriptive claims;
- hypotheses that still require comparison against OpenSiro's own evolution log;
- claims that remain unsupported, including any quantitative VSM development-cost advantage.

The third case triggered an explicit schema revision: `COMPARISON_SCHEMA.md` now records `recursion_boundary_evidence` when a mechanism/invariant depends on distinctions crossing a parent/child recursive boundary. Earlier cases are not retrofitted by analogy; `NOT_APPLICABLE` remains valid when recursion is not material to the reconstructed transition.

The fourth case did **not** require another schema field. Instead, the second synthesis shows two useful calibration results: the local-repair-before-broader-response pattern remains specific to the first three reviewed technical-transition cases, and the earlier mechanism-stronger-than-owner pattern is not a general rule because PydanticAI supplies materially stronger positive owner evidence.

## Research question

For each case, ask:

> Does the VSM/OSM construction method help explain, anticipate, or reduce organizational problems that an OSS harness project encountered while evolving without that explicit method?

A case is useful when it can provide evidence **for or against** that proposition.

## Selection criteria

Prefer projects with:

- a real public AI-agent harness/framework/runtime/control-plane role;
- substantial development history;
- many independent contributors; 100+ contributors is especially valuable when available but is not a hard inclusion threshold;
- primary historical evidence in issues, PRs, commits, RFCs/design docs, release history, CI, contributor/governance documentation, and maintainer discussions;
- at least one reconstructable organizational disturbance and a later response/mechanism.

Do not select a project because its terminology resembles VSM.

## Evidence boundary

Use primary repository evidence wherever practical.

Separate three layers explicitly:

```text
project fact
→ our reconstruction of the organizational problem
→ VSM interpretation
```

Do not collapse them.

For every material claim:

- record dates or pinned revisions when useful;
- distinguish contemporaneous project explanations from retrospective interpretation;
- preserve uncertainty and plausible alternative explanations;
- record missing or contradictory evidence;
- do not infer decision ownership/autonomy from the existence of a tool, role, feature, queue, reviewer, manager, verifier, planner, or governance document;
- map the organizational function first and classify ownership only when evidence establishes the decisive right and its owner;
- when recursion is material, establish the relation at the declared boundary rather than assuming parent/child transfer.

## Recommended case structure

```md
# <Project> organizational evolution case study

## Scope
- repository / repositories
- historical interval
- why this is a useful case
- evidence sources reviewed

## Baseline organization
What can be established about the relevant system boundary before the observed transitions.

## Timeline

| Period | Observed condition/disturbance | Primary evidence | Response/mechanism | Observed consequence | VSM interpretation | Confidence/alternatives |
| --- | --- | --- | --- | --- | --- | --- |

## Detailed transitions

### <transition>

#### Observed facts
What happened, using project-native language.

#### Organizational reconstruction
What concrete interference, control problem, audit problem, adaptation problem, policy question, or other organizational need can actually be established.

#### Response
What mechanism/process/role was introduced or changed.

#### Consequence
What later evidence shows about the effect. Do not assume success from adoption alone.

#### VSM interpretation
Only after the above evidence is established.

#### Alternative explanations / uncertainty
What else could explain the sequence and what evidence is missing.

## Empirical significance for the construction method

### What VSM distinguished usefully
Where a functional distinction appears to explain the history better than implementation vocabulary alone.

### Possible anticipatory value
Whether the OpenSiro elimination method could have produced a falsifiable earlier signal before the eventual mechanism emerged.

### Observable cost before regulation
Rework, conflict, repeated incidents, queueing, maintainer bottlenecks, regressions, or other evidence. Do not invent quantitative cost when the project does not expose it.

### Where the VSM framing was weak or unnecessary
Important evidence that does not fit well, adds little explanatory value, or suggests the method should be narrowed.

## Comparison hooks
Facts that can later be compared across multiple case studies without forcing a ranking.

## References
Stable primary links and pinned revisions.
```

## Comparative dimensions

Useful dimensions include, when evidence exists:

| Organizational phenomenon | Evidence to look for |
| --- | --- |
| Inter-operation interference | duplicate work, conflicting changes, incompatible interfaces, repeated coordination failures |
| Coordination response | ownership/claiming, reservation, scheduling, serialization, negotiation, collision avoidance |
| Current control | priority/resource/commitment decisions across active work, exception handling, intervention paths |
| Independent access/audit | checks based on evidence not controlled solely by the producing operation |
| External/future adaptation | explicit environment/future sensing, adaptation options, two-way relation with current capability |
| Identity/policy authority | legitimate ultimate-policy decisions, escalation, delegated authority boundaries |
| Decision provenance | evidence establishing who actually owned decisive organizational choices |
| Recursion / boundary preservation | whether a relation established at one recursion still has enough information/variety at a parent or child boundary |

These dimensions are prompts for evidence collection, not a checklist requiring every case to contain every VSM function.

## Anti-patterns

Do not write:

- “the project needed S2” because contributors conflicted once;
- “CI is S3*” merely because it verifies code;
- “maintainers are S3” because they manage the repository;
- “roadmaps are S4” because they concern the future;
- “governance is S5” because a governance file exists;
- “100+ contributors proves organizational complexity.”

Instead reconstruct the concrete function, decisive feedback/decision right, evidence path, observed closure, and relevant recursion boundary.

## Relationship to `evolution-log.md`

The internal OpenSiro evolution log and external cases should eventually support the same comparative chain:

```text
observed disturbance
→ response introduced
→ evidence of consequence
→ functional interpretation
→ bounded reusable lesson
```

The first synthesis remains the historical three-case snapshot. The second synthesis adds the fourth owner-evidence case and explicitly narrows/falsifies earlier provisional patterns where required. The downstream causal article still requires comparison against OpenSiro's own evidence and must not treat the external sample as proof of superiority.
