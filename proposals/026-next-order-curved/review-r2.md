VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All of F1–F9 are applied as wording and notation changes only. The block is internally consistent, `appH_insert.tex` is byte-identical to the r2 block, the anchor is unique, and no label changes.

## Source reading
Digest plus targeted reads. This is not a full scan.
- I read the r1→r2 diff in full.
- I read the whole 9180-character block in `appH_insert.tex`.
- I read the anchor lines 217–221 of the dirty working-tree `appH-microscopic-proofs.tex`. The tree is dirty only through the accepted 025 block, which is expected.
- I did not re-read Chapter 17 or Appendix H. The proposal changes no status text, and the closing sentence is the pre-existing "Problems~B, C, D, F and~G remain open."
- I relied on my own r1 re-derivation of the identity (weighted a_1 = 0, weighted a_2 = (1/2)𝒮₄). The r2 diff changes no calculation.

## Claim under review
Problem B (with F): the next order beyond Λ² at the content (N_s, n_D) = (6, 2) on a curved leaf. The proposal is a conditional structural identity plus a bounded no-go. It closes nothing.

Appendix H status for B, F and A (as recorded in the r1 review): OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. The block carries no label edit.

## Checks performed

**Direct verification**
- **Block identity.** A scripted comparison of the fenced LaTeX in `proposal-r2.md` against `appH_insert.tex` returned `True`, with 9180 characters each.
- **Diff r1→r2.** The changes are the changelog, the shortened summary text, the added LaTeX fence, and the avenue and hypothesis lists. Nothing mathematical changed.
- **F1.** The text now says "With one common proper-time limit for all sectors, the coefficient of ln Λ_UV … ∝ ∫ρ²𝒮₄ …; finite terms of the same order are not controlled."
- **F2.** The text says "found to be anti-self-dual-valued in every sampled case with 𝔍=0 … (not proved)". The J ≠ 0 statement is limited to sampled cases.
- **F3.** The closing sentence says no logarithmic coefficient of the cone side is computed, so no G_T versus G_A comparison at logarithmic order follows. No A-side coefficient is asserted anywhere.
- **F4.** The text says "up to total derivatives, which vanish by the same sums".
- **F5.** The text says "the condition 𝔍=O(ε²) is the source-free Maxwell equation".
- **F6 renames.**
  - Scripted counts show 0 occurrences of bare `\mathcal S` without `_4`, and 7 of `\mathcal S_4`.
  - The Gram matrices appear as `\mathsf A`, `\mathsf B`, `\mathsf C` (7 uses).
  - The weights appear as κ_X and κ_i (5 `\kappa`).
  - b appears only as the connection.
  - A grep for a bare stand-alone `S` in the block returned nothing.
- **F7.** The text says "a formal shift of the operator: no gauge-invariant mass term and no ghost or longitudinal consistency is asserted".
- **F8.** The text says "local, on regions where Pf ω ≠ 0". It gives the degenerate locus of the SD example (x¹ = x² = 0, (x⁴)² = 1 + (x³)²). It says G degenerates at r⁴ = C and that the family is valid locally for r⁴ > C.
- **F9.** The text says "with the vector weight 1 and the ghost weight −2 fixed in that scan".
- **Anchor.** The sentence "…nor fermion edge modes, and they give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open." occurs exactly once, at line 219. Line 221 is `\section{Problem C: conformal mode and Cassini}`. Insert between them with a blank line.
- **Labels and macros.**
  - The block uses `\eqref{eq:Smatrix}` (defined once, in ch03) and `\ref{ass:emergent-op}` (defined once, in ch08).
  - It defines no label.
  - `\LUV` is defined in `namcg-book7.tex` line 54.
  - No process language appears in the block.
- **Citations.**
  - The block's only citation is `\cite{Steinacker2023}`.
  - It is defined once in `bib/namcg.bib` (line 121) and is already cited in the chapters (appH lines 1913, 1924, 1983). The integrator's real build will therefore resolve it.
  - The 60 undefined citations in the scratch compile are the missing `.bbl` in a scratch copy and are unrelated to this block.
- **Paragraph title.** The new `\paragraph` title occurs only in the insert, so there is no duplicate.

**Not re-run**
- The numerical and exact-rational scripts, which r2 does not change.
- The Steinacker claim, which is not new in r2. It is phrased as reported in the construction of the cited paper, and similar statements already stand in Appendix H.

## Findings
None. Minor notes for the integrator, non-blocking:
- Preserve CRLF line endings.
- Run `scripts/build_check.py` after insertion.

## Scope of what is established

**Established within the stated hypotheses**
- Hypotheses: Poisson limit, Euclidean section (also checked for η = diag(−1,1,1,1) algebraically), α = 1, one loop, one common proper-time limit, content (6,2), Yukawa couplings and transverse dynamics dropped, local regions with Pf ω ≠ 0.
- Identity: the weighted a_1 vanishes and the weighted a_2 equals (1/2)𝒮₄ up to total derivatives. Here 𝒮₄ = 8 tr𝖠 tr𝖡 + 16 tr(𝖢𝖢ᵀ) ≥ 0, with equality at a point iff b is valued in one su(2) factor there.
- Consequence: at this content the ln Λ_UV coefficient has no R², Ric², Riem², Weyl², Euler, RE or Einstein–Hilbert term. It is a quartic in b.
- Backgrounds: SD and ASD give 0 = 0. The non-BPS d(hΛ³) family was found chiral in every sampled J = 0 case.
- Maxwell expansion: it gives 𝒮₄ > 0 at order ε⁴. This is formal, and convergence and globality are not examined.
- Mass insertion: the EH-type change is nonzero only for SUSY-breaking mass patterns. It is a formal operator shift.

**Conditional or open**
- The A side is not computed, so there is no G_T versus G_A statement at logarithmic order.
- Finite Λ⁰ terms are not controlled.
- Chirality on the non-BPS family is not proved.
- Moyal corrections and fuzzy extra dimensions are not treated.
- Stationarity, the emergent-metric map, and any value or sign of G_eff are not derived.
- B, F and A remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

**Open avenues**, ranked as in the proposal and agreed:
1. The a_3 mixed quartic with a Kaluza–Klein 1/μ² sum. This is relaxing H5/H6, via a mass scale or transverse background in the extended presentation. It is the only place an EH term can enter in this class.
2. The A-side logarithmic coefficient, to test against the T-side zero.
3. Relaxing H8: exact non-chiral J = 0 backgrounds, or a proof that chirality is forced in the SU(2)-invariant classes.
4. Lorentzian colliding waves with the iε prescription.
5. Moyal corrections, tip domains and edge modes, and non-quasi-free states.

## Recommended disposition
Integrate as-is, as integration ordinal 24.

**Exactly what is accepted:** the LaTeX block in `/c/Users/redgi/Projects/namcg-lab/proposals/026-next-order-curved/appH_insert.tex` (identical to the fenced block in `proposal-r2.md`). Insert it into `chapters/appH-microscopic-proofs.tex` after the line ending "Problems~B, C, D, F and~G remain open." (the end of the 024 paragraph, line 219), and before `\section{Problem C: conformal mode and Cassini}`. Nothing else is accepted: no label or status change, no bibliography change, and no other file.

Milestone: M2 (bounded no-go with sharpening). No BREAKTHROUGH and no LABEL-CHANGE-PROPOSED.

## Corrected snippet
None needed.
