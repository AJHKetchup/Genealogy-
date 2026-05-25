---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525230735548
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
promotion_recommendation: hold_for_conversion_qa
created: 2026-05-25
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. **Row-control blocker:** the assigned chunk/source packet and the current converted Markdown identify different entry-172 families. This is not a same-person variant.
2. **Father-field blocker:** the assigned chunk reads `Jose del Carmen Pulgar S.`, while prior reviewed notes in the workspace repeatedly keep the ending open as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. **Canonical-readiness blocker:** existing wiki pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` contain low/draft/probable evidence snapshots from earlier staged material, but the current conflict draft keeps those claims at `hold_for_conversion_qa`.
4. **Pulgar-line blocker:** this entry does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Darío/Dario Pulgar Arriagada. It can only provide a possible Jose/Juana parent-pair clue after row-control QA; it cannot bridge to any Dario identity by name alone.

## Literal Source Readings Kept Separate

### Assigned Chunk / Source Packet Reading

- Entry: 172, register page 58, registration date 7 April 1888.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: 8 March 1888 at 3 p.m.
- Place: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` by the assigned chunk/source packet.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employee, domiciled at `Calle de Valdivia`.

### Current Converted Markdown Reading

- Entry: 172, register page 58, registration date 7 April 1888.
- Child: `José Miguel`.
- Sex: `Varon`.
- Birth: 6 April 1888 at 10 p.m.
- Place: `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`, age 26, employee, domiciled `En esta`.

## Hypotheses And Evidence

### H1: Entry 172 controls as the Pulgar/Arriagada row

Evidence supporting:

- The assigned chunk explicitly transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The staged source packet for this task repeats the same Pulgar/Arriagada row and flags the converted Markdown as a row-control conflict.
- Multiple reviewed/staged conversion notes in the workspace state that image rereads support a Pulgar/Arriagada row, while keeping the father suffix unresolved.
- Existing canonical stubs already reflect earlier staged extraction for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`, but the evidence snapshot confidence for the child-mother relationship is only `1`, which matches the current hold posture.

Evidence against / unresolved:

- The current converted Markdown for the same source file identifies a different child, birth date, birthplace, father, mother, and informant.
- The father's final element is not proof-ready; `S.` may be a surname initial, mark, or over-read.

Scores:

- Identity confidence: 0.62 pending row-control QA.
- Conflict severity: 0.95 high.
- Evidence quality: 0.72 for the assigned chunk/source-packet reading; reduced because the derivative converted file conflicts.
- Conversion confidence: 0.35 for promotion from this packet as currently staged.
- Claim probability: 0.70 that the assigned chunk is pointing at a real Pulgar/Arriagada row; 0.40 that the exact father form includes `S.`.
- Relevance: 0.90 to Pulgar/Arriagada family reconstruction.
- Canonical readiness: 0.10; hold.

### H2: Entry 172 controls as the Burgos/de la Cruz row

Evidence supporting:

- The current converted Markdown transcribes entry 172 as `José Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, with internally coherent birth and informant details.

Evidence against / unresolved:

- The assigned chunk and current staged source packet for this exact task do not match this family.
- The conflict draft identifies the mismatch as row-level conversion conflict, not a name variant.
- The Burgos/de la Cruz row has no Pulgar/Arriagada relevance and provides no support for the staged Pulgar identity candidates.

Scores:

- Identity confidence: 0.30 pending row-control QA.
- Conflict severity: 0.95 high.
- Evidence quality: 0.55 within the converted Markdown only.
- Conversion confidence: 0.35 for promotion because the assigned chunk conflicts.
- Claim probability: 0.30 that this is the controlling row for the assigned task.
- Relevance: 0.05 to Pulgar-line work.
- Canonical readiness: 0.05; hold.

### H3: The father in H1 is the same person as canonical `Jose del Carmen Pulgar`

Evidence supporting:

- Existing wiki page `wiki/people/jose-del-carmen-pulgar.md` has a draft child link to `Tulio Cesar Luis Jose` from separate staged entry-513 material.
- Entry 172's father candidate shares the same base name `Jose del Carmen Pulgar`.
- Separate staged conversion notes for entry 513 mention a Pulgar family row with father/declarant `Jose del Carmen Pulgar` / `Jose del C. Pulgar`.

Evidence against / unresolved:

- Entry 172's father may include an unresolved suffix/mark after `Pulgar`.
- Entry 513's mother candidate is `Juana de Dios Amagada de Pulgar` or a contested variant, while entry 172's mother is `Juana Arriagada de Pulgar`.
- Same-name evidence alone is insufficient to merge the father candidates.

Scores:

- Identity confidence: 0.42.
- Conflict severity: 0.65 medium-high because a premature merge would affect parent-child relationships.
- Evidence quality: 0.50; staged derivative evidence with unresolved conversion QA.
- Conversion confidence: 0.30.
- Claim probability: 0.45 that the entry-172 father and existing `Jose del Carmen Pulgar` stub refer to the same man.
- Relevance: 0.85.
- Canonical readiness: 0.10; hold.

### H4: Entry 172 mother `Juana Arriagada de Pulgar` is the same person as `Juana de Dios Amagada de Pulgar`

Evidence supporting:

- Both names appear in Pulgar child contexts in the workspace.
- Both are mother/wife-style names ending `de Pulgar`.
- The forms `Arriagada` and `Amagada` could be confused in handwriting or conversion, but that is only a QA lead.

Evidence against / unresolved:

- The entry-172 staged packet gives `Juana Arriagada de Pulgar`; the separate entry-513 wiki/staged context gives `Juana de Dios Amagada de Pulgar` and has its own conversion conflict.
- `Arriagada` and `Amagada` are not safe spelling variants without image/proof review.
- The given-name expansion `de Dios` is absent from entry 172.

Scores:

- Identity confidence: 0.25.
- Conflict severity: 0.75 high if merged prematurely.
- Evidence quality: 0.45.
- Conversion confidence: 0.25.
- Claim probability: 0.30 that these are the same woman.
- Relevance: 0.80.
- Canonical readiness: 0.05; do not merge.

### H5: Entry 172 child is relevant to Dario Arturo Pulgar-Smith / Dario Arturo Pulgar / Dario Jose Pulgar-Arriagada / Darío Pulgar Arriagada

Evidence supporting:

- The child surname cluster `Pulgar Arriagada` is family-relevant.
- Existing wiki context includes a family-supplied canonical `Dario Arturo Pulgar-Smith`, and staged/canonical materials separately mention `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and `Darío/Dario Pulgar Arriagada`.
- The canonical `Dario Arturo Pulgar-Smith` page explicitly warns that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith require identity review before attachment.

Evidence against / unresolved:

- Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not any Dario.
- No birth year, parent pair, spouse, child, occupation, or residence bridge in this staged draft links the entry-172 child to any Dario candidate.
- `Dario Arturo Pulgar-Smith` is currently family supplied as Alexander John Heinz's maternal grandfather; the CV source title `Dario Arturo Pulgar` remains a separate document-level identity cluster needing bridge review.
- `Dario Jose Pulgar-Arriagada` and `Dario/Darío Pulgar Arriagada` are staged/canonical same-name clusters with insufficient evidence here to merge with either the entry-172 child or the Pulgar-Smith page.

Ranked Dario-related hypotheses:

1. **No Dario attachment from this entry yet**: strongest. This entry is a Jose/Juana/child identity and row-control problem, not a Dario proof item.
2. **Possible collateral Pulgar-Arriagada family clue**: plausible only after conversion QA certifies the Pulgar row and parent names.
3. **Direct bridge to Dario Arturo Pulgar-Smith or Dario Arturo Pulgar**: currently unsupported.
4. **Direct bridge to Dario Jose Pulgar-Arriagada or Darío/Dario Pulgar Arriagada**: currently unsupported.

Scores:

- Identity confidence for any Dario merge from this draft: 0.05.
- Conflict severity: 0.85 if used for a premature Dario merge.
- Evidence quality: 0.20 for Dario identity; the draft contains no Dario literal reading.
- Conversion confidence: 0.25 for Dario use; blocked by row-control conflict.
- Claim probability: 0.05 for direct identity attachment; 0.35 for future collateral relevance after QA.
- Relevance: 0.60 as a possible Pulgar-family clue, not as Dario evidence.
- Canonical readiness: 0.00 for Dario attachment.

## Conflict Findings

- **Same-person conflict:** Do not treat `Jose del Carmen Segundo Pulgar Arriagada` and `José Miguel` as the same child. The names, parents, birth dates, birthplaces, and informants differ materially.
- **Duplicate-person risk:** Existing wiki stubs for Jose/Juana candidates should not be consolidated from this task. Both row control and mother/father name forms remain unsettled.
- **Name-variant risk:** `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` is a literal-reading issue, not a proven name variant. `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar` is not a proven spelling variant.
- **Relationship conflict:** Parent-child relationships from entry 172 are blocked. If H1 is confirmed, the child-parent links can be proof-reviewed; if H2 is confirmed, the Pulgar/Arriagada parent links from this task should be rejected for this entry.
- **Chronology conflict:** H1 birth date is 8 March 1888 at 3 p.m.; H2 birth date is 6 April 1888 at 10 p.m. These cannot both describe the same entry-172 child.

## Recommended Next Action

1. Run targeted conversion QA for entry 172 using the source image, assigned chunk, current converted Markdown, and the staged source packet.
2. QA must decide whether entry 172 controls as the Pulgar/Arriagada row or the Burgos/de la Cruz row.
3. If the Pulgar/Arriagada row controls, certify the father field exactly as one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. Rerun proof review before promoting child identity, birth facts, father/mother claims, parent-child relationships, or any Jose/Juana duplicate-person analysis.
5. Defer every Dario attachment or Pulgar-Arriagada-to-Pulgar-Smith bridge until a separate identity-bridge proof review compares certified parent/child evidence against the existing Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, and Darío/Dario Pulgar Arriagada clusters.
