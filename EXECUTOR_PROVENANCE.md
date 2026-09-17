# Executor provenance witness

This document defines the repository-local evidence contract for binding a bounded S1 run to the actors that exercised its material decision rights.

It applies the VSM Harness Profile and Methodology; it does not redefine S1 or autonomy. A runtime, scheduler, GitHub identity, signature, transport mechanism, or human intervention does not become the owner of an organizational function merely because it records, constrains, or affects an action.

The contract is intentionally runtime-neutral. ChatGPT, Codex, Claude Code, custom harnesses, local schedulers, dedicated GitHub Apps/bots, and other execution technologies may conform if they produce the required primary evidence.

A conforming witness makes an instrumented M0 trial reviewable. It does **not** require an unrealistically pure run with zero human contact. Human control or intervention is allowed; it must be visible and attributed to the human rather than silently counted as agent-owned discretion.

## Problem being closed

Instrumented trial #16 closed its bounded contribution as PR #17, but repository-only GitHub evidence exposed only the contributor's authenticated identity. A second reviewer could reconstruct the work but could not independently bind material choices to the autonomous executor/session rather than to the human contributor.

The missing evidence is therefore an attribution chain:

```text
pre-run executor/session anchor
        ↓
observable run events
(agent decisions + support + escalation + human intervention)
        ↓
immutable action/result references
        ↓
final attestation / reviewable run record
```

No hidden chain-of-thought is required or desired.

## Minimum witness

A positive executor-provenance witness MUST contain three linked parts.

### 1. Pre-run anchor

Before ordinary contribution work begins, preserve primary evidence of:

- witness format/version;
- unique `run_id`;
- system-in-focus and repository boundary;
- bounded work-item reference;
- frozen repository start revision;
- exact governing role/prompt revision or content digest;
- executor/session attester identity;
- verification material and attestation format;
- declared trust basis for the evidence source;
- pre-start human constraints reference or digest;
- the channels through which post-start human input or intervention may reach the run.

The anchor SHOULD be immutable or independently timestamped before material execution begins. A runtime/model name or retrospective narrative alone is not sufficient.

### 2. Ordered run record

The run record MUST preserve an ordered, tamper-evident or otherwise independently reviewable record of organizationally material events. Each event should record observable facts only, for example:

- event sequence/id and type;
- actor class (`executor`, `human`, or `support`);
- concise decision/input/action/intervention summary;
- evidence available at that moment by reference, where material;
- authority classification (`inside_s1`, `outside_s1_escalation`, `human_intervention`, or `support_only`);
- immutable action/result reference where an observable external action occurred;
- payload/content digest where useful;
- ordering or predecessor binding sufficient to detect material omission/reordering under the declared trust model.

The record MUST include material post-start human inputs and interventions that affect the run. It MAY omit purely mechanical metadata that cannot affect organizational decisions.

The witness does not need private reasoning. Record the observable choice, evidence reference, action, actor, and authority boundary.

### 3. Final attestation / closure record

At run closure, preserve evidence binding:

- `run_id` and pre-run anchor reference;
- the ordered run record or its digest/root;
- closure artifact and material action references;
- whether human input or intervention occurred;
- whether escalation occurred;
- the final repository/result revision where applicable;
- verification material needed by a second reviewer.

## Binding actors to observable decisions

A GitHub action attributed to the contributor's account may still be transported by an autonomous runtime. GitHub attribution alone therefore does not establish organizational ownership.

A material decision counted as executor-owned SHOULD be bound to the run through at least one independently reviewable pattern:

1. **Execution identity binding.** A dedicated agent/bot/App identity is bound to the declared run.
2. **Session/run attestation.** A runtime/session record binds the run, decision/action summary, and immutable result identifiers.
3. **Reviewable transcript/event-log binding.** An immutable or independently verifiable execution record shows the actor and material event sequence.
4. **Stronger equivalent.** Another mechanism gives a second reviewer comparable actor attribution.

The repository does not mandate one vendor, signer, credential model, or transport.

## Human input and intervention

Human involvement is not automatically a failure of viability or autonomy. Real viable systems are expected to encounter disturbances, exceptions, overrides, and interventions.

The requirement is **attribution, not purity**:

```text
human intervention occurs
        ↓
record it as human-owned intervention
        ↓
record what decision/right it affected
        ↓
continue, stop, or re-establish the authority envelope
        ↓
review whether the decisive S1 loop remained agent-owned
```

### Escalation response

A human response to an executor-initiated escalation is compatible with an autonomous S1 arrangement when the record shows:

1. the executor identified a decision outside its current authority/evidence;
2. the escalation preceded the response;
3. the human response is attributed to the human;
4. the response resolves the external decision or supplies requested information/authority;
5. subsequent in-boundary discretion is again exercised by the S1 where applicable.

The escalated decision remains human/parent-owned; it is not reclassified as executor-owned.

### Human intervention inside the S1 envelope

A human MAY intervene in an ordinary in-boundary decision. The run does not become invalid merely because that happened.

When this occurs:

- record the intervention as a material human-owned event;
- identify which local decision/right was overridden, selected, or constrained;
- do not count that specific decision as agent-owned evidence;
- record whether the S1 resumed autonomous operation afterward;
- record whether the intervention changed the work boundary, governing contract, or authority envelope.

An isolated or exceptional intervention does not automatically erase evidence that the S1 normally owns the relevant local discretion. Conversely, if ordinary decisive decisions are routinely selected by the human as part of the standard operating path, that is evidence that the right may actually be human-owned rather than agent-owned.

For an M0 reference trial, a reviewer should ask whether the **decisive organizational loop used as evidence for `S1=A`** was closed by the agent. If human intervention supplied that decisive closure, the run may still be a valid operational run, but it is not sufficient by itself as positive evidence for agent ownership of that loop.

### Unobserved human control

The actual failure mode is not intervention; it is **unattributable intervention**.

Treat ownership evidence as insufficient when a material human input/intervention could affect the run but is absent from the declared evidence boundary, or when the reviewer cannot determine who exercised the relevant decisive right.

A human emergency stop, correction, override, or rescue should therefore be reported rather than hidden. Such events are useful evidence about residual variety and where the organization still loses autonomy or requires stronger regulation.

## Trust assumptions

A provenance mechanism proves only what its declared trust model supports. A second reviewer should be able to evaluate:

- **actor attribution:** material executor and human events can be distinguished;
- **run binding:** evidence belongs to the declared run;
- **input/intervention capture:** material human interventions are represented;
- **action integrity:** references correspond to the observable artifacts they claim to bind;
- **record integrity:** material omission or reordering is detectable to the extent claimed;
- **verification availability:** the reviewer can inspect the evidence without private operator state.

Cryptography or isolated credentials may strengthen these properties but are not themselves organizational owners and are not the only conforming implementation family.

## Reject / insufficient cases

A reviewer MUST NOT treat executor ownership as established when:

- the only evidence is the contributor's GitHub identity;
- the only executor signal is a runtime/model name, scheduler, CI run, PR, or retrospective assertion;
- material decisions cannot be bound to a declared run/actor;
- a material human intervention occurred but is not attributable in the record;
- the decisive closure used to claim agent ownership was actually selected by the human and no independent agent-owned decisive loop remains;
- required verification material is unavailable to the second reviewer.

Use `FAIL / INSUFFICIENT` for the **ownership claim that lacks evidence**, not as a blanket label for every run that contains human intervention.

## Next M0 instrumented trial

A new trial should:

1. freeze the bounded work envelope and start revision;
2. publish the pre-run provenance anchor;
3. execute the work while capturing material executor decisions, support events, escalations, and human interventions;
4. bind material actions to immutable repository artifacts;
5. preserve the final closure record;
6. have a second reviewer verify actor attribution, event ordering, interventions, action references, and closure;
7. evaluate the normal Profile/Methodology sequence: function → decisive decision right → owner → supporting machinery → closure.

A provenance PASS means the reviewer can reconstruct who exercised the relevant rights. It does not mean the run was intervention-free and is not by itself an `S1=A` verdict.

A machine-readable starting point is provided in [`provenance/executor-witness-v1.template.json`](provenance/executor-witness-v1.template.json).

## Operational interpretation

The organization should not optimize for a fictional zero-intervention world. It should make intervention visible and then reduce avoidable intervention and associated loss over repeated operation.

Useful operational observations include:

- intervention count and rate;
- intervention reason/category;
- which decision right was affected;
- whether work resumed autonomously;
- whether intervention prevented or reduced an observed loss;
- whether the same class of intervention recurs.

These are operational improvement signals, not new VSM autonomy states and not automatic evidence of S2/S3/S3*/S4/S5.