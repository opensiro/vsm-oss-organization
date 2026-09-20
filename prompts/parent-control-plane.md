# Parent-governed S5 composition prompt

Use this prompt to compose a bounded parent-governed identity / ultimate-policy decision under [`S5_PARENT_BOUNDARY.md`](../S5_PARENT_BOUNDARY.md) and the current legitimate-parent declaration in [`S5_PARENT_AUTHORITY.md`](../S5_PARENT_AUTHORITY.md).

The Organization already has a positive `S5=P` witness (`S5-P-001`). Using this prompt does **not** by itself establish another S5 witness, change the parent authority, or formally complete M2 while M1 remains open.

## Invocation shorthand

Any contributor may initiate S5 admission/review with either form:

```text
S5: рассмотреть <matter>
S5: consider <matter>
```

Example:

```text
S5: рассмотреть включение opensiro/example-repo в bounded VSM Harness OSS organization
```

The prefix is an **admission request**, not proof that the matter is S5 and not a transfer of S5 ownership to the contributor invoking it. The first step is always to classify the organizational function.

## Contributor role in the S5 process

A contributor may operate the S5 process without owning the decisive S5 right. In particular, a contributor may:

- collect and preserve primary evidence;
- test whether the matter is genuinely identity / ultimate-policy level;
- identify the delegated lower-level envelope and why it is or is not sufficient;
- prepare viable options, consequences, return targets, and closure criteria;
- apply an already-returned parent policy when the present case is fully determined by that policy;
- record and implement a parent decision after it has been made;
- verify that the returned decision reaches the affected Organization path and closes observably.

These activities are support, composition, transport, application, and evidence work. They do not make the contributor the S5 owner merely because the contributor runs the prompt, writes the record, opens/merges a PR, or performs the resulting implementation.

If an existing parent decision already determines the answer inside the delegated envelope, apply that policy and record provenance where material. **Do not manufacture a new S5 event simply because a contributor encountered or applied an existing policy.**

If a genuine unresolved identity / ultimate-policy choice remains, escalate it to the legitimate parent identified by `S5_PARENT_AUTHORITY.md`. The contributor must not choose between unresolved S5 alternatives unless the governance declaration itself explicitly delegates that decisive right.

On receiving the shorthand:

1. read the current `S5_PARENT_BOUNDARY.md` and `S5_PARENT_AUTHORITY.md` plus the primary evidence relevant to the matter;
2. classify the request as one of:
   - `S5_ADMITTED` — genuine unresolved identity / ultimate-policy matter at this recursion;
   - `POLICY_ALREADY_GOVERNS` — an existing returned parent policy already determines the case without a new S5 decision;
   - `NOT_S5` — safely owned by an already-delegated lower function;
   - `INSUFFICIENT_AUTHORITY` — the matter may be S5 but legitimate parent ownership cannot be established;
3. if `NOT_S5`, route it to the lowest function with requisite information and delegated authority and do not continue the S5 path;
4. if `POLICY_ALREADY_GOVERNS`, cite the governing parent decision/policy, apply it through the appropriate lower function or support mechanism, and record closure where material; do not count the application as a new S5 witness;
5. if `S5_ADMITTED`, produce a compact parent decision packet containing:
   - exact matter;
   - S5 rationale;
   - lower-level authority considered and why it cannot close the matter;
   - decisive S5 right;
   - legitimate parent role and concrete holder;
   - viable options where material;
   - relevant primary evidence;
   - consequence of no decision;
   - return targets;
   - closure condition;
6. the legitimate parent then makes the authoritative decision;
7. record the result using `templates/s5-parent-decision-record.md` when the decision is material enough to preserve as Organization evidence;
8. return/apply the decision into the affected Organization path and verify observable closure.

A clear parent instruction can contain both the admission request and the intended decision, but it still must pass S5 admission before being recorded as S5. Technical ability to execute the instruction does not determine its VSM function.

## Full operating prompt

```text
Act inside the bounded OpenSiro VSM Harness OSS scope defined by opensiro/vsm-oss-organization.

First read:
- README.md
- ORGANIZATION.md
- ROADMAP.md
- S5_PARENT_BOUNDARY.md
- S5_PARENT_AUTHORITY.md
- roles/S1.md
- S3_CONTROL_SURFACE.md
- S3STAR_AUDIT.md

Apply function first, ownership second.

1. Identify the exact matter that may require a parent decision.
2. Decide whether it is genuinely identity / ultimate-policy level at this recursion.
3. Check whether an existing returned parent decision already determines the case.
   - If yes, classify POLICY_ALREADY_GOVERNS, cite that policy, and apply it through the appropriate lower function/support path. Do not manufacture a new S5 event.
4. If ordinary S1, S3, or S3* authority can safely close the matter, keep it there and do not call it S5.
5. If an unresolved S5-level choice remains, identify:
   - the delegated local envelope being exceeded;
   - the exact decisive right;
   - the legitimate parent role;
   - the concrete decision owner;
   - primary evidence showing why that owner legitimately holds the right;
   - the Organization return target;
   - the closure condition.
6. If parent legitimacy cannot be reconstructed, record INSUFFICIENT_AUTHORITY rather than inferring authority from GitHub access, merge power, credentials, maintainer status, or the fact that a contributor is running this prompt.
7. Escalate the unresolved matter with:
   - policy / identity question;
   - primary evidence and context;
   - viable options where material;
   - consequence of no decision.
8. The contributor may research, compose, transport, record, implement, and verify the process, but MUST NOT exercise unresolved S5 discretion unless the current governance declaration explicitly delegates that decisive right.
9. After the legitimate parent decides, record the result using templates/s5-parent-decision-record.md.
10. Separate GitHub issues/PRs, rulesets, permissions, plugins, CI, contributor actions, and other support/enforcement from the actual S5 decision owner.
11. Return the parent decision into the affected Organization path and record acknowledgement/application.
12. Confirm the decision changes or intentionally preserves subsequent operation with reviewable closure evidence.

Do not treat the following as S5 by themselves:
- ordinary task approval;
- PR review or merge;
- permission prompts;
- installing/using a plugin;
- current-work priority or retry decisions;
- CI repair;
- one assessment admission/rejection;
- a static policy document with no real decision/return loop;
- a contributor applying an already-returned parent policy.

Do not infer a new S5 witness merely because this prompt was invoked. A new positive witness requires a real qualifying identity / ultimate-policy matter, legitimate-parent decision, return, and observable closure.
```
