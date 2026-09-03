# KETHER → CHOKMAH TRANSITION AUDIO V1 — PROPOSAL

**Status:** `PROPOSAL_NOT_CANON`  
**Scope:** Portal 036  
**Related:** #14, #25, `KETHER_AUDIO_CONFLICT_AUDIT_V1.md`

> This proposal defines an HNK-original technical mapping for existing Kether audio vocabulary. It does not claim that the manuscript originally specified this exact stereo construction or that the preset objectively causes a neurological or spiritual state.

## 1. Source boundary

Accessible HNK material already establishes:

- Solfeggio/audio as part of the transmedia practice architecture;
- `528 Hz` in early Kether ritual instructions;
- `432 Hz base` in legacy QR/player copy;
- `Theta` as a binaural/target-state label;
- Portal 036 requires a `Solfeggio de transição`;
- Portal 036 requires comparison against a baseline session without tuner/Solfeggio/sigil.

The source does not define one exact publishable Portal preset.

## 2. Candidate identity

Name:

**Kether → Chokmah Transition V1**

Preset id:

`hnk.audio.kether_chokmah.transition.v1`

## 3. Proposed layered mapping

### Stereo carrier pair

- Left: **429 Hz**
- Right: **435 Hz**
- Arithmetic center: **432 Hz**
- Difference: **6 Hz**

This preserves the legacy `432 Hz base` as the center of the stereo pair while defining an explicit 6 Hz binaural difference.

### Ritual / Solfeggio layer

- **528 Hz** mono-centered ritual tone;
- mixed below the stereo carriers;
- no claim that 528 Hz has an independently established medical effect.

### Target-state label

- canonical product label candidate: `Theta — HNK target label`;
- the app must not display `Theta detected`;
- the 6 Hz difference is a production parameter, not a brain-state measurement.

## 4. Why 6 Hz

`6` is proposed as an HNK-original design value because:

- it sits inside the commonly named theta-frequency range used in binaural-audio practice literature;
- it participates in the HNK structural rhythm `3 / 6 / 12 / 24 / 36 / 72`;
- it allows a symmetric stereo pair around the already source-backed 432 center.

This rationale is product/editorial design, not historical source recovery.

## 5. Duration

Master duration proposal:

**12 minutes / 720 seconds**.

Envelope:

- fade in: 36 seconds;
- main body: 648 seconds;
- fade out: 36 seconds.

`36 + 648 + 36 = 720`.

The Day 036 practice may continue beyond the audio duration if the canonical induction/record workflow requires it. Playback duration does not independently determine Portal completion.

## 6. Mix proposal

Initial mastering target for review:

- stereo carriers remain the structural bed;
- 528 Hz ritual layer is lower in level than carrier bed;
- no harsh transient at start/end;
- no clipping;
- no mandatory ASMR layer;
- no voice embedded in master V1;
- no angel name encoded as hidden speech;
- no ultrasonic/subsonic content intentionally added.

Exact loudness/mastering values are production parameters to be frozen after listening QA.

## 7. Rendering model

Preferred publication path:

1. deterministic offline generation from a versioned script/recipe;
2. lossless master render;
3. distribution derivative generated from master;
4. SHA-256 checksum for master and derivative;
5. Asset Registry entry;
6. app plays published asset rather than improvising frequencies at runtime.

A future real-time synthesizer may reproduce the preset only if its output is regression-tested against the approved recipe.

## 8. Portal relationship

The Sintonizador Angelical loads this preset in Portal mode.

Sequence responsibility remains:

`audio armed → induction → stable depth → approved Kether sigil → 5-minute gnosis → voluntary return → record`.

The audio itself does not automatically trigger the sigil or mark the Portal complete.

## 9. Baseline condition

Day 036 canon already defines baseline as a session without:

- Sintonizador Angelical;
- Solfeggio de transição;
- sigil.

Therefore V1 does **not** create a synthetic “control tone” for the Portal baseline unless a later canonical revision explicitly asks for one.

The comparison remains:

`FULL HNK PORTAL STACK` vs `INDUCTION-ONLY BASELINE`.

## 10. Safety / UX

- headphones are recommended for binaural stereo;
- user controls volume;
- stop/pause always available;
- no penalty for stopping because of discomfort, headache, tinnitus, anxiety or sensory overload;
- default volume should start conservatively;
- no sudden loud events;
- no medical claim;
- no claim of angelic detection/communication from audio signal;
- reduced-sensory mode may offer the ritual workflow without the audio layer if required for accessibility, while marking the practice variant accurately.

## 11. Preset record candidate

```yaml
id: hnk.audio.kether_chokmah.transition.v1
version: 1
status: proposal
scope: day-036
carrier_left_hz: 429
carrier_right_hz: 435
carrier_center_hz: 432
binaural_difference_hz: 6
ritual_tones_hz:
  - 528
target_state_label: "Theta — HNK target label"
ambient_layers: []
duration_seconds: 720
fade_in_seconds: 36
fade_out_seconds: 36
render_mode: deterministic_offline
master_format: lossless
source_basis:
  - "Kether legacy 432 Hz base references"
  - "Kether 528 Hz ritual/Solfeggio references"
  - "Chapter 0 Solfeggio + binaural Theta transmedia architecture"
  - "Day 036 Solfeggio de transição requirement"
provenance: "HNK-original technical reconciliation proposal"
checksum: null
```

## 12. Approval gates

- [ ] owner approves 432-centered stereo model;
- [ ] owner approves 6 Hz difference;
- [ ] owner approves 528 Hz ritual layer for Portal transition;
- [ ] deterministic render script created;
- [ ] listening QA performed at safe volume;
- [ ] 12-minute master rendered;
- [ ] checksum recorded;
- [ ] Asset Registry updated;
- [ ] Sintonizador points to published preset id;
- [ ] Portal 036 QA compares full stack vs induction-only baseline;
- [ ] issue #14 closes only after sigil and Sintonizador references are also published.
