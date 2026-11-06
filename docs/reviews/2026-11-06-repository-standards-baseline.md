# Repository standards baseline — 2026-11-06 (six in scope)

**Owner:** `opensiro/vsm-oss-organization` [#288](https://github.com/opensiro/vsm-oss-organization/issues/288). **Observation:** 2026-11-06 17:36 UTC, authenticated read-only GitHub API. **Scope:** the six repositories currently declared by [Organization README](../../README.md), including the admitted Upstream Contributions domain under [#274](https://github.com/opensiro/vsm-oss-organization/issues/274#issuecomment-6420871211). This revises the **population**, not the historical [2026-10-25 five-plus-adjacent observation](2026-10-25-repository-standards-baseline.md).

## Primary-source readback

For every row, fetch `GET /repos/opensiro/<name>`, `/branches/main`, `/rulesets`, root directory, root README, and `.github/workflows` on the default branch. For the five active named rulesets, also fetch `/rulesets/<id>`. Git content has the following observed `main` heads; mutable GitHub settings are **point-in-time** observations and not implied by the SHA.

| Repository | `main` SHA | README lines | Root entries | Actions workflows |
| --- | --- | ---: | ---: | ---: |
| [Organization](https://github.com/opensiro/vsm-oss-organization) | `2c14c7c2cd5b4d86839dd8c93e052fd8cc23f6e3` | 115 | 26 | 5 |
| [Profile](https://github.com/opensiro/vsm-harness-profile) | `527fe01ccf1ee22e54bd9525285a89a93179c1e7` | 114 | 18 | 2 |
| [Skills](https://github.com/opensiro/vsm-harness-skills) | `a7ef0c1a27b606bb73d57cec3a2f5e4a8ae2e087` | 152 | 13 | 2 |
| [Index](https://github.com/opensiro/vsm-harness-index) | `5e0707331a61345df50a2d3cfec543d448fde963` | 155 | 27 | 4 |
| [Awesome](https://github.com/opensiro/awesome-vsm-harness) | `5a7b8ada7c2a3739633b9c2b4f3c21425fc6a07c` | 151 | 10 | 2 |
| [Upstream](https://github.com/opensiro/upstream) | `69f13c2917ac939f411039655a59e339a76cdd19` | 254 | 16 | 13 |

All six have a public description, `main` as default, `main protected=true`, `delete_branch_on_merge=true`, a root README and Actions workflows. All six root READMEs directly expose the shared START_HERE, Organization contributor route and TODO; those three links are the **existing REQUIRED routing invariant**, not a newly invented standard. The exact binary routing oracle remains [`check_public_routing.py`](../../scripts/check_public_routing.py) / [`ROUTING_CONFORMANCE.md`](../ROUTING_CONFORMANCE.md); human comprehension has **not** been certified by detecting links.

## README and structure review — advisory human judgment

| Repository | Findings and local ownership |
| --- | --- |
| Organization | Human/AI entry, six-repository scope, ownership and layout are explicit; the dense root is explained in the README and [`docs/README.md`](../README.md). No new structural mandate proposed. |
| Profile | Normative [`PROFILE.md`](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md), versioning, validation and downstream boundary are visible. No local `CONTRIBUTING.md`, but the common contributor route is linked. |
| Skills | Assessment/skill catalog and Profile dependency are explicit. No local `CONTRIBUTING.md`; common contributor route is linked. Experiments are separately identified. |
| Index | Corpus, assessment and generated-view ownership is explicit; local contributor guidance and workflow documents are linked. GitHub topic `evalutation` appears to be a typo, not an assessment-methodology defect. |
| Awesome | Curated downstream nature and non-normative VSM introduction are explicit. Root LICENSE contains CC0 1.0 text while GitHub SPDX detection reports `NOASSERTION`; investigate detection before assuming absent licensing. |
| Upstream | Public portfolio, registry, casebook, pilots, docs, policies, scripts and tests have distinct directories, but the ~22 KB / 254-line root README mixes entry guidance with many dated operational details. A concise top-level contents/quick-navigation block and links to owner docs would improve cold-start usability. No automated quality pass claimed. |

All observed README relative links begin with an existing root path; this coarse check does **not** replace complete target/anchor validation or a fresh-agent comprehension trial. No Project-memory or private repository source was used as audit evidence.

## GitHub settings — observed versus required

| Dimension | Current six-repository evidence | Classification |
| --- | --- | --- |
| Root bootstrap/Organization/TODO routing | 6/6 directly present | **REQUIRED: observed PASS** |
| Public default `main`, protected | 6/6 | Informational; not a complete protection attestation |
| Automatic delete branch on merge | 6/6 `true` | Preferred historical convention; no new policy mandate |
| Named active `Protect main` ruleset | 5/6; Upstream has none returned | Advisory difference; Upstream `main` is still protected |
| Named ruleset required approving reviews | 0 for all five visible named rulesets | Advisory risk/owner choice, **not** evidence that every protection path is uncovered |
| Named ruleset required status-check rule | None in the five visible named rulesets | Advisory risk/owner choice; workflow existence is not mandatory CI enforcement |
| Branch-protection detail endpoint | Integration returns HTTP 403 | **UNKNOWN**; do not infer absence of other controls |
| Repository topics | Present 5/6; Upstream empty | Preferred discoverability; not mandatory |
| Root LICENSE | Present 5/6; Upstream absent | Owner/license decision needed; do not invent a license or claim a legal violation from convention alone |
| GitHub license recognition | Organization/Skills/Index Apache-2.0; Profile CC-BY-4.0; Awesome NOASSERTION despite CC0 root text; Upstream absent | Informational; detection and actual rights are different |
| Root CONTRIBUTING | 4/6; absent Profile/Skills | Advisory; existing shared contributor entry can be sufficient |

The five named rulesets contain deletion/non-fast-forward/update and pull-request rules with zero required approving reviews; no required status-check rule was observed. This proves only those **visible rulesets**. The protected-branch detail endpoint was inaccessible to this integration (`403 Resource not accessible by integration`), so no claim is made that other GitHub protections are absent.

## Owner-local follow-up and decision boundaries

1. **Organization #288 / reviewable PR:** make the read-only probe and Control Plane route six-scope-aware; publish the new baseline without rewriting the historical five-repository snapshot. An automated `PASS` is not an S3* audit.
2. **Upstream [#130](https://github.com/opensiro/upstream/issues/130):** note that `delete_branch_on_merge` and common README routing are now applied. The root license posture remains an explicit copyright/repository-owner choice. Topics and shorter README navigation are optional local improvements.
3. **GitHub administrators / legitimate governance owner:** decide whether any minimum approving review or required CI checks should become mandatory. Observed 0-review rulesets are not automatically violations of an unpublished policy. Any actual settings change requires owner authorization and post-change readback.
4. **Index owner:** correct optional topic typo `evalutation` through normal repo-admin choice; no assessment data change.
5. **Awesome owner:** check why GitHub reports `NOASSERTION` for a root CC0 1.0 license file. Do not replace its legal text merely to make a badge green.

**Functional separation:** this is a read-only tool-supported baseline, not an independent S3* judgment, admitted S3 case, S5 policy selection, executed settings repair or VSM grade claim. No repository settings, licensing or external PRs were modified to obtain the observations. Independent review, human policy decisions and owner-local repairs must retain distinct attributable receipts.

## Follow-up — README navigation resolution (2026-11-06)

The initial comparison checked only the first path component of relative README links. A later source-pinned follow-up compared the **complete relative path** of every simple Markdown inline link from each root README against the full Git tree at the same Git commit. GitHub reported `truncated=false` for all six trees. Results:

| Repository | Pinned commit for README/tree | Distinct relative paths | Missing paths | Same-README anchors |
| --- | --- | ---: | ---: | ---: |
| Organization | [`bf325928`](https://github.com/opensiro/vsm-oss-organization/tree/bf325928deef051e6de5d8eeb56f52b88fe39ae8) | 29 | 0 | 0 |
| Profile | [`527fe01c`](https://github.com/opensiro/vsm-harness-profile/tree/527fe01ccf1ee22e54bd9525285a89a93179c1e7) | 13 | 0 | 0 |
| Skills | [`a7ef0c1a`](https://github.com/opensiro/vsm-harness-skills/tree/a7ef0c1a27b606bb73d57cec3a2f5e4a8ae2e087) | 11 | 0 | 0 |
| Index | [`49ba876c`](https://github.com/opensiro/vsm-harness-index/tree/49ba876ceb80e84fe996e83dc41e7df3161aa011) | 10 | 0 | 0 |
| Awesome | [`5a7b8ada`](https://github.com/opensiro/awesome-vsm-harness/tree/5a7b8ada7c2a3739633b9c2b4f3c21425fc6a07c) | 1 | 0 | 8 |
| Upstream | [`f25f70c7`](https://github.com/opensiro/upstream/tree/f25f70c7da36a81c8084d645d649b1e9a036f0f6) | 43 | 0 | 0 |
| **Total** | Six pinned pairs | **107** | **0** | **8** |

The eight Awesome table-of-contents anchors correspond to its README headings. Two cross-file fragments were inspected separately against the named target headings: Organization `docs/AGENT_CONTROL_PLANE.md#m3-d1-a-autonomous-s3-source-prepared-not-active` and Upstream `docs/ASSESSMENT_TO_IMPROVEMENT.md#mandatory-validation-boundary--native-scripted-tests-only`. Neither full Markdown syntax, remote HTTP links nor every cross-file fragment is certified. The resulting advisory `readme_local_links` probe adds regression detection without changing the existing mandatory routing policy or replacing human readability review.
