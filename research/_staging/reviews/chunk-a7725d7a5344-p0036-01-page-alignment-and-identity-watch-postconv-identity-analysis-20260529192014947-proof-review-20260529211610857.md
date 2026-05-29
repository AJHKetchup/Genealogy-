---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260529211610857
task_id: "proof-review:research/_staging/identity-analysis/chunk-a7725d7a5344-p0036-01-page-alignment-and-identity-watch-postconv-identity-analysis-20260529192014947.md"
staged_draft: "research/_staging/identity-analysis/chunk-a7725d7a5344-p0036-01-page-alignment-and-identity-watch-postconv-identity-analysis-20260529192014947.md"
reviewed_subject: "Dario Pulgar-Arriagada"
reviewed_claim: "A delegate-list entry under Chile names Captain Dario Pulgar-Arriagada, Medical Corps."
source_packet: "research/_staging/source-packets/chunk-a7725d7a5344-p0036-01-dario-pulgar-arriagada-chile-delegate.md"
converted_file: "raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50.codex.md"
chunk: "raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50-codex/page-0036-chunk-01.md"
canonical_readiness: hold
---

# Proof Review: Dario Pulgar-Arriagada Delegate Listing

## Blockers First

1. Page-image verification is not available in the local workspace. The job manifest references `page-images/page-0036.jpg`, but that path is absent, so the visible source cannot be checked directly in this review.
2. There is an unresolved page-alignment conflict. The prepared chunk and source packet give source page `36` and contain the Chile delegate listing; `raw/codex-conversion-jobs/.../page-markdown/page-0041.md` also contains that same text while internally labeling it page `36`; but `page-markdown/page-0036.md` contains different French treaty text and is only a rough Docling conversion.
3. The source does not support identity expansion beyond the page-local form `Dario Pulgar-Arriagada`. It does not state `Dario Jose`, `Darío J.`, `Dario Arturo`, `Pulgar-Smith`, parent names, spouse, child, residence, birth date, or death date.
4. Relationship and merge claims are unsupported. The page gives no family relationship and no bridge to the canonical `Darío Pulgar Arriagada` legal-notice stub, `Dario Arturo Pulgar-Smith`, passenger-list `Dario Pulgar` entries, or Jose/Juana parent candidates.

## Evidence Scores

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.62 | The underlying source is an official/international delegate-list packet, but this review could not inspect the rendered source page image and must rely on derivative conversion artifacts. |
| conversion_confidence_score | 0.58 | The staged chunk, source packet, converted aggregate file, and `page-0041.md` agree on the Chile delegate text; confidence is reduced by the absent image and conflicting `page-0036.md` content. |
| evidence_quantity_score | 0.44 | Multiple local derivative files repeat the same reading, but they appear to derive from the same conversion context rather than independent sources. |
| agreement_score | 0.70 | Agreement is good among the staged draft, packet, chunk, aggregate converted file, and `page-0041.md`; agreement is materially weakened by `page-0036.md` containing different text. |
| identity_confidence_score | 0.82 | High for the narrow page-local person named `Dario Pulgar-Arriagada`; low for broader same-person merges. |
| claim_probability | 0.76 | The narrow claim that the derivative conversion names `Captain Dario Pulgar-Arriagada, Medical Corps` under Chile is likely, but canonical proof remains held for image/page alignment. |
| relevance_level | 1.00 | The evidence directly concerns the staged draft and its named subject. |
| relevance_confidence | 0.96 | The same name, country heading, rank, and service appear in the assigned verification materials. |
| canonical_readiness | 0.28 | Hold. The narrow claim may become promotable after page-image/source-page alignment; identity merges and relationship claims are not ready. |

## Literal Support

The assigned chunk and source packet support this bounded reading:

```text
THE PRESIDENT OF THE REPUBLIC OF CHILE:

 Colonel Guillermo Novoa-Sepulveda, Military Attaché to the
Legation of Chile at Berlin,
 Captain Dario Pulgar-Arriagada, Medical Corps;
```

The aggregate converted file also contains the same delegate entry. The conversion-job `page-markdown/page-0041.md` contains the same passage and internally labels it page `36`. By contrast, `page-markdown/page-0036.md` is a rough Docling conversion of different French text, so it cannot support this claim as the page-36 job output without further alignment review.

## Evidence Strengths

- The narrow name/rank/service claim is consistently represented in the staged draft, source packet, prepared chunk, aggregate converted file, and `page-0041.md`.
- The entry is placed under a Chile heading and adjacent to another Chilean delegate, which supports the Chile delegate-list interpretation.
- The prepared chunk reports no uncertain or illegible words and says the page is complete.
- The staged draft appropriately treats broader identity hypotheses as unresolved rather than proved.

## Claim Judgment

The staged analysis is directionally sound as a cautionary identity review. It should remain a hold for canonical use because page alignment is unresolved and the source page image is unavailable here.

Accept only this provisional, bounded claim for further review: a local derivative transcription of the delegate list names `Captain Dario Pulgar-Arriagada, Medical Corps` under `THE PRESIDENT OF THE REPUBLIC OF CHILE`.

Do not promote or infer these claims from this page: `Jose` as a middle name, `J.` expansion, `Arturo`, `Pulgar-Smith`, parentage from Jose/Juana candidates, identity with the 2000 legal-notice stub, identity with passenger-list stubs, or any family relationship.

## Next Action

Hold for targeted page-alignment review. The next reviewer should inspect the rendered source page image or source PDF page corresponding to internal printed page `36`, then reconcile `page-markdown/page-0036.md`, `page-markdown/page-0041.md`, the aggregate converted file, and `CHUNK-a7725d7a5344-P0036-01`. If the visible source confirms the delegate entry, promote only the narrow delegate/rank/service claim and keep all identity-bridge hypotheses separate.
