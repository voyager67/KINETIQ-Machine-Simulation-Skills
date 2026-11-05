---
name: engineering-reference-reconstruction
description: Reconstruct a machine or mechanism from manuals, photographs, dimensioned drawings, and other references while tracking provenance, units, missing measurements, and confidence. Use when modeling must start from incomplete or conflicting references.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Engineering Reference Reconstruction

## Purpose
Convert scattered reference material into a defensible model specification. The goal is not to guess a machine into existence; it is to establish what is known, what can be inferred, and what still needs measurement before simulation begins.

## When to use
Use before building a simulator from photos, technical manuals, assembly drawings, datasheets, maintenance documents, motion footage, or incomplete descriptions. It is especially useful when multiple sources disagree or when scale and perspective make dimensions uncertain.

## When not to use
Do not treat a perspective photograph as a dimensioned drawing. Do not infer hidden internal geometry with unjustified confidence. Do not bypass copyright, confidentiality, export controls, or data-use restrictions on supplied references.

## Inputs
Collect source files or URLs, machine variant/model/year where relevant, drawing scales, known dimensions, units, orthographic views, motion footage, operating context, and the exact questions the simulator must answer. Ask for a better reference when a missing fact materially changes the geometry or behavior.

## Decision logic
Rank evidence by its ability to establish the required fact. Prefer dimensioned drawings and manufacturer manuals for dimensions, authoritative operating documentation for sequence, and photographs/video for visible shape and motion. Treat third-party images as supporting evidence, not universal specifications. Record conflicts instead of silently choosing one source.

## Procedure
1. Inventory each reference with title, publisher/creator, URL or filename, publication/revision date if known, access date, license or permission status, and the claims it can support.
2. Classify evidence as dimensioned, orthographic, perspective, schematic, descriptive, measured, or illustrative.
3. Extract dimensions into a table with quantity, symbol, value, unit, source location/page, confidence, and any conversion applied.
4. Normalize units once. Keep the original value and unit alongside the normalized value so conversion errors can be audited.
5. Identify machine variant and configuration. Note differences such as left/right-hand versions, model revisions, optional equipment, and changed geometry.
6. Reconcile multiple views. Use shared features and centre lines to establish coordinate frames; account for perspective distortion before estimating ratios.
7. Separate visible dimensions from inferred internals. Assign confidence labels such as high (explicit dimension), medium (multiple consistent views), low (single perspective estimate), or unknown.
8. Build a parts list with stable part IDs, parent/child relationships, material or appearance only when supported, motion type, joint connections, and reference evidence.
9. Reconstruct operating phases from authoritative sequence documentation or observable timing. Do not infer a causal mechanism from a video sequence alone.
10. Create a gap list. For each missing value, estimate the impact on model fidelity and specify the best next measurement or source.
11. Choose whether to proceed with exact, approximate, or conceptual geometry. Make the decision explicit in the model brief and label uncertain parts in the viewer where useful.

## Output contract
Provide a source register, normalized parameter table, parts hierarchy, coordinate convention, confidence map, conflicting evidence list, assumptions/gaps, and a recommendation on whether there is enough evidence for a detailed, approximate, or conceptual simulator.

## Failure modes
- **Mixed machine variants:** verify identifiers and revision details before merging data.
- **Perspective mistaken for scale:** use known reference dimensions and state the uncertainty of derived measurements.
- **Unit drift:** retain original units and test conversions at data boundaries.
- **Untraceable estimates:** attach a source/page or label the value as an assumption.
- **Unsupported internals:** show a simplified or transparent representation rather than inventing a precise hidden assembly.
- **License uncertainty:** omit the asset or obtain permission; attribution alone is not permission.

## Quality gate
Every important modeled dimension is traceable to a source or marked as estimated; units and machine variant are explicit; conflicting evidence remains visible; internal geometry is not presented as observed when it is inferred; and unresolved gaps are documented before detailed modeling.

## Example
Reconstruct a landing-gear assembly from a maintenance manual, an orthographic drawing, and a short deployment video. Use the drawing for pivot locations, the manual for sequence and terminology, and the video only to compare visible motion. Record any hidden linkage length as unknown until a reliable source is found.

## Related skills
machine-teardown-simulator, mechanism-kinematics-and-linkage-solving, physics-model-validation, scientific-visualization-storytelling
