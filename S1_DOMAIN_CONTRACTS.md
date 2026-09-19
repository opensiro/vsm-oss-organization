# S1 domain contracts

This file defines the current M0 operational envelopes for the three S1 domains of the OpenSiro VSM Harness OSS organization.

It applies the VSM Harness Profile but does not redefine S1. Repository location alone is not sufficient to classify work as S1: the decisive work must contribute directly to the declared local operational outcome and stay inside the local authority envelope.

The active M0 S1 domains are:

- **Index** — `opensiro/vsm-harness-index`
- **Skills** — `opensiro/vsm-harness-skills`
- **Awesome** — `opensiro/awesome-vsm-harness`

`opensiro/vsm-harness-profile` is the normative semantic source. `opensiro/vsm-oss-organization` is the metasystem/control-construction surface. Neither is an M0 operational S1 domain.

## Common local S1 contract

Every admitted S1 run must declare exactly one domain and then perform the common action loop from `roles/S1.md`:

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
preserve evidence
        ↓
close or escalate
```

Local variety should be absorbed by the relevant S1 whenever it has the requisite information and delegated authority. Residual variety must be preserved and escalated rather than silently centralized or solved through undelegated authority.

## Index domain

### Durable outcome

Maintain the canonical evidence-backed harness corpus, accepted assessment state, reassessment/provenance history, cohort signatures, and deterministic comparative views.

### Local environment

- public harness repositories and upstream changes;
- discovery/intake sources and candidate batches;
- pinned primary evidence;
- selected Profile/Methodology contract;
- canonical assessments, catalog/provenance, signatures, TLDR and Rankings;
- repository validators and generation tooling.

### Local decision rights

Within an admitted Index work item, S1 may decide:

- how to collect and compare primary repository evidence;
- whether a candidate is duplicate/in-scope at the Index boundary;
- how to apply the selected assessment Methodology to the evidence;
- whether a reassessment/correction is change, no-change, or insufficient-evidence at the pinned boundary;
- which canonical Index surfaces must change as a consequence of that local result;
- how to repair task-local provenance/generation/validation failures without changing the governing semantic contract;
- how to package the result as a reviewable PR or evidence-backed no-change closure.

### Completion evidence

Use the strongest applicable combination of:

- pinned/checked upstream refs and primary evidence links;
- Methodology-conformant assessment artifact;
- catalog/provenance/signature consistency;
- deterministic TLDR/Rankings generation checks where affected;
- Index repository validators/tests;
- exact final diff and append-only history checks.

### Escalate out of Index S1

Escalate when closure requires:

- changing VSM Profile semantics;
- changing system-wide assessment authority rather than applying the selected Methodology;
- changing organization identity/scope;
- resolving cross-S1 authority or whole-system control;
- repository/account security, permission, licensing, or protected-branch policy decisions.

### Representative real evidence path

`opensiro/vsm-harness-index#114` performed real canonical admission work, regenerated dependent views, discovered a completion-oracle defect during execution, repaired it, added regression coverage, and completed repository validation. This is evidence of the operational path and local recovery capability.

## Skills domain

### Durable outcome

Maintain reusable VSM Harness assessment procedure, skills, references, synchronization/provenance tooling, and deterministic procedure-validation surfaces that apply the selected Profile without redefining it.

### Local environment

- selected/released Profile semantics and provenance;
- current assessment procedure implementation;
- procedure/tooling defects;
- skill/reference files and synchronized/generated artifacts;
- validators/tests and downstream consumers of the selected procedure.

### Local decision rights

Within an admitted Skills work item, S1 may decide:

- how to implement or repair an already-selected procedure;
- how to maintain skill/reference/tooling consistency;
- how to synchronize or validate authoritative upstream Profile artifacts without changing their semantics;
- how to repair provenance, validation, generation, or test failures inside the existing procedural contract;
- how to add regression coverage for deterministic procedure invariants;
- how to package the result as a reviewable PR or evidence-backed no-change closure.

Repository location alone is not enough. A proposed change to the system-wide normative/procedural contract must not be smuggled through as ordinary local implementation merely because the file lives in `vsm-harness-skills`.

### Completion evidence

Use the strongest applicable combination of:

- selected Profile version/source provenance;
- procedure/reference consistency;
- repository validator results;
- unit/regression tests;
- Profile snapshot/synchronization checks;
- exact final diff and version/provenance checks when affected.

### Escalate out of Skills S1

Escalate when closure requires:

- redefining Profile semantics;
- selecting a new system-wide Methodology policy/authority rather than implementing an already-authorized procedure;
- changing cross-S1 decision rights;
- changing organization identity/scope or later VSM functions;
- repository/account security, permission, licensing, or protected-branch policy decisions.

### Representative real evidence path

`opensiro/vsm-harness-skills#9`, `#11`, and `#16` show the local repair loop: provenance/validation defects were identified, corrected within the existing contract, and covered by deterministic regression tests. This is evidence of operational repair/validation capability.

## Awesome domain

### Durable outcome

Maintain a curated representative downstream view of organizational forms for the OSS community while keeping canonical assessment facts in the Index.

### Local environment

- current canonical Index corpus and stable links/anchors;
- candidate representative organizational forms;
- editorial evidence about operating domain, organizational distinctiveness, evidence quality, and current relevance;
- community-facing structure and presentation;
- Awesome lint and Index-consistency validation.

### Local decision rights

Within an admitted Awesome work item, S1 may decide:

- whether and how a candidate is representative under the current editorial criteria;
- how to organize or narrow sections to keep the view useful and non-duplicative;
- how to describe organizational form without copying canonical assessment state;
- how to repair canonical links, anchors, formatting, or downstream relationship drift;
- how to package the result as a reviewable PR or evidence-backed no-change closure.

Editorial judgment may be non-deterministic. Deterministic checks constrain factual/canonical consistency but do not own the curation decision.

### Completion evidence

Use the strongest applicable combination of:

- current canonical Index assessment/link relationship;
- evidence supporting representative form/domain relevance;
- Awesome formatting/lint checks;
- Index-consistency validator results;
- exact final diff showing no copied canonical vectors/ranks/signatures where prohibited.

### Escalate out of Awesome S1

Escalate when closure requires:

- changing an Index assessment or canonical state;
- redefining Profile semantics or Methodology;
- changing organization identity/policy or cross-S1 authority;
- repository/account security, permission, licensing, or protected-branch policy decisions.

### Representative real evidence path

`opensiro/awesome-vsm-harness#2`, `#3`, and `#4` show real curation, subsequent narrowing of the editorial surface, and addition of deterministic canonical-Index consistency checks. Together they establish a real local operating/validation path while leaving canonical assessment ownership in Index.

## M0 completion interpretation

M0 construction is complete when all three domains have:

- an explicit local outcome/environment/authority envelope;
- the common S1 action loop;
- an evidence-backed completion path;
- explicit residual-variety escalation boundaries;
- at least one real operational evidence path.

This is a construction/operational milestone. Any formal autonomy-state publication remains governed by the selected Profile/Methodology; this organization does not add a separate executor-identity or GitHub actor-attribution requirement.
