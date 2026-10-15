# M3 #5 — proposed autonomous S3 decision envelope (NOT ISSUED)

**State:** `DESIGN_ONLY / NO_AUTONOMOUS_S3_GRANT`. **Date / source cut:** 2026-10-15, Organization [`dc7176464930a2e0a996ca401e5ea1556eb710b6`](https://github.com/opensiro/vsm-oss-organization/tree/dc7176464930a2e0a996ca401e5ea1556eb710b6). **Governing issue:** [M3 #5](https://github.com/opensiro/vsm-oss-organization/issues/5). Selected Profile v0.2.4 / Methodology v0.3.7. Authoring agent prepares choices only and **does not exercise the S5 issuer's authority**.

## The specific authority gap

Current real **S3=C** regulation substrate already exists: [standing current commitments](../../contracts/s3/standing-current-commitments.md), [first-party S3 constructor](../../scripts/s3_current_regulation.py), [current-view collector](../../scripts/collect_s3_current_view.py), [current-control transaction shape](../../control/s3-current-control-v1.template.json), and [S3→S1 return](../../prompts/apply-s3-control.md). The current only operative S3 grant, [G1](../../contracts/s3/parent-assisted-g1.md), names **human** `xLagerFeuer` as the holder of each current S3 decision right. Agents may observe, recommend and transport only. No file in this proposal changes that fact.

An autonomous agent cannot obtain `S3=A` ownership by running the source-view script, answering a prompt, opening this PR, seeing `owner_class=agent` in a schema, or acting on the human G1 grant. **Creating a distinct agent-owned S3 right, changing the delegation model or redefining milestone closure evidence is reserved to the legitimate S5 parent**, [`parent-authority.md`](../../contracts/s5/parent-authority.md) and [`parent-boundary.md`](../../contracts/s5/parent-boundary.md). No agent-side instruction or generic "continue" may substitute.

## Concrete S5 decisions required (independent questions)

### D1 — Autonomous S3 authority

**Recommended D1-A: NARROW_CONDITIONAL_AGENT_GRANT** (not adopted by this document).

A separate, revocable, finite-term **agent S3 holder**, never the human G1 identity or an agent pretending to be the parent, may autonomously **select** among `CONTINUE` and `REQUIRE_REPAIR` only for independently admitted *present whole-system* reconciliation of either of the two current shared commitments in [standing-current-commitments.md](../../contracts/s3/standing-current-commitments.md). Each case must prove a specifically attributable material choice beyond S1 repair, ordinary S2 coordination and S5 ultimate policy. The bounded decision may return to one existing S1 work item even if the whole-system evidence spans two domains. It must preserve the S1 owner's own local implementation and Index's canonical grade/adjudication. `SET_CONSTRAINT`, `STOP`, freeze/override, budget/policy/Methodology selection, security/permissions, further delegation, upstream source rewriting, and S3* audits remain outside this initial proposed autonomous envelope. G1 human mode stays separate; no simultaneous conflicting decision on the same current case.

**Alternative D1-B: NO_GRANT, PREPARE_ONLY.** Keep the current human G1 as the sole S3 decisor; an agent may prepare choices/analysis but cannot satisfy autonomous `A`. Accept M3 remains open.

No "wide autonomous mandate" is offered by default; broader classes would need a separate explicitly reasoned S5 decision rather than permissive inheritance from generic S3 schema values.

### D2 — M3 evidence acceptance

**Recommended D2-B: SOURCE_FIRST_AUTONOMOUS_MODE_ASSESSMENT** (not adopted by this document). Prospectively amend M3 #5's local completion gate to permit a source-first positive assessment of a **shipped, boundary-reachable first-party agent-decision + S1-return loop**, when actual model-owned discretion, effective delegated authority, operational closure capability, and falsifiers are demonstrated from reproducible primary sources. **No fabricated runtime transaction is required by the general Methodology merely to demonstrate `A`.** A string-only schema, stub, prompt template, deterministic selector or approval-required "agent" is not sufficient positive `A` evidence. If the positive first-party autonomous ownership/closure path cannot be reconstructed, return `INSUFFICIENT`.

**Alternative D2-A: PRESERVE_M3_REAL_TRANSACTION_GATE.** Keep #5's current stricter project-specific requirement to cite at least one actual agent-owned decision, S1 application and effect; this is not silently the general Methodology threshold.

D1 and D2 are distinct: authorizing an agent does not establish its supported first-party operating mode; allowing source-first assessment does not grant authority. No selection made in this document.

## D1-A implementation contract if actually selected by S5

1. **Grant identity and issuance:** publish a **new** immutable, attributable S5 owner choice linked to [#5](https://github.com/opensiro/vsm-oss-organization/issues/5) (or a new explicitly linked S5 decision issue). A reviewable grant on `main` identifies the concrete agent **role and execution identity**, exact in-scope repo set, classes, term (recommended no more than 30 days), revocation source, non-delegation, conflict rule with human G1, owner/support split, and S1 return envelope. Activation requires both explicit owner choice **and** verified publication; a PR approval or green CI alone cannot supply S5 legitimacy. Until then, the mode is **NOT_AUTHORIZED**.
2. **Admit a real S3 case, not an issue title:** build whole-system context from actual current Index/Skills/Awesome sources, verify source and S1 work admission, identify the shared present organizational commitment, prove a nonlocal decision right unavailable to S1/S2, and freeze material exact sources. If not proved: `NON_ADMITTED` / `ESCALATED`, no S3 decision. A valid existing S1 matter may need only one returned target.
3. **Agent owns the actual choice:** compatible agent runtime reads the accepted case and selected envelope, chooses `CONTINUE` or narrowly tailored `REQUIRE_REPAIR` without waiting for a per-case human selection, records the actor execution identity and decision evidence (not hidden chain-of-thought), and cannot reinterpret allowed class support as an instruction to decide. An LLM as *adviser* to a human is not agent autonomy.
4. **First-party Organization route:** expose a reachable `modes/s3-autonomous/README.md` and `RUN.md` **only after** grant publication; reuse [current-control transaction](../../control/s3-current-control-v1.template.json) with `decision.owner_class=agent`, new grant reference and agent-owned selection/return record. Do **not** use `--g1` checks for this actor; those checks correctly reject non-human G1 decision ownership. The new grant must have its own authority verification while general structural guards remain shared. Agent/runtime tools, GitHub API, schedulers, schemas and CI transport/enforce but do not own the decision.
5. **Return into S1 and bounded closure:** after the agent selects, S1 independently checks its own admission, accepts/applies or explicitly rejects/escalates the **bounded current-control instruction**, retains local discretionary grade/technical repair ownership, records acknowledgement and effect. Preserve separate read/write authority: an agent cannot assert an S1 effect merely by setting a JSON field or by creating a GitHub comment. Failure of publication, G1 conflict, grant expiry/revocation, case proof, S1 permission, or real effect → fail closed; no `A` evidence from a forged terminal record.
6. **Evaluation:** source-first assessment must distinguish primary evidence of the actual supported **agent-owned** decision and feedback capability from synthetic fixture smoke tests, API access, CI passing, constructor `C`, parent S5=P, and independent externally published Index grades. The M3 tracker remains open until its **effective, prospectively selected** exit gate is met.

## Explicit negative / protection tests to implement with the mode

- No autonomous action using the existing human G1 grant or before attributable S5 issuance and publication.
- Fail closed on revoked/expired grant, wrong actor/role, unverified GitHub ref, or unsupported class.
- Local Index assessment/queue repair, Skills procedure fix, Awesome curation and S2-only interference remain local; cross-repo mention is not whole-system regulation.
- Chosen decision cannot change selected Profile/Methodology, grade/adjudication, S5 boundary, repository privileges, or independently perform S1 repair.
- Reject manufactured case, missing S1 admission, unsupported shared current obligation, missing exact evidence, and spoofed effect/closure.
- No automatic inference of `S3=C(P)`, `S3*=A`, S2, S4, autonomous `A` grade, or independent review from a grant, mode directory or test success.

## Verification and owner choice

This proposal can be published with ordinary documentation CI because its only effects are **options and an implementation specification**. It cannot authorize a decision, start a run, claim a `S3=A` witness, amend the M3 gate, or change `TODO.md`. After inspection, the legitimate S5 holder can select D1-A/D1-B and D2-A/D2-B **explicitly**. Only then implement the operative mode and assess under the chosen evidence gate.
