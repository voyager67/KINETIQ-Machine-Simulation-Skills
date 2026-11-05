---
name: scientific-visualization-storytelling
description: Present simulation and experimental data with correct units, honest scales, clear uncertainty, traceable provenance, and an explanatory narrative. Use when charts or scientific overlays support a simulator.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Scientific Visualization Storytelling

## Purpose
Help viewers understand scientific and engineering data without losing the evidence behind it. Visual encodings must respect variables, units, uncertainty, and the limitations of the underlying measurements or model.

## When to use
Use for simulation dashboards, experimental plots, engineering explainers, force/flow/temperature overlays, scientific animations, field measurements, and educational visualizations where numerical evidence supports a claim.

## When not to use
Do not use decorative charts to imply a result that has not been measured or computed. Do not hide outliers, truncate axes deceptively, smooth meaningful discontinuities away, or invent statistical confidence.

## Inputs
Collect source data, variable definitions, units, sampling method, coordinate system, time range, uncertainty/error estimates, sample count, audience, and the specific question the visual should answer.

## Decision logic
Choose the simplest encoding that reveals the relationship. Distinguish measured observations, model predictions, interpolated values, and illustrative content. Include uncertainty when it affects interpretation, but only when the source supports it.

## Procedure
1. Write the question the viewer should be able to answer from the visual.
2. Inspect schema, missing values, ranges, units, sampling interval, and data provenance.
3. Classify variables as categorical, ordinal, continuous, spatial, temporal, or vector-valued.
4. Choose a fit-for-purpose encoding: line for time series, scatter for relationships, bars for categories, field/vector views for spatial quantities, or small multiples for comparisons.
5. Label axes, legends, coordinate frames, reference points, and units explicitly.
6. Select scales and normalization deliberately. Explain logarithmic, clipped, normalized, or nondimensional axes.
7. Show sample count and uncertainty/error bars only when supported by the underlying data or model.
8. Use consistent visual meaning for a variable across views and provide non-colour distinctions.
9. Tie annotations to real data points, events, or model states. Avoid unsupported causal language.
10. Add source metadata, processing steps, and reproducible parameters.
11. Review at target display size and check whether the takeaway remains valid without animation or narration.
12. Keep measured values and predicted values visually distinct in overlays and legends.

## Output contract
Deliver a question-led visual plan, data/provenance summary, variable and unit definitions, chart/scene specification, uncertainty treatment, annotations, transformation notes, and limitations.

## Failure modes
- **Pretty but ambiguous:** add units, scale, reference range, and a clear comparison.
- **Misleading axis:** explain normalization or choose a scale that preserves interpretation.
- **Unsupported uncertainty:** omit fabricated intervals and describe missing evidence.
- **Over-annotation:** keep labels that improve interpretation and remove decorative noise.
- **Colour-only meaning:** add symbols, line styles, direct labels, or patterns.
- **False causality:** describe correlation or model output accurately; reserve causal claims for suitable evidence.
- **Hidden processing:** record filtering, interpolation, normalization, and discarded observations.

## Quality gate
The reader can identify variables, units, source, and main comparison; annotations match the data; uncertainty and transformations are disclosed; and the visual does not claim more than the evidence supports.

## Example
Visualize torque and angular speed over one motor cycle. Keep units on both axes, identify operating phases from the model timeline, overlay measured values and simulated curves with distinct styles, and label model-only values as predictions.

## Related skills
physics-model-validation, machine-teardown-simulator, timeline-driven-animation-capture, simulation-visual-regression
