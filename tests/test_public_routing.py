from __future__ import annotations

import base64
import unittest

from scripts.check_public_routing import (
    Repository,
    RoutingError,
    decode_readme_payload,
    evaluate_repositories,
    list_public_repositories,
    route_marker_present,
)


class PublicRoutingTests(unittest.TestCase):
    def test_regular_repository_requires_organization_route(self) -> None:
        readme = (
            "Repository-local work stays here.\n\n"
            "For organization-wide work see "
            "https://github.com/opensiro/vsm-oss-organization/blob/main/CONTRIBUTOR_START.md."
        )
        self.assertTrue(route_marker_present("opensiro/arctic-0", readme, "opensiro"))

    def test_regular_repository_without_route_is_rejected(self) -> None:
        self.assertFalse(
            route_marker_present(
                "opensiro/arctic-0",
                "Repository-local work stays here.",
                "opensiro",
            )
        )

    def test_organization_repository_accepts_relative_entry_point(self) -> None:
        self.assertTrue(
            route_marker_present(
                "opensiro/vsm-oss-organization",
                "Start with [CONTRIBUTOR_START.md](CONTRIBUTOR_START.md).",
                "opensiro",
            )
        )

    def test_base64_readme_payload_decodes(self) -> None:
        text = "route to opensiro/vsm-oss-organization"
        payload = {
            "encoding": "base64",
            "content": base64.b64encode(text.encode("utf-8")).decode("ascii"),
        }
        self.assertEqual(text, decode_readme_payload(payload))

    def test_inventory_uses_live_public_repository_metadata(self) -> None:
        pages = {
            1: [
                {
                    "private": False,
                    "full_name": "opensiro/zeta",
                    "default_branch": "main",
                },
                {
                    "private": True,
                    "full_name": "opensiro/private-repo",
                    "default_branch": "main",
                },
                {
                    "private": False,
                    "full_name": "opensiro/alpha",
                    "default_branch": "trunk",
                },
            ]
        }

        def get_json(url: str, token: str | None) -> object:
            self.assertIsNone(token)
            self.assertIn("type=public", url)
            return pages[1]

        repositories = list_public_repositories(
            "opensiro",
            get_json=get_json,
        )
        self.assertEqual(
            [
                Repository("opensiro/alpha", "trunk"),
                Repository("opensiro/zeta", "main"),
            ],
            repositories,
        )

    def test_evaluation_reports_missing_route(self) -> None:
        repositories = [
            Repository("opensiro/good", "main"),
            Repository("opensiro/bad", "main"),
        ]
        readmes = {
            "opensiro/good": "See opensiro/vsm-oss-organization for shared authority.",
            "opensiro/bad": "Only local instructions.",
        }

        results = evaluate_repositories(
            repositories,
            org="opensiro",
            readme_loader=lambda repo: readmes[repo.full_name],
        )
        self.assertEqual([True, False], [result.ok for result in results])
        self.assertIn("does not reference", results[1].detail)

    def test_evaluation_treats_unreadable_readme_as_failure(self) -> None:
        repository = Repository("opensiro/missing-readme", "main")

        def load(_: Repository) -> str:
            raise RoutingError("GitHub API returned HTTP 404")

        [result] = evaluate_repositories(
            [repository],
            org="opensiro",
            readme_loader=load,
        )
        self.assertFalse(result.ok)
        self.assertIn("404", result.detail)


if __name__ == "__main__":
    unittest.main()
