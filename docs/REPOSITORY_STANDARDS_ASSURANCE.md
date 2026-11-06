# Repository Standards Assurance — bounded S3/S3* support

**Work contract:** [Organization #288](https://github.com/opensiro/vsm-oss-organization/issues/288). **Status:** deterministic read-only probe and initial evidence; **not** a new mandatory organizational policy, active autonomous auditor, independent S3* judgment, or S3 transaction.

## Functional ownership

The governing [Profile](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md) maps operations by function and decisive right, not by script or actor name.

| Stage | Organizational function | Boundary |
| --- | --- | --- |
| Source observation | Supporting probe | Raw GitHub API readback, branch SHA and README/artifact inspection; never acts as a decision owner |
| Independent challenge of material S1/S3 claims | **S3*** only if admitted under [`contracts/s3star/audit.md`](../contracts/s3star/audit.md) | Claim-relative independence, complementary evidence, discretionary owner, `PASS` / `FINDING` / `INSUFFICIENT`, explicit return destination |
| Current whole-system constraints and response | **S3** only for a genuine [`contracts/s3/current-control.md`](../contracts/s3/current-control.md) case | Qualified whole-system need, legitimate decision holder, bounded response, affected S1 application and closure |
| Local repository correction | **S1** in the admitted Index, Skills, Awesome, or Upstream Contributions operational domain | Local owner decides implementation, validation, reviewable PR, residual escalation; no new decision rights follow from a probe |
| New obligatory organization policy or system boundary | **S5** when identity/ultimate policy or domain admission is actually affected | No inferred parent act from comparison tables or this document |

The Organization currently has **four** operational S1 domains across **six** in-scope repositories. [S5 #274](https://github.com/opensiro/vsm-oss-organization/issues/274#issuecomment-6420871211) admitted Upstream Contributions with a bounded envelope, and its construction gate has subsequently been accepted. `opensiro/upstream` is therefore subject to the same **already-adopted root README routing invariant** as the other five repositories. Its external publication, licensing, and repository-admin choices remain with their own legitimate owners; domain admission did not transfer those rights. Experimental Capability and other public OpenSiro repositories remain adjacent unless separately admitted.

## Existing standards inventory — policy owner and scope

This is a classification of **already effective** obligations versus observed practices, **not** a new standard adopted by this document. The probe's machine-readable `rule=ADVISORY` includes both preferred and informational checks; the following table preserves that distinction for human disposition.

| Class | Current checks / evidence | Owning authority and consequence |
| --- | --- | --- |
| **REQUIRED** | Root README directly links shared START_HERE, Organization contributor route, and TODO | [Organization routing conformance](ROUTING_CONFORMANCE.md), all **six** currently in-scope repositories; a proven missing link is `NON_COMPLIANT`. |
| **PREFERRED** | Readable public description, discoverability topics, root contribution guidance or a clear shared substitute, navigable README/structure; conventionally protected `main`, automatic branch cleanup and CI workflows | Repository owner plus Organization's comparative assurance; a difference is `DRIFT` or an improvement candidate, **not** a binding-policy violation. |
| **INFORMATIONAL** | Exact README size/section count, repo layout, GitHub SPDX detection versus actual license text, named ruleset approvals/status-check rules, legacy protection and metadata readback | Each repository's source, GitHub administrators and actual copyright owners; fields can be `UNKNOWN`, especially at a 403 boundary. No license choice or new CI/review mandate is inferred. |
| **NOT_APPLICABLE** | Cross-repository **mandatory** routing compliance for experimental Capability, other OpenSiro projects outside the declared boundary, and third-party targets | Organization [scope](../README.md) and [ECOSYSTEM](ECOSYSTEM.md); adjacent comparison, when explicitly requested, is non-binding and does not admit those repositories. |

If a current shared operational constraint genuinely requires an S3 decision, use [the S3 admission contract](../contracts/s3/current-control.md) and its legitimate decision holder. A new ultimate-policy or boundary decision belongs to the parent S5 process. Repository-local admin settings and rights remain at their actual owner; neither advisory drift nor a passed linter grants authority.

## Read-only probe

```bash
python3 -m unittest discover -s tests -p 'test_repository_standards.py' -v
python3 scripts/check_repository_standards.py \
  --scope-readme README.md \
  --format summary

# Optional reviewable machine-readable output:
python3 scripts/check_repository_standards.py \
  --scope-readme README.md --format json
```

The scope is read from the canonical `Current in-scope public repositories:` block in `README.md`, using the same parser as [`check_public_routing.py`](../scripts/check_public_routing.py). Explicit `--compare-adjacent` repos **remain out of scope**. Every result has its GitHub REST source; successful default-branch inspection captures the current head SHA, and README/source artifacts are then fetched at that **immutable SHA**. If it is unavailable, source checks are `UNKNOWN` rather than silently performed against moving `main`. GitHub repository settings and rulesets are live point-in-time observations, not Git-commit-pinnable data. The probe never writes to GitHub, changes settings, submits PRs, or invokes LLM/agent sessions.

The advisory `readme_local_links` dimension compares simple relative Markdown links in each root README against a **complete Git tree at the same pinned SHA**, and checks anchors pointing to headings in that README. A missing target is `DRIFT`; an inaccessible or truncated tree produces `UNKNOWN`, never a false missing-link claim. This is a focused navigation smoke check, not a full Markdown parser: external links, reference-style links, cross-file anchors, and live URL availability are not certified. A `PASS` is not proof that the README is understandable to a newcomer.

Classification is intentionally conservative:

- `NON_COMPLIANT` — a missing **already adopted mandatory** START_HERE, Organization route or TODO root-README link **inside the current six-repository boundary**, per [`ROUTING_CONFORMANCE.md`](ROUTING_CONFORMANCE.md).
- `DRIFT` — variation from an explicitly described **advisory observed baseline** (for example `delete_branch_on_merge=true`, root LICENSE, active `Protect main` ruleset), or missing routing links on an **adjacent** repo; it is **not** a new mandatory requirement.
- `PASS` — an observation meets that precise check, not a global standards certification.
- `UNKNOWN` — unreturned/malformed fields, inaccessible endpoint or missing primary evidence; permission failures such as 403 must **not** be interpreted as a setting being disabled.

The CLI exits `1` for mandatory `NON_COMPLIANT`, `2` for mandatory `UNKNOWN` or inability to parse the selected boundary, and `0` otherwise. Advisory `DRIFT`/`UNKNOWN` still appears in output; exit `0` does **not** certify complete compliance. Description, topics, README size/headings, root contributing guidance, license detection, and ruleset gate detail are **evidence for human review**, not automatically mandatory standards. A readable README with headings is not proof of comprehensibility. Different root LICENSE types are not evaluated for suitability by this probe. `protected=true` plus no active ruleset does not mean unprotected: a legacy protection rule can exist, and detail endpoints may need GitHub administration permission. A `ruleset_gate_evidence=PASS` means the named ruleset was read, **not** that approvals or checks are adequate or exhaustive.

The unauthenticated public REST endpoint may omit `delete_branch_on_merge`; return `UNKNOWN` until the same field is supplied by an **authorized** readback. The script accepts the ordinary configured `GITHUB_TOKEN` for read-only requests without printing it. Never request additional permissions merely to turn an advisory field into a PASS.

## Independent review and action boundary

For a *separate* S3* audit, freeze the claim, ordinary owner reporting, original refs and sampling choice before beginning. A sufficiently independent reviewer should inspect primary GitHub state and raw files, exercise discretionary judgment, and record the S3* outcome using the existing [`audit record template`](../templates/s3star-audit-record.md). Do **not** describe the probe itself as an independent S3* reviewer.

Only an admitted, legitimate S3 current-control case may choose a whole-system response. The conditional [G1 S3 human-holder grant](../contracts/s3/parent-assisted-g1.md) does not empower the probe or an agent to independently decide. A local S1 repair must follow the affected repository's own contributor/PR rules. Administration-level changes (automatic deletion, branch rulesets, etc.) require the actual repository owner's authorization and permissions. Recheck effective GitHub state **after** any authorized change; a proposed diff does not prove application.

The initial historical **five-in-scope + adjacent Upstream** comparison remains in [`2026-10-25-repository-standards-baseline.md`](reviews/2026-10-25-repository-standards-baseline.md). The current **six-in-scope** readback is in [`2026-11-06-repository-standards-baseline.md`](reviews/2026-11-06-repository-standards-baseline.md). Neither is a perpetual live standards board or a formal S3*/S3 function witness.
