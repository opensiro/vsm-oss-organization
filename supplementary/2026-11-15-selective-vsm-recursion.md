# Selective VSM recursion in the OpenSiro OSS organization

**Recorded:** 2026-11-15. **Type:** supplementary, non-normative architectural reasoning. **Status:** `PROPOSAL / NOT ADOPTED`. **Tracking:** [Organization #330](https://github.com/opensiro/vsm-oss-organization/issues/330).

**Question:** should a multi-repository agent organization instantiate one VSM at its organizational boundary, or one complete VSM for every repository?

**Working conclusion:** retain **one declared parent OpenSiro OSS viable system**, and allow **selective recursive viable systems** inside qualifying operational S1 domains when there is a real locally regulated environment and an evidence-supported need. A GitHub repository is a source-code/governance container, **not** a VSM recursion unit by definition.

This note analyzes a design option. It does **not** declare a child viable system, revise the parent boundary, claim any new S1–S5 ownership state, grant authority, change milestones, or mandate implementation.

## 1. What already exists

The current [Organization boundary](../docs/ORGANIZATION.md) declares one bounded OpenSiro OSS system with four **parent S1 operational domains**:

- **Index** — evidence-backed canonical assessment corpus;
- **Skills** — reusable assessment procedures and tooling;
- **Awesome** — representative downstream curation;
- **Upstream Contributions** — evidence-backed third-party OSS contribution and maintenance outcomes.

[Profile](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md) supplies normative semantics, not a fifth operational S1; this repository constructs/evidences the organizational metasystem, not an automatically established S2–S5 merely by containing its files. Current organizational function/ownership evidence and milestone state must be checked from their owning sources, not inferred from the architecture picture.

The normative [Profile §11](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md#11-recursion-and-autonomy) allows an S1 unit to **itself** be viable. It requires a durable parent contribution, a relevant local environment and identity, distinct operations, meaningful local autonomy/regulation, appropriate metasystemic functions, and parent–child channels without duplicate authority. Spawning subagents or nesting a workflow is *not* evidence of recursive viability.

Thus these statements are compatible:

> At the **parent recursion**, Upstream is one operational S1 domain.
>
> At a **hypothetical child recursion**, Upstream could be analyzed as a separate viable system, *if* its local operations and regulatory closure are actually established.

Neither statement means that every repository is an S1 or that any child VSM is already demonstrated.

## 2. Three competing organization patterns

| Pattern | What it gets right | Main failure / cost |
| --- | --- | --- |
| **One VSM only at the parent** | Shared identity, a clear cross-domain authority boundary, lower duplication | Whole-system S3 can become overloaded by ordinary domain-local decisions |
| **One complete VSM per repository** | Potential for strong local authority boundaries where warranted | Equates Git layout with organizational structure; generates unnecessary “S2/S3/S4/S5” gates, duplicated approvals and false ownership claims |
| **One parent VSM + selective local recursion** *(preferred hypothesis)* | Preserves parent cohesion while keeping locally absorbable variety local | Requires explicit evidence and careful separation of parent and child decision rights |

The third pattern is **not** “install S1–S5 in all four current S1 repositories.” It asks whether a domain is already a coherent locally regulated system, or whether a narrow missing regulatory function would make it one. The answer may legitimately be **no local recursive VSM**.

The relevant distinction is:

```text
GitHub repository
    != operational S1 unit at any specified recursion
    != viable system with a local metasystem

Declared parent OpenSiro OSS viable system
    ├── Index S1 domain
    ├── Skills S1 domain
    ├── Awesome S1 domain
    └── Upstream Contributions S1 domain
          └── possible child system-in-focus (not established)
                ├── locally differentiated operational units, if real
                └── only the regulatory functions justified by local variety
```

## 3. When a local recursive boundary is worth examining

This is a **reasoning test**, not a new admission gate, scoring rubric, or mandatory checklist:

1. **Separate purpose and environment.** Is there a durable contribution to the parent and a distinguishable local environment producing actual disturbances, beyond GitHub repository metadata?
2. **Meaningful operational differentiation.** Are there persistent outcome-owning operational units, rather than merely tasks, agents, batch numbers, pipeline stages, scripts, PRs, or subprocesses?
3. **Local variety with necessary discretion.** Which recurrent operational decisions require local information? Can they be resolved inside an existing delegated envelope? What is actually left as residual variety?
4. **Regulation and closure.** Is a local coordinating/control/adaptation/identity decision path necessary and reachable? What concrete disturbance does it regulate, who chooses the response, and how does the response change subsequent operation?
5. **Parent interface.** Which decisions stay local, which require parent S2/S3/S4/S5 involvement, and how do exceptional escalations and authoritative decisions return? Is authority clearly bounded and non-duplicated?
6. **Avoidable complexity.** Does adding a child metasystem reduce real decision friction or variance, or only multiply roles, gates, documents, queues and statuses?

**Reasons not to instantiate a local VSM:** one work loop is already adequately regulated; a purported multiple-S1 structure is only a set of workers or batches; no evidenced inter-S1 interference requires S2; no distinct local whole-system discretionary control requires S3; no external/prospective adaptation loop requires S4; no legitimate separate identity/policy closure is present; or the parent/local existing contract already resolves the variety with less duplication.

The Profile does **not** require six separately named actors. S3* is a complementary audit function, not a mandatory seventh manager, and none of S2/S3/S3*/S4/S5 follows from component names alone.

## 4. Parent–child decision boundaries

At the **parent recursion**, cross-domain decisions remain with the function owning the relevant variety:

| Decision / disturbance | Expected classification at the parent, conditional on real evidence |
| --- | --- |
| Ordinary source diagnosis, patch verification, and maintenance in Upstream | Local Upstream **S1** variety inside an already valid envelope |
| Concrete interference or oscillation **between parent S1 domains** | Parent **S2** coordination if the specific interference and behavioral feedback path are evidenced |
| Allocation / intervention across parent domains affecting whole-system current commitments | Parent **S3** current control, with a real decision owner and return path |
| Changing external environment and prospective alternatives affecting the whole organization | Parent **S4** if the outside-and-then adaptation loop exists |
| Organizational identity, ultimate policy, or new delegation boundary | Legitimate parent **S5** decision and return-to-operation closure |

A hypothetical **child S3** may regulate that child's current internal commitments without owning the parent's shared resources or identity. A hypothetical child S5 must have a legitimate local policy/identity closure *inside* its parent-delegated envelope; it does not silently replace the real parent authority.

Delegation, message passing, branch locking or a GitHub scheduler do not automatically establish S2. An actor called `manager` does not automatically establish S3. A policy file or approval gate does not automatically establish S5. Existing external maintainer policies, CLA/consent and explicit GitHub action constraints remain effective regardless of any proposed mapping.

**Example:** Upstream can own a bounded local decision to investigate a failing native test. A cross-domain priority/resource conflict belongs to whatever parent decision path is legitimately empowered for it. A proposed expansion of Upstream's third-party publication permissions cannot be inferred from its S1 role, any local-recursion hypothesis, or the existence of a bot: it remains subject to current parent authority and target-side rules.

## 5. Candidate applications, not assessments

| Domain | Why separate recursion might be considered | Default without new evidence |
| --- | --- | --- |
| **Index** | Discovery, assessment, reassessment and evidence synchronization can become distinct durable local operations with nontrivial interactions | Keep existing S1 domain and local procedures; do not label every assessment batch a new S1 |
| **Skills** | Multiple independently maintained procedures/tooling products might eventually require local resource/control tradeoffs | Do not treat a procedure set or workflow scheduler as a child metasystem |
| **Awesome** | Editorial interaction may eventually create independently regulated operational units | Likely little benefit in adding local VSM structure unless actual residual variety emerges |
| **Upstream Contributions** | Heterogeneous external maintainer policies, native testing, contributor-fork paths and long feedback/maintenance loops could justify a richer local boundary | Worth examining **first**, but batches, parallel chats, fork count, multiple PRs and worker agents are not automatically separate S1 units or evidence of a viable child |

These are *hypotheses about possible local variety*, not assertions that the domains are currently recursive viable systems, nor comparative performance rankings.

## 6. Evidence that would advance or falsify the proposal

A limited read-only pilot could take a **specific real Upstream decision**, pin its sources and chosen parent/child system-in-focus, reconstruct the actual operative authority, and compare:

- Did the local owner have the information and rights to close the case without unnecessary parent intervention?
- Did an escalation preserve the distinction between local technical work and reserved parent/third-party authority?
- Did a purported local S2/S3/etc. mechanism address an observed disturbance and return a decision into actual work?
- Would merely adding a local VSM diagram/gate change anything, or only duplicate an already-functioning mechanism?
- Is the outcome supported by the relevant commit, CI, policy, review or operational receipt rather than by labels or documents alone?

**Failure conditions for the design hypothesis:** new local layers increase approval churn, duplicate parent authority, create uncertain ownership, block native work, or supply no clearer closure for real disturbances. A successful case would justify considering only the **smallest needed** regulatory layer, not pre-building a complete local organization.

No new organization-wide metric or automation is proposed here. Existing evidence sources are sufficient for the first inquiry.

## 7. Consequences and limitations

- Keep the **declared parent boundary** stable unless changed through the proper owner/parent process.
- Treat selective recursion as a future **system-in-focus selection** backed by concrete evidence; do not add child organization membership or authority through this note.
- Preserve autonomy grading and assessment ownership in their canonical repositories. Parent or child VSM structure by itself says nothing about `A`, `C`, `P`, `—` or `?`.
- Preserve frozen historical evidence and existing milestones. Neither proposed decomposition nor this analysis establishes M3–M5 completion.
- Keep the distinction between OpenSiro's *reference organization* and arbitrary harnesses assessed by Skills/Index; this is **not** a universal requirement for other repositories.
- Adopt any implementation only through a separate evidence-backed issue with clearly scoped rights, tests and exit conditions.

**Summary:** **one parent VSM; optional, selectively evidenced recursive VSMs; never one VSM per repository by default.** The design objective is to absorb variety at the lowest viable boundary without sacrificing parent cohesion or inventing organizations that exist only in diagrams.

## Sources

- [OpenSiro Organizational boundary](../docs/ORGANIZATION.md)
- [Cross-repository ecosystem responsibilities](../docs/ECOSYSTEM.md)
- [Supplementary design reasoning](design-reasoning.md)
- [VSM Harness Profile — recursion, function-first mapping and autonomy](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md)
- [Organization #48 — operations/metasystem split](https://github.com/opensiro/vsm-oss-organization/issues/48)
- [Organization #274 — parent-governed admission of Upstream](https://github.com/opensiro/vsm-oss-organization/issues/274)
- [Organization #330 — this discussion and proposed follow-up](https://github.com/opensiro/vsm-oss-organization/issues/330)
