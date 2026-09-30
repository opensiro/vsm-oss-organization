# External tool / plugin entry contract

This contract defines how an external tool, plugin, connector, or integration is admitted into the Opensiro VSM Harness OSS organization operating environment.

It is supporting organizational infrastructure. A tool does **not** become S1, S2, S3, S3*, S4, or S5 merely because it exposes capabilities. Organizational function and ownership are classified from the actual decision or feedback right exercised in context.

## Purpose

For each admitted external capability, make reconstructable:

- external system/resource boundary;
- connection owner and runtime users;
- technical permissions;
- delegated, parent-gated, and forbidden organizational action classes;
- permission/resource drift behavior;
- narrowing/revocation path;
- durable evidence after disconnection.

## Function / mechanism boundary

```text
organizational decision or feedback right
        ↓ owned by S1 / S3 / S3* / parent / another function
external tool
        ↓ transports, exposes, or enforces capability
external system
```

A GitHub connector creating a branch does not own S1 judgment; a merge endpoint does not own integration policy; a ruleset API does not own S5; a search tool does not become S4 by reading external information.

## Required entry data

The canonical machine-readable shape is [`../../schemas/external-tool-entry.schema.json`](../../schemas/external-tool-entry.schema.json). Each entry identifies integration identity, external boundary, connection owner, runtime users, technical permissions, organizational action classes, revocation/intervention, failure behavior, re-entry triggers, and evidence retention.

## Action classes

- `READ_ONLY` — non-mutating inspection inside the admitted work/evidence boundary.
- `BOUNDED_MUTATION` — reversible/reviewable mutation inside already-admitted work.
- `INTEGRATION_SENSITIVE` — mutation of shared/default operating state; separately gated unless delegated.
- `POLICY_SECURITY_SENSITIVE` — authority/security/permission/connection changes; not ordinary delegated action.
- `FORBIDDEN` — technically available action outside the organizational envelope.

## Delegation rule

An action is delegated only when both:

1. the organizational function owning the substantive decision already has that right; and
2. the tool entry explicitly permits the corresponding external action/resource.

**The tool never widens organizational authority on its own.** If technical capability exceeds organizational delegation, the narrower organizational envelope wins.

## Parent-gated actions

Parent approval of a tool action is **not automatically an S5 event**. Count S5 only when the underlying matter is genuinely identity/ultimate-policy level under the parent-boundary contract. Routine enforcement of already-selected policy may remain support/enforcement.

## Failure / drift behavior

Fail closed when authentication/connection identity is unavailable, resource scope is unclear, permissions materially drift, external state contradicts assumptions, or the requested action is outside the explicit envelope.

Fail-closed means stop the affected action, preserve evidence/work where possible, report the mismatch, request re-entry/intervention where required, and never broaden scope silently to continue.

## Re-entry triggers

Review/re-admit when provider/integration identity, connection owner, runtime user class, technical permissions, resource scope, action mapping, authentication mode, revocation path, parent/delegation policy, or provider behavior materially changes.

## Evidence retention

Consequential external actions should leave durable evidence where practical: issue/PR/commit refs, pinned revisions, returned external identifiers/statuses, decision/control records, CI/validator results, or explicit failure/no-change records.

## GitHub reference entry

The first concrete entry is [`../../entries/tools/github-chatgpt.json`](../../entries/tools/github-chatgpt.json). It remains transport/support rather than a VSM function owner.
