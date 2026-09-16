# Parallel M0 workstream prompts

These prompts are portable launch surfaces for separate agent/chat runs. They do not create a centralized runtime and do not change VSM semantics.

Run each workstream independently. Before making changes, every agent must inspect the current public default branch, the referenced Issue, related open PRs, and the current released Profile/Methodology contracts. GitHub current state supersedes stale text in the prompt.

Do not share one mutable branch between workstreams. Use the prepared branch named in each prompt only after checking whether it is still suitable relative to the current default branch; if the branch has become stale or already contains unrelated work, create a fresh branch from current `main` and record that decision.

Current parallel workstreams:

1. `19-executor-provenance.md` — critical path for the next instrumented M0 trial.
2. `21-task-admission-recovery.md` — S1 admission, escalation, and routine-recovery contract.
3. `22-profile-completion-oracle.md` — deterministic Profile completion checks.
4. `23-organization-completion-oracle.md` — deterministic Organization contract consistency checks.
5. `24-awesome-index-consistency.md` — deterministic Awesome ↔ Index consistency checks.

The workstreams may proceed in parallel. The next M0 autonomy trial should wait for a usable executor-provenance witness from #19, but it does not need to wait for every completion-oracle workstream.
