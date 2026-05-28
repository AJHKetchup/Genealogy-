---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528132040772"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528132040772.md"
conversion_confidence: "image_reviewed_row_control_with_converted_markdown_conflict"
conversion_qa_concern: "The current converted Markdown identifies entry 172 as Burgos/de la Cruz, while original image review and the assigned chunk identify physical row 172 as Pulgar/Arriagada."
uncertainty: "Father field preserved only as Jose del Carmen Pulgar; a trailing suffix or mark after Pulgar is not promoted from this extraction."
literal_support: "Physical row 172 and assigned chunk support Jose del Carmen Segundo Pulgar Arriagada, father Jose del Carmen Pulgar, mother Juana Arriagada de Pulgar, and informant Ernesto Herrera L."
promotion_recommendation: "hold_for_conversion_qa"
---

# Conversion Review Note: Entry 172 Row Control

Targeted review of the original page image confirms that physical row `172` on register page 58 is the Pulgar/Arriagada row. The row is not the Burgos/de la Cruz entry recorded in the current converted Markdown.

Certified extraction boundary:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, at about `tres de la tarde`, at `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`; father details visible as Chilean, employed, domiciled at `Calle de Colipi`.
- Mother: `Juana Arriagada de Pulgar`; mother details visible as Chilean, `Su sexo`, domiciled at `Calle de Colipi`.
- Informant/compareciente: `Ernesto Herrera L.`, present at the birth, age twenty-six, employed, domiciled at `Calle de Valdivia`.

The current converted Markdown is materially inconsistent because it records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and birth on 6 April 1888. Preserve that disagreement as a conversion conflict. Do not use the Burgos/de la Cruz derivative reading for this Pulgar/Arriagada source packet.

Because proof review previously blocked promotion pending targeted conversion QA and rerun proof review, this revision keeps dependent claims and relationship candidates at `hold_for_conversion_qa`. No canonical claim, relationship, identity merge, Dario-line attachment, or wiki update should be made from this extraction alone.
