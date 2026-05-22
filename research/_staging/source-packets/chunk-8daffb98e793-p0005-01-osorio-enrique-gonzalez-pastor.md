---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-8daffb98e793-P0005-01
worker: postconv-evidence-extraction-20260522134448654
source_title: "Osorio et al., Pioneers of a Century of Anatomical Teaching in the City of Concepcion, Chile"
source_type: journal_article
source_path: "raw/sources/Osorio, H., Toro, J.C., Schorwer, K., Riveros, A., & Cardenas, J. Pioneers of a Century of Anatomical Teaching in the City of Concepción, Chile, International Journal of Morpholog.pdf"
source_sha256: 3a73408510b0c2052341e77030a4f84fdaa56899261a9d30d76aa00e63c49f16
converted_file: "raw/converted/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-cardenas-j-pioneers-of-a-century-of-anatomical-teaching-in-the-city-of-concepci-n-chile-international-journal-of-morpholog-pages-1-10.codex.md"
converted_sha256: 8daffb98e793c0cade2ce4935f574a7b0a672385cfb90e951e9d5ac5ef13aab9
chunk: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/page-0005-chunk-01.md"
chunk_id: CHUNK-8daffb98e793-P0005-01
chunk_manifest: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/manifest.json"
page_reference: "source page 5; printed page 654; assigned page range 5-5"
family_relevance: critical
matched_terms:
  - Birth
  - Juan
  - Luis
  - chunk
conversion_confidence: medium_high
conversion_qa_concern: "Revision reread completed from the original PDF text layer for source page 5 using pdftotext. The PDF text layer confirms the local Enrique Gonzalez Pastor paragraph, including the birth date and place. The expected rendered page image still does not resolve in the current workspace, ImageMagick PDF rendering failed because Ghostscript is unavailable, and both the converted chunk and PDF text extraction show two-column reading-order scrambling near the bottom of the page."
uncertainty: "Low for the narrow wording in the Enrique Gonzalez Pastor biographical paragraph as represented by the original PDF text layer; moderate for canonical genealogy use because this is a 2020 secondary journal article rather than a civil, church, university, obituary, or family record. The matched terms Juan and Luis are names of unrelated professors in the institutional narrative, not family relationship evidence."
promotion_recommendation: promote_after_review
---

# Source Packet: Osorio et al. Anatomy Teaching Article, Page 5

This packet stages evidence from the assigned page 5 chunk of a 2020 journal article about anatomical teaching in Concepcion, Chile. The genealogically useful content is a converted biographical paragraph about Dr. Enrique Gonzalez Pastor.

## Literal Support

Revision reread from original PDF page 5 text layer:

```text
Dr. Enrique Gonzalez Pastor (Fig. 1B) was born in Concepcion on
January 2, 1889. In 1913 he graduated with honors as a surgeon from
the University of Chile, writing a thesis on organ transplantation.
...
course for the recently created Medicine degree. In 1927 he left the
anatomy chair to teach the course of Surgical Pathology, which he
taught until his retirement in 1945.
...
out. After a long battle against a chronic disease, Dr. Gonzalez died in September 1957.
```

Converted chunk support:

```text
Dr.   Enrique   Gonzalez   Pastor   (Fig.   1B)   was   born   in   Concepción   on January   2,   1889.   In   1913   he   graduated   with   honors   as   a   surgeon   from the   University   of   Chile,   writing   a   thesis   on   organ   transplantation.

Returning   to   Chile,   he   settled   in Concepción   and   was   an   active   member   of   the   Pro   University Committee.

... between   1924   and   1927,   he   directed   the   anatomy course   for   the   recently   created   Medicine   degree.

After   a   long   battle   against   a   chronic   disease,   Dr.   Gonzalez   died   in   September   1957.
```

## Evidence Scope

The chunk supports narrow draft claims about Enrique Gonzalez Pastor's birth, education, anatomy-course role, and death month/year. It does not state parent-child, spouse, sibling, or other family relationships. It also names Luis Vargas and Juan Noe among professors or course instructors, but those mentions are institutional context only and are not family clues.

## QA Notes

- Proof-review revision reread was performed directly from the original PDF text layer for source page 5. This confirms the local name/date/place sentence for Dr. Enrique Gonzalez Pastor and improves the extraction confidence for the narrow claims staged from that paragraph.
- Required source-image reread still could not be completed because the expected `page-0005.jpg` is missing from the conversion job's `page-images` directory. A local ImageMagick render attempt failed because Ghostscript is unavailable.
- Page-numbering note: staged drafts retain the converted chunk's printed-page reference `654`, but the direct PDF text-layer extraction ended with printed page number `653`. This discrepancy should be reconciled during conversion QA or visual page review.
- The converted transcription and PDF text extraction both interleave two-column text in places, especially near the bottom of the page. The Enrique Gonzalez Pastor paragraph is locally coherent, but downstream proof review should cite the source-quality limit.
- The source is secondary and should not override civil, church, university, obituary, or family records.
