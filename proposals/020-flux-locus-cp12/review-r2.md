VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All r1 required revisions (1a, 1b, 1c, 2) are applied as specified. Nothing else in the LaTeX changed. block-r2.tex equals the proposal block, the anchor is unique, the BibTeX record is verified, and there is no label change.

## Source reading
Digest + targeted reads. The working tree is dirty with the expected integrations. I read the proposal-r2 and block-r2.tex in full, review-r1 in full, and the appH region around the anchor (lines ~1980-1990). The block changes no scope, status or definition, so no full scan was triggered. This is not a full scan. I did not re-read Ch. 17 or the Problem F entry this round. The status below is carried from review-r1 and the proposal, and the block adds no label change.

## Claim under review
This is a bounded no-go inside the 018 class (H1-H5), with closed forms for f1 and f2 and a codimension-4 locus where f1 = f2 for all ζ. The locus is conditional on the numerically verified self-duality of Q^{-1/2}FQ^{-1/2}. The target is Problem F (matrix-derived G_eff). Status, as quoted in the proposal and review-r1: "OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL". The block ends "This changes no ledger label; Problem~F remains open."

## Checks performed
- **r1 to r2 LaTeX diff.** I extracted the block from proposal-r2.md and compared it with block-r2.tex. They are identical (True, CRLF normalised). I diffed block-r1.tex against block-r2.tex sentence by sentence. Exactly four edits appear:
  - (i) now begins "Conditional on the self-duality statement above, the closed forms give f1=f2 ... exactly on" (1a).
  - "a union of at most two lines unless F is (anti-)self-dual identically" is now "a linear subspace of the ζ-plane (a line, or the whole plane only if F is (anti-)self-dual)" (1b).
  - The scope paragraph gains "The self-duality of Q^{-1/2}FQ^{-1/2} is verified numerically at sampled points and is not proved, so the classification of the set f1=f2 is conditional on it." (1c).
  - In (iii), "Troost's levels ... hep-th/9909187" is now "the Landau levels of the same form, ... of \cite{Troost2000}, eq.~(35)" (2).
  - Finding 3 is untouched, and no other sentence differs.
- **Anchor.** `\section{Problem G: HBEV}` occurs exactly once in appH, at line 1989 in the current working tree (the proposal says 1982; the line number has shifted because of the other integrations). The line before it is the 018 paragraph, which ends "...Chapter~\ref{ch:vierbein-emergence}, and it does not bear on Assumption~\ref{ass:EE}. This changes no ledger label; Problem~F remains open." The block follows that paragraph. It has not yet been inserted (the heading is absent from appH).
- **Labels and citations.** The block defines no labels, so no duplicates are possible. It uses one citation key, Troost2000.
- **Troost2000 BibTeX.** `Troost2000` is absent from bib/namcg.bib (grep count 0, no "Troost" hit). Crossref was fetched for DOI 10.1016/S0550-3213(99)00721-X and returned: title "Constant field strengths on T2n", author Jan Troost, Nuclear Physics B, volume 568, pages 180-194, issued 2000-02. The proposal's record matches (author, title, journal, volume, pages 180--194, year 2000, DOI, eprint hep-th/9909187). **BibTeX record: VERIFIED.** The Crossref check covers the bibliographic data only. Troost's content (eq. 35 in Section 7, the no-tachyon condition in Section 9) was verified in r1 on the arXiv/ar5iv text, and the "same form" phrasing covers the Euclidean-to-local-symbol analogy.
- **Math.** The closed forms, det Q, the V4 identity, the f²/(2π²) density and the compact so(6) result were re-derived or re-run in r1 and are unchanged. The r2 edits are wording only, and they reduce the claim strength as required.
- **Process language and status.** The block contains none. There is no label change, and no emergence issue (as in r1).
- **Build.** I did not re-run the compile. The proposal reports 268 pages with 0 undefined and 0 multiply-defined references (compile_check_r2.out.txt); this is the researcher's result and was not independently re-run. The integrator's build_check will confirm it.

## Findings
none. r1 Finding 3 was "keep as is", and it is kept.

## Scope of what is established
**Accepted exactly:**
1. The LaTeX block in block-r2.tex (equal to the fenced block in proposal-r2.md), inserted in chapters/appH-microscopic-proofs.tex immediately before `\section{Problem G: HBEV}` and after the 018 paragraph ending "Problem~F remains open."
2. The BibTeX entry `Troost2000` as given in the proposal, to be added to bib/namcg.bib in the same integration.

Nothing else is accepted. The researcher's "Stale passages: none" claim is unchanged from r1: no manuscript text states the 018 "avenue 5".

**Proved or conditional.** Everything below is conditional on the numerically verified, unproved self-duality of Q^{-1/2}FQ^{-1/2}. That identification is checked at 300 points and not proved, and the block now says so.
- The closed forms for f1 and f2.
- The codimension-4 locus where f1 = f2 for every ζ.
- The linear growth of the relative instability off the locus.
- The compact so(6) result f2/f1 = |y4|/ℓ with the constant δ contraction.

**Unconditional within H1-H5 (Landau symbol).**
- A ζ-independent transverse flux cannot stabilise an unbounded fibre.
- The vector density tends to f²/(2π²) at f1 = f2, so the ζ-integral diverges there.

**Not established.** The Levi-Civita identification as a proof; the sign and size of w; anything for a position-dependent contraction, Moyal terms, fermions, a finite fibre, or other transverse backgrounds. These are outside the class, and the block does not close any of them. Problem F and the critical-path set remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

**Open avenues (ranked, unchanged from r1, relaxing H-hypotheses):**
1. H2: the position-dependent ambient contraction Q^{-1} (f1 = f2 identically). Determine whether the matrix action, gauge fixing or regulator supplies the (y_a D^a)²/ℓ² term.
2. H4 with a finite fibre: truncate ℓ, with transverse flux f3 ≥ 2 sup|Ln| ζ_max.
3. The SO(4,1)-covariant presentation X^A = M^{A5}.
4. R-f2: compare the radius of convergence of the SUSY flux expansion with |r|/|p|. This is a lead, not an application.
5. H1: exact so(4,2) character analysis with Moyal terms.
6. Fermions help only on the locus.

## Recommended disposition
Integrate as-is, together with the Troost2000 bib entry. The integrator should run build_check and confirm the line-number shift of the anchor (1989 in the current tree). This is a coherent single-purpose bounded no-go with a conditional locus classification. It is not a breakthrough, and no label change is proposed.

## Corrected snippet
None needed.
