---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-bdfcf4d3256f-P0002-01
worker: postconv-evidence-extraction-20260522222530008
source_title: "Osorio et al., Pioneers of a Century of Anatomical Teaching in the City of Concepcion, Chile"
source_type: journal_article
source_path: "raw/sources/Osorio, H., Toro, J.C., Schorwer, K., Riveros, A., & Cardenas, J. Pioneers of a Century of Anatomical Teaching in the City of Concepción, Chile, International Journal of Morpholog.pdf"
source_sha256: 3a73408510b0c2052341e77030a4f84fdaa56899261a9d30d76aa00e63c49f16
converted_file: "raw/converted/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-cardenas-j-pioneers-of-a-century-of-anatomical-teaching-in-the-city-of-concepci-n-chile-international-journal-of-morpholog-pages-1-10.codex.md"
converted_sha256: bdfcf4d3256f3e609480fd7f192e4e8c6368bdd35cb1301570f238808113958f
chunk: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/page-0002-chunk-01.md"
chunk_id: CHUNK-bdfcf4d3256f-P0002-01
chunk_manifest: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/manifest.json"
page_reference: "source page 2; assigned page range 2-2"
family_relevance: critical
matched_terms:
  - Medical
conversion_confidence: medium_high_for_assigned_chunk_text_and_page_image
conversion_qa_concern: "The current chunk front matter and chunk manifest agree that CHUNK-bdfcf4d3256f-P0002-01 covers source page 2 only, and the recorded page image exists in this workspace and visually matches the narrow quoted birth-year/birthplace sentence. However, the local chunk file SHA-256 still differs from the manifest chunk SHA-256, so provenance metadata remains blocked for conversion/file-normalization QA before canonical promotion."
uncertainty: "Low to medium for the narrow secondary-source statements that Dr. Virginio Gomez was born in Los Angeles in 1877, because the assigned chunk text is explicit. This source is a 2020 journal article, not a birth, baptism, civil, or family record; it states no full birth date and no family relationship."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Osorio et al. Anatomy Teaching Article, Page 2

This packet supersedes the stale `CHUNK-8daffb98e793-P0002-01` staging metadata for the assigned page 2 chunk. The current manifest identifies this chunk as `CHUNK-bdfcf4d3256f-P0002-01`, with `page_start: 2`, `page_end: 2`, and `part: 1`. The page-boundary issue is reconciled for extraction scope; the chunk hash mismatch remains unresolved.

## Literal Support

```text
This committee was made up of a group of illustrious people from Concepción with a significant Masonic presence, including Mr. Enrique Molina, Rector of the Men's High School of Concepción and Dr. Virginio Gómez, Director of the San Juan de Dios Hospital (Da Costa, 1995).

** Dr. Virginio Gómez was born in Los Angeles in 1877. Once he received his medical degree, he obtained a scholarship in 1904 to continue his studies in Germany (Luvel, 1968) (Fig. 1A). After a long journey that included his participation in the First World War, upon his return to Chile, in 1917 he was named Director of the San Juan de Dios Hospital in Concepción. In 1920, he was appointed Director of the Hospital San Juan de Dios in Concepción.
```

## Evidence Scope

The assigned chunk supports two narrow secondary-source genealogical statements: a birth year of 1877 and a literal birthplace wording of Los Angeles for Dr. Virginio Gomez. It also contains institutional and medical-career context, but those details are not family relationships and should not be fanned out into broad historical claims for this extraction task.

## QA Reconciliation

- Current chunk metadata: `CHUNK-bdfcf4d3256f-P0002-01`.
- Current manifest metadata: page 2 only, part 1, chunk SHA-256 `2405c50b9f7ba1e2f598a7a3f81ab0d0baeee673978096dab2ba025bf00f94a8`.
- Local file hash observed during this revision: `d663257ddc2c07588891e07cbf07144f3e22b313b8d330d8527366cec0084d69`, which differs from the manifest hash. This is not a source-text contradiction, but it is a provenance blocker for promotion.
- The assembled converted Markdown includes page 3 material immediately after page 2, but the assigned chunk file used here does not; page scope for this packet remains page 2 only.
- The conversion metadata references `page-images/page-0002.jpg`; that image exists in the local conversion job during this revision and visually shows the same page 2 sentence: `Dr. Virginio Gómez was born in Los Angeles in 1877.`

## Promotion Recommendation

Hold for conversion QA. If conversion/file-normalization QA accepts or regenerates the chunk hash metadata, the narrow secondary-source birth-year and literal birthplace claims may proceed to proof review. No full birth date or family relationship should be inferred from this page.
