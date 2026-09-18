# GitHub App executor / attester profile v1

This file defines the first concrete executor-identity profile for the runtime-neutral contract in [`EXECUTOR_PROVENANCE.md`](../EXECUTOR_PROVENANCE.md).

It is M1 proof infrastructure for #35. It does **not** redefine S1, autonomy, or parent governance, and the existence of this profile does not establish `S1=A`.

## Purpose

The profile gives a second reviewer a GitHub-visible actor boundary that is distinct from the contributor account:

```text
bounded agent run
        ↓
short-lived GitHub App installation token
        ↓
dedicated `<app-slug>[bot]` actor
        ├── pre-run anchor
        ├── material GitHub actions
        ├── ordered evidence records
        └── closure attestation

human contributor
        ↓
ordinary human GitHub identity / declared human-input channels
```

The GitHub App is supporting identity/evidence machinery. It does not become the owner of S1 or any other VSM function merely because GitHub attributes an action to its bot identity.

## Identity boundary

A conforming reference run MUST use a dedicated GitHub App whose bot actor is materially distinguishable from every declared human contributor identity used in the run.

Record:

- GitHub App slug and public app reference;
- App id;
- installation id used for the run;
- bot login, normally `<app-slug>[bot]`;
- repositories included in the installation-token scope;
- effective token permissions;
- token issuance / delivery evidence when available;
- declared human GitHub identities and other allowed human-input channels.

The App private key or installation token MUST NOT be committed to this repository or included in provenance artifacts.

For the M1 reference trial, a narrow pre-authorized installation token may be supplied to the executor session. Full policy over who may install the App, mint/expand/revoke credentials, or change repository scope remains M2 parent-governance work in #4/#36.

## Runtime binding

The positive trust claim is narrower than “a bot exists.”

A run may use this profile only when the declared trust basis says that the short-lived installation token for the run is delivered to the declared executor session and is not simultaneously available as an ordinary human execution credential.

If the same material App credential is knowingly available for undeclared human use during the run, the App actor alone cannot distinguish agent action from human action and the ownership witness MUST remain `INSUFFICIENT` unless another independent binding closes that gap.

The token may be minted by a parent/operator before the run. Token issuance is a support/authorization event; it does not transfer ownership of later in-boundary S1 choices to the minter.

## Evidence layout

Reference runs use create-only evidence objects under:

```text
provenance/runs/<run_id>/anchor.json
provenance/runs/<run_id>/events/0001.json
provenance/runs/<run_id>/events/0002.json
...
provenance/runs/<run_id>/closure.json
provenance/runs/<run_id>/witness.json
```

They MAY live initially on a run-specific evidence branch such as `provenance/<run_id>`. The final review should preserve immutable commit/blob references; merging the evidence branch later is useful for long-term reachability but is not itself ownership evidence.

Every publication performed as executor evidence MUST be made with the GitHub App installation token and MUST record the resulting immutable commit/action reference.

The helper [`scripts/publish_executor_evidence.py`](../scripts/publish_executor_evidence.py) implements a create-only publication path and verifies the actor reported by GitHub after publication.

## Pre-run anchor

Before the first material S1 mutation, publish `anchor.json` through the App identity.

The anchor contains at minimum:

- `run_id`;
- system-in-focus;
- declared S1 domain;
- target repository and frozen start SHA;
- work-item reference;
- exact S1 role/prompt ref and SHA-256 digest;
- selected/frozen upstream contract reference or digest;
- pre-start human constraints reference/digest;
- allowed post-start human-input channels;
- GitHub App identity/profile fields;
- declared human identities;
- payload digest.

The commit that first publishes this file is the immutable pre-run anchor reference used by the assembled witness.

A retrospectively written anchor after material work has already begun does not satisfy this profile.

## Ordered event record

Each organizationally material event is published as a separate create-only JSON object.

Events use a SHA-256 chain:

```text
first event.previous_event_digest = "GENESIS"
first event.event_digest = sha256(canonical(first event without event_digest))

next event.previous_event_digest = prior event.event_digest
next event.event_digest = sha256(canonical(next event without event_digest))
```

Canonical JSON is UTF-8 JSON with sorted keys and separators `,` / `:` and no insignificant whitespace.

Each event records:

- sequence and run-scoped event id;
- event kind;
- actor class and observable actor identity;
- observable decision/input/action summary, not hidden reasoning;
- authority classification;
- affected decision right when material;
- evidence refs;
- immutable GitHub action/result refs where applicable;
- the observed GitHub actor for material GitHub mutations;
- hash-chain fields.

For an `executor_action`, the observed GitHub actor must match the declared App bot login. A contributor-authored commit/PR/comment may still be useful evidence, but it is not an executor action under this profile.

## Human inputs and interventions

Every material post-start human input that can affect the run must be represented by a `human_input` or `human_intervention` event and attributed to a declared human identity/channel.

A human intervention does not automatically fail provenance. It changes ownership attribution for the affected decision right and must be reflected in `human_intervention_accounting`.

An undeclared material human channel or an intervention that cannot be attributed makes the relevant ownership claim insufficient.

## Closure

At the end of the run:

1. publish `closure.json` through the App identity;
2. assemble `witness.json` using [`github-app-executor-witness-v1.template.json`](github-app-executor-witness-v1.template.json);
3. compute `run_record_digest` over the ordered list of event digests;
4. compute the final binding digest over run id, anchor ref, run-record digest, closure artifact refs, final result revision, escalation status, and human-intervention status;
5. publish the final witness through the App identity;
6. preserve the final publication commit as `final_attestation.attestation_ref`;
7. have a second reviewer verify both the machine-readable witness and the primary GitHub actor/action evidence.

[`scripts/validate_executor_witness.py`](../scripts/validate_executor_witness.py) checks the structural and hash-chain invariants. It intentionally does not claim that local JSON validation proves the remote GitHub actor; the reviewer must inspect the cited primary GitHub references or use an independent GitHub API check.

## Contributor-only negative case

The ordinary contributor path is intentionally insufficient for this stronger witness.

The validator rejects the GitHub-App profile when:

- the declared bot login equals a declared human identity;
- executor actions are recorded with a different observed GitHub actor;
- no App-specific identity fields exist;
- the pre-run anchor/final attestation are not bound to the App profile;
- material human intervention is declared but not represented in the event record.

Thus an otherwise successful S1 PR authored only through the contributor account remains valid operational evidence but does not become executor-attribution evidence merely by being copied into this witness shape.

## Trust assumptions

A positive provenance verdict under this profile assumes all of the following are reviewable or explicitly accepted:

1. GitHub accurately reports the actor associated with App-authenticated mutations.
2. The declared App id/slug/bot login identify the intended dedicated executor path.
3. The run-scoped installation token was delivered to the declared executor session under the stated trust boundary.
4. Undeclared humans did not share or exercise that same executor credential during the run.
5. Material human inputs that reached the run are represented in the declared evidence boundary.
6. Immutable GitHub refs cited by the witness correspond to the artifacts/actions claimed.
7. The hash chain detects later modification/reordering of the committed event content under the stated evidence model.

This is strong operational provenance, not proof of hidden cognition. The final VSM ownership judgment still follows function → decisive right → owner → support → closure under the selected Profile/Methodology.

## Failure / insufficient cases

Record `FAIL / INSUFFICIENT` for the relevant ownership claim when, for example:

- the App token was available to both executor and undeclared human operator with no independent distinction;
- the first anchor was published after material execution began;
- an executor action points to a GitHub artifact whose observed actor is the contributor account;
- the event chain is broken or material events are missing;
- human intervention accounting contradicts the event record;
- the closure cannot be bound to the run and anchor;
- verification depends on private operator state unavailable to a second reviewer.

## M1 use

#35 supplies the implementation/evidence path. #66 then uses it for natural bounded runs across Index, Skills, and Awesome before any plane-wide `S1=A` conclusion is made.

A provenance `PASS` means the actor/run attribution chain is reconstructable under the declared trust assumptions. It is **not** by itself an `S1=A` verdict.