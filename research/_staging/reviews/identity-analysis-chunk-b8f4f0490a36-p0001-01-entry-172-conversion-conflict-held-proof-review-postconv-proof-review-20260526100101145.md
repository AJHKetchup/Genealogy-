---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526100101145
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526085239273.md"
reviewed_staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526085239273.md"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Analysis Conversion Conflict

- Review task id: `proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526085239273.md`
- Reviewed staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526085239273.md`
- Role: claim_reviewer
- Review status: hold
- canonical_readiness: hold_for_conversion_qa

## Blockers

- The converted Markdown file still records entry 172 as a Burgos/de la Cruz birth for `Jose Miguel`, while the assigned chunk, held source packet, and visible page image support a different Pulgar/Arriagada row for entry 172. This is a controlling row conflict and blocks canonical use.
- The visible page image supports the Pulgar/Arriagada identity analysis in broad outline, but the father's terminal mark after `Jose del Carmen Pulgar` is not certified by this proof review. Do not normalize it to `Jose del Carmen Pulgar` or promote it as `Jose del Carmen Pulgar S.` without targeted conversion QA.
- Parent-child claims for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar [?]`, and `Juana Arriagada de Pulgar` depend on resolving the conversion conflict first.
- The staged draft correctly rejects a same-person or direct relationship bridge to Dario-line candidates. No reviewed source states that the entry-172 child is Dario, a Dario variant, or an intermediate ancestor/relative of a Dario-line person.

## Scoring

- source_quality_score: 0.88
- conversion_confidence_score: 0.42
- evidence_quantity_score: 0.62
- agreement_score: 0.48
- identity_confidence_score: 0.68
- claim_probability: 0.70
- relevance_level: high
- relevance_confidence: 0.90
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The underlying source is a civil birth register image for Los Angeles, Chile, 1888, with entry numbers and a tabular structure that directly records child, birth date/place, parents, and informant.
- The visible page image shows page 58, entry 172 as the Pulgar/Arriagada row rather than the Burgos/de la Cruz row recorded in the current converted Markdown.
- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m., with father beginning `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The held source packet and staged identity analysis both explicitly preserve the conversion conflict and recommend holding dependent claims instead of promoting them.
- The staged identity analysis properly treats Dario-line linkage as unsupported and avoids a same-person merge, name-variant assertion, or relationship jump.

## Review Judgment

The staged identity analysis is substantially supported as a conflict assessment. The source image and assigned chunk make the Pulgar/Arriagada reading more probable than the Burgos/de la Cruz derivative reading for page 58, entry 172. However, canonical readiness remains blocked because the current converted Markdown contradicts the controlling row and the father-name ending is still uncertain.

The safest proof judgment is `hold_for_conversion_qa`. The Pulgar/Arriagada child identity and parent-name claims are plausible and relevant, but they should not be promoted until targeted conversion QA reconciles the converted Markdown and certifies the father field.

## Next Action

Run targeted conversion QA against `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`, and `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.

QA must decide whether entry 172 controls to the Pulgar/Arriagada row or the Burgos/de la Cruz row and must certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before promoting any child identity, birth fact, parent-name fact, parent-child relationship, or Dario-line comparison.
