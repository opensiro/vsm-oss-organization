# OpenHands runtime organizational evolution case study

Parent workstream: [#30](https://github.com/opensiro/vsm-oss-organization/issues/30)  
Case-study task: [#88](https://github.com/opensiro/vsm-oss-organization/issues/88)

## Scope

**Project:** current canonical repository [`OpenHands/OpenHands`](https://github.com/OpenHands/OpenHands), historically developed as OpenDevin / under the All-Hands-AI organization.  
**Historical interval examined:** April–August 2024.  
**Current canonical source snapshot reviewed for repository identity:** `OpenHands/OpenHands@a07364828c8f202e7745c6bce3dcef3915ae7ac1`.

The historical implementation names in this document (`SSHBox`, `ServerRuntime`, `EventStreamRuntime`, `od-runtime-client`) are preserved from contemporaneous evidence. This case does not claim that the exact 2024 class topology remains current in 2026.

This case is useful because the public record exposes a relatively complete replacement sequence:

```text
external/runtime variety
        ↓
old SSH assumption becomes limiting
        ↓
partial compatibility work
        ↓
replacement runtime built without immediate cutover
        ↓
integration + evaluation evidence
        ↓
old runtime removed / replacement made default
```

Unlike the AutoGen case, which has strong evidence of coordination pressure but weaker closure evidence, this transition provides explicit staged validation before a default switch.

This is supplementary empirical evidence, not a VSM Harness Index assessment. It does not assign OpenHands an autonomy vector.

## Research question

> When the SSH-coupled runtime boundary became incompatible with user-provided images and hosted execution, how did OpenDevin/OpenHands move from local compatibility fixes to an architectural replacement, and what evidence was used before retiring the old runtime?

A second question is methodological:

> Does VSM add useful distinctions between environmental adaptation, validation/support, and current-control decisions in this history, or can ordinary architecture-evolution language explain the evidence just as well?

## Baseline condition

The early OpenDevin runtime used an SSH-dependent path between backend/runtime and sandbox. That assumption worked with project-controlled sandbox images but became a constraint when the environment expanded.

Two external/operational pressures are directly visible before the refactor issue:

1. **User-provided images.** Issue [`#1387`](https://github.com/OpenHands/OpenHands/issues/1387), opened 2024-04-26, states that users needed their own sandbox images for languages/tools absent from the default image, while `SSHBox` assumed `sshd` was present. Standard language images such as `node` and `go` often did not satisfy that assumption.
2. **Hosted operation.** Issue [`#1086`](https://github.com/OpenHands/OpenHands/issues/1086), opened 2024-04-14, says installation difficulty was a major problem and proposes a hosted demo, explicitly raising where agents should run as an unresolved hosting question.

The relevant system boundary in this case is the public OpenDevin/OpenHands product-development effort around runtime execution. The user-created agent running inside the product is not the organizational system-in-focus for this case.

## Timeline

| Period | Observed condition / disturbance | Primary evidence | Response / mechanism | Observed consequence | VSM interpretation | Confidence / alternatives |
| --- | --- | --- | --- | --- | --- | --- |
| 2024-04-14 | Users had installation difficulty; a hosted service would need a different answer to where agents execute. | [`#1086`](https://github.com/OpenHands/OpenHands/issues/1086) | Hosted-demo workstream proposed. | Hosted execution became an explicit product/environment requirement. | External/environmental variety is visible; no S4 owner is established. | High confidence in stated need; this issue alone does not imply an architectural function. |
| 2024-04-26 | User-provided sandbox images conflicted with the assumption that `sshd` existed in the image. | [`#1387`](https://github.com/OpenHands/OpenHands/issues/1387) | Proposed making SSH installable at runtime. | A local compatibility path was considered while preserving the SSH model. | Local adaptation/repair to a concrete environment mismatch. | High confidence. This is not yet evidence that the old runtime boundary itself would be replaced. |
| 2024-05-27 → 2024-06-20 | Plugins were coupled to assumptions in the sandbox image. | merged PR [`#2101`](https://github.com/OpenHands/OpenHands/pull/2101) | Introduced sandbox-agnostic plugin setup using an isolated Miniforge environment and image modification. | Agent-skill/Jupyter plugins were demonstrated on Ubuntu 18 / Debian 12 images, but the implementation explicitly retained SSH as a temporary requirement. | Partial attenuation of environmental variety; not final architectural closure. | High confidence, including negative evidence: the PR itself contains a FIXME to remove SSH later. |
| 2024-06-12 | Maintainer states backend SSH communication conflicts with the EventStream direction, complicates arbitrary images and hosted deployment. | [`#2404`](https://github.com/OpenHands/OpenHands/issues/2404) | Explicit architecture-refactor plan: runtime client inside the sandbox, EventStream communication, image-agnostic setup, plugin consolidation, testing, evaluation, then removal of `ServerRuntime`. | Previously separate pressures were converted into one staged replacement plan with explicit exit steps. | Strong evidence of an adaptation/control construction path; ownership/autonomy still unproven. | High confidence in project-native rationale and planned closure. |
| 2024-06-23 → 2024-07-08 | Replacement mechanism existed conceptually but had not yet earned cutover. | merged PR [`#2603`](https://github.com/OpenHands/OpenHands/pull/2603) | Added the EventStream/runtime-client path. The PR explicitly says it does **not** replace the current architecture yet and lists unresolved testing/network/init/output issues. | Replacement could coexist with the old path while deficiencies remained visible. | Important negative evidence: implementation existence was not treated as sufficient closure. | High confidence. |
| 2024-07-30 → 2024-08-01 | New runtime needed comparable integration behavior before broader migration. | merged PR [`#3184`](https://github.com/OpenHands/OpenHands/pull/3184) | Added multi-runtime integration-test support/workflow and fixed EventStreamRuntime-specific failures. | Integration validation became a first-party gate before evaluation/default migration. | Validation is support/evidence, not automatically S3* or the decision owner. | High confidence. |
| 2024-08-02 → 2024-08-06 | Evaluation code still depended on old runtime/global config assumptions. | merged PR [`#3230`](https://github.com/OpenHands/OpenHands/pull/3230) | Migrated evaluation harness to EventStreamRuntime, structured outputs, removed workspace mounting for easier parallelization, and manually verified many benchmark suites. | Broad evaluation evidence existed, while the PR also preserved untested/incompatible cases instead of claiming universal parity. | Evaluation acts as evidence supporting a later replacement decision; tests/benchmarks do not become S3* merely by validating. | High confidence in recorded verification; no claim that every benchmark was fully validated. |
| 2024-08-07 → 2024-08-08 | Replacement path had passed the staged project checks used for cutover. | merged PR [`#3271`](https://github.com/OpenHands/OpenHands/pull/3271) | Removed persistent sandbox, Sandbox/ServerRuntime and workflows; switched default to `EventStreamRuntime`; repaired affected GUI/backend paths. | The old runtime path was retired and the new path became the product default. #2404 closed completed minutes later on 2024-08-08. | Observable closure of the architectural replacement. The decisive organizational right/owner is not fully reconstructed from this evidence. | High confidence in implementation closure; autonomy classification remains unsupported. |

## Detailed transition 1 — environment variety exposes the SSH boundary

### Observed facts

Issue #1387 does not describe an abstract architecture preference. It identifies a concrete mismatch: OpenDevin wanted users to bring sandbox images containing their own language/tool environments, but `SSHBox` assumed `sshd`. Standard language images often did not include it.

The initial response was incremental: make SSH a plugin/installable dependency. PR #2101 then pushed further by making plugins more sandbox-agnostic through an isolated Miniforge environment and generated image modifications.

Crucially, PR #2101 still installed `openssh-server`, and its code included a FIXME to remove the SSH requirement in a future version. The project had attenuated one source of image variability without removing the deeper coupling.

Separately, #1086 established another pressure: installation difficulty motivated a hosted version, which required answering where remote agents/runtimes would execute.

### Organizational reconstruction

The relevant disturbance can be expressed without using VSM vocabulary:

```text
project-controlled sandbox assumptions
        ↓
new environment asks for arbitrary images + hosted execution
        ↓
SSH-specific backend knowledge leaks into deployment/runtime choices
        ↓
local compatibility work becomes increasingly conditional
```

The important fact is not that a component was called `SSHBox`. It is that environment variety exceeded the assumptions encoded at the runtime boundary.

### Response

Issue #2404, opened 2024-06-12, explicitly connects the two pressures. It says SSH does not fit the EventStream-based communication model and makes both different runtime/images and hosted operation harder.

The proposed replacement placed a small runtime client inside the sandbox and moved command/action communication onto the event path. Its checklist went beyond implementing transport:

- arbitrary user image support;
- browser/plugin relocation;
- IPython/agent-skills support;
- reduced dependency/build burden;
- sandbox/integration tests;
- evaluation-suite checks, including SWE-bench;
- final deprecation/removal of `ServerRuntime`.

This makes #2404 stronger evidence than a generic architecture roadmap: it defines both the disturbance and a closure sequence.

### Consequence

Within roughly eight weeks of #2404 opening, the project merged the runtime-client implementation, integration test support, evaluation migration, and final default switch/removal of the previous runtime.

This interval is observable. It should not be interpreted as a causal claim that the issue itself made development fast, nor as a comparison score against OpenSiro.

### VSM interpretation

The record is compatible with **external/future adaptation pressure** because product/environment conditions (arbitrary images and hosted execution) forced the project to reconsider a current architectural boundary.

That is not enough to classify `S4=C` or `S4=A`. The reviewed evidence does not establish, under the OpenSiro Profile:

- a declared organizational S4 system boundary;
- the decisive adaptation right;
- who owned that right as an organizational function rather than contributing/maintaining code;
- a complete option-generation record and two-way S3/S4 ownership relation.

Ordinary architecture-evolution language already explains much of the sequence. VSM is useful only insofar as it forces a distinction between the **environmental signal**, the **adaptation option**, the **validation machinery**, and the **decision to alter current capability**.

## Detailed transition 2 — implementation is deliberately separated from cutover

### Observed facts

PR #2603 is especially useful negative evidence. It implements the new runtime-client/EventStream path but says explicitly that it does not replace current OpenDevin architecture yet and that cutover can happen only after remaining problems are fixed.

The PR records unresolved items including:

- further read/write/browse/recall testing;
- Linux/Mac network mapping;
- websocket initialization behavior;
- formalizing integration/mock tests;
- output formatting issues.

This means the project did not equate “new path exists” with “new path owns production.”

### Organizational reconstruction

The transition contains three distinct roles that are easy to collapse if one reasons from implementation names:

```text
replacement capability exists
        ≠
replacement is sufficiently evidenced
        ≠
organization selects replacement as current default
```

PR #2603 closes the first relation, #3184/#3230 add evidence for the second, and #3271 performs the third at the repository/product level.

### Response and evidence gates

PR #3184 added support for integration tests using multiple runtimes and fixed concrete EventStreamRuntime problems required to make those tests pass. The PR author explicitly postponed the evaluation cutover to a separate PR because the integration change was already large.

PR #3230 then moved the evaluation harness to EventStreamRuntime. It recorded manual verification across SWE-bench, AgentBench, BioCoder, BIRD, GAIA, GPQA, HumanEvalFix, MiniWob, MINT and others.

The same PR also preserved incomplete evidence:

- Gorilla and ToolQA were refactored but not tested due to missing dependency information;
- MLBench had an incompatible image and was deferred;
- WebArena was refactored but untested due to a hosting issue.

This is methodologically valuable because the record does not convert partial coverage into an unsupported universal-parity claim.

Finally, PR #3271 removed the persistent sandbox, old Sandbox/ServerRuntime and associated workflows, repaired backend paths affected by the new runtime, and switched the default.

### Consequence

The replacement has a reviewable closure event rather than only an adopted proposal:

```text
old runtime path present
        ↓
parallel replacement implementation
        ↓
integration evidence
        ↓
evaluation evidence with explicit gaps
        ↓
old runtime deleted
        ↓
new runtime becomes default
```

Issue #2404 closed as completed immediately after the final switch.

### VSM interpretation

This sequence illustrates why **support/evidence machinery must be separated from organizational decision ownership**.

Integration tests and benchmark suites provide evidence about operational reality. They do not automatically become S3*:

- no complementary-audit organizational function is established merely because tests are independent of the new runtime implementation;
- no independent audit judgment owner/feedback path is established from the test existence alone.

Likewise, PR #3271 contains a current product-control choice—change the default and remove the old path—but the evidence sampled here does not establish the whole-system current-control owner/authority relationship required to classify formal S3 ownership.

The bounded lesson is therefore structural, not classificatory: evidence collection, evidence interpretation, and the authority to cut over should be kept distinct when reconstructing organizational control.

## Negative and incomplete evidence

This case is stronger if the unresolved evidence is retained.

1. **#2101 did not solve SSH coupling.** It improved image/plugin portability while still installing SSH and explicitly marking SSH removal as future work.
2. **#2603 did not justify immediate replacement.** Its author explicitly preserved the old architecture and listed unresolved testing/behavior issues.
3. **#3230 did not establish universal evaluation parity.** Several suites were untested or incompatible at merge time.
4. **The decisive owner is not reconstructed.** PR authorship, assignees, review, or merge rights do not by themselves establish a VSM organizational owner.
5. **No quantitative development-cost reduction is available.** Commit counts, changed files, or elapsed time show work volume/time but do not prove savings versus a counterfactual architecture.
6. **The exact 2024 runtime topology may evolve later.** The case establishes a historical transition, not permanence of class names through current main.

## Empirical significance for the OpenSiro construction method

### What VSM distinguished usefully

This case makes four evidence categories unusually clear:

```text
external/environment variety
        ↓
adaptation proposal / replacement capability
        ↓
validation and operational evidence
        ↓
current-capability/default decision
```

OpenSiro's function-first discipline is useful here because common shortcuts would misclassify the evidence:

- `Runtime` is not automatically S3;
- integration/evaluation tests are not automatically S3*;
- architectural planning is not automatically S4;
- a maintainer/PR author is not automatically the owner of the corresponding VSM function.

### Possible anticipatory value

An elimination-style construction process could have asked, as soon as #1387 and #1086 were simultaneously visible:

> Is installing SSH into more image variants still an adequate local repair, or has the environment changed enough that the runtime boundary itself should be adapted?

That is a sharper question than “how do we make SSHBox support another image?” because it distinguishes absorbing local variety from revising the operating boundary.

The public record shows the project independently reached that broader question in #2404. It does not establish that VSM would have reached it earlier or more cheaply.

### Observable cost / effort signals

The record supports bounded effort observations, not a cost model:

- PR #2101 contained 55 commits and still preserved the SSH dependency;
- PR #2603 contained 31 commits and intentionally stopped short of cutover;
- PR #3184 was very large (183 commits / 369 changed files in GitHub metadata), and its author explicitly deferred the evaluation switch to a later PR;
- PR #3230 then changed 78 files while migrating/refactoring the evaluation harness;
- some evaluation suites remained untested/incompatible at that point;
- PR #3271 finally removed substantially more code than it added when retiring the old path.

These are reviewable signs of a non-trivial migration. They do not establish that another organizational method would have required fewer commits or less calendar time.

### Where ordinary engineering language is enough

A conventional explanation is strong:

> The old runtime was too coupled to SSH; maintainers introduced a new runtime protocol, tested it, migrated evaluations, and cut over once it was ready.

VSM should not replace that explanation. Its additional value is only in preserving distinctions that are useful for later comparison:

- environment vs current operation;
- local repair vs boundary adaptation;
- validation evidence vs audit ownership;
- implementation readiness vs authority to switch current operation.

If cross-case comparison does not show these distinctions predicting or avoiding anything useful, then the VSM framing has not demonstrated practical advantage.

## Comparison with the AutoGen case

The first two cases intentionally expose different evidence shapes.

| Dimension | AutoGen multimodal case | OpenHands runtime case |
| --- | --- | --- |
| Initial disturbance | incompatibilities across multimodal/text agents, message forms and workflows | runtime boundary assumption (`sshd`) conflicts with arbitrary images and hosted execution |
| First broad response | roadmap/epic consolidates scattered work and alternatives | explicit architecture-refactor issue defines replacement plus exit sequence |
| Partial/local responses | several quick fixes/capability/message PRs | sandbox/plugin portability work retains SSH; parallel EventStream implementation retains old runtime |
| Negative evidence | an 11-commit proposed fix closed unmerged; ownership/closure weak | replacement PR explicitly not ready for cutover; several eval suites remain untested/incompatible |
| Closure evidence | roadmap later points toward v0.4, but causal chain to rewrite is weak | integration tests → evaluation migration → old runtime deletion/default switch is directly linked |
| Strongest VSM-relevant distinction | interaction disturbance vs generic routing/orchestrator terminology | environment/adaptation vs validation/support vs current-default decision |
| Proven VSM owner/autonomy | not established | not established |
| Quantified VSM advantage | not established | not established |

This difference is useful for the next empirical step: a cross-case schema should not assume every meaningful organizational transition is a coordination problem or every successful change has the same evidence shape.

## Comparison hooks

| Dimension | OpenHands runtime evidence |
| --- | --- |
| First external/runtime pressure | hosted deployment #1086 (2024-04-14) and arbitrary images #1387 (2024-04-26) |
| Partial repair before boundary change | PR #2101 merged 2024-06-20, still required SSH |
| Explicit replacement plan | #2404 opened 2024-06-12 |
| Parallel replacement without cutover | PR #2603 merged 2024-07-08 |
| Integration gate | PR #3184 merged 2024-08-01 |
| Evaluation gate | PR #3230 merged 2024-08-06; several limitations explicitly retained |
| Current-default closure | PR #3271 merged 2024-08-08; old runtime removed/new default selected |
| Issue closure | #2404 closed completed 2024-08-08 |
| Proven decisive adaptation/control owner | not established |
| Formal S3*/S4 autonomy | not established |
| Quantified development-cost saving | not established |

## References

Primary repository evidence reviewed:

- current canonical repository snapshot: `OpenHands/OpenHands@a07364828c8f202e7745c6bce3dcef3915ae7ac1`
- <https://github.com/OpenHands/OpenHands/issues/1086>
- <https://github.com/OpenHands/OpenHands/issues/1387>
- <https://github.com/OpenHands/OpenHands/issues/2404>
- <https://github.com/OpenHands/OpenHands/pull/2101>
- <https://github.com/OpenHands/OpenHands/pull/2603>
- <https://github.com/OpenHands/OpenHands/pull/3184>
- <https://github.com/OpenHands/OpenHands/pull/3230>
- <https://github.com/OpenHands/OpenHands/pull/3271>

## Bounded conclusion

OpenHands provides a stronger closure-oriented comparison than AutoGen. The public record shows environment/runtime pressure, an acknowledged partial repair, a replacement architecture introduced without immediate cutover, explicit integration and evaluation evidence, preserved validation gaps, and a final PR that deletes the old runtime and selects the replacement as default.

The case supports OpenSiro's insistence on separating **function, evidence, owner, support machinery, and closure**. It does not establish a formal S3/S3*/S4 state for OpenHands, and it does not show that VSM would have reduced the migration cost.

With AutoGen and OpenHands now providing two materially different evidence shapes, the empirical track can define a minimal cross-case comparison schema without treating one project's history as the universal template.
