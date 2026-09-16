# S1 autonomy coverage

M0 is not complete merely because one autonomous-looking Pull Request exists. The current objective is to determine which operational work required by the viable-system identity can be admitted to S1, autonomously executed, independently validated, recovered when routine disturbances occur, and closed with reconstructable ownership evidence.

For each operational work class, evaluate the same seven questions:

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
| bounded repository documentation / contributor-surface change | yes | yes | yes | partial | partial | yes | no | executor provenance witness; stronger machine-checkable closure where possible |
| Profile maintenance under an already-decided semantic change | partial | partial | yes | partial | unknown | partial | no | no repository CI/completion oracle for consistency of normative/version/release surfaces; owner witness |
| Methodology / skill maintenance under released Profile semantics | partial | partial | yes | yes | partial | partial | no | owner witness; admission boundary between local procedure work and semantic escalation |
| Index discovery / intake / deduplication | partial | partial | yes | partial | partial | partial | no | end-to-end admissibility/closure contract; owner witness |
| Index assessment / correction / reassessment | partial | partial | yes | yes | partial | yes | no | owner witness; some judgment remains evidence-intensive and must preserve primary evidence |
| Index generated-view / provenance maintenance | yes | partial | yes | yes | partial | partial | no | owner witness; explicit S1 authority for repair choices |
| Awesome VSM Harness curation | partial | partial | yes | partial | unknown | partial | no | upstream consistency checks stronger than `awesome-lint`; explicit curation authority; owner witness |
| Organization/control-plane maintenance inside released semantics | partial | partial | yes | partial | partial | yes | no | owner witness; completion checks for cross-file scope/contract consistency |
| released-contract semantic change | no | no | technically possible | not an S1 closure question | n/a | yes | n/a | requires the authority/process that owns semantic change; do not force into M0 S1 |
| organizational scope / identity / ultimate-policy change | no | no | technically possible | not an S1 closure question | n/a | yes | n/a | outside ordinary S1 authority |

The matrix is intentionally conservative. `partial` means a credible path exists but the current repository contract does not yet make autonomous closure independently reconstructable across the whole work class.

## Current M0 blockers

The next engineering work should reduce blockers in this order without adding later VSM functions merely to complete the diagram:

### 1. Executor provenance witness

The instrumented M0 trial in issue #16 / PR #17 established function, decision-right boundary, support separation, validation, and closure but could not independently establish the owner from repository-only primary evidence. M0 therefore remains open.

The missing capability is a runtime-neutral primary witness that can bind a frozen S1 prompt/session or execution identity to subsequent observable decisions/actions without relying on retrospective self-assertion. A dedicated GitHub bot identity is one possible implementation; a signed runtime attestation is another. The organizational contract must not require one vendor or centralized runtime.

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

Current repositories are uneven here: `vsm-harness-skills`, `vsm-harness-index`, and `awesome-vsm-harness` already expose CI checks, while `vsm-harness-profile` and `vsm-oss-organization` currently rely more heavily on reviewable textual evidence.

### 3. Task-admission contract

S1 must distinguish ordinary operational work from decisions that belong outside its authority. The goal is not to make every GitHub task autonomous. The goal is:

```text
for every presented work item:
    admit as bounded S1 work
    or
    produce an explicit evidence-backed escalation

never silently replace missing authority with hidden human step-by-step control
```

### 4. Routine-recovery coverage

Do not manufacture failures. Instead, when natural stale bases, validation failures, evidence gaps, broken references, or generated-file drift occur, preserve whether the S1 detected and repaired them without human operational direction.

## M0 completion direction

The immediate reference proof remains deliberately narrow:

> Establish one reproducible bounded S1 setup in which the decisive local contribution discretion is agent-owned, the result can be independently validated, routine local variety can be absorbed without step-by-step human control, and the ownership/closure evidence is reconstructable by a second reviewer.

After that proof, use this matrix to expand **S1 operational-variety coverage** across the work domain. Later VSM functions should be introduced only when measured residual variety cannot be absorbed by S1 or by already-established functions.