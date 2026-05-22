---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-bdfcf4d3256f-P0007-01
worker: postconv-evidence-extraction-20260522223033132
source_title: "Osorio et al., Pioneers of a Century of Anatomical Teaching in the City of Concepcion, Chile"
source_type: journal_article
source_path: "raw/sources/Osorio, H., Toro, J.C., Schorwer, K., Riveros, A., & Cardenas, J. Pioneers of a Century of Anatomical Teaching in the City of Concepción, Chile, International Journal of Morpholog.pdf"
source_sha256: 3a73408510b0c2052341e77030a4f84fdaa56899261a9d30d76aa00e63c49f16
converted_file: "raw/converted/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-cardenas-j-pioneers-of-a-century-of-anatomical-teaching-in-the-city-of-concepci-n-chile-international-journal-of-morpholog-pages-1-10.codex.md"
converted_sha256: bdfcf4d3256f3e609480fd7f192e4e8c6368bdd35cb1301570f238808113958f
chunk: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/page-0007-chunk-01.md"
chunk_id: CHUNK-bdfcf4d3256f-P0007-01
chunk_manifest: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/manifest.json"
page_reference: "source page 7; assigned page range 7-7"
family_relevance: critical
matched_terms:
  - Garcia
conversion_confidence: medium_for_chunk_text_low_for_page_image_verification
conversion_qa_concern: "The chunk front matter and manifest agree this is source page 7, but the controller requested reread-page QA. The page image referenced in the chunk metadata, page-images/page-0007.jpg, was not present locally during extraction; only page images 0002-0004 were available for this conversion job. The local chunk file SHA-256 observed during extraction was 8183531716655fc83a96ba37f114d0d8babb87d1da1013707adfd63dda62b289, differing from the manifest chunk SHA-256 8e1c506aa088c56083f5b299d629edb92c3ad5b115b64a48d0b3f095e565263c."
uncertainty: "The matched family term appears only as the surname Garcia in a parenthetical source citation for architectural/campus history. The page does not state a given name, family relationship, vital event, residence, or genealogical fact for any Garcia person."
promotion_recommendation: do_not_promote
---

# Source Packet: Osorio et al. Anatomy Teaching Article, Page 7

## Literal Support

```text
The construction of the definitive pavilion was entrusted to the architects Carlos Miranda and Enrique San Martín who followed the guidelines known as the 'Bruner Plan' (Muñoz, 1993; García).
```

## Evidence Scope

The assigned page is about Enrique Solervicens and the University of Concepcion anatomy building. The only matched family term is `García`, used as a parenthetical bibliographic citation. This page does not identify a Garcia person in the narrative and does not support a family-tree claim.

## QA Notes

- Docling readability status in the chunk metadata: `rough_ok`.
- Controller QC action: `reread-page`.
- Page 7 image was not available locally in the conversion job's `page-images` directory during extraction, so no visual reread could be completed.
- The observed chunk hash differs from the manifest hash, creating a provenance QA concern.

## Promotion Recommendation

Do not promote. Treat this packet as a false-positive/scope guard for the Garcia match until conversion QA can reread the page image.
