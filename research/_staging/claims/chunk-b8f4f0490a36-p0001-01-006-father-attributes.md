---
type: claim
status: draft
claim_type: parent_attributes
subject: "Jose del Carmen Pulgar"
predicate: "was recorded as father with attributes"
object: "Chileno; Empleado; resident at Calle de Colipi"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-jose-del-carmen-segundo-pulgar-arriagada.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
confidence: medium
promotion_recommendation: hold_for_conversion_qa
---

# Claim: Father's Recorded Attributes

- Literal support: assigned chunk says `**Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí`; this source-image reread supports `Jose del Carmen Pulgar` without a clearly visible final `S.` suffix and supports `Chileno`, `Empleado`, and the Calle de Colipi/Colipí residence line. The converted Markdown file instead gives entry 172 as father `Oswaldo Bunster`, nationality `chileno`, occupation `Agricultor`, and domicile `Ballena`.
- Conversion confidence/QA concern: mixed. The source image supports the Pulgar/Arriagada row, but the assigned chunk and image reread disagree on the exact father-name suffix, and the assigned converted Markdown file gives a different entry.
- Uncertainty: Low for listed nationality and occupation on the visible source image; moderate for residence spelling/normalization and the father's exact recorded name; high for promotion readiness until conversion QA resolves the converted-file mismatch and decides whether the father-name suffix is present, absent, or uncertain.
