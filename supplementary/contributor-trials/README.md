# Fresh contributor trials

This directory stores empirical runs for [Fresh contributor conformance](../../CONTRIBUTOR_CONFORMANCE.md).

These trials are stricter than routing-only trials: a run must progress from the public OpenSiro entry surface through task acquisition, current contract resolution, bounded repository work, validation, and normal delivery/review.

A record must never claim a blind result from a maintainer/assistant session that already has OpenSiro context.

Prepared contributor trials are supplementary empirical work, not automatic milestone blockers. A prepared trial may be retired without execution when the research question is no longer active; retirement must remain explicit and must not be rewritten into PASS/FAIL evidence.

## Record states

- `READY` — prompt and evidence schema prepared, no qualifying fresh run executed yet.
- `RUNNING` — a qualifying independent run has started.
- `BLOCKED` — the run reached a genuine infrastructure/permission blocker.
- `PASS` — all required stages completed and normal repository review accepted the bounded work item.
- `FAIL` — the run violated a required stage or produced a materially invalid contribution.
- `RETIRED — NOT EXECUTED` — a prepared design was explicitly closed without a qualifying run; it remains provenance only and has no behavioral evidence value.

Preserve terminal `BLOCKED` and `FAIL` records. Create a new run instead of rewriting an unsuccessful run into a success.

For a retired prepared design, preserve the historical prompt/surface notes only when useful for provenance and make clear that no empirical run occurred. If the question becomes relevant again, create a new trial against current surfaces rather than reviving stale frozen assumptions.

## Minimum record

Each executed run should include:

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
