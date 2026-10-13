# Documentation

Long-form repository documentation lives under `docs/`. Root-level files are reserved for public/bootstrap entry points, standard repository files, machine-readable contracts, and compatibility pointers.

## Canonical documentation

- [`ECOSYSTEM.md`](ECOSYSTEM.md) — cross-repository architecture and responsibility boundaries.
- [`ORGANIZATION.md`](ORGANIZATION.md) — viable-system identity and system boundary.
- [`CONTROL_PLANE.md`](CONTROL_PLANE.md) — operational authority, compatibility gates, and work lifecycle.
- [`AGENT_CONTROL_PLANE.md`](AGENT_CONTROL_PLANE.md) — maintainer-facing single-agent command interface that consumes those authority rules.
- [`../prompts/intake-s3-current-control.md`](../prompts/intake-s3-current-control.md) — bounded S3 current-decision intake for the existing constructor; does not grant authority or establish a witness.
- [`ROADMAP.md`](ROADMAP.md) — OSM construction sequence and evidence narrative.
- [`S2_CROSS_S1_CONSISTENCY_COORDINATOR.md`](S2_CROSS_S1_CONSISTENCY_COORDINATOR.md) — **prospective, not deployed** M4 cross-S1 assessment-operations coordination candidate; not an Independent Reviewer gate or S2=A claim.
- [`METRICS.md`](METRICS.md) — public outcome/observability contract.
- [`AUTONOMOUS_WORK_REPORTING.md`](AUTONOMOUS_WORK_REPORTING.md) — autonomous-run reporting contract.
- [`ROUTING_CONFORMANCE.md`](ROUTING_CONFORMANCE.md) — bootstrap/routing conformance protocol.
- [`CONTRIBUTOR_CONFORMANCE.md`](CONTRIBUTOR_CONFORMANCE.md) — fresh-contributor behavioral conformance.

## Root entry surfaces

The following intentionally remain at repository root:

- [`../README.md`](../README.md) — public human/AI handoff;
- [`../START_HERE.md`](../START_HERE.md) — canonical machine bootstrap;
- [`../TODO.md`](../TODO.md) — current-work scheduler;
- [`../CONTRIBUTOR_START.md`](../CONTRIBUTOR_START.md) — new/unclassified/cross-repository routing;
- [`../CONTRIBUTE_WITH_AI.md`](../CONTRIBUTE_WITH_AI.md) — human contribution handoff;
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — GitHub-standard contribution entry;
- [`../UPSTREAM_CONTRACT.json`](../UPSTREAM_CONTRACT.json) — machine-readable upstream selection.

Root files with the same names as long-form documents are compatibility pointers only. Canonical edits belong under `docs/`.
