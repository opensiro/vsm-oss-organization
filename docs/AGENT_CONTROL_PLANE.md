# OpenSiro OSS — agent control plane

**Purpose:** one human-facing agent interface for navigating, executing, and reporting work across the **currently bounded** public OpenSiro VSM Harness OSS organization. A maintainer can keep one conversation and issue instructions such as `status`, `continue`, or `continue Index #123` without manually rebuilding repository context on each turn.

**Status:** interface/contributor operating instructions, **not** an autonomous agent deployment, a new scheduler, a source of canonical facts, a grant of repository permissions, or evidence of S1/S2/S3/S3*/S4/S5 autonomy. It does not promise background execution or the ability to create independent agent sessions when no authorized runtime exists.

## Start and authority

On **every substantial invocation**, follow [START_HERE.md](../START_HERE.md) → [ECOSYSTEM.md](ECOSYSTEM.md) → the owning repository's **current default branch** → its exact issue/PR/release/frozen artifact. The authoritative organizational boundary is the `Current in-scope public repositories` list in [README.md](../README.md). Other public OpenSiro repositories, including experimental Capability, are **adjacent**, not silently admitted to this bounded control plane.

Use these existing contracts rather than replacing them:

- [docs/CONTROL_PLANE.md](CONTROL_PLANE.md): organizational authority, work lifecycle, upstream compatibility, and merge boundaries.
- [TODO.md](../TODO.md): only the selected cross-repository `NOW` / `NEXT` / `BLOCKED` schedule.
- [CONTRIBUTOR_START.md](../CONTRIBUTOR_START.md): intake/routing for new, unclassified, cross-repository, or authority-sensitive work.
- [AUTONOMOUS_WORK_REPORTING.md](AUTONOMOUS_WORK_REPORTING.md): the `DONE / NOW / BLOCKED / NEXT / NEED YOU` owner-facing status shape.
- [UPSTREAM_CONTRACT.json](../UPSTREAM_CONTRACT.json): Organization-selected upstream contract; exact historical work preserves its own pins.

The conversation is a **control surface**, not a second GitHub issue board, evidence database, reviewer identity, or organizational decision owner. Its remembered state is never authoritative over current owning repository records.

## Maintainer commands

| Say to the agent | Intended operation |
| --- | --- |
| `status` / `show OSS status` | Refresh canonical sources, summarize active milestone, scheduled work, relevant open issues/PRs, CI/gates and observed blockers; distinguish unscheduled issues from `TODO.md` selections. No write is implied. |
| `continue` | Continue a clearly identified already-admitted current work item from the conversation, otherwise follow `TODO.md` `NOW` then `NEXT`; re-check ownership/locks and do only the next legitimately admitted action. |
| `continue <repo> #<issue>` / `continue PR #<n>` | Resume that exact owner/issue/PR, subject to its independent/frozen/permission constraints. Do not silently switch to other batches or repos. |
| `start a batch assessment` | Route to Index, check current method, discovery queue, frozen identities and competing locks; create/execute only a legitimately admitted batch under Index rules. |
| `check PR review status` / `check S3* audit status` | Identify the **specific** semantic/PR/audit gate and its owner; do not conflate a harness S3* classification with Organization complementary audit. |
| `implement this change` / `open a PR` | Implement the scoped change through its owning repository, tests, an attributable PR and appropriate exact-head checks. |
| `S5: consider <matter>` | Request classification through the [parent-governed S5 entry](../prompts/parent-control-plane.md); the prefix does not confer parent decision authority. |

If a command does not name a work item, do **not** promote every open issue or PR into `TODO.md`. If `NOW` and `NEXT` are empty, report `no current scheduled item` and present genuinely eligible choices through [CONTRIBUTOR_START.md](../CONTRIBUTOR_START.md); do not pretend that the scheduler selected one. An explicit user-directed issue/PR can still be handled under its **own** admission contract without changing global scheduling.

## Per-command operating loop

1. **Resolve intent and scope.** Is this status-only, a named task, a selected current-work item, or new intake? Identify the declared system-in-focus and actual owning repository; preserve separate adjacent-research boundaries.
2. **Refresh authority.** Read current public bootstrap/owner state and the exact task record. Recheck task status, ref pins, current branch heads, PRs, claimed lanes, locks, CI and relevant ruleset/permissions. Never import a previous chat's assessment verdict into work requiring a fresh execution.
3. **Determine admissibility.** Apply the owning issue's ordering, read-only/frozen/independent limits, S1 admission/recovery contract and real stop rules. A GitHub issue's existence is not a cross-repository `NOW` selection or carte blanche to mutate it.
4. **Classify the actual gate.** Determine whether semantic review, formal GitHub approval, complementary Organization S3* audit, branch protection, exact-head CI, maintainer policy or a frozen-research independence condition is **really** required. Link to the rule that establishes it; do not invent a stronger default.
5. **Execute within authority.** Use available tools for the smallest authorized concrete action. Prefer reviewable PRs for meaningful changes. If one batch is serial, never skip locked `NEXT` rows or advance `WAITING` before canonical terminal evidence.
6. **Verify and return.** Recheck the exact resulting PR/commit, applicable validations, permitted merge and live owning `main`. If incomplete, state precisely what remains. Record durable progress at the owner before reporting; do not claim that a proposal or CI green is canonical admission.

On `continue`, do **not** stop after planning or demand routine confirmation when a valid, in-scope next action is executable. Conversely, never claim asynchronous work, automatic agent dispatch, a completed review, or a merge that did not actually occur. Work that is explicitly continuous or batched may proceed through its own bounded lifecycle; a default invocation does not silently expand into a new program.

## Independent review without forced new chats

**No automatic post-batch reviewer request.** Closing an ordinary Index assessment row or completing a ten-row batch does **not** by itself require announcing, creating, or waiting on a separate semantic-review task, fresh reviewer context, or Organization S3* audit. An Index `review PR` names the proposed assessment stage, not a second reviewing agent. Do not create a review issue or a `REVIEW_REQUESTED / UNASSIGNED` record simply because a batch ended or because zero reviewers are online. Continue ordinary Index PR/CI/admission under the real current contract and ruleset.

Separate reviewer execution is required **only when an explicit applicable owning task/review contract, actual repository approval requirement, or specific admitted investigation establishes that obligation**. Such an existing explicit contract must not be retrospectively waived by this document. Periodic Organization S3* audits (e.g. [#188](https://github.com/opensiro/vsm-oss-organization/issues/188)) have their own independent batch selection, frozen wave manifests, slots, provenance and finding-return; they do not automatically become a mandatory post-batch Index admission gate. A future every-50-canonical-assessments audit cadence, if separately admitted, would schedule audit work and track debt rather than impose a silent stop on ordinary Index publication.

Four distinct things must remain separate:

1. **The assessed harness's S3* grade** describes a function in the *harness*. It creates no OpenSiro reviewer requirement.
2. **Organization S3* complementary audit** is a claim-relative audit under its own admitted workstream, selection and locks. It is not routine Index PR review.
3. **Index semantic assessment review** is established by the *exact* Index issue/procedure, when required. A separate source-first/blind execution must use a real distinct context and original source before seeing the producer's proposal when that is the contract.
4. **GitHub PR approval/merge checks** are established by the current repo ruleset and applicable issue/branch policy. An independent evidence receipt or S3* `PASS` is not automatically a GitHub `APPROVED`, and a current ruleset with zero required approving reviews does not itself impose a new S3* wait gate.

Before telling the maintainer that a reviewer is needed, distinguish `EXPLICIT_TASK_REVIEW`, `REPO_APPROVAL_RULE`, `ORG_S3STAR_AUDIT`, and `OPTIONAL_OR_NOT_REQUIRED` **as reporting explanations**, not newly invented canonical workflow states. Cite the live governing source. Check whether a real eligible independent human/agent executor and required permissions exist.

One conversation may **coordinate** independent executions, but cannot manufacture them. Do not simulate independence by changing a role prompt, persona, model label, or reviewer name in a context already exposed to the producer's assessment. If the only available context is contaminated or no executor exists, preserve `REVIEW_REQUESTED / UNASSIGNED` (or the owner's actual equivalent), exact missing gate, and a source-only handoff packet **without claiming a first verdict**. Do not ask for a new ChatGPT chat as the automatic/default solution; a human decision or separately instantiated context is sought only when genuinely necessary and available. Continue other **independently admissible** work only where scheduling, locks and task scope permit.

For the prospective reviewer-handoff design and actor-provenance rules, see [Organization #189](https://github.com/opensiro/vsm-oss-organization/issues/189); a draft PR or unassigned packet is **not** a deployed reviewer. All Index assessment review/admission/canonical transitions remain Index-owned.

## Operator snapshot

After a meaningful state change, report compactly using the existing [reporting contract](AUTONOMOUS_WORK_REPORTING.md):

```text
DONE     — accepted outcomes, with owner PR / SHA / verified main when applicable
NOW      — selected current issue or named user-directed lane (state which)
BLOCKED  — exact unmet gate, evidence, responsible owner and next recovery
NEXT     — next permitted action, not merely a desirable task
NEED YOU — none, or the single real un-delegated human decision/input
```

Explain **what was actually executed**, and distinguish `proposed`, `reviewed`, `merged`, `admitted`, and `verified` instead of aggregating them as "completed". Prefer owner links over copying fast-changing queue sizes or corpus counts. If tools are absent, say what was not executed and provide a reviewable draft only; do not fabricate GitHub actions.

## Conformance scenarios (manual acceptance until automated tests exist)

- A normal Index assessment with no task-specific independent-review requirement and no required GitHub approving reviews is **not** sent to a mandatory S3* wait gate merely because no external agent is online.
- An Index issue explicitly requiring independent source-first review **stops at that gate** without a genuine eligible executor; same-chat role switching and PR/CI-only evidence fail closed.
- An Organization S3* `FINDING` is routed to its owning Index correction/adjudication work, **not** counted as accepted grade change or GitHub merge.
- A bare `continue` with empty `TODO.md` `NOW`/`NEXT` does **not** silently treat some unrelated open PR as current scheduled work.
- A named task with an existing frozen SHA or claimed serial row resumes that exact lane and preserves its locks; a stale issue checkpoint is checked against live owner state.

## Non-goals

No new global scheduler, shadow state database, unconditional independent-audit rule, agent spawning service, review rights, changed VSM grades, S3*/S5 authority, CI bypass or blanket merge delegation. This file is an **interface contract for an agent that already has appropriate tools and permissions**; executor provisioning and independent reviewer deployment remain separate work.
