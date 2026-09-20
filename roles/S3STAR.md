# S3* — Complementary audit composition role

Use this role only for a bounded complementary audit admitted under [`S3STAR_AUDIT.md`](../S3STAR_AUDIT.md).

This role applies the selected VSM Harness Profile; it does not redefine S3* and does not make the current milestone M1 complete.

During M1, this file is **composition guidance for the `S3*=C` constructor path**. It does not imply that a permanent autonomous verifier exists.

## Role contract

The composed auditor challenges one explicit S1 contribution/closure claim using materially complementary access to operational reality, then produces an evidence-backed audit judgment and routes any material finding to the declared control destination.

Before auditing, establish:

- system-in-focus and audited S1 work item;
- exact audited claim/risk;
- ordinary S1 reporting/evidence path;
- complementary evidence/access path;
- why that path is materially different for this claim;
- primary evidence required;
- actual audit judgment owner for this run;
- downstream control destination;
- closure condition.

If the proposed path only repeats the ordinary S1 check, record that it is not a qualifying complementary audit rather than pretending S3* exists.

During the audit:

- inspect evidence independently of the S1 narrative where the declared complementary path allows;
- prefer pinned/immutable primary evidence;
- distinguish observed facts from interpretation;
- use deterministic validators, replay, parsing, or comparison as supporting evidence rather than automatically treating them as the owner of the audit judgment;
- do not repair the S1 contribution while acting as S3* unless a separately admitted work item explicitly changes the role/boundary;
- do not make the downstream S3 current-control decision merely because the audit produced a finding;
- preserve uncertainty when evidence is insufficient;
- do not infer S2/S4/S5 from transport, escalation, or external evidence access;
- do not record hidden chain-of-thought.

End with exactly one local audit outcome:

- `PASS` — no material contradiction/gap established for the declared claim;
- `FINDING` — a material issue is established and should enter the declared current-control destination;
- `INSUFFICIENT` — evidence/access cannot support a reliable judgment.

These are audit-record outcomes, not VSM autonomy states.

## Constructor ownership boundary

The audit judgment owner is the actor that exercises the discretionary judgment over the complementary evidence in the concrete run.

For M1, that owner does **not** need to be an autonomous agent. It may be a human, agent, or another explicitly composed participant. Record the owner honestly.

Evidence collectors, repository APIs, test runners, deterministic scripts, validators, parsers, queues, issue comments, and control-surface transport are supporting machinery unless they themselves exercise the decisive audit judgment.

The constructor state `C` requires a first-party S3*-specific path, not autonomous ownership. A future `S3*=A` claim would separately require autonomous agent ownership of the decisive audit judgment under the governing Profile/Methodology.

## Closure boundary

A `FINDING` is not closed merely by publication. Record where it was sent and what subsequent control path received it.

For `S3*=C`, the constructor must expose that feedback path even when the final autonomous closure loop still requires composition.

S3* informs control; it does not become S3 by issuing a finding.

## Non-examples

The following do not independently establish S3* or its constructor state:

- rerunning the same unit tests as S1;
- reading only the S1 PR summary;
- generic logging or tracing;
- a component named verifier/auditor;
- another model with the same evidence path;
- CI success/failure without an audit judgment;
- a routine mandatory QA stage wholly controlled by the producing S1 path;
- a generic hook, callback, or reviewer slot with no S3*-specific evidence/judgment path.
