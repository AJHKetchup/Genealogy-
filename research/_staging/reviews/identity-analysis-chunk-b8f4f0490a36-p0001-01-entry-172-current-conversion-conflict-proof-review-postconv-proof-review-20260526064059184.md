---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526064059184
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044737235.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044737235.md"
reviewed_context:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
review_decision: hold
canonical_readiness: blocked
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

1. The staged draft is supported as a conflict analysis, but the underlying evidence remains blocked for canonical use because the assigned chunk and current converted Markdown disagree on the controlling entry-172 row.
2. The current converted Markdown reads entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the chunk/source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
3. The page image visually supports the Pulgar/Arriagada row at entry 172 more than the current converted Markdown, but this review is not a source-transcription correction pass. The converted Markdown conflict must be resolved through targeted conversion QA before any canonical claim promotion.
4. The father-field reading remains a proof blocker at fine-grained level. The visible field may support `Jose del Carmen Pulgar S.`, but QA should certify only what is visible and preserve uncertainty if needed.
5. No parent-child relationship, same-person merge, duplicate-person resolution, or Dario-line bridge is proof-ready from this staged draft.

## Scores

| Category | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a strong primary source, but the review is constrained by conflicting derivative transcriptions. |
| conversion_confidence_score | 0.35 | The chunk is coherent and the page image broadly supports it, but the current converted Markdown gives a materially different entry 172. |
| evidence_quantity_score | 0.55 | One primary page image plus two derivative transcriptions are available; there is no independent corroborating source in this review scope. |
| agreement_score | 0.40 | Source packet, chunk, and image align toward Pulgar/Arriagada, but converted Markdown conflicts on every identity-bearing field. |
| identity_confidence_score | 0.62 | Pulgar/Arriagada is the better-supported entry-172 identity in the reviewed context, but not proof-ready while conversion state is unresolved. |
| claim_probability | 0.84 | The staged draft's claim that this is a material conversion-row conflict is strongly supported. The Pulgar/Arriagada row as controlling is probable but still requires QA certification. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent candidates; only anti-conflation context for Dario-related candidates. |
| relevance_confidence | 0.92 | The family surnames and entry number are specific, and the conflict directly affects named candidate relationships. |
| canonical_readiness | blocked | Hold until targeted conversion QA resolves the row and the proof review is rerun against corrected conversion context. |

## Evidence Strengths

- The staged draft accurately identifies a row-level conflict, not a spelling variant or ordinary name uncertainty.
- The assigned chunk and source packet agree on the Pulgar/Arriagada reading for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`, birth date `Ocho de Marzo de mil ochocientos ochenta i ocho`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The source image, checked visually for the relevant row only, appears to support the chunk/source-packet Pulgar/Arriagada reading rather than the current converted Markdown's Burgos/de la Cruz reading.
- The staged draft correctly avoids using same-cluster wiki pages as independent corroboration and correctly blocks Dario-line bridges.

## Review Findings

The staged draft is acceptable as a proof-risk and identity-conflict analysis. Its `hold_for_conversion_qa` recommendation is well supported.

Do not promote the child identity, birth facts, father claim, mother claim, informant claim, or parent-child relationships from this staged draft. The apparent image support for Pulgar/Arriagada should be handled by conversion QA, not by silently overriding the converted Markdown inside proof review.

## Next Action

Send this source to targeted conversion QA. QA should compare the image, chunk, source packet, and converted Markdown for `CHUNK-b8f4f0490a36-P0001-01`; decide the controlling transcription for entry 172; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` according to the visible source.

After QA resolves the conversion conflict, rerun proof review for any child identity, birth-event, parent-name, parent-child, duplicate-person, or Pulgar/Dario-line bridge claims.
