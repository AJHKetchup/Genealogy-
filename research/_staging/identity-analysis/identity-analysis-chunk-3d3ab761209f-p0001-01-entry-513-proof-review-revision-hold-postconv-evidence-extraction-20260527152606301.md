---
type: identity_conflict_analysis
status: draft
role: evidence_extractor
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
worker: postconv-evidence-extraction-20260527152606301
source_packet: "research/_staging/source-packets/chunk-3d3ab761209f-p0001-01-entry-513-pulgar-proof-review-revision-hold-postconv-evidence-extraction-20260527152606301.md"
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

Entry 513 should remain a registration-scoped Pulgar family lead, not a canonical identity attachment. The image supports a Pulgar row with father/declarant Jose del Carmen Pulgar and mother Juana de Dios Arriagada de Pulgar. The child surname appears to be Pulgar Arriagada, and the given-name line appears compatible with Jose Dario, but this reading is not yet QA-certified.

## Conflict Map

- Child name: chunk reads `Pulgar Amagada / Jose Luis`; converted file reads `Isolina del Carmen / Jose`; image review favors `Pulgar Arriagada / Jose Dario[?]`.
- Mother surname: chunk reads `Juana de Dios Amagada de Pulgar`; converted file reads `Juana de Dios Amador de Pulgar`; image review favors `Juana de Dios Arriagada de Pulgar`.
- Birth event: chunk reads June 26, 1889 at 4:30 p.m.; converted file reads July 22, 1889 at 4:00 a.m.; image review favors June 22, 1889 at 4:30 p.m., Calle Colon.
- Father/declarant: image review, chunk, and converted file broadly support Jose del Carmen Pulgar / Jose del C. Pulgar as father/declarant, but this field should not be used for identity merges while the row remains blocked.
- Entry 515: image review shows a separate Neira row and should not be used to support Pulgar-family claims from entry 513.

## Identity Guardrails

Do not infer that `Amagada`, `Amador`, and `Arriagada` are equivalent variants. Do not attach this entry to Dario Arturo Pulgar-Smith, Dario/Jose Dario Pulgar Arriagada, Jose del Carmen Segundo Pulgar Arriagada, or existing Jose/Juana pages from this evidence alone.

## Recommended Next Action

Run targeted conversion QA against the original image or a row crop for entry 513 child full name, sex, exact birth date/time, mother surname, and father/declarant wording; include entry 515 row-boundary and lower-row completeness in the same QA pass. After a QA-certified transcription exists, rerun proof review on separate atomic identity, birth-event, and parent-child claims.
