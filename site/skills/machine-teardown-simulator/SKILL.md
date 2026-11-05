---
name: machine-teardown-simulator
description: Build an interactive 3D simulator that explains a real machine or mechanism through model-driven motion, live readouts, subsystem isolation, cutaways, exploded views, camera presets, and a guided tour. Use when a user asks how a machine works, requests a mechanical visual explainer, or wants an offline simulator.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Machine Teardown Simulator

## Purpose
Turn a real machine into an explorable engineering explanation. The viewer should be able to watch it operate, change an input, isolate the part doing the work, inspect hidden relationships, and connect visible motion to an understandable physical model. The deliverable is an educational simulator unless independently validated evidence supports a stronger engineering claim.

## When to use
Use this skill when a user asks how an engine, gearbox, pump, actuator, landing gear, linkage, transmission, robotic mechanism, or other physical system works. It also fits requests for a 3D cutaway, exploded view, interactive engineering lesson, visual teardown, or locally playable machine demonstration.

## When not to use
Do not force 3D onto a question that a clear diagram, animation, or short explanation answers better. Do not present an illustrative prototype as a certified digital twin, CAD design, safety analysis, manufacturing specification, or operational training system. Do not invent dimensions or use the visual model to instruct unsafe real-world actions.

## Inputs
Gather the machine and learning objective, audience, reference photos/manuals/drawings/videos, trusted dimensions, moving input, operating range, important subsystems, target devices, accessibility needs, offline requirement, and requested media. Identify available local tools and dependencies. Mark missing dimensions and physical quantities as unknown, inferred, or assumed.

## Decision logic
Work from the physical question and reference evidence toward the visual experience. Choose the simplest model that explains the important behavior. Select one independent input where possible—such as crank angle, shaft speed, stroke, pressure, position, or time—and derive the complete machine state from it. Keep the mathematical model separate from rendering code. If the inputs do not support a physically faithful model, build a clearly labelled conceptual demonstration instead of pretending otherwise.

## Procedure
1. Inspect the actual reference material. Record component names, geometry, dimensions, motion constraints, material clues, operating phases, and source provenance. Separate directly observed facts from inferred geometry.
2. Draw a system boundary. Identify the input, energy or force path, output, fixed frame, moving bodies, joints, and the minimum subsystems needed to explain the mechanism.
3. Write a model brief before coding. Define coordinates, units, sign conventions, valid input range, equations, simplifications, expected edge cases, and at least one independent reference calculation.
4. Implement the model layer without a rendering dependency. Expose a deterministic function such as `stateFromInput(input)` that returns named positions, orientations, forces or other justified quantities, and derived readouts.
5. Validate equations and units. Check limiting positions, expected direction, joint closure, ratios, periodicity, and numerical behavior. Do not proceed to visual polish while the core motion is known to be wrong.
6. Build the scene from named components and reusable geometry. Keep physical dimensions in consistent units and use explicit transforms for every moving part. Avoid arbitrary keyframes when the movement can be calculated.
7. Make one shared model state drive the 3D transforms, labels, gauges, charts, tooltips, and status panels. A displayed number must be traceable to the same state that moves the object.
8. Design an intentional exploration sequence: whole-machine view, operating motion, selected subsystem, useful cutaway or exploded view, explanatory close-up, and return to the complete machine.
9. Add meaningful controls: play/pause, reset, input or speed control, camera presets, component selection, isolation, explode/cutaway, and a guided tour only where each control supports understanding.
10. Make user input take control immediately. A running tour must stop or yield on click, drag, key press, scroll, or touch; it must never fight the visitor.
11. Package dependencies locally. Do not rely on remote CDNs, hosted APIs, analytics, telemetry, external fonts, or runtime network requests. The final HTML should open with networking disabled.
12. Capture the initial state, every important subsystem state, and difficult transitions at target desktop and mobile sizes. Inspect screenshots/contact sheets, fix geometry and typography issues, then rebuild and repeat.
13. Report source provenance, assumptions, validated calculations, simplifications, unvalidated behavior, runtime requirements, performance limits, and exact output paths.

## Output contract
Deliver the source project, offline-ready simulator page, model brief, reference/provenance list, visible interaction controls, requested stills or video, and a verification report. Distinguish model correctness checks, interaction checks, visual inspection, and any unverified assumptions.

## Failure modes
- **Generic machine shape:** return to the supplied references and match major component proportions and arrangement before adding detail.
- **Decorative telemetry:** derive gauges and labels from the shared model state or remove them.
- **Impossible motion:** stop visual work and repair equations, constraints, or assembly-branch selection.
- **False precision:** expose assumptions and round values to the precision supported by sources.
- **Camera hides defects:** inspect multiple views and correct the geometry instead of hiding intersections.
- **Tour takeover:** interrupt scripted motion as soon as the visitor interacts.
- **Online-only artifact:** bundle dependencies locally and test the final page offline.
- **Looks finished, not verified:** report what was actually tested and what remains illustrative.

## Quality gate
A real reference informs important geometry; variables have units and provenance; equations pass dimensional and reference checks; one model state drives both motion and readouts; controls work with the supported input methods; the user can regain control; the page opens offline; the first frame communicates the subject; and the report does not overstate engineering validity.

## Example
Build an interactive four-stroke single-cylinder engine explainer from a supplied cutaway. Let crank angle determine piston travel, connecting-rod pose, valve timing, and the cycle phase. Add a transparent head, cylinder isolation, a chamber inspection camera, a speed control, and a short guided tour. Label pressure and combustion curves as illustrative unless validated measurements or a documented thermodynamic model support them.

## Related skills
engineering-reference-reconstruction, mechanism-kinematics-and-linkage-solving, physics-model-validation, interactive-3d-explainer-design, simulation-controls-and-subsystem-inspection, timeline-driven-animation-capture, simulation-visual-regression, offline-simulator-packaging
