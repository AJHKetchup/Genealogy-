---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527031004460
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527000641674.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527000641674.md"
reviewed_claim_type: identity_conflict_analysis
reviewed_subject: "Entry 172 birth registration row control"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
source_page_image_checked: "yes; page 58 entry 172 visually checked in cited PNG"
source_quality_score: 0.90
conversion_confidence_score: 0.72
evidence_quantity_score: 0.68
agreement_score: 0.70
identity_confidence_score: 0.86
claim_probability: 0.84
relevance_level: high
relevance_confidence: 0.95
canonical_readiness: hold_for_conversion_control
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- Canonical readiness is `hold_for_conversion_control`. The cited source image and assigned chunk support the Pulgar/Arriagada row for physical entry `172`, but the current converted Markdown for the same source identity still records entry `172` as a different Burgos/de la Cruz birth. This conflict must remain explicit until conversion control fixes or supersedes the stale converted file.
- The father field is not ready for a suffix-bearing canonical name. The assigned chunk reads `Jose del Carmen Pulgar S.`, while the targeted QA note certifies only `Jose del Carmen Pulgar`; visual review does not make the terminal mark clear enough to promote as a definite `S.`.
- No reviewed material supports a Dario-line attachment. Entry `172` names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or any equivalent Dario identity.
- The reviewed entry does not prove that `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are the same person. Any such merge or normalization needs separate image-level identity work.

## Evidence Strengths

- The original civil birth register image is a contemporary official record and visibly places entry `172` on page 58 in the Pulgar/Arriagada row.
- The assigned chunk, source packet, targeted conversion QA note, and conflict draft agree that the physical row for entry `172` names child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, birth date `Ocho de Marzo de mil ochocientos ochenta i ocho`, birth time `a las tres de la tarde`, and place `Calle de Valdivia`.
- The same materials agree on parents bounded as father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`, with the father suffix question preserved rather than silently normalized.
- The staged identity analysis correctly treats the Burgos/de la Cruz text as a row-level conversion mismatch, not as a name variant or competing identity for the Pulgar child.

## Scored Judgment

- `source_quality_score: 0.90` - the controlling source is an official civil birth register image, contemporary to the event and directly relevant.
- `conversion_confidence_score: 0.72` - the image-reviewed chunk and QA note are persuasive for the Pulgar/Arriagada row, but confidence is reduced by the materially contradictory converted Markdown and unresolved father suffix.
- `evidence_quantity_score: 0.68` - one original image plus several staged derivative reviews support the same row-control judgment; the derivatives are useful but not independent sources.
- `agreement_score: 0.70` - source image, chunk, source packet, conflict note, and targeted QA align on row control, while the current converted Markdown materially disagrees.
- `identity_confidence_score: 0.86` - high confidence that physical entry `172` is for `Jose del Carmen Segundo Pulgar Arriagada`; lower confidence for any broader identity merge or father suffix expansion.
- `claim_probability: 0.84` - the row-control claim is probable and visually supported, but canonical action should wait for conversion-control handling of the stale transcript conflict.
- `relevance_level: high`; `relevance_confidence: 0.95` - the entry is directly relevant to Pulgar/Arriagada birth and parent evidence and also relevant as anti-conflation evidence against Dario-line shortcuts.
- `canonical_readiness: hold_for_conversion_control`.

## Next Action

Accept the narrow proof-review judgment that the controlling physical entry `172` is the Pulgar/Arriagada row, while keeping the item out of canonical folders until conversion control resolves or clearly supersedes the stale Burgos/de la Cruz converted Markdown. Any later canonical claim should use father `Jose del Carmen Pulgar` only, preserve the possible suffix as unresolved, and avoid Dario-line or Juana-variant merges without separate proof.
