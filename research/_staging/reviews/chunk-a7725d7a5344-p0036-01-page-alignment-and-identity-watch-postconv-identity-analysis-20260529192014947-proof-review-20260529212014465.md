---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260529212014465
task_id: "proof-review:research/_staging/identity-analysis/chunk-a7725d7a5344-p0036-01-page-alignment-and-identity-watch-postconv-identity-analysis-20260529192014947.md"
staged_draft: "research/_staging/identity-analysis/chunk-a7725d7a5344-p0036-01-page-alignment-and-identity-watch-postconv-identity-analysis-20260529192014947.md"
reviewed_at: 2026-05-29
canonical_readiness: hold
---

# Proof Review: Dario Pulgar-Arriagada Delegate Listing

## Blockers First

1. Canonical promotion should remain on hold. The staged draft's narrow claim is textually supported by derivative Markdown, but the rendered page image paths in the conversion manifest are not present in this checkout, so I could not verify the name against the visible source image.
2. Page alignment remains unresolved. The assigned chunk path is `page-0036-chunk-01.md`, but the conversion-job `page-markdown/page-0036.md` contains unrelated French medical text, while `page-markdown/page-0041.md` contains internal page number `36` and the Chile delegate list.
3. Identifier and checksum metadata conflict. The staged draft/source packet use `CHUNK-a7725d7a5344-P0036-01`, but the actual chunk frontmatter and chunk manifest identify the referenced file as `CHUNK-93fa0ef652f0-P0036-01`. The source packet's converted SHA-256 also does not match the current converted file hash observed in this checkout.
4. The assigned source page gives no age, birth date, parents, spouse, children, residence, signature, full middle name, or explicit bridge to any other Dario Pulgar / Pulgar-Arriagada identity cluster.
5. The page does not support expanding the name to `Dario Jose`, `Darío J.`, `Dario Arturo`, `Pulgar-Smith`, or attaching Jose/Juana parent candidates.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/chunk-a7725d7a5344-p0036-01-page-alignment-and-identity-watch-postconv-identity-analysis-20260529192014947.md`
- Source packet: `research/_staging/source-packets/chunk-a7725d7a5344-p0036-01-dario-pulgar-arriagada-chile-delegate.md`
- Referenced chunk: `raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50-codex/page-0036-chunk-01.md`
- Converted file: `raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50.codex.md`
- Conversion job page Markdown: `page-markdown/page-0036.md` and `page-markdown/page-0041.md`
- Conversion manifests: job manifest and chunk manifest for the same conversion job

## Literal Support

The referenced chunk, source packet, converted file, and conversion-job `page-markdown/page-0041.md` all preserve the same narrow delegate-list text:

```text
THE PRESIDENT OF THE REPUBLIC OF CHILE:

 Colonel Guillermo Novoa-Sepulveda, Military Attaché to the
Legation of Chile at Berlin,
 Captain Dario Pulgar-Arriagada, Medical Corps;
```

This supports only the bounded statement that a derivative conversion names `Captain Dario Pulgar-Arriagada, Medical Corps` under the Chile delegate heading. It does not independently prove family identity, middle name, parentage, or relationship claims.

## Scored Judgment

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.62 | The underlying source appears to be an official convention/delegate-list PDF, but this review could not inspect the referenced page image. |
| conversion_confidence_score | 0.54 | Multiple derivative files agree on the Dario text, but page-markdown alignment, chunk ID, and checksum conflicts reduce confidence. |
| evidence_quantity_score | 0.42 | There is one page-local delegate-list entry and no corroborating vital, family, or identity-bridge data on the assigned page. |
| agreement_score | 0.66 | The chunk, source packet, converted file, and `page-0041.md` agree on the name and role; `page-0036.md` and metadata disagree on page alignment. |
| identity_confidence_score | 0.78 | High for a page-local `Dario Pulgar-Arriagada` delegate mention; low for merging to any broader Dario Pulgar identity. |
| claim_probability | 0.70 | The narrow delegate/rank/service claim is probable in derivative text, but not ready without visible-source/page alignment confirmation. |
| relevance_level | 1.00 | Directly relevant to the staged identity-analysis draft and Pulgar-Arriagada watch item. |
| relevance_confidence | 0.98 | The reviewed files are the exact files referenced by the staged draft and source packet. |
| canonical_readiness | 0.12 | Hold. Do not promote until the page image/source-page alignment and metadata conflicts are resolved. |

## Evidence Strengths

- The derivative transcription is internally stable for the narrow phrase `Captain Dario Pulgar-Arriagada, Medical Corps`.
- The entry is in a coherent delegate-list context under `THE PRESIDENT OF THE REPUBLIC OF CHILE`.
- No uncertain or illegible words are reported in the relevant derivative chunk or in `page-markdown/page-0041.md`.
- The staged draft correctly avoids treating this page as proof of age, parentage, spouse, children, residence, or Pulgar-Smith identity.

## Identity And Relationship Risk

- Identity risk is moderate-high if this evidence is merged by name alone with `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, passenger-list `Dario Pulgar` stubs, or the canonical `Darío Pulgar Arriagada` legal-notice stub.
- Relationship-jump risk is high for Jose/Juana parent candidates because the assigned page has no parent-child or household statement.
- Name-normalization risk is moderate: the page supports `Dario Pulgar-Arriagada` only, not `Dario Jose`, `Darío J.`, `Dario Pulgar A.`, or `Dario Arturo`.
- Conflict risk is concentrated in citation integrity rather than the derivative text reading: internal page number `36` appears in `page-0041.md`, while job `page-0036.md` is different text.

## Next Action

Hold this staged draft for page-alignment QA. The next reviewer should recover or regenerate access to the existing rendered page images for `page-0036.jpg` and `page-0041.jpg`, compare the visible page image against both page-markdown files, and reconcile the chunk ID/checksum metadata before any claim promotion. If the image confirms the delegate-list page, promote only the narrow claim that `Dario Pulgar-Arriagada` was listed under Chile as `Captain ... Medical Corps`; keep all identity-merge, middle-name, and relationship claims unpromoted pending separate bridge evidence.
