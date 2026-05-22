# Proof Review: claim-chunk-3f469b56e502-p0002-01 file subject

- Review task id: `proof-review:research/_staging/claims/claim-chunk-3f469b56e502-p0002-01-file-subject.md`
- Reviewed staged draft: `research/_staging/claims/claim-chunk-3f469b56e502-p0002-01-file-subject.md`
- Role: claim_reviewer
- Worker: `postconv-proof-review-20260522085220396`
- Review status: revise
- canonical_readiness: revise_before_source_metadata_promotion

## Blockers

- Minor literal-transcription blocker: the visible source image appears to read `Conférence diplomatique (juillet 1929)` with lower-case `diplomatique` and `juillet`, while the staged literal support and chunk render these as `Conférence Diplomatique (Juillet 1929)`. The semantic claim is supported, but capitalization should be normalized to the visible source before canonical source-description promotion.
- The rendered page image recorded in the conversion manifest was not present at `raw/codex-conversion-jobs/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25/page-images/page-0002.jpg`. I verified the page by rendering page 2 from `raw/sources/R3578-50-5569-5569-Jacket5.pdf`; the missing recorded JPG is a reproducibility issue, not a contradiction in the claim.
- This claim is source-context metadata only. It does not identify a genealogical person, vital event, or family relationship and should not be promoted as person/family evidence.

## Scoring

| Draft id | source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|
| `claim-chunk-3f469b56e502-p0002-01-file-subject` | 0.86 | 0.88 | 0.82 | 0.94 | 0.98 | 0.94 | low_source_context | 0.96 | revise_before_source_metadata_promotion |

## Evidence Strengths

- The staged draft, page chunk, source packet, and converted page all cite the same page 2 subject block and agree that the file subject concerns a July 1929 diplomatic conference.
- The visible source supports the core French wording: a diplomatic conference called to revise the 1906 Geneva Convention for improving the condition of wounded and sick in armies in the field and to elaborate/develop a prisoner-of-war code.
- Source reliability is good for this narrow claim because the evidence is an archival file cover/routing slip identifying its own administrative subject.
- Identity risk is minimal because the claim concerns the file's subject line rather than a person. There is no relationship jump or family-identity inference.
- No conflict was found between the staged claim, the converted page, and the visible source regarding the conference subject, date month/year, Geneva Convention reference, or prisoner-of-war-code reference.

## Review Judgment

The claim is very likely supported as source-description metadata. The only substantive issue is literal capitalization in the quoted French support. The prose claim itself accurately summarizes the visible subject line and does not overstate genealogical value.

## Next Action

Revise the literal support/transcription capitalization for `diplomatique` and `juillet` before promoting this as canonical source-description metadata. Do not promote it as person, event, or relationship evidence.
