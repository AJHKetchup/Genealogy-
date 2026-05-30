---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-45c0243885f8-P0766-01"
worker: postconv-evidence-extraction-20260530163554877
source_title: "Camara de Senadores de la Nacion, 1936, page 766"
source_type: legislative_debate
source: "raw/sources/Cámara de Senadores de la Nación, 1936.pdf"
source_path: "raw/sources/Cámara de Senadores de la Nación, 1936.pdf"
source_sha256: "221159bd9b79619cfbcad6b7d590f4fd91fff0a92ecd40b9972437ea865bb289"
converted_file: "raw/converted/ca221159bd-c-mara-de-senadores-de-l-p0754-0778-c-mara-de-senadores-de-la-naci-n-1936-pages-754-778.codex.md"
converted_sha256: "45c0243885f824bcfe2c41db2e40714ff0eadb5af5780d5d3c73769d52848efc"
chunk: "raw/chunks/ca221159bd-c-mara-de-senadores-de-l-p0754-0778-c-mara-de-senadores-de-la-naci-n-1936-ffa4bc4dbc/page-0766-chunk-01.md"
chunk_id: "CHUNK-45c0243885f8-P0766-01"
chunk_manifest: "raw/chunks/ca221159bd-c-mara-de-senadores-de-l-p0754-0778-c-mara-de-senadores-de-la-naci-n-1936-ffa4bc4dbc/manifest.json"
page_reference: "source page 766"
page_start: 766
page_end: 766
page_image: "raw/codex-conversion-jobs/ca221159bd-c-mara-de-senadores-de-l-p0754-0778-c-mara-de-senadores-de-la-naci-n-1936-pages-754-778/page-images/page-0766.jpg"
family_relevance: low
matched_terms:
  - "Dario"
conversion_confidence: low
conversion_qa_concern: "Controller requested reread-page. The page image path recorded in chunk metadata and the conversion manifest is not present in the workspace; the manifest marks page 766 image bytes as 0 and image_sha256 as blank. The matched term is an OCR/text-layer line-break artifact in 'descanso llebdema- / dario', corresponding to a non-person word, likely 'hebdomadario'."
uncertainty: "Low uncertainty that the assigned chunk does not name a Dario person; moderate uncertainty in exact OCR repair because page image reread was not possible."
promotion_recommendation: do_not_promote
---

# Source Packet: Page 766 No Family Evidence From Dario Hit

## Literal Support

The assigned chunk contains a debate about Buenos Aires transport concessions, tramway companies, fares, wages, legal workday requirements, retirement contributions, and public costs. The only matched `Dario` text appears in a broken non-person word:

```text
jornada legal de 8 boras y deseanso llebdema-
dario.
```

The same page also refers generally to transport policy and companies:

```text
Este proyecto ha surgido como consecnencia
de una l'arga Ineha de las eompanias tranviarias
para conseguir el aumento de
sus tarifas.
```

## Evidence Scope

This page does not state a family member, family relationship, residence, travel, work, study, meeting attendance, signature, witness role, photograph, or other family-narrative event. The apparent `Dario` match is not a personal name and should not be promoted as evidence about any Dario or Dario Pulgar candidate.

## Conversion Confidence And QA Concern

Conversion confidence is low for exact spelling because the page has obvious OCR/text-layer noise, including `CAITAKA DE SENABODES BE LA NACION`, `boras`, and `deseanso llebdema- / dario`. The requested page-image reread could not be performed: the recorded image path is absent, and the conversion job manifest records page 766 with `image_bytes: 0` and blank `image_sha256`.

## Uncertainty

Low uncertainty that this chunk has no genealogically relevant Dario person claim. Moderate uncertainty remains for exact correction of the broken Spanish word because no page image was available for visual confirmation.

## Promotion Recommendation

Do not promote. No atomic person claim, identity candidate, conflict candidate, or family relationship should be derived from this chunk.
