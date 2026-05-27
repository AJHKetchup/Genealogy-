---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260527194650316
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_conversion_page_markdown: "raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-markdown/page-0001.md"
source_image_status: unavailable_in_workspace
canonical_readiness: not_ready
source_quality_score: 0.72
conversion_confidence_score: 0.25
evidence_quantity_score: 0.45
agreement_score: 0.20
identity_confidence_score: 0.30
claim_probability: 0.90
relevance_level: high
relevance_confidence: 0.75
---

# Proof Review: Entry 172 Row Conflict Revision

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md`.
- The staged draft is supported as a hold/review judgment, not as a promotable identity claim.
- The cited chunk and source packet read entry 172 as a Pulgar/Arriagada birth row: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The cited converted Markdown and conversion-job page Markdown read entry 172 as a different Burgos/de la Cruz row: child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- The manifest points to `raw/codex-conversion-jobs/.../page-images/page-0001.png`, and the source packet points to `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, but neither image file was available at the recorded local path during this review.
- Because the visible source image is unavailable and derivative transcripts directly conflict at row level, no child identity, parent identity, birth fact, parent-child relationship, same-person merge, or Dario-line bridge is ready for canonical use.
- The father field cannot be certified from this review as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Scored Judgment

| score | value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.72 | Civil birth registration would be a strong original source, but this review could not inspect the source image at the recorded path. |
| conversion_confidence_score | 0.25 | The chunk/source packet and converted/page Markdown give incompatible full rows for the same entry number. |
| evidence_quantity_score | 0.45 | Four local derivative artifacts were reviewed, but they split into two conflicting transcript families and no source image was available. |
| agreement_score | 0.20 | Agreement exists within each transcript family, but there is severe disagreement between the Pulgar/Arriagada and Burgos/de la Cruz readings. |
| identity_confidence_score | 0.30 | Identity confidence is low because the controlling row is unresolved; the Pulgar child and Burgos child cannot be treated as variants. |
| claim_probability | 0.90 | Probability is high that the staged draft's core hold judgment is correct: this is a row-level conversion conflict requiring QA before promotion. |
| relevance_level | high | If the Pulgar/Arriagada row controls, the entry is directly relevant to Pulgar/Arriagada identity and relationship work. |
| relevance_confidence | 0.75 | Relevance is constrained by unresolved row control and unavailable image verification. |
| canonical_readiness | not_ready | Nothing from this entry should be promoted while the row conflict remains unresolved. |

## Evidence Strengths

- The staged draft accurately reports the conflict between the assigned chunk/source packet and the current converted Markdown.
- The source packet explicitly flags low conversion confidence and recommends `hold_for_conversion_qa`, which matches the proof-review result.
- The staged draft correctly treats `Jose Miguel` versus `Jose del Carmen Segundo Pulgar Arriagada` as different rows or assignment contexts, not a name variant.
- The staged draft correctly blocks Dario-line attachment: none of the reviewed local evidence literally names Dario, Arturo, Smith, Dario Jose, or Darío Pulgar Arriagada.
- The staged draft's `canonical_readiness: not_ready` is appropriate and should remain unchanged.

## Review Outcome

Hold the staged draft for targeted conversion QA. The proof-supported claim is limited to: local derivative evidence for entry 172 is in severe row-level conflict, and canonical promotion is not ready.

Do not promote either the Pulgar/Arriagada row or the Burgos/de la Cruz row as the controlling entry-172 transcription from this review alone. Do not use this staged draft to merge or attach `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Jose Miguel`, `Oswaldo Burgos`, `Concepcion de la Cruz`, or any Dario-line candidate.

## Next Action

Run targeted conversion QA with the actual page image available. The QA note should decide the controlling entry-172 row and, if the Pulgar/Arriagada row controls, certify the father field only to the degree visible in the image. After QA, rerun proof review before any canonical claim, relationship, identity merge, or wiki update.
