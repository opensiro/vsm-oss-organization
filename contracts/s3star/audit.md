# S3* complementary-audit constructor contract

This contract defines the first-party Organization path for complementary S3* audit.

It applies the selected Profile and Methodology through [`../../UPSTREAM_CONTRACT.json`](../../UPSTREAM_CONTRACT.json). It does not redefine S3* or autonomy states.

Under the selected Methodology, the current constructor target is `S3*=C`: the function is established and a first-party S3*-specific path exists, while autonomous ownership/independence/final closure may still require composition.

## Functional threshold

A qualifying audit establishes:

1. a real material claim/risk for which routine S1/S3 reporting is insufficient;
2. the ordinary reporting path;
3. materially complementary access capable of challenging that path;
4. an S3*-specific judgment surface;
5. one local outcome: `PASS`, `FINDING`, or `INSUFFICIENT`;
6. an explicit downstream control destination for material findings;
7. actual judgment ownership separate from evidence collection, validators, transport, and downstream S3;
8. boundary reachability through a first-party Organization path.

Using another model, rerunning the same test, adding a verifier label, or exposing a generic callback is not sufficient by itself.

## Claim-relative independence

Independence is evaluated relative to the audited claim. Useful complementary access may include raw diffs, pinned primary evidence, replay/reconstruction, independent source-of-truth comparison, sampling not selected solely by the producing S1, or adversarial/counterexample-oriented checks.

## Record and closure

Use [`../../templates/s3star-audit-record.md`](../../templates/s3star-audit-record.md) for a reviewable record. A `FINDING` should identify a current-control destination; publication of a finding alone is not closure.

A material downstream current-control matter may enter [`../s3/current-control.md`](../s3/current-control.md). S3* does not inherit S3 authority merely because its finding initiated control.

## Existing witness

Issue #44 / PR #45 exercised this topology on real repository work. The auditor reconstructed the bounded claim from materially complementary raw/canonical evidence and returned `PASS` without manufacturing a finding. This establishes the current `S3*=C` constructor evidence; it does not establish `S3*=A`.

## Ownership boundary

The audit judgment owner is the actor exercising discretionary judgment over the complementary evidence in the concrete run. During M1 that owner may be human, agent, or another explicitly composed participant. Evidence collectors, APIs, tests, deterministic scripts, validators, parsers, queues, and transport remain support unless they exercise that judgment.

The actor adapter is [`../../roles/S3STAR.md`](../../roles/S3STAR.md). Its presence does not independently establish S3*.
