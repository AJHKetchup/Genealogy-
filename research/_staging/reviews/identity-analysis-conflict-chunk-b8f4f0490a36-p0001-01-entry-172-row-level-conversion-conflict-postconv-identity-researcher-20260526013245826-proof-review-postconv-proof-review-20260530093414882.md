---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530093414882
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Keep this item on `hold_for_conversion_qa`. The assigned chunk/source packet and the current converted Markdown give materially different row readings for entry 172.
2. The raw source image path referenced by the staged draft, source packet, chunk, converted file, and manifest is not currently present under `raw/sources`. The conversion job also lacks the referenced `page-images/page-0001.png` and `extracted-images` directory in this workspace, so this review could not independently verify the handwriting from the visible image.
3. Do not promote child identity, birth event, parent-child relationship, parent merge, Juana-name merge, or Dario-line comparison from this draft. The disagreement affects the child name, parents, birth date/time/place, residence context, and informant.
4. Do not certify the father field as `Jose del Carmen Pulgar S.` from this review. The source packet itself says the visible source supports `Jose del Carmen Pulgar` at minimum but leaves the trailing suffix or mark unresolved.
5. Do not treat the Burgos/de la Cruz converted-file reading as superseding the Pulgar/Arriagada chunk reading without targeted conversion QA. The two text artifacts cannot both be correct for the same row-controlled entry.

## Evidence Strengths

- The staged analysis accurately identifies the core conflict: entry 172 is Pulgar/Arriagada in the assigned chunk/source packet but Burgos/de la Cruz in the current converted Markdown and page Markdown.
- The conflict is literal and substantial, not just a spelling variant. The competing readings name different children, different parents, different birth dates/times/places, and different informants.
- The source packet records an earlier image-reviewed observation that the row numbered 172 on register page 58 is Pulgar/Arriagada, while also preserving uncertainty for the father-field suffix.
- The converted Markdown and conversion job page Markdown consistently support the Burgos/de la Cruz reading, which confirms there is a real conversion-control problem rather than a one-line typo in only one downstream file.
- The staged draft correctly avoids making a Dario attachment. Neither competing entry-172 reading names Dario, Arturo, Smith, a spouse, a descendant, or any bridge to a Dario Pulgar identity cluster.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10 for the underlying civil birth register as a source type; 3/10 for review-verifiable source access in this workspace because the raw/page image is unavailable |
| conversion_confidence_score | 2/10 for any specific entry-172 transcription claim until row-control QA resolves the chunk versus converted-file conflict |
| evidence_quantity_score | 4/10: multiple local text artifacts exist, but they derive from conflicting conversions and the source image is unavailable for this review |
| agreement_score | 2/10 across the assigned chunk/source packet versus converted Markdown/page Markdown; 8/10 only for the narrow fact that a row-level conflict exists |
| identity_confidence_score | 2/10 for promoting any person identity or parent relationship from this item now; 1/10 for any Dario-line attachment |
| claim_probability | 0.95 that the staged item correctly identifies a row-level conversion conflict requiring hold; 0.55 that entry 172 is the Pulgar/Arriagada row based on chunk/source-packet assertions not independently image-verified here; 0.30 that entry 172 is the Burgos/de la Cruz row based on converted-file consistency but conflict with the assigned chunk/source packet |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a conflict/hold analysis, not as proof of a canonical identity or relationship claim. The local review context confirms a hard disagreement between the assigned chunk/source packet and the converted Markdown for the same entry number. Because the actual source image and page-image cache are unavailable in this workspace, this review cannot decide the controlling row from handwriting.

The safest scored judgment is that the row-level conflict itself is highly probable and highly relevant, while all identity and relationship conclusions remain low confidence. The Pulgar/Arriagada reading may be the more family-relevant hypothesis, but it is not promotion-ready without targeted conversion QA.

## Next Action

Run targeted conversion QA for register page 58, entry 172 using the visible source image or regenerated page image. QA must decide the controlling row and certify the father-field reading only to the visible extent, such as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim, relationship, merge, or Dario-line comparison.
