#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate import load_modules

REQUIRED = ["id", "name", "category", "status", "source", "origin", "source_post"]
VALID_STATUS = {"working", "partial", "not-working", "outdated", "needs-retest"}

def main():
    errors = []
    seen = set()
    for path in sorted((Path(__file__).resolve().parents[1] / "modules").glob("*.md")):
        try:
            m = __import__("generate").parse_frontmatter(path.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"{path}: {e}")
            continue
        for key in REQUIRED:
            if not m.get(key):
                errors.append(f"{path}: missing {key}")
        if m.get("status") not in VALID_STATUS:
            errors.append(f"{path}: invalid status {m.get('status')!r}")
        if m.get("id") in seen:
            errors.append(f"{path}: duplicate id {m.get('id')}")
        seen.add(m.get("id"))
    if errors:
        print("\n".join(errors))
        return 1
    print("Validation passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
