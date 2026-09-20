# First bounded cross-case synthesis

Parent empirical track: [#30](https://github.com/opensiro/vsm-oss-organization/issues/30)  
Synthesis work item: [#100](https://github.com/opensiro/vsm-oss-organization/issues/100)

## Status and boundary

This is the first comparative synthesis across three completed external OSS case studies:

1. [`autogen.md`](autogen.md);
2. [`openhands-runtime.md`](openhands-runtime.md);
3. [`langgraph-interrupt-coordination.md`](langgraph-interrupt-coordination.md).

It uses [`COMPARISON_SCHEMA.md`](COMPARISON_SCHEMA.md) as the comparison contract.

This document is **supplementary empirical research**. It is not:

- a VSM Harness Index assessment;
- an autonomy classifier;
- a ranking or scorecard;
- a claim that any external project “implements VSM”;
- evidence that OpenSiro or VSM is faster, cheaper, or better;
- a substitute for the normative semantics in `opensiro/vsm-harness-profile`.

The purpose is narrower: identify which observations recur across independent histories, which remain case-specific, and which future article claims are already supportable or still require evidence.

## Three independent transition shapes

The three cases intentionally do not share one implementation topology.

```text
AutoGen
cross-work / interface interference
→ roadmap coordination surface
→ local repairs + abandoned repair
→ broader architecture later
→ weak direct causal closure to that architecture

OpenHands
external/runtime-boundary pressure
→ partial compatibility repair
→ explicit replacement path
→ integration + evaluation gates
→ old path removed / new default
→ stronger direct implementation closure

LangGraph
parallel feedback ambiguity
→ local shared-resume correction
→ explicit interrupt identity
→ interrupt-id → resume-value mapping
→ ambiguous scalar feedback rejected
→ later nested recursion counterexample
```

The common comparison therefore cannot be “did each project eventually introduce the same mechanism?” It must compare disturbance, response relation, ownership evidence, support/enforcement, closure, negative evidence, and system boundary separately.

## Compact comparison

| Dimension | AutoGen multimodal | OpenHands runtime | LangGraph interrupts |
| --- | --- | --- | --- |
| Historical disturbance | incompatibility among otherwise valid multimodal/text/message/workflow surfaces | runtime assumptions (`sshd`/SSH coupling) conflict with arbitrary images and hosted execution | concurrent pending human-input requests share an ambiguous feedback path |
| Initial/local response | quick multimodal capability/message fixes | image/plugin portability while retaining SSH | consume global resume so parallel subgraphs do not reuse one value |
| Broader response | roadmap/epic coordination; later v0.4 architecture | EventStream replacement path + staged migration | interrupt identity + ID-mapped resumes + later ambiguity rejection |
| Project-native reason | multimodal orchestration did not work seamlessly across workflow forms | current runtime coupling blocked arbitrary images/hosted deployment | unrelated interrupts must not consume the same/order-dependent resume value |
| Support / validation / enforcement | linked issues/PRs/design discussion; current triage/roadmap process | integration tests, evaluation migration, compatibility checks | interrupt IDs, resume-map plumbing, pending-interrupt checks, sync/async tests |
| Direct closure | partial fixes; roadmap later points to v0.4, but causal link is weak | old runtime removed and replacement selected as default | #4028 closed with multi-resume; #6108 enforces rule for covered topologies |
| Negative / incomplete evidence | #2118 closed unmerged; decisive owner and v0.4 causal chain unresolved | no-cutover stage; untested/incompatible eval suites; owner unresolved | #8579 shows nested-subgraph topology still bypasses intended invariant |
| Decisive organizational owner | `NOT_EVIDENCED` | `NOT_EVIDENCED` | `NOT_EVIDENCED` |
| Recursion-boundary evidence | `NOT_APPLICABLE` in the reconstructed transition; no recursion claim made | `NOT_APPLICABLE` in the reconstructed transition; no recursion claim made | explicit negative evidence: child variety can be collapsed by parent task aggregation |
| Quantified VSM cost/time advantage | `NOT_EVIDENCED` | `NOT_EVIDENCED` | `NOT_EVIDENCED` |

This table is descriptive. Differences in closure strength are not project-quality rankings.

## Recurring observations

### 1. A local or partial response precedes the broader response in all three cases

The strongest repeated pattern is not a particular VSM function. It is a development sequence:

```text
observable disturbance
        ↓
local / partial repair
        ↓
residual variety remains visible
        ↓
broader relation / boundary / mechanism
```

Evidence:

- **AutoGen:** local multimodal capability/message repairs coexist with the broader #1975 roadmap coordination surface; at least one proposed repair (#2118) closes unmerged before the later v0.4 direction.
- **OpenHands:** PR #2101 improves image/plugin portability while explicitly retaining SSH; #2404/#2603 then define and implement a replacement runtime without immediate cutover.
- **LangGraph:** PR #3889 fixes accidental global-resume reuse; users then expose the need for several distinct responses, leading to interrupt identity and ID-mapped resume semantics.

This supports an article-safe descriptive claim about these three cases:

> In each reviewed history, the broader mechanism was preceded by at least one narrower response that did not eliminate all of the observed variety.

It does **not** establish that local-first development is generally inefficient or that VSM would have skipped the local response.

### 2. Mechanism evidence is consistently stronger than ownership evidence

All three cases provide concrete evidence that something changed:

- roadmap/coordination machinery and technical repairs in AutoGen;
- runtime replacement, validation gates and cutover in OpenHands;
- addressable feedback plus ambiguity enforcement in LangGraph.

None of the three reconstructed histories independently establishes the decisive **organizational** owner needed for a formal OpenSiro autonomy classification.

This asymmetry is important:

```text
mechanism exists
        ≠
decisive organizational right established
        ≠
owner established
        ≠
autonomy established
```

The repeated absence of owner evidence is itself a calibration result. External public development history can be rich enough to reconstruct disturbances and closure while remaining too weak for autonomy claims.

### 3. Closure must be represented as a separate field

The cases demonstrate three different closure strengths/forms:

- **AutoGen:** local fixes are real, but the direct causal relation between the multimodal roadmap and the later v0.4 rewrite is weak.
- **OpenHands:** the replacement sequence has a much more direct cutover chain—implementation, integration testing, evaluation migration, old-path removal and new default.
- **LangGraph:** one issue closes with the new mapping mechanism and later enforcement exists, but a subsequent nested case proves the invariant was not universal.

Therefore “issue closed”, “PR merged”, or “new architecture exists” cannot serve as one generic closure flag.

A useful synthesis must ask what later operation changed and at which boundary that change remains evidenced.

### 4. Negative evidence materially changes the interpretation in all three cases

Each case would become misleading if only successful changes were retained:

- AutoGen loses the unmerged repair and weak causal bridge to v0.4;
- OpenHands loses explicit no-cutover stages and incomplete evaluation coverage;
- LangGraph loses the later nested recursion failure.

This supports a second article-safe methodological statement:

> For the reviewed cases, failed, deferred, untested, or later-regressed paths are necessary to delimit what the apparent successful mechanism actually proves.

This is an evidence-quality claim, not a claim of VSM superiority.

### 5. Function-first comparison survives different project vocabularies

The projects use very different words:

- `Roadmap`, `VisionCapability`, `GroupChatManager`;
- `SSHBox`, `EventStreamRuntime`, evaluation harness;
- `interrupt`, `Command.resume`, resume maps.

Vocabulary similarity would not produce a useful comparison. The common coordinate appears only after reconstructing the problem first:

```text
what variety became material?
→ what relation or boundary changed?
→ what decisive feedback/decision right is evidenced?
→ what support/enforcement carried it?
→ what later behavior demonstrates closure?
```

This is consistent with OpenSiro's function-first thesis. It shows that the same observation schema can be applied across unlike implementations without requiring the projects to use Beer/VSM terminology.

It still does not prove that this coordinate system improves development outcomes.

## A new dimension exposed by the third case: recursion-boundary evidence

AutoGen and OpenHands did not force the initial schema to distinguish whether a mechanism survives movement between explicit parent/child recursive boundaries.

LangGraph does.

At the child subgraph boundary, two interrupts remain distinct. At the parent task boundary, the grouped representation can collapse them so that the regulator incorrectly observes one pending interrupt. The intended “multiple pending interrupts require ID-mapped feedback” invariant then fails.

This creates a new evidence question:

> At which declared recursion boundary is the mechanism or invariant established, and what evidence shows that operationally relevant distinctions are preserved when crossing to a parent or child boundary?

The synthesis therefore justifies adding `recursion_boundary_evidence` to the comparison schema.

Important limitations:

- AutoGen and OpenHands are **not** retroactively given missing recursion narratives by analogy.
- For their currently reconstructed transitions the field is `NOT_APPLICABLE` unless future primary evidence makes recursion material.
- A mechanism working at one boundary is never assumed to work at another boundary merely because the implementation is nested.

## Case-specific observations that should not be generalized yet

### AutoGen-specific

The strongest distinctive evidence is a roadmap/epic acting as a visible coordination surface around a cross-cutting feature family. The later architectural rewrite has broader project-stated drivers, so the sampled multimodal incidents cannot be treated as the cause of v0.4.

### OpenHands-specific

The strongest distinctive evidence is staged replacement with explicit cutover restraint and unusually direct final closure through old-path deletion/default switch. This case is particularly useful for separating adaptation capability, validation evidence and current-default choice.

### LangGraph-specific

The strongest distinctive evidence is addressable feedback plus runtime rejection of under-specified feedback, followed by a recursion counterexample. This provides a concrete example of variety attenuation through refusal rather than guessed routing.

None of these three mechanisms should be promoted into a universal VSM recipe.

## Article-safe bounded claims now supported

The first three external cases support the following **bounded** statements when explicitly scoped to the reviewed evidence:

1. **Different implementation vocabularies can be normalized by function/problem before ownership.** The same evidence decomposition can describe cross-work interference, environment-boundary mismatch and feedback-routing ambiguity without inferring functions from component names.
2. **Local/partial responses preceded broader responses in all three reviewed histories.** This is reconstructable from primary issue/PR sequences.
3. **Support/enforcement and decisive ownership must be separated.** All three cases contain rich mechanism/support evidence while decisive organizational ownership remains unestablished.
4. **Closure is heterogeneous.** Direct cutover, bounded attenuation, later regression and weak causal closure are materially different evidence states.
5. **Negative evidence is necessary to delimit positive claims.** Abandoned work, deferred cutover, untested paths and later counterexamples change what can responsibly be inferred.
6. **Recursive boundary preservation is an independent evidence question.** LangGraph demonstrates that an invariant can hold at one tested topology and fail when lower-level variety is aggregated at a parent boundary.
7. **No quantitative VSM development-cost advantage has yet been established by these external cases.** This remains `NOT_EVIDENCED`.

These are candidate article statements only at the descriptive/methodological level. They do not yet establish the headline causal thesis that VSM/OSM materially improved OpenSiro development.

## Hypotheses that require comparison with OpenSiro's own evolution log

The external cases can now generate falsifiable hypotheses for the internal OpenSiro history.

### H1 — earlier functional distinction

If OpenSiro's construction method is genuinely anticipatory rather than retrospective, the evolution log should show relevant functional questions being made explicit **before** repeated incidents force the same distinction.

Examples to test later:

- interaction interference recognized before repeated cross-S1 rework;
- environment/adaptation distinction recognized before accumulating compatibility patches;
- feedback/authority ambiguity rejected before accidental return to the wrong operation;
- recursion boundary declared before evidence from one recursion is reused at another.

At present, M4/M5 have not supplied enough real S2/S4 operational history to claim this generally.

### H2 — lower rework from explicit authority boundaries

If function/owner/support separation reduces rework, the OpenSiro log should show fewer cases where support machinery is built and later discarded because it was mistaken for required organizational ownership.

Current internal evidence is mixed rather than purely positive: the dedicated executor-identity proof architecture was built and later deliberately retired. That reversal is valuable counter-evidence and must remain in the comparison.

### H3 — stronger closure discipline

If explicit completion/return contracts improve development, OpenSiro should be able to demonstrate fewer ambiguous “merged therefore done” claims and more cases where closure is tied to later operational effect.

The external cases show why this matters, but they do not establish that OpenSiro performs better.

### H4 — recursion checks expose hidden variety earlier

LangGraph suggests a concrete future test for OpenSiro: whenever a function/evidence claim is reused across recursion, verify that the parent representation preserves the distinctions required for that function's decision or feedback relation.

This is a testable design rule. Its development-cost benefit remains unknown.

## Claims that remain unsupported

The current corpus does **not** support:

- “VSM projects develop faster.”
- “OpenSiro avoided the problems seen in AutoGen/OpenHands/LangGraph.”
- “VSM reduces engineering cost by X%.”
- “AutoGen has S2/S4”, “OpenHands has S3/S4”, or “LangGraph has S2” under the formal OpenSiro autonomy semantics.
- “maintainers owned the relevant VSM functions” because they authored/reviewed/merged changes.
- “the broader response would have been selected earlier under VSM.”
- “all agent harnesses follow local repair → broader mechanism.”
- “a successful mechanism at one recursion transfers to another recursion.”
- any ranking among the three projects or their organizational quality.

These should remain explicitly excluded until stronger evidence exists.

## Implications for future case selection

A fourth case should add evidence that is currently weak rather than duplicating the same pattern.

High-value targets would include one of:

- a reconstructable **whole-system current-control** decision with explicit decision owner and return path;
- a materially **independent audit/complementary evidence** mechanism with identified judgment owner;
- an **identity/ultimate-policy** dispute with explicit legitimate authority and returned policy decision;
- a stronger external/future adaptation case where the option-generation and selection rights are directly evidenced;
- a case with unusually good quantitative timing/rework data.

Another architecture rewrite or generic multi-agent coordination case would add less comparative information unless it supplies one of those missing evidence dimensions.

## Implications for the OpenSiro empirical track

The first three cases are sufficient for a bounded synthesis, but not for the final article thesis.

The next internal priority is not to add VSM labels to the external projects. It is to improve the OpenSiro side of the comparison:

```text
external recurring observation
        ↕
OpenSiro evolution-log event with contemporaneous evidence
        ↓
compare timing / rework / closure / alternative explanation
```

This means preserving:

- reversals such as executor-proof retirement;
- natural rather than manufactured milestone witnesses;
- dates between disturbance, response and closure;
- abandoned work and superseded designs;
- cases where the VSM distinction did not change the implementation outcome.

Only after that internal evidence is mature should the track make a causal development-method claim.

## Bounded conclusion

Across the first three external histories, the strongest recurring result is methodological rather than causal:

> A function-first evidence decomposition can describe materially different OSS evolution paths while keeping mechanism, ownership, support, closure, negative evidence and system boundary separate.

The histories also show why this separation matters: all three have concrete response mechanisms, yet none supplies enough reviewed evidence for a formal autonomy claim; their closure evidence differs; and LangGraph demonstrates that a valid relation at one boundary can fail after recursive aggregation.

What remains unproven is the central downstream hypothesis: that using VSM/OSM during construction makes OpenSiro materially faster, cheaper, less error-prone, or more viable than comparable organic development. The empirical track should continue to treat that as a proposition to test, not a premise.
