---
name: assembly-coordinate-frames-and-joint-authoring
description: Build a consistent machine assembly graph with named coordinate frames, joint definitions, degrees of freedom, and constraint checks. Use when imported parts must move together as a mechanism.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Assembly Frames and Joint Authoring

## Purpose
Translate a parts hierarchy into a coherent kinematic assembly. This skill focuses on coordinate frames, parent-child relationships, joint placement, degrees of freedom, and constraint consistency so the rendered assembly does not drift, snap, or move in contradictory ways.

## When to use
Use after parts have been identified and before implementing motion for mechanisms, machines, articulated products, or multi-part educational models. It is especially useful when imported CAD assets have different origins or when several joints connect the same moving chain.

## When not to use
Do not use it to claim that a real assembly is safe, correctly toleranced, or suitable for manufacture. Do not infer a hidden joint from appearance alone. Do not prescribe real-world assembly, maintenance, or operation procedures. For a simple rigid object with no moving components, use a static hierarchy instead.

## Inputs
Collect stable part IDs, parent-child relationships, source coordinate systems, known pivot and axis data, allowed motion types, fixed references, expected degrees of freedom, and any measured poses. Identify whether the model is a tree or contains closed constraint loops.

## Decision logic
Choose a fixed reference body first, then express each joint in explicit local frames. Use the simplest constraint set that captures the intended motion without over-constraining the mechanism. Distinguish a visual grouping parent from a physical joint. If joint evidence is incomplete, label the connection as assumed and keep it easy to revise.

## Procedure
1. Create an assembly graph with stable IDs, human-readable names, parent links, and a note describing the evidence for each relationship.
2. Choose a world frame and document axis directions, handedness, origin, and units. Keep that convention consistent across geometry, equations, animation, and readouts.
3. Record each part's source transform before applying scene transforms. Convert transforms explicitly rather than stacking undocumented rotations and offsets.
4. Identify the fixed or grounded body. Avoid grounding multiple bodies unless the mechanism definition explicitly requires it.
5. Define each joint by type, participating bodies, anchor frames, axis or plane, allowed coordinates, limits if known, and source/confidence.
6. Check degrees of freedom before driving the mechanism. For each joint, state what translation or rotation is allowed and which relative motions are constrained.
7. Set joint anchors from geometry or documented references. Validate that the two anchor frames coincide in the intended assembly pose within a stated tolerance.
8. For closed loops, identify redundant or conflicting constraints. Prefer a solver-supported formulation and verify closure numerically; do not hide solver instability with arbitrary visual offsets.
9. Separate physical joint coordinates from presentation transforms such as exploded views, cutaways, or temporary part offsets.
10. Define one authoritative mechanism state. Derive every part transform, label, gauge, and camera annotation from the same state rather than maintaining unrelated animation values.
11. Test neutral, boundary, reversed, and representative intermediate configurations. Check axis direction, sign convention, joint limits, collisions, and continuity.
12. Document assumptions, missing measurements, solver limitations, and any joints simplified for teaching purposes.

## Output contract
Provide an assembly graph, frame convention, joint table, degree-of-freedom summary, grounded-body choice, constraint-loop notes, representative-pose checks, assumptions, and a mapping from solver state to rendered transforms.

## Failure modes
- **Axis mismatch:** show each joint axis and verify its direction in the assembled pose.
- **Transform accumulation:** compute transforms from a clean source frame instead of repeated incremental edits.
- **Over-constraint:** remove redundant constraints or reformulate the loop; do not mask solver errors.
- **Hidden presentation offset:** keep exploded-view transforms outside the physical model state.
- **Unclear evidence:** mark assumed joints and request better drawings or measurements.
- **Unstable motion:** test continuity and closure before adding animation polish.

## Quality gate
The assembly graph is traceable; frames and units are explicit; every joint has a defined type and allowed motion; degrees of freedom are understood; representative poses satisfy constraints; and the viewer's part transforms come from one authoritative state.

## Example
Set up a four-bar linkage from supplied component geometry. Ground one link, define four revolute joints with explicit axes and anchors, check the expected mobility, test loop closure at several crank positions, and keep the later exploded view as a separate presentation layer.

## Related skills
cad-mesh-import-and-geometry-preparation, mechanism-kinematics-and-linkage-solving, physics-model-validation, simulation-controls-and-subsystem-inspection
