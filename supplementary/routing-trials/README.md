# Blind routing trials

This directory stores empirical routing trials for [ROUTING_CONFORMANCE.md](../../ROUTING_CONFORMANCE.md).

A trial batch must use fresh agent/runs without OpenSiro project memory or a preloaded Organization URL. Do not use the current maintainer/assistant conversation as a substitute for a blind run.

The trial population is the canonical `Current in-scope public repositories:` set from the Organization README. Public repositories outside that bounded VSM Harness OSS scope are not part of this evidence set.

Use one row per trial:

| Field | Value |
| --- | --- |
| Batch | `<batch-id>` |
| Run | `<run-id>` |
| Start repository | `opensiro/<in-scope-repo>` |
| Start SHA | `<sha>` |
| Task class | `organization-wide` / `repository-local` |
| Prompt | `<verbatim prompt>` |
| Files read | `<ordered paths/URLs>` |
| Links followed | `<ordered links>` |
| Chosen destination | `opensiro/<repo>` |
| Routing rationale | `<short rationale>` |
| Result | `PASS` / `FAIL` |

## Required coverage

Each batch intended as full routing evidence should:

- include every current in-scope VSM Harness OSS repository as a starting point;
- include organization-wide positive cases;
- include repository-local negative controls;
- preserve failed runs rather than rerunning them away;
- record the starting repository revision so the README surface is reconstructable.

A PASS requires both the correct destination and a correct source-of-truth boundary explanation. Aggregate results are empirical routing reliability evidence, not VSM autonomy evidence.