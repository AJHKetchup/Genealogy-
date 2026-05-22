---
type: source_packet
status: draft
source_title: "Guia Medica Nacional, Profesiones Medicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition, page 53"
source_path: "raw/sources/Guía Médica Nacional Profesiones Médicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition.pdf"
source_sha256: 72a88105e04ded44e079ee7643c9c2062bed1ba140fac13611efd16c1bb3a874
converted_file: "raw/converted/ca72a88105-gu-a-m-dica-nacional-pro-p0041-0060-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-41-60.codex.md"
converted_sha256: f2c5548c9fde27d492bee88446b34850f63ff6c1d5eba2bcb170fcfef3772b30
chunk: "raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0041-0060-gu-a-m-dica-nacional-profesiones-m-dic-8fbd29c654/page-0053-chunk-01.md"
chunk_id: CHUNK-f2c5548c9fde-P0053-01
chunk_manifest: "raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0041-0060-gu-a-m-dica-nacional-profesiones-m-dic-8fbd29c654/manifest.json"
page_reference: "source page 53; printed page 56"
source_type: national_medical_directory
source_location: "Chile"
source_date: "1959-07"
family_relevance: critical
matched_terms:
  - Arturo
conversion_confidence: high_after_image_review
conversion_qa_concern: "Controller flagged qc:reread-page. Image reread from page-0053.jpg confirms the relevant row alignment, names, and Santiago localities. The converted Markdown still has two transcription defects: `Vicuña Mackenna 4, 7' Piso` should be read from the image as `Vicuña Mackenna 4, 7º Piso`, and `Merced 250 В` should be read from the image as `Merced 250 B`."
promotion_recommendation: promote_after_review
---

# Source Packet: Arturo Entries In 1959 Chilean Medical Directory, Page 53

This packet stages evidence from source page 53, printed page 56, of the 1959 Chilean national medical directory. The page is an alphabetized table of names, street addresses, and localities. The family-relevant matched term is `Arturo`.

## Literal Support

The converted table includes the following personal-name rows:

```text
| Larraín García, Arturo                | Vicuña Mackenna 4, 7' Piso            | Santiago              |
```

```text
| Lavín Gallegos, Arturo                | Merced 250 В                          | Santiago              |
```

The rendered page image at `raw/codex-conversion-jobs/ca72a88105-gu-a-m-dica-nacional-pro-p0041-0060-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-41-60/page-images/page-0053.jpg` was visually reread for this revision. The image-reviewed readings are:

```text
Larraín García, Arturo     Vicuña Mackenna 4, 7º
                           Piso                  Santiago
Lavín Gallegos, Arturo     Merced 250 B           Santiago
```

## Conversion Confidence And QA Concern

Conversion confidence is high for the two image-reviewed rows. The visual page reread confirms the `Larraín García, Arturo` row alignment, address, and locality requested by proof review. It also confirms the `Lavín Gallegos, Arturo` row. The converted Markdown should not be silently normalized: it reads `7' Piso` where the image reads `7º Piso`, and it reads `Merced 250 В` where the image reads `Merced 250 B`.

## Uncertainty

The page supports directory mentions for Arturo Larraín García and Arturo Lavín Gallegos, with associated Santiago addresses in the image-reviewed table. It does not state birth, death, parents, spouse, children, or any family relationship for either person. Do not merge these mentions with any canonical person solely on the given name `Arturo`.

## Promotion Recommendation

Promote after proof review as directory-listing evidence only. The conversion-review correction note should accompany promotion so the derivative transcript differences remain visible.
