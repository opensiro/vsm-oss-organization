# OpenSiro VSM OSS — experimental S3 autonomous current control

**PLAN_ONLY · LOCAL_UNREVIEWED · EXPERIMENTAL A · PLAN_ONLY — NO EXTERNAL PUBLICATION**

**One-sentence proposal:** Complete the existing M3 D1-A mode so a genuinely delegated autonomous S3 actor can decide whether to continue or require repair of an existing shared current commitment and verify the owning S1 return.
**Local decision receipt:** [roadmap.md](roadmap.md) — Organization-owned local case, sole decision source.
**Technical companion:** [constructor-sufficiency.md](constructor-sufficiency.md)
**Case:** s3-d1a-autonomy-20261126; PREPARED — Organization-owned review artifact.

## 1. Purpose and local VSM assessment

The VSM-informed construction and cost hypotheses are unproven; adoption belongs to the Organization's legitimate governance.

**LOCAL REFERENCE ASSESSMENT** — S1=A · S2=— · S3=C · S3*=C · S4=— · S5=P. Preliminary non-Index baseline in [Organization #346](https://github.com/opensiro/vsm-oss-organization/issues/346), observed 2026-11-26; exact text retained in [exact preliminary baseline](../../assessments/2026-11-26-organization-346-preliminary.md). Organization source e7ad05495be60f1cfc122397b2809114306d0ec8. [Profile 0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/d5f2f8027b37eea3257192b8d0a5c9056c0c2837/PROFILE.md); [Methodology 0.3.9](https://github.com/opensiro/vsm-harness-skills/blob/e83aba26f4be61c0a441ec269e7d4a26f9ad4366/skills/assess-vsm-harness/SKILL.md) and [ownership rules](https://github.com/opensiro/vsm-harness-skills/blob/e83aba26f4be61c0a441ec269e7d4a26f9ad4366/skills/assess-vsm-harness/references/autonomy-states.md). This is a preliminary source-pinned local mapping for a construction hypothesis, not a standalone canonical assessment; broader current S1/S2/S4 coverage is not independently established. The actual [Organization operating selection](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/UPSTREAM_CONTRACT.json) still pins Methodology 0.3.8; this experiment does not change it.
**Repository-wide audit:** [Bounded four-domain recursion](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/docs/ORGANIZATION.md), [ownership coverage](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/records/s1/autonomy-coverage.md), [milestones](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/docs/ROADMAP.md), [runtime and grant](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/modes/s3-autonomous/RUN.md). Historical local grades remain preliminary.

| Function / plain-language role | Historical local state | Current owner / closure and evidence | Disposition and priority |
| --- | --- | --- | --- |
| **S1 · Operations** | A | [S1 coverage](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/records/s1/autonomy-coverage.md): supported local actor modes; strongest evidence in original three domains; Upstream witness is not regrade. | NO_TARGET — historical A; four-domain ownership coverage remains provisional. |
| **S2 · Coordination** | — | [M4](https://github.com/opensiro/vsm-oss-organization/issues/6), [Organization](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/docs/ORGANIZATION.md): local checks and coordination instruments are not an established autonomous inter-S1 interference loop. | DEFER — need concrete interference and return; M4 blocked on M3. |
| **S3 · Current management** | C | [Standing commitments](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s3/standing-current-commitments.md), [D1-A runtime](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/modes/s3-autonomous/runtime_entry.py), [grant](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s3/autonomous-d1a.json): constructor and shipped integration, no operative autonomous grant. | P0 — current-control mode has precise existing decision and missing activation/qualification links. |
| **S3* · Complementary audit** | C | [Audit constructor](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s3star/audit.md) and [audit queue](https://github.com/opensiro/vsm-oss-organization/issues/188): claim-relative complementary evidence, judgment and finding route; independent autonomous ownership not established. | DEFER — preserve independent audit; larger missing independent judgment/closure construction than D1-A. |
| **S4 · Future adaptation** | — | [M5](https://github.com/opensiro/vsm-oss-organization/issues/7), [S4 local C proposal](https://github.com/opensiro/vsm-oss-organization/issues/346): external research without established adaptive decision/return closure. | DEFER — M5 after M4; proposed C is not shipped. |
| **S5 · Identity and policy** | P | [Parent authority](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s5/parent-authority.md), [fourth-domain return](https://github.com/opensiro/vsm-oss-organization/issues/274), [pending public-issue decision](https://github.com/opensiro/vsm-oss-organization/issues/345): legitimate human owner remains ultimate authority. | NO_TARGET — preserve legitimate reserved P; no concrete bounded legitimate A construction identified; human P is intentional. |

A/C/P are ownership categories, not quality ranks. A(P)/C(P) are independently supported modes; P notation only applies to S3/S4/S5. — is bounded absence; ? is unresolved evidence.
**Priority rationale:** M3 is the next existing legitimate construction milestone and reuses the shipped S3 model/transport/feedback code. S2/S4 have later milestones, S3* needs a complete independent autonomous audit-owner path, S5 remains parent-governed, S1 is not an A-target on this historical baseline.
**Deliberate exclusions / methodology challenge:** The four-domain S1 coverage and S3 parent-mode closure are not independently regraded here; no broad autonomy claim from old three-domain evidence.

## 2. Selected construction hypothesis and operator outcome

**Target family:** A
**Target transition:** S3=C -> S3=A
**Current selected function state:** C
**Mode preservation:** PRESERVE
**Prospective authority:** Prospective only: legitimate S5 holder personally issues a finite, revocable D1-A grant to a separately identified agent via the existing two-phase route (https://github.com/opensiro/vsm-oss-organization/issues/5); no current grant.
**Cross-function authority compatibility:** Preserve S5=P, local S1 authority, G1 human path and S3* independence; D1-A stays within its two standing commitments and three-domain delivery scope. Fourth-domain Upstream is visible for boundary checks, not a new authorized recipient (https://github.com/opensiro/vsm-oss-organization/issues/274).
**Function-specific disturbance:** HYPOTHETICAL case of a material current incompatibility between two already binding S1 obligations, e.g. continued Index work under a selected Skills procedure while an affected Awesome publication would violate canonical continuity. Existing standing obligations are observed; no live incident is asserted. Routine S1 repair or S2 coordination alone does not qualify.
**Proposed target capability (P0):** The standard D1-A operating mode verifies current nonlocal case and effective S5 authorization, lets its model independently choose CONTINUE or REQUIRE_REPAIR, delivers the bounded instruction, and verifies later owning-S1 acknowledgement and effect. No developer-built decisive actor or closure callback remains.
**Best native operator alternative:** Existing human G1 holder qualifies and chooses a current-control decision, with the same S1 and return evidence. A routine compatibility discrepancy stays within S1.
**Expected user benefit:** HYPOTHETICAL — reduced repeated human choice over admitted bounded current-control cases, not transfer of ultimate authority.
**Architectural sufficiency argument:** Reuse the shipped model/decision/delivery/reconciliation; supply first-party trusted issuance verification and case qualification, independently sourced S1 feedback and a documented compatible host entry. Retain constructor and separately governed G1 human path; the existing source explicitly does not establish a closed P mode for S3, so do not claim A(P). If later independent evidence proves it, reconsider notation without silently removing it.

## 3. Existing native work versus missing construction

**Track A — native coverage:** [M3 #5](https://github.com/opensiro/vsm-oss-organization/issues/5), [runtime entry](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/modes/s3-autonomous/runtime_entry.py), [two-phase activation](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/modes/s3-autonomous/GITHUB_D1A_ACTIVATION_AND_DELIVERY.md), [standing commitments](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s3/standing-current-commitments.md). Current grant remains PENDING_S5_PUBLIC_ATTESTATION; live entry still needs trusted parent-authorship and nonlocal-case qualification.
**Track B — independent on-top target construction:** Implement the missing first-party standard host verification and qualification paths, then separately seek actual S5 issuance. Do not duplicate the regulator or bypass G1.
| Required target link | Existing coverage | Missing native integration |
| --- | --- | --- |
| Decision owner, information and authority | Shipped model owner and bounded choices; inactive grant | Authentic parent-authorship verifier; real separately identified grant; source-based nonlocal admission |
| Effect and feedback | Shipped GitHub S1 delivery and reconciler | Complete standard-mode wiring and actual independent owning-S1 return/effect evidence |

**Distinctness and falsifier:** If D1-A already has operative trusted source-backed authority and closed standard-mode reachability, the proposed missing delta is false; if either missing callback is still developer-composed or human selects the decisive choice, the A claim fails.

## 4. Priorities and minimum sufficient result

- **P0:** One complete legitimate D1-A S3=A mode over the existing shared standing commitments.
- **P1:** Parent-attestation trust source and finite grant; first-party nonlocal-case qualification and S1 feedback path; explicit fourth-domain boundary checks and negative tests.
- **P2:** NONE — do not widen decision classes, recipient domains, scheduler or S5 authority.

**Proposed target-sufficiency verdict:** PROPOSED_TARGET_SUFFICIENT, conditional on the complete legitimate chain; current A is NOT ESTABLISHED.

## 5. Proposed acceptance and stop gates

**Future positive test:** An actually admitted nonlocal current case supports two permissible choices, an authorized model chooses one, the named S1 acknowledges and later independently verifiable operation reflects that choice.
**Future negative test:** Missing/revoked/expired grant, wrong agent, source drift, local-only repair, S5 policy matter, unauthorized Upstream recipient, conflicting G1, missing S1 effect or absent model all fail closed; no false closure.
**Proposed falsifier:** A trusted verifier still has to be authored by the developer, a human preselects the class, or the real S1 effect cannot be returned in the standard mode.
**Validation state:** NOT_RUN — design only.

## 6. Independent paths

**Original-native contribution:** Continue [M3 #5](https://github.com/opensiro/vsm-oss-organization/issues/5), not a duplicate Issue. Reuse D1-A v1 and its two-phase grant protocol; separate Organization owner decision before any implementation/activation.
**Profile / Skills:** No semantic change proposed; cite the pinned methodology and distinguish the currently selected operational contract.
**Domain fork:** NONE — exact VSM OSS reference realization only.

## 7. Cost hypothesis

Matched task comparison with G1: number of legitimate repeated human choices, time, verification integration, authority administration, false-admission risks and maintenance. Cost status: NOT_MEASURED.

## 8. Decision / handoff

**Proposal-stage decision:** GO
**Research disposition:** NEEDS_EVIDENCE
**Decision reason / next permitted step:** Review the exact standard-mode missing links and verify the independent parent trust mechanism; no operative grant, test success or milestone completion is claimed.
**Agent/developer handoff:** [constructor-sufficiency.md](constructor-sufficiency.md) and [roadmap.md](roadmap.md).
**Rights and publication:** Apache-2.0 [license](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/LICENSE); no product implementation, authority grant, fork, external outreach or operational test. LOCAL_UNREVIEWED / PLAN_ONLY / NO_EXTERNAL_PUBLICATION.
**AI disclosure:** Prepared with AI assistance; no independent assessment, implementation, native test or external publication.
