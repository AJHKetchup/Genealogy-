---
type: source_packet
status: draft
source_id: SP-STAGE-CHUNK-3f469b56e502-P0006-01
source_kind: government_treaty_publication_text
raw_file: raw/sources/R3578-50-5569-5569-Jacket5.pdf
source_path: raw/sources/R3578-50-5569-5569-Jacket5.pdf
converted_file: raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md
chunk: raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0006-chunk-01.md
chunk_id: CHUNK-3f469b56e502-P0006-01
page_start: 6
page_end: 6
page_reference: "page 6"
display_page: "page 6"
source_sha256: 09a9828166381d0dbd9fe5fbfebb432548bf6f216d51556bdf77fe23dcce018f
converted_sha256: 3f469b56e5024d7d0328377f23de9b911d9cfe6353b581c4f564b96ca15981f2
promotion_recommendation: hold_for_conversion_qa
tags: [source-packet, staging, treaty-series, proclamation, prisoners-of-war-convention, source-context]
---

# Source Packet: Proclamation Opening And French Convention Text

## Source Identity

- Source path: `raw/sources/R3578-50-5569-5569-Jacket5.pdf`
- Source SHA-256: `09a9828166381d0dbd9fe5fbfebb432548bf6f216d51556bdf77fe23dcce018f`
- Converted file: `raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md`
- Chunk/page reference: `raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0006-chunk-01.md`, `CHUNK-3f469b56e502-P0006-01`, page 6.
- Chunk manifest: `raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/manifest.json`

## Source Reliability

- Reliability class: printed United States treaty publication text, derived from the published Treaty Series No. 846 item in the League of Nations file jacket.
- Genealogical relevance: source-context evidence only. This page names governments and state offices as treaty parties and begins the French text of the 1929 Prisoners of War Convention. It does not identify a private person, family relationship, vital event, residence, or household.
- Subject attribution: opening page of a presidential proclamation reproducing the French-language Convention relative au traitement des prisonniers de guerre, dated July 27, 1929.

## Literal Support

```text
## By the President of the United States of America

## A PROCLAMATION
```

```text
Whereas, a Convention Relating to the Treatment of Prisoners of War was signed by the respective Plenipotentiaries of the United States of America and forty-six other countries, at Geneva on July 27, 1929
```

```text
## Convention relative au traitement des prisonniers DE GUERRE DU 27 JUILLET 1929.
```

```text
reconnaissant que, dans le cas extreme d'une guerre, il sera du devoir de toute Puissance d'en attenuer, dans la mesure du possible, les rigueurs inevitables et d'adoucir le sort des prisonniers de guerre;
```

## Conversion Confidence And QA Concern

Reading confidence is medium. The page is printed, but the chunk was produced by Docling basic conversion and is explicitly marked `rough_ok`. The conversion preserves the main reading order, but French diacritics and several OCR spellings appear degraded or suspicious, including examples such as `Autriclie`, `Beiges`, `frangaise`, `d^sireux`, `d^velopper`, and `Sudde`. Proof review should compare the converted text with the page image before any source-context claim is promoted.

## Uncertainty

This packet should not be used for canonical person identity, relationship, or event claims. The list of governmental signatories is long and partly OCR-noisy, so normalized country names and office titles should wait for image-level QA or another authoritative treaty text. No genealogical lead is asserted in this chunk.

## Promotion Recommendation

`hold_for_conversion_qa`: the page supports treaty/source-context claims, but the source packet should remain in staging until the printed French text and party list are checked against the page image.

## Extracted Atomic Claims

| Claim | Status | Confidence | Staged file |
| --- | --- | ---: | --- |
| The page begins a presidential proclamation of the United States of America. | draft | 8.0 | `research/_staging/claims/claim-chunk-3f469b56e502-p0006-01-presidential-proclamation.md` |
| The page states that the Prisoners of War Convention was signed at Geneva on July 27, 1929 by the United States and forty-six other countries. | draft | 8.0 | `research/_staging/claims/claim-chunk-3f469b56e502-p0006-01-convention-signed-geneva.md` |
| The page identifies the French-language convention title as concerning treatment of prisoners of war, dated July 27, 1929. | draft | 7.5 | `research/_staging/claims/claim-chunk-3f469b56e502-p0006-01-french-convention-title.md` |
| The page states the convention's humanitarian purpose of mitigating the severities of war and improving the lot of prisoners of war. | draft | 7.0 | `research/_staging/claims/claim-chunk-3f469b56e502-p0006-01-humanitarian-purpose.md` |

## Relationship Evidence Candidates

No family relationship evidence is stated on this page. A negative relationship candidate note is staged separately.

## Identity And Conflict Candidates

No private-person identity candidate is stated. A conversion-QA conflict note is staged separately for OCR-degraded French names and state titles.
