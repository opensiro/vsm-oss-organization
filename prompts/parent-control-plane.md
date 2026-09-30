# Parent-governed S5 composition prompt

Use this prompt to compose a bounded parent-governed identity / ultimate-policy decision under [`../contracts/s5/parent-boundary.md`](../contracts/s5/parent-boundary.md) and the current legitimate-parent declaration in [`../contracts/s5/parent-authority.md`](../contracts/s5/parent-authority.md).

The Organization already has a positive S5 parent-governed witness (`S5-P-001`). Using this prompt does not by itself establish another witness, change parent authority, or complete a later milestone.

## Invocation shorthand

```text
S5: рассмотреть <matter>
S5: consider <matter>
```

The prefix is an admission request, not proof that the matter is S5 and not a transfer of S5 ownership to the contributor invoking it.

## Contributor role

A contributor may collect evidence, test whether the matter is genuinely identity/ultimate-policy level, prepare options/return targets/closure criteria, apply already-returned parent policy, record/implement a parent decision, and verify closure. These actions do not transfer unresolved S5 discretion to that contributor.

If an existing parent decision already determines the answer, apply that policy and preserve provenance where material. Do not manufacture a new S5 event.

If a genuine unresolved identity/ultimate-policy choice remains, escalate it to the legitimate parent named by the current authority declaration.

On invocation:

1. read the current parent-boundary and parent-authority contracts plus primary evidence;
2. classify the request as `S5_ADMITTED`, `POLICY_ALREADY_GOVERNS`, `NOT_S5`, or `INSUFFICIENT_AUTHORITY`;
3. if `NOT_S5`, route to the lowest function with requisite information and delegated authority;
4. if `POLICY_ALREADY_GOVERNS`, cite and apply the existing returned policy without counting a new S5 witness;
5. if `S5_ADMITTED`, prepare a compact parent decision packet with the exact matter, S5 rationale, lower-level authority considered, decisive right, legitimate parent, viable options where material, primary evidence, no-decision consequence, return targets, and closure condition;
6. the legitimate parent makes the authoritative decision;
7. record material decisions using `templates/s5-parent-decision-record.md`;
8. return/apply the decision and verify observable closure.

## Operating boundary

Apply function first, ownership second. Ordinary S1 work, S3 current-control, S3* audit, PR review/merge, permission prompts, routine plugin use, CI repair, current-work priority, or application of an already-returned parent policy are not S5 merely because a human or owner participates.

A new positive S5 witness requires a real qualifying identity/ultimate-policy matter, legitimate-parent decision, return, and observable closure. GitHub permissions, maintainer status, credentials, issue/PR transport, rulesets, connectors, CI, and other support/enforcement mechanisms do not inherit the S5 decision right.
