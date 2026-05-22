---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-a4cd3c3e5c16-P0001-01
source_id: ca5a5078ab-passenger-list-royal-mail-lines-limited-august-7-1953
title: "Royal Mail Lines passenger list, Andes, Southampton to South America, 7 August 1953"
source_path: "raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png"
source_sha256: "5a5078ab4b0d50fdd2cdefb4aa21ffaf6524824329254788ab4437bff500c6d3"
converted_file: "raw/converted/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953.codex.md"
chunk: "raw/chunks/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-a4cd3c3e5c16-P0001-01"
chunk_manifest: "raw/chunks/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953-codex/manifest.json"
page_reference: "image page 1; passenger list page P.M. 25; Pulgar rows"
record_type: passenger_list
ship: "ANDES"
steamship_line: "ROYAL MAIL LINES, LIMITED."
departure_date: "1953-08-07"
departure_port: "Southampton"
destination_region: "South America"
family_relevance: critical
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Draft: Andes Passenger List, Pulgar Rows

## Source Reference

- Source path: `raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png`
- Source SHA-256: `5a5078ab4b0d50fdd2cdefb4aa21ffaf6524824329254788ab4437bff500c6d3`
- Converted file: `raw/converted/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953.codex.md`
- Chunk/page reference: `raw/chunks/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953-codex/page-0001-chunk-01.md`, `CHUNK-a4cd3c3e5c16-P0001-01`, page 1
- Chunk manifest: `raw/chunks/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953-codex/manifest.json`

## Source Description

Passenger list for alien passengers embarked at Southampton on Royal Mail Lines ship `ANDES`, departing `7th. August 1953` and bound for `SOUTH AMERICA`. The page includes consecutive rows for `PULGAR Dario`, `" Dorothy`, and `" Dario`, contracted to land at Buenos Aires.

## Literal Support

```text
Name of Ship "ANDES"
Steamship Line ROYAL MAIL LINES, LIMITED.
Date of Departure 7th. August 1953.
Where Bound SOUTH AMERICA.
NAMES AND DESCRIPTION OF ALIEN PASSENGERS EMBARKED AT THE PORT OF SOUTHAMPTON.
```

Pulgar rows in the converted table:

```text
| | " | PULGAR Dario | " | 64 `92` | | | | | | | | Bedford Corner Hotel, London. | Medical | + | | | | | | | Chile | Chile |
| | " | " Dorothy | " | | 49 `92` | | | | | | | " | - | + | | | | | | | " | " |
| | " | " Dario | " | | | | | 11 | | | | " | Student | + | | | | | | | " | " |
```

The table header identifies the repeated ditto in column 2 as port contracted to land, column 4 as class, column 6 as last United Kingdom address, column 8 as country of last permanent residence, column 9 as country of intended future permanent residence, and column 10 as citizenship or subject country.

## Conversion Confidence And QA Concern

Conversion confidence is low for promotion because the controller flagged `qc:reread-page`, and the conversion-review triage lists page 1 as critical relevance with low confidence and action `reread-page`. I attempted local image review, but the task's source path is not present in `raw/sources`, so the Pulgar rows could not be verified against the original image in this extraction pass.

## Uncertainty

Do not infer canonical relationships from this passenger list alone. The adult rows use the age columns for passengers accompanied by a husband or wife, and the three Pulgar rows are consecutive with ditto marks, but the document does not explicitly label Dorothy as Dario's wife or the younger Dario as their child. The handwritten red annotations beside adult ages also need page-image review before any interpretation.

## Promotion Recommendation

`hold_for_conversion_qa`: the Pulgar facts are family-relevant and structured, but should not flow to the tree until the missing source image is restored or located and the page is reread.
