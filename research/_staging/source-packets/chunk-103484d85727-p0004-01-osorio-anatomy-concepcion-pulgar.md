---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-103484d85727-P0004-01
worker: postconv-evidence-extraction-20260530042030592
source_title: "Osorio et al., Pioneers of a Century of Anatomical Teaching in the City of Concepcion, Chile"
source_type: journal_article
source: "raw/sources/Osorio, H., Toro, J.C., Schorwer, K., Riveros, A., & Cardenas, J. Pioneers of a Century of Anatomical Teaching in the City of Concepción, Chile, International Journal of Morpholog.pdf"
source_path: "raw/sources/Osorio, H., Toro, J.C., Schorwer, K., Riveros, A., & Cardenas, J. Pioneers of a Century of Anatomical Teaching in the City of Concepción, Chile, International Journal of Morpholog.pdf"
source_sha256: 3a73408510b0c2052341e77030a4f84fdaa56899261a9d30d76aa00e63c49f16
converted_file: "raw/converted/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-cardenas-j-pioneers-of-a-century-of-anatomical-teaching-in-the-city-of-concepci-n-chile-international-journal-of-morpholog-pages-1-10.codex.md"
converted_sha256: 103484d85727ba862c16f36adfa82f50eae4617d02b8ec3c028df5278c1dc324
chunk: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/page-0004-chunk-01.md"
chunk_id: CHUNK-103484d85727-P0004-01
chunk_manifest: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/manifest.json"
page_reference: "source page 4; chunk body includes Page Metadata: Source page 4 and printed page 652"
page_start: 4
page_end: 4
family_relevance: critical
matched_terms:
  - Pulgar
narrative_cues:
  - travel
literal_support: "These activities were carried out in a small room at the San Juan de Dios Hospital, under the supervision of Dr. Gómez and accompanied by the surgeons Nicanor Durán, Darío Pulgar, Enrique González Pastor and the dentist Víctor Villalobos (Solervicens, 1964)."
conversion_confidence: medium_for_literal_chunk_text
conversion_qa_concern: "Controller requested reread-page. The chunk records a page image path, but the local conversion-job directory contains page-markdown and work-orders only; no page-images directory was available at extraction time for visual confirmation."
uncertainty: "The page explicitly names Darío Pulgar as one of several surgeons accompanying practical anatomy activities at San Juan de Dios Hospital, but gives no age, full maternal surname, parents, spouse, residence, birth, death, or direct family relationship. Identity linkage to any canonical Dario Pulgar or Dario Pulgar Arriagada profile remains unresolved."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Osorio Anatomy Teaching Article, Pulgar Mention

This packet stages the direct Pulgar mention from page 4 of a secondary journal article about anatomical teaching in Concepcion, Chile. It is family-relevant as a public/professional activity context for a source-named `Darío Pulgar`, but it is not a vital record or direct family relationship source.

## Literal Support

```text
The practical component was associated with demonstrations with cadaveric material
and a number of dissections guided by assistants. These
activities were carried out in a small room at the San Juan
de Dios Hospital, under the supervision of Dr. Gómez and
accompanied by the surgeons Nicanor Durán, Darío Pulgar,
Enrique González Pastor and the dentist Víctor Villalobos
(Solervicens, 1964).
```

## Evidence Scope

The assigned page supports only narrow occupational and activity-context claims for `Darío Pulgar`: he is described as a surgeon and as one of the people accompanying practical anatomy activities at San Juan de Dios Hospital.

The page does not state a kinship relationship for Darío Pulgar. The later travel statement on the page concerns Dr. Virginio Gómez, not Pulgar, and should not be promoted as Pulgar narrative evidence.

## QA Notes

- The conversion method was PDF text-layer fallback after a Docling baseline error, and the chunk says page extraction remains subject to conversion QA.
- The controller explicitly flagged `reread-page`.
- The page image path recorded in the chunk could not be opened locally because the conversion-job directory had no `page-images` folder at extraction time.
