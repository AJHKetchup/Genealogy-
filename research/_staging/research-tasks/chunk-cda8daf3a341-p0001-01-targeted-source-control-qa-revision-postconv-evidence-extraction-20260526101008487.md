---
type: research_task
status: draft
task_id: evidence-extraction:CHUNK-cda8daf3a341-P0001-01
worker: postconv-evidence-extraction-20260526101008487
source_packet: research/_staging/source-packets/chunk-cda8daf3a341-p0001-01-icrc-group-photo-dario-jose-pulgar-arriagada-revision-postconv-evidence-extraction-20260526101008487.md
source: raw/sources/Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives_files/V-P-HIST-03583-07A.JPG
converted_file: raw/converted/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a.codex.md
chunk: raw/chunks/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a-codex/page-0001-chunk-01.md
chunk_id: CHUNK-cda8daf3a341-P0001-01
page_reference: page 1
priority: high
literal_support: "The page consists of a single black and white photograph, occupying the entire page. There is no text or other content on the page.; identity_basis: none"
conversion_confidence: high for no-text conversion; low for named-person image identification and source-control readiness
conversion_qa_concern: The exact source image is absent at the assigned path, and direct page-image/extracted-image files are not available in the conversion job directory.
uncertainty: Verify whether the converted outdoor group photograph is the controlling image for source SHA-256 327c170fda815e9226dbef176e889611718d4ba89c088377a4092588778a6b9a and whether ICRC/archive metadata identifies Dario Jose Pulgar-Arriagada in it.
promotion_recommendation: hold_for_conversion_qa
---

# Research Task: Targeted Source-Control QA For ICRC Group Photograph

Complete targeted conversion/source-control QA before any Dario photograph claim is promoted.

## Required Checks

1. Restore or locate `raw/sources/Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives_files/V-P-HIST-03583-07A.JPG` with SHA-256 `327c170fda815e9226dbef176e889611718d4ba89c088377a4092588778a6b9a`.
2. Restore or locate reviewable conversion page imagery for the job `raw/codex-conversion-jobs/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a`.
3. Compare the assigned source image, converted Markdown, current chunk, and authoritative ICRC/archive metadata.
4. Decide whether the controlling image for this chunk is the outdoor group scene described in conversion.
5. If authoritative metadata identifies Dario Jose Pulgar-Arriagada, record whether it identifies him generally in the photograph or by a specific face/position.
6. Rerun proof review after QA; do not promote a depiction, event-presence, identity merge, or relationship claim before that review.
