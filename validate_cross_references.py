#!/usr/bin/env python3
"""Validate cross-document requirement and source references.

Checks:
- requirements_matrix.md contains exactly PBI-001..PBI-055
- every Source_ID used by the matrix exists in references.md
- active PBI mappings in rules.yaml use only IDs defined by the matrix
- validation fixtures under explicitly_rejected_examples are ignored
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:
    raise SystemExit(
        "Missing dependency: PyYAML. Install it with: python3 -m pip install pyyaml"
    ) from exc


ROOT = Path(__file__).resolve().parent
MATRIX_PATH = ROOT / "docs/microsoft/requirements_matrix.md"
REFERENCES_PATH = ROOT / "docs/microsoft/references.md"
RULES_PATH = ROOT / "rules.yaml"

PBI_PATTERN = re.compile(r"\bPBI-\d{3}\b")
SOURCE_PATTERN = re.compile(r"\bMS-[A-Z]+-\d{2}\b")
EXPECTED_IDS = {f"PBI-{number:03d}" for number in range(1, 56)}
IGNORED_KEYS = {"explicitly_rejected_examples"}


def read_text(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def collect_active_rule_ids(value: Any, parent_key: str | None = None) -> set[str]:
    """Recursively collect PBI IDs, excluding validation-only fixtures."""
    if parent_key in IGNORED_KEYS:
        return set()

    if isinstance(value, dict):
        found: set[str] = set()
        for key, child in value.items():
            found.update(collect_active_rule_ids(child, str(key)))
        return found

    if isinstance(value, list):
        found: set[str] = set()
        for child in value:
            found.update(collect_active_rule_ids(child, parent_key))
        return found

    if isinstance(value, str):
        return set(PBI_PATTERN.findall(value))

    return set()


def main() -> int:
    matrix_text = read_text(MATRIX_PATH)
    references_text = read_text(REFERENCES_PATH)
    rules_text = read_text(RULES_PATH)

    matrix_ids = set(PBI_PATTERN.findall(matrix_text))
    missing_matrix_ids = sorted(EXPECTED_IDS - matrix_ids)
    unexpected_matrix_ids = sorted(matrix_ids - EXPECTED_IDS)

    referenced_source_ids = set(SOURCE_PATTERN.findall(matrix_text))
    registered_source_ids = set(
        re.findall(
            r"^\|\s*(MS-[A-Z]+-\d{2})\s*\|",
            references_text,
            re.MULTILINE,
        )
    )
    missing_sources = sorted(referenced_source_ids - registered_source_ids)

    try:
        rules_data = yaml.safe_load(rules_text)
    except yaml.YAMLError as exc:
        print(f"rules_yaml_parse_error: {exc}")
        return 1

    active_rule_ids = collect_active_rule_ids(rules_data)
    unknown_rule_ids = sorted(active_rule_ids - EXPECTED_IDS)

    checks = {
        "missing_matrix_ids": missing_matrix_ids,
        "unexpected_matrix_ids": unexpected_matrix_ids,
        "missing_source_registry_entries": missing_sources,
        "unknown_active_rules_yaml_ids": unknown_rule_ids,
    }

    failed = False
    for name, values in checks.items():
        print(f"{name}: {values or 'OK'}")
        failed = failed or bool(values)

    if failed:
        return 1

    print("Cross-document validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
