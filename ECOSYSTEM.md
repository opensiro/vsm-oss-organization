# OpenSiro VSM Harness ecosystem architecture

Status: **cross-repository architecture note**

This document explains how the public OpenSiro VSM Harness repositories relate to one another and where cross-repository responsibilities belong.

It does **not** redefine VSM semantics, assessment methodology, canonical assessment state, or the current organizational boundary of `opensiro/vsm-oss-organization`.

Repository-local documentation remains authoritative for how each repository works internally. This document owns only the shared architectural relationship between those repositories and adjacent research tracks.

## Source-of-truth rule

Use the repository that owns the fact or procedure being discussed:

| Question | Source of truth |
| --- | --- |
| What do S1, S2, S3, S3*, S4, S5, recursion, autonomy, variety, escalation and closure mean? | `opensiro/vsm-harness-profile` |
| How is a standalone repository VSM assessment performed and classified? | `opensiro/vsm-harness-skills` |
| What is the accepted repository-relative VSM assessment of a harness? | `opensiro/vsm-harness-index` |
| What empirical evidence supports general per-function capability comparisons? | `opensiro/vsm-harness-capability` (**experimental**) |
| Which organizational forms are selected as representative examples? | `opensiro/awesome-vsm-harness` |
| How are the bounded VSM OSS repositories organized, routed and coordinated? | `opensiro/vsm-oss-organization` |

Do not duplicate repository-owned facts into this repository when a stable reference to the owning source is sufficient.

## Current released architecture

The current released VSM Harness chain is:

```text
Beer / cybernetics
        ↓
vsm-harness-profile
  normative VSM semantics
        ↓
vsm-harness-skills
  assessment + classification methodology
        ↓
vsm-harness-index
  repository-relative canonical assessment corpus
        ↓
awesome-vsm-harness
  curated representative downstream view
```

This chain separates semantics, procedure, canonical assessment instances and curation.

The current bounded `vsm-oss-organization` system remains the one declared in [`README.md`](README.md) and [`ORGANIZATION.md`](ORGANIZATION.md). In particular, the current operational S1 domains remain Index, Skills and Awesome. The experimental Capability repository described below exists outside that bounded system unless and until a separate organizational-boundary change admits it.

## Experimental capability layer

[`opensiro/vsm-harness-capability`](https://github.com/opensiro/vsm-harness-capability) is an **experimental adjacent research repository** for a separate question from canonical VSM assessment. It was bootstrapped from the predecessor `vsm-harness-index/experiments/functional-capability-depth` research surface; active capability ownership now lives here while canonical assessment ownership remains in the Index.

```text
canonical VSM assessment:
Which organizational functions exist at the declared boundary,
and who owns their decisive closure?

general functional capability:
Given an established VSM function,
what empirical evidence exists about how capable that function is
across systems under comparable conditions?
```

The intended distinction is:

```text
canonical closure / ownership
        ≠
general functional capability
        ≠
domain-specific assessment
```

A canonical ownership state such as `A`, `C`, `P`, `A(P)`, `C(P)`, `—`, or `?` is not a performance score. Conversely, benchmark performance does not create or change a canonical ownership state.

### Repository boundary

The repository is:

```text
opensiro/vsm-harness-capability
```

Its intended scope is **general functional capability**. The word `general` is intentionally a scope property rather than part of the repository name.

The repository is currently **experimental**. Its existence does not make it a current S1 domain and does not expand the canonical five-repository `vsm-oss-organization` boundary.

Its intended durable responsibilities are:

- neutral public system observations and provenance;
- linkage between public benchmark/evidence surfaces and concrete systems;
- derived VSM-function relevance mappings that reference, but do not redefine, Profile semantics;
- materially matched comparison cells where public evidence supports them;
- per-function general capability baselines and current evidence frontier;
- frozen historical artifacts migrated from the predecessor `functional-capability-depth` experiment.

It must not own:

- VSM function semantics;
- canonical repository VSM assessments or autonomy states;
- a global harness score;
- a maturity ordering over `A`, `C`, and `P`;
- domain-specific admission, autonomy or evidence requirements;
- an OpenSiro-operated benchmark program whose purpose is to manufacture missing capability evidence.

If a capability evaluation procedure later becomes normative, the procedure belongs in `opensiro/vsm-harness-skills`. If new VSM semantics are required, those semantics belong in `opensiro/vsm-harness-profile` first.

## Meaning of general capability

`vsm-harness-capability` is intended to study **application-domain-independent capability claims about individual VSM functions**.

General capability does not mean an average over domain benchmarks and does not mean that one specialized benchmark is automatically universal evidence.

```text
strong SWE result
        ≠ automatically
strong general S1 capability
```

A capability claim is general only when the intended claim is not restricted to one application domain and the evidence supports that broader scope. Support may come from function-focused evidence, cross-domain replication, independently supported transfer, or another explicit argument for generality.

A raw observation may still record factual context such as:

```text
task domain: software engineering
benchmark: SWE-bench
```

That context is provenance. It does not by itself turn the general capability repository into a SWE assessment system.

## General capability evidence flow

The intended experimental flow is:

```text
public benchmark / paper / leaderboard /
repository result / operational witness
        ↓
evidence-surface identity
        ↓
concrete system identity
        ↓
neutral raw observation
        ↓
provenance + execution metadata
        ↓
optional VSM-function projection
        ↓
general capability comparison
```

The raw observation should be stored once. Function-specific interpretations and comparison views reference the observation rather than copying the empirical payload into parallel databases.

The raw evidence layer does not infer VSM meaning from benchmark vocabulary. Labels such as `coordination`, `manager`, `verification`, `learning`, or `governance` do not automatically establish S2, S3, S3*, S4, or S5.

The canonical Index remains independent:

```text
repository @ pinned revision
        ↓
canonical VSM function / ownership assessment
```

A capability system may link to canonical Index identity and assessment provenance, but it does not own or mutate those facts.

## Domain-specific specialization

Future domain-specific repositories should be treated as **fresh assessment systems**, not filtered views of `vsm-harness-capability`.

A possible naming convention is:

```text
vsm-harness-capability-swe
vsm-harness-capability-science
vsm-harness-capability-<domain>
```

The fourth name component identifies the specialization. The unsuffixed `vsm-harness-capability` remains the general layer.

A domain-specific repository may consume:

- normative VSM semantics from `vsm-harness-profile`;
- canonical repository-relative findings from `vsm-harness-index`;
- reusable public observations or general capability evidence from `vsm-harness-capability`;
- additional domain-specific public evidence.

It then defines its own domain contract, including as appropriate:

- operating purpose and system-in-focus;
- admission boundary;
- required or permitted ownership arrangements for that purpose;
- domain-specific evidence requirements;
- domain-specific capability requirements;
- its own assessment corpus and derived views.

A domain-specific autonomy requirement does not redefine `A`, `C`, `P`, or any VSM function. It states which Profile-defined arrangements are required, permitted, or insufficient for a particular operating purpose.

Therefore a domain-specific assessment is not equivalent to:

```text
vsm-harness-capability
WHERE task_domain = <domain>
```

Instead:

```text
Profile semantics
        +
canonical general assessment evidence
        +
general capability evidence
        +
domain-specific system boundary
        +
domain-specific autonomy requirements
        +
domain-specific evidence requirements
        ↓
fresh domain-specific assessment
```

The same upstream repository may legitimately receive different conclusions in the canonical general Index and in a domain-specific index when the declared system-in-focus, operating purpose, reachable organizational paths, autonomy requirements or evidence boundary differ.

## Relationship to Awesome

`opensiro/awesome-vsm-harness` may organize representative systems by operating domain, but that is a curation and presentation choice rather than a separate domain assessment methodology.

Domain relevance and organizational shape remain separate dimensions. A future domain-specific capability repository should therefore not be implemented inside Awesome merely because Awesome already presents domain-oriented examples.

## Relationship to executable research

`opensiro/terminal-bench-vsm` remains an executable research/experimental artifact with its own product/evaluator boundary. It may provide useful architectural or empirical evidence, but it is not the normative source for general capability methodology.

`opensiro/arctic-0` remains a separate research track concerned with sample-blind capability transfer into compact student models. It is not part of the VSM Harness capability hierarchy.

`opensiro/opensiro.com` remains a presentation layer. It may present synchronized explanations or derived views, but canonical claims remain in their owning repositories.

## Documentation ownership

Use this split when adding documentation:

```text
repository-local implementation / schema / workflow
        → owning repository

cross-repository responsibility / dependency / boundary
        → vsm-oss-organization

plain-language public presentation
        → opensiro.com
```

Examples:

- capability observation schema → `vsm-harness-capability`;
- why Capability is separate from Index → this document;
- definition of S3* → `vsm-harness-profile`;
- procedure for canonical S3* assessment → `vsm-harness-skills`;
- accepted S3* state for a particular harness → `vsm-harness-index`;
- SWE-specific evidence threshold → future SWE-specific repository;
- visual explanation for visitors → `opensiro.com`.

## Promotion boundary

The capability architecture described here is **experimental**.

The existence of `vsm-harness-capability` does not automatically make it part of the bounded `vsm-oss-organization` system. Admission into that system requires a separate explicit boundary change with corresponding updates to organizational contracts, routing, observability and any S1-domain construction evidence required by the organization.

Likewise, creating a domain-specific capability repository does not automatically place it inside the same bounded organization.

This keeps architectural explanation separate from claims that a new organizational function or operational domain has already been established.
