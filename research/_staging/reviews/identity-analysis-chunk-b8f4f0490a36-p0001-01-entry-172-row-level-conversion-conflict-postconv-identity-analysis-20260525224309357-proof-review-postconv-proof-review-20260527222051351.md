---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527222051351
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525224309357.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525224309357.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote the current converted Markdown's entry-172 Burgos/de la Cruz reading. The referenced source image and the assigned chunk visibly support the Pulgar/Arriagada row for entry 172, while the converted Markdown describes a different set of entries and appears misaligned with the source image.
2. Do not promote a canonical person, parent-child relationship, merge, or Dario-line bridge from this item until conversion QA or correction resolves the derivative-file conflict. The proof record still contains contradictory conversion layers for the same converted file/chunk set.
3. Do not silently normalize the father field. The visible row supports `Jose del Carmen Pulgar` with an additional mark or suffix that is not fully certified here; the source-packet form `Jose del Carmen Pulgar S.` should remain a transcription candidate rather than a resolved identity expansion.
4. Do not attach this entry to `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. The source image for entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario, Arturo, Smith, or a descendant bridge.

## Evidence Strengths

- The staged draft accurately identifies a material row-control conflict between the assigned chunk/source packet and the current converted Markdown.
- The source image supports the assigned chunk/source-packet row for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m., with parents `Jose del Carmen Pulgar ...` and `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The conflict draft and source packet correctly recommend holding promotion for conversion QA rather than treating the two text layers as a name variant.
- The staged identity analysis correctly separates the Pulgar/Arriagada row from Dario-line candidates and from possible Juana/Jose parent-candidate merges.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 7/10 for the assigned chunk/source-packet against the source image; 2/10 for the current converted Markdown's Burgos/de la Cruz entry-172 layer |
| evidence_quantity_score | 4/10 |
| agreement_score | 7/10 between source image, assigned chunk, source packet, conflict draft, and staged analysis for the Pulgar/Arriagada row; 1/10 between those files and the current converted Markdown |
| identity_confidence_score | 7/10 for the narrow source-image claim that entry 172 records `Jose del Carmen Segundo Pulgar Arriagada`; 4/10 for linking the father to an existing `Jose del Carmen Pulgar` canonical person; 0.5/10 for any Dario-line identity bridge |
| claim_probability | 0.85 that the visible source image's entry 172 is the Pulgar/Arriagada birth row; 0.15 that the converted Markdown's Burgos/de la Cruz row controls this source image; 0.05 or lower for any Dario identity or relationship claim from this source alone |
| relevance_level | high for Pulgar/Arriagada family research and conversion QA; low for Dario identity proof |
| relevance_confidence | 0.90 for Pulgar/Arriagada relevance; 0.25 for Dario-line relevance |
| canonical_readiness | hold |

## Review Finding

The staged identity-analysis draft is supported as a conflict/hold analysis and should not be promoted as a resolved claim packet. Visual review of the referenced source image favors the assigned chunk/source-packet Pulgar/Arriagada reading over the current converted Markdown, but that does not remove the repository-level conversion conflict because the converted file still contains the incompatible Burgos/de la Cruz extraction.

The safest disposition is `hold_for_conversion_qa` or `revise_after_conversion_correction`: correct or supersede the misaligned converted Markdown, then rerun proof review on the cleaned evidence chain before canonical promotion.

## Next Action

Send this item to targeted conversion QA for the referenced source image, converted file, and chunk. QA should certify that entry 172 controls as the Pulgar/Arriagada row, record the father field only to the visible degree supported by the image, and then regenerate or amend downstream staged evidence before any canonical person, relationship, merge, or Dario-line comparison is promoted.
