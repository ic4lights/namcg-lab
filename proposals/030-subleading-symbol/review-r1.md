VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1

## Verdict
The tail structure, the Maxwell identification of c0, the noncovariance and the EH-form limit hold within the stated class, and A is correct as a whole. The displayed "EH part" formula is algebraically wrong: it is not gauge invariant, and it does not sum with the dilaton term to A. Three smaller wording and notation problems also need fixing before the block can be integrated.

## Source reading
Digest + targeted reads. `make_digest.py --check` reports DIGEST STALE, as expected with `dirty-chapters: yes` (the uncommitted appH integrations). Per CLAUDE.md 3(d) I read the affected passages directly: appH lines 2095-2152 (the 027 and 028 blocks and the anchor) in full. I did not read Chapter 17 or the Problem F/E ledger entries again; the F/E statuses are taken from the 028 review and the task statement, as the proposal itself says. No full scan was done, none is due, and none is claimed.

## Claim under review
Bounded no-go plus a conditional EH-form limit for the next-to-leading symbol of +M_str Tr[χ(H_X−i0)⁻¹], at order ε²q⁴ with the first jet frozen. The class is: Poisson limit, one loop, CP^{1,2} four-matrix class with μ²=−3, supplied content with no bilinear fermion mass, one Gaussian Δ_{3/4} window.

Target problems, as the 028 review records them:
- Problem F: `Status: OPEN. Priority: CRITICAL PATH.` PROGRAMME-CONDITIONAL; treating G_eff as an input leaves F OPEN.
- Problem E: OPEN, CRITICAL PATH for the matrix-derived label.

No label change is proposed or implied.

## Checks performed
- **Anchor.** `\section{Problem G: HBEV}` occurs once, at appH line 2150. It comes directly after the 028 block, whose last sentence reads "This changes no ledger label; Problem~F remains open." The block text in `proposal-r1.md` is identical to `block-r1.tex` after CR stripping. The block has 0 TAB characters. `\ref{ch:vierbein-emergence}` resolves (ch04). The scratch compile output reports 0 errors, 0 undefined and 0 multiply defined references. I did not re-run the compile.
- **Existing outputs re-inspected.** `eh_limit.out.txt`, `maxwell_check.out.txt`, `tail_structure.out.txt`, `theta_structure.out.txt`, `fibre_average.out.txt`, `validate_seeley_4d.out.txt`, `nlo_scan.out.txt`. I re-ran `validate_seeley_4d.py`: c0≈1e-33 and (4π)²c1/⟨√g a₁⟩ = 1.0i, as reported. I did not re-run `eh_limit.py`; I only inspected its output.
- **Independent check of A.** I wrote my own script in the scratchpad (`chk.py`). It takes the Fierz-Pauli quadratic form with the phase-average factor 1/8 (the same convention as `eh_decomposition.py`), with h^{μν}=a^μv^ν+v^μa^ν, q·v=0 and random q, v, a.
  - FP/6 − (1/32)q²(tr h)² equals (1/24)[v²((q·a)²−q²a²) − 2q²(a·v)²] to 1e-16 at 4 random points. So A, including its prefactors, is the FP plus Liouville-measure (dilaton-gradient) second variation.
  - The block's two sub-terms do not sum to A. The dilaton part −(1/8)q²(a·v)² is correct. The stated EH part −(q²/24)(a²v²−(a·v)²) is wrong, because it lacks the term +v²(q·a)²/24. The true value is FP/6 = (1/24)[v²((q·a)²−q²a²)+q²(a·v)²] (numerically matched). The stated EH part is not invariant under a→a+λq, whereas A is invariant: ((q·a)²−q²a²) is invariant when q·v=0.
  - Signature of A on the 3-dimensional quotient, over 20000 random draws (`chk2.py`): q time-like and v space-like gives positive definite in 3608 of 3608. Every draw with q space-like gives mixed eigenvalues (10052 with v space-like, 6340 with v time-like). A annihilates q. Since q·v=0, v is automatically space-like when q is time-like, and q time-like with v time-like cannot occur. The block's claims on gauge invariance, indefiniteness and "positive only for q time-like, v space-like" are confirmed.
- **Maxwell tail (point 1).** The tensor residual is 1e-14 to 1e-16 at points 0-4. At point 5 it is 8e-9, and K(1e5)/prediction has a visible 1.5e-3 imaginary part from the 1/s term. K(α=κ)/K(α) is about 1e-5 to 1e-9, so c0 is gauge invariant. Its sign follows G (the signs agree in all six trials), and G takes both signs. K→c0, a constant, at large s, so ∫ds diverges linearly. c0 is real and carries the F² Maxwell structure, which is expected for an a₂ term. Confirmed numerically at sampled points.
- **Log tail (point 2).** Im Q1 is purely imaginary (|Re|/|Im| ≤ 3e-6). The gauge test fails at 0.04-0.5, the covariant fit residual is 0.06-0.99, and the eigenvalues have both signs. Confirmed at six sampled points.
- **EH-form limit (point 3).** The relative error is linear in f (8e-1 at f=1, 8e-4 at f=1e-3, and so on) at 4 points, so O(f). The gauge test of Im Q1 shrinks with f. The numerical, sampled, O(f) status is stated in the block ("relative 8·10⁻⁴ …"), as required. λ₁ is given by a closed formula and is used in the fit without adjustment; I did not re-derive it separately.
- **Covariance (point 4).** The identity θ η θᵀ = c₀η + yy − tt holds to 1e-15 at six points, with coefficients 1 and −1 fixed. The fibre average is non-covariant (remainder 0.79-0.99) and c_cov changes by a factor 2.07 between rapidity 0 and 0.8, matching the block text. The average uses one base point, as the block says.
- **Steinacker 2303.08012.** I checked the paper through an ar5iv text rendering fetched with WebFetch. The first fetch was truncated and the second, from offset 200000, returned both passages.
  - Sec. 7.1.2 (near Eqs. 7.12-7.14): "is not Lorentz invariant a priori, reflecting the presence of a time-like vector field on the FLRW space-time."
  - Sec. 7.2.1 (near Eqs. 7.21-7.25): "however the latter is not Lorentz invariant, and should be suppressed to obtain a reasonable gravity theory."
  - Both quotes are confirmed, but through a summarising fetch tool and not a raw read, so treat them as "confirmed via ar5iv text, not a direct PDF read". The paper is not cited in the LaTeX, so no overstatement arises. I do not require adding it.
- **Not verified.** The left-symbol recursion, the 1D and 2D heat-kernel validations (`validate_1d.py`, `check_leading.py`) and the λ₁ formula were not independently re-derived. I rely on the end-to-end Seeley-DeWitt match above and on the agreement of tail structure, EH limit and Maxwell identification, which is evidence for the recursion but not a proof. The `controlled_kk` scripts were not rerun.

## Findings
1. **Major.** Location: block, (iii), "the sum of the Einstein–Hilbert second variation (1/6)FP[h] = −(q²/24)(a²v²−(a·v)²) and the dilaton-gradient term". The displayed EH part is wrong (see Checks). The sum of the two displayed terms is not A, and the stated EH part is not gauge invariant. Required action: replace it with the corrected form below, and say that FP is the phase-averaged quadratic form (the same factor-1/8 convention as in the scripts).
2. **Minor.** Location: block, (iv), and (i). The symbol c₀ is used twice with different meaning: the tail coefficient c₀ in (i), and the scalar in θηθᵀ = c₀η + yy − tt. In (iv) the second one is also undefined and is not constant (it takes the values 0.47-2.14 in the output). The identity is also called "exact at six points". Required action: rename the scalar in (iv) (for example c_θ(y), a scalar function of the orbit point), and write "to machine precision at six points", not "exact".
3. **Minor.** Location: block, (i), "agreement to 10⁻¹⁴ in the tensor". At sampled point 5 the residual is 8e-9. Required action: write "10⁻⁸ or better".
4. **Minor.** Location: block, (i), "the derivative expansion is not uniform at small ξ of the non-kernel directions". This mechanism is not computed; the proposal itself calls it an interpretation. Required action: soften it to "is expected to be non-uniform (a mass insertion into the massless non-kernel propagator); not computed".
5. **Minor, consistency note.** The 028 sentence "its value in the six-dimensional leaf requires the next-to-leading symbol and is not computed" stays true for the full leaf. The new block does not contradict the merged 027 and 028 text, and the sign convention +M_str Tr[χ(H_X−i0)⁻¹] with H_X=−□_X is the same. No merged sentence becomes materially false. No change to 027/028 is needed.

## Scope of what is established
**Established, with numerical checks at sampled points, within the stated hypotheses.**
- Class: Poisson limit, one loop, linear in the masses, order ε²q⁴ with the first jet frozen and the window symbol constant, Gaussian Δ_{3/4} window, supplied content with no bilinear fermion mass, formal expansion.
- Within that class, K(s)=c₀+c₁/s+… with these properties:
  - c₀ equals the Maxwell a₂ term of the induced gauge field a_b=εζα_b sinφ. It is gauge invariant, its sign is indefinite (that of G), and its s-integral diverges linearly. So there is no finite coefficient at this order in this window and this expansion.
  - c₁ is purely imaginary. For the actual window it is not gauge invariant, not covariant, and indefinite.
- In a window-family limit f→0 (not the window of the class), c₁→iλ₁A, with A the FP plus dilaton-gradient second variation of the canonical base cometric (after correction 1). This is numerical with O(f) error.
- θθᵀ = c_θη + yy − tt, and the fibre-averaged A is non-covariant at one base point. The window and the leaf both single out y^μ, and the check does not separate the two.

**Conditional or open.**
- The Pauli-Sakharov completion is conjecture and stays out of the LaTeX.
- The result identifies nothing with the emergent metric, gives no sign or value of G_eff, makes no Wick-rotation claim, and keeps spacetime emergent. This was checked in the block text; it is consistent.
- Problem F stays PROGRAMME-CONDITIONAL and OPEN. Problem E is untouched. The result does not close either problem.

**Open avenues after this bounded no-go, ranked by promise.**
1. Background-flux (Landau/nilpotent) resummation as an infrared cutoff for the c₀ divergence. It relaxes the first-order mass expansion and the frozen background.
2. A gauge/diffeo-covariant window, built from X or from the compact fibre bound. It removes the window artefacts in c₁, and it is the relaxation of the window hypothesis.
3. Non-perturbative masses: derive the Pauli-Sakharov completion for the hypoelliptic operator, including the tachyonic μ² branch.
4. Fermion mass patterns, including the M_str=0 plane and the sign of the log-weighted sum.
5. The exact second-order (non-expanded in q) Hessian of the frozen sector.
6. Relaxing the frozen first jet and the constant window symbol, to include window gradients and ∂²T. This is lower on the list because those terms carry fewer powers of q.
7. Transverse flux K, outside the class.

The c₁ result is not a statement about any window other than Δ_{3/4} (or the f→0 family), nor about the exact Moyal/matrix model.

## Recommended disposition
Revise, then integrate. This is a coherent, single-topic package. It gives a necessary consistency result for Problem F (the structure of the next-to-leading symbol of the mass-supertrace term), narrows the candidate EH-form content, and records a clear obstruction (the IR-divergent Maxwell tail and the window artefacts). Not a breakthrough, because it is conditional, numerical and reduced in scope. After the four small corrections, no second round is needed unless the integrator changes more than the corrected formula and the wording below. I recommend ACCEPT of the corrected text at the next step.

## Corrected snippet
Only finding 1 needs new displayed algebra, and it needs no new physics (verified numerically above).

```latex
the sum of the Einstein--Hilbert second variation, with the phase-averaged
Fierz--Pauli form \(\tfrac16\,\mathrm{FP}[h]=\tfrac1{24}\bigl[v^2\bigl((q\cdot a)^2-q^2a^2\bigr)+q^2(a\cdot v)^2\bigr]\),
and the dilaton-gradient term \(-\tfrac18q^2(a\cdot v)^2\) of the Liouville measure.
```

Replace "\(\tfrac16\,\mathrm{FP}[h]=-\tfrac{q^2}{24}\bigl(a^2v^2-(a\cdot v)^2\bigr)\)" in (iii) with the above.

For (iv), replace "\(c_0\eta^{\rho\sigma}\)" with "\(c_\theta\eta^{\rho\sigma}\)" and add "with \(c_\theta\) a scalar function of the orbit point". Replace "\(v^2=c_0q^2+\dots\)" with "\(v^2=c_\theta q^2+\dots\)", and "(exact at six points)" with "(to machine precision at six points)".

For (i), replace "\(10^{-14}\)" with "\(10^{-8}\) or better".

Replace "and the derivative expansion is not uniform at small \(\xi\) of the non-kernel directions" with "and the derivative expansion is expected to be non-uniform at small \(\xi\) of the non-kernel directions (a mass insertion into the massless non-kernel propagator; not computed)".

No extra assumption beyond those already stated in the block is introduced.

Files: `C:\Users\redgi\Projects\namcg-lab\proposals\030-subleading-symbol\proposal-r1.md`, `C:\Users\redgi\Projects\namcg-lab\proposals\030-subleading-symbol\block-r1.tex`, `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex` (lines 2140-2150). My check scripts are in `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\4d0177a0-6b3d-45ad-bb6d-645d2be99f00\scratchpad\` (`chk.py` for the FP decomposition, `chk2.py` for the signature test).
