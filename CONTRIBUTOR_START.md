# VSM Harness OSS contributor routing

This is the common **routing** entry point for new, unclassified, cross-repository, or authority-sensitive work inside the bounded OpenSiro VSM Harness OSS group.

For already tracked work, use [`TODO.md`](TODO.md), then return to the linked owning repository/issue. Canonical membership is the `Current in-scope public repositories:` block in [`README.md`](README.md).

The work-lifecycle ownership map is [`docs/CONTROL_PLANE.md`](docs/CONTROL_PLANE.md). Milestones plan destinations, issues own durable work contracts, `TODO.md` schedules current issues, and organizational contracts own admission/execution/escalation/closure.

## Routing rule

**Repository-local work stays in the repository that owns the relevant source of truth.**

Use `opensiro/vsm-oss-organization` for organization-wide contributor roles, authority boundaries, escalation, cross-repository coordination, shared current-work selection, milestone sequencing, or evolution of the shared contribution control plane.

Public repositories outside the declared scope are not governed by this routing contract merely because they live under `opensiro`.

## Supported autonomous S1 entry

When the resolved work is one ordinary bounded operational contribution in exactly one S1 domain — Index, Skills, or Awesome — use [`modes/s1-autonomous/README.md`](modes/s1-autonomous/README.md).

```text
CONTRIBUTOR_START.md
        ↓
modes/s1-autonomous/README.md
        ↓
modes/s1-autonomous/RUN.md
        ↓
roles/S1.md + contracts/s1/*
        ↓
records/s1/runs/<record>
```

The mode does not widen authority, override an exact issue/frozen-artifact boundary, or establish `S1=A` by itself. Do not use it for genuinely cross-S1, normative, identity/ultimate-policy, security/credential, licensing, or protected-integration decisions.

## Autonomous work reporting

For substantial multi-step autonomous work, follow [`docs/AUTONOMOUS_WORK_REPORTING.md`](docs/AUTONOMOUS_WORK_REPORTING.md).

The owner-facing snapshot is:

```text
DONE
NOW
BLOCKED
NEXT
NEED YOU
```

When executing tracked work, `NOW`, `BLOCKED`, and `NEXT` should reconcile with `TODO.md`. Use `NEED YOU = none` when no real owner decision is required. This reporting contract **does not create a VSM function**, authority, scheduling truth, or autonomy state.

A `BLOCKED` scheduler/reporting state is not itself an algedonic signal.

## Parent-governed S5 entry

Any contributor may request admission to the existing parent-governed S5 process with:

```text
S5: рассмотреть <matter>
S5: consider <matter>
```

The canonical operating prompt is [`prompts/parent-control-plane.md`](prompts/parent-control-plane.md).

The prefix requests classification/routing; it does **not** transfer the unresolved S5 decisive right to the contributor. The process distinguishes:

- `S5_ADMITTED` — unresolved identity / ultimate-policy matter requiring the legitimate parent;
- `POLICY_ALREADY_GOVERNS` — existing returned parent policy determines the case;
- `NOT_S5` — the matter belongs to an already-delegated lower function;
- `INSUFFICIENT_AUTHORITY` — parent ownership cannot be reconstructed sufficiently.

The legitimate parent is defined by [`contracts/s5/parent-authority.md`](contracts/s5/parent-authority.md). Ordinary S1 work, **S3 current-control**, S3* audit, PR review, CI repair, or routine tool use must not be promoted into S5 merely because the matter is important.

## Routing conformance

Direct discoverability of the shared bootstrap/current-work/Organization route is checked mechanically. See [`docs/ROUTING_CONFORMANCE.md`](docs/ROUTING_CONFORMANCE.md) for the scoped oracle and blind-agent protocol.

## In-scope repository map

| Repository | Repository-local responsibility |
| --- | --- |
| `opensiro/vsm-harness-profile` | normative VSM Harness semantics |
| `opensiro/vsm-harness-skills` | assessment methodology, skills, validation tooling |
| `opensiro/vsm-harness-index` | evidence-backed assessments, catalog/provenance, generated views |
| `opensiro/awesome-vsm-harness` | curated downstream organizational examples |
| `opensiro/vsm-oss-organization` | contributor roles, authority, escalation, cross-repository control, work selection, organizational evolution |

## Agent decision procedure

1. Existing tracked work → [`TODO.md`](TODO.md) → linked owner.
2. Otherwise identify the starting repository's local source-of-truth responsibility.
3. Local change → stay with that repository.
4. Ordinary bounded Index/Skills/Awesome S1 contribution → [`modes/s1-autonomous/README.md`](modes/s1-autonomous/README.md).
5. Cross-repository authority/escalation/current-work/milestone/control-plane change → Organization.
6. Identity/ultimate-policy/system-boundary matter → parent-governed S5 admission above.

Public repositories such as `arctic-0`, `terminal-bench-vsm`, and `opensiro.com` remain outside this bounded system unless canonical scope is explicitly changed.
