# S3* complementary audit record

Use with `S3STAR_AUDIT.md`. Preserve observable evidence and judgment; do not record hidden chain-of-thought.

## Audit identity

Audit/run id:

Auditor / composed actor:

System-in-focus:

Audited S1 work item:

Audited repository revision(s):

Governing Organization-selected or explicitly frozen contract:

S3* role/prompt revision:

## Audited claim / risk

Exact claim, omission risk, or closure assertion under audit:

Why complementary audit is warranted for this claim:

## Ordinary S1 reporting path

What S1 already reports/checks:

Primary refs:

## Complementary evidence path

Evidence/access used by S3*:

Why this is materially different from the ordinary path for the declared claim:

Who controls this evidence/access path:

Primary refs:

## Audit judgment ownership

Actor exercising the audit judgment in this run:

Supporting/enforcement machinery used:

Human intervention affecting the judgment, if applicable:

## Observable findings

Facts established from complementary evidence:

Contradictions, omissions, or uncertainty:

## Audit outcome

Select exactly one:

- [ ] `PASS`
- [ ] `FINDING`
- [ ] `INSUFFICIENT`

Bounded judgment:

Confidence / evidence limitation:

## Downstream control destination

Destination for a material finding:

Finding/control-request reference:

Decision owner downstream, if already known:

## Closure

What happened to the finding/judgment:

- [ ] no material finding; bounded audit closed as `PASS`
- [ ] finding entered a current-control path
- [ ] evidence remained insufficient
- [ ] escalated outside the current audit/control boundary

Subsequent S1 effect, if any:

Closure/result refs:

## Prospective Index-batch reporting overlay (when applicable)

Use only when the governing audit contract includes the prospective reporting dimensions. This section is **additional metadata**, not another S3* verdict. For non-Index-batch audits, set `applicability: not_applicable`. For frozen historical waves, do not retrofit the original audit receipt; a separately labeled derived view may reference it.

- applicability: Index-batch / not_applicable
- owning Index batch + actual S1 board/cutoff ref:
- s1_readiness: TERMINAL / PENDING / NOT_READY (cite source):
- process_scope: RECONCILED / PARTIAL / NO_TERMINAL; numerator / eligible denominator; exact original PR/CI/catalog refs:
- semantic_scope: frozen source SHA and contract; preselected row positions; source-checked / eligible; exact bounded subclaim, unsampled limitations and primary refs:
- historical_reviewer_provenance: ESTABLISHED / UNVERIFIED / NOT_ADJUDICATED; observed reviewer evidence, source of attribution, and uncertainty:
- finding_disposition (FINDING only): ROUTED_OPEN / ADJUDICATED / VERIFIED / not_applicable:
- downstream decision owner + routed issue/comment and original evidence SHA:
- owner decision and reason (accept / reject / insufficient / not_yet_observed), dated exact-ref decision reference:
- independently verified correction or reasoned closure refs (Index PR/main SHA when applicable), or `none yet`:

Do not confuse a completed **source/PR/CI reconciliation** with a complete semantic review or a GitHub independent approval. An Index-batch `PENDING` or `UNVERIFIED` historical reviewer status does **not** change the local `PASS/FINDING/INSUFFICIENT` choice above. A routed finding is not downstream S3 closure and cannot automatically change Index grades.

## M1 constructor check

- S3* function established from a real complementary audit need? yes / no / insufficient
- ordinary reporting path explicit? yes / no / insufficient
- materially complementary evidence path explicit? yes / no / insufficient
- first-party S3*-specific judgment surface used? yes / no / insufficient
- actual judgment owner recorded separately from support machinery? yes / no / insufficient
- finding has a downstream current-control path when required? yes / no / n/a / insufficient
- boundary reachability established for the constructor path? yes / no / insufficient

For M1, this record may support `S3*=C` without an autonomous audit owner. Do not translate the record into `A`, `C`, `P`, `—`, or `?` without applying the governing Methodology and its evidence boundary.
