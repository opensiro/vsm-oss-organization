# OpenSiro OSS snapshot — on-demand, read-only

**Control Plane command:** `snapshot` (compatible alias: `OSS snapshot`).

This is an optional reproducibility capture for the **currently bounded** OSS
scope. It implements the lightweight convention recorded in [Organization
#314](https://github.com/opensiro/vsm-oss-organization/issues/314). It does not
establish an ecosystem-wide SemVer, a periodic release, a CI deployment, a new
VSM function, or a new source of canonical facts.

## Command behavior

1. Refresh [START_HERE.md](../START_HERE.md) → [ECOSYSTEM.md](ECOSYSTEM.md)
   and the current Organization default branch. Read the bounded repository set
   from its **pinned README**, not a hard-coded list, and the selected upstream
   dependencies from its **pinned `UPSTREAM_CONTRACT.json`**.
2. Observe the exact default-branch commit SHA of every in-scope repository.
   Capture selected Profile/Methodology release or commit refs independently
   of their potentially newer default-branch heads. Resolve the Index active
   contract at the exact source selected by Organization.
3. Check selected Profile and Methodology version markers, matching Methodology
   selection with Index, and the declared compatible/no-impact Profile release
   path when the Index Profile basis differs. Recheck all default-branch heads
   after the read; if any change, or a source/contract is unavailable, **fail
   closed** without a verified snapshot.
4. Return a JSON manifest with UTC capture time, repository names, default
   branches, full SHAs, selected dependency refs/SHAs, Index contract and the
   exact result of the deterministic checks. Explain that this is a stable
   *observed vector*, **not a globally atomic GitHub transaction**. Contract
   consistency does not prove semantic correctness or agent autonomy.

One local implementation (Python standard library, public GitHub REST API):

```bash
python3 scripts/oss_snapshot.py
```

The default command prints JSON to stdout and makes **no remote writes**. An
optional explicit local path saves one file without overwriting it:

```bash
python3 scripts/oss_snapshot.py --output /path/to/new-snapshot.json
```

`GITHUB_TOKEN` or `GH_TOKEN` may be used for GitHub API rate limits; the public
read-only route does not inherently require a token. In a chat environment
where a shell is unavailable, an agent may use an authorized GitHub read
connector to obtain the same pinned facts and checks. If it cannot establish
the required evidence, it must return `BLOCKED` / `UNVERIFIED`, never fabricate
a manifest or call partial checks `PASS`.

## Persistence and usage

`snapshot` is **capture only**. It does not create GitHub commits, tags,
releases, issues, PRs, background jobs or scheduler entries. The operator may
retain the output as a research/audit attachment or request a separately
reviewable Organization PR to preserve it in Git. No automatic archive or
fixed publication cadence is required.

Snapshots describe historical inputs and remain immutable if later published;
they do not change `UPSTREAM_CONTRACT.json`, Index provenance, pinned research
inputs or which work is selected in `TODO.md`. Follow a snapshot's own SHA
links for reproduction, never `latest`.

## Acceptance examples

- All six current heads are stable, selected Methodology matches Index, and
  selected Profile is equal/compatible-with-no-impact → checked JSON.
- Skills default branch is newer than Organization's selected Methodology
  release → **not drift by itself**; record both current head and selected SHA.
- Index selects a different Methodology than Organization → `BLOCKED`.
- Selected Profile transition requires targeted reassessment/explicit review
  → `BLOCKED` rather than a silent migration.
- A repository head moves while capture is running, or one API read fails →
  `BLOCKED`; retry as a new capture. No partial verified snapshot.
