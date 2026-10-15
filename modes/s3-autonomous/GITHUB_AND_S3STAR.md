# First-party GitHub S1 primary-source verification and S3* intake

**M3 #5, source-first preparation.** The code here is *read-only*. It does **not** issue the missing S5 D1-A grant, call a model, create an S3 intervention, or accept unit fixtures as a real S1 effect. The active grant remains `PENDING_S5_PUBLIC_ATTESTATION`.

## S1 admission and feedback fact checks

[`github_s1_receipts.py`](github_s1_receipts.py) provides a narrowly allowlisted GitHub REST reader using an authenticated `GITHUB_TOKEN` for collaborator permission inspection. It reads only Index/Skills/Awesome GitHub sources; the token must have the permissions needed for `GET /collaborators/{login}/permission`. If the token lacks this source access, verification fails **closed**; public issue visibility is not enough.

**Current S1 admission:** the named owning-S1 issue must be currently open; an exact comment on it by a user with inspected `write|maintain|admin` permissions must contain **exact** machine-readable content:

```text
OPENSIRO_S1_ADMISSION_V1
{"verdict":"ADMIT","target":"https://github.com/opensiro/awesome-vsm-harness/issues/7","commitment_id":"canonical-publication-continuity"}
```

Those values are **format examples**, not real admission claims. At least two source issue refs from distinct S1 repositories must exist. The adapter explicitly sets `nonlocal_right_verified=False` and `s1_s2_s5_falsifiers_checked=False`: verifying factual admission and source identity does **not** determine whether S3 (rather than S1/S2/S5) owns a present cross-system choice. A **separate, real first-party actor's functional assessment** must supply that discretionary admission before calling `decision_loop.run_decision`; do not mechanically turn these booleans true.

**S1 returned effect:** an independently attributable S1 writer must comment on the *exact* target after the S3 delivery comment; this comment cannot come from the S3 transport account. The S1 effect must be a **merged PR with actual changed files**, authored by a different account than the S3 transport actor, linking both the owning issue and exact S3 instruction comment in its body. The merge must postdate the acknowledgement. The verifier checks actor permissions via GitHub, merged PR status and source chronology, returning facts for [`s1_feedback.reconcile`](s1_feedback.py). Even these receipts do not independently prove *semantic correctness* of the repair; assessing the real effect against task-specific requirements remains necessary.

**Non-claim:** Account-login mismatch is not cryptographic proof of independent runtime/human authorship. An agent with access to multiple accounts, compromised credentials, or forged upstream GitHub data defeats identity assumptions. An independently meaningful trust policy/identity attestation is still required to establish genuine autonomy and claim-relative S1 evidence. This is an engineering source-verification primitive, **not** a full trusted deployed adapter.

## S3* material finding path

[`s3star_intake.py`](s3star_intake.py) offers a bounded *non-admitting* bridge for a material `FINDING` from the existing [complementary audit contract](../../contracts/s3star/audit.md), returning `UNADMITTED_S3_CANDIDATE_FROM_S3STAR` with no chosen class or S1 effect. The caller must independently verify the original audit judgment/source owner — including its real complementary access and published provenance — and *still* run D1-A separate S5 grant checks, real S1 admission and nonlocal S3 functional qualification. `PASS`, unsupported evidence, and merely local findings do **not** enter S3 decision state.

This gives a first-party **candidate intake** from S3* without mistaking audit labels, reviewer scripts or GitHub comments for independent audit, an S3 order, or closed S1 effects. Tests are purely simulated. No actual S3* finding is manufactured and no S3* result is changed.

## Assessment boundary

The relevant M3 issue requires the **actual agent-owned** S3 decisive/feedback loop to be reachable in the first-party standard mode, with separately effective S5 delegated autonomy. These read-only validators and candidate bridge alone cannot upgrade `S3=C` to `S3=A`. The missing live S5 attestation and real execution identity remain unaffected by this PR; a specially staged S3 transaction is **not a universal assessment prerequisite**.
