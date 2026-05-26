---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526171150074
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-identity-researcher-20260526135632244.md
staged_draft_reviewed: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-identity-researcher-20260526135632244.md
source_packet_checked: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526095657171.md
converted_file_checked: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk_checked: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source_image_checked: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
review_disposition: supported_hold
canonical_readiness: hold
claim_probability: 0.78
relevance_level: high
relevance_confidence: 0.98
source_quality_score: 0.82
conversion_confidence_score: 0.35
evidence_quantity_score: 0.62
agreement_score: 0.54
identity_confidence_score: 0.74
---

# Proof Review: Entry 172 Identity/Conversion Conflict

## Blockers First

- The staged draft correctly identifies a material row-level conflict: the converted Markdown assigns entry 172 to a Burgos/de la Cruz child, while the chunk, source packet, and visible source image support a Pulgar/Arriagada row.
- Canonical readiness remains `hold`. This review does not support promotion of a child identity, birth facts, parent-child relationships, parent identities, or Dario-line bridges until targeted conversion QA reconciles the derivative artifacts.
- The father field is not fully certified beyond `Jose del Carmen Pulgar` in the source packet. The chunk's `Jose del Carmen Pulgar S.` should remain an unresolved transcription detail until conversion QA or focused image review certifies the trailing mark.
- Existing canonical Pulgar or Juana pages, if any, must not be used as independent corroboration for this staged draft because the staged analysis says they depend on the same held entry-172 source cluster.
- No raw source, converted Markdown, chunk, source packet, or canonical page was edited for this review.

## Evidence Strengths

- The reviewed staged draft is literally supported in its main claim that two derivative readings disagree for the same entry number.
- The source packet explicitly says image review supports the Pulgar/Arriagada row and preserves the converted-file contradiction.
- The chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The converted Markdown transcribes entry 172 as `Jose Miguel`, male, born 6 April 1888 at 10 p.m., father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.
- Direct visual inspection of the referenced page image supports the staged packet's broad conclusion that the visible row 172 aligns with the Pulgar/Arriagada reading rather than the Burgos/de la Cruz converted Markdown row.
- The staged draft appropriately avoids treating the Pulgar/Arriagada row as a Dario identity bridge and keeps surname-only overlap out of canonical conclusions.

## Scored Judgment

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth registration image is a strong source for the event; source packet and image are available locally. |
| conversion_confidence_score | 0.35 | The current converted Markdown and chunk disagree at the row level, so conversion confidence remains low despite the image/chunk alignment. |
| evidence_quantity_score | 0.62 | Three local layers were checked: staged source packet, chunk, converted Markdown, plus targeted image inspection. Evidence is adequate for holding the conflict, not for promotion. |
| agreement_score | 0.54 | Source packet, chunk, and visible image broadly agree on Pulgar/Arriagada; converted Markdown materially disagrees. |
| identity_confidence_score | 0.74 | The Pulgar/Arriagada row is probably the intended entry 172, but the unresolved conversion conflict and father-field suffix prevent high confidence. |
| claim_probability | 0.78 | The staged draft's primary probability for Pulgar/Arriagada as the controlling row is reasonable and supported. |
| relevance_level | high | The staged draft directly addresses register page 58, entry 172 and the conversion conflict assigned for review. |
| relevance_confidence | 0.98 | All checked artifacts share the same source, chunk id, entry number, and staging chain. |
| canonical_readiness | hold | Do not promote until targeted conversion QA resolves the row mismatch and father-field reading. |

## Claim Review

The staged draft's central proof posture is supported: this is a conversion conflict, not a resolved identity claim. The draft keeps the two readings separate, scores the Pulgar/Arriagada row as probable, and recommends `hold_for_conversion_qa`. That is the correct conclusion from the checked materials.

The review supports these limited claims only:

- A row-level conflict exists between the assigned converted Markdown and the chunk/source-packet/image-supported reading.
- The Pulgar/Arriagada reading is more probable for the visible entry 172 than the Burgos/de la Cruz reading.
- The father, mother, and child identity claims are not canonically ready.
- No Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada bridge is supported by this entry alone.

## Next Action

Keep the identity-analysis staged draft on hold and route the source cluster to targeted conversion QA. QA should compare the source image, converted Markdown, chunk, and source packet; certify which row controls entry 172; and explicitly resolve whether the father field should be transcribed as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical promotion.
