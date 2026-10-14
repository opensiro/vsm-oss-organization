# G1 E1 — source-backed public claim use and S3 admission screen

**Date:** 2026-10-14. **Governing issue:** [Organization #241](https://github.com/opensiro/vsm-oss-organization/issues/241). **Actual user selection:** investigate real public use of disputed Index claims; propose substantive G1 S3 options **only if** a real present whole-system right and case can be demonstrated. **Status: `E1_COMPLETE_PUBLIC_SOURCE_RELIANCE_CONFIRMED / S3_NOT_ADMITTED / NO_S3_TRANSACTION`.**

**Assessment provenance:** GPT-6 continuing author context, **not independent**. This is a bounded read-only audit of specified public source cuts and CI receipts, not a general claim that no user or consumer anywhere relies on these grades. It does not change canonical Index data, methodology, S5 boundaries, operational delegation, M1 grade or frozen evidence. See [exact source-linked E1 observation in #241](https://github.com/opensiro/vsm-oss-organization/issues/241#issuecomment-6176401547).

## 1. Frozen source boundaries and the actual consumer

| Surface | Inspected source | Relevance |
| --- | --- | --- |
| Organization | `main@cb9ffd4f166a6e77f1d7e74473d763910d190995` | Bounded S1 = Index/Skills/Awesome; G1 [`parent-assisted-g1.md`](../../contracts/s3/parent-assisted-g1.md), issued 2026-10-14 13:32:30 UTC; expiry 2026-11-13 12:00:00 UTC |
| Index | `main@e27af64449deeb6851340029596d93ed7fdc2474`, committed 2026-10-14 14:16:03Z | Canonical current assessments; Index-owned unresolved review issues |
| Skills | `main@7d0ef14ef4a4ef543bc5a960b3596035e67fa6cd` | Selected Procedure 0.3.7 / Profile 0.2.4, not the grader of individual Index claims |
| Awesome | `main@557094abd704d8a5a965f4f6162924b6f7744695` | Named Rum/SuisuiCode/bb are **not present** in reviewed README or ASSESSMENT_INDEXES surfaces |
| **Website** | `opensiro/opensiro.com@4181bdfb1c738e640d523b2c3ab20f8264b68dfc`, committed 2026-10-13 11:48:04Z | **Real downstream public-repository materialization**, but **outside the three declared Organization S1 domains** |

[Website source manifest](https://github.com/opensiro/opensiro.com/blob/4181bdfb1c738e640d523b2c3ab20f8264b68dfc/assets/harness-index/source-manifest.json) states canonical Index **source SHA `80fc101edd018461ab3b14a5b707af6977cda275`** (12 Oct 2026 18:05:50Z), website revision `f4b015a10838759f`, `included_assessments=499`. This is a **specific materialized stale-source gap** relative to current Index at the inspected date. Lag alone does not imply a changed disputed vector: the named present grades were **still** the same in Index at that cut.

## 2. Positive public-repository claim-use evidence

The generated website [`assets/harness-index/manifest.js`](https://github.com/opensiro/opensiro.com/blob/4181bdfb1c738e640d523b2c3ab20f8264b68dfc/assets/harness-index/manifest.js) has 499 entries, with public source assessment URLs and six-state vectors:

| Harness | Website generated fingerprint | Exact static row and assessment provenance | Canonical dispute state |
| --- | --- | --- | --- |
| **SuisuiCode** | **`A C A — A —`**; disputed `S4=A` | [row chunk `rows-88f20...`](https://github.com/opensiro/opensiro.com/blob/4181bdfb1c738e640d523b2c3ab20f8264b68dfc/assets/harness-index/rows-88f20bae383c5457.js) and [Index historical assessment `8a372087...`](https://github.com/opensiro/vsm-harness-index/blob/8a372087e865279eca3307563c52720f7ad8c4b2/assessments/suisuicode.md) | [Index #1387](https://github.com/opensiro/vsm-harness-index/issues/1387) OPEN; owner-grade correction `A→C` is a **review proposal**, not accepted. [Current Index assessment](https://github.com/opensiro/vsm-harness-index/blob/e27af64449deeb6851340029596d93ed7fdc2474/assessments/suisuicode.md) still `S4=A` |
| **Rum** | **`A — — C — —`**; disputed `S3*=C` | [row chunk `rows-2f47...`](https://github.com/opensiro/opensiro.com/blob/4181bdfb1c738e640d523b2c3ab20f8264b68dfc/assets/harness-index/rows-2f47ca2b57808042.js) and [Index historical assessment `0db4a2...`](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/rum.md) | [Index #1381](https://github.com/opensiro/vsm-harness-index/issues/1381) OPEN; original evidence/CI identity disputed, **not** an adjudicated `C` rejection. [Current Index assessment](https://github.com/opensiro/vsm-harness-index/blob/e27af64449deeb6851340029596d93ed7fdc2474/assessments/rum.md) still `S3*=C` |
| **bb** | **No `get-bb/bb` included website row** | [Current Index `assessments/bb.md`](https://github.com/opensiro/vsm-harness-index/blob/e27af64449deeb6851340029596d93ed7fdc2474/assessments/bb.md) says `status: proposed` | [Index #1382](https://github.com/opensiro/vsm-harness-index/issues/1382) OPEN; proposed `S3*=A` is **not canonically admitted** |

**Important distinction:** this proves that a publicly readable website repository materializes contested claims. It does **not** prove third-party consumer uptake, actual website visitor views, live web-server byte equivalence, or that the underlying grades were already judged wrong. External live `opensiro.com` HTTP retrieval was unavailable; do not silently equate GitHub Pages workflow success with served-content validation.

## 3. Concrete present website snapshot reliability failure

The website [sync workflow](https://github.com/opensiro/opensiro.com/blob/4181bdfb1c738e640d523b2c3ab20f8264b68dfc/.github/workflows/sync-vsm-index.yml) nominally reconciles current Index source, builds static rows, computes Organization historic metrics, then publishes only after checks. The historical finalizer is **after** the Index source materializer but **before** committing the generated snapshot.

Three scheduled sync runs, same exact blocker:

- [2026-10-14 04:53Z run #38513704981](https://github.com/opensiro/opensiro.com/actions/runs/38513704981) — FAILURE;
- [2026-10-14 10:12Z run #38547947498](https://github.com/opensiro/opensiro.com/actions/runs/38547947498) — FAILURE;
- [2026-10-14 15:09Z run #38586810449](https://github.com/opensiro/opensiro.com/actions/runs/38586810449) — FAILURE.

**Repeated logged error:** `metrics window finalizer error: owner renderer failed for opensiro/vsm-harness-index historical revision 81e10dfb73964e70454688d6a7852e1d9eeb4813`. The invoked code belongs to [Organization `scripts/finalize_public_metrics_windows.py`](https://github.com/opensiro/vsm-oss-organization/blob/cb9ffd4f166a6e77f1d7e74473d763910d190995/scripts/finalize_public_metrics_windows.py). It wraps an underlying owner renderer exception, **so the precise cause is not established from current logs**. Do not label this missing dispatch-token or incorrect assessment-grade behavior without further evidence.

[Static Pages run #38587925333](https://github.com/opensiro/opensiro.com/actions/runs/38587925333) at 15:16Z later completed SUCCESS on the **unchanged** website source head `4181bdf...`, showing that successful redeployment **does not** prove Index-sync catch-up or HTTP-served SHA verification.

**Source-owner handoff:** [opensiro.com #30](https://github.com/opensiro/opensiro.com/issues/30) opened for reproducing/repairing the website integration and verifying canonical Index→site→Pages→HTTP provenance. This is an information finding to the owning repository, **not a G1 S3 operational instruction**.

## 4. Real whole-system S3 admission test

| Requirement | E1 evidence | Verdict |
| --- | --- | --- |
| Actual downstream claim publication | Named site-generated Rum/SuisuiCode rows, historical Index links and static site snapshot | **SUPPORTED at public repository artifact level** |
| Actual current integrity/delivery issue | Stale Index source manifest and repeated failing sync | **SUPPORTED for website integration**, root cause unverified |
| Material whole-system **inside-and-now** S3 discretion **within the declared bounded S1 recursion** | Website is not a declared S1; accepted Index correction rights reside with Index S1; reviewed Awesome has no named claim; no new binding **Organization-level** authority or constraint on Index/Skills/Awesome shown | **INSUFFICIENT FOR S3 CASE** |
| Actual affected in-boundary S1 return not already owned locally | Index #1381/#1387 are owner-adjudication tasks; site #30 is an external website integration work item, not an in-boundary S1 return | **NOT ESTABLISHED** |
| Valid case-specific G1 holder action/closure | No admitted matter, no decision packet with lawful operative `SET_CONSTRAINT/REQUIRE_REPAIR/CONTINUE` choice and named S1 return | **NONE** |

**Bounded conclusion:** E1 found **actual downstream public-repository exposure and a concrete broken sync**, correcting the earlier narrower “no explicit downstream item” screen. But this does **not by itself establish a present S3 regulatory case** across the declared Organization. Website owner may fix its pipeline; Index owner may adjudicate claim merits. An S3 controller has **no right to rewrite Index grades or order external Website fixes**, nor does a site sync failure automatically become a Profile S3 whole-system decision. **Do not create an artificial `REQUESTED/DECIDED/APPLIED/CLOSED` transaction.**

## 5. Next routes (not S3 operative choices)

- **R1 — Owner-source repair, recommended:** follow [website #30](https://github.com/opensiro/opensiro.com/issues/30) through verified historical renderer repair, Index→website snapshot update and Pages/served-content provenance. This is website/Organization script technical work, **not** an S3 decision or blanket publication hold.
- **R2 — Existing Index semantic adjudication:** independently resolve [Rum #1381](https://github.com/opensiro/vsm-harness-index/issues/1381) and [SuisuiCode #1387](https://github.com/opensiro/vsm-harness-index/issues/1387) with properly owned source-first review, corrected canonical derived views where required. **No unilateral S3 grade edits**.
- **R3 — Separate S5 organizational-boundary choice (only if wanted):** if Website is to become a declared operational S1 or new cross-boundary policy subject, the legitimate S5 parent must explicitly amend the system-in-focus/mandate, not treat existing G1 grant as effective authority outside its declared recursion.

The routes can coexist; they are **not** mutually exclusive A/B/C S3 decisions. No material S3 case is being withheld from the human: **the evidence does not yet pass admission**. Any later admitted S3 case must use fresh pinned refs, a real organizational present constraint/authority, actionable human-selected G1 options, and a verifiable S1 return.

**Current states preserved:** G1 `ACTIVE_CONDITIONAL` to `2026-11-13T12:00:00Z`; [M1 #39](https://github.com/opensiro/vsm-oss-organization/issues/39) `OPEN/INSUFFICIENT`; target `C(P)` **not an evidenced assessment**; no actual operational parent-governed `P` closure; historical `S3=?` unchanged; no `TODO.md` scheduling or Index/Skills/Awesome modifications.
