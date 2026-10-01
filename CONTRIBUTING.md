# Contributing

This repository defines the contribution/control contract for the bounded OpenSiro VSM Harness OSS group. Contributors may use any runtime, scheduler, model provider, or agent harness; OpenSiro standardizes organizational responsibilities and GitHub boundaries, not execution technology.

## Find current state first

- **GitHub milestones + their tracker issues** own planned destination, exit criteria, and completion history.
- [`TODO.md`](TODO.md) owns only current `NOW` / `NEXT` / `BLOCKED` scheduling.
- [`docs/ROADMAP.md`](docs/ROADMAP.md) is a readable projection of the construction sequence and evidence narrative, **not a second planning authority**.
- [`records/`](records/) contains concrete execution/evidence records and bounded snapshots.
- Canonical general assessment publication belongs in `opensiro/vsm-harness-index`, not here.

The latest bounded self-audit is the explicitly non-canonical [`records/assessment-snapshots/2026-09-30-general-preassessment.md`](records/assessment-snapshots/2026-09-30-general-preassessment.md). **Do not silently promote that snapshot into an Index fact**.

## One bounded S1 contribution

Ordinary bounded S1 work belongs to exactly one declared domain: Index, Skills, or Awesome. Use:

- [`modes/s1-autonomous/README.md`](modes/s1-autonomous/README.md) — supported first-party operating mode;
- [`roles/S1.md`](roles/S1.md) — S1 actor adapter;
- [`contracts/s1/domain-contracts.md`](contracts/s1/domain-contracts.md) — local outcome/authority/completion envelopes;
- [`contracts/s1/task-admission-recovery.md`](contracts/s1/task-admission-recovery.md) — admission, recovery, escalation, and terminal states;
- [`records/s1/autonomy-coverage.md`](records/s1/autonomy-coverage.md) — operational construction evidence;
- [`records/s1/runs/`](records/s1/runs/) — concrete autonomous-mode execution evidence.

A contribution should state its system-in-focus, repository/work boundary, expected outcome, evidence/tests required for completion, locally delegated decisions, and escalation conditions.

Several internal agents or tools may still compose one S1 when they jointly close one durable operational outcome. Process names do not create extra VSM functions.

## Autonomous work observability

For substantial autonomous work follow [`docs/AUTONOMOUS_WORK_REPORTING.md`](docs/AUTONOMOUS_WORK_REPORTING.md). Reporting is an observability surface only; it does not create authority, scheduling truth, or a VSM function.

## Metasystem paths

Organizational contracts live under [`contracts/`](contracts/README.md). Actor-specific composition belongs under `roles/`; concrete executions/evidence under `records/`.

- S3 current-control: [`contracts/s3/current-control.md`](contracts/s3/current-control.md) + [`roles/S3.md`](roles/S3.md)
- S3* complementary audit: [`contracts/s3star/audit.md`](contracts/s3star/audit.md) + [`roles/S3STAR.md`](roles/S3STAR.md)
- S5 parent boundary/authority: [`contracts/s5/`](contracts/s5/)
- external tool admission: [`contracts/tools/external-entry.md`](contracts/tools/external-entry.md)

A contract or role file is **construction**, not positive function evidence.

## Escalation and parent-governed S5

Start with [`CONTRIBUTOR_START.md`](CONTRIBUTOR_START.md) for repository ownership and organization-wide routing. The S5 composition prompt is [`prompts/parent-control-plane.md`](prompts/parent-control-plane.md).

Ordinary S1 work, S3 current-control, S3* audit, PR review, CI repair, or routine tool use must not be promoted into S5 merely because the matter is important.

## GitHub boundary

Prefer one claimed work item → one reviewable PR unless the work contract explicitly defines another artifact. Human review/merge may remain a separate integration right.

## Milestone discipline

Do not add permanent S2/S3/S3*/S4/S5 agents pre-emptively. New roles, contracts, records, queues, or automation count only when concrete residual variety establishes their need and the applicable function/ownership/closure evidence is satisfied.

`A`, `C`, and `P` are ownership arrangements, not maturity scores. Milestone target vectors are construction targets for this reference organization; they are not automatic assessment grades.
