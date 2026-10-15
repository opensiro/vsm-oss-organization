"""Read-only S3-source-view regression tests; not a VSM functional assessment."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

PATH = Path(__file__).resolve().parents[1] / "scripts" / "collect_s3_current_view.py"
SPEC = importlib.util.spec_from_file_location("collect_s3_current_view", PATH)
assert SPEC and SPEC.loader
s = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = s
SPEC.loader.exec_module(s)
SHA = "a" * 40


def fake_api(*, issue_count=1, missing=False):
    def get(path):
        for repo in s.REPOSITORIES:
            if path == f"/repos/{repo}":
                return {"default_branch": "main"}
            if path == f"/repos/{repo}/branches/main":
                return {"commit": {"sha": SHA}}
            if path.startswith(f"/repos/{repo}/issues?"):
                if missing:
                    return None
                return ([{
                    "number": i + 1, "title": f"Issue {i}",
                    "html_url": f"https://github.com/{repo}/issues/{i+1}",
                    "updated_at": "2026-10-15T00:00:00Z",
                } for i in range(issue_count)]
                    + [{"number": 20, "pull_request": {"url": "x"}, "title": "PR",
                        "html_url": f"https://github.com/{repo}/pull/20",
                        "updated_at": "2026-10-15T00:00:00Z"}])
            if path.startswith(f"/repos/{repo}/pulls?"):
                return [{
                    "number": 20, "title": "PR", "head": {"sha": SHA},
                    "html_url": f"https://github.com/{repo}/pull/20",
                    "draft": True,
                }]
        raise AssertionError("unlisted endpoint: " + path)
    return get


class TestS3ReadOnlyView(unittest.TestCase):
    def test_domains_and_pinned_main_refs_without_s3_assertions(self):
        obj = s.collect(fake_api(), observed_at="2026-10-15T00:00:00+00:00")
        self.assertEqual(s.BOUNDARY, obj["classification"])
        self.assertEqual("NOT_ASSESSED", obj["s3_admission"])
        self.assertEqual(len(s.REPOSITORIES), len(obj["domains"]))
        for domain in obj["domains"]:
            self.assertEqual(SHA, domain["main_sha"])
            self.assertTrue(domain["source_main"].endswith(SHA))
            self.assertEqual(1, len(domain["open_issues"]))
            self.assertEqual(1, len(domain["open_pulls"]))
            self.assertEqual("UNKNOWN", domain["open_issues"][0]["work_admitted"])
            self.assertEqual("UNKNOWN", domain["open_pulls"][0]["work_admitted"])
            self.assertTrue(domain["open_pulls"][0]["draft"])

    def test_fail_closed_if_open_issue_inventory_unavailable(self):
        with self.assertRaisesRegex(s.CurrentViewError, "unavailable"):
            s.collect(fake_api(missing=True))

    def test_fail_closed_on_unpaginated_truncation(self):
        # One extra PR-shaped object does not relax the >=100 issue boundary.
        with self.assertRaisesRegex(s.CurrentViewError, "paginated"):
            s.collect(fake_api(issue_count=100))

    def test_unexpected_api_paths_rejected(self):
        with self.assertRaisesRegex(s.CurrentViewError, "refusing"):
            s.github_get("/users/test")


if __name__ == "__main__":
    unittest.main()
