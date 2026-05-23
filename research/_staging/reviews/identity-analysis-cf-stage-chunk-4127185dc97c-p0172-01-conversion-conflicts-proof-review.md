---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260523182533909
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md
staged_draft: research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-4127185dc97c-P0172-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_available: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_chunk_missing: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
canonical_readiness: hold
claim_probability: 0.40
---

# Proof Review: identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts

## Blockers First

- The staged draft is correctly framed as a conversion conflict, not as proof-ready identity evidence. Do not promote any person, parent-child relationship, same-person assertion, or Pulgar/Dario lineage claim from this draft.
- The source packet cites `page-0172-chunk-01.md`, but that referenced chunk is unavailable. The available chunk is `page-0001-chunk-01.md` with a different chunk id and converted hash. This citation mismatch blocks canonical use.
- The converted file and available chunk materially disagree with the source image and source packet QA note for entries 513, 514, and 515.
- Entry 513: the source image supports a Pulgar-related row more than the derivative `Isolina del Carmen / Jose` formatting, but the exact child given names and maternal surname remain uncertain. The image appears closer to a name beginning `Pulgar ... Jose Dani...`; the father/declarant appears to be Jose del Carmen Pulgar / Jose del C. Pulgar, and the mother appears to be Juana de Dios with a surname that should be proofread letter by letter before being normalized.
- Entry 514: the source image appears to support a father field reading like `se ignora`, not the converted `Belisario Riquelme`. Mercedes Riquelme appears in mother/declarant context. Treat any named-father claim for entry 514 as unsupported.
- Entry 515: the source image appears closer to `Pedro Pablo Neira` than the converted `Pedro Pablo Leiva`. Do not promote Leiva or Neira parentage until conversion QA resolves the row.

## Scored Judgment

| Metric | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register page is a strong original-source class, and the page image is available. |
| conversion_confidence_score | 0.24 | Core name and relationship fields conflict between the derivative conversion and the visible image/source packet QA. |
| evidence_quantity_score | 0.46 | One page image plus derivative transcript/chunk/source packet; enough to identify the conflict, not enough for canonical identity proof. |
| agreement_score | 0.28 | Page number and entries agree, but names, surnames, and father fields do not. |
| identity_confidence_score | 0.34 | Page identity is clear; individual identities and relationships remain unstable. |
| claim_probability | 0.40 | Probable only that page 172 contains entries 513-515 and that several derivative readings are wrong or uncertain. |
| relevance_level | direct | The reviewed evidence directly concerns the assigned staged draft and entries 513-515. |
| relevance_confidence | 0.98 | Source packet, source image, converted file, and staged draft all refer to the same page/source image. |
| canonical_readiness | hold | Requires targeted conversion QA before proof review can promote claims. |

## Evidence Strengths

- The page image is now present and readable enough to confirm that the dispute is real rather than a missing-asset issue.
- Page-level facts are supported: page 172, 1889 birth register, Los Anjeles/La Laja jurisdiction wording, and entries 513, 514, and 515.
- Entry 513 has useful candidate evidence for Jose del Carmen Pulgar as father/declarant, but only as a candidate pending precise source transcription.
- The staged draft's hold recommendation is supported by the source packet, the conversion/chunk mismatch, and visual comparison with the image.

## Claim Review

### Page 172 contains birth-register entries 513-515

Supported at page level. The source image, converted file, available chunk, and source packet all support the page and entry-number scope.

- source_quality_score: 0.82
- conversion_confidence_score: 0.70 for page/entry scope only
- evidence_quantity_score: 0.70
- agreement_score: 0.86
- identity_confidence_score: 0.76
- claim_probability: 0.88
- relevance_level: direct
- relevance_confidence: 0.99
- canonical_readiness: revise_before_use

### Entry 513 proves a specific Pulgar child and parent set

Hold. The visible image supports a Pulgar-context hypothesis and appears to support Jose del Carmen Pulgar as father/declarant, but the exact child name and maternal surname are not proof-ready. The converted `Isolina del Carmen / Jose` structure and the source packet's `Jose Dani...` concern need targeted QA.

- source_quality_score: 0.82
- conversion_confidence_score: 0.26
- evidence_quantity_score: 0.44
- agreement_score: 0.36
- identity_confidence_score: 0.42
- claim_probability: 0.52
- relevance_level: direct
- relevance_confidence: 0.96
- canonical_readiness: hold

### Entry 514 names Belisario Riquelme as father

Not supported for promotion. The source image appears closer to an unknown-father statement, while Mercedes Riquelme appears as mother/declarant. The derivative `Belisario Riquelme` father reading should be treated as a conversion error or unresolved reading until QA.

- source_quality_score: 0.82
- conversion_confidence_score: 0.18
- evidence_quantity_score: 0.42
- agreement_score: 0.20
- identity_confidence_score: 0.22
- claim_probability: 0.12
- relevance_level: direct
- relevance_confidence: 0.94
- canonical_readiness: hold

### Entry 515 names Pedro Pablo Leiva as father/declarant

Not supported for promotion. The visible surname appears closer to Neira than Leiva, and the row is partly cut off/visually difficult. Treat Leiva and Neira as competing transcription hypotheses, not identity claims.

- source_quality_score: 0.76
- conversion_confidence_score: 0.18
- evidence_quantity_score: 0.36
- agreement_score: 0.18
- identity_confidence_score: 0.20
- claim_probability: 0.16
- relevance_level: direct
- relevance_confidence: 0.90
- canonical_readiness: hold

## Identity And Relationship Risk

- Same-person risk is high for any attempt to attach entry 513 to existing Pulgar/Dario/Arriagada identities before the child and mother readings are resolved.
- Relationship risk is high for entry 514 because father-known versus father-unknown changes the relationship model.
- Name-normalization risk is high across `Amador`, `Amagada`, `Arriagada`, `Leiva`, and `Neira`. These should remain separate transcription hypotheses unless the source image visibly supports a specific reading.
- The draft contains no direct Dario, Arturo, Smith, or Pulgar-Smith evidence.

## Next Action

Keep the staged draft on hold for conversion QA. The next worker should resolve the missing cited chunk path and perform targeted side-by-side transcription of entries 513-515 from the page image, especially entry 513 child/mother fields, entry 514 father field, and entry 515 father/declarant surname. After that, run a fresh proof review before any canonical promotion.
