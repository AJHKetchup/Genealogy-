---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527195535080
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211540757.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row Conflict

## Blockers First

1. Keep all dependent child identity, birth, parent-name, residence, informant, and relationship claims on hold. The assigned chunk/source packet and the converted Markdown give incompatible readings for entry 172.
2. Do not certify `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, `Jose Miguel`, `Oswaldo Burgos`, or `Concepcion de la Cruz` as the controlling entry-172 row from this review alone.
3. The source image listed in the manifest and staged draft was not locally available at the recorded source path, and no page image was present under the manifest's `page-images/page-0001.png` path. This blocks direct visual verification.
4. Do not use this item as a Dario-line bridge. The staged draft, source packet, chunk, and converted Markdown reviewed here do not literally name Dario, Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada.
5. The father field cannot be resolved by proof review. It remains a conversion QA question whether the visible source supports `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Evidence Strengths

- The staged draft accurately identifies the row-level conflict between the assigned chunk/source packet and the converted Markdown.
- The assigned chunk and source packet agree with each other on a Pulgar/Arriagada reading for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, birth on 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The converted Markdown and page-markdown conversion agree with each other on a Burgos/de la Cruz reading for entry 172: child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth on 6 April 1888 at 10 p.m. in `En esta`.
- The source packet correctly treats the disagreement as a conversion row conflict rather than a spelling variant.
- The staged draft's anti-conflation warning is supported: no reviewed evidence supplies a literal Dario identity bridge or a relationship bridge from this entry to a Dario cluster.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the underlying civil birth register type; direct-source availability for this review is blocked |
| conversion_confidence_score | 2/10 for entry 172 because two local derivative transcripts conflict at the row level |
| evidence_quantity_score | 3/10 for row-control or identity claims; 6/10 for the narrow claim that a row-level conflict exists |
| agreement_score | 2/10 across all derivative artifacts; 8/10 within the Pulgar chunk/source-packet pair and 8/10 within the converted/page-markdown pair |
| identity_confidence_score | 2/10 for any entry-172 child or parent identity promotion; 0/10 for any Dario identity bridge |
| claim_probability | 0.85 that a serious conversion row conflict exists; 0.45 that the Pulgar/Arriagada row controls; 0.45 that the Burgos/de la Cruz row controls; 0.05 or lower for any Dario-line bridge |
| relevance_level | high for Pulgar/Arriagada research if the Pulgar row is certified; low for Dario-line identity proof from this item as currently reviewed |
| relevance_confidence | 0.80 for the conflict-review relevance; 0.20 for Dario-line relevance |
| canonical_readiness | hold; not ready for canonical identity, birth-fact, parent-child relationship, parent merge, or Dario bridge promotion |

## Review Finding

The staged identity/conflict analysis is supported as a cautionary analysis: it correctly blocks promotion because the derivative evidence is internally inconsistent. It should remain `hold_for_conversion_qa`.

This proof review cannot choose the controlling row because the local source image/page image was unavailable and the available derivative artifacts split into two incompatible but internally coherent readings. The conflict is too severe for a proof reviewer to resolve by preference or context.

The staged draft's broader warnings against Dario-line attachment are supported. None of the reviewed literal evidence contains a Dario name, a Smith surname, a spouse/child/grandchild bridge, or a chronology bridge sufficient to connect this entry to any Dario Pulgar cluster.

## Next Action

Run targeted conversion QA against the actual page image or source image. The QA note should identify which row is entry 172 and should record the father field only as far as the visible source supports: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that QA note exists, rerun proof review before promoting any child identity, birth event, parent-child relationship, parent same-person analysis, canonical wiki update, or Dario-line comparison.
