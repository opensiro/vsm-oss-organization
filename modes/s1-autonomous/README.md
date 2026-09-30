# Autonomous S1 operating mode

Status: **supported first-party operating mode for bounded S1 contribution work**.

This mode lets a compatible autonomous agent execute one already-declared S1 contribution without custom organizational glue or step-by-step human control. The agent runtime may vary; the organizational actor, authority envelope, admission/recovery rules, closure states, and evidence record are supplied by this repository.

This mode is **not** an autonomy grade by itself. Positive `S1=A` interpretation still requires real executions and an independent assessment under the selected Profile/Methodology.

## Bootstrap route

A fresh contributor runtime should reach this mode through the normal bootstrap chain:

```text
repository README / AI handoff
        ↓
START_HERE.md
        ↓
ECOSYSTEM.md
        ↓
TODO.md + owning issue        when work is already tracked
or
CONTRIBUTOR_START.md          when work is new/unclassified
        ↓
modes/s1-autonomous/README.md
        ↓
RUN.md
```

Do not bypass an exact issue, frozen-ref, read-only, independent-context, stop, or evidence-source boundary. Those task-specific instructions remain controlling.

## Eligible work

This mode is only for one bounded operational contribution in exactly one declared S1 domain:

- **Index** — `opensiro/vsm-harness-index`;
- **Skills** — `opensiro/vsm-harness-skills`;
- **Awesome** — `opensiro/awesome-vsm-harness`.

The work must fit the canonical S1 contracts:

- [`../../contracts/s1/domain-contracts.md`](../../contracts/s1/domain-contracts.md);
- [`../../contracts/s1/task-admission-recovery.md`](../../contracts/s1/task-admission-recovery.md);
- actor adapter: [`../../roles/S1.md`](../../roles/S1.md).

If the work requires a new normative decision, organization identity/policy decision, cross-S1 authority, protected integration right, security/credential policy, licensing policy, or another undelegated right, do not stretch this mode. Escalate through the owning contract.

## First-party mode boundary

A run may use ChatGPT, Codex, another agent runtime, GitHub transport, CI, validators, or helper tools. Those mechanisms are support machinery.

For a run to count as evidence for the autonomous mode, no developer-specific code, prompt assembly, authority wiring, or hidden step-by-step human selection may be required to turn the repository contracts into the S1 actor. A compatible agent must be able to enter through this mode and execute [`RUN.md`](RUN.md) directly.

If extra custom composition is required, preserve that fact in the run record; such a run must not be cited as evidence that this first-party mode itself closes autonomous S1 ownership.

## Required run record

Every real run intended as evidence for this mode must preserve a record based on [`../../templates/s1-autonomous-run.md`](../../templates/s1-autonomous-run.md) and the machine-readable contract in [`../../schemas/s1-autonomous-run.schema.json`](../../schemas/s1-autonomous-run.schema.json).

Records belong under [`../../records/s1/runs/`](../../records/s1/runs/).

The record must make reconstructable:

- domain, work item, starting revision, and governing contract;
- admission result and declared boundary;
- ordinary decisions actually owned by the autonomous agent;
- supporting/runtime machinery separated from decision ownership;
- every human intervention and the exact decision it affected;
- disturbances and bounded recovery;
- validation and evidence;
- terminal state and reviewable artifact;
- why the autonomous actor/closure path was reachable in this supported mode.

Do not record hidden chain-of-thought.

## Exit states

A run ends with exactly one S1 terminal state:

- `CLOSED_CHANGE`;
- `CLOSED_NO_CHANGE`;
- `ESCALATED`;
- `NON_ADMITTED`.

Human merge/rejection of a reviewable PR may remain a separate integration right after S1 closure. Do not silently attribute that integration decision to the S1 actor.

## Evidence plan for `S1=A`

The initial evidence plan is intentionally narrow:

1. establish this supported first-party mode;
2. exercise one real bounded run in **Index**;
3. exercise one real bounded run in **Skills**;
4. exercise one real bounded run in **Awesome**;
5. freeze the resulting evidence and run a fresh independent general assessment.

No file in this directory may declare `S1=A` merely because the mode exists or because one run succeeded.
