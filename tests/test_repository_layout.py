from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_ROOT_MARKDOWN = {
    "README.md",
    "START_HERE.md",
    "TODO.md",
    "CONTRIBUTOR_START.md",
    "CONTRIBUTE_WITH_AI.md",
    "CONTRIBUTING.md",
}


class RepositoryLayoutTests(unittest.TestCase):
    def test_root_markdown_is_entry_and_control_surface_only(self) -> None:
        actual = {path.name for path in ROOT.glob("*.md")}
        self.assertEqual(ALLOWED_ROOT_MARKDOWN, actual)

    def test_key_route_documents_link_to_existing_local_targets(self) -> None:
        # Offline CI guard for navigation: paths are resolved relative to the
        # authored docs/ file, not the repository root or GitHub's UI.
        for relative in ("docs/ECOSYSTEM.md", "docs/ROADMAP.md"):
            page = ROOT / relative
            content = page.read_text(encoding="utf-8")
            for match in re.finditer(r"(?<!!)\]\(([^)]+)\)", content):
                href = match.group(1).split("#", 1)[0]
                if not href or href.startswith(("https://", "http://", "mailto:")):
                    continue
                target = page.parent / unquote(href)
                with self.subTest(page=relative, href=href):
                    self.assertTrue(target.exists(), f"Broken relative link in {relative}: {href}")

    def test_long_form_docs_and_contracts_have_canonical_homes(self) -> None:
        required = (
            "docs/README.md",
            "docs/ECOSYSTEM.md",
            "docs/ORGANIZATION.md",
            "docs/CONTROL_PLANE.md",
            "docs/ROADMAP.md",
            "docs/METRICS.md",
            "docs/AUTONOMOUS_WORK_REPORTING.md",
            "docs/ROUTING_CONFORMANCE.md",
            "docs/CONTRIBUTOR_CONFORMANCE.md",
            "contracts/s1/domain-contracts.md",
            "contracts/s1/task-admission-recovery.md",
            "contracts/s3/current-control.md",
            "contracts/s3star/audit.md",
            "contracts/s5/parent-boundary.md",
            "contracts/s5/parent-authority.md",
            "contracts/tools/external-entry.md",
            "records/s1/autonomy-coverage.md",
        )
        for relative in required:
            self.assertTrue((ROOT / relative).is_file(), relative)


if __name__ == "__main__":
    unittest.main()
