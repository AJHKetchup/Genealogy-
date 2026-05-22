---
type: claim
status: draft
claim_type: birth_year
subject: "Virginio Gomez"
predicate: "was born in"
object: "1877"
source: "raw/sources/Osorio, H., Toro, J.C., Schorwer, K., Riveros, A., & Cardenas, J. Pioneers of a Century of Anatomical Teaching in the City of Concepción, Chile, International Journal of Morpholog.pdf"
source_packet: "research/_staging/source-packets/chunk-bdfcf4d3256f-p0002-01-osorio-anatomy-concepcion-page-2.md"
converted_file: "raw/converted/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-cardenas-j-pioneers-of-a-century-of-anatomical-teaching-in-the-city-of-concepci-n-chile-international-journal-of-morpholog-pages-1-10.codex.md"
chunk: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/page-0002-chunk-01.md"
chunk_id: CHUNK-bdfcf4d3256f-P0002-01
page_reference: "source page 2"
confidence: medium_high
promotion_recommendation: hold_for_conversion_qa
---

# Claim: Virginio Gomez Birth Year

- Literal support: `Dr. Virginio Gómez was born in Los Angeles in 1877.`
- Conversion confidence/QA concern: Medium-high for the assigned chunk text and page image. The chunk and manifest agree on a page 2-only chunk identifier, resolving the stale `CHUNK-8daffb98e793` page-boundary problem, and the recorded page 2 image is present and visually confirms the sentence. Remaining blocker: the local chunk file hash `d663257ddc2c07588891e07cbf07144f3e22b313b8d330d8527366cec0084d69` differs from manifest chunk SHA-256 `2405c50b9f7ba1e2f598a7a3f81ab0d0baeee673978096dab2ba025bf00f94a8`.
- Uncertainty: This proves only a secondary-source birth year, not a full birth date, parentage, spouse, child, or other family relationship.
- Promotion recommendation: Hold for conversion QA until the chunk hash mismatch is accepted or regenerated. After that QA, this should proceed only as a secondary-source birth-year claim.
