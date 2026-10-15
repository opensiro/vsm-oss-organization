"""Token-backed HTTP adapter source-safe route allowlist; all API responses simulated."""
from __future__ import annotations
import importlib.util
from pathlib import Path
import unittest

path=Path(__file__).resolve().parents[1]/"modes"/"s3-autonomous"/"github_rest.py"
spec=importlib.util.spec_from_file_location("d1a_github_rest",path)
api=importlib.util.module_from_spec(spec)
spec.loader.exec_module(api)

class AllowedRoutes(unittest.TestCase):
    def make(self):
        calls=[]
        def handler(method,path,body):
            calls.append((method,path,body))
            return {"test":"only"}
        return api.GitHubREST(transport=handler),calls
    def test_expected_owner_and_s1_routes(self):
        x,calls=self.make()
        self.assertEqual({"test":"only"},x.get("/repos/opensiro/vsm-oss-organization/branches/main"))
        self.assertEqual({"test":"only"},x("POST","/repos/opensiro/awesome-vsm-harness/issues/7/comments",{"body":"one bounded S3 return"}))
        self.assertEqual(["GET","POST"],[c[0] for c in calls])
    def test_no_index_grades_arbitrary_owners_or_repo_writes(self):
        x,calls=self.make()
        for args in (
           ("POST","/repos/opensiro/vsm-harness-index/issues/7",{"body":"x"}),
           ("POST","/repos/opensiro/vsm-oss-organization/issues/5/comments",{"body":"x"}),
           ("POST","/repos/opensiro/awesome-vsm-harness/pulls/7/merge",{"body":"x"}),
           ("GET","/repos/opensiro/research-icml27-proofstate/issues/4",None),
           ("GET","/repos/opensiro/vsm-harness-index/issues/7?state=all",None),
           ("POST","/repos/opensiro/awesome-vsm-harness/issues/7/comments",{"body":"a"*7000})
        ):
            with self.subTest(args=args),self.assertRaises(api.GitHubTransportError):
                x(*args)
        self.assertEqual([],calls)

if __name__=="__main__":unittest.main()
