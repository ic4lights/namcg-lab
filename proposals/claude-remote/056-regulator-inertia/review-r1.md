VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/0

## Verdict
I re-derived all four parts, (i) to (iv), and they hold within their stated hypotheses. The insert can be accepted after five small text revisions. They fix a notation clash for M, a closing clause that overstates scope, a loose "do not reach", an ambiguous "first paragraph", and a closing clause that repeats the 055 paragraph word for word.

## Source reading
**Digest + targeted reads. This is not a full scan.**
- `make_digest.py --check` printed DIGEST CURRENT. The digest shows dirty-chapters: yes.
- `git diff --stat` shows only appH, +22 lines. That diff is exactly the uncommitted 055 paragraph, which I read in full at appH L1529–1549.
- The digest's appH file hash (01a3bf55a888) is the hash of the working file, so the digest was built from the working tree.
- Read in full:
  - appH L1478–1553: Problem E ledger label, the 053, 054 and 055 paragraphs, and the Status paragraph. This includes L1496 (γ>0 / Anagnostopoulos2026) and L1506 ("For fixed γ>0 … nothing is stated").
  - ch17 L390–399 and L714–720.
  - ch04 L318–328. `ass:lorentzian` is defined once, at L322.
  - The tail of reports/ledger.md (055 entry).
  - proposal-r1.md and appH_insert.tex.
- Scan ruling:
  - 3(a): not due. This is ordinal 54; the full scan is due at 55.
  - 3(b): not triggered. M2 does not stop the loop and needs no milestone digest.
  - 3(c): not triggered. The insert is a new conditional paragraph and changes no definition, assumption, scope or status passage.
  - 3(d): satisfied without a full scan, because the dirty content is exactly the 055 paragraph and I read it in full.
- Unreadable files: none.

## Claim under review
**Problem E (signature).** Status quoted verbatim from Appendix H: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."

Chapter 17 agrees: "OPEN; CRITICAL PATH for the matrix-derived label". The criterion reads "Problem~E: Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})". There is no discrepancy between the two.

The original target is to derive Lorentzian signature. The package instead answers 055 avenue 1: whether a regulator-admissible linear-contour path reaches −𝔆₀ and so identifies the real-timelike limit. Its claims are (i) to (iv) as listed in the task. No label change is proposed.

## Checks performed

**(i) Identities.** I re-derived both by hand, and `exact_examples.py` confirms them symbolically (re-run).
- h = ΛᵀΛ − 2Λᵀe₀e₀ᵀΛ = M − 2ℓℓᵀ, and Re(ℓℓᵀ) = aaᵀ − bbᵀ.
- hΛ⁻¹e₀ = Λᵀηe₀ = −Λᵀe₀ = −MΛ⁻¹e₀.
- Since Re h and Im h are real symmetric, v̄ᵀ(Re h)v = Re(v̄ᵀhv) = −v̄ᵀ(Re M)v.

**(i) Inertia.**
- If Re M ≥ 0: Re h ≥ Re M − 2aaᵀ, which has n₋ ≤ 1, so Weyl monotonicity gives n₋(Re h) ≤ 1. Also v̄ᵀ(Re h)v ≤ 0, so Re h is not positive definite.
- If Re M > 0: rank-one interlacing gives λ₂(Re h) ≥ λ₂(Re M − 2aaᵀ) ≥ λ₁(Re M) > 0. Also v̄ᵀ(Re h)v < 0. So the inertia is (9,1,0).

**(i) Classes.**
- I re-checked 055 (ii) from the pair conditions 0 < β_μ+β_ν < π, using a third index. At most one β lies outside (−π/2, π/2) and at most one outside (0, π). So at least 8 lie in (0, π/2), and Re h has at least 9 negative eigenvalues on −𝔆₀.
- Hence −𝔆₀ is excluded when Re M ≥ 0. Its closure is excluded when Re M > 0, since 9 + 9 > 10.
- Euclidean contours e^{iπ/4}TᵀT have Re h > 0, so they are excluded.
- The regulator-modulus criterion holds: Tr X_αX_β is a real positive semidefinite Gram matrix, and the rank-one case suffices.

**(i) Isotropic P.**
- With QᵀPQ = 1 and QᵀηQ = E = diag(−μ₀, μ, …), we get h = μM − (μ+μ₀)ℓ'ℓ'ᵀ and hv = −μ₀Mv. Sylvester's law gives μ, μ₀ > 0.
- P⁻¹η = QEQ⁻¹. For a boosted P: P⁻¹η = c⁻¹L⁻¹ηL, using L⁻ᵀη = ηL.

**(i) Mass term.**
- iS_γ = −iγ'η_{μν}Tr A_μA_ν. Then M_γ = εΛᵀΛ + iγ'h and (ε+iγ')h = M_γ − 2εℓℓᵀ.
- For γ ≤ 0, φ ∈ [−π/2, 0]. On −𝔆₀, Re(e^{iφ}h) = −Tᵀdiag(|d|cos(β+φ))T, which has n₋ ≥ 8. This contradicts n₋ ≤ 1.
- At ε = 0 with γ < 0, the condition reduces to Im h ≥ 0, which is consistent with the 053 statement at L1506.
- I also checked that the combination of an isotropic P with a mass term goes through, with phase arg(ε/μ + iγ'). The insert does not state that case, which is why finding 2 restricts the closing clause.

**(i) γ>0 counterexample.**
- h = diag(−e^{iπ/4}, e^{−3πi/4}) = −e^{iπ/4}𝟙. Since h_μh_ν = i, S_b = iS_E.
- Re M_γ,00 = (ε+γ')/√2 and Re M_γ,ii = (γ'−ε)/√2. So the contour is admissible exactly when γ' > ε.
- The insert claims admissibility only. Whether this contour is joined to the Hermitian contour is left open: the closing lists "about fixed γ>0" among the non-statements. That scoping is correct.

**(ii) Necessity.**
- Σ_μ Tr A_μ² = ½Σ_a x^{aT}Mx^a, with no colour cross terms.
- With X = Z·diag(R, 1/R, 1/R): det 𝒢 = R⁻² det(ZᵀhZ). I checked this numerically to 1e−15 at R = 10 and R = 100.
- 𝒢₁₁𝒢₂₂, 𝒢₁₂² = O(1) and the (2,3) pair is O(R⁻⁴), so S_b is bounded.
- The regulator modulus is at least e^{εcR²/2 − C}, and it is the factor of the regulated integrand itself.
- The measure gives R⁹·R⁻¹⁰·R⁻¹⁰, and |Pf| gives R⁻⁸. The total exponent is −19, and ∫R⁻¹⁹e^{cεR²} diverges.
- det(ZᵀhZ) is not the zero polynomial: h = SᵀS and Z = S⁻¹E₃ give ZᵀhZ = 𝟙. So it is nonzero on a positive-measure part of any open set.
- The statement concerns absolute convergence only. Conditionally convergent representations are outside it, and the insert says so.

**(iii) Example.**
- I computed it by hand, and `exact_examples` confirms: M₀₀ = 1 − 16/25 = 9/25, Re M₀₁ = 0, h₀₀ = 1 − 64/25 = −39/25, Re h₀₁ = 0, h₁₁ = 4, h₂₂ = −1.

**(iii) Moments.**
- Covariance R(TᵀhT) = T⁻¹R(h)T⁻ᵀ holds by substituting y = Tx.
- At h = e^{iπ/4}𝟙 the weight is a constant phase times (det XᵀX)⁴e^{−S_E}, which is positive. So R = c_E𝟙 with c_E > 0.
- The real-congruence orbit fills e^{iπ/4}Pos, which is a maximal totally real set. The identity theorem then extends the formula to all of 𝔆₀, using that 𝔆₀ is connected (as used in 055 (iv)) and that the denominator is nonzero there (055 (iv)).
- ΛR(h)Λᵀ = c_E e^{iπ/4}Λh⁻¹Λᵀ = c_E e^{iπ/4}η. This matches 053: η₀₀ gives e^{−3πi/4}.
- Evenness R(−h) = R(h) holds because (det)⁴ has degree 12 and S_b is quadratic in h. So the value is −c_E e^{iπ/4}η on −𝔆₀.

**(iii) Path argument.** I checked that it is airtight within its hypotheses.
- At fixed ε, compactness gives a uniform lower bound on Re ΛᵀPΛ. Together with |e^{iS_b}| ≤ 1 and polynomial |Pf|, this justifies Stokes.
- On the end contour, h ∈ 𝔆 gives Cauchy–Binet domination.
- The limit is regulator-independent for every positive definite P (053, proved at N = 2, degree 2 < 14).
- If the end contour were in −𝔆₀, its value would be the negative of that limit, which is impossible since c_E ≠ 0.
- The argument does not use the inertia lemma, so its failure for anisotropic P does not affect it. It does not exclude a −𝔆₀ contour that no such path reaches; the insert correctly says "not decided here". The numerical anisotropic conjecture is kept out of the insert.

**(iv) A→iA.**
- S_b has degree 4, and Pf has degree 8(N²−1); i^{8(N²−1)} = 1 (re-run in `exact_examples`). The Jacobian is constant.
- Λ'ᵀ(ik) = Λᵀk = q, so the mode at ik is bounded on Λ'.
- (ik)·(ik) = κ² gives F_E(e^{iπ/4}κ²), consistent with the 055 −𝔆₀ formula.
- Re M > 0 implies Re M⁻¹ > 0, by v = Mu. Then kᵀk = qᵀ(ΛᵀΛ)⁻¹q has positive real part for real q. This needs M = ΛᵀΛ, which is the point of finding 1.

**Scripts.**
- Re-ran `apply_check.py` (report mode) and `exact_examples.py`. The output matches the .txt files and every hash in the proposal: baseline 550508 / 01a3bf55…d7a9; anchor 61 bytes, count 1, L1551; result 561124 / 587df3f2…3948.
- Confirmed that the insert in the proposal appendix is byte-identical to appH_insert.tex.
- My own check `gk056.py` in the scratchpad (C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk056.py) found no inertia violations among random Re M > 0 samples (P = 𝟙 and boosted P). It found at least 9 negative eigenvalues of Re(e^{iφ}h) on sampled −𝔆₀ for φ ∈ [−π/2, 0], confirmed the det 𝒢 scaling, and confirmed the exponent −19. The sample counts are small; the proof is analytic.
- I did not re-run `moments_check` (Monte Carlo, 6e5 samples), `inertia_checks` (about 5 min) or `aniso_search`. I inspected their outputs. They are checks, not proofs. The Monte Carlo tests only points of 𝔆₀; the sign on −𝔆₀ follows from evenness, which I verified.

**LaTeX.**
- The only reference is `\ref{ass:lorentzian}`, which exists once. There are no labels or citations, `\mathbb 1` is already used in appH, and there is no process language.
- Anagnostopoulos2026 is not used in the insert.
- I ran no build myself, because it would write outside the proposal folder. The researcher reports a two-pass scratch build at exit 0; I have not independently verified it.

**Labels.** No label changes.

## Findings
1. **Minor — (i), mass sentence; also (ii) and (iv).** (i) redefines M as the mass form ("With M now the matrix of this form on the contour"), and (ii) and (iv) then keep using M. Read literally, (iv)'s identity Σ(k^μ)² = qᵀM⁻¹q is false for γ ≠ 0. Likewise (ii), which is stated for M = ΛᵀΛ, is silently needed for the mass form by the closing γ ≤ 0 claim. **Required:** introduce M_γ (replacements R1, R2, R3 below).
2. **Minor — closing paragraph.** "Definition~(A) or a regulator as in (i), γ ≤ 0" can be read as covering an isotropic P combined with a mass term. (i) proves the mass case only for P = 𝟙. The extension holds (I checked it), but it is not in the text. **Required:** restrict the clause (R6).
3. **Minor — (ii), "In particular…".** As written, "do not reach −𝔆₀" is stronger than what is shown. Paths of matrices into −𝔆₀ exist. What is shown is that their end contour cannot carry an absolutely integrable regulated integrand. **Required:** R4.
4. **Minor — (iii), "the first paragraph" (twice).** This is ambiguous, because the section's first paragraph is the Ledger label. **Required:** R5.
5. **Minor — closing sentence.** It repeats the 055 closing clause word for word ("so no signature is derived and Assumption~\ref{ass:lorentzian} is not discharged") on consecutive paragraphs. This defect was already flagged as F5 in 055. **Required:** R7.

## Scope of what is established
**Proved, every N, algebraic.**
- On a linear contour whose regulator modulus is bounded by 1 (Definition (A), or an isotropic P with P⁻¹η having a nine-fold eigenvalue, or P = 𝟙 with γ ≤ 0), h ∉ −𝔆₀.
- If Re M > 0, Re h has exactly η's inertia, and Euclidean contours are excluded.
- The γ > 0 counterexample is exact, but it shows admissibility only.
- The A→iA identity, and the absence of a bounded mode at imaginary timelike momentum when Re M > 0.

**Proved at N = 2.**
- Absolute integrability of I_ε[1] forces Re M ≥ 0. So every damped, absolutely convergent linear contour lies in 𝔆₀, and real causal k is unreachable. This closes 055 avenue 1 for linear contours within absolute convergence.
- R(h) = c_E e^{iπ/4}h⁻¹ on 𝔆₀.
- For any positive definite P, the end points of regulator-decaying paths with Re iS_b ≤ 0 lie in 𝔆₀.

**Not established.**
- Pointwise exclusion of −𝔆₀ for anisotropic P (a numerical conjecture, correctly kept out of the insert).
- Necessity for N ≥ 3.
- Anything about fixed γ > 0 beyond admissibility.

Classification: PROGRAMME-CONDITIONAL sharpening and a bounded no-go (M2). The η is an input, so no signature is derived. Problem E remains OPEN, CRITICAL PATH for the matrix-derived label, PROGRAMME-CONDITIONAL. This is not a breakthrough.

**Open relaxations, ranked as most promising for the infrared / full-GR derivation:**
1. Fixed γ > 0. Decide whether the components of D ∩ GL(10,C) join η to the −𝔆₀ contour at e^{iπ/8}, e^{−3πi/8} along non-diagonal paths, then take the ε→0 limit there. This is the only hypothesis under which the regulator obstruction is lifted.
2. Non-linear (thimble) contours at real causal k, N = 2. These must reproduce ⟨Tr A_μA_ν⟩ → c_E e^{iπ/4}η.
3. Conditionally convergent representations, or a direct oscillatory analysis at real timelike or null k (hypothesis H3).
4. Colour-mixing linear maps in GL(30,C).
5. Versions of (ii) and (iii) for N ≥ 3, which need a lower bound on |Pf| near commuting configurations.
6. Pointwise exclusion of −𝔆₀ for anisotropic P.
7. N→∞ taken first; Definitions (B) and (C).

Even a positive answer to any of these would concern an η that is put in by hand. Deriving the signature still needs a mechanism that selects η.

## Recommended disposition
Revise with R1–R7 below, which are text-only and add no new mathematics. Re-run apply_check for the new hashes and repeat the scratch build. Integrate after a plain ACCEPT.

## Corrected snippet
No extra assumptions are needed. Each original string below occurs exactly once in appH_insert.tex (checked).

**R1.** Replace
`With \(M\) now the matrix of this form on the contour, \((\epsilon+\mathrm i\gamma')h=M-2\epsilon\ell\ell^{\mathrm T}\).`
with
`Write \(M_\gamma=\epsilon\Lambda^{\mathrm T}\Lambda+\mathrm i\gamma'h\) for the matrix of this form on the contour; then \((\epsilon+\mathrm i\gamma')h=M_\gamma-2\epsilon\ell\ell^{\mathrm T}\).`

**R2.** Replace
`while by the identity above it has at most one when \(\operatorname{Re}M\) is positive semidefinite.`
with
`while by the identity above it has at most one when \(\operatorname{Re}M_\gamma\) is positive semidefinite.`

**R3.** Replace
`every linear contour on which \(I_\epsilon[1]\) converges absolutely has \(\operatorname{Re}M\) positive semidefinite.`
with
`every linear contour on which \(I_\epsilon[1]\) converges absolutely has \(\operatorname{Re}M\) positive semidefinite, and the same argument applies to \(\Lambda^{\mathrm T}P\Lambda\) and to \(M_\gamma\).`

**R4.** Replace
`In particular, paths along which \(\operatorname{Re}\mathrm iS_{\mathrm b}\le0\) while \(h\) leaves the closure of \(\mathfrak C\) do not reach \(-\mathfrak C_0\).`
with
`In particular, no path along which \(\operatorname{Re}\mathrm iS_{\mathrm b}\le0\) while \(h\) leaves the closure of \(\mathfrak C\) ends on a contour with \(h\in-\mathfrak C_0\) on which the regulated integrand is absolutely integrable.`

**R5.** Replace `which is the limit of the first paragraph.` with `which is the limit of the paragraph on the regulated Lorentzian integral.`
Also replace `The first paragraph gives this limit` with `That paragraph gives this limit`.

**R6.** Replace
`Definition~(A) or a regulator as in (i), \(\gamma\le0\),`
with
`Definition~(A) with \(\gamma\le0\) or a regulator as in (i) with \(\gamma=0\),`

**R7.** Replace
`The inertia found in (i) is that of the \(\eta\) put into \(S_{\mathrm b}\), so no signature is derived and Assumption~\ref{ass:lorentzian} is not discharged.`
with
`The inertia found in (i) is that of the \(\eta\) put into \(S_{\mathrm b}\), which the regulator carries over to every admissible contour but does not select, so Assumption~\ref{ass:lorentzian} is still required.`

Files reviewed:
- C:\Users\redgi\Projects\namcg-lab\proposals\056-regulator-inertia\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\proposals\056-regulator-inertia\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (L1478–1553)

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/0
