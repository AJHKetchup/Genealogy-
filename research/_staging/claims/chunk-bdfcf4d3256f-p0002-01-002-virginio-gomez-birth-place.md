---
type: claim
status: draft
claim_type: birth_place
subject: "Virginio Gomez"
predicate: "was born in"
object: "Los Angeles"
source: "raw/sources/Osorio, H., Toro, J.C., Schorwer, K., Riveros, A., & Cardenas, J. Pioneers of a Century of Anatomical Teaching in the City of Concepción, Chile, International Journal of Morpholog.pdf"
source_packet: "research/_staging/source-packets/chunk-bdfcf4d3256f-p0002-01-osorio-anatomy-concepcion-page-2.md"
converted_file: "raw/converted/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-cardenas-j-pioneers-of-a-century-of-anatomical-teaching-in-the-city-of-concepci-n-chile-international-journal-of-morpholog-pages-1-10.codex.md"
chunk: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/page-0002-chunk-01.md"
chunk_id: CHUNK-bdfcf4d3256f-P0002-01
page_reference: "source page 2"
confidence: medium
promotion_recommendation: hold_for_conversion_qa
---

# Claim: Virginio Gomez Birth Place

- Literal support: `Dr. Virginio Gómez was born in Los Angeles in 1877.`
- Conversion confidence/QA concern: Medium for the literal place string in the assigned chunk and page image. The source text/page image read `Los Angeles`; do not silently normalize this to `Los Angeles, Chile` or `Los Ángeles` without a separate authority. Remaining blocker: the local chunk file hash differs from the manifest chunk SHA-256.
- Uncertainty: This is a secondary-source birthplace claim only. The page does not specify jurisdictional qualifiers beyond the place name in the sentence, and it does not state a full birth date or family relationship.
- Promotion recommendation: Hold for conversion QA until the chunk hash mismatch is accepted or regenerated. After that QA, this should proceed only as literal secondary-source birthplace wording.
