---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260525171028774
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
review_status: hold_with_revision_needed
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity/Conflict Analysis

## Blockers First

1. The staged draft's central conclusion is supported: entry 172 has a row-level derivative conflict and is not ready for canonical promotion.
2. The staged draft should be revised before reuse because its exact description of the referenced converted Markdown is not fully literal. The converted file reviewed here records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born `En veinte de Febrero de mil ochocientos ochenta i ocho, a las diez de la noche`, place `En Pellin`. The staged draft instead says the converted file names mother `Emilia de la Cruz`, birth date `veinte i seis de Marzo`, and place `En esta`.
3. The source image and current chunk support the Pulgar/Arriagada row for entry 172, but the conflict with the assigned converted file still requires conversion QA before any identity, parent-child, or same-person claim is promoted.
4. The father field remains source-visible but not safely final for canonical identity work: keep the form open as `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]` until targeted QA.
5. No Dario-line bridge is present in this entry. Any attachment to Dario/Pulgar candidates by surname pattern alone remains unsupported.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md`
- Conflict draft referenced by staged draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md`
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md`
- Current chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`

## Evidence Strengths

- The source image is available and visually supports the current chunk's broad row assignment for entry 172 as the Pulgar/Arriagada registration rather than the converted file's Gomez/de la Cruz row.
- The current chunk gives a coherent row for entry 172: `Jose del Carmen Segundo Pulgar Arriagada`, male, registration date 7 April 1888, birth 8 March 1888 at 3 p.m., place `Calle de Valdivia`, father read as `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The staged draft correctly treats this as a conversion or assignment conflict, not as a spelling variant, duplicate-person proof, or relationship proof.
- The staged draft correctly blocks Dario-line attachment; the entry does not name Dario, Arturo, Smith, a spouse, child, occupation bridge, passenger context, or later-life identity.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth registration image is a strong primary source class, and the image is available for review. |
| conversion_confidence_score | 0.36 | The current chunk and converted file assign materially different entry-172 rows. |
| evidence_quantity_score | 0.54 | One relevant register entry plus derivative layers; no independent corroborating source reviewed for identity linkage. |
| agreement_score | 0.46 | Image, source packet, and current chunk agree broadly on the Pulgar/Arriagada row, but the assigned converted Markdown conflicts sharply. |
| identity_confidence_score | 0.66 | Pulgar/Arriagada row identity is probable from image/chunk review but capped by derivative conflict and father-field uncertainty. |
| claim_probability | 0.66 for Pulgar/Arriagada row identity; 0.04 for any Dario-line attachment | The row probably concerns Jose del Carmen Segundo Pulgar Arriagada if the image/chunk is certified; no Dario bridge is present. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada parent-child candidates and to anti-conflation controls. |
| relevance_confidence | 0.92 | The entry clearly contains Pulgar/Arriagada names in the image/current chunk if that row is controlling. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, person merges, or Dario comparisons until targeted conversion QA reconciles the source image, chunk, and converted file. |

## Next Action

Targeted conversion QA should certify the controlling entry-172 row against the source image and reconcile the converted Markdown mismatch. The QA note should explicitly record whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row and should preserve the father-field ending as source-visible rather than normalized. After QA, rerun proof review on the certified child identity, birth facts, father candidate, mother candidate, and parent-child relationship claims.
