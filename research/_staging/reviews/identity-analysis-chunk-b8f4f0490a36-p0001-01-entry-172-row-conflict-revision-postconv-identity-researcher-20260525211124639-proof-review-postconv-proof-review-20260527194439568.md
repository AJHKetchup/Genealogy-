---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527194439568
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211124639.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211124639.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
page_image_checked: unavailable
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row Conflict

## Blockers First

1. The referenced raw source image is not available at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, and the conversion job has no local `page-images/page-0001.png` or extracted image directory available for visual verification.
2. The assigned chunk and current converted Markdown give incompatible readings for entry 172. This is a row-control conflict, not a spelling variation.
3. The chunk/source packet reading identifies `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
4. The converted file and page-level conversion Markdown identify entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
5. No reviewed material in this task supports changing any reading to Dario/Darío, Arturo, Smith, or Dario Jose. Any Dario-line bridge remains unsupported by this record.
6. Canonical promotion is blocked for child identity, birth facts, parent names, parent-child relationships, father-candidate merge, and Dario-line comparison until targeted conversion QA visually certifies the controlling row.

## Evidence Strengths

- The staged identity-analysis draft accurately reports the conflict between the assigned chunk/source packet and the current converted Markdown.
- The staged conflict draft and source packet preserve both derivative readings and recommend `hold_for_conversion_qa`, which is appropriate given the unresolved row assignment.
- The source type, if visually available and correctly assigned, would be a civil birth registration and therefore strong direct evidence for a birth row. The current review cannot give that strength to either derivative reading because the visible source image was unavailable locally.
- The staged draft correctly avoids promoting a name-only or surname-only Pulgar bridge to Dario/Darío Pulgar clusters.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the stated civil birth-register source type if the image is recovered; 4/10 for this review because the source image was unavailable for visual checking |
| conversion_confidence_score | 2/10 overall; two local derivatives disagree at the row level |
| evidence_quantity_score | 2/10 for promotion; one underlying source is referenced, but only conflicting derivative transcriptions were available |
| agreement_score | 1/10 between chunk/source packet and converted/page Markdown |
| identity_confidence_score | 2/10 for any specific child or parent identity from this task; 0.5/10 for any Dario-line identity bridge |
| claim_probability | 0.85 that the staged draft's `hold_for_conversion_qa` recommendation is correct; 0.45 for the Pulgar/Arriagada row as controlling; 0.45 for the Burgos/de la Cruz row as controlling; 0.02 for a Dario/Darío bridge |
| relevance_level | high for Pulgar/Arriagada research if the Pulgar row is visually confirmed; low for Dario-line claims without bridge evidence |
| relevance_confidence | 0.80 for the row-conflict issue; 0.20 for any Dario-line relevance |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a cautionary identity and row-conflict analysis. It should not be promoted as proof of the Pulgar/Arriagada birth row or the Burgos/de la Cruz birth row because the controlling entry-172 row remains unresolved and the source image/page image was unavailable for direct review.

The only claim ready to carry forward from this review is procedural: entry 172 requires targeted conversion QA before any canonical birth, parent, relationship, identity merge, or Dario-line comparison can proceed.

## Next Action

Keep this staged draft on `hold_for_conversion_qa`. Recover or make available the referenced page image, then compare the source image against the converted Markdown, assigned chunk, and source packet. The QA note should certify the controlling entry-172 row and, if the Pulgar row is visible, record the father field only to the visible level: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
