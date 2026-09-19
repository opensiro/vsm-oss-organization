# GitHub App executor setup — human guide

This guide takes an OpenSiro owner or maintainer from **no GitHub App** to a verified distinct executor identity for the M1 provenance mechanism in [`GITHUB_APP_EXECUTOR.md`](GITHUB_APP_EXECUTOR.md).

Each step includes the relevant GitHub or repository link so the setup can be followed linearly without a separate shortcuts page.

## Security boundary

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

You need owner/admin ability to create a GitHub App for the `opensiro` organization, a trusted local machine/runtime for the private key, Python 3.12+, and a local checkout if you want to use the repository helpers.

For the first proof run, keep the capability narrow:

```text
opensiro/vsm-oss-organization
opensiro/vsm-harness-index
```

Do not add Skills/Awesome until their #66 runs are ready unless you deliberately want broader installation scope.

---

## Step 1 — create the GitHub App

**Open:** [Create the OpenSiro Executor Provenance App with pre-filled settings](https://github.com/organizations/opensiro/settings/apps/new?name=OpenSiro%20Executor%20Provenance&description=Dedicated%20executor%20identity%20for%20bounded%20OpenSiro%20VSM%20provenance%20trials.&url=https%3A%2F%2Fgithub.com%2Fopensiro%2Fvsm-oss-organization&public=false&webhook_active=false&contents=write&issues=write&pull_requests=write)

Fallback: [Manage OpenSiro GitHub Apps](https://github.com/organizations/opensiro/settings/apps) · [GitHub registration docs](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app)

The pre-filled creator supplies the suggested name, description, homepage, private visibility, disabled webhook delivery, and initial repository permissions. Review the form before submitting it.

Expected values:

| Field | Value |
|---|---|
| GitHub App name | `OpenSiro Executor Provenance` |
| Homepage URL | `https://github.com/opensiro/vsm-oss-organization` |
| Description | `Dedicated executor identity for bounded OpenSiro VSM provenance trials.` |
| Webhook | disabled / not required |
| User authorization / OAuth | not required |
| Public | disabled / owner-only |

After creation, record the actual App slug and App ID GitHub assigns.

---

## Step 2 — review the App permissions

**Open:** [Manage OpenSiro GitHub Apps](https://github.com/organizations/opensiro/settings/apps)

The reference M1 path needs only repository-scoped permissions:

| Permission | Access | Why |
|---|---:|---|
| Metadata | Read | implicit repository metadata access |
| Contents | Read & write | evidence files/branches and bounded commits |
| Issues | Read & write | bounded issue actions when required |
| Pull requests | Read & write | bounded PR actions when required |

Do **not** grant organization administration, members, secrets, actions, deployments, environments, packages, or security permissions for this path.

The App may be configured with the permissions above while an individual installation token is narrowed further for a specific run.

---

## Step 3 — generate and store the private key

**Open:** [Manage OpenSiro GitHub Apps](https://github.com/organizations/opensiro/settings/apps) → select `OpenSiro Executor Provenance` → **Private keys** → **Generate a private key**

Reference: [Managing private keys for GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps)

GitHub downloads a `.pem` file. Treat it as the long-lived root credential for this App.

Move it outside the repository checkout immediately. Recommended POSIX layout:

```bash
mkdir -p ~/.config/opensiro/executor-provenance
mv ~/Downloads/<downloaded-key>.pem ~/.config/opensiro/executor-provenance/app.private-key.pem
chmod 600 ~/.config/opensiro/executor-provenance/app.private-key.pem
```

The helper [`../scripts/mint_github_app_token.py`](../scripts/mint_github_app_token.py) refuses a group/world-readable private key by default.

Optional local fingerprint check:

```bash
openssl rsa \
  -in ~/.config/opensiro/executor-provenance/app.private-key.pem \
  -pubout -outform DER \
| openssl sha256 -binary \
| openssl base64
```

Compare it with the fingerprint GitHub displays for that key.

Never paste the PEM contents into an issue, PR, chat, provenance JSON, CI log, or screenshot.

---

## Step 4 — install the App on selected repositories

**Open:** [Manage OpenSiro GitHub App installations](https://github.com/organizations/opensiro/settings/installations)

Install using **Only select repositories**. For the first trial select:

```text
opensiro/vsm-oss-organization
opensiro/vsm-harness-index
```

After installation, record these **non-secret** facts:

```text
app_slug
app_id
installation_id
bot_login = <app-slug>[bot]
installed repositories
configured App permissions
```

Installation scope is a capability boundary, not evidence that the App owns a VSM function.

---

## Step 5 — mint a short-lived installation token

**Open:** [`scripts/mint_github_app_token.py`](../scripts/mint_github_app_token.py)

Reference: [Generating an installation access token](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app)

Use the private key only to mint a short-lived, narrowed installation token:

```text
private key
    ↓ signs
short-lived App JWT
    ↓ requests
short-lived installation token
    ↓ narrowed to
selected repositories + permissions
```

First Index-trial example:

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

The helper prints non-secret metadata such as App identity, installation ID, expiry, effective permissions, and repository scope. It does **not** print the token itself.

The token file is create-only and mode `0600`. Mint a new token for later runs rather than making this credential long-lived.

---

## Step 6 — deliver only the installation token to the executor

**Reference:** [GitHub App security best practices](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/best-practices-for-creating-a-github-app)

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

Do not place the token in committed `.env` files, issues/PRs, provenance JSON, public chats, shared shell history, or debug output.

---

## Step 7 — verify the bot actor before proof work

**Open:** [`scripts/publish_executor_evidence.py`](../scripts/publish_executor_evidence.py) · [`EXECUTOR_PROVENANCE.md`](../EXECUTOR_PROVENANCE.md) · [issue #35](https://github.com/opensiro/vsm-oss-organization/issues/35)

Before substantive S1 work, publish a small **provisioning verification** action through the App credential path.

The verification question is:

> Does GitHub independently report the resulting action as performed by the expected `<app-slug>[bot]` actor rather than the human contributor account?

The publisher fetches the resulting commit and fails if the observed GitHub actor does not match the expected bot identity.

Keep public evidence for the App slug/id, installation ID, bot login, repository scope, effective permissions, immutable test action reference, and observed GitHub actor. Do not preserve the key, JWT, or token.

This provisioning test is **not** the natural #66 S1 ownership run.

---

## Step 8 — start the first real #66 run

**Open:** [issue #66 — S1 ownership evidence across all declared S1 domains](https://github.com/opensiro/vsm-oss-organization/issues/66) · [`roles/S1.md`](../roles/S1.md) · [`S1_DOMAIN_CONTRACTS.md`](../S1_DOMAIN_CONTRACTS.md)

Only after actor verification succeeds, choose a **natural bounded Index work item**.

Required order:

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

The pre-run anchor must exist **before** material S1 execution. A retrospectively reconstructed anchor is not positive provenance evidence under this profile.

After Index, #66 repeats the ownership exercise for Skills and Awesome because their local decision rights differ.

---

## Step 9 — close the executor session cleanly

**Open:** [`EXECUTOR_PROVENANCE.md`](../EXECUTOR_PROVENANCE.md) for the closure/witness contract.

At the end of the run:

1. publish closure/final witness;
2. remove the installation-token file;
3. remove the token from the executor environment;
4. retain only public identity facts and immutable action references;
5. keep the private key only in its protected owner-controlled location.

```bash
rm -f /tmp/opensiro-executor-token
unset OPENSIRO_EXECUTOR_GITHUB_TOKEN
```

Removing local copies reduces accidental disclosure even after a short-lived token has expired.

---

## Step 10 — rotate or revoke the private key when needed

**Open:** [Manage OpenSiro GitHub Apps](https://github.com/organizations/opensiro/settings/apps) → select the App → **Private keys**

Reference: [Managing private keys for GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps)

Rotate when the key may have been exposed, a maintainer should lose access, the credential-storage boundary changes, or as scheduled hygiene.

Safe rotation order:

```text
generate new private key
        ↓
store + verify new key locally
        ↓
confirm token minting works
        ↓
delete/revoke old key in GitHub
        ↓
remove obsolete local copies
```

If a secret is ever committed or published, assume compromise. Removing it in a later commit is not sufficient because git history may retain it.

---

## What is safe to publish?

| Item | Public? | Notes |
|---|---:|---|
| App display name | yes | identity metadata |
| App slug | yes | identity metadata |
| App ID | yes | identifier, not credential |
| Installation ID | yes | identifier, not credential |
| `<app-slug>[bot]` login | yes | actor-verification evidence |
| Repository scope | yes | capability-boundary evidence |
| Effective permissions | yes | capability-boundary evidence |
| Commit / PR / issue refs | yes | primary evidence |
| Private key PEM | **no** | long-lived credential |
| App JWT | **no** | bearer credential |
| Installation token | **no** | bearer credential |
| Credential-bearing env/log dump | **no** | may expose credentials |

Knowing the public identifiers is not sufficient to authenticate as the App. The private key and derived bearer credentials are the capability secrets.

## Repository-side safety net

The repository `.gitignore` ignores the common local private-key/token filenames used by this guide. This is only a convenience guardrail, not secret management.

## What this setup does not prove

A visible bot-authored action proves that the distinct capability path exists and GitHub attributed that action to the App actor. It does not by itself establish `S1=A`, agent ownership of every material decision, S3*/S3/S4/S5, legitimate parent policy over the capability, or absence of human intervention.

Those conclusions still require the witness, second review, and governing Profile/Methodology analysis.
