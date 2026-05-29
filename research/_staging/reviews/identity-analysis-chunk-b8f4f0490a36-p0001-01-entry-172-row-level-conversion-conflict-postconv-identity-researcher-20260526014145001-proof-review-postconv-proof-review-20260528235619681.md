---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528235619681
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
reviewed_subject: "Entry 172, Los Angeles birth register, 1888"
reviewed_claim_type: identity_conflict_analysis
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
source_page_image_checked: true
source_quality_score: 0.88
conversion_confidence_score: 0.40
evidence_quantity_score: 0.74
agreement_score: 0.50
identity_confidence_score: 0.72
claim_probability: 0.93
relevance_level: high
relevance_confidence: 0.97
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The staged identity analysis is supported as a conflict note, but it is not ready for promotion because the current converted Markdown and the assigned chunk/source packet disagree on the controlling row for entry `172`.
2. The conflict is row-level. The assigned chunk, source packet, and visible source image support a Pulgar/Arriagada row for entry `172`; the current converted Markdown instead gives a Burgos/de la Cruz row for entry `172`.
3. The disagreement changes child identity, birth date, birth time, birthplace, father, mother, informant, parent residence context, and dependent relationship claims. These cannot be treated as spelling variants or same-person evidence.
4. The father-field ending in the Pulgar/Arriagada row remains a targeted QA issue. The chunk reads `Jose del Carmen Pulgar S.`, but this proof review should not force that suffix beyond the visible-source and conversion-QA boundary.
5. The staged draft's Dario-line comparisons are appropriate only as identity-risk guardrails. Entry `172` does not name Dario, Arturo, Smith, a spouse, a child of Dario, or any passenger-list candidate, so it cannot support a Dario identity bridge.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md`.
- Referenced conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced source image checked for verification context only: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source is a civil birth registration image, a strong primary source class for birth, parent, informant, date, place, and residence claims when the row is certified.
- The visible image for page 58, entry `172`, aligns with the assigned chunk/source-packet reading: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at Calle de Valdivia, with mother `Juana Arriagada de Pulgar` and informant `Ernesto Herrera L.`.
- The assigned chunk and source packet are internally coherent for the Pulgar/Arriagada row and explicitly preserve the need for conversion QA instead of promoting dependent claims.
- The current converted Markdown is useful as conflict evidence because it directly documents the incompatible Burgos/de la Cruz reading under the same entry number: child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at about 10 p.m. in `En esta`, with `Oswaldo Burgos` as informant.
- The staged identity analysis correctly treats the conflict as a blocker before identity merging, relationship promotion, or Dario-line comparison.

## Scored Judgment

- `source_quality_score: 0.88` - the image is an original/primary civil register page and was available for visual verification; reduced slightly because this review did not perform a full independent paleographic recertification of every field.
- `conversion_confidence_score: 0.40` - confidence in the current conversion set is low because the converted Markdown materially conflicts with the chunk, packet, and visible image.
- `evidence_quantity_score: 0.74` - one source image plus the staged draft, conflict draft, source packet, chunk, and converted Markdown are enough to validate the conflict; more QA is needed to certify final transcription details.
- `agreement_score: 0.50` - image, chunk, source packet, and staged analysis agree directionally on Pulgar/Arriagada, while the current converted Markdown disagrees across the row.
- `identity_confidence_score: 0.72` - confidence is moderate-high that the visible entry `172` is the Pulgar/Arriagada row, but canonical identity confidence remains limited by the unreconciled conversion conflict and father-field ending.
- `claim_probability: 0.93` - very high probability that the staged draft correctly identifies a material row-level conversion conflict; lower confidence would apply to any dependent canonical person or relationship claim.
- `relevance_level: high`.
- `relevance_confidence: 0.97` - directly relevant to Pulgar/Arriagada staging and to preventing unsupported Dario-line identity jumps.
- `canonical_readiness: hold_for_conversion_qa`.

## Review Judgment

The staged identity analysis is supported as a hold-level conflict analysis. It should not be promoted to canonical claims, relationships, people, families, or wiki pages while the converted Markdown remains inconsistent with the source image and assigned chunk.

The strongest review-level conclusion is procedural: entry `172` needs targeted conversion QA. The Pulgar/Arriagada row is the stronger visible-source hypothesis, but the exact father-field ending and the cause of the Burgos/de la Cruz converted-file mismatch must be resolved before canonical use.

## Next Action

Run targeted conversion QA against the source image, assigned chunk, source packet, and current converted Markdown. Certify the controlling row for entry `172`, identify whether the converted Markdown is stale, row-shifted, or from a different page/image, and preserve the father field only to the visible level of certainty. After QA, rerun proof review on the narrow row-level claims before any canonical claim, relationship, merge, Dario-line bridge, or wiki update.
