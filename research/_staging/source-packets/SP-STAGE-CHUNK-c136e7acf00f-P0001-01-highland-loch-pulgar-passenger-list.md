---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-c136e7acf00f-P0001-01
worker: postconv-evidence-extraction-20260522115346320
source_id: cadfbbb3a3-passenger-list-pacific-steam-navigation-co-official-number-143667-1928-07-08
title: "Pacific Steam Navigation Company passenger list, Highland Loch, arrival Plymouth, 6 July 1928"
source_path: "raw/sources/Passenger List, Pacific Steam Navigation Co., Official Number 143667, 8th July 1928..png"
source_sha256: "dfbbb3a344f111dd42d0974b6dce8f322118920f3254e0e0f809c9795804ab42"
converted_file: "raw/converted/cadfbbb3a3-passenger-list-pacific-s-passenger-list-pacific-steam-navigation-co-official-number-143667-8th-july-1928.codex.md"
chunk: "raw/chunks/cadfbbb3a3-passenger-list-pacific-s-passenger-list-pacific-steam-navigation-co-offici-bf75a09294/page-0001-chunk-01.md"
chunk_id: "CHUNK-c136e7acf00f-P0001-01"
chunk_manifest: "raw/chunks/cadfbbb3a3-passenger-list-pacific-s-passenger-list-pacific-steam-navigation-co-offici-bf75a09294/manifest.json"
page_reference: "page 1; right page P.M. 26; alien passenger rows 55-56 and 65"
record_type: passenger_list
ship: "HIGHLAND LOCH"
steamship_line: "PACIFIC STEAM NAVIGATION COMPANY"
arrival_date: "1928-07-06"
arrival_port: "Plymouth"
whence_arrived: "Talcahuano, Chile"
family_relevance: critical
matched_terms: ["Dario", "Luis", "Pulgar"]
conversion_confidence: "medium from converted text; source image unavailable locally for required reread"
conversion_qa_concern: "Controller requested reread-page; original PNG path was not present during extraction."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Draft: Highland Loch Passenger List, Pulgar Rows

## Source Reference

- Source path: `raw/sources/Passenger List, Pacific Steam Navigation Co., Official Number 143667, 8th July 1928..png`
- Source SHA-256: `dfbbb3a344f111dd42d0974b6dce8f322118920f3254e0e0f809c9795804ab42`
- Converted file: `raw/converted/cadfbbb3a3-passenger-list-pacific-s-passenger-list-pacific-steam-navigation-co-official-number-143667-8th-july-1928.codex.md`
- Chunk/page reference: `raw/chunks/cadfbbb3a3-passenger-list-pacific-s-passenger-list-pacific-steam-navigation-co-offici-bf75a09294/page-0001-chunk-01.md`, `CHUNK-c136e7acf00f-P0001-01`, page 1
- Chunk manifest: `raw/chunks/cadfbbb3a3-passenger-list-pacific-s-passenger-list-pacific-steam-navigation-co-offici-bf75a09294/manifest.json`

## Source Description

The converted page is a two-page passenger-list spread. The right page is `P.M. 26`, headed `PACIFIC STEAM NAVIGATION COMPANY` and `NAMES AND DESCRIPTIONS OF ALIEN PASSENGERS`, with date of arrival `6th July 1928`, port of arrival `PLYMOUTH`, and whence arrived `TALCAHUANO CHILE`. The left page certification identifies the ship as `HIGHLAND LOCH` and is dated at Liverpool on `12th JULY 1928`.

## Literal Support

```text
Date of Arrival | 6th July 1928
Port of Arrival | PLYMOUTH
Whence Arrived | TALCAHUANO CHILE
PACIFIC STEAM NAVIGATION COMPANY
NAMES AND DESCRIPTIONS OF ALIEN PASSENGERS.
```

Relevant converted rows:

```text
| 55 | Valparaiso | " | Dario Pulgar A. | c/o Anglo South American Bank Ltd. London | 1 | Medical Surgeon | 39 | | | | | | Chile | Chile | | | | | | | France [handwritten diamond symbol] |
| 56 | " | " | Dorothy Pulgar | do | 1 | -- | | 25 | | | | | do | do | | | | | | | do |
| 65 | Mollendo | " | Luis Lopez de Romana | London E.C. 2. | 1 | Mining Engineer | 25 | | | | | | Peru | Peru | | | | | | | " |
```

## Conversion Confidence And QA Concern

Conversion confidence is medium for extracting draft facts from the converted table, but not high enough for promotion. The controller flagged this chunk for `reread-page`, and the original PNG was not present at the task's `source_path` when checked during extraction.

## Uncertainty

The row-level facts depend on column alignment and ditto marks in a dense table. Dorothy Pulgar's citizenship, last residence, and intended future residence use `do` marks, apparently repeating Dario Pulgar A.'s `Chile`, `Chile`, and `France`, but those should be verified against the image. The document does not state a relationship between Dario Pulgar A. and Dorothy Pulgar. `Luis Lopez de Romana` matches the given family term `Luis`, but this page alone does not connect him to the Pulgar family.

## Promotion Recommendation

`hold_for_conversion_qa`: family-relevant rows are present, but page-image reread is required before proof review or canonical promotion.
