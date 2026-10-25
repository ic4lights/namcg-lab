# Proposal 042-constrained-noether-charge, round 2

## Result

The mathematics, the claims and the scope are unchanged from r1; see proposal-r1.md for the derivation, the claim table, the scripts and the ranked avenues. The gatekeeper's r1 verdict was ACCEPT WITH REQUIRED REVISIONS: 4 major findings, 2 minor, no PRIOR-CLAIM-ERROR, and a full scan. This round, r2, applies the six verbatim replacements from the review's "Corrected snippet" section and makes no other edits.

## How each finding was applied

The r1 block is saved unchanged as `appH_insert_r1.tex`. The script `make_r2_insert.py` performs the replacements; its output is in `make_r2_insert.out.txt`. Before replacing, it asserts that each old string occurs exactly once in the r1 block, and all six did.

1. **F1 (major), Compensation paragraph.** Applied replacement (1). The sentence now invokes Stokes' theorem with the flux at spatial infinity, restricts to variations of f of compact support, notes that the improvement vanishes for constant f, and says the freedom "corresponds to" the ambiguity Θ→Θ+dY.
2. **F6 (minor), "corresponds to".** This is covered by replacement (1).
3. **F4 (major), first sentence of Consequence.** Applied replacement (2). The sentence now reads "the Iyer--Wald identity for the induced density does not select r", and it adds that T_η is not identified with T^op of Eq. (first-law).
4. **F2 (major), the n_D=0 sentence.** Applied replacement (3). It now states c_A−c_T=4κ_X, and that G_A=G_T holds if and only if the edge term contributes −4κ_X.
5. **F3 (major), constraint term.** Applied replacement (4), using the literal string `\(b=F[\Theta]\)` present in the file. The sentence now gives the scope, "covariantised composite ... computed only in this setting", and says this is the charge that the comparator and order-Λ² paragraphs list as not computed. No edits are made to those older paragraphs, as the gatekeeper specified.
6. **F5 (minor), weight clause.** Applied replacement (5). After the sentence on the torsion of e, the text adds that √|γ| is 1 in the matrix chart and that √G=ρ²√|γ|.
7. **F4 (major), final scope paragraph.** Applied replacement (6), "do not identify T_η with T^op of Equation~\eqref{eq:first-law}".

## Mechanics

`appH_insert.tex` (r2):
- 8952 bytes, UTF-8, LF.
- 0 CR, 0 TAB, 0 non-ASCII characters, and no control bytes other than LF.
- Braces have net 0. `\(` and `\)` have net 0. There is one `\[` and one `\]`.
- `\label{eq:first-law}` is defined exactly once, in chapters/ch06-entanglement-equilibrium.tex. The other references are unchanged: `eq:Top-FP`, `IyerWald1994` and `JacobsonKangMyers1994`.
- There is still a single closing status sentence.

The anchor is unchanged: insert immediately before the unique line `\section{Problem C: conformal mode and Cassini}`.

Scratch compile with `compile_check.py`:
- It built a copy of the CURRENT working tree outside the repository, which was then deleted.
- It ran pdflatex, bibtex, pdflatex, pdflatex; all exit codes were 0.
- Baseline: 313 pages. With the insert: 315 pages.
- 0 undefined references, 0 undefined citations, 0 multiply defined labels.

## Decisions Taken, milestone, labels, author decision

- **Decisions Taken:** none new.
- **Milestone:** routine.
- **Labels:** no change.
- **Author decision needed:** none.
- **Remaining open step:** as in r1. The gatekeeper ranked T^op of Chapter 7 first.

## Special instructions for the gatekeeper

Confirm that the six replacements appear verbatim, then diff `appH_insert.tex` against `appH_insert_r1.tex`. The integrator should run `scripts/build_check.py` after integration.
