# Provision the M1 executor GitHub App

This is the operator-side bootstrap for the concrete #35 reference profile in [`GITHUB_APP_EXECUTOR.md`](GITHUB_APP_EXECUTOR.md).

It intentionally covers only the narrow M1 proof capability. It does **not** define the later M2 parent-governance policy for installation authority, scope expansion, revocation, emergency control, or credential lifecycle.

## 1. Register the App

Create a **private** GitHub App owned by the OpenSiro organization.

Suggested fields:

| Field | Value |
|---|---|
| GitHub App name | `OpenSiro Executor Provenance` |
| Homepage URL | `https://github.com/opensiro/vsm-oss-organization` |
| Description | `Dedicated executor identity for bounded OpenSiro VSM provenance trials.` |
| Webhook | not required for the M1 reference path |
| User authorization / OAuth | not required |
| Public | disabled / owner-only |

The generated slug/bot login may differ from the display name. Record the actual values from GitHub after registration.

Do **not** commit the App private key, installation tokens, webhook secret, or any copied secret value into this repository.

## 2. Repository permissions

The reference path needs only repository-scoped mutation permissions required by the bounded S1 contribution plus evidence publication.

Start with:

| Permission | Access | Why |
|---|---:|---|
| Metadata | Read | implicit GitHub App repository metadata access |
| Contents | Read & write | create evidence branches/files and bounded code/doc commits |
| Issues | Read & write | bounded issue status/comments when the selected S1 task requires them |
| Pull requests | Read & write | open/update the bounded contribution PR when required |

No organization, administration, members, secrets, actions, deployments, environments, packages, or security permissions are required by the reference profile.

If a specific run does not need Issues or Pull requests mutation, mint the run token with those permissions reduced or omitted. The installation-token helper supports run-specific narrowing.

## 3. Events and webhooks

The M1 reference path is pull/push driven by the executor and does not need inbound webhook events.

Do not subscribe to events merely because the App UI offers them. Adding webhook/event subscriptions increases the capability surface without improving the #35 actor-attribution proof.

## 4. Install on selected repositories only

For the first trial, install the App using **Only select repositories**.

The minimum set is normally:

```text
opensiro/vsm-oss-organization   # provenance evidence publication
opensiro/vsm-harness-index      # first Index S1 trial
```

Add `vsm-harness-skills` and `awesome-vsm-harness` only when the corresponding #66 trial is ready, or install them together if operationally simpler and explicitly record the broader installation scope.

Installation scope is a capability boundary, not evidence that the App owns any VSM function.

## 5. Record non-secret identity facts

Record these public/non-secret facts for the witness:

```text
app_slug
app_id
installation_id
bot_login = <app-slug>[bot]
installed repositories
configured App permissions
```

The private key and installation token are verification credentials/capabilities and must remain outside committed evidence.

## 6. Keep the private key outside the repository

Store the downloaded PEM file outside the repository checkout with owner-only filesystem permissions.

Example local layout:

```text
~/.config/opensiro/executor-provenance/app.private-key.pem
```

On a POSIX host the file should normally be mode `0600`.

The helper [`../scripts/mint_github_app_token.py`](../scripts/mint_github_app_token.py) refuses a group/world-readable private key by default.

## 7. Mint a run-scoped installation token

GitHub installation access tokens are short-lived and can be narrowed to selected repositories and permissions. The helper creates the App JWT locally, resolves or accepts the installation id, requests a narrowed installation token, and writes the token to a mode-`0600` file without printing the secret to normal output.

Example for the first Index trial:

```bash
python scripts/mint_github_app_token.py \
  --app-id <APP_ID> \
  --private-key ~/.config/opensiro/executor-provenance/app.private-key.pem \
  --repository opensiro/vsm-oss-organization \
  --repository opensiro/vsm-harness-index \
  --permission contents=write \
  --permission issues=write \
  --permission pull_requests=write \
  --token-output /tmp/opensiro-executor-token
```

If the App has one installation covering the selected repositories, the helper can derive the installation id from the first repository. Use `--installation-id` when you want to bind the request to a known installation explicitly.

The resulting metadata printed by the helper includes the observed App slug/id, installation id, expiry, effective permissions, and selected repositories, but not the token itself.

## 8. Deliver the token to the executor session

For the reference publisher, expose the short-lived token only to the declared executor runtime/session:

```text
OPENSIRO_EXECUTOR_GITHUB_TOKEN=<contents of token file>
```

Do not paste the token into issues, PRs, provenance JSON, chat transcripts intended as public evidence, shell history, or committed environment files.

The positive #35 trust claim is:

> the short-lived installation token used for the run was delivered to the declared executor session and was not simultaneously used as an undeclared human execution credential.

If that claim is not supportable for a run, keep the ownership result `INSUFFICIENT` or add a stronger independent session binding.

## 9. Verify actor identity before the first S1 proof run

Before using the App for a substantive #66 run, perform a small create-only publication through [`../scripts/publish_executor_evidence.py`](../scripts/publish_executor_evidence.py).

The publisher fetches the resulting commit and fails unless GitHub reports the expected `<app-slug>[bot]` actor.

The test publication should be explicitly marked as provisioning verification rather than counted as the natural S1 ownership trial.

After verification, preserve:

- App public page reference;
- App id / installation id / bot login;
- selected repository scope;
- effective permission scope;
- the immutable test commit/action reference;
- observed GitHub actor.

Do not preserve the token or private key.

## 10. First real #66 run

Once actor verification succeeds, select a **natural bounded Index work item** and begin the actual run in the required order:

```text
freeze work item + start SHA + S1 role/contract
        ↓
publish pre-run anchor through App identity
        ↓
perform material S1 work through declared executor session
        ↓
publish ordered material event/action evidence
        ↓
close contribution / escalation
        ↓
publish closure + final witness
        ↓
independent second review
```

The pre-run anchor must exist before material S1 execution begins. A retrospectively reconstructed anchor is not a positive witness under this profile.

## What this setup does not prove

Successful installation, token minting, or a visible bot-authored commit proves only that the distinct capability path exists and can be attributed at GitHub's actor boundary.

It does not establish:

- `S1=A`;
- that every material decision was agent-owned;
- S3*, S3, S4, or S5;
- legitimate parent policy over the capability;
- absence of human intervention.

Those conclusions still require the witness, second review, and the governing Profile/Methodology analysis.