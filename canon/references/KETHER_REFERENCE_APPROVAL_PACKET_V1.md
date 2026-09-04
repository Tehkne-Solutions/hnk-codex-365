# KETHER REFERENCE APPROVAL PACKET V1

**Status:** `DECISION_PACKET_NOT_CANON`  
**Scope:** Chapter 1 — Kether, Days 001–036  
**Freeze:** `KETHER_CANON_FREEZE_V1`  
**Related issues:** #8, #11, #14, #17, #25  
**Snapshot basis:** `968e8dc2050e7d2a076fc4e892e727e0772594a5`  
**Protocol:** HNK-EP-1.1

> This packet consolidates the remaining Kether reference decisions. It does not by itself canonize any proposal. A proposal becomes canonical only after explicit owner approval, publication/versioning, required asset QA/checksums and a canonical merge.

---

## 1. CURRENT FREEZE STATE

Already resolved or materially completed:

- Kether Days 001–036 exist in `canon/capitulo-01-kether/`;
- review records `reviews/dia-001.review.json` through `reviews/dia-036.review.json` exist;
- Day 035 title/procedure conflict is resolved as `O Ritual do Banimento Primal`;
- Days 002/003/005 XP prose/frontmatter inconsistency is resolved;
- Day 011 premature cycle-closing wording is resolved;
- Day 006 unsupported `52 Hz` reference was removed by the Canon Freeze work;
- Gneo Geo functional ontology is documented;
- four HNK-original proposals and two proposal SVG masters are versioned;
- deterministic Kether→Chokmah transition-audio renderer exists.

Remaining publication blockers are primarily canonical reference approvals and asset publication.

---

## 2. DECISION A — GNEO GEO V1

**Source file:** `canon/references/proposals/GNEO_GEO_GEOMETRY_V1_PROPOSAL.md`  
**Current status:** `PROPOSAL_NOT_CANON`  
**Related:** #11, #25

### Candidate

**Gneo Geo Astral — Estrela Dupla dos Oito Circuitos**  
Asset id: `hnk.gneo_geo.v1.master`

### Proposed topology

- one fixed center `O` = Cockpit / Command Position;
- inner octagram built from two interlocked squares at 45°;
- second congruent outer octagram rotated 22.5° relative to the inner structure;
- eight circuit nodes on a ring between the two octagrams;
- one radial connection from each circuit to the center;
- fixed North / 0° orientation;
- clockwise traversal `1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → O`.

Circuit mapping:

1. Biossobrevivência Oral
2. Emocional / Territorial
3. Neurosemântica
4. Doméstica / Sócio-Sexual
5. Neurosômica
6. Metaprogramação
7. Morfogenética
8. Rede Quântica

### Recommendation

**`RECOMMENDED_APPROVE_AS_HNK_ORIGINAL_V1`**

Reason: the topology is deterministic, mobile-legible, preserves all source-backed functional invariants, supports an active/control comparison and explicitly avoids claiming recovery of a lost historical Gneo Geo drawing.

### Approval meaning

Approval freezes topology, orientation and circuit mapping. It does **not** yet freeze final material/color treatment.

---

## 3. DECISION B — KETHER SIGIL V1

**Source file:** `canon/references/proposals/KETHER_SIGIL_V1_PROPOSAL.md`  
**Current status:** `PROPOSAL_NOT_CANON`  
**Related:** #14, #25

### Candidate

**Sigilo da Coroa de Kether — HNK V1**  
Asset id: `hnk.kether.sigil.v1.master`

### Proposed grammar

- one central origin point;
- three concentric rings in `1 : 2 : 3` proportion;
- twelve gates every 30°;
- thirty-six outer marks, one per Kether Day;
- stable crown axis at North;
- final crown as a restrained three-point geometric termination;
- fixed orientation; no mirrored canonical variant.

### Recommendation

**`RECOMMENDED_APPROVE_AS_HNK_ORIGINAL_V1`**

Reason: it encodes Kether using the already approved HNK structural grammar `3 / 12 / 36`, supports progress semantics for all 36 Days, preserves the Kether visual direction and does not import unrelated historical occult glyphs.

### Approval meaning

Approval freezes geometry/orientation/progression semantics. Final stroke/material treatment remains a production-system concern so long as topology is unchanged.

---

## 4. DECISION C — SINTONIZADOR ANGELICAL V1

**Source file:** `canon/references/proposals/ANGELIC_TUNER_V1_PROPOSAL.md`  
**Current status:** `PROPOSAL_NOT_CANON`  
**Related:** #14, #25

### Candidate

**Sintonizador Angelical HNK — Kether V1**  
Component id: `hnk.tuner.kether.v1`

### Functional definition

A deterministic ritual-audio controller that loads approved HNK metadata and published audio/sigil assets for a session.

Portal fixed sequence:

`READY → AUDIO_ARMED → INDUCTION → SIGIL_READY → GNOSIS → RETURN → RECORD → COMPLETE`

The tuner:

- may load Day/Sephira/cycle/angel/formula metadata already defined by canon;
- must use a published preset id and sigil asset id;
- always preserves play/pause/stop/volume/return controls;
- never detects angels/entities;
- never assigns objective frequencies to entities without a future explicit source;
- never treats audio completion alone as Portal completion.

### Recommendation

**`RECOMMENDED_APPROVE_FUNCTIONAL_CONTRACT_V1`**

Reason: this interpretation converts the manuscript term into a reproducible product instrument without inventing supernatural sensing behavior or undocumented tuning rules.

### Approval meaning

Approval freezes product meaning, data contract and Portal fixed-mode behavior. It does not publish an audio preset or sigil by itself.

---

## 5. DECISION D — KETHER → CHOKMAH TRANSITION AUDIO V1

**Source file:** `canon/references/proposals/KETHER_CHOKMAH_TRANSITION_AUDIO_V1_PROPOSAL.md`  
**Current status:** `PROPOSAL_NOT_CANON`  
**Related:** #14, #25

### Candidate recipe

Preset id: `hnk.audio.kether_chokmah.transition.v1`

- left carrier: `429 Hz`;
- right carrier: `435 Hz`;
- arithmetic center: `432 Hz`;
- binaural difference: `6 Hz`;
- ritual/Solfeggio layer: `528 Hz`;
- target-state product label: `Theta — HNK target label`;
- duration: `720 s / 12 min`;
- fade in: `36 s`;
- main body: `648 s`;
- fade out: `36 s`;
- deterministic offline rendering;
- no voice/ASMR hidden layer in V1.

### Recommendation

**`RECOMMENDED_APPROVE_RECIPE_FOR_LISTENING_QA`**

Reason: it reconciles the source-backed `432 Hz base`, `528 Hz` ritual/Solfeggio and Theta vocabulary without pretending that this precise stereo construction was historically specified by the manuscript.

### Important boundary

Approval of the recipe is **not** publication of the asset. Before `published` status it still requires:

- deterministic master render;
- safe-volume listening QA;
- lossless master + distribution derivative;
- SHA-256 checksums;
- registry entry;
- confirmation that copy does not state `Theta detected` or medical effect.

---

## 6. DECISION E — DAI KOO MYO / MAHASIAH

**Research file:** `docs/research/DAI_KOO_MYO_REFERENCE_RESEARCH_V1.md`  
**Current status:** `REFERENCE_PENDING`  
**Related:** #8

### Source-supported family

The HNK source explicitly requires **Dai Koo Myo (Reiki Usui)** for Days 021–025. External reference research supports the traditional Usui-kanji family:

**`大光明`**

as the defensible semantic/reference family, while also documenting that multiple calligraphic/lineage variants circulate.

### Recommendation

**`RECOMMENDED_APPROVE_REFERENCE_FAMILY`**

Approve:

- semantic master: `大光明`;
- family: traditional Usui Dai Ko Myo kanji reference;
- rendering: HNK-owned vector redrawing that preserves the three kanji and standard Japanese stroke order;
- provenance label: `HNK rendering of traditional Usui Dai Ko Myo kanji reference`;
- exclude Tibetan/Dumo master-symbol geometry from Kether unless later canon explicitly adds it.

Recommended orientation for the HNK master sheet:

**vertical stack, top-to-bottom: `大` → `光` → `明`**.

This orientation is an explicit HNK production decision, not a recovered TW-DVF historical drawing.

### Still required before #8 closes

- vector master;
- stroke-order sheet;
- transparent raster derivative;
- orientation metadata;
- 3D/AR derivative rule;
- provenance/license note;
- SHA-256 checksum;
- Asset Registry entry.

---

## 7. AUDIO ITEMS NOT CLOSED BY DECISION D

The Portal preset does not automatically resolve all Kether audio references.

Still pending under `KETHER_AUDIO_CONFLICT_AUDIT_V1.md`:

- Day 001 mapping of `528 / 432 / Theta`;
- Day 002 mapping;
- Day 004 numeric behavior behind `Theta`;
- remaining Kether audio wording audit;
- Day 030 active/control ASMR asset pair;
- version/checksum for every published preset.

Day 006 `52 Hz` is already resolved as unsupported and removed.

---

## 8. PROPOSED OWNER DECISION SET

The recommended Kether reference decision set is:

- [ ] approve **GNEO GEO V1** topology/orientation/circuit mapping;
- [ ] approve **KETHER SIGIL V1** geometry/orientation/progression semantics;
- [ ] approve **SINTONIZADOR ANGELICAL V1** functional/data/Portal contract;
- [ ] approve **KETHER → CHOKMAH TRANSITION AUDIO V1** recipe for render + listening QA;
- [ ] approve **DAI KOO MYO / 大光明** as the Usui reference family and authorize an HNK-owned vertical vector master.

No checkbox may be converted to `approved` merely because this packet exists.

---

## 9. AFTER APPROVAL

Once the owner decision is explicit, execute in this order:

1. promote approved proposal specs from `PROPOSAL_NOT_CANON` to canonical reference records;
2. generate/finalize required masters;
3. record provenance/version/checksum;
4. close #11 when Gneo Geo published asset is complete;
5. close #8 when Dai Koo Myo package is complete;
6. close #14 only after Sintonizador + transition audio + Kether sigil are all published;
7. update dependent `codex-hnk-app` specs/Asset Registry;
8. re-run Kether canon/review/build QA;
9. resynchronize Days 001–036 to the app/Supabase using the final freeze commit SHA;
10. publish `KETHER_CANON_FREEZE_V1`.

---

## 10. GOVERNANCE RULE

This packet recommends decisions. It does not erase the distinction between:

- recovered/source-defined material;
- HNK-original specification;
- external-reference research;
- implementation detail.

That distinction remains part of HNK-EP-1.1 and of the Kether Canon Freeze contract.
