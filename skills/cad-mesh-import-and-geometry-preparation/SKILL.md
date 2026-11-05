---
name: cad-mesh-import-and-geometry-preparation
description: Prepare locally supplied CAD and mesh assets for reliable machine visualization by checking scale, units, transforms, topology, normals, and simplification. Use when importing complex geometry into a simulator.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ CAD and Mesh Import Preparation

## Purpose
Turn supplied CAD or mesh files into predictable, lightweight scene assets without silently changing their engineering meaning. This skill covers asset intake, geometric hygiene, coordinate normalization, and presentation-ready derivatives. It does not certify a part for manufacture or use.

## When to use
Use when a simulator receives STEP, STL, OBJ, glTF, GLB, or other locally available geometry; when parts arrive at inconsistent scales or origins; or when large assemblies need safe simplification for an interactive viewer.

## When not to use
Do not use this workflow to bypass access controls, remove digital-rights restrictions, or redistribute proprietary geometry. Do not infer tolerances, material properties, hidden internal features, or manufacturability from a display mesh. Do not repair a source file destructively; do not run unknown import scripts or downloaded converters.

## Inputs
Record the supplied file paths, file formats, source and revision, permission to use, units if known, assembly structure, expected coordinate convention, target renderer, and intended level of detail. Work on copies and preserve the original files unchanged.

## Decision logic
Prefer a neutral CAD source when available and a triangulated mesh only when its limitations are acceptable. Keep an engineering source asset separate from any simplified render asset. Fix scale, orientation, and transforms before visual cleanup. If unit metadata is absent, ask for a known dimension rather than guessing from the apparent size on screen.

## Procedure
1. Inventory only the files explicitly supplied for the project. Record filenames, formats, file sizes, and source/revision notes; do not search unrelated folders.
2. Confirm that each asset may be used and redistributed in the intended deliverable. Keep confidential or restricted geometry out of a public repository.
3. Identify the import path and supported format using already-installed local tools. Do not silently install extensions, run shell commands, or download converters; ask before any such action.
4. Establish the unit system from file metadata or a known reference dimension. Compare at least one dimension with the source and record the scale factor. Never infer units from visual appearance alone.
5. Normalize origin and orientation using a documented coordinate frame. Preserve the source transform and describe every transform applied to the presentation copy.
6. Inspect missing faces, duplicate vertices, inverted normals, non-manifold edges, self-intersections, disconnected fragments, and open boundaries where the chosen format exposes those checks.
7. Distinguish intentional open surfaces, thin walls, threads, cosmetic details, and genuinely broken topology. Do not close or smooth geometry automatically when doing so would change a meaningful feature.
8. Separate assembly components into stable named parts when the source structure supports it. Retain part identifiers and parent-child relationships; do not merge moving components merely to reduce draw calls.
9. Create simplified display meshes only as derived assets. Use a measured polygon budget, preserve silhouette and interfaces, and compare critical dimensions and landmarks before and after simplification.
10. Generate or retain collision proxies separately from render meshes. Label approximate collision geometry as approximate and never use it as dimensional evidence.
11. Test representative views, clipping, part isolation, and animation pivots in the actual target scene. Check that normals, scale, and axes remain correct after export and re-import.
12. Record conversion tools and versions only when actually used, licence/provenance, source-to-derived mapping, known defects, and checksums when useful. Do not include temporary files or unrelated user data in the package.

## Output contract
Deliver an asset register, source-to-derived map, unit and coordinate-frame declaration, topology/normal findings, simplification report, preserved-part hierarchy, licence notes, and a list of unresolved geometry questions. Keep original files separate from derived viewer assets.

## Failure modes
- **Unknown scale:** stop and request a known dimension; do not guess.
- **Flattened assembly:** retain separate moving parts and stable identifiers.
- **Visual repair changes the design:** preserve the source and document any display-only patch.
- **Over-simplified interfaces:** protect holes, joints, mating faces, and motion-critical features.
- **Incorrect normals:** inspect orientation and lighting after export, not only in the source tool.
- **Restricted asset leakage:** omit the file from public output unless redistribution permission is explicit.

## Quality gate
The original source remains unchanged; units, transforms, and part identity are traceable; display meshes are clearly marked as derivatives; important interfaces survive simplification; the target scene imports the assets correctly; and no private or unlicensed geometry is packaged.

## Example
Prepare a locally supplied gearbox assembly for a browser explainer. Preserve the source assembly, confirm millimetres using a documented shaft diameter, normalize the coordinate frame, keep gears and shafts as separate parts, create lower-detail outer housings for display, and report any mesh defects instead of silently repairing them.

## Related skills
engineering-reference-reconstruction, assembly-coordinate-frames-and-joint-authoring, low-end-3d-performance-tuning, offline-simulator-packaging
