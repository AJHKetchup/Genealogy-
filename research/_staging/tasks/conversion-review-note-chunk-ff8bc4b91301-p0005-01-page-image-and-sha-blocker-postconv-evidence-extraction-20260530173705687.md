---
type: research_task
status: draft
task_type: conversion_qa_followup
task_id: "evidence-extraction:CHUNK-ff8bc4b91301-P0005-01"
worker: "postconv-evidence-extraction-20260530173705687"
subject: "Habitat Revisited page 5 Pulgar line"
source_packet: "research/_staging/source-packets/chunk-ff8bc4b91301-p0005-01-habitat-revisited-pulgar-vancouver-hold-postconv-evidence-extraction-20260530173705687.md"
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/page-0005-chunk-01.md"
chunk_id: "CHUNK-ff8bc4b91301-P0005-01"
page_reference: "page 5"
priority: high
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Follow-Up: Habitat Revisited Page 5

The staged source packet and claim for page-5 `Pulgar` must remain out of canonical folders.

## Blockers

- `page-0005.jpg` was not present at `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0005.jpg`.
- The chunk records converted SHA-256 `ff8bc4b9130169ba6f4ecc103ba089ba6bf26c7162f5dfebbf3bae9ebd3a7271`, but the live converted file read during this extraction hashed to `97c8a1cbf4db9e4e39f2044e3260d5938381e2a89583f8e49e6777c77d13444c`.
- The manifest records page-5 chunk SHA-256 `78154f079280b003dbe9fc57c0427a7cb0b00df991dc9c77fd098328072a8584`, but the live chunk file read during this extraction hashed to `0c06f927fe30653e7aba9f1a8dc3f2c491b6669abacb42caa3f9c9db76b6504c`.
- Page 5 was not visually proofread during this extraction.

## Required Follow-Up

Restore or locate the page-5 image, reconcile the converted Markdown and chunk hash mismatches, and visually proof the `Pulgar` line. After that, run a focused same-source identity bridge review comparing verified page-5 `Pulgar` with verified Habitat references to `Dario Pulgar` on pages 2, 7, and 8. Do not compare this held page-5 claim to CV or canonical Pulgar-Smith evidence until the same-source bridge is complete.
