# Contributing

This repository defines a VSM-based contribution contract for Opensiro OSS. Contributors may use any local runtime, scheduler, model provider, or agent harness. Opensiro standardizes organizational responsibilities and GitHub boundaries, not execution technology.

## Find current state first

Do not use this file as a live milestone or autonomy-grade dashboard.

- **GitHub milestones + their tracker issues** own planned destination, exit criteria, and completion history.
- [`TODO.md`](TODO.md) owns only current `NOW` / `NEXT` / `BLOCKED` scheduling.
- [`ROADMAP.md`](ROADMAP.md) is a readable projection of the construction sequence and evidence narrative, not a second planning authority.
- [`records/`](records/) contains concrete execution/evidence records and bounded snapshots.
- Canonical general assessment publication, when one exists, belongs in `opensiro/vsm-harness-index`, not here.

The latest bounded self-audit of this reference organization is preserved as the explicitly non-canonical [`records/assessment-snapshots/2026-09-30-general-preassessment.md`](records/assessment-snapshots/2026-09-30-general-preassessment.md). Do not silently promote that snapshot into an Index fact.

## One bounded S1 contribution

The reference operational unit is one bounded S1 contribution inside exactly one declared domain: Index, Skills, or Awesome.

```text
Issue / explicit work item
        ↓
claim one bounded contribution
        ↓
contributor-owned runtime
        ↓
S1 actor adapter + domain/admission contracts
        ↓
research / implementation / validation / recovery
        ↓
Issue artifact / Pull Request / no-change / escalation
```

Use:

- [`roles/S1.md`](roles/S1.md) — executable actor adapter / action loop;
- [`contracts/s1/domain-contracts.md`](contracts/s1/domain-contracts.md) — local outcome, authority, completion, and escalation envelopes;
- [`contracts/s1/task-admission-recovery.md`](contracts/s1/task-admission-recovery.md) — admission, intervention, routine recovery, escalation, and terminal states;
- [`records/s1/autonomy-coverage.md`](records/s1/autonomy-coverage.md) — operational construction evidence.

A contribution should state the system-in-focus, repository/work boundary, expected outcome, evidence/tests required for completion, locally delegated decisions, and escalation conditions.

The contributor owns the runtime envelope: scheduler, model choice, credentials, budget, sandbox, and launch cadence. Those mechanisms do not inherit VSM function ownership merely because they execute or transport an already-selected decision.

## One S1 does not mean one process

A contributor may use several internal agents or tools. Do not create extra VSM functions from process names alone.

Several workers remain one S1 when they jointly close one durable contribution outcome and do not operate as independently regulated operational units with separate environments and autonomy.

## Autonomous work observability

Substantial autonomous work must remain easy for the project owner to supervise without following every intermediate issue, PR, CI run, or tool call.

Follow [`AUTONOMOUS_WORK_REPORTING.md`](AUTONOMOUS_WORK_REPORTING.md) for the common status snapshot and continuation rule. Reporting is an observability surface only; it does not create authority, scheduling truth, or a VSM function.

## Metasystem paths

Organizational contracts live under [`contracts/`](contracts/README.md). Actor-specific composition belongs under `roles/`; concrete executions/evidence belong under `records/`.

- S3 current-control: [`contracts/s3/current-control.md`](contracts/s3/current-control.md) with [`roles/S3.md`](roles/S3.md).
- S3* complementary audit: [`contracts/s3star/audit.md`](contracts/s3star/audit.md) with [`roles/S3STAR.md`](roles/S3STAR.md).
- S5 parent boundary: [`contracts/s5/parent-boundary.md`](contracts/s5/parent-boundary.md) and [`contracts/s5/parent-authority.md`](contracts/s5/parent-authority.md).
- external tool admission: [`contracts/tools/external-entry.md`](contracts/tools/external-entry.md).

A contract or role file is **construction**, not positive function evidence. A later function is credited only when the selected Profile/Methodology evidence requirements are actually met at the declared operating boundary.

## Escalation and parent-governed S5

Start with [`CONTRIBUTOR_START.md`](CONTRIBUTOR_START.md) for repository ownership and organization-wide routing.

A contributor may compose the S5 process using [`prompts/parent-control-plane.md`](prompts/parent-control-plane.md): gather evidence, classify the matter, prepare options, record/apply a returned parent decision, and verify closure. Running the process does not transfer unresolved S5 discretion to the contributor.

Use the shorthand only as an admission request:

```text
S5: рассмотреть <matter>
S5: consider <matter>
```

Existing returned parent policy may be applied without creating a new S5 event. A genuinely unresolved identity/ultimate-policy choice must reach the legitimate parent declared by the current S5 authority contract. Ordinary S1 work, S3 current-control, S3* audit, PR review, CI repair, or routine tool use must not be promoted into S5 merely because the matter is important.

## GitHub boundary

Prefer one claimed work item → one reviewable PR unless the work item explicitly defines another artifact.

Do not mutate shared canonical state merely to prove autonomy. Human review/merge may remain a separate integration right. Whether a GitHub mechanism later participates in S2/S3/S3*/S4/S5 is a function-first evidence question, not a consequence of its name.

## Milestone discipline

Do not add permanent S2/S3/S3*/S4/S5 agents pre-emptively. New roles, contracts, records, queues, or automation count only when concrete residual variety establishes their need and the applicable function/ownership/closure evidence is satisfied.

`A`, `C`, and `P` are ownership arrangements, not maturity scores. Milestone target vectors are construction targets for this reference organization; they are not automatic assessment grades.
