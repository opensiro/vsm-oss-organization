from __future__ import annotations

import base64
import unittest

from scripts.check_public_routing import (
    TODO_URL,
    Repository,
    RoutingError,
    decode_readme_payload,
    evaluate_repositories,
    fetch_repository_metadata,
    route_marker_present,
    scope_repositories_from_readme,
    todo_marker_present,
)


class PublicRoutingTests(unittest.TestCase):
    def test_regular_repository_requires_organization_route(self) -> None:
        readme = (
            "Repository-local work stays here.\n\n"
            "For organization-wide work see "
            "https://github.com/opensiro/vsm-oss-organization/blob/main/CONTRIBUTOR_START.md."
        )
        self.assertTrue(
            route_marker_present("opensiro/vsm-harness-index", readme, "opensiro")
        )

    def test_todo_url_alone_does_not_satisfy_organization_route(self) -> None:
        self.assertFalse(
            route_marker_present(
                "opensiro/vsm-harness-index",
                f"Current work: {TODO_URL}",
                "opensiro",
            )
        )

    def test_regular_repository_without_route_is_rejected(self) -> None:
        self.assertFalse(
            route_marker_present(
                "opensiro/vsm-harness-index",
                "Repository-local work stays here.",
                "opensiro",
            )
        )

    def test_todo_marker_requires_canonical_todo_url(self) -> None:
        self.assertTrue(
            todo_marker_present(
                "opensiro/vsm-harness-index", f"Current work: {TODO_URL}", "opensiro"
            )
        )
        self.assertFalse(
            todo_marker_present(
                "opensiro/vsm-harness-index",
                "Use a local TODO.md for this repository.",
                "opensiro",
            )
        )

    def test_organization_repository_accepts_relative_route_and_todo(self) -> None:
        readme = "Start with [CONTRIBUTOR_START.md](CONTRIBUTOR_START.md) and [TODO.md](TODO.md)."
        self.assertTrue(
            route_marker_present("opensiro/vsm-oss-organization", readme, "opensiro")
        )
        self.assertTrue(
            todo_marker_present("opensiro/vsm-oss-organization", readme, "opensiro")
        )

    def test_scope_is_parsed_from_canonical_readme_block(self) -> None:
        readme = """
## Scope

Current in-scope public repositories:

- `opensiro/vsm-harness-profile`
- `opensiro/vsm-harness-index`
- `opensiro/vsm-oss-organization`

Scope membership does not mean all are S1.
"""
        self.assertEqual(
            [
                "opensiro/vsm-harness-profile",
                "opensiro/vsm-harness-index",
                "opensiro/vsm-oss-organization",
            ],
            scope_repositories_from_readme(readme),
        )

    def test_scope_parser_rejects_missing_marker(self) -> None:
        with self.assertRaises(RoutingError):
            scope_repositories_from_readme("No scope here")

    def test_base64_readme_payload_decodes(self) -> None:
        text = "route to opensiro/vsm-oss-organization"
        payload = {
            "encoding": "base64",
            "content": base64.b64encode(text.encode("utf-8")).decode("ascii"),
        }
        self.assertEqual(text, decode_readme_payload(payload))

    def test_repository_metadata_requires_public_scoped_repository(self) -> None:
        def get_json(url: str, token: str | None) -> object:
            self.assertIsNone(token)
            self.assertTrue(url.endswith("/repos/opensiro/vsm-harness-index"))
            return {
                "private": False,
                "full_name": "opensiro/vsm-harness-index",
                "default_branch": "main",
            }

        self.assertEqual(
            Repository("opensiro/vsm-harness-index", "main"),
            fetch_repository_metadata(
                "opensiro/vsm-harness-index",
                get_json=get_json,
            ),
        )

    def test_private_scoped_repository_is_rejected(self) -> None:
        def get_json(url: str, token: str | None) -> object:
            return {
                "private": True,
                "full_name": "opensiro/vsm-harness-index",
                "default_branch": "main",
            }

        with self.assertRaises(RoutingError):
            fetch_repository_metadata(
                "opensiro/vsm-harness-index",
                get_json=get_json,
            )

    def test_evaluation_requires_route_and_todo(self) -> None:
        repositories = [
            Repository("opensiro/vsm-harness-index", "main"),
            Repository("opensiro/vsm-harness-skills", "main"),
            Repository("opensiro/vsm-harness-profile", "main"),
        ]
        readmes = {
            "opensiro/vsm-harness-index": (
                "See opensiro/vsm-oss-organization for shared authority.\n"
                f"Current work: {TODO_URL}"
            ),
            "opensiro/vsm-harness-skills": (
                "See opensiro/vsm-oss-organization for shared authority."
            ),
            "opensiro/vsm-harness-profile": f"Current work: {TODO_URL}",
        }

        results = evaluate_repositories(
            repositories,
            org="opensiro",
            readme_loader=lambda repo: readmes[repo.full_name],
        )
        self.assertEqual([True, False, False], [result.ok for result in results])
        self.assertIn("shared Organization TODO", results[1].detail)
        self.assertIn("vsm-oss-organization route", results[2].detail)

    def test_evaluation_treats_unreadable_readme_as_failure(self) -> None:
        repository = Repository("opensiro/vsm-harness-profile", "main")

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
