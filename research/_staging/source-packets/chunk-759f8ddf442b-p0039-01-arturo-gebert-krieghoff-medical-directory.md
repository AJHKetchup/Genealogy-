---
type: source_packet
status: draft
source_title: "Guia Medica Nacional, Profesiones Medicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition, page 39"
source_path: "raw/sources/Guía Médica Nacional Profesiones Médicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition.pdf"
source_sha256: 72a88105e04ded44e079ee7643c9c2062bed1ba140fac13611efd16c1bb3a874
converted_file: "raw/converted/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-21-40.codex.md"
converted_sha256: 759f8ddf442bdeb6e07733a26bc90641e5390b72e6bda4eff6b8c10555fb87f8
chunk: "raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dic-5f5453300f/page-0039-chunk-01.md"
chunk_id: CHUNK-759f8ddf442b-P0039-01
chunk_manifest: "raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dic-5f5453300f/manifest.json"
page_reference: "source page 39"
source_type: national_medical_directory
source_location: "Chile"
source_date: "1959-07"
family_relevance: critical
matched_terms:
  - Andes
  - Arturo
  - Carmen
  - Riquelme
conversion_confidence: low_to_medium
conversion_qa_concern: "Controller flagged qc:reread-page. The chunk reports Docling readability status rough_ok, but says conversion QA must compare the output with the rendered page image. The referenced page image page-0039.jpg was not present in the conversion job directory during extraction. Docling flattened a tabular directory into name, address, and locality runs, so row alignment requires visual reread."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Arturo Gebert Krieghoff In 1959 Medical Directory

This packet stages evidence from page 39 of the 1959 Chilean national medical directory. The converted page is an alphabetized directory page of names followed by address and locality runs. The family-relevant name match is `Gebert Krieghoff, Arturo`.

## Literal Support

```text
Gebauer  Weisser,  Teodoro Gebert  Krieghoff,  Arturo Geismar  Block,  Teresa
```

The converted address and locality runs appear to place the Arturo Gebert Krieghoff row near the end of the page:

```text
Moneda  1829 San Martín 980 Eulogia  Sánchez  23
```

```text
Santiago Temuco Santiago
```

Sequential alignment suggests `Gebert Krieghoff, Arturo` may correspond to `San Martín 980` and `Temuco`, with adjacent entries `Gebauer Weisser, Teodoro` and `Geismar Block, Teresa` corresponding to the surrounding address/locality values. This must be visually checked before promotion.

## Matched-Term Review

The matched terms `Carmen`, `Riquelme`, and `Andes` appear in the converted text as address or locality strings rather than explicit personal names or family relationships:

```text
Carmen  Silva  2866
```

```text
Riquelme  274
```

```text
Los  Andes
```

These terms are retained as extraction context but should not be promoted as family evidence from this chunk.

## Conversion Confidence And QA Concern

Conversion confidence is low-to-medium. The name mention itself is legible in the converted text, but the task was prioritized for `qc:reread-page`. The page image path recorded in the chunk metadata, `raw/codex-conversion-jobs/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-21-40/page-images/page-0039.jpg`, was not present when checked. The tabular structure was flattened, so exact address/locality pairing is provisional.

## Uncertainty

The source supports that a person named Arturo Gebert Krieghoff appears on page 39 of the directory. It does not state birth, death, parents, spouse, children, or any family relationship. Address and locality alignment remain uncertain until page 39 is visually reread.

## Promotion Recommendation

Keep on `hold_for_conversion_qa`. After visual reread verifies the row alignment, the named-person listing and any address/locality claim can move to proof review.
