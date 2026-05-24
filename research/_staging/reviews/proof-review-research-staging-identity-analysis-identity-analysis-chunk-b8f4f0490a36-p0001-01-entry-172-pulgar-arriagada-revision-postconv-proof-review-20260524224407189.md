---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260524224407189
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524212140194.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524212140194.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524212140194.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk_checked: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers First

- Hold for conversion QA. The assigned converted Markdown and the assigned chunk materially disagree about entry 172, so this identity analysis should not be used as canonical identity or relationship evidence until the conversion layer is reconciled.
- The staged draft's specific description of the converted Markdown conflict needs revision. The staged draft says the converted Markdown gives `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 in `En esta`; the current converted file instead gives entry 172 as `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born 20 February 1888 in `En Pellin`. The broader conflict remains real, but those exact conflict details are not supported by the current referenced converted file.
- The father-name suffix remains unresolved. The chunk reads `Jose del Carmen Pulgar S.`, while the source image supports `Jose del Carmen Pulgar` with a possible final mark or suffix that is not safe to normalize from this review pass.
- No Dario identity is named in the source image, chunk, source packet, or converted file. The staged warning not to attach this entry to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario Pulgar Arriagada, or a Dario passenger candidate is well founded.

## Evidence Strengths

- The source type is strong: a civil birth register image for Los Angeles/La Laja, 1888, with page 58 and entry 172 visible.
- The source image visibly supports the broad Pulgar/Arriagada row described by the assigned chunk: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`, and Calle de Valdivia/Calle de Colipi context.
- The assigned chunk and source packet agree on the controlling Pulgar/Arriagada identity cluster and on the need to hold for conversion QA.
- The staged draft correctly treats this as anti-conflation evidence rather than proof of a Dario identity or a basis for a surname-only merge.

## Scored Judgment

| Item | source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| Overall staged identity analysis as a hold/QA warning | 0.86 | 0.34 | 0.70 | 0.56 | 0.66 | 0.78 | high | 0.94 | hold_for_conversion_qa |
| Pulgar/Arriagada child-parent identity cluster | 0.86 | 0.36 | 0.72 | 0.62 | 0.72 | 0.74 | high | 0.95 | hold_for_conversion_qa |
| Exact father suffix after `Pulgar` | 0.82 | 0.28 | 0.42 | 0.34 | 0.40 | 0.38 | high | 0.88 | hold_for_conversion_qa |
| Draft's exact converted-conflict description | 0.80 | 0.20 | 0.32 | 0.18 | 0.20 | 0.18 | high | 0.90 | revise |
| No-Dario / anti-conflation warning | 0.86 | 0.58 | 0.68 | 0.74 | 0.84 | 0.90 | high | 0.96 | ready_as_warning_only |

## Review Notes

Literal support is mixed by evidence layer. The source image and assigned chunk support the Pulgar/Arriagada identity cluster at entry 172, while the converted Markdown currently assigns entry 172 to a different family. This makes the staged draft useful as a conversion-QA and anti-conflation warning, not as canonical proof.

The claim confidence is moderate for the broad Pulgar/Arriagada row because the visible source and chunk agree on the main identities. It is low for the exact father suffix and low for the staged draft's exact wording about the converted-file conflict. Relationship jumps are controlled: the draft does not infer a Dario connection and explicitly blocks surname-only attachment.

## Next Action

Keep this staged draft and dependent identity, claim, relationship, and parent-candidate work at `hold_for_conversion_qa`. Revise the draft or QA note to describe the current converted Markdown conflict accurately, then complete targeted conversion QA on entry 172, including the father-name suffix after `Pulgar`. After the conversion layer is reconciled, rerun proof review before any canonical promotion.
