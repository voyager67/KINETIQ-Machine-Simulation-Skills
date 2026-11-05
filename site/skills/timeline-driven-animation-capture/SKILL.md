---
name: timeline-driven-animation-capture
description: Create deterministic animation timelines and repeatable still/video capture so a simulator motion, camera, labels, and optional audio remain synchronized. Use when building a guided tour, repeatable capture, or exportable demo.
license: "CC BY-NC-ND 4.0"
---

# KINETIQ Timeline-Driven Animation and Capture

## Purpose
Make an animation reproducible at any requested timestamp. One shared timeline should control camera moves, machine state, labels, guided-tour beats, and optional sound so the live page and exported film cannot drift apart.

## When to use
Use when a simulator needs a guided tour, repeatable screenshot states, engineering film, regression captures, or audio synchronized to mechanism events.

## When not to use
Do not add video tooling to a simple interactive page. Do not claim frame-accurate output when frames were sampled irregularly. Do not use music or sound assets without clear rights and provenance.

## Inputs
Collect duration, frame rate, canvas dimensions, viewport/device pixel ratio, story beats, camera path, machine input timeline, captions, audio requirements, output format, and available local capture tools.

## Decision logic
Represent animation as an explicit timeline. Prefer a pure render function that derives visual state from time and immutable configuration. For stateful physics, use fixed-step integration or precompute a deterministic trajectory. Keep runtime interaction and capture behavior on the same state model.

## Procedure
1. Write a beat sheet with start/end times, camera, machine input, selected parts, labels, and intended viewer takeaway.
2. Choose one timebase and frame-rate convention. Define whether timestamps refer to frame starts, centres, or exact seconds.
3. Implement a deterministic state function. Seed procedural randomness and keep wall-clock time out of captured frame rendering.
4. Derive machine state, UI readouts, camera, captions, and visual emphasis from the same timeline.
5. Use fixed-step integration or a precomputed table for stateful physics; verify repeated requests for the same timestamp return the same state.
6. Make the live page use the same state function as the capture pipeline.
7. Add explicit pause, seek, and resume. Manual visitor input pauses or overrides the automatic tour without mutating the authored timeline.
8. Capture frame zero and each beat boundary before rendering the full clip. Inspect contact sheets and full-resolution transition frames.
9. Check local browser automation and encoder availability before use. Ask before installing missing packages or downloading binaries.
10. Keep audio optional. Use original, public-domain, or properly licensed assets; align cues to the same timeline and record their source.
11. Record output dimensions, frame rate, codec, browser, device pixel ratio, and any capture settings.
12. Re-render after changes to geometry, typography, camera, timing, or encoding settings.

## Output contract
Provide the beat sheet, timeline representation, deterministic render contract, capture procedure, preview frames/contact sheet, final media metadata, asset provenance, and review notes.

## Failure modes
- **Frame drift:** make render state a function of timestamp or fixed-step checkpoints.
- **Unsynchronized gauges:** read display values from the same simulated state as the scene.
- **Random capture differences:** seed procedural behavior and remove wall-clock dependencies.
- **Empty opening frame:** compose and inspect a meaningful first frame.
- **Unreadable transitions:** hold important states and inspect frames immediately before and after each transition.
- **Audio mismatch:** derive cue timing from the beat sheet and verify the encoded output.
- **Missing capture tool:** deliver the interactive page or stills and explicitly state that video export was not performed.

## Quality gate
Repeated captures of the same timestamp produce the same state; live and recorded scenes agree; the opening frame communicates the subject; transitions are reviewed; media metadata and audio provenance are recorded; and completion claims match the inspected file.

## Example
Create a 20-second gearbox tour at 30 fps. Show the whole assembly, isolate the input shaft, reveal the gear pair, demonstrate the output ratio, and return to the whole assembly. Derive each state from timeline time and inspect the contact sheet before exporting video.

## Related skills
machine-teardown-simulator, simulation-controls-and-subsystem-inspection, offline-simulator-packaging, simulation-visual-regression
