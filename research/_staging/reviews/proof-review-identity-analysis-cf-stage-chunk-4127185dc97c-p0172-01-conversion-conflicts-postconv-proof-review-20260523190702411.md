---
type: proof_review
role: claim_reviewer
status: complete
worker: postconv-proof-review-20260523190702411
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md
staged_draft: research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md
referenced_conflict_draft: research/_staging/conflicts/CF-STAGE-CHUNK-4127185dc97c-P0172-01-conversion-conflicts.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-4127185dc97c-P0172-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
reviewed_at: 2026-05-23
source_quality_score: 0.86
conversion_confidence_score: 0.31
evidence_quantity_score: 0.74
agreement_score: 0.47
identity_confidence_score: 0.38
claim_probability: 0.93
relevance_level: critical
relevance_confidence: 0.98
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Identity Analysis Conversion Conflicts

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The staged identity-analysis draft is supported as a warning/hold judgment only; it does not establish any canonical person, relationship, same-person, duplicate-person, or lineage claim.
- Citation/version mismatch remains material. The source packet and staged draft cite `CHUNK-4127185dc97c-P0172-01` and converted sha `4127185dc97c...`, while the currently restored chunk front matter identifies `CHUNK-d6a12b291d94-P0172-01`, the chunk file hash is `C08EC9A20B2A977CB5D0030AE2C42A93B7DD2FBC649AF4D2F9239B3E77E3105A`, and the current converted-file hash is `E17DA442A810171D5D0C72B49EEA0DF0D94E9DB2987AF8786BDD52E958708C31`.
- The staged draft contains stale availability context. It says the referenced `page-0172-chunk-01.md` was not present and points to `page-0001-chunk-01.md` as the available chunk; in this rerun, `page-0172-chunk-01.md` is present, but it carries a different chunk id/checksum set than the assigned draft.
- Entry 513 remains a proof-risk item. The current converted file and restored chunk read `Tulio Cesar Luis José`, father/declarant `José del Carmen Pulgar` / `José del C. Pulgar`, and mother `Juana de Dios Amagada de Pulgar`. The older conflict draft literal support instead preserves `Isidoro del Carmen Diaz`, and the source packet flags the child field as closer to a Pulgar surname with given names closer to `Jose Dani...`. The image supports the need for targeted QA and does not make the staged identity analysis promotion-ready.
- Entry 514 remains a material relationship-risk item. The current conversion/chunk read father `Belisario Riquelme`, mother/declarant `Mercedes Riquelme`, and child `Rigoberto Juan Bautista`; the source packet and visible image review leave a serious competing reading that the father field may be unknown (`se ignora`-like). Do not promote a named father relationship from this staged draft.
- Entry 515 remains a surname and parentage-risk item. The current conversion/chunk read father/declarant `Pedro Pablo Leiva` and mother `Carmen Fuentes`; the conflict draft/source packet flag `Neira` as a serious competing reading, and the source image appears consistent with a `Pedro Pablo Neira`-type concern. Do not promote Leiva/Neira identity or parentage from this review.
- No literal `Dario`, `Arturo`, `Smith`, `Dario Jose`, or confirmed `Arriagada` identity appears in the reviewed source image, source packet, conflict draft, converted file, or restored chunk. Any Pulgar-to-Dario comparison in the staged identity analysis is relevant only as an anti-conflation warning.

## Evidence Strengths

- The source class is strong: a direct civil birth-register page image for Los Anjeles/La Laja, Chile, 1889.
- Page-level support is good. The source image visibly supports page 172, the 1889 birth-register context, and entries 513, 514, and 515.
- The staged identity-analysis draft, referenced conflict draft, and source packet all converge on the practical outcome: hold affected claims for conversion QA before canonical use.
- The restored converted/chunk text gives a coherent derivative transcription for page 172, so it is usable as a QA target. It is not reliable enough for promotion because several key identity and relationship fields are directly challenged by the source packet and image-level review.
- Some narrow readings are plausible enough to guide the next QA pass, especially entry 513 `José del Carmen Pulgar` / `José del C. Pulgar` and entry 514 `Mercedes Riquelme`. These are guideposts, not promoted conclusions.

## Scores

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 0.86 | Civil registration is a high-value source class, but the scan contrast, handwriting, and page cropping make multiple fields difficult. |
| conversion_confidence_score | 0.31 | The current converted file and restored chunk agree with each other, but they conflict with the older conflict draft, source-packet QA concerns, and several visible image readings. |
| evidence_quantity_score | 0.74 | Reviewed the exact staged identity analysis, referenced conflict draft, source packet, converted file, restored page-172 chunk, and source image; no external research or canonical-page context was used. |
| agreement_score | 0.47 | Agreement is strong for page identity and entry numbers, mixed for entry 513 Pulgar context, and weak for disputed child names, father fields, and Leiva/Neira surname readings. |
| identity_confidence_score | 0.38 | Page identity is clear, but individual identities and relationships in entries 513-515 are not settled enough for canonical use. |
| claim_probability | 0.93 | It is highly probable that the correct proof judgment is to keep this staged identity analysis on conversion-QA hold. |
| relevance_level | critical | The disputed fields directly affect identity, parentage, duplicate-person risk, and canonical readiness. |
| relevance_confidence | 0.98 | The reviewed files are the exact staged draft and the directly referenced page-172 evidence set. |
| canonical_readiness | hold_for_conversion_qa | Reconcile chunk/version metadata and re-proof disputed fields against the source image before promotion. |

## Judgment

The staged draft is supported as a conversion-conflict and anti-conflation analysis. Its core recommendation to hold is stronger than any person-level claim it discusses. It should not be used to create, merge, rename, attach, or promote any person or relationship in canonical folders.

The current restored page image improves reviewability, but it does not remove the blockers. It shows why the source packet's caution is justified: the page frame is readable, while the contested names and relationship fields need targeted field-level conversion QA.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. The next action is to reconcile the staged `CHUNK-4127185dc97c-P0172-01` metadata with the restored `CHUNK-d6a12b291d94-P0172-01` chunk, then perform targeted side-by-side QA for entry 513 child name and mother surname, entry 514 father field, and entry 515 Leiva/Neira surname. After that, rerun proof review on specific claims rather than promoting from this identity-analysis draft.
