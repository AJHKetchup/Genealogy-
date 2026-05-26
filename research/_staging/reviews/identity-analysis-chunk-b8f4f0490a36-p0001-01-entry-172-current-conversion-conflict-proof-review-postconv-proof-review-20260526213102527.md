---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260526213102527
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173036167.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173036167.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
created: 2026-05-26
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- The claim set is not canonically ready because the referenced converted Markdown and the referenced chunk do not describe the same entry 172 row.
- The page image and assigned chunk support a Pulgar/Arriagada entry 172 row, while the converted Markdown currently says entry 172 is a Burgos/de la Cruz row. This is a material row-control conflict, not a name variant.
- The father field is not exact-name certified. The visible row supports at least `Jose del Carmen Pulgar`; the trailing letter or mark after `Pulgar` needs targeted conversion QA before being normalized as `S.` or omitted.
- No Dario identity or Dario relationship is named in this entry. Any attachment to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario Pulgar Arriagada, or passenger-list Dario candidates would be unsupported by this source.
- This review does not promote any claim, relationship, identity merge, or wiki change.

## Evidence Strengths

- The source is an original civil birth-register page image for Los Angeles, Chile, 1888, which is a strong source type for birth registration facts when the row is correctly controlled.
- Direct image inspection agrees with the assigned chunk and source packet that entry 172 on page 58 names `Jose del Carmen Segundo Pulgar Arriagada`, male; born 8 March 1888 at about 3 p.m. at Calle de Valdivia; with father `Jose del Carmen Pulgar` plus an unresolved trailing mark; mother `Juana Arriagada de Pulgar`; and compareciente `Ernesto Herrera L.` present at the birth.
- The staged identity-analysis draft correctly treats the Burgos/de la Cruz reading as a conversion conflict and not as a same-person or duplicate-person problem.
- The draft preserves uncertainty around the father suffix and correctly blocks downstream identity merges involving the Jose/Juana entry-513 candidates and the Dario-line candidates.

## Literal Support Check

| item | support judgment | notes |
| --- | --- | --- |
| Pulgar/Arriagada child row | supported by image, chunk, and source packet | The visible row numbered 172 on page 58 matches the chunk/source-packet reading, not the current converted Markdown reading. |
| Birth date, time, and place | supported with ordinary transcription uncertainty | The image/chunk support 8 March 1888, about 3 p.m., Calle de Valdivia. |
| Father claim | partially supported | `Jose del Carmen Pulgar` is supported; the trailing `S.` or mark is not certified enough for normalization. |
| Mother claim | supported | `Juana Arriagada de Pulgar` is supported by the visible row and chunk. |
| Informant fact | supported | `Ernesto Herrera L.` and presence at birth are supported by image/chunk. |
| Burgos/de la Cruz converted-row claim | unsupported for this visible page image | It is present in the current converted Markdown, but conflicts with the referenced source image and chunk. |
| Same-person/merge claims | not supported | This source alone does not bridge entry 172 persons to entry 513 persons or Dario-line candidates. |

## Scores

| score | value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Original civil registration image is high-quality evidence for birth facts once row control is resolved. |
| conversion_confidence_score | 0.35 | The assigned chunk matches the image, but the controlling converted Markdown conflicts materially with both. |
| evidence_quantity_score | 0.50 | One source image with derivative chunk and source packet; no independent corroborating record. |
| agreement_score | 0.42 | Image, chunk, and source packet agree, but converted Markdown disagrees at the entire-row level. |
| identity_confidence_score | 0.68 | Probable source-local identity for the Pulgar/Arriagada child if this row controls; not enough for broader merges. |
| claim_probability | 0.64 | Pulgar-row claims are more probable than the converted Markdown reading for the visible image, but the conversion conflict caps confidence. |
| relevance_level | high | Pulgar and Arriagada are family-relevant terms and this row concerns a likely relevant birth-registration cluster. |
| relevance_confidence | 0.88 | Relevance is high if the Pulgar/Arriagada row controls; relevance does not justify promotion through a conversion conflict. |
| canonical_readiness | 0.08 | Hold for targeted conversion QA, then rerun proof review before any canonical update. |

## Review Decision

Canonical readiness is `hold_for_conversion_qa`.

The identity-analysis draft is appropriately conservative and should remain held. Its major conclusions are supported: the conflict is row-level conversion/source-control instability; the Pulgar/Arriagada evidence is plausible and image-supported; the current converted Markdown is incompatible with the image/chunk; and no Dario-line attachment or Jose/Juana merge is justified from this source.

## Next Action

Run targeted conversion QA against the page image, current converted Markdown, assigned chunk, and source packet for page 58 entry 172. Certify which row controls entry 172 and preserve the father field only to the visible extent. After QA, rerun proof review for the child birth claim, parent-child claims, informant fact, and any proposed identity bridges.
