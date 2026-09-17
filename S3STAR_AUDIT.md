# Complementary S3* audit contract

This document defines the repository-local operational contract for a complementary S3* audit path used in preparatory M1 work.

It applies the selected VSM Harness Profile and Methodology through `UPSTREAM_CONTRACT.json`; it does **not** redefine S3*, autonomy states, or assessment semantics.

The active roadmap milestone remains M0 until its proof debt is resolved. The existence of this document therefore does **not** establish `S3*=A` or complete M1.

## Purpose

The path exists for claims where ordinary S1 reporting and deterministic completion checks are not enough to establish confidence.

A qualifying audit has this shape:

```text
S1 contribution / closure claim
        ↓ ordinary reporting
PR description / run record / ordinary checks

operational reality
        ↓ materially complementary access
raw diff / pinned evidence / replay / independent inspection
        ↓
S3* audit judgment
        ↓
finding enters a current-control destination
```

The audit function is the independent judgment over complementary evidence. Tools that fetch evidence, rerun checks, parse results, or transport the finding are supporting machinery unless they actually own that judgment.

## Admission of an audit

Do not audit merely because an auditor role exists. Before execution, establish:

1. **System-in-focus** — which contribution/system boundary is being audited?
2. **Audited claim or risk** — what concrete S1 assertion, omission risk, evidence risk, or closure claim is under review?
3. **Ordinary reporting path** — what evidence/checks does S1 already provide?
4. **Complementary access** — what materially different access to operational reality is available?
5. **Independence rationale** — why is that access not controlled solely by the producing S1 for this claim?
6. **Audit owner** — who exercises the audit judgment?
7. **Control destination** — where can a material finding enter subsequent current control?
8. **Closure expectation** — what evidence shows the finding was accepted, rejected, escalated, or otherwise entered a reviewable control path?

If the only available path repeats the ordinary S1 check without adding materially different access, record that the proposed audit is not a qualifying S3* path.

## Claim-relative independence

Independence is claim-relative.

The auditor does not need a completely isolated technology stack. Shared infrastructure, model family, repository host, or deterministic validators do not automatically defeat independence. Conversely, using a different model does not automatically establish it.

The relevant question is:

> Can the audit path challenge the specific S1 claim using evidence or access that the producing S1 does not solely control through its ordinary reporting path?

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
- treating CI success as an audit judgment.

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
- finding severity only when operationally needed;
- downstream control destination;
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

A finding is not a closed organizational function merely because it was written down.

A material `FINDING` SHOULD identify a downstream current-control destination, for example the M1 S3 constructor surface defined by #38 once available.

Audit closure records what happened to the finding:

```text
finding
  ↓
current-control destination
  ↓
accepted / rejected / escalated / insufficient authority
  ↓
subsequent S1 operation changes or remains unchanged with evidence
```

S3* does not own the later S3 decision merely because its finding triggered that decision.

## Human intervention

Human input to the audit is permitted but must be attributed when it affects the judgment or evidence boundary.

If a human supplies the decisive audit conclusion, that conclusion is human-owned for evidence purposes. Do not count it as agent-owned S3* judgment.

## Ownership and proof debt

The intended M1 reference setup eventually requires an agent-owned audit judgment for `S3*=A`.

However, role text, model labels, ChatGPT execution, issue comments, or successful audit artifacts do not by themselves prove the owner. The executor-identity proof debt tracked in #2/#35 remains applicable to formal autonomy claims.

Until stronger provenance is available, preparatory M1 work may establish the functional path, evidence boundary, and closure topology without promoting the autonomy state.

## Non-goals

This contract does not:

- create an autonomous S3 regulator;
- classify ordinary tests/logging/tracing as S3* by default;
- require every S1 work item to receive the same audit;
- define an algedonic severity protocol;
- require a second model/provider;
- introduce S2, S4, or S5;
- require hidden chain-of-thought.

## Reference artifacts

- role: `roles/S3STAR.md`;
- portable prompt: `prompts/audit-s1-work.md`;
- record template: `templates/s3star-audit-record.md`;
- parent work: #37 / #40;
- downstream constructor work: #38;
- end-to-end trial: #39.
