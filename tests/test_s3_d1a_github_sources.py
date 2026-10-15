"""No live GitHub authorization or S3 action: source-receipt fixture contracts."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "modes" / "s3-autonomous"

def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name + ".py"))
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

gh = load("github_s1_receipts")
bridge = load("s3star_intake")
TARGET = "https://github.com/opensiro/awesome-vsm-harness/issues/7"
OTHER = "https://github.com/opensiro/vsm-harness-index/issues/1567"
ADMIT = TARGET + "#issuecomment-17"
DELIVER = TARGET + "#issuecomment-18"
ACK = TARGET + "#issuecomment-19"
PR = "https://github.com/opensiro/awesome-vsm-harness/pull/12"
COMMIT = "a" * 40

def admission():
    return {
        "return_target": TARGET,
        "commitment_id": "canonical-publication-continuity",
        "s1_admission_comment_url": ADMIT,
        "nonlocal_evidence_refs": [TARGET, OTHER]
    }

def action():
    return {
        "status": "S1_RETURN_SENT_EFFECT_UNVERIFIED",
        "closed": False,
        "return_target": TARGET,
        "transport_url": DELIVER
    }

def fixture():
    base = "/repos/opensiro/"
    obj = {}
    obj[base + "awesome-vsm-harness/issues/7"] = {
        "html_url": TARGET, "state": "open", "title": "curation obligation"}
    obj[base + "vsm-harness-index/issues/1567"] = {
        "html_url": OTHER, "state": "open", "title": "canonical status"}
    for n,user,time,body in (
        (17,"s1owner","2026-10-15T11:00:00Z",
         gh.HEADER + json.dumps({
             "verdict": "ADMIT", "target": TARGET,
             "commitment_id": "canonical-publication-continuity"
         })),
        (18,"s3-bot","2026-10-15T12:00:00Z","S3 instruction"),
        (19,"s1owner","2026-10-15T13:00:00Z","Ack S3")):
        obj[base + "awesome-vsm-harness/issues/comments/" + str(n)] = {
            "html_url": TARGET + "#issuecomment-" + str(n),
            "created_at": time, "body": body, "user": {"login": user}}
    for user in ("s1owner","repairer"):
        obj[base + "awesome-vsm-harness/collaborators/" + user + "/permission"] = {
            "permission":"write"}
    obj[base + "awesome-vsm-harness/pulls/12"] = {
        "html_url": PR, "merged_at": "2026-10-15T14:00:00Z",
        "merge_commit_sha": COMMIT, "changed_files": 1,
        "body": "Fix " + TARGET + " after " + DELIVER,
        "user": {"login":"repairer"}
    }
    return obj

class GitHubS1Facts(unittest.TestCase):
    def make(self, records=None):
        data = fixture() if records is None else records
        def read(path):
            if path not in data:
                raise gh.GitHubEvidenceError("API missing: fail closed")
            return data[path]
        return gh.GitHubS1Reader(fetch=read)

    def test_current_s1_admission_is_factual_only(self):
        got = self.make().read_s1_admission(admission())
        self.assertTrue(got["admitted"])
        self.assertFalse(got["nonlocal_right_verified"])
        self.assertFalse(got["s1_s2_s5_falsifiers_checked"])

    def test_untrusted_comment_author_and_missing_admission_are_denied(self):
        records = fixture()
        records["/repos/opensiro/awesome-vsm-harness/collaborators/s1owner/permission"] = {
            "permission":"read"}
        with self.assertRaisesRegex(gh.GitHubEvidenceError,"write/maintain"):
            self.make(records).read_s1_admission(admission())
        with self.assertRaises(gh.GitHubEvidenceError):
            self.make().read_s1_admission({**admission(),
                  "s1_admission_comment_url": OTHER + "#issuecomment-19"})

    def test_distinct_s1_sources_required(self):
        with self.assertRaisesRegex(gh.GitHubEvidenceError,"two real S1"):
            self.make().read_s1_admission({
                **admission(), "nonlocal_evidence_refs":[TARGET,TARGET]})

    def test_independently_verified_s1_receipt_and_effect(self):
        result = self.make().verify_s1_return(action(),
                         acknowledgement_ref=ACK,effect_pr_ref=PR)
        self.assertTrue(result["s1_owner_verified"])
        self.assertTrue(result["effect_verified"])
        self.assertEqual([PR], result["effect_refs"])

    def test_same_actor_fake_ack_fails(self):
        records=fixture()
        records["/repos/opensiro/awesome-vsm-harness/issues/comments/19"]["user"]["login"]="s3-bot"
        records["/repos/opensiro/awesome-vsm-harness/collaborators/s3-bot/permission"]={"permission":"write"}
        with self.assertRaisesRegex(gh.GitHubEvidenceError,"self-attest"):
            self.make(records).verify_s1_return(action(),acknowledgement_ref=ACK,effect_pr_ref=PR)

    def test_unmerged_unlinked_and_stale_effect_fail(self):
        for key,value in (
          ("merged_at",None),
          ("body","This PR has no link to the S3 returned instruction"),
          ("merged_at","2026-10-15T12:20:00Z"),
          ("changed_files",0),
        ):
            records=fixture()
            records["/repos/opensiro/awesome-vsm-harness/pulls/12"][key]=value
            with self.assertRaises(gh.GitHubEvidenceError):
                self.make(records).verify_s1_return(action(),acknowledgement_ref=ACK,effect_pr_ref=PR)

    def test_no_s1_api_proof_from_url_shape(self):
        with self.assertRaises(gh.GitHubEvidenceError):
            self.make({}).read_s1_admission(admission())

class S3StarIntake(unittest.TestCase):
    def finding(self):
        return {
            "outcome":"FINDING",
            "return_target":TARGET,
            "commitment_id":"canonical-publication-continuity",
            "audit_receipt_ref":"https://github.com/opensiro/vsm-oss-organization/issues/188",
            "complementary_evidence_refs":[OTHER],
            "material_whole_system_relevance":True
        }

    def test_source_verified_finding_is_only_unadmitted_candidate(self):
        data=bridge.as_candidate(self.finding(),audit_source_verified=True)
        self.assertEqual("UNADMITTED_S3_CANDIDATE_FROM_S3STAR",data["status"])
        self.assertIsNone(data["selected_class"])
        self.assertEqual([], data["S1_effect_refs"])

    def test_audit_label_alone_never_grants_s3_authority(self):
        with self.assertRaises(bridge.AuditBridgeError):
            bridge.as_candidate(self.finding(),audit_source_verified=False)
        for change in ({"outcome":"PASS"},{"material_whole_system_relevance":False},
                       {"commitment_id":"unrelated"}):
            with self.assertRaises(bridge.AuditBridgeError):
                bridge.as_candidate({**self.finding(),**change},audit_source_verified=True)

if __name__=="__main__":
    unittest.main()
