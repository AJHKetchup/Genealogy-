---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260525171450460
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity/Conversion Conflict

## Blockers First

1. The staged identity analysis correctly treats entry 172 as a row-level conversion conflict and is not ready for canonical promotion. The chunk/source-packet/image reading identifies entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, while the referenced converted Markdown identifies entry 172 as `Jose Francisco`, son of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`.
2. The staged draft says the referenced converted Markdown names mother `Emilia de la Cruz` and birth date/place `veinte i seis de Marzo` / `En esta`; the converted file reviewed here instead reads mother `Rosario de la Cruz de la Maza`, birth date `En veinte de Febrero`, and place `En Pellin`. This does not change the hold decision, but it is a draft-detail mismatch that should be revised or superseded after QA.
3. The father field in the Pulgar/Arriagada row remains field-level uncertain. The visible image and chunk support a Pulgar father, but the final character after `Pulgar` should remain open as `S.` or uncertain until targeted conversion QA records the source-visible form.
4. No reviewed evidence in this entry supports a Dario-line bridge. Do not attach this row to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.

## Evidence Strengths

- Source class is strong: this is a civil birth registration page with entry number, registration date, child, birth facts, parents, informant, and official signature columns.
- The page image visibly supports the chunk/source-packet row-level reading for entry 172 as a Pulgar/Arriagada birth entry on page 58, not the Pellin/Gomez row found in the converted Markdown.
- The staged draft appropriately avoids canonical promotion and frames the issue as conversion QA, not as a same-person merge or spelling variant.
- The source packet, conflict candidate, and chunk are mutually consistent on the main Pulgar/Arriagada facts: registration date 7 April 1888, child `Jose del Carmen Segundo Pulgar Arriagada`, birth date 8 March 1888, birth place `Calle de Valdivia`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil registration is a high-value source class, but practical use is reduced by image resolution and derivative transcription conflict. |
| conversion_confidence_score | 0.38 | The chunk and image agree on the Pulgar/Arriagada row, but the referenced converted Markdown assigns a different family to the same entry number. |
| evidence_quantity_score | 0.55 | There is one directly relevant source image plus derivative layers; no independent corroborating source was reviewed for this task. |
| agreement_score | 0.46 | Chunk/source packet/image agree, but converted Markdown sharply disagrees on names, dates, places, and parents. |
| identity_confidence_score | 0.68 for the Pulgar/Arriagada row; 0.05 for any Dario-line attachment | The visible row supports the Pulgar/Arriagada identity better than the converted file, but the conversion conflict caps identity confidence. Dario is absent from the entry. |
| claim_probability | 0.68 | Probable that the visible entry 172 is the Pulgar/Arriagada registration, but not promotable until conversion QA resolves the derivative conflict. |
| relevance_level | high | If certified, the row is directly relevant to Pulgar/Arriagada parent-child evidence. |
| relevance_confidence | 0.90 | Names and relationships in the visible/chunk row match Pulgar/Arriagada research targets; relevance depends on QA certification. |
| canonical_readiness | hold_for_conversion_qa | Do not promote child identity, parent-child claims, parent merges, or Dario comparisons from this draft. |

## Claim Review

| Claim / hypothesis | Review judgment | Probability |
| --- | --- | ---: |
| Entry 172 is the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by chunk/source packet and visible image; blocked by conflicting converted Markdown. | 0.68 |
| Father is `Jose del Carmen Pulgar S.` | Broad father identity is supported as `Jose del Carmen Pulgar...`; suffix/ending needs QA before exact-name claim. | 0.60 |
| Mother is `Juana Arriagada de Pulgar`. | Supported by chunk/source packet and visible image, pending row-level QA. | 0.70 |
| Entry 172 is the converted-file `Jose Francisco` / `Oswaldo Gomez` / `Rosario de la Cruz de la Maza` row. | Literally present in converted Markdown, but contradicted by the image and chunk for this source packet. | 0.20 |
| Entry 172 supports a relationship to any Dario Pulgar candidate. | Unsupported; no Dario name, later-life identifier, spouse, child, occupation bridge, or chronology bridge is present. | 0.05 |

## Next Action

Run targeted conversion QA against the source image, chunk, and converted Markdown for `CHUNK-b8f4f0490a36-P0001-01`. The QA note should certify the controlling entry-172 row and record the father field exactly as visible. After that, rerun proof review on the certified child identity, birth facts, father claim, mother claim, and parent-child relationship claims before any canonical promotion.
