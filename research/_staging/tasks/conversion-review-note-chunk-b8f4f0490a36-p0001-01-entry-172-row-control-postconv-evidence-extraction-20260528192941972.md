---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528192941972"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528192941972.md"
conversion_confidence: "image_reviewed_row_control_with_converted_markdown_conflict"
conversion_qa_concern: "The current converted Markdown identifies entry 172 as a Burgos/de la Cruz birth, while source-image review and the assigned chunk identify physical row 172 as the Pulgar/Arriagada birth row."
uncertainty: "The father field is preserved only as Jose del Carmen Pulgar; a trailing mark or suffix after Pulgar is visible/possible but not certified for promotion."
literal_support: "Assigned chunk row 172 reads Jose del Carmen Segundo Pulgar Arriagada, father Jose del Carmen Pulgar S., mother Juana Arriagada de Pulgar, and informant Ernesto Herrera L.; direct image review confirms the row number 172 controls this Pulgar/Arriagada row but does not certify the father-name suffix."
promotion_recommendation: "hold_for_conversion_qa"
---

# Conversion Review Note: Entry 172 Row Control

Targeted review of the original source image, assigned chunk, current converted Markdown, and staged extraction history confirms a material derivative-transcript conflict.

The physical row numbered `172` on register page `58` is the Pulgar/Arriagada row. It is not the Burgos/de la Cruz row recorded in the current converted Markdown.

Certified extraction boundary from the image-controlled row:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, at about `tres de la tarde`, at `Calle de Valdivia`.
- Father: bounded to `Jose del Carmen Pulgar`; a possible trailing suffix or mark after `Pulgar` is not certified here.
- Father details: Chilean, employed, domiciled at `Calle de Colipi`.
- Mother: `Juana Arriagada de Pulgar`; Chilean, `Su sexo`, domiciled at `Calle de Colipi`.
- Informant/compareciente: `Ernesto Herrera L.`, present at the birth, age twenty-six, employed, domiciled at `Calle de Valdivia`.

The current converted Markdown instead records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. Preserve that as a conversion conflict and do not use the Burgos/de la Cruz derivative reading for this Pulgar/Arriagada source packet.

Because prior proof review specifically required conversion QA followed by proof review before canonical promotion, dependent claims and relationship candidates created by this worker remain at `hold_for_conversion_qa`. No canonical claim, relationship, identity merge, Dario-line attachment, or wiki update should be made from this extraction alone.
