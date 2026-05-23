# Proof Review: chunk-7d3991a78bc8-p0001-01-002-child-sex

- Review task id: `proof-review:research/_staging/claims/chunk-7d3991a78bc8-p0001-01-002-child-sex.md`
- Reviewed staged draft: `research/_staging/claims/chunk-7d3991a78bc8-p0001-01-002-child-sex.md`
- Role: claim_reviewer
- Worker: `postconv-proof-review-20260523002215327`
- Review status: hold
- canonical_readiness: hold_for_conversion_qa

## Blockers

- The assigned converted file and chunk do not support the staged Pulgar/Arriagada identity context. They transcribe entry 172 as `Jose Miguel`, child of Oswaldo Bunster and Amelia de la Maza, while the staged claim and source packet rely on an image reread for `Jose del Carmen Segundo Pulgar Arriagada`.
- The visible source image supports a male sex reading for entry 172, but the derivative transcript conflict attaches the same entry number and chunk id to two incompatible child identities. This creates elevated identity risk even though the sex field itself is readable.
- Do not promote this claim to canonical claim or person pages until conversion QA corrects or retires the conflicting Bunster/de la Maza derivative transcription.

## Scoring

- source_quality_score: 0.86
- conversion_confidence_score: 0.38
- evidence_quantity_score: 0.60
- agreement_score: 0.48
- identity_confidence_score: 0.72
- claim_probability: 0.88
- relevance_level: critical
- relevance_confidence: 0.92
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The original source image is available at the path cited by the staged draft and source packet.
- Visual inspection of page 58, entry 172 shows the Pulgar/Arriagada row and the sex cell reads `Hombre`.
- The source packet gives the same literal support, `Sexo: Hombre`, and explicitly flags the conversion/chunk conflict rather than hiding it.
- The claim is narrow: it records only the sex value and does not add a parent, relationship, or broader identity conclusion beyond the staged subject label.

## Review Judgment

The sex claim is directly supported by the cited page image and source packet. The exact visible value for entry 172 is `Hombre`, so the field-level claim probability is high.

Canonical readiness remains a hold. The converted Markdown and chunk still contradict the image-reviewed Pulgar/Arriagada evidence by presenting entry 172 as a Bunster/de la Maza child. That derivative conflict lowers agreement and conversion confidence enough to block promotion despite strong visible support for the sex field.

## Next Action

Send to conversion QA to reconcile `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` and `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md` against the source image for page 58, entry 172. Keep this sex claim staged on hold until that reconciliation is recorded.
