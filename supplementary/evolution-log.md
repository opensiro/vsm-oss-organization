# Organizational evolution log

This file records how `vsm-oss-organization` actually evolves over time: observed problems, experiments, decisions, reversals, evidence, and resulting lessons.

It is **descriptive, empirical, and non-normative**. It does not redefine VSM semantics, the VSM Harness Profile, the assessment Methodology, or the roadmap. The purpose is to preserve enough historical evidence that later practical methodology can be derived from what happened rather than reconstructed around the final architecture.

Related artifacts:

- `ROADMAP.md` — intended construction sequence and milestone exit criteria;
- `supplementary/design-reasoning.md` — generalized reasoning patterns that survived, failed, or were narrowed;
- this file — the chronological/evolutionary record from which such reasoning may later be generalized;
- `supplementary/case-studies/` — external OSS histories used as comparative empirical material.

Parent empirical workstream: [#30](https://github.com/opensiro/vsm-oss-organization/issues/30).

## Recording rule

Do not rewrite earlier decisions to make the present design look inevitable.

When later evidence changes an interpretation:

1. preserve the earlier entry;
2. add the later evidence and new decision as a new entry;
3. mark the earlier interpretation `superseded` or `narrowed` where appropriate;
4. keep observed fact separate from VSM interpretation.

The log is not a complete project diary. Record only events that materially affect how a reusable VSM/OSM construction method might be understood.

## Entry schema

Each entry should make the following chain reviewable:

```text
context
→ observed problem / residual variety
→ alternatives considered
→ decision / experiment
→ evidence
→ result
→ VSM interpretation
→ reusable lesson
```

Use this template when adding a new entry:

```md
## YYYY-MM-DD — <decision or transition>

**Status:** `provisional | validated | narrowed | superseded`

### Context

What the organization looked like at this point, including relevant milestone/vector and repository boundary.

### Observed problem

What concrete disturbance, missing evidence, unresolved variety, or design ambiguity triggered the change.

### Alternatives considered

What plausible responses were considered. Omit this subsection only when primary evidence does not preserve the alternatives.

### Decision / experiment

What was actually changed, tested, or deliberately left unchanged.

### Evidence

Primary issues, PRs, commits, trials, traces, or repository state.

### Result

What happened next. Preserve negative and ambiguous outcomes.

### VSM interpretation

Map organizational function only after the observed facts establish it. Do not infer autonomy from feature existence, component names, or successful artifact production.

### Reusable lesson

A bounded lesson that may later be tested against other organizations. Avoid universal claims until comparative evidence exists.
```

## 2026-09-16 — Start from one bounded S1 outcome rather than a complete VSM diagram

**Status:** `validated as a construction constraint; autonomy claim still open`

### Context

M0 was defined around one bounded contributor-owned contribution loop with target vector:

```text
A — — — — —
```

Later VSM functions were intentionally not introduced merely to make the organizational diagram complete.

### Observed problem

A full S1–S5 decomposition could be designed prematurely by assigning familiar component names to VSM functions before concrete organizational disturbances existed.

### Decision / experiment

Use one bounded S1 operational outcome as the initial system-in-focus. Treat helper agents, schedulers, runtimes, tests, and subprocesses as supporting machinery unless they independently satisfy the functional/system-boundary criteria for another organizational unit.

### Evidence

- [M0 tracker #2](https://github.com/opensiro/vsm-oss-organization/issues/2)
- `ROADMAP.md`
- `supplementary/design-reasoning.md`

### Result

The repository gained an explicit construction constraint: later S2/S3/S3*/S4/S5 functions must be justified by observed organizational need rather than implementation vocabulary.

This did **not** establish `S1=A`; it only established the intended construction boundary and proof target.

### VSM interpretation

This follows the function-first rule and the OSM-style elimination principle used by this reference organization: begin with the smallest useful operational system and add a function only when residual variety cannot be absorbed by what already exists.

### Reusable lesson

A construction method should distinguish **which organization is being built** from **which VSM functions have actually become necessary**. Starting from the final VSM diagram risks cargo-cult role creation.

## 2026-09-16 — First end-to-end M0 trial demonstrated closure but not durable proof of autonomous ownership

**Status:** `superseded as sufficient proof; retained as operational evidence`

### Context

The first bounded M0 trial used repository consistency work as a real S1 contribution: inspect current scope/release-contract state, repair only justified inconsistencies, validate the result, and produce a reviewable PR.

### Observed problem

The organization needed a real contribution task to test whether the S1 contract could close end to end rather than remaining a paper design.

### Decision / experiment

Run the scope/release-contract audit as a bounded reference trial with explicit local authority and escalation boundaries.

### Evidence

- [trial #14](https://github.com/opensiro/vsm-oss-organization/issues/14)
- [closure PR #15](https://github.com/opensiro/vsm-oss-organization/pull/15)

### Result

The work item inspected repository state, distinguished current drift from intentional historical references, made bounded corrections, validated the result, and produced a reviewable PR without requiring an escalation.

The trial was initially useful as evidence that the operational contribution loop could close. It was later judged insufficient by itself for the stronger `S1=A` claim because repository evidence did not independently prove who owned the decisive local decisions.

### VSM interpretation

Operational closure and ownership of the decisive organizational right are separate evidence questions. A functioning contribution path is necessary evidence for S1 operation but does not by itself identify the autonomous owner.

### Reusable lesson

Do not equate successful automation, issue/PR production, or closed work with organizational autonomy. A reusable methodology needs an explicit ownership witness in addition to outcome closure.

## 2026-09-16 — Instrumented trial separates contribution closure from executor provenance

**Status:** `validated negative finding`

### Context

After the first trial, the M0 proof standard was made stricter. A second trial froze the system-in-focus, start revision, exact role/prompt revision, human constraints, local/forbidden decision rights, escalation conditions, validation requirements, and expected closure before execution.

### Observed problem

GitHub repository artifacts could show what changed and that a bounded loop closed, but ordinary GitHub attribution bound those artifacts to the contributor account rather than independently to the autonomous agent/session that was claimed to own the decisions.

### Decision / experiment

Run an instrumented trial whose explicit purpose was to make the contribution evidence independently reconstructable and then issue a strict `PASS` or `FAIL / INSUFFICIENT` finding rather than optimizing for a positive autonomy result.

### Evidence

- [instrumented trial #16](https://github.com/opensiro/vsm-oss-organization/issues/16)
- [closure PR #17](https://github.com/opensiro/vsm-oss-organization/pull/17)
- updated [M0 tracker #2](https://github.com/opensiro/vsm-oss-organization/issues/2)

### Result

The bounded contribution loop closed and produced a reviewable artifact, but M0 remained `FAIL / INSUFFICIENT for S1=A` because the decisive local decisions could not be independently attributed to the autonomous agent rather than the authenticated human GitHub identity.

The earlier operational evidence was retained; only the stronger inference from that evidence was withdrawn.

### VSM interpretation

The missing evidence concerned **ownership of the decisive S1 right**, not whether supporting machinery existed or whether a PR had been produced. This sharpened the distinction between organizational ownership and transport/execution infrastructure.

### Reusable lesson

A practical autonomous-organization methodology needs to instrument decision provenance early enough that a second reviewer can reconstruct actor ownership. Retrospective self-assertion should not be used to fill an ownership gap.

## 2026-09-16 — Respond to failed autonomy proof by improving evidence and completion contracts, not by weakening `A`

**Status:** `in progress`

### Context

The strict M0 trial produced a useful negative result: closure was visible but ownership was not independently attributable.

### Observed problem

Without additional contracts, future S1 runs could repeat the same ambiguity or depend on ad-hoc human interpretation of whether work was admitted, recovered, completed, or actually performed by the claimed executor.

### Decision / experiment

Create separate workstreams for the missing operational/evidence surfaces rather than changing the autonomy definition:

- executor provenance (#19);
- task admission and routine recovery (#21);
- deterministic completion-oracle work (#20 and children);
- repository-local organization contract consistency (#23, implemented by merged PR #28).

### Evidence

- [#19](https://github.com/opensiro/vsm-oss-organization/issues/19)
- [#20](https://github.com/opensiro/vsm-oss-organization/issues/20)
- [#21](https://github.com/opensiro/vsm-oss-organization/issues/21)
- [#23](https://github.com/opensiro/vsm-oss-organization/issues/23)
- [merged PR #28](https://github.com/opensiro/vsm-oss-organization/pull/28)

### Result

At the time of this entry, the repository has merged the local organization-contract consistency oracle while executor-provenance and task-admission/recovery work remain separate active workstreams.

The completion oracle is explicitly limited to deterministic repository consistency; it does not claim semantic correctness or autonomous ownership.

### VSM interpretation

The response preserves the distinction between:

- decisive organizational rights;
- evidence of who exercised them;
- deterministic machinery that checks or enforces repository invariants.

Supporting validation machinery is not promoted into an autonomous VSM function merely because it improves reliability.

### Reusable lesson

When an autonomy proof fails, improve observability, admission, provenance, and completion evidence before relaxing the organizational criterion. Negative trials can identify missing infrastructure without invalidating the underlying functional distinction.

## 2026-09-17 — Add an empirical S1 artifact track and external OSS harness histories

**Status:** `provisional research program`

### Context

The repository already had a roadmap and a generalized design-reasoning document, but no dedicated record connecting actual decisions and reversals over time, and no structured comparison against organically evolved OSS harness organizations.

### Observed problem

A future practical `vsmlite`/OSM-style methodology could otherwise become a retrospective narrative based only on the final OpenSiro architecture. That would make it difficult to test whether the method actually anticipates or reduces recurring organizational problems.

### Alternatives considered

- keep only a narrative chronology;
- extend `design-reasoning.md` into a combined history/reasoning document;
- create a separate empirical layer with an internal evolution log plus independently reconstructed external case studies.

### Decision / experiment

Create a distinct S1 evidence-production track:

1. maintain this evolution log;
2. reconstruct histories of substantial OSS agent harnesses from primary evidence;
3. compare concrete disturbances and mechanisms before applying VSM interpretation;
4. allow findings to support **or weaken** the future methodology.

External project research remains an S1 artifact-production activity at the current boundary. It does not become S4 merely because the subject is external; a future S4 claim would require an actual outside/future adaptation loop and two-way closure with S3.

### Evidence

- [empirical track #30](https://github.com/opensiro/vsm-oss-organization/issues/30)
- [first external case-study task #31](https://github.com/opensiro/vsm-oss-organization/issues/31)
- `supplementary/case-studies/README.md`

### Result

A separate empirical workstream now exists alongside, rather than inside, the M0–M5 construction roadmap. The first external task prioritizes a substantial OSS harness with a long public history and preferably 100+ contributors when a qualifying evidence-rich case is available.

### VSM interpretation

The empirical program treats VSM as an implementation-independent hypothesis about organizational functions, not as a vocabulary-matching scheme. External histories must establish the disturbance and response first; functional mapping comes afterward.

### Reusable lesson

A construction methodology becomes more credible when it is tested against organizations that evolved without it. The useful question is not whether another project “has VSM,” but whether VSM distinctions help explain, anticipate, or reduce independently observed organizational problems.

## Backfill policy

Important decisions that predate this log may be added later only when primary evidence supports their date, context, and interpretation. Do not infer a historical sequence solely from the current contents of `design-reasoning.md`.
