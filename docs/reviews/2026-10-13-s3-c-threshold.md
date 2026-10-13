# Source-first review — S3 constructor classification versus M1 real-use acceptance

**Date:** 2026-10-13 UTC
**Repository / reviewed main:** [Organization `cf3de01818e6d54ffbf23ae7b69bef3a1e5ccd52`](https://github.com/opensiro/vsm-oss-organization/tree/cf3de01818e6d54ffbf23ae7b69bef3a1e5ccd52)
**Review status:** author-context, non-blind, **PROPOSAL FOR GOVERNANCE REVIEW** — not a Skills Methodology amendment, not an independent general assessment, not `S3=C` adjudication.
**Assessment authority selected by Organization:** [`UPSTREAM_CONTRACT.json`](../../UPSTREAM_CONTRACT.json): Profile `v0.2.4`, Methodology `v0.3.7`. Published Skills `v0.3.8` is backward-compatible, but the Organization has **not** selected it.

## Question

Does a completed real S3→S1 transaction define `S3=C` **universally**, or is that an additional **Organization M1 acceptance criterion**? Conversely, does having an implemented S3 constructor automatically justify `S3=C`?

**Source-based answer:** Neither extreme is warranted.

- [Selected Profile `v0.2.4`, §7](https://github.com/opensiro/vsm-harness-profile/blob/v0.2.4/PROFILE.md) defines the S3 function: *inside-and-now* cohesion through **whole-system current control**, with a **whole-system current view** and actual authority over current resources/commitments/priorities/constraints. A task router, scheduler, static budget gate, manager name, or ordinary local S1 decision is not sufficient.
- [Selected Skills `v0.3.7` autonomy states](https://github.com/opensiro/vsm-harness-skills/blob/v0.3.7/skills/assess-vsm-harness/references/autonomy-states.md) defines `C` as **function established** plus **first-party function-specific decisive decision/feedback primitive**, while a developer may still need to compose an autonomous actor, authority, independence or closure. [The published `v0.3.8` calibration](https://github.com/opensiro/vsm-harness-skills/blob/v0.3.8/skills/assess-vsm-harness/references/positive-evidence-calibration.md) reiterates that a representative operating trace is an optional inspection aid, not a universal executable-run obligation for `C`; it introduces no changed threshold.
- [Selected Skills `v0.3.7` autonomy states](https://github.com/opensiro/vsm-harness-skills/blob/v0.3.7/skills/assess-vsm-harness/references/autonomy-states.md) defines `A` by **autonomous agent ownership** of the decisive decision/feedback loop, with operational closure in the claimed supported mode. `A` does not require every enforcement mechanism to be agentic; it does require the organizational discretion to be agent-owned.
- [Organization M1 #3](https://github.com/opensiro/vsm-oss-organization/issues/3) and [trial #39](https://github.com/opensiro/vsm-oss-organization/issues/39) explicitly choose a **real reference transaction** as the Organization's local milestone acceptance. An Organization-local contract cannot silently redefine general Skills semantics. Yet absence of a universal run requirement does **not** automatically waive the narrower chosen M1 exit criteria.

## Reconstructable constructor evidence

| Surface (first-party at reviewed revision) | What exists | What it proves / does not prove |
| --- | --- | --- |
| [Operational S1 domains](../../contracts/s1/domain-contracts.md) | Index, Skills, Awesome with concrete responsibilities, local decision rights and escalation limits | A real system-in-focus with current operations. Not itself S3 whole-system allocation/authority. |
| [S3 current-control contract](../../contracts/s3/current-control.md) | Admission rules for whole-system current needs, allowed bounded decisions, ownership vs support | Function-specific intended construction path; normative text alone is not a functional witness. |
| [S3 role](../../roles/S3.md) and [pre-admission intake](../../prompts/intake-s3-current-control.md) | Candidate discrimination, current context, owner and S1 target requirements | More specific than generic extension/handoff. A named role/prompt alone is not actual established current control. |
| [Machine-readable transaction](../../control/s3-current-control-v1.template.json) and [reviewable record](../../templates/s3-control-record.md) | Structured `REQUESTED` intake, decision, owner, support, S1 return and closure fields; undecided fields pending by default | Ready-made S3-shaped request/return infrastructure. No real `DECIDED/APPLIED/CLOSED` witness is created by a template. |
| [S1 role return adapter](../../roles/S1.md) and [application prompt](../../prompts/apply-s3-control.md) | S1 may acknowledge/apply/reject an **already legitimate** bounded returned instruction | A specialized first-party S3→S1 return surface is supported. No known qualifying returned S3 instruction was executed merely by adding the adapter. |
| [M1 issue #39](https://github.com/opensiro/vsm-oss-organization/issues/39), [September 30 frozen pre-assessment](../../records/assessment-snapshots/2026-09-30-general-preassessment.md) | Repeated source-first screens, provisional historical `S3=?`, currently uncompleted trial | No source-backed current positive verdict. Historical `?` must not be rewritten or promoted by changing documentation. |
| [Skills v0.3.8 retrospective](../../records/s3-candidates/2026-10-13-skills-methodology-0.3.8-retrospective.md) | Real Skills publication reviewed against S3; disposition insufficient as whole-system current-control witness | Real S1 work cannot donate S3 authority without an attributed whole-system decision and return. |

**Constructor code paths vs composability.** The JSON template, role prompts, domain and owner conditions explicitly target S3-specific request/decision/S1 return. They support a **strong structural argument for a specialized first-party constructor**, but no inspected source yet establishes *which concrete inside-and-now systemwide variety is actually regulated under an evidenced whole-system S3 authority*. Unlike a hypothetical generic plugin hook, the design is dedicated to S3; unlike a positively witnessed S3 function, its current decision owner and exercised regulation remain unresolved.

## Threshold decision matrix

| Question | Methodology test | Separate local M1 test |
| --- | --- | --- |
| Function | Real S3 regulation of current whole-system commitments/constraints, not just a generic manager | Qualifying real present-time Organization choice and current S1 refs must be frozen |
| First-party path | S3-specific decisive decision/feedback primitive, reachable in supported mode | Issue #39 transaction and existing S1 return procedure executed |
| Owner and closure | Owner/support distinguished; **actor, authority or closure may require composition for `C`** | Explicit owner choice and observable S1 acknowledgement/effect required to complete trial |
| Evidence technique | Source-first explicit/structural/observed evidence, sufficient to **establish** the function; no universal provider-backed or completed live-run rule | Owner-chosen stronger exercise of the constructor |
| Grade | `C` if function + specific constructor fully supported; `?` if evidence insufficient | Milestone may remain open even if a future independent Methodology assessment finds `C`; vice versa no constructed grade inferred merely because a local workflow ran |
| Autonomous ownership | `A` needs an agent to own organizational decision and close it operationally | M3 objective; M1 explicitly does not require `A` |

## Finding and falsifiers

**F1 — wording conflates tests.** Before this proposed draft, [M1 roadmap](../ROADMAP.md) and [S3 contract](../../contracts/s3/current-control.md) describe "one real transaction" as if it were universally required to credit constructor state `C`. That language is **more restrictive** than the general Methodology definition and should be marked as this Organization's *local M1 evidence/exit choice*, not a universal rule.

**F2 — constructor exists, positive S3 not automatic.** The current source has a dedicated construction surface, but source-first review does not yet establish qualifying S3 whole-system regulation and actual decision authority. Consequently this review returns **`INSUFFICIENT` for an independently supportable fresh positive `S3=C` interpretation**, rather than `S3=C` or `S3=A`. It also does not assert negative `—`.

**F3 — M1 review/authority is separate.** [Issue #39](https://github.com/opensiro/vsm-oss-organization/issues/39) currently owns a genuine real-use trial as an explicit admission/execution contract; [parent M1 #3](https://github.com/opensiro/vsm-oss-organization/issues/3) owns the milestone exit. This draft **does not** edit either issue, mark #39 complete or replace the planned trial. Any relaxation or replacement of that local acceptance test needs a **prospective, attributable owner decision** and aligned issue/roadmap/contract changes. A generic user `continue` or release approval is not that decision.

**F4 — no fabricated proof.** Neither Skills `v0.3.8` publication, a migration between selected versions, green CI, a PR approval, GitHub permissions, issue descriptions nor `REQUESTED` placeholders are evidence of executed S3 current-control. The distinction addresses the evidence standard without retroactively manufacturing a decision.

## Owner-governed next choices (not executed by this review)

1. **Preserve the already selected M1 live-trial acceptance:** keep #39 OPEN, inspect actual new current whole-system needs; if none qualifies, do not stage one. This remains the effective gate until the owner changes it.
2. **Prospectively reassess local M1 acceptance:** separately commission an appropriately fresh source-first assessment focused on establishing the S3 function and the boundary-reachable specific constructor **without imposing an unwritten universal live-run condition**. If it positively establishes `C`, the Organization owner may then decide whether the additional integration trial remains necessary for M1 and amend #3/#39 **explicitly**. If insufficient, keep the current gate. A reviewer must be independent of this author context for any claimed independent result.
3. **Future `A`:** evaluate only an actual autonomous S3 actor owning current whole-system decisions and closing the loop in a supported mode (M3), never from constructor readiness alone.

## Disposition / publication boundaries

**Verdict:** `LOCAL_M1_THRESHOLD_CONFLATION_CONFIRMED; S3_POSITIVE_NOT_ADJUDICATED`. Clarify the wording in the Organization repository **as a proposed local documentation correction only**. No Profile or Skills release, canonical Index change, S3 transaction, S3 classification upgrade, milestone closure, historical assessment overwrite, reviewer approval or autonomous deployment is authorized.

This review is **context-exposed** and was prepared by the same assistant context that discussed and implemented the constructor follow-ups and v0.3.8 release. It does not qualify as an independent S3 assessment.
