# OpenSiro OSS Control Plane

This document is the operational control plane for the bounded **OpenSiro VSM Harness OSS group** defined in `README.md`. It records authority boundaries, compatibility gates, and the current hand-off points between in-scope public repositories. It is **not** a control plane for every OpenSiro project, private work, or downstream consumer, and it is **not** a second source of VSM semantics or assessment data.

The in-scope repository set is maintained explicitly in `README.md`. Repository membership in the `opensiro` organization does not automatically place a project under this control plane. Contributor-local runtimes, schedulers, credentials, budgets, and sandboxes also remain outside this repository's authority.

Contributors who want a minimal human-parent interface before the full M2 implementation may use [`prompts/parent-control-plane.md`](prompts/parent-control-plane.md). That prompt is a demo interface pattern, not evidence that `S5=P` has already been achieved.

## Authority chain

```text
VSM Harness Profile
        ↓ normative semantics
VSM Harness Methodology
        ↓ assessment / autonomy / synthesis procedure
VSM Harness Index @ exact Git revision
        ↓ evidence corpus + generated views
Awesome VSM Harness

VSM OSS Organization
        ↳ local OSM operationalization of the released contract
```

Source-of-truth rules:

- `opensiro/vsm-harness-profile` owns S1, S2, S3, S3*, S4, S5, recursion, variety, escalation, ownership/enforcement, and closure semantics.
- `opensiro/vsm-harness-skills` owns the Methodology used to apply the Profile, including `A/C/P/—/?`, evidence procedure, synthesis, and deterministic ranking projection rules.
- `opensiro/vsm-harness-index` owns the evidence-backed corpus. The exact Index Git revision identifies one corpus/output state.
- `opensiro/awesome-vsm-harness` owns its curated representative downstream view; it does not redefine Profile or Index facts.
- this repository owns only the bounded VSM Harness OSS contribution organization and its OSM construction sequence.
- `opensiro/terminal-bench-vsm`, `opensiro/arctic-0`, and `opensiro/opensiro.com` are outside this organizational scope even when they consume, demonstrate, experiment with, or present related artifacts.

## Released contract vs frozen work

There are deliberately two compatible Methodology states in flight:

| Surface | Profile | Methodology | Meaning |
| --- | --- | --- | --- |
| active contract for new work | `0.2.1` | `0.2.3` | current released semantic/procedure pair |
| Index Reassessment R1 | `0.2.0` | `0.2.1` | frozen round contract; must not silently upgrade mid-round |

This is intentional, not drift. A frozen reassessment round is historical work under a declared contract. New assessments or operational design outside R1 use the active `0.2.1 / 0.2.3` pair.

Current released state:

- Profile `0.2.1` is tagged/released at normative commit `e1aaff7d2cd50d5d5ed9ab76c3606a6ef39d1976`; that tag target is treated as the immutable release identity.
- Methodology `0.2.3` is tagged/released at commit `30474da360b76edd1458ef51457fb2bb2323dcd1`; the bundled Profile records exact normative source revision `e1aaff7d2cd50d5d5ed9ab76c3606a6ef39d1976` plus the Profile blob.
- the Index active contract is `Profile 0.2.1 / Methodology 0.2.3` for new work.
- R1 remains frozen on `Profile 0.2.0 / Methodology 0.2.1` and the scope snapshot declared by `vsm-harness-index#47`.
- out-of-scope presentation consumers may consume canonical Index state, but their publication workflow is not governed here.

## Current change graph

```text
Profile #3  ── merged/released: v0.2.0 ownership / closure semantics
Profile #8  ── merged/released: v0.2.1 explicit S2 evidence witness
     ↓
Skills #8  ── merged: Methodology 0.2.3 S2 function-before-state rule
Skills #9/#11 ── merged: exact Profile source provenance + validation hardening
     ↓
Methodology v0.2.3 ── released at 30474da360b76edd1458ef51457fb2bb2323dcd1
     ↓
Index #52 ── merged: active contract → Profile 0.2.1 / Methodology 0.2.3
     ├── new work uses active contract
     └── R1 remains frozen on 0.2.0 / 0.2.1
             ↓
Index #53 ── OPEN: targeted R1 S2 same-ref re-review queue
```

Out-of-scope downstream repositories may have their own synchronization or presentation changes; those are context, not nodes governed by this control plane.

Historical note: Index #48 introduced a separate compatibility metadata/schema axis. Index #49 intentionally superseded that design with the smaller contract:

```text
Profile version + Methodology version + exact Index Git revision
```

Do not reintroduce an independent Index/TLDR/RANKINGS semantic version unless a future architectural need is demonstrated.

## Released S2 clarification vs frozen R1

Profile `0.2.1` makes the S2 evidence witness mechanically explicit. A positive S2 mapping identifies, at the declared recursion level:

1. distinct S1 operational units;
2. a **specific actual or structurally evidenced** interference, conflict, or oscillation arising from their interaction;
3. a coordination relation specifically capable of attenuating that disturbance;
4. feedback or closure by which the result changes subsequent S1 behaviour.

Generic mailboxes, routing, shared state, task sequencing, dependency fields, speaker selection, or delegation do not establish S2 merely because they could be used to build coordination.

Methodology `0.2.3` additionally makes the function-before-state boundary explicit for `S2=C`: the S2 function itself must already be established, and the first-party primitive must expose an S2-specific decision/feedback path. `C` does not mean generic framework expressiveness.

This clarification does **not** migrate R1. Frozen Profile `0.2.0` already requires a coordination problem and regulation of interference, and frozen Methodology `0.2.1` already excludes delegation/routing/sequencing/handoff alone and requires interference/oscillation regulation. Therefore weak historical S2 positives discovered in R1 are handled as same-ref corrections under `0.2.0 / 0.2.1`, as tracked by `vsm-harness-index#53`.

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
| representative curation under unchanged canonical facts | Awesome VSM Harness PR | consume canonical upstream facts; no independent semantic authority |
| OpenSiro contributor role/control implementation | this repository | local OSM change; escalate upstream only if it reveals a reusable semantic/procedure defect |
| out-of-scope experiment/presentation work | its own repository | may consume in-scope artifacts but is not routed or governed here |

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
- execute the targeted S2 re-review queue in `vsm-harness-index#53` as part of R1, using same-ref corrections where the frozen evidence contract was previously over-interpreted;
- use `0.2.1 / 0.2.3` for new work outside R1;
- operate this repository at M0 and add later VSM functions only when their declared disturbance appears.

### Requires an explicit maintainer decision

None at the current release/provenance boundary.

A new maintainer decision is required only when a future semantic proposal changes the released Profile/Methodology contract, a frozen downstream round needs an explicit successor, or the OSM implementation reaches a roadmap gate whose organizational disturbance must be demonstrated rather than assumed.
