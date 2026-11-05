---
name: low-end-3d-performance-tuning
description: Optimize interactive 3D simulations for integrated GPUs, laptops, and mobile devices using measured profiling, quality tiers, bounded scene complexity, and graceful fallbacks. Use when a simulator is slow or must run on modest hardware.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Low-End 3D Performance Tuning

## Purpose
Make an interactive simulator usable across realistic hardware. Optimize measured bottlenecks while preserving the details needed to understand the mechanism.

## When to use
Use when a 3D explainer targets laptops, integrated graphics, phones, tablets, shared lab computers, or when frame rate, memory use, startup time, or thermal load is a concern.

## When not to use
Do not prematurely remove geometry or reduce model fidelity without measurement. Do not claim a frame rate based on an unrepeatable single run or a different machine from the target device.

## Inputs
Collect target devices, GPU/browser details, scene complexity, current frame rate, startup time, draw calls, texture sizes, shadows, post-processing, viewport/device pixel ratio, and user-visible quality priorities.

## Decision logic
Profile first, then optimize the largest measured cost. Keep physical/model calculations separate from rendering-quality changes. Build quality tiers that scale visual effects without changing the underlying simulation state or numerical readouts.

## Procedure
1. Establish a baseline on at least one realistic low-power device or a documented emulation environment.
2. Measure startup, steady-state frame time, input latency, memory, draw calls, geometry count, texture memory, and shader compilation stalls where tools support it.
3. Separate CPU work, JavaScript allocations, model solving, geometry updates, GPU shading, shadows, and post-processing.
4. Reduce repeated allocations in animation loops. Reuse typed arrays, vectors, matrices, and buffers where correctness permits.
5. Use instancing or merged static geometry for repeated parts when it reduces draw overhead without breaking selection needs.
6. Use sensible level-of-detail, capped pixel ratio, smaller shadow maps, and simplified materials for low-power tiers.
7. Avoid expensive per-fragment operations when a cheaper representation explains the same physical idea.
8. Warm important shaders before the user begins interacting, where the rendering stack supports it.
9. Update labels and charts at a rate appropriate to their information needs rather than redrawing everything every frame.
10. Keep the model timestep and physical equations independent of frame rate. Do not change simulation speed to hide rendering slowness.
11. Add automatic quality selection only when it is transparent and user-overridable; provide a manual low/medium/high setting.
12. Re-run numerical and visual regression checks after each optimization. Confirm the lower tier still shows important contacts, motion, labels, and cutaways.

## Output contract
Provide a measured baseline, bottleneck ranking, changes made, target-device comparison, quality-tier definitions, before/after metrics, regression results, and any remaining limitations.

## Failure modes
- **Optimizing the wrong subsystem:** profile CPU and GPU separately before changes.
- **Visual quality hides motion:** preserve critical geometry and use simpler materials rather than removing moving parts.
- **Frame-rate-dependent physics:** use a fixed or deterministic model timestep.
- **Overly aggressive automatic scaling:** expose quality state and let users override it.
- **Regression after optimization:** rerun model invariants, interaction, and visual checks.
- **Unsupported performance claim:** report device, browser, scene, and measurement method.

## Quality gate
A reproducible baseline exists; optimizations target measured costs; numerical behavior is unchanged; low-tier controls remain responsive; and frame rate or memory claims identify the tested environment.

## Example
A pump simulator runs poorly on an integrated GPU. Profile first, cap pixel ratio, reduce shadow resolution, instance repeated bolts, simplify secondary materials, and throttle non-critical chart updates. Re-test pump speed and impeller motion to ensure performance changes did not alter model time or displayed readings.

## Related skills
machine-teardown-simulator, interactive-3d-explainer-design, simulation-visual-regression, offline-simulator-packaging
