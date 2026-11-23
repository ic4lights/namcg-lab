# Proposal 074-f-tree-nonderivative-wave, round 3

## Result
Unchanged from round 2. Round 3 makes only the cross-reference fix F1 of scan-pass-2.md and adopts the optional
scope-sentence wording of review-r2.md. No mathematics, status sentence, label or in-place edit (E1-E3) changes.

## Target and status
Unchanged from proposal-r2.md (Problem F, OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; no label change proposed).

## Source reading
Digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT`. The full scan is
complete: pass 1 is in review-r2.md and passes 2-4 are in scan-pass-2..4.md. Live
`chapters/appH-microscopic-proofs.tex` sha256 = 29ac2a634bb819df7ecb29e138f97ae014656d4c0bb812b86f3573759a872046
(the pre hash; verified).

## Research and reasoning
F1: the vacuum-term display (pre L3055) is in the paragraph on the response of the scale of K. That paragraph sits
three paragraphs before the insert, so "the two preceding paragraphs" did not cover it. The sentence already names
"the reduced form of the paragraph on the response of the scale of K", so "that paragraph" is unambiguous.

## Claim classification
Unchanged from round 2.

## Proposed changes
File `chapters/appH-microscopic-proofs.tex`. E1-E3 are byte-identical to round 2, with the same anchors. E4 inserts
`appH_insert_r3.tex` (LF in the folder, CRLF on insertion) immediately before the unique line
`\section{Problem G: HBEV}`, as in round 2. The exact diff of `appH_insert_r3.tex` against `appH_insert_r2.tex`
is two in-line replacements and nothing else:

1. F1 (paragraph "The channel along y^mu y^nu", in the added passage):
```latex
% old
... the term \(-3\varpi/m^2\) of the leading symbol of the tree form is not among the terms of the displays of the two preceding paragraphs.
% new
... the term \(-3\varpi/m^2\) of the leading symbol of the tree form is not among the terms of the vacuum-term display of that paragraph or of the displays of the two preceding paragraphs.
```
2. Optional review-r2 wording (scope sentence), adopted:
```latex
% old
the conjugate-coordinate class with the supplied bilinear term and the matter fields at their vanishing background and \(C_{\mu\nu\lambda}=0\) on \(M\)
% new
the conjugate-coordinate class with the supplied bilinear term, the matter fields at their vanishing background and \(C_{\mu\nu\lambda}=0\) on \(M\)
```

## Verification scripts
- `make_insert_r3.py` builds `appH_insert_r3.tex` from `appH_insert_r2.tex` (kept). It asserts that each old
  string occurs exactly once and that the single status sentence stays at the end. Output is in
  `make_insert_r3_output.txt`.
- `apply_and_build_r3.py` is `apply_and_build_r2.py` with only the insert file name, the temp prefix and POST
  changed. It checks the pre hash, the E1-E3 anchors (each 1x, inside the intended paragraph), labels and
  process-language/label words. It then applies the edits to a copy outside the repository and, with `--build`,
  runs pdflatex, bibtex and pdflatex twice. Output is in `apply_and_build_r3_output.txt`.

Reproduction pack (run from the proposal folder):
- `python -I make_insert_r3.py`: expect `F1 display reference: old occurs 1x`, `W scope wording: old occurs 1x`,
  and insert sha256(LF) 75b89a9d200757fe7a13c0f70aeec3946c07d117b618a9a5f1b283212eb43bfd (9652 bytes).
- `python -I apply_and_build_r3.py --build`: expect the pre hash 29ac2a63...2046 to match, E1-E3 1x each and
  inside the paragraph, post sha256 84f9c61e066fa19fda86907a5651e551f35e3112bfba6697a76c1b0efee0224f (777025
  bytes, 3721 lines, 0 bare LF), 422 pages, 0 undefined/multiply-defined warnings, `BUILD CLEAN`, and the temp
  copy removed.

## Decisions Taken
- The optional review-r2 wording was adopted. It removes the double "and" and changes no content.
- No other edits.

## Milestone assessment
Routine.

## Status-label recommendation
None. Labels unchanged.

## Author decision needed
None.

## Remaining open step
Unchanged from proposal-r2.md.

## Special instructions for the gatekeeper
Check that the two replacements above are the only differences between appH_insert_r2.tex and appH_insert_r3.tex
(`diff`), and that E1-E3 are unchanged from round 2.
