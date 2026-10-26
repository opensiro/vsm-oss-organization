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

## OSM-aware delegation and authority transfer

**Trigger:** the operator asks to transfer autonomy from a human to an agent, widen an agent's standing mandate, reduce repetitive approvals, or reconcile an execution gate with VSM/OSM. Do **not** answer by treating the most restrictive current adapter as the desired organizational design. Re-establish the current default-branch [OSM Roadmap](ROADMAP.md), the selected [Profile semantics](ECOSYSTEM.md), [S1 domain/admission contracts](../contracts/s1/domain-contracts.md), [S1 runtime](../modes/s1-autonomous/README.md), and [S5 authority](../contracts/s5/parent-authority.md), then the owning repository/issue.

Use this **function-first decision-right check**, while preserving any task-specific fresh-context/read-only/frozen gates:

1. **Local variety/outcome:** which concrete operational S1 result is produced and who has requisite information? Keep ordinary local planning, implementation, validation and recovery at the lowest domain with an **effective** delegated right; do not centralize them in S5 or manufacture S3/S2/S4.
2. **Decisive right and owner:** list the decisions the agent already owns, decisions still owned by a human or external maintainer, and decisions proposed for future transfer. Distinguish organizational authority from GitHub push permission, connector capability, branch rules, and CI enforcement.
3. **Decide at the correct recursion:** a change to the *bounded Organization's delegation model or organizational boundary* is reserved to its legitimate [S5 parent](../contracts/s5/parent-authority.md). The parent has now selected Upstream S1 membership under [#274](https://github.com/opensiro/vsm-oss-organization/issues/274#issuecomment-6420871211), but this membership decision does not establish new live external-write rights. Upstream's actual repository/fork owner must still issue separately effective local stage grants when required. Those are different rights; for either scope the issuer/actor, expiry/revocation and return/application must be effective **before** exercising new rights.
4. **Bounded execution:** when an effective, verifiable mandate and provider capabilities already cover the action, execute ordinary S1 decisions without repeatedly demanding task-level approval. Otherwise preserve the existing gate and do as much read-only/source preparation as allowed. Do not substitute a proposal digest, generic `continue`, GitHub login, `authorize=True`, or this section for authority.
5. **Feedback and autonomy evidence:** record who really decided, what validation and recovery occurred, human interventions, and how the result affected subsequent S1 work. Assess `A/C/P/—/?` only under the owning Skills Methodology/selected Profile; these are **ownership arrangements, not sequential maturity levels**. A contract, runnable tool, CI pass, or grant by itself is not positive autonomy evidence.

**Upstream S1 (boundary selected; general executor prospective):** the [fourth S1 envelope](../contracts/s1/domain-contracts.md#upstream-contributions-domain) covers source-backed external issues, bounded native-tested fixes, authorized working branches, recovery, maintenance and attributable outcomes. Outside separately authorized cases, the operator retains the **external PR publication decision**, and external maintainers retain acceptance/merge. See [Upstream #6](https://github.com/opensiro/upstream/issues/6). General fork/patch/PR rights remain subject to independent effective grants and actual provider/host capabilities. [Organization #274](https://github.com/opensiro/vsm-oss-organization/issues/274#issuecomment-6420871211) decided the organizational boundary, **not** a standing fork-creation port or autonomy grade. No code/doc change or stage-specific live authorization is implied by domain admission alone.

**Finite Corrective publication mandate (operator decision, 2026-10-23):** the owner expressly authorized public `opensiro-contributions` forks/working branches and external **Draft PRs without per-case reapproval for only 34 fixed, source-tested Corrective cases**. See the Upstream-owned [mandate](https://github.com/opensiro/upstream/blob/main/docs/CORRECTIVE_PR_PUBLICATION.md), [ledger](https://github.com/opensiro/upstream/blob/main/data/corrective-publication/2026-10-23-01.json), and [handoff](https://github.com/opensiro/upstream/blob/main/docs/NEXT_SESSION_CORRECTIVE_PR_PROMPT.md). This exhausted finite cohort is **not** renewed or enlarged by later S1 admission. Every write still needs an authenticated actor, sufficient rights, fresh source, contributor-policy/duplicate checks and provider readback. License/CLA/DCO/issue-assignment gates can block a row. This owner decision does **not** activate the general Upstream P1 mandate, grant external merges, or assign a VSM autonomy grade. Only actual external PR receipts establish `SUBMITTED`.

**Upstream batch continuation (operator direction, 2026-10-22):** when the *already selected exact work* is [Upstream #56](https://github.com/opensiro/upstream/issues/56), `continue`/`продолжай` means apply the [Upstream-owned frozen assessment-candidate batch contract](https://github.com/opensiro/upstream/blob/main/docs/ASSESSMENT_CANDIDATE_BATCHES.md), not stall at the same technically prepared case. Record an honest per-candidate `AWAITING_EXTERNAL` handoff and move to the next eligible **Index-first** screening row. Do not extend this meaning to unrelated work, infer an exact-stage grant or create an Organization scheduler entry. Technical gates use **native deterministic source/CLI scripts only; live LLM-agent/model-provider/Browser quality runs are prohibited**. This rule is neither the S5 boundary decision nor an external-write permission.

When responding, prefer a small **current owner → target owner → exact change/authority needed → observable closure** matrix over a blanket permission prompt. Escalate only the residual, actually un-delegated decision; do not elevate routine S1 variety merely because a human has GitHub credentials.

## Parent S5 decision before assessment

For a request to establish S3 for the Organization, choose its domain, mandate or holder, route the **governance decision** to the legitimate S5 parent before evaluating any individual S3 intervention. The parent can approve prospective/conditional authority even without an incident or positive `S3=C` assessment. A particular **operational S3 action** still needs a real whole-system case and effective delegated rights. An **assessment grade** requires its own evidence and never grants or revokes authority.

Do not interpret an `INSUFFICIENT` grade or missing live case as a veto over a legitimate parent's prospective decision. Do not treat a design-only S5 choice or a generic `continue` as appointment or activation. See [S5 parent authority](../contracts/s5/parent-authority.md) and the [source-based failure review](reviews/2026-10-14-s5-s3-assessment-gate-inversion.md).

## First-contact action menu (client-adaptive presentation)

`START_HERE.md` is the discovery/bootstrap entry; **this document owns the command mappings and behavior**. On a bare bootstrap/control-plane/help request with no named task, show a compact **OpenSiro Control Plane** panel rather than a wall of repository instructions. A concrete user task always takes precedence over the introductory panel.

Before offering live status, read the current Organization scope and `TODO.md` and relevant owner records. Show a short, **source-linked, time-of-check** `NOW / BLOCKED / NEXT` snapshot only for facts actually verified. If GitHub or required tools cannot be reached, mark the snapshot `unverified / read-only`, explain the access limitation, and avoid inventing a current queue or enabled operations.

| Visible action | Command dispatched on selection | Initial behavior |
| --- | --- | --- |
| **OSS Status** | `status` | Read-only live status and gates. |
| **Roadmap** | `show OSS roadmap` | Read-only milestone/roadmap view; check live tracker issues and distinguish goals from demonstrated evidence. |
| **Continue Work** | `continue` | Re-evaluate `TODO.md` `NOW`/`NEXT`, current conversation target, locks and admission; report `no current scheduled item` if none. |
| **Batch Assessment** | `start a batch assessment` | Route to Index and apply Index discovery/admission/serial-lock rules before any write. |
| **PR Review** / **S3* Audit** | `check PR review status` / `check S3* audit status` | Separate read-only gate inspections; never fabricate independent review. |
| **Current Control (S3)** | `S3: inspect current control` | Read-only source-first intake across actual S1 operations; **does not itself create an S3 decision or witness**. |
| **Contribute Upstream** | `contribute to other harnesses` | Read-only opportunity discovery first; optional contributor-profile monitoring is a later **explicit opt-in**. |
| **Prepare Upstream Change** | `prepare upstream contribution` | Prepare and display one exact **read-only** action packet from the Upstream-owned contract; no branch, fork, PR or human approval implied. |
| **S1 Function Test (Upstream)** | `test S1 function: upstream contributions` | **Assessment-driven** fourth-S1 evidence test: start from a pinned Index harness assessment, qualify a native change, then inspect preparation/execution/return. Read-only by default; no new write or autonomy-grade inference. |
| **Open Issue or PR** | `continue <repo> #<issue>` / `continue PR #<n>` | Ask for an exact target when missing; do not dispatch a literal placeholder or guess across repositories. |
| **Propose Change** / **S5 Matter** | `open a PR` / `S5: consider <matter>` | Require the actual scope/matter and all owner/parent permission gates. |

**Render rules:**

- Prefer **real native buttons/action controls** supported by the current chat client; their click action must dispatch the mapped command as a *new user-selected request*, not execute hidden work while constructing the menu. Labels may match the user's language; underlying command semantics remain stable. Do not invent platform-specific JSON, code, fake Markdown links that look like buttons, or claim that GitHub Markdown itself runs agent actions.
- If interactive controls are not supported, render the **same high-value actions** as one concise numbered text menu with exact copyable command strings; accept typed commands, natural-language requests and issue/PR links equally. No UI library, hosted service, plugin or new runtime is required for this fallback.
- Present useful **read-only options without requiring write permissions**. Do not imply a mutating action is available when tools/credentials are absent. Selection may yield an explicit permission blocker or reviewable draft; a rendered button is never delegation or evidence of execution.
- Do not initiate `continue`, batch execution, a GitHub write, S5 escalation, a reviewer session or profile monitoring merely because the panel was displayed. An affirmative menu selection still passes through the [per-command operating loop](#per-command-operating-loop) and the owning authorization/independence gates. A blocked `continue` must not silently select some unrelated open issue.
- Do not turn this presentation into a global scheduler, S2 coordination owner, S3 controller, S3* reviewer, or S5 policy authority. The panel is a view/control **interface** over existing GitHub-backed contracts, never their replacement.

## Maintainer commands

| Say to the agent | Intended operation |
| --- | --- |
| `status` / `show OSS status` | Refresh canonical sources, summarize active milestone, scheduled work, relevant open issues/PRs, CI/gates and observed blockers; distinguish unscheduled issues from `TODO.md` selections. No write is implied. |
| `show OSS roadmap` | Show current milestones and next admissible milestone work, using live Organization milestone tracker issues/owner evidence alongside `docs/ROADMAP.md`; distinguish planned target vectors from established construction/evidence state. Read-only. |
| `continue` | Continue a clearly identified already-admitted current work item from the conversation, otherwise follow `TODO.md` `NOW` then `NEXT`; re-check ownership/locks and do only the next legitimately admitted action. |
| `continue <repo> #<issue>` / `continue PR #<n>` | Resume that exact owner/issue/PR, subject to its independent/frozen/permission constraints. Do not silently switch to other batches or repos. |
| `start a batch assessment` | Route to Index, check current method, discovery queue, frozen identities and competing locks; create/execute only a legitimately admitted batch under Index rules. |
| `contribute to other harnesses` / `find upstream contribution opportunities` | Discover and present a fresh, actionable shortlist of **external** OSS harness contributions; ask whether the contributor wants optional public GitHub-profile tracking. Discovery is read-only and outside the bounded Organization S1 scheduler. See [External upstream contributions](#external-upstream-contributions). |
| `test S1 function: upstream contributions` | Inspect the **assessment-driven** Upstream S1 loop: pinned canonical Index assessment → harness finding → independently verified upstream-native fit → bounded authorized action → validation/feedback. Follow [Upstream test contract](https://github.com/opensiro/upstream/blob/main/docs/ASSESSMENT_DRIVEN_S1_TEST.md), [#6](https://github.com/opensiro/upstream/issues/6) and [S5 decision #274](https://github.com/opensiro/vsm-oss-organization/issues/274#issuecomment-6420871211). The test grants no external writes or autonomy grade. |
| `prepare upstream contribution` / `prepare upstream contribution <source/issue>` | After source-first discovery and one specific proposed candidate, route to the **Upstream-owned** [Control Plane handoff](https://github.com/opensiro/upstream/blob/main/docs/CONTROL_PLANE_HANDOFF.md). Read-only: present one pinned `prepare_contribution` action for **separate exact operator confirmation**; never infer authorization from this command. |
| `check PR review status` / `check S3* audit status` | Identify the **specific** semantic/PR/audit gate and its owner; do not conflate a harness S3* classification with Organization complementary audit. |
| `implement this change` / `open a PR` | Implement the scoped change through its owning repository, tests, an attributable PR and appropriate exact-head checks. |
| `assess OpenSiro S3` / `reassess M1 #39` | Conduct a **source-first VSM assessment** of the Organization S3 function and its first-party decision/feedback constructor under [#39](https://github.com/opensiro/vsm-oss-organization/issues/39); live operation is optional for `C`, and case intake is **not** the grade gate. See [assessment proof rules](#m1-s3-source-first-assessment-vs-live-case-intake). |
| `S3: inspect current control` / `S3: consider <present choice>` | Run [pre-admission S3 intake](../prompts/intake-s3-current-control.md) for a real current Organization-wide decision. No S3 transaction, owner discretion or classification is implied by invoking this command. |
| `S5: consider <matter>` | Request classification through the [parent-governed S5 entry](../prompts/parent-control-plane.md); the prefix does not confer parent decision authority. |

If a command does not name a work item, do **not** promote every open issue or PR into `TODO.md`. If `NOW` and `NEXT` are empty, report `no current scheduled item` and present genuinely eligible choices through [CONTRIBUTOR_START.md](../CONTRIBUTOR_START.md); do not pretend that the scheduler selected one. An explicit user-directed issue/PR can still be handled under its **own** admission contract without changing global scheduling.

## Operational current-commitment regulation (S3 candidate constructor)

The [standing shared-commitment contract](../contracts/s3/standing-current-commitments.md) owns the already-binding selected-Methodology and canonical Index→Awesome continuity subjects; `python scripts/s3_current_regulation.py --help` exposes a read-only whole-current-contract observation and bounded **unselected** G1 current-regulation options. It does **not** convert automatic compatibility checks into an S3 choice or turn an open Issue into admitted work. S3 functional assessment remains separate from individual case admission, and actual application always follows the existing G1 and S1 return contracts.

## M3 D1-A autonomous S3 (source-prepared, not active)

The operator selected the narrow **D1-A design** for implementation. The first-party [autonomous S3 mode](../modes/s3-autonomous/README.md) and [RUN protocol](../modes/s3-autonomous/RUN.md) specify an **agent-owned** decision/return path, but its separate [D1-A grant](../contracts/s3/autonomous-d1a.json) is deliberately `PENDING_S5_PUBLIC_ATTESTATION`; it does **not** inherit human G1. The [operator-selection handoff](../records/s5/2026-10-15-m3-d1a-selection-handoff.md) is recorded by an assistant, not authenticated public S5 authorship. No agent may run a current-control decision until a separately attributable owner act, concrete runtime identity, bounded published grant and live revocation checks are established. Run `python scripts/check_s3_d1a_gate.py contracts/s3/autonomous-d1a.json --agent-id <attested-agent-execution-id>` only as a **negative/readiness check**; even its hypothetical structural success is never live authority. Keep M3 `S3=A` assessment separate, and do not alter Index/Skills/Awesome S1 decisions.

**OSS deployment boundary — owner clarification (2026-10-15):** OpenSiro is an **OSS reference ecosystem**, not a required operator of a hosted autonomous S3 service. Setting up, selecting or maintaining an ecosystem-operated Docker/Python worker, GitHub Actions runner, always-on agent, dedicated bot-account infrastructure, or provider-specific runtime is **EXCESSIVE / NOT REQUIRED** for M3 merely to make this code available or conduct a source-first assessment. Do not repeatedly propose a runtime deployment or turn one into a new M3 prerequisite. Consumers may bring their own compatible execution host and credentials; keep implementation interfaces and supported first-party source evidence reviewable without an OpenSiro-managed deployment. This operational-scope clarification **does not** change the current D1-A grant, invent an S5 authorization, dispense with real actor ownership and authorization when an agent actually operates, or grant a positive `S3=A` from dormant code alone. Evaluate autonomy and reachable decision→S1 return/feedback on their genuine primary-source evidence; report insufficiency where that evidence is missing. No automatic service launch, runtime selection, or synthetic transaction follows from this note.

## M1 S3 source-first assessment vs live case intake

**Two independent evidence questions:**

1. **VSM assessment of whether `S3=C` is established** (command `assess OpenSiro S3`). Follow [M1 #3](https://github.com/opensiro/vsm-oss-organization/issues/3) / [#39](https://github.com/opensiro/vsm-oss-organization/issues/39), current owning source pins, selected Profile/Methodology and the [post-G1 source-first assessment](reviews/2026-10-15-s3-c-post-g1-source-first-reassessment.md). Reconstruct (a) **an established inside-and-now whole-system current-control function/variety** over real Index/Skills/Awesome operations, including a **source-evidenced standing first-party regulatory rule or arrangement** even if no specific intervention has yet occurred; (b) the **S3-specific decisive right/feedback path** and legitimate owner or composable authority; (c) the dedicated **first-party, boundary-reachable construction** and its return into subsequent S1 work; (d) falsifiers that would instead make this S1/S2/S3*/S5, generic policy, routing or deterministic CI. Record distinct `established` / `conditional` / `not established` findings and concrete source anchors. **No executed S3 decision, current incident, `REQUESTED` transaction, live S1 receipt, agent-owned control or provider-backed test is universally required for Methodology `C`**. A static label, template, G1 mandate or plausible future story alone is also **not** evidence that the function is established. Do not mark lack of a live case as the sole failure. A positive source-first functional assessment may establish `C` without a live operational transaction; a negative assessment must identify the actual missing **function/right/path** precisely, not simply demand a run. Distinguish `C(P)` (distinct operationally closed parent mode), `A` (autonomous agent-owned loop), and frozen historical results.
2. **Admission of one actual G1 S3 intervention** (commands `S3: inspect current control` / `S3: consider <present choice>`). This is **operational case governance**, not the Methodology `C` assessment threshold. It requires a real present matter, source-backed S1 targets, attributable authorized human choice under an effective non-revoked grant, and actual application/effect closure. None of those case events may be simulated or inferred from an assessment verdict.

**Reassessment loop:** perform the assessment first; if it identifies an implementable first-party **functional** gap with a legitimate owning task, repair via reviewable PR and tests, then reassess. If the only missing fact is an unobserved whole-system right/obligation, do not code more validators/monitoring or manufacture intervention. CI verifies artifact integrity only, not the semantic grade. Keep Index semantic grade choices with **Index S1**; do not transfer third-party harness assessment disputes to human S3/S5 or revive the deprecated independent reviewer mechanism.

## S3 current-control intake (M1)

The **Current Control (S3)** menu action dispatches only `S3: inspect current control`; a typed `S3: consider <present choice>` may identify an existing present-tense cross-Organization choice. Both read the current [S3 intake](../prompts/intake-s3-current-control.md), [S3 contract](../contracts/s3/current-control.md) and [M1 #39](https://github.com/opensiro/vsm-oss-organization/issues/39) after the shared bootstrap. They are distinct from the **S3* Audit** action (complementary verification), `continue` (scheduled work), and **S5 Matter** (ultimate policy). Showing the action does not trigger it.

The initial inventory is **read-only**. A new `REQUESTED` transaction is not admissible until facts establish existing S1 work, a concrete whole-system current resource/commitment/constraint choice, an authorized and explicitly attributed decisive owner, specific S1 return targets and observable closure criteria. Preserve local S1 and S2 authority. The actual owner must make the decision; the panel, selected menu item, operator prompt, issue/PR comment or generic user `continue` cannot impersonate that decision. After a real owner decision, apply the existing [S3 → S1 return procedure](../prompts/apply-s3-control.md), and verify application/effects separately.

If the current evidence does not establish a genuine present S3 matter or legitimate authority, report **no S3 transaction**, the exact missing evidence/owner decision and permissible next source check. No manufactured budget conflict, no standing autonomous S3 agent, no change to the historical pre-assessment, and **no `S3=C` promotion** on menu integration, intake or CI success. M1 is developed on the roadmap rather than on an emergency schedule; classification remains evidence-driven.

## External upstream contributions

**Commands:** `contribute to other harnesses` (discovery), `find upstream contribution opportunities` (alias), or `contribute to <owner/repo>` / `contribute to <upstream issue URL>` (targeted intake). The first two **show choices**, not automatically choose a repository or open a PR. The contributor may select an offered opportunity, ask for a new shortlist, or supply a specific upstream issue.

**Boundary:** This is an **opt-in Upstream S1 discovery interface for independent external OSS projects**. Those external projects remain **outside** the six-repository Organization and are not individually admitted to `TODO.md` or granted Organization decision rights. The external project's maintainers, current default branch, contributing/CLA/licensing/security rules, review and CI own acceptance. Index/Awesome are candidate-discovery inputs only; their grades never authorize external changes.

### S1 function test — Upstream Contributions

**Command:** `test S1 function: upstream contributions`.

This command tests **automation of contributions to AI agent harnesses originating
from canonical OpenSiro Index assessments**. Its starting point is the assessment
corpus, **not** a familiar project, a random GitHub issue, or the current Upstream
registry. Use the current Index default branch and its exact assessment source
and revision, then rediscover the assessed upstream repository and compare its
**current** source, policies and review state. Do not preselect Cognee or any
other historical example as the test target. The standalone
`contribute to other harnesses` command still provides general OSS discovery;
it does **not** substitute for this assessment-driven test.

This is a read-only-by-default **S1 construction/evidence test** for the fourth admitted domain, not
a new permission envelope or autonomy grade. Index, Skills and Awesome retain their functions. [Organization #274](https://github.com/opensiro/vsm-oss-organization/issues/274#issuecomment-6420871211)
already records the formal S5 boundary decision; it does not authorize external writes.
The Upstream owner defines the [assessment-driven S1 test contract](https://github.com/opensiro/upstream/blob/main/docs/ASSESSMENT_DRIVEN_S1_TEST.md);
[Upstream #6](https://github.com/opensiro/upstream/issues/6) owns implementation
and actual stage capability.

Follow these gates **in order**; do not promote a later GitHub opportunity over a
failed earlier Index-evidence gate:

| Test point | Required evidence | Fail-closed boundary |
| --- | --- | --- |
| 1. Assessment discovery | Canonical Index assessment path at exact Index commit SHA; assessed system identity/upstream URL, actual function/ownership findings and source evidence | An issue URL alone, a low VSM grade, or an unpinned remembered result is **not** an assessment-driven candidate |
| 2. Candidate qualification | Derive a falsifiable engineering hypothesis from that assessment; refresh the harness upstream default branch, current code, contributor policy and overlapping PRs | The assessment does not prove a software bug, right to change code, or need for a higher VSM grade |
| 3. Product-native fit | Separately check source-backed upstream need, native implementation mechanism, useful counterfactual **without any VSM branding**, and fit with current upstream scope | If need/fit is not supported, report `NO_ELIGIBLE_ASSESSMENT_CANDIDATE` / `BLOCKED_EVIDENCE`; do not fall back to generic issue hunting or manufacture work |
| 4. Propose and select | Trace `Index assessment → harness/finding → evidence → proposed change → tests`; present Upstream `proposal_only` candidate IDs and independently selected stages | Preview selection/hash is not authorization; no silent project substitution |
| 5. Execute only if separately authorized | Actual GitHub actor/grant, destination, stage, tested diff/branch and verified provider rights | Existing [Upstream #6](https://github.com/opensiro/upstream/issues/6) live gates prevail; an old fork does not prove `create_public_fork`, and a test command is not permission to write |
| 6. Validate, recover and return | Tested artifact and real receipts or precise blocker, human interventions, upstream review disposition when available and what feedback changes later work | A green mock CI or internal PR does not prove an upstream contribution, acceptance, full S1 closure or autonomy |

On each invocation: refresh [Index](https://github.com/opensiro/vsm-harness-index)
and discover candidate harness assessments **before** selecting one; inspect
the owning assessment, [Upstream #6](https://github.com/opensiro/upstream/issues/6),
current Upstream `main`, [Organization #274](https://github.com/opensiro/vsm-oss-organization/issues/274)
and present S1 rights. Preserve assessment provenance (including historical
source pin) without rewriting Index grades. For an eligible candidate report
an evidence/decision/feedback matrix including assessed function, hypothesized
patch, independent native-fit evidence, available stage, who really decides,
what was exercised, and observed or missing closure. If no assessment yields a
source-backed candidate, finish the **discovery test** honestly with no
contribution selected; do not switch to a convenience upstream issue.

Return stage observations as `SOURCE_PREPARED / OBSERVED / EXERCISED / CLOSED /
BLOCKED / UNKNOWN`, and say `PARTIAL` or `INSUFFICIENT` for unproven end-to-end
closure. These are descriptive test findings, **not** canonical VSM grades.
The command itself is **read-only**: it cannot create forks/branches, push
patches, open external PRs, change `TODO.md`, activate credentials or issue a
standing agent mandate. A separately named operational action must pass its
own current actor, consent, policy, tool, per-stage and readback gates.
Preserve the [Skills-owned assessment methodology](https://github.com/opensiro/vsm-harness-skills),
the deferred [Organization #276](https://github.com/opensiro/vsm-oss-organization/issues/276)
autonomy investigation and all S5 rights. No `S1=A`, `S1=C` or `S1=C(P)`
follows from this contract or a successful technical test.

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

### Control Plane → Upstream preparation handoff (one stage, read-only)

**Command:** `prepare upstream contribution` (or `prepare upstream contribution <source/issue>`).
This is the **existing conversation Control Plane**, not a second interface, a
new Organization S1 domain, a deployment or a new GitHub credential pathway.
Resolve this command only after the user chooses one real external source and
candidate; discovery, `prepare`, `approve`, `execute` and `close` are
separate decisions/states. The implementation owner is
[`opensiro/upstream` → `CONTROL_PLANE_HANDOFF.md`](https://github.com/opensiro/upstream/blob/main/docs/CONTROL_PLANE_HANDOFF.md),
not Organization's `TODO.md` queue.

1. **Refresh:** start at the canonical bootstrap and current default branches,
   refresh [Upstream #6](https://github.com/opensiro/upstream/issues/6),
   the real target's issue/source/CLA/contribution instructions, the owner
   of the *existing* writable fork and any overlapping PR. Resolve ambiguity
   before presenting a plausible executable action.
2. **Proposal and selection:** use Upstream-owned
   [`batch_proposals.py`](https://github.com/opensiro/upstream/blob/main/scripts/batch_proposals.py)
   with `--draft`, selected ID and `--scope`. No `selection_scope_sha256`,
   `PROPOSAL_PREVIEW` or claimed `approved_by` proves permission. Reject
   blocked candidates and missing `prepare_contribution` from its proposed
   stages.
3. **Exact action:** use the Upstream-owned **read-only**
   [`control_plane_handoff.py`](https://github.com/opensiro/upstream/blob/main/scripts/control_plane_handoff.py)
   to bind exactly **one** candidate and `prepare_contribution` to the
   existing working fork, pinned 40-hex base SHA, new `opensiro/...` branch,
   new `tests/` file and proposed UTF-8 content SHA-256. Display the packet
   and meaningful test plan in chat; `ACTION_PREPARED_NOT_AUTHORIZED` is
   always **no-write**, not a grant.
4. **Ask for an exact decision:** the operator must explicitly approve or
   decline **this candidate, stage, existing working repo, pinned base SHA,
   new branch, path and content digest**, after seeing the specific change.
   Generic `продолжай`, `подтверждаю`, approval of implementing Control
   Plane itself, a prior chat or a menu click does **not** authorize the
   particular external write. A draft packet, hash or model-authored text
   cannot authenticate the human; only a trusted current-session host can
   establish the actor and applicable instruction. If unavailable: **BLOCKED**.
5. **Execute only if separately allowed:** the host must supply an actual
   trusted current-session `authorize(intent)` and a connected GitHub API
   port to Upstream's
   [`connected_stage_adapter.py`](https://github.com/opensiro/upstream/blob/main/scripts/connected_stage_adapter.py).
   The current published code is **source-prepared, not host-connected**.
   Recheck consent envelope, content bytes/digest, target's rules/license,
   public matching fork and push rights, pinned branch SHA, and absence
   of a colliding branch/file **before any write**. The adapter must never
   be bypassed by directly calling a writer just because ChatGPT can
   access GitHub. If the necessary host binding cannot actually be
   enforced, report the missing capability and **do not write**.
6. **Return real receipts:** `BLOCKED`, `FAILED`, `PARTIAL`,
   `PENDING_VERIFICATION` or `CREATED_VERIFIED`, backed by exact refs.
   Branch creation does not imply test validation, an upstream PR, merged
   upstream outcome or S1 autonomy. Source-first evidence and negative
   outcomes return to Upstream #6 when relevant.

**Hard stops:** this stage does not implement `create_public_fork`,
`submit_external_pr`, archiving, a token/runner or public tracking of user
identity. No staged permission carries into another stage, another project
or a future session. No fallback to `UPSTREAM_FORK_TOKEN`, legacy
`create_fork.py --execute` or workflow dispatch. The current
Organization S1 domains are Index, Skills, Awesome and Upstream; **#274 does not activate this live write stage**.
Do not display this feature as an active write-capable button or claim a
successful operator-confirmed external pilot without exact evidence.

### Selected contribution execution and outcome

After the contributor **selects** a candidate or requests a specific upstream issue, treat the upstream as the **system-in-focus**: refresh its live default branch, exact issue/PR and contribution policy; record the intended product-native problem, smallest patch, permission/test gates and overlap with existing work. Do not substitute an OpenSiro assessment vector for a feature request. Read-only investigation can proceed without modification rights; pushing, PR creation and any integration-sensitive action require the actual user's/tool's authority and upstream rules. Use normal reviewable PRs, run relevant checks and record what *really* happened (proposed, opened, reviewed, merged, rejected, blocked).

When work is materially initiated or shaped by OpenSiro assessment/research, preserve successes and negative outcomes under `experiments/upstream-intervention-fit/observations.json` with evidence and regenerate `snapshot.json` under its Organization-owned contract; do **not** create a new intervention for each review fix, rebase or replacement PR. Public profile tracking is **not required** for this manual evidence-backed recording. Independent work must not be falsely attributed to OpenSiro. The experimental ledger remains separate from internal six-repo PR telemetry, canonical VSM assessments, the website and productivity rankings.

Reporting after discovery should include the shortlist, provenance and unknowns, the **optional** profile-tracking question, and a clear choice of next upstream task. After execution report concrete upstream PR/commit/CI status and any ledger change; do not imply that a discovery command, follow-up scan or proposed contribution is a deployed continuous service.

## Internal assessment → repair → reassessment loop

When the operator asks to *assess our own OpenSiro organization, implement what the assessment finds missing, and repeat*, make the **bounded Organization system** the assessment target; external harness grade repair remains Index S1. Run the following cycle within the actual owning task and authority:

1. **Assess current first-party evidence** under the Organization-selected Profile and Methodology; separate **established VSM function**, ownership/autonomy, technical prerequisites and real organizational permissions. Record a falsifiable precise gap with source refs. A missing *real current obligation or owner act* is not a missing code file.
2. **Implement only an actionable admitted gap** at its owning first-party source, preferably one small reviewable PR with regression tests. Do not manufacture S3 incidents, introduce new human review gates or rewrite normative upstream semantics.
3. **Validate the exact changed head**, and where legitimately permitted integrate via GitHub's real checks. Then **reassess against that new source**, explicitly distinguishing a repaired tool/guard from newly proven whole-system S3 function, G1 parent `P` closure or autonomous `A`.
4. Repeat while a new source-supported **implementable** gap remains in scope; otherwise report the exact non-code evidence or owner-decision blocker, and show the owner the actual completed change, limitations and next entry condition. Do not loop identical `INSUFFICIENT` source scans, schedule unsupervised background work, or create a fresh reviewer task.

**Concrete S3 example:** a general structurally valid S3 transaction can request `STOP`, but the current human G1 grant prohibits it. Implement and test an **opt-in G1 envelope guard** on the existing transaction checker, then reassess honestly: this closes an enforcement-boundary defect, **not** the separate missing positive real whole-system S3 function. Existing M1 [#39](https://github.com/opensiro/vsm-oss-organization/issues/39) governs S3 source-first positive evidence.

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

Separate reviewer execution is required **only when an explicit currently effective owning task/review contract, actual repository approval requirement, or specific admitted investigation establishes that obligation**. Such an existing explicit contract must not be retrospectively waived by this document **or by an agent on its own**. However, an **authorized maintainer can prospectively amend an issue-level reviewer requirement at its owning source**; that later explicit owner amendment supersedes the earlier task-specific wording, provided no higher-priority branch protection, frozen research protocol, or other still-binding rule requires independent execution. Do not freeze a withdrawn task gate into permanent authority merely because older issue or PR text still mentions it. Periodic Organization S3* audits (e.g. [#188](https://github.com/opensiro/vsm-oss-organization/issues/188)) have their own independent batch selection, frozen wave manifests, slots, provenance and finding-return; they do not automatically become a mandatory post-batch Index admission gate. A future every-50-canonical-assessments audit cadence, if separately admitted, would schedule audit work and track debt rather than impose a silent stop on ordinary Index publication.

Four distinct things must remain separate:

1. **The assessed harness's S3* grade** describes a function in the *harness*. It creates no OpenSiro reviewer requirement.
2. **Organization S3* complementary audit** is a claim-relative audit under its own admitted workstream, selection and locks. It is not routine Index PR review.
3. **Index semantic assessment review** is established by the *exact* Index issue/procedure, when required. A separate source-first/blind execution must use a real distinct context and original source before seeing the producer's proposal when that is the contract.
4. **GitHub PR approval/merge checks** are established by the current repo ruleset and applicable issue/branch policy. An independent evidence receipt or S3* `PASS` is not automatically a GitHub `APPROVED`, and a current ruleset with zero required approving reviews does not itself impose a new S3* wait gate.

Before telling the maintainer that a reviewer is needed, distinguish `EXPLICIT_TASK_REVIEW`, `REPO_APPROVAL_RULE`, `ORG_S3STAR_AUDIT`, and `OPTIONAL_OR_NOT_REQUIRED` **as reporting explanations**, not newly invented canonical workflow states. Cite the live governing source. Check whether a real eligible independent human/agent executor and required permissions exist.

One conversation may **coordinate** independent executions, but cannot manufacture them. Do not simulate independence by changing a role prompt, persona, model label, or reviewer name in a context already exposed to the producer's assessment. If the only available context is contaminated or no executor exists, preserve `REVIEW_REQUESTED / UNASSIGNED` (or the owner's actual equivalent), exact missing gate, and a source-only handoff packet **without claiming a first verdict**. Do not ask for a new ChatGPT chat as the automatic/default solution; a human decision or separately instantiated context is sought only when genuinely necessary and available. Continue other **independently admissible** work only where scheduling, locks and task scope permit.

### No S1-to-parent grade escalation

**Assessed system vs assessing organization:** When Index applies the released Skills Methodology to an external OSS harness (including corrections arising from an Organization S3* audit), the *harness* is the assessment target and Index is the operational **S1 owner** of evidence evaluation and classification. An Organization S3 or S5 task may examine whether the **OpenSiro OSS organization itself** controls its operations, but must not silently move decisions about external harness grades to a human S3/S5 role.

A source-backed, method-conformant disputed classification is an **ordinary Index S1 decision**, including `C` / `?` / `—` alternatives. The Index actor should inspect counterevidence, select a justified disposition, repair assessment/derived views, run validations and preserve its decision in the owning issue/PR. If evidence remains genuinely insufficient, record `INSUFFICIENT` with the missing source and only escalate a *real* outside-S1 right; do not demand a human preference to cure uncertainty.

**Escalate only when the actual missing right lies outside S1:** Profile/Skills semantic-authority changes, whole-Organization present-control decisions, S5 identity/delegation changes, security/licensing or repository integration protections. A parent can change the **delegation envelope**, not become a mandatory human assessor merely because S3/S5 exists. This clarification does not assert the formal OpenSiro grade `S1=A`: that still requires its own observed function/ownership/closure evidence.

**Anti-regression acceptance:** Given an external harness correction where the owner explicitly withdrew separate reviewers, a `continue` **must not** issue a form asking the human to choose `S3*=C` or `S4=C` for the harness. It must continue Index S1 analysis or truthfully report a source/permissions blocker. When the user asks about **OpenSiro S3**, route to the Organization S3 current-control intake and actual G1 authority, not to external harness grading.

### Reviewer-gate change / anti-resurrection rule

Before creating a reviewer handoff, waiting for an independent reviewer, or saying a correction is blocked on one:

1. **Identify the live positive authority:** link the exact currently effective requirement, and distinguish it from an assessment's S3* grade, a historical Organization audit, a closed prototype, a comment, or an author's proposed checklist. Absence of a reviewer is not itself evidence that one is required.
2. **Reconcile explicit maintainer choices:** if the authorized owner has withdrawn an issue-level reviewer requirement, update the **owning issue** to say so and record the superseding process. If old linked PR text is misleading, reconcile its status/description; close obsolete reviewer-only handoffs as `not planned`, not `review passed`. Historical evidence/immutable receipts must remain untouched.
3. **Do not manufacture a replacement gate:** no fresh reviewer ticket, `REVIEW_REQUESTED` loop, blind packet or new chat solely to cure a reviewer that the owner no longer wants. `continue` resumes source investigation and the next owner-admissible action, not reviewer recruitment. Creating a new independent-review workstream needs a fresh explicit authority and an actual eligible executor.
4. **Keep Index S1 assessment ownership local:** under the [Index S1 domain contract](../contracts/s1/domain-contracts.md), the admitted Index agent owns ordinary source evaluation, semantic assessment/correction and evidence-backed grade disposition. It must **not** escalate a disputed external harness grade to the Organization's human S5 parent merely because an old issue says `owner adjudication` or reviewers were withdrawn. Preserve a source-linked decision and real methodological constraints; separate any actual protected-branch/integration, Profile/Skills normative, permissions or S5 governance right. CI does not prove semantic correctness.
5. **Fail closed for real external constraints:** an applicable required GitHub approval, Skills/Profile mandate, external project's policy, or preregistered independence/frozen research contract cannot be waived through an Index issue edit. State the controlling source and leave that specific gate unresolved.

**Regression acceptance cases:**
- Ordinary Index correction, no mandatory reviewer rule: Index S1 agent inspects original evidence, tests alternative grade interpretations, **chooses and records the justified classification within its delegated local authority**, and executes normal validation/publication steps; **no reviewer handoff or mandatory human grading choice**.
- Old task-specific independent review, followed by a documented authorized cancellation: follow **the revised issue**, close reviewer-only tickets, return the pending assessment disposition to **Index S1**, and preserve genuine integration permissions; **no gate resurrection from stale PR prose and no replacement human semantic gate**.
- A repository rule actually demands another approver: **keep that specific permission gate**, regardless of owner preference; do not fabricate `APPROVED`.
- Frozen audit already reported a `FINDING`: keep audit provenance; Index S1 may disposition its own assessment claim, while separately evidenced downstream return/effect verification (when actually required) remains distinct from the semantic grade.

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

- Bare `START_HERE.md` URL / `show control plane` with no specific task produces a source-linked bounded Control Plane summary and **real clickable actions where supported**, with no GitHub write before a selection.
- A text-only client sees a readable numbered menu exposing the same commands; a user can type `status` or provide a named issue instead of clicking a button.
- Selecting **Current Control (S3)** calls `S3: inspect current control` as an independent new user request; it performs only source-first inventory and does not invent a `REQUESTED` transaction or a decisive owner. A targeted `S3: consider <present choice>` must obey the same gate.
- Selecting **S1 Function Test (Upstream)** invokes `test S1 function: upstream contributions`: it **begins from a live, pinned Index assessment of a harness**, then checks native upstream need/fit before evaluating proposal, action rights, execution, validation and closure evidence from Upstream #6. A GitHub issue alone, a convenient Cognee example or low VSM grade **does not qualify**. It never issues a GitHub write, claims `S1=A/C`, or schedules work merely because the domain is now admitted.
- A `PROPOSAL_PREVIEW` with a narrowed stage-scope hash is **not** approval or executed S1 closure; if the connected GitHub client cannot fork, the test reports that limitation without installing a broad token or inventing a runner.
- **S3 intake** is not **S3* Audit**, S1 local repair, S2 coordination or S5 policy. A menu item, issue status or CI result is never `S3=C` evidence.
- A concrete named PR/issue command executes the ordinary gated task path directly; the introduction does not block it, and a button does not confer review, merge, scheduling, or S5 authority.
- With unavailable live GitHub access or write tools, the interface labels status unverified and actions constrained rather than claiming current facts or pretending a write succeeded.
## Non-goals

No new global scheduler, shadow state database, unconditional independent-audit rule, agent spawning service, review rights, changed VSM grades, S3*/S5 authority, CI bypass or blanket merge delegation. This file is an **interface contract for an agent that already has appropriate tools and permissions**; executor provisioning and independent reviewer deployment remain separate work.
