# VSM OSS outcome metrics

This document defines the public metrics contract for the bounded OpenSiro VSM Harness OSS group.

It is an organization-wide observability contract. It does **not** redefine VSM semantics, repository ownership, assessment methodology, curation policy, milestone evidence, or decision authority. Canonical facts remain in the repository that owns them.

The machine-readable projection of this contract is [`metrics.yaml`](metrics.yaml).

## Scope

Only the current public repositories inside the organization boundary are measured:

- `opensiro/vsm-harness-profile`
- `opensiro/vsm-harness-skills`
- `opensiro/vsm-harness-index`
- `opensiro/awesome-vsm-harness`
- `opensiro/vsm-oss-organization`

Repositories outside this set are not included merely because they belong to OpenSiro, consume these artifacts, or are operationally related.

## Principle: count accepted outputs, not edits

The default public scoreboard measures **durable repository-owned state** and **completed state transitions**.

A metric may increase only when the owning repository reaches the completion gate declared for that metric. Activity that merely moves work toward a gate is not itself an outcome.

Examples:

| Activity / state | Public outcome KPI? |
| --- | --- |
| commit created | no |
| lines changed | no |
| PR opened | no |
| issue closed | no, unless the metric explicitly requires a semantically qualified terminal artifact |
| assessment admitted to the canonical corpus | yes |
| reassessment event accepted into canonical history | yes |
| released Profile/Methodology state validated under its repository contract | yes |
| Awesome entry admitted and canonical-Index consistency validated | yes |
| organization control/audit transaction completed with its required evidence path | yes |

Commits, merged PRs, workflow runs, and similar quantities may be exposed as **secondary engineering telemetry**. They must never be presented as productivity, quality, or verified-output metrics.

## Stock, flow, health, and state

The dashboard should distinguish four kinds of values:

- **stock** — current durable corpus/state, such as included assessments;
- **flow** — completed qualifying transitions during a window, normally 7 or 30 days;
- **health** — validation/consistency result for the current state;
- **state** — non-numeric current identity such as the active Profile release or formal organization milestone.

A stock is not automatically a target to maximize. A flow is descriptive throughput, not an incentive to split one meaningful change into many smaller artifacts.

## Cross-repository anti-gaming rules

1. **Repository ownership wins.** A fact is counted from its canonical owner, not duplicated across consumers.
2. **One transition, one count.** Generated/materialized downstream files do not create extra outputs for the same underlying transition.
3. **No edit-volume substitution.** Commits, changed files, LOC, comments, issues, PRs, and workflow runs are not verified outputs.
4. **Completion gates are mandatory.** A flow counts only after the repository-specific validation/acceptance boundary is satisfied.
5. **Corrections are not new admissions.** A same-object correction changes state but does not create a second object unless the owning repository explicitly records a new event type, such as a reassessment event.
6. **Generated views are projections.** Regenerating TLDR, rankings, metrics, snapshots, or synchronized files does not create an additional semantic output.
7. **No cross-repo double counting.** A Profile release consumed by Skills and Index is one Profile outcome, not three outcomes.
8. **Semantic metrics require semantic evidence.** Mechanical closure alone must not be used to claim a control transaction, audit, milestone, autonomy state, or other semantically qualified event.
9. **Public scope only.** Private repositories and out-of-bound OpenSiro work are excluded from this contract.
10. **No fabricated live values.** A dashboard may display only values derived from declared sources at a pinned collection time.

## Repository metric contracts

### `opensiro/vsm-harness-index`

**Role:** operational S1; canonical evidence-backed corpus and its provenance/history/materialized comparative views.

Primary public metric:

- **Included assessments** (`stock`) — current `corpus.included_assessments` from `data/metrics.json`.

Supporting metrics:

- **Catalog entries** (`stock`) — current `corpus.catalog_entries` from `data/metrics.json`.
- **Reassessment events** (`stock`) — current accepted `corpus.reassessment_events` from `data/metrics.json`.
- **Assessments admitted** (`flow`) — positive delta of included-assessment identities across pinned snapshots, excluding corrections to an already included identity.
- **Reassessments completed** (`flow`) — positive delta of accepted reassessment events across pinned snapshots.
- **Corpus consistency** (`health`) — Index validators and generated-view checks pass for the collected revision.
- **Active contract** (`state`) — Profile and Methodology versions recorded by the Index metrics artifact.

Completion gates:

- an admission counts only after the assessment is accepted into the canonical corpus and repository validation passes;
- a reassessment counts only when the Index records the accepted reassessment event/history under its local contract;
- regeneration of signatures, TLDR, rankings, or metrics as consequences of the same admission does not create additional outputs.

Not KPIs: commits, assessment Markdown line count, generated-file count, candidate discoveries, queued candidates, PR count, issue count.

### `opensiro/vsm-harness-skills`

**Role:** operational S1; reusable assessment procedure, Methodology, references, synchronization/provenance tooling, and deterministic validation surfaces.

Primary public metric:

- **Current validated Methodology release** (`state`) — the Methodology version identified by `skills/assess-vsm-harness/VERSION`, with repository validation passing at the collected revision.

Supporting metrics:

- **Published Methodology releases** (`stock`) — immutable Methodology releases/tags that satisfy the repository release contract.
- **Methodology releases published** (`flow`) — qualifying new immutable Methodology releases during the window.
- **Skill catalog entries** (`stock`) — reusable skills declared by the repository's skill catalog.
- **Profile snapshot synchronized** (`health`) — the bundled Profile snapshot/provenance checks pass against the selected Profile release.
- **Procedure validation** (`health`) — repository validation/tests for the current Methodology pass.

Completion gates:

- a Methodology release counts only after the versioned procedure and its required references/provenance are committed under the release contract and validation passes;
- edits to generated Profile snapshots, reference files, or tests do not independently count as new methodology outputs;
- experimental material under `experiments/` does not count as a released Methodology outcome until explicitly promoted through the repository's release boundary.

Not KPIs: commits, number of prompts/Markdown files, test count by itself, generated snapshot changes, PR count, issue count.

### `opensiro/awesome-vsm-harness`

**Role:** operational S1; curated representative downstream view backed by canonical Index evidence.

Primary public metric:

- **Curated representative entries** (`stock`) — current admitted project entries in the curated view, excluding headings, candidate directions, related lists, and other non-entry links.

Supporting metrics:

- **Entries admitted** (`flow`) — newly admitted representative project identities during the window.
- **Entries retired/replaced** (`flow`) — project identities deliberately removed or replaced by a completed curation decision; report separately from admissions rather than netting them away.
- **Canonical Index consistency** (`health`) — all curated project evidence links/anchors required by the local contract resolve consistently to canonical Index state and Awesome validation passes.

Completion gates:

- an admission counts only after the project is present as an accepted representative entry and local formatting/Index-consistency validation passes;
- adding a candidate to the Index, mentioning a project in an issue, or creating a future domain direction does not count as an Awesome admission;
- canonical Index assessment changes do not become new Awesome outputs unless they cause a completed curation-state transition here.

Not KPIs: number of links, number of sections, candidate count, README LOC, commits, PR count, issue count.

### `opensiro/vsm-harness-profile`

**Role:** normative semantic authority consumed by the bounded organization.

Primary public metric:

- **Current validated Profile release** (`state`) — the version in `VERSION`, with repository validation and release-impact metadata consistent at the collected revision.

Supporting metrics:

- **Published Profile releases** (`stock`) — immutable Profile releases/tags that satisfy the repository versioning/release contract.
- **Profile releases published** (`flow`) — qualifying new immutable Profile releases during the window.
- **Release-impact chain valid** (`health`) — `RELEASE_IMPACT.json` and consumer/release metadata pass repository validation for the current release line.
- **Repository validation** (`health`) — the deterministic Profile completion-oracle checks pass at the collected revision.

Completion gates:

- a Profile release counts only after normative/release metadata is committed under the Profile versioning contract, the immutable release/tag exists, and deterministic repository validation passes;
- examples, literature changes, wording corrections, or generated metadata changes do not become separate verified outputs merely because they required separate commits;
- the number of normative requirements is intentionally not a productivity metric: more requirements are not inherently better.

Not KPIs: requirement count growth, normative LOC, citations added, commits, PR count, issue count.

### `opensiro/vsm-oss-organization`

**Role:** organizational/metasystem construction and shared control surface for the bounded group.

Primary public metric:

- **Current formal construction milestone** (`state`) — the milestone state supported by the repository's committed roadmap/evidence; design targets and preparatory artifacts must not be reported as achieved state.

Supporting metrics:

- **Operational S1 domains with evidence paths** (`stock`) — declared S1 domains for which the repository records an explicit local contract and real operational evidence path.
- **Completed current-control transactions** (`flow`, semantic evidence required) — naturally qualifying whole-system S3 current-control transactions that complete the repository-defined request/decision/return path into subsequent S1 operation.
- **Completed complementary audits** (`flow`, semantic evidence required) — qualifying S3* audit transactions that complete the repository-defined complementary-evidence/judgment/outcome path.
- **Parent-authority witnesses established** (`stock`, semantic evidence required) — committed witnesses that satisfy the repository's explicit parent-authority evidence contract.
- **Organization contract consistency** (`health`) — repository-local validation/consistency checks for the current control surfaces pass.

Completion gates:

- issues, comments, approvals, scheduler changes, labels, or ordinary reports do not count as S3/S3*/S5 transactions by themselves;
- a control/audit/witness metric counts only when the complete evidence path required by the owning organizational contract exists;
- milestone target vectors are not achievements until their stated evidence conditions are satisfied.

Not KPIs: governance-document count, prompts added, issues closed, TODO churn, commits, PR count, comments, approvals.

## Organization-level presentation

The public organization view should present repository-owned state without collapsing unlike outputs into a single synthetic productivity score.

Recommended shape:

```text
VSM OSS — PUBLIC STATE

INDEX
  included assessments        <stock>
  reassessments / 30d         <flow>
  corpus consistency          <health>

SKILLS
  methodology                 <state>
  releases / 30d              <flow>
  validation                  <health>

AWESOME
  curated entries             <stock>
  admissions / 30d            <flow>
  Index consistency           <health>

PROFILE
  profile                     <state>
  releases / 30d              <flow>
  release-impact chain        <health>

ORGANIZATION
  formal milestone            <state>
  S1 evidence paths           <stock>
  control/audit tx / 30d      <flow>
```

Do not sum heterogeneous repository outputs into a single "productivity" number. If an aggregate is useful for navigation, label it **verified state transitions** and show its composition explicitly rather than presenting it as a quality score.

## Secondary engineering telemetry

Optional telemetry may include commits, merged PRs, repositories touched, workflow runs, or CI duration. If displayed:

- place it below outcome/state metrics;
- label it **engineering activity** or **telemetry**, not productivity;
- never use it to rank repositories or contributors;
- do not mix bot/automation and human activity unless attribution is explicitly defined;
- keep the collection window and commit identity rules visible.

A large commit count may demonstrate the amount of auditable Git activity behind the system, but it does not prove useful output by itself.

## Collection and publication

A future collector/dashboard should:

1. pin an exact revision for each repository;
2. collect only from sources declared in `metrics.yaml`;
3. run or verify the declared completion/health checks where mechanically possible;
4. preserve the collection timestamp and repository revisions;
5. compute flows from pinned historical snapshots rather than GitHub activity volume;
6. leave semantically qualified metrics unclaimed when the required evidence cannot be mechanically established;
7. publish the raw machine-readable snapshot alongside any human-facing rendering.

This keeps `opensiro.com` or another presentation surface as a consumer of the bounded VSM OSS state rather than a second metrics authority.