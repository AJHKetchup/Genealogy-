---
type: identity_conflict_analysis
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260525082133967
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525082133967.md"
conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 172 Conversion Blocker

## Family Cluster Under Review

If the current chunk is confirmed as the controlling row, entry 172 supports a family-relevant birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`.

## Source Conflict

The current chunk and copied source packet preserve the Pulgar/Arriagada row:

```text
Nombre. Jose del Carmen Segundo Pulgar Arriagada ... Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho ... Lugar. Calle de Valdivia ... Nombre del padre Jose del Carmen Pulgar S. ... Nombre de la madre Juana Arriagada de Pulgar
```

The assigned converted Markdown instead records entry 172 as a different child and parent pair:

```text
Nombres. José Francisco ... Fecha. El veinte i seis de Marzo de mil ochocientos ochenta i ocho ... Lugar. En esta ... Nombre del padre: Oswaldo Gomez ... Nombre de la madre: Emilia de la Cruz
```

This is a row-level conversion or assignment conflict. It is not a spelling normalization issue.

## Promotion Boundary

Do not promote any child identity, birth fact, parent-name claim, parent-child relationship, parental-pair clue, or parent merge from this evidence until targeted conversion QA decides the controlling row and records the father field exactly as source-visible.

The father field must remain unresolved as one of:

- `Jose del Carmen Pulgar`
- `Jose del Carmen Pulgar S.`
- `Jose del Carmen Pulgar [?]`

## Anti-Conflation Notes

This entry does not name Dario, Arturo, Smith, Dario Jose, Dario Pulgar Arriagada, Alexander John Heinz, or any later occupational/passenger/expropriation context. Treat any Dario-line comparison as negative or anti-conflation context unless a separate source provides an identity-bearing bridge.

Do not merge `Juana Arriagada de Pulgar` with separate `Juana de Dios Amagada de Pulgar` or `Juana de Dios Amador de Pulgar` readings from other entries based only on this staged note.

## Next Step

Send the source image, assigned converted Markdown, current chunk, and this staging set to targeted conversion QA. After QA, rerun proof review before any canonical promotion.
