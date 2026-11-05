# KINETIQ workflow

## Master sequence

1. **Research:** reconstruct reference geometry, operating phases, provenance, and confidence.
2. **Prepare geometry:** when CAD or meshes are supplied, check units, transforms, topology, and derived display meshes.
3. **Build the assembly:** define part identity, coordinate frames, grounded bodies, joints, and degrees of freedom when motion requires them.
4. **Scope and model:** identify system boundaries, inputs, outputs, and the viewer question; derive kinematics and physics independently of the renderer.
5. **Add domain models:** use drivetrain, fluid-power, or thermal methods only when the machine requires them.
6. **Validate and quantify:** check units, constraints, reference cases, energy/power balances, and the effect of uncertain parameters.
7. **Visualize and interact:** build the scene, cameras, labels, cutaways, meaningful controls, isolation, reset, and tour handoff.
8. **Capture and verify:** derive live and recorded views from one deterministic state; assert numerical invariants, test controls, inspect images, and profile target devices.
9. **Package:** bundle local dependencies, test offline, scan archive paths and text, and document limitations.

## Deliverables

- Machine/model brief from `templates/machine-model-brief.md`.
- Part/parameter register from `templates/parts-and-parameters.csv`.
- Reproducible tour timeline based on `templates/animation-timeline.json`.
- Verification report using `templates/simulation-verification-checklist.md`.
- Source project and portable build, if requested.

Do not run all skills by default. Choose the smallest skill set that covers the real task.
