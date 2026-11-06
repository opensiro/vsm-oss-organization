# Organizational-code change route

**Owner:** `opensiro/vsm-oss-organization` — [#285](https://github.com/opensiro/vsm-oss-organization/issues/285). **Purpose:** route and evidence changes to the bounded Organization's operating rules, roles, contracts, modes, prompts, control-plane interfaces, admission, recovery, and coordination code. This is an **execution/routing procedure**, not an additional VSM function, independent reviewer, permission grant, or competing Profile/Skills methodology.

## 1. Source first, then classify the decisive change

Start with [`START_HERE.md`](../START_HERE.md) → [`ECOSYSTEM.md`](ECOSYSTEM.md) → the **current owning repository default branch** → exact issue/PR/mandate/frozen artifact. Existing work follows [`TODO.md`](../TODO.md); a new cross-repository or authority-sensitive matter follows [`CONTRIBUTOR_START.md`](../CONTRIBUTOR_START.md).

Identify **what decision or operating contract changes** before treating a file edit as governance. A routine fix to an existing rule is not necessarily a new S3, S4, or S5 decision. Identify the system-in-focus, effective scope and actual decision owner:

| Change or decision required | Owning source/route | Boundary |
| --- | --- | --- |
| Local assessment, method implementation, curated view, routine repair | The actual Index / Skills / Awesome S1 domain, if admitted by its contract | Local actor can implement/test/prepare PR within delegated scope; default-branch integration remains separately governed. |
| Cross-S1 coordination or shared sequencing | Existing Organization S2 contract only when genuine coordination discretion is needed | A task list or CI check alone does not establish S2. |
| Current whole-system commitments/resources/constraint choice | Existing S3 current-control path when a real case and effective mandate exist | Not every cross-repository change is S3. |
| Independent verification | Existing S3* audit contract where genuinely applicable | Do not claim independence from a review in the same context or summon unrequired agents. |
| External adaptation of the bounded system | Existing S4 contract if an actual environment→adaptation decision exists | Checking a third-party policy is an input gate, not itself S4 evidence. |
| System boundary, purpose/identity, ultimate policy, delegation model/holder/right | Legitimate [S5 parent](../contracts/s5/parent-authority.md) | Prepare a proposal; only the attributable holder decides. No automatic policy change from a PR or an assessment grade. |
| External upstream contribution process (adjacent, not admitted S1) | [`opensiro/upstream`](https://github.com/opensiro/upstream) owning docs and its actual repository owner/third-party rules | Organization routes and observes; it does not confer a fourth S1 domain or GitHub rights. |
| VSM semantics / assessment methodology / canonical Index facts | Profile / Skills / Index respectively | Organization cannot change their canonical content by editing its own docs. |

Read [`CONTROL_PLANE.md`](CONTROL_PLANE.md), [S1 admission](../contracts/s1/task-admission-recovery.md) and [S5 parent authority](../contracts/s5/parent-authority.md) for the binding decision boundaries. For a right transfer, additionally use the [OSM delegation route](AGENT_CONTROL_PLANE.md#osm-aware-delegation-and-authority-transfer) **before exercising newly proposed rights**.

## 2. Required change packet

For a meaningful organizational-code change, put a short packet in its **owning issue and reviewable PR** (or link an existing equivalent):

1. **Intent and provenance:** observed problem, source/evidence, exact issue, current ref, expected observable outcome; distinguish a hypothesis from a proven defect.
2. **Owner and class:** repository/source-of-truth owner, system-in-focus, affected actual VSM function(s) and **decisive right**, including why the change is local implementation, bounded coordination, or a reserved policy decision.
3. **Authority:** current authorized actor, allowed mutations and forbidden decisions; record separately any proposed S5 or third-party authorization (issuer, scope, expiry/revocation). GitHub ability alone is not VSM authority.
4. **Effects and contracts:** consumers/return targets, affected invariants and contracts, version/frozen-ref handling, compatibility and rollback/recovery expectation.
5. **Validation:** reproducible relevant native checks, negative/control cases, required first-party CI and explicit untested surfaces. A script test is not evidence of agent efficacy; a CI check is not the owner of a semantic decision.
6. **Disposition:** exact diff/PR, observed review/merge/readback and downstream return, or documented `NO_CHANGE`/`BLOCKED` with the unmet gate. Only observed external merge is upstream acceptance.

Use the smallest reviewable change. A single-repository ordinary S1 fix need not open a redundant Organization issue; link its owner instead. A cross-repository decision or new shared routing contract belongs in Organization, not duplicated into every consumer.

## 3. Separate machine preflight from reserved decisions

Run gates at the stage where they matter; never lump every unmet future condition into `BLOCKED` during candidate discovery.

| Stage | Automatically check when a suitable legitimate port exists | Must remain separately decided/attested |
| --- | --- | --- |
| **Candidate intake (before local patch)** | Current target/branch, license grant and compatibility for **planned reuse/fork**, actual LICENSE/NOTICE text, issue/PR overlap, contributor guidelines and branch policy. Missing license/redistribution grant is a hard `NOT_ELIGIBLE_LICENSE` for a public derivative. | Copyright-holder permission if required; do not infer a grant from public visibility or a missing GitHub license label. |
| **Before implementation** | Frozen source, problem relevance, duplicate existing fix, scope, test/toolchain feasibility, compatible branch format, issue requirement and available authorization. | New external issue/contact, new mandate, policy exception or license rights when not already authorized. |
| **Before Draft PR** | Native RED/GREEN, static tests, fork parent/visibility/actor, diff/secrets, required **pre-submission** contributor checks, duplicate PR, base/head SHA, draft eligibility. | Authentic DCO/CLA certification by the proper person; conflicting first-party branch/PR policy or an explicit human approval requirement. |
| **Before merge or release** | First-party CI suites, review state, integrations and documentation required **at that stage**, branch protection, current source. | Upstream maintainer's merge, reserved Organization integration/S5 choice, and any required legitimate independent reviewer decision. |
| **After observation** | GitHub readback, receipts, downstream return/feedback, ledger links and current next item. | Do not synthesize a passed gate, accepted PR, VSM grade, or owner approval. |

**Automation rule:** a check may be automated; its *authority* cannot be manufactured. Search/reuse of an existing issue, branch-policy parsing, tests, CI monitoring, duplicate checks, license classification and readbacks are mechanical candidates. Creation of a third-party issue or policy-compatible branch is executable only when the active mandate covers it. **Never automatically sign another person's DCO/CLA, waive a required maintainer gate, create an unlicensed fork, or expand an exact finite queue.**

If the first-party rules permit an incomplete **Draft** but demand full suite/real-world acceptance only before **merge**, label `DRAFT_PENDING_UPSTREAM_GATE` instead of a permanent `BLOCKED`; do not run prohibited LLM-agent/model/browser quality tests to satisfy an unrelated validation demand. If the project explicitly requires those tests *before any PR*, record `POLICY_CONFLICT` and stop that publication path. An incompatible upstream branch prefix versus a limited `opensiro/*` mandate is an **authority-envelope conflict**, not a test failure; revise the mandate only through a new legitimate issuer decision, not silently.

## 4. Execution and durable return

1. Resolve admissibility and decisive authority **before external writes**; otherwise do read-only preparation and route the exact missing right.
2. Apply the bounded implementation in the **owning repository** on a reviewable branch; respect independent/frozen-reference constraints and original tests.
3. Verify relevant native checks, generated artifacts, source-of-truth and GitHub readback. Keep Draft/merge/release and technical benefit distinct.
4. Link the owning issue/PR and, when a real cross-Organization decision occurred, its actual return to affected S1 consumers. Record real `BLOCKED`, `NO_CHANGE` and negative outcomes without manufacturing a positive effect.
5. Revisit provisional gates on new evidence; do not silently rewrite frozen cohorts or mutate historical receipts. `TODO.md` remains **only** the selected NOW/NEXT/BLOCKED issue scheduler, not this protocol's permanent change log.

### Example: adjacent upstream experiment #56

The [Upstream candidate-batch protocol](https://github.com/opensiro/upstream/blob/main/docs/ASSESSMENT_CANDIDATE_BATCHES.md) owns early **license-first** screening and the remaining automated contribution-policy preflight. Its [34-case publication mandate](https://github.com/opensiro/upstream/blob/main/docs/CORRECTIVE_PR_PUBLICATION.md) is already finite and does **not** authorize new candidates, other branch families, automatic issue publication or DCO attestation. Existing ledger `BLOCKED` receipts may be re-evaluated under fresh first-party evidence and a legitimate scope decision, but **are not silently converted** by this documentation change. External publication remains paused until separately resumed.

## Checklist for PR authors

- [ ] Current bootstrap, owning source, exact issue/refs and evidence checked
- [ ] Scope, decisive right, existing vs proposed authority and S5 reservation classified
- [ ] Source-owner and impacted contract/return target identified
- [ ] Earliest meaningful automated gate performed; restrictions preserved
- [ ] Bounded tests, negative cases and untested claims disclosed
- [ ] Reviewable PR/readback plus actual outcome or precise blocker recorded
- [ ] No new autonomy grade, fourth S1 domain, forged legal assent or external merge claimed
