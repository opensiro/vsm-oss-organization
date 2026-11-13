# S5 decision record: bounded autonomous CLA template execution

**Date:** 2026-11-13. **System-in-focus:** current bounded OpenSiro VSM Harness OSS organization. **Decision kind:** parent-governed change to allowable future delegation. **Evidence state:** `OWNER_DIRECTIVE_TRANSCRIBED / TEMPLATE_ENROLMENT_PENDING / NO_CLA_ACCEPTANCE_CLAIMED`.

## Authority and attribution

The legitimate parent is `xLagerFeuer` under [S5 parent authority](../../contracts/s5/parent-authority.md). In the 2026-11-13 operator exchange, the owner explicitly instructed: agents are authorized to complete CLA acceptance on the owner's behalf using **concrete templates for specific organizations**, and requested a scientific/historiographic note. [Organization issue #323](https://github.com/opensiro/vsm-oss-organization/issues/323) is the public, agent-transcribed and traceable work record. An issue created using a connected GitHub account is **not** itself an independently verified first-person legal signature to an external CLA.

The standing [Upstream external-PR mandate](https://github.com/opensiro/upstream/blob/main/docs/STANDING_EXTERNAL_PR_PUBLICATION.md) already delegates qualified PR publication but reserves contributor-person legal statements. This decision adds a **conditional template-specific delegation category**; it does not erase the standing policy's refusal for unenrolled or ambiguous attestations.

## Decision / returned boundaries

- Create the owner/signer-capacity and exact-term enrolment contract at [`contracts/s5/cla-template-delegation.md`](../../contracts/s5/cla-template-delegation.md).
- Upstream S1 implements preflight, template records, authenticated execution receipts and hard refusal on policy drift under [Upstream #274](https://github.com/opensiro/upstream/issues/274).
- Legal terms remain governed by third-party maintainers/counterparties. CLA and per-commit DCO are distinct, and no unapproved future agreement or corporate representation is authorized.
- Exceptions return to the authorized human signatory. Inactive/revoked templates cannot be executed by a standing GitHub token.

## Source-specific motivating cases (not sign-offs)

| First-party source | Mechanism | Observed boundary |
| --- | --- | --- |
| [Revka CLA v1.0](https://github.com/KumihoIO/Revka/blob/main/docs/contributing/cla.md) | PR submission itself is individual CLA assent | [Prepared fork PR #1](https://github.com/opensiro-contributions/Revka/pull/1) is not original-project acceptance |
| [Microsoft Fara #96](https://github.com/microsoft/fara/pull/96#issuecomment-6810190721) | CLA bot requests `@microsoft-github-policy-service agree`, individual/corporate variants | An existing PR and bot message do not establish assent |
| [VOLY DCO policy](https://github.com/voly-codes/voly/blob/main/CONTRIBUTING.md) | Each commit needs `Signed-off-by` | Outside this CLA-specific delegation |

## Evidence and closure boundary

This records a **decision**, not its successful application. A real template-specific mandate, current exact terms, source-native compliance, provider-recorded acceptance and downstream organizational consequences each require separately attributable evidence. The [historiographic note](../../supplementary/2026-11-13-cla-template-delegation-in-oss-vsm.md) preserves an interpretive research account, not a positive autonomy assessment.
