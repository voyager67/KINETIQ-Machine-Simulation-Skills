"""Copy KINETIQ skill folders into a selected AI-agent project directory."""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
AGENT_DIRS = {
    "codex": ".agents/skills",
    "gemini-cli": ".gemini/skills",
    "claude-code": ".claude/skills",
    "github-copilot": ".github/skills",
    "cursor": ".cursor/skills",
    "opencode": ".opencode/skills",
    "windsurf": ".windsurf/skills",
}


def available_skills() -> set[str]:
    return {p.parent.name for p in SKILLS_ROOT.glob("*/SKILL.md")}


def install(target: Path, agents: list[str], selected: list[str] | None = None,
            overwrite: bool = False, dry_run: bool = False) -> tuple[list[str], list[str]]:
    available = available_skills()
    requested = set(selected or [])
    unknown = sorted(requested - available)
    if unknown:
        raise ValueError("Unknown skill(s): " + ", ".join(unknown))
    names = sorted(requested) if requested else sorted(available)
    resolved_target = target.expanduser().resolve()
    copied: list[str] = []
    skipped: list[str] = []
    for agent in agents:
        if agent not in AGENT_DIRS:
            raise ValueError(f"Unsupported agent '{agent}'")
        base = resolved_target / AGENT_DIRS[agent]
        for name in names:
            source = SKILLS_ROOT / name / "SKILL.md"
            destination = base / name / "SKILL.md"
            if destination.exists() and not overwrite:
                skipped.append(f"{agent}:{name}")
                continue
            copied.append(f"{agent}:{name}")
            if not dry_run:
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)
    return copied, skipped


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Install KINETIQ skills into a project-level agent skills directory.")
    parser.add_argument("--target", required=True, help="Target project directory")
    parser.add_argument("--agent", required=True, choices=[*AGENT_DIRS, "all"], help="Agent host or 'all'")
    parser.add_argument("--skills", help="Comma-separated skill names; default installs all")
    parser.add_argument("--overwrite", action="store_true", help="Replace only existing selected SKILL.md files")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    args = parser.parse_args(argv)
    selected = [x.strip() for x in args.skills.split(",") if x.strip()] if args.skills else None
    agents = list(AGENT_DIRS) if args.agent == "all" else [args.agent]
    try:
        copied, skipped = install(Path(args.target), agents, selected, args.overwrite, args.dry_run)
    except (OSError, ValueError) as exc:
        print(f"Install failed: {exc}", file=sys.stderr)
        return 2
    verb = "Would install" if args.dry_run else "Installed"
    print(f"{verb} {len(copied)} skill file(s) across {len(agents)} agent location(s).")
    if skipped:
        print("Skipped existing (use --overwrite to replace only SKILL.md): " + ", ".join(skipped))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
