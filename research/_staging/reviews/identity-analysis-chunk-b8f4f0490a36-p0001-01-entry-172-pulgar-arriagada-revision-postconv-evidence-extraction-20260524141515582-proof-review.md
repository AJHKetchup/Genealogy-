---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260524145822135
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- The referenced converted Markdown and referenced chunk disagree at the row level. The converted file transcribes entry 172 as a Gomez/de la Cruz birth registration, while the chunk and visible page image support a Pulgar/Arriagada birth registration for entry 172. This is not a normal spelling or normalization issue.
- The father's exact suffix or final mark after `Jose del Carmen Pulgar` is not settled enough for canonical identity use. The chunk reads `Jose del Carmen Pulgar S.`, but the staged draft correctly keeps this uncertain.
- Do not connect this entry to any Dario candidate. The staged draft's guardrail is supported: the visible entry and derivative chunk do not name Dario.

## Scores

- source_quality_score: 0.86
- conversion_confidence_score: 0.40
- evidence_quantity_score: 0.62
- agreement_score: 0.45
- identity_confidence_score: 0.70
- claim_probability: 0.74
- relevance_level: high
- relevance_confidence: 0.86
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The page image is a civil birth register spread, a strong primary source type for birth identity, parent names, birth date/place, and informant when the row is correctly identified.
- Direct visual review supports that page 58 entry 172 is the Pulgar/Arriagada row rather than the Gomez/de la Cruz row in the converted Markdown.
- The chunk supports the core identity cluster: child `Jose del Carmen Segundo Pulgar Arriagada`, father broadly `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The staged draft accurately preserves uncertainty and does not over-promote the father suffix or make a relationship jump to unrelated Dario identities.

## Review Judgment

The staged identity analysis is materially cautious and source-bound. The core claim that the page image/chunk contain a Pulgar/Arriagada entry at no. 172 is probable, but the referenced conversion conflict lowers conversion confidence and agreement. This should remain out of canonical claim, relationship, and person/family pages until conversion QA reconciles the converted Markdown with the source image and chunk.

## Next Action

Send to targeted conversion QA. The QA note should resolve the row-level conflict in the converted Markdown and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` based only on visible source support. After that, rerun proof review for child identity, birth facts, child-parent relationships, and any proposed parent-candidate merge.
