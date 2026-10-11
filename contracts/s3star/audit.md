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

## Prospective Index-batch audit reporting dimensions (additive, not a verdict)

**Applies only to audits prospectively admitted under a contract that includes this section.** For Index assessment-batch S3* audits, record the following separately, when evidence exists. For other audit scopes, mark these fields `not_applicable`. These dimensions are *reporting metadata*, never replacements for the one local `PASS`, `FINDING`, or `INSUFFICIENT` judgment above.

| Dimension | Admissible reporting and evidence boundary |
| --- | --- |
| `s1_readiness` | `TERMINAL` / `PENDING` / `NOT_READY`, referring only to the original Index batch's actual serial board. Nonterminal source claims do not become failed audits. Include observed cutoff and owner issue. |
| `process_scope` | `RECONCILED` / `PARTIAL` / `NO_TERMINAL` plus an exact numerator and denominator for original source identity, accepted/rejected terminal rows, review/admission PRs, exact-head checks and canonical entries. Separate technical source-unavailable terminals from accepted or excluded assessments. `RECONCILED` may refer only to existing terminal rows in an unfinished batch; it cannot silently imply whole-batch completion. |
| `semantic_scope` | Exact frozen source SHA and applicable Profile/Methodology, preselected row positions, reviewed/eligible counts, claim-specific bounded source judgments and named counterevidence. A spot check is **not** an exhaustive six-function or ten-row semantic verification; do not refill precommitted unavailable sample slots. |
| `historical_reviewer_provenance` | `ESTABLISHED` / `UNVERIFIED` / `NOT_ADJUDICATED`, with reviewed PR/event references. `ESTABLISHED` requires an attributable, actually independent historical semantic reviewer for the stated claim; green CI, another model invocation, or separate GitHub login by itself is not enough. `UNVERIFIED` is not an assertion of absence or a retroactive rule violation. Distinguish this from the present auditor and the current publication-review gate. |
| `finding_disposition` | For a `FINDING`: `ROUTED_OPEN` → `ADJUDICATED` → `VERIFIED`, with destination, Index decision owner, dated exact-ref decision and an independently checked closure/effect reference. An owner may accept, reject with reasons, or declare evidence insufficient. A routing comment alone is never closure; approval, regression check and canonical mutation remain owner-authorized. Other local verdicts use `not_applicable`. |

**Aggregation rule:** publish each numerator/denominator and claim scope separately. Do not aggregate unlike `PASS`/`INSUFFICIENT` judgments into Index accuracy, treat `PENDING` as semantic failure, or infer reviewer attribution from CI. Distinguish `FINDING` (immutable local judgment) from its subsequently evolving downstream *disposition*. Update disposition with linked append-only evidence, not by rewriting historical local results.

**Independence/authority rule:** complementary evidence and its discretionary judgment are distinct from support tools, historical Index PR approval, current Organization publication review and downstream S3 control. Nothing here mandates a human auditor, grants S3* merge/grade authority, or proves Organization `S3*=A`.

**Non-retroactivity:** frozen W001/W002 source refs, manifests, sample positions, original audit verdicts and Index owner locks remain as published. A later comparative display may be marked **derived/read-only** and cite them; it is not a retroactive migration or fresh verdict. The reusable agent-executable Index reviewer/PR-gate design stays separately owned by [Organization #189](https://github.com/opensiro/vsm-oss-organization/issues/189). Reporting provenance/closure improvement is tracked in [Organization #196](https://github.com/opensiro/vsm-oss-organization/issues/196).

## Existing witness

Issue #44 / PR #45 exercised this topology on real repository work. The auditor reconstructed the bounded claim from materially complementary raw/canonical evidence and returned `PASS` without manufacturing a finding. This establishes the current `S3*=C` constructor evidence; it does not establish `S3*=A`.

## Ownership boundary

The audit judgment owner is the actor exercising discretionary judgment over the complementary evidence in the concrete run. During M1 that owner may be human, agent, or another explicitly composed participant. Evidence collectors, APIs, tests, deterministic scripts, validators, parsers, queues, and transport remain support unless they exercise that judgment.

The actor adapter is [`../../roles/S3STAR.md`](../../roles/S3STAR.md). Its presence does not independently establish S3*.

## Prospective concurrent-wave coordination

For new parallel Index-batch audit lanes, use the Organization-owned [atomic S3* slot protocol](claims.md) before starting source judgment. This is a coordination instrument, not a replacement for the complementary-audit threshold, the actual judgment owner or Index review/merge authorization. Preexisting frozen W001 claim comments remain historical rather than retroactively atomically locked.
