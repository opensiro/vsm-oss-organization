# Executor provenance witness

This document defines the repository-local evidence contract for binding an ordinary bounded S1 run to the autonomous executor/session that exercised its decisive local decision rights.

It applies the VSM Harness Profile and Methodology; it does not redefine S1 or autonomy. In particular, it does not make a runtime, scheduler, GitHub identity, signature, or transport mechanism the owner of an organizational decision merely because that mechanism records or enforces an action.

The contract is intentionally runtime-neutral. ChatGPT, Codex, Claude Code, custom harnesses, local schedulers, dedicated GitHub Apps/bots, and other execution technologies may conform if they produce the required primary evidence.

A conforming witness makes a new instrumented M0 trial reviewable. The existence of the witness or this document does **not** establish `S1=A`; the trial still has to establish function, decisive right, owner, support/enforcement separation, and closure from primary evidence.

## Problem being closed

Instrumented trial #16 closed its bounded contribution as PR #17, but GitHub exposed only the contributor's authenticated identity. A second reviewer could reconstruct the decisions and actions but could not independently bind them to the autonomous executor/session rather than to a human manually performing or dictating the same ordinary local choices.

The missing evidence is therefore not another statement that "an agent did the work". It is a primary provenance chain:

```text
pre-run executor/session anchor
        ↓
observable run events, including all post-start human inputs
        ↓
immutable action/result references
        ↓
final attestation bound to the same run
```

No hidden chain-of-thought is required or desired.

## Minimum witness

A positive executor-provenance witness MUST contain three linked parts.

### 1. Pre-run anchor

Before ordinary contribution decisions/actions begin, publish or otherwise make immutable primary evidence of:

- witness format/version;
- unique `run_id`;
- system-in-focus and repository boundary;
- bounded work-item reference;
- frozen repository start revision;
- exact governing role/prompt revision or content digest;
- executor/session attester identity;
- verification key/certificate/identity reference and signature format;
- trust basis for why that attester is controlled by the execution boundary rather than by the contributor during the run;
- pre-start human constraints reference or digest;
- the complete allowed channel set through which post-start human input may reach the executor.

The anchor MUST be bound to the attester by a verifiable signature or equivalent third-party attestation. A self-description, runtime/model name, unsigned session ID, or contributor-authored statement is not sufficient.

The pre-run anchor prevents a provenance record from being created only after the result is known.

### 2. Ordered run record

The run record MUST be bound to the same `run_id` and attester and MUST preserve an ordered, tamper-evident record of organizationally material events. Each material event records only observable facts needed for review, for example:

- event sequence/id and type;
- actor class (`executor`, `human`, or `support`);
- concise observable decision/input/action summary;
- evidence available at that moment by reference, where material;
- authority classification (`inside_s1`, `outside_s1_escalation`, or `support_only`);
- immutable action/result reference when an observable external action occurred;
- digest or equivalent binding for payloads whose content matters;
- previous-event/root binding or another mechanism that makes omission/reordering detectable.

The record MUST include every post-start human input that can reach the executor through an allowed input channel, including a human response to an escalation. It MAY omit purely mechanical transport metadata that cannot affect executor decisions.

The witness does not need to expose private reasoning. A decision entry should state the observable choice, evidence references, chosen action, and authority boundary, not chain-of-thought.

### 3. Final attestation

At run closure, the same execution trust chain MUST attest:

- `run_id` and pre-run anchor digest/reference;
- digest/root of the ordered run record;
- immutable references for the closure artifact and material observable actions;
- whether any post-start human inputs occurred;
- whether any escalation occurred;
- the final repository/result revision where applicable;
- the attestation signature/verification material.

A reviewer MUST be able to verify that the final attestation is cryptographically or independently bound to the same execution identity/trust chain declared before work began.

## Binding executor/session to observable actions

A GitHub action attributed to the contributor's human account can still be used when the execution runtime acts through the contributor's connector or credentials, but GitHub attribution alone is not the ownership witness.

Each decisive observable action counted as executor-owned MUST be bound to the run by at least one of these patterns:

1. **Execution identity binding.** The action is performed by a dedicated bot/App/agent identity whose credential custody is part of the accepted execution trust basis, and the action is linked to the declared `run_id`.
2. **Signed session binding.** The execution boundary attests an action/result record containing the `run_id`, action type, content/payload digest where relevant, and immutable result identifier such as commit SHA, issue-comment ID/URL, PR number/URL, or comparable primary reference.
3. **Stronger equivalent.** Another primary mechanism provides at least the same separation between contributor identity and execution ownership and is independently reviewable.

A plain commit, PR, GitHub Actions run, scheduler record, or runtime/model label does not satisfy this binding by itself.

## Human input after start

Pre-start human constraints are allowed and should be frozen in or referenced by the pre-run anchor.

After the run starts, human input is acceptable only when it remains observable in the provenance record. The reviewer must be able to distinguish support/escalation from hidden step-by-step control.

### Legitimate escalation

A post-start human response can remain compatible with autonomous S1 ownership when all of the following are visible in order:

1. the executor records an escalation before the human response;
2. the escalation identifies the specific decision that exceeds the declared S1 authority or available evidence;
3. the human response is captured in the same auditable input channel;
4. the response resolves only the escalated boundary decision or supplies explicitly requested external information/authority;
5. ordinary in-boundary implementation/research/repair choices after the response remain executor-owned.

The escalated decision itself is not reclassified as executor-owned merely because the executor requested it.

### Hidden step-by-step control

Treat ownership as **insufficient** for the affected run when a human post-start input selects or dictates an ordinary decision that the pre-run contract assigned to S1, for example choosing which in-boundary file to edit, exact implementation wording, which ordinary repair to try, or whether to repeat a routine validation check.

Also treat the witness as insufficient when a decision-relevant human input channel exists but is not covered by the provenance capture boundary. A claim that no hidden input occurred is retrospective self-report unless the accepted attester/trust basis provides the capture guarantee.

A human emergency stop may terminate a run, but an aborted run does not become positive autonomy evidence merely because its provenance is valid.

## Dedicated bot identity vs signed session attestation

### Dedicated agent/bot identity

A dedicated GitHub App/bot identity has a useful property: observable repository actions are directly separated from the contributor's normal GitHub identity.

It is **not sufficient by identity alone**. If a human can freely wield the bot credential, or the same bot identity is not bound to the declared run, the reviewer still cannot distinguish autonomous execution from manual operation.

It becomes a conforming witness when the accepted trust basis establishes execution-bound credential custody for the run, the pre-run anchor binds the bot identity to `run_id`, and post-start human inputs are accounted for.

### Signed runtime/session attestation

A signed session witness allows the executor to operate through ordinary contributor-owned GitHub transport while a separate execution-bound signer attests which actions and inputs belong to the run.

This is the baseline design for this repository because it does not require one GitHub identity model or execution vendor. Its trust cost is explicit: the reviewer must trust evidence that the signing key/attester is isolated from ordinary human control during the run and that decision-relevant human inputs are completely captured.

A combined bot identity + signed session attestation is stronger but is not required by this contract.

## Trust assumptions

Cryptography proves integrity and key possession; it does not by itself prove autonomous decision ownership. A positive trial therefore depends on an explicit accepted trust basis for the attester.

At minimum, the reviewer must be able to evaluate these assumptions:

- **key/credential custody:** the contributor cannot use the executor's signing/action credential to fabricate executor events during the run under the declared trust model;
- **run binding:** the attester cannot silently reuse unrelated events under the same `run_id`;
- **input capture completeness:** every decision-relevant post-start human input channel available to the executor is covered by the provenance record;
- **action integrity:** action/result identifiers and payload digests correspond to the observable primary artifacts they claim to bind;
- **record integrity:** event omission/reordering after capture is detectable;
- **verification availability:** a second reviewer can obtain the public verification material and verification procedure without private operator state.

The repository does not mandate one vendor, hardware root, signature algorithm, or GitHub App design. Maintainer policy decides which concrete attester roots/custody models are trusted for a positive M0 trial.

## Reject / insufficient cases

A reviewer MUST NOT treat executor ownership as established when any of the following is true:

- the only executor signal is the contributor's GitHub identity;
- the evidence is only a runtime/model name, scheduler, GitHub Actions run, PR, or retrospective narrative;
- the attestation has no pre-run anchor;
- the signature verifies but there is no accepted trust basis separating the signer from ordinary human control;
- decisive actions are not bound to the declared `run_id` by immutable references/digests;
- post-start decision-relevant human inputs are missing, unverifiable, or can arrive through an unobserved channel;
- a human response dictates an ordinary in-boundary S1 decision rather than resolving a genuine escalation boundary;
- the final attestation does not bind the run record and closure artifact;
- required verification material is unavailable to the second reviewer.

Use `FAIL / INSUFFICIENT` rather than inferring ownership from missing evidence.

## Next M0 instrumented trial

A new trial using this contract should, before edits:

1. freeze the normal #16-style work envelope;
2. create and publish the pre-run provenance anchor;
3. verify the anchor signature/trust material before ordinary work begins;
4. execute the bounded S1 work while capturing material events and all post-start human inputs;
5. publish/retain immutable action bindings and the final attestation;
6. have a second reviewer verify signatures, event ordering, action references, human-input accounting, and trust assumptions;
7. only then evaluate the ordinary Profile/Methodology sequence: function → decisive decision right → owner → supporting machinery → closure.

Passing provenance verification is necessary evidence for the owner claim in this trial design, not a standalone proof that the full `S1=A` state exists.

A machine-readable starting point is provided in [`provenance/executor-witness-v1.template.json`](provenance/executor-witness-v1.template.json). Implementations may serialize or transport equivalent evidence differently if the reviewer can verify the same fields and bindings.

## Maintainer policy choice

This contract deliberately leaves one substantive policy decision outside #19: **which attester roots and credential/key-custody models are acceptable trust anchors for a positive M0 trial**.

Examples may include a dedicated GitHub App whose token is only exposed inside the executor boundary, a managed runtime that emits verifiable session provenance, a hardware-backed/local harness signer with independently reviewable custody, or another mechanism with equivalent guarantees.

Choosing that trust set is a maintainer risk/policy decision. It must not be smuggled into the definition of `A`, and it does not create S2/S3/S3*/S4/S5.
