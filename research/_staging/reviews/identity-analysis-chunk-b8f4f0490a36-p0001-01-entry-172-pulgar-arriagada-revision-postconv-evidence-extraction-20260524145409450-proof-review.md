---
type: proof_review
status: draft
role: claim_reviewer
worker: postconv-proof-review-20260524154447655
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524145409450.md"
reviewed_staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524145409450.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524145409450.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
review_status: hold
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- The reviewed identity analysis depends on a visible source-image/chunk reading of entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, but the referenced converted file transcribes entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`. This is a row-level conflict, not a minor spelling or normalization issue.
- The referenced chunk supports the Pulgar/Arriagada row, while the referenced converted file gives a different family for the same entry number. Canonical promotion should wait until conversion QA explains, corrects, or supersedes the conflicting derivative transcript.
- The father's final name element remains unresolved. The chunk reads `Jose del Carmen Pulgar S.`, while the draft correctly preserves uncertainty as no suffix, `S.`, or an unresolved final mark. Do not normalize this father identity beyond what conversion QA and direct source review can support.
- This source does not name Dario. Any attachment to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario Pulgar Arriagada, or a Dario passenger candidate would be an unsupported relationship or identity jump.

## Scoring

- source_quality_score: 0.86
- conversion_confidence_score: 0.42
- evidence_quantity_score: 0.62
- agreement_score: 0.48
- identity_confidence_score: 0.74
- claim_probability: 0.76
- relevance_level: high
- relevance_confidence: 0.90
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The original source image is present and visibly shows page 58, entry 172 as the Pulgar/Arriagada entry, including the child name, sex, registration date, birth date, birth place, father, mother, and informant fields.
- The referenced chunk directly supports the core family cluster: child `Jose del Carmen Segundo Pulgar Arriagada`, father broadly `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The staged identity analysis accurately flags the conversion/file-assignment conflict and recommends `hold_for_conversion_qa` rather than treating the image reread as canonically settled.
- The draft appropriately limits the evidence to the entry 172 Pulgar/Arriagada cluster and explicitly blocks Dario-based identity attachment by surname or family context alone.

## Review Judgment

The visible civil birth register image and the assigned chunk give moderately strong support for the Pulgar/Arriagada identity cluster in entry 172. On image evidence alone, the identity-analysis probability is moderately high. However, the referenced converted file contradicts the same entry at the row level, so the derivative evidence set is not reliable enough for canonical promotion.

Keep this staged identity analysis on hold for conversion QA. The current draft is directionally sound as a warning and review aid, but not ready to promote into canonical claims, relationships, or wiki pages.

## Next Action

Send this item to conversion QA to reconcile the referenced converted file and chunk against the source image for page 58, entry 172. QA should explicitly decide whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form, then rerun proof review before any canonical use.
