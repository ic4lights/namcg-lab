VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
The r2 insert differs from r1 only by the six replacements I specified in review-r1. All four major findings (F1–F4) and both minor findings (F5, F6) are closed, and the r1 mathematics is unchanged.

## What I checked
**Diff of appH_insert_r1.tex against appH_insert.tex (CR stripped).** Exactly four lines differ: lines 4, 14, 16 and 18. The changes are the six replacements and nothing else:
- Line 4 (Covariant variables): the weight clause "Densities carry the factor √|γ| … √G = ρ²√|γ|" is inserted (F5).
- Line 14 (Compensation): the sentence now uses Stokes on the Cauchy surface. It says the boost charge of the shift of T_η equals the shift of the Σ-charge minus the flux of Q at spatial infinity. It restricts the claim to compactly supported variations of f and keeps the term at infinity, with a remark on constant f (F1).
  - "the same freedom is" has become "this freedom corresponds to" (F6).
- Line 16 (Consequence):
  - The Iyer–Wald wording and the clause "T_η … not identified here with T^op_{μν} of Eq. (first-law)" are added (F4).
  - The reworded n_D=0 sentence now reads c_A−c_T=4κ_X, and G_A=G_T holds iff the replica's edge term contributes the r=−4 coefficient (F2).
  - The new constraint-term sentence gives the covariantised-composite scope and says it is the charge listed as not computed in the comparator and order-Λ² paragraphs (F3).
- Line 18 (scope paragraph): "do not identify T_η with T^op_{μν} of Equation (first-law)" is added.

**Byte and syntax check:**
- Size is 8952 bytes, with 0 CR, 0 TAB, 0 non-ASCII and 0 control bytes other than LF.
- Braces are net 0, `\(`/`\)` are net 0, there is one `\[ … \]` pair, and the file ends with LF.

**Anchor and labels, against the clean working tree:**
- `\section{Problem C: conformal mode and Cassini}` occurs exactly once.
- It is immediately preceded by a blank line and then the 041 Moser-variables paragraph. That paragraph's last sentences are "They derive no local Lorentz symmetry. Problems~B and~D remain open and PROGRAMME-CONDITIONAL."
- The title "Covariant variables, the joint flow" occurs 0 times.
- `eq:first-law` is defined exactly once (ch06). `eq:Top-FP` was unique in r1 and is unchanged.
- The cite keys are unchanged. A scratch compile of the current tree gives 313 → 315 pages with 0 undefined references and 0 duplicate labels. That is the proposal's evidence; I did not re-run pdflatex.

**Re-verification of the r1 mathematics.** None of it changed, so the r1 checks stand: s1–s4 and my analytic proof of the compensation identity. The r1 full scan also stands for this item.

## Exactly what is accepted
Accepted text: the full contents of `proposals/042-constrained-noether-charge/appH_insert.tex` (r2, 8952 bytes), verbatim, converted to CRLF.

Insertion point: in `chapters/appH-microscopic-proofs.tex`, immediately before the unique line `\section{Problem C: conformal mode and Cassini}`, after the 041 Moser-variables paragraph, with one blank line between them.

No other file or chapter text is to be edited. There are no label changes: B, D and A stay `Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL` (A's priority reads "CRITICAL PATH for the matrix-derived label"). The result is conditional and does not derive a critical-path step. It is not a breakthrough and no milestone trigger fires. The scope and the ranked open avenues are as in review-r1.

Unrelated, pre-existing and not part of this item: the hard-coded "Theorem 7.3 / 7.3–12.4", "Appendix D" and "Assumption E.1" references in ch16 and appE.
