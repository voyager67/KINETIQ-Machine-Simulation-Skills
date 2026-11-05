---
name: offline-simulator-packaging
description: Package a simulator as a dependable local/offline deliverable with bundled dependencies, documented runtime needs, reproducible builds, and no hidden network services. Use when preparing an interactive simulator for handoff or publication.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Offline Simulator Packaging

## Purpose
Make an interactive simulator easy to open, inspect, share, and archive without depending on a hosted backend or undocumented network access. A portable artifact should explain its own runtime requirements and source materials.

## When to use
Use when a user requests a single HTML page, offline demonstration, portable engineering lesson, local static site, or repeatable build package.

## When not to use
Do not force a single-file bundle when the model or assets are too large or when a documented multi-file package is safer and clearer. Do not download binaries, install system dependencies, or alter machine configuration without appropriate approval.

## Inputs
Collect target OS/browser, expected offline behavior, local runtime availability, dependency list, asset sizes/licences, build command, output structure, and any limits on file size or portability.

## Decision logic
Prefer static local assets and explicit dependencies. Bundle runtime JavaScript, styles, fonts, model files, and textures when license terms permit. If the artifact remains multi-file, package it with a clear index and relative paths. Avoid APIs, credentials, remote CDNs, analytics, telemetry, and hidden update checks.

## Procedure
1. Inventory all source files, dependencies, fonts, models, textures, audio, and generated outputs.
2. Inspect each dependency's license and provenance. Keep notices and attribution with redistributed assets where required.
3. Pin dependency versions and record the build environment. Avoid floating versions for reproducible deliverables.
4. Build from local source. Do not require an account, API key, or hosted build endpoint.
5. Use relative asset paths and bundle required runtime resources. Ensure no external resource is fetched at startup.
6. Separate source, build output, temporary captures, and user-provided references. Never include local secrets, private directories, personal files, or test data.
7. Add a short README beside the artifact with opening instructions, browser/runtime requirements, controls, known limitations, and source/licence notes.
8. Test from a clean output directory. Open the deliverable directly or via the documented local static server, depending on browser restrictions.
9. Disable network access and repeat the smoke test. Inspect browser network logs and console errors for hidden dependencies.
10. Verify the archive contains only expected paths. Reject `.git`, caches, virtual environments, environment files, credentials, and unrelated workspace files.
11. Compare the packaged output with the source build and record checksums or a build manifest if the handoff requires integrity tracking.
12. Report any feature that still requires internet access or a local dependency that could not be bundled.

## Output contract
Deliver a source directory, portable build/archive, concise run instructions, dependency/licence inventory, offline test result, clean archive manifest, and known limitations.

## Failure modes
- **CDN dependency remains:** bundle the resource locally or document why offline mode is not supported.
- **File URL restrictions:** provide a minimal local server command and explain the browser security constraint.
- **Unclear licence:** exclude the asset or obtain permission rather than assume redistribution is allowed.
- **Platform-specific binary:** document OS/runtime compatibility and offer a source-based alternative.
- **Archive leakage:** inspect every archive path and scan for secrets before delivery.
- **Build not reproducible:** pin dependencies and record the exact command and environment.

## Quality gate
A clean archive opens using documented steps; offline mode does not make unexpected requests; all redistributed assets have traceable rights; no credentials or unrelated files are present; and every runtime requirement is disclosed.

## Example
Package a machine explainer into a `dist/` folder containing `index.html`, local JavaScript/CSS, and local model assets. Create a ZIP, extract it into a fresh temporary directory, disable networking, open it with the documented local server, and confirm that all controls and camera views still work.

## Related skills
machine-teardown-simulator, timeline-driven-animation-capture, simulation-visual-regression, low-end-3d-performance-tuning
