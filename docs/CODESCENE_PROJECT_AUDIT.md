# Optional CodeScene project-level audit for OpenSiro OSS

**Status:** Skill instructions prepared; **CodeScene MCP/Core project connection not established or verified**. No CodeScene audit was executed by adding these files.

## Purpose and ownership

Use [CodeScene's `prioritizing-technical-debt` skill](../.agents/skills/prioritizing-technical-debt/SKILL.md) for a source-backed **maintainability / hotspot / technical-debt** review of current OpenSiro OSS repositories. It is a third-party engineering analysis, **not** the OpenSiro canonical VSM Harness assessment and **not** a new VSM function, independence guarantee, authority grant, external reviewer certification, repository admission or global OSS quality score.

The canonical system boundary is the current `Current in-scope public repositories` list in [Organization README](../README.md); read it afresh rather than copying a permanent list here. Route all findings for a repository back to its owning repository using [START_HERE.md](../START_HERE.md) and [ECOSYSTEM.md](ECOSYSTEM.md). Cross-repository aggregation and tool-admission questions belong to Organization. Nothing here changes Profile semantics, Skills Methodology, Index assessment state, Upstream permissions, or existing S3/S3*/S5 boundaries.

## Prerequisites (fail closed)

1. Select each intended repository and verify its current **public** default branch and exact Git SHA. Explicitly enumerate the in-scope repositories and which are *actually* included in CodeScene.
2. Inspect the official pinned [CodeScene skill provenance](../.agents/skills/prioritizing-technical-debt/SOURCE.md), [CodeHealth MCP installation](https://github.com/codescene-oss/codehealth-mcp#installation), and [available provider tools](https://github.com/codescene-oss/codehealth-mcp/blob/main/docs/tools.md). A local `SKILL.md` alone is not a connected service.
3. Obtain an **actual authenticated CodeScene Core project context** (or another verified offering with the same project-level tools). Project hotspots, churn, and project technical-debt goals depend on available CodeScene project data; **standalone local Code Health is not equivalent to a project-level audit**. Prefer interactive/provider-managed OAuth; never commit, paste into logs, or request tokens in a PR or chat.
4. Before connecting an external service for organization use, establish the actual connection owner, exact resource/permission scope, revocation and evidence policy under [external tool entry](../contracts/tools/external-entry.md). Do not treat this proposal or a locally copied skill as admission or as permission to upload source code. No automatic CI, repository hooks, scheduled execution or write capability is enabled here.
5. If the runtime has no CodeScene tools, the repository is not registered, authentication is missing, provider terms/licensing are unaccepted, or a requested operation exceeds the verified envelope, **stop at `NOT_RUN` or `PARTIAL`** with the missing prerequisite. Do not simulate CodeScene scores.

## Read-only review workflow

For each **verified, explicitly selected** CodeScene project and mapped Git repository:

1. Record project identity, repository URL, default-branch SHA, CodeScene analysis date/version, accessible analysis period, and whether its dataset matches the selected Git revision. Record any missing/stale link as a limitation.
2. Select the project with the actual server-advertised project-selection tool; the upstream skill calls this `select_project` but names may vary by MCP release. **Discover available names and fail closed on unsupported calls.**
3. Use CodeScene's project-level technical-debt hotspot and goal tools, then inspect selected file-level hotspots/goals, code-health scores and supported change/churn evidence. Prioritize by **observed hotspots, churn and actual debt goals**, not by an invented repository-wide grade or a model-generated guess.
4. Preserve linked evidence and the actual tool/result identity for each finding. Distinguish measurable CodeScene data from human inference and from GitHub CI or VSM assessments.
5. Return a per-repository ranked shortlist with exact file paths, issue/risk, evidence links or recorded tool receipts, why it matters, minimal incremental fix proposal, and test suggestions. Escalate resulting implementation only through the relevant repository's existing task and PR process. **No automatic changes or issue publication** follow from a read-only audit.

## Required outcome report

Use one row per current in-scope repository; missing data must remain visible:

| Repository @ SHA | CodeScene project / analysis date | Coverage | Observed hotspots and technical-debt evidence | Suggested priority | Limitations |
| --- | --- | --- | --- | --- | --- |
| repo and immutable SHA | verified ID / dated run or `none` | `ASSESSED`, `PARTIAL` or `NOT_RUN` | source-backed paths and measurements or `none` | evidence-backed action or `unranked` | stale, missing, inaccessible or incomplete data |

A cross-repository summary is valid only for the actually covered set, with explicit exclusions. Do **not** turn the CodeScene Code Health scale into a universal OpenSiro VSM autonomy score. Findings may inform engineering work and future risk-focused testing, but cannot change canonical `A/C/P/—/?` ownership states or claim demonstrated S3* independence. Positive CI status does not independently validate CodeScene findings, and a CodeScene score does not establish correct VSM governance.

## Provenance, licensing and changes

The [CodeScene source](https://github.com/codescene-oss/codehealth-mcp) provides public agent skills and a mixed-license MCP implementation. We copy **only** the pinned public `prioritizing-technical-debt` instruction file, with attribution under its [upstream license notice](https://github.com/codescene-oss/codehealth-mcp/blob/main/LICENSE). Provider binaries, access subscriptions and the external connection are **not** redistributed or installed by this PR. Keep the upstream skill's instructions separate from this OpenSiro-specific review boundary. Future source upgrades require review against an explicit new upstream revision and applicable license/provider requirements.
