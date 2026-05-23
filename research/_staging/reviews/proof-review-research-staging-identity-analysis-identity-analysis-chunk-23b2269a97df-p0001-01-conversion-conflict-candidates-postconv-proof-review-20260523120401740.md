---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-23b2269a97df-p0001-01-conversion-conflict-candidates.md
worker: postconv-proof-review-20260523120401740
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-23b2269a97df-p0001-01-conversion-conflict-candidates.md
reviewed_source_packet: research/_staging/source-packets/chunk-23b2269a97df-p0001-01-entry-172-pulgar-arriagada.md
reviewed_converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
reviewed_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
review_status: hold
canonical_readiness: hold
---

# Proof Review: Entry 172 Identity Conflict

## Blockers

- Canonical readiness is `hold`. The staged identity analysis is directionally right that this entry has a critical same-source conversion conflict, but it is not ready for canonical promotion because the controlling transcript has not been reconciled in the converted file or chunk.
- The source image for register page 58, entry 172 visibly supports the Pulgar/Arriagada row: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registration date 7 April 1888, birth on 8 March 1888 at about 3 p.m., birthplace `Calle de Valdivia`, father appearing as `Jose del Carmen Pulgar`, and mother appearing as `Juana Arriagada de Pulgar`.
- The referenced converted Markdown and chunk do not support those Pulgar/Arriagada facts. They currently transcribe entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, birth on 26 March 1888 at 10 p.m., and informant `Oswaldo Gomez`.
- The staged draft's description of the derivative conflict is internally stale or mismatched: it says the converted/chunk text gives `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`. That is not what the currently referenced converted file and chunk say. This does not rescue the derivative transcript; it adds another reason to hold until conversion QA records the exact competing readings.
- The father's exact full name remains uncertain at detail level. The visible source appears consistent with `Jose del Carmen Pulgar`, but suffixes, residence/occupation details, and informant details should stay out of canonical claims until targeted QA records the source-visible forms.
- The entry does not name Dario. There is no current basis to attach this entry to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada.

## Evidence Strengths

- The underlying source is a civil birth registration image for Los Angeles, Chile, page 58, entry 172. As a source type, it is strong evidence for the child's registered name, sex, registration date, birth date/time/place, and stated parents once the transcript is reconciled.
- The source packet correctly flags `conversion_confidence: mixed` and `promotion_recommendation: hold_for_conversion_qa`.
- The page image directly explains why the derivative converted/chunk transcript is unreliable for this entry: entry 172 in the image is a Pulgar/Arriagada registration, not the Gomez/de la Cruz row now in the derivative transcript.
- The staged draft's conservative recommendation not to promote identity or relationship claims is well supported.

## Scored Judgment

| category | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong primary source for the event and stated relationships. |
| conversion_confidence_score | 0.22 | Low for the assigned converted file/chunk because they contradict the visible source image for entry 172. |
| evidence_quantity_score | 0.62 | One direct source image plus a source packet and conflicted derivative artifacts; enough to identify the conflict, not enough to promote. |
| agreement_score | 0.18 | Source image/source packet and converted/chunk materially disagree on child, parents, birth details, and informant. |
| identity_confidence_score | 0.78 | The visible entry supports the Pulgar/Arriagada identity cluster, reduced because the canonical transcript layer is unreconciled. |
| claim_probability | 0.80 | Probable that entry 172 is the Pulgar/Arriagada birth registration, but this should remain a held probability pending conversion QA. |
| relevance_level | 0.96 | Directly relevant to Pulgar/Arriagada identity and parent-child evidence; also important as a false-merge guardrail. |
| relevance_confidence | 0.94 | The source packet, staged draft, and visible image all concern the same source path and entry number. |
| canonical_readiness | 0.05 | Hold. Do not promote claims, relationships, or wiki updates from this draft until conversion QA resolves the transcript conflict. |

## Review Decision

Hold the staged identity analysis for conversion QA. The most probable identity reading is the image-visible Pulgar/Arriagada registration, but the referenced converted file and chunk are materially wrong or assigned to the wrong row for entry 172. The staged draft should not be promoted as a canonical proof note because it also misstates the current derivative reading as Burgos/de la Cruz rather than the currently referenced Gomez/de la Cruz transcript.

## Next Action

Run targeted conversion QA for `CHUNK-23b2269a97df-P0001-01` / the current chunk file against the source image. The QA note should:

- record the image-visible entry 172 transcript as the controlling reading or explicitly explain why it is not controlling;
- retire, correct, or reassign the derivative `Jose Francisco` / `Oswaldo Gomez` / `Emilia de la Cruz` row currently attached to entry 172;
- reconcile the staged draft's stale `Jose Miguel` / `Oswaldo Burgos` / `Concepcion de la Cruz` conflict wording with the current converted/chunk text;
- keep Dario-line identities out of this entry unless a later source provides direct identity-bridging evidence.
