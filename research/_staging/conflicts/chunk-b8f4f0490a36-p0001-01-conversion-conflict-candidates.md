---
type: conflict_candidate
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-jose-del-carmen-segundo-pulgar-arriagada.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
confidence: high
promotion_recommendation: hold_for_conversion_qa
---

# Conversion And Identity Conflict Candidates

## Reread-page QA Flag

- Literal support reviewed: entry 172 full row.
- Conversion confidence/QA concern: earlier staged notes report that the original image was located and reread on 2026-05-22, supporting the Pulgar/Arriagada row. This 2026-05-23 worker could not locate the source image or manifest page image for direct verification. The assigned chunk supports the Pulgar/Arriagada row, but the converted Markdown file's entry 172 is an unrelated Jose Miguel / Oswaldo Bunster / Amelia de la Maza row. Father-name suffix remains a textual QA issue within the Pulgar/Arriagada row.
- Uncertainty: Image support is inherited from earlier reread notes rather than freshly verified in this pass. Converted-file mismatch and father-name suffix still need conversion QA.
- Promotion recommendation: hold_for_conversion_qa for father-name identity decisions.

## Father Name Suffix Disagreement

- Literal support: assigned chunk states `**Nombre del padre** Jose del Carmen Pulgar S.`; image reread supports `Jose del Carmen Pulgar` and does not show a clearly visible final `S.` suffix.
- Conversion confidence/QA concern: textual contradiction between the assigned chunk and image-reviewed evidence.
- Uncertainty: Moderate for the exact father name and any canonical identity merge.
- Promotion recommendation: hold_for_conversion_qa for father-name claims and parent relationship candidates until conversion QA reconciles the suffix.

## Converted File Entry 172 Mismatch

- Literal support: converted Markdown file entry 172 states `**Nombres.** José Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`; assigned chunk and earlier image-reread notes show entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`/`Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.
- Conversion confidence/QA concern: material mismatch between the converted Markdown file and both the assigned chunk and source image for the same entry number.
- Uncertainty: High for using the converted Markdown file as support for this task; low for the assigned chunk reading, but high for promotion readiness because this worker could not inspect the source image directly.
- Promotion recommendation: hold_for_conversion_qa for any draft that depends on the converted Markdown text itself; image-supported child, mother, and event facts may proceed only with explicit proof review awareness of this mismatch.

## Source Path Encoding Variant

- Literal support: task JSON source path contains mojibake while the chunk frontmatter and manifest contain `Circunscripción de Los Ángeles`.
- Conversion confidence/QA concern: source identity appears stable by SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`.
- Uncertainty: Low for source identity; preserve SHA-256 and normalized path in staged drafts.
- Promotion recommendation: do_not_promote as a genealogical conflict; keep as administrative QA note.
