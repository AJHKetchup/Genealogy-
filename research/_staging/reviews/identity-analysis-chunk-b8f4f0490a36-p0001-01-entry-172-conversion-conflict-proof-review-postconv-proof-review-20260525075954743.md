---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525075954743
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict

## Blockers First

1. The staged draft is correct to block canonical promotion because the referenced converted Markdown and the referenced chunk do not agree on entry 172. The converted Markdown identifies entry 172 as `Jose Francisco`, child of `Oswaldo Gomez` and `Emilia de la Cruz`, while the chunk and visible source image identify entry 172 as a Pulgar/Arriagada birth registration.

2. The source image supports the Pulgar/Arriagada row for entry 172, but the father-name ending remains uncertain at proof-review level. I can verify `Jose del Carmen Pulgar` as the controlling father reading from the row context; I cannot safely promote the trailing `S.` without targeted conversion QA.

3. No canonical identity, parent-child relationship, or same-person merge should be promoted from this staged draft. The row-level conversion conflict must be resolved before claims about the child, father, mother, residences, or parent candidates are made canonical.

4. The draft's anti-conflation warning is supported. Entry 172 does not visibly name Dario, Arturo, Smith, Geneva/ICRC, Alexander John Heinz, a spouse, an adult occupation bridge, or any lineage bridge to a canonical Dario page.

5. The comparison between `Juana Arriagada de Pulgar` and separate entry-513 `Juana de Dios Amagada/Amador de Pulgar` candidates remains a lead only. This entry does not provide enough evidence for that same-person conclusion.

## Evidence Strengths

- The source type is strong for birth facts: an 1888 civil birth registration image from Los Angeles, Chile.
- The source image and the chunk agree on the core entry-172 identity cluster: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at Calle de Valdivia, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The staged draft accurately treats the converted Markdown conflict as material and not as a spelling variant.
- The staged draft appropriately keeps Dario-related hypotheses below promotion threshold because there is no literal Dario support in this entry.
- The staged draft preserves uncertainty instead of rewriting the source transcription or silently normalizing the father name.

## Scores

| Review dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil registration image is a high-quality genealogical source, though the image is a photographed spread with some handwriting difficulty. |
| conversion_confidence_score | 0.42 | The chunk aligns with the visible source image, but the assigned converted Markdown is materially wrong for this row. |
| evidence_quantity_score | 0.58 | There is one directly relevant source image and derivative chunk; no independent corroborating source was reviewed or required for this hold decision. |
| agreement_score | 0.48 | Source image, source packet, staged conflict, and chunk agree; assigned converted Markdown conflicts materially. |
| identity_confidence_score | 0.70 | The Pulgar/Arriagada entry-172 identity is visually plausible, but proof confidence is held down by the conversion conflict and father suffix uncertainty. |
| claim_probability | 0.72 | The draft's main claim that entry 172 likely concerns the Pulgar/Arriagada cluster is more likely than not, but not ready for canonical use. |
| relevance_level | high | Pulgar and Arriagada are named in the supported row, and the source packet marks the row family-relevant. |
| relevance_confidence | 0.90 | Family relevance is strong for Pulgar/Arriagada research; relevance to Dario-specific identities is low and correctly rejected. |
| canonical_readiness | hold_for_conversion_qa | Canonical promotion is blocked until conversion QA reconciles the converted file, chunk, and image. |

## Claim Judgment

The staged draft should remain a hold, not a promoted claim. Its central analysis is supported: the current chunk and visible source image point to a Pulgar/Arriagada entry 172, while the assigned converted Markdown points to a different row/person cluster. This is a conversion or file-assignment problem, not an identity variant.

The most defensible working probability is:

- Pulgar/Arriagada row is the intended entry-172 evidence cluster: 0.72.
- Assigned converted Markdown is not reliable for this row: 0.78.
- Direct attachment to any Dario identity from this entry: 0.03.
- Same-person merge between entry-172 `Juana Arriagada de Pulgar` and entry-513 `Juana de Dios Amagada/Amador de Pulgar`: 0.14.

## Next Action

Targeted conversion QA should reconcile the source image, chunk, and converted Markdown for page 58, entry 172. The QA note should explicitly decide whether the converted Markdown is from a wrong row/file assignment and should record the father field as source-visible `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any claim, relationship, parent-candidate merge, or canonical page update.
