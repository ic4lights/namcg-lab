VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1

## Verdict
The Jacobi-commutator argument, the corrected double-Duhamel engine and the numbers all reproduce, and 032 contains no false sentence. Two wording revisions are needed: the "correction of" framing, and the unsupported "no sign-definite, covariant coefficient" conclusion.

## Source reading
Digest + targeted reads, not a full scan.
- The digest is STALE (`dirty-chapters: yes`, expected). Per CLAUDE.md 3(d) I read the affected passages directly: appH lines 2085-2234 (the 030 and 032 blocks, including the full 032 Landau paragraph), the Problem E and F ledger entries, and the Chapter 17 critical-path criterion (grep of the relevant lines).
- Ordinal assumption: 034 is the 34th integrated item (the ledger shows 33 so far), so no 5th-item full scan is due. If 037 lands first, 034 becomes the 35th and the gatekeeper full scan is then mandatory.
- Anchor: `\section{Problem G: HBEV}` occurs exactly once, now at appH line 2234. The proposal's "line 2214" is stale and harmless. Line 2232 ends the 032 block with "This changes no ledger label; Problem~F remains open.", which matches the stated anchor.
- `block-r1.tex` is byte-identical to the block in `proposal-r1.md` (diff after CR strip). It has no TAB characters. I did not complete a check for non-ASCII bytes: the `grep -P` call failed in this locale. The proposal reports ASCII only, so treat this as not independently verified.
- The only label used is `ch:vierbein-emergence`, which exists. No new label, cite or bib entry.

## Claim under review
Bounded no-go plus a model correction. Class: Poisson limit, leaf CP^{1,2}, one loop, nilpotent leading symbol resummed in the centre flux, Lorentzian iε, M_str term, sampled orbit points and centre directions.

Targets, quoted from appH:
- Problem F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- Problem E: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

No label change is proposed or implied. Emergence is preserved: the block explicitly makes no identification with the emergent metric.

## Checks performed
Direct re-runs:
- `l1_jacobi.py`: κ^a = σ q^a y^4 holds to about 1e-14. [W_a,Y] = σ q_a Ham(y^4) holds to 1e-15. The vertical part of [W_a,Y] is below 1e-14 at 8 points. The flux term y^c S_ac^k is not parallel to κ (residual 1.0).
- `t3_gauge_e.py`: the central engine is invariant under α→α+λκ to 1e-14 at F≠0, y≠0. The F→0 limit agrees with the old engine to 1e-8.
- `t2_gauge.py`: the interleaved (032) model changes by 0.073-0.164 relative at F≠0, and by 3e-14 at F=0. This matches the block's "0.07-0.16". The superseded `engine_c` shows 0.4-0.5, as expected for the discarded seam formula.
- `toy2d_e.py` and a full rerun of `toy2d_direct.py` (exact 2D Landau diagonalisation): direct 0.08491501 and 0.08262229 versus engine 0.08489561 and 0.08260391. The relative difference is 2e-4, and the engine result is real.
- `l5_forms.py 21 1.4 central`, rerun: it reproduces the stored output exactly. Gauge invariance of yy, cc and full is 1e-9 or better. The yy-versus-A residual is 0.004 and 0.000, with A-like eigenvalues of mixed sign.
- Stored outputs checked against the block's numbers:
  - `l5_12_0.8` and `l5_12_2.0` match the quoted residuals 0.54/0.85 and 0.08/0.48.
  - `l4_run` shows T2·s/c = 1.0000 in every case.
  - `l2_leaf_map` gives Q_EH/A_engine = 1.
  - `l7_neglected` gives the ratio 0.014-0.49.
  - `l3_conv` shows convergence at moderate |s| but only ~1% changes at large rho, so "two digits" is appropriate.

Independent re-derivation of the central algebra:
- {T_a, φ} = κ_a and the Jacobi identity give [W_a, Y] = Ham(κ_a) = σ q_a Ham(y^4).
- If Ham(y^4) lies in D = span(W_a) (checked numerically), the vertical part vanishes in any complement. With W_a y^k = 0 (constant c), the vertical balance y^c S_ac^k + W_a y^k + … = 0 cannot hold, so the interleaved model is inconsistent with the Jacobi identity.
- Conjugating by exp(-iελ cosφ Y) with Y central shifts α by λκ. This is the invariance that fails for the 032 model. I did not independently re-derive the Plancherel seam identification beyond the toy.

Not independently verified:
- The scratch compile (301 pages, 0 undefined).
- Most of the 24-case `l4_run` table beyond the stored output.
- The multiprecision engine beyond the convergence file.
- The cited Hattori-Itakura-Ozaki and Bastianelli et al. equations. The block cites no literature and imports nothing from them, so nothing depends on them.

## Findings

**F1 (major). Location: the block's Result (iv) and the sentence "A finite, covariant, sign-definite Einstein--Hilbert coefficient does not emerge in this class".**
- The computations support only these statements, and only at sampled points and centre directions:
  - the tetrad (yy) part of Fin is not ∝ A;
  - the yy spectra have both signs;
  - A is non-covariant (inherited from 030).
- Not shown: the eigenvalue signs of the full Fin form (yy+cc+cross); covariance or non-covariance of Fin itself; any window average over the centre variable. The cc part is positive-definite in the real part in one sample (seed 21, theta 1.4: eigenvalues 0.006, 0.31, 1).
- The coefficient of the effective action is what a window average of Fin(ζ) would give, and that is not computed. "Does not emerge" therefore overstates the result.
- Required action: scope the final conclusion to the sampled per-centre-variable forms. Say that sign-definiteness and covariance of the full Fin form and of the window-averaged coefficient were not tested. See the corrected snippet.

**F2 (minor/wording). Location: the heading "correction of the preceding Landau model", and "the commutator that the Jacobi identity forbids".**
- The result is a supersession of a model that 032 already labelled "a model and not the leaf"; it is not a correction of a false statement (see PRIOR-CLAIM-ERROR below).
- "Forbids" should read "is inconsistent with, at the nilpotent order with frozen coefficients". The weight-one terms and the gradient of y^k are exactly the dropped ingredients.
- Required action: reword as in the snippet.

**F3 (minor). Location: the "Checks" paragraph.** The 2D toy validates the central-c-number prescription only. In the toy, F·y ∥ κ holds automatically and K is a constant c-number, whereas on the leaf F·y is not ∥ κ (residual 0.7-1.0). The identification of the leaf Y with the seam insertion P = y^c ω_c + c is conditional on the nilpotent order and first-jet freezing. The block's closing paragraph says this only implicitly. Add "the seam identification on the leaf is conditional on the nilpotent order with frozen coefficients; the two-dimensional test validates the prescription for a central K".

## PRIOR-CLAIM-ERROR check on merged 032 (uncommitted)
Result: no merged sentence is false, so no flag. 032 is only scoped, and the scoping is already in the text. I read the whole 032 Landau paragraph (appH 2230-2232). Every merged sentence checks out:
- "reproduces the sector of the preceding paragraph with the commutators [ω_a,ω_b]=iF_ab kept, but without the commutator of Y with W_a that the Jacobi identity fixes on the leaf, so it is a model and not the leaf (an omission shared with the frozen-frame paragraph above)". This is exactly what 034 finds, and it is accurate.
- "gauge invariance in n at F≠0 (2·10^-15)". This is true for n and the pure-n field. 032 never claims α→α+λκ invariance at y≠0.
- The F=0 checks, the unchanged log coefficient A and the Fin values are statements about that model, and they remain correct as such.
- The closing paragraph repeats "the Landau model for the Einstein--Hilbert sector is not the leaf".

The 030 text (appH ~2203-2211: the EH form A, its gauge invariance under a→a+λq, non-covariance) concerns F=0, where both models agree (t2/t3: 3e-14). Nothing in 030 relies on the F≠0 gauge behaviour.

034's new content is that the 032 model is not invariant under α→α+λκ at F≠0, y≠0, and that its Fin values should not be read as leaf values. That is a sharpening of a stated scope, not a correction of a merged claim. Because there is no false sentence, there are no old→new replacement strings. For the same reason I did not escalate to a 3(c) full scan; the targeted reads cover all passages affected.

No other chapter mentions Landau, Fin or the nilpotent symbol (grep over chapters: only appH). No stale statement is created.

## Scope of what is established
- **Established (algebra, numerically confirmed to 1e-14):** κ^a = σ M^{45} q^a, and [W_a, Y] = σ q_a Ham(y^4) with no vertical part. The centre flux term y^c F_ac is not parallel to κ.
- **Established (numerical):** the 032 interleaved model is not gauge invariant at F≠0, y≠0 (7-16%). The central model is gauge invariant (1e-14) and matches exact 2D diagonalisation to 2e-4.
- **Conditional:** the identification of leaf Y with the seam insertion P in the nilpotent, first-jet-frozen order. The weight-one terms are dropped, and their relative size (0.01-0.5 per unit ζ) is not uniformly small.
- **Numerical, sampled only:** c = A/16π² is unchanged. Fin is finite per centre variable. The tetrad part is not ∝ A (3 samples). The yy spectra are indefinite. A is non-covariant (inherited from 030).
- **Open:** the full-Fin sign and covariance, the window average, the Zeeman-dressed vector term at order ε², the weight-one terms, Moyal corrections.
- No-go class: Poisson limit, one loop, nilpotent symbol with central P at the seam, iε proper time, M_str term, sampled orbit points. It does not close F or E. F and E remain OPEN, PROGRAMME-CONDITIONAL. No breakthrough.

Open avenues, ranked (hypotheses to relax):
1. Zeeman-dressed vector-mass term at order ε² (matrix-valued engine with P at the seam). It decides whether the mass-linear coefficient is finite.
2. Window average of the full Fin(ζ), not just the yy part, to test sign-definiteness and covariance of the actual coefficient (relaxes "per centre variable").
3. Weight-one terms and the gradients of y^k and y^c, since the ratio is up to 0.5 (relaxes the nilpotent order).
4. Spectral, mode-by-mode definition of the vector sector, and non-perturbative or positive mass.
5. Moyal order and wider sampling.

## Recommended disposition
Revise the block per F1-F3, then integrate. The anchor, LaTeX and labels are fine. The block is one coherent package (Jacobi identity, engine and leaf outcomes share dependencies). No ledger edit.

## Corrected snippet
No new physics; wording only.

1. Heading: replace "…; correction of the preceding Landau model)" with "…; supersession of the preceding Landau model)".
2. Replace "this is the commutator that the Jacobi identity forbids at the nilpotent order." with "this commutator is inconsistent with the Jacobi identity at the nilpotent order with frozen coefficients."
3. Add to the Checks paragraph, after the 2D test sentence: "The two-dimensional test validates the prescription for a central \(K\); the identification of the leaf field \(Y\) with the seam insertion \(P\) is conditional on the nilpotent order and the frozen first jet."
4. Replace the last sentence of (iv) "A finite, covariant, sign-definite Einstein--Hilbert coefficient does not emerge in this class." with: "In the sampled per-centre-variable forms the tetrad part of the finite remainder is neither proportional to the form \(A\) nor sign-definite; the sign and covariance of the full finite remainder (tetrad, charge and cross parts) and of its window average over the centre variable were not tested, so no finite, covariant, sign-definite Einstein--Hilbert coefficient is obtained here."
5. In the closing paragraph, add "the sign and covariance of the full finite remainder" to the list of items "not included".

Extra assumptions: none.
