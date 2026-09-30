# Organizational contracts

This directory contains the first-party organizational protocols used by the bounded Opensiro VSM Harness OSS organization.

The repository separates three artifact classes deliberately:

```text
contracts/
  what organizational path, authority envelope, and closure rule exist

roles/
  how a composed actor participates in an already-defined contract

records/
  evidence that a concrete function/path actually ran
```

The presence of a contract or role does **not** establish that the corresponding VSM function is currently evidenced at a positive assessment state. Function mapping, ownership, boundary reachability, and closure remain evidence questions under the selected Profile and Methodology.

## Current layout

- `s1/domain-contracts.md` — local operational envelopes for Index, Skills, and Awesome.
- `s1/task-admission-recovery.md` — S1 admission, recovery, intervention, escalation, and terminal-state contract.
- `s3/current-control.md` — S3-specific current-control request/decision/return constructor.
- `s3star/audit.md` — complementary-audit constructor contract.
- `s5/parent-boundary.md` — parent-governed identity/ultimate-policy admission and return contract.
- `s5/parent-authority.md` — current legitimate-parent declaration.
- `tools/external-entry.md` — admission/delegation contract for external tools and connectors.

Normative S1-S5 semantics remain owned by `opensiro/vsm-harness-profile`. These files operationalize the selected semantics for this reference organization; they do not redefine them.
