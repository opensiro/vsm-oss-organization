# First-party model-owned S3 and S1-feedback components

**Scope:** Organization M3 D1-A. Shipped grant remains `PENDING_S5_PUBLIC_ATTESTATION`; neither this model adapter nor its simulated tests authorize or execute an S3 action.

## Model as the *decisive* S3 actor

`model_owner.py` supplies a concrete [Responses API](https://platform.openai.com/docs/api-reference/responses/create) Structured Outputs invocation using a **model selected by the runtime host** and `OPENAI_API_KEY` supplied only after the prior trusted D1-A checks in `decision_loop.py`.

The adapter uses `store=false`, no provider tools, a strict JSON schema for `CONTINUE` / `REQUIRE_REPAIR` / `ESCALATE`, bounded request/response sizes, provider timeout, and no logging of secrets. An `ESCALATE` result raises an exception rather than becoming a fabricated S3 `DECIDED` state. Source-issue content is passed as **untrusted context**, not governing agent instructions. The enclosing `decision_loop.run_decision` checks the effective grant, verified current S1 admission and allowed classes before calling this adapter; source URL strings alone are not admitted evidence.

A future compatible host passes:

```python
from functools import partial
# An explicit host must supply independently authenticated authority/admission
# and real authorized GitHub S1 transport. These are NOT supplied in this snippet.
agent_decide = partial(model_owner.model_decider, model="explicit-model-id")
# Pass agent_decide to decision_loop.run_decision(...) AFTER active S5 grant.
```

This is a **real model API implementation**, not a hard-coded `CONTINUE` or `REQUIRE_REPAIR` selector. However no model key/actual model inference, owner signature, S1 admission, or user S3 decision is claimed to have been exercised in CI. Supported model ID/API access must be supplied and verified by the actual deployment.

## Feedback path and independent S1 effect

`s1_feedback.py` takes a delivered-but-unclosed S3 action and only moves it into `S1_RETURNED_EFFECT_VERIFIED` after an **independent owning-S1 verification** of (a) exact target issue acknowledgement, (b) source-pinned effect in that same S1 repo, (c) source and actor independence from the original S3 agent. An arbitrary boolean supplied by the model or a GitHub comment cannot be trusted as evidence: the required `fetch_verified_s1_result` host adapter must inspect the actual S1 primary source, owner and work admission and reject unsupported results.

The [decision loop](decision_loop.py) intentionally returns `S1_RETURN_SENT_EFFECT_UNVERIFIED` on delivery; this new function performs a **separate subsequent feedback reconciliation**. A first-party host must still supply a real owner-authenticated verifier for current GitHub sources, without relying on test fixtures.

## D1-A entry conditions still not met

The [current grant](../../contracts/s3/autonomous-d1a.json) lacks public attributable owner issuance and actual runtime identity. The first-party mode still lacks **trusted live authority and S1-admission adapters and a GitHub S1 write transport**; the newly added model adapter alone is not a complete activated mode. Do not mark M3 or `S3=A` complete merely because the library can call an API or the unit tests pass. Source-first assessment is admissible, but the decisive autonomy/closure path and real S5 right must be fully supported by the evaluated first-party boundary.
