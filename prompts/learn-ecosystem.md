# Learn the OpenSiro VSM Harness OSS group

Use this prompt when you want an agent to understand the public OpenSiro VSM Harness workspace before taking work.

```text
Start from the current public default branch of:
https://github.com/opensiro/vsm-oss-organization/blob/main/START_HERE.md

Follow START_HERE.md exactly. Do not reconstruct the ecosystem from prior chat context or from this prompt.

After following the bootstrap chain, return a concise map of:
1. what each relevant repository owns;
2. which repository is authoritative for each kind of change involved in the task;
3. current tracked work relevant to a new contributor, if any;
4. any ambiguity that genuinely requires maintainer input.

Do not modify repositories unless explicitly asked.
```

This prompt is only an executable adapter to `START_HERE.md`; it does not own a second copy of the ecosystem architecture, scope, or source-of-truth rules.
