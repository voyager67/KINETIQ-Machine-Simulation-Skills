# Package architecture

- `skills/` is the canonical source for all portable AI-agent playbooks.
- `site/skills/` is a byte-identical read-only mirror for the static browser explorer.
- `catalog.json` and `site/catalog.json` index skill names, descriptions, categories, and paths.
- `scripts/install.py` copies chosen canonical skill folders to a host-specific project directory. It does not execute skill instructions.
- `scripts/validate.py` checks frontmatter, required sections, related-skill references, catalogue parity, mirror parity, and repository-wide credential, contact-detail, and machine-specific path patterns, plus sensitive-file and static-site network checks.
- `tests/` exercises installer and repository invariants with Python's standard library.
- `site/index.html` is a static client-side skill browser with no backend or external runtime dependencies.

The installer writes only to a user-selected target folder. It never edits agent settings, global home-directory configuration, system packages, or external services.
