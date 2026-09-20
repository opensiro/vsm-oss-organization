# External tool / plugin entry contract

This document defines how an external tool, plugin, connector, or integration is admitted into the OpenSiro VSM Harness OSS organization operating environment.

It is supporting organizational infrastructure. A tool does **not** become S1, S2, S3, S3*, S4, or S5 merely because it exposes capabilities. Organizational function and ownership are classified from the actual decision or feedback right exercised in context.

The active formal milestone remains M1. This M2-supporting contract uses the parent-governed authority declared in `S5_PARENT_BOUNDARY.md` and `S5_PARENT_AUTHORITY.md` without claiming that every tool authorization is itself S5.

## Purpose

For each admitted external capability, make the following reconstructable:

- what external system and resources can be reached;
- who owns the connection and who may invoke it;
- what technical permissions exist;
- which organizational actions are delegated without per-action parent approval;
- which actions are parent-gated or forbidden;
- how permission/resource drift is handled;
- how the parent can narrow or revoke access;
- what evidence survives after the tool is disconnected.

Reference lifecycle:

```text
candidate external tool
        ↓
capability + risk inspection
        ↓
connection / authorization
        ↓
entry record + delegated-use envelope
        ↓
runtime invocation inside that envelope
        ↓
observable external result
        ↓
review / re-entry / narrowing / revocation
```

## Function / mechanism boundary

Always separate:

```text
organizational decision or feedback right
        ↓ owned by S1 / S3 / S3* / parent / another function
external tool
        ↓ transports, exposes, or enforces capability
external system
```

Examples:

- a GitHub connector creating a branch does not own the S1 implementation judgment;
- a merge endpoint does not own the decision to integrate work;
- a ruleset API does not own S5 merely because it can enforce policy;
- a search tool does not become S4 merely because it reads external information.

## Required entry data

The canonical machine-readable shape is `schemas/external-tool-entry.schema.json`.

Each admitted tool entry must identify:

1. **integration identity** — provider/tool name and entry id;
2. **external boundary** — service/account/organization/repository/resource scope;
3. **connection owner** — actor/role that can authorize, narrow, revoke, or replace the connection;
4. **runtime users** — agents/runtimes allowed to invoke it;
5. **technical permissions** — concrete observed/granted capabilities;
6. **organizational action classes** — how those capabilities map into delegated, parent-gated, or forbidden use;
7. **revocation/intervention path**;
8. **failure behavior**;
9. **re-entry triggers**;
10. **evidence retention** after disconnection.

Technical permission names are evidence about capability, not organizational policy by themselves.

## Action classes

Every concrete entry should classify actions using at least these local classes.

### `READ_ONLY`

Inspection that does not mutate the external system.

Examples: repository/file/issue/PR reads, status inspection, search, metadata retrieval.

Default policy: may be delegated when the underlying information is inside the admitted work boundary.

### `BOUNDED_MUTATION`

Reversible or reviewable mutation inside an already-admitted operational work item.

Examples: create/update an issue, create a feature branch, update files on that branch, open/update a PR, post a bounded work record.

Default policy: may be delegated when the relevant S1/metasystem contract already delegates the substantive decision and the target resource is in scope.

### `INTEGRATION_SENSITIVE`

Mutation that changes the shared/default operating state and can affect other participants or domains.

Examples: merge to a protected/default branch, close a system-wide control item, change a shared generated artifact when integration itself is separately gated.

Default policy: parent-gated or otherwise explicitly gated by the current Organization authority/enforcement model. This gate is an operational safeguard and is **not automatically S5**; classify the underlying decision separately.

### `POLICY_SECURITY_SENSITIVE`

Capability that changes authority, security posture, connection scope, credentials, or the policy/enforcement surface itself.

Examples: expand plugin scopes, install/replace an integration, change repository administration/rulesets, alter organization permissions, manage credentials/secrets.

Default policy: not delegated to ordinary agent operation. Requires explicit parent authorization or a separately established delegated governance path. Some instances may be genuine S5 matters when they change the delegated authority envelope; routine enforcement of an already-selected policy may not be.

### `FORBIDDEN`

Technically available capability that is outside the admitted organizational envelope.

The runtime must not use it merely because the API/tool exposes it.

## Delegation rule

An action is delegated only when **both** conditions hold:

1. the organizational function owning the substantive decision already has the right to make that decision; and
2. the tool entry explicitly allows the corresponding external action class/resource.

The tool never widens organizational authority on its own.

If the technical capability exceeds the delegated envelope, the narrower organizational envelope wins.

## Parent-gated actions

A parent gate is required when the current entry marks an action as parent-gated. The parent for this Organization recursion is declared in `S5_PARENT_AUTHORITY.md`.

Parent approval of a tool action is **not automatically an S5 event**. Count S5 only when the underlying matter is genuinely identity/ultimate-policy level under `S5_PARENT_BOUNDARY.md`.

Examples:

- approving one merge because current branch policy requires owner integration may be an operational integration gate rather than S5;
- expanding the delegated capability envelope for all agents may be an S5 matter if it changes ultimate policy/delegation;
- revoking a compromised connection can be emergency enforcement without redefining organizational identity.

## Failure / drift behavior

The runtime must fail closed when any of the following occur:

- authentication disappears or changes unexpectedly;
- resource scope cannot be established;
- granted permissions differ materially from the recorded entry;
- the external system reports state inconsistent with the work item's assumptions;
- a requested action is not explicitly classified inside the delegated envelope;
- the connection identity cannot be established.

Fail-closed behavior means:

1. stop the affected external action;
2. preserve the current work/evidence where possible;
3. report the observed mismatch;
4. request re-entry or parent intervention when required;
5. do not silently downgrade evidence or broaden scope to continue.

## Re-entry triggers

Review or re-admit an entry when any of these materially change:

- provider/integration identity;
- connection owner;
- runtime user class;
- technical permissions/scopes;
- reachable organizations/repositories/resources;
- delegated/parent-gated/forbidden action mapping;
- authentication mode;
- revocation path;
- relevant parent/delegation policy;
- provider behavior that changes the meaning/risk of an existing capability.

A version bump in provider software without a material boundary change does not automatically require organizational re-entry.

## Evidence retention

An external action that matters to organizational closure should leave durable first-party or stable external evidence where practical, such as:

- issue/PR/commit references;
- immutable or pinned revision identifiers;
- returned API identifiers/statuses;
- reviewable decision/control records;
- CI/validator results;
- explicit no-change/failure records.

Disconnecting the tool must not erase the only evidence needed to reconstruct a consequential organizational decision.

## GitHub reference entry

The first concrete entry is `entries/tools/github-chatgpt.json`.

For the current OpenSiro reference use:

- `READ_ONLY` repository/issue/PR inspection is delegated inside the admitted work boundary;
- bounded issue/branch/file/PR mutation is delegated when the owning S1/metasystem contract already delegates the substantive choice;
- default-branch integration remains explicitly gated by the current owner/integration policy;
- repository/org administration, integration installation/replacement, permission expansion, ruleset/security/credential changes are not ordinary delegated actions;
- the GitHub integration is transport/support and does not own VSM functions.

## Relationship to M2

This contract supports the already-explicit parent/delegation model:

- `S5_PARENT_BOUNDARY.md` defines the identity/ultimate-policy admission and return path;
- `S5_PARENT_AUTHORITY.md` declares the current legitimate parent arrangement;
- this document constrains how external capabilities may be used inside that policy envelope.

The existence of a connected tool or a parent-gated permission does not independently establish `S5=P`.
