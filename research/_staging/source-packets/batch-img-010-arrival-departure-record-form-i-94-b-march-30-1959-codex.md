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
conversion_confidence: medium
qa_review:
  triage: research/_conversion-review/triage/2026-05-14-dario-pulgar-conversion-qa.md
  corrections: research/_conversion-review/corrections/2026-05-14-dario-pulgar-conversion-corrections.md
  page_queue: research/_conversion-review/page-queues/2026-05-14-dario-pulgar-reread-queue.md
  qa_status: reread-region
promotion_recommendation: hold
tags: [staging, source-packet, immigration, transit, pulgar, dario]
---

# Staged Source Packet

## Source Identity

- Source path: `raw/codex-conversion-jobs/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959/source/Arrival-Departure Record, Form I-94 B, March 30, 1959.png`
- Converted file: `raw/converted/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959.codex.md`
- Chunk manifest: `raw/chunks/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex/manifest.json`
- Chunk/page reference: `CHUNK-2080170a5175-P0001-01`, page 1.
- QA triage: dated review on 2026-05-14 queued a targeted reread of the identity block and travel/visa block before promotion.

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

This record strongly supports a transit arrival for Dario A. Pulgar in New York City on March 30, 1959 after boarding BOAC flight BA 549 in London. The dated QA pass, however, explicitly warns against identity drift with the existing `Dario Pulgar Smith` context and asks for a reread of the birthdate, address, visa-place, and adjacent handwritten notes before promotion.

## Uncertainty Notes

- `Birthdate: 1 Jun. 1902[?]` is under explicit reread.
- `Concepcion[?]` is likely the permanent-address city but remains under explicit reread.
- `RIO[?]` as visa-issue place is plausible but still queued for confirmation.
- The small notation near the passport number and the lower-right route/detention notation are not reliable enough for claim staging.
- Do not merge this traveler with `Dario Pulgar Smith` without separate identity review.

## Candidate Entities And Claims

- Person candidate: Dario A. Pulgar.
- Place candidate: Concepcion, Chile.
- Event candidate: New York City transit arrival on 30 March 1959.
- Claim draft: `research/_staging/claims/batch-img-010-dario-a-pulgar-nyc-transit-1959-03-30.md`
- Claim draft: `research/_staging/claims/batch-img-010-dario-a-pulgar-recorded-birthdate-1902-06-01.md`
- Claim draft: `research/_staging/claims/batch-img-010-dario-a-pulgar-permanent-address-concepcion.md`

## Proposed Claim Status And Confidence

- Transit event claim: `probable`, confidence 7.8/10.
- Recorded birthdate claim: `possible`, confidence 5.8/10.
- Permanent address claim: `possible`, confidence 5.7/10.

## Follow-Up Tasks

- Perform the queued local reread of the birthdate, permanent-address city, visa-place field, and adjacent handwritten notations.
- Compare this traveler against `batch-pdf-022` and other Pulgar travel records before any identity merge.

## Promotion Recommendation

`hold` until the dated reread queue for the I-94 is cleared.