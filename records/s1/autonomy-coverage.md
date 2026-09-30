# S1 operational coverage

M0 constructed three declared operational S1 domains:

- **Index** — `opensiro/vsm-harness-index`;
- **Skills** — `opensiro/vsm-harness-skills`;
- **Awesome** — `opensiro/awesome-vsm-harness`.

`opensiro/vsm-harness-profile` and `opensiro/vsm-oss-organization` are not current operational S1 domains. Profile supplies normative semantics; Organization is the metasystem/control-construction surface.

The executable actor adapter is [`../../roles/S1.md`](../../roles/S1.md). Canonical local envelopes are in [`../../contracts/s1/domain-contracts.md`](../../contracts/s1/domain-contracts.md). Admission/recovery is governed by [`../../contracts/s1/task-admission-recovery.md`](../../contracts/s1/task-admission-recovery.md).

## Operational path

For one bounded contribution inside exactly one declared domain, the first-party construction supports:

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

Terminal states are `CLOSED_CHANGE`, `CLOSED_NO_CHANGE`, `ESCALATED`, and `NON_ADMITTED`.

Git, GitHub, plugins/connectors, CI, validators, schedulers, helper agents, model/runtime selection, sandboxes, and deterministic enforcement are supporting mechanisms. Their presence does not establish a VSM function or autonomy state.

## Domain evidence

### Index

Representative evidence: `opensiro/vsm-harness-index#114` performed canonical admission work, updated dependent corpus/provenance/generated surfaces, encountered and repaired a completion-oracle defect, added regression coverage, and completed repository validation.

### Skills

Representative evidence: `opensiro/vsm-harness-skills#9`, `#11`, and `#16` identified provenance/validation failures, repaired them inside the selected procedural contract, and added deterministic regression coverage without redefining Profile semantics.

### Awesome

Representative evidence: `opensiro/awesome-vsm-harness#2`, `#3`, and `#4` performed real curation, subsequent narrowing/correction, and deterministic Index-consistency validation while preserving canonical assessment ownership in Index.

## Construction status

| S1 domain | Explicit envelope | Local execution path | Completion evidence | Routine correction/recovery | Residual-variety escalation |
| --- | --- | --- | --- | --- | --- |
| Index | yes | yes | yes | yes | yes |
| Skills | yes | yes | yes | yes | yes |
| Awesome | yes | yes | yes | yes | yes |

These are **construction and operational-path claims**. They do not by themselves establish `S1=A`.

The organization intentionally allows contributor-owned runtimes, schedulers, model choice, credentials, budgets, and sandboxes. Whether a concrete deployed mode therefore qualifies as `A`, `C`, another ownership arrangement, or insufficient evidence is a separate Methodology question. See [`../assessment-snapshots/2026-09-30-general-preassessment.md`](../assessment-snapshots/2026-09-30-general-preassessment.md) for one bounded independent pre-assessment.

## Residual variety

Residual variety becomes evidence for a later VSM function only when the concrete disturbance and required relation are established. For example:

- concrete interference among S1 domains may justify S2;
- whole-system current resource/commitment regulation may justify S3;
- materially complementary audit may justify S3*;
- external/future adaptation with closure into present capability may justify S4;
- identity/ultimate-policy closure may justify S5.

Do not infer those functions from repository names, routing, scheduling, or the existence of constructor files.

Supplementary development history under [`../../supplementary/`](../../supplementary/) remains research evidence, not a fourth operational S1 domain.
