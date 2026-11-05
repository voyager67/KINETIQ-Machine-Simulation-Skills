"""Validate KINETIQ skill files, catalogue, website mirrors, and packaging hygiene."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SITE = ROOT / "site"
REQUIRED_HEADINGS = (
    "## Purpose", "## When to use", "## When not to use", "## Inputs",
    "## Decision logic", "## Procedure", "## Output contract",
    "## Failure modes", "## Quality gate", "## Example", "## Related skills",
)
SECRET_PATTERNS = (
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{24,}\b"),
    re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|secret[_-]?key|password)\s*[:=]\s*['\"][^'\"\s]{8,}['\"]"),
)
PRIVACY_PATTERNS = (
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    re.compile(r"(?i)\b[A-Z]:\\Users\\[^\\\s]+\\"),
    re.compile(r"/(?:home|Users)/[A-Za-z0-9._-]+/"),
)
TEXT_SUFFIXES = {".md", ".py", ".json", ".html", ".js", ".css", ".yml", ".yaml", ".toml", ".txt", ".csv", ".svg"}
SENSITIVE_SUFFIXES = {".pem", ".p12", ".pfx", ".key"}
SENSITIVE_FILENAMES = {".env", ".npmrc", ".pypirc", "id_rsa", "id_ed25519", "credentials", "secrets.json"}
FORBIDDEN_PATH_PARTS = {".git", ".venv", "venv", "node_modules", ".idea", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def sensitive_content_findings(content: str) -> list[str]:
    """Return labels for likely credentials or private contact/path data."""
    findings = []
    if any(pattern.search(content) for pattern in SECRET_PATTERNS):
        findings.append("possible credential or private-key pattern")
    if any(pattern.search(content) for pattern in PRIVACY_PATTERNS):
        findings.append("possible private email or machine-specific path")
    return findings


def parse_frontmatter(content: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data


def discover_skills(root: Path = ROOT) -> list[dict[str, object]]:
    found = []
    base = root / "skills"
    for path in sorted(base.glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        found.append({
            "name": meta.get("name", path.parent.name),
            "description": meta.get("description", ""),
            "path": path.relative_to(root).as_posix(),
            "words": len(text.split()),
        })
    return found


def validate(root: Path = ROOT, minimum_words: int = 300) -> list[str]:
    errors: list[str] = []
    skill_paths = sorted((root / "skills").glob("*/SKILL.md"))
    if not skill_paths:
        return ["No skills found under skills/*/SKILL.md"]

    names: set[str] = set()
    for path in skill_paths:
        content = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(content)
        label = path.relative_to(root).as_posix()
        for key in ("name", "description", "license"):
            if not meta.get(key):
                errors.append(f"{label}: missing frontmatter field '{key}'")
        name = meta.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"{label}: invalid skill name '{name}'")
        if name != path.parent.name:
            errors.append(f"{label}: folder name does not match frontmatter name")
        if name in names:
            errors.append(f"{label}: duplicate skill name '{name}'")
        names.add(name)
        description = meta.get("description", "")
        if len(description) > 1024:
            errors.append(f"{label}: description exceeds 1024 characters")
        if not description or "Use when" not in description:
            errors.append(f"{label}: description must explain what it does and when to use it")
        for heading in REQUIRED_HEADINGS:
            if heading not in content:
                errors.append(f"{label}: missing section '{heading}'")
        if len(content.split()) < minimum_words:
            errors.append(f"{label}: only {len(content.split())} words (minimum {minimum_words})")
        if re.search(r"\b(?:TODO|TBD|FIXME)\b", content):
            errors.append(f"{label}: unresolved TODO/TBD/FIXME marker")
        related = re.search(r"## Related skills\s*\n(.*?)(?:\n## |\Z)", content, re.S)
        if related:
            linked = [x.strip() for x in related.group(1).replace("\n", "").split(",") if x.strip()]
            for item in linked:
                if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", item):
                    errors.append(f"{label}: malformed related-skill name '{item}'")
                elif not (root / "skills" / item / "SKILL.md").is_file():
                    errors.append(f"{label}: related skill '{item}' does not exist")
        for finding in sensitive_content_findings(content):
            errors.append(f"{label}: {finding}")
        mirror = root / "site" / "skills" / path.relative_to(root / "skills")
        if not mirror.is_file():
            errors.append(f"{label}: missing static-site mirror")
        elif mirror.read_bytes() != path.read_bytes():
            errors.append(f"{label}: static-site mirror differs from canonical skill")

    for catalogue_path in (root / "catalog.json", root / "site" / "catalog.json"):
        if not catalogue_path.is_file():
            errors.append(f"Missing {catalogue_path.relative_to(root)}")
            continue
        try:
            catalogue = json.loads(catalogue_path.read_text(encoding="utf-8"))
            catalogue_names = {entry.get("name") for entry in catalogue}
            if catalogue_names != names:
                errors.append(f"{catalogue_path.relative_to(root)} does not match discovered skills")
            if len(catalogue) != len(names):
                errors.append(f"{catalogue_path.relative_to(root)} has duplicate or missing entries")
            for entry in catalogue:
                if not (root / entry.get("path", "")).is_file():
                    errors.append(f"catalogue entry '{entry.get('name')}' points to a missing file")
        except (json.JSONDecodeError, OSError, AttributeError) as exc:
            errors.append(f"{catalogue_path.relative_to(root)} cannot be read: {exc}")
    if (root / "catalog.json").is_file() and (root / "site" / "catalog.json").is_file():
        if (root / "catalog.json").read_bytes() != (root / "site" / "catalog.json").read_bytes():
            errors.append("site/catalog.json is stale")

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in FORBIDDEN_PATH_PARTS for part in rel.parts):
            errors.append(f"forbidden build/cache path included: {rel.as_posix()}")
        if path.name in SENSITIVE_FILENAMES or path.suffix.lower() in SENSITIVE_SUFFIXES:
            errors.append(f"sensitive file type/name should not be packaged: {rel.as_posix()}")
        if path.name.startswith(".env") and path.name != ".env.example":
            errors.append(f"environment file should not be committed: {rel.as_posix()}")
        if path.suffix.lower() in TEXT_SUFFIXES:
            try:
                content = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                errors.append(f"text file cannot be safely inspected: {rel.as_posix()}")
                continue
            for finding in sensitive_content_findings(content):
                errors.append(f"{rel.as_posix()}: {finding}")

    # The static explorer may fetch only same-origin catalogue/skill files.
    explorer = root / "site" / "index.html"
    if explorer.is_file():
        code = explorer.read_text(encoding="utf-8")
        if re.search(r"\bfetch\s*\(\s*['\"]https?://", code, re.I):
            errors.append("site/index.html contains an external fetch request")
        if re.search(r"\b(?:XMLHttpRequest|WebSocket)\b|navigator\.sendBeacon", code):
            errors.append("site/index.html contains an unexpected network-capable API")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("KINETIQ validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    skills = discover_skills()
    print(f"KINETIQ validation passed: {len(skills)} skills, {len({Path(str(s['path'])).parent.name for s in skills})} unique folders, mirrors and catalogues in sync.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
