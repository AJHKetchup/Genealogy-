---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525150350561
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121047961.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121047961.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Pulgar/Arriagada Conversion Conflict

## Blockers First

1. Canonical promotion is blocked by a material derivative-transcript conflict. The reviewed chunk and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`; the reviewed converted Markdown instead identifies entry 172 as `José Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`.
2. The identity-analysis draft preserves an older conflict summary naming `Jose Francisco`, `Oswaldo Gomez`, and `Emilia de la Cruz`. The current converted file does not match that exact summary, but it still conflicts with the Pulgar/Arriagada chunk across child, parents, birth date, place, informant, and register context.
3. The exact father-name ending after `Jose del Carmen Pulgar` remains a controlled uncertainty. The source image and chunk support a visible final mark/initial after Pulgar at review level, but this proof review should not promote a normalized father identity until targeted conversion QA certifies `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. The staged analysis correctly warns against using this entry as a Dario-line bridge. This source does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, Alexander John Heinz, or a Smith relationship.

## Evidence Strengths

- The source image, chunk, and source packet are aligned for the page 58, entry 172 Pulgar/Arriagada reading: registration date 7 April 1888; child `Jose del Carmen Segundo Pulgar Arriagada`; male; birth 8 March 1888 at 3 p.m.; birth place Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; parent residence Calle de Colipi/Colipí; informant `Ernesto Herrera L.`
- The source type is a civil birth register, so the source quality is strong for birth facts and declared parent names if the row assignment is settled.
- The conflict itself is well supported. The converted Markdown transcribes a different register state for entries 171-176 and cannot be reconciled with the visible Pulgar/Arriagada row as a spelling variant.
- The staged identity analysis keeps literal readings separate from interpretation and assigns hold status rather than promoting dependent identities or relationships.

## Scored Judgment

| Metric | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth registration image is a strong source for birth and parent declarations; image quality is usable though small handwriting limits exact-suffix certainty. |
| conversion_confidence_score | 0.44 | The chunk/source packet align with the visible source image, but the assigned converted Markdown conflicts materially with them. |
| evidence_quantity_score | 0.62 | One source image plus chunk and source packet support the Pulgar/Arriagada reading; no independent corroborating record was reviewed for identity bridging. |
| agreement_score | 0.48 | Agreement is high between image/chunk/source packet, but low across all derivative files because the converted Markdown records a different row family. |
| identity_confidence_score | 0.63 | Moderate confidence that the reviewed row concerns the Pulgar/Arriagada child and parents; not enough for parent-stub merge or Dario-line attachment. |
| claim_probability | 0.68 | The Pulgar/Arriagada entry-172 claim is probable from the visible page and chunk, but held below promotion level due to conversion-file conflict and father-suffix uncertainty. |
| relevance_level | high | The entry is highly relevant to Pulgar/Arriagada family research if QA confirms the row, but only low direct relevance to Dario identity questions. |
| relevance_confidence | 0.82 | Pulgar and Arriagada names are visible/local and family-relevant; no direct Dario bridge is present. |
| canonical_readiness | hold | Do not promote claims, relationships, merges, or canonical page edits until targeted conversion QA resolves the file conflict and father field. |

## Claim Probability Notes

- Birth claim for `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888 at 3 p.m. at Calle de Valdivia: probability 0.70, hold for conversion QA.
- Parent claim naming father as `Jose del Carmen Pulgar S.`: probability 0.64, hold for exact suffix certification.
- Parent claim naming mother as `Juana Arriagada de Pulgar`: probability 0.72, hold because it depends on the same row-level conversion conflict.
- Same-person or lineage bridge from this entry to any Dario Pulgar identity: probability 0.06, not supported for promotion.

## Next Action

Run targeted conversion QA against the source image, converted Markdown, chunk, and source packet. The QA note should explicitly decide whether the authoritative entry 172 for this source packet is the Pulgar/Arriagada row or the Bunster/de la Maza row now present in the converted Markdown, and should certify the father field without normalizing beyond the visible source. After that, rerun proof review for the child birth facts and child-parent relationships before any canonical use.
