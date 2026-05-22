---
type: claim
status: draft
claim_type: source_identifier
confidence: 4.0
subject: Treaty Series No. 846 cover in League of Nations registry file
predicate: has_handwritten_file_number
object: "top-center handwritten file number present; exact reading unresolved"
date: null
place: null
source: raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md
source_path: raw/sources/R3578-50-5569-5569-Jacket5.pdf
source_packet: research/_staging/source-packets/sp-stage-chunk-3f469b56e502-p0005-01-treaty-series-846-cover.md
chunk: raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0005-chunk-01.md
chunk_id: CHUNK-3f469b56e502-P0005-01
page_reference: "page 5"
conversion_confidence: low_for_exact_number
promotion_recommendation: hold_for_conversion_qa
tags: [claim, staging, source-identifier, handwritten-number, conversion-qa]
---

# Atomic Claim: Handwritten File Number Present

## Claim

The page has a handwritten top-center file number, but the exact reading is unresolved and should not be promoted as canonical source metadata.

## Literal Source Support

Current conversion text reads:

```text
[Handwritten at top center]
50 /5509/5509
```

Proof review reports that the page image confirms a handwritten top-center identifier, but does not clearly support the exact converted reading `50 /5509/5509`; the final group may read closer to a `5569`-like value.

## Source Path

- Source path: `raw/sources/R3578-50-5569-5569-Jacket5.pdf`
- Converted file: `raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md`
- Chunk/page reference: `CHUNK-3f469b56e502-P0005-01`, page 5.

## Conversion Confidence And QA Concern

Reading confidence is low for the exact number. The converted transcription gives `50 /5509/5509`, nearby jacket metadata uses `50 5569 5569`, and proof review found the image-reviewed evidence does not clearly support the staged exact reading. This is a conversion-QA blocker for the handwritten identifier only.

## Uncertainty

The number may be a conversion misread, a handwritten variant, or a separate administrative notation. The only supported claim at this stage is that a top-center handwritten identifier is present. The exact transcription remains unresolved.

## Promotion Recommendation

Hold for conversion QA. Do not promote the exact handwritten number until the page image is re-read and reconciled with adjacent file metadata.
