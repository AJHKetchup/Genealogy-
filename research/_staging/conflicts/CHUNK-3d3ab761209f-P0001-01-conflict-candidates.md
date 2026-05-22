---
type: staged_conflict_candidates
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
chunk_id: CHUNK-3d3ab761209f-P0001-01
status: draft
promotion_recommendation: hold_for_review
---

# Conflict And QA Candidates: Birth Register Entries 513-515

## Shared Source Reference

- Source path: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Converted file: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk/page reference: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, CHUNK-3d3ab761209f-P0001-01, page range 1-1, register page 172
- Conversion confidence / QA concern: main entries high; specific QA concerns listed below.

| Candidate id | Candidate issue | Literal support | Uncertainty | Promotion recommendation |
| --- | --- | --- | --- | --- |
| conflict-514-father-unknown | Record 514 explicitly states that the father is unknown. | "**Nombre del padre.**<br>Se ignora" | This conflicts with any later claim assigning a father to Juan Bautista Riquelme Aviles unless supported by stronger evidence. | Promote as a conflict/negative-evidence note after review. |
| qa-514-witness-utiera | Witness surname in record 514 may be misread. | Converted witness text: "Benjamin Utiera"; conversion note: "The surname of the witness in record 514 is transcribed as `Utiera`, but the handwriting is somewhat difficult to read." | The visible source should be checked before creating or merging a witness identity. | Hold pending image review. |
| qa-514-street-sanegueso | Street name in record 514 is unusual. | Converted location and domicile text: "Calle Sanegueso"; conversion note: "The street name in record 514 is transcribed as `Sanegueso`, which is an unusual spelling. The handwriting is clear, but the name itself is uncommon." | May be a period street name, spelling variant, or conversion/read issue. | Promote only with QA note after image/place review. |
| qa-515-neira-emendation | Record 515 has a surname emendation note. | "Neira=emendado=<br>vale=<br>Emilio Larenas<br>O. de R. C." | Supports "Neira" as corrected text but should be verified against image before canonical normalization. | Hold for image review before promotion. |
| qa-page-cropped | The page is cropped at the bottom. | Conversion audit: "The page is from a bound volume and is cropped at the bottom, so there may be additional records on the physical page that are not visible in the image. Three complete records (513, 514, 515) have been transcribed." | Does not undermine the three extracted entries but limits page-level completeness. | Preserve as source packet QA note. |
