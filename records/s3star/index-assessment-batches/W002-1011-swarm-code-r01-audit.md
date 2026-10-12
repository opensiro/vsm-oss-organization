# W002 S3* audit — Index #1011 row 1 swarm-code (bounded abort-control finding)

**Audit ID:** `S3STAR-INDEX-BATCH-20261011-W002-1011-R01-001`.
**Local S3* outcome: FINDING** — specific S3 abort/control-return claim, *not* a conclusion that the entire S3=C classification is wrong. Whole Index #1011 batch audit remains **INSUFFICIENT/PENDING** due seven incomplete assessment rows and unavailable preregistered sample positions 5/10.

## Identity and ordinary S1 claim

- Scope: [Organization W002 #190](https://github.com/opensiro/vsm-oss-organization/issues/190), frozen W002 position five; [Index assessment batch #1011](https://github.com/opensiro/vsm-harness-index/issues/1011), frozen intake #875. W001 is separately locked.
- Frozen upstream: [skyblanket/swarm-code@53007abac1d521e32c2508af5328412bd6bbb67b](https://github.com/skyblanket/swarm-code/tree/53007abac1d521e32c2508af5328412bd6bbb67b), complete 91-entry nontruncated source-tree inventory. Canonical [Index assessment at frozen Index main](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/swarm-code.md), status included, vector `A C C — — —`, original Profile 0.2.4 / Methodology 0.3.6.
- Ordinary Index S3 claims include whole-current phase/task control, the supported stop-file abort and a closure path reading `launch/withhold/advance/done/abort decision → child/phase state changes`. This claim deserves complementary checking because deterministic validation cannot prove actual abort/intervention over child agent work.
- Ordinary publication: accepted Index prose, #1011 board, review PR #1012, admission PR #1054, generated catalog/signature and CI. Audit access: pinned raw first-party flow controller AND detached-child process implementation, not mere rerun of tests.

## Primary-source challenge

1. [`Flows.run_valid_workflow` lines 182–205](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/Flows.sw#L182-L205) constructs a background task table and starts the first phase. [`spawn_phase_tasks/fill_phase_slots` lines 277–305](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/Flows.sw#L277-L305) admit child tasks; [`launch_task` lines 359–390](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/Flows.sw#L359-L390) invokes `Background.launch` on a headless swarm-code subprocess. This proves real first-party current orchestration, not just a diagram.
2. [`Flows.render_loop` lines 403–464](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/Flows.sw#L403-L464) first refreshes children and refills slots/possibly advances the phase (405–437), then tests the **single global** `/tmp/swarm-flows-stop` (441–445), deletes it, sets only the controller state `phase=aborted` (448–450), and exits the render loop with final rendering and `print_summary` (454–458).
3. The entire pinned [`src/Flows.sw`](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/Flows.sw) contains **zero calls** to `Background.kill_task`, `pid_kill_group` or another child termination mechanism. Its documented stop path marks the controller display/state and terminates the orchestration loop; it does not implement an operational kill of running subordinate S1 processes. A non-instance-specific stop-file also gives no grounded guarantee of targeted stop behavior if multiple independent flow instances run concurrently.
4. [`background.sw` lines 135–154](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/background.sw#L135-L154) launches children using OS-detached `shell_detached` (double-fork / `setsid`); they do not depend on the foreground render loop remaining active. There **is** a separately implemented real cancellation primitive [`Background.kill_task` lines 216–241](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/background.sw#L216-L241) using `pid_kill_group`, which `Flows.render_loop` never invokes on stop.
5. Because the stop-file is examined **after** `fill_phase_slots` and phase transition at lines 419–435, a final iteration can even **launch fresh subordinate children before noticing the stop**. This is a static code-path consequence, not evidence that a particular deployed run experienced it.
6. [`Flows.launch_quota` lines 312–355](https://github.com/skyblanket/swarm-code/blob/53007abac1d521e32c2508af5328412bd6bbb67b/src/Flows.sw#L312-L355), child status polling and phase progression independently support resource-capacity S2 and other current-control S3 properties. The source contradiction is thus about the **specific asserted operational abort/control-return subclaim**, not about having no S3 or about changing the categorical VSM vector.

## S3* judgment / owner / bounded result

**Outcome: FINDING.** At this exact SHA, the Index description of stop-file as an abort decision affecting subordinate operational commitments is materially stronger than the demonstrated implementation: the stop event changes **local flow display/orchestration state**, but no actual termination of OS-detached active S1s occurs in the shown first-party stop path. The finding is about closure semantics, **not** about an asserted production incident, successful runtime reproduction or a certain alternative autonomy state. The other phase and concurrency controls remain plausible evidence for published `S3=C`.

- Actual discretionary auditor: this W002 Organization ChatGPT source-review context. GitHub source fetch and check-run API merely deliver evidence. No separate formal GitHub reviewer/human/blind-first-attempt is claimed; the connector identity is the same public account as historical Index producer, so actor independence is bounded.
- Confidence: high for the observed missing abort→kill call and detached launch under pinned static source; actual real-run observability untested.
- Complementarity: direct challenge of published S3 return semantics via controller and process-group ownership rather than trust in assessor's text/CI.
- Downstream legitimate control destination: **Index #1011 row1 swarm-code**, existing accepted same-ref assessment, for separate Index-owner adjudication of the S3 wording and/or optional runtime test. A source-grounded claim correction may be made only via its ordinary same-ref Index review/admission gates. Do not advance row4 Sangxia.ai, jump rows5/10, change signatures/catalog or repin source as S3* auditor.
- S3* finding is published as a bounded observation, **not** an Organization S3 corrective act. Its owner notification must be separately evidenced. Retain W002 #1011 whole-batch `INSUFFICIENT/PENDING`, overall wave open and all W001 locks unchanged.

## Audit lifecycle

Local judgment: `FINDING`. Downstream review/closure: **OPEN** until the responsible Index owner confirms/refutes/narrows the subclaim using admissible source evidence. Original source and Index revision fixed. Organization draft PR #191 is a **reviewable, unmerged audit record**; it does not authorize rewriting any Index artifact or count as independent PR approval.


## Independent full-tree source completeness probe — frozen code and control alternatives

To check that the earlier observation had not missed another first-party automatic child-termination hook, independently fetched and checked out the **exact** upstream commit `53007abac1d521e32c2508af5328412bd6bbb67b` as detached `HEAD` in an isolated clean Git workspace. Read the complete `src/Flows.sw`, `src/agent.sw`, `src/background.sw`, `src/tools.sw`, `src/FlowsRender.sw`, and the relevant `src/test_runner.sw` cases and ran this **whole tracked-tree** inspection:

```sh
git rev-parse HEAD
git grep -n -E 'swarm-flows-stop|kill_task\(|pid_kill_group\(|run_flows\(' -- . ':!docs/*'
git grep -n -E 'Background\.launch\(|Background\.kill_task\(' -- src tests
git grep -n -E -i 'flow.*abort|abort.*flow|swarm-flows-stop|flow.*stop' -- tests src/Flows.sw
git status --short
```

**Observed facts:**

- The only pinned `/tmp/swarm-flows-stop` decision/consumption in executable implementation is `src/Flows.sw:441–443`; `FlowsRender.sw:561,571` prints a UI hint. No `Background.kill_task`, `pid_kill_group` or `shell_detached` invocation appears anywhere in the complete `src/Flows.sw` (907 lines).
- **Actual termination alternatives are present elsewhere**: `agent.sw:3621` invokes `Background.kill_task` only inside `bg_cmd_kill` for a separately user-requested `/bg kill <id>`; `tools.sw:460,1600` invoke it for independent foreground/bash/tool-specific kill operations. None of these is called as a consequence of the `/flows` stop-file path.
- `agent.sw:1243` calls `Flows.run_flows(...)` and then returns the existing conversation `history` when the command exits — the caller does not kill pending child tasks. The detached background spawning and explicit `pid_kill_group` implementation remain distinct operations.
- The frozen `test_runner.sw:2174–2191` exercises **the explicit `bg_kill_group` mechanism**, demonstrating the project does have a test for terminating a detached worker's process group. The tracked `tests/` tree and the `Flows.sw` stop references show no test of **`/flows` stop-file → active subagent termination** in the pinned source. Absence of an identified test is not itself proof of wrong runtime behavior.
- A direct independent Python **source-code invariant probe**, executed against the frozen files (exit 0), asserted that a flow task launches through `Background.launch`, `fill_phase_slots` appears **before** the global stop-file check in `render_loop`, aborted state assignment is present, no flow child-kill call is present, explicit process-group termination is available outside Flows, and the parent slash dispatcher returns history after `Flows.run_flows`. It printed:

```text
EXACT_FROZEN_SOURCE_ASSERTIONS=PASS
FLOW_STOP_FILE_PASSES=1
FLOW_KILL_CALL_SITES=0
BACKGROUND_HAS_PGROUP_TERMINATION=True
REFILL_PRECEDES_STOP=True
PARENT_FLOW_RETURN_TO_HISTORY=True
SWC_COMPILER_PRESENT=no
CLEAN_UPSTREAM=yes
```

The test is a **static exact-ref path/invariant check**, not an executable `.sw` runtime replay. The pinned source's `Makefile` requires `../swarmrt/bin/swc`, which is not installed in the isolated checkout. Do not infer a compiled full-system test, observed survivor PID or platform-specific deployed cancellation consequence. Explicit operator `/bg kill` remains possible; it is **not automatic stop-file closure**.

**Auditor outcome unchanged:** one preexisting bounded `FINDING` on the asserted S3 abort-to-subordinate-control-return interpretation. The actual S2 capacity and S3 current phase/admission control evidence remains valid. No new finding is counted, no categorical vector correction is asserted; downstream Index #1011 must adjudicate same-source wording/procedure.
