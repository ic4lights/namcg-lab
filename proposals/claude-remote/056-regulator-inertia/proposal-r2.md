# Proposal 056-regulator-inertia, round 2

## Changes r1 -> r2

| # | Review item | Change |
|---|---|---|
| 1 | F1 (minor): M redefined for the mass form | Insert R1, R2, R3 applied verbatim: the mass form is now M_γ = εΛᵀΛ + iγ'h, the identity reads (ε+iγ')h = M_γ − 2εℓℓᵀ, and (ii) states that the necessity argument applies to ΛᵀPΛ and to M_γ. M = ΛᵀΛ throughout (ii) and (iv). Proposal: M_eff renamed M_γ everywhere (Result, Step 1, Step 2, verification sections, gatekeeper instructions). |
| 2 | F2 (minor): closing clause scope | Insert R6 applied verbatim: "Definition (A) with γ ≤ 0 or a regulator as in (i) with γ = 0". |
| 3 | F3 (minor): "do not reach −C_0" too strong | Insert R4 applied verbatim. Proposal Result item 2 and Step 2 consequence reworded to match ("no such path ends on an absolutely integrable −C_0 contour"). |
| 4 | F4 (minor): "the first paragraph" ambiguous | Insert R5 (two parts) applied verbatim. Proposal Step 3 wording matched ("the paragraph on the regulated Lorentzian integral"). |
| 5 | F5 (minor): repeated 055 closing clause | Insert R7 applied verbatim. |
| 6 | Mechanics | `apply_r2_edits.py` requires the r1 hash (b58cda7e…056c), checks that each old string occurs once before and each new string once after, keeps the r1 bytes as `appH_insert.r1.tex`, and refuses a second run. Output in `apply_r2_edits.txt`. Hashes, apply_check output and the scratch build are refreshed. |

No mathematics, numerics or scripts other than apply_r2_edits.py changed. Everything below is the r1 text with these corrections.


## Result

Avenue 1 of review 055-r2 asked for a regulator-admissible path from the Hermitian contour to −C_0 that keeps
Re iS_b ≤ 0 but leaves cl(C). If one existed, the ε→0 limit at real timelike k would be identified with
F_E(e^{iπ/4}κ²). **The answer is no.** The obstruction is the regulator itself, not the damping set. It is
precise, and for Definition (A) it needs no hypothesis on paths at all.

1. **Regulator inertia lemma (exact, linear algebra, every N).** Write M = ΛᵀΛ, so the regulator of
   Definition (A) on A = ΛX is ε Σ M_{αβ} Tr X_αX_β, and h = ΛᵀηΛ.
   - Then h = M − 2ℓℓᵀ, where ℓ = a + ib is row 0 of Λ, so Re h = Re M − 2aaᵀ + 2bbᵀ.
   - Also v = Λ⁻¹e_0 satisfies hv = −Mv.
   - Hence if Re M ≥ 0, Re h has at most one negative eigenvalue and is not positive definite.
   - If Re M > 0, Re h has exactly the inertia of η: 9 positive eigenvalues and 1 negative.
   - On −C_0, Re h has at least 9 negative eigenvalues (055 (ii)). So no contour whose regulator factor is
     bounded by 1 has h ∈ −C_0, and none with Re M > 0 has h ∈ cl(−C_0).
   - The same holds for every regulator matrix P for which P⁻¹η has a nine-fold eigenvalue, e.g. a boosted
     regulator cLᵀL.
   - It also holds with a Lorentz-invariant mass of either sign γ ≤ 0. The identity used is
     (ε+iγ')h = M_γ − 2εℓℓᵀ, together with the fact that at least eight β_μ lie in (0, π/2).
2. **Necessity (proved at N = 2).** If Re aᵀMa < 0 for some real a, the integrand of I_ε[1] is not absolutely
   integrable on the contour, at any ε > 0. Hence at N = 2:
   - every damped linear contour that carries the regulated integral absolutely convergently lies in C_0;
   - so the 055 sector no-go (iii) covers all of them, whatever path leads there;
   - in particular no path with Re iS_b ≤ 0 that leaves cl(C) ends on a −C_0 contour on which the regulated
     integrand is absolutely integrable.

   The 055 example A_0 = X_0, A_i = e^{2πi/3}X_i has Re M = diag(1, −1/2, …). The regulator grows on the
   spatial matrices, so that contour is not a contour of I_ε at all.
3. **Any positive definite regulator, N = 2 (paths).** For anisotropic P, the inertia in item 1 can fail. An
   exact example has Re ΛᵀPΛ > 0 and two negative eigenvalues of Re h. Even so, no admissible path ends in
   −C_0. The reason is a sign:
   - on C_0, ⟨Tr X_αX_β⟩_h = c_E e^{iπ/4}(h⁻¹)_{αβ};
   - so ⟨Tr A_μA_ν⟩ = +c_E e^{iπ/4}η_{μν} on every C_0 contour, which is the 053 limit;
   - by evenness in h, the value is −c_E e^{iπ/4}η_{μν} on every −C_0 contour;
   - a path to −C_0 would make the regulator-independent 053 limit equal its own negative.
4. **What −C_0 contours compute (exact, every N).** Write Λ = iΛ'. Since A → iA leaves S_b and Pf M invariant,
   −C_0 integrals of O are C_0 integrals of O(i·).
   - The real-timelike value F_E(e^{iπ/4}κ²) is therefore the Fourier mode at the imaginary momentum ik. It is
     numerically the 055 real-spacelike limit at k·k = κ².
   - Imaginary timelike momenta have no bounded mode on any contour with Re M > 0, because
     Re Σ(k^μ)² = Re qᵀM⁻¹q > 0.
   - So that value is not a datum of the regulated integral at real timelike k. This is exactly the
     "different object" the task asked about.

**Fork outcome (bounded).** The obstruction is lifted only for fixed γ > 0, the case the manuscript leaves open
("nothing is stated"). There the −C_0 Euclidean contour A_0 = e^{iπ/8}X_0, A_i = e^{−3πi/8}X_i is admissible
when γ/2g² > ε. Whether it is joined to the Hermitian contour is open; diagonal paths are excluded, as shown in
Step 6.

**What this does not do.** No signature is derived: the inertia found is that of the η put into S_b. Problem E
stays OPEN, CRITICAL PATH for the matrix-derived label, PROGRAMME-CONDITIONAL. Classification: M2 bounded no-go,
which closes avenue 1 of 055 within linear contours, plus exact sub-lemmas.

## Target and status

- **Problem E**, appH `sec:status-E` (L1482–1553 in the working file), read in full: the ledger label, the
  053, 054 and 055 blocks, and the Status paragraph.
  - Ledger label, verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion:
    PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or
    matrix-derived Lorentzian signature."
  - Status paragraph: "Remains Assumption~\ref{ass:lorentzian}."
- **Chapter 17** (ch17 L394–399): "OPEN; CRITICAL PATH for the matrix-derived label."
  - The criterion at L718–719: "Problem~E: Lorentzian signature is derived rather than retained
    (Assumption~\ref{ass:lorentzian})."
  - The two sources agree, so there is no discrepancy to flag.
- **Original target:** derive Lorentzian signature rather than retain `ass:lorentzian` (ch04 L321–328).
- **Current critical-path set** (ch17 criterion and appH): A, B, C, D1, E, F, G-derived, N.
- **Dependencies used:**
  - 053 block: Definition (A); the R_u; the N = 2 identity Pf = c_P(det 𝒢)⁴; the Cauchy–Binet bound and the
    flat-direction bound; the polynomial limit display; regulator independence for every positive definite M;
    the γ statements.
  - 054 block: F_E.
  - 055 block:
    - the damping set 𝔆 and its normal form;
    - (ii): inertia counts and the classes;
    - (iii): the sector;
    - (iv): W holomorphic, W(·,0) ≠ 0 on C_0, the identity-theorem argument;
    - (v): the spacelike limit.
- **Classification:** PROGRAMME-CONDITIONAL sharpening and an M2 bounded no-go. No label change.

### Why this target

- Avenue 1 was named the sharpest by the 055 gatekeeper. It is also decisive: a positive answer would have
  produced the first identification of the real-timelike limit; a negative answer closes the linear-contour line
  completely.
- It proved tractable in full, because the obstruction turned out to be algebraic (item 1).
- Avenues 2 (thimbles) and 3 (direct oscillatory analysis at real timelike k) are harder. With linear contours
  now fully closed, they are the residual routes. They are ranked below.

## Source reading

**Digest + targeted reads. Not a full scan.**

- `make_digest.py --check` printed DIGEST CURRENT. The digest header shows `dirty-chapters: yes`.
  - `git diff --stat HEAD` shows only appH, with 22 insertions. The diff consists exactly of the 055 insert
    (the uncommitted integration), and I read that insert in full.
  - So the dirty state is fully accounted for, and CLAUDE.md 3(d) does not require a full scan for a content
    change that has been read. I record this for the gatekeeper.
- Working appH: 550508 bytes, sha256 01a3bf55…7a9, CRLF 3242, bare LF 0. This is the stated baseline.
- Read in full:
  - appH L1482–1553 (Problem E: label, the 053/054/055 paragraphs, Status);
  - ch17 L390–402 and L708–728;
  - ch04 L314–336 (`ass:lorentzian`, defined once at L322);
  - proposals/055-index-mixing-contours/review-r2.md and proposal-r2.md;
  - the 053/054/055 entries at the tail of reports/ledger.md;
  - 055's lemma_checks.py, mc_check.py and apply_check.py.
- Searched:
  - `\mathfrak C` (055 only, the notation reused here);
  - `\gamma'`, which does not occur in appH, so it is a new local symbol;
  - `\mathbb 1`, already used in appH.
- No definition, assumption, scope or status passage changes, so no full scan is due under CLAUDE.md 3(c).
  Integration ordinal would be 54; the 5th-item full scan is due at 55.
- Unreadable files: none.

## Research and reasoning

**Conventions.**
- η = diag(−1, 1, …, 1).
- Λ ∈ GL(10, C); A_μ = Σ_ν Λ_{μν} X_ν with X traceless Hermitian; h = ΛᵀηΛ; M = ΛᵀPΛ, where P is the regulator
  matrix (P = 1 in Definition (A)).
- G_{αβ} = Tr X_αX_β is a real positive semidefinite Gram matrix; every rank-one psd matrix occurs, taking
  X_α = a_α T.
- The regulator exponent on the contour is −ε tr(M G). So |regulator factor| ≤ 1 on the whole contour iff
  Re M ≥ 0, since tr(Re M · G) ≥ 0 for every psd G iff Re M ≥ 0.

### Step 1. Inertia lemma (exact; every N)

The identities:
- ΛᵀηΛ = ΛᵀΛ − 2Λᵀe_0e_0ᵀΛ = M − 2ℓℓᵀ, with ℓ = Λᵀe_0 = a + ib.
- Re(ℓℓᵀ) = aaᵀ − bbᵀ, so **Re h = Re M − 2aaᵀ + 2bbᵀ**.
- For v = Λ⁻¹e_0: hv = Λᵀηe_0 = −Λᵀe_0 = −Mv.
- Re h and Im h are real symmetric, so for complex v, v̄ᵀ(Re h)v = Re(v̄ᵀhv) = −Re(v̄ᵀMv) = −v̄ᵀ(Re M)v.

The consequences:
- **(a) If Re M ≥ 0.** Re h ≥ Re M − 2aaᵀ, and n_−(Re M − 2aaᵀ) ≤ 1, so n_−(Re h) ≤ 1 by Weyl monotonicity.
  Also v̄ᵀ(Re h)v ≤ 0 with v ≠ 0, so Re h is not positive definite.
- **(b) If Re M > 0.** Interlacing gives λ_2(Re h) ≥ λ_2(Re M − 2aaᵀ) ≥ λ_1(Re M) > 0, so there are 9 positive
  eigenvalues. Also v̄ᵀ(Re h)v < 0, so there is 1 negative. The inertia is (9, 1, 0).
- **(c) Classes.** By 055 (ii), on −C_0 Re h has ≥ 9 negative eigenvalues, and by continuity ≥ 9 non-positive
  ones on cl(−C_0).
  - (a) excludes −C_0.
  - (b) excludes cl(−C_0), since 9 + 9 > 10.
  - Re h is never positive definite, so every Euclidean contour e^{iπ/4}TᵀT is excluded. This generalises 053's
    R_1 statement.

**Isotropic regulators.** Take a real basis with QᵀPQ = 1 and QᵀηQ = E = diag(−μ_0, μ_1, …, μ_9), and set
Λ = QΛ'.
- If μ_1 = … = μ_9 = μ, then h = μM − (μ+μ_0)ℓ'ℓ'ᵀ, and Λ'⁻¹e_0 satisfies hv = −μ_0Mv. The same proof applies.
- P⁻¹η ∼ E, so the condition is that P⁻¹η has a nine-fold eigenvalue.
- P = cLᵀL with L ∈ O(9,1) qualifies, since P⁻¹η = c⁻¹L⁻¹ηL.

**Mass term.** iS_γ = −iγ'Σ η_{μν}Tr A_μA_ν with γ' = γ/2g², so the quadratic exponent is
−Σ(εδ + iγ'η)_{μν}Tr A_μA_ν.
- On the contour, M_γ = εΛᵀΛ + iγ'h, so (ε+iγ')h = εh + iγ'h = ε(ΛᵀΛ − 2ℓℓᵀ) + iγ'h = M_γ − 2εℓℓᵀ.
- If Re M_γ ≥ 0, then Re((ε+iγ')h) ≥ Re M_γ − 2εaaᵀ, so n_− ≤ 1.
- For γ ≤ 0 and ε ≥ 0 (not both zero), φ = arg(ε+iγ') ∈ [−π/2, 0].
- On −C_0, h = −Tᵀdiag(|d|e^{iβ})T with β ∈ K_0, so Re(e^{iφ}h) = −Tᵀdiag(|d|cos(β+φ))T.
- At least 8 of the β lie in (0, π/2) (055 (ii)). For those, β + φ ∈ (−π/2, π/2), so n_− ≥ 8.
- This contradicts n_− ≤ 1. So −C_0 is excluded for every γ ≤ 0, including ε = 0 with γ < 0.
  - Consistency check: at ε = 0, γ < 0 the condition is Im h ≥ 0, which R_1 satisfies, so the 053 statement
    that the contour reaches u = 1 for fixed γ < 0 is reproduced.
  - Re h positive definite is allowed in that case, so the "never Euclidean" clause is not claimed for γ ≠ 0.

**γ > 0 counterexample.** Take Λ = diag(e^{iπ/8}, e^{−3πi/8} × 9). Then h = diag(−e^{iπ/4}, e^{−3πi/4}) = −e^{iπ/4}·1
∈ −C_0, and h_μh_ν = i, so iS_b = −S_E.
- M_γ,00 = (ε − iγ')e^{iπ/4}, with Re = (ε + γ')/√2.
- M_γ,ii = (ε + iγ')e^{−3πi/4}, with Re = (γ' − ε)/√2.
- So the contour is admissible iff γ' > ε.

Here the pencil eigenvalues of (η, εI + iγ'η) are complex, and Step 1's sign argument is unavailable.

### Step 2. Necessity of Re M ≥ 0 at N = 2

Suppose Re aᵀMa ≤ −2c < 0. Choose:
- an open cone U ∋ a with Re a'ᵀMa' ≤ −c|a'|², and |a'| = 1;
- the colour columns x¹ = Ra', x² = z_2/R, x³ = z_3/R, with z_{2,3} in the unit ball B of R¹⁰.

Then:
- **Determinant.** X = Z·diag(R, 1/R, 1/R) with Z = (a', z_2, z_3), so 𝒢 = XᵀhX and
  det 𝒢 = R²·R⁻⁴·det(ZᵀhZ) = R⁻² det(ZᵀhZ). The script checks this identity to 1e−12.
- **Action.** σ_2(𝒢) = R²s²[⋯] + s⁴[⋯] with s = 1/R, which is bounded. So |e^{iS_b}| ≥ e^{−C}.
- **Regulator.** Σ_μ Tr A_μ² = ½ Σ_a x^{aT}Mx^a has no colour cross terms. Its real part is ≤ −(c/2)R² + C', so
  the regulator factor is ≥ e^{εcR²/2 − εC'}.
- **Polynomial.** det(ZᵀhZ) is a polynomial in (a', z_2, z_3). It is not identically zero, since at a complex Z
  with ZᵀhZ = 1 (h invertible complex symmetric) it equals 1. So |det(ZᵀhZ)| ≥ δ > 0 on a subset of U×B×B of
  positive measure.
- **Measure.** R⁹dR dΩ for x¹ and R⁻¹⁰ for each of x², x³.
- **Total.** ∫ R^{9−20}·R^{−8}·e^{εcR²/2} dR = ∫ R^{−19}e^{εcR²/2} dR = ∞.

So at N = 2, absolute convergence of I_ε[1] on a linear contour forces Re M ≥ 0. The same argument applies with
any quadratic exponent matrix (P or M_γ).

**Consequence (N = 2).**
- A damped contour (h ∈ C) on which I_ε converges absolutely has h ∈ C_0 by Step 1.
- Its bounded modes have k·k in the 055 sector, so real causal k ≠ 0 is unreachable.
- No path hypothesis is needed. Avenue 1's path class (Re iS_b ≤ 0, leaving cl(C)) is a special case: no such
  path ends on a contour with h ∈ −C_0 on which the regulated integrand is absolutely integrable.

**N ≥ 3.** Step 1 still applies to contours with Re M ≥ 0, the domination class of the Stokes arguments.
Non-integrability outside that class needs a lower bound on |Pf| near commuting configurations, which is not
given. The insert says so.

### Step 3. Second moments and the sign argument (N = 2; any positive definite P)

Define R(h)_{αβ} = ⟨Tr X_αX_β⟩_h for h ∈ C at ε = 0. It is the ratio of ∫(det𝒢)⁴e^{iS_b}Tr X_αX_β to
∫(det𝒢)⁴e^{iS_b}.
- **Holomorphy.** By domination (055 Step 0; degree 2 < 14), numerator and denominator are holomorphic on C. The
  denominator is ≠ 0 on C_0, by 055 (iv) (W(h,0) = c|det T|⁻³∏d^{−3/2}, c ≠ 0).
- **Covariance.** For real T, substituting Y = TX gives R(TᵀhT) = T⁻¹R(h)T⁻ᵀ.
- **Euclidean point.** At h = e^{iπ/4}1 the weight is a constant phase times (det XᵀX)⁴e^{−S_E}, the
  first-paragraph Euclidean weight at N = 2. So R = c_E·1, with c_E = ⟨Tr Ã_0²⟩_E > 0 because the weight is
  positive.
- **Real congruence orbit.** R(e^{iπ/4}TᵀT) = c_E(TᵀT)⁻¹ = c_E e^{iπ/4}(e^{iπ/4}TᵀT)⁻¹.
- **Identity theorem.** e^{iπ/4}·Pos(10) is open in the maximal totally real subspace e^{iπ/4}Sym(10, R).
  C_0 is open and connected, being the image of GL⁺(10,R) × D_0 with D_0 contractible. So
  **R(h) = c_E e^{iπ/4}h⁻¹ on C_0.**
- **Contour values.** On a contour Λ: ⟨Tr A_μA_ν⟩ = (ΛR(h)Λᵀ)_{μν}.
  - On C_0 this is c_E e^{iπ/4}(Λh⁻¹Λᵀ) = c_E e^{iπ/4}η.
  - It matches the 053 limit: ⟨Tr A_0²⟩ → e^{−3πi/4}c_E = c_E e^{iπ/4}η_00, ⟨Σ_i Tr A_i²⟩ → 9c_E e^{iπ/4}, and the
    off-diagonal entries are 0.
  - The integrand is even in h, so R(−h) = R(h). On −C_0: ΛR(h)Λᵀ = c_E e^{iπ/4}Λ(−h)⁻¹Λᵀ = −c_E e^{iπ/4}η.

**Path argument.** Take Λ(τ) piecewise C¹ with:
- Λ(0) real;
- h(τ) ∈ D = {Im[h(a,a)h(b,b) − h(a,b)²] ≥ 0}, which at N = 2 is equivalent to Re iS_b ≤ 0 on the contour;
- Re Λ(τ)ᵀPΛ(τ) > 0;
- h(1) ∈ C.

Then:
- At fixed ε, the swept integrand is bounded by poly·e^{−εc|X|²}, so Stokes moves I_ε[O] for O = 1 and
  O = Tr A_μA_ν to Λ(1).
- On Λ(1) there is domination by C(1+|X|²)(det XᵀX)⁴e^{−cS_E}, and the regulator modulus is ≤ 1. So
  lim ⟨Tr A_μA_ν⟩_ε = (value on Λ(1)).
- The paragraph on the regulated Lorentzian integral (053) gives the limit as c_E e^{iπ/4}η for every positive
  definite P.
- If h(1) ∈ −C_0, then c_E e^{iπ/4}η = −c_E e^{iπ/4}η, which is impossible since c_E ≠ 0. So h(1) ∈ C_0. ∎

**Anisotropic P.**
- The exact example, P = diag(1,1,¼,1,…), gives Re ΛᵀPΛ = diag(9/25, 1, …) and Re h = diag(−39/25, 4, −1, 1, …),
  so Step 1 fails as an inertia statement.
- Whether some anisotropic P admits a contour in −C_0 is not proved either way. Numerical searches in
  dimensions 3, 4 and 10 (aniso_search) found none: the suprema of λ_min(Re M)/|M| over −C_0 lie between
  −1.6e−7 and −1.3e−4, approaching 0 from below for isotropic and anisotropic weights alike. I record this as
  a conjecture only; it is not in the insert.

### Step 4. What −C_0 contours compute (exact; every N)

- **Substitution.** On −C_0, Λ = iΛ' with h(Λ') = −h ∈ C_0. S_b has degree 4 and Pf M has degree 8(N²−1), so
  both are invariant under A → iA; the Jacobian is constant. At ε = 0, therefore,
  ⟨O⟩_Λ = ⟨O(i·)⟩_{Λ'} wherever both converge absolutely.
- **Fourier mode.** O = Tr e^{ik·A} gives Tr e^{i(ik)·A}, the mode at imaginary momentum ik on a C_0 contour.
  For real timelike k = κe_0 the value is F_E(e^{iπ/4}(ik)·(ik)) = F_E(e^{iπ/4}κ²). This is the same number as
  055 (v) at real spacelike k·k = κ².
- **Imaginary momenta are not reachable either.**
  - Re M > 0 implies Re M⁻¹ > 0: with v = Mu, Re v̄ᵀM⁻¹v = Re ūᵀM̄u = ūᵀ(Re M)u.
  - A bounded mode requires q = Λᵀk real (055 (iii)), and then Σ_μ(k^μ)² = qᵀM⁻¹q has positive real part.
  - At k = iκe_0, Σ(k^μ)² = −κ² < 0. So no Definition (A)-admissible linear contour has a bounded mode there.
  - Equivalently, row 0 imaginary gives Re h = Re M + 2bbᵀ > 0, which contradicts Step 1.

### Step 5. Fork analysis: hypotheses of the new obstruction and relaxations

| # | Hypothesis | Relaxation explored | Outcome |
|---|---|---|---|
| H1 | Linear contour, Λ ⊗ 1_colour | Paths leaving cl(C) with Re iS_b ≤ 0 (avenue 1) | Closed: Steps 1–3 |
| H1' | same | ε-dependent linear contours Λ_ε | Closed for P = 1. Inertia holds at every ε; limits have n_−(Re h) ≤ 1, disjoint from the open −C_0 |
| H1'' | same | Colour-mixing linear maps L ∈ GL(30,C) | Open. The algebra generalises: Re Lᵀ(η⊗1_3)L has inertia (27,3) when Re LᵀL > 0, by the same rank argument with three time rows. But the damping/bounded-mode analysis for colour-mixing contours is not done |
| H1''' | same | Non-linear contours (thimbles) | Open (055 avenue 2). Constraint found: any valid representation must reproduce ⟨Tr A_μA_ν⟩ → c_E e^{iπ/4}η, a check that rules out −C_0-type end pieces |
| H2 | Quadratic regulator, P = 1 or isotropic | Anisotropic P | Paths closed at N = 2 (Step 3); pointwise exclusion conjectural (numerics) |
| H2' | same | Mass γ ≤ 0 | Closed (Step 1) |
| H2'' | same | **Mass γ > 0** | **Obstruction lifted**: −C_0 Euclidean contour admissible for γ' > ε. Connection to the Hermitian contour open |
| H3 | Absolute convergence (Stokes class) | Conditionally convergent representations | Open. Equivalent in difficulty to the direct oscillatory analysis (055 avenue 3) |
| H4 | ε → 0 at fixed N | N → ∞ first | Step 1 is N-independent at fixed ε, so the class of linear contours carrying I_ε is the same at every N. The limit identification is open |
| H5 | N = 2 for Steps 2–3 | N ≥ 3 | Step 1 holds; necessity and the sign argument need the N ≥ 3 versions of 053's bound and of 055 (iv) |

### Step 6. The γ > 0 opening, a first probe (not in the insert)

Take diagonal paths Λ = diag(e^{iφ_μ}), with h = diag(−e^{2iφ_0}, e^{2iφ_i}).
- D requires sin(2φ_i + 2φ_j) ≥ 0 for spatial pairs. Lift ψ_i = 2φ_i continuously from 0. Each pair sum
  ψ_i + ψ_j is continuous and cannot leave [0, π], since it cannot jump to another interval [2kπ, (2k+1)π].
- The −C_0 target needs ψ_i + ψ_j ≡ π/2 (mod 2π) with ψ_i ≡ 5π/4. Inside [0, π] the sums must equal π/2, so
  ψ_i = π/4 for all i (n ≥ 3), which is ≢ 5π/4.
- So no diagonal path in D reaches the γ > 0 admissible contour above, whatever γ.
- Non-diagonal paths are not analysed. Whether D ∩ GL(10) has the Hermitian contour and −C_0 in different
  components (a regulator-free version of the obstruction) is open. If it does, the γ > 0 opening also closes
  for linear contours.

**Ranked open avenues:**
1. γ > 0: components of D ∩ GL containing η and −C_0. This decides whether the γ > 0 Lorentzian integral can
   be the −C_0 Euclidean model with mass e^{3πi/4}. That would be relevant to the inequivalence for γ > 0
   stated in Anagnostopoulos2026 (as recorded in appH; not re-verified here).
2. Non-linear (thimble) contours at real causal k, N = 2.
3. Direct oscillatory analysis of the real timelike/null limit, N = 2.
4. Colour-mixing linear contours.
5. Pointwise exclusion of −C_0 for anisotropic P (conjecture).
6. N ≥ 3 versions of Steps 2–3.
7. N → ∞ first; Definitions (B), (C); OS positivity.

None of these derives signature while η is an input.

### Literature

- No new citations.
- The lemma uses only Weyl's monotonicity and interlacing for Hermitian matrices, which are standard and are
  not cited in the insert.
- The γ remark refers only to manuscript statements already present: 053's "for fixed γ > 0 … nothing is stated".
  I re-read that statement in the appH working file.
- The Anagnostopoulos2026 claim (failure of equivalence for γ > 0) is quoted from the appH text, not from the
  paper. It is not independently verified in this round, and it is not used in the insert.

## Claim classification

| Claim | Class |
|---|---|
| Re h = Re M − 2aaᵀ + 2bbᵀ; hv = −Mv | established (identity) |
| Re M ≥ 0 ⇒ n_−(Re h) ≤ 1 and Re h not positive definite; Re M > 0 ⇒ inertia (9,1) | established (every N) |
| −C_0 ∩ {Re M ≥ 0} = ∅; cl(−C_0) ∩ {Re M > 0} = ∅; Euclidean contours excluded | established (every N, P = 1 or isotropic) |
| Mass γ ≤ 0: −C_0 excluded | established (every N) |
| Mass γ > 0: explicit admissible −C_0 contour for γ' > ε | established (exact) |
| Necessity of Re M ≥ 0 for absolute convergence | established at N = 2; unresolved at N ≥ 3 |
| Damped absolutely convergent linear contours lie in C_0; real causal k unreachable | established at N = 2; at N ≥ 3 for Re M ≥ 0 |
| R(h) = c_E e^{iπ/4}h⁻¹ on C_0; sign flip on −C_0 | established at N = 2 (MC check moments_check) |
| No admissible path to −C_0 for any positive definite P | established at N = 2 |
| Anisotropic P: Re h can have 2 negative eigenvalues | established (exact example) |
| Anisotropic P: −C_0 never admissible | conjecture (numerics only; not in insert) |
| −C_0 integrals = C_0 integrals of O(i·); imaginary-momentum reading | established (every N, where convergent) |
| Imaginary timelike momenta unreachable when Re M > 0 | established |
| Diagonal-path exclusion for γ > 0 | established (proposal only) |
| Connectivity of D ∩ GL; γ > 0 limit | unresolved |
| Any signature derivation | not claimed |

## Proposed changes

### chapters/appH-microscopic-proofs.tex

**Placement.**
- Insert the new paragraph `appH_insert.tex` immediately before the unique anchor (61 bytes, count 1, at
  L1551):

      \paragraph{Status.}
      Remains Assumption~\ref{ass:lorentzian}.

- Follow the insert with one blank line. This places it after the 055 paragraph, which ends "…so no signature
  is derived and Assumption~\ref{ass:lorentzian} is not discharged."
- Nothing is replaced or removed.

**Anchor and insert data** (from `apply_check.py` in report mode; apply_check.txt).
- Baseline: 550508 bytes, sha256 01a3bf55a888ea30f4f3182358877b4ba6db5ac6237f2b7fff7e06093277d7a9, CRLF 3242,
  bare LF 0.
- Anchor: 61 bytes, sha256 a7c774127bc78a19a76b5ab005d0e4e59a3b56b66a3be64b71e38cd13ade26cc, count 1, line 1551.
- Insert, LF form (proposal file): 10944 bytes, sha256
  7de1216ae107ead895254a3278ac3d96e409fd1de8d8be3693c4890543146c79 (r1: 10602 bytes, b58cda7e…056c, kept as
  appH_insert.r1.tex).
- Insert, CRLF form: 10956 bytes, sha256 48a977c23c503e55c41ae2cc51189aa9d3ae084d325c5ce14b2dd509f816463b.
- Resulting appH: 561466 bytes, sha256 ea5c753b0f01a3a92e426435f747fa464521980f609ab330f4a432868daba1f5, CRLF
  3255, bare LF 0.

**Form.**
- ASCII, LF only, no trailing whitespace.
- The only reference is `\ref{ass:lorentzian}`, which is defined once (ch04 L322).
- There are no labels, no citations and no process language.
- Local symbols: `M`, `\ell`, `\gamma'`, `P`, `c_{\mathrm E}`. The symbols `\mathfrak C`, `\mathfrak C_0`, `h`,
  `\Lambda`, `\mathcal G`, `S_{\mathrm E}`, `F_{\mathrm E}` and `\beta_\mu` come from the 053–055 paragraphs.
  `c_{\mathrm E}` is defined in the text as ⟨Tr Ã_0²⟩_E, the notation of the paragraph on the regulated Lorentzian integral.

**Stale passages elsewhere.**
- The 055 closing caveat "about paths along which Re iS_b ≤ 0 but h leaves the closure of 𝔆" stays a correct
  description of that paragraph's scope. The new paragraph, which follows directly, settles it, so no edit is
  needed.
- The 053 sentence "At fixed ε the contour therefore does not reach the Euclidean model" stays correct, and (i)
  generalises it.
- No other file is affected.

The full block is in `appH_insert.tex`, which is reproduced verbatim in the Appendix.

## Verification scripts

All are in `proposals/056-regulator-inertia/`, with outputs in `.txt`.

**`inertia_checks.py` → `inertia_checks.txt`** (numerical; about 5 min).
- **A.**
  - 2355 random admissible Λ, of the form S·D·R0·(1+tZ) with complex Lorentz S, phases |φ| < π/4 and complex
    Z: inertia (9,1,0) always, the identity Re h = Re M − 2aaᵀ + 2bbᵀ holds, λ_2(Re h) ≥ λ_1(Re M) (min
    margin +4.5e−14), and λ_1(Re h) ≤ −v̄ᵀRe M v/|v|².
  - Adversarial optimisation (12 starts): margin ≥ 0 (3.8e−19).
- **B.** The 055 example has Re M eigenvalues {−0.5, 1}, class −C_0.
- **C.** 464 samples with boosted/time-rescaled P: inertia (9,1,0).
- **D.**
  - The 3×3 and 10×10 anisotropic examples: Re M min 0.36; Re h inertia (8,2,0).
  - Searches for −C_0 with Re M > 0 (isotropic and two anisotropic weight sets, n = 10): best values negative.
- **G.**
  - Mass γ ≤ 0: the identity (ε+iγ')h = M_γ − 2εℓℓᵀ holds, and Re((ε+iγ')h) has ≤ 1 negative eigenvalue in
    51/51 admissible samples.
  - 300 random h ∈ −C_0 × 7 values of φ ∈ [−π/2, 0]: ≥ 9 negative eigenvalues of Re(e^{iφ}h). The claim is ≥ 8.
  - The γ > 0 example: h = −e^{iπ/4}1, class −C_0, h_μh_ν = i; min eig Re M_γ = +0.0707 at (ε, γ') = (0.1, 0.2),
    −0.0354 at (0.1, 0.05), +0.2121 at (0, 0.3).
- **E.**
  - 2384 admissible samples: Re(kᵀk) > 0 for real q.
  - Imaginary row 0: Re h = Re M + 2bbᵀ exactly, and the optimised λ_min(Re M) stays ≤ 0 (−1.2e−9).
- **F.** The N = 2 scaling det𝒢 = R²s⁴det(ZᵀhZ) holds to 1e−12, and σ_2 is bounded at s = 1/R.

**`aniso_search.py` → `aniso_search.txt`.**
- Maximises λ_min(Re ΛᵀΛ)/|M| over Λ with ΛᵀEΛ = −diag(e^{iβ}) ∈ −C_0. h is diagonal WLOG, Λ = SΛ_0 with S
  complex E-orthogonal, and β is parametrised in the part of K_0 with at most one β outside (0, π/2).
- Runs: n = 3, 4 (30 restarts) and n = 10 (4 restarts), five weight patterns each.
- All suprema found are negative, between −1.6e−7 and −1.3e−4. They approach 0 from below, for the isotropic
  controls (where the lemma proves ≤ 0) and for the anisotropic patterns alike.
- The n = 10 pattern with weights up to 30⁸ overflowed in every restart and gives no data.
- This is a numerical search, not a proof. It supports the conjecture only.

**`exact_examples.py` → `exact_examples.txt`** (sympy, exact).
- The identities h = M − 2ℓℓᵀ, Re h = Re M − 2aaᵀ + 2bbᵀ and h Λ⁻¹e_0 = −M Λ⁻¹e_0, for a generic symbolic Λ.
- The mass identity (ε+iγ')h = M_γ − 2εℓℓᵀ.
- The 10D anisotropic example: Re ΛᵀPΛ = diag(9/25, 1, …) and Re h = diag(−39/25, 4, −1, 1, …), with
  off-diagonal real parts 0.
- The γ > 0 example: h = −e^{iπ/4}1, Re M_γ entries √2(ε+γ')/2 and √2(γ'−ε)/2, and h_μh_ν = i.
- i^{8(N²−1)} = 1.

**`moments_check.py` → `moments_check.txt`.** Importance-sampled MC at N = 2 (6e5 samples, 055 sampler).
- Euclidean point: c_E = 0.36099; off-diagonal |R| ≤ 8e−4.
- Contours: two diagonal contours with distinct phases (π/4 ± 0.25, ± 0.4), and OᵀDO.
  - |R − c_E e^{iπ/4}h⁻¹|/|pred| = 0.0039, 0.0068 and 0.0073.
  - The opposite sign would give 2.000.
  - Entrywise deviations: median 0.9–1.0σ, max 2.8–3.8σ over 100 entries. The σ do not include the
    uncertainty of c_E, and all rows share one sample set.
- This is a check, not a proof.

**`apply_check.py` → `apply_check.txt`.**
- Checks the baseline, anchor uniqueness, insert form and hashes.
- With a path outside the repository, it writes the would-be appH there.

**Scratch build.**
- Two pdflatex passes (`-interaction=nonstopmode -halt-on-error`) on a copy of namcg-book7.tex, chapters/,
  frontmatter/, bib/, figs/, the .bbl and the root images, in the session scratchpad (`build056`), with the
  patched appH written by apply_check.
- Both passes exit 0: 363 pages (361 after 055), 0 undefined references or citations, 0 multiply defined
  labels.
- The scratch copy is left in place in the scratchpad; no removal was attempted.

## Decisions Taken

1. **Target: avenue 1.** It was ranked sharpest by 055-r2. It is decisive either way, and it proved tractable
   in closed form.
   - Rejected: avenues 2 and 3 first. They are harder, and their value depends on avenue 1's answer: if linear
     contours had reached real timelike k, thimbles would have been unnecessary.
2. **Lead with the pointwise lemma, not only the path statement.** For Definition (A) the lemma is stronger
   (no path hypothesis, every N) and simpler.
   - The sign argument is kept because it covers anisotropic P, where the lemma fails as an inertia statement.
3. **Include the γ > 0 counterexample in the insert.** It bounds the hypothesis class honestly: the obstruction
   is not robust to γ > 0. This is where the manuscript already says nothing is stated.
   - The diagonal-path probe stays in the proposal, because it is partial.
4. **Exclude the anisotropic −C_0 conjecture from the insert,** apart from "not decided here". The evidence is
   numerical only.
5. **Present the −C_0 values as observables at imaginary momenta.** This addresses the task's warning about
   different objects, using an exact identity rather than an interpretation.
6. **No edit to the 055 caveat.** It remains a correct scope statement of that paragraph.

## Milestone assessment

**M2: a new bounded no-go.** It closes the route "reach −C_0 (hence real timelike k) by regulator-admissible
deformation of linear contours outside cl(C)". The 055 paragraph explicitly left that route open.
- Exact sub-lemmas are included: the regulator inertia lemma, the N = 2 necessity, and the second-moment sign.
- It also identifies a precise opening, fixed γ > 0.
- It is not M1/BREAKTHROUGH: no step of a signature derivation is made, and η is an input.
- It is not M3 (no merged claim is wrong), M4 or M5.

## Status-label recommendation

- Current critical-path set (ch17 criterion and appH): A, B, C, D1, E, F, G-derived, N.
- Affected label: Problem E only. It stays OPEN; CRITICAL PATH for the matrix-derived label;
  PROGRAMME-CONDITIONAL.
- No change is proposed.

## Author decision needed

None.

For the author's information, the lemma adds to 053 ledger note (a). On every linear contour that carries the
regulated integral, Re h has exactly η's inertia. The Euclidean regulator transports the Lorentzian inertia of the
η put in by hand; it does not create it.

## Remaining open step

To close Problem E, Lorentzian signature must be derived from the matrix theory rather than retained. Within
this line:
- (a) fixed γ > 0: connectivity of D ∩ GL between η and −C_0 (non-diagonal paths), and the ε → 0 limit there;
- (b) thimbles or direct oscillatory analysis at real causal k, N = 2;
- (c) colour-mixing linear contours;
- (d) N ≥ 3 versions of Steps 2–3;
- (e) N → ∞ first; Definitions (B) and (C).

Even a full answer concerns an η put in by hand. A signature derivation needs a mechanism that selects η, which
this line does not supply.

## Special instructions for the gatekeeper

**Re-derive:**
- Step 1: the identity Re h = Re M − 2aaᵀ + 2bbᵀ; hv = −Mv; the interlacing; the class exclusion using 055 (ii).
- The isotropic-P reduction.
- The mass identity (ε+iγ')h = M_γ − 2εℓℓᵀ, and "≥ 8 of the β in (0, π/2)" from 055 (ii).
- The γ > 0 example: Re M_γ entries (ε+γ')/√2 and (γ'−ε)/√2.
- Step 2: the scaling, the boundedness of σ_2, the measure exponent −19, and the nonvanishing polynomial.
- Step 3:
  - the covariance;
  - the Euclidean-point value c_E;
  - the identity theorem on C_0;
  - the sign flip under h → −h;
  - the match with the 053 limit;
  - the Stokes/DC hypotheses of the path argument.
- Step 4: the degree count 8(N²−1); Re M⁻¹ > 0.
- The exact 10D anisotropic example: 9/25 and −39/25.

**Must not be asserted:**
- any signature derivation;
- pointwise exclusion of −C_0 for anisotropic P;
- anything about γ > 0 beyond the admissibility example;
- non-linear contours;
- N ≥ 3 necessity.

**Check:**
- the "(algebraic at every N, proved at N = 2)" heading matches the content: (i) is algebraic for every N, and
  (ii)–(iii) are at N = 2;
- the closing paragraph's caveat list matches the claim table.

## Appendix: insert and build

**Build:** scratch copy, two pdflatex passes, exit 0. 363 pages, 0 undefined references, 0 multiply defined
labels (r2 build; r1 build also 363 pages, 0/0). The patched appH there has sha256 ea5c753b…a1f5, identical to
the apply_check result.

**Insert** (`appH_insert.tex`, verbatim):

```latex
\paragraph{The regulator fixes the class of linear contours (algebraic at every \(N\), proved at \(N=2\)).}
Keep the setting and notation of the preceding paragraph. On the contour \(A_\mu=\sum_\nu\Lambda_{\mu\nu}X_\nu\) the regulator of Definition~(A) is \(\epsilon\sum_{\alpha,\beta}M_{\alpha\beta}\operatorname{Tr}X_\alpha X_\beta\) with \(M=\Lambda^{\mathrm T}\Lambda\). The matrix \((\operatorname{Tr}X_\alpha X_\beta)\) is a real Gram matrix, and every real positive semidefinite matrix of rank one occurs, so the regulator factor has modulus at most \(1\) on the whole contour exactly when \(\operatorname{Re}M\) is positive semidefinite.

(i) \emph{Inertia.} Let \(\ell=a+\mathrm ib\), with \(a,b\) real, be the row \(\mu=0\) of \(\Lambda\). Then \(h=M-2\ell\ell^{\mathrm T}\), so \(\operatorname{Re}h=\operatorname{Re}M-2aa^{\mathrm T}+2bb^{\mathrm T}\), and \(v=\Lambda^{-1}e_0\) satisfies \(hv=-Mv\), so \(\bar v^{\mathrm T}(\operatorname{Re}h)v=-\bar v^{\mathrm T}(\operatorname{Re}M)v\). If \(\operatorname{Re}M\) is positive semidefinite, \(\operatorname{Re}h\) therefore has at most one negative eigenvalue and is not positive definite. If \(\operatorname{Re}M\) is positive definite, \(\operatorname{Re}h\) has exactly one negative and nine positive eigenvalues, the inertia of \(\eta\). By (ii) of the preceding paragraph, \(\operatorname{Re}h\) has at least nine negative eigenvalues on \(-\mathfrak C_0\), and so at least nine non-positive ones on its closure. Hence \(h\notin-\mathfrak C_0\) in the first case, and \(h\) is not in the closure of \(-\mathfrak C_0\) in the second. In particular \(\operatorname{Re}h\) is never positive definite, whereas the Euclidean contours \(h=\mathrm e^{\mathrm i\pi/4}T^{\mathrm T}T\), \(T\) real, have \(\operatorname{Re}h\) positive definite. These statements are algebraic and hold for every \(N\). The same proof, in a real basis in which \(P\) is the identity and \(\eta\) is diagonal, gives them for the regulator \(\epsilon\sum_{\mu,\nu}P_{\mu\nu}\operatorname{Tr}A_\mu A_\nu\), with \(M=\Lambda^{\mathrm T}P\Lambda\), whenever \(P\) is positive definite and \(P^{-1}\eta\) has a nine-fold eigenvalue, for example \(P=c\,L^{\mathrm T}L\) with \(c>0\) and \(L\) a real Lorentz transformation. With the mass term the quadratic part of the exponent is \(-\sum_{\mu,\nu}(\epsilon\delta_{\mu\nu}+\mathrm i\gamma'\eta_{\mu\nu})\operatorname{Tr}A_\mu A_\nu\), where \(\gamma'=\gamma/2g_{\mathrm{YM}}^2\). Write \(M_\gamma=\epsilon\Lambda^{\mathrm T}\Lambda+\mathrm i\gamma'h\) for the matrix of this form on the contour; then \((\epsilon+\mathrm i\gamma')h=M_\gamma-2\epsilon\ell\ell^{\mathrm T}\). Let \(\gamma\le0\) and \(\epsilon\ge0\), not both zero, and write \(\epsilon+\mathrm i\gamma'=|\epsilon+\mathrm i\gamma'|\mathrm e^{\mathrm i\varphi}\) with \(-\pi/2\le\varphi\le0\). Write \(h\in-\mathfrak C_0\) as \(-T^{\mathrm T}\operatorname{diag}(d_\mu)T\) with the arguments \(\beta_\mu\) of \(\mathfrak C_0\). By (ii) of the preceding paragraph at least eight of the \(\beta_\mu\) lie in \((0,\pi/2)\), so \(\operatorname{Re}(\mathrm e^{\mathrm i\varphi}h)\) has at least eight negative eigenvalues, while by the identity above it has at most one when \(\operatorname{Re}M_\gamma\) is positive semidefinite. So \(h\notin-\mathfrak C_0\) persists. For fixed \(\gamma>0\) it fails. The contour \(A_0=\mathrm e^{\mathrm i\pi/8}X_0\), \(A_i=\mathrm e^{-3\pi\mathrm i/8}X_i\) has \(h=-\mathrm e^{\mathrm i\pi/4}\mathbb 1\in-\mathfrak C_0\) and \(\operatorname{Re}\mathrm iS_{\mathrm b}=-S_{\mathrm E}\), and its quadratic exponent has negative real part whenever \(\gamma'>\epsilon\).

(ii) \emph{Necessity at \(N=2\).} At \(N=2\) the condition on \(\operatorname{Re}M\) is necessary for absolute convergence. Suppose \(\operatorname{Re}(a^{\mathrm T}Ma)<0\) for a real \(a\). Take the colour columns \(x^1=Ra'\), \(x^2=z_2/R\) and \(x^3=z_3/R\), with \(a'\) in a small cone around \(a\), \(|z_2|,|z_3|<1\) and \(R\) large. Then \(\det\mathcal G=R^{-2}\det(Z^{\mathrm T}hZ)\) with \(Z=(a',z_2,z_3)\), \(S_{\mathrm b}\) is bounded, and the regulator factor has modulus at least \(\mathrm e^{c\epsilon R^2-C}\). Since \(\det(Z^{\mathrm T}hZ)\) is a nonzero polynomial, the modulus of the integrand of \(I_\epsilon[1]\) integrates to at least a constant times \(\int^\infty R^{-19}\mathrm e^{c\epsilon R^2}\,\mathrm dR=\infty\). So at \(N=2\) every linear contour on which \(I_\epsilon[1]\) converges absolutely has \(\operatorname{Re}M\) positive semidefinite, and the same argument applies to \(\Lambda^{\mathrm T}P\Lambda\) and to \(M_\gamma\). By (i) its \(h\) is not in \(-\mathfrak C_0\), and if the contour is damped, \(h\in\mathfrak C\), then \(h\in\mathfrak C_0\). The bounded no-go of (iii) of the preceding paragraph therefore covers every damped linear contour on which the regulated integrand is absolutely integrable, whatever path leads to it. In particular, no path along which \(\operatorname{Re}\mathrm iS_{\mathrm b}\le0\) while \(h\) leaves the closure of \(\mathfrak C\) ends on a contour with \(h\in-\mathfrak C_0\) on which the regulated integrand is absolutely integrable. For \(N\ge3\) the same holds for the contours on which the regulator factor is bounded by \(1\), the class used in the Stokes arguments above. Non-integrability outside that class is not shown for \(N\ge3\).

(iii) \emph{General positive definite regulators at \(N=2\).} For a general positive definite \(P\) the inertia in (i) is not fixed. Take \(P=\operatorname{diag}(1,1,\tfrac14,1,\dots,1)\) and \(\Lambda=\operatorname{diag}(1,1,2,1,\dots,1)\Lambda'\), where \(\Lambda'\) has rows \((0,0,1)\), \((1,0,0)\) and \((4\mathrm i/5,1,0)\) in the first three indices and is the identity in the others. Then \(\operatorname{Re}\Lambda^{\mathrm T}P\Lambda=\operatorname{diag}(\tfrac9{25},1,1,\dots,1)\), while \(\operatorname{Re}h=\operatorname{diag}(-\tfrac{39}{25},4,-1,1,\dots,1)\) has two negative eigenvalues. Whether such \(P\) admit contours with \(h\in-\mathfrak C_0\) is not decided here. A statement about paths holds instead. At \(N=2\) and for \(h\in\mathfrak C_0\), let \(\langle\operatorname{Tr}X_\alpha X_\beta\rangle_h\) be the ratio of the integrals over real \(X\) of \((\det\mathcal G)^4\mathrm e^{\mathrm iS_{\mathrm b}}\operatorname{Tr}X_\alpha X_\beta\) and of \((\det\mathcal G)^4\mathrm e^{\mathrm iS_{\mathrm b}}\); the denominator does not vanish by (iv) of the preceding paragraph. This ratio equals \(c_{\mathrm E}\mathrm e^{\mathrm i\pi/4}(h^{-1})_{\alpha\beta}\), with \(c_{\mathrm E}=\langle\operatorname{Tr}\tilde A_0^2\rangle_{\mathrm E}>0\). Both sides are holomorphic on \(\mathfrak C_0\), transform alike under real congruences, and agree at \(h=\mathrm e^{\mathrm i\pi/4}\mathbb 1\). So they agree at every \(\mathrm e^{\mathrm i\pi/4}T^{\mathrm T}T\), and by the identity theorem, as in (iv) of the preceding paragraph, everywhere on \(\mathfrak C_0\). On a contour with \(h\in\mathfrak C_0\) this gives \(\langle\operatorname{Tr}A_\mu A_\nu\rangle=c_{\mathrm E}\mathrm e^{\mathrm i\pi/4}\eta_{\mu\nu}\), which is the limit of the paragraph on the regulated Lorentzian integral. The integrand is even in \(h\), so on a contour with \(h\in-\mathfrak C_0\) the same ratio gives \(-c_{\mathrm E}\mathrm e^{\mathrm i\pi/4}\eta_{\mu\nu}\). Now let \(\Lambda(\tau)\), \(0\le\tau\le1\), be piecewise continuously differentiable, with \(\Lambda(0)\) real, \(\operatorname{Re}\mathrm iS_{\mathrm b}\le0\) on every contour of the path, \(\operatorname{Re}\Lambda(\tau)^{\mathrm T}P\Lambda(\tau)\) positive definite and \(h(1)\in\mathfrak C\). Stokes' theorem at fixed \(\epsilon\), as for the \(\mathcal R_u\), and dominated convergence on the last contour give the limit of \(\langle\operatorname{Tr}A_\mu A_\nu\rangle_\epsilon\) as its value on that contour. That paragraph gives this limit as \(c_{\mathrm E}\mathrm e^{\mathrm i\pi/4}\eta_{\mu\nu}\) for every positive definite \(P\). Hence \(h(1)\in\mathfrak C_0\). For every such regulator, no path of linear contours along which \(\operatorname{Re}\mathrm iS_{\mathrm b}\le0\) and the regulator decays joins the Hermitian contour to \(-\mathfrak C_0\).

(iv) \emph{What the contours of \(-\mathfrak C_0\) compute.} For \(h\in-\mathfrak C_0\) write \(\Lambda=\mathrm i\Lambda'\), so that the contour \(\Lambda'\) has \(-h\in\mathfrak C_0\). The functions \(S_{\mathrm b}\) and \(\operatorname{Pf}\mathcal M\) are homogeneous of degrees \(4\) and \(8(N^2-1)\), so the weight at \(\epsilon=0\) is the same on both contours up to a constant factor. The expectation value of \(O\) on the contour \(\Lambda\) is therefore that of \(A\mapsto O(\mathrm iA)\) on \(\Lambda'\), for every \(N\) where these integrals converge absolutely. For \(O=\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\) this is the Fourier mode at the momentum \(\mathrm ik\) on a contour of \(\mathfrak C_0\). At \(N=2\) and real timelike \(k\), the value \(F_{\mathrm E}(\mathrm e^{\mathrm i\pi/4}\kappa^2)\) of the preceding paragraph is the number that (v) there gives as the real spacelike limit at \(k^\mu k_\mu=\kappa^2\). No contour with \(\operatorname{Re}M\) positive definite makes the mode bounded at an imaginary timelike momentum \(k^\mu=\mathrm i\kappa\delta^\mu_0\). For real \(q=\Lambda^{\mathrm T}k\) one has \(\sum_\mu(k^\mu)^2=q^{\mathrm T}M^{-1}q\), whose real part is positive because \(\operatorname{Re}M^{-1}\) is positive definite, while \(\sum_\mu(k^\mu)^2=-\kappa^2\) at that momentum. The value on \(-\mathfrak C_0\) at real timelike \(k\) is therefore not obtained in this way as a limit of the regulated integral, at real or at imaginary timelike momentum.

So, for linear contours, Definition~(A) with \(\gamma\le0\) or a regulator as in (i) with \(\gamma=0\), and \(\epsilon\to0\) taken at fixed \(N\), the damped contours on which the regulated integrand is absolutely integrable (at \(N=2\)) or the regulator factor is bounded by \(1\) (at \(N\ge3\)) all lie in \(\mathfrak C_0\), the class of the Hermitian contour. None of them reaches a real causal momentum. For any positive definite regulator, the same holds at \(N=2\) for the end points of paths as in (iii). The contours of \(-\mathfrak C_0\) that make the mode bounded at real timelike \(k\) compute observables at imaginary momenta. This is no statement about non-linear contours, about linear maps that also mix the colour components, about contours with \(h\in-\mathfrak C_0\) for general positive definite \(P\), about fixed \(\gamma>0\), about whether \(F_{\mathrm E}\) continues beyond \(\arg t=-3\pi/4\), about the pointwise limit at real timelike or null \(k\), about \(N\to\infty\) taken first, or about Definitions~(B) and~(C). The inertia found in (i) is that of the \(\eta\) put into \(S_{\mathrm b}\), which the regulator carries over to every admissible contour but does not select, so Assumption~\ref{ass:lorentzian} is still required.
```
