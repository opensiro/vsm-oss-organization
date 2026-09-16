# Workstream #22 — Profile completion oracle

Use the following as the first message in a separate agent/chat run.

```text
Work on OpenSiro M0 completion-oracle workstream #22 for opensiro/vsm-harness-profile.

Primary tracker:
- https://github.com/opensiro/vsm-oss-organization/issues/22
Parent tracker:
- https://github.com/opensiro/vsm-oss-organization/issues/20

Write target:
- opensiro/vsm-harness-profile

Prepared branch:
- m0-profile-completion-oracle-22

Before changing anything:
1. Inspect the current public default branch of opensiro/vsm-harness-profile, its open PRs, releases/tags/versioning surfaces, scripts, and GitHub Actions state.
2. Re-read issues #20 and #22 in opensiro/vsm-oss-organization.
3. Inspect current vsm-harness-skills validation/sync behavior where it consumes Profile artifacts, but do not move Profile authority into Skills.
4. Confirm whether the prepared branch still starts from a suitable current base. If main has moved, prefer a fresh branch from current main or otherwise document/reconcile the delta before editing.

Goal:
Give ordinary Profile maintenance a stronger deterministic completion oracle for repository consistency without pretending that semantic correctness can be unit-tested.

Normative boundary:
- vsm-harness-profile remains the authoritative source of VSM semantics.
- The validator may check structural/version/release/reference invariants.
- The validator must NOT decide whether a new VSM semantic statement is conceptually correct.

Investigate deterministic invariants such as:
- VERSION agrees with the current version declared on active normative/profile-facing surfaces;
- CHANGELOG/versioning/release metadata is internally consistent where repository policy requires it;
- required normative files and local references exist;
- deterministically checkable release/provenance invariants hold;
- no second manually maintained normative database is introduced;
- downstream bundled/sync relationships remain source-of-truth correct.

Expected work:
1. Build an inventory of current completion signals and current gaps.
2. Separate deterministic invariants from semantic reviewer judgment.
3. Implement only the smallest high-value local validation script and CI/workflow needed.
4. Add representative negative/self-test cases where practical so a broken invariant demonstrably fails.
5. Run the validator on current repository state.
6. Inspect the final diff for accidental semantic changes.
7. Open a normal PR in opensiro/vsm-harness-profile.

Parallelization boundary:
Own Profile-local completion checks only. Do not modify Profile semantics, executor provenance, Organization admission policy, Index assessments, or Awesome selection policy.

Exit condition:
A reviewable Profile PR materially improves machine-checkable closure for ordinary Profile maintenance while leaving semantic judgment with the appropriate evidence/review process.

At completion, report:
- branch and PR;
- deterministic invariants implemented;
- commands/CI used to validate them;
- representative failure cases tested;
- important Profile correctness questions that intentionally remain non-deterministic.
```
