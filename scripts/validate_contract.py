#!/usr/bin/env python3
"""Deterministic repository-local consistency checks for the Organization contract.

This validator checks duplicated/local contract surfaces only. Passing it does not
establish VSM semantics, function mapping, autonomous ownership, or an autonomy
state such as S1=A.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPO_PATTERN = re.compile(r"`(opensiro/[A-Za-z0-9_.-]+)`")
VERSION_PATTERN = r"([0-9]+\.[0-9]+\.[0-9]+)"
ALLOWED_VECTOR_TOKENS = {"A", "C", "P", "—", "?"}
NON_SEMANTIC_NOTICE = (
    "Passing these checks establishes only repository-local deterministic "
    "consistency; it does not establish VSM semantics, function mapping, "
    "autonomous ownership, or S1=A."
)


def _read(root: Path, relative: str, errors: list[str]) -> str:
    path = root / relative
    if not path.is_file():
        errors.append(f"missing required file: {relative}")
        return ""
    return path.read_text(encoding="utf-8")


def _repo_bullet_block(text: str, marker: str, errors: list[str]) -> set[str]:
    pos = text.find(marker)
    if pos < 0:
        errors.append(f"README missing marker: {marker}")
        return set()

    repos: set[str] = set()
    started = False
    for raw_line in text[pos + len(marker) :].splitlines():
        line = raw_line.strip()
        if not line and not started:
            continue
        if line.startswith("- "):
            started = True
            match = REPO_PATTERN.search(line)
            if match:
                repos.add(match.group(1))
            continue
        if started:
            break

    if not repos:
        errors.append(f"no repository entries found after marker: {marker}")
    return repos


def _active_pair_from_readme(readme: str, errors: list[str]) -> tuple[str, str] | None:
    profile = re.search(
        rf"Normative VSM semantics:\s*`opensiro/vsm-harness-profile`\s*`{VERSION_PATTERN}`",
        readme,
    )
    methodology = re.search(
        rf"`opensiro/vsm-harness-skills`\s+Methodology\s+`{VERSION_PATTERN}`",
        readme,
    )
    if not profile:
        errors.append("README active Profile version reference is missing or malformed")
    if not methodology:
        errors.append("README active Methodology version reference is missing or malformed")
    if not profile or not methodology:
        return None
    return profile.group(1), methodology.group(1)


def _active_pair_from_control(control: str, errors: list[str]) -> tuple[str, str] | None:
    row = re.search(
        rf"^\|\s*active contract for new work\s*\|\s*`{VERSION_PATTERN}`\s*\|\s*`{VERSION_PATTERN}`\s*\|",
        control,
        re.MULTILINE,
    )
    if not row:
        errors.append("CONTROL_PLANE active-contract table row is missing or malformed")
        return None
    return row.group(1), row.group(2)


def _normalize_vector(raw: str, context: str, errors: list[str]) -> tuple[str, ...] | None:
    tokens = tuple(raw.replace("`", "").split())
    if len(tokens) != 6 or any(token not in ALLOWED_VECTOR_TOKENS for token in tokens):
        errors.append(f"invalid six-state milestone vector in {context}: {raw!r}")
        return None
    return tokens


def _roadmap_table_vectors(
    roadmap: str, heading: str, vector_column: int, errors: list[str]
) -> dict[str, tuple[str, ...]]:
    heading_match = re.search(rf"^## {re.escape(heading)}\s*$", roadmap, re.MULTILINE)
    if not heading_match:
        errors.append(f"ROADMAP missing section: {heading}")
        return {}

    tail = roadmap[heading_match.end() :]
    next_heading = re.search(r"^## ", tail, re.MULTILINE)
    section = tail[: next_heading.start()] if next_heading else tail

    result: dict[str, tuple[str, ...]] = {}
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) <= vector_column:
            continue
        milestone = re.search(r"\b(M[0-5])\b", cells[0])
        if not milestone:
            continue
        vector = _normalize_vector(cells[vector_column], f"ROADMAP {heading} {milestone.group(1)}", errors)
        if vector:
            result[milestone.group(1)] = vector

    expected = {f"M{i}" for i in range(6)}
    if set(result) != expected:
        errors.append(
            f"ROADMAP {heading} must contain exactly M0-M5 vectors; found {sorted(result)}"
        )
    return result


def _roadmap_section_vectors(roadmap: str, errors: list[str]) -> dict[str, tuple[str, ...]]:
    result: dict[str, tuple[str, ...]] = {}
    for match in re.finditer(
        r"^## (M[0-5]) —[^\n]+\n\nTarget:\s*`([^`]+)`",
        roadmap,
        re.MULTILINE,
    ):
        vector = _normalize_vector(match.group(2), f"ROADMAP {match.group(1)} section", errors)
        if vector:
            result[match.group(1)] = vector
    expected = {f"M{i}" for i in range(6)}
    if set(result) != expected:
        errors.append(f"ROADMAP milestone sections must contain exactly M0-M5 targets; found {sorted(result)}")
    return result


def _readme_vector_after_marker(
    readme: str, marker: str, errors: list[str]
) -> tuple[str, ...] | None:
    pos = readme.find(marker)
    if pos < 0:
        errors.append(f"README missing vector marker: {marker}")
        return None
    tail = readme[pos + len(marker) :]
    block = re.search(
        r"```text\s*\nS1\s+S2\s+S3\s+S3\*\s+S4\s+S5\s*\n([^\n]+)\n```",
        tail,
    )
    if not block:
        errors.append(f"README missing six-state vector after marker: {marker}")
        return None
    return _normalize_vector(block.group(1), f"README {marker}", errors)


def _check_local_links(root: Path, errors: list[str]) -> None:
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0].strip("<>")
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"local Markdown link escapes repository: {path.relative_to(root)} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken local Markdown link: {path.relative_to(root)} -> {target}")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    readme = _read(root, "README.md", errors)
    control = _read(root, "CONTROL_PLANE.md", errors)
    roadmap = _read(root, "ROADMAP.md", errors)
    _read(root, "CONTRIBUTING.md", errors)
    _read(root, "roles/S1.md", errors)

    prompt_dir = root / "prompts"
    if not prompt_dir.is_dir() or not any(prompt_dir.glob("*.md")):
        errors.append("prompts/ must contain at least one Markdown prompt")

    if readme and control:
        in_scope = _repo_bullet_block(readme, "Current in-scope public repositories:", errors)
        out_scope = _repo_bullet_block(readme, "Explicitly outside this organizational scope:", errors)

        overlap = sorted(in_scope & out_scope)
        if overlap:
            errors.append(f"repositories cannot be both in scope and explicitly out of scope: {overlap}")

        expected_control_owned = in_scope - {"opensiro/vsm-oss-organization"}
        control_owned = set(
            re.findall(r"^- `(opensiro/[A-Za-z0-9_.-]+)` owns\b", control, re.MULTILINE)
        )
        if control_owned != expected_control_owned:
            errors.append(
                "CONTROL_PLANE source-of-truth ownership repository set drifts from README scope: "
                f"expected {sorted(expected_control_owned)}, found {sorted(control_owned)}"
            )

        outside_line = re.search(
            r"^- .* are outside this organizational scope even when ", control, re.MULTILINE
        )
        control_out_scope = set(REPO_PATTERN.findall(outside_line.group(0))) if outside_line else set()
        if control_out_scope != out_scope:
            errors.append(
                "CONTROL_PLANE explicit out-of-scope repository set drifts from README: "
                f"expected {sorted(out_scope)}, found {sorted(control_out_scope)}"
            )

        readme_pair = _active_pair_from_readme(readme, errors)
        control_pair = _active_pair_from_control(control, errors)
        if readme_pair and control_pair and readme_pair != control_pair:
            errors.append(
                f"active Profile/Methodology pair drifts: README={readme_pair}, CONTROL_PLANE={control_pair}"
            )

        if control_pair:
            release_profile = re.search(rf"Profile `{VERSION_PATTERN}` is tagged/released", control)
            release_methodology = re.search(rf"Methodology `{VERSION_PATTERN}` is tagged/released", control)
            index_active = re.search(
                rf"Index active contract is `Profile {VERSION_PATTERN} / Methodology {VERSION_PATTERN}`",
                control,
            )
            if not release_profile or release_profile.group(1) != control_pair[0]:
                errors.append("CONTROL_PLANE released Profile bullet drifts from active contract")
            if not release_methodology or release_methodology.group(1) != control_pair[1]:
                errors.append("CONTROL_PLANE released Methodology bullet drifts from active contract")
            if not index_active or index_active.groups() != control_pair:
                errors.append("CONTROL_PLANE Index active-contract bullet drifts from active contract")

    if readme and roadmap:
        correspondence = _roadmap_table_vectors(
            roadmap, "GitHub milestone correspondence", 2, errors
        )
        sequence = _roadmap_table_vectors(roadmap, "Milestone sequence", 1, errors)
        sections = _roadmap_section_vectors(roadmap, errors)
        for milestone in (f"M{i}" for i in range(6)):
            values = [mapping.get(milestone) for mapping in (correspondence, sequence, sections)]
            concrete = [value for value in values if value is not None]
            if concrete and any(value != concrete[0] for value in concrete[1:]):
                errors.append(
                    f"ROADMAP {milestone} target vector drifts across duplicated milestone surfaces: {values}"
                )

        current = _readme_vector_after_marker(readme, "Current milestone:", errors)
        final = _readme_vector_after_marker(readme, "Long-term reference target:", errors)
        if current and correspondence.get("M0") and current != correspondence["M0"]:
            errors.append(f"README current milestone vector drifts from ROADMAP M0: {current} != {correspondence['M0']}")
        if final and correspondence.get("M5") and final != correspondence["M5"]:
            errors.append(f"README long-term target vector drifts from ROADMAP M5: {final} != {correspondence['M5']}")

    _check_local_links(root, errors)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)

    errors = validate(args.root)
    if errors:
        print("Organization contract consistency FAILED:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        print(NON_SEMANTIC_NOTICE, file=sys.stderr)
        return 1

    print("Organization contract consistency OK.")
    print(NON_SEMANTIC_NOTICE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
