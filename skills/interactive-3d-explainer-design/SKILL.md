---
name: interactive-3d-explainer-design
description: Design accessible 3D explainers with meaningful camera views, part selection, cutaways, exploded views, guided tours, and controls tied to a learning objective. Use when spatial relationships matter.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Interactive 3D Explainer Design

## Purpose
Make a 3D scene teach a concept. The model, camera, labels, controls, and sequence should explain cause and effect rather than merely provide an attractive object to rotate.

## When to use
Use for engineering lessons, interactive product explainers, scientific models, component walkthroughs, assemblies, mechanisms, and explorable diagrams where spatial relationships matter.

## When not to use
Do not add 3D when a 2D diagram, timeline, table, or physical equation communicates more clearly. Do not rely on hover-only interactions, tiny labels, color alone, or unverified claims about a real product.

## Inputs
Identify the audience, learning objective, key parts, reference evidence, target device, expected interactions, accessibility requirements, and whether the scene is a live product or illustrative prototype.

## Decision logic
Define the learning sequence before choosing visual effects. Start with the whole object, orient the viewer, reveal one subsystem at a time, and finish by reconnecting the component to the complete system. Each control must answer a viewer question.

## Procedure
1. Write one sentence describing what the viewer should understand after the first minute.
2. Select the smallest useful number of parts and give each stable names and identifiers.
3. Establish an overall camera and purposeful presets that reveal important spatial relationships.
4. Provide selection/isolation controls with visible selected-state feedback and an obvious reset path.
5. Use exploded views, clipping planes, transparency, or x-ray treatment only when they reveal an otherwise hidden relationship.
6. Attach labels to the correct parts and prevent them from covering geometry or colliding with other labels.
7. Use a consistent visual language for fixed, moving, selected, hidden, and uncertain components.
8. Add keyboard access, touch-sized controls, persistent text labels, visible focus, and a non-motion way to inspect important states.
9. Respect reduced-motion preferences. Provide pause/reset and never trap the visitor in a scripted tour.
10. Compose desktop and mobile layouts intentionally; do not merely shrink a dense desktop control panel.
11. Keep the model's coordinate system and scene scale consistent. Provide a scale cue when it helps interpretation.
12. Verify the scene without sound, animation, color discrimination, or a high-end GPU.

## Output contract
Provide a story outline, scene hierarchy, part naming scheme, interaction map, camera plan, responsive layout, keyboard/touch behavior, reduced-motion approach, and visual-review checklist.

## Failure modes
- **Orbit without understanding:** add camera presets that answer specific questions.
- **Too many controls:** remove controls that do not reveal a relationship.
- **Unclear part selection:** add persistent labels and selected-state feedback.
- **Cutaway hides context:** provide a reset and whole-object comparison.
- **Color-only encoding:** add text, shape, outline, or icon distinctions.
- **Mobile becomes unreadable:** recompose for a deliberate inspector panel.
- **Auto-tour blocks the visitor:** stop it immediately after user input.

## Quality gate
A first-time viewer can orient themselves, inspect the critical part, return to the whole system, and understand the cause/effect sequence with keyboard or touch controls. The scene remains usable with reduced motion and on a modest device.

## Example
Explain a centrifugal pump with a whole-machine view, casing cutaway, selectable impeller and shaft, conceptual flow-direction overlay, and an inspector showing inlet/outlet and rotation direction. Clearly label the flow path conceptual unless an appropriate fluid model supports stronger claims.

## Related skills
machine-teardown-simulator, simulation-controls-and-subsystem-inspection, scientific-visualization-storytelling, simulation-visual-regression
