---
type: proof_review
status: draft
role: claim_reviewer
worker: postconv-proof-review-20260525203527292
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170036486.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
review_decision: hold
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict

## Blockers First

- The staged identity-analysis draft is correctly conservative in recommending `hold_for_conversion_qa`, but its description of the assigned converted Markdown is not supported by the current referenced converted file. The staged draft says the converted Markdown records `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, birth at `En Pellin`; the current converted file instead records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth on 1888-04-06 at 10 p.m., place `En esta`.
- The assigned chunk and the visible source image both support entry 172 as the Pulgar/Arriagada row: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.` or an uncertain final suffix/mark, and mother `Juana Arriagada de Pulgar`.
- Because the staged draft relies on a stale or mismatched description of the converted Markdown conflict, it should not be promoted as written. The underlying proof posture remains a hold until conversion QA reconciles the converted file, chunk, source packet, and page image.
- The father-field ending remains unresolved for canonical purposes. Do not normalize it beyond the visible/source-supported choices `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- No Dario claim, merge, bridge, or relationship is supported by this entry. Shared Pulgar/Arriagada surname context is only a later double-check cue.

## Evidence Checked

- Staged identity-analysis draft assigned for this task.
- Referenced conflict draft.
- Referenced source packet.
- Referenced converted Markdown.
- Referenced chunk Markdown.
- Referenced page image.

## Evidence Strengths

- The chunk gives a complete row-level transcription for entry 172 with child name, sex, registration date, birth date/time, place, father, mother, residences, informant, and official signature context.
- The page image visibly aligns with the chunk on the Pulgar/Arriagada row for entry 172, including the child name, father name beginning `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The staged identity-analysis draft correctly treats the issue as a row/file-assignment or conversion conflict rather than a spelling variant.
- The draft correctly blocks canonical promotion and warns against Dario-line conflation.

## Scored Judgment

| Measure | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a direct source for the event; image is readable enough for the main row, though some handwriting detail remains difficult. |
| conversion_confidence_score | 0.42 | Chunk and image agree on Pulgar/Arriagada, but the current converted file disagrees and the staged draft describes a different converted-file conflict than the current file contains. |
| evidence_quantity_score | 0.62 | One direct source image plus two derivative transcriptions and staging notes were checked; no independent corroborating record was reviewed. |
| agreement_score | 0.48 | Source image and chunk agree, but converted Markdown, source packet narrative, and identity-analysis narrative are not internally synchronized. |
| identity_confidence_score | 0.72 | For the row visible as entry 172, the Pulgar/Arriagada identity is substantially supported; final father suffix and derivative-file conflict keep it below proof-ready. |
| claim_probability | 0.74 | It is more probable than not that this source image's entry 172 is the Pulgar/Arriagada birth registration, but the claim remains blocked by conversion QA. |
| relevance_level | direct | The reviewed evidence is directly about the assigned entry 172 identity conflict. |
| relevance_confidence | 0.96 | The staged draft, chunk, source packet, and image all refer to the same page/image assignment, despite derivative transcription disagreement. |
| canonical_readiness | 0.10 | Hold for conversion QA; do not promote child, parent, relationship, duplicate-person, or Dario-line claims from this staged draft as written. |

## Claim-Level Assessment

| Claim Or Hypothesis | Probability | Readiness | Notes |
| --- | ---: | --- | --- |
| Entry 172 in the source image records `Jose del Carmen Segundo Pulgar Arriagada`. | 0.78 | hold | Supported by chunk and visible page image; blocked by conflicting current converted file. |
| Father is `Jose del Carmen Pulgar S.` exactly. | 0.58 | hold | Chunk reads this and image appears compatible, but final suffix/mark needs targeted QA. |
| Father can be canonicalized as `Jose del Carmen Pulgar` without suffix. | 0.45 | hold | The base name is supported; dropping or interpreting the suffix would be premature. |
| Mother is `Juana Arriagada de Pulgar`. | 0.76 | hold | Supported by chunk and visible source row; still dependent on resolving row-level conversion conflict. |
| Current converted Markdown's entry 172 (`Jose Miguel` / `Oswaldo Burgos` / `Concepcion de la Cruz`) is the controlling reading. | 0.18 | hold/revise | Present in converted file, but not supported by the visible entry 172 row in the checked image. |
| Staged draft's reported converted-file reading (`Jose Francisco` / `Oswaldo Gomez` / `Rosario de la Cruz de la Maza`) is supported by the current referenced converted file. | 0.02 | revise | Not found in the current converted file checked for this review. |
| Any Dario identity bridge follows from this entry. | 0.01 | reject for this draft | No Dario appears in the source row, chunk, or converted file. |

## Source Reliability And Identity Risk

- Source reliability is high for event-level evidence because the image is a contemporaneous civil birth register page.
- Conversion reliability is mixed because the same source assignment has at least two incompatible derivative descriptions: the chunk/source-image Pulgar row and the current converted-file Burgos/de la Cruz row. The staged identity-analysis draft also preserves an older or alternate Gomez/de la Cruz de la Maza description not present in the current converted file.
- Identity risk is moderate-high for parent linkage until the father suffix and converted-file assignment are settled.
- Relationship-jump risk is high if child-parent links are promoted before QA; it is low if the row is kept staged as a conversion conflict.
- Conflict severity remains high because child, parents, birth date, place, and informant context differ across derivative readings.

## Next Action

Keep this staged identity-analysis draft and all dependent claims at `hold_for_conversion_qa`. Create or update a targeted conversion QA note that explicitly compares:

1. The current converted file's entry 172 reading of `Jose Miguel` / `Oswaldo Burgos` / `Concepcion de la Cruz`.
2. The chunk and page-image reading of `Jose del Carmen Segundo Pulgar Arriagada` / `Jose del Carmen Pulgar S.` or uncertain suffix / `Juana Arriagada de Pulgar`.
3. The stale conflict wording in the staged identity-analysis and source-packet notes that mentions `Jose Francisco`, `Oswaldo Gomez`, `Rosario de la Cruz de la Maza`, and `En Pellin`.

After conversion QA resolves the controlling row and certifies the father-field ending, rerun proof review before any canonical promotion.
