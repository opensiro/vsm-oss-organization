# Design reasoning examples

This file records reasoning patterns from the initial design discussion for `vsm-oss-organization`. It is supplementary, non-normative, and intentionally includes both reasoning that survived re-check and reasoning that was rejected or narrowed after applying the current VSM Harness Profile.

Its purpose is to help contributors avoid cargo-cult VSM mappings while evolving the organization bottom-up.

## Reasoning that survived re-check

### 1. Start from one bounded operational outcome

Good reasoning:

```text
one claimed work item
        ↓
one autonomous contribution loop
        ↓
one reviewable Issue artifact or PR
```

Why it survives:

S1 is an operational unit with an outcome, environment, and meaningful local variety. Several internal workers do not become several S1 units merely because they are separate processes or prompts.

### 2. Keep runtime ownership with the contributor

Good reasoning:

```text
OpenSiro defines role/function boundaries
contributor defines model + scheduler + budget + credentials
agent owns local organizational decisions
```

Why it survives:

The Profile separates organizational decision ownership from supporting/enforcement machinery. A scheduler can launch or constrain the loop without owning the S1 decision right.

### 3. Add S2 only after identifying inter-S1 interference

Good reasoning:

Before mapping S2, identify:

1. the distinct S1 units;
2. the concrete interference or oscillation between them;
3. the coordination path that attenuates it;
4. how the result changes subsequent S1 behaviour.

Why it survives:

Routing, delegation, message passing, and speaker selection are not sufficient evidence by themselves. See `opensiro/vsm-harness-profile#7` for the active clarification discussion.

### 4. Mutex is a useful witness, not a definition

Good reasoning:

```text
S1-A wants resource R
S1-B wants resource R
        ↓
mutual exclusion / reservation
        ↓
one proceeds, the other waits or replans
```

Why it survives:

This makes the regulated interference and closure easy to observe. But S2 is broader than mutex: schedules, negotiated plans, collision avoidance, duplicated-work prevention, and other stabilizing channels may serve the same function.

### 5. S3* can justify an early independent-audit milestone

Good reasoning:

An autonomous S1 should not be trusted merely because it reports success. A complementary agent can inspect raw evidence, tests, diffs, pinned sources, replay, or other materially different access and decide whether a finding is material.

Why it survives:

This is closer to the Profile's S3* function than ordinary production QA. The audit finding must still enter subsequent control.

### 6. Defer S4 until external/future adaptation is actually needed

Good reasoning:

Do not add S4 merely because an agent researches, learns, plans, or improves itself. Introduce S4 when the organization must distinguish external/future change, develop adaptation options, and feed them into a two-way S3 conversation.

Why it survives:

This follows the Profile's outside-and-then criterion and keeps the early system small.

## Reasoning that was rejected or narrowed

### 1. "A supervisor that delegates to specialists is S2"

Rejected as a general rule.

Example considered:

```text
Supervisor
├─ sends work to specialist A
├─ sends work to specialist B
└─ forwards context / aggregates replies
```

Why it fails:

Delegation and mediation do not show that A and B interfere or oscillate. Without a concrete coordination problem, this is routing/task decomposition rather than established S2.

### 2. "A PR boundary proves S2 is unnecessary"

Rejected as a general rule.

Why it fails:

If several independent S1 units exist, isolated branches, reservations, issue claims, or serialized PR integration may themselves attenuate their interference and therefore participate in S2.

The correct question is not "does the system use PRs?" but "what distinct S1 units exist, what interference can occur, and what regulates it?"

### 3. "If work is non-production, S2 is unnecessary"

Rejected.

Why it fails:

S2 is about destructive interference/oscillation among S1 units, not specifically production incidents. Two research or documentation S1 units can still duplicate work, invalidate each other, contend for shared state, or oscillate around incompatible interfaces.

Risk severity may affect how much coordination is required, but it does not define the function.

### 4. "Mutex is the strict definition of S2"

Rejected.

Why it fails:

Mutex covers one narrow shared-resource disturbance. Treating it as the definition would exclude valid non-locking coordination such as negotiated schedules or oscillation damping.

### 5. "GitHub scheduler / merge queue / lock is S2=A"

Rejected.

Why it fails:

Deterministic machinery can enforce a coordination decision without owning the relevant organizational discretion. `A` requires agent-owned decisive coordination judgment and operational closure.

### 6. "S3* is the algedonic channel"

Narrowed.

Corrected reasoning:

S3* is complementary independent access to operational reality. It may discover exceptional pain/opportunity and originate an algedonic signal, but the algedonic channel is the exceptional communication path to an authority capable of responding. It is not another VSM system and is not identical to S3*.

### 7. "Human approval means S5=P"

Rejected.

Why it fails:

`P` requires a genuine identity/ultimate-policy issue, transfer to a legitimate parent authority, authoritative parent decision, return of that decision, and subsequent operation governed by it. Approval of an ordinary PR or task is not S5.

### 8. "Choose the target autonomy vector first and design to fit it"

Rejected as an assessment method.

The long-term `A A A A A P` vector is a roadmap target only. Each state must emerge from a demonstrated function, decision right, owner, supporting mechanisms, and closure. Intermediate milestones are allowed to omit functions entirely.

## Current design principle

The construct should grow by elimination:

```text
start with Environment ⇄ S1
        ↓
observe residual variety
        ↓
add the smallest missing organizational function
        ↓
repeat
```

The goal is not to simulate six departments. The goal is to reach the desired autonomous organization with the fewest organizational entities needed to regulate the variety that actually exists.
