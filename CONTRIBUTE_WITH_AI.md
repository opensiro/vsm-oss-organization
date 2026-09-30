# Contribute to OpenSiro with AI

This is the human-facing contribution entry for the public OpenSiro VSM Harness ecosystem.

You do not need to reconstruct the repository architecture or learn every VSM/OSM control document before making a contribution. Give your AI agent the repository or idea you want to work on. The repository `README.md` is the common entry surface: an AI should follow its **I'm AI** route into the current public bootstrap and then follow the owning repository's contracts.

## I want to help, but I do not have a task yet

Give an AI agent with GitHub access:

```text
I want to contribute to OpenSiro.

Start from this repository:
https://github.com/opensiro/vsm-oss-organization

Treat its README.md as the common entry point and follow the "I'm AI" route.
Reconstruct the current public OpenSiro context from the canonical bootstrap it points to.

Find one appropriate currently tracked contribution, route it to the owning repository, and execute it through the normal review path.

Respect repository authority, task boundaries, admission rules, validation requirements, and source-of-truth boundaries.
Do not ask me to make routine implementation decisions that are already inside the delegated contribution boundary.

Return to me when:
- you have a reviewable result or pull request;
- genuine human input or authority is required; or
- the work cannot safely be admitted.
```

## I have an idea

Give the agent your idea together with:

```text
I want to contribute this to OpenSiro:

<idea>

Start from:
https://github.com/opensiro/vsm-oss-organization

Treat README.md as the common entry point and follow its "I'm AI" route.
Determine which repository owns the outcome, preserve its source-of-truth boundary, and take the work through the normal contribution process.
```

## I want to work on a specific repository or issue

Give the agent the repository or issue URL together with:

```text
Work on this OpenSiro contribution:
<repository or issue URL>

Start from the target repository's README.md when available. Follow its "I'm AI" entry route and the current public bootstrap it identifies before acting.

Follow the current owning repository, issue, authority, evidence, validation, and review contracts. Keep unrelated work out of scope.
```

## What the AI should do for you

The AI should reconstruct current context, identify the owning repository and exact work contract, decide whether the work can be admitted, perform routine in-boundary research or implementation, validate the result, recover from ordinary local failures, and produce a reviewable result, no-change conclusion, or explicit escalation.

## What remains human-owned

You choose broad intent and provide the accounts, credentials, budget, or access you want the runtime to have. Decisions that are genuinely reserved for human/parent authority remain human-owned; connecting a tool or giving an agent GitHub access does not widen its organizational authority by itself.

For AI runtimes, [`START_HERE.md`](START_HERE.md) remains the canonical machine bootstrap after the README handoff. [`CONTRIBUTOR_START.md`](CONTRIBUTOR_START.md) owns detailed routing for new or unclassified work, while [`TODO.md`](TODO.md) selects already tracked current work.