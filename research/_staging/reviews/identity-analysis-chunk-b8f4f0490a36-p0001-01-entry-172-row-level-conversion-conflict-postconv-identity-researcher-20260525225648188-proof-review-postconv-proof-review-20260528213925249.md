---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260528213846674"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225648188.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225648188.md"
output_area: "research/_staging/reviews/"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The assigned identity-analysis draft cannot be promoted canonically because the current converted Markdown and the assigned chunk/source packet disagree on the controlling entry `172` row.
2. The physical source image and assigned chunk support a Pulgar/Arriagada birth-registration row for entry `172`, but the current converted Markdown still records a different Burgos/de la Cruz row for the same entry number.
3. The father field in the Pulgar/Arriagada row remains a transcription-risk point. The visible source supports a father named `Jose del Carmen Pulgar` with a possible trailing mark or abbreviation; it should not be silently normalized to or merged with another Jose candidate.
4. No Dario-line identity bridge is supported by this item. The reviewed entry does not name Dario, Arturo, Smith, a medical title, a passenger context, or a relationship bridge to Dario Arturo Pulgar-Smith or similarly named Dario candidates.
5. Canonical person pages, relationship claims, duplicate merges, and parent-child relationships should remain on hold until the converted Markdown conflict is resolved or a certified conversion-QA note is used as the controlling transcription.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225648188.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Findings

The staged identity-analysis draft is substantively supported as a hold note. It correctly treats the problem as a row-control/conversion-control conflict rather than as a same-person, duplicate-person, or ordinary name-variant problem.

The assigned chunk and source packet read physical entry `172` on register page `58` as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered `Siete de Abril de mil ochocientos ochenta i ocho`, born `Ocho de Marzo de mil ochocientos ochenta i ocho` at `tres de la tarde`, at `Calle de Valdivia`, with father `Jose del Carmen Pulgar` plus a possible suffix/mark, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.

The current converted Markdown instead reads entry `172` as `Jose Miguel`, male, born `El seis de Abril de mil ochocientos ochenta i ocho` at `diez de la noche`, father/informant `Oswaldo Burgos`, and mother `Concepcion de la Cruz`. This contradicts the assigned chunk, source packet, and visible image for the physical row. The converted Markdown should not be used as the controlling evidence for this staged Pulgar/Arriagada claim without correction or an explicit QA override.

The identity analysis is appropriately cautious about the Dario comparison. Surname/family-line relevance justifies anti-conflation review, but this entry alone supplies no literal Dario identity evidence and no relationship bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada.

## Scores

| Dimension | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration image is a strong direct source for a birth row when the row is correctly controlled. |
| conversion_confidence_score | 0.44 | Physical image/chunk support Pulgar/Arriagada, but the current converted Markdown materially conflicts. |
| evidence_quantity_score | 0.62 | One primary image plus derivative chunk/source packet; no independent corroborating source for identity bridges. |
| agreement_score | 0.48 | Image, chunk, and source packet agree against the current converted Markdown; derivative layers are not yet reconciled. |
| identity_confidence_score | 0.58 | Moderate for the physical Pulgar/Arriagada row; low for attaching it to any canonical Jose/Juana/Dario identity. |
| claim_probability | 0.78 | The claim that physical entry `172` is the Pulgar/Arriagada row is probable, but not canonically ready while the conversion conflict persists. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada family claims and to preventing Dario-line conflation. |
| relevance_confidence | 0.91 | The literal Pulgar and Arriagada names make the item highly relevant if the row is certified. |
| canonical_readiness | 0.15 | Hold for conversion QA and separate claim-level proof review before promotion. |

## Evidence Strengths

- The physical page image visibly places entry `172` on register page `58` in the Pulgar/Arriagada row, matching the assigned chunk and source packet at the broad row level.
- The source class is strong: a civil birth register can directly support child name, sex, registration date, birth date/time/place, named parents, and informant once the transcription is certified.
- The staged identity analysis correctly avoids converting this into a Dario identity bridge or a Jose/Juana merge based only on surname and local context.

## Review Decision

`hold_for_conversion_qa`.

The staged identity-analysis draft is acceptable as a conflict/hold analysis, but not as a canonical claim source. Do not promote the Pulgar/Arriagada child, birth, parent, or relationship claims until the conversion-control conflict is closed and the father field is reread to the visible extent only.

## Next Action

Run or reference targeted conversion QA that explicitly reconciles the source image, assigned chunk, source packet, and current converted Markdown for physical entry `172`. After row control is certified, create separate proof-review notes for the child identity, birth facts, father claim, mother claim, and parent-child relationships. Keep all Dario-line links and Jose/Juana identity merges out of canonical space unless later source-level bridge evidence supports them.
