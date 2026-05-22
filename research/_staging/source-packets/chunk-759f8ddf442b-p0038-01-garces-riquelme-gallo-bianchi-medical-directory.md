---
type: source_packet
status: draft
source_title: "Guia Medica Nacional, Profesiones Medicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition, page 38"
source_path: "raw/sources/Guía Médica Nacional Profesiones Médicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition.pdf"
source_sha256: 72a88105e04ded44e079ee7643c9c2062bed1ba140fac13611efd16c1bb3a874
converted_file: "raw/converted/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-21-40.codex.md"
converted_sha256: 759f8ddf442bdeb6e07733a26bc90641e5390b72e6bda4eff6b8c10555fb87f8
chunk: "raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dic-5f5453300f/page-0038-chunk-01.md"
chunk_id: CHUNK-759f8ddf442b-P0038-01
chunk_manifest: "raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dic-5f5453300f/manifest.json"
page_reference: "source page 38"
source_type: national_medical_directory
source_location: "Chile"
source_date: "1959-07"
family_relevance: critical
matched_terms:
  - Arturo
  - Riquelme
conversion_confidence: low_to_medium
conversion_qa_concern: "Controller flagged qc:reread-page. The chunk reports Docling readability status rough_ok, but says conversion QA must compare the output with the rendered page image. Docling flattened the tabular directory into separate name, address, and locality runs, so exact address/locality alignment requires visual reread."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Page 38 Matched Directory Entries

This packet stages evidence from page 38 of the 1959 Chilean national medical directory. The converted page is an alphabetized directory page of names followed by address and locality runs. The family-relevant converted name mentions are `Gallo Bianchi, Arturo` and `Garcés Riquelme, Jorge`; the page also includes `Arturo Prat 113` as an address line, which is not treated as a person-name match.

## Literal Support

```text
Gallo  Bianchi,  Arturo
```

```text
Garcés  Riquelme,

Jorge
```

The converted address/locality runs that appear to align by sequence are:

```text
Nueva  Hannover  5810
```

```text
Miraflores  269,  Depto.  22
```

```text
Santiago
```

## Conversion Confidence And QA Concern

Conversion confidence is low-to-medium. The name mentions are readable in converted text, but the controller requested `reread-page`. The source appears to be a multi-column or tabular directory page, and Docling flattened names, addresses, and localities into separate runs. Sequential alignment suggests Arturo Gallo Bianchi corresponds to `Nueva Hannover 5810`, Santiago, and Jorge Garcés Riquelme corresponds to `Miraflores 269, Depto. 22`, Santiago, but this should not be promoted without visual row confirmation.

## Uncertainty

Low-to-moderate uncertainty that the page contains directory entries for Arturo Gallo Bianchi and Jorge Garcés Riquelme. Higher uncertainty remains around exact row alignment, diacritics, and whether any address or locality was shifted during conversion.

## Promotion Recommendation

Keep on `hold_for_conversion_qa`. After visual reread verifies the name spellings and row alignment, the named-person listing claims and any address/locality claims can move to proof review.
