# Proposal 065-b-ward-measure-insertion-sublemma, local round 3

## Result

The mathematics is the same as in local r2. This round adds the three replacements the gatekeeper's full scan
requires (scan-pass-1 to scan-pass-3), using the scan's texts verbatim. It also adopts the optional measure wording
from scan-pass-3. The package is still a conditional sub-lemma and does not close anything. Problems B and D stay
OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Target and status

The target and status are as in proposal-local-r2.md, with no change: Problem B (sec:status-B), OPEN, CRITICAL PATH,
PROGRAMME-CONDITIONAL. Result type: PROGRAMME-CONDITIONAL sub-lemma.

## Source reading

Digest + targeted reads. `make_digest.py --check` printed DIGEST CURRENT, with dirty-chapters: yes. The full scan
for this package is the gatekeeper's scan-pass-1..4. I re-read the following:
- appH L437, the Foster2006 sentence;
- ch01 L245-262;
- ch03 L138-160 (eq:Smatrix is an action and specifies no measure; this motivates o1/o2);
- ch06 L350-400 (ass:EE and prop:ward are conditional);
- the bib entries FlissFrenkelHartnollSoni2025 (L994), Frenkel2023EdgeModes (L1052) and Foster2006;
- the labels sec:status-B (appH L155), sec:status-G (appH L2942), ass:EE, prop:ward and eq:Smatrix.

## Research and reasoning

None of the derivations changed. `derive_local_r2.py` was re-run. Its output is byte-identical to
`derive_local_r2.out` (both sha256 352c0aad...): 26 PASS, ALL PASS.

## Claim classification

The classification is unchanged from local r2. The new texts are classified as follows:
- **appH L437 replacement.** A literature-status statement. It narrows "no entropy has been identified" to "no
  definitive entropy expression is found" in Foster2006, and points to the later aether treatments already in the
  insert (ArataLiberatiNeri2026, ArataIsmailLiberati2026).
- **ch01 replacement.** A correction of an overstatement. Stationarity is Assumption ass:EE, used through the
  conditional prop:ward; its derivation stays open (Problem B). This matches ch06 L51-56, ch06 prop:ward and ch07
  L329-330.
- **Edge-modes clause.** A literature pointer. Both keys are already cited in sec:status-G.

## Proposed changes

### Diffs from local r2

| id | file | change | source |
|---|---|---|---|
| e1 | insert (`insert-local-r3.tex`) | Edge-modes clause added after the ChoudhuryLaurenzano2024 clause | scan-pass-2, verbatim |
| o1 | insert | First measure sentence reworded | scan-pass-3 optional wording, adopted |
| o2 | insert | Scope sentence reworded to match o1 | same wording, adopted |
| R1 | `chapters/appH-microscopic-proofs.tex` L437 | One sentence replaced | scan-pass-1, verbatim |
| R2 | `chapters/ch01-geometrogenesis.tex` L257-259 | Three lines replaced by six | scan-pass-3, verbatim |

Nothing else changes:
- The insertion point (before `\section{Problem C: conformal mode and Cassini}`) is unchanged.
- `bib_additions.bib` is unchanged (sha bda5b1bc...), and the bib post-state is identical to r2.
- No new bib entries are needed.

The insert, `insert-local-r3.tex`, has sha256 3b24011e5af9019e3c49760b25d5a819ede0fed33eef6845a6ee11a74034d4b0. It
is generated from `insert-local-r2.tex` (c8a2422b...) by `make_insert_local_r3.py`. That script asserts that each
old string occurs exactly once.

**e1.** The old text:
```latex
the entanglement of the black 0-brane with its Hawking radiation in the BFSS model~\cite{ChoudhuryLaurenzano2024};
```
The new text:
```latex
the entanglement of the black 0-brane with its Hawking radiation in the BFSS model~\cite{ChoudhuryLaurenzano2024}; block entanglement with edge modes in matrix quantum mechanics~\cite{FlissFrenkelHartnollSoni2025,Frenkel2023EdgeModes}, applied to a compact fuzzy factor in Section~\ref{sec:status-G};
```

**o1.** The old text:
```latex
For the flat Lebesgue matrix measure of Equation~\eqref{eq:Smatrix} the Jacobian term vanishes identically;
```
The new text:
```latex
For the flat Lebesgue measure on the matrix entries, with the action of Equation~\eqref{eq:Smatrix}, the Jacobian term vanishes identically;
```

**o2.** The old text:
```latex
the flat matrix measure of Equation~\eqref{eq:Smatrix}, Presentation~A
```
The new text:
```latex
the flat Lebesgue measure on the matrix entries with the action of Equation~\eqref{eq:Smatrix}, Presentation~A
```

**Why o1/o2 are adopted.** I adopt this wording because it is clearly better. eq:Smatrix (ch03 L141-155) defines
the action $S_{\mathrm{matrix}}$ and no integration measure, so "the flat matrix measure of
Equation~\eqref{eq:Smatrix}" attributes to the equation something it does not contain. The new wording separates the
measure (flat Lebesgue on the entries) from the action. o2 applies the same wording to the second occurrence (the
scope sentence) so that the paragraph does not describe the measure in two ways. That extension beyond the single
phrase in the scan is mine; the gatekeeper should confirm it.

### R1: `chapters/appH-microscopic-proofs.tex`, L437

The sentence occurs once. The rest of L437 is kept. The old sentence:
```latex
This is the form of the obstruction for the unit vector of Einstein-aether theory, where the derivation fails and no entropy has been identified~\cite{Foster2006}; here a compensating rotation exists but is rigid.
```
The new sentence:
```latex
This is the form of the obstruction for the unit vector of Einstein-aether theory, where the derivation fails and no definitive entropy expression is found~\cite{Foster2006} (later treatments of the aether contribution are recorded in the paragraph on the nearest published statements at the end of this section); here a compensating rotation exists but is rigid.
```
The apply script checks that "the end of this section" resolves. L437 and the insert's paragraph "Nearest published
statements and the reduced-action charge mechanism" are both inside sec:status-B, and that paragraph is the last one
before `\section{Problem C...}`.

### R2: `chapters/ch01-geometrogenesis.tex`, L257-259 (CRLF)

The old three lines occur once, and "It is a Ward identity of the" occurs once. L249-256 (including
eq:deltaS-preview) and L260 onward are kept. The old lines:
```latex
is not an extra thermodynamic slogan. It is a Ward identity of the
microscopic theory, and that identity forbids \(m_T^2\neq 0\) in the
infrared.
```
The new lines:
```latex
is not an extra thermodynamic slogan. It enters as the load-bearing
hypothesis of the framework, Assumption~\ref{ass:EE}, used in the form
of the conditional entanglement Ward identity of
Proposition~\ref{prop:ward}; under that hypothesis the identity forbids
\(m_T^2\neq 0\) in the infrared. Its derivation from the matrix theory
remains open (Problem~\ref{sec:status-B}).
```
Each of ass:EE, prop:ward and sec:status-B is defined exactly once. This text changes no label: "remains open"
restates the existing status of Problem B.

## Verification scripts

- `make_insert_local_r3.py` (output in `make_insert_local_r3.out`) builds the r3 insert from r2 with count-asserted
  edits e1, o1 and o2.
- `apply_build_local_r3.py` (output in `apply_build_local_r3.out`) works as follows:
  - It checks the pre-hashes of appH, bib and the live ch01.
  - It checks that each of the following occurs exactly once: the splice anchor, the header, the L437 sentence and
    the ch01 passage.
  - It splices the insert, applies R1 and R2, and appends the bib additions.
  - It checks that each edit changes only its own span, using round-trip reversal checks.
  - It checks the cite keys, the labels and the process-language words.
  - With `--build`, it builds a copy outside the repo. The copy is left in place at
    `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\8095df06-9555-40ba-b1c2-719eb5f35f33\scratchpad\build065r3`.
- `derive_local_r2.py` was re-run and its output saved as `derive_local_r2_rerun_r3.out`, which is identical to
  `derive_local_r2.out`.

### Reproduction pack

Run these commands from the proposal folder:
```
python -I make_insert_local_r3.py           # e1/o1/o2 occurrences 1,1,1; insert sha 3b24011e...
python -I apply_build_local_r3.py           # APPLY CHECK PASS
python -I apply_build_local_r3.py --build <new dir outside repo>   # 399 pp, 0 undefined, BUILD PASS
python -I derive_local_r2.py                # 26 PASS, ALL PASS (identical to derive_local_r2.out)
```

Pre- and post-hashes (sha256):

| file | pre | post |
|---|---|---|
| appH | 4d6d58cf7947dae9570e917ced6db8b6e40287437162321c4517eb726a568fce | 5106f9938be746607dd0b5fe6ecbf89a2918d795ffad7ee79d9ed7bf972d7681 (3538 CRLF, 0 bare LF) |
| bib | a7aec454de0f6591c157ecb4709179f212c876b6f0df5df67713df85bb0493ed | a0b2319a3d1cce3c616f188b6859b7a508d582c0f547786794662a73a80e2962 (same as r2; 111 entries) |
| ch01 | 3983506127bf8d2863dd5c0b56d7a5c7754fd63645a8a3a16913e646f77de284 | 8c08273aed9594162ef2358443314353c39a8cc34ffb2b47cd041eb0df7ab844 (388 CRLF, 0 bare LF) |
| insert | 3b24011e5af9019e3c49760b25d5a819ede0fed33eef6845a6ee11a74034d4b0 | (input) |

Build result:
- Passes: pdflatex 383 pp, then bibtex, pdflatex 399 pp, pdflatex 399 pp.
- There are 0 undefined or multiply-defined warnings and 0 bibtex warnings.
- All 11 of the 11 new keys are in the bbl.

## Decisions Taken

- **o1/o2 adopted.** eq:Smatrix is an action and not a measure, so the old wording was imprecise. The same wording is
  applied to both occurrences for consistency. I rejected two alternatives:
  - leaving the old wording, because it is imprecise;
  - changing only the first occurrence, because the paragraph would then describe the measure inconsistently.
- **R1 and R2 recorded as anchored replacements.** They are not new paragraphs. This is the smallest text, and it is
  verbatim from the scan.

## Milestone assessment

Routine.

## Status-label recommendation

No change. B and D stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. The current critical-path set (A, B, C, D1, E,
F, G-derived, N) is unaffected.

## Author decision needed

None.

## Remaining open step

The remaining open step is unchanged from local r2. It is a derivation from eq:Smatrix of fixed-volume stationarity
of the tensor block, which needs:
- locality or large-N factorisation, to turn contact identities into a Ward identity of the block;
- the fixed-volume constraint itself, derived rather than modelled as Tr(G1 B)=0;
- the edge-term selection.

## Special instructions for the gatekeeper

- Confirm that the o2 extension (the same wording at the second occurrence) is acceptable.
- R2 edits ch01. Integration touches three files (appH, bib and ch01).
- As in r2, integrate 065 before local 070. 070 re-anchors on 065's closing sentence followed by the Problem C header.
  That pair still occurs once in the post-state (asserted).
- No labels are added or changed.
