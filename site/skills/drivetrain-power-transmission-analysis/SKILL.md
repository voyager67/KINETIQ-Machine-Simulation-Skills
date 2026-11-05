---
name: drivetrain-power-transmission-analysis
description: Analyze educational drivetrain models by tracing speed, torque, direction, power, and idealized losses through gears, belts, chains, and shafts. Use when a machine explainer needs consistent power-flow readouts.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Drivetrain and Power-Transmission Analysis

## Purpose
Explain how rotational motion and power pass through a simplified drivetrain. Keep gear ratios, direction changes, torque, speed, and power mutually consistent, and expose the assumptions behind ideal or approximate efficiency values.

## When to use
Use for gearboxes, belt and chain drives, pulley systems, shafts, couplings, and educational machine explainers that show input/output speed or torque. Use with the kinematics skill when the geometry and motion of gears or linkages also need to be solved.

## When not to use
Do not use this skill to size a real drive, select components for a real installation, certify fatigue life, establish allowable loads, or provide machinery operating instructions. Do not invent friction, efficiency, material, or load data. If a value is not documented, present an idealized or illustrative model and label it clearly.

## Inputs
Collect the drivetrain topology, tooth counts or pulley diameters if documented, rotation directions, shaft connections, input speed and torque, load assumptions, efficiency evidence, unit system, and intended level of realism. Identify any missing ratio or loss data.

## Decision logic
Trace power from source to output and compute each stage from documented geometry or explicitly stated assumptions. Separate kinematic ratio from power loss: ideal gearing changes speed and torque but does not create power. If losses are unknown, show ideal results first and optionally provide a clearly labelled sensitivity range rather than a false precise efficiency.

## Procedure
1. Draw a power-flow graph from input to output with one node per rotating shaft and one edge per transmission stage.
2. Assign stable IDs to gears, pulleys, sprockets, belts, chains, shafts, and couplings. Note which elements are physically connected and which are only grouped visually.
3. Record source-backed tooth counts, pitch diameters, centre distances, belt stages, and rotation-direction conventions. Retain units and provenance.
4. Define the ratio convention once, for example output angular speed divided by input angular speed. State whether a sign indicates direction reversal.
5. For a simple external gear pair, derive the speed ratio from tooth counts and reverse direction; for internal gears, belt drives, or multi-stage trains, state the appropriate geometry and direction rules used.
6. Calculate ideal angular speed and torque with consistent ratio conventions. For an ideal lossless stage, check that input and output power agree within numerical tolerance.
7. Apply efficiency only when the value is sourced or explicitly illustrative. For a stage with efficiency eta, keep the power loss visible and avoid applying the same loss twice.
8. Track rotational direction through every stage, including idlers and crossed belt paths when applicable. Verify the final direction against a simple hand-worked case.
9. Model shaft power using consistent angular-speed units. Convert rpm to radians per second at a single well-defined boundary; do not mix rpm and rad/s inside one equation.
10. Add load response only when the model defines a load or torque balance. Otherwise show transmission ratios without implying a dynamic load simulation.
11. Synchronize input and output gauges, gear labels, arrows, and animation from the same drivetrain state.
12. Test single-stage and multi-stage reference cases, zero input, direction reversal, and plausible boundary inputs. Record which outputs are ideal, estimated, or measured.

## Output contract
Provide a power-flow graph, ratio convention, stage-by-stage speed and torque table, direction map, power-balance checks, loss assumptions, input/output units, reference cases, and a concise limitations statement.

## Failure modes
- **Ratio convention flips:** write the convention in the output and test a known gear pair.
- **Power appears from nowhere:** check torque, speed, and efficiency at every stage.
- **Efficiency counted twice:** assign each loss to one transmission stage only.
- **Direction arrows disagree:** derive arrow direction from signed angular velocity.
- **Unsupported component data:** replace false precision with ideal values or a visible assumption range.
- **Visual animation masks wrong math:** validate the numerical state before reviewing the animation.

## Quality gate
Every ratio and direction is traceable; speed, torque, and power use consistent units; the loss model is explicit; ideal power balance is checked; and the visualization never presents an illustrative estimate as a measured drivetrain specification.

## Example
Explain a two-stage gearbox with documented tooth counts. Calculate the signed speed ratio at each mesh, derive output speed and ideal torque from the input state, optionally show a clearly hypothetical efficiency slider, and make all readouts update from the same calculated shaft state.

## Related skills
mechanism-kinematics-and-linkage-solving, physics-model-validation, assembly-coordinate-frames-and-joint-authoring, scientific-visualization-storytelling
