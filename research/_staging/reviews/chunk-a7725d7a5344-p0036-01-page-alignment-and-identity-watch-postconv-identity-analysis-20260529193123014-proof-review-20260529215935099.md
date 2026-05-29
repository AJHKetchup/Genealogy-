---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260529215935099
task_id: "proof-review:research/_staging/identity-analysis/chunk-a7725d7a5344-p0036-01-page-alignment-and-identity-watch-postconv-identity-analysis-20260529193123014.md"
staged_draft: "research/_staging/identity-analysis/chunk-a7725d7a5344-p0036-01-page-alignment-and-identity-watch-postconv-identity-analysis-20260529193123014.md"
reviewed_at: 2026-05-29
canonical_readiness: hold
---

# Proof Review: Dario Pulgar-Arriagada Delegate Entry

## Blockers First

1. Page-image/source-page alignment is not resolved. The staged draft cites source page `36`, but the conversion-job page Markdown containing the delegate-list text is `raw/codex-conversion-jobs/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50/page-markdown/page-0041.md`, while `page-0036.md` contains unrelated French treaty text.
2. The referenced source PDF `raw/sources/R3578-50-5569-5569-Jacket5.pdf` is not present in the workspace, and the manifest-declared page images are deferred/missing from the conversion-job folder. I could not visually verify the source page.
3. Staged metadata is stale or inconsistent: the staged draft/source packet cite converted SHA/chunk prefix `a7725d7a5344`, while the current chunk file and chunk manifest show `93fa0ef652f0` for the same chunk path.
4. The reviewed evidence supports only the page-local claim that `Captain Dario Pulgar-Arriagada, Medical Corps` appears under the Chile delegation. It does not support middle-name expansion, parent/child relationships, spouse, residence, later property ownership, passenger identity, or merger with any canonical Dario Pulgar cluster.

## Evidence Checked

- Staged draft: `research/_staging/identity-analysis/chunk-a7725d7a5344-p0036-01-page-alignment-and-identity-watch-postconv-identity-analysis-20260529193123014.md`
- Referenced conflict draft: `research/_staging/conflicts/chunk-a7725d7a5344-p0036-01-page-alignment-and-identity-watch.md`
- Referenced source packet: `research/_staging/source-packets/chunk-a7725d7a5344-p0036-01-dario-pulgar-arriagada-chile-delegate.md`
- Referenced chunk path: `raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50-codex/page-0036-chunk-01.md`
- Referenced converted file: `raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50.codex.md`
- Conversion-job page Markdown cross-checks: `page-markdown/page-0036.md` and `page-markdown/page-0041.md`

## Literal Support

The chunk and converted file support this literal reading:

```text
THE PRESIDENT OF THE REPUBLIC OF CHILE:

 Colonel Guillermo Novoa-Sepulveda, Military Attache/Attaché to the
Legation of Chile at Berlin,
 Captain Dario Pulgar-Arriagada, Medical Corps;
```

The page-local name, rank, country grouping, and service label are supported in the derivative text. The conversion-job page `page-0041.md` contains the same printed page `36` text. The conversion-job page `page-0036.md` does not contain this delegate entry.

## Scored Judgment

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.68 | Government/international convention delegate-list source type is good for a delegate-list claim, but the source PDF is unavailable for direct inspection. |
| conversion_confidence_score | 0.62 | Chunk, converted file, and `page-0041.md` agree on the reading; missing images/PDF and page-file mismatch lower confidence. |
| evidence_quantity_score | 0.46 | Multiple derivative files agree, but they appear to derive from the same conversion lineage and no visual/source corroboration was available. |
| agreement_score | 0.70 | Agreement is strong for the literal name/rank/service text; metadata and page-file alignment disagree. |
| identity_confidence_score | 0.84 | High only for the page-local identity `Dario Pulgar-Arriagada`, Chile delegate, Medical Corps. |
| claim_probability | 0.80 | The narrow delegate-list claim is likely, pending source-page/image alignment. |
| relevance_level | high | Directly relevant to the assigned staged identity-analysis draft. |
| relevance_confidence | 0.96 | The reviewed files all reference the same assigned staged draft and delegate-list issue. |
| canonical_readiness | 0.20 | Hold. Do not promote until source/page-image alignment and stale hash metadata are resolved. |

## Identity And Relationship Risk

- Same-person confidence is high only inside this page-local record.
- Identity risk is moderate-high if this is merged with `Dario Jose Pulgar-Arriagada`, `Dario Pulgar A.`, `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, passenger-list stubs, or the canonical `Darío Pulgar Arriagada` page without a separate bridge.
- Relationship jumps are unsupported. No parents, spouse, children, household, lineage, age, residence, or signature appear in the reviewed page text.
- No visible-source basis was found here for `Jose`, `Arturo`, `Smith`, `J.`, or an expansion of `A.`.

## Evidence Strengths

- The staged draft correctly treats the evidence as a bounded delegate-list claim rather than a family relationship or canonical merge.
- The literal entry is consistently transcribed in the referenced chunk, converted file, source packet, and conversion-job `page-0041.md`.
- The staged draft correctly flags the page-alignment concern and recommends holding broader identity conclusions.

## Next Action

Hold this staged draft. Before any canonical promotion, resolve the missing source/image problem and determine whether `page-0041.md` is the correct rendered image/file for printed source page `36`, or whether the chunk/source-packet page assignment is wrong. If that alignment is verified, promote only the narrow claim that `Dario Pulgar-Arriagada` is listed under Chile as `Captain ... Medical Corps`; run a separate identity-bridge review before attaching that claim to any broader person or family cluster.
