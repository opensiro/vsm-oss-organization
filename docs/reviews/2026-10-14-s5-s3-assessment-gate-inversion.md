# Incident review — S5 authority inverted into an S3 assessment gate (2026-10-14)

**Status:** author-context operational postmortem and corrective design; **not** an independent review, retrospective autonomy reassessment, Stage-2 delegation, or authorization to merge another PR.

## Sources and verified sequence

At Organization `main@0455007b5139ce86e787014f8af3862c36c8691d`, the selected [Profile `v0.2.4`](https://github.com/opensiro/vsm-harness-profile/blob/v0.2.4/PROFILE.md) defines S3 as whole-system *inside-and-now* regulation and S5 as legitimate ultimate policy/identity. The selected [Skills Methodology `v0.3.7`](https://github.com/opensiro/vsm-harness-skills/blob/v0.3.7/skills/assess-vsm-harness/references/autonomy-states.md) uses `P` to **classify observed parent-governed closure**, not to allocate legal/governance rights. The Organization's [parent declaration](../../contracts/s5/parent-authority.md) already names `xLagerFeuer` as the legitimate S5 parent and reserves the delegation model to that owner. [S5-P-001](../../records/s5/2026-09-18-routing-scope-correction.md) is an existing bounded parent-governed witness; no new grade is inferred here.

Reconstructable causal chain:

1. [M1 #39](https://github.com/opensiro/vsm-oss-organization/issues/39) attempted a **source-first S3 constructor/function assessment** under M1 Option B; [2026-10-14 review](2026-10-14-s3-c-existing-constructor-qualification.md) legitimately returned `INSUFFICIENT` for *positive `S3=C` evidence*. It did **not** revoke S5 parent authority.
2. [#39 scope packet](https://github.com/opensiro/vsm-oss-organization/issues/39#issuecomment-6157935711) proposed a concrete claim-assurance envelope and A/B/C design-scope selection. Operator **A** authorized prospective design only; [PR #235](https://github.com/opensiro/vsm-oss-organization/pull/235) was created non-operative with no S3 actor.
3. [S5 owner request #236](https://github.com/opensiro/vsm-oss-organization/issues/236) separated *Stage 1 design adoption* from *Stage 2 actual delegation*. The authenticated owner [adopted Stage 1](https://github.com/opensiro/vsm-oss-organization/issues/236#issuecomment-6167388750) for exact PR head `f5436a8ddbbc362fc3f81d4fdfea3259280c9432`, but appointed nobody and activated nothing.
4. The [next assistant screen](https://github.com/opensiro/vsm-oss-organization/issues/236#issuecomment-6167572305) examined Rum, bb and SuisuiCode, saw no proven extra-Index current obligation, and labelled the candidate `NOT_ADMITTED_FOR_STAGE_2`. **The narrow evidence result may be valid for a specific *S3 exercise*; the process error was using it to veto *prospective S5 constitution/appointment*.** This was later acknowledged to be the wrong boundary. The screen also used evidence of cross-domain consumption as the practical bar, even though a genuine whole-system S3 decision may return to only one S1.
5. The authenticated owner [clarified reserved decision rights](https://github.com/opensiro/vsm-oss-organization/issues/236#issuecomment-6167754468): while S5 is operated in parent-governed `P` mode, the legitimate S5 holder retains key policy, organizational-function and delegation choices; an assessor provides **evidence**, not permission. The instruction explicitly does **not** appoint a holder or activate Stage 2.

## Root cause and contributing factors

**Primary root cause — type error / gate inversion:** the workflow conflated three distinct decision types:

| Decision type | Legitimate owner | Admission/evidence criterion | May block |
| --- | --- | --- | --- |
| **S5 governance**: should the bounded Organization constitute S3, choose mandate/recipient, set standing conditions or revoke it? | Declared legitimate S5 parent (`xLagerFeuer` under current declaration) | Explicit owner choice and bounded delegation-model authority. A real present case is **not required** to authorize a prospective role. | **Unapproved authority grant**, not design or owner's decision request |
| **S3 operational exercise**: should an effective S3 holder intervene in a specific current claim/commitment? | Named holder with **already effective** S3 rights | Real materially whole-system present-control variety, complete current view, exact right, affected S1 return | **That specific S3 intervention** if absent |
| **VSM evidence assessment**: is `S3=C` / `A` / parent mode positively supported? | Source-first assessor under Profile/Skills Methodology; canonical general corpus owned by Index | Pinned primary function/decision-path evidence at reviewed boundary | **Unsupported grade claim**, not S5's choice to constitute/delegate |

The `NOT_ADMITTED_FOR_STAGE_2` phrase silently crossed from the *operational exercise* row to the *parent's appointment* row. Stage-2 delegation may be prospective **with a condition on future cases**; the condition is checked on exercise, not necessarily to approve the standing authorization.

**Contributors:** (a) the specific claim-assurance design was mistaken for a universal prerequisite to introducing S3; (b) the #236 two-stage wording mixed holder appointment with per-case evidence and invited misrouting; (c) existing contracts separate governance/assessment implicitly but did not express the decisive **anti-veto rule** in the primary agent entrypoint; (d) repeated author-context review produced no independent adversarial challenge. These are bounded findings about this workflow, not claims that all other agents or assessment batches have the same defect.

## Corrective operating rule (prospective)

1. When the operator directs an organizational **mandate, appointment, activation, revocation or S3 domain-fit policy**, classify and route it to **S5 first**. Show the actual parent and scope, not a calculated autonomy grade. Never require `S3=C`, an observed S3 incident, cross-S1 harm or `REQUESTED` transaction *before allowing the legitimate parent to make a prospective choice*.
2. Ask the S5 parent to select precisely **what** is decided: `DESIGN_ONLY`, `STANDING_GRANT_WITH_CONDITIONS`, `IMMEDIATE_ACTIVATION`, `REVISE` or `REJECT`. **Do not silently escalate** a generic `continue`, select an actor, or interpret Stage 1 as Stage 2. Effective grants still need named recipient, scope, start, revocation and reporting.
3. Before an **S3 exercise**, independently verify the present whole-system need, that action is within the actual grant, affected S1 return, acknowledgement and closure. If absent, block **only the exercise**. Real incidents are not to be invented for an assessment.
4. Separately publish a source-first `C/A/P/?/—` finding under the selected Methodology. `INSUFFICIENT` stays an evidence statement. A positive `P`/other notation does **not itself constitute, replace or revoke** the parent's rights; an authority succession is a separate governance decision.
5. Preserve S1 authority: canonical Index grades/adjudications, Skills procedures and Awesome curation are not subsumed by the phrase “key decisions.” S5 decides *delegation structure*, not every routine S1 task.
6. On any unexpected refusal, output explicitly: `BLOCKED_GOVERNANCE_DECISION`, `BLOCKED_OPERATIONAL_EXERCISE`, or `INSUFFICIENT_ASSESSMENT_EVIDENCE`, with the exact missing right or fact. **Never reuse the same `NOT_ADMITTED` label across these layers.**

## Regression scenarios

- Parent asks **“establish S3 for our domain prospectively”** with zero current incidents → S5 authorization can be recorded; no S3 action occurs; assessment unchanged.
- Parent authorizes **standing S3 grant with future-case predicates** → possible only with *explicit named owner and rights*; unfulfilled predicates stop specific future interventions, not existence of the grant.
- Agent finds **no cross-S1 Rum/SuisuiCode exposure** → do not issue a claim-specific instruction; parent may still decide whether S3 should be instantiated.
- Assessor returns `INSUFFICIENT` for `S3=C` after a parent mandate → leave grade unproved; do not reverse the mandate without owner decision.
- Parent selects **design only** → do not appoint or activate S3 even if documents/tests pass.
- A normal Index correction is in S1 rights → no S5 approval or S3 command needed, despite the existence of parent authority.

## Actual bounded disposition

[Owner policy clarification](https://github.com/opensiro/vsm-oss-organization/issues/236#issuecomment-6167754468) has been recorded with authenticated GitHub actor `xLagerFeuer`. [Stage-1 adoption](https://github.com/opensiro/vsm-oss-organization/issues/236#issuecomment-6167388750) stands; [PR #235](https://github.com/opensiro/vsm-oss-organization/pull/235) remains a non-operative draft. **No Stage-2 recipient or effective grant, no S3 transaction, no M1 closure and no grade upgrade** are inferred. This postmortem and linked control-plane documentation are **prospective prevention**, not retroactive rewriting of decision or assessment history.

**Reviewer provenance:** GPT-6 continuing author-context, not independent. Approval/merge and exact-head CI are separate publication checks and do not turn this into an independent assessment.
