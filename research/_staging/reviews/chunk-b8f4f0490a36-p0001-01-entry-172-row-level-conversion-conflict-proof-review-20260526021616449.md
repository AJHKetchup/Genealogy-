---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526021616449
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: "2026-05-26"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The staged draft is materially supported as a conflict analysis, but the underlying conversion set is inconsistent: the source image and assigned chunk show entry 172 as a Pulgar/Arriagada birth row, while the current converted Markdown shows entry 172 as a Burgos/de la Cruz birth row.
2. The father field is readable only to a cautious level from the reviewed context. The row supports `Jose del Carmen Pulgar` and may support a trailing initial or mark, but the exact suffix should remain uncertified until targeted conversion QA.
3. No Dario identity bridge is present. The reviewed source supports a child named `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario`, `Dario Arturo`, `Dario Jose`, or a Pulgar-Smith identity.
4. Parent identity and duplicate-person conclusions are not ready. The entry may be relevant to Jose/Juana Pulgar-Arriagada clusters, but it does not prove that similarly named canonical candidates are the same people.
5. Canonical promotion remains blocked until the controlling conversion artifact is corrected or a QA note explicitly certifies the image/chunk row over the current converted Markdown.

## Evidence Strengths

- Civil birth registration is a strong source type for the child's name, sex, birth date, birth place, parents, and informant when the correct row is controlled.
- The source image visibly places entry number 172 on page 58 with the Pulgar/Arriagada row. The visible row aligns with the assigned chunk and source packet, not with the current converted Markdown.
- The assigned chunk gives direct row-level details for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 about 3 p.m. at Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- The staged draft accurately preserves the core uncertainty: it treats the Pulgar/Arriagada row as likely, but recommends hold for conversion QA rather than canonical promotion.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | A civil birth register image is high-quality direct evidence for birth and parentage facts, assuming row control is resolved. |
| conversion_confidence_score | 0.52 | The chunk and image agree, but the current converted Markdown directly contradicts them on the same entry number. |
| evidence_quantity_score | 0.70 | Review has one direct image, one assigned chunk, one source packet, and one conflicting converted file; enough to identify the conflict, not enough to promote. |
| agreement_score | 0.62 | Image, chunk, source packet, and staged draft agree on Pulgar/Arriagada; converted Markdown strongly disagrees. |
| identity_confidence_score | 0.78 | The entry-172 child identity as `Jose del Carmen Segundo Pulgar Arriagada` is strongly supported by image/chunk, reduced by unresolved conversion control. |
| claim_probability | 0.82 | It is probable that entry 172 in the image is the Pulgar/Arriagada row, but the canonical claim should not be promoted from conflicting conversion artifacts. |
| relevance_level | high | The row is directly relevant to Pulgar/Arriagada child-parent evidence and anti-conflation review. |
| relevance_confidence | 0.90 | The names `Pulgar` and `Arriagada` are visible/repeated in the supported row and source packet. |
| canonical_readiness | hold | Requires targeted conversion QA before any claim, relationship, merge, or Dario-line conclusion is promoted. |

## Claim Review

The staged draft's main claim, that this is a row-level conversion conflict requiring hold for conversion QA, is supported. The conflict is not a minor spelling variation. It changes the child, parents, birth date, birth time, place, and informant.

The Pulgar/Arriagada row is better supported by the source image and assigned chunk than the Burgos/de la Cruz row in the converted Markdown. However, this review should not rewrite the source transcription or promote canonical facts directly from the review note. The proper disposition is `hold_for_conversion_qa`.

The draft appropriately rejects Dario-line promotion. Shared surname context may make the source relevant for later Pulgar-family analysis, but it does not establish that the child in entry 172 is any Dario candidate or that the listed parents are duplicates of other Jose/Juana candidates.

## Next Action

Run targeted conversion QA against the source image, current converted Markdown, and assigned chunk to certify the controlling entry-172 row and father-field reading. After QA resolves row control, rerun proof review for the child identity, birth facts, parent-child relationships, and any separate parent-identity comparisons. Do not promote this item to canonical claims or relationships before that QA step.
