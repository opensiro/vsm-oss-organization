# Autonomous S1 run records

This directory stores concrete execution records produced by the supported [`../../../modes/s1-autonomous/`](../../../modes/s1-autonomous/) operating mode.

Records are evidence artifacts, not autonomy grades and not canonical Index assessments.

A record intended for later `S1=A` review must:

- correspond to one real bounded S1 work item;
- identify exactly one declared domain: Index, Skills, or Awesome;
- preserve the starting revision and governing task/contract artifacts;
- separate agent-owned decisions from runtime/support machinery;
- record every human intervention that affected a decision right;
- record disturbances/recovery and validation;
- end in one canonical S1 terminal state;
- explain boundary reachability and whether custom organizational composition was required.

Use [`../../../templates/s1-autonomous-run.md`](../../../templates/s1-autonomous-run.md) and [`../../../schemas/s1-autonomous-run.schema.json`](../../../schemas/s1-autonomous-run.schema.json).

The initial evidence sequence is one real run per declared domain before any fresh independent general reassessment:

```text
Index witness
    +
Skills witness
    +
Awesome witness
    ↓
frozen evidence set
    ↓
independent assessment
```

Do not manufacture synthetic work solely to create a positive autonomy witness.
