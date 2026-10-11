"""Negative fixtures for GitHub first-winner S3* claim control (#194)."""
from __future__ import annotations

import base64
import importlib.util
import json
import unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "scripts" / "s3star_claims.py"
SPEC = importlib.util.spec_from_file_location("s3star_claims", PATH)
assert SPEC and SPEC.loader
s = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(s)

P = {
    "wave": "S3STAR-INDEX-BATCH-20261011-W001", "batch": 1302,
    "kind": "semantic", "row": 1, "epoch": 0, "source_sha": "a" * 40,
    "index_sha": "b" * 40, "actor": "audit-context-a", "claim_id": "claim-context-a",
    "manifest": "https://github.com/opensiro/vsm-oss-organization/issues/188#issuecomment-6107447382",
}
ISSUE = "https://github.com/opensiro/vsm-oss-organization/issues/188"


class InMemoryGitHub:
    """No network, but POST /git/refs has actual atomic-create / 422 semantics."""

    def __init__(self):
        self.refs = {"refs/heads/main": "f" * 40}
        self.commits = {"f" * 40: {"tree": {"sha": "tree-main"}}}
        self.files = {}
        self.counter = 0

    def request(self, method, path, data=None):
        self.counter += 1
        if method == "GET" and path.startswith("/git/ref/"):
            key = "refs/" + path[len("/git/ref/"):]
            if key not in self.refs:
                raise s.GitHubError(404, "not found")
            return {"object": {"sha": self.refs[key]}}
        if method == "GET" and path.startswith("/git/commits/"):
            return self.commits[path.split("/")[-1]]
        if method == "GET" and path.startswith("/contents/"):
            file, sha = path[len("/contents/"):].split("?ref=")
            if (sha, file) not in self.files:
                raise s.GitHubError(404, "missing")
            return {"encoding": "base64", "content": base64.b64encode(
                json.dumps(self.files[(sha, file)]).encode()).decode()}
        if method == "POST" and path == "/git/trees":
            tree_sha = f"t{self.counter:039d}"
            self.files[(tree_sha, data["tree"][0]["path"])] = json.loads(data["tree"][0]["content"])
            return {"sha": tree_sha}
        if method == "POST" and path == "/git/commits":
            sha = f"c{self.counter:039d}"
            self.commits[sha] = {"tree": {"sha": data["tree"]}}
            for (tree, filename), value in list(self.files.items()):
                if tree == data["tree"]:
                    self.files[(sha, filename)] = value
            return {"sha": sha}
        if method == "POST" and path == "/git/refs":
            if data["ref"] in self.refs:
                raise s.GitHubError(422, "already exists")
            self.refs[data["ref"]] = data["sha"]
            return {"ref": data["ref"]}
        raise AssertionError((method, path))


class S3StarClaimTests(unittest.TestCase):
    def setUp(self):
        self.api = InMemoryGitHub()
        self.payload = dict(P)

    def test_first_claimant_wins_and_idempotent_retry_stays_locked(self):
        self.assertEqual(s.claim(self.api, self.payload)["status"], "RECORDED")
        other = dict(P, actor="audit-context-b", claim_id="claim-context-b")
        self.assertEqual(s.claim(self.api, other)["status"], "LOCKED")
        self.assertEqual(s.claim(self.api, self.payload)["status"], "LOCKED")
        self.assertEqual(s.event(self.api, P, "claim")["actor"], P["actor"])

    def test_simultaneous_create_race_uses_server_side_422(self):
        other = dict(P, actor="audit-context-b", claim_id="claim-context-b")
        self.assertEqual(s.create_event(self.api, P, "claim")["status"], "RECORDED")
        self.assertEqual(s.create_event(self.api, other, "claim")["status"], "LOCKED")

    def test_nonowner_or_stale_source_cannot_finalize(self):
        s.claim(self.api, P)
        for bad in (dict(P, claim_id="claim-context-b", actor="audit-context-b"),
                    dict(P, source_sha="c" * 40)):
            with self.assertRaisesRegex(s.AuditLockError, "nonowner|changed"):
                s.finalize(self.api, bad, "PASS", ISSUE)
        self.assertEqual("RECORDED", s.finalize(self.api, P, "PASS", ISSUE)["status"])
        self.assertEqual("LOCKED", s.finalize(self.api, P, "FINDING", ISSUE)["status"])

    def test_claimed_source_memo_not_a_terminal_outcome(self):
        s.claim(self.api, P)
        self.assertIsNone(s.event(self.api, P, "terminal"))
        self.assertEqual(s.verify_slots(self.api, [dict(P)])["unique"], 0)

    def test_evidence_url_and_invalid_actor_or_source_fail_closed(self):
        for key, value in (("actor", "AI"), ("source_sha", "main"), ("manifest", "https://example.org")):
            with self.assertRaises(s.AuditLockError):
                s.claim(self.api, dict(P, **{key: value}))
        s.claim(self.api, P)
        with self.assertRaises(s.AuditLockError):
            s.finalize(self.api, P, "PASS", "https://example.org/no-evidence")

    def test_corrupt_published_event_fails_closed(self):
        s.claim(self.api, P)
        sha = self.api.refs[s.reference(P, "claim")]
        self.api.files[(sha, s.record_path(P, "claim"))]["slot"]["row"] = 10
        with self.assertRaisesRegex(s.AuditLockError, "invalid or unrelated"):
            s.finalize(self.api, P, "PASS", ISSUE)

    def test_w001_1314_and_1315_duplicate_comments_do_not_inflate(self):
        receipts = []
        for batch in (1314, 1315):
            for row in (1, 5, 10):
                x = dict(wave=P["wave"], batch=batch, kind="semantic", row=row,
                         claim_id=f"legacy-{batch}-{row}", outcome="PASS", verified_owner=True)
                receipts.extend((x, x.copy()))
        r = s.reduce_receipts(receipts)
        self.assertEqual((r["unique"], r["semantic"], r["supplements"]), (6, 6, 6))
        receipts[-1] = dict(receipts[-1], outcome="FINDING")
        with self.assertRaisesRegex(s.AuditLockError, "conflicting"):
            s.reduce_receipts(receipts)

    def test_disjoint_wave_and_lifecycle_slot(self):
        a = s.claim(self.api, P)
        wave = dict(P, wave="S3STAR-INDEX-BATCH-20261011-W002")
        lifecycle = dict(P, kind="lifecycle")
        self.assertNotEqual(a["ref"], s.claim(self.api, wave)["ref"])
        self.assertNotEqual(a["ref"], s.claim(self.api, lifecycle)["ref"])

    def test_yield_does_not_count_as_completed_audit(self):
        s.claim(self.api, P)
        s.finalize(self.api, P, "YIELDED", ISSUE)
        self.assertEqual(s.verify_slots(self.api, [dict(P)])["unique"], 0)

    def test_handoff_requires_yield_or_maintainer_override(self):
        s.claim(self.api, P)
        new = dict(P, epoch=1, actor="audit-context-c", claim_id="claim-context-c")
        key = "records/s3star/handoffs/" + s.base(P) + ".json"
        auth = dict(schema="s3star-handoff-v1", active_epoch=1,
                    previous_claim_id=P["claim_id"],
                    next_claim_id=new["claim_id"], next_actor=new["actor"],
                    authorization_pr="https://github.com/opensiro/vsm-oss-organization/pull/999")
        self.api.files[("f" * 40, key)] = auth
        with self.assertRaisesRegex(s.AuditLockError, "YIELDED"):
            s.claim(self.api, new)
        auth["maintainer_override_issue"] = "https://github.com/opensiro/vsm-oss-organization/issues/194"
        self.assertEqual(s.claim(self.api, new)["status"], "RECORDED")
        with self.assertRaisesRegex(s.AuditLockError, "superseded"):
            s.finalize(self.api, P, "PASS", ISSUE)

    def test_handoff_is_exactly_bound_to_next_claimant(self):
        s.claim(self.api, P)
        auth = dict(schema="s3star-handoff-v1", active_epoch=1,
                    previous_claim_id=P["claim_id"], next_claim_id="claim-context-c",
                    next_actor="audit-context-c",
                    authorization_pr="https://github.com/opensiro/vsm-oss-organization/pull/999",
                    maintainer_override_issue="https://github.com/opensiro/vsm-oss-organization/issues/194")
        self.api.files[("f" * 40, "records/s3star/handoffs/" + s.base(P) + ".json")] = auth
        with self.assertRaisesRegex(s.AuditLockError, "unassigned"):
            s.claim(self.api, dict(P, epoch=1, claim_id="claim-context-d", actor="audit-context-d"))

    def test_verified_coverage_reads_tags_not_author_issued_numbers(self):
        scope = {k: P[k] for k in ("wave", "batch", "kind", "row")}
        s.claim(self.api, P)
        self.assertEqual(s.verify_slots(self.api, [scope])["unique"], 0)
        s.finalize(self.api, P, "PASS", ISSUE)
        r = s.verify_slots(self.api, [scope, scope])
        self.assertEqual((r["unique"], r["supplements"]), (1, 1))
        self.assertEqual(s.reduce_receipts([dict(scope, outcome="PASS")])["unique"], 0)


if __name__ == "__main__":
    unittest.main()
