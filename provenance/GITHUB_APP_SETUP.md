# GitHub App executor setup — human guide

This guide takes an OpenSiro owner or maintainer from **no GitHub App** to a verified distinct executor identity that can be used by the M1 provenance mechanism in [`GITHUB_APP_EXECUTOR.md`](GITHUB_APP_EXECUTOR.md).

You do not need to understand the full provenance format before following this guide. The important security boundary is simple:

```text
PUBLIC / safe to record
App name / slug / App ID / installation ID / bot login
installed repositories / effective permissions / immutable action refs

SECRET / never commit or paste into public evidence
GitHub App private key (.pem)
App JWT
installation access token
credential-bearing shell history, logs, env dumps, or config files
```

This setup creates proof-enabling infrastructure only. It does **not** by itself prove `S1=A`, establish S5, or complete M1.

## Before you start

You need:

- owner/admin ability to create a GitHub App for the `opensiro` organization;
- a local machine or trusted runtime where the private key can be stored outside the repository;
- Python 3.12+ for the repository helpers;
- the repository checked out locally if you want to use the helper scripts.

For the first proof run, keep the capability narrow. The normal initial repository set is:

```text
opensiro/vsm-oss-organization
opensiro/vsm-harness-index
```

Do not add Skills/Awesome until their #66 runs are ready unless you deliberately want the broader installation scope.

## Step 1 — create the GitHub App

Create a **private** GitHub App owned by the OpenSiro organization.

In GitHub, use the organization settings path for GitHub Apps. GitHub may move labels over time; the current official documentation is linked under [GitHub references](#github-references).

Suggested fields:

| Field | Value |
|---|---|
| GitHub App name | `OpenSiro Executor Provenance` |
| Homepage URL | `https://github.com/opensiro/vsm-oss-organization` |
| Description | `Dedicated executor identity for bounded OpenSiro VSM provenance trials.` |
| Webhook | disabled / not required |
| User authorization / OAuth | not required |
| Public | disabled / owner-only |

The display name, slug, and resulting bot login are related but not identical. After GitHub creates the App, record the actual values it shows.

## Step 2 — grant only the repository permissions needed

Start with this repository permission set:

| Permission | Access | Why |
|---|---:|---|
| Metadata | Read | repository metadata; GitHub grants this implicitly |
| Contents | Read & write | evidence branches/files and bounded commits |
| Issues | Read & write | bounded issue updates/comments when needed |
| Pull requests | Read & write | bounded contribution PRs when needed |

Do **not** grant organization administration, members, secrets, actions, deployments, environments, packages, or security permissions for this M1 path.

The installation may have the permissions above while an individual run token is narrowed further. A run that only needs `contents=write` should not receive extra permissions merely because the App could receive them.

## Step 3 — generate the private key

After creating the App, open its settings page and find **Private keys** → **Generate a private key**.

GitHub downloads a `.pem` file to your computer. GitHub retains only the public portion; the downloaded PEM is the secret that lets a holder authenticate as the App and mint installation tokens.

Treat it like a root credential for this App.

### Move it out of Downloads immediately

Recommended local location on a POSIX machine:

```text
~/.config/opensiro/executor-provenance/app.private-key.pem
```

Then restrict access:

```bash
mkdir -p ~/.config/opensiro/executor-provenance
mv ~/Downloads/<downloaded-key>.pem ~/.config/opensiro/executor-provenance/app.private-key.pem
chmod 600 ~/.config/opensiro/executor-provenance/app.private-key.pem
```

If your download path differs, adjust the first path. Do not move the key into the repository checkout even temporarily.

The helper [`../scripts/mint_github_app_token.py`](../scripts/mint_github_app_token.py) refuses a group/world-readable private key by default.

### Optional: verify that the local key matches GitHub

GitHub shows a SHA-256 fingerprint for the public/private key pair. You can compare it with the fingerprint derived locally:

```bash
openssl rsa \
  -in ~/.config/opensiro/executor-provenance/app.private-key.pem \
  -pubout -outform DER \
| openssl sha256 -binary \
| openssl base64
```

Compare the result with the fingerprint displayed for that key in the App settings.

Do not paste the key contents into an issue, PR, chat, provenance JSON, CI log, or troubleshooting screenshot.

## Step 4 — install the App on selected repositories

Install the App using **Only select repositories**.

For the first trial select:

```text
opensiro/vsm-oss-organization
opensiro/vsm-harness-index
```

Installation scope is only a capability boundary. It is not evidence that the App owns an organizational function.

After installation, record these **non-secret** facts:

```text
app_slug
app_id
installation_id
bot_login = <app-slug>[bot]
installed repositories
configured App permissions
```

It is safe for these values to appear in public provenance evidence.

## Step 5 — mint a short-lived installation token

Do not use the private key directly for ordinary repository writes. The normal flow is:

```text
private key
    ↓ signs
short-lived App JWT
    ↓ requests
short-lived installation token
    ↓ narrowed to
selected repositories + permissions
    ↓ used by
one declared executor session
```

Use the repository helper for the first Index trial:

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

If the App has one installation covering the selected repositories, the helper can derive the installation id from the first repository. Use `--installation-id` when you want the request bound to a known installation explicitly.

The helper prints non-secret metadata such as App identity, installation id, expiry, effective permissions, and repository scope. It does **not** print the token itself.

The token file is written create-only with mode `0600`.

GitHub installation access tokens normally expire after one hour. Mint a new one for a later run instead of attempting to make this credential long-lived.

## Step 6 — deliver only the installation token to the executor

The executor session needs the short-lived installation token, not the App private key.

For the reference publisher:

```text
OPENSIRO_EXECUTOR_GITHUB_TOKEN=<contents of /tmp/opensiro-executor-token>
```

Preferred boundary:

```text
owner-controlled private-key store
        ↓ mint token
short-lived narrowed token
        ↓ one-way delivery
bounded executor session
        ↓ GitHub actions
<app-slug>[bot]
```

Do not give the executor the long-lived `.pem` unless the runtime itself is explicitly the trusted credential broker. For the M1 reference path, keeping the private key outside the executor session makes the trust boundary easier to review.

Never store the token in:

- the repository;
- `.env` committed to git;
- an issue or PR body/comment;
- provenance JSON;
- a public chat transcript;
- shell commands that will be retained in shared history;
- CI/debug output that prints environment variables.

## Step 7 — verify the bot actor before doing proof work

Before starting a substantive #66 S1 run, perform a small provisioning verification using [`../scripts/publish_executor_evidence.py`](../scripts/publish_executor_evidence.py).

The verification must answer one simple question:

> Does GitHub independently report the resulting action as performed by the expected `<app-slug>[bot]` actor rather than the human contributor account?

The publisher fetches the resulting commit and fails if the observed GitHub actor does not match the expected bot identity.

Mark this test explicitly as **provisioning verification**. Do not count it as the natural Index S1 trial.

Keep the following public evidence:

- App slug/id;
- installation id;
- bot login;
- selected repository scope;
- effective permissions;
- immutable test commit/action reference;
- actor GitHub reports for that action.

Do not preserve the private key, JWT, or installation token.

## Step 8 — start the first real #66 run

Only after actor verification succeeds, choose a **natural bounded Index work item**.

The order matters:

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

The pre-run anchor must be published **before** material S1 execution. A retrospectively reconstructed anchor is not positive provenance evidence under this profile.

After Index, #66 repeats the ownership exercise for Skills and Awesome because their local decision rights differ.

## Step 9 — end the session cleanly

At the end of a run:

1. publish the closure/final witness;
2. remove the local installation-token file;
3. unset/remove the token from the executor environment;
4. retain only public identity facts and immutable action references;
5. keep the private key in its protected owner-controlled location for future token minting.

Example cleanup:

```bash
rm -f /tmp/opensiro-executor-token
unset OPENSIRO_EXECUTOR_GITHUB_TOKEN
```

An expired token is no longer useful, but removing local copies reduces accidental disclosure and makes the operating procedure easier to audit.

## Step 10 — rotate or revoke the private key when needed

GitHub App private keys do not automatically expire. Rotation/revocation is therefore an owner responsibility.

Rotate the key when:

- it may have been copied to an untrusted machine or log;
- a maintainer who had access should no longer retain it;
- the credential-storage boundary changes;
- you want scheduled hygiene even without a known incident.

Safe rotation order:

```text
generate a new private key in GitHub
        ↓
store + verify new key locally
        ↓
confirm token minting works with new key
        ↓
delete/revoke the old key in GitHub
        ↓
securely remove obsolete local copies
```

If you suspect compromise, stop using the old key and revoke it as soon as you have a replacement path. Any still-valid installation token minted before revocation should also be treated as exposed and removed/revoked where practical.

## What is safe to publish?

| Item | Public? | Notes |
|---|---:|---|
| App display name | yes | identity metadata |
| App slug | yes | identity metadata |
| App ID | yes | identifier, not credential |
| Installation ID | yes | identifier, not credential |
| `<app-slug>[bot]` login | yes | required for actor verification |
| Repository scope | yes | useful evidence of capability boundary |
| Effective permissions | yes | useful evidence of capability boundary |
| Commit / PR / issue refs | yes | primary evidence |
| Private key PEM | **no** | long-lived App credential |
| App JWT | **no** | bearer credential used to request installation tokens |
| Installation token | **no** | bearer credential for repository actions |
| Credential-bearing env/log dump | **no** | may contain any of the above |

Knowing App ID, installation ID, bot login, repository scope, or permissions is not sufficient to authenticate as the App. The private key / derived bearer credentials are the capability secrets.

## Repository-side safety net

The repository `.gitignore` ignores the common local private-key/token filenames used by this guide. That is only a convenience guardrail: `.gitignore` is **not** a secret-management system and does not protect a secret that was already committed, pasted into GitHub, logged, or otherwise published.

If a secret is ever committed, assume compromise and rotate/revoke it. Removing the file in a later commit is not sufficient because git history may retain it.

## What this setup does not prove

A visible bot-authored action proves that the distinct capability path exists and that GitHub attributed that action to the App actor.

It does not by itself establish:

- `S1=A`;
- that every material decision was agent-owned;
- S3*, S3, S4, or S5;
- legitimate parent policy over the capability;
- absence of human intervention.

Those conclusions still require the witness, second review, and governing Profile/Methodology analysis.

## GitHub references

GitHub's current public documentation:

- [Managing private keys for GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps)
- [Generating an installation access token for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app)
- [Best practices for creating a GitHub App](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/best-practices-for-creating-a-github-app)
