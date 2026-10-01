# VSM OSS outcome metrics

This document defines the public metrics contract for the bounded OpenSiro VSM Harness OSS group.

It is an organization-wide observability contract. It does **not** redefine VSM semantics, repository ownership, assessment methodology, curation policy, milestone evidence, or decision authority. Canonical facts remain in the repository that owns them.

The machine-readable projection of this contract is [`metrics.yaml`](metrics.yaml).

## Scope

Only these current public repositories are in scope:

- `opensiro/vsm-harness-profile`
- `opensiro/vsm-harness-skills`
- `opensiro/vsm-harness-index`
- `opensiro/awesome-vsm-harness`
- `opensiro/vsm-oss-organization`

Repositories outside this set are excluded even if they belong to OpenSiro or consume these artifacts.

## Principle: count accepted outputs, not edits

The public scoreboard measures **durable repository-owned state** and qualified transitions. Activity that merely moves work toward a completion gate is not itself an outcome.

| Activity / state | Public outcome KPI? |
| --- | --- |
| commit created | no |
| lines changed | no |
| PR opened | no |
| issue closed | no, unless a metric explicitly owns that terminal artifact |
| assessment admitted to the canonical corpus | yes |
| reassessment event accepted into canonical history | yes |
| released Profile/Methodology state validated under its repository contract | yes |
| Awesome entry admitted and canonical-Index consistency validated | yes |
| organization control/audit transaction completed with the required semantic evidence | yes |

Commits, merged PRs, workflow runs, and similar quantities may be exposed as **secondary engineering telemetry**. They must never be presented as productivity, quality, or verified-output metrics.

## Stock, flow, health, state, and window change

The dashboard distinguishes:

- **stock** — current durable corpus/state, such as included assessments;
- **flow** — completed qualifying transitions during a window;
- **health** — validation/consistency result for the current state;
- **state** — non-numeric current identity such as the active Profile release;
- **window change** — the difference between the current canonical stock/state and the same repository-owned state at a historical cutoff.

The default public comparison windows are **24h, 7d, and 30d**.

For a numeric stock:

```text
window change = current canonical stock - canonical stock at cutoff
```

This is **net canonical state change, not gross event count**. For example, `included assessments +15 / 24h` means that the canonical included-assessment stock is 15 higher than at the 24-hour cutoff. It is not independently claiming that exactly 15 admission events occurred.

A true flow such as `assessments_admitted` or `entries_retired` is a different semantic claim and requires the owning repository's event/identity semantics. The organization collector must not manufacture gross flow from a stock delta.

For state-valued metrics, a window reports whether the repository-owned state changed during the window rather than assigning a numerical productivity value.

## Historical-source rule

Current and historical values must be calculated by the **same owning repository logic** whenever possible.

1. Read the current metric from its declared repository-owned source.
2. At each 24h/7d/30d cutoff, read the same source from the latest repository revision at or before the cutoff.
3. If the generated metric artifact did not yet exist but the owning repository exposes a read-only renderer for the historical source tree, use that renderer.
4. Do **not** reimplement another repository's counting logic inside `vsm-oss-organization`.
5. If a repository did not yet exist at the cutoff, cumulative numeric stock uses a zero pre-inception baseline.
6. Semantic-evidence metrics remain unclaimed when the required evidence cannot be mechanically established.

For Index specifically, current corpus counts come from `data/metrics.json`. Historical pre-instrumentation core counts are evaluated through the Index-owned `scripts/render_metrics.py --source-root ... --stdout-core-json` interface. Organization does not count Index assessments from `signatures.psv`, `catalog.psv`, or assessment files itself.

## Cross-repository anti-gaming rules

1. **Repository ownership wins.** A fact is counted from its canonical owner, not duplicated across consumers.
2. **One transition, one count.** Generated/materialized downstream files do not create extra outputs for the same underlying transition.
3. **No edit-volume substitution.** Commits, changed files, LOC, comments, issues, PRs, and workflow runs are not verified outputs.
4. **Completion gates are mandatory.** A semantic flow counts only after its repository-specific validation/acceptance boundary is satisfied.
5. **Corrections are not new admissions.** A same-object correction changes state but does not create a second object unless the owner explicitly records a new event type.
6. **Generated views are projections.** Regenerating TLDR, rankings, metrics, snapshots, or synchronized files does not create another semantic output.
7. **No cross-repo double counting.** A Profile release consumed by Skills and Index is one Profile outcome, not three.
8. **Semantic metrics require semantic evidence.** Mechanical closure alone must not claim a control transaction, audit, milestone, autonomy state, or other semantically qualified event.
9. **Public scope only.** Private repositories and out-of-bound OpenSiro work are excluded.
10. **No fabricated live values.** A dashboard may display only values derived from declared sources at pinned revisions/times.

## Repository metric contracts

### `opensiro/vsm-harness-index`

**Role:** operational S1; canonical evidence-backed corpus and its provenance/history/materialized comparative views.

Primary:

- **Included assessments** (`stock`) — `corpus.included_assessments` from Index-owned `data/metrics.json`.

Supporting:

- **Catalog entries** (`stock`) — `corpus.catalog_entries` from `data/metrics.json`.
- **Reassessment events** (`stock`) — `corpus.reassessment_events` from `data/metrics.json`.
- **Assessments admitted** (`flow`) — only when derived from an explicit Index-owned admission/event identity boundary; not inferred from stock delta.
- **Reassessments completed** (`flow`) — only when derived from accepted reassessment history/event semantics.
- **Corpus consistency** (`health`) — Index validators and generated-view checks pass.
- **Active contract** (`state`) — Profile and Methodology versions recorded by the Index metrics artifact.

Completion: an assessment/reassessment counts only after the Index owns the accepted canonical state and its required validation passes. Regeneration of signatures, TLDR, rankings, or metrics does not create additional outputs.

Not KPIs: commits, Markdown lines, generated-file count, candidate discoveries, queued candidates, PR count, issue count.

### `opensiro/vsm-harness-skills`

**Role:** operational S1; reusable assessment procedure, Methodology, references, synchronization/provenance tooling, and deterministic validation surfaces.

Primary:

- **Current validated Methodology release** (`state`) — `skills/assess-vsm-harness/VERSION` under the repository release/validation contract.

Supporting:

- **Published Methodology releases** (`stock`).
- **Methodology releases published** (`flow`).
- **Skill catalog entries** (`stock`).
- **Profile snapshot synchronized** (`health`).
- **Procedure validation** (`health`).

Experimental material is not a released Methodology outcome until promoted through the repository release boundary.

Not KPIs: commits, Markdown/prompt count, test count by itself, generated snapshot changes, PR count, issue count.

### `opensiro/awesome-vsm-harness`

**Role:** operational S1; curated representative downstream view backed by canonical Index evidence.

Primary:

- **Curated representative entries** (`stock`) — current admitted project entries, excluding headings, future directions, related-list references, and other non-entry links.

Supporting:

- **Entries admitted** (`flow`) — explicit completed curation admissions.
- **Entries retired/replaced** (`flow`) — explicit completed removals/replacements; report separately from admissions.
- **Canonical Index consistency** (`health`).

A change in the stock over 24h/7d/30d is net curation-state change; a negative value is valid and can reflect deliberate narrowing.

Not KPIs: link count, section count, candidate count, README LOC, commits, PR count, issue count.

### `opensiro/vsm-harness-profile`

**Role:** normative semantic authority.

Primary:

- **Current validated Profile release** (`state`) — `VERSION`, with release-impact metadata/repository validation governing the release state.

Supporting:

- **Published Profile releases** (`stock`).
- **Profile releases published** (`flow`).
- **Release-impact chain valid** (`health`).
- **Repository validation** (`health`).

Requirement count growth is intentionally not a productivity metric: more normative requirements are not inherently better.

Not KPIs: normative LOC, citations added, commits, PR count, issue count.

### `opensiro/vsm-oss-organization`

**Role:** organizational/metasystem construction and shared control surface for the bounded group.

Primary:

- **Current formal construction milestone** (`state`, semantic evidence required).

Supporting:

- **Operational S1 domains with evidence paths** (`stock`, semantic evidence required).
- **Completed current-control transactions** (`flow`, semantic evidence required).
- **Completed complementary audits** (`flow`, semantic evidence required).
- **Parent-authority witnesses established** (`stock`, semantic evidence required).
- **Organization contract consistency** (`health`).

Issues, comments, approvals, scheduler changes, labels, or ordinary reports do not count as S3/S3*/S5 evidence by themselves. If the semantic evidence cannot be established mechanically, the public collector reports the metric as **unclaimed**, not zero and not guessed.

Not KPIs: governance-document count, prompts added, issues closed, TODO churn, commits, PR count, comments, approvals.

## Organization-level presentation

The primary public view should emphasize current repository-owned state plus iterative growth:

```text
VSM OSS — PUBLIC STATE

                         CURRENT    24H     7D      30D
Index assessments          193      +15    +112     +193
Awesome curated entries      5        0      -6       +5
Profile                    0.2.4   changed   ...      ...
Methodology                0.3.6   changed   ...      ...
Organization milestone    unclaimed  —       —        —
```

The values above are illustrative of the rendering shape; live values must always come from the machine-readable snapshot.

Do not sum heterogeneous repository outputs into a synthetic productivity number. If an aggregate is useful for navigation, its composition must be explicit.

## Secondary engineering telemetry

Optional telemetry may include commits, merged PRs, repositories touched, workflow runs, or CI duration. If displayed:

- use the same 24h/7d/30d windows where useful;
- place it below outcome/state metrics;
- label it **engineering activity** or **telemetry**, not productivity;
- never use it to rank repositories or contributors;
- do not mix bot/automation and human activity unless attribution is explicitly defined;
- keep the collection window and commit identity rules visible.

A large commit count may demonstrate the amount of auditable Git activity behind the system, but it does not prove useful output by itself.

## Collection and publication

The public collector must:

1. pin an exact revision for each repository;
2. collect current state only from sources declared in `metrics.yaml`;
3. compute 24h/7d/30d net window change from the same repository-owned state at historical cutoffs;
4. use owning-repository renderers for pre-instrumentation history rather than duplicating their counting logic;
5. preserve the collection timestamp, cutoff revisions, and repository revisions;
6. keep stock window change distinct from semantically stronger flow/event claims;
7. verify completion/health checks where mechanically possible;
8. leave semantic metrics unclaimed when required evidence cannot be mechanically established;
9. keep engineering activity structurally separate from outcome metrics;
10. publish the raw machine-readable snapshot alongside any human-facing rendering.

This keeps `opensiro.com` or another presentation surface as a consumer of bounded VSM OSS state rather than a second metrics authority.
