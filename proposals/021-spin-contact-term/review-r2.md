VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All eight r1 findings (F1–F8) are applied as specified. The LaTeX otherwise equals r1, the mathematics is unchanged, and the block is a bounded, conditional Problem B no-go with no label change.

## Source reading
Digest + targeted reads. The CLAUDE.md 3(a) full scan for ordinal 20 is covered by my r1 full scan of all 30 chapter files. I confirmed that coverage this way:
- `git diff HEAD -- chapters` shows exactly one change, 17 inserted lines at about line 1993 of `appH-microscopic-proofs.tex`.
- That change is the 022 block ("Conjugate-coordinate class ..."), which is far from the 021 anchor.
- `git diff --stat 60d0d39 HEAD -- chapters bib` is empty, so HEAD has not moved the chapters or bib since the author's 017–020 commit.
- The 021 block title does not yet occur anywhere in `chapters/`.

I did not re-examine 022 beyond locating it.

## Claim under review
Problem B (`sec:status-B`). Current Appendix H status, quoted as in r1: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-order identity is established, but the stationarity condition for the tensor block is not derived." (r1 quote retained; the status passage is untouched in the working tree.)

The Chapter 17 full-GR criterion is unchanged: A, B, C, D1, E, F, G-derived and N DERIVED; H, I, J optional. No label change is proposed.

Claim:
- The Dirac spin excess (+1 per Dirac field) is the Lichnerowicz contact at n=1, so no further spin contact exists.
- The smooth first-order replica gives c_A^sm = −N_tot/12.
- At (n_D, N_s) = (2, 6), c_A is 2 (fixed-state), 1 (with a Kabat vector contact) or 0 (smooth, a 0=0 equality).
- The ambiguity is localised to the replica and flux datum.

## Checks performed
- **Diff of the r2 block against the r1 block**, sentence by sentence (Python difflib). Only the F1–F8 edits differ:
  - **F1:** "adding to it the contact of \(Q_fR_G\), which at the weight \(-1\) shifts \(c_A\) by \(+1\) per Dirac field, would count it twice" (matches snippet 1).
  - **F2:** "The values \(2\) and \(0\) correspond to a replica in which \(\ln\rho\) carries no flux ... and one in which it carries the full deficit; intermediate fluxes are not computed, and which replica the matrix state selects depends on the state and the tip regularisation, which are not derived here". The binary "is the flux" sentence is gone. The closing disclaimer now reads "do not derive the replica, the state, the tip domain or the gluing".
  - **F3:** Kabat is cited only for "a Dirac field with the Levi-Civita spin connection the black-hole and entanglement entropies coincide~\cite{Kabat1995}"; the torsion-reading equality (both +1/3) is stated to be "the computation above".
  - **F4:** \(Q_f=Q_s=\tfrac14\) in the torsion reading; "an equality of \(n\)-derivatives at \(n=1\), not an identity in \(n\)"; the branch-free −1/2 is restricted to a "regularised smooth family" and "The branch issue of the unregularised singular-\(\rho\) cone is not removed."
  - **F5:** "fixed-state replica" is defined (pulled-back replica, ρ regular, cone on G, antiperiodic gluing). Also added: "This does not by itself exclude the fixed-state replica as the definition of \(\operatorname{Tr}\rho^n\)", with the statement scoped "about constant \(\bar\Theta\)".
  - **F6:** "checked symbolically for a generic \(\bar\omega\) and follow from the Weitzenb\"ock identities of the paragraph on the torsion invariant".
  - **F7:** the four paragraph references are named in words. The "preceding paragraph(s)" wording is removed.
  - **F8:** the weights "+1 Dirac, −1 vector, 0 scalars/ghosts" are scoped to "fields minimally coupled in the variables \((G,\rho,\partial\Theta)\)"; "within this class ... at most the value 1"; the torsion-reading bosonic contacts are stated not to belong to the class.
- **Nothing else changed.** The remaining sentences are identical to r1, including all the numerical content: the 2/1/0 values, c_T = 0, N_tot = 0, and the IKKT 0=0 caveat.
- **Mathematics:** I re-derived the F1 direction check, since it is the headline. Weight −1 with Q_f = 1/4 gives −4(1/6−1/4) = +1/3, against −2/3 at Q = 0, so the shift is +1 per Dirac field and raises c_A. The r2 wording is consistent with this. The other mathematics is the same as the r1 content I already verified: scripts, identities and bookkeeping. The proposal folder is clean in git (scripts, outputs and `bib_entries.bib` unmodified), so I did not re-run the scripts.
- **`appH_insert.tex`:**
  - After normalising line endings it equals the r2 block exactly (6129 characters, Python comparison).
  - It is now LF-only, not CRLF as noted in r1. The proposal says so, and the integrator must write CRLF into the chapter (CLAUDE.md).
- **Anchor:**
  - "…do not compute the next order of either side. Problems~B, C, D, F and~G remain open." occurs once, at line 198 of `appH-microscopic-proofs.tex`.
  - `\section{Problem C: conformal mode and Cassini}` occurs once, at line 200.
  - The 021 block goes between them (after line 198, before line 200).
  - The 022 insert is elsewhere, near line 1993.
  - `\LUV` is defined at `namcg-book7.tex:54` (verified in r1).
- **Bib:**
  - `bib_entries.bib` is identical to the BibTeX in the r2 proposal and to the r1 version.
  - Kabat1995 and DonnellyWall2016 are still absent from `bib/namcg.bib` (grep count 0), so the integrator must append them.
  - Kabat1995: BibTeX record: VERIFIED (Crossref, r1: NPB 453, 281–299, 1995, DOI 10.1016/0550-3213(95)00443-V, hep-th/9503016; only the abstract was verified, not the full text).
  - DonnellyWall2016: BibTeX record: VERIFIED (PRD 94, 104053, 2016, DOI 10.1103/PhysRevD.94.104053, 1506.05792).
- **Not independently verified:** the proposal's scratch compile (271 pages, 0 undefined or multiply-defined references). The integrator must run `scripts/build_check.py`.
- **Emergence:** G, ρ and g_ρ are built from Θ throughout. Spacetime remains emergent.

## Findings
None. F1–F8 are closed.
- No label is changed.
- The block says "conditional; not closure".
- It does not call the flux decisive or binary.
- Fermion and symplectic-gauge edge modes are marked not examined.
- The vector contact −1 is marked as an input.
- The block ends with a single scoped status sentence: "Problems~B, C, D, F and~G remain open."

## Scope of what is established
**Established (conditional; M2, bounded no-go).** The hypothesis class is: Poisson limit, Euclidean section, α=1, the Λ² term, one loop, the 019 constants (quasi-free state, rotational flow, less singular extension, uniqueness of continuation), the pulled-back antiperiodic fixed-state replica, and the first-order smooth replica for a regularised smooth family about constant Θ̄. Within that class:
1. The Dirac spin excess is the weighted Q_f contact at n=1. It is already inside c_A and raises it, so no further spin contact is available.
2. The smooth first-order replica gives c_A^sm = −N_tot/12 = c_A + bosonic contacts. At (2, 6) this is 0 = 0 for every sector-uniform Q, which is not a derivation of G_T = G_A.
3. Standard contacts (Dirac +1 included, vector −1 as an input, scalar and ghost 0, in the (G,ρ,∂Θ) class) reach at most c_A = 1 at (2, 6), against the 0 needed.

**Inputs and unresolved.**
- The vector contact −1 and its applicability to a^μ (an input; the torsion-reading net connection-sector contact would be −1/2).
- Fermion and symplectic-gauge edge modes (not examined).
- The state, tip domain, gluing and actual replica flux.
- The next order of either side, and G_eff.

**Status.** Problem B stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No label change. No BREAKTHROUGH.

**Open avenues, ranked (from r1, unchanged).**
1. The replica and flux datum: compute c_A for intermediate flux of ∇lnρ through Σ, and the replica of the matrix state, as a Problem A sub-lemma.
2. The next order (Λ⁰ and log) on a curved J=0 leaf, where c_T = c_A = 0 at Λ².
3. Tip domains for the vector, ghost and scalar sectors; a Maxwell-like edge term for the symplectic gauge sector (bounded at c_A=1 if so); fermion edge modes.
4. A non-quasi-free or non-rotational state.
5. Contents on N_s = 14 − 4n_D, as a non-vacuity check only (unphysical contents).
6. Sector cutoffs (tuned; low).

## Recommended disposition
Integrate as-is.

**Accepted for integration (exactly):**
(a) The LaTeX block in `proposals/021-spin-contact-term/appH_insert.tex` (identical to the r2 block), inserted immediately after the line ending "...do not compute the next order of either side. Problems~B, C, D, F and~G remain open." (line 198) and before `\section{Problem C: conformal mode and Cassini}`, written with CRLF line endings.
(b) The two BibTeX entries Kabat1995 and DonnellyWall2016 appended to `bib/namcg.bib`, as in `bib_entries.bib`.
(c) Nothing else: no label change, no other file. The integrator should run `python scripts/build_check.py` after insertion.

## Corrected snippet
None needed.
