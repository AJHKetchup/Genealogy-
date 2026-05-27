---
type: proof_review_note
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527065927502
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031003832.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031003832.md"
reviewed_files:
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
  - "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
source_quality_score: 0.88
conversion_confidence_score: 0.46
evidence_quantity_score: 0.72
agreement_score: 0.62
identity_confidence_score: 0.76
claim_probability: 0.82
relevance_level: high
relevance_confidence: 0.94
canonical_readiness: hold_for_conversion_control
canonical_readiness_score: 0.12
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- Canonical readiness is `hold_for_conversion_control`. The visible source image and assigned chunk support physical entry `172` as the Pulgar/Arriagada row, but the current converted Markdown still records entry `172` as a different Burgos/de la Cruz birth. No claim or relationship should be promoted while the canonical converted file remains materially inconsistent with the controlling row evidence.
- The current converted Markdown is not reliable for entry `172` identity extraction. It gives child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and birth on 6 April 1888 at 10 p.m.; these details conflict with the visible row numbered `172` on page 58.
- The father suffix is not proof-ready. The chunk reads `Jose del Carmen Pulgar S.`, but the source packet and QA note deliberately certify only `Jose del Carmen Pulgar`; visual review does not make the terminal mark sufficiently certain for promotion.
- No Dario identity bridge is supported by this entry. The row does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada.
- Parent identity merges remain blocked. `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are supported as row-local parent names, but this entry alone does not prove broader same-person merges with other Jose or Juana candidates.

## Evidence Strengths

- The source is a civil birth register image, a strong direct source for the row-local child name, sex, birth date and place, parents as recorded, informant, and registration date.
- Visual review of the referenced page image supports the row-control finding: the row numbered `172` on page 58 reads as `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, born 8 March 1888 at 3 p.m. at Calle de Valdivia, with mother `Juana Arriagada de Pulgar` and informant `Ernesto Herrera L.`
- The assigned chunk, source packet, and targeted QA note agree on the Pulgar/Arriagada row as physical entry `172`; their disagreement is limited mainly to whether the father field includes a terminal `S.`
- The staged identity analysis accurately preserves the conflict rather than converting it into a promoted conclusion. Its hold recommendation is appropriate.

## Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration image is direct and relevant, though handwriting and image contrast limit certainty for small terminal marks. |
| conversion_confidence_score | 0.46 | Mixed derivative state: chunk and QA align with the image, but the current converted Markdown materially conflicts. |
| evidence_quantity_score | 0.72 | One direct register row plus chunk, packet, QA note, and converted file comparison; enough for row-control review, not enough for broader identity merges. |
| agreement_score | 0.62 | Strong agreement among image-reviewed staging files, but severe disagreement with the converted Markdown. |
| identity_confidence_score | 0.76 | Good confidence for the row-local Pulgar/Arriagada child and parents; low confidence for any cross-record identity bridge. |
| claim_probability | 0.82 | Probable that physical entry `172` is the Pulgar/Arriagada registration and that the converted file is stale, row-shifted, or mismatched. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada family extraction and high-risk for mistaken canonical attachment. |
| relevance_confidence | 0.94 | Relevance is clear because the row contains Pulgar and Arriagada names and is the assigned entry under review. |
| canonical_readiness | 0.12 | Hold; not ready for canonical claim, relationship, or identity promotion until conversion-control resolves the derivative conflict. |

## Proof Judgment

The staged draft is supported as a conflict analysis. The strongest supported judgment is that physical row `172` on register page 58 is the Pulgar/Arriagada birth registration, while the existing converted Markdown contains a materially conflicting Burgos/de la Cruz entry for the same entry number.

Use only bounded row-local claims at this stage: child candidate `Jose del Carmen Segundo Pulgar Arriagada`; father field bounded to `Jose del Carmen Pulgar` with suffix unresolved; mother field `Juana Arriagada de Pulgar`; birth on 8 March 1888 at 3 p.m.; registration on 7 April 1888; informant `Ernesto Herrera L.` No broader Dario, Jose, or Juana identity merge is proved.

## Next Action

Quarantine this staged analysis from promotion and route the conversion conflict to conversion-control. A focused crop or conversion-control correction should decide whether the father terminal mark is a suffix, abbreviation, or stray mark before any father-name suffix is used canonically. After the converted Markdown is repaired or superseded, a separate proof review can evaluate row-local child and parent claims for promotion.
