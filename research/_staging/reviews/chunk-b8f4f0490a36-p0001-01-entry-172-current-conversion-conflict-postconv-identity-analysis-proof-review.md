---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526195646250
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526174903677.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526174903677.md
reviewed_subject: "Entry 172, Los Angeles birth register, 1888"
reviewed_claim_type: identity_conflict_analysis
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
source_page_image_checked: true
source_quality_score: 0.86
conversion_confidence_score: 0.42
evidence_quantity_score: 0.70
agreement_score: 0.48
identity_confidence_score: 0.68
claim_probability: 0.94
relevance_level: high
relevance_confidence: 0.97
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The staged identity analysis correctly identifies a material row-level conflict: the assigned chunk and staged source packet give entry `172` as a Pulgar/Arriagada birth-registration row, while the current converted Markdown gives entry `172` as a Burgos/de la Cruz row.
- The conflict affects the whole row, not only a name spelling: child, birth date, birth time, birthplace, father, mother, informant, residence context, and relationship candidates all differ between the chunk/source-packet reading and the current converted Markdown.
- The father field in the Pulgar/Arriagada row remains unresolved at the trailing element. The chunk reads `Jose del Carmen Pulgar S.`, while the source packet appropriately limits the image-supported reading to `Jose del Carmen Pulgar` plus an uncertified trailing letter or mark.
- No canonical claim, relationship, merge, or wiki update should be made from this draft until targeted conversion QA certifies which physical row controls entry `172` and explains why the current converted Markdown diverges from the assigned chunk and visible source image.
- The staged draft's Dario-comparison section is useful as an identity-risk guardrail, but this proof review did not inspect the referenced canonical Dario/Pulgar wiki pages because the row-level conversion conflict was already sufficient to block promotion. Those comparison notes should not be treated as independently revalidated by this review.

## Evidence Strengths

- The referenced source image was available and visually checked. At the review level, entry `172` on page 58 is consistent with the assigned chunk and staged source packet's Pulgar/Arriagada row, not with the Burgos/de la Cruz row in the current converted Markdown.
- The assigned chunk directly transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at about 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The staged source packet repeats the same Pulgar/Arriagada reading and explicitly preserves the conversion QA concern rather than promoting dependent claims.
- The current converted Markdown directly supports the existence of the opposing Burgos/de la Cruz reading under entry `172`: child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`, with `Oswaldo Burgos` as informant.
- The staged identity analysis accurately treats the Burgos/de la Cruz and Pulgar/Arriagada readings as incompatible row candidates, not same-person variants or relationship evidence.

## Scored Judgment

- `source_quality_score: 0.86` - civil birth registration is a strong primary source class, and the referenced image is available; reduced because this review is focused on conversion conflict resolution rather than a full paleographic certification of every field.
- `conversion_confidence_score: 0.42` - the assigned chunk and visible image agree directionally, but the current converted Markdown materially disagrees with them for the same entry number.
- `evidence_quantity_score: 0.70` - one source image plus three local derivative files were reviewed; enough to confirm the conflict, not enough to certify all final row readings.
- `agreement_score: 0.48` - chunk, source packet, and image agree on the Pulgar/Arriagada row, but the current converted Markdown conflicts across the row.
- `identity_confidence_score: 0.68` - the Pulgar/Arriagada row is the stronger local hypothesis for entry `172`, but identity confidence remains below canonical level until conversion QA resolves the row-control problem and father-field uncertainty.
- `claim_probability: 0.94` - the claim that there is a material conversion conflict for entry `172` is very probable.
- `relevance_level: high`; `relevance_confidence: 0.97` - the conflict is directly relevant to Pulgar/Arriagada identity and relationship work because it controls whether any dependent birth or parent-child claims can be trusted.
- `canonical_readiness: hold_for_conversion_qa`.

## Review Judgment

The staged identity analysis is supported as a conflict-analysis note and should remain held. It is not ready for canonical promotion because the current converted Markdown, assigned chunk, source packet, and visible source image have not been reconciled into one certified row-level transcription.

The safest claim from the present evidence is procedural: entry `172` requires targeted conversion QA. The Pulgar/Arriagada reading appears stronger in the reviewed local evidence, but the final father-field reading and the cause of the Burgos/de la Cruz converted-file mismatch remain unresolved.

## Next Action

Run targeted conversion QA against the original image, assigned chunk, current converted Markdown, and staged source packet. Certify which physical row controls entry `172`; resolve whether the father field should be recorded as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`; and determine whether the current converted Markdown is row-shifted, stale, or sourced from a different image/page. Rerun proof review before any canonical claim, relationship, merge, or wiki update.
