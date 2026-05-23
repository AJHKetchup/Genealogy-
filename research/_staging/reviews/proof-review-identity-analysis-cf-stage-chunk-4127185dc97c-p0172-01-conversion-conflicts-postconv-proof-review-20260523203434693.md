---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260523203434693
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md
staged_draft: research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md
referenced_conflict_draft: research/_staging/conflicts/CF-STAGE-CHUNK-4127185dc97c-P0172-01-conversion-conflicts.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-4127185dc97c-P0172-01-los-angeles-birth-register-1889-page-172.md
source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
referenced_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
canonical_readiness: hold
---

# Proof Review: Identity Analysis CF-STAGE-CHUNK-4127185dc97c-P0172-01

## Blockers First

- The assigned staged draft remains a conversion-versus-source-image identity analysis, not a resolved independent-source proof. It should not be promoted to claims, relationships, or canonical person pages.
- The source image is now present and matches the source packet's source SHA-256 `05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545`, but derivative metadata still does not line up with the staged identifiers.
- The staged draft and source packet cite `CHUNK-4127185dc97c-P0172-01` and converted SHA `4127185dc97c...`. The current chunk front matter and manifest identify `CHUNK-fb0d63eb2b71-P0172-01`, with manifest converted SHA `fb0d63eb...`. Current file hashes also differ from both older staged values. This blocks clean citation to the assigned staged chunk.
- The visible source image supports the conflict concern more than the stale literal-support block. Entry 513 is not safely supported as `Isidoro del Carmen Diaz`; it visibly appears to be a Pulgar entry, with the child name and maternal surname still requiring careful letter-by-letter QA.
- Entry 514 should not be promoted with a named father from the older conversion. The visible father field appears closer to `Se ignora`; Mercedes Riquelme appears in the mother/declarant context.
- Entry 515 should not be promoted as Leiva-based. The visible father/declarant surname appears closer to `Neira` than `Leiva`.

## Evidence Strengths

- The page image directly supports page identity: `Paj. 172`, an 1889 birth register for `Los Anjeles`, `num. 1o de La Laja`, with entries 513, 514, and 515 visible.
- The current converted file and current chunk now agree with the image on the heading form `Los Anjeles` and `La Laja`, and they agree that the page contains entries 513-515.
- For entry 513, the image visibly supports father/declarant context for `Jose del Carmen Pulgar` / `Jose del C. Pulgar`; this is a useful candidate reading, but not yet promotion-ready because the child name and mother's surname are still contested.
- For entry 514, the image supports a Mercedes Riquelme mother/declarant context and gives a strong reason to reject the older father-as-named reading.
- For entry 515, the source image gives a strong reason to reopen the surname reading as Neira rather than Leiva.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | A civil birth register page is a strong source class, and the restored source image is present with the expected source hash. |
| conversion_confidence_score | 0.43 | Page structure and several fields are now visually supportable, but stale staged metadata and contested names prevent high confidence. |
| evidence_quantity_score | 0.58 | One direct page image plus derivative conversion/chunk evidence; enough to identify the QA problem, not enough for canonical identity promotion. |
| agreement_score | 0.39 | The image, current conversion, current chunk, source packet, and staged conflict note agree on the need for QA, but not on stable identifiers or all name readings. |
| identity_confidence_score | 0.31 | Page identity is high; individual child and parent identities remain too unstable for canonical attachment. |
| claim_probability | 0.72 | It is probable that the staged draft correctly identifies a real conversion conflict on page 172 entries 513-515. Exact person claims from the stale reading are much less probable. |
| relevance_level | direct | The evidence is exactly the source image, source packet, converted file, and chunk cited by the assigned staged draft. |
| relevance_confidence | 0.99 | No external or unrelated evidence was needed. |
| canonical_readiness | hold | Hold for conversion QA and metadata reconciliation before any claim or relationship promotion. |

## Claim-Level Notes

| Item | Probability | Review judgment |
| --- | ---: | --- |
| Page 172 contains entries 513-515 in the 1889 Los Anjeles/La Laja birth register | 0.92 | Supported by the image and current conversion/chunk. |
| Entry 513 is a Diaz child as in the stale literal-support block | 0.08 | Not supported by the visible image; do not promote. |
| Entry 513 is a Pulgar-related child with father/declarant Jose del Carmen Pulgar | 0.67 | Plausible and visually supported in father/declarant fields, but child name and mother surname need targeted QA. |
| Entry 514 father is a named Riquelme father from the older conversion | 0.12 | The visible father field appears closer to `Se ignora`; do not promote a named father. |
| Entry 514 mother/declarant is Mercedes Riquelme | 0.80 | Visually plausible, but should wait for a corrected conversion note before canonical promotion. |
| Entry 515 is Leiva-based | 0.15 | The visible surname appears closer to Neira; do not promote Leiva. |
| Entry 515 is Neira-based | 0.76 | Strong competing reading from the image, but still requires corrected conversion/chunk metadata before promotion. |

## Identity And Relationship Risk

- Identity risk is high for entry 513 if `Diaz`, `Pulgar`, `Amador`, `Amagada`, or related Pulgar-line identities are normalized from derivative text rather than from the image.
- Relationship risk is high for entry 514 because father-known versus father-unknown changes the parentage claim.
- Relationship risk is high for entry 515 because Leiva versus Neira changes the father/declarant identity.
- No Dario, Arturo, Smith, or confirmed Arriagada identity is supported by this page. Any Dario/Pulgar-line use remains an anti-conflation comparison only.

## Next Action

Keep the assigned staged draft on `hold_for_conversion_qa`. Reconcile the staged `CHUNK-4127185dc97c-P0172-01` / converted SHA metadata with the current `CHUNK-fb0d63eb2b71-P0172-01` derivative set, then update or create a corrected conversion-QA note for entries 513-515 from the restored source image. After that, rerun proof review on specific narrow claims: entry 513 child name and parent fields, entry 514 father-unknown and Mercedes Riquelme fields, and entry 515 Neira/Leiva surname resolution.
