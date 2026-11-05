---
name: thermal-system-modelling-and-heat-transfer-visualization
description: Build transparent educational thermal models using heat capacity, thermal resistance, conduction, convection, radiation, and energy balances. Use when machine explainers need temperature or heat-flow behaviour.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Thermal System Modelling and Visualization

## Purpose
Explain where heat enters, moves, accumulates, and leaves a simplified machine system. Keep temperature displays tied to an explicit energy model and distinguish a lumped educational approximation from a spatial thermal simulation.

## When to use
Use for motors, brakes, engines, bearings, heat exchangers, enclosures, electronics housings, and other machine explainers where temperature change or heat flow is important to understanding the mechanism.

## When not to use
Do not use a simplified model to determine safe operating temperature, material limits, fire risk, component sizing, cooling-system ratings, or product compliance. Do not claim finite-element or computational-fluid-dynamics accuracy without an appropriate validated solver and evidence. Do not invent material properties or boundary conditions.

## Inputs
Collect geometry or lumped component volumes, mass and material data if available, heat sources, ambient conditions, thermal contact assumptions, airflow or coolant assumptions, initial temperatures, time horizon, units, and desired model fidelity.

## Decision logic
Use a lumped thermal network when the component can reasonably be represented by a small number of near-uniform temperature nodes. Use a spatial model only when gradients matter and a suitable numerical method is available. If material properties or boundary conditions are missing, use a qualitative heat-path visualization or expose the uncertain parameter rather than inventing a precise temperature.

## Procedure
1. Draw a thermal network showing heat-generating nodes, thermal storage, conductive paths, interfaces, and heat-rejection boundaries.
2. Identify heat sources and mark each as measured, documented, estimated, or illustrative. Do not infer losses solely from how hot a part appears in a photograph.
3. Record thermal mass, heat capacity, conductivity, emissivity, contact resistance, and convection assumptions only where supported by sources or declared examples.
4. Define the system boundary, ambient or coolant temperature, initial conditions, and sign convention for heat flow.
5. For a lumped node, use an explicit energy balance: stored energy changes according to heat added minus heat removed. Keep the equation and units visible in the model notes.
6. Represent conduction, convection, and radiation as distinct mechanisms. State when linearized or constant-coefficient approximations are used.
7. Choose a time step appropriate to the fastest modelled thermal time constant. Check numerical stability and verify that energy does not drift without a documented source or sink.
8. Derive temperature labels, heat-flow arrows, and charts from the same state used by the numerical model.
9. Use visual gradients carefully. Include numeric values, units, a legend, and an uncertainty indication where quantitative results exist; otherwise label the colors as qualitative.
10. Test equilibrium, zero heat input, changed ambient conditions, and a simple reference case whose expected trend is known.
11. Compare model outputs with supplied measurements only at matching locations and times. Explain any mismatch instead of tuning parameters solely to fit one screenshot.
12. Document spatial limitations, omitted effects, property sources, and the non-operational nature of the educational visualization.

## Output contract
Provide a thermal network, node/parameter table, equations and assumptions, boundary and initial conditions, time-step rationale, energy-balance checks, temperature/heat-flow visual mapping, reference comparison, and a limitations statement.

## Failure modes
- **Temperature gradient drawn without a model:** use a qualitative label or implement a declared spatial model.
- **Unbounded heat accumulation:** inspect energy sources, sinks, and numerical stability.
- **Material data guessed:** show a range or leave the parameter unresolved.
- **Wrong boundary condition:** specify ambient/coolant temperatures and where heat leaves the system.
- **Color implies exact temperature:** add units and a legend, or mark the display qualitative.
- **Model used as a safety rating:** clearly state the model is educational and not a design or compliance assessment.

## Quality gate
The thermal boundary and energy balance are explicit; every quantitative property has provenance or an uncertainty range; the time integration is checked; visual temperature indicators derive from model state; and no operational or safety limit is inferred from the explainer.

## Example
Build a lumped thermal explanation of a motor housing. Represent winding losses as an illustrative heat source, use a documented or clearly assumed thermal resistance to ambient, show the housing temperature over time, and display a separate qualitative heat-path overlay. Do not present the output as a certified motor temperature rating.

## Related skills
physics-model-validation, parameter-uncertainty-and-sensitivity-analysis, scientific-visualization-storytelling, simulation-visual-regression
