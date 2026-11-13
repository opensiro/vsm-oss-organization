# Organization-specific CLA template delegation (S5)

**Status:** S5 owner-approved delegation category, with per-template enrolment required. **Parent decision:** [Organization #323](https://github.com/opensiro/vsm-oss-organization/issues/323), recording the owner's instruction of 2026-11-13. **Owner:** `xLagerFeuer` under [parent-authority.md](parent-authority.md). **Execution owner:** Upstream Contributions S1, [Upstream #274](https://github.com/opensiro/upstream/issues/274).

## Delegated authority

The owner authorizes AI agents to execute contributor license agreement (CLA) acceptances **on the owner's behalf, using specific templates for specific organizations**. This is permission to establish and use a *bounded mechanism*, not blanket assent to unknown contracts, future revisions, every project, a company's obligations, or an unverified personal intellectual-property representation.

**S5** defines the legitimate human signatory, eligible contract categories, appointment and revocation. **Upstream S1** checks third-party current terms, executes only an enrolled exact template, preserves the provider receipt and returns exceptions. Third-party organizations control their own agreement and acceptance requirements. A GitHub credential, authenticated agent, S1 PR publication mandate or agent-written issue is not independently sufficient evidence of personal legal consent.

## Enrolment contract: fail closed

A CLA template is executable only when the following have been confirmed and recorded:

1. First-party counterparty and applicable original repositories; CLA URL; exact text/version and immutable digest.
2. Named natural-person or corporate signatory, GitHub identity and capacity to bind that party; truthful ownership, employment, copyright and patent assertions.
3. Literal prescribed acceptance procedure (e.g. a bot command vs PR submission that itself constitutes assent); no substitutions and no undisclosed extra statements.
4. **Attributable signatory approval of the specific current terms and template**, not just approval to create automation; valid start, expiry/renewal and revocation.
5. At execution, fresh source/terms and actor preflight, exactly bound repository/diff when acceptance occurs by PR, non-duplication and target-native checks; authenticated provider readback afterward.
6. Refusal for new/revised terms, source mismatch, different company capacity, missing rights, invalid authorization, unverified readback or unsupported third-party mechanism. Return the exact blocked case to the human signatory.

Lifecycle: `DISCOVERED -> PROPOSED -> APPROVED_EXACT_TERMS -> VERIFIED -> SUBMITTED -> TARGET_CONFIRMED`. Only `TARGET_CONFIRMED` is a target-side acceptance observation, and even that is not independent legal-validity certification. All earlier states and any drift or revocation remain non-executable.

**Explicit exclusions:** DCO `Signed-off-by`, corporate CLA absent actual corporate authorization, undisclosed patent/employment representations, authority expansion outside named third-party scopes, third-party merges and waived CI/security requirements. DCO remains under separate legal-person rules.

## Application and evidence

- [S5 decision record](../../records/s5/2026-11-13-cla-template-delegation-decision.md) and [historiographic analysis](../../supplementary/2026-11-13-cla-template-delegation-in-oss-vsm.md).
- [Upstream #274](https://github.com/opensiro/upstream/issues/274) owns a version-pinned deny-by-default registry and tests; existing [standing publication policy](https://github.com/opensiro/upstream/blob/main/docs/STANDING_EXTERNAL_PR_PUBLICATION.md) continues to forbid fabricated legal attestations for unenrolled cases.

No named template is activated by this policy alone. The decision is a prospective S5 envelope, not proof that a CLA was signed or that any VSM autonomy grade improved.
