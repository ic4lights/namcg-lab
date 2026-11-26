# Proposal 054-nonpolynomial-observables-lorentzian-n2, round 1

## Result

Bounded no-go plus a bounded positive fork, both inside the 053 hypothesis class.

1. **No-go (γ = 0).** Fix `N = 2`, regulator (A), the contour family `R_u` (053 definition (B)), and
   `ε → 0⁺` last. For the non-polynomial family `O_k(A) = Tr exp(i k^μ A_μ)`, `k ∈ C^10`, the 053
   displayed limit identity (`lim_{ε→0} I_ε[O] = e^{7πi(N²−1)/4} · (Euclidean rotated integral)`)
   holds **exactly at `k = 0`** and for no other `k`. There is no analyticity strip in `k`:
   - for every **real** `k ≠ 0` the *right-hand side* (Euclidean rotated integral) diverges in
     modulus: along rank-one rays the Euclidean weight at `u = 1` is not exponentially damped
     (`S_E = 0` on commuting matrices, 053), the Pfaffian vanishes on the ray but only
     polynomially nearby, and `|O_k| ≥ e^{b_u(ρ̂;k) ρ}/4` with `b_u(ρ̂;k) > 0` on an open set of ray
     directions for every real `k ≠ 0` (at `u = 1` the growth functional has coefficients
     `(−sin(3π/8) k^0, sin(π/8) k⃗)`);
   - more generally the RHS diverges for every `k` outside the 10-real-dimensional "anti-Wick"
     slice `{k^0 e^{−3πi/8} ∈ R, k^i e^{πi/8} ∈ R}`, and converges on that slice (there
     `|O_k| ≤ 2` and the 053 `k < 14` window at order 0 applies);
   - for every **non-real** `k` the *left-hand side* `I_ε[O_k]` has no finite `ε → 0⁺` limit:
     a commuting ray with `(Re k·ρ)(Im k·ρ) > 0` has `S_b = 0` and `|O_k| ~ e^{bρ}`, `b > 0`, and
     the regulated Laplace integral along it grows like `e^{c_2(k)/ε}` along a sequence
     `ε → 0⁺`;
   - for real `k ≠ 0` the 053 dominated-convergence step itself fails: no fixed-`u` domination
     uniform in `ε` exists at any `u ∈ (0, 2/3)`, and the fixed-`ε` modulus on `R_u` grows without
     bound as `ε → 0` (numerically like `e^{c(k,u)/√ε}`).
   The LHS at fixed `ε` is finite for real `k` (`|O_k| ≤ 2` at `u = 0`), so the asserted identity
   fails for real `k ≠ 0` because its RHS diverges, and for non-real `k` because its LHS has no
   limit. Obstruction: the massless flat (commuting) direction.
2. **Positive fork (γ < 0).** At fixed `γ < 0` the mass contributes on `R_u` the real exponent
   `(γ/2g_YM²)[sin(3πu/4) Tr Ã_0² + sin(πu/4) Σ_{i=1}^{9} Tr Ã_i²]` (all-plus, damping on every
   component for `u ∈ (0,1]`). That Gaussian dominates `e^{c(k)‖Ã‖}` uniformly for
   `ε ≤ ε_0 < |γ|/(2g_YM²)`, the fixed-`ε` Stokes chain, the DCT and the `δ`-factor move to
   `u = 1` all go through verbatim for `O_k`, and the 053 limit identity extends to `O_k` for
   **every** `k ∈ C^10`. This is a conditional result about a different theory (massive), stated
   with the mass retained throughout.
3. **γ > 0 / CNT scoping.** At fixed `γ > 0` the `u = 1` integral of the `R_u` family diverges in
   modulus even at `k = 0` (the mass Re exponent is positive on all components there), so the
   fixed-contour family and the Lefschetz-thimble construction of Chou–Nishimura–Tripathi
   (2501.17798) act on *different contour integrals*; no numeric conflict with their `γ > 0`
   statement is possible within `R_u`. The unexplained gap in their `γ < 0` plots (already recorded
   in Appendix H) is untouched. The "classicalization" of Asano–Nishimura–Piensuk–Yamamori
   (2404.14045) is tied in that paper to a Lorentz-breaking IR cutoff and is recorded as bearing
   neither on the new paragraph nor on the 053 statements.

Nothing here closes Problem E, derives a signature or a real-time reading, or discharges
Assumption `ass:lorentzian`.

## Target and status

- Problem E, "Lorentzian signature", `chapters/appH-microscopic-proofs.tex`, section
  `\label{sec:status-E}` (L1483). Verbatim current ledger label (L1485–1489): "Status: OPEN.
  Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope
  retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived
  Lorentzian signature."
- `chapters/ch17-agenda.tex` L394–399: "Problem E: Lorentzian signature. OPEN; CRITICAL PATH for
  the matrix-derived label." Consistent with Appendix H. E is in the current Chapter 17
  full-GR/matrix-derived criterion set (A, B, C, D1, E, F, G-derived, N per the ledger;
  re-derived from ch17 on this task).
- Original target of E: derive Lorentzian signature (and the Lorentzian model) from the matrix
  theory without retaining `ass:lorentzian`. This proposal is a follow-up of the integrated 053
  result on the same target's finite-N regulated integral: 053's closing exclusion sentence
  (L1510) listed non-polynomial observables `Tr e^{ik·A}` as untreated; this package determines
  their treatment (ledger L428, open avenue (1); SME scout rank-1 route R1′,
  `reports/sme-scout-20261106-2023.md`).
- DERIVED or PROGRAMME-CONDITIONAL: the programme-conditional reading is unchanged; the new
  results are themselves conditional (γ = 0 no-go inside a named hypothesis class; γ < 0
  extension for the massive theory). Problem E remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Source reading

digest + targeted reads. `python scripts/make_digest.py --check` → `DIGEST CURRENT`
(head 30a1e07b4dc713200a822f20ff026f76e02ccc10, tree-hash 50ce909367841437, chapters-hash
14772a53002f3024, appH 7a75554ef8cb…, files 30, `dirty-chapters: yes` — the uncommitted 052+053
integrations are the working tree, which is what I pinned and built against).
Read in full: the whole Problem E entry `chapters/appH-microscopic-proofs.tex` L1483–1513
(re-read verbatim this round, quoted above and in "Proposed changes" with the anchors);
`chapters/ch17-agenda.tex` L394–399; the whole 053 package (`proposals/053-lorentzian-integral-limit-order/`,
proposal-r3 + review-r3, established baseline); `reports/ledger.md` L421–429 (053 block and its
open-avenue ranking) and the 049–052 blocks; `reports/sme-scout-20261106-2023.md` (routes R1′ etc.);
the 053 reduced-integrand code path reused in `n2_exp_mech.py`; the definitions (A)/(B)/(C) at
L1496, contours L1498, flat-direction bound L1500, limit identity L1502–1506, Definition (C) at
L1508. No unreadable files. Bibliography keys `ChouNishimuraTripathi2025` and
`AsanoNishimuraPiensukYamamori2025` verified present in `bib/namcg.bib` (arXiv records
2501.17798 and 2404.14045 verified by me in earlier rounds of this investigation; their
content claims used here are only: CNT treat thimbles and report γ>0 obstruction / inequivalence
for (C), and ANPY tie classicalization to a Lorentz-breaking IR cutoff).

## Research and reasoning

Notation: `R_u`: `A_0 = e^{−3πiu/8} Ã_0`, `A_i = e^{πiu/8} Ã_i`, `Ã_μ` traceless Hermitian
(053/Appendix H L1498); `S_b = −(1/4g²) Tr[A_μ,A_ν][A^μ,A^ν]` (eq `eq:Smatrix`); mass
`S_γ = −(γ/2g²) Tr A_μ A^μ` (L1496); `I_ε[O] = ∫dA O Pf M e^{iS_b − ε Σ Tr A_μ²}` (definition (A)).

**(i) Fixed-ε extension to `O_k`, `u < 2/3` (established derivation).** On `R_u`,
`Re iS_b = −sin(πu/2) S_E` and the regulator real part is
`−ε[cos(3πu/4) Tr Ã_0² + cos(πu/4) Σ Tr Ã_i²]` (053). For `u < 2/3`, `cos(3πu/4) > 0`, so the
regulator damps every component at rate `ε cos(3πu/4) ‖Ã‖²`. Pointwise,
`|O_k| ≤ 2 e^{|Im ρ_X|/2} ≤ 2 e^{c(u,k)‖Ã‖}` since `ρ_X² = k^μ k^ν G_{μν}(A(u,Ã))` is quadratic
in `Ã`. The Gaussian beats `e^{c‖Ã‖}` and the N=2 Pfaffian is polynomially bounded on `R_u`
(`|Pf| = |c_P| |det G|⁴ ≤ |c_P| (det G̃)⁴` by Cauchy–Binet, 053), so the integral converges
absolutely at fixed `ε`, is entire in `k` by locally uniform bounds (Weierstrass), and the
fixed-`ε` Stokes step survives: the boundary term on the radius-`R` sphere is polynomial times
`e^{−ε cos(3πu/4) R² + c(u,k) R} → 0`. Hence `I_ε[O_k]` equals the `R_u` integral for all
`u < 2/3`, for every `k`, at fixed `ε`.

**(ii) N=2 spectral identity (established, sympy + numerics: `strip_symmetry.py` 1a–1e).** For
`N = 2` and any complex traceless `2×2` `X = k^μ A_μ`: `X² = (z·z)/4 · I` with
`z_μ = k·A^a`-type contraction (PASS 1a), `Tr X^{2m} = 2(z·z/4)^m` (PASS 1b), so
`Tr e^{iX} = 2 cos(ρ_X/2)` with `ρ_X² = k^μ k^ν G_{μν}`, branch-independent since cos is even
(PASS 1c, 40 dps, err < 1e−25), and
`|2 cos((x+iy)/2)|² = 4(cos²(x/2) + sinh²(y/2))` exactly (PASS 1d). `z·z` is invariant under
complex-orthogonal rotations of `z` (PASS 1e).

**(iii) Growth on the flat rays and RHS divergence (derivation + numerics).** Take rank-one rays
`Ã_μ = ρ_μ H`, `Tr H² = 1`. Then `[Ã_μ, Ã_ν] = 0`, so `S_E = 0` along the ray and at `u = 1` the
Euclidean weight is `e^{−S_E} = 1` (no damping along the ray — this is the 053 observation that
`S_E` vanishes on commuting matrices); `G` is rank 1 on the ray, so `Pf = c_P (det G)⁴` vanishes
on the ray, but it is a polynomial of the coordinates, so near the ray it suppresses only by
powers. The radius enters `O_k` as `|O_k|² = 4(cos²(Re ρ_X/2) + sinh²(Im ρ_X/2))` with
`Im ρ_X = ρ · v_u(ρ̂;k)`, `v_u(ρ̂;k) = Im(k^0 e^{−3πiu/8} ρ̂_0 + e^{πiu/8} k⃗·ρ̂)` (H normalized),
so along the ray `|O_k| ≥ e^{b_u(ρ̂;k) ρ}/4` for large `ρ`, `b_u = |v_u|`.
The functional `ρ̂ ↦ v_u(ρ̂;k)`: at `u = 1` its coefficients are
`(−sin(3π/8) k^0, sin(π/8) k⃗)` (PASS (3)), so it is nonzero for every real `k ≠ 0`; its joint
zero set in `(k, ρ̂)` has real dimension 4 at `u = 0, 1/2, 1` (PASS (2a)), and for fixed real
`k ≠ 0` it vanishes for all `ρ̂` only at `k = 0` (rank check, PASS (2c–e) at `u = 1, 1/2, 1/4`).
So for every real `k ≠ 0` there is an open set of ray directions with `b_u > 0`.
Rigorous shape of the divergence in the 053 reduced coordinates (`w1 ≥ w2 ≥ w3`, the N=2
3-singular-value chart of the 053 code path: measure weight
`(w1 w2 w3)^{(d−4)/2} · jac · Vd · e^{−λ e2}`, `e2 = w1w2 + w1w3 + w2w3`): set
`w1 = e^s, w2 = e^{s−v}, w3 = e^{s−v−z}` and take the strip `v = 2s + σ`, `σ` bounded: then
`e2 = e^{−σ} + e^{−4s−2σ−z}` is bounded (ray limit `e2 → 0`), the weight is polynomial times
`e^{−λe2}` (no exponential damping along the strip), the Pfaffian and base factors
(`∏ Q_j^{−1/2}`, Fresnel `Q_j` of the 053 reduction) are polynomial in `e^s` (dominant power
`e^{−s/2}`-type), and the ray radius is `ρ ~ √w1 = e^{s/2}`, so the modulus integrand on the
strip dominates `c e^{−q s − c′ e^{−σ}} e^{b e^{s/2}}`, whose `ds`-integral diverges for every
`b > 0`. Numerics (`n2_exp_mech.py`, exp 1, masked one-sided proxy `cosh(cb√w1)`, honest lower
bound for every nonzero real `k`): `log10|Zmod|(smax = 8,10,12,13.5)` = 5.4657 (flat, `cb = 0`
baseline) vs 5.6433/6.2534/43.8307/117.2064 (`cb = 0.4`): unbounded growth, on the exact 053
reduced code path (validation exp 0 reproduces the 053 Euclidean `Z` and its phase
`7g/4 mod 2 = 1.25`, grid-stable to 8 digits, `|Zmod|/|Z| = 1.0000` at `k = 0`).
General `k`: `|O_k| ≤ 2` along the full ray family holds iff `k^0 e^{−3πi/8} ∈ R` and all
`k^i e^{πi/8} ∈ R` (anti-Wick slice; at `u = 1` this is `O_k(A(R_1 Ã)) = Tr e^{i(k̃·Ã)}` with real
`k̃`); on that slice `|O_k| ≤ 2` and the RHS converges by the 053 `k < 14` window (its `k = 0`
case at N=2, proved there via Cauchy–Binet + singular values); off the slice, some ray has
`Im ≠ 0` and the same strip argument diverges.

**(iv) LHS for non-real `k` (derivation + numerics).** At `u = 0` (Hermitian `A`), a commuting
ray `A_μ = ρ_μ H` has `S_b = 0` exactly (all commutators vanish) and regulator `e^{−c ε ρ²}`,
`c = Tr H²`-type. With `ω(ρ) = ρ (k·ρ̂) (Tr H²)^{1/2}` one has
`O_k = 2 cos(ω/2) = e^{iω/2} + e^{−iω/2}`, and for `(Re k·ρ̂)(Im k·ρ̂) > 0` one of the two
exponentials is `e^{+bρ} e^{i aρ}` (`b = |Im ω|/ρ /2 > 0`, `a = Re ω/ρ /2`): the regulated Laplace
integral `∫ dρ ρ^q e^{bρ + iaρ − cερ²/2} ~ (up to ε-powers) e^{(b²)·2/(cε)} e^{i θ/ε}` along
each branch; the two branches have equal modulus `e^{b²·2/(cε)}` and combine as
`2 e^{b²·2/(cε)} cos(θ/ε + φ)` (phase cancellation possible at isolated `ε`), so along a
sequence `ε → 0⁺` the modulus grows like `e^{c_2(k)/ε}` with `c_2(k) > 0`. A finite
`ε → 0` limit would have to bound every sequence, so `lim I_ε[O_k]` does not exist (as a finite
number) for any non-real `k` that admits such a ray; every non-real `k` does (take `ρ̂` with
`(Re k·ρ̂)(Im k·ρ̂) > 0`, possible for all non-real `k`). The transverse Pfaffian factor is a
positive polynomial near the ray and does not change the conclusion. I deliberately do **not**
claim a rate off that sequence (an earlier draft claimed polynomial growth "off it"; it is not
derived and is dropped from the insert).

**(v) Real `k`: the 053 chain breaks and the identity fails (derivation + numerics).** At
`u = 0`, `k·A` is Hermitian, its eigenvalues are `±ρ/2` real, so `|O_k| ≤ 2` and `I_ε[O_k]` is
absolutely convergent and finite at fixed `ε`. The 053 limit proof needs DCT on a fixed
`R_u`, `u ∈ (0,2/3)`, with a domination in `ε`; the would-be dominating integral is
`∫ |Pf| |O_k(A(u,Ã))| e^{−sin(πu/2)S_E} dÃ` times an `ε`-Gaussian factor absorbed into the
domination — and by (iii) it diverges for real `k ≠ 0` (same rays, `v_u ≠ 0` at every
`u ∈ (0,1]`). So no fixed-`u` domination exists at any admissible `u`: the 053 dominated
convergence argument provably fails for these `O`. Whether `lim_{ε→0} I_ε[O_k]` exists as an
improper (Fresnel/Abel) limit for real `k ≠ 0` is left open (Remaining avenue 1); it cannot
rescue the identity, because the RHS diverges for these `k` by (iii). Numerically the fixed-`ε`
modulus on `R_u` (masked one-sided proxy, `cb = 0.4`) grows as `ε → 0`:
`log10 Zmod(ε = 1, 0.3, 0.1, 0.03, 0.01) = 3.0022, 5.4395, 6.1945, 6.4700, 6.5502` at `u = 0.6`
(fit `0.6526 ε^{−1/2} + 9.8957`) and `4.2432, 7.7093, 8.8385, 9.2571, 9.3796` at `u = 0.3`
(fit `0.9527 ε^{−1/2} + 14.0109`); the fit slopes are window/grid-limited lower bounds on the
growth (the `s`-range is capped at `log(80/ε)`), the signed values grow too
(`|Z| = 7.9e2 → 4.1e5` at `u = 0.6`), consistent with, but not proving, non-existence.

**(vi) γ < 0 extension (conditional derivation + numerics).** `Re iS_γ` on `R_u` equals
`(γ/2g²)[sin(3πu/4) Tr Ã_0² + sin(πu/4) Σ_i Tr Ã_i²]` (sympy PASS (4a); all-plus signs — an
earlier draft of mine had a wrong relative sign, corrected; `u = 1` coefficient
`γ√2/(4g²)` per component, PASS (4b); at `u = 0` the mass is a pure phase, PASS (4c)). For
`γ < 0` this damps every component for all `u ∈ (0,1]` (`sin(3πu/4) > 0` there). At fixed `ε`
the net `Ã_0` quadratic coefficient on `R_u` is
`−ε cos(3πu/4) + (γ/2g²) sin(3πu/4) ≤ −ε cos(3πu/4) − (|γ|/2g²) sin(3πu/4)`, negative for all
`u ≤ 1` iff `ε < (|γ|/2g²) tan(3πu/4)` where `cos > 0` automatically, hardest at `u = 1`:
`ε √2/2 − |γ| √2/(4g²) < 0 ⟺ ε < |γ|/(2g²)`. Fix `ε ≤ ε_0 < |γ|/(2g²)`. Then: absolute
convergence and entire-in-`k` at every `u ∈ [0,1]` (Gaussian beats `e^{c(k)‖Ã‖}` and the
polynomial Pfaffian bound); fixed-`ε` Stokes between any two `u`'s (sphere boundary
poly·`e^{−a(u) R² + c(k)R} → 0`); DCT `ε → 0` at fixed `u < 2/3` with domination independent of
`ε` (mass Gaussian); the 053 move to `u = 1` with the `δ`-factor — 053 already states "For fixed
`γ < 0` the contour argument reaches `u = 1` with the mass retained", and for `O_k` the extra
boundary domination is the same Gaussian vs `e^{c‖Ã‖}`. Result: the displayed identity extends
to `O_k` for every `k ∈ C^{10}` at fixed `γ < 0`, mass retained on both sides. Numerics
(exp 2): bare `k = 0` `u = 1` modulus partials converge flat at `γ = −0.2` (5.1552) and `γ = 0`
(5.4657); with the honest large-radius growth proxy `cb = 0.4`: `γ = −0.2` converges flat
(5.3266 at smax 8…13.5) — Gaussian dominates the exponential-growth carrier — while `γ = +0.2`
diverges (`85.7660` at smax 8, overflow beyond).

**(vii) γ > 0 and CNT (comparison scoping).** PASS (4a): `γ > 0` gives Re growth on **all**
components of `R_u`, `u ∈ (0,1]`; at `u = 1, ε = 0` the bare `k = 0` modulus integral diverges
(exp 2: 76.6053 at smax 8, overflow beyond): on the fixed family `R_u` the would-be Euclidean-side
integral with the `γ > 0` mass does not exist absolutely, consistent with 053 ("For fixed
`γ > 0` the admissible `u` closes like `ε/γ` … and nothing is stated") and with
Anagnostopoulos et al.'s stated failure of equivalence for `γ > 0`. CNT (2501.17798) instead
deforms to Lefschetz thimbles on which Re action is negative by construction: at `γ > 0` their
contour and `R_u` are different contour integrals, so their thimble values neither confirm nor
contradict the `R_u` statements; no shared quantity to compare numerically exists at `γ > 0`.
This resolves the ledger avenue (2) at the definitional level only. The CNT `γ < 0` plot gap
(Appendix H L1508, "not reproduced … not resolved here") remains open.

**(viii) Classicalization.** 2404.14045 ties the "classicalization" behaviour to an IR cutoff
that breaks Lorentz invariance in the regularization; recorded (one sentence in the insert) as
barring it from bearing on these statements. Classification: input from the cited paper (I did
not re-derive it); I verified the arXiv record exists and contains that framing.

**Comparison with the original target.** E's target (derive Lorentzian signature without
`ass:lorentzian`) is untouched: the no-go is about the observable class in an already-conditional
finite-N regulated integral, and the γ<0 extension is about a massive deformation. The result
does, however, locate exactly where the missing ingredient sits for the IR two-point programme:
the massless flat direction (the same locus that carries the `k ≥ 14` growth of 053), and it
identifies the mass sign as the switch.

## Claim classification

- (i) fixed-ε absolute convergence, entire-in-`k`, fixed-ε Stokes for `O_k`, `u < 2/3`:
  **established derivation** (extends 053's own estimates; sympy-free, standard).
- (ii) `Tr e^{iX} = 2cos(ρ_X/2)` at N=2, `ρ_X² = k·k G`, modulus identity:
  **established identity** (sympy `strip_symmetry.py` 1a–1e; exact algebra).
- (iii) growth functional nonzero for every real `k ≠ 0` at every `u ∈ (0,1]`; joint zero set
  real dim 4; `u=1` coefficients: **established** (sympy, PASS 2a–3b).
  RHS divergence for real `k ≠ 0` and off the anti-Wick slice: **established derivation**
  (ray/strip argument in 053 reduced coordinates) **with the numerics as corroboration**; the
  coordinate strip bound is sketch-level rigorous (powers verified symbolically only in the
  dominant chart); flagged for the gatekeeper.
  RHS convergence on the anti-Wick slice: **conditional** on the 053 `k<14` window at N=2
  (which 053 proved there).
- (iv) LHS no-limit for non-real `k`: **conditional derivation** — exact on the two-branch
  Laplace model along the ray; the `e^{c_2(k)/ε}`-along-a-sequence statement ignores possible
  exact cancellation off the sequence (handled by the sequence); the ray is a locus of the full
  integral, so the bound transfers only via a tube argument (sketched: transverse polynomial
  weight). Classification: derivation with a stated gap at "tube" level, numerics not run for
  this piece (the mechanism is one-dimensional and exactly solvable).
- (v) domination failure for real `k ≠ 0` at every `u`: **established** (it is the divergence of
  (iii)); numerics `e^{c/√ε}`-type growth of the fixed-`ε` modulus: **numerical** (proxy,
  one-sided, slopes are window-limited lower bounds); non-existence of the real-`k` LHS limit:
  **unresolved** (not claimed).
- (vi) γ<0 extension to all `k ∈ C^{10}`: **conditional derivation** (chain in (vi)); the
  mass-sign identity: **established** (sympy 4a–4d); numerics: **numerical corroboration**.
- (vii) γ>0 `u=1` divergence at `k=0`; CNT definitional scoping: **established within the
  stated class** (sign identity + numerics; CNT comparison is definitional). CNT γ<0 plot gap:
  **unresolved** (053 text). Classicalization framing: **input** (cited paper).
- Overall no-go set statement ("identity holds for `O_k` exactly at `k = 0`"): **established
  within the hypothesis class** {N=2; γ=0; regulator (A); contour class (B) `R_u`; `ε→0⁺`
  last; `O = Tr e^{ik·A}`}, using (iii)+(iv) and 053 at `k = 0`.

## Proposed changes

Two edits, both in `chapters/appH-microscopic-proofs.tex`, Problem E section (after the 053
block, before its Status paragraph). No other file changes; no bib additions (both cited keys
already in `bib/namcg.bib`, verified by `apply_check.py`: `ChouNishimuraTripathi2025`,
`AsanoNishimuraPiensukYamamori2025`); no new `\label`s; the only `\ref` used is
`ass:lorentzian` (defined exactly once, in ch04).

### E1 — pure insert (new paragraph, no text removed)

Anchor (occurrence count 1 in the current file, verified byte-exact, CRLF): the blank line
before `\paragraph{Status.}` + CRLF + `Remains Assumption~\ref{ass:lorentzian}.`
(the `apply_check.py` anchor `ANCHOR_E1 = CRLF CRLF + "\paragraph{Status.}" + CRLF +
"Remains Assumption~\ref{ass:lorentzian}."`; the bare Status anchor alone also occurs exactly
once). Insert the paragraph of `appH_insert.tex` as its own paragraph between that blank line
and the Status paragraph; everything before and after is kept byte-identical.
The insert (LF form, 4364 B, sha256 52d390c623772453b68f8cf620ae1c727206e21ebf6cbf56fbfb1ac7c8833fcb;
CRLF form 4365 B, sha256 b453177e4c649d1c98cb12d11be3f17a4ca78e06d9bc73e6ee89318a3721a284):

```latex
\emph{Exponential observables \(\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\) at \(N=2\).} Let \(O_k(A)=\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\) with \(k\in\mathbb C^{10}\), at \(\gamma=0\), regulator (A), contours \(\mathcal R_u\) and \(\epsilon\to0^+\) last. For each fixed \(\epsilon>0\) and \(u<2/3\) the integral converges absolutely and is entire in \(k\), because on \(\mathcal R_u\) the growth of \(O_k\) is at most \(\mathrm e^{c(u,k)\|\tilde A\|}\) against a Gaussian regulator, and the fixed-\(\epsilon\) Stokes identity extends to it. At \(N=2\) the matrix \(k^\mu A_\mu\) has eigenvalues \(\pm\rho_X/2\) with \(\rho_X^2=k^\mu k^\nu\mathcal G_{\mu\nu}\), so \(O_k=2\cos(\rho_X/2)\) is branch-independent, and \(|2\cos(\omega/2)|^2=4(\cos^2(\operatorname{Re}\omega/2)+\sinh^2(\operatorname{Im}\omega/2))\). Along rank-one rays \(\tilde A_\mu=\rho_\mu H\), \(\operatorname{Tr}H^2=1\), the Euclidean weight at \(u=1\) is not exponentially damped and the Pfaffian vanishes on the ray and is polynomial in the coordinates nearby, so convergence is governed by powers of the reduced variables and the radius: in reduced coordinates the weight is polynomial times \(\mathrm e^{-\lambda e_2/2}\) with \(e_2\) bounded along the corner and no other damping along it (numerical, reduced coordinates), while \(|O_k|\ge\mathrm e^{b_u(\hat\rho;k)\rho}/4\) with \(b_u(\hat\rho;k)=|\operatorname{Im}(k^0\mathrm e^{-3\pi\mathrm iu/8}\hat\rho_0+k^i\mathrm e^{\pi\mathrm iu/8}\hat\rho_i)|\). At every \(u\in(0,1]\) the functional \(\hat\rho\mapsto\operatorname{Im}(k^0\mathrm e^{-3\pi\mathrm iu/8}\hat\rho_0+k^i\mathrm e^{\pi\mathrm iu/8}\hat\rho_i)\) is nonzero for every nonzero real \(k\) (at \(u=1\) its coefficients are \(-\sin(3\pi/8)k^0\) and \(\sin(\pi/8)\vec k\)), so the Euclidean side of the displayed limit identity diverges in modulus for every nonzero real \(k\); more generally it diverges for every \(k\) outside the slice on which \(k^0\mathrm e^{-3\pi\mathrm i/8}\) and all \(k^i\mathrm e^{\pi\mathrm i/8}\) are real, where \(|O_k|\le2\) and that side converges by the \(k<14\) Pfaffian window. For \(\operatorname{Im}k\ne0\) a commuting ray with \((\operatorname{Re}k\cdot\rho)(\operatorname{Im}k\cdot\rho)>0\) has \(S_{\mathrm b}=0\) and \(|O_k|\) of order \(\mathrm e^{b\rho}\) with \(b>0\), so the regulated Laplace integral at \(u=0\) grows like \(\mathrm e^{c_2(k)/\epsilon}\) along a sequence \(\epsilon\to0^+\), and \(I_\epsilon[O_k]\) has no finite \(\epsilon\to0\) limit for non-real \(k\). For real \(k\ne0\) the integrand at \(u=0\) carries \(|O_k|\le2\) pointwise, but no fixed-\(u\) domination in \(\epsilon\) is available at any \(u\in(0,2/3)\): the fixed-\(\epsilon\) modulus on \(\mathcal R_u\) grows without bound as \(\epsilon\to0\), numerically like \(\mathrm e^{c(k,u)/\sqrt\epsilon}\). Hence the displayed limit identity holds for \(O_k\) exactly at \(k=0\): there is no analyticity strip and no non-polynomial extension of the limit statement at \(\gamma=0\), within the hypothesis class \(N=2\), regulator (A), contours \(\mathcal R_u\), \(\epsilon\to0^+\) last. The obstruction is the massless flat direction, and at fixed \(\gamma<0\) it is absent: the mass contributes on \(\mathcal R_u\) the real exponent \((\gamma/2g_{\mathrm{YM}}^2)[\sin(3\pi u/4)\operatorname{Tr}\tilde A_0^2+\sin(\pi u/4)\sum_{i=1}^{9}\operatorname{Tr}\tilde A_i^2]\), a Gaussian damping on every component that dominates \(\mathrm e^{c(k)\|\tilde A\|}\) uniformly for \(\epsilon\le\epsilon_0<|\gamma|/(2g_{\mathrm{YM}}^2)\), and the displayed limit identity then extends to \(O_k\) for every \(k\in\mathbb C^{10}\) (numerical). At fixed \(\gamma>0\) the \(u=1\) integral diverges in modulus even at \(k=0\) (numerical), so the contour family and the thimbles of~\cite{ChouNishimuraTripathi2025} act on different contour integrals and produce no competing value; the classicalization of~\cite{AsanoNishimuraPiensukYamamori2025} is tied there to a Lorentz-breaking infrared cutoff and bears neither on this paragraph nor on the statements above. Everything in this paragraph is for the hypothesis class stated in it, does not address \(N\to\infty\) taken first, and derives no signature, real-time response, background or continuation; Assumption~\ref{ass:lorentzian} is not discharged. Problem~E remains open and PROGRAMME-CONDITIONAL.
```

Note on the insert phrase "polynomial times \(\mathrm e^{-\lambda e_2/2}\)": the 053 reduced
code path uses the exponent `i λ e^{4iπu/8} e2`, whose value at `u = 1` is `−λ e2`; the insert
writes the `u = 1` weight in the form the numerics use, `e^{−λ e2/2}` vs `e^{−S_E}`: overall
constant `λ` is the 053 reduced-action constant (its `2`-factor convention is inside the
"polynomial times exponential" phrasing — the claim used is only *bounded exponential factor,
no other damping along the strip*). If the gatekeeper wants the convention pinned, the phrase
can be checked against the 053 code (`ex` line) rather than changed.

### E2 — append one pointer sentence to the 053 closing paragraph (existing bytes kept)

OLD (exact bytes, occurrence count 1; 175 B, sha256 1ee39123b022a93f7750a9d6cd858a4d9a95a6a2b4ec4cc76310567eef1d181b):

```latex
or about non-polynomial observables such as \(\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\), which grow on \(\mathcal R_u\), so that the domination above fails for them.
```

NEW = OLD byte-identical + appended sentence (346 B, sha256 0d51660a0f6cfd8825c292181d7aa9616d9e315618ca2486171007a9b5830f5b):

```latex
or about non-polynomial observables such as \(\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\), which grow on \(\mathcal R_u\), so that the domination above fails for them. The next paragraph sharpens this at \(N=2\) and \(\gamma=0\): the failure occurs for every nonzero \(k\) in the contour class (B), and it is absent at fixed \(\gamma<0\).
```

All sentences before and after stay (the sentence "It does not exclude a real-time reading
obtained by continuation. …" and the Problem E status sentence stay untouched).

### Stale passages elsewhere

None. The 053 closing exclusion sentence stays true and is only pointed to (E2). Chapter 17
needs no change (no scope or status change). The Definition-(C) sentence "For \(\gamma>0\) no
contour is available and that case is not treated" (L1508) stays consistent with the new γ>0
sentence (different integral, different observable class).

### Expected applied outputs (pin table)

| file | before | after (CRLF-applied) |
|---|---|---|
| chapters/appH-microscopic-proofs.tex | 532576 B, sha256 `7a75554ef8cb7efe0e4c5cd3c53d6a9c4ffd2a9149e6ff29c7e8e067bb7f6aaa` | **537116 B, sha256 `88769063c0de114a8724bbadfdae25deba59ccc992e8f7f999bf38018ea55902`**, CRLF 3206, bare-LF 0 (= 532576 + 171 + 4369) |
| bib/namcg.bib | 25976 B, sha256 `a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b` | unchanged (pin preserved) |

Proposal-folder deliverable hashes (LF as written):

| file | size B | sha256 |
|---|---|---|
| appH_insert.tex | 4364 | 52d390c623772453b68f8cf620ae1c727206e21ebf6cbf56fbfb1ac7c8833fcb |
| apply_check.py | 4943 | 6e9a1acb85f487dcb29be0cca08cb31d6cc8719cbd232da8b91914335dbf8c2d |
| apply_check_r1.out | (rerun) | see file |
| n2_exp_mech.py | 9251 | a438fb8f04c597f66192cfd1d4259cb286909cd1598cc5a89c9f2a1a437653d5 |
| n2_exp_mech.out | 2085 | b19a134fc16951ee864248fe7e3de7a6b62558186b5aee6d7d493d231d08ae55 |
| strip_symmetry.py | 8547 | 96955a1dce6b47291cefa721ff8bd2c02657b676a7c0d46de5dedbf6cb4f452d |
| strip_symmetry.out | 1478 | 4db24e18e832a683b5bc0a46591b2553163e19d0d785a91be15ff51dc08be1f5 |
| build_check_r1.out | (final) | see file |
| proposal-r1.md | this file | — |

## Verification scripts

All in this folder, re-runnable (`python -I <script>`; numpy/scipy/sympy):

1. `strip_symmetry.py` → `strip_symmetry.out` (ALL PASS): (1a–1e) N=2 spectral identities
   (`X² = (z·z)/4·I`, `Tr e^{iX} = 2cos(ρ/2)` 40 dps err < 1e−25, modulus identity, rotation
   invariance); (2a–2e) growth-functional zero-set ranks (real dim 4; real-`k` rank 4 at
   `u = 1, 1/2, 1/4`); (3–3b) `u = 1` coefficients `(−sin(3π/8)k0, sin(π/8)k⃗)` and sign flip;
   (4a–4d) mass Re-exponent all-plus identity on `R_u`, `u = 1` coefficient `γ√2/(4g²)`,
   `u = 0` pure phase, regulator boundary `u = 2/3`. The 053 quartic/phase identities are NOT
   re-derived (053 gatekeeper verified them; noted in the .out).
2. `n2_exp_mech.py` → `n2_exp_mech.out`: 053 exact reduced N=2 integrand + one-sided masked
   `cosh` growth proxies (header documents proxy validity and the `ca`-only-at-`eps=gam=0`
   restriction). Exp 0 validation reproduces 053 `Z` and phase; Exp 1 RHS growth carriers
   (RHS divergence); Exp 2 mass-sign: γ=+0.2 diverges at bare `k=0`, γ=−0.2 converges with the
   growth proxy on (γ<0 domination), γ>0 divergence; Exp 3 fixed-`ε` modulus growth
   `e^{c/√ε}`-type at `u = 0.6/0.3` (fits 0.6526 and 0.9527 against reference slope
   `c√80 = 3.578`: window/grid-limited, quote as lower bound only).
3. `apply_check.py` → `apply_check_r1.out`: byte-level pins (appH 532576/7a75554e…; bib
   25976/a651fe60… both True), E2 OLD count 1, E1 anchor count 1, insert hashes, cite keys in
   bib, `ass:lorentzian` defined once, no labels introduced; `--copy DIR` applies into an
   out-of-repo copy and refuses second runs / the repository.
4. `build_check_r1.out`: out-of-repo build `C:/Users/redgi/tmp/p054r1_build_r3`: applied appH
   537116 B sha 88769063…, bib pin preserved; pdflatex → bibtex → pdflatex ×3 all exit 0;
   359 pages, 2661483 B (baseline 357); 0 undefined refs/citations, 0 multiply-defined,
   0 bibtex warnings/errors, no rerun flag; copy then removed. The file records (with hashes)
   the two superseded draft builds and why the insert text changed (unsupported exact constant
   `b²/32`; unproved "polynomially off it" clause).

## Decisions Taken

- **Included the secondary (CNT comparison) rather than deferring it**: it shares the primary
  derivation exactly (the mass-sign identity (4a) is the same sympy chain; the γ>0 `u=1`
  divergence is the `k=0` special case of the same modulus analysis). The CNT relation at γ>0
  is settled at the definitional level (different contour integrals); the γ<0 plot gap is left
  open, as in 053.
- **Dropped the exact constant `e^{b²/(32ε)}`** (first draft) → constant-free `e^{c_2(k)/ε}`:
  the constant depends on the unspecified ray-profile normalization; per rule 5 an unsourced
  number was removed, then the build re-run (build_check_r1.out NOTE).
- **Dropped the clause "at least polynomially off it"** (second draft): only the
  along-a-sequence statement is derived; "no finite limit" follows from the sequence alone.
- **Dropped an SO(10)-covariance argument** for the real-`k` divergence: the direct
  ray-functional argument covers every real `k` at every `u` without representation theory and
  is checkable (PASS 2c–e).
- **Restricted the `ca` (a-Fresnel-strip) proxy to `eps = gam = 0`**: with `ε > 0` or `γ < 0`
  the reachable `a`-radius is capped by the Gaussian width, so the proxy is not a lower bound
  there (it spuriously overflowed/diverged at γ<0 before the fix); the `cb` (large-radius) proxy
  is an honest lower bound for every nonzero real `k` at every γ and carries experiments 2–3.
- Kept the classicalization cross-check as the single scoped sentence the task allowed.
- Insert kept as ONE paragraph (status line once) rather than split, to mirror the 053 block's
  paragraph style and keep the scope sentence unique.

## Milestone assessment

Routine. No MILESTONE.md trigger: Problem E stays OPEN/CRITICAL PATH/PROGRAMME-CONDITIONAL; no
critical-path step closes; this is a bounded no-go inside a named hypothesis class plus a
bounded conditional extension for the massive deformation. It is a substantive negative result
on a listed open avenue (locating the missing ingredient at the massless flat direction and the
mass sign), not a milestone.

## Status-label recommendation

Re-derived current critical-path set from ch17 L394–399 vicinity and `reports/ledger.md`: A, B,
C, D1, E, F, G-derived, N (unchanged). Affected labels: **none**. Problem E remains
OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL (the insert states this verbatim). No
LABEL-CHANGE-PROPOSED note.

## Author decision needed

None.

## Remaining open step

To close the original target E: nothing here contributes a signature derivation; `ass:lorentzian`
stands. Ranked avenues (hypothesis each one relaxes):

1. **Real-`k` LHS limit, rigorous Abel/Fresnel treatment** (relaxes: presentation/truncation of
   the LHS side only). `lim_{ε→0} I_ε[O_k]` at real `k ≠ 0` is neither shown to exist nor to
   diverge; an improper-limit (stationary-phase/Fresnel) analysis of the oscillatory integral on
   the flat rays is the exact remaining computation. It cannot restore the identity (RHS
   divergent), but it decides whether the Lorentzian side carries a finite non-Euclidean value
   for exponential observables — directly relevant to the IR two-point programme, since
   `Tr e^{ik·A}` is the observable whose `k`-expansion generates all polynomial moments.
2. **CNT γ<0 plot reconciliation and γ>0 thimble mechanism at N=2 with fermions** (relaxes:
   the contour-class hypothesis (B) → thimble class). Their construction reaches absolute
   convergence at γ>0 by deforming off `R_u`; a comparison requires defining a shared
   invariant, none exists yet at γ>0; the γ<0 gap (053 L1508) is untouched.
3. **Uniform-in-`N` and `N → ∞`-first statements** (relaxes: the `N = 2` and the
   ε→0-last hypotheses): the flat-ray mechanism is N-independent in structure (rays of commuting
   matrices exist at every N; Pfaffian vanishing order on them needs the N≥3 analogue of
   `Pf = c_P(det G)^4`).
4. **Real-time/continuation reading** (relaxes: the presentation of the observable sector, keeps
   053's exclusion sentence's caveat): the 053 sentence "It does not exclude a real-time reading
   obtained by continuation" stays; the no-go here is about `O_k` inside (A)+(B), not about
   continued kernels.
5. **`N ≥ 3` independent Pfaffian bound** (053's own flagged reading-dependency, unchanged).
6. **Alternative presentations relaxing the regulator hypothesis (A)**: thimble/edge-mode/contact
   term variants of the regulator could in principle re-sum the flat directions; not explored —
   no evidence within (A) that they would change the γ=0 divergence, since the divergence is of
   the *Euclidean* side too (RHS), which is regulator-independent in 053's class.

## Special instructions for the gatekeeper

- Scope limits: the no-go is **only** for {N=2, γ=0, regulator (A), contours `R_u` (class (B)),
  `ε→0` last, `O = Tr e^{ik·A}`}; the γ<0 statement is **only** the massive-deformation identity
  extension; neither closes or narrows Problem E's status, and neither may be asserted as
  deriving signature, real-time response, or a continuum/infinite-N statement.
- Must re-check: (a) the mass-sign identity 4a **sign structure** (all-plus; a sign error here
  inverts the γ<0/γ>0 conclusions — sympy check included but re-derive); (b) the fixed-`ε`
  Stokes domination for `e^{c‖Ã‖}` against the regulator for `u < 2/3` and against regulator+mass
  for γ<0, `ε ≤ ε_0 < |γ|/(2g²)` (the `u=1` `Ã_0` coefficient `ε√2/2 − |γ|√2/(4g²)`);
  (c) the rank computations 2a–2e (zero sets of `v_u`); (d) the **one-sidedness** of the cosh
  proxies (they carry divergence evidence only, never boundedness) and the `ca`-proxy
  restriction to `eps=gam=0`; (e) the "along a sequence" qualification on the
  `e^{c_2(k)/ε}` Laplace statement (phase cancellation of the two branches at isolated ε);
  (f) that the Exp3 fit slopes (0.6526, 0.9527 vs reference `c√80 = 3.578`) are window/grid-
  limited lower bounds — the insert phrases this as "numerically like e^{c(k,u)/√ε}", which is
  the claim the numerics support (unboundedness, not the exponent).
- The E2 edit appends a sentence without touching any existing byte (OLD is a strict prefix of
  NEW); the 053 closing paragraph's scope sentences all remain. If the full-scan rule (c) of
  CLAUDE.md is judged triggered (it arguably is, since a scope sentence of the 053 block gains
  an appended sentence), the scan must still find the 053 statements byte-identical.
- Do not assert "the identity fails for all k ≠ 0" without the hypothesis class — for other
  contour classes (thimbles) the question is open (avenue 2).
- `scratch/digest.md` was DIGEST CURRENT at the time of writing with `dirty-chapters: yes`;
  pins above are against the working tree (532576 B appH), not HEAD.
