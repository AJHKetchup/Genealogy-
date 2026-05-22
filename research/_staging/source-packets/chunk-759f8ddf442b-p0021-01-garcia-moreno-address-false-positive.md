---
type: source_packet
status: draft
source_title: "Guia Medica Nacional, Profesiones Medicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition, page 21"
source_path: "raw/sources/Guía Médica Nacional Profesiones Médicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition.pdf"
source_sha256: 72a88105e04ded44e079ee7643c9c2062bed1ba140fac13611efd16c1bb3a874
converted_file: "raw/converted/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-21-40.codex.md"
converted_sha256: 759f8ddf442bdeb6e07733a26bc90641e5390b72e6bda4eff6b8c10555fb87f8
chunk: "raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dic-5f5453300f/page-0021-chunk-01.md"
chunk_id: CHUNK-759f8ddf442b-P0021-01
chunk_manifest: "raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dic-5f5453300f/manifest.json"
page_reference: "source page 21"
source_type: national_medical_directory
source_location: "Chile"
source_date: "1959-07"
family_relevance: false_positive_after_review
matched_terms:
  - García
conversion_confidence: medium
conversion_qa_concern: "Controller flagged qc:reread-page. The chunk reports Docling readability status rough_ok and says conversion QA must compare the output with the rendered page image before research extraction."
promotion_recommendation: do_not_promote
---

# Source Packet: Page 21 Garcia Moreno Address Scope

This packet stages the page-21 family-term hit from the 1959 Chilean national medical directory. The converted page is an alphabetized table of medical directory entries. The matched term `García` appears in an address line, not as a listed person surname.

## Literal Support

```text
| Castro Diabuno, Juan E.                              | García Moreno 1470                       | Santiago            |
```

## Extraction Assessment

The literal support identifies a directory entry for `Castro Diabuno, Juan E.` with the address `García Moreno 1470` in `Santiago`. It does not identify a person named García, a García family relationship, or a genealogical event for a García subject.

## Conversion Confidence And QA Concern

Conversion confidence is medium for the false-positive assessment because the table row is readable in the chunk text. The controller still requested `reread-page`, and the chunk states that visual conversion QA is required before research extraction. The page should be checked against the rendered image before any non-scope use.

## Uncertainty

Low uncertainty that the matched family term is an address component rather than a person name. Moderate residual uncertainty remains until page-image reread confirms row alignment and spelling.

## Promotion Recommendation

Do not promote this packet to canonical genealogy claims. Retain it as a scope note explaining why the `García` match on page 21 should not fan out into family claims.
