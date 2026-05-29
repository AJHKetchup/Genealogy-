---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260529000036251
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_page: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical blocker: the staged draft is correct to hold. The current converted Markdown and the assigned chunk/source packet disagree on the controlling row for entry 172, affecting the child, parents, birth date, birth time, place, and informant.
- Conversion-artifact blocker: the source image visible for entry 172 aligns with the Pulgar/Arriagada row described in the chunk and source packet, while the converted Markdown records a different Burgos/de la Cruz row. The converted file therefore cannot be treated as clean support for canonical claims until targeted conversion QA updates or supersedes the artifact conflict.
- Father-field blocker: the visible source supports a Jose del Carmen Pulgar father reading, but the final extent of the suffix/mark after Pulgar remains a conversion-QA question. Do not normalize it beyond the visible support.
- Identity-bridge blocker: entry 172 does not name Dario, Arturo, Smith, Pulgar-Smith, a spouse, a child of Dario, or a passenger-list identity. It is not evidence for a Dario identity merge or Dario relationship claim by itself.
- Relationship blocker: parent-child claims for Jose del Carmen Segundo Pulgar Arriagada with Jose del Carmen Pulgar and Juana Arriagada de Pulgar should remain staged/held until row-control QA is complete.

## Evidence Reviewed

- Assigned staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md`.
- Conflict candidate: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Verification Findings

The staged draft's main judgment is supported: this is a row-level conversion conflict that should remain on hold. The chunk and source packet consistently identify entry 172 as a Pulgar/Arriagada birth registration for Jose del Carmen Segundo Pulgar Arriagada, with parents Jose del Carmen Pulgar and Juana Arriagada de Pulgar, and informant Ernesto Herrera. The page image visibly supports that row family and does not visibly support the Burgos/de la Cruz row for entry 172.

The converted Markdown is materially inconsistent. It assigns entry 172 to Jose Miguel, son of Oswaldo Burgos and Concepcion de la Cruz, with different birth facts and informant. Because the converted Markdown remains an active referenced artifact, the review should not promote any claim even though the visible image favors the chunk/source-packet reading.

The staged draft appropriately separates source transcription from identity interpretation. Its Dario-line cautions are supported: no reviewed entry-172 evidence names or directly identifies any Dario candidate.

## Scores

| Metric | Score / Level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a direct original-style record for the event, but the review used an image view rather than a full fresh conversion. |
| conversion_confidence_score | 0.45 | The chunk/source packet and image align, but the converted Markdown conflicts at row level. |
| evidence_quantity_score | 0.62 | There is one direct source image plus two consistent staging derivatives; still only one underlying record. |
| agreement_score | 0.55 | Chunk, source packet, conflict candidate, and image agree with each other; converted Markdown materially disagrees. |
| identity_confidence_score | 0.58 | Confidence is moderate for the Pulgar/Arriagada row identity as visible in the source, but not ready for canonical attachment because artifact control is unresolved. |
| claim_probability | 0.72 | The staged draft's claim that this is a hold-level row-control conflict is more likely than not and visibly supported. |
| relevance_level | high | Highly relevant to entry-172 Pulgar/Arriagada staging and conversion QA; weak for Dario-line identity claims. |
| relevance_confidence | 0.88 | Relevance is clear because the staged draft, packet, chunk, converted file, and image all concern the same entry number and row conflict. |
| canonical_readiness | hold | No canonical claim, relationship, merge, or name variant should be promoted from this item yet. |

## Evidence Strengths

- The staged draft correctly identifies the controlling issue as row-level, not merely a spelling or name-variant issue.
- The chunk and source packet provide internally consistent Pulgar/Arriagada details for entry 172.
- The page image supports the existence of the Pulgar/Arriagada row in entry 172 strongly enough to justify targeted conversion QA.
- The draft avoids an unsupported jump from a Pulgar/Arriagada birth row to Dario-line identities.

## Next Action

Keep the staged draft on hold and send the source image, chunk, and converted Markdown to targeted conversion QA. The QA scope should be limited to entry 172 row control and the visible extent of the father name after `Jose del Carmen Pulgar`. After that, rerun proof review on the specific child, birth, parent, residence, and informant claims before any canonical update.
