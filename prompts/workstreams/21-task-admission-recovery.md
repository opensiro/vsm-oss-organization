# Workstream #21 — task admission and routine recovery

Use the following as the first message in a separate agent/chat run.

```text
Work on OpenSiro M0 workstream #21: define the S1 task-admission, escalation, and routine-recovery contract.

Primary tracker:
- https://github.com/opensiro/vsm-oss-organization/issues/21

Related context:
- M0 tracker #2
- viable-system definition PR #18 if still open, otherwise its merged result
- S1 role and contributor prompts in current opensiro/vsm-oss-organization main

Target repository:
- opensiro/vsm-oss-organization

Prepared branch:
- m0-task-admission-recovery-21

Before changing anything:
1. Inspect the current public default branch and open PRs in opensiro/vsm-oss-organization.
2. Re-read issue #21 and the current M0 tracker #2.
3. Read current organizational identity/work-domain material; if PR #18 is still open, inspect it rather than assuming it is merged.
4. Read current released Profile/Methodology boundaries from opensiro/vsm-harness-profile and opensiro/vsm-harness-skills.
5. Verify whether the prepared branch is still suitable; rebase/recreate from current main if needed rather than building on stale assumptions.

Goal:
Make every presented work item resolve before execution into either:
- admitted bounded S1 work with an explicit authority envelope; or
- an evidence-backed non-admission/escalation.

There must be no implicit third path in which a human silently supplies ordinary operational decisions while the run is still described as autonomous.

Constraints:
- Do not claim that all OSS work belongs to S1.
- Do not invent later VSM roles to route work.
- Do not solve executor provenance (#19).
- Do not implement repository-specific validation suites (#20/#22/#23/#24).
- Keep merge/integration authority separate from ordinary S1 operational autonomy unless explicitly delegated.
- Do not manufacture failure scenarios as evidence; define contracts and use real observed disturbances when available.

Expected work:
1. Derive a concise admission checklist from the current viable-system work domain.
2. Distinguish ordinary bounded contribution work from at least:
   - semantic or Methodology authority changes;
   - organizational identity/scope/ultimate-policy changes;
   - insufficient-evidence work that cannot yet be safely admitted.
3. Define what must be frozen before execution: repository boundary, outcome, authority envelope, forbidden decisions, validation expectation, escalation conditions.
4. Define routine-recovery expectations for natural disturbances such as stale base, validation failure, broken reference, generated-file drift, evidence gaps, or a no-change result.
5. Define what counts as escalation versus ordinary local recovery.
6. Define the evidence preserved when work is rejected/non-admitted or escalated.
7. Update the smallest appropriate docs/templates/prompts.
8. Open a normal PR against current main and validate that no VSM semantics were redefined.

Exit condition:
A reviewable PR provides a runtime-neutral admission/recovery contract usable by future M0 trials and continuous S1 operation, while explicitly preserving work that belongs outside S1.

At completion, report:
- branch and PR;
- files changed;
- admission decision model;
- routine-recovery model;
- explicit escalation categories;
- any remaining ambiguity that requires maintainer or normative authority.
```
