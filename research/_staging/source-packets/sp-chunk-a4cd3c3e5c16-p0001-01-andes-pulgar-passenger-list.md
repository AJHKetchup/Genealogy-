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

Conversion confidence is mixed. Prior staged proof reviews report visible-image confirmation for the narrow child-row fields: child row name by ditto, age `11`, occupation `Student`, the `+` mark in the England subcolumn, and ditto marks in columns 9 and 10 following `Chile`. In this revision pass, however, the source image named by the manifest is not present at `raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png`, and the rendered page image named by the conversion manifest is not present under `raw/codex-conversion-jobs/.../page-images/page-0001.png`.

The child row's column 6 last-address cell remains a QA concern. The conversion renders a ditto mark for the child Dario address, but the proof-review revision notes state that image-reviewed evidence did not make that mark sufficiently clear for a promotable address claim. Preserve this disagreement instead of silently normalizing the child address to the adult Pulgar address.

## Uncertainty

Do not infer canonical relationships from this passenger list alone. The adult rows use the age columns for passengers accompanied by a husband or wife, and the three Pulgar rows are consecutive with ditto marks, but the document does not explicitly label Dorothy as Dario's wife or the younger Dario as their child. The handwritten red annotations beside adult ages also should not be treated as vital facts without separate interpretation.

## Promotion Recommendation

`hold_for_conversion_qa` for the source packet until the missing source/page image is restored or regenerated through the normal conversion QA workflow. Promote individual child-row claims selectively only where separate proof review has already confirmed the visible field and preserved scope: age, student occupation, England last-permanent-residence mark, and Chile ditto-mark fields. The child last-UK-address reading should remain held for targeted conversion QA.
