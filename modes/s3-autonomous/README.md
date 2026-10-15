# OpenSiro S3 — autonomous current-control mode

**Mode availability: SOURCE-PREPARED / INACTIVE pending an attributable S5 D1-A grant.** The first-party agent can read this source, test its readiness and construct evidence candidates, but **must never choose or apply an S3 decision** until the distinct agent grant is authenticated and effective. This mode does not inherit or replace human G1.

## Route and governance

`START_HERE.md` → `docs/ECOSYSTEM.md` → current Organization `main` and M3 [#5](https://github.com/opensiro/vsm-oss-organization/issues/5) → [S5 authority](../../contracts/s5/parent-authority.md) → [D1-A machine grant](../../contracts/s3/autonomous-d1a.json) → [RUN](RUN.md). Read the operating sources and current issue each time. If any governing source is inaccessible, stop autonomous action.

The [source-selected model decision adapter](model_owner.py), [independent S1 feedback step](s1_feedback.py), and [integration/limits](MODEL_AND_FEEDBACK.md) extend the first-party actor/return capabilities without making the pending D1-A grant effective. The [first-party decision/return orchestrator](decision_loop.py) and its [bounded adapter contract](DECISION_LOOP.md) wire an **actual model-owned choice** to S1 delivery only after externally verified authority and admission. No model/transport/identity adapter is provided implicitly, and the shipped pending grant prevents any actor from choosing.

This mode uses real first-party current-regulation [standing commitments](../../contracts/s3/standing-current-commitments.md), [observation/option constructor](../../scripts/s3_current_regulation.py), [control transaction](../../control/s3-current-control-v1.template.json) and [return to S1](../../prompts/apply-s3-control.md). The script and validators are **support only**: an eligible agent runtime **itself** evaluates evidence, makes a bounded decision and records an attributable chosen response **without a per-case human choice**, or escalates when it lacks permission/evidence. GitHub merges and S1 technical adjudication remain separately owned.

**Authorized classes after activation:** only `CONTINUE` and `REQUIRE_REPAIR`. Neither `SET_CONSTRAINT`, `STOP`, grade override, global pause, S5 policy, Skills Methodology selection nor grant extension is allowed. Not even a real contract mismatch is automatically an S3 matter: ordinary S1/S2 repairs remain theirs.

## GitHub primary evidence and S3* trigger entry

[GitHub S1 source verification](github_s1_receipts.py) can verify real owning issue/comment/permission facts, S1 admission and independently attributable merged S1 effect metadata. Its [limitations](GITHUB_AND_S3STAR.md) are explicit: primary-source existence **does not itself prove whole-system S3 discretion**, and account permissions are not cryptographic proof of independent authorship. [S3* finding intake](s3star_intake.py) constructs only an **UNADMITTED** S3 candidate, never a selected decision. All remain behind actual separately effective D1-A authority.

## Public S5 authorization and S1 outbound transport

[Live public S5 source checker](github_s5_authority.py), [bounded GitHub REST client](github_rest.py), and [S1 comment delivery adapter](github_s1_delivery.py) implement **source and transport checks**, not a new delegated right. [Activation format and verification limits](GITHUB_D1A_ACTIVATION_AND_DELIVERY.md) require a separately authenticated parent decision, actual grant publication and revocation verification. The grant remains pending; its absence blocks every autonomous S3 choice.

## Runtime / feedback boundary

A compatible assistant/agent enters [RUN.md](RUN.md) directly and can use its available read/write transport within separately granted credentials; no private orchestration code is necessary to *interpret* the first-party decision process. Before each actual case, check live grant attribution/publication, identity, non-revocation and time; then verify separately admitted S1 work and the whole-system regulatory right. Distinguish an agent's **choice** from a deterministic script's validation and S1's subsequent **acknowledgement/effect**. The actor can only close an S1-returned case upon authentic downstream evidence, not its own assertion.

Current D1-A gate is **PENDING**; `scripts/check_s3_d1a_gate.py` must fail closed. Passing a future structural gate never substitutes for **live** owner authentication, revocation and actual S1 receipts.

## Source-first assessment

M3 uses the user's selected source-first evidence method, *not a mandatory fabricated transaction*. A positive `S3=A` assessment still requires a genuinely supported agent-owned decisive right with reachable autonomous operation and S1 feedback/closure, not simply this mode directory, CI or a design-only grant. Human G1 and parent S5 operate separately; no independent reviewer is invented.
