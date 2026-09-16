# Workstream #19 — executor provenance

Use the following as the first message in a separate agent/chat run.

```text
Work on OpenSiro M0 workstream #19: establish a runtime-neutral executor provenance witness.

Primary tracker:
- https://github.com/opensiro/vsm-oss-organization/issues/19

Critical prior evidence:
- M0 tracker #2
- instrumented trial #16
- closure PR #17

Target repository:
- opensiro/vsm-oss-organization

Prepared branch:
- m0-executor-provenance-19

Before changing anything:
1. Inspect the current public default branch of opensiro/vsm-oss-organization.
2. Re-read issues #2, #16, #19 and PR #17, including any newer comments/changes.
3. Inspect the current public default branches of opensiro/vsm-harness-profile and opensiro/vsm-harness-skills for the released ownership/autonomy rules. GitHub current state is source of truth.
4. Inspect open PRs that may touch the same evidence surfaces.
5. Verify whether the prepared branch is still a clean/suitable base. If it is stale or contains unrelated work, create a fresh branch from current main instead and record why.

Goal:
Define the minimum primary evidence mechanism by which a second reviewer can bind ordinary decisive S1 decisions/actions to an autonomous executor/session rather than only to the contributor's GitHub identity.

Constraints:
- Keep the organizational contract runtime-neutral. ChatGPT, Codex, Claude Code, custom harnesses, local schedulers, or other execution technologies must remain possible.
- Do not weaken the current definition of A.
- Do not treat PR existence, GitHub Actions, a scheduler, runtime/model naming, or retrospective self-report as ownership proof.
- Do not require hidden chain-of-thought.
- Do not introduce S2, S3, S3*, S4, or S5 merely to solve provenance.
- Do not redesign repository completion/test coverage (#20/#22/#23/#24) or task admission/recovery (#21) except where an interface is strictly required.

Expected work:
1. Compare plausible witness families, including at least dedicated agent/bot execution identity and signed runtime/session attestation.
2. Define the minimum evidence fields and trust assumptions.
3. Define how observable actions/decisions bind to the declared executor/run.
4. Define how human inputs after run start are represented, including the difference between legitimate escalation and hidden step-by-step control.
5. Define explicit reject/insufficient cases for an independent reviewer.
6. Implement the smallest repository-local contract/templates/docs needed to support a new instrumented M0 trial.
7. Validate all changes against the current source-of-truth boundaries.
8. Open a normal PR against current main.

Exit condition:
A reviewable PR defines a runtime-neutral primary executor-provenance witness that is concrete enough to run a new bounded instrumented M0 trial. The PR itself MUST NOT claim S1=A; only the later trial may establish or fail to establish that state.

At completion, report:
- branch and PR;
- files changed;
- witness design selected and alternatives rejected;
- exact remaining trust assumptions;
- whether a new M0 trial can now be started;
- any escalation requiring maintainer policy choice.
```
