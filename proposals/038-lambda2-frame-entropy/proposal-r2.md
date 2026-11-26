# Proposal 038-lambda2-frame-entropy, round 2

## Changelog (r1 -> r2; only the LaTeX sentences listed change; appH_insert_r1.tex keeps the r1 block)
- F1 (major): the final paragraph's "None of the contacts above ..." sentence is replaced verbatim by the review's corrected snippet. The replica contacts are a mismatch; the Noether coefficient is undetermined (r = -4 would match and is selected only by the match; the ledger value r = -2 leaves 2 kappa_X). The body wording below is aligned.
- F2 (major): the review's scoping sentence is added at the end of the paragraph containing the table ("contributes no entropy" refers to the fixed-state replica, rho regular, or the presentation r = 0). The dragging paragraph now states that the singular-rho family is the second reading of the paragraph on the geometry that carries the cone.
- F3 (minor): the Noether paragraph states that R denotes R[G] with sqrt(G) = rho^2 and that the presentations differ from rho R[g_rho] by V^2 and total-derivative terms kept in the remainder.
- Avenues: replaced by the review's ranked list (below).
- Nothing else in the block changed (diff of appH_insert_r1.tex against appH_insert.tex touches only these four places). Block: 10739 bytes, 0 TAB, 0 CR, 0 control characters, 0 non-ASCII (checked in Python); anchor `\section{Problem C: conformal mode and Cassini}` occurs once (grep), insertion immediately before it after the 037 block. Scratch compile outside the repo (block + three bib entries, pdflatex/bibtex/pdflatex x2): 0 undefined or multiply defined references.

## Result
As in r1, with the wording corrected. Under the 031 hypotheses (Poisson limit, Euclidean, one loop, alpha = 1, Lambda^2 term, totally geodesic Sigma, first order in 1-n, f = |z|^(n-1), first-order additive rule, ledger inputs):
- Replica contacts: mismatch. Residue before any contact 4 (1/G_A - 1/G_T = 2 Lambda_{UV,v}^2/pi, all N_s); after contacts 3 or 5 (holonomy -alpha_v sigma), 7/2 - N_s/4 (delta contact -N_tot/4), 5/2 - N_s/4 or 9/2 - N_s/4 (both); Dirac holonomy zero; zeros only at special content.
- Noether coefficient of rho^2 X: undetermined, not obstructed. The pure-diffeomorphism charge vanishes on Sigma, the coefficient is the R[G]-coefficient r of the chosen presentation, c_W - c_T = kappa_X (r+4); r = -4 would match and is selected only by the match; the ledger value r = -2 leaves 2 kappa_X. It stays undetermined until the frame is dragged by a flow with a local internal symmetry (Problem D).
- Hypotheses section (B-R2), cone cross term, torsion algebra: unchanged from r1 (see proposal-r1.md; scripts s1-s8 unchanged).

## Target and status
Problems B and A, unchanged: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; closes nothing. Chapter 17 and Appendix H consistent.

## Source reading
Digest + targeted reads (r1 reads plus review-r1.md in full). Not a full scan.

## Research and reasoning
Unchanged from r1 (no new mathematics in r2).

## Claim classification
Unchanged from r1; "Noether coefficient undetermined" is a conditional statement (Iyer-Wald structure for the coframe presentation), the replica mismatch is conditional on the ledger inputs and the additive rule.

## Proposed changes
Insert appH_insert.tex (updated) before `\section{Problem C: conformal mode and Cassini}`, after the 037 block, one blank line, CRLF by the integrator. No \label/\ref. BibTeX for IyerWald1994, JacobsonKangMyers1994, Foster2006 as in proposal-r1.md (Crossref-verified, absent from bib/). Stale passages: none.

## Verification scripts
s1-s8 and compile_check.out.txt as in r1, unchanged.

## Decisions Taken
Applied the review's snippets verbatim; kept the r1 mathematics; used the review's ranked avenue list.

## Milestone assessment
Routine; no breakthrough.

## Status-label recommendation
None.

## Author decision needed
None.

## Remaining open step
Ranked avenues (review):
1. Local-frame-rotation link with Problem D: whether Lorentz locking forces or suppresses the Lorentz-violating class [X]; would make the Noether coefficient unique (a prediction or a match).
2. First law with the rigid compensating rotation (relaxing L_xi phi = 0).
3. Replica from the modular flow (Problem A): alpha_v, the n > 1 branch.
4. Exact singular-cone spectrum, to test the additive rule.
5. Constraint-term charge (B-R3).
6. Fermion and edge-mode contacts; second circulation with a regular Sigma metric.

## Special instructions for the gatekeeper
Diff appH_insert_r1.tex against appH_insert.tex: four edits only. Confirm the closing wording says mismatch for replica contacts and indeterminacy for the Noether coefficient, and that nothing says r = -4 is excluded.
