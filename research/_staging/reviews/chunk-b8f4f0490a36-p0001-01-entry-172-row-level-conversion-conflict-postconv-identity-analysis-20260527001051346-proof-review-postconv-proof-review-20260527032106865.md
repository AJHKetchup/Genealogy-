---
type: proof_review
status: reviewed
role: claim_reviewer
worker: postconv-proof-review-20260527032106865
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527001051346.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527001051346.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
reviewed_conversion_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: revise_before_canonical
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The current converted Markdown is not reliable for this staged draft's controlling row. It records Entry 172 as a Burgos/de la Cruz birth for Jose Miguel, while the source image, assigned chunk, source packet, and targeted QA note identify Entry 172 on page 58 as the Pulgar/Arriagada birth row.
2. Canonical promotion should not cite the stale converted Markdown as if it supported Pulgar/Arriagada. Use the image-reviewed QA/source-packet evidence path, or first revise the conversion-control layer.
3. The father name is supportable only as `Jose del Carmen Pulgar` for canonical purposes. The chunk's terminal `S.` reading remains possible but not sufficiently certain for promotion.
4. No Dario-line identity bridge is supported by this record. The source names Jose del Carmen Segundo Pulgar Arriagada, not Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada.
5. No proof-reviewed bridge supports merging `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar` from this source alone.

## Evidence Strengths

- The page image is a direct civil birth-register image for Los Angeles, Chile, 1888, pages 58-59, entries 171-176.
- Entry 172 is visibly the middle row on page 58 and agrees with the assigned chunk and targeted QA on the child name, sex, birth date/time, birthplace, mother, declarant, and most father-field content.
- The targeted QA note correctly isolates the conflict: the converted Markdown appears stale, row-shifted, or sourced from a different page/image set for this source identity.
- The staged identity analysis is appropriately conservative about Dario attachments, parent-candidate merges, and the father suffix.

## Scored Judgment

Primary claim reviewed: controlling physical Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

- source_quality_score: 0.88
- conversion_confidence_score: 0.74 for the image-reviewed chunk/QA row reading; 0.18 for the stale converted Markdown as a source for this claim
- evidence_quantity_score: 0.78
- agreement_score: 0.82 among source image, chunk, source packet, and targeted QA; 0.20 if the current converted Markdown is included unqualified
- identity_confidence_score: 0.86 for the named child within this record
- claim_probability: 0.90
- relevance_level: high
- relevance_confidence: 0.94
- canonical_readiness: revise_before_canonical

Secondary bounded findings:

- Father field as `Jose del Carmen Pulgar`: claim_probability 0.78; identity_confidence_score 0.70; canonical_readiness `ready_only_without_suffix_after_conversion-control_note`.
- Father suffix `S.`: claim_probability 0.42; canonical_readiness `hold`.
- Mother field as `Juana Arriagada de Pulgar`: claim_probability 0.88; identity_confidence_score 0.84; canonical_readiness `ready_after_row-control_handling`.
- Same-person bridge from `Juana Arriagada de Pulgar` to `Juana de Dios Amagada de Pulgar`: claim_probability 0.16; canonical_readiness `not_ready`.
- Any Dario-line same-person, parent-child, or lineage bridge from this source: claim_probability 0.04; canonical_readiness `not_ready`.

## Review Decision

The staged identity analysis is substantially supported as a conflict analysis and should be retained as a proof-reviewed hold/revise item. It should not be promoted as a clean canonical claim until the conversion conflict is explicitly handled. The most probable reading is that the physical Entry 172 row is the Pulgar/Arriagada registration, and the Burgos/de la Cruz content in the converted Markdown is not controlling for this source image.

## Next Action

Revise or annotate the conversion-control layer so the converted Markdown conflict is no longer silently carried into downstream claims. After that, promote only narrow Entry 172 claims for the child, registration date, birth date/time, birthplace, father without suffix, mother, and declarant. Keep the father suffix, Juana/Amagada identity bridge, and all Dario-line attachments on hold for separate proof review with direct supporting evidence.
