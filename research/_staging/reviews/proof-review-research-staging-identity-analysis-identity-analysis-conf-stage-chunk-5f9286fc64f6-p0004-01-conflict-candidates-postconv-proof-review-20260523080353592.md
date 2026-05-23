---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conf-stage-chunk-5f9286fc64f6-p0004-01-conflict-candidates.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conf-stage-chunk-5f9286fc64f6-p0004-01-conflict-candidates.md
review_status: hold
canonical_readiness: hold
reviewer: postconv-proof-review-20260523080353592
---

# Proof Review: Identity Conflict Analysis for CHUNK-5f9286fc64f6-P0004-01

## Blockers

- The staged draft is properly conservative, but it is not canonically ready because page 4 is a continuation CV page and the page body does not state `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or any family relationship.
- Identity attribution rests on document-level metadata: `raw/sources/CV of Dario Arturo Pulgar.pdf`, the converted title, and the source packet title. Page 4 itself supplies occupational text only.
- The referenced chunk path exists, but its front matter reports `chunk_id: CHUNK-56be215c030b-P0004-01` and `converted_sha256: 56be215c030b...`, while the staged draft and source packet use `CHUNK-5f9286fc64f6-P0004-01` and `converted_sha256: 5f9286fc64f6...`.
- A fresh local hash check of `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md` returned `d8bf6fa795b77018c9044d3fcb56a90f97197f43593cada8e2c9191c612d9a14`, which does not match either the source packet or chunk converted SHA. Reconcile the conversion/chunk/source-packet lineage before promotion.
- The source packet says the rendered page image was missing, but `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg` is now present and was inspected. This reduces transcription risk but does not resolve metadata/hash provenance.
- Page 4 contains no direct relationship evidence, no parent/spouse/child statement, and no bridge to `Dario Arturo Pulgar-Smith` or to Pulgar-Arriagada/Jose/Juana candidate clusters.

## Evidence Scores

| field | score | rationale |
|---|---:|---|
| source_quality_score | 0.62 | A CV is useful for occupational chronology but is authored or compiled biographical evidence, not independent vital or kinship evidence. |
| conversion_confidence_score | 0.78 | The page image is present and visibly supports the key IBRD and Antamina readings, including correction of `aassessing` to `assessing`; metadata/hash mismatch still limits confidence. |
| evidence_quantity_score | 0.46 | One continuation page plus document-level metadata supports occupational entries, but there is no page-local name or independent identity bridge. |
| agreement_score | 0.54 | The image, converted file, chunk body, and source packet agree on the page text and no direct conflict; the chunk id and converted SHA values disagree. |
| identity_confidence_score | 0.58 | The document title and source path point to `Dario Arturo Pulgar`, but page 4 does not name the person and does not bridge to `Pulgar-Smith`. |
| claim_probability | 0.84 | The staged draft's main claim, no direct internal conflict on page 4 with identity-attribution hold, is well supported. |
| relevance_level | 0.86 | The review is directly relevant to conflict/identity handling for page 4 and to preventing over-attachment of CV occupational entries. |
| relevance_confidence | 0.90 | The reviewed files and page image are the exact staged draft's referenced evidence set. |
| canonical_readiness | 0.20 | Hold. Do not promote, merge, rename, or attach page-4 occupational claims to canonical person pages until provenance and identity bridging are resolved. |

## Evidence Strengths

- The rendered page image visibly supports the page-4 occupational entries for `2000`, `International Bank for Reconstruction and Development (IBRD)`, `Bolivia, Peru`, `Senior Consultant`, `1999 - 2000`, `Antamina Mining Company`, `Huarmey, Peru`, and `Head Community Relations`.
- The visible page supports the staged draft's caution that no full personal name appears in the page body.
- The source packet and converted page correctly identify page 4 as occupational CV evidence, not family relationship evidence.
- The staged draft correctly treats Pulgar-Arriagada and Jose/Juana comparisons as anti-conflation risks rather than as supported same-person or relationship conclusions from this page.
- The raw PDF exists locally and its SHA-256 matches the source packet/source metadata: `07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424`.

## Review Judgment

The staged identity/conflict analysis is supported as a held no-direct-conflict finding. Page 4 supports occupational text for the document-level CV subject, but it does not independently identify that subject, does not prove that `Dario Arturo Pulgar` is canonical `Dario Arturo Pulgar-Smith`, and does not support any Pulgar-Arriagada or Jose/Juana relationship attachment.

No source transcription correction is authorized from this review note. The visible image can support asking whether the converted text should be re-QA'd, especially where the conversion has `aassessing` but the image reads `assessing`; the review boundary does not allow changing source or canonical text here.

## Next Action

Keep `research/_staging/identity-analysis/identity-analysis-conf-stage-chunk-5f9286fc64f6-p0004-01-conflict-candidates.md` on hold. Reconcile the converted-file SHA, chunk id, source packet id, and staged draft id; then rerun or record conversion QA against the available page image. Only after that, seek an identity-bearing CV page or accepted local bridge that explicitly connects `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith` before promoting page-4 occupational claims or attaching them to a canonical person.
