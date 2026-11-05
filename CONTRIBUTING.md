# Contributing to KINETIQ

Contributions should make a machine-simulation workflow more accurate, portable, understandable, or verifiable. Keep the collection focused.

## Before opening a pull request

1. Read `AGENTS.md` and the relevant skill.
2. Explain the user problem and why a new skill or change is needed.
3. Prefer improving an existing playbook over creating a duplicate.
4. Keep skill names kebab-case and align the folder name with the frontmatter `name`.
5. Preserve the standard sections and include a useful example, failure modes, and a testable quality gate.
6. Add related-skill links only when the destination exists.
7. Keep references, code, and media legally reusable; include attribution and licence details.
8. Update both the canonical `skills/` copy and `site/skills/` mirror, catalogue, and tests as needed.
9. Run `python scripts/validate.py` and `python -m unittest discover -s tests -v`.

## Scope

Do not add a hosted backend, API requirement, analytics, telemetry, credentials, or large media bundle without a clear reason and explicit design review.
