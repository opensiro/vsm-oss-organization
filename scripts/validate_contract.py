#!/usr/bin/env python3
"""Check Organization-local and upstream contract consistency."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_RE = re.compile(r"`(opensiro/[A-Za-z0-9_.-]+)`")
VERSION_RE = re.compile(r"^(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
STATES = {"A", "C", "P", "—", "?"}
SOURCE_KINDS = {"release", "commit", "branch"}
NON_SEMANTIC_NOTICE = (
    "Passing these checks establishes only deterministic contract consistency; "
    "it does not establish VSM semantics, function mapping, autonomous ownership, or S1=A."
)


def read(root: Path, relative: str, errors: list[str]) -> str:
    path = root / relative
    if not path.is_file():
        errors.append(f"missing required file: {relative}")
        return ""
    return path.read_text(encoding="utf-8")


def load_json(path: Path, context: str, errors: list[str]) -> dict | None:
    if not path.is_file():
        errors.append(f"missing required file: {path.name}")
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{context}: invalid JSON: {exc}")
        return None
    if not isinstance(data, dict):
        errors.append(f"{context}: expected a JSON object")
        return None
    return data


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
            parsed = vector(
                cells[column], f"ROADMAP {heading} {milestone.group(1)}", errors
            )
            if parsed:
                result[milestone.group(1)] = parsed
    expected = {f"M{i}" for i in range(6)}
    if set(result) != expected:
        errors.append(
            f"ROADMAP {heading} must contain exactly M0-M5 vectors; found {sorted(result)}"
        )
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
        errors.append(
            f"ROADMAP milestone sections must contain exactly M0-M5 targets; found {sorted(result)}"
        )
    return result


def readme_vector(
    text: str, markers: tuple[str, ...], context: str, errors: list[str]
) -> tuple[str, ...] | None:
    found = [(marker, text.find(marker)) for marker in markers if marker in text]
    if not found:
        errors.append(
            f"README missing {context} vector marker; accepted markers: {markers}"
        )
        return None
    if len(found) > 1:
        errors.append(
            f"README has multiple {context} vector markers: {[item[0] for item in found]}"
        )
        return None
    marker, pos = found[0]
    block = re.search(
        r"```text\s*\nS1\s+S2\s+S3\s+S3\*\s+S4\s+S5\s*\n([^\n]+)\n```",
        text[pos + len(marker) :],
    )
    if not block:
        errors.append(
            f"README missing six-state vector after {context} marker: {marker}"
        )
        return None
    return vector(block.group(1), f"README {context}", errors)


def check_links(root: Path, errors: list[str]) -> None:
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        for target in re.findall(
            r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")
        ):
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
                errors.append(
                    f"local Markdown link escapes repository: {path.relative_to(root)} -> {target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"broken local Markdown link: {path.relative_to(root)} -> {target}"
                )


def load_upstream_contract(root: Path, errors: list[str]) -> dict | None:
    path = root / "UPSTREAM_CONTRACT.json"
    data = load_json(path, "UPSTREAM_CONTRACT.json", errors)
    if data is None:
        return None

    expected_sections = {"profile", "methodology", "index"}
    if set(data) != expected_sections:
        errors.append(
            "UPSTREAM_CONTRACT.json: expected exactly profile/methodology/index sections"
        )
        return data

    for section in expected_sections:
        item = data.get(section)
        if not isinstance(item, dict):
            errors.append(f"UPSTREAM_CONTRACT.json: {section} must be an object")
            continue
        for key in ("repository", "source_kind", "ref"):
            if not isinstance(item.get(key), str) or not item[key]:
                errors.append(
                    f"UPSTREAM_CONTRACT.json: {section}.{key} must be a non-empty string"
                )
        if item.get("source_kind") not in SOURCE_KINDS:
            errors.append(
                f"UPSTREAM_CONTRACT.json: {section}.source_kind must be one of {sorted(SOURCE_KINDS)}"
            )

    profile = data.get("profile", {})
    methodology = data.get("methodology", {})
    index = data.get("index", {})

    for section, item in (("profile", profile), ("methodology", methodology)):
        version = item.get("version")
        if not isinstance(version, str) or not VERSION_RE.fullmatch(version):
            errors.append(
                f"UPSTREAM_CONTRACT.json: {section}.version must be Semantic Version"
            )
        version_path = item.get("version_path")
        if not isinstance(version_path, str) or not version_path:
            errors.append(
                f"UPSTREAM_CONTRACT.json: {section}.version_path must be a non-empty string"
            )

    if profile.get("source_kind") == "release":
        expected_ref = f"v{profile.get('version', '')}"
        if profile.get("ref") != expected_ref:
            errors.append(
                f"UPSTREAM_CONTRACT.json: released Profile ref must be {expected_ref!r}"
            )
    for key in ("consumer_contract_path", "release_impact_path"):
        if not isinstance(profile.get(key), str) or not profile[key]:
            errors.append(
                f"UPSTREAM_CONTRACT.json: profile.{key} must be a non-empty string"
            )

    if methodology.get("source_kind") == "release":
        expected_ref = f"v{methodology.get('version', '')}"
        if methodology.get("ref") != expected_ref:
            errors.append(
                f"UPSTREAM_CONTRACT.json: released Methodology ref must be {expected_ref!r}"
            )
    elif methodology.get("source_kind") == "commit":
        ref = methodology.get("ref")
        if not isinstance(ref, str) or not SHA_RE.fullmatch(ref):
            errors.append(
                "UPSTREAM_CONTRACT.json: commit-pinned Methodology ref must be a 40-hex SHA"
            )

    active_contract_path = index.get("active_contract_path")
    if not isinstance(active_contract_path, str) or not active_contract_path:
        errors.append(
            "UPSTREAM_CONTRACT.json: index.active_contract_path must be a non-empty string"
        )

    return data


def check_manifest_references(readme: str, control: str, errors: list[str]) -> None:
    for name, text in (("README.md", readme), ("CONTROL_PLANE.md", control)):
        if "UPSTREAM_CONTRACT.json" not in text:
            errors.append(f"{name}: must reference UPSTREAM_CONTRACT.json")
    if re.search(
        r"Normative VSM semantics:\s*`opensiro/vsm-harness-profile`\s*`\d+\.\d+\.\d+`",
        readme,
    ):
        errors.append(
            "README.md: active Profile version must come from UPSTREAM_CONTRACT.json, not a duplicated source-boundary literal"
        )
    if re.search(
        r"`opensiro/vsm-harness-skills`\s+Methodology\s+`\d+\.\d+\.\d+`",
        readme,
    ):
        errors.append(
            "README.md: active Methodology version must come from UPSTREAM_CONTRACT.json, not a duplicated source-boundary literal"
        )
    if re.search(r"^\|\s*active contract for new work\s*\|", control, re.MULTILINE):
        errors.append(
            "CONTROL_PLANE.md: do not maintain a second active-contract version table"
        )


def parse_index_contract(text: str, errors: list[str]) -> tuple[str, str] | None:
    rows = [line.strip() for line in text.splitlines() if line.strip()]
    if len(rows) != 2 or rows[0] != "profile_version|methodology_version":
        errors.append(
            "Index active contract: expected profile_version|methodology_version header and one data row"
        )
        return None
    cells = rows[1].split("|")
    if len(cells) != 2 or any(not VERSION_RE.fullmatch(cell) for cell in cells):
        errors.append("Index active contract: malformed version pair")
        return None
    return cells[0], cells[1]


def release_path(
    release_impact: dict,
    start_version: str,
    target_version: str,
    errors: list[str],
) -> list[dict] | None:
    releases = release_impact.get("releases")
    if not isinstance(releases, list):
        errors.append("Profile RELEASE_IMPACT.json: releases must be an array")
        return None

    by_version: dict[str, dict] = {}
    for item in releases:
        if not isinstance(item, dict):
            errors.append(
                "Profile RELEASE_IMPACT.json: each release entry must be an object"
            )
            continue
        version = item.get("version")
        if isinstance(version, str):
            by_version[version] = item

    if target_version == start_version:
        return []
    if target_version not in by_version:
        errors.append(
            f"Profile RELEASE_IMPACT.json: selected Profile {target_version} is missing"
        )
        return None

    path: list[dict] = []
    current = target_version
    seen: set[str] = set()
    while current != start_version:
        if current in seen:
            errors.append("Profile RELEASE_IMPACT.json: release chain contains a cycle")
            return None
        seen.add(current)
        item = by_version.get(current)
        if item is None:
            errors.append(
                f"Profile RELEASE_IMPACT.json: cannot reconstruct path from {start_version} to {target_version}; missing {current}"
            )
            return None
        path.append(item)
        previous = item.get("previous")
        if not isinstance(previous, str) or previous == "baseline":
            errors.append(
                f"Profile RELEASE_IMPACT.json: cannot reconstruct path from {start_version} to {target_version}"
            )
            return None
        current = previous

    path.reverse()
    return path


def check_upstream_contract(
    manifest: dict,
    profile_root: Path,
    methodology_root: Path,
    index_root: Path,
    errors: list[str],
) -> None:
    profile = manifest["profile"]
    methodology = manifest["methodology"]
    index = manifest["index"]

    profile_version = read(profile_root, profile["version_path"], errors).strip()
    if profile_version and profile_version != profile["version"]:
        errors.append(
            f"Profile upstream version drift: selected {profile['version']}, checked-out source reports {profile_version}"
        )

    consumer_contract = profile_root / profile["consumer_contract_path"]
    if not consumer_contract.is_file():
        errors.append(
            f"Profile upstream missing consumer contract: {profile['consumer_contract_path']}"
        )

    impact_path = profile_root / profile["release_impact_path"]
    impact = load_json(impact_path, "Profile RELEASE_IMPACT.json", errors)
    if impact is not None:
        if impact.get("profile") != profile["repository"]:
            errors.append(
                "Profile RELEASE_IMPACT.json: profile repository identity does not match Organization selection"
            )
        releases = impact.get("releases")
        if isinstance(releases, list):
            selected = [
                item
                for item in releases
                if isinstance(item, dict) and item.get("version") == profile["version"]
            ]
            if len(selected) != 1:
                errors.append(
                    f"Profile RELEASE_IMPACT.json: expected exactly one entry for selected Profile {profile['version']}"
                )

    methodology_version = read(
        methodology_root, methodology["version_path"], errors
    ).strip()
    if methodology_version and methodology_version != methodology["version"]:
        errors.append(
            f"Methodology upstream version drift: selected {methodology['version']}, checked-out source reports {methodology_version}"
        )

    index_contract_text = read(index_root, index["active_contract_path"], errors)
    pair = parse_index_contract(index_contract_text, errors) if index_contract_text else None
    if pair is None:
        return
    index_profile, index_methodology = pair

    if index_methodology != methodology["version"]:
        errors.append(
            "Index active Methodology does not match Organization selection: "
            f"Index={index_methodology}, Organization={methodology['version']}"
        )

    if impact is None:
        return
    path = release_path(impact, index_profile, profile["version"], errors)
    if path is None:
        return
    for transition in path:
        version = transition.get("version", "?")
        compatibility = transition.get("compatibility")
        assessment_impact = transition.get("assessment_impact")
        if compatibility != "compatible" or assessment_impact != "none":
            errors.append(
                "Profile compatibility review required before silent Organization adoption: "
                f"transition to {version} is compatibility={compatibility!r}, "
                f"assessment_impact={assessment_impact!r}"
            )


def validate(
    root: Path,
    *,
    profile_root: Path | None = None,
    methodology_root: Path | None = None,
    index_root: Path | None = None,
) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    readme = read(root, "README.md", errors)
    control = read(root, "CONTROL_PLANE.md", errors)
    roadmap = read(root, "ROADMAP.md", errors)
    read(root, "CONTRIBUTING.md", errors)
    read(root, "roles/S1.md", errors)
    manifest = load_upstream_contract(root, errors)

    prompts = root / "prompts"
    if not prompts.is_dir() or not any(prompts.glob("*.md")):
        errors.append("prompts/ must contain at least one Markdown prompt")

    if readme and control:
        in_scope = repo_block(readme, "Current in-scope public repositories:", errors)
        expected_owned = in_scope - {"opensiro/vsm-oss-organization"}
        actual_owned = set(
            re.findall(
                r"^- `(opensiro/[A-Za-z0-9_.-]+)` owns\b", control, re.MULTILINE
            )
        )
        if actual_owned != expected_owned:
            errors.append(
                "CONTROL_PLANE source-of-truth ownership repository set drifts from README scope: "
                f"expected {sorted(expected_owned)}, found {sorted(actual_owned)}"
            )
        check_manifest_references(readme, control, errors)

    if readme and roadmap:
        correspondence = roadmap_table(
            roadmap, "GitHub milestone correspondence", 2, errors
        )
        sequence = roadmap_table(roadmap, "Milestone sequence", 1, errors)
        sections = roadmap_sections(roadmap, errors)
        for milestone in (f"M{i}" for i in range(6)):
            values = [
                mapping.get(milestone)
                for mapping in (correspondence, sequence, sections)
            ]
            concrete = [item for item in values if item is not None]
            if concrete and any(item != concrete[0] for item in concrete[1:]):
                errors.append(
                    f"ROADMAP {milestone} target vector drifts across duplicated milestone surfaces: {values}"
                )

        current = readme_vector(
            readme,
            ("Current milestone target:", "Current milestone:"),
            "current milestone",
            errors,
        )
        final = readme_vector(
            readme,
            ("Long-term reference target:",),
            "long-term reference target",
            errors,
        )
        if current and correspondence.get("M0") and current != correspondence["M0"]:
            errors.append(
                f"README current milestone vector drifts from ROADMAP M0: {current} != {correspondence['M0']}"
            )
        if final and correspondence.get("M5") and final != correspondence["M5"]:
            errors.append(
                f"README long-term target vector drifts from ROADMAP M5: {final} != {correspondence['M5']}"
            )

    roots = (profile_root, methodology_root, index_root)
    if any(item is not None for item in roots) and not all(item is not None for item in roots):
        errors.append(
            "upstream validation requires --profile-root, --methodology-root, and --index-root together"
        )
    elif manifest is not None and all(item is not None for item in roots):
        check_upstream_contract(
            manifest,
            profile_root.resolve(),
            methodology_root.resolve(),
            index_root.resolve(),
            errors,
        )

    check_links(root, errors)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--profile-root", type=Path)
    parser.add_argument("--methodology-root", type=Path)
    parser.add_argument("--index-root", type=Path)
    args = parser.parse_args(argv)
    errors = validate(
        args.root,
        profile_root=args.profile_root,
        methodology_root=args.methodology_root,
        index_root=args.index_root,
    )
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
