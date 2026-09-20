# Empirical OSS harness case studies

This directory contains comparative empirical artifacts for the `vsm-oss-organization` supplementary empirical track.

Parent workstream: [#30](https://github.com/opensiro/vsm-oss-organization/issues/30).

Case-study tasks:

- first case: [#31](https://github.com/opensiro/vsm-oss-organization/issues/31);
- second case: [#88](https://github.com/opensiro/vsm-oss-organization/issues/88).

These documents are **not VSM Harness Index assessments** and are not a second assessment database. Their purpose is to reconstruct how real OSS harness organizations changed over time so the practical significance of VSM/OSM construction ideas can be tested against independent history.

## Cases

- [`autogen.md`](autogen.md) — AutoGen multimodal coordination pressure, roadmap/epic consolidation, partial repairs, and the later `v0.4` architectural boundary. The case intentionally leaves decisive S2/S4 ownership and causal development-cost claims unproven where the public evidence does not establish them.
- [`openhands-runtime.md`](openhands-runtime.md) — OpenDevin/OpenHands runtime migration from SSH-coupled execution toward EventStreamRuntime, including partial compatibility work, parallel replacement implementation, integration/evaluation gates, preserved validation gaps, and final retirement/default switch. The case does not infer S3/S3*/S4 ownership from runtime, testing, or maintainer vocabulary.

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
- map the organizational function first and classify ownership only when evidence establishes the decisive right and its owner.

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

These dimensions are prompts for evidence collection, not a checklist requiring every case to contain every VSM function.

## Anti-patterns

Do not write:

- “the project needed S2” because contributors conflicted once;
- “CI is S3*” merely because it verifies code;
- “maintainers are S3” because they manage the repository;
- “roadmaps are S4” because they concern the future;
- “governance is S5” because a governance file exists;
- “100+ contributors proves organizational complexity.”

Instead reconstruct the concrete function, decisive feedback/decision right, evidence path, and observed closure.

## Relationship to `evolution-log.md`

The internal OpenSiro evolution log and external cases should eventually support the same comparative chain:

```text
observed disturbance
→ response introduced
→ evidence of consequence
→ functional interpretation
→ bounded reusable lesson
```

Cross-case synthesis should begin only after enough independent artifacts exist to distinguish recurring evidence from a single-project anecdote.
