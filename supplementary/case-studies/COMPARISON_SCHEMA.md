# Minimal cross-case comparison schema

Parent empirical track: [#30](https://github.com/opensiro/vsm-oss-organization/issues/30)  
Initial schema work item: [#90](https://github.com/opensiro/vsm-oss-organization/issues/90)  
First explicit schema revision: [#100](https://github.com/opensiro/vsm-oss-organization/issues/100)

This schema defines the smallest shared evidence shape currently justified by three independent case studies:

- [`autogen.md`](autogen.md);
- [`openhands-runtime.md`](openhands-runtime.md);
- [`langgraph-interrupt-coordination.md`](langgraph-interrupt-coordination.md).

It is **supplementary research infrastructure**. It is not a VSM Harness Profile, assessment procedure, autonomy classifier, ranking system, or second Index database.

## Purpose

Use one common structure to ask whether VSM/OSM distinctions explain or anticipate independently observed OSS development problems without forcing unlike histories into the same narrative.

The schema must preserve this separation:

```text
primary project fact
        ↓
organizational reconstruction
        ↓
VSM interpretation
        ↓
comparison / bounded hypothesis
```

A missing field remains missing. Do not fill evidence gaps by inference from names, popularity, maintainer status, successful delivery, or the presence of automation.

## Why two cases were required first

The initial cases exposed different transition shapes.

```text
AutoGen
cross-work interference
→ roadmap coordination surface
→ partial repairs
→ broader architecture later
→ weak direct closure / ownership evidence

OpenHands
external/runtime pressure
→ partial compatibility repair
→ parallel replacement
→ integration/evaluation gates
→ old path removed / new default
→ stronger direct implementation closure
```

A schema derived from only AutoGen would overemphasize coordination. A schema derived from only OpenHands would overemphasize staged replacement and cutover. The shared contract therefore records **what kind of evidence exists** without requiring one canonical transition topology.

## Revision after the third case

The LangGraph case adds another materially different transition shape:

```text
parallel feedback ambiguity
→ local shared-resume correction
→ explicit request identity
→ request-id → feedback mapping
→ ambiguous feedback rejected
→ nested recursive boundary later exposes incomplete coverage
```

The first two cases did not require a dedicated field for whether a mechanism/invariant remains established when crossing an explicit parent/child recursion boundary. LangGraph does: distinct child interrupts can be aggregated into one parent task representation, hiding variety needed for the parent-level feedback decision.

Therefore #100 adds one field, `recursion_boundary_evidence`, rather than silently forcing the observation into generic closure/negative-evidence prose.

This revision does **not** retroactively invent recursion narratives for AutoGen or OpenHands. Their currently reconstructed transitions may use `NOT_APPLICABLE` unless future primary evidence makes recursion material.

## Case header

Every case MUST identify:

| Field | Meaning |
| --- | --- |
| `project` | Project/repository name used for the case. |
| `current_canonical_source` | Current canonical public repository when resolvable. |
| `historical_identity` | Historical repository/project name when materially different. |
| `historical_interval` | Bounded period actually reconstructed. |
| `system_boundary` | What development/organizational system is in focus and what adjacent systems are excluded. |
| `source_snapshot` | Current or historical revision(s) used where practical. |
| `primary_refs` | Issues, PRs, commits, design docs, releases, or other primary project evidence. |
| `selection_reason` | Why this case supplies an independent comparison surface. |

The current repository snapshot is provenance, not permission to project today's architecture backward into the historical interval.

## Transition record

A case MAY contain one or more transition records. Each transition should use the following fields when evidence exists.

| Field | Required treatment |
| --- | --- |
| `transition_id` | Stable case-local label or heading. |
| `first_observed` | Earliest primary evidence in the reviewed record; use `UNKNOWN` if not reconstructable. |
| `observed_disturbance` | Project fact describing the failure, interference, constraint, exception, external change, or policy problem before VSM interpretation. |
| `project_native_explanation` | Contemporaneous explanation in the project's own concepts. |
| `initial_response` | Local/ad-hoc/partial response, including failed or abandoned responses when relevant. |
| `broader_response` | Later mechanism/process/role/architecture introduced to regulate the problem, if any. |
| `decision_or_feedback_right` | The decisive right/feedback relation actually evidenced. Use `NOT_EVIDENCED` rather than inferring it from maintainer/reviewer/tool existence. |
| `owner_evidence` | Evidence identifying who/what owned the decisive right. Keep separate from GitHub identity, transport, automation, CI, tests, queues, or implementation authorship. |
| `support_validation_enforcement` | Machinery that transported, checked, validated, scheduled, or enforced the response without automatically owning the organizational decision. |
| `closure_evidence` | Observable later state showing change, attenuation, replacement, preservation, abandonment, or unresolved status. |
| `recursion_boundary_evidence` | When recursion is material, evidence showing the boundary at which the relation/invariant is established and whether relevant distinctions survive movement to a parent/child boundary. Use `NOT_APPLICABLE` when the reconstructed transition does not materially depend on recursion; do not infer transfer across boundaries. |
| `negative_or_incomplete_evidence` | Failed PRs, untested paths, reversals, unresolved ownership, contradictory facts, later regressions, or explicit limitations. |
| `timing_rework_effort` | Only reconstructable dates/counts/repeated incidents/rework/changed artifacts. No synthetic cost estimate. |
| `alternative_explanations` | Plausible non-VSM explanations that fit the same facts. |
| `vsm_interpretation` | Function-level interpretation after the facts are established; ownership/autonomy stays separate. |
| `anticipatory_prediction` | A falsifiable question or prediction the OpenSiro construction method could have made earlier. |
| `causal_status` | What the evidence supports about effect/causality; default to uncertainty rather than a success claim. |

## Missing-value vocabulary

Use explicit prose where possible. When a compact marker is useful, only these neutral markers are defined:

- `UNKNOWN` — the reviewed evidence does not establish the value;
- `NOT_EVIDENCED` — the positive claim would require evidence not present in the reviewed record;
- `NOT_APPLICABLE` — the field does not meaningfully apply to this bounded transition.

These are not scores and do not form an ordering.

For `recursion_boundary_evidence`, `NOT_APPLICABLE` is preferable to inventing a recursive interpretation merely because the implementation contains nesting or layered components.

## Disturbance classification

Only after `observed_disturbance` is established, a case may describe the organizational variety using one or more of these analytical distinctions:

- **local operational** — ordinary variety attributable to one bounded operating surface;
- **interaction / cross-work** — interference, conflict, incompatibility, contention, or oscillation among otherwise valid work/operation surfaces;
- **current-control relevant** — a present whole-system constraint/priority/resource/commitment/intervention question;
- **complementary-audit relevant** — ordinary reporting is insufficient and materially complementary access/judgment is needed;
- **external / future relevant** — environmental or prospective change requires adaptation beyond present internal execution;
- **identity / ultimate-policy relevant** — mission, system boundary, ultimate authority, or delegated policy envelope is at issue;
- **unclear** — available evidence does not support a narrower classification.

This vocabulary is analytical only. It does not award S2/S3/S3*/S4/S5 or autonomy states.

## Owner / support / closure separation

Every positive organizational interpretation should make this decomposition reviewable:

```text
function / variety
        ↓
decisive decision or feedback right
        ↓
owner evidence
        ↓
support / validation / transport / enforcement
        ↓
closure back into later operation
```

If the record establishes the mechanism and closure but not the owner, preserve that asymmetry. Do not promote the mechanism into an autonomous VSM owner.

Examples from the existing cases:

- AutoGen's roadmap issue provides evidence of a coordination relation but does not independently establish the decisive coordination owner.
- OpenHands integration tests and evaluation suites provide evidence supporting a runtime replacement but do not become S3* owners merely because they validate the replacement.
- LangGraph interrupt IDs, resume maps and runtime validation provide a feedback-disambiguation mechanism and enforcement, but do not establish the organizational owner of an S2 function.

## Recursion / system-boundary rule

Evidence at one declared boundary does not automatically transfer to another recursion.

When recursion is material, record:

```text
boundary where disturbance is observed
        ↓
representation exposed to parent/child
        ↓
which distinctions are preserved or aggregated
        ↓
which decision / feedback relation depends on those distinctions
        ↓
evidence that the invariant still holds — or fails — across the boundary
```

A valid result may be:

> The mechanism is established for the reviewed top-level task topology, but transfer to nested child interrupts is disproven by later primary evidence.

Do not require every case to have recursive evidence. Recursion is a comparison dimension only when it is operationally material to the reconstructed transition.

## Closure forms

Cases do not need the same closure form. Record the strongest closure actually evidenced, for example:

- local defect repaired;
- interaction attenuated or serialized;
- repeated conflict stops/reduces;
- constraint/intervention returned into current work;
- old mechanism removed/replaced;
- new default or process adopted;
- policy/identity decision returned and governed later work;
- proposal abandoned;
- issue closed without evidence that the underlying disturbance was resolved;
- bounded closure later narrowed by a regression/counterexample;
- unresolved / insufficient evidence.

Issue closure, PR merge, test success, release, or adoption alone is not automatically organizational closure. State what later behavior changed and, when material, at which boundary it changed.

## Timing, effort, and cost

Prefer reconstructable signals:

- first-observed date;
- mechanism-introduced date;
- closure date;
- repeated incidents or duplicate fixes;
- failed/abandoned PRs;
- commit or changed-file counts when they merely document work volume;
- blocked iterations;
- explicit maintainer statements about complexity, flakiness, bottlenecks, or rework.

Do not convert these into money/time saved without a defensible counterfactual.

A valid result is:

> Observable migration effort is substantial, but comparative cost reduction is `NOT_EVIDENCED`.

## Causal-status rule

The schema intentionally avoids a numeric evidence-strength scale. Describe causal support in prose.

At minimum distinguish:

1. **observed sequence** — event A preceded response B and both are evidenced;
2. **project-attributed mechanism** — primary project evidence explicitly links the problem and response;
3. **plausible analytical mechanism** — our interpretation explains the sequence but the project does not explicitly make the claim;
4. **counterfactual unsupported** — the evidence cannot establish what would have happened under VSM/OSM or another development method.

Do not turn temporal order into causality.

## Anticipatory-prediction rule

The comparison becomes useful only when the OpenSiro construction method can state a falsifiable earlier question, not merely relabel history afterward.

Good form:

> If repeated incompatibilities now arise from interaction among separately valid work surfaces, expect a need for an explicit coordination relation rather than continuing independent local fixes.

Another good form:

> If environment variety repeatedly forces compatibility patches around one architectural assumption, test whether the system boundary itself requires adaptation before adding another local patch.

A recursion-oriented good form, justified by the LangGraph case:

> If a parent-level decision depends on distinguishing several child-level requests, test whether the parent representation preserves those distinctions before reusing the lower-level invariant at the parent recursion.

Bad form:

> The project eventually added X, therefore VSM predicted X.

For each case, record whether the prediction could have been stated **before** the later mechanism appeared and what evidence would falsify it.

## Cross-case comparison row

For lightweight synthesis, each transition can be represented with this compact row shape:

| Case / transition | Disturbance | Initial response | Broader response | Right / owner evidence | Support evidence | Closure | Recursion boundary | Negative evidence | Timing / effort | VSM distinction | Alternative explanation | Causal status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Cells should summarize and link back to the full case. This table is not a scorecard.

## Calibration from the first three cases

The schema preserves materially different evidence shapes without ranking them:

| Field | AutoGen multimodal | OpenHands runtime | LangGraph interrupts |
| --- | --- | --- | --- |
| Disturbance shape | cross-work/interface interference | environment/runtime-boundary mismatch | ambiguous feedback among concurrent pending requests |
| Initial response | quick/local multimodal fixes | image/plugin portability while retaining SSH | consume shared/global resume at subgraph boundary |
| Broader response | roadmap coordination + later architecture | explicit replacement runtime path | explicit interrupt identity + ID-mapped resume + ambiguity rejection |
| Support/validation | linked issues/PRs/design discussion | integration tests + evaluation migration | interrupt IDs, resume-map plumbing, pending-interrupt validation/tests |
| Closure evidence | weaker direct causal closure to v0.4 | direct removal/default-switch closure | #4028 bounded closure + #6108 enforcement for covered topology |
| Recursion boundary | `NOT_APPLICABLE` in reconstructed transition | `NOT_APPLICABLE` in reconstructed transition | later nested-subgraph counterexample disproves universal transfer |
| Owner evidence | not established | not established | not established |
| Negative evidence | unmerged repair; causal link weak | deliberate no-cutover stage; untested eval cases | #8579 shows incomplete nested coverage |
| Quantified VSM advantage | not established | not established | not established |

The differences in closure, recursion evidence, and implementation effort are descriptive, not project-quality rankings.

## Future-case update rule

Adding a new case must not silently rewrite prior case observations to make a cross-case thesis cleaner.

For each new case:

1. reconstruct the case independently from primary evidence;
2. fill only fields the evidence supports;
3. preserve `UNKNOWN` / `NOT_EVIDENCED` / `NOT_APPLICABLE` values;
4. compare after the standalone case is complete;
5. if the new case exposes a genuinely missing comparison field, revise this schema explicitly and explain why the earlier cases did not reveal it;
6. do not retroactively fill older cases from analogy;
7. when stronger primary evidence changes an older case, update that case with an explicit dated/revision note rather than silently changing the historical interpretation.

The schema should evolve by observed comparative need, following the same elimination principle as the wider Organization design.

## Relationship to VSM semantics

Normative VSM semantics remain in `opensiro/vsm-harness-profile`.

This schema does not redefine:

- S1–S5;
- recursion semantics;
- autonomy states;
- Constructor thresholds;
- evidence-boundary rules;
- assessment procedure.

A case-study phrase such as “S2-like coordination pressure” or “S4-relevant external variety” is an analytical interpretation unless the full governing Profile/Methodology evidence requirements are independently satisfied. External case studies in this track are not canonical Index assessments.

## What this schema can and cannot support

After multiple cases, the schema may support bounded empirical statements such as:

- a particular functional distinction recurs before a later mechanism appears;
- one class of disturbance repeatedly produces local rework before a broader relation is introduced;
- the OpenSiro construction process formulated an equivalent distinction earlier in its own history;
- a mechanism closes one boundary but remains unproven or fails at another recursion;
- no measurable advantage is visible despite conceptual similarity.

It cannot, by itself, establish:

- that VSM caused a project to improve;
- that OpenSiro is faster/better;
- that an external project has a particular autonomy vector;
- that one organizational form is universally superior;
- that evidence from one recursion transfers to another without boundary-specific proof.

Those remain empirical questions for later synthesis.
