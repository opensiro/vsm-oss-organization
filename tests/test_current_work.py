from __future__ import annotations

import unittest

from scripts.check_current_work import (
    IssueRef,
    RoutingError,
    parse_current_work,
    validate_live_issue,
)


class CurrentWorkTests(unittest.TestCase):
    def test_accepts_only_now_next_blocked_issue_links(self) -> None:
        parsed = parse_current_work(
            """
# Current work

## NOW
- https://github.com/opensiro/vsm-harness-index/issues/107

## NEXT
- https://github.com/opensiro/vsm-oss-organization/issues/61

## BLOCKED
- https://github.com/opensiro/vsm-oss-organization/issues/39
"""
        )
        self.assertEqual(
            [IssueRef("opensiro/vsm-harness-index", 107)], parsed["NOW"]
        )
        self.assertEqual(
            [IssueRef("opensiro/vsm-oss-organization", 61)], parsed["NEXT"]
        )
        self.assertEqual(
            [IssueRef("opensiro/vsm-oss-organization", 39)], parsed["BLOCKED"]
        )

    def test_rejects_watch_or_later(self) -> None:
        with self.assertRaises(RoutingError):
            parse_current_work(
                """
## NOW

## NEXT

## BLOCKED

## WATCH
- https://github.com/opensiro/vsm-harness-index/issues/1
"""
            )

    def test_rejects_free_form_scheduler_task(self) -> None:
        with self.assertRaises(RoutingError):
            parse_current_work(
                """
## NOW
- assess another harness

## NEXT

## BLOCKED
"""
            )

    def test_rejects_duplicate_issue(self) -> None:
        with self.assertRaises(RoutingError):
            parse_current_work(
                """
## NOW
- https://github.com/opensiro/vsm-harness-index/issues/107

## NEXT
- https://github.com/opensiro/vsm-harness-index/issues/107

## BLOCKED
"""
            )

    def test_live_issue_must_be_open_issue_not_pr(self) -> None:
        ref = IssueRef("opensiro/vsm-harness-index", 107)

        def open_issue(url: str, token: str | None) -> object:
            self.assertTrue(url.endswith("/repos/opensiro/vsm-harness-index/issues/107"))
            return {"state": "open"}

        validate_live_issue(ref, get_json=open_issue)

        def closed_issue(url: str, token: str | None) -> object:
            return {"state": "closed"}

        with self.assertRaises(RoutingError):
            validate_live_issue(ref, get_json=closed_issue)

        def pull_request(url: str, token: str | None) -> object:
            return {"state": "open", "pull_request": {}}

        with self.assertRaises(RoutingError):
            validate_live_issue(ref, get_json=pull_request)


if __name__ == "__main__":
    unittest.main()
