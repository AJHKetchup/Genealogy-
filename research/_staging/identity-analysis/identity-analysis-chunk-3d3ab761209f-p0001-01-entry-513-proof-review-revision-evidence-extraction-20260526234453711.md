---
type: identity_conflict_analysis
status: draft
role: evidence_extractor
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
source_packet: "research/_staging/source-packets/sp-chunk-3d3ab761209f-p0001-01-entry-513-515-proof-review-revision-evidence-extraction-20260526234453711.md"
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
page_reference: "image page 1; register page 172; entry 513"
confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Identity Analysis: Entry 513 Pulgar Row

## Leading Position

Entry 513 should remain a registration-scoped Pulgar family lead, not a canonical identity attachment. The image supports a Pulgar row with father/declarant Jose del Carmen Pulgar and mother Juana de Dios ... de Pulgar, but it does not securely support the derivative child full name or the mother surname.

## Conflict Map

- Child name: chunk reads `Pulgar Amagada / Jose Luis`; image review sees a `Pulgar Ama...` surname line, but the given-name line is not safely `Jose Luis` and appears closer to `Rosa Da...` or similar.
- Mother surname: chunk reads `Juana de Dios Amagada de Pulgar`; image review supports `Juana de Dios ... de Pulgar` but the middle surname remains uncertain.
- Birth event: chunk reads June 26, 1889 at 4:30 p.m., Calle Colon; image review supports June 1889, 4:30 p.m., and Calle Colon, while the exact day remains a QA target.
- Father/declarant: image review supports Jose del Carmen Pulgar / Jose del C. Pulgar, father, agriculturist, Calle Colon, but this should not be used to merge identities while the row remains blocked.
- Entry 515: image review sees a Neira row and marginal emendation, but lower-row mother completeness remains a blocker and should not be promoted from this packet.

## Identity Guardrails

Do not infer that `Amagada` equals `Arriagada`. Do not attach this entry to Dario Arturo Pulgar-Smith, Dario/Dario Jose Pulgar Arriagada, Jose del Carmen Segundo Pulgar Arriagada, or existing Jose/Juana pages from this evidence alone.

## Recommended Next Action

Run targeted conversion QA against the original image or a row crop for entry 513 child full name, sex, exact birth date/time, mother surname, and father/declarant wording; include entry 515 lower-row completeness in the same QA pass. After a QA-certified transcription exists, rerun proof review on separate atomic identity, birth-event, and parent-child claims.
