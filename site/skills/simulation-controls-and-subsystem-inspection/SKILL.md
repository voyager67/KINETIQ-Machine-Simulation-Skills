---
name: simulation-controls-and-subsystem-inspection
description: Design reliable controls for simulation inputs, operating modes, part isolation, exploded views, cutaways, camera presets, and guided inspection. Use when viewers need to explore a complex machine without losing context.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Simulation Controls and Subsystem Inspection

## Purpose
Create an interaction model that lets viewers explore a machine confidently. Controls should expose the relationship between input, subsystem, and output while preserving a reliable path back to the complete system.

## When to use
Use when a simulator has multiple moving parts, operating modes, camera views, selectable components, exploded assemblies, inspection overlays, or a guided tour.

## When not to use
Do not add controls merely to make the interface appear sophisticated. Avoid controls that claim to modify physical behavior when they only change presentation. Do not build a cockpit full of knobs when a few direct controls answer the learning goal.

## Inputs
Collect the viewer's learning objective, independent simulation variables, operating modes, selectable part hierarchy, camera requirements, target viewport, input devices, and accessibility needs.

## Decision logic
Separate simulation controls from presentation controls. A simulation control changes the model input/state; a presentation control changes visibility, camera, selection, or explanatory emphasis. Make this distinction explicit in labels and state. Prefer a small number of reversible controls.

## Procedure
1. List each control, the state it changes, its valid range, default value, and expected user benefit.
2. Identify the independent physical inputs. Avoid sliders for values that are not actually controllable or meaningful.
3. Choose input widgets that fit the quantity: bounded slider for a continuous range, discrete selector for modes, and play/pause for time progression.
4. Display units, bounds, current values, and reset behavior. Never imply a control has physical meaning if it is illustrative.
5. Build a stable part hierarchy with persistent component IDs and readable names.
6. Define isolation behavior: retain enough neighbouring geometry to explain connections, provide an always-visible return-to-assembly action, and show the isolated part's parent context.
7. Define exploded-view offsets as a reversible presentation transform. Preserve original assembly positions and do not mutate the physical model.
8. Define cutaway/x-ray states so hidden content is legible without confusing transparency depth ordering or implying an actual section drawing.
9. Give each camera preset a purpose and a descriptive name, such as overall, input side, output side, or internal view.
10. Make automatic tour steps idempotent and time-bounded. User input interrupts the tour and manual mode takes precedence.
11. Provide keyboard operation, focus states, accessible labels, touch-friendly targets, and reduced-motion alternatives.
12. Test invalid values, rapid changes, reset from every mode, and combinations such as isolated part plus cutaway.

## Output contract
Deliver a control inventory, state model, component hierarchy, interaction map, range/unit definitions, keyboard/touch behavior, reset strategy, and test cases for mode combinations.

## Failure modes
- **Unclear slider meaning:** add units, range, and a short explanation.
- **Isolation removes context:** keep connected parts faintly visible or provide an assembly breadcrumb.
- **Exploded positions drift:** calculate offsets from immutable original transforms.
- **Mode lock-in:** expose reset and a route to the overall view from every state.
- **Tour/manual conflict:** stop or yield to manual input immediately.
- **Touch controls are too small:** redesign the mobile layout and tap targets.

## Quality gate
Every control has a clear purpose and reversible state; physical and presentation controls are distinguished; users can always reset and regain context; keyboard and touch access are tested; and tours never override active user input.

## Example
For a gearbox explainer, provide a shaft-speed control, pause/reset, whole-system and bearing-side cameras, gear-pair isolation, a reversible exploded view, and a load-path tour. Keep gear geometry fixed when the exploded view changes only presentation.

## Related skills
machine-teardown-simulator, interactive-3d-explainer-design, timeline-driven-animation-capture, simulation-visual-regression
