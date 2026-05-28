---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528222747761
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526000554848.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526000554848.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote any child identity, birth fact, parent name, parent-child relationship, parent identity merge, or Dario-line bridge from this staged draft while the row-control conflict remains unresolved in the converted file.
2. The staged draft, source packet, chunk, and visible source image support page 58, entry 172 as a Pulgar/Arriagada row, but the referenced converted Markdown reports the same entry number as a Burgos/de la Cruz row. This is a material conversion-control conflict, not a minor spelling variance.
3. The father field must remain uncertified. The visible row and chunk support `Jose del Carmen Pulgar` with an apparent trailing element, but this review should not force the reading to `S.` without targeted conversion QA.
4. No visible source text in the reviewed entry names Dario, Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Darío Pulgar Arriagada. Those remain anti-conflation checkpoints only.

## Evidence Strengths

- The civil birth-register image is a direct, contemporary source for the entry and is stronger than downstream converted text for row-control verification.
- The chunk transcribes entry 172 on page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The source packet independently flags the same row-control mismatch and correctly recommends `hold_for_conversion_qa`.
- Visual inspection of the referenced source image supports the staged packet's narrow row-control point: page 58, entry 172 is a Pulgar/Arriagada entry, not the Burgos/de la Cruz row shown in the converted Markdown.
- The staged identity analysis correctly avoids promoting the Pulgar row into Dario-related identity or relationship claims.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 4/10 overall; 7/10 for the chunk/source-packet Pulgar row reading; 2/10 for the current converted Markdown entry-172 row |
| evidence_quantity_score | 5/10 |
| agreement_score | 6/10 overall; high agreement among source image, chunk, source packet, and staged analysis, but direct disagreement from the converted Markdown |
| identity_confidence_score | 7/10 that the visible entry 172 is the Pulgar/Arriagada row; 4/10 for exact father-name suffix; 1/10 for any Dario identity bridge |
| claim_probability | 0.82 that page 58 entry 172 is the Pulgar/Arriagada row; 0.45 that the father suffix is exactly `S.`; 0.05 or lower for a Dario-line bridge from this entry alone |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold |

## Review Finding

The staged draft is supported as a hold recommendation. The evidence is strong enough to say the current converted Markdown likely has row-level drift for entry 172, because the source image, chunk, source packet, and staged analysis all point to the Pulgar/Arriagada row while the converted Markdown gives a wholly different Burgos/de la Cruz family.

This review does not certify the exact father-field suffix and does not support expanding the row into Dario-related identity claims. The only source-supported direction is targeted conversion QA for the controlling entry and a narrow reread of the father field.

## Next Action

Run targeted conversion QA against the source image for page 58, entry 172. Certify whether the controlling row is the Pulgar/Arriagada row and record the father field exactly as visible. Only after that should downstream workflows consider staged claims for the child, birth details, parent names, and parent-child relationships. Keep all Dario-related merges and relationship bridges on hold pending separate direct evidence.
