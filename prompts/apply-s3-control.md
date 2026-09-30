# Apply one returned S3 current-control decision to S1

Use this prompt with [`../contracts/s3/current-control.md`](../contracts/s3/current-control.md) when a declared first-party S3 constructor transaction has returned a decision to one bounded S1 work item.

```text
Apply one returned current-control decision to the affected S1 work item.

First inspect:
- the current S1 work-item boundary and admission record;
- the S3 control transaction and its immutable/current reference;
- the trigger evidence and whole-system current view;
- the recorded decision owner;
- the returned decision class and bounded instruction;
- the governing Organization-selected upstream contract or explicitly frozen historical contract.

Do not treat an arbitrary comment, approval, label, chat message, or human instruction as S3. Apply this prompt only when the transaction satisfies contracts/s3/current-control.md and explicitly targets this S1 work item.

Before applying the decision, verify:
- the transaction identifies this S1 work item/boundary;
- the decision is one of the transaction's allowed response classes;
- the actual decision owner is recorded;
- the instruction is inside the declared S3 current-control authority envelope;
- the matter is not actually identity/ultimate-policy work that must escalate elsewhere;
- the returned instruction is concrete enough to apply or explicitly reject/escalate.

Then:
- record S1 acknowledgement of the returned decision;
- apply the bounded instruction to subsequent operation;
- preserve which S1 decisions remain locally autonomous and which current constraint/intervention came from the S3 transaction;
- do not reinterpret transport/enforcement as the owner of the S3 decision;
- if applying the instruction changes the original S1 admission boundary or governing contract, re-establish admission before further ordinary execution;
- if the instruction cannot be applied without crossing an undelegated boundary, record escalation rather than improvising authority;
- preserve observable effect/closure references.

Do not record hidden chain-of-thought.

End by recording acknowledgement, application summary, effect refs, whether S1 resumed/stopped/repaired/re-entered admission, and transaction closure/escalation status.

This prompt applies a returned current-control decision. It does not create an autonomous S3 owner, establish S3=C/A by itself, or introduce S2/S4/S5.
```
