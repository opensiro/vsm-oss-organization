# Viable-system identity

This repository organizes one bounded public viable system: the **OpenSiro VSM Harness OSS organization**.

Its purpose is to maintain for the open-source community a public, current, evidence-backed representation of the organizational structure of AI-agent harnesses through the Viable System Model.

A compact statement of the primary transformation is:

```text
public harness ecosystem evidence
        ↓
VSM semantics + assessment methodology
        ↓
evidence-backed assessments
        ↓
normalized comparative knowledge
        ↓
curated public views for the OSS community
```

The system is viable when it can continue this transformation while upstream harnesses, evidence, methodology, the assessed corpus, and community contributions change.

## Repository participation

The current in-scope repositories participate in that transformation in different ways:

| Repository | Organizational contribution |
| --- | --- |
| `opensiro/vsm-harness-profile` | Normative VSM semantic coordinate system used by this ecosystem. |
| `opensiro/vsm-harness-skills` | Reusable skills/tooling repository. Only the procedures and skills that participate in producing or maintaining VSM Harness knowledge are inside this viable system's operational boundary. The repository may also contain general-purpose skills for other systems; those are not governed by this control plane merely because they share the repository. |
| `opensiro/vsm-harness-index` | Evidence-backed harness corpus, reassessment history, provenance, signatures, and deterministic comparative views. |
| `opensiro/awesome-vsm-harness` | Curated representative downstream view for the community. |
| `opensiro/vsm-oss-organization` | Organizational/control plane for contribution work that maintains the transformation above. |

Repository membership and functional participation are therefore distinct. An in-scope repository may contain artifacts whose purpose belongs to another system. This control plane governs only the work that contributes to the declared VSM Harness OSS transformation.

## Operational work domain

The organization must be able to absorb or explicitly escalate work needed to maintain this transformation. Current work classes include:

```text
discover harnesses
        ↓
collect and pin primary evidence
        ↓
assess under the released methodology
        ↓
admit / correct / reassess corpus entries
        ↓
regenerate and validate comparative views
        ↓
curate representative public views
        ↓
maintain semantic/methodology contracts when evidence exposes a defect
        ↓
maintain releases, provenance, compatibility, and contributor surfaces
```

This is a work-domain description, not a VSM mapping. Do not infer S1/S2/S3/S3*/S4/S5 merely from stages in this lifecycle.

## Viability criterion

For this organization, viability means preserving public VSM Harness knowledge as **current, evidence-backed, internally coherent, and reconstructable** despite disturbances such as:

- new harnesses appearing;
- upstream repositories changing;
- evidence becoming stale or contradictory;
- assessment corrections or reassessments;
- Profile or Methodology releases;
- generated-view drift;
- provenance or reference breakage;
- duplicate discovery/intake;
- community corrections;
- concurrent contribution conflicts;
- changing external harness ecosystems.

Later OSM functions are introduced only when such observed variety cannot be absorbed by the existing organization. This file does not redefine VSM semantics; normative function definitions remain in `opensiro/vsm-harness-profile`.