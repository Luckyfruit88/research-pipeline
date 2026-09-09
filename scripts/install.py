#!/usr/bin/env python3
"""Install runtime files and optionally add a scoped Codex default. No network."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import tempfile
import unicodedata
import uuid

NAME = "research-pipeline"
RUNTIME = ("SKILL.md", "agents", "references", "templates", "LICENSE")
START = "<!-- research-pipeline:default:start -->"
END = "<!-- research-pipeline:default:end -->"
RECEIPT = ".research-pipeline-install.json"


class InstallError(RuntimeError):
    pass


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def path_key(path: Path) -> tuple[str, ...]:
    # Conservatively reject case/Unicode aliases even on case-sensitive volumes.
    # resolve() alone does not canonicalize casing on macOS.
    return tuple(unicodedata.normalize("NFC", part).casefold() for part in path.resolve().parts)


def same_entry(left: Path, right: Path) -> bool:
    try:
        if left.samefile(right):
            return True
    except (FileNotFoundError, NotADirectoryError):
        pass
    return path_key(left) == path_key(right)


def paths_overlap(left: Path, right: Path) -> bool:
    a, b = path_key(left), path_key(right)
    return a[:len(b)] == b or b[:len(a)] == a


def payload(source: Path) -> dict[str, str]:
    files = {}
    for name in RUNTIME:
        top = source / name
        if not top.exists():
            raise InstallError(f"Missing runtime path: {name}")
        paths = [top, *top.rglob("*")] if top.is_dir() else [top]
        for path in paths:
            if path.is_symlink():
                raise InstallError(f"Runtime symlinks are not supported: {path}")
            if path.is_file():
                files[path.relative_to(source).as_posix()] = digest(path)
    return dict(sorted(files.items()))


def installed_payload(target: Path) -> dict[str, str]:
    files = {}
    for path in target.rglob("*"):
        if path.is_symlink():
            raise InstallError(f"Existing installation contains a symlink: {path}")
        if path.is_file() and path.relative_to(target).as_posix() != RECEIPT:
            files[path.relative_to(target).as_posix()] = digest(path)
    return dict(sorted(files.items()))


def marker_range(text: str) -> tuple[int, int] | None:
    starts, ends = text.count(START), text.count(END)
    if not starts and not ends:
        return None
    if starts != 1 or ends != 1 or text.index(END) < text.index(START):
        raise InstallError("Malformed or duplicated default markers; preserve the file and repair them first.")
    return text.index(START), text.index(END) + len(END)


def default_text(original: bytes | None, skill: Path, remove: bool = False) -> bytes:
    text = "" if original is None else original.decode("utf-8")
    bounds = marker_range(text)
    if remove:
        return (text if bounds is None else text[:bounds[0]] + text[bounds[1]:]).encode("utf-8")
    path = json.dumps(str(skill / "SKILL.md"), ensure_ascii=False)
    block = (
        f"{START}\n"
        "## Default computational research workflow\n\n"
        "For research design, study/experiment planning, scientific feasibility, "
        "and building, evaluating or repairing research pipelines, use $research-pipeline by default.\n"
        f"Read the skill at {path} and only its relevant references.\n"
        "Honor the current user/project scope, later stage authorizations and existing evidence. "
        "Keep engineering, scientific and authorization judgments separate. "
        "Complete authorized nonblocked work; do not repeatedly ask for already-granted permission.\n"
        "Do not apply this default to standalone factual lookups, translation or prose-only edits.\n"
        f"{END}"
    )
    if bounds:
        return (text[:bounds[0]] + block + text[bounds[1]:]).encode("utf-8")
    return (text + ("\n" if not text or text.endswith("\n") else "\n\n") + block + "\n").encode("utf-8")


def backup_path(path: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return path.with_name(f"{path.name}.backup-{stamp}-{uuid.uuid4().hex[:8]}")


def read_agents(path: Path) -> bytes | None:
    if path.is_symlink():
        raise InstallError(f"Refusing to replace a symlinked AGENTS file: {path}")
    if path.exists() and not path.is_file():
        raise InstallError(f"AGENTS path is not a file: {path}")
    return path.read_bytes() if path.exists() else None


def write_agents(path: Path, expected: bytes | None, updated: bytes) -> str | None:
    if read_agents(path) != expected:
        raise InstallError("AGENTS.md changed during installation; retry after reviewing the new file.")
    if expected == updated:
        return None
    path.parent.mkdir(parents=True, exist_ok=True)
    backup = None
    if expected is not None:
        backup = backup_path(path)
        shutil.copy2(path, backup)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o600
    fd, tmp = tempfile.mkstemp(prefix=".research-pipeline-agents-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as out:
            out.write(updated)
            out.flush()
            os.fsync(out.fileno())
        os.chmod(tmp, mode)
        if read_agents(path) != expected:
            raise InstallError("AGENTS.md changed before commit; existing contents were preserved.")
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    return str(backup) if backup else None


def install(source: Path, skill_home: Path, agents_file: Path, *,
            set_default: bool = False, replace: bool = False,
            dry_run: bool = False) -> dict:
    source = source.resolve()
    target = skill_home.expanduser().resolve() / NAME
    agents_file = agents_file.expanduser().absolute()
    files = payload(source)
    if set_default and paths_overlap(agents_file, target):
        raise InstallError("AGENTS.md and the skill installation must not overlap; no changes made.")
    if set_default and any(same_entry(agents_file, source / rel) for rel in files):
        raise InstallError("AGENTS.md must not replace a source runtime file; no changes made.")
    if target.is_symlink():
        raise InstallError(f"Existing skill target is a symlink; no changes made: {target}")
    if target.exists() and not target.is_dir():
        raise InstallError(f"Existing skill target is not a directory: {target}")
    previous = installed_payload(target) if target.exists() else None
    if set_default and previous is not None and any(same_entry(agents_file, target / rel) for rel in previous):
        raise InstallError("AGENTS.md aliases an installed file; no changes made.")
    different = previous is not None and previous != files
    if different and not replace:
        raise InstallError("A different installation exists. Review it, then use --replace to back it up and update.")
    original = read_agents(agents_file) if set_default else None
    updated = default_text(original, target) if set_default else None
    result = {
        "skill_path": str(target),
        "skill_action": "replace" if different else "unchanged" if previous is not None else "install",
        "default_action": "update" if set_default and updated != original else "unchanged" if set_default else "not_requested",
        "agents_file": str(agents_file) if set_default else None,
        "runtime_files": len(files),
        "dry_run": dry_run,
    }
    if dry_run:
        return result
    if previous != files:
        target.parent.mkdir(parents=True, exist_ok=True)
        stage = Path(tempfile.mkdtemp(prefix=".research-pipeline-stage-", dir=target.parent))
        old = None
        try:
            for rel in files:
                dst = stage / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source / rel, dst)
            (stage / RECEIPT).write_text(json.dumps({"skill": NAME, "files": files}, indent=2) + "\n")
            if installed_payload(stage) != files:
                raise InstallError("Staged bytes differ from the source; nothing installed.")
            # Refuse a concurrent change instead of overwriting newly created work.
            now = installed_payload(target) if target.exists() else None
            if now != previous:
                raise InstallError("Skill target changed during installation; retry after review.")
            try:
                if target.exists():
                    old = backup_path(target)
                    target.rename(old)
                stage.rename(target)
            except BaseException:
                if old is not None and old.exists() and not target.exists():
                    old.rename(target)
                raise
            result["skill_backup"] = str(old) if old else None
        finally:
            if stage.exists():
                shutil.rmtree(stage)
    if set_default:
        try:
            result["agents_backup"] = write_agents(agents_file, original, updated)
        except Exception as exc:
            raise InstallError(f"Skill is installed at {target}, but the default was not updated: {exc}") from exc
    if installed_payload(target) != files:
        raise InstallError("Installed bytes do not match the source.")
    if set_default and read_agents(agents_file) != updated:
        raise InstallError("Default instruction read-back failed.")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-home", type=Path, default=Path.home() / ".agents" / "skills")
    codex_dir = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    parser.add_argument("--agents-file", type=Path, default=codex_dir / "AGENTS.md")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--set-default", action="store_true")
    mode.add_argument("--remove-default", action="store_true",
                      help="Remove only the managed default block; keep the skill installed.")
    parser.add_argument("--replace", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        if args.remove_default:
            path = args.agents_file.expanduser().absolute()
            original = read_agents(path)
            updated = default_text(original, Path("."), remove=True)
            result = {"agents_file": str(path), "default_action": "remove" if original not in (None, updated) else "unchanged", "dry_run": args.dry_run}
            if not args.dry_run and original is not None:
                result["agents_backup"] = write_agents(path, original, updated)
        else:
            result = install(Path(__file__).resolve().parents[1], args.skill_home, args.agents_file,
                             set_default=args.set_default, replace=args.replace, dry_run=args.dry_run)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (InstallError, OSError, UnicodeError) as exc:
        print(f"Installation not completed: {exc}", file=__import__("sys").stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
