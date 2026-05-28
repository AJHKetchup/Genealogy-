---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528202527922
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173924316.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173924316.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528165422297.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528165422297.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote the current converted Markdown's entry `172` reading. It gives `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`, but the source image and assigned chunk support a different physical row for entry `172`.
2. Do not promote a father-name suffix after `Jose del Carmen Pulgar`. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the targeted row-control review certifies only `Jose del Carmen Pulgar`; visual review here does not safely certify the trailing mark.
3. Do not attach this row to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. The source row does not name Dario, Arturo, Smith, a later spouse, a child, or a bridge identifier.
4. Do not merge `Burgos/de la Cruz` into the Pulgar/Arriagada family as a name variant or duplicate person. The conflict is derivative conversion content, not a supported source variant.

## Evidence Strengths

- The original page image visibly places entry `172` on register page 58 as the middle row, with child name `Jose del Carmen Segundo Pulgar Arriagada`, sex male, registration date 7 April 1888, and birth date 8 March 1888.
- The assigned chunk agrees with the image-controlled row for the child, mother, birth date, birth place, informant, and parent residence; only the terminal father-name mark remains bounded.
- The source packet and conversion review note consistently flag the converted Markdown as a row-level derivative conflict and identify the Pulgar/Arriagada row as the controlled physical entry.
- The record is a civil birth registration image, so it is strong primary evidence for the narrow birth-registration and stated-parent claims once the row conflict is preserved.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8.5/10 |
| conversion_confidence_score | 8/10 for the image-controlled row and assigned chunk; 2/10 for the conflicting converted Markdown entry `172` |
| evidence_quantity_score | 4/10 |
| agreement_score | 7/10 overall: source image, chunk, source packet, and QA note agree, but the converted Markdown materially conflicts |
| identity_confidence_score | 8.5/10 for the narrow source-row identity of `Jose del Carmen Segundo Pulgar Arriagada`; 5.5/10 for attaching source-named parents to existing canonical stubs; 0.5/10 for any Dario-line bridge |
| claim_probability | 0.90 that physical row `172` is the Pulgar/Arriagada birth registration; 0.86 for the child's recorded name; 0.72 for the mother name; 0.60 for the father base name only; 0.02 or lower for Dario-line attachment |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold for canonical promotion until row-control conflict is handled; ready only as reviewed staging evidence for a narrow Pulgar/Arriagada row correction and bounded claims |

## Review Finding

The staged identity analysis is supported as a proof-review hold with a clear correction path. The best-supported judgment is that physical entry `172` on page 58 is the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`, with mother `Juana Arriagada de Pulgar` and father certified only as `Jose del Carmen Pulgar`.

The current converted Markdown is not reliable for this row because it describes a different birth registration under the same entry number. That conflict should remain explicit in staging and should not be converted into identity variation evidence.

## Next Action

Revise or supersede the derivative converted-row evidence before canonical promotion. After that, promote only narrow row-level claims for the child, birth facts, and stated parents, keeping the father suffix unresolved and keeping all Dario-line identity bridges on hold for separate proof review.
