# VSM Harness OSS contributor routing conformance

This document defines how OpenSiro verifies that a contributor or agent can begin from an arbitrary repository **inside the declared VSM Harness OSS system boundary**, discover the shared current-work entry point, and route into the correct owning repository without turning `vsm-oss-organization` into a second source of truth for repository-local work.

## Invariant

Every repository in the canonical `Current in-scope public repositories:` block in [README.md](README.md) must expose two things directly from its root README:

1. the Organization routing surface for organization-wide questions;
2. the shared [TODO.md](TODO.md) current-work entry point for already tracked work.

Repository-local work stays with the repository that owns the relevant source of truth. Questions about contributor roles, authority boundaries, escalation, cross-repository coordination, current-work ordering, milestone sequencing, or shared organizational evolution across the in-scope group route to `opensiro/vsm-oss-organization` and its [CONTRIBUTOR_START.md](CONTRIBUTOR_START.md) entry point.

`TODO.md` owns cross-repository selection/status/order only. After a tracked item is selected, the contributor returns to the linked issue and owning repository for task scope, evidence, frozen refs, validation, acceptance, and canonical artifacts.

Public OpenSiro repositories outside that canonical scope are **not** subjects of this routing invariant. Public visibility or organization membership does not add a repository to the bounded VSM Harness system.

## Mechanical live check

[`scripts/check_public_routing.py`](scripts/check_public_routing.py) reads the canonical repository set from the Organization README scope block. This intentionally reuses the same scope surface consumed by `scripts/validate_contract.py` instead of introducing a second manually maintained allowlist.

For each in-scope repository it:

1. reads live GitHub metadata and confirms the repository is public;
2. reads the repository's reported default branch;
3. fetches the root README from that branch;
4. verifies a direct Organization routing reference;
5. verifies a direct reference to the shared Organization `TODO.md` current-work entry point;
6. for `vsm-oss-organization` itself, accepts the relative `CONTRIBUTOR_START.md` and `TODO.md` entry points;
7. reports every missing/unreadable route explicitly and exits non-zero if any in-scope repository fails.

The check is intentionally separate from `scripts/validate_contract.py`. The contract validator is repository-local and deterministic; routing discoverability is a temporal cross-repository property that depends on live GitHub state.

A newly created public OpenSiro repository does not become subject to this oracle merely by existing. It becomes subject to the oracle only when the canonical Organization scope is explicitly changed to admit it.

The `VSM OSS contributor routing` workflow runs the scoped live check manually, weekly, and when the routing oracle itself changes.

## Evidence boundary

A passing mechanical check proves **direct discoverability inside the declared scope**, not that an arbitrary agent will interpret the boundary correctly.

The mechanical oracle does not prove:

- that an agent will follow the Organization or TODO link;
- that it will distinguish tracked-work selection from repository-local task ownership;
- that it will distinguish local work from organization-wide work;
- that it will route back to the owning repository after consulting Organization;
- that repositories outside scope participate in this organization;
- any VSM autonomy state.

Those are separate questions. Agent interpretation requires blind trials; scope membership remains an explicit Organization decision.

## Blind-agent trial protocol

A qualifying behavioral trial uses a fresh agent/run with:

- no OpenSiro project prompt;
- no prior OpenSiro conversation or memory supplied to the run;
- no preloaded `vsm-oss-organization` URL;
- exactly one **in-scope** repository as the starting point;
- permission to read and navigate public GitHub links.

Each current in-scope repository must appear as a starting point in the batch. The task set must include both organization-wide positive cases and repository-local negative controls.

Representative positive cases:

- find and pick up already tracked cross-repository work without scanning every issue tracker;
- change contributor authority across in-scope repositories;
- resolve an escalation spanning two in-scope repository owners;
- change shared milestone sequencing;
- change the cross-repository contribution/control workflow.

Representative negative controls:

- change Profile semantics;
- change Skills assessment procedure;
- reassess one Index harness;
- change Awesome curation.

A trial is a PASS only when the agent chooses the correct destination and states the source-of-truth boundary. Tracked-work tasks should discover `TODO.md` and then return to the linked owner. Organization-wide tasks must independently discover Organization; local tasks must stay in, or explicitly return to, the owning repository.

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

## Current scope

The routing invariant applies to the five repositories declared in the Organization README: Profile, Skills, Index, Awesome, and Organization itself.

`arctic-0`, `terminal-bench-vsm`, and `opensiro.com` are outside this bounded VSM Harness OSS system and are not subjects of this routing invariant.
