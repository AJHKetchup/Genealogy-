---
type: research_task
status: draft
task_id: evidence-extraction:CHUNK-cda8daf3a341-P0001-01
worker: postconv-evidence-extraction-20260526100318514
source_packet: research/_staging/source-packets/chunk-cda8daf3a341-p0001-01-icrc-group-photo-dario-jose-pulgar-arriagada-revision-postconv-evidence-extraction-20260526100318514.md
source: raw/sources/Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives_files/V-P-HIST-03583-07A.JPG
converted_file: raw/converted/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a.codex.md
chunk: raw/chunks/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a-codex/page-0001-chunk-01.md
chunk_id: CHUNK-cda8daf3a341-P0001-01
page_reference: page 1
priority: high
literal_support: "The page consists of a single black and white photograph, occupying the entire page. There is no text or other content on the page.; identity_basis: none"
conversion_confidence: high for the no-text conversion; low for named-person image identification and source-control readiness
conversion_qa_concern: Exact source path and conversion page image are missing; a related same-folder image is nonmatching by hash and apparent content.
uncertainty: Verify whether the converted outdoor group photograph, the missing source hash, and the same-folder indoor assembly JPG are separate archival images, renamed files, or a source-preparation mismatch.
promotion_recommendation: hold_for_conversion_qa
---

# Research Task: Targeted Source-Control QA For ICRC Photograph

Complete targeted conversion/source-control QA before any Dario photograph claim is promoted.

## Required Checks

1. Restore or locate `raw/sources/Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives_files/V-P-HIST-03583-07A.JPG` with SHA-256 `327c170fda815e9226dbef176e889611718d4ba89c088377a4092588778a6b9a`.
2. Restore or locate `raw/codex-conversion-jobs/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a/page-images/page-0001.jpg` and the extracted visual crop referenced by the converted Markdown.
3. Compare the assigned source image, converted Markdown, current chunk, and any same-folder related JPGs.
4. Decide whether the controlling image for this chunk is the converted outdoor group scene or another Geneva Convention photograph.
5. If authoritative metadata identifies Dario Jose Pulgar-Arriagada, record whether it identifies him generally in the photograph or specifically by seat/table/position.
6. Rerun proof review after QA; do not promote a depiction, person merge, or relationship claim before that review.
