---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-f128f4a0ac0d-P0001-01
worker: postconv-evidence-extraction-20260524140153089
source_id: cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959
title: "Arrival-Departure Record, Form I-94 B, Dario A. Pulgar, 30 March 1959"
source_path: "raw/sources/Arrival-Departure Record, Form I-94 B, March 30, 1959.png"
source_sha256: "db3e1a4b10817e6fda3e3ece8f55d0717d2806c802660cb9d3e4366affff6d1a"
converted_file: "raw/converted/cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959.codex.md"
chunk: "raw/chunks/cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-f128f4a0ac0d-P0001-01"
chunk_manifest: "raw/chunks/cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959-codex/manifest.json"
page_reference: "page 1"
record_type: "arrival_departure_record_form_i_94_b"
record_date: "1959-03-30"
family_relevance: high
matched_terms: ["Dario", "Pulgar"]
conversion_confidence: "medium-high from converted chunk for name, birthdate, address, and carrier fields"
conversion_qa_concern: "Original PNG path named in the task was not present locally during extraction; several converted fields are explicitly uncertain, including nationality text, passport suffix, initial, and visa-issued-at."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Draft: Dario A. Pulgar I-94 Transit Record

## Source Reference

- Source path: `raw/sources/Arrival-Departure Record, Form I-94 B, March 30, 1959.png`
- Source SHA-256: `db3e1a4b10817e6fda3e3ece8f55d0717d2806c802660cb9d3e4366affff6d1a`
- Converted file: `raw/converted/cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959.codex.md`
- Chunk/page reference: `raw/chunks/cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959-codex/page-0001-chunk-01.md`, `CHUNK-f128f4a0ac0d-P0001-01`, page 1
- Chunk manifest: `raw/chunks/cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959-codex/manifest.json`

## Source Description

The converted page is an Arrival-Departure Record, Form I-94 B, for `DARIO A PULGAR`. It records a continuous transit through New York on 30 March 1959, with boarding at London, England, and a stated destination/address context in Chile.

## Literal Support

```text
Surname
PULGAR
Given Name
DARIO
Initial
A
Birthplace
CHILE
Birthdate
1 JUN 1942
United States Address
TRANSIT TO CHILE
Permanent Address
Box 1244 CONCEPCION CHILE
CONTINUOUS TRANSIT
MAR 30 '59 NYC
Vessel Name or Airline and Flight No. of Arrival
BOAC BA 549
Passenger Boarded At
LONDON ENGLAND
KLM 492 NY
3/30/59
```

## Conversion Confidence And QA Concern

Conversion confidence is medium-high for the main person-first facts above because the converted chunk gives clear field labels and entries. The original PNG named by the task was not present at extraction time, so these drafts should remain staged until source image QA. The converted note flags uncertainty for the `Initial`, passport number suffix, `Visa Issued At`, and some handwritten entries. The nationality field is converted as `CHILFAN`, probably intended to be `CHILEAN`, but that requires image review before promotion.

## Uncertainty

The record identifies a source person as `DARIO A PULGAR`; it does not state the expanded middle name, parents, spouse, child, or other family relationship. The source may be relevant to the known family member Dario Arturo Pulgar-Smith because of the Dario/Pulgar name form and middle initial `A`, but identity attachment should be reviewed before canonical promotion.

## Promotion Recommendation

`hold_for_conversion_qa`: the converted record contains strong family-relevant travel and identity evidence, but the source image is absent locally and several fields need proof review.
