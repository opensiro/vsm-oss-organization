# Second bounded cross-case synthesis

Parent empirical track: [#30](https://github.com/opensiro/vsm-oss-organization/issues/30)  
Synthesis work item: [#104](https://github.com/opensiro/vsm-oss-organization/issues/104)

## Status and provenance

This is the second bounded comparative synthesis across four completed external OSS case studies:

1. [`autogen.md`](autogen.md);
2. [`openhands-runtime.md`](openhands-runtime.md);
3. [`langgraph-interrupt-coordination.md`](langgraph-interrupt-coordination.md);
4. [`pydanticai-prioritization.md`](pydanticai-prioritization.md).

It uses [`COMPARISON_SCHEMA.md`](COMPARISON_SCHEMA.md) as the comparison contract.

The original [`CROSS_CASE_SYNTHESIS.md`](CROSS_CASE_SYNTHESIS.md) remains the historical three-case snapshot produced before PydanticAI was selected. This file does not rewrite that provenance. Its purpose is to test whether observations from the first synthesis survive a deliberately different evidence shape.

This document is supplementary empirical research. It is not:

- a VSM Harness Index assessment;
- an autonomy classifier;
- a ranking or scorecard;
- a claim that any external project “implements VSM”;
- evidence that OpenSiro or VSM is faster, cheaper, or better;
- a substitute for the normative semantics in `opensiro/vsm-harness-profile`.

## Why the fourth case matters

The first three cases shared one important evidentiary asymmetry:

```text
mechanism / response evidence    strong
support / enforcement evidence   strong
decisive owner evidence          weak / NOT_EVIDENCED
```

PydanticAI was selected specifically to challenge that pattern rather than add another architecture/runtime/coordination history.

Its public repository-development contract states that maintainers set present work priorities, agree non-trivial approaches, assign work, and supply the human review that counts. Current automation routes decisions requiring maintainer input back to a human maintainer endpoint while remaining advisory/supporting machinery.

This creates a useful stress test:

> Was weak owner evidence a recurring observation in the first sample, or a general property of public OSS evidence?

The four-case result is: **it was a recurring observation in the first three, not a general rule.**

## Compact four-case comparison

| Dimension | AutoGen multimodal | OpenHands runtime | LangGraph interrupts | PydanticAI prioritization |
| --- | --- | --- | --- | --- |
| Historical disturbance | incompatibility among otherwise valid multimodal/text/message/workflow surfaces | runtime assumptions (`sshd`/SSH coupling) conflict with arbitrary images and hosted execution | concurrent pending human-input requests share an ambiguous feedback path | issue/PR/AI-assisted contribution volume exceeds sustainable maintainer attention and crowds out higher-impact present work |
| Disturbance class | interaction / cross-work | external/runtime-boundary pressure | feedback/coordination ambiguity | current-control relevant present commitment/review-capacity pressure |
| Initial/local response | quick multimodal capability/message fixes | image/plugin portability while retaining SSH | consume global resume so parallel subgraphs do not reuse one value | `NOT_EVIDENCED` in the same local-repair sense; #4052 already frames the disturbance at the project work-priority level |
| Broader response | roadmap/epic coordination; later v0.4 architecture | EventStream replacement path + staged migration | interrupt identity + ID-mapped resumes + ambiguity rejection | explicit maintainer prioritization/admission contract + contributor pre-alignment + review/triage support automation |
| Decision / feedback right | `NOT_EVIDENCED` | `NOT_EVIDENCED` | feedback mapping mechanism is evidenced; decisive organizational owner is `NOT_EVIDENCED` | present-work priority, admission of non-trivial work, and human review judgment are explicitly reserved to maintainers |
| Owner evidence | `NOT_EVIDENCED` | `NOT_EVIDENCED` | `NOT_EVIDENCED` | explicit maintainer-team contract; current workflow routes maintainer-required questions to `@DouweM` where that endpoint is evidenced |
| Support / validation / enforcement | linked issues/PRs/design discussion; current triage/roadmap process | integration tests, evaluation migration, compatibility checks | interrupt IDs, resume-map plumbing, pending-interrupt checks, sync/async tests | contributor/champion context, `AGENTS.md`, labels, CI, review/triage bots; automated review remains advisory |
| Direct closure | partial fixes; roadmap later points to v0.4, but causal link is weak | old runtime removed and replacement selected as default | #4028 closed with multi-resume; #6108 enforces rule for covered topologies | contributor-facing policy merged and remains current; normal admission/review behavior is intentionally selective |
| Negative / incomplete evidence | #2118 closed unmerged; decisive owner and v0.4 causal chain unresolved | no-cutover stage; untested/incompatible eval suites; owner unresolved | #8579 shows nested-subgraph topology still bypasses intended invariant | #4052 remains open; not every priority choice is public; no quantified time saving; named endpoint does not prove sole ownership |
| Recursion-boundary evidence | `NOT_APPLICABLE` | `NOT_APPLICABLE` | explicit negative evidence: child variety can be collapsed by parent task aggregation | `NOT_APPLICABLE` to the primary reconstructed transition |
| Quantified VSM cost/time advantage | `NOT_EVIDENCED` | `NOT_EVIDENCED` | `NOT_EVIDENCED` | `NOT_EVIDENCED` |

This table is descriptive. It does not rank projects or imply that stronger owner evidence means higher organizational quality.

## Retest of the first synthesis

### Observation A — local/partial response precedes the broader response

**First-synthesis result:** true in all three reviewed histories.

**Four-case result:** **narrows rather than survives as a general cross-case statement.**

- AutoGen: yes — local multimodal fixes precede the broader roadmap/architecture response.
- OpenHands: yes — portability repairs retain SSH before the EventStream replacement/cutover sequence.
- LangGraph: yes — shared-resume correction precedes explicit interrupt identity/mapping and ambiguity rejection.
- PydanticAI: no equivalent local technical repair is established before the broader current-control response. #4052 itself identifies the problem at the level of project-wide review/prioritization and proposes selective prioritization. #4301/#5006 then supply support and operational return.

Therefore the article-safe statement becomes:

> In the first three technical-transition cases, the broader mechanism was preceded by a narrower response. The fourth governance/current-control case does not establish the same sequence, so local-repair-first is not supported as a general rule across the four-case corpus.

This is a useful falsification result. The comparison method must preserve `NOT_EVIDENCED` rather than force PydanticAI into the earlier pattern.

### Observation B — mechanism evidence is stronger than owner evidence

**First-synthesis result:** true in all three cases.

**Four-case result:** **falsified as a general rule.**

AutoGen, OpenHands and LangGraph still retain the asymmetry:

```text
mechanism established
owner not established
```

PydanticAI provides the counterexample needed to calibrate the schema:

```text
present-work control right explicitly defined
        ↓
maintainer role explicitly owns alignment / priority / human review
        ↓
automation remains advisory / supporting
        ↓
returned contributor behavior is observable
```

The correct reusable conclusion is therefore not “public OSS history rarely establishes owners.” It is narrower:

> Public OSS history may establish response mechanisms without establishing decisive owners, but explicit project governance/operating contracts can make the owner layer independently evidenced.

That supports keeping `owner_evidence` separate from mechanism evidence and proves that `NOT_EVIDENCED` is not a default value baked into the schema.

### Observation C — closure must remain a separate field

**First-synthesis result:** supported.

**Four-case result:** **survives unchanged and becomes stronger.**

The fourth case adds another closure form:

- AutoGen — partial fixes plus weak causal bridge to broader architecture;
- OpenHands — staged replacement and explicit default cutover;
- LangGraph — bounded enforcement later narrowed by recursive counterexample;
- PydanticAI — a current-control rule returned into the live contributor/admission/review process while the underlying inflow pressure remains ongoing.

PydanticAI shows why closure cannot mean “the disturbance disappeared.” Incoming issue/PR variety remains. Closure is the changed control relation by which that variety reaches scarce maintainer capacity.

### Observation D — negative evidence materially constrains interpretation

**First-synthesis result:** supported in all three.

**Four-case result:** **survives.**

PydanticAI contributes its own limiting evidence:

- the original meta prioritization issue remains open;
- not every priority decision is public;
- the named maintainer endpoint does not prove sole ownership of all relevant decisions;
- no controlled before/after time saving is available;
- ordinary OSS governance explains the response without invoking VSM.

The cross-case methodological statement remains:

> Failed, deferred, unresolved, later-regressed, or simply unobserved evidence is necessary to delimit what a positive mechanism/owner/closure claim actually proves.

### Observation E — function-first comparison survives unlike vocabulary

**Four-case result:** **survives and gains a stronger owner test.**

The fourth case uses governance/process vocabulary rather than runtime vocabulary:

- `priority`;
- `champion`;
- `assignment`;
- `human review`;
- `AGENTS.md`;
- review/triage bots.

A name-based approach could easily equate maintainers with S3 or bots with regulation. The useful comparison appears only after reconstructing:

```text
what present variety is material?
→ what decision right regulates it?
→ who is explicitly authorized to exercise that right?
→ what support routes or checks the decision?
→ what later operational behavior changes?
```

That is consistent with the function-first thesis while remaining non-causal about development advantage.

### Observation F — recursion-boundary preservation is independent

**Four-case result:** **survives unchanged.**

Only LangGraph currently makes recursion operationally material to the reconstructed transition. The other three remain `NOT_APPLICABLE` for this field.

This strengthens the reason to keep recursion as an independent optional evidence dimension rather than forcing every case into recursive language.

## Schema stress-test result

**No comparison-schema revision is required.**

PydanticAI fills existing fields differently rather than exposing a missing field:

```text
decision_or_feedback_right        positive
owner_evidence                    positive
support_validation_enforcement    positive but non-owning
closure_evidence                  positive
recursion_boundary_evidence       NOT_APPLICABLE
```

This is a meaningful validation of the schema design. A field should not be added merely because a later case contains stronger evidence.

The schema now supports at least these contrasting evidence shapes:

1. strong mechanism + weak owner;
2. strong mechanism + strong direct cutover closure;
3. bounded enforcement + recursive counterexample;
4. explicit current-control right + positive owner evidence + advisory support machinery.

## Four-case article-safe claims

The following statements are supported when explicitly scoped to the reviewed corpus:

1. **Function/problem can be normalized before project vocabulary.** The same evidence decomposition works across interface interference, runtime replacement, feedback ambiguity and maintainer work-priority control.
2. **Owner evidence is independent from mechanism evidence.** The first three cases leave owners unestablished; PydanticAI supplies a positive owner case because its operating contract explicitly reserves the relevant judgment to maintainers.
3. **A positive owner claim requires more than authorship, merge rights, role names or automation.** The strongest PydanticAI evidence is the public decision contract, not self-merge or assignment metadata.
4. **Closure remains heterogeneous.** Repair, cutover, bounded enforcement, recursive failure and returned operating policy are materially different closure forms.
5. **Negative evidence remains necessary to bound every positive interpretation.** The fourth case does not remove this requirement.
6. **Recursion-boundary preservation remains an independent optional question.** LangGraph demonstrates why; the other cases need not be given artificial recursion narratives.
7. **The local-repair-before-broader-response pattern is not established across all four cases.** It remains a fact about the first three reviewed technical-transition histories, not a general OSS-development rule.
8. **No quantitative VSM development-cost advantage is established.** This remains `NOT_EVIDENCED` across all four cases.

These are descriptive/methodological statements only. They do not establish the headline causal thesis that VSM/OSM materially improved OpenSiro development.

## Implications for the OpenSiro comparison

PydanticAI changes what the external corpus can test against OpenSiro.

The first three cases mainly tested whether OpenSiro's method helps distinguish mechanism, support, closure and recursion without inventing ownership.

The fourth case adds a sharper comparator for **present current-control ownership**:

```text
present work / commitment pressure
        ↓
explicit decisive right
        ↓
legitimate owner evidence
        ↓
support / routing / validation kept separate
        ↓
return into affected operation
```

This topology resembles the evidence decomposition OpenSiro is trying to require for its own S3 work, but that similarity is analytical only. PydanticAI is not assigned an S3 autonomy state, and its repository-development boundary is not assumed equivalent to OpenSiro's declared organization boundary.

### Testable internal question

For OpenSiro's eventual real S3 witness, ask:

> Is the decisive present-control right and its owner evidenced as clearly as the support/transport machinery, and does the returned decision visibly alter the affected S1 operation?

This does not relax #39. A natural whole-system current-control event is still required; external analogy cannot substitute for an internal witness.

## Updated hypotheses for the future article

### H1 — function-first normalization

**Current status:** descriptive support increased.

Four unlike histories can be compared using the same decomposition without forcing common vocabulary or mechanisms.

What remains unproven is whether doing this during construction improves outcomes.

### H2 — explicit owner/support separation reduces mistaken architecture

**Current status:** plausible, not causal.

PydanticAI demonstrates a project-native arrangement where support automation is explicitly advisory while human maintainers retain the decisive review/admission right.

OpenSiro's own executor-proof reversal remains essential counter-evidence: it shows that even an explicit VSM-oriented construction process can initially overbuild proof machinery and later remove it.

The article must compare these histories rather than claim owner/support separation automatically prevents rework.

### H3 — stronger closure discipline

**Current status:** descriptive comparison possible; benefit unproven.

The corpus now includes four closure forms. OpenSiro should be compared on whether its completion claims consistently require returned operational effect rather than merge/status alone.

### H4 — recursion checks expose hidden variety earlier

**Current status:** still primarily motivated by LangGraph.

No new evidence from PydanticAI changes this hypothesis.

### H5 — current-control capacity becomes explicit when work-arrival variety exceeds review/regulation capacity

**Current status:** directly evidenced in PydanticAI, not yet a general law.

A future case or OpenSiro event could test whether explicit admission/priority rights emerge before or after repeated overload and whether earlier declaration measurably reduces blocked or wasted work.

## Claims that remain unsupported

The four-case corpus still does **not** support:

- “VSM projects develop faster.”
- “OpenSiro avoided the problems seen in AutoGen/OpenHands/LangGraph/PydanticAI.”
- “VSM reduces engineering cost by X%.”
- formal autonomy vectors for any of the four projects from these supplementary histories;
- “PydanticAI has S3=A/C” because maintainers own review/prioritization decisions;
- “maintainers are S3” as a label-based shortcut;
- “bots are S3/S3*” because they triage, review or enforce checks;
- “the broader response would have been selected earlier under VSM.”
- “all agent harnesses follow local repair → broader mechanism.”
- “public OSS evidence always lacks owner provenance.”
- any ranking among the four projects or their organizational quality.

## What the fourth case falsified or narrowed

Two useful corrections now belong in the research record:

```text
Earlier observation:
all reviewed cases show local/partial repair before broader mechanism

Four-case calibration:
true for the first three; NOT_EVIDENCED in the same form for PydanticAI
→ narrow the claim
```

```text
Earlier observation:
mechanism evidence is consistently stronger than owner evidence

Four-case calibration:
true for the first three; contradicted by explicit PydanticAI owner evidence
→ do not generalize
```

This is evidence that the empirical track can falsify its own provisional patterns instead of only accumulating confirming examples.

## Next evidence gap

After four deliberately different cases, adding another case is useful only if it supplies materially new evidence. High-value gaps now include:

- independent/complementary audit with an identified judgment owner;
- legitimate identity/ultimate-policy authority with a returned policy decision;
- external/future adaptation where option generation, option selection and owner evidence are all public;
- unusually strong quantitative timing/rework data suitable for a bounded cost comparison.

A fifth generic runtime rewrite, coordination mechanism or maintainer-governance example would add less value unless it closes one of these gaps.

## Bounded conclusion

The second synthesis strengthens the methodological result while narrowing two earlier recurring observations.

Across four unlike OSS histories, the comparison schema continues to separate:

```text
disturbance / function
        ↓
decisive decision or feedback right
        ↓
owner evidence
        ↓
support / validation / enforcement
        ↓
closure
        ↓
negative evidence and recursion boundary
```

PydanticAI demonstrates that positive owner evidence can be established when the project explicitly defines the relevant decision right. It also shows that the local-repair-before-broader-response sequence from the first three cases should not be promoted into a general rule.

What remains unproven is unchanged and central: whether using VSM/OSM during OpenSiro construction produces a measurable advantage in development time, rework, coordination cost, or organizational viability. The four-case corpus improves the comparison instrument; it does not by itself establish that causal thesis.
