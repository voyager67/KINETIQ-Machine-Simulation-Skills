---
name: fluid-power-system-visualization
description: Create clearly bounded educational models of hydraulic and pneumatic circuits, showing flow paths, pressure states, valves, actuators, and simplified continuity relationships. Use when fluid power is part of a machine explainer.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Fluid-Power System Visualization

## Purpose
Make fluid-power concepts understandable without implying that a simplified animation is a validated hydraulic or pneumatic design. Represent components, flow paths, pressure differences, and actuator motion with assumptions that remain visible to the viewer.

## When to use
Use for educational explainers of pumps, reservoirs, pipes, valves, cylinders, accumulators, compressors, and pneumatic actuators. It can support a conceptual machine cutaway or a simplified lumped-parameter demonstration.

## When not to use
Do not design, rate, commission, troubleshoot, or prescribe operating settings for real pressurized equipment. Do not infer safe pressure limits, component compatibility, relief settings, or stored-energy hazards. Do not claim to perform computational fluid dynamics (CFD) when using a few equations or animated particles. Escalate real equipment decisions to qualified engineering review and validated tools.

## Inputs
Collect a circuit diagram or source description, component identities, known flow and pressure values, fluid or gas assumptions, actuator geometry if provided, boundary conditions, units, and the desired fidelity. Determine whether the model is symbolic, lumped-parameter, or backed by a validated flow solver.

## Decision logic
Begin with a readable circuit graph and conservation rules. Use a symbolic path animation when quantitative data is missing. Use a lumped model only when its assumptions and boundary conditions can be stated. Do not substitute decorative moving particles for a computed flow field, and do not show a precise pressure value without a defined model or source.

## Procedure
1. Build a directed circuit graph with stable component IDs, connection ports, and named branches. Keep supply, return/exhaust, and control paths visually distinct.
2. Record each component's role from an authoritative diagram or supplied reference. Mark inferred connections and unknown components instead of silently guessing.
3. Declare fluid/gas assumptions, units, sign conventions, and the reference locations for pressure and flow measurements.
4. For a conceptual model, animate flow direction only along documented or explicitly assumed paths. Label the flow as illustrative.
5. For a lumped quantitative model, identify volumes, restrictions, valves, actuator areas, compressibility assumptions, and boundary conditions required by the chosen equations.
6. Apply continuity and pressure/force relationships only within their valid assumptions. State where compressibility, transient effects, leakage, heat, cavitation, turbulence, or two-phase behavior are omitted.
7. Keep pressure, flow, actuator displacement, and valve state tied to one model state. Avoid independent animations that can imply impossible combinations.
8. Distinguish a command signal from actual valve spool or actuator state. Do not imply control-loop fidelity when no controller model exists.
9. Show units and measurement locations beside readouts. If source values are absent, use qualitative labels such as low/relative/high only when the comparison is justified.
10. Include pause, reset, and a static circuit view. Make fluid direction and component state understandable without motion or color alone.
11. Test disconnected branches, closed paths, zero-flow states, direction changes, and boundary conditions within the declared educational model.
12. Document model fidelity, omitted physics, data provenance, and the fact that the explainer is not a real equipment operating guide.

## Output contract
Provide a circuit graph, component glossary, flow-path map, modelling-fidelity label, assumptions and boundary conditions, units and readout locations, representative state checks, and limitations. Separate sourced values from illustrative inputs.

## Failure modes
- **Particles imply real CFD:** label them as path indicators unless a real velocity field drives them.
- **Pressure values lack a reference:** name the measurement point and reference pressure.
- **Wrong connection topology:** verify every port against the supplied diagram.
- **Incompressible assumption used for gas:** state compressibility limits or choose a suitable model.
- **Decorative valve animation:** derive valve and actuator states from the same circuit model.
- **Operational misuse:** remove actionable settings and state that real equipment requires qualified review.

## Quality gate
The circuit topology is traceable; model fidelity is honestly labelled; units, boundary conditions, and measurement locations are explicit; the animated state obeys the declared simplified relationships; and no result is presented as a safe operating specification.

## Example
Create an educational hydraulic-cylinder explainer from a supplied circuit drawing. Show the pump, directional valve, cylinder, and return path; animate only the documented flow route; display qualitative pressure zones if no measured values exist; and label the motion as a conceptual sequence rather than a rated hydraulic design.

## Related skills
engineering-reference-reconstruction, physics-model-validation, scientific-visualization-storytelling, interactive-3d-explainer-design
