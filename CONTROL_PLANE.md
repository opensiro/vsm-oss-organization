# OpenSiro OSS Control Plane

This document is the operational control plane for the bounded **OpenSiro VSM Harness OSS group** defined in `README.md`. It records authority boundaries, compatibility gates, and hand-off rules between in-scope public repositories. It is **not** a second source of VSM semantics, Methodology rules, or Index assessment data.

The in-scope repository set is maintained explicitly in `README.md`. Repository membership in the `opensiro` organization does not automatically place a project under this control plane. Contributor-local runtimes, schedulers, credentials, budgets, and sandboxes also remain outside this repository's authority.

Contributors who want a minimal human-parent interface before the full M2 implementation may use [`prompts/parent-control-plane.md`](prompts/parent-control-plane.md). That prompt is a demo interface pattern, not evidence that `S5=P` has already been achieved.

## Authority chain

```text
VSM Harness Profile
        ↓ normative semantics + release-impact facade
VSM Harness Methodology
        ↓ assessment / autonomy / synthesis procedure
VSM Harness Index
        ↓ evidence corpus + active assessment contract + generated views
Awesome VSM Harness

VSM OSS Organization
        ↳ local OSM operationalization of a selected upstream contract
```

Source-of-truth rules:

- `opensiro/vsm-harness-profile` owns S1, S2, S3, S3*, S4, S5, recursion, variety, escalation, ownership/enforcement, closure semantics, and Profile release-impact declarations.
- `opensiro/vsm-harness-skills` owns the Methodology used to apply the Profile, including `A/C/P/—/?`, evidence procedure, synthesis, and deterministic ranking projection rules.
- `opensiro/vsm-harness-index` owns the evidence-backed corpus and its active assessment contract. The exact Index Git revision identifies one corpus/output state.
- `opensiro/awesome-vsm-harness` owns its curated representative downstream view; it does not redefine Profile or Index facts.
- this repository owns only the bounded VSM Harness OSS contribution organization, its OSM construction sequence, and which upstream contract it elects to consume.
- `opensiro/terminal-bench-vsm`, `opensiro/arctic-0`, and `opensiro/opensiro.com` are outside this organizational scope even when they consume, demonstrate, experiment with, or present related artifacts.

## Upstream contract selection

[`UPSTREAM_CONTRACT.json`](UPSTREAM_CONTRACT.json) is the **only local machine-readable selection surface** for the upstream Profile, Methodology, and Index contract inputs used by this organization.

It records, for each upstream source:

- repository;
- source kind (`release`, `commit`, or `branch`);
- ref;
- relevant version/contract path.

The manifest selects an upstream state; it does not copy upstream semantics. Documentation in this repository should refer to the manifest instead of maintaining independent current-version pairs.

The selected Profile is consumed as a released semantic boundary. The selected Methodology may be pinned to an exact accepted commit when its current repository version is newer than the latest published GitHub Release; the manifest must represent that source status truthfully rather than pretending a release exists. The Index active contract is read from its canonical `data/active-contract.psv` surface.

## Profile compatibility gate

An exact Profile version attached to an assessment, trial, or other artifact is immutable **provenance**. A later Profile version is a separate compatibility question.

Organization validation applies the Profile's own downstream facade:

```text
artifact / Index Profile basis
        ↓
Profile RELEASE_IMPACT.json transition chain
        ↓
Organization-selected Profile
```

A silent Organization upgrade is allowed only when every intervening Profile transition is:

```text
compatibility: compatible
assessment_impact: none
```

This means an Index assessment produced under an older Profile can remain usable without rewriting its stored Profile provenance when the Profile itself declares the later transition no-impact.

If any intervening transition is `targeted`, `all`, or `breaking`, or if a complete transition path cannot be reconstructed, the validator must reject silent adoption. The required response is an explicit compatibility/reassessment decision at the authority that owns the affected artifact or procedure.

The Organization never infers compatibility from SemVer strings alone and never treats a newer Profile version as an automatic corpus-wide reassessment trigger.

## Cross-repository completion oracle

Repository-local checks remain useful, but they are not sufficient for upstream-contract correctness. CI therefore checks the selected upstream repositories directly.

The deterministic contract oracle verifies:

1. the local upstream-selection manifest is well formed;
2. the selected Profile ref exposes the declared `VERSION`, consumer contract, and release-impact history;
3. the selected Profile release is present in that release-impact history;
4. the selected Methodology ref exposes the declared Methodology version;
5. the Index active Methodology equals the Methodology selected by Organization;
6. if the Index Profile basis differs from Organization's selected Profile, the Profile release-impact chain proves a compatible/no-impact path;
7. repository-local scope, roadmap vectors, links, and source-of-truth ownership surfaces remain internally consistent.

These checks establish contract consistency only. They do **not** establish semantic correctness, function mapping, decision ownership, or `S1=A`.

## Frozen work and provenance

A frozen assessment/reassessment round or historical trial keeps the contract declared when that work began. Advancing the Organization upstream selection does not mutate historical provenance and does not silently upgrade work already frozen under another pair.

The distinction is:

```text
historical artifact
→ exact producing Profile / Methodology provenance

current Organization operation
→ selected upstream contract in UPSTREAM_CONTRACT.json

compatibility between them
→ derived from authoritative upstream compatibility rules
```

When a frozen workstream explicitly adopts a successor contract, that migration must be recorded by the workstream that owns it.

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
| meaning/boundary of S1–S5, recursion, variety, escalation, ownership or closure | Profile PR + accepted Profile release | consume Profile-declared impact; review Methodology/Index only to the declared scope |
| Profile release with `assessment_impact: none` | Profile release | Organization may advance its semantic boundary after compatibility validation; do not rewrite historical assessment provenance |
| Profile release with targeted/breaking impact | Profile + affected downstream owner | explicit scoped compatibility/reassessment decision; never infer corpus-wide work from version number alone |
| assessment/autonomy/synthesis procedure with unchanged VSM meaning | Methodology change | update Organization/Index contract selection after compatibility validation; do not rewrite old provenance |
| one harness evidence/classification/freshness event | Index PR | regenerate only affected deterministic corpus views; no Profile/Methodology release |
| cohort changes / signatures / rankings under unchanged Methodology | Index PR | exact Index Git revision identifies the new state |
| representative curation under unchanged canonical facts | Awesome VSM Harness PR | consume canonical upstream facts; no independent semantic authority |
| OpenSiro contributor role/control implementation | this repository | local OSM change; escalate upstream only if it reveals a reusable semantic/procedure defect |
| out-of-scope experiment/presentation work | its own repository | may consume in-scope artifacts but is not routed or governed here |

## Merge gates for this repository

A local PR is ready when all applicable gates hold:

1. **Boundary:** system-in-focus and recursion level are explicit.
2. **Upstream contract:** normative claims resolve through the selected upstream Profile/Methodology contract, not an open semantic proposal.
3. **Compatibility:** a newer Profile is accepted only through the Profile release-impact facade; insufficient or non-zero impact is escalated rather than silently adopted.
4. **Local proposal marking:** stricter experimental rules are labelled local/proposed until accepted upstream.
5. **Function first:** component names are not used as VSM evidence.
6. **Ownership:** decision right, owner, support/enforcement, and closure are separated.
7. **No maturity inference:** `A/C/P/—/?` is not treated as an ordinal score.
8. **Frozen work:** historical/frozen work keeps its declared version pair until its owning workstream explicitly migrates it.
9. **Generated consumers:** presentation layers are not manually promoted into sources of truth.
10. **Completion oracle:** repository-local and applicable upstream-contract checks pass without treating those checks as proof of semantic correctness or autonomy.

## Current operator boundary

At M1, ordinary Organization work uses the selected upstream contract and its deterministic compatibility gate. Task admission/recovery, completion evidence, complementary S3* audit, and S3 control-return remain separate organizational concerns.

A maintainer decision is required when:

- a Profile transition is not provably compatible/no-impact for the intended use;
- Methodology changes alter the procedure this organization relies on;
- a frozen workstream needs an explicit successor contract;
- organizational scope, identity, or ultimate-policy authority changes;
- an OSM milestone gate requires a new organizational function rather than ordinary S1 repair.
