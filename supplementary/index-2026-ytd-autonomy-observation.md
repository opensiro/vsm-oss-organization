# 2026 YTD harness-autonomy observation

**Status:** provisional empirical observation

This supplementary note records a corpus-level observation from the public OpenSiro VSM Harness Index. It is descriptive and non-normative. It does not redefine VSM semantics, alter any standalone harness assessment, or claim that the observed cohort is representative of all agent software.

## Source snapshot

- **Index repository:** `opensiro/vsm-harness-index`
- **Index revision:** `eebe516174b712a144b143da7afd7b636f6e070b`
- **Snapshot date:** 2026-09-21
- **Semantic contract:** VSM Harness Profile 0.2.3 / Methodology 0.3.5
- **Cohort:** canonical `status: included` harnesses whose GitHub repository was created in calendar year 2026
- **Cohort size:** 59 harnesses
- **Primary report:** [`vsm-harness-index` PR #243](https://github.com/opensiro/vsm-harness-index/pull/243)
- **Recurring temporal projection follow-up:** [`vsm-harness-index` issue #242](https://github.com/opensiro/vsm-harness-index/issues/242)

Repository creation time is only a temporal cohort selector. VSM states come from the standalone canonical assessments at the pinned Index revision.

## Observed distribution

| VSM function | Strict `A` | Strict `A` share | Base `A` (`A` + `A(P)`) | Base `A` share |
| --- | ---: | ---: | ---: | ---: |
| S1 | 59 / 59 | 100.0% | 59 / 59 | 100.0% |
| S2 | 15 / 59 | 25.4% | 15 / 59 | 25.4% |
| S3 | 14 / 59 | 23.7% | 20 / 59 | 33.9% |
| S3* | 18 / 59 | 30.5% | 18 / 59 | 30.5% |
| S4 | 5 / 59 | 8.5% | 6 / 59 | 10.2% |
| S5 | 1 / 59 | 1.7% | 1 / 59 | 1.7% |

`A(P)` is kept distinct in strict counts and collapsed to base `A` only where the existing Index base-state convention requires it. `C`, `C(P)`, `P`, `—`, and `?` are not treated as fractional autonomy and are not ordered as lower maturity states.

The same snapshot has:

- **Full-A:** 0 / 59 — 0.0%
- **5 / 6 base-agent-owned functions:** 2 / 59 — 3.4%
- **exactly 1 / 6 base-agent-owned functions:** 31 / 59 — 52.5%

Because S1 is base `A` for the entire admitted cohort, the last figure means that 31 of the 59 2026-created included harnesses have base-agent-owned autonomy only at S1 and not at S2, S3, S3*, S4, or S5.

## Descriptive interpretation

### 1. The cohort is strongly operation-first

The largest visible asymmetry is between S1 and the metasystem functions. Autonomous operation is universal inside this admitted cohort, while base-agent-owned closure falls to roughly one quarter or one third for S2/S3/S3*, about one tenth for S4, and about two percent for S5.

This supports a bounded description of the current corpus: many contemporary harnesses close an operational model/tool/task loop without closing the broader organizational functions around coordination, current control, independent audit, adaptation, and identity/ultimate policy at the same ownership level.

It does **not** show that all 2026 agent projects have autonomous S1. The Index admission boundary itself selects for a substantive first-party operational organization, so S1=100% is selection-sensitive.

### 2. Regulation and audit are materially more common than adaptation and identity closure

In this cohort, S2/S3/S3* base autonomy is observed in the 25–34% range, while S4 is 10.2% and S5 is 1.7%.

A useful research hypothesis is therefore that current harness engineering has progressed further in orchestration, regulation, supervision, and corrective challenge than in organization-level prospective adaptation or self-owned identity/ultimate-policy closure.

That is a hypothesis about mechanism prevalence, not a maturity ranking. Constructor and Parent-governed arrangements may be deliberate and appropriate for a system's boundary.

### 3. Parent-governed modes materially affect the S3 picture

Strict S3 autonomy is 23.7%, while base S3 autonomy is 33.9%. The difference is entirely due to `A(P)` cases: agent-owned S3 operation exists in the base mode, while a Parent retains decisive authority in a declared parent mode.

The much smaller S4 gap, 8.5% strict versus 10.2% base, suggests that parent-assisted composites currently contribute more visibly to current-control ownership than to adaptation ownership in this snapshot.

This is an empirical reason to preserve `A` and `A(P)` as different ownership arrangements rather than flatten them into one binary autonomous/not-autonomous label at the assessment layer.

### 4. Whole-organization base autonomy is rare in the snapshot

No 2026-created canonical harness at the pinned revision has base `A` on all six functions, and only two systems have base `A` on five of six functions.

The observation is more informative as a structural pattern than as a ranking: autonomous closure of one operational loop is common inside the admitted corpus, whereas closing nearly the whole VSM organization under agent ownership is uncommon.

### 5. S3* is currently more common than strict S3 or S2

Strict S3* appears in 30.5% of the cohort, compared with 23.7% strict S3 and 25.4% S2.

The snapshot alone cannot explain why. A testable hypothesis is that independent reviewer/verifier/corrective-challenge loops are easier to add as bounded first-party mechanisms than full inter-S1 disturbance attenuation or discretionary whole-system current control.

This should be tested against implementation evidence rather than inferred from component names such as `reviewer`, `verifier`, `manager`, or `coordinator`.

## Research implications

The snapshot suggests an empirical progression worth testing rather than assuming:

```text
autonomous operation
        ↓
coordination / current control / independent audit
        ↓
prospective adaptation
        ↓
identity / ultimate-policy closure
```

This diagram is a **research hypothesis about observed prevalence**, not a VSM maturity ladder and not a prescribed construction sequence.

A stronger temporal test would measure the same states over closed quarters. In particular, quarter-level projections could test whether later cohorts show:

- rising S2/S3/S3* autonomy while S4/S5 remain comparatively rare;
- rising S4 without corresponding S5 closure;
- increasing use of `A(P)` as systems become more operationally autonomous while preserving Parent authority;
- changes in the share of systems with 1/6, 4/6, 5/6, or 6/6 base-agent-owned functions.

If such patterns persist across closed periods, they would provide stronger evidence for describing how harness organizations are changing over time. A single YTD snapshot cannot establish a trend.

## Limitations and alternative explanations

1. **Admission selection.** The Index is an assessed harness corpus, not a random sample of all agent software. In particular, S1 is affected by the requirement for a substantive first-party operational boundary.
2. **2026 is incomplete.** The snapshot is from 2026-09-21; calendar 2026 and Q3 are still open.
3. **Repository creation date is a coarse temporal proxy.** It records when the repository was created, not when every relevant organizational mechanism was implemented.
4. **Assessment states are repository- and revision-relative.** Later upstream changes, reassessments, or same-ref corrections can change later snapshots without invalidating this pinned observation.
5. **Function prevalence is not causal evidence.** The snapshot does not establish that one VSM function causes another, that systems naturally mature through the observed frequency order, or that more autonomous functions produce better products.
6. **Ownership arrangements are categorical.** `A`, `C`, and `P` represent different decision-right configurations; they are not an ordinal score.

## Follow-up

The most useful next step is the deterministic year/quarter projection tracked in Index issue #242. Closed-quarter comparisons should reuse the same state-collapse rules and mark open periods explicitly rather than silently comparing a partial current period with complete historical periods.

Until then, this note should be cited only as a **2026 YTD corpus observation at the pinned Index revision**.