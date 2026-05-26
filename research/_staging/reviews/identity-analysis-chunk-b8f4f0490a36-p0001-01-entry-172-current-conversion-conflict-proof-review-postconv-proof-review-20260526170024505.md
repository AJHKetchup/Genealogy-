---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526170024505
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-identity-researcher-20260526140101459.md
reviewed_staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-identity-researcher-20260526140101459.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526095657171.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
chunk_id: CHUNK-b8f4f0490a36-P0001-01
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict Identity Analysis

## Blockers

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-identity-researcher-20260526140101459.md`.
- The row-level conversion conflict is real and material. The current converted Markdown labels entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the chunk, source packet, and visible source image support a Pulgar/Arriagada row for entry 172.
- This disagreement changes the child, parents, birth date, birth place, informant, and surrounding row context. It is not a spelling variant or minor transcription uncertainty.
- The father field should not be over-certified. The source packet's safe reading is `Jose del Carmen Pulgar`; the chunk reads `Jose del Carmen Pulgar S.`, but the final initial or trailing mark remains a targeted QA issue.
- No parent-child relationship, person merge, name variant, Dario-line bridge, or canonical birth fact should be promoted until conversion QA reconciles the source image, converted Markdown, chunk, and source packet.

## Scoring

- source_quality_score: 0.88
- conversion_confidence_score: 0.34
- evidence_quantity_score: 0.66
- agreement_score: 0.44
- identity_confidence_score: 0.70
- claim_probability: 0.76
- relevance_level: critical
- relevance_confidence: 0.96
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The source is a direct civil birth registration image for Los Angeles, Chile, 1888, with page 58 and entry number 172 visible.
- The chunk gives a coherent Pulgar/Arriagada reading for entry 172: `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source packet correctly preserves the conversion conflict, reports image review favoring the Pulgar/Arriagada row, and keeps promotion at `hold_for_conversion_qa`.
- Visual inspection of the source image supports the source packet's basic conclusion that page 58, entry 172 is the Pulgar/Arriagada row rather than the Burgos/de la Cruz row.
- The staged identity analysis handles identity risk appropriately by rejecting surname-only bridges to Dario candidates and by warning against treating existing canonical pages as independent proof.

## Review Judgment

The staged identity analysis is supported as a conflict analysis. Its main conclusion, that the Pulgar/Arriagada row is probably the controlling entry 172 while canonical use remains blocked, is consistent with the source packet, chunk, and visible page image.

The proof value is still not canonical-ready because the converted Markdown remains an incompatible derivative transcription for the same entry number. The safest scored judgment is a high-relevance hold: probable Pulgar/Arriagada identity evidence, low conversion confidence, and no authority to promote dependent facts or relationships.

## Next Action

Send this source cluster to targeted conversion QA. QA should decide whether the converted Markdown should be corrected to the Pulgar/Arriagada row or whether a page/row assignment error explains the mismatch, and should certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review on the child identity, birth facts, father claim, mother claim, parent-child relationships, and any Pulgar-line Dario comparison.
