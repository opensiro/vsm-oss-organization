# S1 autonomy coverage

M0 covers three declared operational S1 domains:

- **Index** — `opensiro/vsm-harness-index`;
- **Skills** — `opensiro/vsm-harness-skills`;
- **Awesome** — `opensiro/awesome-vsm-harness`.

`opensiro/vsm-harness-profile` and `opensiro/vsm-oss-organization` are not current operational S1 domains. Profile supplies normative semantics; Organization is the metasystem/control-construction surface. Work on those repositories is not positive M0 evidence of local S1 autonomy.

The common role is [`roles/S1.md`](roles/S1.md). The canonical local envelopes are in [`S1_DOMAIN_CONTRACTS.md`](S1_DOMAIN_CONTRACTS.md). Admission/recovery is governed by [`S1_TASK_ADMISSION_RECOVERY.md`](S1_TASK_ADMISSION_RECOVERY.md).

## M0 action-level contract

For one bounded contribution inside exactly one declared domain, the S1 path supports:

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

Terminal states remain:

- `CLOSED_CHANGE`
- `CLOSED_NO_CHANGE`
- `ESCALATED`
- `NON_ADMITTED`

Git, GitHub, plugins/connectors, CI, validators, schedulers, helper agents, model/runtime selection, sandboxes, and deterministic enforcement are supporting mechanisms. Their presence does not establish a VSM function or autonomy state.

## Domain boundaries

### Index S1

**Durable outcome:** canonical evidence-backed harness corpus, reassessment/provenance history, signatures, and deterministic comparative views.

**Local environment / variety:** public harness repositories and upstream changes, discovery/intake sources, primary evidence, assessment/reassessment triggers, deduplication, corpus corrections, generated-view drift, and provenance repair.

**Local authority:** evidence collection, application of the selected Methodology, repository-relative assessment/correction/reassessment judgments, task-local corpus/provenance updates, deterministic regeneration/validation, and routine repair inside the selected contract.

**Escalate:** Profile semantics, system-wide Methodology authority changes, organization identity/scope, cross-S1 authority, later metasystem decisions, security/permissions/licensing/protected-branch policy.

### Skills S1

**Durable outcome:** reusable VSM Harness assessment procedure/skills/tooling that applies the selected Profile without redefining it.

**Local environment / variety:** selected Profile semantics/provenance, procedure implementation, skill/reference files, sync/generation tooling, tests/validators, and downstream procedure consumers.

**Local authority:** implementation/repair of an already-selected procedure, skill/tool/reference maintenance, upstream artifact synchronization, deterministic procedure/provenance validation, and routine repair inside the current procedural contract.

**Escalate:** Profile semantic change, selection of new system-wide Methodology policy/authority, cross-S1 decision rights, organization identity/scope, later metasystem decisions, security/permissions/licensing/protected-branch policy.

Repository location alone is insufficient: a file in `vsm-harness-skills` is not automatically S1 work.

### Awesome S1

**Durable outcome:** curated representative downstream view for the OSS community linked to canonical Index facts.

**Local environment / variety:** current Index corpus, representative candidate forms, editorial evidence, community-facing presentation needs, and canonical link/fact drift.

**Local authority:** representative curation under current editorial criteria, section organization/narrowing, local descriptions, canonical link/anchor repair, and downstream consistency/format validation without copying or redefining Index facts.

**Escalate:** changes to Index assessments/canonical state, Profile/Methodology semantics, organization identity/policy, cross-S1 authority, later metasystem decisions, security/permissions/licensing/protected-branch policy.

## M0 operational evidence

M0 does not require synthetic trials when equivalent real work already exists. The following merged work provides representative operational evidence for each domain.

### Index evidence

`opensiro/vsm-harness-index#114`:

- admitted and canonicalized real assessment work under the selected contract;
- updated dependent corpus/provenance/generated surfaces;
- discovered a validator/completion-oracle defect during execution;
- repaired the defect and added regression tests;
- completed repository validation before merge.

This demonstrates a real inspect/decide/mutate/validate/recover/close path inside the Index domain.

### Skills evidence

`opensiro/vsm-harness-skills#9`, `#11`, and `#16`:

- identified provenance/validation failures inside the existing procedural contract;
- repaired source-revision/history handling without changing Profile semantics;
- added deterministic regression coverage for the Methodology publication contract;
- kept semantic correctness outside the scope of mechanical tests.

This demonstrates a real repair/validation/closure path inside the Skills domain.

### Awesome evidence

`opensiro/awesome-vsm-harness#2`, `#3`, and `#4`:

- performed real editorial curation under explicit representative-form criteria;
- narrowed an over-broad domain presentation in a follow-up change rather than treating the first design as final;
- added deterministic Awesome ↔ Index consistency validation while keeping editorial judgment non-deterministic and canonical assessment ownership in Index.

This demonstrates a real curation/correction/validation path inside the Awesome domain.

## M0 construction status

| S1 domain | Explicit envelope | Local execution path | Completion evidence | Routine correction/recovery path | Residual-variety escalation | Independent owner proof |
| --- | --- | --- | --- | --- | --- | --- |
| **Index** | yes | yes | yes | yes | yes | no — deferred |
| **Skills** | yes | yes | yes | yes | yes | no — deferred |
| **Awesome** | yes | yes | yes | yes | yes | no — deferred |

The first five columns are M0 operational-construction claims. They do **not** imply the final column.

## Local variety versus residual variety

The governing design rule is:

```text
local disturbance
        ↓
can the relevant S1 distinguish it and act with delegated authority?
        ├─ yes → absorb locally
        └─ no  → preserve residual variety and escalate
```

The metasystem should not duplicate ordinary Index, Skills, or Awesome decisions merely to centralize control.

Residual variety becomes evidence for a later VSM function only when the concrete disturbance and required relation are established. For example:

- concrete interference among S1 domains may justify S2;
- whole-system current resource/commitment regulation may justify S3;
- materially complementary audit may justify S3*;
- external/future adaptation with closure into present capability may justify S4;
- identity/ultimate-policy closure may justify S5.

Do not infer those functions merely because Profile or Organization repositories exist.

## Strict executor-ownership proof debt

The repository evidence above is attributable through the contributor's GitHub account. It demonstrates operational paths, but it does not independently prove that an autonomous executor owned every decisive local choice rather than receiving hidden human operational direction.

The stronger distinct-executor identity mechanism is now an M1 proof dependency in `#35`. Until it is implemented and exercised, formal public evidence for the published autonomy state `S1=A` remains insufficient on this dimension. M2 consumes that capability later under an explicit parent-governance envelope; it does not gate creation of the proof witness itself.

M0 completion therefore means:

> the S1 organization is constructed and operationally exercised across Index, Skills, and Awesome, with explicit local authority, completion evidence, recovery, and escalation boundaries.

It does **not** mean:

> the deferred actor-attribution problem has been solved or that repository attribution alone proves `S1=A`.

## Supplementary development evidence

`supplementary/evolution-log.md` and related case studies are side artifacts of building and studying this organization. They are not a fourth S1 domain and not part of the primary production transformation.

Their primary downstream purpose is to support a future evidence-backed article/case study testing whether VSM/OSM exposed organizational problems earlier, reduced rework/coordination cost, or otherwise improved development relative to plausible organically evolved alternatives. Reusable skills/methodology extraction is a possible secondary use.
