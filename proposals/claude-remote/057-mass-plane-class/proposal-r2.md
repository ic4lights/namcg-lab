# Proposal 057-mass-plane-class, round 2

## Changes r1 -> r2

| # | Review finding | Change |
|---|---|---|
| 1 | F1 (minor): (iii) claimed failure of domination for gamma_j unbounded; domination step implicit | R2 (two replacements) applied verbatim: non-integrability is for any real gamma in the mass term; the domination conclusion is restricted to gamma converging to a finite limit, and the step "a dominating function would also dominate the integrand at eps=0 on Lambda_inf with that limit of gamma" is stated. Proposal: Result item 2, order-of-limits answer, Step 6, claim classification and Remaining open step carry the same restriction. |
| 2 | F2 (minor): "there" ambiguous in the gamma <= 0 sentence | R1 applied verbatim: "For gamma <= 0, where -pi/2 <= phi <= 0, the interval (-pi, 2phi-pi] is empty, and the inertia argument of (i) of the preceding paragraph applies instead." |
| 3 | F3 (minor): closing clause repeated 056's | R3 applied verbatim: "... so they select no signature, and the positive mass does not discharge Assumption~ref{ass:lorentzian}." |
| 4 | F4 (bookkeeping) | apply_check and scratch build re-run; new hashes below. r1 insert kept as appH_insert.r1.tex (7714 bytes, f7fbbade...af82). Edits applied by apply_r2_edits.py (r1 hash checked; each old string once before, each new string once after; output apply_r2_edits.txt). |

No other change to the insert. The mathematics is unchanged.


## Result

This takes avenue 1 of review 056-r2: a fixed positive mass γ > 0. The result is a bounded no-go (M2, non-stopping). It closes the γ > 0 opening that 056 left for linear contours, at every N. Notation: γ' = γ/2g², M_γ = εΛᵀΛ + iγ'h, φ = arg(ε+iγ') ∈ (0, π/2), h_φ = e^{iφ}h, and D is the weak damping condition Re iS_b ≤ 0.

1. **Plane-class invariant (algebraic, every N).** Take a path of linear contours A = Λ(τ)X starting from a real Λ(0), with Re M_γ positive definite and Re iS_b ≤ 0 throughout. These are the conditions the Stokes arguments in appH use.
   - Let E be a real 2-plane on which Re h_φ is positive definite. The continuous branch Θ(E) = arctan σ₁ + arctan σ₂ of arg det(h_φ|_E) lies either in [2φ, π) (upper class) or in (−π, 2φ−π] (lower class). The two sets are separated by a gap of length π.
   - The identity (ε+iγ')h = M_γ − 2εℓℓᵀ gives Re h_φ > 0 on a real subspace of dimension ≥ 8. So the positive planes form a connected set, and their class is conserved along the path.
   - The Hermitian contour is in the upper class (Θ = 2φ).
   - Every contour with h ∈ −𝔆₀ and Re M_γ > 0 has a lower-class plane. This uses 055's normal form, in which at least eight β_μ lie in (0, π/2).
   - **Hence no such path joins the Hermitian contour to −𝔆₀.** In particular none reaches 056's γ > 0 contour A₀ = e^{iπ/8}X₀, A_i = e^{−3πi/8}X_i.
   - The same holds for isotropic P, since P − cη has rank one.
   - For γ ≤ 0 the lower class is empty, which is consistent with 056's separate inertia argument.
2. **ε → 0 (classes at every N, non-integrability at N = 2).** Take γ_j/ε_j → ∞, which includes fixed γ > 0. Suppose the end points of such paths converge to an invertible Λ_∞.
   - Then Im h_∞ = −κvvᵀ with κ ≥ 0.
   - On Σv_αX_α = 0, the quartic term S_b and the mass term are real, so at ε = 0 the integrand has modulus |Pf|.
   - At N = 2 the ε = 0 integrand of I[1] on Λ_∞ is not absolutely integrable (∫R^{26+24−9}dR = ∞).
   - This non-integrability holds with any real γ in the mass term.
   - So for fixed γ > 0, and for γ/ε → ∞ with γ converging to a finite limit, no linear contour reached from the Hermitian contour, fixed or convergent as ε → 0, carries the dominated-convergence argument used for γ ≤ 0: a dominating function would also dominate the ε = 0 integrand on Λ_∞ with that limit of γ. For γ_j → ∞ only the rank-one and reality statements are claimed. This explains the "admissible u closes like ε/γ" already recorded in appH.
3. **Not established:**
   - whether lim_{ε→0} I_{ε,γ} exists at fixed γ > 0, and whether it differs from the Euclidean model;
   - non-linear (thimble) contours and colour-mixing maps;
   - paths with Re M_γ only positive semidefinite;
   - anisotropic P, families that do not converge, N → ∞ first, and Definitions (B) and (C).

η is an input to S_b, and the classes are fixed by η and by the regulator. No signature is selected, and ass:lorentzian is retained. Problem E stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No label change is proposed.

**Answers to the avenue-1 questions in the task:**
- *Connectivity.* D ∩ GL(10,C), together with the regulator and the mass kept admissible (Re M_γ > 0), does **not** join η to the −𝔆₀ contour. This holds for all paths, diagonal or not, and at every N.
- *ε → 0 there.* The question is moot for linear contours: the −𝔆₀ contour is not reached, and no reached contour has a damped limit. 056 (iv) showed that the −𝔆₀ value is a mode at imaginary momentum, a different object. That observation is therefore not needed in order to exclude it, and it stays a statement about a different object.
- *Role of γ.* γ is a supplied Lorentz-invariant deformation of S_b, as in appH ("may be added"). Since no limit is reached, no physical role is assigned to it.
- *Order of limits.* With γ → 0 first, or γ/ε bounded, 053 gives the Euclidean values at phases. With ε → 0 at fixed γ > 0, or γ/ε → ∞ with γ converging to a finite limit, the linear-contour reduction is unavailable, so the order matters and the second order is undecided.

## Target and status

- **Problem E (signature).** Appendix H `sec:status-E`, quoted verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- **Chapter 17** (L394–399): "OPEN; CRITICAL PATH for the matrix-derived label. A scope that retains Assumption~\ref{ass:lorentzian} gives up the claim that Lorentzian signature is emergent or derived." The full-GR criterion list (L718) reads "Problem~E: Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})".
- The two sources are consistent. No discrepancy.
- **Original target:** derive Lorentzian signature rather than retaining ass:lorentzian (ch04 L321–327).
- **Dependencies:** 053–056, Problem E paragraphs (appH L1495–1562). Classification: **PROGRAMME-CONDITIONAL**. The package bounds one route, the regulated Lorentzian integral with a positive mass. It derives no signature.

## Source reading

- Digest + targeted reads. This is not a full scan.
- `make_digest.py --check` printed DIGEST CURRENT.
- `dirty-chapters: yes` is from 055 + 056 in appH only. `git status` shows only appH modified, plus this folder untracked.
- The baseline appH hash matches the task value: 561466 bytes, sha256 ea5c753b…a1f5.
- Read in full:
  - the appH Problem E section, L1482–1566, including the dirty 055 and 056 paragraphs (L1529–1562);
  - ch17 L394–399 and L712–725;
  - ch04 L314–331 (`ass:lorentzian`, label at L322);
  - 056 review-r2, the 056 proposal-r2 Step 6 and its γ statements;
  - the ledger tail for 053–056;
  - lines of the SME scout 20261102-after50 about γ.
- I did not use the SME scout for any claim. It also says not to treat γ > 0 as derived, and this package complies.
- Unreadable files: none.
- No definition, assumption, scope or status passage is changed, so 3(c) is not triggered. The ordinal-55 full scan is the gatekeeper's.

## Research and reasoning

Setting and notation are as in appH: Definition (A), and the linear contour A_μ = Σ_ν Λ_{μν}X_ν. Then
- h = ΛᵀηΛ;
- ℓ = Λᵀe₀ = a + ib, the row μ = 0 of Λ;
- M_γ = εΛᵀΛ + iγ'h, the matrix of the quadratic exponent on the contour (056);
- 𝔆 = 𝔆₀ ∪ (−𝔆₀), the normal form of 055.

### Step 0. Why fixed γ > 0 needs a new invariant
- For γ ≤ 0, 056 (i) excluded −𝔆₀ by inertia: Re(e^{iφ}h) has ≤ 1 negative eigenvalue, against ≥ 8 negative eigenvalues on −𝔆₀ when φ ∈ [−π/2, 0].
- For φ ∈ (0, π/2), the −𝔆₀ entries e^{iφ}(−d_μ) can have positive real part, so the inertia test passes. 056's example shows exactly this.
- The 056 Step 6 probe (not integrated) excluded only diagonal paths.
- So an invariant beyond inertia is needed.

### Step 1. The class of a positive plane
Let E be a real 2-plane with r = Re h_φ|_E > 0, and s = Im h_φ|_E, both in a real basis.
- Then det(h_φ|_E) = det r · Π_j(1 + iσ_j), where σ_j are the eigenvalues of r⁻¹s. These are real because r⁻¹s is similar to r^{−1/2}sr^{−1/2}, and they do not depend on the basis because a change of basis B conjugates r⁻¹s.
- Θ(E) = Σ arctan σ_j ∈ (−π, π) is a continuous branch of the argument on the open set {r > 0}.
- Damping at N = 2: Re iS_b = −(1/4g²) Σ_{a<b} Im[h(x^a,x^a)h(x^b,x^b) − h(x^a,x^b)²]. With x³ = 0, this shows Re iS_b ≤ 0 ⟺ Im det(h|_E) ≥ 0 for all real planes.
- For N ≥ 3, restrict to su(2) blocks. limit_checks.py check 5 confirms numerically that S_b on an N = 3 su(2) block equals the N = 2 formula (relative difference 1.8e−14).
- det(h|_E) = e^{−2iφ} det(h_φ|_E) in the same basis. So the damping condition reads sin(Θ − 2φ) ≥ 0.
- Since Θ − 2φ ∈ (−2π, π), this gives Θ ∈ [2φ, π) ∪ (−π, 2φ−π]. The excluded gap (2φ−π, 2φ) has length π.

### Step 2. Many positive directions
(ε+iγ')h = εΛᵀΛ − 2εℓℓᵀ + iγ'h = M_γ − 2εℓℓᵀ.
- For real x with aᵀx = bᵀx = 0 we have ℓᵀx = 0. Then xᵀ Re(h_φ) x = Re(xᵀM_γx)/|ε+iγ'| > 0.
- This subspace has dimension ≥ 8, so n₊(Re h_φ) ≥ 8.
- Checked numerically: identity residual 8.9e−16; min eig of Re h_φ on Z is > 0 in 357 admissible samples.

### Step 3. Connectedness and conservation
- **Connectedness of the positive planes.** Let R be a real symmetric matrix with n₊ ≥ 2. Let V₊ be its positive eigenspace and V_≤ the sum of its other eigenspaces; these are R-orthogonal. Take a plane E with R|_E > 0. Then E ∩ V_≤ = 0. For t ∈ [0, 1], E_t = {x₊ + t·x_≤ : x ∈ E} is a 2-plane, and R(x₊ + t·x_≤) = R(x₊) + t²R(x_≤) ≥ R(x) > 0. So E_t joins E to a plane in V₊, and Gr(2, V₊) is connected.
- **Conservation.** Θ is continuous with values in two disjoint relatively closed sets. So the class is constant on the positive planes at each τ. Each positive plane stays positive for nearby τ, so the class is locally constant in τ and hence constant on [0, 1].
- Continuity of the path is enough for this step. Piecewise C¹ is kept in the insert because the Stokes arguments use it.
- Numerically (check D), on 28 D-members, every sampled positive plane had one class and no gap value occurred.

### Step 4. End point classes
- **Hermitian end, τ = 0.** h is real with the inertia of η, and h_φ|_E = e^{iφ}r₀ with r₀ > 0. So σ = tan φ and Θ = 2φ: upper (check B).
- **−𝔆₀ end.** Write h = −Tᵀdiag(d)T. Here T is real, and the args β of d satisfy the 𝔆₀ pairwise condition. By 055 (ii), at least eight β lie in (0, π/2).
  - Re h_φ = Tᵀ diag(−Re e^{iφ}d_μ) T. By Step 2 and Sylvester, at least eight μ have −Re e^{iφ}d_μ > 0.
  - Since 8 + 8 > 10, at least six indices have both properties.
  - For such μ: β_μ ∈ (0, π/2), and cos(β_μ+φ) < 0 forces β_μ > π/2 − φ.
  - In the plane spanned by T⁻¹e_μ and T⁻¹e_ν, h_φ = diag(|d_μ|e^{i(β_μ+φ−π)}, …), so θ_μ = β_μ + φ − π ∈ (−π/2, 0).
  - Θ = β_μ + β_ν + 2φ − 2π < 2φ − π: lower.
- Checked: 1125 random admissible −𝔆₀ samples all passed. For 300 of them, a random real congruence was applied and all sampled positive planes were lower.
- **056 example.** Λ_* = diag(e^{iπ/8}, e^{−3πi/8}·1₉) gives h_* = −e^{iπ/4}·1. min eig Re M_γ = (γ'−ε)/√2, so Λ_* is admissible iff γ' > ε, i.e. φ > π/4 (check C). Then Θ(h_*) = 2φ − 3π/2: lower (check B, exact to 1e−9).
- **γ ≤ 0** gives φ ∈ [−π/2, 0], and the lower set (−π, 2φ−π] is empty. So the invariant is the γ > 0 tool, and 056's inertia argument covers γ ≤ 0. Consistent.

### Step 5. Isotropic regulators
- Take P > 0. In a real basis with P = 1 and η diagonal, the eigenvalues of P⁻¹η are one negative and nine positive. So a nine-fold eigenvalue 1/c has c > 0, and P − cη = κwwᵀ is rank one with κ > 0.
- Then (εc + iγ')h = εΛᵀPΛ + iγ'h − εκ(Λᵀw)(Λᵀw)ᵀ, and Steps 2–4 go through with φ = arg(εc + iγ').
- check G verifies the identity for P = diag(p₀, p, …, p) (residual 5e−15).

### Step 6. The ε → 0 limit
Take ε_j → 0 with γ_j'/ε_j → ∞, and reached end points Λ_j → Λ_∞ invertible.
- Re M_γ/|ε+iγ'| = cos φ·Re ΛᵀΛ − sin φ·Im h → −Im h_∞. So −Im h_∞ ≥ 0.
- Suppose n₊(−Im h_∞) ≥ 2. Take a plane E positive for −Im h_∞ = Re(i h_∞) = lim Re h_{φ_j}. Then E is positive for large j and upper: Θ_j(E) ≥ 2φ_j → π. But Θ_j(E) → Θ_∞(E) ∈ (−π, π). Contradiction.
- Hence Im h_∞ = −κvvᵀ with κ ≥ 0. Configurations with Σv_αX_α = 0: every imaginary contribution to S_b and to the mass term contains a factor v·X, so both are real. This holds at every N.
- **N = 2 non-integrability.** Write the colour columns as x^a = x_V^a + y_a v, with x_V^a ∈ v^⊥, which has dimension 9.
  - h_∞|_{v⊥} is real, of rank ≥ n − 2 = 8. So det 𝒢 restricted to v^⊥ is a nonzero real polynomial of degree 6. Check 3: nonzero, real, degree 6; rank 9 in the sample.
  - On an open cone with |x_V| = R, |det 𝒢| ≥ c'R⁶.
  - Im S_b has degree ≥ 2 in y and ≤ 2 in x_V (check 1), so |Im S_b| ≤ CR²|y|².
  - The mass part of the real exponent is −(γ'κ/2)|y|² (check 2).
  - For |y| ≤ R⁻³ the exponent is bounded, and det 𝒢 changes by O(R⁵·R⁻³) = O(R²).
  - |Pf| = |c_P||det 𝒢|⁴ ≥ cR²⁴.
  - So ∫|integrand| ≥ C∫^∞ R²⁶ · R²⁴ · R⁻⁹ dR = ∞. The mass part is bounded on the shift ball for any real γ, so this holds with any real γ in the mass term.
- **Domination step (r2).** If γ_j → γ_∞ finite, the integrands on Λ_j converge pointwise to the ε = 0 integrand on Λ_∞ with γ_∞; a dominating function G would satisfy G ≥ |that limit|, which is not integrable, so no integrable G exists. If γ_j → ∞, the pointwise limit of the moduli is supported on y = 0 and Fatou gives nothing; no domination statement is made there.
- R_u illustration (check H): at fixed γ' = 1, the largest admissible u is ≈ (4/3π)ε/γ' → 0, and the limit contour is h₀ = η, which is undamped. These numbers stay in the proposal; the insert only cites appH's "closes like ε/γ".

### Fork analysis (directive 2026-10-15)
Hypotheses of the no-go, and the relaxation for each:

| # | Hypothesis | Relaxation | Status |
|---|---|---|---|
| H1 | Linear contours A = ΛX, colour-blind | Non-linear contours / Lefschetz thimbles at fixed ε, γ | Open. The plane class is a linear invariant; a thimble decomposition is homological and not constrained by it. **Rank 1.** |
| H2 | Re M_γ positive definite along the path | Positive semidefinite boundary passages | Open. Step 2 then gives Re h_φ ≥ 0 on Z only. At N = 2, 056 (ii) shows Re M_γ ≥ 0 is necessary for absolute convergence, so only measure-zero boundary passages remain. Low rank. |
| H3 | Definition (A) / isotropic P | Anisotropic P | Open. P − cη has rank ≥ 2; the dimension bound becomes n − 2·rank. It survives for rank ≤ 4, which is not stated in the insert. |
| H4 | Convergent families Λ_j → Λ_∞ | Divergent or degenerate families | Open. Under the real congruence X → TX, h and M_γ are congruent, so a normalisation could reduce this. Not done. |
| H5 | Dominated convergence | Conditionally convergent / direct oscillatory analysis of I_{ε,γ} at N = 2 | Open. This is now the only route left for fixed γ > 0 at finite N. **Rank 2.** |
| H6 | Fixed N | N → ∞ first | The invariant is N-independent: the reachable linear contours are the same at every N. So N → ∞ first does not reopen linear contours. The limit itself is open. |
| H7 | Colour-blind linear maps | Colour-mixing linear maps | Open. **Rank 3.** |
| H8 | γ a supplied deformation | A dynamically generated mass | Out of scope here. No mechanism is in the manuscript. |

**Ranked open avenues for the queue** (r2: the review ranks the direct oscillatory analysis first, as the only finite-N route left for fixed γ > 0; I adopt that order, so items 1 and 2 below are swapped in priority):
1. Thimbles at fixed γ > 0, N = 2.
2. A direct oscillatory or conditionally convergent analysis of lim_{ε→0} I_{ε,γ} at N = 2. This would decide whether the γ > 0 integral is genuinely non-Euclidean; the inequivalence for γ > 0 recorded from Anagnostopoulos2026 is not re-verified here.
3. Colour-mixing maps.
4. Anisotropic P of low rank.
5. Thimbles at real causal k for γ = 0 (056 avenue 2).
6. N → ∞ first; Definitions (B) and (C).

**Bearing on the NAMCG derivation.** For γ > 0 the regulated integral cannot be reduced to the Euclidean model by linear contour rotation. Nor can it be pushed to the −𝔆₀ contour that would compute imaginary-momentum data. The only contours available degenerate onto the undamped Lorentzian contour as ε → 0. So γ > 0 is the one setting where an intrinsically Lorentzian (oscillatory) limit is not excluded by these methods. That supports avenue 2 as the next target. It does not derive η, because the classes are those of the η in S_b.

### Literature
No new citation is used. The insert relies only on manuscript statements (053–056 paragraphs). Anagnostopoulos2026 is not used for any claim, and is mentioned above only as what appH already records.

## Claim classification

| Claim | Class |
|---|---|
| Θ(E) branch; upper/lower dichotomy under Re iS_b ≤ 0 (N = 2 equivalence; N ≥ 3 via su(2) block) | established |
| Re h_φ > 0 on a subspace of dimension ≥ 8 when Re M_γ > 0 | established (exact identity) |
| Connectedness of positive planes; conservation of class along paths | established |
| Hermitian contour upper; every admissible −𝔆₀ contour lower; no path joins them (every N) | established |
| 056 γ > 0 contour excluded for every γ' > ε | established |
| Isotropic P extension | established |
| γ ≤ 0: lower class empty | established (consistency) |
| ε → 0 with γ/ε → ∞: Im h_∞ = −κvvᵀ; S_b and mass term real on v·X = 0 (every N) | established, conditional on convergence of Λ_j |
| N = 2: ε = 0 integrand on Λ_∞ not absolutely integrable, any real γ in the mass term | established (N = 2) |
| No dominated convergence along reached families for fixed γ > 0, or γ/ε → ∞ with γ converging to a finite limit | established (N = 2) |
| Domination statement for γ_j → ∞ | not claimed |
| Existence or value of lim_{ε→0} I_{ε,γ} at fixed γ > 0 | unresolved |
| Non-linear contours, colour mixing, anisotropic P, psd paths, divergent families, N → ∞ first, Definitions (B) and (C) | unresolved |
| Random-walk and sample numerics (checks D, E, F) | numerical illustration, not proof |
| Lorentzian signature | not derived; η is an input (ass:lorentzian retained) |

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`, Problem E.
- **Placement:** insert one new paragraph, `proposals/057-mass-plane-class/appH_insert.tex` (LF; CRLF on integration), immediately before the unique anchor at L1564–1565. Follow it with one blank line.
  ```
  \paragraph{Status.}
  Remains Assumption~\ref{ass:lorentzian}.
  ```
  The anchor is 61 bytes in CRLF form, sha256 a7c77412…26cc. It occurs exactly once; the other "Remains Assumption" line is `ass:EFT-a2`, at L3246.
- **What is kept:** all existing text. Nothing is replaced or removed, and the Status paragraph is unchanged.
- **Stale passages elsewhere:**
  - 056's closing sentence "This is no statement about … about fixed γ > 0 …" remains true as a scope statement of that paragraph. The new paragraph treats fixed γ > 0 within its own scope, so no edit is needed.
  - 053's "For fixed γ>0 the admissible u closes like ε/γ as ε→0, and nothing is stated" is consistent with (iii) and is kept.
  - The ledger and appJ are not affected.

```latex
\paragraph{A positive mass: the class of planes fixed by the regulator (algebraic at every \(N\), proved at \(N=2\)).}
Keep the setting and notation of the two preceding paragraphs, with Definition~(A) and the mass term, and let \(\gamma>0\). Write \(\epsilon+\mathrm i\gamma'=|\epsilon+\mathrm i\gamma'|\mathrm e^{\mathrm i\varphi}\) as in (i) of the preceding paragraph, now with \(0<\varphi<\pi/2\), and put \(h_\varphi=\mathrm e^{\mathrm i\varphi}h\). Consider paths \(\Lambda(\tau)\), \(0\le\tau\le1\), piecewise continuously differentiable, with \(\Lambda(0)\) real, \(\operatorname{Re}\mathrm iS_{\mathrm b}\le0\) on every contour of the path and \(\operatorname{Re}M_\gamma(\tau)\) positive definite, the conditions used for the Stokes arguments above.

(i) \emph{Classes of planes.} ... [full text in appH_insert.tex; 8046 bytes LF]
```
The exact text to integrate is `appH_insert.tex`. It is not reproduced in full here to avoid divergence. It has five blocks: the intro, (i), (ii), (iii), and the closing paragraph.

- **Labels:** only `\ref{ass:lorentzian}` is used. It is defined once, at ch04 L322. No new labels and no citations.
- **New local symbols:** `h_\varphi`, `\Theta(E)`, `E`, `r`, `s`, `\sigma_{1,2}`, `a'`, `b'`, `\kappa`, `v`, `c'`, `\Lambda_\infty`, `h_\infty`, `\epsilon_j`, `\gamma_j`, `\varphi_j`.
  - `\varphi` is reused with 056's definition, arg(ε+iγ'), now in (0, π/2).
  - `c` is reused locally in (ii) for 1/(nine-fold eigenvalue). It does not clash with 056's `c_{\mathrm E}` or with (iii), which uses `\kappa`.
  - `T`, `d_\mu`, `\beta_\mu` are used as in 055 (i).

**Hashes (apply_check.txt):**
- baseline appH: 561466 bytes, sha256 ea5c753b0f01a3a92e426435f747fa464521980f609ab330f4a432868daba1f5, CRLF 3255, bare LF 0;
- insert (r2), LF form: 8046 bytes, sha256 4e0a85d101eaa1300a6206ed8760d83e4c5a74950b8b789d8fcfc3d7c20c0a7d;
- insert (r2), CRLF form: 8056 bytes, sha256 bcc5ccef706012f26ae998ed121eb4e7aa025391cbb37da004991def5bc49253;
- resulting appH: 569524 bytes, sha256 9443341b74f991d49fee3b08830dd44da7f9a12245922f52aaa193b0bd607bcd, CRLF 3266, bare LF 0;
- r1 insert kept as appH_insert.r1.tex: 7714 bytes, sha256 f7fbbade4567d6843f13fe50f06ccb457cc78ac230863e1505b0bdb8f074af82.

**Scratch build:**
- The repository files were copied to the session scratchpad (`build057/`), the resulting appH was put in place, and two `pdflatex -interaction=nonstopmode -halt-on-error` passes were run.
- r2 rebuild: both passes exited 0. Output: **365 pages**, 0 "undefined" and 0 "multiply" matches in the log. The appH in the build copy has the expected resulting hash 9443341b...7bcd.
- The result file hash in the build copy equals the expected resulting hash.

## Verification scripts

All are in `proposals/057-mass-plane-class/`. Outputs are saved as `.txt`.
- `plane_class_checks.py` → `plane_class_checks.txt` (about 2 min):
  - A: the identity, Z-positivity and n₊ ≥ 8;
  - B: Θ at η (= 2φ, upper) and at h_* (= 2φ − 3π/2, lower);
  - C: admissibility of Λ_* iff γ' > ε;
  - D: a single class on the positive planes of D-members;
  - E: the −𝔆₀ lemma, 1125 samples;
  - F: random walks inside the admissible set starting on R_u, u = 0.3ε/γ'. The class stays upper. Biased walks are blocked early; the third case accepted no steps at this step size, so it is illustration only;
  - G: the isotropic-P identity;
  - H: R_u admissible u ≈ (4/3π)ε/γ'.
- `limit_checks.py` → `limit_checks.txt` (about 4 min, sympy):
  - 1: Im S_b has degree ≥ 2 in y and ≤ 2 in x_V;
  - 2: the imaginary part of the mass form is −κΣy²;
  - 3: det 𝒢 on v^⊥ is nonzero, real and of degree 6;
  - 4: the exponent count;
  - 5: the N = 3 su(2)-block reduction of S_b.
- `apply_check.py` → `apply_check.txt`: baseline, anchor, insert form (ASCII, LF, no trailing whitespace) and hashes. It writes the would-be appH only outside the repository.
- `edit_insert.py`, `edit_insert2.py`, `edit_insert3.py`: the r1 drafting edits applied to the insert, recorded for transparency. They are idempotent.
- `apply_r2_edits.py` → `apply_r2_edits.txt`: the r1 → r2 replacements R1, R2a, R2b, R3 (r1 hash check; uniqueness of old and new strings).
- `make_r2.py`: builds this file from proposal-r1.md.

## Decisions Taken

1. **Target: avenue 1 (fixed γ > 0), not thimbles or the oscillatory analysis.** It is the one open hole in 056's no-go. It is algebraic, so it is tractable at every N. Either outcome changes the direction: a reachable −𝔆₀ would give a new object, while exclusion makes the direct γ > 0 analysis the remaining route. Avenues 2 and 3 are heavier and are now re-ranked behind the γ > 0 oscillatory analysis.
2. **Path class:** Re M_γ positive definite with Re iS_b ≤ 0. This matches 056 (iii) and the Stokes class used throughout appH. The psd boundary is recorded as open (H2), not claimed.
3. **Include (iii), the ε → 0 family statement.** It answers the task's "what is the ε → 0 limit there" and explains appH's existing "closes like ε/γ". Non-integrability is claimed only at N = 2. At N ≥ 3 only the reality of S_b on v·X = 0 is stated.
4. **Isotropic P is included and anisotropic P is excluded.** The rank-one proof is one sentence. The low-rank anisotropic case (rank ≤ 4) needs a separate end-point lemma and is left open.
5. **No reliance on Anagnostopoulos2026.** The γ > 0 inequivalence is not invoked in the insert.
6. **Wording of γ:** "a supplied deformation of the action", following appH's "may be added" and the SME caution. γ is not called a physical mass or a derived regulator.

## Milestone assessment

M2: a reproducible bounded obstruction that changes the research direction. It closes the γ > 0 linear-contour opening and shows that, for γ > 0, only a non-linear or direct oscillatory analysis remains. This is non-stopping, and not a breakthrough: no critical-path step is derived, and η stays an input.

## Status-label recommendation

- **Critical-path set:** from the ch17 full-GR criterion list (read at L712–725) and the appH ledger labels, it is A, B, C, D1, E, F, G-derived and N.
- **Affected:** Problem E only. Its label is unchanged: OPEN, CRITICAL PATH for the matrix-derived label, PROGRAMME-CONDITIONAL.
- No label change is recommended.

## Author decision needed

None.

## Remaining open step

To close Problem E, Lorentzian signature must be derived rather than retained: η must come out of the matrix theory, not out of S_b or the regulator. For the γ > 0 route specifically, the next step is to decide whether lim_{ε→0} I_{ε,γ} exists at fixed γ > 0 at N = 2, and whether it differs from the Euclidean model. That needs a direct oscillatory or conditionally convergent analysis, or non-linear (thimble) contours. The linear-contour exclusion of dominated convergence is stated only for γ converging to a finite limit; families with γ_j → ∞ are covered only by the rank-one and reality statements. Even a positive answer would show only that the γ-deformed Lorentzian integral is inequivalent to the Euclidean one; it would not derive η.

## Special instructions for the gatekeeper

- Re-derive these:
  - (a) the dichotomy sin(Θ − 2φ) ≥ 0 ⟹ Θ ∈ [2φ, π) ∪ (−π, 2φ−π];
  - (b) the dimension-8 positivity from (ε+iγ')h = M_γ − 2εℓℓᵀ;
  - (c) connectedness of the positive planes, and why n₊ ≥ 2 is needed;
  - (d) the −𝔆₀ lemma, including "β > π/2 − φ" and Θ = β_μ + β_ν + 2φ − 2π;
  - (e) the limit argument Θ_j ≥ 2φ_j → π;
  - (f) the R-exponent count 26 + 24 − 9.
- Must not be asserted:
  - that the γ > 0 limit is or is not Euclidean;
  - that γ is physical or derived;
  - that the classes select a signature;
  - anything about non-linear contours.
- Check that the insert's "in line with the closing of the admissible u on R_u like ε/γ" faithfully cites 053's sentence (appH Problem E, first paragraph, "For fixed γ>0 the admissible u closes like ε/γ as ε→0").
- The c in (ii) is local to the isotropic-P sentence.
- Ordinal 55: the 5th-item full scan is due on your side.
- Process note: no git write commands were run. I wrote only in this folder and in the session scratchpad (`appH_057_result*.tex`, `build057/`). Nothing was denied, and I deleted nothing.
