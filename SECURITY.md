# Security policy

KINETIQ is a collection of agent instructions, a static browser catalogue, and small local helper scripts. It is not a sandbox and cannot make a host AI agent safe by itself.

## Reporting

Do not publish credentials, private drawings, proprietary machine data, or exploit details in public issues. Report suspected vulnerabilities privately through the maintainer's GitHub profile. Include the affected file, reproduction steps, impact, and suggested mitigation.

## Safe-use expectations

- Inspect skill text before installing it into a trusted environment.
- The installer does not execute skill content; it only copies selected Markdown files. The validator scans repository text for common credential patterns, private contact details, and machine-specific paths, and rejects sensitive file types. This is a useful screening layer, not a guarantee; review the final archive before publishing.
- Review source and dependencies before an AI agent runs generated code.
- Do not add secrets, telemetry, remote APIs, hidden downloads, or unrelated user files.
- Do not rely on an educational simulation for safety-critical engineering decisions.
