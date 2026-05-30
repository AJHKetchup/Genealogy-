---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530013728268
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525123339261.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525123339261.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Conversion Conflict

## Blockers First

1. Keep this staged draft at `hold_for_conversion_qa`. The referenced converted Markdown and the referenced chunk still disagree materially about the literal row for entry 172.
2. Revise the staged draft's summary of the converted Markdown before reuse. The staged draft and source packet say the converted Markdown reads `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born `veinte i seis de Marzo`; the currently referenced converted file and page Markdown read entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril ... a las diez de la noche`.
3. The source image was not available at the referenced `raw/sources/...Entry No. 172;.png` path, and the manifest-listed `page-images/page-0001.png` was also absent in this workspace. I could not perform independent image reread, so no source-visible correction should be made from this review.
4. Do not promote the Pulgar/Arriagada birth facts, parent-child relationships, father-name suffix, or any Dario-line attachment from this draft. The derivative evidence chain is conflicted and image-level verification is missing.
5. Do not normalize or merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar`, and do not attach the entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Darío Pulgar Arriagada` by surname/context alone.

## Evidence Strengths

- The source type, if image-verified, is a civil birth registration, which is a strong source class for birth, parent, residence, and informant facts.
- The current chunk and source packet agree on the Pulgar/Arriagada reading for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, birth on 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The converted Markdown and page-level Markdown agree with each other on a different non-Pulgar row for entry 172: `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth on 6 April 1888 at 10 p.m. in `En esta`.
- The staged draft correctly treats the conflict as row-level and correctly blocks Dario-line attachment. Its final hold recommendation is supported even though its converted-file details need revision.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the civil-registration source class; 4/10 as reviewed here because the image was unavailable for direct verification |
| conversion_confidence_score | 3/10 overall; two derivative transcriptions disagree on the controlling row for entry 172 |
| evidence_quantity_score | 4/10; one source event is represented by multiple derivatives, but they are not independent evidence and conflict materially |
| agreement_score | 2/10 overall; chunk/source packet agree with each other, converted/page Markdown agree with each other, but the two derivative groups contradict each other |
| identity_confidence_score | 5/10 for the Pulgar/Arriagada staged identity cluster as a follow-up candidate; 2/10 for any same-person or Dario bridge |
| claim_probability | 0.55 that the Pulgar/Arriagada row is relevant to the intended staged task; 0.45 that the controlling converted row is the Burgos/de la Cruz row or that file assignment/chunking is wrong; 0.05 for Dario attachment |
| relevance_level | high for Pulgar/Arriagada conversion QA and anti-conflation controls; low for Dario identity proof |
| relevance_confidence | 0.85 for the QA need; 0.20 for any broader identity bridge |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is directionally sound as a hold note, not as promotion-ready proof. Its central blocker is supported: the entry-172 evidence chain has a material row-level conflict between the converted Markdown/page Markdown and the current chunk/source packet.

The draft should be revised before downstream use because it describes the converted Markdown with names and dates that do not match the current referenced converted file. That discrepancy reinforces the need for targeted conversion QA rather than resolving the claim here.

No reviewed text supports changing the record to a Dario identity, merging same-name Pulgar/Juana candidates, or promoting parent-child relationships. The father field `Jose del Carmen Pulgar S.` remains a chunk/source-packet reading only until the source image is restored and reread.

## Next Action

Restore or locate the source page image for SHA `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, then run targeted conversion QA against the image, converted Markdown, page Markdown, chunk, and source packet. The QA note should explicitly decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and should certify the father field only if the Pulgar row is confirmed.
