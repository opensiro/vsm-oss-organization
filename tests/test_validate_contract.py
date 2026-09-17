from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_contract.py"
SPEC = importlib.util.spec_from_file_location("validate_contract", MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)

IN_SCOPE = [
    "opensiro/vsm-harness-profile",
    "opensiro/vsm-harness-skills",
    "opensiro/vsm-harness-index",
    "opensiro/awesome-vsm-harness",
    "opensiro/vsm-oss-organization",
]
VECTORS = {
    "M0": "A — — — — —",
    "M1": "A — C A — —",
    "M2": "A — C A — P",
    "M3": "A — A A — P",
    "M4": "A A A A — P",
    "M5": "A A A A A P",
}
METHOD_SHA = "01e13e595c101bd526fd1913863bfd8170f08116"


def roadmap_text() -> str:
    first = "\n".join(
        f"| `{milestone}` — test | #{index + 2} | `{value}` | scope |"
        for index, (milestone, value) in enumerate(VECTORS.items())
    )
    second = "\n".join(
        f"| {milestone} — test | `{value}` | why |"
        for milestone, value in VECTORS.items()
    )
    sections = "\n\n".join(
        f"## {milestone} — test\n\nTarget: `{value}`\n\nText."
        for milestone, value in VECTORS.items()
    )
    return f"""# OSM Roadmap

## GitHub milestone correspondence

| GitHub milestone | Tracker issue | Target vector | Scope introduced |
| --- | --- | --- | --- |
{first}

## Milestone sequence

| Milestone | Target vector | Why it exists |
| --- | --- | --- |
{second}

{sections}
"""


def readme_text() -> str:
    in_scope = "\n".join(f"- `{repo}`" for repo in IN_SCOPE)
    return f"""# VSM OSS Organization

## Scope

Current in-scope public repositories:

{in_scope}

Repositories outside the declared current in-scope set may still consume related artifacts.

## Source boundary

[Upstream](UPSTREAM_CONTRACT.json) [Control](CONTROL_PLANE.md)
[Roadmap](ROADMAP.md) [Contributing](CONTRIBUTING.md)
[Role](roles/S1.md) [Prompt](prompts/contribute.md)

Current milestone:

```text
S1  S2  S3  S3* S4  S5
{VECTORS['M0']}
```

Long-term reference target:

```text
S1  S2  S3  S3* S4  S5
{VECTORS['M5']}
```
"""


def control_text() -> str:
    return """# Control Plane

[Upstream contract](UPSTREAM_CONTRACT.json)

- `opensiro/vsm-harness-profile` owns semantics.
- `opensiro/vsm-harness-skills` owns methodology.
- `opensiro/vsm-harness-index` owns corpus.
- `opensiro/awesome-vsm-harness` owns curation.
"""


def manifest() -> dict:
    return {
        "profile": {
            "repository": "opensiro/vsm-harness-profile",
            "source_kind": "release",
            "ref": "v0.2.2",
            "version": "0.2.2",
            "version_path": "VERSION",
            "consumer_contract_path": "CONSUMER_CONTRACT.md",
            "release_impact_path": "RELEASE_IMPACT.json",
        },
        "methodology": {
            "repository": "opensiro/vsm-harness-skills",
            "source_kind": "commit",
            "ref": METHOD_SHA,
            "version": "0.3.1",
            "version_path": "skills/assess-vsm-harness/VERSION",
        },
        "index": {
            "repository": "opensiro/vsm-harness-index",
            "source_kind": "branch",
            "ref": "main",
            "active_contract_path": "data/active-contract.psv",
        },
    }


def impact(assessment_impact: str = "none") -> dict:
    selectors = [] if assessment_impact == "none" else ["concept:test"]
    return {
        "profile": "opensiro/vsm-harness-profile",
        "releases": [
            {
                "version": "0.2.0",
                "previous": "baseline",
                "compatibility": "compatible",
                "assessment_impact": "targeted",
                "selectors": ["concept:ownership"],
            },
            {
                "version": "0.2.1",
                "previous": "0.2.0",
                "compatibility": "compatible",
                "assessment_impact": "none",
                "selectors": [],
            },
            {
                "version": "0.2.2",
                "previous": "0.2.1",
                "compatibility": "compatible",
                "assessment_impact": assessment_impact,
                "selectors": selectors,
            },
        ],
    }


class ContractValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name) / "organization"
        self.profile = Path(self.tempdir.name) / "profile"
        self.methodology = Path(self.tempdir.name) / "methodology"
        self.index = Path(self.tempdir.name) / "index"

        (self.root / "roles").mkdir(parents=True)
        (self.root / "prompts").mkdir()
        (self.root / "README.md").write_text(readme_text(), encoding="utf-8")
        (self.root / "CONTROL_PLANE.md").write_text(control_text(), encoding="utf-8")
        (self.root / "ROADMAP.md").write_text(roadmap_text(), encoding="utf-8")
        (self.root / "CONTRIBUTING.md").write_text("# Contributing\n", encoding="utf-8")
        (self.root / "roles" / "S1.md").write_text("# S1\n", encoding="utf-8")
        (self.root / "prompts" / "contribute.md").write_text("# Prompt\n", encoding="utf-8")
        (self.root / "UPSTREAM_CONTRACT.json").write_text(
            json.dumps(manifest(), indent=2) + "\n", encoding="utf-8"
        )

        self.profile.mkdir()
        (self.profile / "VERSION").write_text("0.2.2\n", encoding="utf-8")
        (self.profile / "CONSUMER_CONTRACT.md").write_text("# Consumer\n", encoding="utf-8")
        (self.profile / "RELEASE_IMPACT.json").write_text(
            json.dumps(impact(), indent=2) + "\n", encoding="utf-8"
        )

        method_version = self.methodology / "skills" / "assess-vsm-harness"
        method_version.mkdir(parents=True)
        (method_version / "VERSION").write_text("0.3.1\n", encoding="utf-8")

        (self.index / "data").mkdir(parents=True)
        (self.index / "data" / "active-contract.psv").write_text(
            "profile_version|methodology_version\n0.2.1|0.3.1\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def errors(self, upstream: bool = False) -> list[str]:
        if not upstream:
            return validator.validate(self.root)
        return validator.validate(
            self.root,
            profile_root=self.profile,
            methodology_root=self.methodology,
            index_root=self.index,
        )

    def test_valid_local_contract_passes(self) -> None:
        self.assertEqual([], self.errors())

    def test_valid_cross_repository_contract_accepts_no_impact_profile_advance(self) -> None:
        self.assertEqual([], self.errors(upstream=True))

    def test_concurrent_readme_target_wording_is_allowed(self) -> None:
        path = self.root / "README.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "Current milestone:\n", "Current milestone target:\n"
            ),
            encoding="utf-8",
        )
        self.assertEqual([], self.errors())

    def test_scope_membership_drift_is_rejected(self) -> None:
        path = self.root / "README.md"
        text = path.read_text(encoding="utf-8").replace(
            "- `opensiro/vsm-oss-organization`\n",
            "- `opensiro/vsm-oss-organization`\n- `opensiro/arctic-0`\n",
            1,
        )
        path.write_text(text, encoding="utf-8")
        self.assertTrue(
            any(
                "ownership repository set drifts from README scope" in error
                for error in self.errors()
            )
        )

    def test_manifest_release_ref_drift_is_rejected(self) -> None:
        path = self.root / "UPSTREAM_CONTRACT.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["profile"]["ref"] = "main"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(
            any("released Profile ref must be" in error for error in self.errors())
        )

    def test_readme_must_not_restore_duplicated_active_pair(self) -> None:
        path = self.root / "README.md"
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\n- Normative VSM semantics: `opensiro/vsm-harness-profile` `0.2.2`.\n",
            encoding="utf-8",
        )
        self.assertTrue(
            any(
                "active Profile version must come from UPSTREAM_CONTRACT.json" in error
                for error in self.errors()
            )
        )

    def test_profile_source_version_drift_is_rejected(self) -> None:
        (self.profile / "VERSION").write_text("0.2.1\n", encoding="utf-8")
        self.assertTrue(
            any(
                "Profile upstream version drift" in error
                for error in self.errors(upstream=True)
            )
        )

    def test_methodology_source_version_drift_is_rejected(self) -> None:
        path = self.methodology / "skills" / "assess-vsm-harness" / "VERSION"
        path.write_text("0.2.3\n", encoding="utf-8")
        self.assertTrue(
            any(
                "Methodology upstream version drift" in error
                for error in self.errors(upstream=True)
            )
        )

    def test_index_methodology_mismatch_is_rejected(self) -> None:
        (self.index / "data" / "active-contract.psv").write_text(
            "profile_version|methodology_version\n0.2.1|9.9.9\n",
            encoding="utf-8",
        )
        self.assertTrue(
            any(
                "Index active Methodology does not match" in error
                for error in self.errors(upstream=True)
            )
        )

    def test_targeted_profile_transition_requires_explicit_review(self) -> None:
        (self.profile / "RELEASE_IMPACT.json").write_text(
            json.dumps(impact("targeted"), indent=2) + "\n", encoding="utf-8"
        )
        self.assertTrue(
            any(
                "compatibility review required" in error
                for error in self.errors(upstream=True)
            )
        )

    def test_missing_intermediate_profile_transition_is_rejected(self) -> None:
        (self.index / "data" / "active-contract.psv").write_text(
            "profile_version|methodology_version\n0.2.0|0.3.1\n",
            encoding="utf-8",
        )
        data = impact()
        data["releases"] = [
            item for item in data["releases"] if item["version"] != "0.2.1"
        ]
        (self.profile / "RELEASE_IMPACT.json").write_text(
            json.dumps(data), encoding="utf-8"
        )
        self.assertTrue(
            any(
                "cannot reconstruct path" in error
                for error in self.errors(upstream=True)
            )
        )

    def test_partial_upstream_roots_are_rejected(self) -> None:
        errors = validator.validate(self.root, profile_root=self.profile)
        self.assertTrue(any("requires --profile-root" in error for error in errors))

    def test_milestone_vector_drift_is_rejected(self) -> None:
        path = self.root / "ROADMAP.md"
        text = path.read_text(encoding="utf-8").replace(
            "| M3 — test | `A — A A — P` | why |",
            "| M3 — test | `A A A A — P` | why |",
        )
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("M3 target vector drifts" in error for error in self.errors()))

    def test_broken_local_link_is_rejected(self) -> None:
        path = self.root / "README.md"
        path.write_text(
            path.read_text(encoding="utf-8") + "\n[Missing](missing.md)\n",
            encoding="utf-8",
        )
        self.assertTrue(
            any("broken local Markdown link" in error for error in self.errors())
        )

    def test_success_notice_does_not_claim_semantic_or_ownership_proof(self) -> None:
        notice = validator.NON_SEMANTIC_NOTICE
        self.assertIn("does not establish VSM semantics", notice)
        self.assertIn("autonomous ownership", notice)
        self.assertIn("S1=A", notice)


if __name__ == "__main__":
    unittest.main()
