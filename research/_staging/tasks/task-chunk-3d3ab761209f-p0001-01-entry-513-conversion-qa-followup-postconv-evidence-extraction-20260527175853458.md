---
type: research_task
status: open
task_id: conversion-qa-followup:CHUNK-3d3ab761209f-P0001-01-entry-513
created_by: postconv-evidence-extraction-20260527175853458
source_packet: "research/_staging/source-packets/chunk-3d3ab761209f-p0001-01-entry-513-pulgar-proof-review-revision-hold-postconv-evidence-extraction-20260527175853458.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
page_reference: "image page 1; register page 172; entries 513 and 515"
priority: high
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Follow-Up: Entry 513 Pulgar Row

## Task

Restore or locate the original PNG/page image and perform targeted row-level conversion QA for entry 513. Check entry 515 as row-control context to rule out lower-row spillover.

## Required QA Targets

- Entry 513 child surname and given-name lines.
- Entry 513 sex field.
- Entry 513 exact birth date and time.
- Entry 513 father/declarant wording, age, occupation, and domicile.
- Entry 513 mother surname and full name.
- Entry 515 child/father/mother fields and whether the lower row is complete enough for separate proof review.

## Blocker

This worker could not perform the image QA because neither `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png` nor `raw/codex-conversion-jobs/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513/page-images/page-0001.png` exists in the current checkout.

## Completion Criteria

After a QA-certified transcription exists, rerun proof review on the staged atomic identity, birth-event, registration-event, father/declarant, mother, and parent-child relationship drafts. Do not promote any canonical tree claims from the current held drafts.
