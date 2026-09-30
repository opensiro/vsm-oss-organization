# Parent-governed S5 boundary contract

This document defines the first-party Organization surface for composing a parent-governed S5 identity / ultimate-policy decision during preparatory M2 work.

It applies the selected VSM Harness Profile and Methodology through `UPSTREAM_CONTRACT.json`; it does **not** redefine S5, parent mode `P`, recursion, or autonomy semantics.

The active formal roadmap milestone remains M1 until its exit conditions are satisfied. The existence of this contract therefore does **not** establish `S5=P` or complete M2 by itself.

## Purpose

Use this path only when a matter is genuinely about the identity, purpose, ultimate policy, legitimate authority, declared system boundary, or delegation model of the bounded OpenSiro VSM Harness OSS organization.

Reference flow:

```text
ordinary Organization operation
        ↓
identity / ultimate-policy exception
        ↓ leaves delegated local envelope
legitimate parent authority
        ↓ authoritative decision
returned policy / identity decision
        ↓
Organization acknowledgement / application
        ↓
subsequent operation governed by returned decision
```

The contract records and transports the parent decision. It does not make every human decision S5 and it does not prove that any particular actor is the legitimate parent merely because that actor can merge, administer, or configure repositories.

## System-in-focus

The relevant recursion for this contract is the bounded **OpenSiro VSM Harness OSS organization** declared by `README.md` and `ORGANIZATION.md`.

The current scope includes:

- `opensiro/vsm-harness-profile` as normative semantic authority consumed by the organization;
- `opensiro/vsm-harness-skills` as an operational S1 domain for assessment procedure/skills/tooling;
- `opensiro/vsm-harness-index` as an operational S1 domain for the canonical evidence-backed corpus;
- `opensiro/awesome-vsm-harness` as an operational S1 domain for curated downstream views;
- `opensiro/vsm-oss-organization` as the organizational/metasystem construction surface.

Changing that declared scope is itself a candidate S5 matter because it changes the system boundary at this recursion.

## Delegated local envelope

The following remain outside S5 when they can be closed under an already-delegated lower-level authority:

- ordinary bounded Index, Skills, or Awesome S1 work;
- local implementation, validation, repair, reassessment, curation, and recovery inside an S1 domain contract;
- complementary S3* audit judgment over an admitted claim/risk;
- whole-system S3 current-control decisions that remain inside an already-selected identity/policy envelope;
- ordinary repository maintenance, PR discussion, CI repair, task assignment, scheduling, routing, or merge mechanics;
- routine use of an already-admitted external capability inside its delegated scope.

A human or parent participating in one of those activities does not turn the matter into S5.

## Reserved S5 matters

A matter should leave the delegated envelope when the decisive right is genuinely identity / ultimate-policy level at this recursion. Candidate classes include:

- changing the declared system-in-focus or repository participation boundary;
- changing the organization's purpose or viable-system identity;
- changing which authority is ultimate for organizational policy at this recursion;
- changing the delegated autonomy envelope itself;
- changing the relationship between this Organization and its normative semantic authority rather than merely consuming an already-selected compatible release;
- deciding whether an entire consequential external capability class is permitted or forbidden as organizational policy, rather than configuring one ordinary use;
- terminating, merging, splitting, or fundamentally redefining the bounded organization.

These are candidate classes, not automatic labels. Map the actual function first.

## Legitimate parent

A positive parent-governed S5 case requires a reconstructable **legitimate parent role and concrete decision owner**.

For each case record:

1. the parent role that holds ultimate authority for the matter at this recursion;
2. the concrete actor or explicitly evidenced distributed arrangement exercising that role;
3. primary evidence showing why that actor/arrangement legitimately holds the decisive right;
4. the exact decision right reserved to that parent;
5. any limits on that authority relevant to the case.

Repository authorship, maintainer status, merge capability, administrator permissions, tool ownership, or possession of credentials are not sufficient by themselves to prove legitimate S5 parenthood.

If legitimate parent ownership cannot be reconstructed, record the case as insufficient for `S5=P` rather than inferring authority from access.

## Escalation admission

Before using this path, establish:

1. **Matter** — what concrete question requires a decision?
2. **S5 rationale** — why does the matter concern identity / ultimate policy rather than ordinary S1, S3, or S3* authority?
3. **Current delegated envelope** — what lower-level decisions are already allowed and why can they not close this matter?
4. **Decisive right** — what exact organizational choice must be made?
5. **Legitimate parent** — which role and concrete owner may make that choice?
6. **Evidence** — what primary sources establish the matter and parent legitimacy?
7. **Return targets** — which Organization artifacts, constraints, roles, or operating paths must consume the decision?
8. **Closure expectation** — what observable subsequent behavior would demonstrate that the returned decision governs operation?

If the matter can be safely closed inside an already-delegated S1/S3/S3* envelope, do not escalate it as S5.

## Parent decision record

Use `templates/s5-parent-decision-record.md` as the default reviewable record.

A material record SHOULD preserve:

- work item / decision id and governing revisions;
- system-in-focus;
- exact identity / ultimate-policy matter;
- S5 classification rationale;
- lower-level authority considered and why it is insufficient;
- legitimate parent role;
- concrete decision owner;
- parent-legitimacy evidence;
- decisive right;
- considered options where material;
- authoritative decision;
- returned constraint / policy / identity statement;
- support/transport/enforcement mechanisms separately;
- Organization return targets;
- acknowledgement/application evidence;
- observable effect or intentional preservation;
- final closure state and references.

The record is evidence/transport. It is not the owner of the decision.

## Local lifecycle states

The following repository-local states may be used in records:

- `ESCALATED` — a qualifying S5 matter has left the local delegated envelope;
- `DECIDED` — the legitimate parent has returned an authoritative decision;
- `APPLIED` — the Organization has acknowledged/applied the returned decision;
- `CLOSED` — the resulting governance of subsequent operation is reviewable;
- `INSUFFICIENT_AUTHORITY` — parent legitimacy or decisive authority cannot be established;
- `CANCELLED` — the matter ceased to require a parent decision before a decisive choice was made.

These are local workflow states, not VSM autonomy symbols.

## Return and closure

A parent decision establishes a useful S5 loop only when it returns into the Organization and governs later operation.

A qualifying return identifies:

- the returned policy / identity constraint;
- affected Organization artifacts or operating paths;
- acknowledgement by the affected path;
- whether application changed, stopped, constrained, admitted, excluded, or intentionally preserved subsequent behavior;
- primary evidence for closure.

An external opinion, chat answer, approval button, or merge without a reconstructable identity/policy matter and return effect is not sufficient.

## Support and enforcement boundary

The following may support, transport, or enforce a parent decision without owning S5:

- GitHub issues and pull requests;
- branch rules and rulesets;
- repository permissions;
- plugins/connectors and API scopes;
- CI workflows and validators;
- labels, project fields, queues, and schedulers;
- policy/configuration files;
- deterministic checks or deployment gates.

Classify ownership from the decisive organizational judgment, not from the mechanism with the strongest technical enforcement power.

## Historical candidate: routing scope correction

Issue #59 / PR #62 is a strong historical **functional candidate** for this topology:

```text
routing implementation widened governed population to all public OpenSiro repositories
        ↓
system-boundary problem identified
        ↓
scope restored to the five declared repositories
        ↓
routing oracle / conformance / trial population changed
        ↓
earlier all-public routing evidence superseded
```

This demonstrates an identity/boundary-level matter and a concrete return into subsequent Organization behavior.

It must **not** be credited as formal `S5=P` solely from authorship or merge history. A positive historical classification additionally requires primary evidence that the concrete decision owner was the legitimate parent for that scope right at this recursion. If that cannot be reconstructed, retain the case as functional/history evidence and use the next natural post-contract S5 matter for the positive witness.

## Relationship to M2 supporting work

- #81 owns the parent-authority / first-witness track.
- #82 owns this implementation.
- #36 may define how external tools enter an already-selected delegated policy envelope.
- #29 may map an already-selected authority model into GitHub branch enforcement.

Neither #36 nor #29 establishes S5 merely by adding permissions or restrictions.

## Non-goals

This contract does not:

- claim `S5=P` before a real operationally closed parent case exists;
- make ordinary human approval S5;
- make tool installation or permission prompts S5 by default;
- infer legitimate parenthood from GitHub access alone;
- create an autonomous S5 owner;
- promote S3 or S3* to `A`;
- introduce S2 or S4;
- redefine VSM semantics owned by the Profile.
