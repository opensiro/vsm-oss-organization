"""Native deterministic fixtures for the read-only standards probe (#288)."""

from __future__ import annotations

import base64
import unittest

from scripts.check_public_routing import RoutingError
from scripts.check_repository_standards import build_report, inspect_repository


BASE = "https://api.github.com/repos/opensiro"
SHA = "a" * 40
START = "https://github.com/opensiro/vsm-oss-organization/blob/main/START_HERE.md"
TODO = "https://github.com/opensiro/vsm-oss-organization/blob/main/TODO.md"
ROUTE = "https://github.com/opensiro/vsm-oss-organization/blob/main/CONTRIBUTOR_START.md"


def source_fixture(repo: str = "opensiro/vsm-harness-index", *, complete: bool = True) -> dict:
    base = f"{BASE}/{repo.split('/', 1)[1]}"
    readme = f"{START}\n{TODO}\n{ROUTE}" if complete else "Local documentation only"
    return {
        base: {"full_name": repo, "private": False, "default_branch": "main",
               "delete_branch_on_merge": True},
        base + "/branches/main": {"protected": True, "commit": {"sha": SHA}},
        base + "/rulesets": [{"name": "Protect main", "enforcement": "active"}],
        base + f"/readme?ref={SHA}": {
            "encoding": "base64", "content": base64.b64encode(readme.encode()).decode()
        },
        base + f"/contents?ref={SHA}": [{"name": "LICENSE", "type": "file"}],
        base + f"/contents/.github/workflows?ref={SHA}": [{"name": "verify.yml", "type": "file"}],
    }


def loader(responses: dict):
    def fetch(url: str, token: str | None = None):
        if url not in responses:
            raise RoutingError(f"GitHub API returned HTTP 403 for {url}")
        response = responses[url]
        if isinstance(response, BaseException):
            raise response
        return response

    return fetch


def by_dimension(findings):
    return {finding.dimension: finding for finding in findings}


class RepositoryStandardsProbeTests(unittest.TestCase):
    def test_complete_in_scope_repository_is_pinned_and_passes(self) -> None:
        sha, found = inspect_repository(
            "opensiro/vsm-harness-index", in_scope=True,
            get_json=loader(source_fixture()),
        )
        self.assertEqual(sha, SHA)
        self.assertEqual({f.status for f in found}, {"PASS"})
        self.assertEqual(by_dimension(found)["common_start_here"].rule, "REQUIRED")

    def test_absent_routing_is_non_compliant_only_inside_scope(self) -> None:
        responses = source_fixture(complete=False)
        _, scoped = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                        get_json=loader(responses))
        _, adjacent = inspect_repository("opensiro/vsm-harness-index", in_scope=False,
                                          get_json=loader(responses))
        self.assertEqual(by_dimension(scoped)["shared_todo"].status, "NON_COMPLIANT")
        self.assertEqual(by_dimension(adjacent)["shared_todo"].status, "DRIFT")
        self.assertEqual(by_dimension(adjacent)["shared_todo"].rule, "ADVISORY")

    def test_actual_upstream_like_settings_are_drift_not_silent_policy(self) -> None:
        responses = source_fixture(repo="opensiro/upstream", complete=False)
        base = f"{BASE}/upstream"
        responses[base]["delete_branch_on_merge"] = False
        responses[base + "/rulesets"] = []
        responses[base + f"/contents?ref={SHA}"] = [{"name": "README.md", "type": "file"}]
        sha, found = inspect_repository("opensiro/upstream", in_scope=False,
                                        get_json=loader(responses))
        self.assertEqual(sha, SHA)
        dimensions = by_dimension(found)
        self.assertEqual(dimensions["delete_branch_on_merge"].status, "DRIFT")
        self.assertEqual(dimensions["root_license"].status, "DRIFT")
        self.assertEqual(dimensions["protect_main_ruleset"].status, "DRIFT")
        self.assertEqual(dimensions["branch_protected"].status, "PASS")
        self.assertTrue(all(f.status != "NON_COMPLIANT" for f in found))

    def test_provider_403_is_unknown_not_evidence_of_missing_protection(self) -> None:
        responses = source_fixture()
        responses.pop(f"{BASE}/vsm-harness-index/rulesets")
        _, found = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                      get_json=loader(responses))
        dimension = by_dimension(found)["protect_main_ruleset"]
        self.assertEqual(dimension.status, "UNKNOWN")
        self.assertIn("403", dimension.detail)

    def test_pinned_readme_403_is_unknown_not_routing_violation(self) -> None:
        responses = source_fixture()
        responses.pop(f"{BASE}/vsm-harness-index/readme?ref={SHA}")
        sha, found = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                        get_json=loader(responses))
        self.assertEqual(sha, SHA)
        self.assertEqual(by_dimension(found)["common_start_here"].status, "UNKNOWN")
        self.assertEqual(by_dimension(found)["shared_todo"].status, "UNKNOWN")

    def test_missing_metadata_is_unknown_and_does_not_claim_success(self) -> None:
        _, found = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                      get_json=loader({}))
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].status, "UNKNOWN")
        self.assertEqual(found[0].rule, "REQUIRED")

    def test_missing_sha_prevents_unpinned_source_checks(self) -> None:
        responses = source_fixture()
        responses[f"{BASE}/vsm-harness-index/branches/main"]["commit"]["sha"] = "invalid"
        sha, found = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                        get_json=loader(responses))
        self.assertIsNone(sha)
        self.assertEqual(by_dimension(found)["shared_todo"].status, "UNKNOWN")
        self.assertIn("immutable", by_dimension(found)["shared_todo"].detail)

    def test_report_scope_cannot_admit_adjacent_repository(self) -> None:
        scope_text = "Current in-scope public repositories:\n\n- `opensiro/vsm-harness-index`\n"
        all_responses = {**source_fixture(), **source_fixture("opensiro/upstream", complete=False)}
        report = build_report(scope_text, adjacent=["opensiro/upstream", "opensiro/upstream"],
                              get_json=loader(all_responses), as_of="2026-10-25T00:00:00Z")
        items = report["repositories"]
        self.assertEqual([item["repository"] for item in items],
                         ["opensiro/vsm-harness-index", "opensiro/upstream"])
        self.assertEqual([item["in_scope"] for item in items], [True, False])
        self.assertEqual(items[1]["default_head_sha"], SHA)

    def test_rejects_unbounded_or_cross_owner_adjacent_name(self) -> None:
        scope_text = "Current in-scope public repositories:\n\n- `opensiro/vsm-harness-index`\n"
        with self.assertRaises(RoutingError):
            build_report(scope_text, adjacent=["someone/another"], get_json=loader({}))


if __name__ == "__main__":
    unittest.main()
