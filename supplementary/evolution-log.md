# Organizational evolution log

This file records how `vsm-oss-organization` actually evolves over time: observed problems, experiments, decisions, reversals, evidence, and resulting lessons.

It is **descriptive, empirical, non-normative, and supplementary**. It is a side artifact of building and studying the organization, not a primary operational product of the current viable system and not an additional S1 domain. It does not redefine VSM semantics, the VSM Harness Profile, the assessment Methodology, or the roadmap.

Its **primary downstream purpose** is to preserve an auditable evidence base for a future article/case study testing how applying VSM/OSM changed the development process: where organizational problems were exposed earlier, where rework/coordination cost was reduced, where a regulating mechanism appeared sooner than in comparable organically evolved OSS projects, and where no such advantage can be supported. The log must therefore preserve negative results, reversals, timing/rework evidence when available, and alternative explanations rather than reconstructing a success story around the final architecture.

A future separate pipeline may also derive reusable skills, methodology artifacts, or teaching material from this history, but that is a **secondary** downstream use and is not part of the current operational architecture.

Related artifacts:

- `ROADMAP.md` — intended construction sequence and milestone exit criteria;
- `supplementary/design-reasoning.md` — generalized reasoning patterns that survived, failed, or were narrowed;
- this file — the chronological/evolutionary side record used as development evidence for the future article/case study;
- `supplementary/case-studies/` — external OSS histories used as comparative empirical material.

Parent empirical workstream: [#30](https://github.com/opensiro/vsm-oss-organization/issues/30).

## Recording rule

Do not rewrite earlier decisions to make the present design look inevitable.

When later evidence changes an interpretation:

1. preserve the earlier entry;
2. add the later evidence and new decision as a new entry;
3. mark the earlier interpretation `superseded` or `narrowed` where appropriate;
4. keep observed fact separate from VSM interpretation;
5. preserve timing, repeated incidents, rework, blocked iterations, duplicated work, or avoided work when the evidence actually supports those observations;
6. keep plausible non-VSM explanations visible.

The log is not a complete project diary. Record only events that materially affect how a reusable VSM/OSM construction method, or a future empirical claim about its development impact, might be understood.

## Entry schema

Each entry should make the following chain reviewable:

```text
context
→ observed problem / residual variety
→ alternatives considered
→ decision / experiment
→ evidence
→ development cost / timing / rework signal when available
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

Primary issues, PRs, commits, trials, traces, or repository state. Preserve timing/rework/duplicate-work evidence when it is actually reconstructable.

### Result

What happened next. Preserve negative and ambiguous outcomes.

### VSM interpretation

Map organizational function only after the observed facts establish it. Do not infer autonomy from feature existence, component names, or successful artifact production.

### Reusable lesson

A bounded lesson that may later be tested against other organizations. Avoid universal or causal claims until comparative evidence exists.
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

## 2026-09-17 — Close M0 construction from real domain paths rather than synthetic trials

**Status:** `validated construction closure; ownership proof deferred`

### Context

After the S1 boundary was narrowed to Index, Skills, and Awesome, the remaining M0 question was whether each domain had an explicit local authority/completion envelope and a real exercised operating path.

The repository already contained extensive real work in all three domains, while the historical strict M0 proof had separately shown that GitHub repository attribution could not identify the autonomous executor independently from the human account.

### Observed problem

Two failure modes were possible:

1. create synthetic “M0 demo” tasks merely to prove capabilities that had already been exercised in real repository work;
2. close M0 by quietly treating successful repository artifacts as proof of `S1=A`, contradicting the earlier negative executor-ownership finding.

A third practical problem was that domain outcomes and escalation boundaries were distributed across several documents rather than exposed as one portable local contract.

### Alternatives considered

- run three new synthetic trials, one in each S1 repository;
- keep M0 open until the M2 identity mechanism exists, conflating construction sequencing with ownership-proof sequencing;
- use existing real operational evidence, add explicit domain envelopes, and close M0 as a construction/operational milestone while carrying the actor-attribution proof debt forward unchanged.

### Decision / experiment

Add `S1_DOMAIN_CONTRACTS.md` as the canonical local envelope for Index, Skills, and Awesome. Bind `roles/S1.md` and `prompts/contribute.md` to exactly one declared domain per run. Convert `S1_AUTONOMY_COVERAGE.md` from planning language to an operational-closure record.

Use existing real work as evidence rather than manufacturing new tasks:

- Index: `opensiro/vsm-harness-index#114`;
- Skills: `opensiro/vsm-harness-skills#9`, `#11`, `#16`;
- Awesome: `opensiro/awesome-vsm-harness#2`, `#3`, `#4`.

Clarify the milestone semantics in README/ROADMAP: M0 completion establishes the local S1 construction and real operating paths, while the stronger executor-identity witness remains deferred to `#35` / M2.

At the same time, clarify this log's research purpose: its primary downstream is the future evidence-backed article/case study comparing OpenSiro's VSM-guided development with organically evolved OSS organizations. Deriving reusable skills or methodology artifacts is secondary.

### Evidence

- [M0 finalization #50](https://github.com/opensiro/vsm-oss-organization/issues/50)
- [existing operational evidence record #52](https://github.com/opensiro/vsm-oss-organization/issues/52)
- [domain-contract task #53](https://github.com/opensiro/vsm-oss-organization/issues/53)
- [closure-semantics task #54](https://github.com/opensiro/vsm-oss-organization/issues/54)
- [contributor-prompt task #55](https://github.com/opensiro/vsm-oss-organization/issues/55)
- [M0 finalization PR #56](https://github.com/opensiro/vsm-oss-organization/pull/56)
- `S1_DOMAIN_CONTRACTS.md`
- `S1_AUTONOMY_COVERAGE.md`
- `roles/S1.md`
- `prompts/contribute.md`

### Result

M0 now has one explicit operational contract for each of the three S1 domains and real evidence that the domains can produce, validate, correct/recover, and close local work.

No S2/S3/S3*/S4/S5 function was added to obtain that closure. Profile/Organization work remains outside positive S1 evidence.

The earlier negative ownership finding is preserved rather than overwritten: repository attribution still does not independently establish that the autonomous executor owned every decisive local choice. That proof debt remains scheduled for Parent-assisted M2.

For the future article, this transition is itself useful evidence: the construction process rejected a tempting “successful PR = autonomy” shortcut, kept a failed proof visible, narrowed the system boundary, and reused real operational evidence instead of creating benchmark-like demonstrations solely to obtain a positive milestone result. Whether that discipline produced measurable development advantage still requires comparison against external cases.

### VSM interpretation

The closure separates three questions that should not be collapsed:

```text
is there an S1 function?
        ↓
is the local S1 operating contract constructed and exercised?
        ↓
can independent evidence prove who owns the decisive S1 discretion?
```

M0 closes the middle construction question for the three declared domains. The last question remains an autonomy-evidence problem and is not solved by the existence of files, PRs, CI, or a human-attributed GitHub history.

### Reusable lesson

Do not manufacture work to prove an organizational capability when equivalent real operating evidence already exists. At the same time, do not let successful production artifacts erase an unresolved ownership gap. Construction milestones and autonomy-evidence claims can progress on different timelines as long as the distinction is explicit and historically preserved.

## 2026-09-18 — Correct contributor routing after an oracle validated the wrong system boundary

**Status:** `validated reversal; behavioral evidence in progress`

### Context

After M0 construction closure, the organization added a common contributor-routing surface intended to let a contributor or fresh agent arrive through an in-scope repository, distinguish repository-local work from organization-wide work, and discover `vsm-oss-organization` when cross-repository authority, escalation, coordination, or milestone sequencing was involved.

The canonical Organization boundary already listed exactly five in-scope public repositories: Profile, Skills, Index, Awesome, and Organization.

### Observed problem

The first routing implementation generalized the invariant from the declared five-repository system to **every public repository under the `opensiro` GitHub organization**. The resulting live oracle passed across that broader population, but the population itself was wrong: unrelated or separate tracks such as ARCTIC, `terminal-bench-vsm`, and `opensiro.com` had been pulled into the routing/conformance surface solely because they were public organization members.

This produced a concrete negative result: a deterministic check can be internally correct and fully green while validating the wrong system-in-focus if its population-selection rule is not bound to the canonical organizational boundary.

### Alternatives considered

- keep the all-public routing convention as a broader convenience layer while stating that VSM scope remained narrower;
- maintain a second routing allowlist independent of the Organization scope declaration;
- make the routing oracle consume the existing canonical scope declaration directly and remove out-of-scope routing obligations.

### Decision / experiment

Treat the all-public generalization as a boundary error rather than as a harmless navigation layer.

The corrective change:

1. bound contributor routing to the canonical `Current in-scope public repositories:` set;
2. changed the routing oracle to derive its target population from that existing README scope block rather than enumerating every public repository or maintaining a second allowlist;
3. reverted the routing blocks previously added to ARCTIC, `terminal-bench-vsm`, and `opensiro.com`;
4. tightened Organization wording so out-of-scope repositories are not subjects of the routing invariant unless scope is explicitly changed;
5. retained mechanical conformance only as a discoverability check and opened a separate blind-agent behavioral trial for interpretation quality.

The first behavioral batch is deliberately stronger than a single positive-path smoke test: five in-scope start repositories are crossed with both organization-wide and repository-local/ownership-control tasks, for ten frozen runs. Exact prompts are held out until after execution so an agent cannot discover its own answer key while following public links. After a run has made its routing decision, its session experience may be posted to issue #61 as post-run evidence.

### Evidence

- [routing parent #59](https://github.com/opensiro/vsm-oss-organization/issues/59)
- [initial all-public routing/oracle PR #60](https://github.com/opensiro/vsm-oss-organization/pull/60)
- [boundary correction PR #62](https://github.com/opensiro/vsm-oss-organization/pull/62)
- [wording cleanup PR #63](https://github.com/opensiro/vsm-oss-organization/pull/63)
- [blind routing trial #61](https://github.com/opensiro/vsm-oss-organization/issues/61)
- [ARCTIC corrective PR #2](https://github.com/opensiro/arctic-0/pull/2)
- [terminal-bench-vsm corrective PR #3](https://github.com/opensiro/terminal-bench-vsm/pull/3)
- [opensiro.com corrective PR #5](https://github.com/opensiro/opensiro.com/pull/5)
- `CONTRIBUTOR_START.md`
- `ROUTING_CONFORMANCE.md`
- `scripts/check_public_routing.py`

### Result

The corrected mechanical routing surface now checks only the five declared in-scope repositories and reports `5/5` conformance; its unit-test suite covers the scoped population logic. The earlier `8/8` all-public result remains historical evidence of the implementation error and is superseded as routing evidence rather than erased.

The correction caused real rework across multiple repositories: three out-of-scope README changes had to be reverted and the Organization oracle/docs/issues had to be narrowed. That rework is part of the empirical record rather than hidden by the final architecture.

Mechanical conformance is no longer treated as sufficient evidence that an unfamiliar agent will interpret the routing boundary correctly. Issue #61 now owns the behavioral evidence: Batch 001 freezes the five start revisions, exercises positive and negative/control cases, preserves failures, and publishes verbatim prompts only after execution.

### VSM interpretation

The incident is primarily a **system-boundary and evidence-design** failure, not evidence for a new VSM function. GitHub organization membership and public visibility are implementation/container facts; they do not define the viable system-in-focus.

The corrected design reuses the already-declared organizational boundary as the population source for the mechanical oracle. This reduces the chance that support machinery silently expands the organization it is supposed to check.

The move from a static discoverability oracle to blind behavioral trials also separates two claims:

```text
is the route visibly present at the declared boundary?
        ↓
can a fresh agent interpret and follow that route correctly?
```

A green result for the first claim cannot substitute for evidence about the second.

### Reusable lesson

Bind conformance populations to the authoritative system-boundary declaration instead of deriving organizational membership from deployment containers such as a GitHub organization. A validator should not be trusted merely because all of its checks pass; first verify that it is checking the right system.

For empirical methodology work, preserve mistaken expansions and their rollback cost. They provide stronger evidence about where boundary discipline matters than a cleaned-up final architecture alone. When testing human/agent discoverability, keep mechanical presence checks separate from blind behavioral interpretation tests and prevent the test specification itself from becoming part of the agent-visible routing surface before execution.

## 2026-09-19 — Build and then remove the dedicated executor-identity proof layer

**Status:** `validated reversal; earlier executor-identity sequencing superseded`

### Context

The 2026-09-16 provenance trial had left an explicit evidence gap: ordinary GitHub attribution could not independently identify an autonomous executor behind work performed through the contributor account. On 2026-09-17 the organization therefore retained a dedicated executor-identity path as future proof infrastructure while continuing construction work.

During 2026-09-18 and 2026-09-19 that idea progressed from a deferred possibility into a concrete GitHub App implementation path.

### Observed problem

The proof mechanism began to acquire substantial implementation and operational surface area even though the underlying organizational question remained narrower: whether the relevant VSM function and its decisive decision right were established under the governing Profile/Methodology.

A distinct GitHub actor could make technical provenance easier to reconstruct, but the actor identity itself did not create an S1 function, an S3* audit function, or ownership of either function. Requiring a dedicated App as part of the active milestone risked turning one convenient attribution mechanism into an architectural prerequisite that the functional model did not require.

### Alternatives considered

- finish the GitHub App path and require App-attributed natural trials before allowing later milestone progress;
- retain the App/provenance machinery as dormant optional evidence infrastructure while removing it from the milestone gate;
- remove the dedicated executor-identity layer from the active organization and let the selected functional/autonomy methodology determine what ownership evidence is actually required.

### Decision / experiment

The organization first implemented and elaborated the stronger technical-identity path, then deliberately removed it.

The implementation sequence included:

- a GitHub App executor profile, witness schema, evidence publisher, validator, and regression tests in PR #68;
- provisioning/token/bootstrap machinery in PR #69;
- an end-to-end human setup guide in PR #71;
- setup shortcuts in PR #72;
- further consolidation of those shortcuts into the main setup guide in PR #73.

Issue #74 then reconsidered the active proof requirement. PR #75 removed the dedicated GitHub App/executor-provenance machinery and its milestone dependencies; PR #76 removed residual proof-debt language from the active contracts.

The historical M0 trials and their original attribution limitation were not deleted from this evolution log. What changed was the later conclusion that resolving that limitation through a dedicated GitHub identity must remain an active organizational construction requirement.

### Evidence

- [executor-identity task #35](https://github.com/opensiro/vsm-oss-organization/issues/35)
- [cross-domain ownership trial task #66](https://github.com/opensiro/vsm-oss-organization/issues/66)
- [GitHub App executor implementation PR #68](https://github.com/opensiro/vsm-oss-organization/pull/68)
- [provisioning bootstrap PR #69](https://github.com/opensiro/vsm-oss-organization/pull/69)
- [human setup guide PR #71](https://github.com/opensiro/vsm-oss-organization/pull/71)
- [setup-links PR #72](https://github.com/opensiro/vsm-oss-organization/pull/72)
- [setup consolidation PR #73](https://github.com/opensiro/vsm-oss-organization/pull/73)
- [simplification plan #74](https://github.com/opensiro/vsm-oss-organization/issues/74)
- [removal PR #75](https://github.com/opensiro/vsm-oss-organization/pull/75)
- [cleanup PR #76](https://github.com/opensiro/vsm-oss-organization/pull/76)

### Result

At least five merged PRs developed or refined the dedicated executor-identity path before two later PRs removed that path and cleaned its active-contract references. This is direct rework evidence: the final repository alone would hide a non-trivial implementation branch that was explored and then rejected.

The current organization no longer requires a special agent-vs-human GitHub actor-attribution layer for M1. Normal contributor identities may carry work; VSM function and autonomy interpretation remain governed by the selected Profile/Methodology and the concrete decision/feedback paths.

This reversal supersedes the active sequencing assumption in the earlier 2026-09-17 entry “Defer strong executor identity to the Parent-assisted boundary without erasing proof debt” and the corresponding ownership-proof language in the M0 closure entry. Those earlier entries remain historical records of what the organization believed at the time.

A plausible non-VSM explanation remains: this can also be described as ordinary engineering over-specification followed by simplification. The log does not establish that VSM caused the correction or that the same amount of rework would have been avoided by another team.

### VSM interpretation

The reversal sharpened the distinction between **evidence infrastructure** and **organizational function/ownership**. A bot identity, credential path, witness schema, or provenance publisher can improve observability without owning the decisive organizational right that determines S1 or S3* classification.

The exercise therefore produced a negative architectural result: stronger technical attribution was possible, but the organization did not retain it merely to make an autonomy proof look stronger than the selected functional criteria required.

### Reusable lesson

Before hardening a proof mechanism into organizational architecture, ask whether the mechanism is required by the function/ownership claim or merely makes one form of attribution convenient. Evidence infrastructure can accumulate operational cost and become a de facto design commitment even when the organizational function does not depend on it; a reversible construction process should be willing to remove that machinery and preserve the rework record.

## 2026-09-20 — Narrow S3* from autonomous ownership to a constructor target after real audit use

**Status:** `validated narrowing; autonomous S3* deferred until justified by observed variety`

### Context

The organization already had a first-party complementary-audit surface and had exercised it on real work in #44 / PR #45. The audit reconstructed the production claim through materially complementary repository evidence and returned `PASS` without manufacturing a finding.

The earlier roadmap shape still treated the immediate M1 audit target as autonomous S3*, which encouraged a design question about a permanent verifier actor even though the real trial had established the function and path more directly than it had established a need for permanent autonomous ownership.

### Observed problem

Keeping `S3*=A` as the immediate target risked adding a second agent, bot identity, or permanent verifier primarily to satisfy an autonomy vector rather than to regulate observed audit variety.

The real audit evidence supported a narrower claim: a concrete S3* function existed, ordinary reporting was insufficient for the audited claim, materially complementary access was available, a distinct audit judgment was produced, and a material finding had a route toward later current control. It did not demonstrate that the organization currently needed a permanently autonomous S3* owner.

### Alternatives considered

- retain `S3*=A` and construct a permanent autonomous verifier before closing M1;
- remove the S3* milestone claim because no material finding occurred;
- preserve the real S3* function and first-party decision/feedback path as `S3*=C`, and promote it to `A` only if later observed audit variety justifies autonomous ownership.

### Decision / experiment

PR #77 changed M1 so both new metasystem paths are Constructor states:

```text
A — C C — —
```

For S3*, the constructor contract now requires the real audit function, ordinary/complementary evidence distinction, a function-specific judgment surface, feedback for material findings, explicit run-level ownership, and boundary-reachable first-party construction. It explicitly does **not** require a permanent autonomous verifier, separate provider, bot account, or second agent.

The cumulative roadmap retains `S3*=C` through later milestones. `S3*=A` is no longer assumed to be a necessary maturity step; it should be introduced only if future organizational variety establishes that need.

### Evidence

- [real complementary-audit work #44](https://github.com/opensiro/vsm-oss-organization/issues/44)
- [audited evolution-log PR #45](https://github.com/opensiro/vsm-oss-organization/pull/45)
- [M1 tracker #3](https://github.com/opensiro/vsm-oss-organization/issues/3)
- [M1 constructor reframing PR #77](https://github.com/opensiro/vsm-oss-organization/pull/77)
- [roadmap/evidence-state synchronization PR #86](https://github.com/opensiro/vsm-oss-organization/pull/86)
- `S3STAR_AUDIT.md`

### Result

`S3*=C` is now established from the real #44 / PR #45 use plus the first-party constructor surface. M1 remains open only because `S3=C` still lacks one natural current-control transaction.

This is a downward revision of intended autonomy rather than an upgrade. The organization kept the functional audit path while declining to add autonomous ownership solely to complete a richer-looking vector.

A plausible alternative explanation is ordinary scope reduction: the change may reflect removal of an unnecessary implementation requirement rather than a distinctive benefit of VSM. Comparative evidence is still needed before treating the decision as evidence that the methodology reduces development cost.

### VSM interpretation

`A`, `C`, and `P` are ownership arrangements, not a maturity ladder. A real complementary-audit function can be useful and first-party while remaining a Constructor path whose concrete judgment owner is composed per run.

The trial also reinforces that S3* independence is claim-relative and evidence-path based. A separate technical identity or model can support independence, but neither is the organizational function itself.

### Reusable lesson

Do not promote a useful constructor into autonomous ownership just because `A` appears stronger. Let observed residual variety justify the ownership arrangement. A construction roadmap should be able to narrow an autonomy target after real use shows that the function is valuable but permanent autonomous ownership is not yet required.

## 2026-09-20 — Keep M1 open rather than manufacture an S3 current-control disturbance

**Status:** `validated negative screening; S3 constructor evidence remains open`

### Context

After `S3*=C` was established, M1 had one remaining evidence gap: use the existing first-party S3 constructor on a real current exception that exceeds ordinary local S1 authority, then return the decision into affected S1 operation.

The infrastructure already existed. Closing the milestone therefore required evidence of the function in use, not another control-plane artifact.

### Observed problem

Current repository activity offered several superficially plausible events that could have been labeled S3 if the milestone were optimized for closure rather than for functional evidence.

On 2026-09-20 the organization screened three classes of candidate disturbance:

1. upstream Profile/Methodology contract drift — no actual exception existed because the selected contracts remained aligned;
2. stale downstream milestone vectors after PR #77 — a real consistency defect, but repairable as local metasystem/tracker maintenance without a whole-system current-control right returned into S1;
3. Index discovery/candidate concurrency — real concurrent work, but still inside the Index S1 envelope for deduplication, sequencing, validation, and local recovery absent a concrete exception that exceeds that authority.

None satisfied the admission gate for S3.

### Alternatives considered

- reinterpret one of the available defects or concurrent-work cases as S3 so M1 could close immediately;
- inject a fake bug, fake audit finding, or synthetic resource conflict solely to exercise the constructor;
- keep M1 open until a naturally occurring current exception establishes the required whole-system current-control function.

### Decision / experiment

Reject all three screened candidates and create no S3 transaction.

Issue #39 now admits a trial only when a concrete active S1 exception cannot be safely closed under the domain's local authority, the required choice is genuinely current control on behalf of the whole declared system, the whole-system current context and decisive right are reconstructable, and the returned decision can close through the canonical S1 hook.

No synthetic finding or conflict is introduced for milestone completion.

### Evidence

- [M1 S3 trial #39](https://github.com/opensiro/vsm-oss-organization/issues/39)
- [M1 tracker #3](https://github.com/opensiro/vsm-oss-organization/issues/3)
- `S3_CONTROL_SURFACE.md`
- `S1_DOMAIN_CONTRACTS.md`
- 2026-09-20 natural-case screening recorded on #39

### Result

M1 remains open despite having all preparatory constructor machinery on `main`. No current repository event was promoted into S3 merely because it could be routed through the S3 surface.

This is a negative empirical result rather than missing documentation: the organization inspected available candidates and found insufficient evidence for a qualifying S3 transaction at that time.

The choice also avoids a specific kind of benchmark contamination in the development history: a control function is not demonstrated by manufacturing the disturbance that the same milestone requires it to regulate.

### VSM interpretation

Function existence is conditional on organizational variety at the declared boundary. A `manager`, current-control schema, whole-system status view, or callable control surface does not establish S3 until a real inside-and-now disturbance requires a whole-system current-control decision and that decision returns into operation.

The result therefore preserves the elimination principle already used at M0: if local S1 authority can absorb the variety, do not centralize it merely to instantiate another VSM function.

### Reusable lesson

A falsifiable construction method must permit “not yet needed” as an outcome. Milestone pressure should not convert ordinary local recovery or synthetic incidents into positive evidence for a metasystem function. Preserve rejected candidate events and the reason for rejection; they are evidence about the method's admission discipline, not failed progress.

## 2026-09-20 — Reconstruct an earlier scope decision as a parent-governed S5 witness without rewriting its chronology

**Status:** `validated retrospective witness; chronology caveat retained`

### Context

The 2026-09-18 routing correction had already established an important fact: the governed VSM Harness OSS system should remain bounded to Profile, Skills, Index, Awesome, and Organization rather than expand automatically to every public `opensiro/*` repository.

That event had been recorded in this log as a system-boundary/evidence-design reversal, not as an S5 claim. By 2026-09-20 the M2 design work separately asked what a genuine parent-governed identity/ultimate-policy closure would require.

### Observed problem

The organization needed an S5 witness, but creating a fresh policy controversy merely to exercise the M2 path would repeat the same synthetic-evidence problem avoided for S3.

The historical scope correction already had much of the functional topology of S5: it changed the system-in-focus and returned that scope choice into routing, conformance, workflow, and trial populations. What was not contemporaneously explicit was whether the concrete decision owner was the legitimate parent for this recursion. GitHub authorship or merge authority alone was insufficient to establish that point.

### Alternatives considered

- treat PR #62 as `S5=P` solely because the repository owner/maintainer authored or merged the correction;
- ignore the historical case and wait for a new identity/policy event after the M2 contract was written;
- define the parent-authority contract, reconstruct legitimate ownership from primary Organization governance evidence, and use the earlier event only if that missing ownership link could be made reviewable without pretending the later contract existed in 2026-09-18.

### Decision / experiment

PR #83 added the first-party S5 parent-boundary contract but deliberately made no positive S5 claim from infrastructure alone.

PR #84 then made the current legitimate parent role explicit — the OpenSiro organization owner — and recorded `S5-P-001` as a retrospective reconstruction of #59 / PR #62. The record preserves the actual dates: the scope decision closed on 2026-09-18; explicit parent-legitimacy attribution and the formal witness were added on 2026-09-20.

The returned decision is concrete: the bounded system remains the five declared repositories, and the routing oracle, conformance surface, and blind-trial population consume that boundary. The earlier all-public `8/8` evidence remains superseded.

Supporting tool-entry work in PR #85 is kept separate from the S5 decision itself; permissions and connectors may enforce delegated capability but do not become S5 merely because a parent authorizes them.

### Evidence

- [routing scope parent #59](https://github.com/opensiro/vsm-oss-organization/issues/59)
- [scope correction PR #62](https://github.com/opensiro/vsm-oss-organization/pull/62)
- [M2 S5 workstream #81](https://github.com/opensiro/vsm-oss-organization/issues/81)
- [parent-boundary implementation PR #83](https://github.com/opensiro/vsm-oss-organization/pull/83)
- [parent authority and witness PR #84](https://github.com/opensiro/vsm-oss-organization/pull/84)
- [external-tool entry PR #85](https://github.com/opensiro/vsm-oss-organization/pull/85)
- `S5_PARENT_BOUNDARY.md`
- `S5_PARENT_AUTHORITY.md`
- `records/s5/2026-09-18-routing-scope-correction.md`

### Result

The repository now has a positive parent-governed S5 witness without manufacturing a new policy event. `S5=P` is established for the M2 evidence component, while formal M2 completion remains sequenced after M1 because the inherited `S3=C` state is still open.

The witness is intentionally retrospective rather than backdated. The later parent-authority declaration makes the earlier ownership relation reconstructable; it does not alter the fact that the explicit contract and formal classification were created two days after the underlying scope decision.

A plausible alternative explanation is ordinary governance formalization after the fact. The case does not by itself show that VSM caused the correct boundary decision; its empirical value is that the method can distinguish the functional event, the legitimate decision owner, the return path, and the later act of making those facts reviewable.

### VSM interpretation

Construction sequence and evidence-discovery sequence need not be identical. A real organizational function may occur before the repository has the vocabulary or record template used later to recognize it, provided retrospective classification does not invent missing ownership or closure evidence.

For this case the S5 matter is the identity/system-scope decision, not the PR, GitHub ownership permission, routing oracle, or connector machinery. `P` records that the decisive S5 right belongs to the legitimate parent at this recursion and returns into the child organization's subsequent operation.

### Reusable lesson

Prefer reconstructing a real earlier event over manufacturing a new one when the primary evidence can establish the missing functional and ownership links. Preserve the chronology of recognition: later formalization may make an earlier event classifiable, but it must not be written as if the later governance contract already existed at the time.

## Backfill policy

Important decisions that predate this log may be added later only when primary evidence supports their date, context, and interpretation. Do not infer a historical sequence solely from the current contents of `design-reasoning.md`.