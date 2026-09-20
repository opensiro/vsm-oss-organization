# Complementary S3* audit constructor contract

This document defines the repository-local first-party construction surface for complementary S3* audit during M1.

It applies the selected VSM Harness Profile and Methodology through `UPSTREAM_CONTRACT.json`; it does **not** redefine S3*, autonomy states, or assessment semantics.

The active formal roadmap milestone is M1. Its S3* target is constructor state `C`, not autonomous state `A`.

Under the selected Methodology, `C` means the VSM function is established and a first-party primitive specifically exposes the relevant decisive decision or feedback path, while the autonomous actor, authority, independence, or closure loop may still require downstream composition.

## Purpose

S3* exists when routine S1/S3 reporting is insufficient for a material claim or risk and the organization needs materially complementary access to operational reality.

The M1 constructor path has this shape:

```text
S1 contribution / closure claim
        ↓ ordinary reporting
PR description / run record / ordinary checks

operational reality
        ↓ materially complementary access
raw diff / pinned evidence / replay / independent inspection
        ↓
first-party S3* audit surface
        ↓ composed audit judgment
PASS / FINDING / INSUFFICIENT
        ↓ finding when present
current-control destination
```

The constructor surface exposes the S3*-specific path. It does not require a permanently running verifier or an autonomous audit owner.

## M1 constructor threshold

For `S3*=C`, establish all of the following:

1. **Function** — a real claim/risk exists for which routine reporting is insufficient and complementary access is organizationally relevant.
2. **Ordinary reporting path** — the evidence/checks already supplied by the producing S1/S3 path are explicit.
3. **Complementary access path** — the constructor exposes materially different access capable of challenging the ordinary claim.
4. **S3*-specific judgment surface** — the first-party path represents the audited claim/risk, evidence boundary, judgment, and one of the local outcomes `PASS`, `FINDING`, or `INSUFFICIENT`.
5. **Feedback destination** — a material finding has an explicit path toward subsequent current control rather than ending as an isolated report.
6. **Ownership separation** — the actual audit judgment owner is recorded separately from evidence collectors, deterministic validators, transport, and downstream S3 control.
7. **Boundary reachability** — the constructor path is part of the declared Organization operating surface, not merely an adjacent example or generic extension point.

An autonomous verifier is **not** an M1 requirement. A future `S3*=A` claim would additionally require an autonomous agent to own the decisive audit judgment through an operationally closed first-party mode under the governing Methodology.

## Existing functional witness

Issue #44 / PR #45 exercised the complementary audit topology on real repository work and closed with an evidence-backed `PASS`.

That run demonstrated:

- a concrete audited claim/risk;
- an ordinary S1 reporting path;
- a materially complementary evidence path using raw/canonical repository evidence;
- a reviewable audit judgment and outcome;
- no manufactured finding merely to exercise downstream control.

For M1 this is evidence that the S3* function and constructor path are real. It is **not** an `S3*=A` claim.

## Admission of an audit

Do not audit merely because an auditor role or review tool exists. Before execution, establish:

1. **System-in-focus** — which contribution/system boundary is being audited?
2. **Audited claim or risk** — what concrete S1 assertion, omission risk, evidence risk, or closure claim is under review?
3. **Ordinary reporting path** — what evidence/checks does S1 already provide?
4. **Complementary access** — what materially different access to operational reality is available?
5. **Independence rationale** — why can that access challenge the ordinary path for this claim?
6. **Judgment owner** — who exercises the audit judgment in this concrete run?
7. **Control destination** — where can a material finding enter subsequent current control?
8. **Closure expectation** — what records the result and any downstream handoff?

If the only available path repeats the ordinary S1 check without materially different access, it is not a qualifying S3* path.

## Claim-relative independence

Independence is claim-relative and belongs to the evidence path first.

The auditor does not need a completely isolated technology stack. Shared infrastructure, model family, repository host, or deterministic validators do not automatically defeat complementary access. Conversely, using a second model does not automatically establish S3*.

The relevant question is:

> Can this audit challenge the specific S1 claim using evidence or access that is materially different from the producing S1's ordinary reporting path?

Examples that may qualify when material to the claim:

- inspect the complete raw diff instead of trusting a summarized change list;
- inspect pinned primary repository evidence instead of trusting cited prose;
- reconstruct a generated artifact from canonical inputs rather than trusting the produced artifact;
- compare declared scope against independent repository/source-of-truth surfaces;
- replay a result from immutable refs;
- sample evidence not selected solely by S1;
- perform an adversarial or counterexample-oriented check over the claimed closure.

Examples that do not qualify by themselves:

- rerunning the same unit test that S1 already used;
- reading the same PR description and restating it;
- assigning a component named `verifier` or `auditor`;
- using another model with no complementary evidence path;
- treating CI success as an audit judgment;
- exposing only a generic hook/callback from which a developer could someday build an audit function.

## Audit record

Each material audit SHOULD preserve:

- audited work item and revisions;
- exact claim/risk;
- ordinary S1 evidence path;
- complementary evidence path;
- independence rationale;
- primary evidence references;
- observable audit judgment;
- judgment owner;
- support/enforcement mechanisms separately;
- downstream control destination for a finding;
- closure/result references.

Use `templates/s3star-audit-record.md` as the default record surface.

## Operational findings

Use the following local record states:

- `PASS` — the complementary evidence did not establish a material contradiction/gap for the audited claim;
- `FINDING` — the audit established a material issue that should enter a current-control path;
- `INSUFFICIENT` — the available evidence/access cannot support a reliable audit judgment.

These are local audit outcomes, **not** VSM autonomy states and not assessment publication notation.

A `PASS` does not prove the entire contribution correct; it closes only the declared audited claim/risk.

## Feedback and closure

A material `FINDING` SHOULD identify a downstream current-control destination, including the M1 S3 constructor surface when the finding requires whole-system current regulation.

```text
finding
  ↓
current-control destination
  ↓
accepted / rejected / escalated / insufficient authority
  ↓
subsequent operation may change
```

For `S3*=C`, the constructor must expose this feedback path; the full autonomous closure loop may still require composition. S3* does not own the later S3 decision merely because its finding triggered that decision.

## Ownership boundary

The audit judgment owner is whichever actor exercises the discretionary judgment over the complementary evidence in the concrete run.

That actor may be human, agent, or another explicitly composed participant. M1 records the owner honestly but does not require autonomous ownership.

Evidence collectors, repository APIs, test runners, deterministic scripts, validators, parsers, queues, issue comments, and control-surface transport are supporting machinery unless they themselves exercise the decisive audit judgment.

## Non-goals

This contract does not:

- establish `S3*=A`;
- require a permanently running verifier;
- require an independent second agent;
- create an autonomous S3 regulator;
- classify ordinary tests/logging/tracing as S3* by default;
- require every S1 work item to receive the same audit;
- define an algedonic severity protocol;
- require a second model/provider;
- introduce S2, S4, or S5;
- require hidden chain-of-thought.

## Reference artifacts

- role/composition guidance: `roles/S3STAR.md`;
- portable prompt: `prompts/audit-s1-work.md`;
- record template: `templates/s3star-audit-record.md`;
- constructor work: #37 / #40;
- real functional witness: #44 / PR #45;
- downstream S3 constructor: #38;
- M1 current-control trial: #39.
