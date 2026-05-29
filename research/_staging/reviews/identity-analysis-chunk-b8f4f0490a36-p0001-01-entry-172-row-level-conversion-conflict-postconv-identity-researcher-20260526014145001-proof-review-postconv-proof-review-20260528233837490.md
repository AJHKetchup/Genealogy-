---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260528233837490
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_page: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Conversion-control blocker: the current converted Markdown gives entry 172 as a Burgos/de la Cruz birth row, while the assigned chunk, source packet, conflict draft, and visible source image support entry 172 as a Pulgar/Arriagada birth row. Canonical claims must remain held until conversion QA certifies or repairs the controlling conversion.
- Father-field precision blocker: the visible source supports `Jose del Carmen Pulgar` as the father, but the final mark or suffix after `Pulgar` is not secure enough here to promote as `S.` without targeted conversion QA.
- Identity-bridge blocker: the source image and assigned chunk do not name Dario, Arturo, Smith, Pulgar-Smith, a spouse, a child, or a later-life identifier. The staged draft correctly blocks Dario-line comparisons from this entry alone.
- Relationship-promotion blocker: parent-child claims for Jose del Carmen Segundo Pulgar Arriagada, Jose del Carmen Pulgar, and Juana Arriagada de Pulgar are plausible from the source-visible row, but they should not be promoted while the canonical converted file contradicts the row.

## Evidence Checked

- Staged identity-analysis draft named in this task.
- Referenced conflict draft for entry 172 row control.
- Referenced source packet for the Pulgar/Arriagada row.
- Referenced assigned chunk, `CHUNK-b8f4f0490a36-P0001-01`.
- Referenced converted Markdown for the same source.
- Referenced source page image, limited to entry 172 and adjacent row context needed to verify row control.

## Evidence Strengths

- The source page image visibly places entry 172 on page 58 and supports a Pulgar/Arriagada row: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888, with parents Jose del Carmen Pulgar and Juana Arriagada de Pulgar, and compareciente Ernesto Herrera L.
- The assigned chunk and source packet are internally consistent with the visible source image for the row-level identity, date, place, mother, and informant.
- The staged draft correctly treats the Burgos/de la Cruz text as a row-level conversion conflict rather than trying to harmonize two incompatible readings.
- The staged draft correctly refuses to attach this entry to any Dario candidate without an independent identity bridge.

## Scored Judgment

| Metric | Score / Level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a primary source and the entry is mostly legible, though some handwriting details and the father suffix need closer QA. |
| conversion_confidence_score | 0.45 | The assigned chunk tracks the visible source image, but the current converted Markdown for the same source records an incompatible row. |
| evidence_quantity_score | 0.74 | Review has the image, chunk, source packet, conflict draft, and converted file; no independent identity-bridge source is present. |
| agreement_score | 0.55 | Image, chunk, source packet, and conflict draft agree on Pulgar/Arriagada; the converted file materially disagrees. |
| identity_confidence_score | 0.68 | The visible row supports the child and parent candidate cluster, but not a canonical merge or any Dario identity. |
| claim_probability | 0.90 | The staged draft's main claim, that this is a conversion conflict requiring hold and not a Dario bridge, is strongly supported. |
| relevance_level | high | Highly relevant to entry 172 Pulgar/Arriagada staging and conversion QA; low direct relevance to Dario identity. |
| relevance_confidence | 0.88 | The source-visible Pulgar/Arriagada names make the row relevant to Pulgar/Arriagada research, while the absence of Dario is clear. |
| canonical_readiness | hold | No canonical promotion should proceed until conversion QA resolves the converted-file conflict and father-field extent. |

## Claim Probability Detail

| Claim / Hypothesis | Probability | Review judgment |
| --- | ---: | --- |
| Entry 172 on the source image is the Pulgar/Arriagada row described by the assigned chunk. | 0.88 | Supported by visible source and chunk. |
| The current converted Markdown's Burgos/de la Cruz row controls this source image's entry 172. | 0.04 | Not supported by the inspected image; appears to be a conversion-row or source mismatch. |
| Father should be promoted exactly as `Jose del Carmen Pulgar S.`. | 0.58 | Plausible from chunk and source packet, but the suffix needs targeted visual QA before canonical use. |
| Entry 172 proves a Dario-line identity or relationship. | 0.02 | Not supported; the entry does not name or identify Dario. |
| The staged draft should remain held from canonical promotion. | 0.95 | Directly supported by the unresolved conversion contradiction. |

## Next Action

Run targeted conversion QA on the referenced source image, assigned chunk, and converted Markdown to certify entry 172's controlling row and the exact father-field extent. After QA, rerun proof review only on the certified row-level claims before promoting any child identity, parent-child relationship, parent identity, name variant, or Pulgar/Arriagada family-context claim. Keep Dario-line linkage in a separate identity-bridge review unless a source explicitly names or connects Dario.
