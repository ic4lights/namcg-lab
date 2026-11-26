VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The Gaussian lemma, the supertrace sum rules, the closed forms and the SD identities check out. The tangency justification in the cone-window paragraph is mathematically wrong as written, and the block uses undefined symbols (`D_1`, `g`) and overstates some numerical precision. These must be fixed before integration.

## Source reading
- Full scan, because the proposed integration is ordinal 25 (CLAUDE.md 3(a)) and the tree is dirty (3(d)).
- Manifest read in full, 30 files: ch01–ch18 (ch17 first, then the rest in order) and appA–appL (A, B, C, D, E, F, G, H, I, J, K, L).
- appH (2581 lines) was read in several large ranges plus targeted ranges. These covered lines 1–400, 400–820, 820–1185, 1183–1212, 1205–1545, 1544–1943, 1944–2002, 2001–2080 and 2078–2582.
- `scripts/make_digest.py --check` printed `DIGEST STALE`. This is expected given the uncommitted 025 block. The digest was not used for navigation.
- Unreadable files: none.
- Scripts and my own checks were run in `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\4d0177a0-6b3d-45ad-bb6d-645d2be99f00\scratchpad`. Nothing was written in the repo (`git status` shows only `M chapters/appH-microscopic-proofs.tex`).

## Claim under review
- **Claim.** Conditional, bounded results for the weight-two (Einstein–Hilbert-type) coefficient in the conjugate-coordinate class, in five parts:
  - a Gaussian-window lemma;
  - a fibre-bounded cone-window moment;
  - the Zeeman rates;
  - the vector/ghost/spin terms of the invariant sector;
  - a supertrace remainder.
- **Original target (Problem F).** Appendix H, verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- **Problem E (touched only by the caveat on Assumption `ass:lorentzian`).** Appendix H, verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- **Chapter 17.** The current criterion, §"What finished would mean", lists A, B, C, D1, E, F, G-derived and N as critical path. The block changes no label.

## Checks performed

### Direct, re-derived or re-run

1. **Mass-moment lemma, by hand.**
   - Principal-value identity: 1/(σ−i0) = i∫₀^∞ ds e^{−isσ}.
   - Gaussian average: ∏(1+isλ_k)^{−1/2}, with Re(1+isλ)=1, so the principal branch is correct.
   - Contour rotation: s = e^{−iθ}r, θ from 0 to π/2.
     - For λ₀ = −c, Im(1−isc) = −cr·sin(π/2−θ) < 0 throughout, so the limit is (1−cu−i0)^{−1/2}.
     - The branch cut of the λ₀ factor lies on the negative imaginary axis for u > 1/c, which gives the factor i(cu−1)^{−1/2}.
     - The λ_k > 0 branch points lie on the positive imaginary axis.
     - The arc contribution vanishes as s^{−2}.
   - The substitutions u = (1∓v²)/c give exactly the two displayed formulas. Re M > 0 and Im M > 0 follow.
   - For λ_k = λ the closed form 2/(λ+c) follows from ∫₀¹(1+k−kv²)^{−3/2}dv = 1/(1+k).
   - `gaussian_pv_lemma.py` re-run: 8e-11 against the contour integral over 300 spectra; 4000 samples all positive.
   - The inertia claim (one negative, three positive, two zero) is Sylvester's law applied to σ(Box) of signature (3,1) and rank 4. The rank is exactly 4 for y⁴≠0, since the Gram determinant is ℓ²|y⁴|⁶ (appH, "where the flux eigenvalues coincide"). It does not rest on sampling.
   - **Result: proved, as claimed.**

2. **Five early scripts (outputs were not saved), all re-run.**
   - `tangency_identity.py`: max deviations over 60 points are |c−½| 6.7e-15, a_k spread 4.4e-13, c/a vs ℓ²/y⁴² 9.7e-14, |w|²−1−ℓ²/y⁴² 7.95e-10, time component 7e-15. This supports "10⁻⁹ or better".
   - `cone_window_geometry.py`: the S_uu eigenvalues are (−½, a, a, a) with a = ½ sinh²τ; Schur residual ~1e-16; |w| = cothτ.
   - `cone_window_moment.py`: Δ = O(10⁻³) against I₀ ~ 1–70 at the sampled points. I₀ = 8π²/cosh²τ matches.
   - `shell_apex_lemma.py`: I₀ matches 2π²·2/(a+c) = 32.1721. The trace identity tr(S⁻¹J) = I₀tr(S⁻¹)/2 holds to 1e-15. This means the quadratic polynomial satisfies the Q_L wave equation. The apex-inside check at |p|=0.45, r=1 gives 14.1914 vs 14.1898.
   - `sd_scalar_vs_exact.py`: SD E+R/6 equals the 025 exact D₁ to ~1e-125 at all 3 points (125 digits confirmed).
     - The script also prints "det check ... False". That is a malformed test condition; the explicit inverse check passes.
     - Please fix or remove that test.

3. **Independent P-scan** (my own script `pscan.py` in the scratchpad, reusing the proposal's `P_brute_vec`; threshold 1.2991, r = 1).

   | Offset P | Quadratic formula vs brute-force quadrature |
   |---|---|
   | ≤ 1.30 (N=96) | agree to ≤ ~4e-3 on values 12 → 5 |
   | 1.32 | diff −0.062 |
   | 1.35 | diff −0.233 |
   | 1.40 | diff −0.645 |
   | 1.50 | diff −1.79 |

   - Axis and off-axis directions give identical results.
   - The sharp departure at tangency is confirmed numerically.
   - The proposal's stated reason for it is wrong; see Finding 1.

4. **Zeeman closed forms.**
   - `flux_closed_forms.py` re-run: centre-plane A_c² and B_c² match the closed forms to 2e-14 and 1.2e-13; vertical-plane deviation 1.3e-10; base B = 2.8e-13.
   - Base maximum of A_b² vs (1+a²)/2 is only 6.2e-5 over 3000 sampled directions, and the run reports 59 points, not 60 (a NaN point; see Finding 3).
   - `centre_flux_kernel.py` re-run: q_c = A²−B² ∝ (1−a²)/(1+2a²), changing sign at a=1. 19 of 40 points are magnetic-dominated, 21 electric-dominated.
   - Fibre rate 2A = 2s_f sinhτ with |ζ|² = 2s_f²: correct. The determinant factorisation (σ²−4B²)(σ²+4A²) follows from the eigenvalues ±2B, ±2iA.

5. **Invariant sector.**
   - `sd_vector_spin.py`, `sd_dirac_spin.py` (saved outputs): tr(E+R/6) = 4D₁ + 6s²(1+a²)/(t+isa²) − 4isμ² agrees to ~1e-123 at 3 points, including an off-axis point and μ²=−3, 1.
   - The Dirac trace is ½ the vector spin term for both signs.
   - `closed_forms_Q.py` and `invariant_sector_Q.py` re-run:
     - Re Q_sp = −8/(1+a²) and Re Q_μ = −2μ²/(1+a²).
     - Hence Re[Q_sp + 4Q_μ] = 16/(1+a²) for μ²=−3, and Re Q_bos = (2+n_ex)Re Q + (16−2n_exμ_i²)/(1+a²). Both agree with the table (spot-checked at a=1: 10.2274 = 2.2274 + 8).
   - `spin_tail_6d.py` re-run: C is purely imaginary, with a sign change between a=0.924 (−) and a=1.028 (+), matching 2q_c.
   - I did not re-derive the Seeley–DeWitt matrix machinery independently beyond these re-runs.

6. **Supertrace.**
   - `susy_sum_rules.py` re-run:
     - Σ_V and Σ_D satisfy the so(3,1) algebra with the same sign.
     - tr(Σ_DΣ_D) = ½ tr(Σ_VΣ_V) for all index pairs.
     - str(s) − 4(cos sB − cosh sA)² = 0 identically; the s⁴ coefficient is (A²+B²)².
     - The s² coefficient is vector 4(A²−B²) vs Dirac 2(A²−B²), so 1·vector − 2·Dirac = 0.
   - Consistency with 019: count N_tot = 8−4n_D = 0 and index b = 1−n_D/2 = 0 at n_D = 2. Here 16 real components at weight −½ equal n_D = 2 Dirac at weight −1. The Euclidean order α⁴ term (x²−y²)²/16 maps under x→iA, y→iB to (A²+B²)²: consistent.
   - 025: the mode-count term is proportional to N_b−N_f, which is 0 here. Consistent.
   - No merged sentence becomes materially false, so no PRIOR-CLAIM-ERROR. See minor Finding 7 on the 025 threshold wording.

7. **Compile.** `compile_check_r1.py` re-run with a scratchpad `SCRATCH`: anchor unique, pdflatex–bibtex–pdflatex–pdflatex rc 0, 0 errors, 0 undefined, 0 multiply defined, 283 pages.

8. **Anchor.**
   - `\section{Problem G: HBEV}` occurs exactly once (line 2078).
   - It is immediately preceded by the 025 block, whose last sentence is "This changes no ledger label; Problem~F remains open." (line 2076).
   - Labels `ch:vierbein-emergence` and `ass:lorentzian` exist once. No new labels, bib entries or `\cite`.

### Not verified
- The Seeley–DeWitt matrix machinery beyond the re-runs.
- The fermion content (a supplied input).
- Any literature: none is cited in the block. The SME scout reference (2405.09804) is not used as input and was not independently verified.

## Findings

**1. Major. Location: the "Mass moment in the fibre-bounded cone window" paragraph, the sentence "For spacelike p the same expression holds up to the tangency distance ... follows from the unique continuation ... to the domain of dependence".**
- *Finding.* The stated justification is incorrect.
- *Reason.*
  - P(p) = PV∫_{|x−p|<R} d⁴x/Q_L is a global solution of the Q_L wave equation. I confirmed that the quadratic polynomial satisfies it, via the trace identity.
  - John/Holmgren unique continuation from the open ball |p|<R reaches only the domain of dependence of a spacelike slab inside the ball.
  - The time-like line through p (v=0) at spatial distance P > R never meets the ball.
  - So "every causal line meets the ball iff P < r√(1+v_c²)" is false. That formula is the distance of the nearest null line, not the farthest causal line.
  - Holmgren therefore does not reach |p⃗|>R on p⁰=0.
  - The observed validity range ends exactly at the touching of ∂B with the characteristic cone of the apex. That is a Landau-type singularity of P(p), which is consistent with the sharp numerical threshold at 1.2991. It is not a domain-of-dependence statement.
  - The numerical observation stands. The mechanism offered does not, and the claim must not be presented as following from a theorem.
- *Required action.* Replace the sentence by a numerical-observation statement (see corrected snippet 1). Do not assert unique continuation or a domain-of-dependence mechanism. The sign claim Re⟨·⟩>0 must remain explicitly conditional on this observation.

**2. Major. Location: the opening paragraph and the "Vector and ghost sectors" paragraph.**
- *Finding.* The block uses objects that are not defined in the manuscript.
  - The opening paragraph refers to "the functions \(g\) and \(Q(a)\) of the exact invariant sector". No \(g\) function appears in the 025 invariant-sector paragraph. Only \(D_0\), \(Q(a)\), \(G^{\mu\nu}\) and "the subtraction at \(x=1\)" appear.
  - The vector paragraph writes tr(E+R/6) = 4D₁ + ... and calls \(D_1\) "the scalar first correction of the preceding paragraph". \(D_1\) does not occur in the preceding paragraph; it exists only in 025's scripts.
  - The convention "tr(E+R/6)" (rather than the manuscript's a₁ = tr(R/6−E)) is not stated. It is the density of e^{tΔ+...} with exponent Δ+E.
  - The symbol \(x=s/t\) is introduced only in the proposal's conventions.
- *Required action.* Define \(D_1\) as the first-order coefficient of the diagonal, D = D₀(1+D₁+…), with D₁ homogeneous of degree one in (z,w) = (t−is, is) (taken from 025 `s0_exact_expansion.py`). State the E+R/6 sign convention. Delete the reference to \(g\), or define it. Define \(x\) where it is used.

**3. Minor. Location: the "Zeeman field and electric growth" paragraph, "At the same 60 points (10⁻⁹)".**
- *Finding.* The saved and re-run output of `flux_closed_forms.py` covers 59 points. One point is singular in the whitening (division-by-zero warning).
  - The base-plane maximum A_max = |u|coshτ/√2 is confirmed only to 6e-5 over 3000 sampled directions.
  - Only the centre and vertical plane forms and B_base are at ≤1.3e-10.
- *Required action.* State the point count and the base-maximum accuracy honestly, or sample a point set that avoids the singular point. State why the point is singular.

**4. Minor. Location: "The fibre-driven electric rate ... bounded in the window ... and not removed by the fibre bound".**
- *Finding.* The sentence is internally ambiguous. The rate is bounded by an expression linear in the base cutoff, not independent of it.
- *Required action.* Say that the rate is bounded by a quantity growing linearly with the cutoff, whose fibre part is bounded independently of it.
- *Related.* "The determinant stays finite" should read: the log det has only integrable logarithmic singularities at σ=±2B, at the leading symbol (as 025 states).

**5. Minor. Location: "Lorentzian moment finite: ... simple pole against a Lipschitz window function".**
- *Finding.* The window χ(|u|²−|ζ|²)1_{|u|≥|ζ|} has a jump at the cone edge when χ(0)≠0, so it is not Lipschitz. The edge is tangent to the null cone at one point. Finiteness there is exactly the content of the tangency formula.
- *Required action.* Rest the finiteness claim on the conditional shell formula, not on "Lipschitz".

**6. Minor. Location: notation.**
- `A`, `B`: the electric/magnetic eigenvalues vs. "second variation under \(A\)" (matrix fluctuation \(A^a\)).
- `\mathcal J` is used three times: \(\mathcal J_{ab}\), \(\mathcal J_a\), \(\mathcal J_c\).
- `S`: the form σ(Box) vs. \(S^2=2C_{41}-C_{42}\) in the preceding paragraph.
- `⟨…⟩_W` denotes an integral, not an average.
- *Required action.* Rename or define. Suggested: eigenvalues \(a_e,b_m\) or \(\mathcal A,\mathcal B\); a different symbol for the Jacobian.

**7. Minor. Location: the "Flux" statement of 025 and the zero-crossing claim at |y⁴|=ℓ.**
- *Finding.* 025 says F_abF^ab is "negative for (y⁴)²≲0.4, positive above". That is a sampled-points statement; the exact threshold on the kernel plane is |y⁴|=ℓ, and the sampled ℓ varied. The kernel-plane signs are consistent with 025 (small y⁴ electric-dominated, F²<0); the vertical plane has the opposite sign pattern.
- *Required action.* Add one clause: the exact kernel-plane threshold is |y⁴|=ℓ and replaces the sample-dependent value; state which plane. The 025 sentence is not materially false (it concerns sampled points), so there is no PRIOR-CLAIM-ERROR.

**8. Minor. Location: the "Supertrace" paragraph's closing sentence.**
- *Finding.* Two wording problems, both within the block's own scope:
  - "which is then a property of the next order" is a conclusion by elimination. The order-F⁴ Zeeman character is not the full next-order coefficient, and the A-dependence of the mass-supertrace term is not computed (the scope paragraph says so).
  - "−Σm² ... mass supertrace 4μ²+n_exμ_i² times the positive moment" omits the explicit minus sign relative to Q_μ=−μ²J. The sign of the supertrace itself is not claimed.
- *Required action.* Reword to "does not by itself carry; whether it arises at higher order or through the A-dependence is not computed". State the sign explicitly.

**9. Minor. Location: stale-sentence interaction with 025.**
- The 025 closing sentence "the Lorentzian moments are not computed in the fibre-bounded window, and the positivity of the moment is numerical" is partly superseded by the new block, and the block says so. This is acceptable. Optionally the integrator may refine the 025 sentence (author's choice).

**Nothing else is blocking.** The proposal was candid about the unsaved outputs, and re-running them reproduced the claims. The significance is modest: one genuinely proved lemma, a conditional exact shell identity, a bounded no-go on the species-independent part of the weight-two coefficient for the supplied content, and a sharp correction of an expected O(Q²) displacement term. This is a coherent package (single context: Lorentzian window moments for the weight-two term), and it should not be split.

## Scope of what is established

**Proved.** For every Gaussian window of the class, Re M>0 and Im M>0, using that σ(Box) is rank 4 with signature (3,1) for y⁴≠0.

**Established as exact identities or high-precision checks at sampled points.**
- The geometric identities (tangency, |w|=cothτ), at 60 points.
- The Zeeman closed forms on three planes.
- The SD identity to 120+ digits, and its agreement with the exact scalar kernel.
- E_spin = 6s²(1+a²)/(t+isa²).
- Q_μ, Q_sp and the sum rules.
- The Zeeman character identity.
- tr(Σ_DΣ_D) = ½ tr(Σ_VΣ_V).
- Count and index cancellation for the supplied content (consistent with the merged 019 rules).

**Conditional.**
- The shell identity beyond the apex-inside case. Numerically supported; mechanism not established (Finding 1).
- The sign of Re⟨σ⁻¹⟩_W, which rests on the preceding item.
- The supplied fermion content (16 real components at weight −½, n_ex=6, no bilinear mass).
- The formal SD coefficient being the weight-two term on the full leaf.

**Not established.**
- The sign or size of G_eff or w (nothing in the block claims it).
- The second variation under the matrix fluctuation.
- The exact vector kernel.
- The next-order term.
- The real/imaginary identification of the action.
- Moyal terms.
- A window built from dynamical matrices.
- Any Wick-rotation statement (none is made; the contour rotation in the Schwinger parameter is not a spacetime Wick rotation).
- Spacetime stays emergent: the block identifies no induced metric with the emergent metric of Chapter `ch:vierbein-emergence` and leaves Assumption `ass:lorentzian` in place (Problem E).

**Classification.** PROGRAMME-CONDITIONAL. Problem F remains OPEN. No label change is proposed.

**Hypothesis class of the no-go (state it this way in the LaTeX).**
- Poisson limit, one loop, leading symbol.
- The invariant (s=0, fibre-constant) sector.
- The four-matrix class with μ²=−3.
- Gaussian windows or the cone window of the stated form.
- The supplied fermion content, no bilinear fermion mass, equal bosonic and fermionic window.
- Weight-two term at A=0, species-independent part.

**Open avenues after this no-go** (relaxations that could still favour the infrared or full-GR derivation), ranked by promise:
1. **The A-dependence (second variation under the matrix fluctuation) of the mass-supertrace term and of the Zeeman-character order s⁴ term** (most promising). The count and index cancellations only remove the species-independent part. The block states this explicitly, and it is the natural continuation.
2. **Fermion content or mass pattern beyond "no bilinear mass"**: supersymmetric bilinear terms, fermion masses, or the eight-matrix (5,1) set. The mass supertrace need not vanish or have indefinite sign there. This also relaxes the supplied-input hypothesis.
3. **A window with |p|<r**, or a proof of the tangency continuation, to turn the conditional sign into a theorem. Note that the ranking in the researcher's list put this second.
4. **Exact vector kernel and Plancherel in the five-matrix presentation**, which would test the SD-coefficient-as-weight-two-term assumption.
5. **Real/imaginary identification of the action, and non-Gaussian windows built from dynamical matrices.**
6. **Moyal terms**, and branching of SO(4,1) to SO(3,1) for the non-central C₃₁.

## Recommended disposition
Revise, then integrate. Specifically:
- Correct the tangency justification (Finding 1).
- Define or remove the undefined symbols (Finding 2).
- Fix the point-count and accuracy statements (Findings 3–4).
- Tighten the supertrace wording (Finding 8).
- Rename the clashing symbols (Finding 6).
- Re-submit for a quick confirmation of the changed sentences; the mathematics does not need re-derivation.
- Also save the outputs of the five early scripts as `.out.txt` files (the proposal's own request).

## Corrected snippets
These need no new physics. They only restate what the scripts show and define existing 025 objects.

1. **Replace the sentence** "For spacelike \(p\) the same expression holds up to the tangency distance \(R\coth\tau\): this follows from the unique continuation ... it is argued, not proved here." by:
```latex
For spacelike \(p\) with \(|p|\ge R\), quadrature indicates that the same
expression continues to hold up to the tangency distance \(R\coth\tau\)
(agreement to \(10^{-3}\) in the sampled cases) and departs from it beyond; this is a
numerical observation and is not proved here.
```
2. **After the Zeeman-field sentence "At the same \(60\) points (\(10^{-9}\))"**, state the point count and accuracy actually obtained, for example: "At \(59\) of the \(60\) points (one point is singular in the whitening), to \(10^{-9}\) except for the maximum over the base plane, which is obtained from \(3000\) sampled directions to \(6\cdot10^{-5}\)".
3. **Replace** "bounded in the window and not removed by the fibre bound" by:
```latex
whose fibre part is bounded independently of the base cutoff and whose base part is bounded by a quantity linear in it; the growth is a property of the Schwinger representation and is not removed by the fibre bound
```
4. **Add the definition of \(D_1\)** at its first use:
```latex
Write the diagonal of \(\mathrm e^{z\Delta_{H^4}+w\Delta_{H^3}}\) as \(D=D_0(1+D_1+\dots)\), with \(D_1\) homogeneous of degree one in \((z,w)=(t-\mathrm is,\mathrm is)\); \(\operatorname{tr}(E+R/6)\) is the first Seeley--DeWitt density of \(\mathrm e^{t\Delta_{H^4}-\mathrm isH_V}\) in the convention that the exponent is \(\Delta+E\).
```
   Remove the reference to "the function \(g\)" in the opening paragraph, or define it.
5. **Replace** the final clause of the supertrace paragraph by:
```latex
the curvature and connection part of the weight-two term therefore does not by itself carry the Newton coefficient for this content; whether it arises at higher order of the expansion or through the dependence on \(A\) is not computed.
```
   State the sign explicitly: the remaining coefficient is \(-\bigl(4\mu^2+n_{\mathrm{ex}}\mu_i^2\bigr)\mathcal J_a\), without claiming a sign for the supertrace.
