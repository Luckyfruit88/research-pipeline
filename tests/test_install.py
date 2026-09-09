import importlib.util
from pathlib import Path
import tempfile
import shutil
import os
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts" / "install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.home = self.root / "skills"
        self.agents = self.root / "config" / "AGENTS.md"

    def run_install(self, **kwargs):
        return installer.install(ROOT, self.home, self.agents, **kwargs)

    def copy_source(self):
        source = self.root / "source"
        for rel in installer.payload(ROOT):
            destination = source / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, destination)
        return source

    def test_fresh_runtime_bytes_and_no_default_side_effect(self):
        result = self.run_install()
        target = self.home / installer.NAME
        self.assertEqual(installer.payload(ROOT), installer.installed_payload(target))
        self.assertFalse((target / "evals").exists())
        self.assertFalse(self.agents.exists())
        self.assertEqual("install", result["skill_action"])

    def test_default_preserves_existing_content(self):
        self.agents.parent.mkdir()
        existing = "用户规则：保持已有成果。\nNo unrelated changes.\n"
        self.agents.write_text(existing)
        result = self.run_install(set_default=True)
        text = self.agents.read_text()
        self.assertTrue(text.startswith(existing))
        self.assertIn("$research-pipeline", text)
        self.assertEqual(existing, Path(result["agents_backup"]).read_text())

    def test_idempotent_install_and_default_do_not_rewrite(self):
        self.run_install(set_default=True)
        before = self.agents.stat().st_mtime_ns
        result = self.run_install(set_default=True)
        self.assertEqual("unchanged", result["skill_action"])
        self.assertEqual("unchanged", result["default_action"])
        self.assertEqual(before, self.agents.stat().st_mtime_ns)
        self.assertEqual(1, self.agents.read_text().count(installer.START))

    def test_existing_different_target_is_preserved(self):
        self.run_install()
        p = self.home / installer.NAME / "SKILL.md"
        p.write_text("local modification\n")
        with self.assertRaises(installer.InstallError):
            self.run_install(set_default=True)
        self.assertEqual("local modification\n", p.read_text())
        self.assertFalse(self.agents.exists())

    def test_replace_keeps_unknown_files_in_backup(self):
        self.run_install()
        extra = self.home / installer.NAME / "local-note.txt"
        extra.write_text("preserve me\n")
        result = self.run_install(replace=True)
        self.assertEqual("preserve me\n", (Path(result["skill_backup"]) / "local-note.txt").read_text())
        self.assertFalse(extra.exists())
        self.assertEqual(installer.payload(ROOT), installer.installed_payload(self.home / installer.NAME))

    def test_dry_run_writes_nothing(self):
        result = self.run_install(set_default=True, dry_run=True)
        self.assertTrue(result["dry_run"])
        self.assertEqual([], list(self.root.iterdir()))

    def test_malformed_markers_abort_before_install(self):
        self.agents.parent.mkdir()
        original = "original\n" + installer.START + "\n"
        self.agents.write_text(original)
        with self.assertRaises(installer.InstallError):
            self.run_install(set_default=True)
        self.assertFalse(self.home.exists())
        self.assertEqual(original, self.agents.read_text())

    def test_duplicate_markers_abort(self):
        original = ((installer.START + "\nx\n" + installer.END + "\n") * 2).encode()
        with self.assertRaises(installer.InstallError):
            installer.default_text(original, self.home / installer.NAME)

    def test_default_update_preserves_surrounding_user_text(self):
        original = "prefix\n" + installer.START + "\nold\n" + installer.END + "\nsuffix\n"
        updated = installer.default_text(original.encode(), self.home / installer.NAME).decode()
        self.assertTrue(updated.startswith("prefix\n"))
        self.assertTrue(updated.endswith("\nsuffix\n"))
        self.assertEqual(1, updated.count(installer.START))

    def test_remove_default_keeps_surrounding_instructions(self):
        original = "prefix\n" + installer.START + "\nold\n" + installer.END + "\nsuffix\n"
        updated = installer.default_text(original.encode(), Path("."), remove=True).decode()
        self.assertEqual("prefix\n\nsuffix\n", updated)

    def test_target_symlink_is_not_followed(self):
        self.home.mkdir()
        other = self.root / "other"
        other.mkdir()
        (self.home / installer.NAME).symlink_to(other)
        with self.assertRaises(installer.InstallError):
            self.run_install()
        self.assertEqual([], list(other.iterdir()))

    def test_agents_symlink_is_not_replaced(self):
        self.agents.parent.mkdir()
        other = self.root / "real-agents"
        other.write_text("retain\n")
        self.agents.symlink_to(other)
        with self.assertRaises(installer.InstallError):
            self.run_install(set_default=True)
        self.assertEqual("retain\n", other.read_text())
        self.assertFalse(self.home.exists())

    def test_shared_skill_home_symlink_is_supported(self):
        shared = self.root / "shared"
        shared.mkdir()
        self.home.symlink_to(shared)
        result = self.run_install()
        self.assertTrue(Path(result["skill_path"]).samefile(shared / installer.NAME))
        self.assertTrue((shared / installer.NAME / "SKILL.md").exists())

    def test_concurrent_agents_change_is_preserved(self):
        self.agents.parent.mkdir()
        self.agents.write_text("new user instruction\n")
        with self.assertRaises(installer.InstallError):
            installer.write_agents(self.agents, b"old", b"replacement")
        self.assertEqual("new user instruction\n", self.agents.read_text())

    def test_interrupted_promotion_restores_previous_installation(self):
        self.run_install()
        original = self.home / installer.NAME / "SKILL.md"
        original.write_text("preserve existing installation\n")
        rename = Path.rename

        def interrupt_stage(path, target):
            if path.name.startswith(".research-pipeline-stage-"):
                raise KeyboardInterrupt()
            return rename(path, target)

        with mock.patch.object(Path, "rename", new=interrupt_stage):
            with self.assertRaises(KeyboardInterrupt):
                self.run_install(replace=True)
        self.assertEqual("preserve existing installation\n", original.read_text())
        self.assertEqual([], list(self.home.glob(".research-pipeline-stage-*")))

    def test_new_install_rejects_overlapping_agents_before_writing(self):
        for name in ["AGENTS.md", "SKILL.md"]:
            with self.subTest(name=name):
                path = self.home / installer.NAME / name
                with self.assertRaises(installer.InstallError):
                    installer.install(ROOT, self.home, path, set_default=True)
                self.assertFalse(self.home.exists())

    def test_existing_install_rejects_overlapping_agents_without_changes(self):
        self.run_install()
        target = self.home / installer.NAME
        before = installer.installed_payload(target)
        for name in ["AGENTS.md", "SKILL.md"]:
            with self.subTest(name=name):
                with self.assertRaises(installer.InstallError):
                    installer.install(ROOT, self.home, target / name, set_default=True)
                self.assertEqual(before, installer.installed_payload(target))

    def test_source_runtime_cannot_become_agents_file(self):
        source = self.copy_source()
        before = (source / "SKILL.md").read_bytes()
        with self.assertRaises(installer.InstallError):
            installer.install(source, self.home, source / "SKILL.md", set_default=True)
        self.assertEqual(before, (source / "SKILL.md").read_bytes())
        self.assertFalse(self.home.exists())

    def test_fresh_case_alias_target_is_rejected_before_mutation(self):
        with self.assertRaises(installer.InstallError):
            installer.install(ROOT, self.home, self.home / "RESEARCH-PIPELINE" / "AGENTS.md", set_default=True)
        self.assertFalse(self.home.exists())

    def test_existing_case_alias_target_is_rejected(self):
        self.run_install()
        before = installer.installed_payload(self.home / installer.NAME)
        for name in ["AGENTS.md", "skill.md"]:
            with self.subTest(name=name), self.assertRaises(installer.InstallError):
                installer.install(ROOT, self.home, self.home / "RESEARCH-PIPELINE" / name, set_default=True)
        self.assertEqual(before, installer.installed_payload(self.home / installer.NAME))

    def test_source_runtime_case_alias_is_rejected(self):
        source = self.copy_source()
        before = installer.payload(source)
        with self.assertRaises(installer.InstallError):
            installer.install(source, self.home, source / "skill.md", set_default=True)
        self.assertEqual(before, installer.payload(source))
        self.assertFalse(self.home.exists())

    def test_source_hardlink_alias_is_rejected(self):
        source = self.copy_source()
        alias = self.root / "outside.md"
        os.link(source / "SKILL.md", alias)
        before = alias.read_bytes()
        with self.assertRaises(installer.InstallError):
            installer.install(source, self.home, alias, set_default=True)
        self.assertEqual(before, alias.read_bytes())
        self.assertFalse(self.home.exists())

    def test_installed_hardlink_alias_is_rejected(self):
        self.run_install()
        target = self.home / installer.NAME
        alias = self.root / "outside.md"
        os.link(target / "SKILL.md", alias)
        before = installer.installed_payload(target)
        with self.assertRaises(installer.InstallError):
            installer.install(ROOT, self.home, alias, set_default=True)
        self.assertEqual(before, installer.installed_payload(target))


if __name__ == "__main__":
    unittest.main()
