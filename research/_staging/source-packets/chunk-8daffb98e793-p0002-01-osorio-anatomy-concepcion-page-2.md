---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-8daffb98e793-P0002-01
worker: postconv-evidence-extraction-20260522124143912
source_title: "Osorio et al., Pioneers of a Century of Anatomical Teaching in the City of Concepcion, Chile"
source_type: journal_article
source_path: "raw/sources/Osorio, H., Toro, J.C., Schorwer, K., Riveros, A., & Cardenas, J. Pioneers of a Century of Anatomical Teaching in the City of Concepción, Chile, International Journal of Morpholog.pdf"
source_sha256: 3a73408510b0c2052341e77030a4f84fdaa56899261a9d30d76aa00e63c49f16
converted_file: "raw/converted/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-cardenas-j-pioneers-of-a-century-of-anatomical-teaching-in-the-city-of-concepci-n-chile-international-journal-of-morpholog-pages-1-10.codex.md"
converted_sha256: 8daffb98e793c0cade2ce4935f574a7b0a672385cfb90e951e9d5ac5ef13aab9
chunk: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/page-0002-chunk-01.md"
chunk_id: CHUNK-8daffb98e793-P0002-01
chunk_manifest: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/manifest.json"
page_reference: "source page 2; assigned page range 2-2"
family_relevance: critical
matched_terms:
  - Dios
  - Juan
  - knowledge
conversion_confidence: medium_high_for_visible_page_2_sentence
conversion_qa_concern: "The rendered page 2 image is present and was reread, confirming the biographical sentence about Dr. Virginio Gomez's birth year and literal birthplace wording. The assigned chunk still includes a second Page Metadata/Literal Transcription block for page 3, so page-boundary cleanup remains needed before any canonical promotion. The matched terms appear to be false positives from 'San Juan de Dios Hospital' and generic article text rather than direct family evidence."
uncertainty: "Low for the narrow visible page 2 sentence that states Dr. Virginio Gomez was born in Los Angeles in 1877. Moderate for other biographical, occupational, and identity-normalization uses because the source is a secondary journal article and the chunk contains page 3 contamination."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Osorio et al. Anatomy Teaching Article, Page 2

This packet stages evidence from the assigned page 2 chunk of a 2020 journal article about anatomical teaching in Concepcion, Chile. The page contains general institutional history and a short biographical paragraph about Dr. Virginio Gomez.

Revision note, 2026-05-22: The rendered page image `raw/codex-conversion-jobs/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-cardenas-j-pioneers-of-a-century-of-anatomical-teaching-in-the-city-of-concepci-n-chile-international-journal-of-morpholog-pages-1-10/page-images/page-0002.jpg` is present in this workspace and visibly confirms the birth-year and literal birthplace sentence. Canonical promotion remains on hold because the assigned chunk is contaminated with page 3 material and has not had page-boundary cleanup.

## Literal Support

```text
This committee was made up of a group of illustrious people from Concepción with a significant Masonic presence, including Mr. Enrique Molina, Rector of the Men's High School of Concepción and Dr. Virginio Gómez, Director of the San Juan de Dios Hospital (Da Costa, 1995).

** Dr. Virginio Gómez was born in Los Angeles in 1877. Once he received his medical degree, he obtained a scholarship in 1904 to continue his studies in Germany (Luvel, 1968) (Fig. 1A). After a long journey that included his participation in the First World War, upon his return to Chile, in 1917 he was named Director of the San Juan de Dios Hospital in Concepción. In 1920, he was appointed Director of the Hospital San Juan de Dios in Concepción.
```

## Evidence Scope

The page supports narrow, image-confirmed birth-year and literal birthplace wording for Dr. Virginio Gomez. These remain staged as secondary-source evidence and should not be promoted until conversion/page-boundary QA is resolved. Other biographical and office-holding details are staged only as context or unresolved candidates. It does not state any parent-child, spouse, sibling, or other family relationship. It is a secondary published article, not a vital record.

## QA Notes

- The rendered page 2 image confirms: `Dr. Virginio Gómez was born in Los Angeles in 1877.`
- The chunk itself contains page 3 material after the page 2 transcription, including a figure caption that may expand `Dr. Virginio Gómez` to `Dr. Virginio Gómez Gonzalez`. Because the assignment page range is 2-2, that page 3 support is not used for promotable page 2 claims.
- The directorship sentence gives two dates, 1917 and 1920, for apparently similar appointments to San Juan de Dios Hospital in Concepcion. The image confirms both date statements as printed/translated, but they remain an internal conflict or chronology issue until cited references are reviewed.
- The matched terms `Dios` and `Juan` occur in the hospital name `San Juan de Dios`; they are not evidence of a family named Juan or Dios.
