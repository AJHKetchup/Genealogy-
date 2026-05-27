---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526232219797.md
worker: postconv-identity-analysis-20260527000642279
staged_draft: research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526232219797.md
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526232219797.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
analysis_status: hold
canonical_readiness: hold
---

# Identity And Conflict Analysis: Entries 513 And 515

## Blockers

- The exact staged conflict draft is already a `hold_for_conversion_qa` item: `research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526232219797.md`.
- Entry 513 has identity-controlling conversion conflicts. The converted/chunk text reads child `Isolina del Carmen / Jose` and sex `Masculino`, while reviewed notes preserve disagreement about the child-name field and indicate the image may support a different Pulgar-surname-style reading.
- Entry 513 mother surname is unresolved. Literal converted/chunk text reads `Juana de Dios Amador de Pulgar`; reviewed local concerns preserve an `Amagada`-style or possibly `Arriagada`-style reading. Do not normalize these forms from family context.
- Entry 513 father/declarant profession remains a QA issue. The converted/chunk text reads `Agricultor`; the staged packet flags profession verification before promotion.
- Entry 515 is a row-control conflict only for this analysis. The converted/chunk text reads `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`, but the staged conflict draft says partial image evidence does not securely support promotion and may require surname reconciliation.
- No direct evidence in this staged draft names Dario, Arturo, Smith, Dario Jose, or Darío/Dario Pulgar Arriagada. Any Dario-line comparison is an anti-conflation safeguard, not a promotion-ready bridge.

## Evidence Base

Literal converted/chunk readings:

- Entry 513: `Nombre. Isolina del Carmen / Jose`; `Sexo. Masculino`.
- Entry 513: father `Jose del Carmen Pulgar`; declarant `Jose del C. Pulgar`, `Padre`, age forty-seven, profession `Agricultor`, domicile `Calle Colon`.
- Entry 513: mother `Juana de Dios Amador de Pulgar`, Chilean, `Labores de su sexo`, domicile `Calle Colon`.
- Entry 515: child `Rosa Elvira del Carmen`; father/declarant `Pedro Pablo Leiva`.

Reviewed conflict indicators:

- Entry 513 child-name/sex field is unresolved against image-reviewed disagreement.
- Entry 513 mother surname may not be `Amador`; the draft preserves an `Amagada`-style concern.
- Entry 513 father/declarant profession needs targeted QA.
- Entry 515 child and father/declarant fields are not secure enough for promotion.

Existing wiki context used for comparison:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns not to merge similarly named Pulgar records automatically.
- `wiki/people/dar-o-pulgar-arriagada.md` is a separate Darío Pulgar Arriagada stub tied to a 2000 Chiguayante expropriation event.
- `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, and `wiki/people/tulio-cesar-luis-jose.md` hold draft family links from related staged evidence.
- `wiki/people/juana-arriagada-de-pulgar.md` and `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` are a separate Pulgar/Arriagada cluster from other staged source context.

## Hypothesis 1: Registration-Scoped Hold

The assigned draft supports only registration-scoped conflict candidates for entries 513 and 515 until conversion QA settles the row readings.

Supporting evidence:

- The source packet and converted/chunk files are for a civil birth-register page, register page 172, entries 513-515.
- The staged draft expressly recommends `hold_for_conversion_qa`.
- The unresolved fields include child identity, parent surname, profession, and row-spillover controls.

Interpretation:

- This is the leading hypothesis. The page is relevant to Pulgar research, but it is not proof-ready for canonical identity, relationship, or duplicate-person decisions.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Strong page-local evidence for named candidates, weak exact identity resolution. |
| conflict_severity | 0.90 | Names and relationship-controlling fields conflict. |
| evidence_quality | 0.58 | Civil register evidence is strong in type, but decisive readings are unstable. |
| conversion_confidence | 0.30 | The staged draft and packet both mark low confidence. |
| claim_probability | 0.70 | Probable that the page contains Pulgar-relevant entry data; not probable enough for exact claims. |
| relevance | 0.98 | Directly addresses the assigned staged draft. |
| canonical_readiness | 0.05 | Hold; no promotion. |

## Hypothesis 2: Entry 513 Jose/Juana Pair Matches Existing Jose/Juana Stubs

Entry 513 may involve the same parent candidates represented by `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` stubs.

Supporting evidence:

- Literal converted/chunk evidence names father/declarant `Jose del Carmen Pulgar` / `Jose del C. Pulgar`.
- Existing wiki context has `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` pages with draft child links to `Tulio Cesar Luis Jose`.
- The mother given names and `de Pulgar` context are consistent with the existing Juana candidate at a broad level.

Conflicts:

- The assigned draft's mother surname is literally `Amador`, with an `Amagada`-style concern, not a settled `Amagada` reading.
- The child name in this exact draft reads `Isolina del Carmen / Jose`, conflicting with the existing `Tulio Cesar Luis Jose` stub context.

Interpretation:

- Plausible but blocked. Existing stubs must not be used to force a preferred reading into this conversion conflict.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Father name aligns, but child and mother surname do not settle. |
| conflict_severity | 0.78 | A premature match could propagate the wrong child or maternal surname. |
| evidence_quality | 0.50 | Existing context is draft-backed and this draft is held. |
| conversion_confidence | 0.28 | Exact identity fields remain low-confidence. |
| claim_probability | 0.45 | Possible same family pair; not proved. |
| relevance | 0.92 | Direct Jose/Juana comparison required by task. |
| canonical_readiness | 0.08 | Hold. |

## Hypothesis 3: Mother Surname Is Arriagada/Amagada Rather Than Amador

The entry 513 mother may belong near the `Juana Arriagada de Pulgar` or `Juana de Dios Amagada de Pulgar` cluster rather than literal converted `Amador`.

Supporting evidence:

- The staged draft preserves an image-reviewed `Amagada`-style concern.
- The source packet says the surname remains image-sensitive and may appear closer to an `Arriagada`/`Amagada`-style reading than to `Amador`.
- Existing wiki contains separate Juana candidates: `Juana de Dios Amagada de Pulgar` and `Juana Arriagada de Pulgar`.

Conflicts:

- The literal converted/chunk text for this assigned draft is `Juana de Dios Amador de Pulgar`.
- `Juana Arriagada de Pulgar` belongs to a separate cluster with `Jose del Carmen Segundo Pulgar Arriagada`, an 1888 birth context, and different staged evidence.

Interpretation:

- This is a targeted QA lead, not a correction. `Amador`, `Amagada`, and `Arriagada` must remain separate until crop-level conversion QA and proof review settle the surname.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Variant signal exists, but no settled reading. |
| conflict_severity | 0.84 | Surname normalization could merge separate women or children. |
| evidence_quality | 0.46 | Review notes are useful, but conflict indicators are not replacement transcriptions. |
| conversion_confidence | 0.24 | The surname is one of the key low-confidence fields. |
| claim_probability | 0.34 | Possible, not promotable. |
| relevance | 0.90 | Central to the Pulgar-line and Jose/Juana comparison. |
| canonical_readiness | 0.03 | Hold. |

## Hypothesis 4: Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar Bridge

Entry 513 might eventually become relevant to the broader Pulgar line that includes family-supplied `Dario Arturo Pulgar-Smith` or staged CV/document subject `Dario Arturo Pulgar`.

Supporting evidence:

- The entry 513 father/declarant is a Pulgar candidate.
- Canonical `Dario Arturo Pulgar-Smith` is a Pulgar-line person in existing wiki context.
- Local staged CV/Habitat context elsewhere discusses document-level `Dario Arturo Pulgar`, but those materials require a separate identity bridge to `Dario Arturo Pulgar-Smith`.

Conflicts:

- The assigned draft does not name Dario, Arturo, Smith, a spouse, a child of Dario, a grandchild, or any direct lineage bridge.
- Family context can justify a later double-check, but not attachment by surname alone.

Interpretation:

- Low-probability lineage lead only. The exact next step would be: first resolve entry 513 conversion QA; then proof-review the confirmed child-parent relationship; only after that compare the confirmed family unit to accepted local evidence for `Dario Arturo Pulgar` and separately to `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | No direct Dario evidence in this draft. |
| conflict_severity | 0.76 | Premature attachment would create unsupported lineage claims. |
| evidence_quality | 0.38 | Contextual only for Dario. |
| conversion_confidence | 0.30 | Underlying row remains unsettled. |
| claim_probability | 0.07 | Very low from this draft alone. |
| relevance | 0.70 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not attach or promote. |

## Hypothesis 5: Same As Dario Jose Pulgar-Arriagada Or Darío/Dario Pulgar Arriagada

The entry 513 or 515 candidates are the same person as `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`.

Supporting evidence:

- Only broad surname/family-context overlap exists.
- Canonical `Darío Pulgar Arriagada` exists as a separate person stub, but its current evidence is a 2000 expropriation event, not this 1889 birth-register page.

Conflicts:

- The assigned draft does not name Dario.
- The assigned draft does not confirm `Arriagada`.
- Entry 513's candidate child is not settled and cannot be compared to a Dario cluster.

Interpretation:

- Unsupported as a same-person claim. Preserve as an anti-conflation guardrail only.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.02 | No direct Dario or confirmed Arriagada evidence. |
| conflict_severity | 0.86 | Name-only merging risks cross-generation conflation. |
| evidence_quality | 0.34 | No bridge evidence in this draft. |
| conversion_confidence | 0.24 | The only possible surname bridge is unresolved. |
| claim_probability | 0.02 | Not supported. |
| relevance | 0.62 | Required comparison only. |
| canonical_readiness | 0.00 | Do not merge. |

## Conflict Summary

- Same-person conflict: unresolved. No person in this staged draft is ready for same-person attachment to an existing canonical page.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar`; high if `Amador`, `Amagada`, and `Arriagada` are collapsed by context.
- Name-variant conflict: `Amador` versus `Amagada` versus possible `Arriagada`; `Isolina del Carmen / Jose` versus other local entry-513 child-name readings.
- Relationship conflict: entry 513 parentage cannot be promoted until child name and mother surname are settled. Entry 515 cannot be used as promoted Leiva evidence from this draft.
- Chronology conflict: none proved for Dario-line identities from this draft. Entry 513 date/time remains part of targeted QA before promotion.
- Conversion conflict: converted/chunk files agree with each other, but the staged proof-review context reports material derivative-vs-image disagreement.

## Ranked Hypotheses

| rank | hypothesis | probability | next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Registration-scoped hold only | 0.70 | Targeted conversion QA for entries 513 and 515. |
| 2 | Entry 513 Jose/Juana pair may match existing Jose/Juana stubs | 0.45 | After QA, proof-review child full name, father/declarant, mother surname, and parent-child relationship. |
| 3 | Mother surname may be Amagada/Arriagada rather than Amador | 0.34 | Crop-level surname reread; keep variants separate until accepted. |
| 4 | Broad bridge lead to Dario Arturo Pulgar-Smith / Dario Arturo Pulgar | 0.07 | Only after accepted entry-513 relationship proof, run a separate lineage/identity-bridge proof review. |
| 5 | Same as Dario Jose Pulgar-Arriagada or Darío/Dario Pulgar Arriagada | 0.02 | No current action except anti-conflation tracking. |

## Recommended Next Action

Keep the assigned staged conflict draft on `hold_for_conversion_qa`. Do not promote facts, merge people, rename pages, or attach this evidence to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Jose del Carmen Pulgar`, or any Juana candidate from this note.

The exact next step is targeted conversion QA against the source image for entry 513 child full name/sex, birth date/time/place, father/declarant form, father profession, and mother surname; and entry 515 child/father/declarant row controls. After QA produces either a corrected transcription or explicit uncertainty markers, rerun proof review on each atomic claim and only then run a focused identity comparison for the Jose/Juana parent candidates.
