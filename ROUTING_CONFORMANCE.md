# Public contributor routing conformance

This document defines how OpenSiro verifies that a contributor or agent can begin from an arbitrary public repository and discover the correct organizational routing surface without turning `vsm-oss-organization` into a second source of truth for repository-local work.

## Invariant

Every public repository under `opensiro` must expose organization-wide contributor routing directly from its root README.

Repository-local work stays with the repository that owns the relevant source of truth. Questions about contributor roles, authority boundaries, escalation, cross-repository coordination, milestone sequencing, or shared organizational evolution route to `opensiro/vsm-oss-organization` and its [CONTRIBUTOR_START.md](CONTRIBUTOR_START.md) entry point.

This routing invariant is broader than the bounded VSM Harness system. Passing the routing check does not make ARCTIC, the website, `terminal-bench-vsm`, or any future public repository an S1 domain.

## Mechanical live check

[`scripts/check_public_routing.py`](scripts/check_public_routing.py) queries GitHub for the current public repositories in the `opensiro` organization. It does not rely on a manually maintained repository allowlist.

For each repository it:

1. reads the repository's reported default branch;
2. fetches the root README from that branch;
3. verifies a direct reference to `opensiro/vsm-oss-organization`;
4. for `vsm-oss-organization` itself, accepts the relative `CONTRIBUTOR_START.md` entry point;
5. reports every missing/unreadable route explicitly and exits non-zero if any public repository fails.

The check is intentionally separate from `scripts/validate_contract.py`. The contract validator is repository-local and deterministic; public routing is a temporal cross-repository property that depends on live GitHub state.

The `Public contributor routing` workflow runs the live check manually, weekly, and when the routing oracle itself changes.

## Evidence boundary

A passing mechanical check proves **direct discoverability**, not that an arbitrary agent will interpret the boundary correctly.

The mechanical oracle does not prove:

- that an agent will follow the link;
- that it will distinguish local work from organization-wide work;
- that it will route back to the owning repository after consulting Organization;
- any VSM autonomy state.

Those are behavioral questions and require blind trials.

## Blind-agent trial protocol

A qualifying behavioral trial uses a fresh agent/run with:

- no OpenSiro project prompt;
- no prior OpenSiro conversation or memory supplied to the run;
- no preloaded `vsm-oss-organization` URL;
- exactly one public OpenSiro repository as the starting point;
- permission to read and navigate public GitHub links.

Each public repository must appear as a starting point in the batch. The task set must include both organization-wide positive cases and repository-local negative controls.

Representative positive cases:

- change contributor authority across repositories;
- resolve an escalation spanning two repository owners;
- change shared milestone sequencing;
- change the cross-repository contribution/control workflow.

Representative negative controls:

- change Profile semantics;
- change Skills assessment procedure;
- reassess one Index harness;
- change Awesome curation;
- change ARCTIC archive/schema/tooling;
- change website presentation;
- change experimental harness-local behavior in `terminal-bench-vsm`.

A trial is a PASS only when the agent chooses the correct destination and states the source-of-truth boundary. Organization-wide tasks must independently discover Organization; local tasks must stay in, or explicitly return to, the owning repository.

Record at least:

```text
start repository @ SHA
prompt / task class
files read
links followed
chosen destination
short routing rationale
PASS / FAIL
```

A batch result is empirical reliability evidence only. It must not be reported as proof of unrelated S1-S5 autonomy states.

## Current rollout

The routing entry point was rolled out across the public repository set before enabling this oracle. Future repositories become subject to the same invariant automatically when they become public because the live check enumerates GitHub rather than a frozen list.
