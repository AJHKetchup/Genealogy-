---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528045246425
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525210755405.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525210755405.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote child, birth, parent, relationship, or identity-bridge claims from the staged draft. The assigned converted Markdown and the assigned chunk give incompatible families for entry 172.
2. The assigned chunk and source packet support entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the converted Markdown instead gives `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.
3. This is a row-level conversion or file-assignment conflict, not a normal name variant. The child names, parent names, birth dates, places/residences, informant, and page context do not reconcile into one family cluster.
4. The father field in the Pulgar/Arriagada row remains uncertain at the suffix level. The reviewed materials justify asking whether the visible reading is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`; they do not justify silently normalizing it.
5. The entry does not name Dario, Arturo, Smith, a descendant, spouse, or any bridge to the Dario Pulgar identity cluster. No Dario-related identity or relationship claim is supported by this source alone.

## Evidence Strengths

- The staged identity analysis accurately preserves the conflict instead of promoting either family cluster.
- The source packet, conflict draft, and chunk agree on the Pulgar/Arriagada reading for page 58, entry 172.
- Visual review of the referenced source image supports the Pulgar/Arriagada row as the visible entry 172 on page 58, while also leaving the father's trailing suffix or mark insufficiently certain for automatic normalization.
- Civil birth registration is a strong source type for a narrow birth/parent claim after conversion QA. If the Pulgar/Arriagada row is certified, it would be direct evidence for the named child, birth event, and stated parents.
- The staged draft correctly rejects treating `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` as same-person/name-variant readings.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the civil birth register image as a source type; 6/10 for current usable proof because the controlling conversion is conflicted |
| conversion_confidence_score | 3/10 overall; 7/10 that the visible source image and chunk support the Pulgar/Arriagada row, but 2/10 that the assigned converted Markdown is reliable for entry 172 |
| evidence_quantity_score | 4/10; one direct register image plus derivative chunk/source-packet review, with no independent corroborating record checked in this task |
| agreement_score | 5/10 overall; high agreement among chunk, packet, conflict draft, and visible image for the Pulgar/Arriagada row, but material disagreement with the assigned converted Markdown |
| identity_confidence_score | 7/10 for a distinct entry-172 Pulgar/Arriagada child if row QA certifies it; 3/10 for the Burgos/de la Cruz reading as controlling this source; 1/10 for any same-person merge between the two rows; 1/10 for Dario-line identity linkage |
| claim_probability | 0.78 that the source image/chunk row is Pulgar/Arriagada; 0.24 that the converted Markdown's Burgos/de la Cruz row controls this assigned source; 0.03 that both rows are variants of one identity; 0.05 or lower for Dario identity/relationship claims |
| relevance_level | high for the staged row-level conflict and possible Pulgar/Arriagada birth/parent claims; low for Dario-line claims |
| relevance_confidence | 0.95 for the conflict review; 0.20 for Dario identity relevance |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a hold. Its main conclusion is sound: the reviewable local evidence points toward a Pulgar/Arriagada entry on the visible source image, but the assigned converted Markdown contradicts it with a different child and parent set. Because this conflict is in the controlling transcription layer, no canonical claim should be strengthened from the staged draft until targeted conversion QA reconciles the image, chunk, source packet, and converted file.

The proof risk is not only a spelling uncertainty. It is a family-cluster conflict. Promoting either row without QA would risk assigning the wrong child and parents to entry 172.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`. The QA note should identify which row controls entry 172 and separately certify the father's name field, including whether the trailing mark after `Pulgar` is an `S.`, an uncertain abbreviation, or not part of the name. After that, rerun proof review for any child, birth, parent, identity, or relationship claim before promotion.
