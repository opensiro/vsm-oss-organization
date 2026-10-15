# S3 current-control constructor contract

This contract defines the first-party Organization path for carrying a bounded **inside-and-now, whole-system current-control decision** into subsequent S1 operation.

It applies the selected Profile and Methodology through [`../../UPSTREAM_CONTRACT.json`](../../UPSTREAM_CONTRACT.json). It does not redefine S3 or the Methodology state `C`.

The presence of this contract does **not** establish `S3=C` or `S3=A`. Under the selected Skills Methodology, `C` still requires an **established S3 function** and a boundary-reachable, S3-specific decisive decision/feedback construction path; a developer may yet need to compose the actor, authority or closure loop. A completed live transaction is strong evidence but **not a universal Methodology prerequisite for every `C`**. Under the approved #3/#39 alternative, the local M1 exit accepts a sufficiently evidenced source-first functional constructor witness instead of mandatory live execution. See [the source-first threshold review](../../docs/reviews/2026-10-13-s3-c-threshold.md). No current S3 grade changes.

## Time-bounded G1 parent-assisted holder grant (S5-issued)

The declared S5 parent has [selected the `C(P)` target](https://github.com/opensiro/vsm-oss-organization/issues/238#issuecomment-6169206967) and subsequently made an [explicit `G1` S3 holder appointment](https://github.com/opensiro/vsm-oss-organization/issues/238#issuecomment-6169376275). The **only canonical operational bounds** for this temporary role are [`parent-assisted-g1.md`](parent-assisted-g1.md), under the attributable [S5 decision record](../../records/s5/2026-10-14-s3-g1-parent-assisted-grant.md).

**G1 names human `xLagerFeuer` separately in an S3 role; agents present options and apply only the owner's selected bounded choice.** No live authority derives from this source before the grant is on current `main` through a verified normal merge, and it expires absolutely on `2026-11-13T12:00:00Z` or earlier on revocation. Every S3 case still needs independent evidence, current whole-system admission, an actual chosen decision and real S1 return/closure. This does **not** establish `C(P)`, `C`, `P`, or autonomous `A` by itself.

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

**Approved local M1 Option B (effective 2026-10-13):** [governing #3 operator decision](https://github.com/opensiro/vsm-oss-organization/issues/3#issuecomment-6154518187), prospectively reflected in [#3](https://github.com/opensiro/vsm-oss-organization/issues/3) and [#39](https://github.com/opensiro/vsm-oss-organization/issues/39), permits a source-first, function-specific positive S3 constructor witness **without universally requiring a completed live transaction**. The witness must still establish a real whole-system present-control function, legitimate decisive decision/feedback right, a boundary-reachable first-party S3-specific path and return to S1. Mere naming, templates, developer promises, generic coordination and GitHub privileges are insufficient. See [ROADMAP](../../docs/ROADMAP.md#m1-s3c-acceptance--approved-source-first-alternative-2026-10-13).

The selected Methodology `C` test and an optional real-use integration test remain separate. `C` permits composition of actor, authority or closure; `A` requires autonomous decisive ownership and operational closure. This governance amendment is **not itself a positive function witness or a new grade**.

M1 may optionally schedule a **bounded real-use integration trial**. If conducted, the trial must still freeze genuine active S1 commitments, relevant whole-system state, the actual S3 decision right and owner, a real choice with operational consequences, and the return target before the decision. The transaction is evidence only after the returned instruction has been acknowledged/applied (or explicitly rejected/escalated), with an observable effect or justified preservation of subsequent operation. If no substantive current-control choice exists, do not stage a dummy transaction or promote the autonomy grade.

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

## Offline transaction-state validation (structural only)

An instantiated S3 transaction may be checked before publication or application:

```bash
python scripts/check_s3_current_control.py path/to/instantiated-transaction.json
python scripts/check_s3_current_control.py --previous path/to/prior.json path/to/next.json
python scripts/check_s3_current_control.py --g1 --g1-now path/to/new-g1-transaction.json
python scripts/check_s3_current_control.py --g1 path/to/historical-g1-transaction.json
python scripts/check_s3_current_control.py --g1 --previous path/to/prior.json path/to/next.json
python -m unittest tests.test_s3_current_control -v
```

When `--previous` is supplied, it also checks strict adjacent lifecycle progression and immutable decision scope; it cannot establish that the supplied previous file is authentic. The checker rejects uninstantiated template placeholders, unknown fields, out-of-bound S1 work-item targets, prefilled decisions at `REQUESTED`, unsupported decision classes, or unsubstantiated structural jumps to `APPLIED` / `CLOSED`. `ESCALATED` and `CANCELLED` remain possible before an actual owner choice if their terminal disposition has proper source references.

**Limit:** Offline validation checks types, state completeness and GitHub reference *shapes*, not whether a URL resolves, an actor is legitimately authorized, a function is S3 rather than S1/S2/S5, or a returned effect actually happened. Generic passing output is `STRUCTURALLY_VALID_NOT_S3_FUNCTION_WITNESS`; this check never authorizes a decision or establishes `S3=C` / `S3=A`.

**G1-specific authority-envelope regression guard:** `--g1` additionally reads the **currently checked-out** [G1 grant](parent-assisted-g1.md) and fails closed when requested decision classes exceed its published `CONTINUE`, bounded `SET_CONSTRAINT`, `REQUIRE_REPAIR` envelope, or when a non-human is attributed as the G1 decisor. Generic S3 transactions remain governed by their own grant rather than silently inheriting G1 restrictions. The additional **`--g1-now`** flag is required for prospective G1 actions: it checks the locally published half-open UTC term (inclusive start, exclusive expiry) from the canonical grant, failing closed outside that interval. Keep historical artifact inspection on plain `--g1`, so expiry does not invalidate archival structure. This time gate uses the machine's clock and checked-out source: it **does not confirm GitHub publication freshness, revocation, identity, or a genuine whole-system matter**. Neither guard authenticates an individual GitHub owner decision, confirms case admissibility or verifies S1 effect. Callers must independently check those facts immediately before any S3 action; a `G1_*_SHAPE_VALID_*` output is **never** an authority token, a transaction admission, or an S3 functional witness.

## S1 return

A returned decision affects S1 only when the transaction identifies the affected work, records the decision owner, stays within the admitted current-control envelope, and supplies a bounded instruction that S1 can acknowledge/apply or explicitly reject/escalate.

The S1-side adapter is [`../../roles/S1.md`](../../roles/S1.md). Arbitrary comments, approvals, labels, chat messages, scheduler states, and CI failures do not become S3 input merely because S1 can see them.

## S3* relation

A material S3* finding may trigger this contract, but audit and current-control ownership remain distinct. The complementary-audit contract is [`../s3star/audit.md`](../s3star/audit.md).

## Standing regulation of existing shared current commitments

The [first-party standing current-commitment function](standing-current-commitments.md) explicitly identifies **existing shared S1 operational obligations** and the restricted G1-regulated *current* nonlocal reconciliation right, instead of requiring a manufactured incident. [`scripts/s3_current_regulation.py`](../../scripts/s3_current_regulation.py) observes the actual selected/consumed contract state and constructs **unselected, source-required** G1 current-regulation options; it routes local S1 repair and S5 contract selection away from S3. Its conditional packet is **not** a case admission or an owner instruction, and the command cannot alter S1, override grades, reselect Methodology, or impose blanket gates. The decisive G1 owner and existing S3→S1 return procedures remain separately required for any real operating case. A source-first Methodology `C` assessment can consider this **specialized standing regulatory function/path** without demanding a live decision; the resulting grade is a separate evidence decision.

## Current evidence boundary

The constructor is implemented, but a *qualifying whole-system S3 function at this boundary* is not yet positively established by the available source-linked evidence. The approved **Organization M1 exit gate** in #39 permits either genuinely evidenced real-use current control and S1 return or positive source-first function/constructor qualification. Neither has yet positively established the function in the available source-linked record, and no present grade changes. A future review must distinguish established whole-system regulation from the ability to compose a decision actor, avoiding any fabricated operational receipt.

The actor adapter is [`../../roles/S3.md`](../../roles/S3.md). It must not be treated as evidence that the function already exists.
