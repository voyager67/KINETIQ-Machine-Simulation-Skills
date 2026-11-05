# Simulation verification checklist

## Evidence and model
- [ ] Machine variant and reference sources are recorded.
- [ ] Important parameters have units, provenance, and confidence.
- [ ] Equations pass dimensional checks.
- [ ] At least one independent reference calculation is compared.
- [ ] Valid range, singularities, and omitted effects are documented.

## Motion and readouts
- [ ] One shared state drives all moving parts and displayed numbers.
- [ ] Joint/link/gear constraints stay within stated tolerances.
- [ ] Reset returns to the expected initial state.
- [ ] Unreachable inputs and assembly branches have explicit behavior.

## Interaction and accessibility
- [ ] Play, pause, input, reset, isolate, explode, and cutaway controls work.
- [ ] Keyboard and pointer behavior are tested.
- [ ] Mobile/touch layout is checked where relevant.
- [ ] Reduced-motion behavior exists.
- [ ] User input always interrupts or overrides the guided tour.

## Visual and performance
- [ ] Opening frame communicates the subject.
- [ ] Whole-machine, subsystem, and difficult transition states are inspected.
- [ ] Labels do not clip or cover important geometry.
- [ ] Low-power quality tier remains understandable.

## Offline and privacy
- [ ] Artifact opens with networking disabled.
- [ ] No remote API, analytics, telemetry, CDN, or credential is embedded.
- [ ] Dependencies and media licences are documented.
- [ ] Archive contains no `.git`, `.env`, caches, private paths, or unrelated files.

## Handoff
- [ ] Source and build paths are listed.
- [ ] Commands and checks actually run are recorded.
- [ ] Numerical, functional, visual, and performance evidence are separated.
- [ ] Educational model is not described as certified engineering output.
