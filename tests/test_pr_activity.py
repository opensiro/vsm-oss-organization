"""Mocked GitHub REST PR lifecycle and attribution boundary tests (offline)."""
import importlib.util
import json
import unittest
from datetime import datetime, timezone

from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "collect_pr_activity.py"
SPEC = importlib.util.spec_from_file_location("pr_activity", SCRIPT)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)
NOW = datetime(2026, 10, 12, 0, 0, tzinfo=timezone.utc)
REPO = "opensiro/vsm-harness-index"


def pr(number, created="2026-10-11T10:00:00Z", updated="2026-10-11T23:00:00Z",
       merged=None, closed=None, state="open", login="author"):
    return dict(id=number+1000, number=number, state=state,
                created_at=created, updated_at=updated, merged_at=merged, closed_at=closed,
                user={"login": login, "type": "User"})


def review(time="2026-10-11T09:00:00Z", login="reviewer", kind="User", state="APPROVED"):
    return dict(state=state, submitted_at=time, user={"login": login, "type": kind})


class PRActivityTests(unittest.TestCase):
    def test_core_event_windows_and_outcomes(self):
        old_merge = pr(1, created="2026-09-01T00:00:00Z",
                       merged="2026-10-11T01:00:00Z", closed="2026-10-11T01:00:00Z", state="closed")
        just_opened = pr(2, created="2026-10-11T12:00:00Z")
        closed = pr(3, created="2026-10-03T00:00:00Z", closed="2026-10-11T12:00:00Z", state="closed")
        result = mod.compute_repository(REPO, [old_merge, just_opened, closed], [just_opened],
                                        {1: [], 2: [review()], 3: []}, NOW)
        day = result["windows"]["24h"]
        self.assertEqual((day["opened"], day["merged"], day["closed_without_merge"]), (1, 1, 1))
        self.assertEqual(day["time_to_merge"]["sample_size"], 1)
        self.assertEqual(result["open_prs"], 1)
        self.assertEqual(day["first_review_latency"]["sample_size"], 1)
        self.assertEqual(result["status"], "complete")

    def test_exact_cutoff_excluded_and_no_sample_not_zero(self):
        d = pr(4, created="2026-10-11T00:00:00Z", updated="2026-10-11T01:00:00Z")
        outcome = mod.compute_repository(REPO, [d], [d], {4: []}, NOW)
        self.assertEqual(outcome["windows"]["24h"]["opened"], 0)
        self.assertIsNone(outcome["windows"]["24h"]["time_to_merge"]["median_hours"])
        self.assertEqual(outcome["windows"]["24h"]["time_to_merge"]["sample_size"], 0)

    def test_first_review_filters_self_bot_pending_and_issue_comment_nonexistent(self):
        p = pr(5)
        attempts = [review("2026-10-10T08:00:00Z", "author"),
                    review("2026-10-10T08:30:00Z", "ci[bot]", "Bot"),
                    review("2026-10-10T09:00:00Z", "human", "User", "PENDING"),
                    review("2026-10-11T09:00:00Z", "human", "User", "COMMENTED")]
        first, complete = mod.first_qualifying_review(p, attempts)
        self.assertTrue(complete)
        self.assertEqual(first.isoformat(), "2026-10-11T09:00:00+00:00")
        self.assertEqual(mod.first_qualifying_review(p, attempts[:3]), (None, True))

    def test_unknown_reviewer_is_partial_and_no_fake_median(self):
        p = pr(5)
        outcome = mod.compute_repository(REPO, [p], [p], {5: [review(login="unknown", kind="Ghost")]}, NOW)
        self.assertEqual(outcome["status"], "partial")
        self.assertEqual(outcome["windows"]["24h"]["first_review_latency"]["status"], "partial")
        self.assertIsNone(outcome["windows"]["24h"]["first_review_latency"]["sample_size"])
        self.assertEqual(outcome["windows"]["24h"]["opened"], 1)

    def test_missing_review_history_preserves_pr_counts_not_partial_median(self):
        p = pr(6)
        result = mod.compute_repository(REPO, [p], [p], {}, NOW)
        self.assertEqual(result["windows"]["24h"]["opened"], 1)
        self.assertEqual(result["windows"]["24h"]["first_review_latency"]["status"], "partial")

    def test_double_count_and_bad_stock_are_rejected(self):
        p = pr(7)
        with self.assertRaisesRegex(mod.PRActivityError, "duplicate PR"):
            mod.compute_repository(REPO, [p,p], [p], {7: []}, NOW)
        with self.assertRaisesRegex(mod.PRActivityError, "non-open"):
            mod.compute_repository(REPO, [p], [pr(7, state="closed")], {7: []}, NOW)

    def test_lifecycle_after_reopen_not_classified_as_closed(self):
        p = pr(8, state="open", closed="2026-10-09T12:00:00Z")
        result = mod.compute_repository(REPO, [p], [p], {8: []}, NOW)
        self.assertEqual(result["windows"]["7d"]["closed_without_merge"], 0)

    def test_p90_and_median(self):
        self.assertEqual(mod.quantile([1,2,3,4,5,6,7,8,9,10]),
                         {"median_hours": 5.5, "p90_hours": 9, "sample_size": 10})

    def test_pagination_repo_id_canonical_links_and_cutoff(self):
        calls = []
        def fake(url):
            calls.append(url)
            if "page=2" in url:
                return [pr(9, updated="2026-09-10T00:00:00Z")], None
            return [pr(10)], '<https://api.github.com/repositories/1234/pulls?state=all&per_page=100&page=2>; rel="next"'
        client=mod.GitHubAPI(requester=fake)
        result=client.list_prs(REPO,state="all",cutoff=NOW-mod.WINDOWS["30d"])
        self.assertEqual([p["number"] for p in result], [10])
        self.assertEqual(client.requests, 2)

    def test_api_pagination_limit_fails_closed(self):
        def fake(url):
            return [pr(10)], '<https://api.github.com/repositories/1234/pulls?page=2>; rel="next"'
        with self.assertRaisesRegex(mod.PRActivityError, "pagination limit"):
            list(mod.GitHubAPI(requester=fake,max_pages=1).pages(f"/repos/{REPO}/pulls?per_page=100"))

    def test_pagination_external_url_refused(self):
        def fake(url):
            return [], '<https://evil.example/repos/opensiro/foo/pulls>; rel="next"'
        with self.assertRaisesRegex(mod.PRActivityError, "unexpected API"):
            list(mod.GitHubAPI(requester=fake).pages(f"/repos/{REPO}/pulls"))

    def test_collector_failure_marks_unavailable_not_zero(self):
        class Failing:
            requests=0
            def list_prs(self,*args,**kwargs):
                raise mod.PRActivityError("HTTP 403")
        result=mod.collect(Failing(),NOW)
        self.assertEqual(len(result["repositories"]),5)
        self.assertEqual(result["complete_repositories"],0)
        for row in result["repositories"].values():
            self.assertEqual(row["status"],"unavailable")
            self.assertIsNone(row["open_prs"])
            self.assertIsNone(row["windows"])

    def test_review_outage_preserves_complete_open_and_events(self):
        class One:
            def list_prs(self,repo,*,state,cutoff=None):
                return [pr(9)] if state=="all" else [pr(9)]
            def list_reviews(self,repo,number):
                raise mod.PRActivityError("rate limit")
        row=mod.collect_one(One(),REPO,NOW)
        self.assertEqual(row["windows"]["24h"]["opened"],1)
        self.assertEqual(row["status"],"partial")
        self.assertIn("rate limit",row["review_collection_issue"])


if __name__=="__main__":
    unittest.main()
