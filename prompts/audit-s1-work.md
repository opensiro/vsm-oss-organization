# Audit one S1 work item with complementary evidence

Use this prompt with [`S3STAR_AUDIT.md`](../S3STAR_AUDIT.md) for preparatory M1 work.

```text
Audit one bounded S1 contribution/closure claim using a materially complementary evidence path.

First inspect the current repository state, the audited work item, the Organization-selected upstream contract (or explicitly frozen historical contract), and the ordinary S1 evidence/reporting path.

Before making an audit judgment, establish:
- system-in-focus and exact audited S1 work item;
- exact claim/risk under audit;
- ordinary S1 reporting/evidence path;
- complementary evidence/access path;
- why that access is materially different for this claim;
- primary evidence required;
- actor that owns the audit judgment;
- supporting deterministic checks/tools separately;
- downstream current-control destination for a material finding;
- closure condition.

If the proposed audit only repeats the ordinary S1 check or reads only the same S1 narrative, do not pretend it is S3*. Record that the complementary-access requirement is not satisfied.

Inspect the declared complementary evidence independently where possible. Prefer pinned primary evidence, raw diffs, complete changed-file sets, replay/reconstruction, source-of-truth comparisons, or other evidence not controlled solely by the producing S1 for the audited claim.

Do not infer S3* merely from another model, a verifier label, CI, logs, tracing, or a routine QA stage.

Do not repair the S1 contribution while acting as S3* unless that repair is separately admitted as a new work item. Do not make the downstream S3 current-control decision merely because the audit found a problem.

End with exactly one local audit outcome:
- PASS — no material contradiction/gap established for the declared claim;
- FINDING — a material issue is established and should enter the declared control destination;
- INSUFFICIENT — evidence/access cannot support a reliable judgment.

For FINDING, preserve the primary evidence and route the finding to the declared current-control destination. Record whether and how it enters subsequent control; publication alone is not closure.

Attribute any human intervention affecting the audit judgment. Do not count a human-selected conclusion as agent-owned evidence.

Use templates/s3star-audit-record.md for the reviewable record. Do not record hidden chain-of-thought.

This prompt does not establish S3*=A, activate M1, create an autonomous S3 regulator, or introduce S2/S4/S5.
```
