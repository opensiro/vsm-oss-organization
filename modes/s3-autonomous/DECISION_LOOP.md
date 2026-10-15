# D1-A executable choice / return boundary

This module provides the **actual first-party orchestration shape**, not an active S3 grant or proof of `S3=A`.

A compatible **model-owned** S3 agent host invokes `decision_loop.run_decision(...)` with four separately supplied adapters:

1. `check_live_authority(grant, runtime_actor_id)` — verifies the current S5 owner-attested GitHub decision, grant publication, scope, agent identity, effective time, revocation, and G1 conflict; returns evidence-backed verification fields, not a locally invented "approved" boolean.
2. `check_current_admission(case)` — independently reads actual current S1 admission and real beyond-local shared-commitment evidence. An issue URL, fixture or source text alone does not establish admission.
3. `agent_decide(context)` — the *real model-backed* S3 runtime makes a non-deterministic choice; returns a bounded, source-citing `CONTINUE` or `REQUIRE_REPAIR` without human per-case selection.
4. `return_to_s1(action)` — an authorized transport to the named owning-S1 issue, using actual tool permissions, returning verifiable delivery receipt. **The resulting state is always `S1_RETURN_SENT_EFFECT_UNVERIFIED`**; the S1 owner's independent acknowledgement/actual effect is a different subsequent event, required before claiming closure.

No default provider, model credentials, authority adapter or write transport is embedded. A standalone `python decision_loop.py` has **no effect**. The shipped [D1-A grant](../../contracts/s3/autonomous-d1a.json) is `PENDING_S5_PUBLIC_ATTESTATION`, so `run_decision` **fails before calling any of the four adapters**, including a model or write operation. It cannot use human G1 instead.

[`tests/test_s3_d1a_decision_loop.py`](../../tests/test_s3_d1a_decision_loop.py) tests the callback wiring with explicitly **hypothetical** authority/admission/agent/transport fixtures: these are *not* first-party live S3 authorization, actual case admission, model-owned production operation or returned S1 effect. Green CI validates code boundaries only. A future real host must implement trusted adapters and present primary source receipts; arbitrary adapter booleans are not sufficient for a positive VSM `A` assessment.

Real subsequent S1 acknowledgement, effects and closure remain governed by [S3 current-control contract](../../contracts/s3/current-control.md) and [apply-to-S1 protocol](../../prompts/apply-s3-control.md). No Index grade, S5 policy or delegated class extension is authorized by this module.

## Concrete model and verified-feedback adapters

[model_owner.py](model_owner.py) can be passed as `agent_decide` through `functools.partial(..., model="<explicit model id>")` after D1-A gates; it makes a **real model-produced** bounded choice, with refusal/escalation fail closed and no tools. After independent S1 owner/effect verification, [s1_feedback.py](s1_feedback.py) can reconcile an exact named S1 work item's acknowledgement and effect. See [MODEL_AND_FEEDBACK.md](MODEL_AND_FEEDBACK.md). Neither new adapter proves active S5 grant, live admitted work, automatic S1 authority, or a current autonomy grade.
