# Parent-governed S5 composition prompt

Use this prompt to compose a bounded parent-governed identity / ultimate-policy decision under [`S5_PARENT_BOUNDARY.md`](../S5_PARENT_BOUNDARY.md).

This is preparatory M2 operating guidance. It does **not** establish `S5=P` merely because a human is present or because the prompt is used.

```text
Act inside the bounded OpenSiro VSM Harness OSS scope defined by opensiro/vsm-oss-organization.

First read:
- README.md
- ORGANIZATION.md
- ROADMAP.md
- S5_PARENT_BOUNDARY.md
- roles/S1.md
- S3_CONTROL_SURFACE.md
- S3STAR_AUDIT.md

Apply function first, ownership second.

1. Identify the exact matter that may require a parent decision.
2. Decide whether it is genuinely identity / ultimate-policy level at this recursion.
3. If ordinary S1, S3, or S3* authority can safely close it, keep it there and do not call it S5.
4. If it is S5-level, identify:
   - the delegated local envelope being exceeded;
   - the exact decisive right;
   - the legitimate parent role;
   - the concrete decision owner;
   - primary evidence showing why that owner legitimately holds the right;
   - the Organization return target;
   - the closure condition.
5. If parent legitimacy cannot be reconstructed, record INSUFFICIENT_AUTHORITY rather than inferring authority from GitHub access, merge power, credentials, or maintainer status.
6. Escalate the matter with:
   - policy / identity question;
   - primary evidence and context;
   - viable options where material;
   - consequence of no decision.
7. After the legitimate parent decides, record the result using templates/s5-parent-decision-record.md.
8. Separate GitHub issues/PRs, rulesets, permissions, plugins, CI, and other support/enforcement from the actual S5 decision owner.
9. Return the parent decision into the affected Organization path and record acknowledgement/application.
10. Confirm the decision changes or intentionally preserves subsequent operation with reviewable closure evidence.

Do not treat the following as S5 by themselves:
- ordinary task approval;
- PR review or merge;
- permission prompts;
- installing/using a plugin;
- current-work priority or retry decisions;
- CI repair;
- one assessment admission/rejection;
- a static policy document with no real decision/return loop.

Until a real qualifying case has legitimate-parent evidence and returned operational closure, describe this as preparatory M2 composition and do not claim S5=P completion.
```