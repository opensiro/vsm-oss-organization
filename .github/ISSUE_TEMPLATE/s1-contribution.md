---
name: S1 contribution
about: Define one bounded autonomous contribution unit
title: "[S1] "
labels: ""
assignees: ""
---

## System-in-focus

Repository / boundary:

## Start revision

Repository start commit SHA:

## Outcome

What reviewable artifact should this S1 produce?

## Exact role / prompt revision

Which role or prompt governs this contribution? Pin the repository revision, blob SHA, release, or other immutable identifier when available.

## Runtime / harness support

What runtime, scheduler, model, tools, or harness transport are being used?

These are supporting mechanisms. Do not infer organizational decision ownership from runtime or enforcement capability alone.

## Human-provided constraints

Which constraints, acceptance conditions, or boundaries were supplied by the contributor before execution?

## Evidence / checks

What primary evidence, tests, or validation determine completion?

## Local decision rights

Which implementation/research/evidence/repair decisions may the autonomous S1 make without escalation?

## Forbidden decisions

Which decisions are explicitly outside this S1's delegated authority?

## Escalation conditions

Which observed conditions require the S1 to stop or transfer the decision rather than decide locally?

## Expected closure artifact

- [ ] Issue artifact
- [ ] Pull Request
- [ ] Other (explain)

## Observable decision trail

Record only organizationally relevant observable decisions. Do not record hidden chain-of-thought.

For each material decision, preserve:

```text
decision
→ evidence available at that moment
→ chosen action
→ why the decision remained inside S1 authority
```

Examples include choosing one file over another, classifying a reference as historical rather than stale, rebuilding from a newer base, repeating a validation check, stopping for insufficient evidence, or escalating because authority was exceeded.

## Notes

Do not add S2/S3/S3*/S4/S5 labels merely because the implementation uses multiple agents, a scheduler, tests, routing, or human approval. Map organizational function first.
