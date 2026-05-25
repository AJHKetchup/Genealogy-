---
type: proof_review
status: reviewed_hold
role: claim_reviewer
worker: postconv-proof-review-20260525081308835
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict Analysis

## Blockers First

1. Canonical readiness is blocked by a material row-level conversion conflict. The current chunk and page image support entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the assigned converted Markdown gives entry 172 as `Jose Francisco`, child of `Oswaldo Gomez` and `Emilia de la Cruz`.

2. The staged identity analysis correctly treats the conflict as conversion/file-assignment level, not as a same-person name variant. However, no dependent claim or relationship should be promoted until conversion QA reconciles why the converted file disagrees with the chunk and visible page.

3. The father field remains a literal-reading blocker. The chunk reads `Jose del Carmen Pulgar S.` and the image appears broadly consistent with a Pulgar father entry, but this review does not certify the final mark after `Pulgar`; preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as QA outcomes.

4. No Dario-line attachment is supported by this source. The reviewed entry does not name Dario, Arturo, Smith, Geneva, ICRC, occupation, passenger travel, expropriation, spouse, child, or any bridge to a Dario canonical page.

## Evidence Checked

- Staged draft under review: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041.md`.
- Referenced conflict note: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525051608746.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md`.
- Referenced current chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

No external research was performed. No raw source, converted Markdown, chunk Markdown, or canonical wiki page was edited.

## Scored Judgment

| Claim / issue reviewed | source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| Draft's main conclusion that entry 172 is blocked by row-level conversion conflict | 0.86 | 0.42 | 0.78 | 0.38 | 0.72 | 0.90 | high | 0.96 | hold_for_conversion_qa |
| Current chunk/source-packet Pulgar-Arriagada identity cluster as the likely intended row | 0.86 | 0.58 | 0.72 | 0.74 | 0.76 | 0.82 | high | 0.94 | hold_for_conversion_qa |
| Assigned converted Markdown row as controlling evidence for this staged identity draft | 0.72 | 0.28 | 0.55 | 0.12 | 0.18 | 0.12 | medium | 0.80 | not_ready |
| Parent relationship: Jose del Carmen Pulgar/Pulgar S. as father | 0.84 | 0.55 | 0.68 | 0.70 | 0.68 | 0.74 | high | 0.90 | hold_for_father_field_qa |
| Parent relationship: Juana Arriagada de Pulgar as mother | 0.84 | 0.62 | 0.70 | 0.78 | 0.76 | 0.82 | high | 0.92 | hold_for_conversion_qa |
| Any same-person or direct-line claim involving Dario Arturo Pulgar-Smith / Dario Pulgar Arriagada | 0.84 | 0.56 | 0.30 | 0.18 | 0.05 | 0.03 | low_for_direct_identity; medium_for_anti_conflation | 0.88 | do_not_attach |

## Evidence Strengths

- The staged draft's central blocker is literally supported by the referenced files: the chunk/source packet and converted Markdown describe different entry-172 rows.
- The source packet accurately preserves the current chunk's family-relevant reading and warns that the converted Markdown conflict must be resolved before promotion.
- The page image provides direct source context and visibly supports that the left-page entry 172 row is a Pulgar/Arriagada-style registration rather than the converted Markdown's Gomez/de la Cruz row.
- The draft appropriately separates identity analysis from transcription correction. It does not silently rewrite the converted file or promote a corrected canonical version.
- The anti-conflation cautions are justified: the source does not contain a Dario bridge and should not be used to attach Dario identities by surname similarity.

## Review Finding

The staged identity analysis is substantially supported as a proof judgment. Its promotion recommendation should remain `hold_for_conversion_qa`, not because the Pulgar/Arriagada row is weak, but because the assigned conversion artifacts are internally inconsistent and the father-field ending still needs targeted source-visible QA.

The strongest supported claim is narrow: current evidence favors that the intended entry-172 family-relevant row concerns `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`/`Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`. This should remain provisional until the converted Markdown conflict is resolved.

## Next Action

Targeted conversion QA should reconcile the page image, current chunk, and assigned converted Markdown for page 58, entry 172. The QA note should decide whether the converted file is wrong or misassigned, and should certify the exact father-field reading after `Pulgar`. After that, rerun proof review before any canonical claim, relationship, parent merge, or Dario-line comparison is promoted.
