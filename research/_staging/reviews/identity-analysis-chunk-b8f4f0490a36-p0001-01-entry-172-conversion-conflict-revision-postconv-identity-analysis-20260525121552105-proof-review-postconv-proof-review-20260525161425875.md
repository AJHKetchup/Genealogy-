---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260525161425875
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md"
status: hold_revise_for_conversion_qa
canonical_readiness: hold_for_conversion_qa
review_date: 2026-05-25
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Conflict Analysis

## Blockers First

1. The staged draft correctly identifies a material row-level conflict between the chunk/source-packet reading and the assigned converted Markdown, but it inaccurately describes the current converted Markdown's entry 172 row. The staged draft says the converted file assigns entry 172 to `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`; the current converted file actually reads entry 172 as `José Miguel`, father `Oswaldo Bunster`, mother `Amelia de la Maza`.
2. The conflict still blocks promotion because the converted Markdown and the chunk/source packet describe different entry-172 child-parent clusters. This is not a spelling variant.
3. The source image visibly supports the Pulgar/Arriagada row for entry 172 more strongly than the converted Markdown row, but the father-name ending remains uncertain. The review can support "Pulgar/Arriagada row likely," not a final exact father-name form.
4. No Dario-line identity bridge is visible in the reviewed source image, chunk, source packet, or converted file. Any connection to Dario, Arturo, Smith, Dario Jose, or Darío Pulgar Arriagada remains unsupported by this entry alone.
5. Canonical pages and prior reviews were not treated as independent proof for this review because the assignment limits verification to the staged draft and the referenced conversion/chunk/source packet/source image needed to verify it.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md`.
- Conflict draft referenced by staged draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md`.
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted file: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source image shows page 58, entry 172 as a male child named `Jose del Carmen Segundo Pulgar Arriagada`, with mother `Juana Arriagada de Pulgar`; this matches the chunk and source packet at the row level.
- The chunk and source packet preserve a coherent civil birth registration: registration date 7 April 1888, birth date 8 March 1888, birth place Calle de Valdivia, parents at Calle de Colipí, and informant Ernesto Herrera L.
- The staged draft's main proof judgment, `hold_for_conversion_qa`, is appropriate because the converted file currently points to a different entry-172 row and cannot be used as harmonized support.
- The staged draft appropriately rejects Dario-line promotion from this entry; no reviewed source names Dario, Arturo, Smith, or a later Pulgar identity bridge.

## Scores

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth registration is a strong source class, and the source image is available for direct review. |
| conversion_confidence_score | 0.45 | The chunk and source packet align with the source image, but the assigned converted Markdown is materially inconsistent. |
| evidence_quantity_score | 0.65 | There is one relevant source image plus derivative chunk/source-packet support; no independent corroborating record was reviewed. |
| agreement_score | 0.52 | Source image, chunk, and source packet agree on the Pulgar/Arriagada row; converted Markdown disagrees, and the staged draft misquotes that converted row. |
| identity_confidence_score | 0.74 for entry 172 as the Pulgar/Arriagada child; 0.05 for any Dario-line bridge | The visible row supports the Pulgar/Arriagada child identity, but Dario linkage is absent. |
| claim_probability | 0.74 | Probable that the source page's entry 172 is the Pulgar/Arriagada birth registration; not ready for canonical use until conversion QA resolves the derivative conflict. |
| relevance_level | high | If confirmed, the row is directly relevant to Pulgar/Arriagada parent-child identity work. |
| relevance_confidence | 0.88 | The source-visible surnames and parent-child structure are family-relevant, but exact downstream identity placement remains blocked. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, merges, or Dario identity bridges until targeted conversion QA and a renewed proof review are complete. |

## Review Judgment

Revise/hold. The staged draft's final `hold_for_conversion_qa` recommendation is supported, and its caution against Dario-line identity promotion is supported. However, the draft should not be accepted as written because it incorrectly states the current converted Markdown's conflicting entry-172 names. The accurate blocker is: chunk/source packet/source image support `Jose del Carmen Segundo Pulgar Arriagada`, father read as `Jose del Carmen Pulgar` with an uncertain ending, and mother `Juana Arriagada de Pulgar`; the current converted Markdown instead gives entry 172 as `José Miguel`, father `Oswaldo Bunster`, mother `Amelia de la Maza`.

## Next Action

Run targeted conversion QA against the source image, converted file, and chunk. The QA note should explicitly settle the controlling entry-172 row and record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim, relationship, parent merge, or Dario-line comparison is promoted.
