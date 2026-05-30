---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530114925419
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-evidence-extraction-20260530102722394.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530102722394.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Control Conflict

This proof review covers the exact staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md`.

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The assigned chunk/source packet and the current converted Markdown give mutually incompatible readings for entry `172`.
2. The source image named by the derivatives is absent from this checkout, so this review cannot visually certify which physical row controls entry `172`.
3. The conflict is material, not orthographic: the two readings differ on child, parents, birth date/time, place, informant, and register context.
4. The father field in the Pulgar/Arriagada reading must not be normalized beyond `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar [?]` until the suffix after `Pulgar` is visible and certified.
5. No reviewed item names Dario, Arturo, Smith, a Dario spouse, a Dario descendant, or any bridge to a Dario-line identity. Do not attach this entry to any Dario candidate by surname context alone.
6. Existing canonical material, if any, cannot be strengthened from this packet because the row-control conflict blocks promotion.

## Evidence Strengths

- The underlying source type is a civil birth registration, which would normally be strong evidence for birth identity and stated parentage.
- The assigned chunk and source packet agree internally that entry `172` names `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888 at about three in the afternoon at `Calle de Valdivia`, with father transcribed as `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The current converted Markdown independently preserves a structured entry `172`, but reads it as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at ten at night at `En esta`.
- The staged identity analysis correctly treats the disagreement as a row-control conflict and recommends no promotion, no merge, and no Dario-line attachment.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.75 | Civil registration is high-quality for birth and parentage, but this pass lacks the actual page image for direct verification. |
| conversion_confidence_score | 0.35 | The converted Markdown and assigned chunk disagree on nearly every identity-controlling field. |
| evidence_quantity_score | 0.45 | There are multiple derivative witnesses, but they derive from a disputed conversion chain and no full-page image is available here. |
| agreement_score | 0.20 | Agreement is strong only within the chunk/source-packet pair; agreement between chunk and converted Markdown is very low. |
| identity_confidence_score | 0.45 | A Pulgar/Arriagada row candidate is plausible as a staged target, but identity certification is blocked by row control. Dario identity confidence is near zero. |
| claim_probability | 0.60 | Probability that the staged target is a Pulgar/Arriagada entry-172 row candidate; probability of canonical promotion now is 0.05; probability of a Dario identity bridge from this evidence is 0.02. |
| relevance_level | high | The Pulgar/Arriagada names are family-relevant if the row is certified. |
| relevance_confidence | 0.88 | Relevance is clear as a lead, but not as promotable proof. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, merges, or wiki updates before full-image row-control QA. |

## Review Finding

The staged identity analysis is supported as a hold judgment. It properly preserves the hard boundary between verification context and source transcription: it asks for row-control certification and father-field bounding, but does not claim a corrected canonical identity from the disputed derivatives.

The proof state is not ready for canonical use. The Pulgar/Arriagada reading may be the intended row, but the conflicting converted Markdown and absent original image prevent reliable promotion of birth-name, birth-event, parent-child, spouse-clue, or identity-merge claims.

## Next Action

Run targeted conversion QA against the original full-page image, assigned chunk, converted Markdown, and manifest. The QA worker should certify which physical row controls entry `172` and bound the father field if the Pulgar/Arriagada row is confirmed. After that, rerun proof review only on the narrow birth identity, birth event, parent names, and parent-child claims.
