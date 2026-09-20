# Article claim audit

Parent empirical track: [#30](https://github.com/opensiro/vsm-oss-organization/issues/30)  
Audit work item: [#106](https://github.com/opensiro/vsm-oss-organization/issues/106)

## Purpose

This document is an evidence gate for future article/paper writing. It does **not** draft the article and does not convert the current empirical corpus into a success narrative.

Each candidate claim is classified as one of:

- `SUPPORTED` — directly defensible from the reviewed evidence at the stated scope;
- `PLAUSIBLE` — a useful hypothesis with partial support but material alternative explanations or missing comparative closure;
- `NOT_EVIDENCED` — should not be stated as a finding yet.

These are epistemic categories, not scores, ranks, or maturity levels.

## Evidence inputs

Primary internal evidence:

- [`evolution-log.md`](evolution-log.md)
- linked issues/PRs/trials referenced by that log

External comparative evidence:

- [`case-studies/CROSS_CASE_SYNTHESIS.md`](case-studies/CROSS_CASE_SYNTHESIS.md)
- [`case-studies/CROSS_CASE_SYNTHESIS_V2.md`](case-studies/CROSS_CASE_SYNTHESIS_V2.md)
- [`case-studies/COMPARISON_SCHEMA.md`](case-studies/COMPARISON_SCHEMA.md)

The external corpus currently contains four bounded histories: AutoGen, OpenHands runtime, LangGraph interrupt coordination, and PydanticAI maintainer prioritization.

## Claim-audit rule

A claim must keep these layers separate:

```text
observed project fact
        ↓
organizational reconstruction
        ↓
methodological interpretation
        ↓
performance / causal claim, if any
```

Evidence that a method changed **what the project did** is not automatically evidence that the method made the project **faster, cheaper, or better**.

---

## C1 — Function-first decomposition works as a comparison coordinate across unlike implementations

**Status:** `SUPPORTED`

### Scope

The reviewed OpenSiro and four external case-study artifacts.

### Evidence

The external corpus contains materially different implementation vocabularies and transition shapes:

- AutoGen: multimodal orchestration / roadmap coordination;
- OpenHands: SSH/runtime replacement and evaluation migration;
- LangGraph: interrupt identity / mapped feedback / recursive counterexample;
- PydanticAI: issue/PR prioritization, maintainer admission/review rights, and advisory automation.

Despite those differences, the same evidence decomposition remained usable:

```text
disturbance / function
→ decision or feedback right
→ owner evidence
→ support / validation / enforcement
→ closure
→ negative evidence / recursion boundary
```

The PydanticAI case also stress-tested the schema by supplying positive owner evidence where the first three did not, without requiring a new owner field.

### Alternative explanation

This may simply show that the schema is broad and disciplined enough to organize heterogeneous software-project histories. It does not establish that VSM is uniquely capable of doing so.

### Allowed wording

> Across the four reviewed external histories, a function-first decomposition provided a stable comparison coordinate despite materially different project vocabularies and implementation mechanisms.

### Do not write

> VSM is the only framework capable of comparing heterogeneous agent organizations.

---

## C2 — Explicit system-boundary discipline exposed a green validator that was checking the wrong organization

**Status:** `SUPPORTED`

### Scope

The OpenSiro contributor-routing incident recorded on 2026-09-18.

### Evidence

The initial routing/oracle implementation generalized the organization from the declared five repositories to all public `opensiro/*` repositories. The resulting oracle reported `8/8` conformance while including ARCTIC, `terminal-bench-vsm`, and `opensiro.com`, which were outside the declared Organization boundary.

The correction:

- rebound the routing population to the canonical five-repository scope;
- changed the oracle to consume that declared scope rather than maintain a second population rule;
- reverted routing blocks in three out-of-scope repositories;
- replaced the `8/8` result with the bounded `5/5` result;
- separated mechanical routing presence from later blind behavioral interpretation.

### Alternative explanation

This can be described as ordinary requirements/scope correction: the validator's input population was wrong and the implementation was fixed.

### Allowed wording

> In the routing workstream, an explicit system-boundary contract exposed that a fully green oracle was validating the wrong population, forcing a multi-repository rollback from an all-public `8/8` scope to the declared five-repository `5/5` system.

### Do not write

> VSM prevented scope errors.

The incident itself is evidence that a scope error occurred.

---

## C3 — Separating organizational ownership from technical actor attribution changed OpenSiro architecture

**Status:** `SUPPORTED`

### Scope

The executor-provenance / GitHub App sequence ending in PRs #75 and #76.

### Evidence

OpenSiro first treated distinct executor attribution as an important proof gap and built a substantial technical-identity path:

- PR #68 — GitHub App executor profile, witness schema, publisher, validator, tests;
- PR #69 — provisioning/bootstrap machinery;
- PR #71 — setup guide;
- PR #72 — setup shortcuts;
- PR #73 — shortcut consolidation.

The project then reconsidered whether that machinery was required by the actual organizational function/ownership claim.

PR #75 removed the dedicated GitHub App/executor-provenance machinery and milestone dependencies. PR #76 removed the residual proof-debt language from active contracts.

The evolution log explicitly preserves the earlier negative provenance finding while changing the later conclusion about what technical mechanism must remain architectural.

### Alternative explanation

Ordinary engineering over-specification followed by simplification explains the sequence without requiring a VSM-specific benefit claim.

### Allowed wording

> OpenSiro's function/ownership distinction materially changed the architecture: a dedicated executor-identity proof layer was built across at least five merged PRs and later removed when technical actor attribution was judged unnecessary for the selected functional ownership criteria.

### Do not write

> VSM prevented overengineering.

The record instead contains substantial overengineering/rework before the removal.

---

## C4 — The construction process permits a negative “not yet evidenced” milestone result

**Status:** `SUPPORTED`

### Scope

M1 / S3 current-control evidence as of 2026-09-20.

### Evidence

The first-party S3 constructor machinery exists, but #39 still requires a real whole-system current exception that exceeds ordinary local S1 authority and returns a bounded decision into the affected S1 operation.

Several candidate events were screened and rejected:

- no actual upstream contract drift;
- stale tracker/vector consistency repair remained local maintenance;
- Index discovery/candidate concurrency remained local Index S1 variety;
- later screened Index assessment/CI work also remained local S1 variety.

The organization kept M1 open instead of manufacturing a conflict or reclassifying ordinary local recovery as S3.

### Alternative explanation

This is also ordinary rigorous experimental hygiene: do not declare a capability demonstrated when the qualifying event has not occurred.

### Allowed wording

> The current construction process is falsifiable enough to preserve a negative state: M1 remains open even though the S3 transport/control surface is implemented, because no natural qualifying whole-system current-control event has yet been observed.

### Do not write

> OpenSiro has proven autonomous/current S3 control.

The missing real transaction is the point of #39.

---

## C5 — Real audit use narrowed the planned S3* ownership target instead of escalating it

**Status:** `SUPPORTED`

### Scope

The transition recorded on 2026-09-20 around #44 / PR #45 and PR #77.

### Evidence

A real complementary-audit path was exercised successfully. The resulting evidence established the S3* function and first-party constructor path, but did not establish a present need for permanent autonomous S3* ownership.

PR #77 changed the roadmap target from autonomous S3* toward `S3*=C`, keeping the audit function while removing the assumption that a permanent verifier/agent/bot was required.

### Alternative explanation

This may be ordinary scope reduction after implementation experience: the team learned it did not need the stronger architecture yet.

### Allowed wording

> After real complementary-audit use, OpenSiro narrowed the S3* ownership target from autonomous ownership to a constructor state rather than treating `A` as a maturity upgrade that had to be reached.

### Do not write

> VSM proved that autonomous audit is unnecessary in agent organizations.

The claim is bounded to the current OpenSiro variety and evidence.

---

## C6 — OpenSiro can classify an earlier real policy event retrospectively without rewriting chronology

**Status:** `SUPPORTED`

### Scope

The routing-scope decision of 2026-09-18 and its later S5-P reconstruction on 2026-09-20.

### Evidence

The five-repository scope correction occurred before the explicit S5 parent-authority contract existed.

Later work:

- added the parent-boundary contract;
- made the legitimate parent role explicit;
- reconstructed the earlier scope decision as `S5-P-001` only after the missing ownership relation became reviewable;
- preserved the actual dates rather than pretending the later contract existed when the original decision was made.

### Alternative explanation

This is ordinary governance formalization after the fact.

### Allowed wording

> The project demonstrates a chronology-preserving retrospective classification: a real earlier system-scope decision was reused as an S5-P witness only after legitimate parent ownership was independently made explicit, without backdating the later governance contract.

### Do not write

> OpenSiro predicted or autonomously executed S5 before the governance model existed.

---

## C7 — Explicit boundary/function/owner separation reduces future rework

**Status:** `PLAUSIBLE`

### Supporting evidence

- the routing correction now derives its population from one authoritative boundary instead of a duplicate allowlist;
- executor-identity machinery was removed after the project separated technical attribution from organizational ownership;
- S3* was narrowed rather than expanded into a permanent autonomous verifier;
- M1 candidate screening prevents ordinary local work from being centralized merely to instantiate S3.

### Counter-evidence / uncertainty

- the routing incident already caused multi-repository rework;
- the executor-proof path consumed at least five merged implementation/refinement PRs before removal;
- there is no controlled comparison against an equivalent OpenSiro development process without these distinctions;
- ordinary architecture review/scope discipline could produce the same simplifications.

### Allowed wording

> The current evidence suggests that explicit boundary and owner/support distinctions may prevent some future duplication or overbuilding, but the project also contains substantial rework before those distinctions were applied correctly.

### Do not write

> VSM reduced OpenSiro rework.

That net effect is not established.

---

## C8 — Explicit system-boundary contracts may improve validator reliability

**Status:** `PLAUSIBLE`

### Supporting evidence

The routing oracle became correct only after its checked population was bound to the canonical declared system boundary.

### Missing evidence

One incident does not establish a general reliability improvement. There is no measured pre/post defect rate for boundary-related validators.

### Allowed wording

> The routing incident motivates a testable design hypothesis: conformance tools that derive their population from the authoritative system boundary may be less prone to silently validating the wrong organization.

### Do not write

> Boundary contracts make validators reliable.

---

## C9 — Refusing synthetic milestone witnesses improves evidentiary quality

**Status:** `PLAUSIBLE`

### Supporting evidence

OpenSiro explicitly refused to manufacture an S3 disturbance, and reused a real earlier S5 event instead of creating a fresh policy controversy solely to exercise the path.

This keeps the empirical record from containing a positive witness whose disturbance was introduced by the same project for the purpose of proving the milestone.

### Missing evidence

There is no external controlled study showing that this policy improves downstream scientific validity or development performance.

### Allowed wording

> OpenSiro's current evidence policy reduces one obvious source of self-generated milestone contamination by preferring natural events and chronology-preserving reconstruction over synthetic positive witnesses.

### Do not write

> The methodology guarantees unbiased evidence.

---

## C10 — VSM/OSM made OpenSiro faster or cheaper than comparable OSS projects

**Status:** `NOT_EVIDENCED`

### Why

The external corpus has no common cost baseline and the internal log has no counterfactual OpenSiro control group.

There are reconstructable work-volume signals, including:

- multiple repair/reversal PRs in OpenSiro;
- notification/review-load signals in PydanticAI;
- staged migration work in OpenHands;
- abandoned/partial responses in AutoGen and LangGraph.

But these are not commensurate enough to support a quantitative speed/cost comparison.

### Allowed wording

> Quantitative development-cost or time advantage remains `NOT_EVIDENCED`.

### Do not write

> OpenSiro/VSM reduced engineering cost by X%.

or

> OpenSiro reached the same organizational mechanisms faster than the external projects.

---

## C11 — OpenSiro anticipated or avoided the organizational problems seen in the external cases

**Status:** `NOT_EVIDENCED`

### Why

The four external cases describe different disturbances at different system boundaries. OpenSiro has not yet accumulated equivalent operating history for several later functions, especially real S3, S2, and S4 usage.

The internal log also contains its own failures and reversals:

- wrong routing population;
- dedicated executor-proof overbuild and removal;
- ownership-proof ambiguity;
- M1 remaining open for lack of a real S3 event.

### Allowed wording

> The external cases generate falsifiable comparison questions for OpenSiro; they do not establish that OpenSiro avoided the same classes of failure.

### Do not write

> VSM let OpenSiro avoid the problems that AutoGen/OpenHands/LangGraph/PydanticAI encountered.

---

## C12 — VSM/OSM reduced total rework inside OpenSiro

**Status:** `NOT_EVIDENCED`

### Why

The log contains direct rework evidence but no baseline for whether the total amount is lower than under another method.

The executor-proof sequence is especially important counter-evidence: substantial proof infrastructure was built and then removed. The routing error also required reversions in three out-of-scope repositories plus Organization-side corrections.

### Allowed wording

> The evolution log now makes rework visible and attributable; it does not yet show that total rework is lower because of VSM/OSM.

### Do not write

> VSM reduced rework in OpenSiro.

---

## C13 — The S3 constructor has demonstrated development value

**Status:** `NOT_EVIDENCED`

### Why

The constructor surface and return hook exist, but #39 has not yet observed a qualifying real S3 transaction.

Without a real current-control event, the project cannot establish what effect the S3 path has on recovery time, decision quality, blocked work, or coordination cost.

### Allowed wording

> S3 infrastructure is ready but its real operational effect remains untested because the natural witness is still missing.

### Do not write

> S3 improved OpenSiro current control.

---

## C14 — The OpenSiro method is superior to ordinary OSS governance/engineering practice

**Status:** `NOT_EVIDENCED`

### Why

Every major internal transition also has a plausible ordinary-engineering explanation:

- scope correction;
- simplification after over-specification;
- staged architecture refinement;
- conservative experimental criteria;
- governance formalization;
- contributor/review triage.

The external PydanticAI case is particularly useful because it reaches a clear owner/support separation using ordinary project governance rather than explicit VSM terminology.

### Allowed wording

> The current evidence supports a disciplined comparative vocabulary and several observable process effects inside OpenSiro, but does not establish superiority over ordinary engineering/governance alternatives.

### Do not write

> VSM is a better way to build agent organizations than ordinary software engineering.

---

## Claim matrix

| ID | Candidate claim | Status | Article-safe use |
| --- | --- | --- | --- |
| C1 | Function-first decomposition is usable across unlike reviewed implementations | `SUPPORTED` | methodological result |
| C2 | Explicit boundary contract exposed wrong-population green routing oracle | `SUPPORTED` | OpenSiro case finding |
| C3 | Owner/support distinction changed architecture by removing executor-proof layer | `SUPPORTED` | OpenSiro process/architecture finding |
| C4 | Method permits a negative “not yet evidenced” milestone state | `SUPPORTED` | methodological/falsifiability finding |
| C5 | Real S3* use narrowed planned ownership from `A` to `C` | `SUPPORTED` | OpenSiro roadmap/evidence finding |
| C6 | Earlier real S5 event was classified retrospectively without rewriting chronology | `SUPPORTED` | evidence-method finding |
| C7 | Boundary/owner separation reduces future rework | `PLAUSIBLE` | hypothesis only |
| C8 | Canonical boundary-derived validator populations improve reliability | `PLAUSIBLE` | testable design hypothesis |
| C9 | Natural-witness policy improves evidentiary quality | `PLAUSIBLE` | methodology hypothesis |
| C10 | VSM/OSM made OpenSiro faster/cheaper | `NOT_EVIDENCED` | exclude as finding |
| C11 | OpenSiro anticipated/avoided external-project problems | `NOT_EVIDENCED` | exclude as finding |
| C12 | VSM/OSM reduced total OpenSiro rework | `NOT_EVIDENCED` | exclude as finding |
| C13 | S3 constructor has demonstrated operational value | `NOT_EVIDENCED` | exclude until #39 real witness |
| C14 | OpenSiro method is superior to ordinary engineering/governance | `NOT_EVIDENCED` | exclude as finding |

## What an article can responsibly claim today

A defensible current article can make a **methodological/process** contribution stronger than a **performance** contribution.

An article-safe core could be:

> OpenSiro applies a function-first organizational construction process that keeps decision rights, ownership evidence, support machinery, closure, and recursion boundaries separate. In the project's own history, this discipline exposed a validator bound to the wrong system boundary, contributed to removal of a dedicated executor-identity proof architecture, allowed a real audit function to remain constructor-owned rather than being promoted to autonomous ownership, and kept a milestone open when no natural S3 event existed. Four independent OSS histories show that the same evidence decomposition remains usable across unlike project vocabularies, while also falsifying two provisional patterns from the initial three-case sample. These observations establish process effects and a falsifiable comparison method, but they do not yet establish faster, cheaper, or lower-rework development than ordinary alternatives.

That paragraph is still a bounded summary, not proof of the downstream headline thesis.

## What evidence would upgrade the causal claims

For a stronger development-method paper, collect at least some of the following:

1. a real #39 S3 event with reconstructable time-to-decision, alternative local paths, returned effect, and any avoided/added work;
2. later S2/S4 events where the function-first distinction existed **before** repeated failure, not only after it;
3. repeated boundary/oracle incidents showing whether the canonical-boundary pattern actually prevents recurrence;
4. comparable timing/rework measures across internal events and selected external histories;
5. negative cases where the VSM distinction was made early but did **not** improve the implementation outcome;
6. fresh contributor-routing trials (#61/#80) that test whether explicit organizational surfaces improve behavior rather than merely existing in files.

## Current conclusion

The empirical track has enough evidence to support several concrete claims about **how OpenSiro's construction process behaves** and how its evidence schema compares unlike OSS histories.

It does **not** yet have evidence for the stronger claim that VSM/OSM materially reduces development cost, development time, or total rework.

The most important result at this stage is therefore not a superiority claim. It is a narrower research contribution:

> the method creates explicit, reviewable distinctions that can survive negative results, reversals, missing witnesses, and counterexamples without forcing every event into a completed VSM diagram.

Whether that discipline produces a measurable engineering advantage remains the next empirical question.
