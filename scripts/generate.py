#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
MODULES_DIR = ROOT / "modules"
DATA_DIR = ROOT / "data"
README_FILE = ROOT / "README.md"
JSON_FILE = DATA_DIR / "modules.json"

STATUS = {
    "working": "🟢 Working",
    "partial": "🟡 Partial",
    "not-working": "🔴 Not Working",
    "outdated": "🟠 Outdated",
    "needs-retest": "⚪ Needs Retest",
}

STATUS_ORDER = ["working", "partial", "not-working", "outdated", "needs-retest"]

def parse_frontmatter(text):
    if not text.startswith("---"):
        raise ValueError("Missing frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Invalid frontmatter")
    data = {}
    for line in parts[1].strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        if value.lower() == "null":
            value = None
        data[key] = value
    return data

def load_modules():
    result = []
    for file in sorted(MODULES_DIR.glob("*.md")):
        data = parse_frontmatter(file.read_text(encoding="utf-8"))
        data["_file"] = str(file.relative_to(ROOT))
        result.append(data)
    return result

def clean_cell(value):
    return str(value or "").replace("|", "\\|").replace("\n", " ")

def module_link(module):
    name = clean_cell(module["name"])
    source = module.get("source")
    return f"[{name}]({source})" if source else name

def generate_json(modules):
    DATA_DIR.mkdir(exist_ok=True)
    output = [{k:v for k,v in m.items() if not k.startswith("_")} for m in modules]
    JSON_FILE.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def generate_readme(modules):
    lines = [
        "# Temporal Root Modules List", "",
        "Community-maintained compatibility list for modules and tools tested with Temporal Root.", "",
        "> Compatibility can vary depending on the device, ROM, Android version, Temporal Root version, module version, and other installed software.", "",
        "## Status", "",
        "| Status | Meaning |", "|---|---|",
        "| 🟢 Working | Confirmed working |",
        "| 🟡 Partial | Partially working or has limitations |",
        "| 🔴 Not Working | Confirmed not working |",
        "| 🟠 Outdated | Marked outdated |",
        "| ⚪ Needs Retest | Requires a new test |", ""
    ]
    for status in STATUS_ORDER:
        items = [m for m in modules if m.get("status") == status]
        if not items: continue
        lines += [f"## {STATUS[status]}", ""]
        cats = {}
        for m in items:
            cats.setdefault(m.get("category", "Other"), []).append(m)
        for category in sorted(cats):
            lines += [f"### {category}", "", "| Module | Notes |", "|---|---|"]
            for m in sorted(cats[category], key=lambda x: x.get("name","").lower()):
                notes = m.get("warning") or m.get("notes") or ""
                lines.append(f"| {module_link(m)} | {clean_cell(notes)} |")
            lines.append("")
    lines += [
        "## Find New Modules", "",
        "Looking for modules to test with Temporal Root? These sources can help you discover new modules and projects:", "",
        "- [GitDroid](https://t.me/gitdroid)",
        "- [Xposed Modules](https://rushiranpise.github.io/xposed-modules/)",
        "- [Shizuku Modules](https://rushiranpise.github.io/shizuku-modules/)",
        "- [LSPosed Modules Repository](https://modules.lsposed.org/)",
        "- [Magisk Modules Repo](https://github.com/magisk-modules-repo)",
        "- [Magisk Modules Alt Repo](https://github.com/Magisk-Modules-Alt-Repo/)",
        "- [Androidacy Magisk Modules Repository](https://www.androidacy.com/magisk-modules-repository/)",
        "- [Yuki](https://github.com/carlelieser/yuki)",
        "- [ShizuCoreFetch](https://github.com/elhizazi1/ShizuCoreFetch)",
        "",
        "These are discovery sources only. A module should be tested with Temporal Root before being added to this list.", "",
        "## Add a Module", "",
        "Found a module that you tested with Temporal Root?", "",
        "Create a new module file in `modules/` and submit a pull request.", "",
        "See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the required format.", "",
        "## Update a Module", "",
        "If compatibility changes, submit a pull request with the new test result and environment details.", "",
        "## Source", "",
        "The initial module list was imported from the [XDA Developers Temporal Root testing thread](https://xdaforums.com/t/list-of-modules-working-on-temporal-root.4796105/).", ""
    ]
    README_FILE.write_text("\n".join(lines), encoding="utf-8")

def main():
    modules = load_modules()
    if not modules:
        raise SystemExit("No module files found.")
    generate_json(modules)
    generate_readme(modules)
    print(f"Generated README.md and data/modules.json from {len(modules)} module files.")

if __name__ == "__main__":
    main()
