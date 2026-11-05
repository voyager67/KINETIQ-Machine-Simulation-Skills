---
name: parameter-uncertainty-and-sensitivity-analysis
description: Quantify how uncertain model inputs affect simulation outputs using documented ranges, sensitivity measures, and reproducible sampling. Use when estimates or incomplete measurements could change the conclusion.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Parameter Uncertainty and Sensitivity Analysis

## Purpose
Show how much a simulation result depends on uncertain inputs. Separate measured values, source-backed values, estimates, and illustrative assumptions, then determine which inputs most affect the outputs that matter to the explanation.

## When to use
Use when dimensions, loads, efficiencies, friction values, material properties, boundary conditions, or other parameters are incomplete or uncertain. It is useful before claiming that a model is robust or comparing alternative configurations.

## When not to use
Do not use uncertainty analysis to manufacture confidence in an invalid model, infer safety margins, replace qualified engineering review, or certify a design. Do not assign probability distributions without evidence. Do not report more precision than the source data or numerical method supports.

## Inputs
Collect the model equations or runnable baseline, output quantities of interest, parameter values, units, source/provenance, plausible bounds or probability information, dependencies between inputs, and acceptable compute budget. Identify which inputs are measured versus assumed.

## Decision logic
Start with a transparent range or one-at-a-time sensitivity check before using more complex sampling. Use probabilistic methods only when distributions and dependencies have a defensible basis. Keep uncertainty in inputs separate from numerical solver error, measurement error, and model-form limitations.

## Procedure
1. List every parameter that materially affects the chosen outputs. Record value, unit, source, confidence, lower/upper bounds, and whether it is measured, sourced, estimated, or illustrative.
2. Select output quantities before running the analysis, such as speed ratio, peak displacement, cycle time, force trend, or temperature rise.
3. Check baseline model validity first. Uncertainty analysis cannot correct a wrong equation, inconsistent unit, missing physical effect, or invalid boundary condition.
4. Define plausible input ranges from measurements, source tolerances, published uncertainty, or explicit scenario assumptions. Do not invent statistical distributions to make a chart look scientific.
5. Identify dependencies and correlated parameters. Do not vary physically linked values independently when doing so would create impossible combinations.
6. Run a one-at-a-time sweep for each important parameter to reveal direction and approximate sensitivity. Keep other inputs at the documented baseline.
7. When justified, use a reproducible sampling method such as a bounded grid or seeded Monte Carlo sample. Record the method, sample count, seed, and any rejected combinations.
8. Propagate each valid input set through the same model version. Capture the output range, median or other stated summary, and any threshold crossing without implying a formal reliability guarantee.
9. Rank inputs using a clearly described sensitivity measure. Avoid comparing raw slopes across parameters with different units without normalization.
10. Check edge cases and inspect whether outputs change smoothly. Investigate discontinuities, solver failures, and implausible combinations rather than dropping them silently.
11. Visualize uncertainty with bands, intervals, or scenario comparisons. Label their meaning and avoid displaying unsupported confidence intervals.
12. Record which additional measurement would reduce uncertainty most. Update the result when better evidence is supplied and preserve the prior run metadata for comparison.

## Output contract
Deliver an uncertainty register, baseline model/version, assumptions on ranges or distributions, method and reproducibility settings, output ranges, sensitivity ranking, failed-run notes, plots or tables, and a prioritized list of measurements that would improve confidence.

## Failure modes
- **Distribution without evidence:** use bounded scenarios or request data instead.
- **Correlated values sampled independently:** encode the dependency or constrain valid samples.
- **Sensitivity mistaken for causality:** state the tested model context and parameters.
- **False confidence from many samples:** explain model-form and evidence limitations.
- **Over-precise outputs:** round to the resolution supported by inputs and solver.
- **Invalid samples hidden:** report rejection criteria and count, including solver failures.

## Quality gate
Input provenance and ranges are documented; baseline model checks pass; sampling is reproducible; dependencies are respected; output intervals are described accurately; invalid runs are reported; and the conclusions identify what remains uncertain.

## Example
A gearbox explainer has an estimated efficiency and one uncertain pulley diameter. Sweep each input separately to see its effect on output speed and power, then run a seeded scenario sample only if defensible ranges exist. Report the parameter that dominates the result and recommend measuring that dimension before presenting a precise readout.

## Related skills
physics-model-validation, engineering-reference-reconstruction, drivetrain-power-transmission-analysis, thermal-system-modelling-and-heat-transfer-visualization, scientific-visualization-storytelling
