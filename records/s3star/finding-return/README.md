# S3* → Index S1 finding-return evidence (derived view)

**Owner:** [Organization #200](https://github.com/opensiro/vsm-oss-organization/issues/200). This directory holds **dated, derived follow-up snapshots** for already recorded Organization S3* findings, never new audit verdicts or a canonical Index correction ledger.

## Authority and scope

- W001's original selection, findings and locks: [#188](https://github.com/opensiro/vsm-oss-organization/issues/188). W002's original selection, findings and locks: [#190](https://github.com/opensiro/vsm-oss-organization/issues/190) and [draft #191](https://github.com/opensiro/vsm-oss-organization/pull/191).
- The downstream **Index issue/PR and exact accepted Index main** own the adjudication and correction outcome. GitHub issue status or CI alone is not semantic adjudication.
- The future general *reporting metadata contract* is separately proposed in [#196 / draft #197](https://github.com/opensiro/vsm-oss-organization/pull/197). This historical view does **not** retroactively amend the W001/W002 S3* audits or require that draft's integration.
- Source-first independent Index PR review is separately owned by [#189 / draft #198](https://github.com/opensiro/vsm-oss-organization/pull/198). An S3* finding cannot be treated as GitHub PR approval.
- Actual S3 current-control functions require [independent S3 admission](../../../contracts/s3/current-control.md), not just a routed discrepancy.

## Existing dated cut

[2026-10-11-index-open.json](2026-10-11-index-open.json) enumerates exactly four *already routed* claim-specific findings, with frozen source SHAs and their legitimate Index owner destinations. All are `ROUTED_OPEN` **at this observation cut**. This does not assert that they will remain open later.

The structural validator pins the SHA-256 of that initial four-finding JSON and compares every later snapshot against its exact frozen finding identities, upstream SHAs, claim scopes, original audit references, and owning Index destinations. A syntactically valid but different 40-character SHA or alternate valid Index issue must fail closed. New snapshots may update dates, observed repository main refs and attributed owner/verification evidence, **not** silently replace or drop historical findings. This pin is an internal integrity gate only; it does not authenticate independent semantic judgments or current GitHub outcomes.

```bash
python scripts/check_s3star_finding_return.py \
  records/s3star/finding-return/2026-10-11-index-open.json
python -m unittest tests.test_s3star_finding_return -v
```

## Distinct stages (no automatic promotion)

| Derived stage | Minimum actual evidence |
| --- | --- |
| `ROUTED_OPEN` | Original S3* `FINDING`, stable frozen identity/source SHA, Index owner issue and routed receipt. Never call this resolved. |
| `ADJUDICATED` | A *genuine Index owner* decides `CORRECTION_REQUIRED`, `NO_CHANGE_EVIDENCED` or `INSUFFICIENT_EVIDENCE` with an attributed dated exact-ref source and reason; cannot be inferred from an Organization comment. |
| `VERIFIED` | Only after a distinct checker checks the **actual** Index result against that decision. Correction requires an authorized changed Index PR merged and checked on exact live `main`; reasoned no-change requires a documented source-grounded owner decision and independent verification. `INSUFFICIENT_EVIDENCE` cannot be `VERIFIED`. |

Any future status update requires reading the live owner issue/comments, PR head/merge and exact Index main, preserving the original JSON as historical. Publish a **new dated derived snapshot or an append-only issue receipt**, link the previous snapshot and actual source of truth, and keep the original `FINDING` immutable. The structural validator checks *claimed references and consistency*, not actual GitHub identity, reviewer independence, source semantics, CI success, or whether a referenced PR merged. Never substitute its `STRUCTURAL PASS` for that independent observation.

A reasoned `NO_CHANGE_EVIDENCED` is a valid owner adjudication; it is not a finding that a downgrade occurred. A source-pinned factual discrepancy can remain real without requiring a categorical grade change. Do not combine unrelated audit denominators or promote S1=A/S3*=A based on this view.

**No permissions are transferred:** this directory does not authorize new S3* waves, W001/#1302 lock takeovers, Index canonical edits, review/admission merges, Profile/Skills methodology changes, or automatic Organization scheduling.