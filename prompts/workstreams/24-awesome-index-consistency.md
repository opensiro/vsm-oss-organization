# Workstream #24 — Awesome ↔ Index consistency

Use the following as the first message in a separate agent/chat run.

```text
Work on OpenSiro M0 completion-oracle workstream #24: strengthen deterministic consistency between Awesome VSM Harness and the canonical VSM Harness Index.

Primary tracker:
- https://github.com/opensiro/vsm-oss-organization/issues/24
Parent tracker:
- https://github.com/opensiro/vsm-oss-organization/issues/20

Write target:
- opensiro/awesome-vsm-harness

Read-only canonical source:
- opensiro/vsm-harness-index

Prepared branch:
- m0-awesome-index-consistency-24

Before changing anything:
1. Inspect the current public default branches of opensiro/awesome-vsm-harness and opensiro/vsm-harness-index.
2. Inspect open PRs in both repositories that may change links, identifiers, generated views, assessments, or curation structure.
3. Re-read issues #20 and #24 in opensiro/vsm-oss-organization.
4. Inspect current Awesome selection policy and current Index source-of-truth relationships. Do not infer policy from names alone.
5. Verify that the prepared Awesome branch still has a suitable base; if stale, recreate/reconcile from current main before editing.

Goal:
Improve Awesome completion evidence beyond format lint by mechanically checking deterministic relationships to the canonical Index, without turning Awesome into a second assessment database or making curation taste deterministic.

Investigate checks such as:
- each referenced Index assessment exists;
- linked TLDR/RANKINGS/other canonical targets and anchors exist where used;
- harness/repository identifiers resolve unambiguously to the intended Index entry;
- Awesome does not manually duplicate canonical VSM state vectors or assessment facts that should remain synchronized from Index;
- existing awesome-lint remains useful but is not the only closure oracle.

Constraints:
- Index assessments and rankings remain canonical in the Index.
- Do not modify Index assessments as part of this workstream.
- Do not encode organizational distinctiveness, representative value, popularity, or curation taste as a deterministic admission score.
- Do not redefine VSM semantics or autonomy states.
- Prefer referencing/generating from upstream over adding a new manually maintained mapping.

Expected work:
1. Inventory current Awesome entries and their deterministic dependencies on Index.
2. Identify the smallest invariant set that can be mechanically verified without copying canonical facts.
3. Implement a validator and CI integration in Awesome if justified.
4. Add representative broken-link/missing-assessment/identifier-drift failure cases where practical.
5. Run the validator on current Awesome and current canonical Index.
6. Open a normal PR in opensiro/awesome-vsm-harness.

Parallelization boundary:
Own Awesome↔Index deterministic consistency only. Do not modify Index assessment content, executor provenance, Organization task admission, or general Profile semantics.

Exit condition:
A reviewable Awesome PR materially improves deterministic consistency with the canonical Index while preserving Awesome as a curated downstream view rather than a second assessment store.

At completion, report:
- branch and PR;
- deterministic relationships checked;
- how the validator obtains canonical Index facts without duplicating them;
- failure cases tested;
- curation judgments intentionally left non-deterministic.
```
