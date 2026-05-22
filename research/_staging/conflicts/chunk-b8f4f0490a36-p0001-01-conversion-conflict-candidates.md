---
type: conflict_candidate
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-jose-del-carmen-segundo-pulgar-arriagada.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
confidence: medium
promotion_recommendation: hold_for_conversion_qa
---

# Conversion And Identity Conflict Candidates

## Reread-page QA Flag

- Literal support reviewed: entry 172 full row.
- Conversion confidence/QA concern: converted file says no uncertain or illegible portions, but controller priority includes `qc:reread-page`.
- Uncertainty: This is a workflow conflict rather than a textual contradiction. Promote facts only after proof review against the image.
- Promotion recommendation: hold_for_conversion_qa for resolving the QA flag itself.

## Father Name Abbreviation

- Literal support: `**Nombre del padre** Jose del Carmen Pulgar S.`
- Conversion confidence/QA concern: high transcription confidence, but `S.` is an abbreviation or initial that should not be expanded from this record alone.
- Uncertainty: Moderate for matching to any fuller canonical identity.
- Promotion recommendation: hold_for_conversion_qa for identity merge decisions; use literal name in staged claims.

## Source Path Encoding Variant

- Literal support: task JSON source path contains mojibake while the chunk frontmatter and manifest contain `Circunscripción de Los Ángeles`.
- Conversion confidence/QA concern: source identity appears stable by SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`.
- Uncertainty: Low for source identity; preserve SHA-256 and normalized path in staged drafts.
- Promotion recommendation: do_not_promote as a genealogical conflict; keep as administrative QA note.
