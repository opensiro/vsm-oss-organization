# W002 / Index batch #1202 — 10/10 row lifecycle reconciliation

**Scope:** independent first-party process/provenance reconciliation, distinct from deep semantic findings. [W002 owner #190](https://github.com/opensiro/vsm-oss-organization/issues/190), source [batch #1202](https://github.com/opensiro/vsm-harness-index/issues/1202), frozen intake [#868](https://github.com/opensiro/vsm-harness-index/issues/868). Index snapshot main at 0db4a2ecdefe9c2641306ab20fc17eab114e0681.

## Cross-surface matrix

| Row | Canonical harness | pinned SHA prefix, linked assessment | separate review PR | separate admission PR | catalog position | Exact-head Index checks |
|---:|---|---|---|---|---:|---|
| 1 | foxagent | [321f5eae7bd9](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/foxagent.md) | [#1203](https://github.com/opensiro/vsm-harness-index/pull/1203) | [#1204](https://github.com/opensiro/vsm-harness-index/pull/1204) | 409 | 2 + 2 succeeded |
| 2 | loopex | [3f81b0482890](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/loopex.md) | [#1205](https://github.com/opensiro/vsm-harness-index/pull/1205) | [#1206](https://github.com/opensiro/vsm-harness-index/pull/1206) | 410 | 2 + 2 succeeded |
| 3 | wtsup-code | [abff97e3a6bc](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/wtsup-code.md) | [#1207](https://github.com/opensiro/vsm-harness-index/pull/1207) | [#1208](https://github.com/opensiro/vsm-harness-index/pull/1208) | 411 | 2 + 2 succeeded |
| 4 | grinta | [98112110dc30](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/grinta.md) | [#1209](https://github.com/opensiro/vsm-harness-index/pull/1209) | [#1210](https://github.com/opensiro/vsm-harness-index/pull/1210) | 412 | 2 + 2 succeeded |
| 5 | dodo | [156d60ca2f74](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/dodo.md) | [#1211](https://github.com/opensiro/vsm-harness-index/pull/1211) | [#1212](https://github.com/opensiro/vsm-harness-index/pull/1212) | 413 | 2 + 2 succeeded |
| 6 | forja | [db34341cfacb](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/forja.md) | [#1213](https://github.com/opensiro/vsm-harness-index/pull/1213) | [#1214](https://github.com/opensiro/vsm-harness-index/pull/1214) | 414 | 2 + 2 succeeded |
| 7 | autonomous-coding-agent | [eda302b5a93c](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/autonomous-coding-agent.md) | [#1215](https://github.com/opensiro/vsm-harness-index/pull/1215) | [#1216](https://github.com/opensiro/vsm-harness-index/pull/1216) | 415 | 2 + 2 succeeded |
| 8 | marspi-cli | [e8e46a39e9da](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/marspi-cli.md) | [#1217](https://github.com/opensiro/vsm-harness-index/pull/1217) | [#1218](https://github.com/opensiro/vsm-harness-index/pull/1218) | 416 | 2 + 2 succeeded |
| 9 | autonomouscodingagent | [5054511c8065](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/autonomouscodingagent.md) | [#1219](https://github.com/opensiro/vsm-harness-index/pull/1219) | [#1220](https://github.com/opensiro/vsm-harness-index/pull/1220) | 417 | 2 + 2 succeeded |
| 10 | primusclaw | [bbd925a5b12b](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/primusclaw.md) | [#1221](https://github.com/opensiro/vsm-harness-index/pull/1221) | [#1222](https://github.com/opensiro/vsm-harness-index/pull/1222) | 418 | 2 + 2 succeeded |

## Independent checks and bounds

- **Frozen identity and catalog:** source #1202 original ten frozen rows were cross-checked against authoritative Index data/catalog.psv at the pinned main. Rows 409–418 match their full original upstream SHAs. Index data/signatures.psv carries the same ten positions and harness IDs. The signatures are derived materializations, not semantic ground truth.
- **Separate lifecycle transactions:** each of the twenty actual GitHub PR objects was fetched independently, confirming all ten review PRs and all ten separate admission PRs closed and merged, with exact head SHA and merge commit. The #1202 final board is terminal 10/10 ADMITTED and the issue is closed.
- **Exact-head checks:** GitHub check-run collections for ALL TWENTY distinct PR head SHAs show two completed/success Index checks on each precise SHA. This is evidence of historical code validation, NOT of independent semantic reviewer judgment or today's Organization CI.
- **Sampling:** semantic first / middle / last rows 1/5/10 were frozen ahead of semantic examination and have individual source-first audit records: [FoxAgent](W002-1202-foxagent-audit.md), [Dodo](W002-1202-dodo-audit.md), [PrimusClaw](W002-1202-primusclaw-audit.md). Sampling 3/10 never certifies semantic correctness for all 10.
- **Reviewer events:** GitHub review-object inspection was made for sampled review PRs #1203, #1211 and #1221 (zero formal reviews each), NOT all ten reviews; no universal zero-review claim is made. The historically required process cannot be changed retroactively and absence of formal GitHub review does not establish a historical violation.
- **Limits:** no harness runtime tests, no benchmark evidence, no Index canonical mutations, no overlap with another chat's W001 locks.

## Local status / downstream

- **Lifecycle coverage:** 10/10 reviewed; 20/20 PRs merged; 20/20 exact-head check collections have successful checks; catalog identity mismatches = 0.
- **Semantic coverage:** 3/3 preregistered row positions inspected in pinned primary source; residual questions are documented in each record.
- **Combined W002 batch #1202 S3* outcome: INSUFFICIENT**, not a clean whole-batch PASS: reviewer identity provenance for sampled historical PRs cannot be established from public review events; PrimusClaw has a real unresolved functional S4 boundary between internal task-experience learning and the Profile's outside-and-then adaptation. No alternate canonical classification asserted.
- **Control destination:** Organization [#189](https://github.com/opensiro/vsm-oss-organization/issues/189) for prospective attributable-review handoff; if a source-grounded concrete semantic correction is later established, Index must own a separate same-ref review. No S3 current-control decision was made.

This record remains proposed in draft Organization PR #191 until properly reviewed/merged. Nine other frozen W002 batches remain uncovered; do not declare W002 complete.