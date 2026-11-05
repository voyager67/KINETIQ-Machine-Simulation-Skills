from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.install import AGENT_DIRS, install
from scripts.validate import ROOT, discover_skills, parse_frontmatter, sensitive_content_findings, validate


class KinetiqRepositoryTests(unittest.TestCase):
    def test_catalogue_and_skill_count(self) -> None:
        skills = discover_skills()
        catalogue = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(len(skills), 17)
        self.assertEqual({x["name"] for x in skills}, {x["name"] for x in catalogue})

    def test_all_skill_files_pass_full_validation(self) -> None:
        self.assertEqual(validate(), [])

    def test_skill_metadata_matches_folder_and_description_is_triggerable(self) -> None:
        for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
            meta = parse_frontmatter(path.read_text(encoding="utf-8"))
            self.assertEqual(meta["name"], path.parent.name)
            self.assertTrue(meta["description"].startswith(("Build", "Reconstruct", "Derive", "Design", "Create", "Verify", "Package", "Present", "Optimize", "Prepare", "Analyze", "Model", "Quantify")))
            self.assertEqual(meta["license"], "CC BY-NC-ND 4.0")

    def test_site_mirrors_are_byte_identical(self) -> None:
        for path in (ROOT / "skills").glob("*/SKILL.md"):
            mirror = ROOT / "site" / "skills" / path.relative_to(ROOT / "skills")
            self.assertEqual(path.read_bytes(), mirror.read_bytes())

    def test_security_scanner_flags_credentials_and_private_contact_data(self) -> None:
        fake_key = "ghp_" + ("A" * 30)
        fake_email = "private" + "@" + "example.invalid"
        findings = sensitive_content_findings(f"token={fake_key}; contact={fake_email}")
        self.assertEqual(len(findings), 2)

    def test_security_scanner_accepts_safe_local_first_text(self) -> None:
        findings = sensitive_content_findings("No runtime API, no credential, and no user-specific path.")
        self.assertEqual(findings, [])

    def test_installer_skips_existing_skill_without_overwriting(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            existing = target / ".agents/skills/machine-teardown-simulator"
            existing.mkdir(parents=True)
            skill = existing / "SKILL.md"
            sentinel = existing / "LOCAL-NOTE.txt"
            skill.write_text("local version", encoding="utf-8")
            sentinel.write_text("preserve me", encoding="utf-8")
            copied, skipped = install(target, ["codex"], ["machine-teardown-simulator"])
            self.assertEqual(copied, [])
            self.assertEqual(skipped, ["codex:machine-teardown-simulator"])
            self.assertEqual(skill.read_text(encoding="utf-8"), "local version")
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserve me")

    def test_installer_overwrites_only_skill_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            existing = target / ".claude/skills/physics-model-validation"
            existing.mkdir(parents=True)
            (existing / "SKILL.md").write_text("old", encoding="utf-8")
            note = existing / "my-reference.txt"
            note.write_text("keep", encoding="utf-8")
            copied, skipped = install(target, ["claude-code"], ["physics-model-validation"], overwrite=True)
            self.assertEqual(copied, ["claude-code:physics-model-validation"])
            self.assertEqual(skipped, [])
            self.assertIn("KINETIQ Physics Model Validation", (existing / "SKILL.md").read_text(encoding="utf-8"))
            self.assertEqual(note.read_text(encoding="utf-8"), "keep")

    def test_dry_run_has_no_filesystem_side_effects(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            copied, skipped = install(target, ["codex"], ["machine-teardown-simulator"], dry_run=True)
            self.assertEqual(copied, ["codex:machine-teardown-simulator"])
            self.assertFalse(target.exists())

    def test_unknown_skill_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(ValueError):
                install(Path(temp), ["codex"], ["not-a-skill"])

    def test_agent_map_is_explicit_and_project_local(self) -> None:
        self.assertEqual(AGENT_DIRS["codex"], ".agents/skills")
        self.assertEqual(AGENT_DIRS["claude-code"], ".claude/skills")
        self.assertTrue(all(not x.startswith("~") for x in AGENT_DIRS.values()))


    def test_license_and_readme_media_assets_are_present(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("CC BY-NC-ND 4.0", license_text)
        self.assertIn("creativecommons.org/licenses/by-nc-nd/4.0", license_text)
        for asset in (
            "kinetiq-pages-overview.png",
            "kinetiq-skill-library.png",
            "kinetiq-workflow-preview.png",
            "kinetiq-static-pages-tour.gif",
            "kinetiq-static-pages-tour.mp4",
        ):
            self.assertTrue((ROOT / "assets" / asset).is_file(), asset)
            self.assertIn(asset, readme)

    def test_github_pages_is_static_about_and_skill_explorer(self) -> None:
        page = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
        workflow = (ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")
        self.assertIn('id="about"', page)
        self.assertIn('id="explore"', page)
        self.assertIn("No live simulation", page)
        self.assertIn("path: site", workflow)


if __name__ == "__main__":
    unittest.main()
