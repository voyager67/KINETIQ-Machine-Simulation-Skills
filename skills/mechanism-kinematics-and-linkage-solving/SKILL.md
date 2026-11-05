---
name: mechanism-kinematics-and-linkage-solving
description: Derive and verify motion for linkages, gears, cams, sliders, joints, and constrained assemblies before animating them. Use when a simulator needs physically consistent part positions or motion ratios.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Mechanism Kinematics and Linkage Solving

## Purpose
Turn a mechanism drawing into a solvable set of geometric relationships. Each link should move from a defined input and constraint system, not from independently tuned keyframes that only look plausible.

## When to use
Use for slider-cranks, four-bar linkages, walking mechanisms, gear trains, cams, rack-and-pinion systems, landing gear, robotic joints, folding structures, and assemblies with constrained movement.

## When not to use
Do not invent dimensions from a vague image, treat a visual approximation as a manufacturing design, or assume rigid planar links when compliance, backlash, deformation, impacts, or three-dimensional constraints materially affect the result.

## Inputs
Collect a dimensioned reference, link lengths, gear tooth counts/module or pitch data, joint types, fixed pivots, coordinate system, input variable, operating range, assembly branch, and expected output motion. Identify whether the mechanism is planar or spatial.

## Decision logic
Count degrees of freedom before choosing the solver. Prefer a closed-form solution for a simple mechanism. Use numerical constraint solving only when the geometry requires it, and define convergence tolerance, initial conditions, branch selection, and behavior when a position is unreachable.

## Procedure
1. Identify rigid bodies, fixed frames, joints, and permitted degrees of freedom. Give each component and joint a stable identifier.
2. Define coordinates, units, positive rotation direction, and angle convention. Do not mix degrees and radians implicitly.
3. Perform a mobility/degree-of-freedom check. Confirm one selected input determines the intended configuration.
4. Express geometric constraints before writing rendering code. Use fixed link lengths, joint coincidence, gear ratios, pitch geometry, cam profiles, or other justified relationships.
5. Solve a known reference pose and compare it with the drawing or an independent hand calculation.
6. Select the intended assembly branch explicitly. Track a known initial solution so a numerical solver does not flip between alternate configurations.
7. Derive velocity and acceleration only when the explanation needs them. State the method and numerical differentiation step if used.
8. Handle singularities, dead centres, collisions, travel limits, gear engagement boundaries, and unreachable inputs. Expose invalid states rather than silently forcing an impossible pose.
9. Create a deterministic state function from the independent input to every component transform.
10. Test link-length invariants, joint closure, gear ratios, signed direction, periodicity, boundary positions, and return to the initial pose.
11. Sample multiple points over the complete cycle. Compare numerical geometry against references, not just a single attractive frame.
12. Pass the solved state to the rendering layer; never calculate a second, inconsistent motion path for visual effects.

## Output contract
Deliver a body/joint table, coordinate and unit convention, mobility analysis, governing constraints/equations, solver description, assembly-branch behavior, edge cases, tests/tolerances, valid input range, and a rendering-ready state function.

## Failure modes
- **Too many free variables:** revisit mobility and constraint completeness.
- **Wrong assembly branch:** initialize from a known pose and track the selected branch.
- **Link drift:** derive positions from constraints instead of incrementing transforms independently.
- **Sudden flips:** detect singular configurations and make branch transitions explicit.
- **Gear direction mismatch:** document the signed ratio and rotation axes before animation.
- **Impossible input:** expose an unreachable state and explain the valid range.
- **Pretty but inaccurate motion:** compare link and joint positions numerically through the cycle.

## Quality gate
Constraints remain within declared tolerances over the valid range; gear ratios and directions are tested; branch selection is stable; singular/unreachable configurations have explicit behavior; and the same solved state drives every animated component.

## Example
For a four-bar linkage, identify ground, input, coupler, and output links. Fix the ground pivots, use input crank angle as the independent variable, solve the remaining pivots from circle intersections, check both assembly branches, then test closure and output angle throughout a full revolution.

## Related skills
engineering-reference-reconstruction, machine-teardown-simulator, physics-model-validation, simulation-visual-regression
