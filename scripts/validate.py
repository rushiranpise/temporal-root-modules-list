#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MODULES_DIR = ROOT / "modules"

def parse_frontmatter(text):
    if not text.startswith("---"):
        raise ValueError("Missing frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Invalid frontmatter")
    data = {}
    for line in parts[1].strip().splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        data[key.strip()] = value
    return data

REQUIRED = ["id", "name", "category", "status", "source", "origin", "source_post"]
VALID_STATUS = {"working", "partial", "not-working", "outdated", "needs-retest"}

def main():
    errors = []
    seen_ids = {}
    seen_names = {}

    for path in sorted(MODULES_DIR.glob("*.md")):
        try:
            m = parse_frontmatter(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path}: {exc}")
            continue

        for key in REQUIRED:
            if not m.get(key):
                errors.append(f"{path}: missing {key}")

        if m.get("status") not in VALID_STATUS:
            errors.append(f"{path}: invalid status {m.get('status')!r}")

        module_id = m.get("id")
        module_name = m.get("name")

        if module_id in seen_ids:
            errors.append(f"{path}: duplicate id {module_id!r}; already used by {seen_ids[module_id]}")
        else:
            seen_ids[module_id] = str(path)

        if module_name in seen_names:
            errors.append(f"{path}: duplicate name {module_name!r}; already used by {seen_names[module_name]}")
        else:
            seen_names[module_name] = str(path)

    if errors:
        print("\n".join(errors))
        return 1

    print(f"Validation passed: {len(seen_ids)} unique modules.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
