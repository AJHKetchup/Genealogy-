---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-8daffb98e793-P0002-02
worker: postconv-evidence-extraction-20260522131200710
source_title: "Osorio et al., Pioneers of a Century of Anatomical Teaching in the City of Concepcion, Chile"
source_type: journal_article
source_path: "raw/sources/Osorio, H., Toro, J.C., Schorwer, K., Riveros, A., & Cardenas, J. Pioneers of a Century of Anatomical Teaching in the City of Concepción, Chile, International Journal of Morpholog.pdf"
source_sha256: 3a73408510b0c2052341e77030a4f84fdaa56899261a9d30d76aa00e63c49f16
converted_file: "raw/converted/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-cardenas-j-pioneers-of-a-century-of-anatomical-teaching-in-the-city-of-concepci-n-chile-international-journal-of-morpholog-pages-1-10.codex.md"
converted_sha256: 8daffb98e793c0cade2ce4935f574a7b0a672385cfb90e951e9d5ac5ef13aab9
chunk: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/page-0002-chunk-02.md"
chunk_id: CHUNK-8daffb98e793-P0002-02
chunk_manifest: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/manifest.json"
page_reference: "assigned source page range 2-2; chunk body includes Page Metadata: Page 4 and printed page 652"
family_relevance: critical
matched_terms:
  - Dios
  - Juan
  - Pulgar
  - chunk
  - knowledge
conversion_confidence: medium_for_literal_chunk_text
conversion_qa_concern: "Controller requested reread-page. The chunk path and manifest identify this as page 2 part 2, but the chunk body contains page 3 figure material and a later literal transcription labeled Page Metadata: Page 4 / printed page 652. No rendered source page matching that Page 4 transcription was available in the page-images directory during this task. Treat all claims from this chunk as held for conversion/page-boundary QA."
uncertainty: "The chunk explicitly names Dario Pulgar as one of several surgeons accompanying practical anatomy activities at San Juan de Dios Hospital, but gives no age, full surname, parents, spouse, residence, birth, death, or direct family relationship. Identity linkage to any canonical Dario Pulgar or Dario Pulgar Arriagada profile is unresolved."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Osorio et al. Anatomy Teaching Article, Pulgar Mention

This packet stages the direct Pulgar mention from the assigned chunk. The article is a secondary journal article about anatomical teaching in Concepcion, Chile, not a vital or civil-registration source.

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

The chunk supports only a narrow occupational/activity-context candidate for `Darío Pulgar`: he is described as one of the surgeons accompanying practical anatomy activities at San Juan de Dios Hospital. It does not state that he was related to any other named person.

## QA Notes

- `Juan` and `Dios` occur in the institutional name `San Juan de Dios Hospital`; they are not family-name evidence in this chunk.
- The assignment says page range 2-2, while the chunk body contains material labeled Page 4 / printed page 652. This packet should not flow to canonical promotion until page-boundary QA confirms the correct source page and literal wording.
