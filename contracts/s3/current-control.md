# S3 current-control constructor contract

This contract defines the first-party Organization path for carrying a bounded **inside-and-now, whole-system current-control decision** into subsequent S1 operation.

It applies the selected Profile and Methodology through [`../../UPSTREAM_CONTRACT.json`](../../UPSTREAM_CONTRACT.json). It does not redefine S3 or the Methodology state `C`.

The presence of this contract does **not** establish `S3=C` or `S3=A`. A positive mapping still requires a real S3 function at the declared boundary and reviewable closure.

## Admission

Use this path only for a **real present-tense whole-system current-control choice** that exceeds ordinary local S1 decision authority and regulates the declared system's existing operations. A prospective allocation, priority, commitment, resource, or shared-constraint decision can qualify, as can a material current exception or S3* finding. An emergency, failed S1, contributor-count threshold, or overloaded maintainer is **not** a prerequisite. A mere task assignment, generic scheduling decision, or milestone declaration is not sufficient.

A qualifying transaction establishes:

1. system-in-focus;
2. actual current operational need / trigger (including an exception when present);
3. relevant whole-system present-state context;
4. decisive current-control right;
5. allowed bounded response classes;
6. actual decision owner;
7. support/enforcement separately;
8. affected S1 return target(s);
9. closure evidence.

Ordinary local repair remains S1; ordinary inter-S1 conflict attenuation without a whole-system control choice remains S2. Identity/ultimate-policy matters leave this contract for the S5 boundary. A planned M1 trial may select existing S1 work and a real current organizational choice; it must not create a synthetic conflict, arbitrary constraint, or meaningless intervention solely to claim `S3=C`.

## Milestone selection versus functional evidence

M1 may deliberately schedule a **bounded reference trial before organizational load demands regular S3 operation**. The trial must still freeze genuine active S1 commitments, relevant whole-system state, the actual S3 decision right and owner, a real choice with operational consequences, and the return target before the decision. The transaction is evidence only after the returned instruction has been acknowledged/applied (or explicitly rejected/escalated), with an observable effect or justified preservation of subsequent operation. If no substantive current-control choice exists, do not stage a dummy transaction or promote the autonomy grade.

The frozen [2026-09-30 general pre-assessment](../../records/assessment-snapshots/2026-09-30-general-preassessment.md) remains a non-canonical source-pinned review; its provisional `S3=?` is not retroactively upgraded by revising this contract. Reassessment of future positive claims remains governed by Profile/Methodology, not by the milestone schedule.

## Decision classes

When functionally justified, local response classes may include:

- `CONTINUE`;
- `STOP`;
- `REQUIRE_REPAIR`;
- `SET_CONSTRAINT`;
- `SET_RETRY_BUDGET`;
- `OTHER_CURRENT_CONTROL` with explicit justification.

The class name never establishes S3 by itself.

## Ownership

A transaction MUST separate:

```text
S3 function
  ↓
decisive current-control right
  ↓ owned by an identified actor
first-party constructor / transport
  ↓
support / enforcement
  ↓
returned decision
  ↓
S1 acknowledgement / application
  ↓
observable closure
```

During M1 the decision owner may be human, parent, external actor, or another explicitly composed owner. The contract does not invent a permanent S3 agent. A later `S3=A` claim requires autonomous ownership under the M3 evidence conditions.

## Transaction surface

Use [`../../control/s3-current-control-v1.template.json`](../../control/s3-current-control-v1.template.json) as the machine-readable starting shape and [`../../templates/s3-control-record.md`](../../templates/s3-control-record.md) for the reviewable record.

Lifecycle states are `REQUESTED`, `DECIDED`, `APPLIED`, `CLOSED`, `ESCALATED`, and `CANCELLED`. They are operational states, not autonomy grades.

## S1 return

A returned decision affects S1 only when the transaction identifies the affected work, records the decision owner, stays within the admitted current-control envelope, and supplies a bounded instruction that S1 can acknowledge/apply or explicitly reject/escalate.

The S1-side adapter is [`../../roles/S1.md`](../../roles/S1.md). Arbitrary comments, approvals, labels, chat messages, scheduler states, and CI failures do not become S3 input merely because S1 can see them.

## S3* relation

A material S3* finding may trigger this contract, but audit and current-control ownership remain distinct. The complementary-audit contract is [`../s3star/audit.md`](../s3star/audit.md).

## Current evidence boundary

The constructor is implemented, but issue #39 remains the missing real-use witness for `S3=C`: one qualifying present-tense whole-system current-control choice, relevant current view, explicit owner, returned decision, S1 application, and observable closure must occur in one reconstructable transaction. The reference trial may be scheduled under M1 rather than waiting for an incident; scheduling is not the witness.

The actor adapter is [`../../roles/S3.md`](../../roles/S3.md). It must not be treated as evidence that the function already exists.
