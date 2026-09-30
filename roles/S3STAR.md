# S3* — complementary-audit actor adapter

Use this role only after an audit has been admitted under the canonical [`contracts/s3star/audit.md`](../contracts/s3star/audit.md) contract.

This file is an **actor adapter**, not the S3* definition and not evidence that a permanent autonomous auditor exists. The contract owns functional admission, complementary-access requirements, judgment/owner separation, finding states, feedback destination, and closure rules. Normative S3* semantics remain upstream in the selected Profile.

## One admitted audit

For the concrete audit:

1. identify the system-in-focus and exact audited claim/risk;
2. identify the ordinary S1/S3 reporting path;
3. use the declared materially complementary evidence/access path rather than merely rereading the producer narrative;
4. inspect primary evidence independently where that path permits;
5. distinguish observed facts from interpretation;
6. keep APIs, retrieval, replay, parsers, deterministic validators, tests, and CI separate from the discretionary audit judgment owner;
7. do not repair the producing S1 artifact while acting as S3* unless a separately admitted work item changes the role;
8. do not make the downstream S3 decision merely because the audit found a problem;
9. preserve uncertainty when evidence is insufficient;
10. end with exactly one local outcome: `PASS`, `FINDING`, or `INSUFFICIENT`.

A `FINDING` must identify its downstream control destination. Publication alone is not closure.

## Ownership

Record the actor that actually exercises the audit judgment in this run. Under the current constructor mode that owner may be human, agent, or another explicitly composed participant. Do not infer `S3*=A` from this adapter, from use of another model, or from the existence of a verifier/reviewer slot.

## Evidence output

Use [`../templates/s3star-audit-record.md`](../templates/s3star-audit-record.md). Preserve the audited work/revisions, claim/risk, ordinary path, complementary path, independence rationale, evidence refs, judgment owner, support/enforcement separately, outcome, control destination, and closure refs.
