---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-515-declarant.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-515-declarant.md
reviewer: postconv-proof-review-20260522185454990
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: Entry 515 Declarant

## Blockers

- Canonical readiness is `hold`. The staged draft and source packet already recommend `hold_for_conversion_qa` because entry 515 is in the cropped lower row of the available source image.
- The staged object says Pedro Pablo Leiva declared entry 515 as father and gives age 28, profession `jornalero`, and domicile `Calle San Joaquin`. Direct image review visibly supports the declarant name `Pedro Pablo Leiva` and role `Padre`, but the lower declarant attributes are cut off or not readable in the available PNG.
- The referenced converted file does not support the full staged declarant attribute bundle. Its entry 515 declarant cell reads `Pedro Pablo Leiva`, `Padre`, and blank `Edad`, `Prof.`, and `Dom.` labels; it does not supply age 28, declarant profession, or declarant domicile.
- The referenced chunk path, `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md`, is unavailable in the workspace, so the staged literal support cannot be verified against the named chunk.
- The visible image appears to show `Prof. Jornalero` in the father column for Pedro Pablo Leiva, but that is not the same as image-verifiable support for the declarant attributes in the declarant column. Do not transfer the father-column profession into the declarant-column claim without explicit source support.

## Scores

| source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
|---:|---:|---:|---:|---:|---:|---|---:|---|
| 0.88 | 0.42 | 0.45 | 0.35 | 0.72 | 0.48 | high | 0.92 | hold |

## Evidence Strengths

- The cited source is a civil birth register, a strong source type for declarant identity and role when the row is complete and legible.
- The staged draft, source packet, converted file, conflict notes, and image all refer to page 172, entry 515 of the 1889 Los Anjeles birth register.
- Direct image review supports the core identity/role portion of the claim: the entry 515 declarant column visibly reads `Pedro Pablo Leiva` with `Padre` beneath it.
- The father column also visibly names `Pedro Pablo Leiva`, reducing the risk that the declarant name is attached to the wrong row or person.

## Review Judgment

Hold or revise the staged claim. The narrow assertion that Pedro Pablo Leiva was the father-declarant for entry 515 is probable, but the full staged claim is over-specific. Age 28, declarant profession, and declarant domicile are not supported by the referenced converted file and are not visible enough in the available cropped image.

This is not a rejection of Pedro Pablo Leiva as the entry 515 father/declarant. It is a scored proof judgment that the current atomic claim combines a supported identity/role with unsupported attributes.

## Next Action

Keep this claim out of canonical folders. Either perform targeted conversion QA against a complete lower-row image or revise the staged claim to the source-supported narrower assertion: Pedro Pablo Leiva appears as the declarant and is identified as father for entry 515. Do not include age, declarant profession, or declarant domicile unless a complete source image or reliable corrected conversion visibly supports those fields.
