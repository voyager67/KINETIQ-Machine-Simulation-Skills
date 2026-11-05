---
name: simulation-visual-regression
description: Verify interactive simulations across model states, input modes, devices, and rendering tiers using numerical assertions, deterministic captures, and visual review. Use when checking a simulator before calling it complete.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Simulation Visual Regression

## Purpose
Catch failures that ordinary unit tests may miss: broken geometry, incorrect clipping, camera regressions, unreadable labels, failed controls, unstable frames, and disagreement between numerical model state and rendered scene.

## When to use
Use for browser-based simulations, machine explainers, animated diagrams, scientific visualizations, and interactive engineering demos with multiple states or viewports.

## When not to use
Do not treat a screenshot comparison as proof of physical correctness, accessibility, or safety. Do not use exact pixel matching as the only gate when operating systems, browsers, GPUs, or fonts legitimately render differently.

## Inputs
Collect baseline version, expected model states, representative inputs, target browsers/viewports, quality tiers, interactions, tolerances, and known-good numerical or visual references.

## Decision logic
Use layered verification. First test mathematical invariants and state outputs; then test controls and navigation; finally inspect visual captures. Prefer structural or region-based comparisons when rendering environments vary.

## Procedure
1. Define representative states: initial, normal operation, minimum/maximum input, reverse direction, pause, isolation, cutaway, exploded view, reset, and invalid input where relevant.
2. Add numerical assertions for dimensions, constraints, ratios, phase, direction, bounds, and synchronized readouts.
3. Test controls with mouse and keyboard; test touch where the layout targets mobile. Verify reset from multiple combined modes.
4. Capture a baseline with fixed viewport, device pixel ratio, browser, seed, and quality tier.
5. Capture all representative states from deterministic inputs.
6. Build a labelled contact sheet with state, viewport, and capture time.
7. Inspect full-resolution images around failure-prone joints, intersections, thin parts, clipping planes, text, and material transitions.
8. Compare numerical and visual differences against declared tolerances. Record permitted nondeterminism and any environment-specific baseline.
9. Run a low-power rendering tier to expose problems hidden by high-end hardware.
10. Check console errors, failed local assets, unexpected network requests, offline startup, and accessibility basics.
11. Keep only useful regression artifacts. Exclude large transient captures and any user/private data from the repository.
12. Report numerical, functional, performance, offline, and visual results separately.

## Output contract
Deliver a state matrix, numerical test results, control checks, baseline/current captures, identified regressions, tolerance rationale, environment details, and pass/fail summary.

## Failure modes
- **False pass from one image:** include all important states and an alternate viewport.
- **False failure from GPU noise:** compare stable regions or structure and record environment details.
- **Visual pass with incorrect physics:** assert model invariants separately.
- **Model pass with broken controls:** exercise the actual interactions and focus paths.
- **Hidden network dependency:** test with networking disabled and inspect local resource references.
- **Unreproducible baseline:** lock inputs, seeds, dimensions, and capture timing.
- **Artifact bloat:** retain representative contact sheets and the capture recipe, not every intermediate frame.

## Quality gate
Model tests, interactions, offline loading, and visual review pass or have explicit exceptions; failures are reproducible; all comparison tolerances are stated; and the report distinguishes numerical, functional, performance, and visual evidence.

## Example
For landing gear, test fully extended, mid-retraction, stowed, reverse cycle, and reset. Assert strut and door poses against the mechanism model, capture whole-aircraft and close-up views, and inspect the contact sheet for clipping and intersecting parts.

## Related skills
machine-teardown-simulator, physics-model-validation, interactive-3d-explainer-design, timeline-driven-animation-capture, low-end-3d-performance-tuning
