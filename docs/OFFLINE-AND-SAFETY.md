# Offline, privacy, and engineering safety

## Local-first requirements

- Prefer self-contained HTML or a documented local static server.
- Bundle runtime scripts, styles, models, textures, and fonts locally where licence terms permit.
- Do not add hosted APIs, API keys, analytics, telemetry, remote CDNs, hidden update checks, or tracking pixels.
- Make all external dependencies explicit and pin versions for reproducible builds.
- Test the final extracted archive with networking disabled.

## Safe packaging

Exclude `.git`, `.env*`, virtual environments, caches, local downloads, private project directories, credentials, user datasets, proprietary drawings, and unrelated files. Review the archive manifest before sharing.

## Engineering claims

An interactive 3D explainer is not automatically a digital twin. Label measured values, sourced parameters, estimates, assumptions, and illustrative behavior. A simplified model must not be used to certify safety, manufacturing tolerances, or operational procedures. Escalate safety-critical analysis to qualified engineering review and validated tools.

## Agent trust boundary

`SKILL.md` files are instructions for an AI agent. Review them before installation. A skill does not grant any permission to execute commands, change files, install dependencies, publish content, or access external services.
