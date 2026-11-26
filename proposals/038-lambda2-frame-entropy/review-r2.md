VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All r1 findings (F1-F3) are applied correctly, and the rest of the block is unchanged byte for byte.

## Source reading
Digest plus targeted reads. I diffed `appH_insert_r1.tex` against `appH_insert.tex` and re-checked the anchor, the bib keys and the block bytes. I did not do a full scan. CLAUDE.md 3(d) applies and was satisfied in r1 by reading the affected Appendix H passages; the r2 changes add no scope or status text.

## Claim under review
Same as r1. Problems B and A stay OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. There is no label change.

## Checks performed
Diff of the r1 block against the r2 block. The only changed regions are the four expected ones.
- **F1 (verbatim snippet).** The final paragraph now opens "None of the contacts above (E-type, ..., zero for Dirac) supplies the required -4kappa_X of c: ... The Noether coefficient is not obstructed but undetermined: the density fixes no value of r, the value r=-4 would match and is selected only by the match, and the value r=-2 ... leaves 2kappa_X. It stays undetermined until ...".
  - It matches my corrected snippet.
  - The contradictory clause "no value of the Noether coefficient ... supplies" is removed.
  - The scope clause and the closing sentence "Problem B stays open and PROGRAMME-CONDITIONAL." are retained, and there is still only one closing status line.
- **F2 (scoping).** The added sentence is present, at the end of the first paragraph (L2 of the block), where the block's `...is used.` is followed by it.
  - It reads: "The statement of the normalisation paragraph that rho^2X contributes no entropy refers to the fixed-state replica, with rho regular, or equivalently to the presentation r=0 below; a Wald-type coefficient of rho^2X is presentation dependent."
  - The dragging paragraph now also says the singular-rho family "is the second reading of the paragraph on the geometry that carries the cone". This is consistent with Appendix H L172, where the paragraph is "Which geometry carries the cone".
- **F3.** The Noether paragraph now states that R denotes R[G] with sqrt(G)=rho^2. It adds that the presentations differ from rho R[g_rho] by terms in V^2 and total derivatives, which are kept in the remainder.
- **Wording.** There is no "obstruction" or "mismatch" overclaim. The contacts are described as not supplying the required term, and the Noether coefficient as undetermined. This is the substance of "mismatch for replica contacts; indeterminacy of Noether coefficient". The paragraph title is unchanged and still neutral.
- **Nothing else changed.** The diff shows no other edits.
- **Block bytes (Python -I).**
  - Size: 10739 bytes, as stated.
  - Counts: 0 TAB, 0 CR, and 0 non-ASCII or control characters other than LF.
  - Brace balance: 0.
  - Math delimiters: 199 `\(` and 199 `\)`.
  - No `\label` and no `\ref`.
- **Anchor.** `\section{Problem C: conformal mode and Cassini}` occurs exactly once in `chapters/appH-microscopic-proofs.tex`. The accepted insertion point is the line immediately before it, after the 037 block. This was the situation in r1 and is unchanged.
- **Bib.** `grep -c` finds 0 existing entries for IyerWald1994, JacobsonKangMyers1994 and Foster2006 in `bib/namcg.bib`. The Crossref and abstract checks from r1 stand.
- **Labels.** No label is added or changed. Problem labels and status text are untouched.

## Findings
None.

## Scope of what is established
The r1 scope statement stands unchanged: PROGRAMME-CONDITIONAL; B and A remain OPEN, CRITICAL PATH. The class is the 031 hypotheses plus the first-order additive rule. The ranked open avenues in my r1 review also stand, led by the local-frame-rotation link to D.

## Recommended disposition
Integrate as-is.

## Exactly what is accepted
1. The LaTeX block in `proposals/038-lambda2-frame-entropy/appH_insert.tex` (r2 version, 10739 bytes). The integrator inserts it before `\section{Problem C: conformal mode and Cassini}`, after the 037 block, separated by one blank line, with CRLF line endings.
2. The three BibTeX entries IyerWald1994, JacobsonKangMyers1994 and Foster2006, to append to `bib/namcg.bib`. They are in `proposals/038-lambda2-frame-entropy/proposal-r1.md`, section "BibTeX (append to bib/namcg.bib)", lines 69-103. `proposal-r2.md` L29 refers to them "as in proposal-r1.md".

Nothing else is accepted. The existing key LewkowyczMaldacena2013 is reused.

## Breakthrough assessment
Not a breakthrough. This is a bounded obstruction and indeterminacy result, with no label change.

## Corrected snippet
None needed.
