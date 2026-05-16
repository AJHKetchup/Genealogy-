---
type: source_prep_chunk
chunk_id: CHUNK-1b9c4f9af495-P0001-01
source_converted: raw/converted/cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959.codex.md
converted_sha256: 1b9c4f9af4950a42b4ec4e3968a086aaadb44542e3de2a888d88c79026826646
source: raw/sources/Arrival-Departure Record, Form I-94 B, March 30, 1959.png
source_sha256: db3e1a4b10817e6fda3e3ece8f55d0717d2806c802660cb9d3e4366affff6d1a
source_manifest: raw/codex-conversion-jobs/cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959/manifest.json
page_start: 1
page_end: 1
part: 1
---

# Arrival-Departure Record, Form I-94 B, March 30, 1959

## Conversion Metadata

- Source: `raw/sources/Arrival-Departure Record, Form I-94 B, March 30, 1959.png`
- Source SHA-256: `db3e1a4b10817e6fda3e3ece8f55d0717d2806c802660cb9d3e4366affff6d1a`
- Manifest: `raw/codex-conversion-jobs/cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959/manifest.json`
- Conversion method: Codex local vision workbench
- Extracted images: `raw/codex-conversion-jobs/cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959/extracted-images`

## Page Metadata
- Task id: `source-prep:cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959:p0001`
- Model route: `lite`
- Route reasons: simple_page
- Source: `raw/sources/Arrival-Departure Record, Form I-94 B, March 30, 1959.png`
- Page: 1

## Layout And Reading Order
The page is a form with several fields for personal information, travel details, and authorization. The reading order follows the standard top-to-bottom, left-to-right flow of form fields. There is also a vertical text block on the right side of the page.

## Literal Transcription
```
Surname Given Name Initial Passport Number
PULGAR DARIO A 258 142
Nationality (Citizenship) Birthplace Birthdate
CHILFAN CHILE 1 JUN 1942
United States Address
TRANSIT TO CHILE
Permanent Address
Box 1244 CONCEPCION CHILE CONTINUOUS TRANSIT
Visa Issued At
TRWIOV
Date Visa Issued
Vessel Name or Airline and Flight No. of Arrival
BOAC BA 549
Passenger Boarded At
LONDON ENGLAND
Form I-94 B (Rev. 7-1-57)
ARRIVAL-DEPARTURE RECORD
Authorised pursuant to agreement under
Sec. 238(d) of Immigration Act.
MAR 30 '59 NYC
Carrier directed to detain alien during
transit and remove from United States via
NY
(Departure Port)
(Carrier)
044 3/29/59 97
(Date) (Intl. [illegible])
ANY HANDWRITTEN ENTRIES MUST BE IN BLOCK CAPITALS.
```

## Images, Captions, And Visual Notes
- A stamp with "MAR 30 '59 NYC" is present in the middle right section of the form.
- A vertical text block on the right side reads "ANY HANDWRITTEN ENTRIES MUST BE IN BLOCK CAPITALS."

## Uncertain Or Illegible
- The last part of the "Permanent Address" field after "CONCEPCION" is partially obscured and difficult to read. It appears to be "CHILE CONTINUOUS TRANSIT".
- The "Visa Issued At" field contains handwritten text that is difficult to decipher. It appears to be "TRWIOV".
- The "Passport Number" field has a handwritten character after "258" that is unclear.
- The "Intl. [illegible]" field at the bottom right has illegible handwritten text.

## Completeness Audit
The page appears to be fully transcribed. All visible fields and handwritten entries have been captured.

## Visual Region Manifest
```json
{
  "visual_regions": [
    {
      "region_id": "0001",
      "kind": "stamp",
      "bbox_pct": [568, 568, 709, 604],
      "caption_literal": "MAR 30 '59 NYC",
      "caption_type": "source-caption",
      "identity_basis": "source-text",
      "source_context": "Form I-94 B (Rev. 7-1-57) ARRIVAL-DEPARTURE RECORD",
      "confidence": 0.9,
      "suggested_filename": "0001-stamp-MAR-30-59-NYC.png",
      "inline_anchor": "MAR 30 '59 NYC"
    },
    {
      "region_id": "0002",
      "kind": "text_block",
      "bbox_pct": [678, 399, 739, 734],
      "caption_literal": "ANY HANDWRITTEN ENTRIES MUST BE IN BLOCK CAPITALS.",
      "caption_type": "source-caption",
      "identity_basis": "source-text",
      "source_context": "Form I-94 B (Rev. 7-1-57) ARRIVAL-DEPARTURE RECORD",
      "confidence": 0.95,
      "suggested_filename": "0002-text-block-ANY-HANDWRITTEN-ENTRIES-MUST-BE-IN-BLOCK-CAPITALS.png",
      "inline_anchor": "ANY HANDWRITTEN ENTRIES MUST BE IN BLOCK CAPITALS."
    }
  ],
  "no_visual_regions_reason": null
}
```
