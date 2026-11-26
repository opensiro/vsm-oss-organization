# VSM OSS reference Roadmap — S3=C -> S3=A

## Identity and pins
- Mode: LOCAL_UNREVIEWED
- Case ID: s3-d1a-autonomy-20261126
- Receipt contract: organization-local-roadmap
- Persistence: PREPARED on proposal branch; PERSISTED_LOCAL only on verified Organization main (Git readback is authoritative).
- Source worktree: clean pinned Git checkout at observation
- Local skill method: [OpenSiro Local v0.1.0](https://github.com/opensiro/vsm-harness-skills/blob/e83aba26f4be61c0a441ec269e7d4a26f9ad4366/skills/opensiro-local/SKILL.md), [generic experimental A/P research semantics](https://github.com/opensiro/upstream/blob/6281adbff6ba8303f9b17db55c7166e02ac21bf6/docs/EXPERIMENTAL_ROADMAP_TARGETS.md) only; no Upstream receipt or public gate used.
- Implementation: NOT_STARTED
- Original repository: opensiro/vsm-oss-organization
- Original HEAD: e7ad05495be60f1cfc122397b2809114306d0ec8
- Observed at: 2026-11-26
- Local assessment source: https://github.com/opensiro/vsm-oss-organization/issues/346
- Local assessment artifact: [exact preliminary baseline](../../assessments/2026-11-26-organization-346-preliminary.md)
- Baseline qualification: source-pinned preliminary local mapping, not a standalone canonical methodology artifact or accepted Index assessment; re-use for hypothesis only. Broader current S1/S2/S4 coverage not independently established.
- Local assessment SHA-256: 7cd13430cd68084762504cb3e86021e1ec3fd1fb2702994e956a3d7533424eb6
- Local assessed ref: e7ad05495be60f1cfc122397b2809114306d0ec8
- Local assessed at: 2026-11-26
- Profile ref: https://github.com/opensiro/vsm-harness-profile/blob/d5f2f8027b37eea3257192b8d0a5c9056c0c2837/PROFILE.md
- Methodology ref: https://github.com/opensiro/vsm-harness-skills/blob/e83aba26f4be61c0a441ec269e7d4a26f9ad4366/skills/assess-vsm-harness/SKILL.md
- System in focus: bounded public OpenSiro VSM OSS organization, four S1 domains; no private or external maintainer authority.
- Local VSM vector: S1=A · S2=— · S3=C · S3*=C · S4=— · S5=P
- Repository-wide source map: [Organization](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/docs/ORGANIZATION.md), [source routing](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/docs/ECOSYSTEM.md), [S1 coverage](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/records/s1/autonomy-coverage.md), [S3 control](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s3/current-control.md), [S3* audit](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s3star/audit.md), [S5 authority](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s5/parent-authority.md), [operating modes](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/modes/s3-autonomous/RUN.md), [milestones](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/docs/ROADMAP.md), [contributor policy](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/CONTRIBUTING.md). Source tree inspected, scripts/runtime/test entry points and supported modes surveyed; no independent re-assessment or fresh complete domain audit. This is continuity work from the earlier local draft, not an independent Track B replication. Local source #346 preliminary. Classification methodology 0.3.9 differs from current operating selection 0.3.8 in [UPSTREAM_CONTRACT](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/UPSTREAM_CONTRACT.json). No silent change.

## Rights and authority
- Target family: A
- Target transition: S3=C -> S3=A
- Current selected function state: C
- Mode preservation: PRESERVE
- Mode rationale: Retain constructor and separately governed G1 human path; the existing source explicitly does not establish a closed P mode for S3, so do not claim A(P). If later independent evidence proves it, reconsider notation without silently removing it.
- Prospective authority: Prospective only: legitimate S5 holder personally issues a finite, revocable D1-A grant to a separately identified agent via the existing two-phase route (https://github.com/opensiro/vsm-oss-organization/issues/5); no current grant.
- Cross-function authority compatibility: Preserve S5=P, local S1 authority, G1 human path and S3* independence; D1-A stays within its two standing commitments and three-domain delivery scope. Fourth-domain Upstream is visible for boundary checks, not a new authorized recipient (https://github.com/opensiro/vsm-oss-organization/issues/274).
- License: [Apache-2.0](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/LICENSE); internal self-study only; no fork, product mutation or grant. Applicable separate Organization parent authority and external consent remain binding.

## Existing work / overlap
[M3 #5](https://github.com/opensiro/vsm-oss-organization/issues/5) OPEN; implementation PRs 260–269 merged per M3 source; [runtime entry](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/modes/s3-autonomous/runtime_entry.py), [pending grant](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s3/autonomous-d1a.json), [activation and delivery](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/modes/s3-autonomous/GITHUB_D1A_ACTIVATION_AND_DELIVERY.md) shipped. [Human G1](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s3/parent-assisted-g1.md) distinct, not agent grant. [M4 #6](https://github.com/opensiro/vsm-oss-organization/issues/6) and [M5 #7](https://github.com/opensiro/vsm-oss-organization/issues/7) open, #345 proposed/not effective; [fourth S1 #274](https://github.com/opensiro/vsm-oss-organization/issues/274) closed; #346 local S4 C proposal open, not implementation.

## Function ownership
- S1 disposition: Historical A; [S1 coverage](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/records/s1/autonomy-coverage.md): supported local actor modes; strongest evidence in original three domains; Upstream witness is not regrade. NO_TARGET — historical A; four-domain ownership coverage remains provisional.
- S2 disposition: Historical —; [M4](https://github.com/opensiro/vsm-oss-organization/issues/6), [Organization](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/docs/ORGANIZATION.md): local checks and coordination instruments are not an established autonomous inter-S1 interference loop. DEFER — need concrete interference and return; M4 blocked on M3.
- S3 disposition: Historical C; [Standing commitments](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s3/standing-current-commitments.md), [D1-A runtime](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/modes/s3-autonomous/runtime_entry.py), [grant](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s3/autonomous-d1a.json): constructor and shipped integration, no operative autonomous grant. P0 — current-control mode has precise existing decision and missing activation/qualification links.
- S3* disposition: Historical C; [Audit constructor](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s3star/audit.md) and [audit queue](https://github.com/opensiro/vsm-oss-organization/issues/188): claim-relative complementary evidence, judgment and finding route; independent autonomous ownership not established. DEFER — preserve independent audit; larger missing independent judgment/closure construction than D1-A.
- S4 disposition: Historical —; [M5](https://github.com/opensiro/vsm-oss-organization/issues/7), [S4 local C proposal](https://github.com/opensiro/vsm-oss-organization/issues/346): external research without established adaptive decision/return closure. DEFER — M5 after M4; proposed C is not shipped.
- S5 disposition: Historical P; [Parent authority](https://github.com/opensiro/vsm-oss-organization/blob/e7ad05495be60f1cfc122397b2809114306d0ec8/contracts/s5/parent-authority.md), [fourth-domain return](https://github.com/opensiro/vsm-oss-organization/issues/274), [pending public-issue decision](https://github.com/opensiro/vsm-oss-organization/issues/345): legitimate human owner remains ultimate authority. NO_TARGET — preserve legitimate reserved P; no concrete bounded legitimate A construction identified; human P is intentional.

## Capability priority
- Priority rationale: M3 is the next legitimate milestone, existing current shared-commitment C path and shipped model/delivery/reconciliation minimize missing construction. M4 and M5 are downstream under current governance. S3* has a separate C witness and requires additional independent audit-owner/closure construction; S5 retains parent; S1 historical A does not require regrade.
- P0: Complete standard D1-A current-control mode for exact S3=C -> S3=A.
- P1 dependencies: First-party trusted S5 authorship verification and source-backed nonlocal case qualification; real finite grant, concrete runtime identity, independently sourced S1 return; fourth-domain visibility without unauthorized delivery.
- P2 optional: NONE.
- Scenario basis: HYPOTHETICAL

## Implementation options
- Proposed target construction: Reuse shipped model/decision/transport/reconciliation; complete first-party authentication and current-case qualification, preserve the separately governed human G1 path without claiming P closure and actual S1 feedback. Compatible host/configuration can supply credentials and identity, not the missing decisive actor or closure. No new decision class. Source-specific design detailed in AI contract.
- Target sufficiency falsifier: Human chooses decisive class, a developer still must compose the decisive actor/authority/closure, unsupported authority passes, or delivery cannot return real subsequent S1 effect.
- Proposed validation: Native positive qualified case plus negative missing/revoked authority, local S1/S2/S5 falsifiers, stale evidence, wrong recipient and absent feedback. Future python3 -m unittest discover -s tests -p 'test_s3*.py'; independent real source review. No staged live incident for grade.
- Validation state: NOT_RUN

## Specification and domain alternatives
No semantic changes, no fork, no transfer of ultimate S5 ownership. Retain G1 as native alternative. Align review with existing M3 #5 instead of duplicating a roadmap Issue.

## Cost experiment
- Cost status: NOT_MEASURED
Matched human G1 versus standard D1-A on the same eligible case, including human decision burden, trust setup, admission verification, review and maintenance. No measured improvement.

## Delivery and publication
- Result: PLAN_ONLY
- Proposal-stage decision: GO
- Research disposition: NEEDS_EVIDENCE
- Proposal falsifier: Equivalent active standard S3=A already exists or proposed chain cannot attain legitimate agent ownership/return; no-go for actual activation until effective S5 grant and qualified case.
- External publication: NONE
- Owning work item: [M3 #5](https://github.com/opensiro/vsm-oss-organization/issues/5)
- Next action: Local review only under [Organization-local skill](../../../skills/vsm-oss-local/SKILL.md); LOCAL_UNREVIEWED / PLAN_ONLY / NO_EXTERNAL_PUBLICATION. No implementation or authority grant.

## Parallel contribution-on-top review
- Evaluation object: bounded current control of the two standing cross-S1 commitments, same source and case in both tracks.
- Existing-work overlap: [M3](https://github.com/opensiro/vsm-oss-organization/issues/5), existing model and GitHub transport/reconciler; no duplicate regulator.
- Our on-top contribution: first-party trust verification and source-backed qualification plus standard-mode integration with effective finite S5 grant and independent S1 effect.
- Incremental benefit: HYPOTHETICAL reduction in repeated human current-control decisions while preserving ultimate authority; NOT_MEASURED.
- Decision scope: GO for prospective bounded design, NEEDS_EVIDENCE for its actual realization. No source semantic certification or external publication.
