---
name: physics-model-validation
description: Build and check simplified physical models with dimensional consistency, explicit assumptions, reference cases, numerical tests, uncertainty, and honest limits. Use when a visualization displays calculated engineering or scientific quantities.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Physics Model Validation

## Purpose
Turn a physical explanation into a model whose variables, equations, units, assumptions, and limits can be inspected and tested. Prevent an attractive animation from being mistaken for a correct physical simulation.

## When to use
Use for forces, torque, energy, mechanical motion, pressure, flow, heat, electrical behavior, simple flight/vehicle dynamics, and any visualization whose readouts depend on calculated quantities.

## When not to use
Do not use a simplified model to certify equipment, predict safety-critical loads, replace a validated solver, or guide real-world operation without qualified engineering review. Do not infer missing values and present them as measurements.

## Inputs
Identify the physical question, system boundary, independent variables, outputs, available measurements, governing references, units, operating range, and acceptable error. Request a manual, datasheet, paper, or measured sample when its absence materially changes the result.

## Decision logic
Choose the simplest model that answers the question and can be checked independently. Separate measured inputs, sourced constants, inferred values, assumptions, and unknowns. State whether each result is analytic, numerical, empirical, illustrative, or hybrid.

## Procedure
1. Draw the system boundary and list inputs, outputs, internal states, and external influences.
2. Create a variable table with symbol, meaning, unit, source, confidence, valid range, and whether measured or assumed.
3. Choose equations appropriate to the physical regime. List omitted effects such as friction, backlash, turbulence, compressibility, thermal losses, compliance, and control delay.
4. Perform dimensional analysis on every equation. Convert units at boundaries and use one consistent internal unit system.
5. Check limiting cases: zero input, maximum supported input, sign reversal, steady state, symmetry, and singular configurations.
6. Derive at least one hand-calculable reference case and compare the implementation against it before adding complex behavior.
7. Add deterministic tests for invariants, conservation relationships where applicable, monotonicity, bounds, expected phase, and direction.
8. Check numerical stability, solver convergence, timestep sensitivity, and discontinuities. Explain the numerical method and tolerances.
9. Compare results against an authoritative source or measurement. Report the comparison method and residual/error, not only a visual impression.
10. Represent uncertainty with ranges or sensitivity analysis when source parameters are uncertain. Do not invent confidence intervals.
11. Document what the model cannot represent and what evidence is needed before extending its scope.

## Output contract
Provide a model definition, variable/unit table, equations and assumptions, independent reference calculation, automated checks, validation comparison, uncertainty notes, valid operating range, and plain-language limitations.

## Failure modes
- **Unit mismatch:** normalize quantities and add boundary-conversion tests.
- **Plausible but wrong curve:** compare against a hand calculation or trusted reference case.
- **Overfitted constants:** record provenance and test ranges rather than tuning to one image.
- **Unstable integration:** inspect timestep sensitivity and use a suitable solver or analytic solution.
- **Unlabelled simplification:** name omitted effects and restrict the claim.
- **Precision theatre:** round values to match the evidence and expose uncertainty.
- **Circular validation:** do not validate a model only against outputs from itself.

## Quality gate
Every important variable has a unit and provenance; equations pass dimensional checks; an independent reference case matches within a stated tolerance; invalid inputs and edge cases are tested; and limitations remain visible wherever results appear.

## Example
For a slider-crank, define crank radius, rod length, angle, and piston displacement. Derive the geometric solution, test top and bottom dead centre, compare a representative angle with a hand calculation, and label any pressure curve illustrative unless supported by measurements or a documented thermodynamic model.

## Related skills
machine-teardown-simulator, mechanism-kinematics-and-linkage-solving, scientific-visualization-storytelling, simulation-visual-regression
