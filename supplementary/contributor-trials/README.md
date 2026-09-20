# Fresh contributor trials

This directory stores empirical runs for [Fresh contributor conformance](../../CONTRIBUTOR_CONFORMANCE.md).

These trials are stricter than routing-only trials: a run must progress from the public OpenSiro entry surface through task acquisition, current contract resolution, bounded repository work, validation, and normal delivery/review.

A record must never claim a blind result from a maintainer/assistant session that already has OpenSiro context.

## Record states

- `READY` — prompt and evidence schema prepared, no qualifying fresh run executed yet.
- `RUNNING` — a qualifying independent run has started.
- `BLOCKED` — the run reached a genuine infrastructure/permission blocker.
- `PASS` — all required stages completed and normal repository review accepted the bounded work item.
- `FAIL` — the run violated a required stage or produced a materially invalid contribution.

Preserve terminal `BLOCKED` and `FAIL` records. Create a new run instead of rewriting an unsuccessful run into a success.

## Minimum record

Each run should include:

- exact verbatim launch prompt;
- fresh-run declaration;
- public entry URL;
- observed repository revisions;
- ordered navigation/read trail;
- selected work item and resolved task envelope;
- validation evidence;
- PR/review outcome when delivery is in scope;
- stage-by-stage result and short failure analysis.

A pilot may be prepared in advance, but values the fresh agent is expected to discover must not be injected into its launch prompt.