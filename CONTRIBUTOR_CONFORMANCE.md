# Fresh contributor conformance

This document defines a behavioral check for whether a zero-context contributor or coding/research agent can move from the public OpenSiro organization surface to one bounded, reviewable repository-local contribution without maintainer-specific instructions.

It complements [ROUTING_CONFORMANCE.md](ROUTING_CONFORMANCE.md). Routing conformance asks **where work belongs**. Fresh contributor conformance asks whether a newcomer can then acquire the correct work item, assemble the current contract, preserve the task boundary, validate the change, and deliver it through the owning repository's normal review path.

This is contributor-experience evidence. It is not a VSM autonomy grade and does not change the current roadmap milestones.

## Qualifying run

A qualifying run uses a fresh agent/run with:

- no OpenSiro project prompt;
- no prior OpenSiro conversation or memory supplied to the run;
- no preloaded repository other than the public organization entry URL;
- permission to read and navigate public OpenSiro/GitHub surfaces;
- normal repository write capability only if the trial is intended to reach a real PR;
- no maintainer instructions after launch unless the agent reaches a genuine blocker and records it.

The current maintainer/assistant conversation is not a qualifying run.

## Reference prompt

Use this prompt verbatim for the first Index pilot unless the trial record explicitly declares another prompt:

> Start at https://github.com/opensiro. Contribute one valid standalone assessment to the OpenSiro VSM Harness Index. Do not ask the maintainer for instructions unless you are genuinely blocked. Do not change unrelated files. Preserve repository source-of-truth boundaries and submit the work through the normal review path.

The prompt intentionally does not name `opensiro.com`, `CONTRIBUTOR_START.md`, the Index repository, an assessment batch, a `NEXT` row, a pinned revision, Profile/Methodology versions, or validation commands. Discovering those surfaces is part of the trial.

## Required stages

A complete Index pilot records whether the fresh contributor successfully passed each stage:

1. **Orientation** — recognizes `opensiro.com` / posters as optional explanatory material without treating the site as normative.
2. **Routing** — identifies `vsm-harness-index` as the owner of standalone assessment work and preserves Profile/Skills/Organization boundaries.
3. **Task acquisition** — finds a frozen `[Assessment batch]`, reads its Manual assessment board, and selects only the current `NEXT` row.
4. **Contract assembly** — resolves the frozen repository/ref and current active semantic contract; where available, uses repository tooling such as `scripts/assessment_preflight.py` rather than reconstructing the envelope ad hoc.
5. **Semantic preparation** — reads current `vsm-harness-profile/main` and `vsm-harness-skills/main` before mapping the row.
6. **Bounded execution** — assesses only the selected repository at the frozen boundary, maps organizational function before autonomy, and avoids importing adjacent/external system functions.
7. **Validation** — runs the active assessment-structure check and all repository-required generated-view/index checks relevant to the change.
8. **Delivery** — produces one bounded, reviewable PR without unrelated canonical changes and does not advance the batch board unless explicitly authorized.

## PASS / FAIL

A trial is `PASS` only when all required stages complete and the resulting contribution is accepted as a valid bounded work item by the normal repository review/validation path.

The following are failures even if a PR can be opened:

- selecting a queued row instead of `NEXT`;
- silently repinning the candidate;
- treating the website as semantic authority;
- using stale Profile/Methodology instructions instead of current sources;
- changing unrelated rows or repositories;
- inventing VSM functions from component names;
- skipping required validation;
- advancing shared task state without authority;
- producing an assessment that normal review rejects for a material methodology/boundary error.

Infrastructure or permission failures that prevent otherwise-correct work should be recorded as `BLOCKED`, not converted into a semantic `FAIL` or rerun away.

## Evidence record

Record at least:

```text
batch / run id
start URL
time / date
fresh-run declaration
verbatim prompt
organization/profile revision observed
repositories and SHAs observed
files/pages read in order
links followed in order
selected assessment batch
selected NEXT row
preflight output or equivalent resolved envelope
Profile main SHA read
Skills main SHA read
candidate frozen ref
files changed
validation commands + results
PR URL
review outcome
blocker, if any
stage-by-stage PASS / FAIL / BLOCKED
final result
short failure analysis
```

Preserve failed and blocked runs. Do not rerun them away when reporting reliability.

## Interpretation

One passing run demonstrates that the current public surfaces can support one successful zero-context path. It does not establish general reliability.

Repeated batches should vary the starting time and available work while preserving the same evidence schema. A later regression can therefore be localized to orientation, routing, task acquisition, contract assembly, semantic preparation, execution, validation, or delivery instead of being reported only as "the agent failed."

Trial records live under [`supplementary/contributor-trials/`](supplementary/contributor-trials/).