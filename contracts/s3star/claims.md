# S3* audit slot serialization (prospective v1)

Owner: Organization [#194](https://github.com/opensiro/vsm-oss-organization/issues/194); audit parent [#188](https://github.com/opensiro/vsm-oss-organization/issues/188). This controls **audit-lane coordination**, not normative Profile S3* semantics, an independent reviewer runtime, or Index admission/approval.

## Atomic admission, not an advisory comment

New executions must acquire one **frozen audit slot** before doing semantic judgment or publishing a terminal verdict. One slot is `(wave_id, Index batch issue, kind, immutable board row)`; `kind` is `semantic` or `lifecycle`. A whole batch is **not** one atomic claim: a worker must acquire every distinct row it intends to handle and must stop on partial conflicts rather than claim a full batch.

`scripts/s3star_claims.py claim` builds a Git commit containing a bounded JSON identity record then calls GitHub's **atomic `POST /git/refs`** for a *deterministic tag*:

`refs/tags/s3star-locks/v1/<wave>/<batch>/<kind>-<row>/e<epoch>-claim`

A duplicate ref yields `LOCKED`; a second writer **cannot win** by choosing another run ID, model, context or issue comment. The script never updates/deletes the tag. A separate `e<epoch>-terminal` tag records exactly one local result. It verifies the winning owner/claim ID, manifest, pinned upstream SHA and Index SHA before accepting finalization. Retrying does not replace the earlier result.

This is an **API atomic-create guarantee, not proof of tamper-resistant refs**: an administrator might move/delete tags unless server rules prevent it. Actor names in records are attribution assertions, not cryptographic proof of independently instantiated agents. The first-party S3* discretionary auditor still has to read complementary evidence and identify its actual judgment owner.

## Operator procedure

Use authorized `GH_TOKEN` / `GITHUB_TOKEN` with Organization Git contents write access, Python 3.12+, and a real published frozen manifest issue comment. Never put credentials in issue comments or files.

```bash
python scripts/s3star_claims.py claim \
  --wave S3STAR-INDEX-BATCH-20261011-W003 --batch 1500 \
  --kind semantic --row 1 --epoch 0 \
  --source-sha <actual-40-character-frozen-source-SHA> \
  --index-sha <actual-40-character-Index-main-SHA> \
  --manifest https://github.com/opensiro/vsm-oss-organization/issues/188#issuecomment-6107447382 \
  --claim-id <unique-context-identifier> --actor <actual-reviewer-context>
```

This is an **example**, not authorization to create a W003 wave or claim #1302. `RECORDED` exit 0 is the only positive slot-claim outcome: independently fetch the tag and JSON event before review. `LOCKED` exit 3 means stop or yield, never duplicate. `BLOCKED` exit 2 means missing evidence/authentication/API or invalid scope; fail closed.

Perform actual complementary first-party source review under the frozen Organization S3* contract. Publish the separate audit receipt with primary-source links, exact claim and judgment owner; then call the **same exact slot and owner inputs** using `terminal --outcome PASS|FINDING|INSUFFICIENT --evidence-url <owning-public-issue-comment>`. Additional administrative terminal states are `YIELDED` and `BLOCKED`; neither counts as an audit result. A posted `FINDING` does not close the downstream Index correction.

`verify_slots(api, slots)` fetches accepted claim and terminal tags and validates owner/ref equality **before** `reduce_receipts` counts each unique slot once. The reducer refuses conflicting distinct outcomes/owners. Plain comments without an admitted tag are **not** tagged as verified by this API.

## No stale-lock theft; exact handoff

A silent claimant stays claimed. Prospective epoch 1+ requires an **explicit new Organization-main handoff document**, merged by an authorized PR:

`records/s3star/handoffs/s3star-locks/v1/<wave>/<batch>/<kind>-<row>.json`

```json
{
  "schema": "s3star-handoff-v1",
  "active_epoch": 1,
  "previous_claim_id": "previous-context-id",
  "next_claim_id": "new-context-id",
  "next_actor": "new-reviewer-context",
  "authorization_pr": "https://github.com/opensiro/vsm-oss-organization/pull/999"
}
```

Require either the preceding actual `YIELDED` terminal or, for a maintainer-authorized exceptional takeover, an additional `maintainer_override_issue` linking the separately governed decision. A reviewer must check that the authorization PR was actually merged; the script checks the corresponding handoff JSON **on main** and predecessor evidence but does not itself confer GitHub approval or independently establish that an arbitrary PR URL was approved. It admits only the exact named successor; older epochs become stale. Historical tags/events are never rewritten.

## Legacy wave boundaries and tests

W001 has already been frozen, with a separate **advisory** #1302 claim [here](https://github.com/opensiro/vsm-oss-organization/issues/188#issuecomment-6107958223). These new tags do **not retroactively establish an atomic claim**, release that reservation, or authorize a duplicate review. W001's #1314/#1315 duplicate comments remain historical; they count as one audited semantic row each, not two independent observations. W002 [#190](https://github.com/opensiro/vsm-oss-organization/issues/190) is a separate frozen wave.

`python -m unittest tests.test_s3star_claims -v` checks a simulated server-side competing `POST /git/refs` race, same-slot retry, nonowner/stale-ref terminal, missing claim, corrupt event, disjoint waves, handoff with and without override, YIELDED excluded from coverage, and legacy duplicate/conflicting receipts. The normal Organization CI test-discovery step also runs these tests. No actual GitHub claim tags are created by tests.

**Boundary:** no Index vectors, assessment PRs, catalog, signatures, branch settings, Profile/Skills semantics or W001 frozen refs change through this control.