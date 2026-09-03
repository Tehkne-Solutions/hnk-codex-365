# SINTONIZADOR ANGELICAL V1 — PROPOSAL

**Status:** `PROPOSAL_NOT_CANON`  
**Scope:** Portal 036 and reusable Kether audio control surface  
**Related:** #14, #25

> The Sintonizador Angelical is proposed as an HNK ritual-audio controller and contextual instrument. It is not a detector of angels, spirits, external entities or objective supernatural frequencies.

## 1. Purpose

Define the product/editorial meaning of `Sintonizador Angelical` so the Portal 036 experience can execute one reproducible sequence without implementation-time invention.

The instrument coordinates:

- canonical Day/cycle context;
- approved audio preset;
- ritual formula metadata;
- session timing;
- user-controlled playback;
- start/stop/return;
- evidence logging.

## 2. Candidate identity

Canonical candidate name:

**Sintonizador Angelical HNK — Kether V1**

Component id:

`hnk.tuner.kether.v1`

## 3. What the tuner IS

A deterministic interface that loads approved HNK metadata and audio assets for a practice/session.

For each supported session it may display:

- Day;
- Sephira;
- cycle/angel name already defined by canonical content;
- formula already defined by canonical content;
- audio preset id/version;
- duration;
- volume control;
- headphones recommendation when binaural content is present;
- session status;
- stop/return control.

## 4. What the tuner IS NOT

It must not:

- scan the environment for entities;
- claim to detect an angel;
- assign a measured Hz value to an angel unless a future canonical source explicitly defines such a mapping;
- say that a user has objectively entered a brain-wave state;
- claim supernatural communication from signal amplitude, microphone input or sensor data;
- convert private journal content into tuning parameters.

## 5. Data contract

Minimum configuration:

```yaml
id: string
version: integer
status: draft | review | approved | published
sephira: string
day: integer | null
cycle: string | null
angel: string | null
formula: string | null
audio_preset_id: string
sigil_asset_id: string | null
duration_seconds: integer
headphones_recommended: boolean
user_volume_control: true
stop_always_available: true
source_basis: []
checksum: string | null
```

Null means unresolved/not applicable and must not be silently filled.

## 6. Portal 036 fixed mode

Portal mode is intentionally constrained.

### Fixed context

- Sephira: `Kether`;
- Day: `036`;
- Level before completion: `1 — Neófito`;
- transition target: `Chokmah`;
- transition result after valid completion: `Level 2 — Iniciado`;
- no new angelic name is introduced by the tuner;
- audio preset must be the separately approved Kether→Chokmah transition preset;
- sigil must be the separately approved Kether Sigil V1 or successor.

### Portal control sequence

`READY → AUDIO_ARMED → INDUCTION → SIGIL_READY → GNOSIS → RETURN → RECORD → COMPLETE`

The tuner does not automatically mark completion merely because playback ended.

## 7. User controls

Always available:

- play/pause;
- stop;
- volume;
- restart current phase;
- return/grounding shortcut;
- reduced sensory mode.

Optional when the published preset supports it:

- ambient layer on/off;
- haptic pulse on/off;
- visual intensity reduced/full.

The user cannot change canonical carrier/ritual-tone parameters inside a canonical Portal run.

## 8. Seven-fragment Crown context

The Portal tuner may visualize the already-derived `Coroa 7/7` as readiness context.

It must not let the user manually toggle Fragment states.

Fragment state is derived from valid completion data for the seven Kether cycles.

## 9. Relationship to audio

The tuner is a controller, not the audio source of truth.

Audio source of truth is a versioned preset/asset record.

The tuner loads:

- `audio_preset_id`;
- asset checksum;
- duration;
- channel/headphone requirements;
- safety notes.

It does not synthesize undocumented parameters at runtime.

## 10. Relationship to sigils

The tuner may reveal or animate an approved sigil.

It may not:

- generate random sigils;
- mutate canonical topology;
- substitute a missing asset with an unrelated occult symbol and call it Kether.

## 11. Evidence

Portal session record should include at minimum:

- tuner version;
- preset version;
- sigil version;
- start/end timestamps;
- completed phases;
- stop/safety events;
- user-reported clarity/orientation;
- return confirmed;
- Portal completion gate result.

Raw private journal text is separate.

## 12. Safety

- volume always user-controlled;
- stop always available;
- headphones warning shown when binaural stereo requires them;
- no penalty for stopping due to discomfort;
- no flashing/strobing requirement;
- reduced-motion and reduced-sensory modes supported;
- app does not claim medical, neurological or supernatural detection.

## 13. Visual behavior

Kether mode should feel like an instrument emerging from the void, not a mixing console dashboard.

Preferred hierarchy:

1. current sacred/context state;
2. central tuner/sigil surface;
3. one primary action;
4. subtle technical metadata;
5. emergency/stop access that remains easy to reach.

## 14. Provenance

If approved:

`HNK-original ritual-audio controller defined for the Kether Portal. It organizes approved canonical metadata and published audio/sigil assets; it does not claim entity detection or objective angel-frequency measurement.`

## 15. Approval gates

- [ ] owner approves functional meaning;
- [ ] Portal fixed mode approved;
- [ ] data contract implemented in app;
- [ ] no entity-detection wording remains;
- [ ] audio preset approved/published;
- [ ] Kether sigil approved/published;
- [ ] accessibility/safety QA passes;
- [ ] version/checksum recorded where applicable;
- [ ] Portal 036 removes `CANONICAL_REFERENCE_PENDING` only after all three operator references are published.
