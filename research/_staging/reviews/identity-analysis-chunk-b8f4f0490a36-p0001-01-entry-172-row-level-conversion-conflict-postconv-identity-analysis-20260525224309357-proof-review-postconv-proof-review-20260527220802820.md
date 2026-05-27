---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527220802820
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

1. Do not promote any child identity, birth fact, parent-child relationship, parent merge, or Dario-line bridge from this staged draft while the converted Markdown and chunk/source-packet disagree on the controlling entry-172 row.
2. The converted Markdown is materially inconsistent with the referenced source image and chunk for page 58 entry 172. It gives `Jose Miguel`, `Oswaldo Burgos`, `Concepcion de la Cruz`, a 6 April birth, and `En esta`; the referenced image visibly aligns entry 172 with the Pulgar/Arriagada row described by the chunk.
3. Even though the source image supports the Pulgar/Arriagada row over the converted Markdown, the conversion layer remains formally conflicted. Canonical use should wait for targeted conversion QA or correction of the converted file/chunk relationship.
4. The father field should not be normalized beyond the visible/source-supported uncertainty. The reviewed materials support a reading in the range of `Jose del Carmen Pulgar S.` or similar, but this review does not certify expansion or identity with an existing `Jose del Carmen Pulgar` page.
5. No reviewed source text supports identifying this child or either parent with Dario Arturo Pulgar, Dario Arturo Pulgar-Smith, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada.

## Evidence Strengths

- The staged identity analysis accurately identifies a row-control conflict between the current converted Markdown and the assigned chunk/source packet.
- The conflict draft and source packet preserve the two competing derivative readings rather than silently choosing one.
- Visual review of the referenced source image supports the staged draft's claim that page 58 entry 172 is a Pulgar/Arriagada birth-registration row, not the Burgos/de la Cruz row currently recorded in the converted Markdown.
- The staged draft correctly treats the conflict as a conversion/row-control problem, not a spelling variant or same-person problem.
- The staged draft appropriately warns against parent merges, Juana surname normalization, and Dario-line attachment without a separate identity bridge.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 4/10 overall because the converted Markdown conflicts with the chunk and visible source image; 8/10 for the chunk/source-packet reading of the narrow entry-172 row |
| evidence_quantity_score | 5/10 |
| agreement_score | 6/10 overall: source image, chunk, source packet, conflict draft, and identity analysis agree on Pulgar/Arriagada, but the converted Markdown strongly disagrees |
| identity_confidence_score | 7/10 for the narrow existence of an entry-172 Pulgar/Arriagada child in the image/chunk; 4/10 for attaching that child to existing canonical person pages; 1/10 for any Dario bridge |
| claim_probability | 0.82 that the visible entry 172 row is the Pulgar/Arriagada row; 0.12 that the converted Markdown's Burgos/de la Cruz reading controls this source image; 0.08 or lower for Dario/Pulgar-Smith identity or relationship claims |
| relevance_level | high for Pulgar/Arriagada family research; low for direct Dario identity proof |
| relevance_confidence | 0.90 for Pulgar/Arriagada relevance; 0.20 for Dario-line relevance |
| canonical_readiness | hold |

## Review Finding

The staged draft is supported as a proof-review hold. Its central claim is not that the Pulgar/Arriagada identity is ready for canonical promotion, but that the derivative record set contains a material row-level conflict that blocks promotion. That judgment is supported.

The source image gives strong support to the chunk/source-packet Pulgar/Arriagada reading for entry 172. However, because the current converted Markdown attached to the same source path records an unrelated Burgos/de la Cruz entry, downstream canonical work should wait for targeted conversion QA or a corrected conversion artifact. The conflict affects literal support, source reliability at the conversion layer, relationship confidence, and identity safety.

## Next Action

Keep this draft on `hold_for_conversion_qa`. A targeted conversion QA worker should reconcile the source image, converted Markdown, chunk, and source packet, then certify the controlling entry-172 row and the exact father-field reading. After that, run separate proof review before promoting a child identity, attaching parents, merging any Jose/Juana candidates, or using this record in any Dario-line argument.
