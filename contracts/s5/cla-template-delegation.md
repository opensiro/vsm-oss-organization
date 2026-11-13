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
4. **Attributable signatory approval of the specific current terms and template**, not just approval to create automation; valid start, any **actual** expiry/renewal rules and revocation. No invented per-PR expiration or reapproval when unchanged.
5. At **first acceptance**, fresh source/terms and actor preflight, exactly bound repository/diff when acceptance occurs by PR, non-duplication and target-native checks; authenticated provider readback afterward. For **later PRs**, verify the still-valid, repository-scoped accepted CLA separately from per-PR code/rights and technical checks.
6. Refusal for new/revised terms, source mismatch, different company capacity, missing rights, invalid authorization, unverified readback or unsupported third-party mechanism. Return the exact blocked case to the human signatory.

Lifecycle: `DISCOVERED -> PROPOSED -> APPROVED_EXACT_TERMS -> VERIFIED -> SUBMITTED -> TARGET_CONFIRMED`. Only `TARGET_CONFIRMED` is a target-side acceptance observation, and even that is not independent legal-validity certification. All earlier states and any drift or revocation remain non-executable.

**Explicit exclusions:** DCO `Signed-off-by`, corporate CLA absent actual corporate authorization, undisclosed patent/employment representations, authority expansion outside named third-party scopes, third-party merges and waived CI/security requirements. DCO remains under separate legal-person rules.

## Reusable, repository-scoped CLA consent

**Default for an eligible one-time CLA:** the signatory accepts the exact first-party CLA text **once** for one specified original repository. After the first verified acceptance, the recorded `(human signatory, capacity, original repository, counterparty, CLA text SHA-256)` remains reusable for later contributions under those same terms. Do **not** request a new CLA approval merely because a later PR has a different branch, commit, head SHA, patch, issue number, or submission date. A consent/record may be revoked or time-limited by its actual governing terms or the signatory's scope; do not invent a short expiration for a perpetual agreement.

**Per-contribution check is not another CLA signature.** For every proposed external PR, Upstream S1 still verifies current original-repository CLA text/digest, identity/capacity, the contributor's rights to *that particular code* (including employer and third-party interests), current target instructions and native technical tests, clean fork/branch provenance and the independent publication mandate. Such checks need no repeated human acceptance of unchanged CLA terms; new rights conflicts require separate resolution rather than a recycled declaration.

**Renew/re-enrol only when material to the authorization:** first-party text/version or counterparty changes, target repository outside approved scope, signer/capacity changes, actual expiry or revocation, an external project's own mandatory repeated declaration, or an unresolved contributor-rights representation. Do not silently extend an individual CLA to OpenSiro as a corporate signatory or to a different upstream repo.

**Separate acceptance from delivery idempotency.** A single-use cryptographic receipt or nonce may protect the *first acceptance event* or one outbound GitHub operation against replay. Its consumption **does not expire the accepted CLA**. Per-PR technical POST retry protection is likewise separate from the lifetime of the CLA. DCO `Signed-off-by` remains per commit when required and does not inherit this reusable CLA rule.

Revka v1.0 currently provides no stated fixed expiration or per-PR re-acceptance requirement. Its first-party mechanism says submitting a PR/patch indicates acceptance; that original acceptance has not yet been independently confirmed for the prepared OpenSiro fork-local proposal. This rule describes reuse **after valid first acceptance**, not a claim that this chat or a GitHub token has already created one.

## Application and evidence

- [S5 decision record](../../records/s5/2026-11-13-cla-template-delegation-decision.md) and [historiographic analysis](../../supplementary/2026-11-13-cla-template-delegation-in-oss-vsm.md).
- [Upstream #274](https://github.com/opensiro/upstream/issues/274) owns a version-pinned deny-by-default registry and tests; existing [standing publication policy](https://github.com/opensiro/upstream/blob/main/docs/STANDING_EXTERNAL_PR_PUBLICATION.md) continues to forbid fabricated legal attestations for unenrolled cases.

No named template is activated by this policy alone. The decision is a prospective S5 envelope, not proof that a CLA was signed or that any VSM autonomy grade improved.
