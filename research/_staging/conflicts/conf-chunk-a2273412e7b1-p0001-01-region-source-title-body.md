---
type: conflict_candidate
status: draft
confidence: 7.0
source: "raw/converted/cad653020f-resoluci-n-283-ministeri-p0001-0001-resoluci-n-283-ministerio-de-vivienda-y-urbanismo-servicio-de-vivienda-y-urbanizaci-n-v-regi-n-de-valpara-so-january-15-2001-pages-1.codex.md"
source_path: "raw/sources/Resolución 283, Ministerio de Vivienda y Urbanismo; Servicio de Vivienda y Urbanización; V Región de Valparaíso, January 15, 2001.pdf"
source_packet: "research/_staging/source-packets/sp-chunk-a2273412e7b1-p0001-01-resolucion-283-expropriation-pulgar.md"
chunk: "raw/chunks/cad653020f-resoluci-n-283-ministeri-p0001-0001-resoluci-n-283-ministerio-de-vivienda-f9de686035/page-0001-chunk-01.md"
chunk_id: "CHUNK-a2273412e7b1-P0001-01"
page_reference: "page 1 of 1"
conversion_confidence: high
promotion_recommendation: do_not_promote
tags: [conflict-candidate, staging, region, conversion-qa]
---

# Conflict Candidate: Source Region Title Versus Body Text

## Candidate Result

The source file and converted title identify `V Región de Valparaíso`, but the transcribed notice body names `Serviu Región del Bío Bío`, Chiguayante, and a Director Serviu Región del Bío Bío. This is a source-identity or metadata conflict to verify during page reread; it is not a person-identity conflict by itself.

## Literal Support Reviewed

```text
MINISTERIO DE VIVIENDA Y URBANISMO; SERVICIO DE VIVIENDA Y
URBANIZACIÓN; V REGIÓN DE VALPARAÍSO
```

```text
Por resolución 283, 5 diciembre 2000, Serviu Región del Bío Bío ordenó
expropiación parcial inmueble ubicado en Línea Ferrea s/n° ... comuna Chiguayante
```

```text
Director Serviu Región del Bío Bío.
```

## Source Path

- Source path: `raw/sources/Resolución 283, Ministerio de Vivienda y Urbanismo; Servicio de Vivienda y Urbanización; V Región de Valparaíso, January 15, 2001.pdf`
- Converted file: `raw/converted/cad653020f-resoluci-n-283-ministeri-p0001-0001-resoluci-n-283-ministerio-de-vivienda-y-urbanismo-servicio-de-vivienda-y-urbanizaci-n-v-regi-n-de-valpara-so-january-15-2001-pages-1.codex.md`
- Chunk/page reference: `CHUNK-a2273412e7b1-P0001-01`, page 1 of 1

## Conversion Confidence And QA Concern

The conversion says the page is clear, but the controller requested `reread-page`. The region mismatch may come from source metadata, title capture, or document text and should be checked against the page image/PDF.

## Uncertainty

Uncertainty is about document/source identity metadata, not about the literal presence of the personal names in the converted text.

## Promotion Recommendation

Do not promote as a canonical conflict. Keep as a QA caution on related claims.
