---
type: proof_review
status: hold
role: claim_reviewer
worker: "postconv-proof-review-20260527201707382"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Row Conflict

## Blockers

1. The expected original source image is not present at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, and the expected job page image `page-images/page-0001.png` is also absent. This review cannot independently certify the visible source row.
2. The assigned chunk and the current converted Markdown give incompatible readings for entry `172`. The chunk/source packet read a Pulgar/Arriagada birth row; the converted Markdown reads a Burgos/de la Cruz birth row.
3. The father-field suffix remains unresolved. The assigned chunk has `Jose del Carmen Pulgar S.`, while the reviewed row-control note only certifies the father as `Jose del Carmen Pulgar` and leaves a terminal mark or suffix uncertified.
4. The staged identity analysis correctly rejects a Dario-line attachment from this entry. No reviewed source in this assignment names Dario, Dario Arturo, or Jose Dario in entry `172`.
5. Canonical promotion is blocked because row control and derivative reconciliation are not settled in the current converted file.

## Evidence Strengths

- The staged draft accurately identifies the central conflict: the chunk/source packet and converted Markdown cannot both describe the same physical entry `172`.
- The assigned chunk and source packet are internally consistent for the Pulgar/Arriagada reading: child `Jose del Carmen Segundo Pulgar Arriagada`, father beginning `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, birth on 8 March 1888, registration on 7 April 1888.
- The converted Markdown is internally consistent for a different Burgos/de la Cruz reading: child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth on 6 April 1888.
- A referenced row-control QA note reports image-level certification in favor of the Pulgar/Arriagada row, but this review treats that as staged QA context rather than direct visual verification because the image is unavailable here.
- The staged draft keeps the Dario question separated from literal transcription and does not attempt to rename or merge people from surname context alone.

## Scores

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil birth registration would be strong primary evidence if the source image were available; in this checkout the review relies on derivative files and staged QA notes. |
| conversion_confidence_score | 0.34 | The derivative conversion chain is materially conflicted, and the controlling image cannot be rechecked in this pass. |
| evidence_quantity_score | 0.52 | There is one target source chain plus a QA note; quantity is enough to identify the conflict but not enough to promote. |
| agreement_score | 0.30 | Chunk/source packet and current converted Markdown disagree on child, parents, birth date, place wording, informant, and page context. |
| identity_confidence_score | 0.62 | Moderate confidence that the Pulgar/Arriagada row is the relevant held hypothesis, but low confidence for any broader identity merge or Dario bridge. |
| claim_probability | 0.80 | High probability that the correct disposition is `hold_for_conversion_qa`; lower probability for any promotable person/relationship claim. |
| relevance_level | high | The evidence is directly relevant to entry-172 row control and Pulgar/Arriagada parent-child candidates. |
| relevance_confidence | 0.90 | The staged draft, source packet, chunk, converted file, and QA note all concern this same entry-number conflict. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, identity merges, names, or canonical page edits from this draft. |

## Claim Probability

The staged draft's main claim is well supported: entry `172` must remain held because derivative transcripts conflict and the physical source image is unavailable in this checkout. Probability for that hold judgment is `0.80`.

The Pulgar/Arriagada row is the stronger working hypothesis than the Burgos/de la Cruz row because the assigned chunk, source packet, and row-control QA note align on it. However, promotion probability remains below threshold because the current converted Markdown still conflicts and this reviewer cannot inspect the image.

The probability that this entry supports a Dario-line same-person or relationship bridge is very low, estimated at `0.05`, because no reviewed entry-172 material names Dario or provides a direct identity bridge.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. The next action is targeted conversion-control reconciliation: restore or locate the source image matching SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, compare it against both the assigned chunk and current converted Markdown, and certify the physical row plus father-field boundary. After that, rerun proof review before any canonical claim, relationship, or identity update.

No raw source, converted Markdown, chunk, source packet, canonical page, claim, or relationship file was edited in this review.
