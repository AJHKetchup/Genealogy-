---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526003932000
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525234847240.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525234847240.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical promotion is blocked by a severe row-control conflict. The source image and assigned chunk show entry 172 as the Pulgar/Arriagada birth row; the current converted Markdown describes a Burgos/de la Cruz birth row.
- The conflict changes all identity-bearing facts: child name, parents, birth date, birth place, informant, and surrounding family cluster.
- The father field in the Pulgar/Arriagada row should remain cautiously certified as beginning `Jose del Carmen Pulgar`; the trailing mark or suffix is not fully resolved in this proof review.
- No child identity, parent-child relationship, parent identity merge, or Dario/Pulgar comparison should be promoted from this draft until targeted conversion QA resolves the controlling row and father-field reading.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525234847240.md`.
- Conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

No external research was performed. No raw source, converted Markdown, chunk, or canonical page was edited.

## Literal Support Check

The assigned chunk transcribes page 58, entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.

The source image visibly supports the same row placement: entry number 172 on page 58 is a Pulgar/Arriagada row, not the Burgos/de la Cruz row in the converted Markdown. The child and mother readings are sufficiently supported for a held candidate. The father reading is materially supported as `Jose del Carmen Pulgar`, but the trailing suffix or mark remains uncertain enough to require conversion QA rather than proof-review correction.

The current converted Markdown records entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`, with informant `Oswaldo Burgos`. That converted text is not supported for this specific row by the viewed image and assigned chunk.

## Scored Judgment

| metric | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register page image is a direct source for the birth registration, but the image quality and handwriting leave a narrow father-suffix uncertainty. |
| conversion_confidence_score | 0.32 | The assigned chunk matches the image for row identity, but the current converted Markdown is materially wrong for entry 172, so conversion reliability for this item is low until QA resolves it. |
| evidence_quantity_score | 0.62 | Evidence consists of one direct source image, one assigned chunk, one source packet, and one conflicting conversion. It is enough to identify a row conflict, not enough for canonical promotion. |
| agreement_score | 0.48 | Source image, chunk, source packet, and conflict draft agree on Pulgar/Arriagada row control; the converted Markdown strongly disagrees. |
| identity_confidence_score | 0.70 | The child candidate `Jose del Carmen Segundo Pulgar Arriagada` is likely the entry-172 child in the source image, but row-control QA and father-field certification remain required. |
| claim_probability | 0.78 | Probable that the Pulgar/Arriagada row is the correct row for entry 172; not yet ready to promote as a canonical claim because the conversion layer conflicts. |
| relevance_level | 0.95 | Directly relevant to Pulgar/Arriagada identity and parent-child claims. |
| relevance_confidence | 0.96 | The source image and chunk both place Pulgar and Arriagada names in the target entry 172 row. |
| canonical_readiness | 0.10 | Hold. Canonical promotion would risk importing a known conversion conflict and uncertain father suffix. |

## Proof Decision

Decision: `hold_for_conversion_qa`.

The staged identity analysis is well supported as a conflict analysis. It should not be treated as proof of a promotable child identity or relationship yet. The appropriate claim-level conclusion is that entry 172 has a conversion-control conflict and requires targeted QA.

## Evidence Strengths

- The source image directly shows page 58, entry 172 as a Pulgar/Arriagada row.
- The assigned chunk and source packet independently preserve the same family-relevant row structure.
- The conflict is clearly bounded and not a speculative identity problem: it is a conversion or row-control problem.
- The staged draft correctly avoids merging the child with Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or other Pulgar/Dario candidates.

## Next Action

Run targeted conversion QA on `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` against the converted Markdown and chunk. QA should decide whether the controlling entry-172 transcription is the Pulgar/Arriagada row and should certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any child identity, birth fact, father relationship, mother relationship, or Pulgar/Dario identity comparison.
