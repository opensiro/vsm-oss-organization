"""Native deterministic fixtures for the read-only standards probe (#288)."""

from __future__ import annotations

import base64
import unittest
from pathlib import Path

from scripts.check_public_routing import RoutingError
from scripts.check_repository_standards import (
    _readme_heading_anchors,
    _readme_local_targets,
    build_report,
    inspect_repository,
)


BASE = "https://api.github.com/repos/opensiro"
SHA = "a" * 40
START = "https://github.com/opensiro/vsm-oss-organization/blob/main/START_HERE.md"
TODO = "https://github.com/opensiro/vsm-oss-organization/blob/main/TODO.md"
ROUTE = "https://github.com/opensiro/vsm-oss-organization/blob/main/CONTRIBUTOR_START.md"


def source_fixture(repo: str = "opensiro/vsm-harness-index", *, complete: bool = True) -> dict:
    base = f"{BASE}/{repo.split('/', 1)[1]}"
    readme = f"# Test repository\n{START}\n{TODO}\n{ROUTE}" if complete else "Local documentation only"
    return {
        base: {"full_name": repo, "private": False, "default_branch": "main",
               "delete_branch_on_merge": True, "description": "Evidence-backed VSM work",
               "topics": ["vsm"], "license": {"spdx_id": "Apache-2.0"}},
        base + "/branches/main": {"protected": True, "commit": {"sha": SHA}},
        base + "/rulesets": [{"id": 1, "name": "Protect main", "enforcement": "active"}],
        base + "/rulesets/1": {"rules": [{"type": "pull_request",
                                           "parameters": {"required_approving_review_count": 0}}]},
        base + f"/readme?ref={SHA}": {
            "encoding": "base64", "content": base64.b64encode(readme.encode()).decode()
        },
        base + f"/git/trees/{SHA}?recursive=1": {"truncated": False, "tree": [
            {"path": "README.md", "type": "blob"},
            {"path": "docs", "type": "tree"},
            {"path": "docs/guide.md", "type": "blob"},
        ]},
        base + f"/contents?ref={SHA}": [{"name": "LICENSE", "type": "file"},
                                         {"name": "CONTRIBUTING.md", "type": "file"}],
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
    def test_readme_local_links_are_source_pinned_and_advisory(self) -> None:
        responses = source_fixture()
        base = f"{BASE}/vsm-harness-index"
        readme = (f"# Intro\n{START}\n{TODO}\n{ROUTE}\n"
                  "[Guide](./docs/guide.md#usage) [Intro](#intro) "
                  "[Missing](docs/missing.md) [External](https://example.com/x.md)\n")
        responses[base + f"/readme?ref={SHA}"]["content"] = base64.b64encode(readme.encode()).decode()
        _, findings = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                          get_json=loader(responses))
        finding = by_dimension(findings)["readme_local_links"]
        self.assertEqual(finding.status, "DRIFT")
        self.assertEqual(finding.rule, "ADVISORY")
        self.assertEqual(finding.source, base + f"/git/trees/{SHA}?recursive=1")
        self.assertIn("docs/missing.md", finding.detail)
        self.assertNotIn("example.com", finding.detail)

    def test_readme_local_links_ignore_code_and_check_self_anchors(self) -> None:
        readme = ("# I'm human\n## Same\n## Same\n"
                  "[Human](#im-human) [Second](#same-1) [Guide](docs/guide.md)\n"
                  "```md\n[Fake](missing-in-code.md)\n```\n")
        paths, anchors = _readme_local_targets(readme)
        self.assertEqual(paths, {"docs/guide.md"})
        self.assertEqual(anchors, {"im-human", "same-1"})
        self.assertTrue(anchors.issubset(_readme_heading_anchors(readme)))

    def test_missing_readme_self_anchor_is_advisory_drift(self) -> None:
        responses = source_fixture()
        base = f"{BASE}/vsm-harness-index"
        readme = f"# Intro\n{START}\n{TODO}\n{ROUTE}\n[Bad anchor](#missing-heading)\n"
        responses[base + f"/readme?ref={SHA}"]["content"] = base64.b64encode(readme.encode()).decode()
        _, findings = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                          get_json=loader(responses))
        finding = by_dimension(findings)["readme_local_links"]
        self.assertEqual(finding.status, "DRIFT")
        self.assertEqual(finding.rule, "ADVISORY")
        self.assertIn("missing-heading", finding.detail)

    def test_inaccessible_tree_does_not_report_missing_readme_links(self) -> None:
        responses = source_fixture()
        base = f"{BASE}/vsm-harness-index"
        responses.pop(base + f"/git/trees/{SHA}?recursive=1")
        _, findings = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                          get_json=loader(responses))
        finding = by_dimension(findings)["readme_local_links"]
        self.assertEqual(finding.status, "UNKNOWN")
        self.assertIn("403", finding.detail)

    def test_truncated_tree_is_unknown_not_a_false_positive(self) -> None:
        responses = source_fixture()
        base = f"{BASE}/vsm-harness-index"
        responses[base + f"/git/trees/{SHA}?recursive=1"]["truncated"] = True
        _, findings = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                          get_json=loader(responses))
        self.assertEqual(by_dimension(findings)["readme_local_links"].status, "UNKNOWN")

    def test_existing_control_plane_routes_to_read_only_probe(self) -> None:
        control = (Path(__file__).resolve().parents[1] / "docs" /
                   "AGENT_CONTROL_PLANE.md").read_text(encoding="utf-8")
        self.assertIn("| **Repository Standards** | `check repository standards` |", control)
        self.assertIn("REPOSITORY_STANDARDS_ASSURANCE.md", control)
        self.assertIn("Upstream is in the current six-repository scope", control)

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

    def test_upstream_settings_are_advisory_even_when_in_scope(self) -> None:
        responses = source_fixture(repo="opensiro/upstream")
        base = f"{BASE}/upstream"
        responses[base]["topics"] = []
        responses[base]["license"] = None
        responses[base + "/rulesets"] = []
        responses[base + f"/contents?ref={SHA}"] = [{"name": "README.md", "type": "file"}]
        sha, found = inspect_repository("opensiro/upstream", in_scope=True,
                                        get_json=loader(responses))
        self.assertEqual(sha, SHA)
        dimensions = by_dimension(found)
        self.assertEqual(dimensions["delete_branch_on_merge"].status, "PASS")
        self.assertEqual(dimensions["repository_topics"].status, "DRIFT")
        self.assertEqual(dimensions["root_license"].status, "DRIFT")
        self.assertEqual(dimensions["github_license_detection"].status, "DRIFT")
        self.assertEqual(dimensions["protect_main_ruleset"].status, "DRIFT")
        self.assertEqual(dimensions["branch_protected"].status, "PASS")
        self.assertTrue(all(f.status != "NON_COMPLIANT" for f in found))

    def test_upstream_routing_is_required_inside_current_scope(self) -> None:
        responses = source_fixture(repo="opensiro/upstream", complete=False)
        _, found = inspect_repository("opensiro/upstream", in_scope=True,
                                      get_json=loader(responses))
        self.assertEqual(by_dimension(found)["common_start_here"].status, "NON_COMPLIANT")
        self.assertEqual(by_dimension(found)["shared_todo"].rule, "REQUIRED")

    def test_six_repo_boundary_is_read_from_current_readme(self) -> None:
        root = Path(__file__).resolve().parents[1]
        scope_text = (root / "README.md").read_text(encoding="utf-8")
        names = ["vsm-harness-profile", "vsm-harness-skills", "vsm-harness-index",
                 "awesome-vsm-harness", "upstream", "vsm-oss-organization"]
        responses = {}
        for name in names:
            responses.update(source_fixture(f"opensiro/{name}"))
        report = build_report(scope_text, get_json=loader(responses),
                              as_of="2026-11-06T00:00:00Z")
        self.assertEqual(len(report["repositories"]), 6)
        self.assertTrue(all(item["in_scope"] for item in report["repositories"]))
        self.assertIn("6-repository", report["system_in_focus"])

    def test_provider_403_is_unknown_not_evidence_of_missing_protection(self) -> None:
        responses = source_fixture()
        responses.pop(f"{BASE}/vsm-harness-index/rulesets")
        _, found = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                      get_json=loader(responses))
        dimension = by_dimension(found)["protect_main_ruleset"]
        self.assertEqual(dimension.status, "UNKNOWN")
        self.assertIn("403", dimension.detail)

    def test_ruleset_detail_403_is_unknown_not_zero_approvals(self) -> None:
        responses = source_fixture()
        responses.pop(f"{BASE}/vsm-harness-index/rulesets/1")
        _, found = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                      get_json=loader(responses))
        dimension = by_dimension(found)["ruleset_gate_evidence"]
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
        self.assertEqual(by_dimension(found)["readme_local_links"].status, "UNKNOWN")

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
        self.assertEqual(by_dimension(found)["readme_local_links"].status, "UNKNOWN")
        self.assertIn("immutable", by_dimension(found)["shared_todo"].detail)

    def test_missing_default_branch_cannot_skip_required_routing(self) -> None:
        responses = source_fixture()
        del responses[f"{BASE}/vsm-harness-index"]["default_branch"]
        sha, found = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                        get_json=loader(responses))
        self.assertIsNone(sha)
        dimensions = by_dimension(found)
        self.assertEqual(dimensions["default_branch"].status, "UNKNOWN")
        for dimension in ("pinned_head", "common_start_here",
                          "organization_route", "shared_todo"):
            with self.subTest(dimension=dimension):
                self.assertEqual(dimensions[dimension].status, "UNKNOWN")
                self.assertEqual(dimensions[dimension].rule, "REQUIRED")

    def test_malformed_commit_payload_is_unknown_instead_of_crash(self) -> None:
        responses = source_fixture()
        responses[f"{BASE}/vsm-harness-index/branches/main"]["commit"] = None
        sha, found = inspect_repository("opensiro/vsm-harness-index", in_scope=True,
                                        get_json=loader(responses))
        self.assertIsNone(sha)
        self.assertEqual(by_dimension(found)["pinned_head"].status, "UNKNOWN")
        self.assertEqual(by_dimension(found)["common_start_here"].status, "UNKNOWN")

    def test_report_scope_cannot_admit_adjacent_repository(self) -> None:
        scope_text = "Current in-scope public repositories:\n\n- `opensiro/vsm-harness-index`\n"
        all_responses = {**source_fixture(), **source_fixture("opensiro/vsm-harness-capability", complete=False)}
        report = build_report(scope_text, adjacent=["opensiro/vsm-harness-capability", "opensiro/vsm-harness-capability"],
                              get_json=loader(all_responses), as_of="2026-10-25T00:00:00Z")
        items = report["repositories"]
        self.assertEqual([item["repository"] for item in items],
                         ["opensiro/vsm-harness-index", "opensiro/vsm-harness-capability"])
        self.assertEqual([item["in_scope"] for item in items], [True, False])
        self.assertEqual(items[1]["default_head_sha"], SHA)

    def test_rejects_unbounded_or_cross_owner_adjacent_name(self) -> None:
        scope_text = "Current in-scope public repositories:\n\n- `opensiro/vsm-harness-index`\n"
        with self.assertRaises(RoutingError):
            build_report(scope_text, adjacent=["someone/another"], get_json=loader({}))


if __name__ == "__main__":
    unittest.main()
