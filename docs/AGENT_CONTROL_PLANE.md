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
| `contribute to other harnesses` / `find upstream contribution opportunities` | Discover and present a fresh, actionable shortlist of **external** OSS harness contributions; ask whether the contributor wants optional public GitHub-profile tracking. Discovery is read-only and outside the bounded Organization S1 scheduler. See [External upstream contributions](#external-upstream-contributions). |
| `check PR review status` / `check S3* audit status` | Identify the **specific** semantic/PR/audit gate and its owner; do not conflate a harness S3* classification with Organization complementary audit. |
| `implement this change` / `open a PR` | Implement the scoped change through its owning repository, tests, an attributable PR and appropriate exact-head checks. |
| `S5: consider <matter>` | Request classification through the [parent-governed S5 entry](../prompts/parent-control-plane.md); the prefix does not confer parent decision authority. |

If a command does not name a work item, do **not** promote every open issue or PR into `TODO.md`. If `NOW` and `NEXT` are empty, report `no current scheduled item` and present genuinely eligible choices through [CONTRIBUTOR_START.md](../CONTRIBUTOR_START.md); do not pretend that the scheduler selected one. An explicit user-directed issue/PR can still be handled under its **own** admission contract without changing global scheduling.

## External upstream contributions

**Commands:** `contribute to other harnesses` (discovery), `find upstream contribution opportunities` (alias), or `contribute to <owner/repo>` / `contribute to <upstream issue URL>` (targeted intake). The first two **show choices**, not automatically choose a repository or open a PR. The contributor may select an offered opportunity, ask for a new shortlist, or supply a specific upstream issue.

**Boundary:** This is an **opt-in contribution-discovery interface for independent external OSS projects**, outside the bounded Organization S1 scheduler and not an admission of those projects into the five-repository OpenSiro organization, `TODO.md`, its S1 modes, or its decision rights. The external project's maintainers, current default branch, contributing/CLA/licensing/security rules, open issues, PR review and CI own acceptance. OpenSiro Index/Awesome are candidate-discovery inputs **only**; their assessment classifications never authorize upstream modifications or establish a need to improve a grade.

### Discovery and the offered list

On a discovery invocation, without requiring a GitHub username or permission to track it:

1. Re-establish the current OpenSiro bootstrap and read the owning Index/Awesome catalog as **discovery sources**; identify real public upstream harness repositories, not static hard-coded favourites. Check the current default branch and upstream primary sources for each shortlisted repository.
2. Prefer **upstream-native** opportunities backed by a live open issue, maintainer request, roadmap or documented product gap. Check `CONTRIBUTING`, licensing/CLA, repository activity, relevant code paths/tests, and existing open PRs before describing a change as actionable. A VSM S1-S5 assessment gap or potential grade uplift **alone is not an upstream need**. If a candidate lacks a first-party need signal, label it *speculative* rather than presenting it as approved work.
3. Reconcile against [the external intervention ledger](../experiments/upstream-intervention-fit/README.md) and current upstream PRs to avoid proposing a duplicate active intervention or confusing a replacement PR with a second contribution. Recent closed/merged interventions can inform lessons but do not imply another opportunity exists.
4. Display a **ranked but non-binding shortlist of about 5-10 eligible harnesses** when enough evidence exists. Each row must give: upstream repository link, **specific issue/problem and first-party evidence URL**, plausible minimal upstream-native patch, current upstream status/checked date, contributor prerequisites or CLA if known, active-PR/duplication risk, and confidence/effort. Offer fewer rather than inventing or padding the list; clearly distinguish open maintainer-backed tasks from speculative investigations and unknown prerequisites.
5. Ask which harness/issue the contributor wants to take. Do not create forks, branches, PRs, tracking tasks, or public records as a side effect of `show`/discovery. If no suitable first-party evidence exists, report that honestly and offer broader search/filtering instead of manufacturing changes.

### Optional contributor-profile tracking — explicit permission gate

After presenting the opportunities (or upon targeted contribution intake), **offer** a separate, non-blocking choice in plain language:

> May I check your **public GitHub profile and PR activity** for future contributions to other harnesses? If yes, which GitHub username should I use: **one-time scan** or **ongoing monitoring**? You can also decline; it will not affect your ability to contribute.

- **Default: OFF.** Do not infer permission from a linked GitHub tool, the logged-in account, a previous PR, profile URL, or merely invoking this command. Never silently enroll another contributor, scan that account's contribution history, or create a recurring task. If declined or unanswered, proceed with the shortlist and any selected upstream contribution without tracking. The contributor may provide PR links voluntarily.
- **One-time scan:** only after an affirmative choice and explicit public GitHub login; inspect public authored PRs relevant to external OSS harnesses. A match is a **candidate observation**, not proof that OpenSiro initiated the work. Cross-check original upstream PRs, commits and reviews before attribution or a durable ledger entry.
- **Ongoing monitoring:** requires a separate affirmative choice **plus a stated schedule/monitoring mechanism** accepted by the contributor. Set up monitoring only if an actually authorized recurring capability exists; otherwise offer a reusable manual check without claiming a background watcher. Scope it to the stated public login and public PR information, not private repositories, connected-account secrets, email, browsing history, or everyone who collaborated on a PR.
- **Storage and revocation:** distinguish permission to *look* from permission to *publish or store the monitored username or monitoring preferences* in a public repository. Do not commit a tracking roster or consent record publicly without a separate explicit publication decision. Allow the contributor to withdraw future monitoring permission; stop further scheduled scans where the environment permits. Do not promise retroactive deletion of independently public upstream GitHub evidence.
- **Anti-attribution shortcut:** a matching username, OpenSiro mention, or merged PR is not itself evidence of an OpenSiro-shaped intervention, human identity, equal participant credit, or `product_native_fit=pass`. The [ledger contract](../experiments/upstream-intervention-fit/README.md) governs inclusion, replacement-chain deduplication, participants and four evidence gates.

### Selected contribution execution and outcome

After the contributor **selects** a candidate or requests a specific upstream issue, treat the upstream as the **system-in-focus**: refresh its live default branch, exact issue/PR and contribution policy; record the intended product-native problem, smallest patch, permission/test gates and overlap with existing work. Do not substitute an OpenSiro assessment vector for a feature request. Read-only investigation can proceed without modification rights; pushing, PR creation and any integration-sensitive action require the actual user's/tool's authority and upstream rules. Use normal reviewable PRs, run relevant checks and record what *really* happened (proposed, opened, reviewed, merged, rejected, blocked).

When the work is materially initiated or shaped by OpenSiro assessment/research, preserve both successes and negative outcomes under `experiments/upstream-intervention-fit/observations.json` with evidence and regenerate `snapshot.json` through its owner computation contract; do **not** create a new intervention for each review fix, rebase, contributor, or replacement PR. Public profile tracking is **not required** for this manual evidence-backed recording. If the chosen work is independent of OpenSiro, do not falsely claim it as OpenSiro-generated impact. The ledger is experimental, separate from internal five-repo PR telemetry, canonical VSM assessments, the website, and productivity rankings.

Reporting after discovery should include the shortlist, provenance and unknowns, the **optional** profile-tracking question, and a clear choice of next upstream task. After execution report concrete upstream PR/commit/CI status and any ledger change; do not imply that a discovery command, follow-up scan or proposed contribution is a deployed continuous service.

## Per-command operating loop

1. **Resolve intent and scope.** Is this status-only, a named task, a selected current-work item, or new intake? Identify the declared system-in-focus and actual owning repository; preserve separate adjacent-research boundaries.
2. **Refresh authority.** Read current public bootstrap/owner state and the exact task record. Recheck task status, ref pins, current branch heads, PRs, claimed lanes, locks, CI and relevant ruleset/permissions. Never import a previous chat's assessment verdict into work requiring a fresh execution.
3. **Determine admissibility.** Apply the owning issue's ordering, read-only/frozen/independent limits, S1 admission/recovery contract and real stop rules. A GitHub issue's existence is not a cross-repository `NOW` selection or carte blanche to mutate it.
4. **Classify the actual gate.** Determine whether semantic review, formal GitHub approval, complementary Organization S3* audit, branch protection, exact-head CI, maintainer policy or a frozen-research independence condition is **really** required. Link to the rule that establishes it; do not invent a stronger default.
5. **Execute within authority.** Use available tools for the smallest authorized concrete action. Prefer reviewable PRs for meaningful changes. If one batch is serial, never skip locked `NEXT` rows or advance `WAITING` before canonical terminal evidence.
6. **Verify and return.** Recheck the exact resulting PR/commit, applicable validations, permitted merge and live owning `main`. If incomplete, state precisely what remains. Record durable progress at the owner before reporting; do not claim that a proposal or CI green is canonical admission.

On `continue`, do **not** stop after planning or demand routine confirmation when a valid, in-scope next action is executable. Conversely, never claim asynchronous work, automatic agent dispatch, a completed review, or a merge that did not actually occur. Work that is explicitly continuous or batched may proceed through its own bounded lifecycle; a default invocation does not silently expand into a new program.

## Independent review without forced new chats

**Prospective only:** [Independent Reviewer Batch coordination hypothesis](INDEPENDENT_REVIEWER_BATCH_HYPOTHESIS.md) describes how separately admitted review jobs *might* be batched and what evidence would be required before describing any part of that work as Organization S2. It is not an active batch command, reviewer deployment, added review obligation, S3 current-control decision, or M4 completion claim. Follow the live owning issue's gates, not the hypothesis, for execution.

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
