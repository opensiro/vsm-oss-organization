# VSM OSS Organization

A minimal organizational profile for autonomous OpenSiro OSS contributors.

This repository applies, but does not redefine, the public [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile). It is built bottom-up using an OSM-style elimination method: add an organizational function only when a concrete variety or disturbance cannot be absorbed by the functions already present.

## Source boundary

- Normative VSM semantics: `opensiro/vsm-harness-profile` `0.2.0`.
- Local `A/C/P/—/?` autonomy notation and assessment procedure: `opensiro/vsm-harness-skills` Methodology `0.2.2`.
- This repository is a local operationalization for OpenSiro OSS contribution. It does not redefine S1-S5.

See [CONTROL_PLANE.md](CONTROL_PLANE.md) for the released-contract boundary, frozen Index work, current cross-repository change graph, merge gates, and maintainer decision points. In particular, open semantic proposals are not treated as released Profile rules.

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
