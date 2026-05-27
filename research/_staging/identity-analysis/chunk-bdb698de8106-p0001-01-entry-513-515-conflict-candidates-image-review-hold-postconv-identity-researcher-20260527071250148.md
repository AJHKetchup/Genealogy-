---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527071250148
task_id: "identity-analysis:research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-image-review-hold-postconv-evidence-extraction-20260527045039396.md"
staged_draft: "research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-image-review-hold-postconv-evidence-extraction-20260527045039396.md"
source_packet: "research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260527045039396.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md"
chunk_id: "CHUNK-bdb698de8106-P0001-01"
canonical_readiness: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Entry 513-515 Image-Review Hold

## Blockers First

1. The exact staged draft reviewed is `research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-image-review-hold-postconv-evidence-extraction-20260527045039396.md`.
2. The named `$genealogy-proof-review` skill was not installed in this session, so this note follows the task's proof-review evidence contract directly: literal support, uncertainty, source reliability, conversion confidence, claim confidence, identity risk, relationship jumps, conflicts, relevance, claim probability, and canonical readiness.
3. Entry `513` has identity-controlling conflicts in the child-name field, birth date/time field, and mother-surname field. These conflicts block canonical person matching and parent-child promotion.
4. Entry `515` is a separate lower row and is usable here only as a row-boundary control. It must not be used as Pulgar-family evidence for entry `513`.
5. The father/declarant reading `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, role `Padre`, profession `Agricultor`, and residence `Calle Colon` is comparatively strong, but it remains scoped to this unstable entry `513` row until conversion QA.
6. The mother field must remain unresolved as `Juana de Dios Amador de Pulgar` versus `Juana de Dios Ama[?]gar` / `Ama[?]gada de Pulgar`. Do not silently normalize this to `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, or any other Juana page.
7. No evidence in this staged draft names `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Dario Pulgar Arriagada`. Pulgar-line comparison is anti-conflation only.

## Literal Source Readings

Converted/chunk layer for entry `513`:

```text
Nombre. Isolina del Carmen / Jose ... Sexo. Masculino
Fecha. El mismo veinte dos ... a las cuatro de la manana. Lugar. Calle Colon
Nombre del padre. Jose del Carmen Pulgar ... Prof. Agricultor ... Domicilio. Calle Colon
Nombre de la madre. Juana de Dios Amador de Pulgar
Jose del C. Pulgar ... Padre ... Edad. Cuarenta i siete Anos ... Prof. Agricultor ... Dom. Calle Colon
```

Image-reviewed layer preserved by the staged draft and source packet:

```text
513 child name appears to begin Pulgar Rosa ... with following given-name lines uncertain; Sexo. Masculino.
513 birth field appears to read Junio veinte i dos ... a las cuatro i media de tarde.
513 father reads Jose del Carmen Pulgar; father/declarant profession reads Agricultor; domicile reads Calle Colon.
513 declarant reads Jose del C. Pulgar, Padre, Edad Cuarenta i siete Anos.
513 mother reads Juana de Dios Ama[?]gar or Ama[?]gada de Pulgar.
515 lower row confirms a separate non-Pulgar entry boundary.
```

## Interpretation Boundary

The source cluster is relevant to Pulgar-line research because it appears to name a father/declarant `Jose del Carmen Pulgar` in entry `513`. That relevance does not prove the child identity, the mother identity, a spouse relationship, a duplicate-person merge, or a Dario-line bridge. Literal source readings remain separated above from the ranked hypotheses below.

## Hypotheses And Evidence

### H1: Entry 513 Is A Pulgar-Family Birth Row With Unresolved Child Identity

Supporting evidence: the staged conflict draft, current source packet, converted file, and chunk all keep entry `513` on register page `172`. Both the derivative layer and image-review layer support a father/declarant named `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, role `Padre`, profession `Agricultor`, and residence `Calle Colon`. The image-review layer sees a child-name field beginning with `Pulgar...` and confirms sex `Masculino`.

Conflicts: the derivative child reading is `Isolina del Carmen / Jose`; image review instead sees a likely `Pulgar Rosa ...` beginning with uncertain following lines. The birth date/time and mother surname also disagree. The row is likely Pulgar-relevant, but the child's identity cannot be promoted.

Scores: identity confidence 0.58; conflict severity 0.86; evidence quality 0.62; conversion confidence 0.28; claim probability 0.64; relevance 0.90; canonical readiness `hold_for_conversion_qa`.

### H2: Entry 513 Child Is `Isolina del Carmen Jose`

Supporting evidence: the converted Markdown and chunk transcribe the child-name field as `Isolina del Carmen / Jose` and the row as male.

Conflicts: the staged image review says the visible child name appears instead to begin `Pulgar Rosa ...` and that the converted `Isolina del Carmen` reading is not supported by that review. A female-looking given-name string paired with `Masculino` also increases identity risk unless the literal source is rechecked.

Scores: identity confidence 0.22; conflict severity 0.86; evidence quality 0.36; conversion confidence 0.28; claim probability 0.20; relevance 0.62; canonical readiness `not_ready`.

### H3: Entry 513 Child Is A `Pulgar Rosa ... Jose` Or Similar Image-Reviewed Name

Supporting evidence: the staged draft and source packet preserve an image-reviewed child-name beginning `Pulgar Rosa ...` with a later `Jose` line and sex `Masculino`. This is more compatible with the father/declarant `Jose del Carmen Pulgar` as a Pulgar row than the converted child-name reading.

Conflicts: the image-reviewed name is explicitly uncertain and not a final replacement transcription. The given-name sequence, surname order, and whether `Rosa` is part of the child's name or a line-boundary/reading artifact remain unresolved.

Scores: identity confidence 0.46; conflict severity 0.82; evidence quality 0.54; conversion confidence 0.28; claim probability 0.52; relevance 0.86; canonical readiness `hold_for_conversion_qa`.

### H4: `Jose del Carmen Pulgar` And `Jose del C. Pulgar` Are The Same Row-Local Father/Declarant

Supporting evidence: the row has father `Jose del Carmen Pulgar`; the compareciente/declarant reads `Jose del C. Pulgar`, role `Padre`, age `Cuarenta i siete Anos`, profession `Agricultor`, domicile `Calle Colon`. The abbreviation `C.` is row-local and consistent with `Carmen`.

Conflicts: this row-local equivalence does not prove that every `Jose del Carmen Pulgar` in the workspace is the same person. The canonical stub `wiki/people/jose-del-carmen-pulgar.md` exists and already has staged child-link context, but name-core overlap alone is not enough to merge entry `513` with entry `172` father candidates or any other Jose page.

Scores: identity confidence 0.72 for row-local father/declarant equivalence; conflict severity 0.42; evidence quality 0.72; conversion confidence 0.46; claim probability 0.76; relevance 0.88; canonical readiness `hold_for_row_conversion_qa`.

### H5: Entry 513 Mother Is `Juana de Dios Amador de Pulgar`

Supporting evidence: the converted Markdown and chunk transcribe the mother field as `Juana de Dios Amador de Pulgar`.

Conflicts: the staged image review does not secure `Amador`; it preserves alternatives `Ama[?]gar` or `Ama[?]gada de Pulgar`. Promoting `Amador` would treat a disputed derivative reading as settled.

Scores: identity confidence 0.28; conflict severity 0.76; evidence quality 0.38; conversion confidence 0.28; claim probability 0.26; relevance 0.78; canonical readiness `not_ready`.

### H6: Entry 513 Mother Is `Juana de Dios Ama[?]gar` / `Ama[?]gada de Pulgar`

Supporting evidence: the staged draft and source packet preserve the image-reviewed mother line as closer to `Juana de Dios Ama[?]gar` or `Ama[?]gada de Pulgar`. Existing wiki context has `wiki/people/juana-de-dios-amagada-de-pulgar.md`, but that page must remain a candidate/stub and not a proof substitute.

Conflicts: the exact surname letters are unresolved. `Ama[?]gada` may look similar to `Amagada`, but the current staged draft does not certify the canonical spelling. It also does not bridge this Juana to `Juana Arriagada de Pulgar` from the separate entry `172` cluster.

Scores: identity confidence 0.50; conflict severity 0.76; evidence quality 0.56; conversion confidence 0.28; claim probability 0.54; relevance 0.82; canonical readiness `hold_for_conversion_qa`.

### H7: `Juana de Dios Ama[?]gada de Pulgar` Equals `Juana Arriagada de Pulgar`

Supporting evidence: both are local Jose/Juana/Pulgar parent-candidate contexts, and both appear near Pulgar-line research in the workspace. Entry `172` context separately records `Juana Arriagada de Pulgar` as mother of `Jose del Carmen Segundo Pulgar Arriagada`.

Conflicts: the names differ materially (`de Dios`, uncertain `Ama...` versus `Arriagada`), the children/entries differ, and this entry `513` draft has no direct bridge to entry `172`. Similar married-name form `de Pulgar` is not identity proof.

Scores: identity confidence 0.16; conflict severity 0.82 if merged prematurely; evidence quality 0.22; conversion confidence 0.28 for entry `513`; claim probability 0.14; relevance 0.52; canonical readiness `not_ready`.

### H8: Entry 515 Belongs To The Same Pulgar Family Cluster

Supporting evidence: entry `515` is on the same register page and is mentioned in the staged conflict draft.

Conflicts: the staged draft explicitly says entry `515` is a separate lower row and should only be used as a row-boundary control. Existing staged relationship notes also treat entry `515` as partial/unstable and non-Pulgar for this task.

Scores: identity confidence 0.08; conflict severity 0.70 if used as Pulgar evidence; evidence quality 0.30; conversion confidence 0.25; claim probability 0.05; relevance 0.18 except as row-boundary control; canonical readiness `not_ready`.

### H9: Entry 513 Bridges To `Dario Arturo Pulgar-Smith` Or `Dario Arturo Pulgar`

Supporting evidence: the Pulgar surname and the row-local father/declarant `Jose del Carmen Pulgar` make this a possible future Pulgar-line lead. Existing canonical context identifies `Dario Arturo Pulgar-Smith` from family-supplied knowledge, and staged CV contexts elsewhere use `Dario Arturo Pulgar`.

Conflicts: entry `513` does not name Dario, Arturo, Smith, Pulgar-Smith, a grandchild, a spouse, a later occupation, or any lineage bridge. The row is also not conversion-stable enough to use as a parentage anchor.

Scores: identity confidence 0.06; conflict severity 0.90 if attached prematurely; evidence quality 0.18; conversion confidence 0.28; claim probability 0.04; relevance 0.30 as a future lead only; canonical readiness `not_ready`.

### H10: Entry 513 Bridges To `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, Or `Dario/Dario Pulgar Arriagada`

Supporting evidence: local workspace context has separate Dario/Pulgar-Arriagada clusters, and entry `513` may eventually clarify a Jose/Juana/Pulgar parent candidate if conversion QA confirms the row.

Conflicts: this draft does not name Dario or Arriagada. The mother field is disputed as `Amador` versus `Ama[?]gar` / `Ama[?]gada`; it cannot be normalized to `Arriagada`. No age, birth date, medical-title, passenger, property, CV, or family-chain bridge connects this row to any Dario Pulgar Arriagada candidate.

Scores: identity confidence 0.05; conflict severity 0.90 if merged prematurely; evidence quality 0.16; conversion confidence 0.28; claim probability 0.03; relevance 0.36 as anti-conflation context; canonical readiness `not_ready`.

## Conflict Types

- Same-person conflict: high risk if `Isolina del Carmen Jose`, `Pulgar Rosa ... Jose`, and any later normalized child name are treated as the same person before conversion QA.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` if entry `513`, entry `172`, and canonical stub references are merged by name alone.
- Name-variant risk: high for `Amador`, `Ama[?]gar`, `Ama[?]gada`, `Amagada`, and `Arriagada`; these must remain literal alternatives or separate candidates until proof review accepts a bridge.
- Relationship-conflict risk: high if parent-child links are promoted while the child name and mother surname are unresolved.
- Chronology-conflict risk: moderate for entry `513` birth date/time because the derivative transcript reads same-day/four a.m. while image review suggests June 22/four-thirty p.m.; high for any Dario attachment because no Dario chronology is present.

## Ranked Findings

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | Entry `513` is Pulgar-relevant because the father/declarant is likely `Jose del Carmen Pulgar` / `Jose del C. Pulgar` | 0.76 row-local father/declarant equivalence | Hold for conversion QA; proof-review father/declarant after child and mother fields are stabilized. |
| 2 | Entry `513` is a Pulgar-family birth row, but the child identity is unresolved | 0.64 | Preserve as staged identity conflict; do not create or attach a canonical child. |
| 3 | Mother field likely reads an `Ama... de Pulgar` form rather than secure `Amador` | 0.54 | Run targeted conversion QA on the mother surname; keep `Amador`, `Ama[?]gar`, and `Ama[?]gada` separate literal readings. |
| 4 | Converted child reading `Isolina del Carmen Jose` controls the row | 0.20 | Treat as disputed derivative transcription; do not promote. |
| 5 | `Juana de Dios Ama[?]gada de Pulgar` equals `Juana Arriagada de Pulgar` | 0.14 | Preserve as separate Juana candidates pending direct identity-bridge proof review. |
| 6 | Entry `515` supports a Pulgar-family inference | 0.05 | Use entry `515` only as a row-boundary control. |
| 7 | Entry `513` bridges to `Dario Arturo Pulgar-Smith` / `Dario Arturo Pulgar` | 0.04 | Do not attach; require separate identity-bridge proof review using direct Dario-line evidence. |
| 8 | Entry `513` bridges to `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Dario Pulgar Arriagada` | 0.03 | Do not merge; preserve as anti-conflation context only. |

## Recommended Next Action

Run targeted conversion QA on entry `513` from the source image, converted Markdown, chunk, and source packet. The QA note should certify or explicitly uncertainty-mark: the full child-name field, sex, birth date/time, father/declarant name and role, and mother surname. The exact proof-review step after QA is a narrow row-level proof review for entry `513` that decides whether the father/declarant can be accepted as `Jose del Carmen Pulgar` / `Jose del C. Pulgar` and whether any child-parent relationship can be staged.

Do not promote `Isolina del Carmen Jose`, `Pulgar Rosa ...`, `Juana de Dios Amador de Pulgar`, `Juana de Dios Amagada de Pulgar`, or any child-parent relationship from this draft. Do not merge `Jose del Carmen Pulgar` with other Jose candidates, do not merge `Juana de Dios Ama[?]gada de Pulgar` with `Juana Arriagada de Pulgar`, and do not attach this source cluster to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Dario Pulgar Arriagada` without a later identity-bridge proof review that names direct bridging evidence.
