#!/usr/bin/env python3
"""Read-only structural checks. These checks do not assess scientific behavior."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def check(root: Path) -> list[str]:
    errors = []
    required = [
        "SKILL.md", "agents/openai.yaml", "README.md", "README.zh-CN.md",
        "LICENSE", "references/design.md", "references/evidence.md",
        "references/execution.md", "references/state.md", "templates/stage-record.md",
        "evals/README.md", "evals/rubric.md", "evals/results/v0.1.0.md",
    ]
    for rel in required:
        if not (root / rel).is_file():
            errors.append(f"Missing file: {rel}")
    entry = root / "SKILL.md"
    if entry.exists():
        text = entry.read_text()
        parts = text.split("---", 2)
        if not text.startswith("---\n") or len(parts) != 3:
            errors.append("SKILL.md must start with YAML frontmatter.")
        else:
            header = parts[1]
            if not re.search(r"(?m)^name: research-pipeline$", header):
                errors.append("Skill name must be research-pipeline.")
            if not re.search(r"(?m)^description: .+", header):
                errors.append("Description is missing.")
        if "[TODO:" in text:
            errors.append("Unfinished initializer placeholder in SKILL.md.")
    meta = root / "agents" / "openai.yaml"
    if meta.exists() and not re.search(r"(?m)^  allow_implicit_invocation: true$", meta.read_text()):
        errors.append("Automatic invocation must be enabled for this package.")
    for path in root.rglob("*.md"):
        if any(p in {".git", "work", "outputs", "runs"} for p in path.relative_to(root).parts):
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
            target = target.strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            local = unquote(target.split("#", 1)[0])
            resolved = (path.parent / local).resolve()
            if not resolved.is_relative_to(root.resolve()):
                errors.append(f"Link escapes package in {path.relative_to(root)}: {target}")
            elif not resolved.exists():
                errors.append(f"Broken local link in {path.relative_to(root)}: {target}")
    return errors


if __name__ == "__main__":
    issues = check(ROOT)
    for issue in issues:
        print(issue, file=sys.stderr)
    if issues:
        raise SystemExit(1)
    print("PASS: package files, metadata and local links; behavior is evaluated separately.")
