---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531001505918.md
worker: postconv-proof-review-20260531084402561
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531001505918.md
review_status: hold
canonical_readiness: not_ready
created_at: 2026-05-31T08:44:02Z
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

## Blockers

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531001505918.md`.
- Physical page control is unresolved. The assigned chunk contains a 1979-1970 work-history page, while the conversion-job page Markdown for page 5 contains a 1999-1997 consulting-work page.
- The controlling visible source could not be checked in this review. `raw/sources/CV of Dario Arturo Pulgar.pdf`, `page-images/page-0005.jpg`, and `extracted-images/page-0005.jpg` are absent locally.
- Provenance is unstable. The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for the same path/page with different character counts and hashes, and the source packet records drift between recorded and observed converted/chunk hashes.
- Page 5, in either derivative text, does not independently state `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, a parent, spouse, child, or kinship relationship.
- No canonical claim, relationship, person merge, identity attachment, or wiki update should be promoted from this staged item.

## Evidence Strengths

- The staged identity analysis accurately identifies the issue as a conversion-control conflict, not a resolved biographical contradiction.
- The source packet and assigned chunk literally support the existence of a derivative 1979-1970 work-history transcription for HABITAT, National Film Board of Canada, Chile Films, and CITELCO.
- The conversion-job page Markdown and current aggregate converted file literally support a competing page-5 derivative transcription for PROFONANPE, Television Trust for the Environment, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- The document-level source title in metadata supports only the broad context that the CV is titled for `Dario Arturo Pulgar`; it does not, by itself, prove attachment to any canonical Dario/Pulgar identity.

## Scored Judgment

| field | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.30 | The cited source is a CV and likely relevant, but the source PDF and page image are unavailable for direct visual verification in this checkout. |
| conversion_confidence_score | 0.15 | Two conflicting derivative page-5 transcriptions, duplicate manifest entries, missing page image/PDF, and hash drift make conversion control unsafe. |
| evidence_quantity_score | 0.35 | There are multiple derivative texts and a source packet, but no authoritative visible source for page 5 and no relationship evidence. |
| agreement_score | 0.20 | The source packet and assigned chunk agree with each other, but they materially conflict with `page-markdown/page-0005.md` and the current aggregate page-5 sequence. |
| identity_confidence_score | 0.45 | Moderate only for document-level `Dario Arturo Pulgar` as CV-title context; low for attachment to `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada/Jose/Juana cluster. |
| claim_probability | 0.40 | It is plausible both derivative bodies belong somewhere in the CV, but this review cannot certify which text controls physical page 5. |
| relevance_level | high | The reviewed materials directly address the assigned staged draft and its page-control conflict. |
| relevance_confidence | 0.98 | The draft, source packet, chunk, converted file, page Markdown, and manifests all point to the same disputed page-5 control problem. |
| canonical_readiness | 0.05 | Not ready for canonical facts, relationships, identity merges, identity renames, or promotion. |

## Claim Assessment

- Literal support: partial and derivative-only. Each competing text is readable, but neither can be certified as the physical page-5 source without restored source/page-image control.
- Uncertainty: high for page assignment and derivative chain; moderate for document-level identity; very high for canonical identity attachment.
- Source reliability: blocked by missing visible source and missing rendered page image.
- Conversion confidence: very low until conversion QA reconciles page Markdown, chunk output, manifests, and hashes.
- Identity risk: high if this page is attached to a canonical person or used in a same-person bridge before page-control repair.
- Relationship jumps: unsupported. No parent, spouse, child, family, or kinship relationship is stated in the reviewed page-5 materials.
- Conflict handling: the staged draft's `hold_for_conversion_qa` recommendation is supported.

## Next Action

Keep this item on `hold_for_conversion_qa`.

Required next step: restore or locate the authoritative source PDF and rendered page-5 image, then run conversion QA to decide whether physical page 5 controls to the 1999-1997 consulting-work text or the 1979-1970 work-history text. After that, rerun proof review for the surviving page-5 claims and perform any identity-bridge review separately.

No external research was performed. No raw sources, converted Markdown, chunks, source packets, staged claims, or canonical wiki pages were edited.
