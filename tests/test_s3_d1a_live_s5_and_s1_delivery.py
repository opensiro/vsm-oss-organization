"""Hypothetical API fixtures only; no owner approval or S1 writes."""
import base64
import copy
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
MODE=ROOT/"modes"/"s3-autonomous"
def mod(name):
    spec=importlib.util.spec_from_file_location(name,MODE/(name+".py"))
    obj=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj
auth=mod("github_s5_authority")
send=mod("github_s1_delivery")
SAVED=json.loads((ROOT/"contracts/s3/autonomous-d1a.json").read_text())
BASE="a"*40
HEAD="b"*40
ACTOR="s3-autonomous-test-runtime-001"
REF="https://github.com/opensiro/vsm-oss-organization/issues/5#issuecomment-987"
TARGET="https://github.com/opensiro/awesome-vsm-harness/issues/7"
START="2026-10-15T12:00:00Z"
END="2026-10-18T12:00:00Z"
AT=datetime(2026,10,16,10,tzinfo=timezone.utc)
def active():
    d=copy.deepcopy(SAVED)
    d.update(status="ACTIVE",recipient_execution_identity=ACTOR,
        owner_attestation_url=REF,grant_publication_commit=BASE,
        effective_from_utc=START,expires_at_utc=END)
    return d
def fixtures():
    d=active()
    p={**d,"grant_publication_commit":None}
    obj={"decision":"AUTHORIZE_D1A","recipient_execution_identity":ACTOR,
      "allowed_classes":d["allowed_classes"],
      "allowed_standing_commitments":d["allowed_standing_commitments"],
      "effective_from_utc":START,"expires_at_utc":END,
      "grant_publication_commit":BASE}
    def blob(x):
        return {"encoding":"base64","content":base64.b64encode(json.dumps(x).encode()).decode()}
    pre="/repos/opensiro/vsm-oss-organization"
    return {
        pre+"/branches/main":{"commit":{"sha":HEAD}},
        pre+"/compare/"+BASE+"..."+HEAD:{"status":"ahead"},
        pre+"/contents/contracts/s3/autonomous-d1a.json?ref="+HEAD:blob(d),
        pre+"/contents/contracts/s3/autonomous-d1a.json?ref="+BASE:blob(p),
        pre+"/issues/comments/987":{"html_url":REF,"created_at":"2026-10-15T10:00:00Z",
            "user":{"login":"xLagerFeuer"},"body":auth.ATTEST+json.dumps(obj)},
        pre+"/issues/5":{"number":5},
        pre+"/issues/5/comments?per_page=100&page=1":[]
    }
def fetch(data):
    def get(path):
        if path not in data:raise auth.S5AuthorizationError("missing remote primary source")
        return data[path]
    return get
def action():
    return {"owner_class":"agent","actor_execution_id":ACTOR,
        "grant_owner_receipt":REF,"selected_class":"REQUIRE_REPAIR",
        "instruction":"Return a narrowly scoped current shared obligation correction",
        "evidence_refs":[TARGET],"return_target":TARGET,
        "commitment_id":"canonical-publication-continuity",
        "closed":False,"S1_acknowledgement_ref":None,"S1_effect_refs":[]}
def authority(a):
    return {"authorized":True,"revocation_checked":True,
            "owner_comment_url":REF,"attested_actor":ACTOR}
def admitted(a):
    return {"admitted":True,"return_target":TARGET,
            "nonlocal_right_verified":True,"s1_s2_s5_falsifiers_checked":True}

class S5Checks(unittest.TestCase):
    def verify(self,data=None,**kw):
        return auth.verify_active_grant(active(),ACTOR,fetch(data or fixtures()),now=AT,**kw)
    def test_real_shipped_source_inactive(self):
        with self.assertRaisesRegex(auth.S5AuthorizationError,"not active"):
            auth.verify_active_grant(SAVED,ACTOR,lambda x:self.fail("called"))
    def test_login_not_parent_authority(self):
        with self.assertRaisesRegex(auth.S5AuthorizationError,"not independently"):
            self.verify()
    def test_structural_source_check_requires_parent_assurance(self):
        self.assertTrue(self.verify(parent_authorship=lambda _:True)["authorized"])
    def test_revocation_blocks_even_with_active_grant(self):
        d=fixtures()
        d["/repos/opensiro/vsm-oss-organization/issues/5/comments?per_page=100&page=1"]=[
          {"user":{"login":"xLagerFeuer"},
           "body":auth.REVOKE+json.dumps({"owner_attestation_url":REF})}]
        with self.assertRaisesRegex(auth.S5AuthorizationError,"revoked"):
            self.verify(d,parent_authorship=lambda _:True)
    def test_wrong_owner_main_and_incomplete_history_fail(self):
        for kind in ("owner","diverged","truncated"):
            d=fixtures()
            pre="/repos/opensiro/vsm-oss-organization"
            if kind=="owner": d[pre+"/issues/comments/987"]["user"]["login"]="s3-agent"
            elif kind=="diverged": d[pre+"/compare/"+BASE+"..."+HEAD]["status"]="diverged"
            else:d[pre+"/issues/5/comments?per_page=100&page=1"]=[
                {"user":{"login":"other"},"body":"ordinary"} for _ in range(100)]
            with self.subTest(kind=kind),self.assertRaises(auth.S5AuthorizationError):
                self.verify(d,parent_authorship=lambda _:True)

class S1Writes(unittest.TestCase):
    def execute(self, a=None, authcheck=authority, admcheck=admitted, login="d1a-bot", state="open", comments=None):
        calls=[]
        prefix="/repos/opensiro/awesome-vsm-harness"
        def api(method,path,body):
            calls.append((method,path,body))
            if (method,path)==("GET","/user"):return {"login":login}
            if (method,path)==("GET",prefix+"/collaborators/"+login+"/permission"):
                return {"permission":"write"}
            if (method,path)==("GET",prefix+"/issues/7"):
                return {"state":state,"html_url":TARGET}
            if (method,path)==("GET",prefix+"/issues/7/comments?per_page=100&page=1"):
                return comments or []
            if (method,path)==("POST",prefix+"/issues/7/comments"):
                return {"html_url":TARGET+"#issuecomment-22","user":{"login":login}}
            raise send.S1DeliveryError("unexpected API operation")
        try:return send.deliver(a or action(),api=api,verify_authority=authcheck,
                 verify_admission=admcheck,transport_login=login),calls
        except Exception as e:e.calls=calls;raise
    def test_no_verified_grant_no_api_request(self):
        with self.assertRaises(send.S1DeliveryError) as e:
            self.execute(authcheck=lambda x:{"authorized":False})
        self.assertEqual([],e.exception.calls)
    def test_no_admitted_s3_no_api_request(self):
        with self.assertRaises(send.S1DeliveryError) as e:
            self.execute(admcheck=lambda x:{"admitted":False})
        self.assertEqual([],e.exception.calls)
    def test_post_once_and_idempotent_retry(self):
        result,calls=self.execute()
        self.assertEqual("POSTED_S1_EFFECT_UNVERIFIED",result["delivery_status"])
        self.assertEqual(1,sum(m=="POST" for m,*_ in calls))
        body=next(x[2]["body"] for x in calls if x[0]=="POST")
        duplicate={"body":body,"html_url":result["transport_url"],
                   "user":{"login":"d1a-bot"}}
        again,calls2=self.execute(comments=[duplicate])
        self.assertEqual("ALREADY_SENT",again["delivery_status"])
        self.assertEqual(0,sum(m=="POST" for m,*_ in calls2))
    def test_nonparent_account_and_open_s1_required(self):
        for kwargs in ({"login":"xLagerFeuer"},{"state":"closed"}):
            with self.assertRaises(send.S1DeliveryError):
                self.execute(**kwargs)
    def test_inadmissible_class_or_preclosed_effect_blocked(self):
        for x in ({"selected_class":"STOP"},{"closed":True},
                  {"S1_effect_refs":["https://github.com/opensiro/awesome-vsm-harness/pull/12"]}):
            with self.assertRaises(send.S1DeliveryError):self.execute(a={**action(),**x})

if __name__=="__main__":unittest.main()
