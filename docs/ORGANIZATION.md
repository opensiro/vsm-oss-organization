# Viable-system identity

This repository organizes one bounded public viable system: the **OpenSiro VSM Harness OSS organization**.

Its purpose is to maintain for the open-source community public, current, evidence-backed VSM Harness knowledge through three operational domains while consuming a separate normative semantic source and evolving the organization itself through a separate metasystem/control plane.

## Operations and metasystem boundary

The current architecture separates the operational S1 plane from the normative/metasystem plane:

```text
normative / metasystem plane
├── opensiro/vsm-harness-profile
│   └── authoritative VSM semantics
└── opensiro/vsm-oss-organization
    └── organizational/control construction

operational S1 plane
├── opensiro/vsm-harness-index
├── opensiro/vsm-harness-skills
└── opensiro/awesome-vsm-harness
```

This is a system-boundary statement, not a shortcut from repository name to VSM function.

`vsm-harness-profile` is the authoritative semantic source consumed by this organization. It is not an operational S1 product of the current system-in-focus, and it is not automatically classified as S5 merely because it carries normative authority.

`vsm-oss-organization` is where later metasystem/control functions are constructed and evidenced. The repository itself is not automatically S2, S3, S3*, S4, or S5. Each such function must still be established from the concrete variety it regulates, its decisive decision/feedback right, owner, support, and closure.

## Three operational S1 domains

M0 currently declares exactly three operational S1 domains.

| S1 domain | Local environment | Durable operational outcome |
| --- | --- | --- |
| **Index** — `opensiro/vsm-harness-index` | public harness repositories and changes; candidate/intake sources; primary evidence; selected Profile/Methodology contract; corpus corrections and reassessment triggers | evidence-backed canonical corpus, provenance, reassessment history, signatures, and deterministic comparative views |
| **Skills** — `opensiro/vsm-harness-skills` | selected Profile semantics; assessment practice; procedure/tool defects; tests; downstream users of VSM Harness assessment skills | reusable assessment procedure/skills/tooling that apply the selected Profile without redefining it |
| **Awesome** — `opensiro/awesome-vsm-harness` | canonical Index state; candidate representative forms; community-facing presentation needs; editorial evidence | curated representative downstream view linked to canonical Index facts |

Repository location alone is not enough to classify work as S1. The decisive question is whether the work produces the local operational outcome inside the declared authority envelope.

For example, implementation or repair of an already-selected assessment procedure in `vsm-harness-skills` may be ordinary Skills S1 work. A change that redefines system-wide normative semantics, organizational identity, cross-S1 authority, or another metasystemic decision leaves the ordinary S1 boundary even if the edited file physically lives in an operational repository.

## Primary transformation

The operational transformation is now expressed without treating Profile evolution or organization design as S1 production:

```text
selected normative semantics / procedure contract
                    ↓ constraints
public harness evidence → Index S1 → canonical evidence-backed corpus
                    │
                    ├────────────→ Awesome S1 → curated public view
                    │
                    └────────────→ Skills S1 maintains reusable assessment execution capability
```

The three S1 domains contribute different durable outputs to the same public VSM Harness knowledge ecosystem. They may each contain multiple tasks, tools, helper agents, or subprocesses; those are not additional S1 units merely because they are separate processes.

## Local variety and residual variety

The default regulation rule is:

> absorb variety at the lowest operational domain that has the requisite information and delegated authority; escalate only residual variety that cannot be safely closed there.

Examples of local variety include:

- Index: discovery, deduplication, evidence reconstruction, assessment/reassessment, generated-view drift, provenance repair;
- Skills: procedure implementation, test/validator repair, selected-contract synchronization, reusable tooling maintenance;
- Awesome: representative curation, canonical-link consistency, presentation repair, downstream editorial maintenance.

The metasystem must not duplicate those ordinary local decisions merely to centralize control. Later VSM functions are introduced only for residual variety that cannot be safely absorbed by the relevant S1 domain, such as concrete inter-S1 interference, whole-system current regulation, complementary audit, external/future adaptation, or identity/ultimate-policy closure.

This preserves redundancy of potential command in the practical sense used here: the decision should remain with the operational domain that has the relevant local information and authority unless the disturbance genuinely exceeds that boundary.

## Repository participation

The five current public repositories remain in the broader organizational scope, but they participate in different planes:

| Repository | Current role in this system-in-focus |
| --- | --- |
| `opensiro/vsm-harness-profile` | Normative semantic authority consumed by the organization; outside the operational S1 plane. |
| `opensiro/vsm-harness-skills` | Operational S1 domain for reusable VSM Harness assessment procedure/skills/tooling, subject to the boundary above. |
| `opensiro/vsm-harness-index` | Operational S1 domain for the canonical evidence-backed corpus and derived deterministic views. |
| `opensiro/awesome-vsm-harness` | Operational S1 domain for curated representative downstream views. |
| `opensiro/vsm-oss-organization` | Metasystem/control-plane construction and organizational evidence; outside the operational S1 plane. |

Repository membership and functional participation remain distinct. An in-scope repository may contain work whose decisive right belongs outside the local S1 boundary.

## Viability criterion

For this organization, viability means that the three operational domains can continue producing their durable outcomes while relevant local variety is absorbed locally and residual variety is escalated to an appropriate function rather than silently centralized or ignored.

Relevant disturbances include:

- new harnesses and upstream repository changes;
- stale, missing, or contradictory evidence;
- assessment corrections and reassessments;
- Profile or Methodology contract changes that operational domains must consume;
- generated-view or provenance drift;
- duplicate discovery/intake;
- curation drift and community corrections;
- concrete interference between operational domains;
- changing external harness ecosystems.

Later OSM/VSM functions are introduced only when observed residual variety cannot be absorbed by the existing operational domains. Normative VSM definitions remain owned by `opensiro/vsm-harness-profile`.