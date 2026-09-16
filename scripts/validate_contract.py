#!/usr/bin/env python3
"""Check deterministic repository-local Organization contract consistency."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_RE = re.compile(r"`(opensiro/[A-Za-z0-9_.-]+)`")
VERSION = r"([0-9]+\.[0-9]+\.[0-9]+)"
STATES = {"A", "C", "P", "—", "?"}
NON_SEMANTIC_NOTICE = (
    "Passing these checks establishes only repository-local deterministic "
    "consistency; it does not establish VSM semantics, function mapping, "
    "autonomous ownership, or S1=A."
)


def read(root: Path, relative: str, errors: list[str]) -> str:
    path = root / relative
    if not path.is_file():
        errors.append(f"missing required file: {relative}")
        return ""
    return path.read_text(encoding="utf-8")


def repo_block(text: str, marker: str, errors: list[str]) -> set[str]:
    pos = text.find(marker)
    if pos < 0:
        errors.append(f"README missing marker: {marker}")
        return set()
    repos: set[str] = set()
    started = False
    for raw in text[pos + len(marker) :].splitlines():
        line = raw.strip()
        if not line and not started:
            continue
        if line.startswith("- "):
            started = True
            match = REPO_RE.search(line)
            if match:
                repos.add(match.group(1))
            continue
        if started:
            break
    if not repos:
        errors.append(f"no repository entries found after marker: {marker}")
    return repos


def readme_pair(text: str, errors: list[str]) -> tuple[str, str] | None:
    profile = re.search(
        rf"Normative VSM semantics:\s*`opensiro/vsm-harness-profile`\s*`{VERSION}`",
        text,
    )
    methodology = re.search(
        rf"`opensiro/vsm-harness-skills`\s+Methodology\s+`{VERSION}`", text
    )
    if not profile:
        errors.append("README active Profile version reference is missing or malformed")
    if not methodology:
        errors.append("README active Methodology version reference is missing or malformed")
    if not profile or not methodology:
        return None
    return profile.group(1), methodology.group(1)


def control_pair(text: str, errors: list[str]) -> tuple[str, str] | None:
    match = re.search(
        rf"^\|\s*active contract for new work\s*\|\s*`{VERSION}`\s*\|\s*`{VERSION}`\s*\|",
        text,
        re.MULTILINE,
    )
    if not match:
        errors.append("CONTROL_PLANE active-contract table row is missing or malformed")
        return None
    return match.group(1), match.group(2)


def vector(raw: str, context: str, errors: list[str]) -> tuple[str, ...] | None:
    result = tuple(raw.replace("`", "").split())
    if len(result) != 6 or any(item not in STATES for item in result):
        errors.append(f"invalid six-state milestone vector in {context}: {raw!r}")
        return None
    return result


def roadmap_table(
    text: str, heading: str, column: int, errors: list[str]
) -> dict[str, tuple[str, ...]]:
    start = re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE)
    if not start:
        errors.append(f"ROADMAP missing section: {heading}")
        return {}
    tail = text[start.end() :]
    end = re.search(r"^## ", tail, re.MULTILINE)
    section = tail[: end.start()] if end else tail
    result: dict[str, tuple[str, ...]] = {}
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) <= column:
            continue
        milestone = re.search(r"\b(M[0-5])\b", cells[0])
        if milestone:
            parsed = vector(cells[column], f"ROADMAP {heading} {milestone.group(1)}", errors)
            if parsed:
                result[milestone.group(1)] = parsed
    expected = {f"M{i}" for i in range(6)}
    if set(result) != expected:
        errors.append(f"ROADMAP {heading} must contain exactly M0-M5 vectors; found {sorted(result)}")
    return result


def roadmap_sections(text: str, errors: list[str]) -> dict[str, tuple[str, ...]]:
    result: dict[str, tuple[str, ...]] = {}
    for match in re.finditer(
        r"^## (M[0-5]) —[^\n]+\n\nTarget:\s*`([^`]+)`", text, re.MULTILINE
    ):
        parsed = vector(match.group(2), f"ROADMAP {match.group(1)} section", errors)
        if parsed:
            result[match.group(1)] = parsed
    expected = {f"M{i}" for i in range(6)}
    if set(result) != expected:
        errors.append(f"ROADMAP milestone sections must contain exactly M0-M5 targets; found {sorted(result)}")
    return result


def readme_vector(
    text: str, markers: tuple[str, ...], context: str, errors: list[str]
) -> tuple[str, ...] | None:
    found = [(marker, text.find(marker)) for marker in markers if marker in text]
    if not found:
        errors.append(f"README missing {context} vector marker; accepted markers: {markers}")
        return None
    if len(found) > 1:
        errors.append(f"README has multiple {context} vector markers: {[item[0] for item in found]}")
        return None
    marker, pos = found[0]
    block = re.search(
        r"```text\s*\nS1\s+S2\s+S3\s+S3\*\s+S4\s+S5\s*\n([^\n]+)\n```",
        text[pos + len(marker) :],
    )
    if not block:
        errors.append(f"README missing six-state vector after {context} marker: {marker}")
        return None
    return vector(block.group(1), f"README {context}", errors)


def check_links(root: Path, errors: list[str]) -> None:
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0].strip("<>")
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(f"local Markdown link escapes repository: {path.relative_to(root)} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken local Markdown link: {path.relative_to(root)} -> {target}")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    readme = read(root, "README.md", errors)
    control = read(root, "CONTROL_PLANE.md", errors)
    roadmap = read(root, "ROADMAP.md", errors)
    read(root, "CONTRIBUTING.md", errors)
    read(root, "roles/S1.md", errors)

    prompts = root / "prompts"
    if not prompts.is_dir() or not any(prompts.glob("*.md")):
        errors.append("prompts/ must contain at least one Markdown prompt")

    if readme and control:
        in_scope = repo_block(readme, "Current in-scope public repositories:", errors)

        expected_owned = in_scope - {"opensiro/vsm-oss-organization"}
        actual_owned = set(re.findall(r"^- `(opensiro/[A-Za-z0-9_.-]+)` owns\b", control, re.MULTILINE))
        if actual_owned != expected_owned:
            errors.append(
                "CONTROL_PLANE source-of-truth ownership repository set drifts from README scope: "
                f"expected {sorted(expected_owned)}, found {sorted(actual_owned)}"
            )

        rp, cp = readme_pair(readme, errors), control_pair(control, errors)
        if rp and cp and rp != cp:
            errors.append(f"active Profile/Methodology pair drifts: README={rp}, CONTROL_PLANE={cp}")
        if cp:
            profile = re.search(rf"Profile `{VERSION}` is tagged/released", control)
            method = re.search(rf"Methodology `{VERSION}` is tagged/released", control)
            index = re.search(rf"Index active contract is `Profile {VERSION} / Methodology {VERSION}`", control)
            if not profile or profile.group(1) != cp[0]:
                errors.append("CONTROL_PLANE released Profile bullet drifts from active contract")
            if not method or method.group(1) != cp[1]:
                errors.append("CONTROL_PLANE released Methodology bullet drifts from active contract")
            if not index or index.groups() != cp:
                errors.append("CONTROL_PLANE Index active-contract bullet drifts from active contract")

    if readme and roadmap:
        correspondence = roadmap_table(roadmap, "GitHub milestone correspondence", 2, errors)
        sequence = roadmap_table(roadmap, "Milestone sequence", 1, errors)
        sections = roadmap_sections(roadmap, errors)
        for milestone in (f"M{i}" for i in range(6)):
            values = [mapping.get(milestone) for mapping in (correspondence, sequence, sections)]
            concrete = [item for item in values if item is not None]
            if concrete and any(item != concrete[0] for item in concrete[1:]):
                errors.append(f"ROADMAP {milestone} target vector drifts across duplicated milestone surfaces: {values}")

        current = readme_vector(
            readme,
            ("Current milestone target:", "Current milestone:"),
            "current milestone",
            errors,
        )
        final = readme_vector(readme, ("Long-term reference target:",), "long-term reference target", errors)
        if current and correspondence.get("M0") and current != correspondence["M0"]:
            errors.append(f"README current milestone vector drifts from ROADMAP M0: {current} != {correspondence['M0']}")
        if final and correspondence.get("M5") and final != correspondence["M5"]:
            errors.append(f"README long-term target vector drifts from ROADMAP M5: {final} != {correspondence['M5']}")

    check_links(root, errors)
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
