# OpenSiro OSS Control Plane

This document is the operational control plane for the **public OpenSiro OSS group** governed by this repository. It records authority boundaries, compatibility gates, and the current hand-off points between repositories. It is **not** a control plane for all OpenSiro activity, and it is **not** a second source of VSM semantics or assessment data.

## Scope boundary

The canonical repository scope is defined in [README.md](README.md). At present this control plane covers public OSS contribution work across:

- `opensiro/vsm-harness-profile`
- `opensiro/vsm-harness-skills`
- `opensiro/vsm-harness-index`
- `opensiro/awesome-vsm-harness`
- `opensiro/terminal-bench-vsm`
- `opensiro/arctic-0`
- `opensiro/opensiro.com`
- `opensiro/vsm-oss-organization`

It does not govern private OpenSiro repositories, private R&D context, contributor-local runtimes/credentials/budgets, or unrelated projects merely because they share an owner or name. Third-party repositories may appear as environment or evidence but are not governed by this control plane.

Scope membership does not collapse repository responsibilities. In particular, ARCTIC remains a separate research track, the website remains a presentation layer, the Profile remains the normative VSM source, and the Index remains the evidence corpus.

## Authority chain

```text
VSM Harness Profile
        ↓ normative semantics
VSM Harness Methodology
        ↓ assessment / autonomy / synthesis procedure
VSM Harness Index @ exact Git revision
        ↓ evidence corpus + generated views
curated / presentation consumers

VSM OSS Organization
        ↳ local OSM operationalization of the released contract
```

Source-of-truth rules:

- `opensiro/vsm-harness-profile` owns S1, S2, S3, S3*, S4, S5, recursion, variety, escalation, ownership/enforcement, and closure semantics.
- `opensiro/vsm-harness-skills` owns the Methodology used to apply the Profile, including `A/C/P/—/?`, evidence procedure, synthesis, and deterministic ranking projection rules.
- `opensiro/vsm-harness-index` owns the evidence-backed corpus. The exact Index Git revision identifies one corpus/output state.
- `opensiro/opensiro.com` and other downstream views consume canonical upstream artifacts; they do not redefine them.
- this repository owns only the OpenSiro OSS contribution organization and its OSM construction sequence.

## Released contract vs frozen work

There are deliberately two compatible Methodology states in flight:

| Surface | Profile | Methodology | Meaning |
| --- | --- | --- | --- |
| active contract for new work | `0.2.0` | `0.2.2` | current released semantic/procedure pair |
| Index Reassessment R1 | `0.2.0` | `0.2.1` | frozen round contract; must not silently upgrade mid-round |

This is intentional, not drift. A frozen reassessment round is historical work under a declared contract. New assessments or operational design may use the active `0.2.2` Methodology.

Current released state:

- Profile `0.2.0` is tagged/released and immutable at its release identity.
- Methodology `0.2.1` and `0.2.2` are tagged/released; `0.2.2` is active for new work.
- the Index active contract is `Profile 0.2.0 / Methodology 0.2.2`.
- R1 remains frozen on `Profile 0.2.0 / Methodology 0.2.1` and the scope snapshot declared by `vsm-harness-index#47`.
- the website consumes the canonical Index and records the source revision during publication.

## Current change graph

```text
Profile #3  ── merged: v0.2.0 ownership / closure semantics
     ↓
Skills #2/#3/#5 ── merged: Methodology 0.2.0 → 0.2.1 → 0.2.2
     ↓
Index #44/#45/#46/#49 ── merged: provenance, R1, reduced active contract
     ↓
Index #50 ── merged: first R1 batch
     ↓
opensiro.com #2 ── merged: canonical Index → website synchronization

Profile #7 ── OPEN PROPOSAL: stricter explicit S2 evidence threshold

vsm-oss-organization #1 ── establishes the local OSM bootstrap on released
                           Profile 0.2.0 / Methodology 0.2.2
```

Historical note: Index #48 introduced a separate compatibility metadata/schema axis. Index #49 intentionally superseded that design with the smaller contract:

```text
Profile version + Methodology version + exact Index Git revision
```

Do not reintroduce an independent Index/TLDR/RANKINGS semantic version unless a future architectural need is demonstrated.

## Proposed semantics are not released semantics

`opensiro/vsm-harness-profile#7` proposes making the S2 evidence threshold mechanically explicit:

1. distinct S1 units;
2. concrete potential or observed interference/oscillation;
3. an attenuation/coordination path;
4. closure that changes subsequent S1 behaviour.

Profile `0.2.0` already requires a real coordination problem among S1 units and regulation of that interference. Issue #7 is therefore a compatible proposed clarification, but it is **not part of the released Profile until a Profile release incorporates it**.

This repository may use the four-part test as a deliberately stricter **local OSM construction gate**. When it does, it must label the test as local/proposed rather than claiming that Profile `0.2.0` literally contains that exact four-item rule.

## OSM state semantics

The roadmap vectors describe the intended ownership arrangement of this one reference organization. They are not a universal maturity ladder.

- `A`, `C`, and `P` are different ownership arrangements.
- `—` means no material first-party path at the declared boundary, not "immature".
- the local transition `S3=C → S3=A` means this design plans to close one existing constructor/control path with an autonomous owner; it does **not** establish a general ordering `C < A`.
- `S5=P` is a deliberate governance topology: ultimate identity/policy authority remains with the legitimate parent. It is not a lower stage awaiting `S5=A`.
- milestone ordering is an OSM construction sequence for this repository, not a claim that VSM functions have a universal installation order.

## Change routing

Use the smallest authority that actually owns the change:

| Change | Route | Downstream consequence |
| --- | --- | --- |
| meaning/boundary of S1–S5, recursion, variety, escalation, ownership or closure | Profile PR + released Profile version | Methodology compatibility review; new Index work may adopt the new contract; existing frozen rounds remain frozen |
| assessment/autonomy/synthesis procedure with unchanged VSM meaning | Methodology PR + release | update Index active contract after compatibility validation; do not rewrite old provenance |
| one harness evidence/classification/freshness event | Index PR | regenerate only affected deterministic corpus views; no Profile/Methodology release |
| cohort changes / signatures / rankings under unchanged Methodology | Index PR | exact Index Git revision identifies the new state |
| website rendering/presentation | presentation repository | consume upstream canonical data; no independent semantic authority |
| OpenSiro contributor role/control implementation | this repository | local OSM change; escalate upstream only if it reveals a reusable semantic/procedure defect |

## Merge gates for this repository

A local PR is ready when all applicable gates hold:

1. **Boundary:** system-in-focus and recursion level are explicit.
2. **Released contract:** any normative claim is supported by a released Profile/Methodology version, not only an open issue.
3. **Local proposal marking:** stricter experimental rules are labelled local/proposed until released upstream.
4. **Function first:** component names are not used as VSM evidence.
5. **Ownership:** decision right, owner, support/enforcement, and closure are separated.
6. **No maturity inference:** `A/C/P/—/?` is not treated as an ordinal score.
7. **Frozen work:** active downstream rounds such as R1 keep their declared version pair.
8. **Generated consumers:** presentation layers are not manually promoted into sources of truth.

## Current operator queue

### Ready / no semantic decision required

- continue R1 under its frozen `0.2.0 / 0.2.1` contract;
- use `0.2.0 / 0.2.2` for new work outside R1;
- keep website/index synchronization downstream-only;
- operate this repository at M0 and add later VSM functions only when their declared disturbance appears.

### Requires an explicit maintainer decision

1. **Profile #7 release policy** — decide whether the stricter four-part S2 witness should become a normative Profile patch now or remain a local/proposed clarification until more reassessment evidence accumulates.

No other current release/provenance contradiction requires a maintainer intervention.
