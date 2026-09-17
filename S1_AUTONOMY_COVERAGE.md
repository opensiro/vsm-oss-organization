# S1 autonomy coverage

M0 is not complete merely because one autonomous-looking Pull Request exists. The current objective is to determine which operational work required by the viable-system identity can be admitted to S1, autonomously executed, independently validated, recovered when routine disturbances occur, and closed with reconstructable evidence.

The active S1 role is [`roles/S1.md`](roles/S1.md). M0 evaluates S1 against explicit operational action classes rather than against a particular runtime, GitHub API, model, or artifact type.

## M0 action-level contract

For one bounded S1 contribution, evaluate whether the system can perform these action classes without step-by-step human control:

| Action class | M0 question | Typical observable evidence |
| --- | --- | --- |
| **1. Inspect / observe** | Can S1 reconstruct the relevant current state and primary evidence before acting? | pinned/current refs, files/issues/PRs inspected, source-of-truth references |
| **2. Bound / admit** | Can S1 distinguish bounded operational work from undelegated authority/policy work? | `ADMIT` or `NON-ADMIT`, work boundary, outcome, authority, forbidden decisions, escalation conditions |
| **3. Choose local execution** | Can S1 choose the ordinary implementation/research/evidence/repair path itself? | observable action/results showing local strategy, ordering, evidence selection, tool/helper use, retry choices |
| **4. Produce / mutate** | Can S1 perform the actual bounded production work? | code/docs/data/research/generated artifact changes; branch/commit/PR or equivalent reviewable output |
| **5. Validate** | Can S1 distinguish a closed result from a plausible-looking result? | tests, validators, generation/provenance checks, primary-evidence comparison, diff inspection |
| **6. Recover** | Can S1 absorb ordinary local disturbances without human operational direction? | repair/retry/rebase/conflict resolution/reference repair/generated-drift repair or evidence-backed escalation |
| **7. Preserve evidence / package outcome** | Can another reviewer reconstruct the bounded result and its support? | start refs, evidence refs, changed surfaces, validation, interventions/escalations, final artifact refs |
| **8. Close or escalate** | Can S1 terminate honestly rather than forcing success? | `CLOSED_CHANGE`, `CLOSED_NO_CHANGE`, `ESCALATED`, or `NON_ADMITTED` |

These are organizational action classes. Git, GitHub, plugins/connectors, CI, validators, schedulers, helper agents, model/runtime selection, sandboxes, and deterministic enforcement are supporting mechanisms used to perform them.

A work class is not broadly covered merely because all eight actions happened once. Coverage asks whether the organization has a credible repeatable path for that class and whether unresolved judgment/authority boundaries remain explicit.

## Cross-cutting evidence questions

For each operational work class, evaluate the same questions:

1. **Admit** — can the system recognize the work item as bounded S1 work rather than an authority-level or metasystemic decision?
2. **Authority** — is the local decision envelope explicit enough for the agent to act without step-by-step human control?
3. **Execute** — are the repository surfaces and tools sufficient to perform the work?
4. **Validate** — is there a completion oracle strong enough for the S1 to distinguish a correct closed result from a plausible-looking result?
5. **Recover** — can routine failures or drift be handled inside S1 authority?
6. **Escalate** — are conditions that exceed S1 authority explicit and observable?
7. **Prove owner** — can a second reviewer reconstruct that the decisive local organizational discretion was exercised by the autonomous agent rather than hidden human control?

Use `yes`, `partial`, `no`, or `unknown`. These are coverage observations for this organization, **not** VSM autonomy states.

## Initial coverage matrix

| Work class | Admit | Authority | Execute | Validate | Recover | Escalate | Prove owner | Current blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bounded repository documentation / contributor-surface change | yes | yes | yes | partial | partial | yes | no | stronger machine-checkable closure where possible; strict executor identity deferred to Parent-assisted |
| Profile maintenance under an already-decided semantic change | partial | partial | yes | partial | unknown | partial | no | semantic acceptance remains evidence/reviewer judgment beyond deterministic repository consistency |
| Methodology / skill maintenance under released Profile semantics | partial | partial | yes | yes | partial | partial | no | admission boundary between local procedure work and semantic escalation |
| Index discovery / intake / deduplication | partial | partial | yes | partial | partial | partial | no | end-to-end admissibility/closure contract and evidence-intensive decisions |
| Index assessment / correction / reassessment | partial | partial | yes | yes | partial | yes | no | some judgment remains evidence-intensive and must preserve primary evidence |
| Index generated-view / provenance maintenance | yes | partial | yes | yes | partial | partial | no | explicit S1 authority for repair choices |
| Awesome VSM Harness curation | partial | partial | yes | partial | unknown | partial | no | curation judgment remains non-deterministic even where canonical consistency is machine-checked |
| Organization/control-plane maintenance inside released semantics | partial | partial | yes | partial | partial | yes | no | semantic/authority changes remain outside ordinary S1 even though contract consistency is machine-checked |
| released-contract semantic change | no | no | technically possible | not an S1 closure question | n/a | yes | n/a | requires the authority/process that owns semantic change; do not force into M0 S1 |
| organizational scope / identity / ultimate-policy change | no | no | technically possible | not an S1 closure question | n/a | yes | n/a | outside ordinary S1 authority |

The matrix is intentionally conservative. `partial` means a credible path exists but the current repository contract does not yet make autonomous closure independently reconstructable across the whole work class.

## Current M0 implementation priorities

M0 should improve S1 itself before introducing later VSM functions.

### 1. Explicit operational action coverage

The active S1 role must expose the complete loop:

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

No later VSM role is required to complete this operational loop. A human merge boundary may remain outside S1.

### 2. Completion-oracle coverage

Autonomous S1 work requires reliable closure evidence. This is broader than traditional unit-test coverage.

Examples:

```text
code / scripts
→ tests and static validation

structured corpus
→ schema + provenance + deterministic-generation checks

documentation / contracts
→ reference + version + link + cross-file consistency checks

assessment work
→ Methodology conformance + pinned primary evidence

release work
→ version + tag + source/provenance consistency

curation
→ canonical upstream existence + link/fact consistency + format checks
```

All five in-scope repositories expose deterministic validation surfaces for at least part of their ordinary work, and the Profile/Organization path additionally checks upstream contract compatibility across repositories. Coverage is intentionally uneven: semantic correctness, evidence interpretation, curation judgment, authority changes, and other non-deterministic decisions must not be disguised as unit tests merely to increase machine-checked coverage.

### 3. Admission and escalation coverage

S1 must distinguish ordinary operational work from decisions outside its authority:

```text
for every presented work item:
    admit as bounded S1 work
    or
    produce an explicit evidence-backed non-admission / escalation

never silently replace missing authority with hidden human step-by-step control
```

### 4. Routine-recovery coverage

Do not manufacture failures. When natural stale bases, validation failures, evidence gaps, broken references, generated-file drift, tool failures, or ordinary conflicts occur, preserve whether S1 detected and repaired them without human operational direction.

### 5. Strict executor-ownership proof debt

The instrumented M0 trial in issue #16 / PR #17 established a bounded operational loop but could not independently establish the decision owner from repository-only attribution.

The stronger distinct-executor identity mechanism is intentionally deferred to Parent-assisted work in #35. Until it is implemented and exercised, formal public evidence for `S1=A` remains insufficient on that dimension.

This deferred proof debt does **not** require M0 to add a new chatbot/model, S3/S3*, or an agent-specific GitHub identity now. The current M0 engineering task is to make the S1 operational contract itself explicit and usable.

## M0 completion direction

The immediate operational target is:

> One bounded S1 can inspect current reality, admit or reject the work, choose local actions, produce the bounded outcome, validate it, recover from ordinary local disturbances, preserve reviewable evidence, and close or escalate without step-by-step human operational control.

Formal `S1=A` remains a separate evidence claim under the governing Methodology. The deferred executor-identity gap must not be silently erased.

After the S1 operational contract is stable, expand **S1 operational-variety coverage** across the work domain. Introduce later VSM functions only when measured residual variety cannot be absorbed by S1 or by already-established functions.
