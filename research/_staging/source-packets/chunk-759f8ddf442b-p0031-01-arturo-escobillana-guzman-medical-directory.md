---
type: source_packet
status: draft
source_title: "Guia Medica Nacional, Profesiones Medicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition, page 31"
source_path: "raw/sources/Guía Médica Nacional Profesiones Médicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition.pdf"
source_sha256: 72a88105e04ded44e079ee7643c9c2062bed1ba140fac13611efd16c1bb3a874
converted_file: "raw/converted/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-21-40.codex.md"
converted_sha256: 759f8ddf442bdeb6e07733a26bc90641e5390b72e6bda4eff6b8c10555fb87f8
chunk: "raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dic-5f5453300f/page-0031-chunk-01.md"
chunk_id: CHUNK-759f8ddf442b-P0031-01
chunk_manifest: "raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dic-5f5453300f/manifest.json"
page_reference: "source page 31"
source_type: national_medical_directory
source_location: "Chile"
source_date: "1959-07"
family_relevance: critical
matched_terms:
  - Arturo
conversion_confidence: low_to_medium
conversion_qa_concern: "Controller flagged qc:reread-page. The chunk reports Docling readability status rough_ok, but says conversion QA must compare the output with the rendered page image. The referenced page image page-0031.jpg was not present in the conversion job directory during extraction. Docling flattened a tabular directory into separate name, address, and locality runs, so address/locality alignment requires visual reread."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Arturo Escobillana Guzmán In 1959 Medical Directory

This packet stages evidence from page 31 of the 1959 Chilean national medical directory. The converted page is an alphabetized directory page of names followed by address and locality runs. The family-relevant name is `Escobillana Guzmán, Arturo`.

## Literal Support

```text
Escobillana  Guzmán,  Arturo
```

Nearby converted text also includes the adjacent entry:

```text
Escobillana  Guzmán,  Eliana
```

The converted address/locality runs that appear to align with these adjacent entries are:

```text
Centro  de  Salud Arturo  Prat  139
```

```text
Ancud Graneros
```

## Conversion Confidence And QA Concern

Conversion confidence is low-to-medium. The name mention itself is reasonably legible in the converted text, but the task was prioritized for `qc:reread-page`. The page image path recorded in the chunk metadata, `raw/codex-conversion-jobs/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-21-40/page-images/page-0031.jpg`, was not present when checked. The tabular structure was flattened, so the exact mapping from name to address and city is provisional.

## Uncertainty

Low-to-moderate uncertainty that this page contains a directory entry for Arturo Escobillana Guzmán. Higher uncertainty remains around the address/locality pairing until the original page layout is reread. Sequential alignment suggests Arturo Escobillana Guzmán may correspond to `Centro de Salud` and `Ancud`, while Eliana Escobillana Guzmán may correspond to `Arturo Prat 139` and `Graneros`; this should not be promoted without visual confirmation.

## Promotion Recommendation

Keep on `hold_for_conversion_qa`. After visual reread verifies the row alignment, the named-person listing and any address/locality claim can move to proof review.
