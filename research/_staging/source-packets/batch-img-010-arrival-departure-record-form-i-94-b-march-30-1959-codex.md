---
type: staged_source_packet
status: draft
source_path: raw/codex-conversion-jobs/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959/source/Arrival-Departure Record, Form I-94 B, March 30, 1959.png
converted_file: raw/converted/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959.codex.md
chunk_manifest: raw/chunks/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex/manifest.json
chunk_refs:
  - CHUNK-2080170a5175-P0001-01
page_refs:
  - Page 1
source_reliability_class: original government transit form
source_reliability_score: 8
source_reliability_rationale: Original immigration record with official arrival stamp; travel details are strong, while some identity fields are self-reported and partly hard to read.
evidence_type: direct evidence of transit travel; source-stated evidence of birth date, nationality, and address
informant_proximity: Self-reported identity/travel details recorded on an official form.
conversion_confidence: high
qa_review:
  triage: research/_conversion-review/triage/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex.md
  page_queue: research/_conversion-review/page-queues/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex.md
  qa_status: pass
promotion_recommendation: revise
tags: [staging, source-packet, immigration, transit, pulgar, dario]
---

# Staged Source Packet

## Source Identity

- Source path: `raw/codex-conversion-jobs/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959/source/Arrival-Departure Record, Form I-94 B, March 30, 1959.png`
- Converted file: `raw/converted/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959.codex.md`
- Chunk manifest: `raw/chunks/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex/manifest.json`
- Chunk/page reference: `CHUNK-2080170a5175-P0001-01`, page 1.
- QA triage: pass with family-term matches `Dario` and `Pulgar`; no reread queue was opened.

## Source Reliability

- Reliability class: original government transit form.
- Reliability score: 8/10.
- Evidence type: direct evidence of the March 30, 1959 transit event; source-stated evidence of nationality, birth date, and permanent address.
- Informant proximity: likely self-reported identity and routing information captured on an official form.

## Literal Source Support

```text
Surname: PULGAR
Given Name: DARIO
Initial: A
Nationality (Citizenship): CHILEAN
Birthplace: CHILE
Birthdate: 1 Jun. 1902[?]
United States Address: TRANSIT TO CHILE
Permanent Address:
Box 1244 Concepcion[?] Chile
Visa Issued At:
RIO[?]
Vessel Name or Airline and Flight No. of Arrival:
BOAC BA 549
Passenger Boarded At:
London England
[stamp]
MAR 30 '59 N Y C
```

## Translation

Not applicable; the source is already in English.

## Interpretation

This record strongly supports a transit arrival for Dario A. Pulgar in New York City on March 30, 1959 after boarding BOAC flight BA 549 in London. It also offers a candidate birth date and Chilean permanent address, but those two fields should be corroborated against cleaner sources because the handwritten readings are less certain than the travel fields and official stamp.

## Uncertainty Notes

- `Birthdate: 1 Jun. 1902[?]` is legible but not perfectly clean in the final digits.
- `Concepcion[?]` is likely the permanent-address city but should be checked against another source.
- `RIO[?]` as visa-issue place is plausible but not fully certain.
- The small notation near the passport number and the carrier route notation are not reliable enough for claim staging.

## Candidate Entities And Claims

- Person candidate: Dario A. Pulgar.
- Place candidate: Concepcion, Chile.
- Event candidate: New York City transit arrival on 30 March 1959.
- Claim draft: `research/_staging/claims/batch-img-010-dario-a-pulgar-nyc-transit-1959-03-30.md`
- Claim draft: `research/_staging/claims/batch-img-010-dario-a-pulgar-recorded-birthdate-1902-06-01.md`
- Claim draft: `research/_staging/claims/batch-img-010-dario-a-pulgar-permanent-address-concepcion.md`

## Proposed Claim Status And Confidence

- Transit event claim: `probable`, confidence 8.2/10.
- Recorded birthdate claim: `possible`, confidence 6.1/10.
- Permanent address claim: `possible`, confidence 6.0/10.

## Follow-Up Tasks

- Check the Dario Arturo Pulgar CV and nearby travel records for a cleaner birth date.
- Compare the address field with other Pulgar travel/passport materials to confirm `Concepcion` and the box number.

## Promotion Recommendation

`revise` for identity and address details; the travel event itself looks review-ready.