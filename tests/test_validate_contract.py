from __future__ import annotations

import importlib.util
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

Repositories outside the declared current in-scope set may still consume related artifacts. Dependency alone does not place them under this control plane.

## Source boundary

- Normative VSM semantics: `opensiro/vsm-harness-profile` `0.2.1`.
- Local `A/C/P/—/?` autonomy notation and assessment procedure: `opensiro/vsm-harness-skills` Methodology `0.2.3`.

[Control](CONTROL_PLANE.md) [Roadmap](ROADMAP.md) [Contributing](CONTRIBUTING.md)
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

- `opensiro/vsm-harness-profile` owns semantics.
- `opensiro/vsm-harness-skills` owns methodology.
- `opensiro/vsm-harness-index` owns corpus.
- `opensiro/awesome-vsm-harness` owns curation.
- `opensiro/terminal-bench-vsm`, `opensiro/arctic-0`, and `opensiro/opensiro.com` are outside this organizational scope even when they consume related artifacts.

## Released contract vs frozen work

| Surface | Profile | Methodology | Meaning |
| --- | --- | --- | --- |
| active contract for new work | `0.2.1` | `0.2.3` | current |
| Index Reassessment R1 | `0.2.0` | `0.2.1` | frozen historical contract |

Current released state:

- Profile `0.2.1` is tagged/released at a pinned commit.
- Methodology `0.2.3` is tagged/released at a pinned commit.
- the Index active contract is `Profile 0.2.1 / Methodology 0.2.3` for new work.
- R1 remains frozen on `Profile 0.2.0 / Methodology 0.2.1`.
"""


class ContractValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "roles").mkdir()
        (self.root / "prompts").mkdir()
        (self.root / "README.md").write_text(readme_text(), encoding="utf-8")
        (self.root / "CONTROL_PLANE.md").write_text(control_text(), encoding="utf-8")
        (self.root / "ROADMAP.md").write_text(roadmap_text(), encoding="utf-8")
        (self.root / "CONTRIBUTING.md").write_text("# Contributing\n", encoding="utf-8")
        (self.root / "roles" / "S1.md").write_text("# S1\n", encoding="utf-8")
        (self.root / "prompts" / "contribute.md").write_text("# Prompt\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def errors(self) -> list[str]:
        return validator.validate(self.root)

    def test_valid_contract_allows_frozen_historical_versions(self) -> None:
        self.assertEqual([], self.errors())

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
            any("ownership repository set drifts from README scope" in error for error in self.errors())
        )

    def test_active_release_pair_drift_is_rejected(self) -> None:
        path = self.root / "CONTROL_PLANE.md"
        text = path.read_text(encoding="utf-8").replace(
            "| active contract for new work | `0.2.1` | `0.2.3` |",
            "| active contract for new work | `0.2.1` | `9.9.9` |",
        )
        path.write_text(text, encoding="utf-8")
        self.assertTrue(
            any("active Profile/Methodology pair drifts" in error for error in self.errors())
        )

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
        self.assertTrue(any("broken local Markdown link" in error for error in self.errors()))

    def test_success_notice_does_not_claim_semantic_or_ownership_proof(self) -> None:
        notice = validator.NON_SEMANTIC_NOTICE
        self.assertIn("does not establish VSM semantics", notice)
        self.assertIn("autonomous ownership", notice)
        self.assertIn("S1=A", notice)


if __name__ == "__main__":
    unittest.main()
