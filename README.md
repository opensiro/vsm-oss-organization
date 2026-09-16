# VSM OSS Organization

A minimal organizational profile for autonomous OpenSiro OSS contributors.

This repository applies, but does not redefine, the public [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile). It is built bottom-up using an OSM-style elimination method: add an organizational function only when a concrete variety or disturbance cannot be absorbed by the functions already present.

## Scope

This repository is the organizational/control plane for the **public OpenSiro OSS group**. It is not a control plane for every OpenSiro project, account, or private R&D activity.

Current in-scope public repositories:

- `opensiro/vsm-harness-profile`
- `opensiro/vsm-harness-skills`
- `opensiro/vsm-harness-index`
- `opensiro/awesome-vsm-harness`
- `opensiro/terminal-bench-vsm`
- `opensiro/arctic-0`
- `opensiro/opensiro.com`
- `opensiro/vsm-oss-organization`

The repositories remain separate systems with separate sources of truth. Inclusion here means their **public OSS contribution work** may be organized through this contributor/control plane; it does not transfer semantic ownership between repositories.

`arctic-0` remains a separate research track. Its inclusion in the OSS organizational scope does not make ARCTIC part of the VSM Harness Index architecture.

Out of scope by default:

- private OpenSiro repositories and private R&D context;
- credentials, local contributor runtimes, schedulers, model providers, budgets, and sandboxes;
- third-party upstream repositories except as environment/evidence for an in-scope contribution;
- downstream forks or projects not explicitly admitted to this public OSS scope.

A repository may be added to or removed from this scope only explicitly; org membership or naming alone is not enough.

## FOR CONTRIBUTORS

You do not need to implement a VSM runtime to start contributing. Use the prompts as portable entry points with your own agent/runtime:

1. **New to OpenSiro OSS:** [prompts/learn-ecosystem.md](prompts/learn-ecosystem.md) — map the repositories, authority boundaries, current milestone, and open work before changing anything.
2. **Ready to work:** [prompts/contribute.md](prompts/contribute.md) — execute one bounded contribution under the current S1-first contract.
3. **Want an explicit control plane now:** [prompts/parent-control-plane.md](prompts/parent-control-plane.md) — demo a human-parent autonomy envelope and escalation interface ahead of the full M2 implementation.

The prompt pack is operational guidance, not additional VSM semantics and not evidence that a future roadmap milestone is already complete.

## Source boundary

- Normative VSM semantics: `opensiro/vsm-harness-profile` `0.2.1`.
- Local `A/C/P/—/?` autonomy notation and assessment procedure: `opensiro/vsm-harness-skills` Methodology `0.2.3`.
- This repository is a local operationalization for OpenSiro OSS contribution. It does not redefine S1-S5.

See [CONTROL_PLANE.md](CONTROL_PLANE.md) for the released-contract boundary, frozen Index work, current cross-repository change graph, merge gates, and maintainer decision points. Open semantic proposals are never treated as released Profile rules.

## Contribution model

OpenSiro defines organizational roles and GitHub contribution boundaries. Contributors own their runtime:

```text
OpenSiro contribution contract
        ↓
contributor-owned scheduler / harness / credentials / budget
        ↓
VSM role prompt(s)
        ↓
autonomous contribution
        ↓
Issue / Pull Request
```

A contributor may use one agent or many internal workers. Internal workers are not separate S1 units merely because they are separate processes or prompts. The current minimal system-in-focus is one bounded contribution loop with one operational outcome.

## OSM roadmap

The implementation starts from the smallest useful organization and introduces functions only when their disturbance appears.

Current milestone:

```text
S1  S2  S3  S3* S4  S5
A   —   —   —   —   —
```

Long-term reference target:

```text
S1  S2  S3  S3* S4  S5
A   A   A   A   A   P
```

The final vector is a design target, not a present assessment claim. `A`, `C`, and `P` are ownership arrangements, not maturity scores; the milestone ordering is the construction sequence for this reference organization rather than a universal VSM installation order. Each milestone has explicit entry and exit conditions in [ROADMAP.md](ROADMAP.md).

## Current role

Only the S1 role is standardized in the first milestone. See [roles/S1.md](roles/S1.md).

Future roles are added only when the roadmap establishes a concrete organizational need for them. This is deliberate: VSM functions are organizational responsibilities, not a checklist of permanent agent processes.

## Design rationale

See [supplementary/design-reasoning.md](supplementary/design-reasoning.md) for worked examples from the design discussion, including reasoning that survived re-check and reasoning that was rejected or narrowed after applying the current Profile.