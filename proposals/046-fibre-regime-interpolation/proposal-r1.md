# Proposal 046-fibre-regime-interpolation, round 1

## Result

This package computes the regime interpolation that 045 left as an argument, for CP^{1,2} (finite fibre) × K at the IKKT content, at the frozen leading symbol. Main finding: within the computations, no open range of the K scale gives a single Einstein coefficient on the five traceless level-one polarisations with c_A = c_T. Isolated tuned values of the K data are not excluded; they would lie where the fibre trace dominates. The two readings of 045 are the two ends of an exact interpolation, but the end where the averaged frame would hold lies outside the control of the expansion that produces the averaged-frame forms.

**(a) Loop fibre spectrum.** Established exactly, plus a numerical orbit identity.
- Lie–Poisson identities: □t = −3t and □(tt) = −6tt + 2ηMM. On the orbit, ηMM = c_θ η + yy − tt.
- Hence on the fibre over a base point, −□(C·t^J) = J(J+2) C·t^J for C transverse to y and traceless on y^⊥.
  - Checked for J = 1, 2, 3 at two base points, one with y^i ≠ 0; residual ≤ 8e-16.
  - The fibre levels are μ_J = J(J+2) (R = 1). They agree with Steinacker's m_s² = 3s (2303.08012, eq. (7.5)) at J = 1 and exceed it for J ≥ 2. The two are not reconciled here.
- The base–fibre cross term 2η{T,φ}{T,Y} preserves J. Its closed form at y^i = 0 has singular values (2m/|y⁰|)·√((y⁴q₀J)² + (ℓ|q⃗|m_L)²); Monte Carlo agreement is within 4%. It is O(1) relative to the kinetic and gap terms when m|q| ~ J. As in 045 (H6), it is dropped.

**(b) Duhamel weights and the interpolation.** Exact within the hypotheses.
- *Index vertex.* Its weight is ∫₀¹ e^{−sΔa} da.
- *Scalar vertex (−∂γ∂).* The q² part is ∫ e^{−sΔa}[a(1−a)F₁ + (1−2a)²F₂], with F₁ and F₂ explicit.
  - Checked against an independent Isserlis computation in both signatures.
  - At Δ = 0 it reproduces 4× the 045 scalar density exactly in both signatures (the calibration constant is 1/4).
- *Fibre coupling.* (2J+1)·⟨J0 20|J′0⟩².
- *Resulting forms.*
  - Index: W_X^(0)·IX₁ + W_X^(2)·(IX₂ − IX₁).
  - Scalar: W_R^(0)·SC₁ + W_R^(1)·L₁ + W_R^(2)·L₂, with L₁ + L₂ = SC₂ − SC₁ exactly at 7 cases, and L₂ ≡ 0 on the five traceless polarisations.
- *Cone.* It carries only the diagonal weight. So the mixed-term part of the fixed-state gap on the generalised eigendirections of the five is −W_X^(2)(λ_i + 2).
- *The form therefore interpolates exactly between 045 (ii) and 045 (i).*
- **New regime fact.** Fibre levels are suppressed only by a power. Each level contributes ≈ (2J+1)τ₂/μ_J, because τ^K ≈ τ₂s² at small s. The transitions J → J are degenerate.
  - Consequently β_X = W_X^(2)/W_X^(0) is small only if M·Σ_{J≥1}(2J+1)/μ_J ≪ 1 and M ≪ μ₂ = 8, where M is the K scale in □ units.
  - β_X → 1 as n → ∞ at any fixed M; the sum grows as 2 ln n.
  - Numbers for τ^K ∝ s²e^{−sM}, n = 30: β_X = 0.065, 0.40, 0.86 and 0.96 at M = 0.01, 0.1, 1 and 8. With 3J levels: 0.19, 0.69, 0.94, 0.97.
  - The half-spread on the five is 2.42·β_X about −2.
  - **This corrects 045's uncomputed argument** that the full trace approaches the averaged forms "when the fibre gaps exceed the scale of K".

**(c) Background torsion and the first term.** Computed at first order, then a window analysis.
- *Background torsion.* CP^{1,2} has T̄^{abμ} = η^{aμ}y^b − η^{bμ}y^a, with size coth τ in □ units, and coth²τ ≥ 1 on the leaf. It enters the flux operator of every species.
  - For fibre-constant loop modes at frozen coefficients, σ^M = N(s)⟨tr e^{−sZ(k)} − dim⟩_k exactly.
  - Q₁^D = m⁴·IX₁ to machine precision at 10 points. So for J = 0 modes the Dirac index density is the torsion invariant of the averaged frame; this removes 045's carried-over identification for that sector. Also Q₁^V = 2Q₁^D.
- *Computed second-order parts.*
  - Q₂^D: the mixed-term correction at flux order (4,2), relative size s·coth²τ.
  - P₂ = Q₂^V − 2Q₂^D: the first term s0^K(v^M − 2σ^M) at order four (pure M, base torsion), with log weight ∫ds s⁻¹ s0^K.
- *Exact structure.* On the five traceless polarisations at 7 points:
  - IX₂ − IX₁, Q̂₂ and P̂₂ lie in span{EH, one form}, with P̂₂ = −6Q̂₂ mod EH and IX₂ − IX₁ = λQ̂₂ mod EH, where −3.31 ≤ λ ≤ −0.32 (residual < 1e-11);
  - one double eigenvalue of Q̂₂ relative to EH equals (3/2)coth²τ;
  - the scalar leak L₁ is not in this span.
- *Window analysis.*
  - Where β_X is small (M·Σ ≪ 1), the torsion parameter is coth²τ/M ≫ coth²τ·Σ ≥ 1.
  - So the order-(2,2) forms behind the averaged-frame c_T = W_R/6 − 2W_X and c_A − c_T = 0 are not the leading result there.
  - Where the torsion expansion holds (M ≫ coth²τ), β_X ≈ 1 and the trace reading applies.
  - At first order in torsion, with the first-term log weighted by L/c (a parameter), the non-Einstein coefficient of the index sector has one zero M*. At base (5,3), q₁, n = 2..300:
    - for L/c = 0: M* ∈ [0.21, 0.67] with coth²τ/M* ≥ 4.2, outside control;
    - for L/c = 1, 10: M* ∈ [1.1, 30] with β_X = 0.52–0.97, i.e. a cancellation between the fibre-trace leakage and the first-term torsion term, in the trace regime.
  - L comes from K-zero modes, whose torsion expansion is not controlled at large s.
  - A single coefficient there would also need the scalar L₁ coefficient W_R^(1) to vanish and the cone to match at the same order (not computed). That is codimension ≥ 2 in the K data, not a window, and not the averaged-frame result.
  - The S²–M fibre-flux first-term part is estimated by power counting only (per level ~ J²/μ_J) and is not computed.

**Breakthrough self-assessment.** A single matrix-derived Einstein coefficient with G_A = G_T is **not** obtained in any computed regime of a rank-6 class.

## Target and status

**Problem F** (`sec:status-F`, appH L1366), verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- Ch17 target (`sec:ch17-done` item 6): A, B, C and the sign/scheme dependence of G_eff, computed from the specified operators.

**Problem B** (L45): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- Ch17 target: Assumption EE as a lemma, including the non-conformal tensor block.
- Sub-target used here: G_T = G_A (normalisation paragraph, L174–179).

**Critical-path set** (`sec:ch17-done`): A, B, C, D1, E, F, G-derived, N. Appendix H agrees; no discrepancy.

**Dependencies:**
- F depends on D1, E and the class.
- B depends on A (replica/state) and F.

**Classification:** PROGRAMME-CONDITIONAL; nothing DERIVED.

## Source reading

**Full scan.** `make_digest --check` printed DIGEST CURRENT with dirty-chapters: yes, so CLAUDE.md 3(d) applies.
- I read every file of the 30-file manifest: ch01–ch18, appA–appG, appI–appL, and appH L1–2907 in ranges.
- Some of ch12–ch16 and the appendices were read via `cat` with blank lines stripped.
- The dirty diff is the accepted 043/044/045 integrations, the ch07 ξ fix and the Chen2022 bib entry.

**Also read:**
- 045 r1, r2, review-r1, review-r2 and scripts (forms_lib, cp12_realisation, s1, s2, s4);
- 044 r1 (to §3), r2 and the review avenue lines; the s1 header;
- `reports/sme-scout-20261025.md` (full);
- `proposals/strategy-20261025/assessment.md` (§0–1).

**Steinacker 2303.08012:** PDF fetched and pdftotext-extracted. Read §7 through §7.2.2, including (7.1)–(7.5), §7.1.2 (7.10)–(7.14), (7.18) and (7.21)–(7.33).

No unreadable files.

## Research and reasoning

### Hypotheses
- **H1–H9 of 045:**
  - product M × K, no mixed flux;
  - IKKT content supplied;
  - Poisson limit on M;
  - one loop;
  - frozen leading symbol at y^i = 0;
  - hybrid fibre treatment;
  - 044 cone values;
  - orientation-even mixed term;
  - formal η.
- **Inert amplitudes set to zero** (not eliminated).
- **H10.** Fibre levels from −□ at zero base momentum. The cross term is dropped, though shown to be J-diagonal and O(1) at m|q| ~ J.
- **H11.** Commutative Clebsch–Gordan coefficients with truncation at J ≤ n (the semiclassical fuzzy fibre).
- **H12.** The torsion correction is evaluated for J = 0 loop modes only. It is first order in T̄².
- **H13.** Single-scale K model τ^K = F²s²e^{−sM} (and v^K − τ^K of the same shape), used for the quoted numbers. The structural statements (power-law level weights, β → 1 as n → ∞) need only τ^K ~ τ₂s² at small s.

### (a) Spectrum
- s1 (E1–E3) are exact polynomial identities, for both bracket signs.
- (N1) is ηMM = c_θη + yy − tt at 40 orbit points.
- (N3) gives Box(C·t^J) = −J(J+2)C·t^J. The derivation is that each pair of t-factors contributes −2(tt) from the −tt part of ηMM, giving −3J − J(J−1) = −J(J+2). The c_θη and yy parts vanish on traceless transverse C.
- The cross term (N4) is i·(J-Euler part) plus the (q⃗·L) part. Hence it is J-preserving, with the singular values quoted.

### (b) Interpolation
- **Second-order trace.** It is (s/2)∫₀^s du Tr[V e^{−uH} V e^{−(s−u)H}].
- **Scalar part.**
  - Shift k = p − aq. The exponent is −s pγ̄p − s a(1−a) qγ̄q exactly.
  - Gaussian moments then give I₂ = N/s·[a(1−a)F₁ + (1−2a)²F₂]. This is verified symbolically by Isserlis with random rational data, in both signatures.
  - The weights are m₁(x) = ∫a(1−a)e^{−xa} and m₂(x) = ∫(1−2a)²e^{−xa}, in closed form and checked by quadrature.
- **Index part.** δT ∝ q² already, so the k-moment ⟨kk⟩ at q⁰ suffices and the weight is m₀.
- **Fibre algebra.** Wigner–Eckart gives Σ_{mm′}|⟨J′m′|Y_{2M}|Jm⟩|² = (2J+1)/(4π)·c(J,J′). The closed forms of c are checked against sympy CG.
- **K weighting.** The sums have the closed form W₁ = Σ(2J+1)/(M+μ_J) and β_X via ln-weights. They are checked against quadrature in s4.

### (c) Torsion
- **Model.** H = −□ + κΣ^{ab}𝒵_ab with κ = −1. Σ_V and Σ_D are normalised so that tr_V ΣΣ = 2 tr_D ΣΣ, matching the merged operators.
- **Series.** Z(k) = κiΣ·T(k) commutes with the kinetic symbol at frozen coefficients, so tr e^{−sZ} is expanded and averaged with ⟨kk⟩ = G/(2s) and ⟨kkkk⟩ = (GG+GG+GG)/(4s²). This gives Q₁ = ¼G tr ZZ and Q₂ = (1/96)Σ_{pairings} tr ZZZZ.
- **Quadratic part.** Q₂'s part quadratic in δT₀ is extracted by polynomial interpolation in the amplitude.
- **Weights.**
  - Mixed term: Γ ⊃ (1/128π²)[Q₁∫s⁻²τ + Q₂∫s⁻¹τ].
  - First term: Γ ⊃ −(1/32π²)P₂∫s⁻¹s0^K.
- **Window inequality.** With W₂/W₁ ≈ 1/M at J = 0 dominance and Σ_{J≥1}(2J+1)/μ_J ≥ S₁ = 1, smallness of β_X forces coth²τ/M ≫ 1.

### Fork: hypotheses of the bounded no-go and relaxations

The no-go rests on:
- H1–H13;
- the inert amplitudes set to zero;
- the level-one graviton;
- the leading symbol.

| Hypothesis | Relaxation | Explored here? / outcome |
|---|---|---|
| H12 first-order torsion | resum T̄ exactly (Gaussian k-integral of tr e^{−sZ}, Euclidean section) | not done; would decide the sign of the non-Einstein coefficient at small M |
| H10 cross term dropped | include the J-diagonal (q⃗·L, J) cross term in the level weights | closed form obtained (s1); weights not recomputed; expected O(1) change and still power-law |
| inert = 0 | Schur-eliminate the inert amplitudes with the tree Maxwell forms (merged L2162 window) | not done (045 avenue 2) |
| fibre-flux first term | compute S²–M on J ≥ 1 levels | power counting only |
| product background / no mixed flux | K flux varying along the fibre (equivariant K) so that fibre and K fluxes mix | not explored |
| level-one graviton | graviton from J = 2 or mixed hs modes | not explored |
| cone values | cone corrections at order s·T̄² | not computed |
| presentation | five-matrix presentation M^{A5} (self-dual flux, f₁ = f₂) | not explored |

**Ranked open avenues:**
1. Decide the tuned point. This needs:
   - an exact Gaussian resummation of the background torsion in the J = 0 sector (Euclidean section) as a function of M;
   - the K-zero-mode first term beyond first order in T̄ (its log L);
   - the scalar leakage coefficient W_R^(1);
   - the cone at the same order.

   Whether all non-Einstein coefficients and c_A − c_T vanish simultaneously at some K data is a K-tuning question, not a window.
2. Schur elimination of the inert amplitudes and of the J = 2 levels (045 avenue 2).
3. S²–M fibre-flux part on J ≥ 1 levels with the cross term.
4. Equivariant K (mixed M–K flux) as the mechanism that could suppress the fibre-level tail.
5. The trace polarisation and Problem C, as an open question.
6. Non-product backgrounds and other presentations.

## Claim classification

| # | Claim | Class |
|---|---|---|
| 1 | □t = −3t and □(tt) = −6tt + 2ηMM | established (exact polynomial identity) |
| 2 | ηMM = c_θη + yy − tt on the orbit | established numerically (40 points, 1e-15) |
| 3 | μ_J = J(J+2) on fibre harmonics | established (from 1 and 2; numerical check at 2 base points) |
| 4 | Disagreement with (7.5) for J ≥ 2 | established (comparison); reason not reconciled |
| 5 | Cross term J-diagonal, with closed-form singular values | derivation plus Monte Carlo check (4%) |
| 6 | Duhamel weights m₀, m₁, m₂; scalar kernel F₁, F₂; calibration 1/4 | established (symbolic and exact) |
| 7 | Interpolation formula for the index and scalar forms; L₁ + L₂ = SC₂ − SC₁; L₂ = 0 on the five | established at the frozen symbol under H10–H11 (exact at 7 cases) |
| 8 | Mixed gap on five = −W_X^(2)(λ_i + 2) | conditional (044 cone values; cone diagonal) |
| 9 | Power-law level weights; β_X → 1 as n → ∞ | established given τ^K ~ τ₂s² at small s (H10, H11) |
| 10 | β_X numbers | numerical, single-scale model (H13) |
| 11 | Correction of 045's regime argument | established within H10–H11 |
| 12 | Q₁^D = m⁴IX₁ (J = 0 index density is the torsion invariant) | established at the frozen symbol (10 points, machine precision) |
| 13 | Span structure; P̂₂ = −6Q̂₂ mod EH; λ range; (3/2)coth²τ | numerical-exact (residual < 1e-11 at 7 points); not proved |
| 14 | No open window for the averaged-frame result (torsion parameter ≫ 1 where β small) | conditional (first-order torsion, J = 0, H10–H13) |
| 15 | M* ranges: L/c = 0 → [0.21, 0.67], coth²/M* ≥ 4.2; L/c = 1, 10 → [1.1, 30] with β_X 0.52–0.97 | numerical, model, base (5,3); L/c is a free parameter |
| 15b | Tuned isolated K data could give a single coefficient on the five | conjecture, not excluded; needs W_R^(1) = 0 and a cone match (uncomputed) |
| 16 | S²–M per-level weight ~ J²/μ_J | conjecture (power counting) |
| 17 | No G_eff value, no closure | unresolved |

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`

**Placement.** Insert `proposals/046-fibre-regime-interpolation/appH_insert.tex` (10683 bytes: ASCII, LF, 0 CR, 0 TAB) as one paragraph:
- immediately after the 045 paragraph, whose last sentence is "...or bear on Assumption~\ref{ass:lorentzian}. Problems~B and~F remain open and PROGRAMME-CONDITIONAL.";
- immediately before the unique line `\section{Problem G: HBEV}`, with one blank line before the anchor.

The anchor is unique, and the preceding line is the 045 closing (s5). Nothing is replaced. The integrator converts the file to CRLF.

**Checks (s5):**
- refs `sec:status-B`, `ch:vierbein-emergence` and `ass:lorentzian` each occur once;
- cite `Steinacker2023` is present;
- no `\label`, one `\paragraph`;
- braces and math delimiters balanced;
- no title collision;
- no process language.

```latex
(see appH_insert.tex, authoritative byte-exact copy; reproduced below)
```

The text is identical to `appH_insert.tex`. The reviewer should read that file directly.

**Prior-claim note (soft PRIOR-CLAIM-ERROR).** The merged 045 sentence "The full trace approaches them when the fibre gaps exceed the scale of \(K\), since intermediate states in the second harmonic are then suppressed in the proper-time integral; this is an argument and is not computed." (one occurrence, checked) is incomplete:
- the higher fibre levels are suppressed only by powers of μ_J;
- the condition is M·Σ_{J≥1}(2J+1)/μ_J ≪ 1, which fails in the Poisson limit.

Decision: no edit to the merged text. The sentence is labelled there as an uncomputed argument, and the new paragraph states the correction explicitly ("The argument of the preceding paragraph ... is therefore incomplete: ..."), with "correction of a regime argument" in its title, following the merged correction pattern (L2352, L2361). If the gatekeeper prefers an in-place edit, the exact replacement is:
- old: `The full trace approaches them when the fibre gaps exceed the scale of \(K\), since intermediate states in the second harmonic are then suppressed in the proper-time integral; this is an argument and is not computed.`
- new: `Whether and when the full trace approaches them is computed in the following paragraph.`

**Stale passages.** None besides the above.
- 044's "The first term has no two-derivative part" is scoped to the four-coordinate class, where T̄ = 0, and remains true.
- 045's "identification carried over ... not recomputed" is now confirmed for J = 0 modes. The new paragraph says so ("on these modes the index density is the torsion invariant of the averaged frame"); no edit is needed.

**BibTeX.** None new.

## Verification scripts

All are in `proposals/046-fibre-regime-interpolation/`, with saved `.out.txt`. `forms_lib.py` and `cp12_realisation.py` are copied from 045. The `s*.err` files are stderr warnings from quad/overflow and are harmless.

- **`s1_fibre_spectrum.py`** (~1 min):
  - (E1–E3) exact identities for both bracket signs;
  - (N1) θθ identity;
  - (N2–N3) μ_J at 2 base points;
  - (N4) cross term and its closed form.
- **`s2_duhamel_interpolation.py`** (~1.5 min):
  - CG coefficients;
  - Isserlis check of the scalar kernel;
  - calibration 1/4 against forms_lib.scalar_form;
  - l = 2 forms at the 7 045 cases (consistency L₁ + L₂ = SC₂ − SC₁; eigenvalues);
  - moment functions;
  - K-weighted β tables for both spectra;
  - spread on the five.
- **`s3_background_torsion.py`** (~1.5 min):
  - Clifford and representation checks;
  - Q₁ = m⁴IX₁;
  - Q₂^D and P₂ eigenvalues on the five at 10 base/q cases;
  - coth² scaling.
- **`s4_window_scan.py`** (~1 min):
  - analytic K-sums against quadrature;
  - (S) span test of L_X, P₂, L₁, SC₂ − SC₁ against {Q̂₂, EH};
  - (N) non-Einstein coefficient, sign change, M* and expansion parameters.
- **`s5_insert_mechanics.py`** — bytes, refs, cites, anchor, title, process language, presence of the corrected 045 sentence.
- **`compile_check.py`** — scratch build of the CURRENT working tree outside the repo:
  - baseline 323 pages, with the insert 325 pages;
  - exit codes 0; 0 undefined references, 0 undefined citations, 0 multiply defined labels;
  - CRLF preserved; scratch removed.

## Decisions Taken

1. **Spectrum discrepancy with (7.5).**
   - Decision: report μ_J = J(J+2) as derived, and give the β tables for both J(J+2) and 3J so that the conclusions do not depend on the discrepancy.
   - Rejected: adopting 3J by citation.
2. **Index measure of "single coefficient".**
   - Decision: use the spread of the generalised eigenvalues on the five, together with an explicit span test, which is basis-free.
   - Rejected: a scalar "minimum deviation" scan. It was computed first and showed accidental cancellations between non-Einstein structures; that motivated the span test, which identifies one common non-Einstein form.
3. **Torsion correction scope.**
   - Decision: first order and J = 0 only, stated as such.
   - Rejected: claiming the sign change at M* as a window. The zero is an isolated tuning (one condition on L/c and M per sector), and the first-term log L is not controlled.
   - An initial s4 run used the wrong factor (1/λ_P instead of λ_P) for the first-term contribution. It was corrected (λ_P = −6) before submission; the saved output is the corrected one.
4. **045 sentence.** Corrected in the new paragraph, not edited in place; an optional replacement string is given.
5. **Cone at torsion order.** Not computed. The c_A = c_T statement in the window is therefore phrased via the forms that the averaged result rests on, not via a computed gap.

## Milestone assessment

**Routine; no milestone.**
- M2 is a weak candidate only. This is a bounded no-go within H1–H13 for the CP^{1,2} × K level-one route at second order in the K flux. The avenues above (exact torsion resummation, inert elimination, equivariant K) remain open, so the 044/045 review standard for M2 is not met.
- Not a breakthrough.

## Status-label recommendation

None. B and F remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. The critical-path set is A, B, C, D1, E, F, G-derived, N.

## Author decision needed

None.

## Remaining open step

For a single matrix-derived Einstein coefficient with G_A = G_T in a rank-6 class:
1. resum the background torsion (or find the leading-order structure at M ~ coth²τ) together with the cone at the same order;
2. eliminate the inert and J = 2 amplitudes;
3. compute the S²–M fibre-flux part;
4. alternatively, find a background (equivariant K, mixed flux) in which the fibre-level tail and the background torsion are both suppressed relative to the K scale;
5. fix the trace polarisation, K and the sign of W_R, and the replica (Problem A), with derived signature (Problem E).

## Special instructions for the gatekeeper

- **Do not assert:**
  - any window or K-tuned point as an Einstein result;
  - that 3J is wrong (only that J(J+2) is derived here and the two are not reconciled);
  - that S²–M is computed;
  - that the "(3/2)coth²τ" double eigenvalue is helicity two (not identified);
  - any closure.
- **Re-check:**
  - s1 (E2) and (N3) for J = 2 (−8);
  - s2 calibration 1/4 and L₁ + L₂ = SC₂ − SC₁;
  - s3 Q₁^D = m⁴IX₁;
  - s4 span residuals and P̂₂ = −6Q̂₂ (a = −6.000);
  - the window inequality (Σ_{J≥1}(2J+1)/μ_J ≥ 1 for n ≥ 1).
- **Runtimes:** about 1–1.5 min each; compile 25 s.
