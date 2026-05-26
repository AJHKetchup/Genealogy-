---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526234346970
task_id: proof-review:research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-researcher-20260526231230332.md
staged_draft: research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-identity-researcher-20260526231230332.md
reviewed_source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526214615021.md
reviewed_conflict_draft: research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526214615021.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_qa_note: research/_staging/tasks/conversion-review-note-chunk-3d3ab761209f-p0001-01-entry-513-515.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entries 513 And 515 Conflict Candidates

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. The staged draft correctly treats the identity analysis as a scored hold, not a promotable conclusion.
- Entry 513 child identity is not proved. The current converted file and bdb698de chunk read `Isolina del Carmen Jose`, sex `Masculino`, but the prior image-reviewed QA note records a material competing child-name reading from another derivative chunk and keeps the child-name line unresolved.
- Entry 513 mother identity is not proved. The converted file and bdb698de chunk read `Juana de Dios Amador de Pulgar`, while the QA note records a conflicting `Juana de Dios Amagada de Pulgar` reading and states the maternal surname still needs targeted review.
- Entry 513 date/time is not reliable enough for promotion. The staged draft is supported in treating chronology as conflicted because the QA note records disagreement between `Julio veintidos ... cuatro de la manana` and a June/tarde-style reading.
- Entry 515 child identity is not proved. The converted file and bdb698de chunk read `Rosa Elvira del Carmen`, but the QA note records Neira/Ulloa-style conflict context and says the lower row is not fully confirmed.
- No same-person merge, canonical page rename, relationship attachment, or Dario-line bridge is supported from this packet.

## Evidence Strengths

- The source type is strong: a civil birth register page for Los Angeles, La Laja, Chile, 1889, page 172, entries 513-515.
- The converted file and reviewed bdb698de chunk agree with each other on the main derivative readings for entries 513 and 515.
- Entry 513 has meaningful Pulgar-family relevance. The image, converted file, chunk, source packet, and QA note all support a Pulgar family row with father/declarant `Jose del Carmen Pulgar` / `Jose del C. Pulgar` and male sex.
- The staged draft handles uncertainty appropriately by preserving `Amador`, `Amagada`, and other candidate readings as separate hypotheses rather than forcing a correction.
- The draft's negative Dario conclusion is supported: the reviewed materials do not name Dario, Arturo, Smith, Arriagada as a Dario bridge, passenger/medical facts, or any 20th-century identity link.

## Scores

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil register is a high-quality source type, but the page image has difficult handwriting and contested row-level fields. |
| conversion_confidence_score | 0.30 | The current converted file and chunk agree, but the prior QA note records material disagreements against image review on names, mother surname, and chronology. |
| evidence_quantity_score | 0.46 | There is one relevant register page plus derivative/QA layers; quantity is limited for identity resolution. |
| agreement_score | 0.38 | Agreement is good between the current converted file and current chunk, poor across the broader conversion/QA record. |
| identity_confidence_score | 0.28 | Pulgar-family relevance is likely, but exact child identity, mother surname, and cross-person matching remain unresolved. |
| claim_probability | 0.70 | Probability applies only to the narrow claim that entry 513 is Pulgar-family relevant through the father/declarant; exact identity claims are lower. |
| relevance_level | high | Entry 513 directly concerns a Pulgar father/declarant and a Juana de Pulgar mother candidate. |
| relevance_confidence | 0.86 | Family relevance is well supported even though identity promotion is blocked. |
| canonical_readiness | hold_for_conversion_qa | Targeted source-image reread is required before any canonical promotion. |

## Claim-Level Judgment

| Claim or hypothesis | Probability | Identity risk | Canonical readiness |
| --- | ---: | --- | --- |
| Entry 513 is a Pulgar-family male child record involving father/declarant `Jose del Carmen Pulgar`. | 0.70 | Moderate | hold_for_conversion_qa |
| Entry 513 mother is specifically `Juana de Dios Amagada de Pulgar`. | 0.56 | High | hold_for_targeted_crop_review |
| Entry 513 mother is specifically `Juana de Dios Amador de Pulgar`. | 0.38 | High | hold_for_targeted_crop_review |
| Entry 513 child is the same person as `Tulio Cesar Luis Jose`. | 0.25 | High | not_ready |
| Entry 515 child is securely `Rosa Elvira del Carmen`. | 0.32 | High | hold_for_conversion_qa |
| Entry 513/515 proves a bridge to any Dario Pulgar identity cluster. | 0.02 | Severe if asserted | not_supported |

## Required Next Action

Keep the staged draft on hold and send the page to targeted conversion QA. The QA pass should reread the original image for entry 513 child-name lines, sex, birth date/time, father/declarant details, and mother surname, and separately reread entry 515 child/father/mother fields. After a corrected or confidence-scored transcription exists, rerun proof review on atomic identity and relationship claims before any canonical edit.
