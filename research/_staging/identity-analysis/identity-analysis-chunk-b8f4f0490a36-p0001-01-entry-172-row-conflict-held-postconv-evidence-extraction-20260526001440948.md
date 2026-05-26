---
type: identity_conflict_analysis
status: draft
role: evidence_extractor
worker: "postconv-evidence-extraction-20260526001440948"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
promotion_recommendation: hold_for_conversion_qa
created: 2026-05-26
---

# Identity/Conflict Analysis: Entry 172

## Findings

The source image and assigned chunk support treating entry 172 as a Pulgar/Arriagada birth row, but the current converted Markdown assigns entry 172 to a Burgos/de la Cruz birth row. This is not an identity-merge problem; it is a conversion row-control problem.

The Pulgar/Arriagada reading supports a possible child identity for Jose del Carmen Segundo Pulgar Arriagada, with parents Jose del Carmen Pulgar or Jose del Carmen Pulgar S. and Juana Arriagada de Pulgar. It does not directly name Dario, Arturo, Smith, Dario Jose, or any later Dario Pulgar-Arriagada identity.

## Confidence And Blocking Issues

- Row-control confidence: low for canonical promotion because the derivative converted Markdown and chunk disagree materially.
- Image support: moderate for the Pulgar/Arriagada row as the visible row numbered 172.
- Father-field confidence: low-to-moderate; the field begins Jose del Carmen Pulgar, but the trailing suffix must be certified by conversion QA.
- Relationship confidence: low until row control and father-field QA are complete.

## Anti-Conflation Note

Do not use this entry to merge any Jose del Carmen Pulgar candidate, Juana Arriagada de Pulgar candidate, or Dario-line person by surname alone. If QA confirms the Pulgar/Arriagada row, proof review should separately evaluate child identity, birth facts, father, mother, and parent-child relationships.

## Recommendation

Keep all dependent evidence at `hold_for_conversion_qa`. Route the source image, converted Markdown, assigned chunk, and source packet to targeted conversion QA. After QA, rerun proof review before any canonical claim, relationship, identity merge, or Dario-line comparison is promoted.
