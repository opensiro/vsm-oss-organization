# Source-first documentation and governance review — 2026-10-16

**Reviewer:** continuing GPT-6 ChatGPT execution, implementation-aware; **not** an independent or blind assessment.
**Scope:** public default-branch entrypoints for Profile, Skills, Index, Awesome, and Organization; deeper Organization bootstrap, current-work scheduler, milestone trackers, S3 grants, published M3 mode source, contracts, and public outcome-metrics contract.
**Disposition:** narrow documentation reconciliation proposed; no M3 closure, S5 delegation, Index grade, or autonomous operation asserted.

## Source boundary and inspected evidence

- Canonical entry and ownership: [START_HERE](../../START_HERE.md) → [ECOSYSTEM](../ECOSYSTEM.md) → repository-local owning source; [Organization scope](../../README.md); [UPSTREAM_CONTRACT](../../UPSTREAM_CONTRACT.json) pins Profile `v0.2.4`, Methodology `v0.3.7`, and live Index `main`.
- [M0–M5 roadmap](../ROADMAP.md), [M3 tracker #5](https://github.com/opensiro/vsm-oss-organization/issues/5), [M2 tracker #4](https://github.com/opensiro/vsm-oss-organization/issues/4), and [current work](../../TODO.md).
- [D1-A pending grant](../../contracts/s3/autonomous-d1a.json), [M3 RUN](../../modes/s3-autonomous/RUN.md), [composed source entry](../../modes/s3-autonomous/runtime_entry.py), [model decision](../../modes/s3-autonomous/decision_loop.py), [post-source assessment](2026-10-15-m3-s3-a-post-live-source-first-reassessment.md), and [OSS runtime clarification PR #270](https://github.com/opensiro/vsm-oss-organization/pull/270).
- Parent-governed [S5 authority](../../contracts/s5/parent-authority.md); parent-assisted [human G1](../../contracts/s3/parent-assisted-g1.md), distinct from D1-A agent ownership.
- Read the `README.md` files from all five bounded repositories for bootstrap/ownership consistency; read the [outcome-metrics contract](../METRICS.md). **This was not a full audit of all five codebases or a re-execution of Index assessments.**

## Findings

| ID | Severity | Observation | Disposition |
| --- | --- | --- | --- |
| F1 | Medium | Organization README described M3 as `planning milestone only` without acknowledging shipped, inactive D1-A source components, causing understandable ambiguity between engineering readiness and assessed autonomy. | **Fixed in this PR** by distinguishing source preparation, S5 authority, and S3=A proof. |
| F2 | Medium | Roadmap's one-line M3 status omitted D1-A source preparation while correctly withholding a positive `A`. | **Fixed in this PR**, without altering targets/assessment authority. |
| F3 | Low | `docs/CONTROL_PLANE.md` still framed a demo S5 prompt as something used *before full M2 implementation*, although M2 tracker #4 is closed. | **Fixed in this PR** by pointing to actual M2 evidence and S5 authority. |
| F4 | High (operational boundary; not a code exploit finding) | Checked-in D1-A is still `PENDING_S5_PUBLIC_ATTESTATION`, with null execution identity and authorization/publication dates. First-party source supports a fail-closed prepared mode, **not an effective S5 grant nor S3=A**. | **Open, intentional**. A separately attributable S5 decision, published bounded agent identity/term, independently supported S3 qualification and positive source-first ownership/return assessment are still required. No agent-authored GitHub post may impersonate the S5 issuer. |
| F5 | Medium (governance-document drift) | M3 tracker #5's dated top narrative says D1 choice was still missing, whereas [D1-A source-preparation PRs #260–#270](https://github.com/opensiro/vsm-oss-organization/pull/270) and its checked-in grant record the **design selection**. This is not the missing personally attested S5 issuance. | **Follow-up:** reconcile the tracker wording to say D1-A *design selected, operational grant not issued*; do not falsely claim a new S5 decision. |
| F6 | Low (routing) | Shared `TODO.md` selects no NOW or NEXT; its sole BLOCKED entry is [blind routing #167](https://github.com/opensiro/vsm-oss-organization/issues/167). The preregistered independence/prompt-vault boundary prohibits using this continuing context as a qualifying trial. | **Preserve** blocked/held-out semantics. Do not auto-admit M3 or regenerate prompts. |
| F7 | Informational | Profile, Skills, Index, Awesome and Organization READMEs all expose common human/AI entry routing while retaining distinct repository-owned semantics, procedure, corpus, curation, and control boundaries. Metrics distinguish durable outputs from mere commits/PRs. | No cross-repository entrypoint change justified by this bounded check. |

## Recommended follow-through

1. Merge this documentation-only PR after current-head validation. Re-read README/ROADMAP/control-plane and the live M3 #5 tracker after merge.
2. Update the **dated status summary** of M3 #5 to distinguish *selected source-prepared design* from *effective separate parent S5 grant*, with links to its later merged PRs. Do not turn assistant-authored comments into owner attestation.
3. Keep the OSS runtime boundary: no mandatory OpenSiro-operated worker, provider, GitHub App, or independent reviewer deployment. Users of the OSS interfaces may choose their own runtime.
4. Admit a substantive M3 source-first reassessment only when the actual authorization and agent-owned, boundary-reachable decision/return evidence exists. Do not stage an artificial S3 case. S1/S2/S3*/S5 classification falsifiers remain independent.
5. If routing #167 is revisited, obey its frozen preregistration and isolated fresh-context trial contract; an ordinary author-context review is not a qualifying run.

## Validation and limits

The proposed changes are documentation only and do not change `contracts/s3/autonomous-d1a.json`, behavior, tests, historical provenance or milestone status. Checked source-path and governing-issue relationships; automated repository CI on the exact PR head is a separate publication gate. No full five-repository test matrix, credentialed runtime operation, synthetic autonomous transaction, or independent evidence review was executed by this report.
