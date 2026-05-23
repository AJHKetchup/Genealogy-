---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260523180329671
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md
staged_draft_reviewed: research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md
canonical_readiness: hold
review_date: 2026-05-23
---

# Proof Review: Page 172 Conversion Conflicts

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md`.
- The referenced chunk path remains unavailable: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md`. The available chunk is `page-0001-chunk-01.md` with chunk id `CHUNK-bdb698de8106-P0001-01`, not the staged draft's `CHUNK-4127185dc97c-P0172-01`.
- The restored source image supports the page identity and entries 513-515, but it also supports the staged draft's warning that the converted/chunk transcription is not reliable for identity promotion.
- Entry 513 is not supportable as `Isolina del Carmen José` from the image review. The visible row is closer to a Pulgar child with given-name text resembling `Rosa Dani...`, while the father/declarant context appears to be `José del Carmen Pulgar` / `José del C. Pulgar`.
- Entry 514 is not supportable as father `Belisario Riquelme`. The visible father field appears closer to `se ignora`, while the mother/declarant line supports `Mercedes Riquelme`.
- Entry 515 is not supportable as `Pedro Pablo Leiva`. The visible row appears closer to `Pedro Pablo Neira` and a Neira child/family context.
- No Dario, Arturo, Smith, Dario Jose, or confirmed Arriagada identity is visible in this source page. Any Pulgar-to-Dario or Pulgar-Smith linkage would be an unsupported relationship jump from this draft.

## Evidence Strengths

- Source class is strong: a civil birth register page is direct evidence for births and parent/declarant details when the image is read correctly.
- The source image confirms `Páj. 172`, year 1889, jurisdiction wording consistent with Los Anjeles/La Laja, and visible entries 513, 514, and 515.
- Entry 513 visibly supports a Pulgar context, including a father/declarant candidate whose given and surname forms align with `José del Carmen Pulgar` / `José del C. Pulgar`.
- Entry 514 visibly supports Mercedes Riquelme as the mother/declarant context, even though the converted father field is unreliable.
- Entry 515 visibly supports a Neira reading as a serious competing surname to the converted `Leiva` reading.

## Scored Judgment

| Item | source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| Page 172 records entries 513-515 in the 1889 Los Anjeles/La Laja birth register | 0.88 | 0.72 | 0.82 | 0.78 | 0.86 | 0.92 | direct | 0.98 | review_later |
| Entry 513 is a Pulgar-related birth entry, not a Diaz entry | 0.86 | 0.38 | 0.58 | 0.42 | 0.58 | 0.72 | direct | 0.96 | hold |
| Entry 513 father/declarant candidate is José del Carmen Pulgar / José del C. Pulgar | 0.86 | 0.48 | 0.62 | 0.55 | 0.66 | 0.74 | direct | 0.94 | hold |
| Entry 513 mother surname is Amador/Amagada/Arriagada or any normalized variant | 0.86 | 0.24 | 0.36 | 0.24 | 0.28 | 0.32 | direct | 0.88 | hold |
| Entry 514 father is unknown / `se ignora`, not Belisario Riquelme | 0.86 | 0.26 | 0.50 | 0.30 | 0.46 | 0.68 | direct | 0.91 | hold |
| Entry 514 mother/declarant is Mercedes Riquelme | 0.86 | 0.56 | 0.60 | 0.58 | 0.64 | 0.76 | direct | 0.90 | hold |
| Entry 515 is Neira-related rather than Leiva-related | 0.86 | 0.28 | 0.46 | 0.30 | 0.42 | 0.66 | direct | 0.88 | hold |
| Any relationship from this page to Dario Arturo Pulgar, Dario Arturo Pulgar-Smith, Dario Jose Pulgar-Arriagada, or a Pulgar-Arriagada identity | 0.86 | 0.10 | 0.05 | 0.02 | 0.02 | 0.03 | anti-conflation | 0.95 | blocked |

## Review Findings

The staged draft's core recommendation is supported: this page should remain a conversion-QA conflict, not a source for canonical promotion. The restored image changes the prior asset blocker but does not remove the proof blocker. It confirms that the converted file and available chunk contain material identity errors or unstable readings in the exact fields needed for person and relationship claims.

The strongest claim is page-level, not person-level. Page number, year, civil-register type, and entry numbers are usable context. Individual names and parentage for entries 513-515 require a corrected transcription before claim extraction.

For entry 513, Pulgar is more probable than Diaz, and José del Carmen Pulgar is a plausible father/declarant candidate. That remains a scored hypothesis rather than a promotable conclusion because the child name and mother surname are not stable enough in the current derivatives.

For entry 514, the converted `Belisario Riquelme` father claim should not be used. The image-reviewed evidence favors an unknown father field and a Mercedes Riquelme mother/declarant context.

For entry 515, the converted `Leiva` reading should not be used for identity or parentage promotion. The image supports a competing `Neira` hypothesis that requires corrected transcription.

## Next Action

Keep `research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md` on hold for conversion QA.

Create or regenerate the correct page chunk for `CHUNK-4127185dc97c-P0172-01`, then perform a targeted corrected transcription of entries 513-515 from the source image. Only after that should any proof-review worker evaluate whether entry 513 connects to existing Pulgar/Juana wiki identities. Do not promote, merge, rename, or attach any Dario/Pulgar/Pulgar-Smith/Arriagada identity from this staged draft.
