---
type: identity_conflict_analysis
status: draft
role: evidence_extractor
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
worker: postconv-evidence-extraction-20260527215759892
source_packet: "research/_staging/source-packets/chunk-3d3ab761209f-p0001-01-entry-513-pulgar-targeted-image-reread-hold-postconv-evidence-extraction-20260527215759892.md"
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

Entry 513 should remain a Pulgar family lead, not a canonical identity attachment. Targeted image reread confirms that the row is Pulgar-relevant and supports `Jose del Carmen Pulgar` / `Jose del C. Pulgar` as father/declarant, but the child full name and mother's intervening surname remain too unstable for promotion.

## Conflict Map

- Child name: the assigned chunk reads `Pulgar Amagada / Jose Luis`; the converted Markdown reads `Isolina del Carmen / Jose`; prior image-reviewed staging favored `Pulgar Arriagada / Dario Jose` or similar. The current reread confirms `Pulgar` and male sex but does not certify the full name.
- Mother surname: the assigned chunk reads `Amagada`, the converted Markdown reads `Amador`, and prior image-reviewed staging favored `Arriagada`. The current reread supports `Juana de Dios ... de Pulgar` and sees the surname as closer to `Arriagada` than `Amador`, but holds the field for QA.
- Birth event: the assigned chunk reads June 26, 1889 at 4:30 p.m.; the converted Markdown reads July 22, 1889 at 4:00 a.m.; the current reread favors June 22, 1889 at 4:30 p.m., Calle de Colon, but keeps the exact wording held.
- Father/declarant: image, chunk, and converted Markdown agree in broad substance on Jose del Carmen Pulgar / Jose del C. Pulgar as father/declarant, agriculturist, Calle de Colon. This field should not be used for identity merges while the row remains blocked.
- Entry 515: image review confirms entry 515 is a separate lower row and not support for entry 513 Pulgar claims.

## Identity Guardrails

Do not infer that `Amagada`, `Amador`, and `Arriagada` are equivalent variants. Do not attach this record to Dario Arturo Pulgar-Smith, Dario Jose Pulgar Arriagada, Jose del Carmen Segundo Pulgar Arriagada, Jose del Carmen Pulgar, Juana Arriagada de Pulgar, or Juana de Dios Amagada de Pulgar without a QA-certified transcription and proof-reviewed identity bridge.

## Recommended Next Action

Run formal conversion QA on the original image or a high-resolution crop for entry 513. The QA result should certify or explicitly bracket the child full name, sex, exact birth date/time, mother surname, father/declarant wording, and row boundaries for entries 513-515. After that, rerun proof review on separate atomic identity, birth-event, and parent-child claims.
