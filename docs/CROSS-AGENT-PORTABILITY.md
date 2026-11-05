# Cross-agent portability

KINETIQ uses the portable Agent Skills shape: a directory containing a `SKILL.md` file with YAML frontmatter (`name`, `description`) and Markdown instructions. The method and quality gate stay the same between hosts; the discovery folder and invocation syntax may differ.

## Recommended use

1. Install a skill folder into the location documented by the target agent, or provide its full `SKILL.md` as project knowledge/instructions.
2. Ask the agent to use the skill by name and provide the task, references, target device, allowed file changes, and desired deliverables.
3. Ask for evidence labels: measured/sourced, inferred, assumed, illustrative, and unknown.
4. Require the same quality gate regardless of model vendor.
5. Verify the host actually loaded the skill; a file being present does not prove it was discovered or invoked.

## Host directories

| Host | Project-level directory |
|---|---|
| Codex | `.agents/skills/<skill-name>/SKILL.md` |
| Gemini CLI | `.gemini/skills/<skill-name>/SKILL.md` or shared `.agents/skills/<skill-name>/SKILL.md` |
| Claude Code | `.claude/skills/<skill-name>/SKILL.md` |
| GitHub Copilot / VS Code | `.github/skills/<skill-name>/SKILL.md` |
| Cursor | `.cursor/skills/<skill-name>/SKILL.md` |
| OpenCode | `.opencode/skills/<skill-name>/SKILL.md` |
| Windsurf | `.windsurf/skills/<skill-name>/SKILL.md` |

These are documented/common project-skill locations, not a guarantee that every version or configuration scans every folder. Check the current host documentation for changes. KINETIQ's installer writes project-level copies only; it does not modify global home-directory settings.

## When a host has no compatible loader

Attach or paste the complete `SKILL.md` into the host's project instructions or knowledge feature, then explicitly invoke it by name. If the host cannot read Markdown instructions or access files, use the skill as a human-readable workflow guide rather than claiming automatic integration.

## Tool portability

A skill does not create shell, filesystem, browser, rendering, or publishing permissions. The agent must check what tools are actually available. If a required local capability is missing, it should produce a safe partial result, name the missing capability, and not invent a successful build or test.

## References

- [VS Code: Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [Anthropic: Skills for Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/skills)
- [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/skills/)
- [OpenAI Codex documentation](https://developers.openai.com/codex/)

Host-specific documentation takes precedence over this convenience table.
