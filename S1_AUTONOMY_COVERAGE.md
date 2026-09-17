# S1 autonomy coverage

M0 evaluates autonomous operation across three declared S1 domains:

- **Index** — `opensiro/vsm-harness-index`;
- **Skills** — `opensiro/vsm-harness-skills`;
- **Awesome** — `opensiro/awesome-vsm-harness`.

`opensiro/vsm-harness-profile` and `opensiro/vsm-oss-organization` are not current operational S1 domains. Profile supplies normative semantics; Organization is the metasystem/control construction surface. Work on those surfaces may be necessary for the larger viable system, but it is not positive evidence of local S1 autonomy for M0.

The active S1 role is [`roles/S1.md`](roles/S1.md). M0 evaluates each operational domain against explicit action classes rather than against a particular runtime, GitHub API, model, or artifact type.

## M0 action-level contract

For one bounded S1 contribution inside one declared domain, evaluate whether the system can perform these action classes without step-by-step human control:

| Action class | M0 question | Typical observable evidence |
| --- | --- | --- |
| **1. Inspect / observe** | Can S1 reconstruct the relevant current state and primary evidence before acting? | pinned/current refs, files/issues/PRs inspected, source-of-truth references |
| **2. Bound / admit** | Can S1 distinguish local operational work from undelegated normative/metasystem decisions? | domain, `ADMIT` or `NON-ADMIT`, work boundary, outcome, authority, forbidden decisions, escalation conditions |
| **3. Choose local execution** | Can S1 choose the ordinary implementation/research/evidence/repair path itself? | observable action/results showing local strategy, ordering, evidence selection, tool/helper use, retry choices |
| **4. Produce / mutate** | Can S1 perform the actual bounded production work of the domain? | code/docs/data/research/generated artifact changes; branch/commit/PR or equivalent reviewable output |
| **5. Validate** | Can S1 distinguish a closed result from a plausible-looking result? | tests, validators, generation/provenance checks, primary-evidence comparison, diff inspection |
| **6. Recover** | Can S1 absorb ordinary local disturbances without human operational direction? | repair/retry/rebase/conflict resolution/reference repair/generated-drift repair or evidence-backed escalation |
| **7. Preserve evidence / package outcome** | Can another reviewer reconstruct the bounded result and its support? | start refs, evidence refs, changed surfaces, validation, interventions/escalations, final artifact refs |
| **8. Close or escalate** | Can S1 terminate honestly rather than forcing success? | `CLOSED_CHANGE`, `CLOSED_NO_CHANGE`, `ESCALATED`, or `NON_ADMITTED` |

These are organizational action classes. Git, GitHub, plugins/connectors, CI, validators, schedulers, helper agents, model/runtime selection, sandboxes, and deterministic enforcement are supporting mechanisms used to perform them.

## Domain boundaries

### Index S1

**Durable outcome:** canonical evidence-backed harness corpus, reassessment/provenance history, signatures, and deterministic comparative views.

**Local environment / variety:** public harness repositories and changes, discovery/intake sources, primary evidence, assessment/reassessment triggers, deduplication, corpus corrections, generated-view drift, provenance repair.

**Typical local work:** discovery, intake/deduplication, evidence collection, assessment/correction/reassessment under the selected contract, catalog/provenance maintenance, deterministic regeneration/validation.

**Escalate out of S1 when:** closure requires changing normative Profile semantics, changing system-wide assessment authority rather than applying the selected contract, changing organization identity/scope, or resolving a cross-S1/metasystem issue.

### Skills S1

**Durable outcome:** reusable VSM Harness assessment procedure/skills/tooling that applies the selected Profile without redefining it.

**Local environment / variety:** selected Profile semantics, current assessment practice, procedure/tool implementation defects, tests/validators, generated/synced artifacts, downstream skill consumers.

**Typical local work:** implement or repair an already-selected procedure, maintain skills/tooling/tests, synchronize selected upstream artifacts, improve executable procedure surfaces without silently changing normative authority.

**Escalate out of S1 when:** the work would redefine Profile semantics, alter system-wide normative/procedural authority, change cross-S1 decision rights, or otherwise modify the metasystem rather than the local Skills outcome.

Repository location alone is insufficient: a file in `vsm-harness-skills` is not automatically S1 work.

### Awesome S1

**Durable outcome:** curated representative downstream view for the OSS community linked to canonical Index facts.

**Local environment / variety:** current Index corpus, representative candidate forms, community-facing presentation needs, editorial evidence, canonical link/fact drift.

**Typical local work:** curate representative entries, maintain descriptions/structure, repair canonical relationships, validate downstream consistency without duplicating Index facts.

**Escalate out of S1 when:** the work would redefine Index assessments, Profile semantics, organization identity/policy, or cross-S1/metasystem authority.

## Cross-cutting coverage questions

For each domain, evaluate the same questions:

1. **Admit** — can the system recognize local bounded S1 work rather than an authority-level or metasystemic decision?
2. **Authority** — is the local decision envelope explicit enough for the agent to act without step-by-step human control?
3. **Execute** — are the repository surfaces and tools sufficient to perform the local work?
4. **Validate** — is there a completion oracle strong enough to distinguish a correct closed result from a plausible-looking result?
5. **Recover** — can routine local failures or drift be handled inside the domain's authority?
6. **Escalate** — are residual-variety conditions that exceed local authority explicit and observable?
7. **Prove owner** — can a second reviewer reconstruct that the decisive local discretion was exercised by the autonomous agent rather than hidden human control?

Use `yes`, `partial`, `no`, or `unknown`. These are coverage observations, **not** VSM autonomy states.

## Current domain coverage

| S1 domain | Admit | Authority | Execute | Validate | Recover | Escalate | Prove owner | Current blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Index** | partial | partial | yes | yes | partial | yes | no | sharpen repeatable admission/authority coverage across discovery, assessment, reassessment and corpus maintenance; strict executor identity deferred |
| **Skills** | partial | partial | yes | yes | partial | yes | no | keep implementation of selected procedure distinct from system-wide normative/procedural authority; strict executor identity deferred |
| **Awesome** | partial | partial | yes | partial | partial | yes | no | curation judgment remains non-deterministic even where canonical consistency is machine-checked; strict executor identity deferred |

The matrix is intentionally conservative. `partial` means a credible operational path exists but autonomous closure is not yet independently reconstructable across the whole domain.

## Local variety versus residual variety

The governing design rule is:

```text
local disturbance
        ↓
can the relevant S1 distinguish it and act with delegated authority?
        ├─ yes → absorb locally
        └─ no  → preserve residual variety and escalate
```

The metasystem should not duplicate ordinary Index, Skills, or Awesome decisions merely to centralize control. Residual variety becomes evidence for a later organizational function only when the concrete disturbance and required relation are established.

Examples:

- concrete interference among the three S1 domains may justify S2;
- whole-system current resource/commitment regulation may justify S3;
- materially complementary audit of operational claims may justify S3*;
- external/future adaptation with closure into present capability may justify S4;
- identity/ultimate-policy closure may justify S5.

Do not infer those functions merely because the Profile or Organization repositories exist.

## M0 implementation priorities

### 1. Domain-specific action coverage

Each of the three operational domains should support the same bounded loop:

```text
inspect / observe
        ↓
bound / admit
        ↓
choose local execution
        ↓
produce / mutate
        ↓
validate
        ↓
recover when needed
        ↓
preserve evidence / package outcome
        ↓
close or escalate
```

No later VSM role is required to complete this local operational loop. A human merge boundary may remain outside S1.

### 2. Completion-oracle coverage

Use domain-appropriate closure evidence:

```text
Index
→ Methodology conformance + pinned primary evidence + corpus/provenance/generation checks

Skills
→ tests + Profile/source sync + procedure/tool validation

Awesome
→ editorial evidence + format checks + canonical Index relationship validation
```

Semantic correctness, evidence interpretation, curation judgment, authority changes, and other non-deterministic decisions must not be disguised as unit tests merely to increase machine-checked coverage.

### 3. Admission and escalation coverage

For every presented item:

```text
admit as bounded local S1 work
or
produce explicit evidence-backed non-admission / escalation
```

Do not silently route Profile/Organization/metasystem work through S1 just because a repository is writable.

### 4. Routine-recovery coverage

Do not manufacture failures. Preserve whether S1 detects and repairs natural stale bases, validation failures, evidence gaps, broken references, generated drift, tool failures, or ordinary conflicts inside its local authority.

### 5. Strict executor-ownership proof debt

The stronger distinct-executor identity mechanism remains intentionally deferred to Parent-assisted work in #35. Until it is implemented and exercised, formal public evidence for `S1=A` remains insufficient on executor ownership.

This deferred proof debt does **not** require M0 to add a new chatbot/model, S3/S3*, or an agent-specific GitHub identity now.

## Supplementary development evidence

`supplementary/evolution-log.md` and related empirical histories are side artifacts of developing and studying this organization. They are useful evidence for later methodology extraction, but they are **not a fourth operational S1 domain and not part of the primary production transformation**.

A future separate pipeline may derive reusable skills or methodology artifacts from those histories. That pipeline is planned only; it is not part of the current M0 operational architecture.

## M0 completion direction

The operational target is:

> Index, Skills, and Awesome each have a bounded local S1 path that can inspect current reality, admit or reject work, choose local actions, produce the domain outcome, validate it, recover from ordinary local disturbances, preserve reviewable evidence, and close or escalate without step-by-step human operational control.

Formal `S1=A` remains a separate evidence claim under the governing Methodology. The deferred executor-identity gap must not be silently erased.