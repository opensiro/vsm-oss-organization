# Organizational evolution log

This file records how `vsm-oss-organization` actually evolves over time: observed problems, experiments, decisions, reversals, evidence, and resulting lessons.

It is **descriptive, empirical, non-normative, and supplementary**. It is a side artifact of building and studying the organization, not a primary operational product of the current viable system and not an additional S1 domain. It does not redefine VSM semantics, the VSM Harness Profile, the assessment Methodology, or the roadmap.

Its purpose is to preserve enough historical evidence that later practical methodology can be derived from what happened rather than reconstructed around the final architecture. A future separate pipeline may derive reusable skills or methodology artifacts from this history, but that pipeline is planned only and is not part of the current operational architecture.

Related artifacts:

- `ROADMAP.md` — intended construction sequence and milestone exit criteria;
- `supplementary/design-reasoning.md` — generalized reasoning patterns that survived, failed, or were narrowed;
- this file — the chronological/evolutionary side record from which such reasoning may later be generalized;
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

## 2026-09-17 — Consume the Profile compatibility facade instead of duplicating active contract facts

**Status:** `validated infrastructure decision`

### Context

The Organization originally repeated active Profile and Methodology versions in several local documents. Its repository-local validator could prove that those copies agreed with each other while the actual upstream Skills/Index state had already moved.

Profile `v0.2.2` introduced a downstream consumer contract and release-impact history that separates immutable provenance from compatibility with later Profile releases.

### Observed problem

Local consistency was not enough to prove upstream consistency. A downstream repository could remain internally coherent while silently consuming stale semantic/procedural facts, and a simple version bump risked being treated as an automatic reassessment trigger even when the authoritative Profile declared no assessment impact.

### Alternatives considered

- continue manually updating current versions in multiple Organization documents;
- query mutable upstream state ad hoc without one local selection record;
- select upstream contract surfaces once in a machine-readable Organization manifest and validate that selection directly against the authoritative repositories.

### Decision / experiment

Adopt one local upstream-selection manifest and cross-repository completion oracle.

`UPSTREAM_CONTRACT.json` selects released Profile `v0.2.2`, Methodology `0.3.1` from an exact Skills commit, and the current Index active-contract surface. The validator follows the Profile release-impact chain rather than treating version-string inequality as semantic migration.

### Evidence

- [consumer task #33](https://github.com/opensiro/vsm-oss-organization/issues/33)
- [merged PR #34](https://github.com/opensiro/vsm-oss-organization/pull/34)
- `UPSTREAM_CONTRACT.json`
- Profile `v0.2.2` `CONSUMER_CONTRACT.md` and `RELEASE_IMPACT.json`

### Result

Organization now validates selected Profile/Methodology/Index state against upstream source-of-truth surfaces. The Index may retain Profile `0.2.1` assessment provenance while Organization consumes Profile `0.2.2` because the authoritative `0.2.1 → 0.2.2` transition is `compatible` with `assessment_impact: none`.

Current-version prose is no longer the authority merely because several local files repeat it.

### VSM interpretation

This change strengthens provenance, transduction, and deterministic support/enforcement around the organizational contracts. It does not establish a new S-function or transfer semantic authority into Organization.

### Reusable lesson

Separate **which exact contract produced an artifact** from **whether that artifact remains compatible with a later contract**. Version freshness and semantic migration are different questions; downstream systems should consume an explicit compatibility signal rather than infer organizational impact from version numbers alone.

## 2026-09-17 — Defer strong executor identity to the Parent-assisted boundary without erasing proof debt

**Status:** `narrowed implementation sequence; proof remains open`

### Context

The executor-provenance and S1 admission/recovery contracts were implemented after the negative M0 trial, but ordinary GitHub actions still expose the contributor account rather than an independently distinguishable autonomous executor identity.

A concrete GitHub App/bot path was identified as a possible stronger witness, while Parent-assisted M2 was already planned to make parent authority, delegated capability, intervention, revocation, and external enforcement boundaries explicit.

### Observed problem

Implementing a distinct technical identity immediately would solve only part of the evidence problem. It would still leave implicit who may authorize the App, expand its permissions, revoke it, distinguish human-delegated from agent-specific credentials, and admit external ChatGPT plugins/connectors into the organization.

At the same time, simply postponing the mechanism could accidentally be read as if the negative M0 ownership finding had disappeared.

### Alternatives considered

- implement a GitHub App during M0 and treat the technical identity as sufficient;
- block all later design work until the identity mechanism exists;
- defer the concrete identity/enforcement implementation to Parent-assisted M2 while preserving the strict M0 ownership gap explicitly as proof debt.

### Decision / experiment

Move the concrete executor-identity task to M2 and make external-tool admission a companion Parent-assisted workstream.

- #35 now covers binding agent execution to a distinct GitHub identity with explicit parent authorization/revocation and run/session binding;
- #36 defines a general plugin/tool entry contract with GitHub as the first reference case;
- M2 tracker #4 records both tasks together with the later replacement of the temporary owner-only `main` guardrail;
- M0 tracker #2 continues to state `FAIL / INSUFFICIENT` for the strict `S1=A` proof from the executed evidence.

### Evidence

- [M0 tracker #2](https://github.com/opensiro/vsm-oss-organization/issues/2)
- [M2 tracker #4](https://github.com/opensiro/vsm-oss-organization/issues/4)
- [executor-identity task #35](https://github.com/opensiro/vsm-oss-organization/issues/35)
- [plugin/tool entry task #36](https://github.com/opensiro/vsm-oss-organization/issues/36)
- `EXECUTOR_PROVENANCE.md`

### Result

Preparatory work on later organizational layers can continue, but it cannot cite M0 as an established autonomous-ownership proof. The stronger external identity witness remains an explicit debt that must be revisited when Parent-assisted capability boundaries are implemented.

The planned GitHub App/plugin machinery is treated as identity, transport, and enforcement support. No new chatbot/model is required by this decision.

### VSM interpretation

A GitHub App, plugin connection, credential broker, or bot identity is not S1 or S5 merely because it carries authority. M2 may use such mechanisms to enforce a parent-governed policy/identity boundary, but the S5 mapping still requires a genuine identity/ultimate-policy issue, legitimate parent decision, and returned closure into subsequent operation.

### Reusable lesson

Proof sequencing and implementation sequencing can differ, but the gap must remain visible. Deferring stronger evidence is safer than weakening the criterion only when the organization records the unresolved proof debt and prevents later artifacts from silently inheriting the unproved claim.

## 2026-09-17 — Prepare complementary audit and current-control paths before claiming M1

**Status:** `provisional implementation; functional proof open`

### Context

M0 work established that deterministic completion checks improve reliability but do not settle every evidence interpretation or omitted-fact risk. The next roadmap target requires complementary S3* audit plus a first-party S3 current-control constructor path.

At the time this work began, the repository had only the S1 role; no pre-existing S3/S3* role was treated as authoritative merely because the roadmap named future functions.

### Observed problem

A routine verifier or repeated CI run would not provide materially complementary access to operational reality. Conversely, an audit finding alone would not close anything if it had no S3-specific path capable of returning a current-control decision into later S1 operation.

There was also a category-error risk: adding a generic `manager`, mailbox, JSON object, or second model could look like M1 implementation without establishing either function.

### Decision / experiment

Implement the two preparatory paths separately before running a reference trial.

PR #41 added `S3STAR_AUDIT.md`, a bounded S3* role, audit record, and portable prompt. Independence is claim-relative: complementary evidence access matters; using a different model/provider is neither necessary nor sufficient by itself.

PR #43 added `S3_CONTROL_SURFACE.md`, a machine-readable S3-specific request/decision/return transaction, a reviewable record, application prompt, and an explicit S1 return hook. No autonomous S3 role was created; the actual decision owner must be supplied and evidenced per transaction.

### Evidence

- [M1 tracker #3](https://github.com/opensiro/vsm-oss-organization/issues/3)
- [S3* path #37](https://github.com/opensiro/vsm-oss-organization/issues/37)
- [S3* implementation #40](https://github.com/opensiro/vsm-oss-organization/issues/40)
- [merged PR #41](https://github.com/opensiro/vsm-oss-organization/pull/41)
- [S3 constructor path #38](https://github.com/opensiro/vsm-oss-organization/issues/38)
- [constructor implementation #42](https://github.com/opensiro/vsm-oss-organization/issues/42)
- [merged PR #43](https://github.com/opensiro/vsm-oss-organization/pull/43)
- `S3STAR_AUDIT.md`
- `S3_CONTROL_SURFACE.md`

### Result

Both preparatory paths now exist on `main` and pass the Organization cross-repository consistency workflow. #37 and #38 are closed as implementation workstreams; #39 remains open for actual end-to-end evidence.

Their presence does not establish `S3*=A` or `S3=C`. A real use must still establish the audited claim/risk, complementary access and audit judgment, or the whole-system current-control function and returned closure respectively. Formal agent-ownership claims also retain the executor-identity limitation recorded in #2/#35.

### VSM interpretation

The work keeps the functions distinct:

```text
S3* complementary evidence access
        ↓
independent audit judgment
        ↓ finding
S3 current-control decision path
        ↓
returned constraint/intervention
        ↓
subsequent S1 operation
```

The audit role does not inherit S3 authority, and the constructor surface does not own its decision. Supporting transport and deterministic enforcement remain separate from the organizational right they carry.

### Reusable lesson

Before claiming a new VSM function, implement and test the **specific feedback/decision path** that would close it, while keeping ownership explicit. Separate functional construction from autonomy proof: files, role names, model diversity, and transport primitives are preparation, not evidence that the function is already enacted.

## 2026-09-17 — Separate the three operational S1 domains from the normative/metasystem plane

**Status:** `narrowed system boundary`

### Context

Earlier M0 artifacts treated a wide range of repository work as possible S1 activity, including Profile maintenance, Organization/control-plane maintenance, and a supplementary empirical artifact track. The roadmap also described multi-S1 operation as something introduced only at M4.

At the same time, the actual ecosystem already exposed three durable operational product domains with their own environments and local variety: Index, Skills, and Awesome.

### Observed problem

The broad S1 boundary mixed production of operational outcomes with work that changes the rules or autonomy structure of the viable system itself.

That created two problems:

1. metasystem work could be counted as evidence of S1 autonomy merely because it produced a repository artifact;
2. later S2 reasoning was distorted because the roadmap implied multiple S1 units did not exist until M4, even though three operational domains already existed structurally.

The empirical evolution log also risked becoming a fourth operational product merely because it was useful and durable, despite being a record *about* construction rather than part of the primary VSM Harness knowledge production transformation.

### Alternatives considered

- keep all five repositories as candidate S1 work surfaces and classify task-by-task;
- treat Profile as another operational S1 because it is a repository with maintainable artifacts;
- separate operational products from normative/metasystem construction and define the current S1 plane explicitly as Index, Skills, and Awesome.

### Decision / experiment

Adopt three explicit operational S1 domains:

```text
operational S1 plane
├── Index
├── Skills
└── Awesome
```

Treat:

- `vsm-harness-profile` as the authoritative normative semantic source consumed by the organization, outside the current operational S1 plane;
- `vsm-oss-organization` as the surface where metasystem/control functions are constructed and evidenced, also outside the operational S1 plane.

Do **not** infer that Profile is automatically S5 or that Organization is automatically S2–S5. Concrete functions still require function-first evidence.

Keep local variety at the S1 domain with the requisite information and delegated authority. Only residual variety that cannot be safely absorbed locally should motivate later metasystem functions.

Update M4 accordingly: the three S1 domains already exist from M0; M4 is the point where autonomous S2 is added only if concrete interference among those domains requires coordination.

Classify this evolution log itself as a **supplementary side artifact**. It preserves evidence about how the organization was built but is not a primary operational outcome and does not create another S1 domain.

A possible future pipeline that derives reusable skills or methodology artifacts from development history remains planned only and is deliberately absent from the current architecture.

### Evidence

- [boundary work #48](https://github.com/opensiro/vsm-oss-organization/issues/48)
- `ORGANIZATION.md`
- `roles/S1.md`
- `S1_AUTONOMY_COVERAGE.md`
- `ROADMAP.md`
- `README.md`
- this log header/current entry

### Result

The system boundary now distinguishes operational production from normative/metasystem construction:

```text
Profile ─────── normative semantics
                  │
Organization ── metasystem/control construction
                  │
            ┌─────┼─────┐
            ▼     ▼     ▼
          Index Skills Awesome
            S1    S1    S1
```

M0 can now focus on local autonomy inside those three domains without treating changes to the organization's own autonomy machinery as S1 evidence. Later functions are justified from residual variety rather than from repository membership or a desire to complete the VSM diagram.

The earlier 2026-09-17 entry that described the empirical history work as a distinct S1 evidence-production track is therefore **narrowed by this later boundary decision**. Its historical rationale is preserved, but the current classification of the evolution log is supplementary, not operational S1.

### VSM interpretation

This applies the operations/metasystem distinction and the requisite-variety rule at the declared recursion level. Operational units should absorb the local variety for which they have information and authority; central/metasystem mechanisms should not duplicate those decisions merely to centralize command.

The change does not itself establish S2, S3, S3*, S4, or S5. It makes the evidence boundary cleaner so later functions can be introduced only when a concrete residual disturbance requires them.

### Reusable lesson

Define operational outcomes before counting autonomous units. A durable artifact is not automatically an S1 product: ask whether it enacts the parent system's primary transformation or instead records, constrains, or redesigns how that transformation is organized.

## Backfill policy

Important decisions that predate this log may be added later only when primary evidence supports their date, context, and interpretation. Do not infer a historical sequence solely from the current contents of `design-reasoning.md`.