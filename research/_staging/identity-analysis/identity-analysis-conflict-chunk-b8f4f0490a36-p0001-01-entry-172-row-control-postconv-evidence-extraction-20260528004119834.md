---
type: identity_conflict_candidate
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528004119834"
subject: "Entry 172 row-control conflict"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528004119834.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
confidence: 0.86
conversion_confidence: "image_reviewed_row_control_with_converted_markdown_conflict"
conversion_qa_concern: "Image and assigned chunk support Pulgar/Arriagada for physical row 172; current converted Markdown supports Burgos/de la Cruz for entry 172."
uncertainty: "This is a derivative-transcript conflict, not evidence that the Pulgar/Arriagada child and Burgos/de la Cruz child are the same person."
promotion_recommendation: "promote_after_review"
created: "2026-05-28"
---

# Identity/Conversion Conflict: Entry 172

## Conflict

The original image and assigned chunk identify physical row `172` as the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

The current converted Markdown identifies entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.

## Interpretation

Treat this as a row-control or derivative-transcript conflict. Do not merge the Pulgar/Arriagada child with the Burgos/de la Cruz child, and do not treat the converted Markdown as controlling for this entry unless later correction supersedes it.

## Literal Support

Assigned chunk:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. ... **Nombre de la madre** Juana Arriagada de Pulgar ...
```

Converted Markdown conflict:

```text
Entry 172 ... Nombres. José Miguel ... Nombre del padre: Oswaldo Burgos ... Nombre de la madre: Concepcion de la Cruz
```
