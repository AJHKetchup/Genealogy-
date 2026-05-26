---
type: research_task
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: "05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md"
chunk_id: "CHUNK-bdb698de8106-P0001-01"
source_packet: "research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md"
page_reference: "image page 1; register page 172; entries 513-515"
priority: high
family_relevance: high
matched_family_terms: ["Pulgar"]
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Follow-Up: CHUNK-bdb698de8106-P0001-01

## Task

Run targeted conversion QA against the source image, converted Markdown, chunk Markdown, and staged source packet for register page 172. This follow-up supersedes any older page-172 task that used a different chunk id/path for this same image.

## Family-Relevant Scope

Entry 513 is the family-relevant row because the father/declarant field visibly supports a `Pulgar` reading and the converted transcript names `José del Carmen Pulgar` / `José del C. Pulgar`. Keep the row staged, but do not promote any child, parent, declarant, or relationship claim until the row-level transcription conflicts are resolved.

## Literal Support And Known Conflicts

- Current converted/chunk transcript for entry 513 reads child `Isolina del Carmen José`, sex `Masculino`, father `José del Carmen Pulgar`, mother `Juana de Dios Amador de Pulgar`, and declarant `José del C. Pulgar`, father, age forty-seven, agriculturist, domiciled Calle Colon.
- Direct image reread supports the page as register page 172 in the Los Anjeles/La Laja birth register and supports a Pulgar father/declarant field for entry 513, but the visible child-name field appears closer to a Pulgar-surname line with unresolved given-name lines than to `Isolina del Carmen José`.
- The entry 513 mother surname remains image-sensitive. It appears closer to an `Arriagada`/`Amagada`-style reading than to converted `Amador`, but this task does not replace the transcription from inference.
- Entry 514 and entry 515 retain derivative-vs-image conflicts noted in the staged packet. They should be reconciled only as row-control/context needed for this page, not promoted as generic non-family claims.

## Acceptance Criteria

- Confirm or correct entry 513 child full name, sex, birth date/time, father/declarant form, father age/profession/residence, and mother full name.
- Confirm whether entry 513 mother surname should be transcribed as `Amador`, `Amagada`, `Arriagada`, or an explicitly uncertain form.
- Confirm whether entry 513 child name should preserve a visible `Pulgar` surname line, and record all unresolved words with `[?]` rather than silently normalizing.
- Reconcile entry 514 father field and entry 515 child/father/declarant surname only enough to prevent row spillover into entry 513 evidence.
- After corrected conversion QA, rerun proof review on each atomic claim and the child-parent relationship before any canonical promotion.

## Promotion Recommendation

`hold_for_conversion_qa`. The Pulgar evidence is family-relevant, but the current derivative transcript and image-reviewed evidence disagree on fields that control identity and relationship promotion.
