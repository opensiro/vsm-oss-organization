# S3 autonomous decision and return — first-party operating protocol

**Current activation: NOT AUTHORIZED until the separate S5 D1-A grant is issued and published.** Compatible agent runtimes may follow steps 0–2 as **read-only preflight**, but must not run the decision or effect steps under the human G1 mandate.

## 0. Establish role and authority from live sources

1. Rebootstrap current Organization, selected Profile/Methodology and exact M3 #5; pin the current default branch, S1 owners and first-party S3 contracts.
2. Read the machine grant `contracts/s3/autonomous-d1a.json`. **Fail closed** unless its status is `ACTIVE`, concrete agent execution identity is attributable to this actual runtime, expiry/time is current, and a *separately owner-authored* S5 decision and normal grant publication on `main` are independently verified using the owning sources. Read linked revocations; local metadata and a GitHub account used as transport **do not authenticate** parent authorship.
3. Check `python scripts/check_s3_d1a_gate.py contracts/s3/autonomous-d1a.json --agent-id <attested-current-runtime-id>`. Even if it reports `STRUCTURAL_READY_LIVE_AUTHORITY_STILL_REQUIRED`, independently verify all live publication/parent/revocation facts. Human `G1` is **not** a fallback agent grant. Reject any unrecognized/changed policy or grant.

## Optional first-party GitHub evidence/S3* support

[`github_s1_receipts.py`](github_s1_receipts.py) verifies facts about the **real** owning S1 issue, separately attributable admission comment and later S1 PR/acknowledgement, failing closed when source/permissions are inaccessible. It deliberately cannot mark `nonlocal_right_verified` or `s1_s2_s5_falsifiers_checked` true. [`s3star_intake.py`](s3star_intake.py) routes a separately verified material S3* `FINDING` as an **UNADMITTED** source candidate only; it must pass the normal current-control qualification and D1-A grant before any decision. [Source criteria and limitations](GITHUB_AND_S3STAR.md).

## Optional first-party live S5-source and bounded S1 write support

[`github_s5_authority.py`](github_s5_authority.py) checks public D1-A grant content on current `main`, attributed parent issue decision, revocation pages and time. It also requires **separate trusted parent authorship attestation**: an issue comment posted using delegated credentials cannot prove the human S5 personally authorized autonomy. [`github_s1_delivery.py`](github_s1_delivery.py) has bounded, idempotent S1 issue-comment delivery after independently verified grant/admission; [`github_rest.py`](github_rest.py) allowlists actual GitHub REST routes. This is *not* a standalone operative host; [see publication and authority limits](GITHUB_D1A_ACTIVATION_AND_DELIVERY.md). Never pass fixture callbacks into a live host.

## 1. Observe the real inside-and-now organization

Read current Index/Skills/Awesome sources and the two existing [shared obligations](../../contracts/s3/standing-current-commitments.md). Obtain source-pinned **admitted** present S1 work; distinguish actual commitments, data from GitHub, current nonlocal exception and S1/S2/S5 rights. A source link with no fact/actor verification does not pass. A local assessment correction or curated-list update stays S1. If no material whole-system regulatory choice exists: **NON_ADMITTED / no decision**. Do not manufacture a disturbance.

## 2. Prepare a bounded, verifiable current-control case

Use [`scripts/s3_current_regulation.py`](../../scripts/s3_current_regulation.py) and the real S1 admission records as support (its candidate packet has `chosen_option=null` intentionally). Freeze source refs, affected original S1 work item, exact present shared right, risks, expiry/rollback and allowable classes. Ensure that the current S3 right truly exceeds S1/S2 but is not S5 ultimate policy; return may target one S1. A missing material fact escalates, not guessed into existence.

## First-party executable agent/transport boundary

[`decision_loop.py`](decision_loop.py) composes the **actual agent choice**, independent live authority/admission verification and a bounded S1 delivery. [`DECISION_LOOP.md`](DECISION_LOOP.md) defines mandatory adapters. No default trusted adapters are shipped, and the current `PENDING_S5_PUBLIC_ATTESTATION` grant makes the loop fail **before model invocation or S1 writes**. Callback-shaped mocked tests are engineering regression evidence, never source-first proof that a production model already owns S3.

## Optional first-party model and subsequent S1 feedback path

The [model-owned decision adapter](model_owner.py) issues a bounded OpenAI Responses API Structured Outputs request only when the enclosing D1-A decision-loop explicitly invokes it **after** independent S5 authority and current S1 admission checks. It is not a deterministic decision selector. The [S1 feedback reconciler](s1_feedback.py) can close a returned effect **only** on externally verified current owning-S1 acknowledgement and observed effect, rather than on the model's own assertion. [Integration contract and limitations](MODEL_AND_FEEDBACK.md).

Neither adapter supplies credentials, owner-attested S5 grant, independent GitHub read checks, or S1 write permission. They cannot run a real S3 decision or establish `A` from the shipped pending grant.

## 3. Own the decision autonomously (only after grant activation)

The **model-owned S3 actor** chooses `CONTINUE` (considered preservation of current work) or `REQUIRE_REPAIR` (bounded demand for an **existing** S1 work item), without asking the G1 human to choose the class. Record actual agent identity, authorized separate grant, source-linked basis, selected class, precise instruction and immutable transaction/decision evidence; **do not record hidden chain-of-thought**. If choice would require a forbidden class/altered grade or policy, escalate to S5 or the appropriate S1 owner.

Create a real [S3 current-control transaction](../../control/s3-current-control-v1.template.json) with `decision.owner_class = agent`, actual grant reference and a non-prefilled `REQUESTED → DECIDED` progression. Generic [state validator](../../scripts/check_s3_current_control.py) may check structure; **do not invoke `--g1`**, which correctly rejects agent ownership under human G1.

## 4. Return to S1 and observe actual subsequent effect

Follow [`apply-s3-control.md`](../../prompts/apply-s3-control.md) with existing named S1 work, exact owner and bounded instruction. Preserve S1 authority to choose the *technical/evidentiary fix*, decline an illegitimate instruction, re-admit a changed local work boundary or escalate. The agent must **not fabricate** an S1 acknowledgement, action or effect: record independently verifiable owning-S1 receipts. Only then mark `APPLIED`/`CLOSED`; otherwise remain pending or `ESCALATED`.

## 5. Recover, revoke or stop

On grant revocation/expiry, actor-identity mismatch, unavailable source, simultaneous conflicting human G1 case, nonlocal-proof failure or false effect: stop deciding immediately, leave an attributable pending/escalation record, do not silently switch to human G1 or extend authority. CI, labels, GitHub privileges and deterministic state checks are *enforcers only*.

## 6. Assessment record

A later source-first VSM assessment independently examines **positive first-party autonomous decisive ownership and reachable return** under Profile/Methodology, using this mode, effective S5 authority and applicable primary sources; a synthetic test or dormant mode proves neither `A` nor `C(P)`. The source-first evidence path is allowed without a newly staged incident but cannot substitute a missing actual grant.
