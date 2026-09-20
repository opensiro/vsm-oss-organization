# S5 parent decision record

Use this template only for a matter admitted under [`S5_PARENT_BOUNDARY.md`](../S5_PARENT_BOUNDARY.md).

The record makes one parent-governed identity / ultimate-policy decision reconstructable. It does not establish `S5=P` merely because the fields are completed.

## Decision identity

- decision / work item id:
- date:
- system-in-focus:
- governing Organization revision:
- governing Profile / Methodology contract:

## Matter

- exact identity / ultimate-policy question:
- why this is S5-level at the declared recursion:
- lower-level S1 / S3 / S3* authority considered:
- why the matter cannot be closed safely inside that delegated envelope:

## Parent authority

- legitimate parent role:
- concrete decision owner:
- primary evidence of parent legitimacy:
- decisive S5 right:
- authority limits / caveats:

If legitimate parent authority is not reconstructable, use `INSUFFICIENT_AUTHORITY` and do not claim `S5=P`.

## Evidence / options

- primary evidence refs:
- relevant current policy / identity state:
- viable options considered, if material:
- consequence of no decision:

## Parent decision

- lifecycle state: `ESCALATED | DECIDED | APPLIED | CLOSED | INSUFFICIENT_AUTHORITY | CANCELLED`
- authoritative decision:
- returned policy / identity constraint:
- decision evidence ref:

## Support / enforcement

List mechanisms that transport or enforce the decision without owning it:

- GitHub issue / PR:
- ruleset / permissions:
- plugin / connector:
- CI / validator:
- other support:

## Return into Organization

- return target(s):
- acknowledgement / application ref(s):
- expected change or intentional preservation in subsequent operation:
- observed effect:

## Closure

- final state:
- closure evidence:
- remaining uncertainty:
- does this record support a positive `S5=P` witness? `YES | NO | INSUFFICIENT`
- rationale:

## Boundary checks

- [ ] matter is genuinely identity / ultimate-policy level;
- [ ] legitimate parent role is explicit;
- [ ] concrete decision owner is explicit;
- [ ] parent legitimacy is evidenced independently of mere technical access;
- [ ] decisive right is separated from support/enforcement;
- [ ] returned decision reaches Organization operation;
- [ ] subsequent operation changes or is intentionally preserved under the returned decision;
- [ ] ordinary approval / merge / permission prompt is not being misclassified as S5;
- [ ] no unrelated S2 / S3 / S3* / S4 autonomy claim is inferred from this record.
