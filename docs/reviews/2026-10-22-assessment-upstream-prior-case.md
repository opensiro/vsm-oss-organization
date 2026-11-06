# Dated case receipt — assessment-derived AgentBox S2 candidate

**Snapshot as inspected 2026-10-22.** This is a **historical continuity aid, not canonical current project state, not a candidate queue and not the entrypoint for fresh blind discovery**. Read it only in explicit `CONTINUE_PINNED_CASE` mode or *after* a new `FRESH_INDEX_FIRST` candidate-selection lock. [Fresh replay protocol](../ASSESSMENT_UPSTREAM_REPLAY.md). Current GitHub owners override this snapshot.

## Why this case was selected

Canonical [Index assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/ag/agentbox.md) observes that cross-box same-file task grouping/coordination is manual; future manager instructions are planned. This gave an `ASSESSMENT_DERIVED` **S2 hypothesis origin** about attenuating interfering parallel work, not a measured breakage in real concurrently writing boxes, positive S2 autonomy evidence or a desire to upgrade an Index grade.

Historical Index discovery source: `opensiro/vsm-harness-index@5393b698bfdfa4ca14d97a79238234eca20694e5`, assessed AgentBox source `review_ref=463a6a0a20176147f0b0dbfa8a261aba5e43cbd6`. Latest Index default must be queried afresh. Historical AgentBox pilot was source-pinned at `madarco/agentbox@605ee75d63319003c188bc532d4e5b2ba36a51d6`, not asserted to remain its current head.

## Grounded baseline → proposed mechanism → native checks

| Phase | Immutable evidence / observation | Important bound |
| --- | --- | --- |
| Index-first hypothesis | [Candidate card](https://github.com/opensiro/upstream/blob/design/improvement-candidates-intake-20261020/candidates/agentbox-overlap-manager-20261020.md), [Upstream #61](https://github.com/opensiro/upstream/issues/61) | Candidate source records `BLOCKED_EVIDENCE` until first-party scope/benefit fit; VSM assessment does not itself prove product bug |
| Actual CLI assignment baseline | [Merged research PR #64](https://github.com/opensiro/upstream/pull/64) | With a mock Hub API, two descriptions sharing an intended path can be assigned to separate boxes. Not a real two-worker collision |
| Separate dependency allocation baseline | [Merged research PR #65](https://github.com/opensiro/upstream/pull/65) | `dependsOn` predecessor still `todo`, dependent task can be allocated/marked in progress. Allocation is not child execution; may be valid |
| Opt-in source-only advisory | [OpenSiro PR #72](https://github.com/opensiro/upstream/pull/72) | Pure module grouping explicitly supplied write scopes; no default AgentBox manager/worker integration and no changes in third-party repo |
| Paired planning-decision exercise | [Native CI #39683286746](https://github.com/opensiro/upstream/actions/runs/39683286746) | Native AgentBox TS/Vitest **20/20 PASS**, build, TS typecheck and ESLint PASS. Existing assignment recommends three separate box targets through stub; advisory suggests co-grouping overlapping pair and parallel docs. **Not real product before/after** |
| Final pinned pilot head at snapshot | `opensiro/upstream` [PR #72](https://github.com/opensiro/upstream/pull/72), `0ac60e589993f6cedf00fe074c48977e20aea28f` | All four workflows at that head `SUCCESS`; PR **open / ready for internal review**, **not merged** at snapshot |
| Upstream issue-first handoff | [Prepared AgentBox issue draft](https://github.com/opensiro/upstream/blob/research/agentbox-s2-manager-advisory-prototype-20261022/pilots/agentbox-s2/manager-advisory/UPSTREAM_ISSUE_HANDOFF.md) | External issue **unpublished**, third-party PR **none**, no first-party acceptance |

**Effect:** positive deterministic *planning-output* difference in a source-compatible injected helper, **not** measured saved user files, prevented collisions, independent box execution or operator effort. **No shipped native benefit** or full assessment-to-upstream causal outcome can be claimed.

## Decisions and open gates (do not silently resolve)

- [Upstream experiment #56](https://github.com/opensiro/upstream/issues/56) owns the origin-class distinction and full strict experimental objective, separate from issue-driven Kit / HarnessDesk / Agent Code engineering.
- [Upstream case #61](https://github.com/opensiro/upstream/issues/61) owns the AgentBox hypothesis, native-fit gates and staged work; operator allowed **bounded internal prototype before maintainer response**, not blanket external consent.
- [Upstream proposal PR #72](https://github.com/opensiro/upstream/pull/72) owns the implementation receipt and test status; retrieve current ref/reviews before action.
- [AgentBox CONTRIBUTING](https://github.com/madarco/agentbox/blob/main/CONTRIBUTING.md) requests an issue before work larger than bugfix; external maintainers own feature direction, CLA and merge. Silence is not approval.
- [Organization #274](https://github.com/opensiro/vsm-oss-organization/issues/274) and [Upstream #6](https://github.com/opensiro/upstream/issues/6) own scope/authorization boundaries. **No fourth admitted S1** at snapshot. External issue, fork, branch and PR actions require their actual current authority.

### Next real measurements / acceptable stop conditions

1. Independently re-check AgentBox's intended Phase 4 behavior, whether manager instructions, not task-store schema, should supply opt-in scope grouping, and who may decide on actual box dispatch.
2. Preregister a **genuine native workload** with two agents/boxes competing to edit the same known file and a disjoint parallel control, matched `before` vs `after`, collision rate, retained edits, number of human interventions, time/throughput cost, unknown scopes, stale paths and rollback. The exact native box setup must respect operator sandbox/runtime costs and true constraints.
3. A planner-only implementation is **not sufficient** to claim prevention of file-write collisions. If real native execution is unavailable, return `NATIVE_BENEFIT_NOT_MEASURED`; do not substitute task descriptions or synthetic file writes for real worker behavior.
4. If first-party fit rejects this design, report `NO_ELIGIBLE` / `BLOCKED_NATIVE_DESIGN_FEEDBACK` / negative native fit and select a genuinely independently qualified new case rather than overstating results.
5. External contribution lifecycle (issue-first/contact, permitted working fork, upstream PR by human, maintainer feedback) remains **not performed** at snapshot.

## Control Plane replay check

The experiment remains **incomplete** for strict success. A new *blind* Control Plane test must use [the generic protocol](../ASSESSMENT_UPSTREAM_REPLAY.md) before seeing this receipt. A named continuation may legitimately use it, but may **not** count the same known candidate as independently rediscovered. Never count a green plan-only CI as real conflict reduction or an internal PR as external upstream acceptance.
