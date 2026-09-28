# Upstream Intervention Fit

Status: **experimental**

Issue: #165

This experiment asks whether upstream changes motivated by OpenSiro assessment/research remain independently useful to the upstream project when OpenSiro/VSM/grade pressure is removed from the rationale.

It is intentionally outside the canonical organization metrics contract. Nothing here changes `METRICS.md`, `metrics.yaml`, VSM semantics, assessment methodology, canonical grades, or organizational authority.

## Unit of observation

One observation is one **upstream intervention identity**: normally an upstream pull request, or a pre-PR branch/issue if no PR exists yet.

Rebases, review-fix commits, force-pushes, and revisions do not create new observations.

Every intervention materially initiated or shaped by OpenSiro assessment/research belongs in the log, including rejected, withdrawn, closed-unmerged, and unsuccessful work.

## Primary metric

`product_native_fit_rate`

```text
completed fit reviews = pass + fail
product_native_fit_rate = pass / completed fit reviews
```

`pending` interventions are reported but excluded from the denominator until the fit review is complete.

This is not an upstream acceptance rate and not a VSM-grade-improvement rate.

## Fit gates

An intervention derives `pass` only when **all four** gates are supported by public evidence:

1. **upstream_need** — public upstream evidence or maintainer evidence supports a real upstream-native need, risk, problem, or workflow served by the intervention;
2. **native_mechanism** — the intervention uses or extends an upstream-owned mechanism/pattern rather than adding a VSM-only control surface;
3. **counterfactual_value** — the intervention remains justifiable if all OpenSiro, VSM, assessment, and grade language is removed;
4. **scope_compatibility** — current public upstream scope/direction does not conflict with the intervention.

Gate states are:

- `pass` — evidence supports the gate;
- `fail` — evidence materially contradicts the gate, or a completed negative-evidence review establishes that the required upstream-native basis is absent;
- `unknown` — evidence is incomplete.

Derived fit state:

```text
any gate = fail                  -> fail
all gates = pass                 -> pass
otherwise                        -> pending
```

A maintainer merge/approval is strong evidence but is not required and is not itself the metric. Likewise, a rejected PR is not automatically a fit failure: maintainers may reject a product-native change for implementation, timing, maintenance, or other reasons.

## Evidence discipline

Prefer, in order:

1. explicit maintainer statements or accepted upstream issue/roadmap intent;
2. current first-party upstream documentation and architecture;
3. current first-party implementation/extension points;
4. repository-wide negative-evidence review when a proposed responsibility appears to have no upstream-native basis.

OpenSiro's own assessment or desired grade cannot satisfy any gate.

## Anti-gaming rules

- Log all OpenSiro-shaped upstream interventions, not only successful ones.
- One intervention identity counts once regardless of revisions.
- Never use a grade increase as fit evidence.
- Do not classify `unknown` as `pass` to improve the metric.
- Do not convert merge state into fit state mechanically.
- Preserve closed/withdrawn observations; they remain part of experiment history.
- If evidence changes, update the observation and regenerate the snapshot rather than rewriting history elsewhere.

## Files

- `metric.json` — machine-readable metric and gate contract;
- `observations.json` — intervention log and evidence summaries;
- `compute.py` — deterministic stdlib-only validator/renderer;
- `snapshot.json` — generated current metric projection.

Run:

```bash
python experiments/upstream-intervention-fit/compute.py
python experiments/upstream-intervention-fit/compute.py --check
python experiments/upstream-intervention-fit/compute.py --stdout
```

## Initial cohort

The bootstrap cohort records the current interventions around:

- Marveen #1516;
- oh-my-agent #819;
- Scion #2047;
- Headcount #47;
- Henterprise #1.

The initial snapshot intentionally leaves incomplete reviews as `pending` rather than guessing fit.

## Extraction boundary

This directory is designed to move to a dedicated repository later without depending on Organization collectors or canonical metrics machinery.

A future extraction should be able to preserve the experiment contract, observations, computation, and snapshot essentially unchanged. Promotion/extraction is a separate decision; existence here does not admit a new repository into the bounded VSM OSS organization.
