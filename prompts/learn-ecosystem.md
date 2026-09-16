# Learn the OpenSiro VSM Harness OSS group

Use this prompt when you want an agent to understand the in-scope public OSS workspace before taking work.

```text
Study the OpenSiro VSM Harness OSS group starting from opensiro/vsm-oss-organization.

Use current public default branches as source of truth. Read the repository scope and control plane first, then follow the authoritative chain:

VSM Harness Profile
→ VSM Harness Skills / Methodology
→ VSM Harness Index
→ Awesome VSM Harness / other explicitly in-scope curated views.

Only treat repositories listed as in-scope by opensiro/vsm-oss-organization as part of this control plane. In particular, terminal-bench-vsm, arctic-0, and opensiro.com are outside this organizational scope even if they consume, demonstrate, experiment with, or present related artifacts.

Do not use private repositories or private R&D context.

Return a concise map of:
1. what each in-scope repository owns;
2. which repository is authoritative for each kind of change;
3. the current OSM milestone and autonomy vector;
4. open work that is relevant to a new contributor;
5. any ambiguity that requires maintainer input.

Do not modify repositories unless explicitly asked.
```
