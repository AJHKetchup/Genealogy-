---
type: research_task
status: draft
task_id: evidence-extraction:CHUNK-5f493562b763-P0001-01
subject: "Dario A. Pulgar"
source: "raw/sources/Arrival-Departure Record, Form I-94 B, March 30, 1959.png"
converted_file: "raw/converted/cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959.codex.md"
chunk: "raw/chunks/cadb3e1a4b-arrival-departure-record-arrival-departure-record-form-i-94-b-march-30-1959-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-5f493562b763-P0001-01"
page_reference: "page 1"
priority: high
promotion_recommendation: hold_for_conversion_qa
---

# Source Image And Field QA: Dario A. Pulgar I-94

## Task

Locate or restore the original PNG named by the source and proof the converted fields before promoting claims from this record.

## Literal Support And Known QA Points

- Converted name fields: `PULGAR`, `DARIO`, initial `A`.
- Converted birth fields: `CHILE`, `1 JUN 1942`.
- Converted address fields: `TRANSIT TO CHILE`; `Box 1244 CONCEPCION CHILE`.
- Converted travel fields: `BOAC BA 549`; `LONDON ENGLAND`; `MAR 30 '59 NYC`; `KLM 492 NY`; `3/31/59`.
- The source path `raw/sources/Arrival-Departure Record, Form I-94 B, March 30, 1959.png` was not present locally during this extraction.
- The chunk uncertainty section flags nationality, visa-issued-at, permanent-address overlay text, passport suffix, and bottom date/officer entries for review.

## Acceptance Criteria

- Confirm whether `Nationality (Citizenship)` reads `CHILEAN` or another value; converted text currently says `CHILFAN`.
- Confirm the initial `A` and whether it should be treated as a middle initial for identity review.
- Confirm the full passport number if it is needed for identity work; converted text clearly has `258` followed by an uncertain suffix.
- Confirm the travel fields `BOAC BA 549`, `LONDON ENGLAND`, `MAR 30 '59 NYC`, `KLM 492 NY`, and `3/31/59`.
- Compare the record with established evidence before canonical person attachment.

## Promotion Recommendation

`hold_for_conversion_qa` until the original image is available and the uncertain fields are proofed.
