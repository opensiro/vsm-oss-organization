# Independent Reviewer Batch — prospective coordination hypothesis

**Status:** PROPOSED / NOT DEPLOYED / NOT VSM EVIDENCE. This is a falsifiable design and review-intake note, not an accepted S2 assessment, reviewer runtime, new scheduler, review approval, or milestone promotion.

**Governance owner:** [Organization #189](https://github.com/opensiro/vsm-oss-organization/issues/189) (agent-executable independent review/handoff). **Formal organization-level S2 evidence owner:** [M4 / #6](https://github.com/opensiro/vsm-oss-organization/issues/6). Adjacent [#200 / draft PR #201](https://github.com/opensiro/vsm-oss-organization/issues/200) concerns the *distinct* S3* finding-return verification lifecycle, not this candidate's acceptance.

**Normative authority:** [Profile v0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/v0.2.4/PROFILE.md) sections 3–8; [Skills Methodology v0.3.7](https://github.com/opensiro/vsm-harness-skills/blob/v0.3.7/skills/assess-vsm-harness/SKILL.md) (function before ownership, boundary and S2 interference/feedback). Actual Organization scope is [ORGANIZATION.md](ORGANIZATION.md); the selected upstream refs are in [UPSTREAM_CONTRACT.json](../UPSTREAM_CONTRACT.json). Re-read owners' current refs and exact issues for actual work; these versions are the **basis of this proposal**, not a replacement for live authority.

## Motivation and hypothesis

An actual operational problem is visible: some explicitly governed independent assessment or publication reviews have source-pinned proposals and successful CI but no legitimately separate executing reviewer. This is primarily a **review execution/availability problem** at the owning task gate; it is not, on its own, an established S3 transaction, an inter-S1 conflict, or proof of S2.

The proposed *Independent Reviewer Batch* is a bounded coordinator for multiple **separately admitted** review jobs. It might eventually support **S2** if evidence demonstrates that it regulates a *specific interference, conflict or oscillation between distinct S1 operational units* and returns a coordination result that changes subsequent S1 operation.

**Hypothesis H-S2-RB-001:** Where independently valid work in two or more Organization S1 domains causes observed or structurally evidenced coordination interference (e.g. Index/Skills contract-change contention or Index/Awesome invalidation/rework), an explicitly scoped reviewer-batch coordination relation could attenuate that disturbance with a reviewable return to both affected domains. If no qualifying cross-S1 interference and closure can be reconstructed, reject the **Organization-level S2** interpretation even if batch execution improves review throughput.

This is a functional hypothesis, **not** a promise that introducing the batch will create S2, or that S3 necessarily produced S2.

## Declared system and recursion boundary

At the **bounded OpenSiro Organization** level, the operational S1 units are **Index, Skills and Awesome**. Profile owns normative semantics; Organization is the metasystem construction surface. Five parallel reviewer agents, PRs or assessment rows **inside Index** do not become five Organization S1 domains.

It is possible to study a separate *lower-recursion* reviewer organization, but that requires an independently declared system-in-focus, purpose, local environments and durable operational units; do not transfer its conclusions to Organization/M4.

Distinguish roles at either level:

| Concern | Function / responsibility | Cannot be inferred from |
| --- | --- | --- |
| Local assessment / PR lifecycle | Owning **S1** domain | A backlog item existing in Organization |
| Whole-system current constraints, resources or intervention | Potential **S3**; see [#39](https://github.com/opensiro/vsm-oss-organization/issues/39) and [current-control contract](../contracts/s3/current-control.md) | Missing reviewer, ordinary PR repair, CI green, batch scheduler |
| Specific inter-S1 interference regulation and feedback | Potential **S2**; formal evidence and autonomous owner belong to **M4 / #6** | Queueing, assigning, sequencing, locks, shared state or multiple reviewers by themselves |
| Complementary, claim-relative access to operational reality and attributable audit judgment | **S3***; [audit contract](../contracts/s3star/audit.md) | An ordinary semantic PR review, another LLM call or mechanical tests |

The Organization's current S3 constructor is **not** positive S3 evidence until the natural, bounded current-control trial in #39 closes. A reviewer batch may be designed while that remains open; it must not bypass M1–M3 or imply M4 completion.

## Proposed execution model — separate from S2 attribution

```text
owning task / actual independently required gate
               |
     coordinator admission only
     (frozen batch manifest; no new review obligation)
               |
   +-----------+-----------+
   |                       |
reviewer execution A   reviewer execution B ... (isolated per claim/task)
   |                       |
independent receipt A   independent receipt B
   +-----------+-----------+
               |
         owning repository
semantic disposition / PR checks / authorized merge / verified main
```

The batch coordinator **never** grants new GitHub approval, review authority, audit judgment, permission to publish, or canonical Index admission. Reviewers are independent *executions*, not personas in a producer-exposed conversation. A batch may have mixed outcome statuses; a blocked item must not silently block otherwise admissible and disjoint items, or advance locked serial Index rows.

**Types stay distinct:** an Index source-first **semantic review** under the exact Index task contract, a **publication review** of code/docs (such as draft Organization PR #201), and a claim-specific **S3*** complementary audit each has its own admission/evidence/decision owner. Combining them in one batch does **not** turn all three into S3*.

**No default post-batch review.** No automatic reviewer request after each ten-row assessment batch, every PR, or arbitrary frequency. Select jobs only where their *live owning contract, actual GitHub approval requirement or separately admitted investigation* explicitly requires review. Ordinary Index review/admission continues when no separate reviewer is required. This proposal does not modify [TODO.md](../TODO.md) or freeze a new audit wave.

### Minimum per-job admission record (proposed)

- Unique owning task / issue / PR and classified **actual** gate; explicit admission reason.
- Declared system boundary and recursion, source repository and full frozen SHA where applicable, Profile/Methodology refs when applicable, reviewed PR head, current owning branch/base, lock or serial-row state.
- Review type, producer context/exposure, reviewer selection and real distinct execution/context ID **only when actually assigned**; `UNASSIGNED` must remain honest.
- Reviewer-visible inputs. For source-first semantic work, withhold proposed vector, producer analysis, PR description and Index assessment until immutable first-source verdict is recorded, as required by [#189](https://github.com/opensiro/vsm-oss-organization/issues/189) / [draft PR #198](https://github.com/opensiro/vsm-oss-organization/pull/198).
- Per-job receipt: actual execution provenance, primary evidence, uncertainty, `PASS / FINDING / INSUFFICIENT` under the **owning** contract, review outcome, exact head and timestamp.
- Owning-repository adjudication, separate formal GitHub approval where required, exact-head CI, authorized merge, verified main and serial board advancement **only when actually observed**.
- Revalidate identities/refs/gates before attempts and before any state transition; stop on stale source/head, insufficient reviewer independence or competing claim.

A manifest and deterministic validator are **support machinery**, not autonomous S2 judgment or independently attributable reviewer evidence. Batch dispatch requires a real separately provisioned runtime; this note does not deploy one.

## Falsifiable S2 evidence plan (M4-owned)

Before any positive Organization S2 mapping, record the following in a *real* case, or explicitly disconfirm the hypothesis:

| Profile / M4 requirement | Evidence to collect | Counterexample / rejection |
| --- | --- | --- |
| Distinct operational S1s | Two or more among Index, Skills, Awesome, with respective current work/owner refs | Five Index reviewers or two Index PRs only |
| Actual or structurally evidenced inter-S1 disturbance | The precise race, resource contention, oscillation or contradictory assumptions **arising from their interaction** | A single PR waiting on a reviewer; hypothetical conflict without concrete mechanism |
| Coordination relation tailored to it | Who reconciles conflicting review windows, exact contract version, shared constraint or collision; where the first-party path is reachable | Generic FIFO batch queue or a coordinator label |
| Decisive coordination right and owner | Who actually chooses/revises the stabilizing response (agent, human, composed owner) vs locks/schedulers enforcing it | Calling a deterministic dispatcher `S2=A` |
| S1 return and attenuation | Dated receipts showing returned coordination to **affected S1s** and changed later operation, fewer collisions/retractions/invalidations under that specific mechanism | A review comment or dashboard with no subsequent behavioural change |
| Autonomous S2=A claim | Independent evidence the **autonomous agent** holds and closes the decisive coordination discretion in supported Organization operation; valid M4 sequence/prerequisites | Human decision only, or agent does task assignment but not the coordination decision |

Potential observations include an Index assessment contract changing while Skills changes its procedure, or an Index correction repeatedly invalidating Awesome's view. These are **investigation examples**, not assertions that the disturbance was seen or that batch review addresses it.

If cross-domain evidence is absent, report **reviewer-throughput infrastructure** only. If a qualifying function is found but its decision owner is composed or deterministic, distinguish possible `C` (under Methodology's narrow function-specific constructor threshold) from `A`; do not retroactively promote M4. `A / C / — / ?` are published methodological ownership states, not implementation progress stages, and no positive state is assigned by this design note.

## Next admissible steps and ownership

1. **Organization #189** — treat this as a non-normative proposal for an optional batching layer *after* genuine reviewer execution can be established. Review existing [draft PR #198](https://github.com/opensiro/vsm-oss-organization/pull/198) without merging its separate scope into this document or manufacturing a blind review. A technical reviewer-runner pilot may be considered under its own admitted contract; the first actual independent execution is mandatory before declaring review capability deployed.
2. **Owning repositories** — each task stays under its own actual reviewer, adjudication, CI, permission and merge gates. No Index mutation or scope expansion by Organization. S3* waves retain their frozen sampling, atomic slots and audit judgment contracts.
3. **M4 / #6** — when an actual qualifying inter-domain disturbance appears and M4 prerequisites hold, preregister the proposed coordination response, then test/observe ownership, closure and attenuation without injecting fake conflicts. Distinguish a genuine S2 finding from an ordinary efficiency improvement.
4. **Control Plane** — may *describe* this candidate or prepare a **read-only eligibility shortlist**; do not advertise an executable `independent reviewer batch` command until an authorized runtime and repeatable admission/receipt path exist.

**Explicit non-goals:** no new mandatory review cadence; no new canonical scheduler; no S1 domain creation; no independent reviewer impersonation; no S2/S3/S3*/S4/S5 grade change; no M1/M3/M4 milestone closure; no parent-policy or permission change; no retrospective reinterpretation of frozen W001/W002 audit receipts.
