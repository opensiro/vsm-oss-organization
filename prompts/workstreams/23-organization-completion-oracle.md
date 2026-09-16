# Workstream #23 — Organization completion oracle

Use the following as the first message in a separate agent/chat run.

```text
Work on OpenSiro M0 completion-oracle workstream #23 for opensiro/vsm-oss-organization.

Primary tracker:
- https://github.com/opensiro/vsm-oss-organization/issues/23
Parent tracker:
- https://github.com/opensiro/vsm-oss-organization/issues/20

Write target:
- opensiro/vsm-oss-organization

Prepared branch:
- m0-org-completion-oracle-23

Before changing anything:
1. Inspect the current public default branch and all open PRs that may change scope, roadmap, contracts, prompts, roles, or version references.
2. Re-read issues #20 and #23 and the current M0 tracker #2.
3. If PR #18 is still open, inspect its identity/coverage definitions but do not assume they are merged.
4. Inspect the current released Profile/Methodology versions and the control-plane source-of-truth rules.
5. Confirm whether the prepared branch is still suitable relative to current main. If it is stale, recreate/reconcile before editing.

Goal:
Add a small deterministic completion oracle for repository-local organizational-contract consistency, without encoding semantic or ownership judgments as tests.

Candidate deterministic invariants include:
- the declared in-scope repository set is internally consistent across active authoritative local surfaces;
- explicitly out-of-scope repositories are not accidentally presented as governed by this control plane;
- active released Profile/Methodology references do not drift across current contract surfaces while intentionally frozen historical references remain allowed;
- required local links among README, CONTROL_PLANE, ROADMAP, roles, prompts, and contributor surfaces resolve;
- M0–M5 target vectors do not silently diverge where exact deterministic comparison is appropriate;
- validators never claim that CI success proves agent ownership or VSM autonomy.

Expected work:
1. Inventory repository-local facts that are duplicated today and classify whether duplication should be removed, generated, or mechanically checked.
2. Define the smallest stable set of deterministic invariants.
3. Implement a small validator and CI workflow if justified.
4. Add representative negative/self-test cases where practical.
5. Test against current main and relevant open-PR state without baking temporary PR content into permanent invariants.
6. Keep historical evidence/frozen references distinguishable from active-contract references.
7. Open a normal PR against current main.

Parallelization boundary:
Own Organization-local consistency checks only. Do not solve executor provenance (#19), task admission/recovery (#21), Profile validation (#22), or Awesome↔Index validation (#24).

Exit condition:
A reviewable PR gives autonomous S1 work a deterministic way to detect important Organization contract drift, while leaving semantic interpretation and ownership evidence outside the validator.

At completion, report:
- branch and PR;
- invariants enforced;
- duplicated facts removed/generated/checked;
- negative cases tested;
- intentionally non-deterministic judgments left to reviewers;
- any conflicts with concurrently open Organization PRs.
```
