---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260523175202826
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md
staged_draft: research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-4127185dc97c-P0172-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
referenced_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
available_chunk_checked: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
canonical_readiness: hold
---

# Proof Review: Page 172 Identity Candidates

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md`.
- No external research was performed. I checked only the staged draft, the referenced source packet, the referenced converted file, the cited chunk path, the available chunk for the same source image, and the source page image.
- The staged draft cannot support canonical promotion because its cited chunk path, `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md`, is unavailable. The available chunk is `page-0001-chunk-01.md` and carries a different chunk id, `CHUNK-bdb698de8106-P0001-01`.
- Entry 513 is materially conflicted. The staged draft says the candidate was previously treated as `Isidoro del Carmen Diaz`, while the converted/available chunk reads a Pulgar child and the page image visibly supports a Pulgar-row reading rather than the staged Diaz identity.
- Entry 514 is materially conflicted. The converted/available chunk reads child `Riquelme Juan Teodoro` and father `Belisario Riquelme`, while the source packet and page image support uncertainty around the child-name and father fields, including a plausible `se ignora` father reading.
- Entry 515 is materially conflicted. The converted/available chunk reads father/declarant `Pedro Pablo Leiva`, while the source packet and page image appear closer to `Pedro Pablo Neira`; the lower part of the row remains image-sensitive.
- Relationship jumps are not supported. Do not attach these rows to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío Pulgar Arriagada, Jose del Carmen Pulgar, Juana de Dios Amagada de Pulgar, or Juana Arriagada de Pulgar from this staged draft alone.

## Evidence Strengths

- The source is a civil birth register page, a strong source type for birth-entry facts when the handwriting is confidently read.
- The page image, source packet, converted file, and available chunk agree on the broad page frame: page 172, 1889, birth register, entries 513-515.
- The staged draft correctly recommends holding for conversion QA rather than promoting identity or relationship conclusions.
- Entry 513 has a useful, image-visible Pulgar-family lead, but the child name and maternal surname need field-level proofing before any canonical identity work.

## Review Scores

| Review item | source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| Overall staged identity analysis | 0.82 | 0.22 | 0.58 | 0.28 | 0.30 | 0.36 | direct | 0.99 | hold |
| Page/entry frame: page 172, entries 513-515 | 0.86 | 0.72 | 0.76 | 0.78 | 0.70 | 0.82 | direct | 1.00 | revise_before_canonical_use |
| Entry 513 identity candidate | 0.84 | 0.28 | 0.62 | 0.34 | 0.42 | 0.48 | direct | 0.98 | hold |
| Entry 514 identity candidate | 0.84 | 0.20 | 0.58 | 0.24 | 0.32 | 0.34 | direct | 0.96 | hold |
| Entry 515 identity candidate | 0.82 | 0.18 | 0.50 | 0.20 | 0.26 | 0.30 | direct | 0.94 | hold |

## Judgment

The staged draft is reliable as a warning note and identity-risk analysis, not as a source of promotable identity claims. The broad page frame is likely correct, but the person-level claims have low conversion confidence and low agreement across the staged draft, source packet, converted transcript, available chunk, and visible page image.

The strongest supported conclusion is: page 172 contains entries 513-515, but the identity candidates for those entries must remain on hold pending conversion QA. The probability that this staged draft is ready for canonical person or relationship promotion is very low.

## Conflicts And Risks

- Literal-support conflict: the page-image and packet review do not support treating the earlier `Isidoro del Carmen Diaz` reading as a settled entry 513 identity.
- Conversion conflict: the available chunk and converted file preserve disputed readings, while the source packet flags those readings as low-to-medium confidence.
- Identity risk: entry 513 could be wrongly merged into a Pulgar lineage by surname alone.
- Relationship risk: entry 514 could incorrectly create a named father where the record may indicate father unknown.
- Surname risk: entry 515 could be wrongly indexed under Leiva if the visible source supports Neira.
- Citation risk: the missing `page-0172-chunk-01.md` blocks clean traceability from this staged draft to its cited chunk.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`.

Resolve the chunk citation mismatch first. Then perform targeted field-level conversion QA against the page image for entry 513 child name/surname, father/declarant, and mother surname; entry 514 child name and father field; and entry 515 father/declarant surname plus the lower-row fields. After those readings are proof-reviewed, create separate identity or relationship reviews only for claims directly supported by the visible source.
