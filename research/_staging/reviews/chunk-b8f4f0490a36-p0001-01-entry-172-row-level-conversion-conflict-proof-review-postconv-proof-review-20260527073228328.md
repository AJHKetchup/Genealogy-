---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527073228328
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md"
reviewed_staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

- Review task id: `proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md`
- Reviewed staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md`
- Role: claim_reviewer
- Review status: hold
- canonical_readiness: hold_for_conversion_qa

## Blockers

- The current converted Markdown still records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the source image, assigned chunk, source packet, and targeted QA note support the visible physical row `172` as the Pulgar/Arriagada birth entry.
- The derivative conflict is row-level and relationship-impacting. Until conversion-control reconciles, supersedes, or annotates the converted Markdown, this evidence should not be promoted into canonical claims, relationships, person pages, family pages, or merge decisions.
- The father field should remain bounded to `Jose del Carmen Pulgar`. The terminal mark or suffix after `Pulgar` is not clear enough in the reviewed materials to promote as part of the name.
- This staged draft does not provide a Dario identity bridge. It should not be attached to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or any `Dario/Dario Pulgar Arriagada` variant without separate bridging proof.
- Parent identity merges remain unproved. The entry may be relevant to future `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` work, but it does not prove same-person identity with other Jose/Juana candidates by itself.

## Scoring

- source_quality_score: 0.88
- conversion_confidence_score: 0.54
- evidence_quantity_score: 0.72
- agreement_score: 0.58
- identity_confidence_score: 0.86
- claim_probability: 0.89
- relevance_level: critical
- relevance_confidence: 0.96
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The original page image is available and visibly shows page 58 with entry `172` on the left page as the Pulgar/Arriagada row.
- Direct image inspection supports the targeted QA note's row-control conclusion: the visible child name reads as `Jose del Carmen Segundo Pulgar Arriagada`, with mother `Juana Arriagada de Pulgar`, and no visible support for the Burgos/de la Cruz child-parent set at physical row `172` on this image.
- The assigned chunk, source packet, conflict draft, and targeted conversion QA note consistently identify the physical row `172` as the Pulgar/Arriagada entry.
- The staged identity analysis correctly keeps the Dario-line attachment, parent-candidate merges, father-name suffix, and canonical promotion on hold.

## Review Judgment

The staged draft is well supported as a conflict analysis. The strongest evidence is the source image itself, which supports the row-control claim that physical entry `172` on register page 58 is the Pulgar/Arriagada birth entry. The conflicting Burgos/de la Cruz text in the converted Markdown appears derivative and incompatible with the visible row in the cited image.

The proof result is not ready for canonical promotion because the workspace still contains two incompatible derivative readings for the same entry number and source path. Treat the Pulgar/Arriagada row-control finding as probable and relevant for QA routing, but keep tree-impacting use on hold until the conversion layer is reconciled.

## Next Action

Send this item to conversion-control or conversion QA to reconcile the converted Markdown and chunk lineage against the visible source image for page 58, physical row `172`. After that is resolved, run a focused parent-identity review for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`; do not use this review to attach the entry to any Dario-line identity or to merge Jose/Juana candidates.
