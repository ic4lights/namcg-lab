# Proposal 054-055-r2 (gpu line, combined 054 + 055), round 3

Review addressed: `review-r2.md` in this folder (AWRR, one MAJOR PRIOR-CLAIM-ERROR, five minor). The r2 files are kept
unchanged. The r3 texts are `E1_053_sentence.r3.tex`, `E2_insert_054_055.r3.tex`, `E3_056_adjusted.r3.tex` and
`E4_057_adjusted.r3.tex`, all CRLF. `build_r3.py` produces them from the r2 files and asserts that each replacement
occurs exactly once.

## Result

- **Finding 1 (MAJOR, PRIOR-CLAIM-ERROR) is confirmed and corrected.**
  - The soft-mode exponents carried from 057 into 055 were a factor 2 too small relative to Definition (A).
  - The cause: `Tr(a sigma^3/2)^2 = a^2/2` was not carried into the Gaussian coefficient `Q`.
  - In Definition (A), `Q = (1/2) e^{-3 pi i u/4}(eps - i gamma/(2 g_YM^2))`. With it the exponents are:
    - frozen coefficient: `r0^2 cos(3pi u/4 - pi/4)/(8 eps)` at `gamma = 0`, and `g^2 r0^2 sin(3pi u/4 - pi/4)/(4|gamma|)` at fixed `gamma < 0`;
    - contour-dependent coefficient: `r0^2/(8 sqrt2 eps)` at `gamma = 0`, and `-g^2 r0^2/(4 sqrt2 |gamma|)` at fixed `gamma < 0`.
  - All four are re-derived here and checked by sympy and by quadrature.
  - None of the qualitative statements changes: u-independence, a constant below one at fixed `gamma < 0`, and the
    frozen-model artefact.
- **The reduced-model numbers: option (i), conversion to Definition (A).** The normalisation of the reduced code is
  fixed by matching the exponents symbolically, as explicit 2x2 matrices. The code variables `a_k` are Pauli
  components, and the code is Definition (A) at `g_YM^2 = 1/2`, with `eps_A = 2 eps_code` and `gamma_A = gamma_code`.
  This solution is unique. The quoted numbers become:
  - the ladder end, `eps = 3e-3` -> `6e-3`;
  - the exact-insertion threshold, `eps >= 0.1` -> `0.2`;
  - the corner value, `0.044/eps` -> `r0^2/(8 sqrt2 eps) ~ 0.088/eps`;
  - the 054 proxy range, `eps in [0.01,1]` -> `[0.02,2]`;
  - `gamma = -0.2, -0.05`, unchanged.
  - The ratios and the fit slope are also unchanged.
- **Minor findings 2, 3, 4 and 6** are applied verbatim as snippets (d), (e), (f) and (g). In (f) the proxy range is
  converted to the units of Definition (A).
- **Finding 5:** every difference between the moved correction and the original 057 text is disclosed below.
- **Status.** Nothing derives a signature or changes a label. Problem E remains OPEN, CRITICAL PATH for the
  matrix-derived label, and PROGRAMME-CONDITIONAL.

## Target and status

- **Problem E (signature).** In `chapters/appH-microscopic-proofs.tex`, `\section{Problem E: signature}`, the
  ledger reads "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion:
  PROGRAMME-CONDITIONAL."
- **Chapter 17.** ch17 L394-399 and the completion list at L718-719 agree with Appendix H: "Problem~E: Lorentzian
  signature is derived rather than retained (Assumption~\ref{ass:lorentzian})". There is no discrepancy. I
  re-checked them this round.
- **Original target.** Lorentzian signature derived, not retained.
- **Critical-path set** (full-GR / matrix-derived scope): A, B, C, D1, E, F, G-derived, N.
- **This package.** It is a bounded sub-lemma and obstruction at `N=2`. It is PROGRAMME-CONDITIONAL: `eta`, the
  fermion content and the regulator are supplied. Its dependencies are unchanged from r2.

## Source reading

- **Mode.** Digest + targeted reads. `python scripts/make_digest.py --check` gives `DIGEST CURRENT`, with
  `dirty-chapters: yes`.
- **Tree state.** The appH sha256 is `6a83d79e...`, identical to r2, so no tree change has occurred since r2.
- **Read this round.**
  - Definition (A): appH L1523, in full.
  - The linear-contour regulator paragraph: L1579.
  - The code paths of `055-*/n2_slice_r1.py`, `055-*/slice_ray_r1.py` and `054-*/n2_exp_mech.py`, for the
    normalisation.
  - The r2 snippets and the gpu source of 057.
- **No full scan.** As in r2, the dirty hunks (appH Problem A, the Problem I region, ch14 L227) do not overlap
  Problem E. The full scan the gatekeeper owes before a final ACCEPT is the gatekeeper's own obligation.

## Research and reasoning

### 1. Factor-2 correction, re-derived

All steps are in `check_r3.py`, (2g)-(2i).

1. **Definition (A) on `R_u`.** The integrand factor is `e^{iS_b + iS_gamma - eps sum_mu Tr A_mu^2}`, with
   `A_0 = e^{-3 pi i u/8} A~_0`. Take the soft temporal mode `A~_0 = a sigma^3/2` (Pauli component, the convention
   `A = sum_a A^a sigma^a/2` of the ledger). Then `Tr A~_0^2 = a^2/2`.
   - The regulator gives `-eps e^{-3pi i u/4} a^2/2`.
   - The mass gives `i S_gamma = -i gamma/(2g^2) Tr A_mu A^mu`. Its `mu = 0` part, with `eta^{00} = -1`, is
     `+i gamma e^{-3 pi i u/4} a^2/(4 g^2)`.
   - Together they give `e^{-Q a^2}` with `Q = (1/2) e^{-3pi i u/4}(eps - i gamma/(2g^2))`. This is check (2g); the
     trace is computed, not assumed.
2. **The insertion.** `k^0 A_0` with `k^0 = e^{3pi i/8} r0` has eigenvalues `+- e^{3pi i(1-u)/8} r0 a/2`, so
   `O_k = 2cos(gamma_c a)` with `gamma_c = e^{i phi} r0/2`. Here `phi = 3pi(1-u)/8` for the contour coefficient and
   `phi = 3pi/8` for the frozen model.
3. **The branch integral.** It is `2 sqrt(pi/Q) e^{-gamma_c^2/(4Q)}`, valid for `Re Q > 0`. Its exponent is
   `Re[-gamma_c^2/(4Q)]`.
   - **Contour, `gamma = 0`.**
     `-gamma_c^2/(4Q) = -e^{3pi i(1-u)/4} r0^2/4 / (2 e^{-3pi i u/4} eps) = -e^{3pi i/4} r0^2/(8 eps)`, so the
     real part is `r0^2/(8 sqrt2 eps)`.
   - **Contour, fixed `gamma = -|gamma|`, `eps -> 0`.** `4Q -> i e^{-3pi i u/4} |gamma|/g^2`, so
     `-gamma_c^2/(4Q) = i e^{3pi i/4} g^2 r0^2/(4|gamma|)`. Since `Re(i e^{3pi i/4}) = -1/sqrt2`, this gives
     `-g^2 r0^2/(4 sqrt2 |gamma|)`.
   - **Frozen, `gamma = 0`.** `Re[-e^{3pi i(1+u)/4}] r0^2/(8 eps) = r0^2 cos(3pi u/4 - pi/4)/(8 eps)`, since
     `-cos(x + pi) = cos x` with `x = 3pi u/4 - pi/4`.
   - **Frozen, fixed `gamma < 0`.** `g^2 r0^2 sin(3pi u/4 - pi/4)/(4|gamma|)`, by the same shift.
4. **Independent checks.**
   - `gk_normcheck_r2.py`, run with `python -I`, gives four zeros and `|I| = 7.41732077747273` against the
     predicted `7.41732077747273` (the stated value was `6.6667`). The output is in `gk_normcheck_r2.rerun_r3.out`.
   - `check_r3.py` (2h): the quadrature of the 1D integral matches the closed form at four points
     `(u, eps, gamma) = (0, 0.7, 0), (0.4, 0.5, 0), (0.4, 0.3, -0.3), (0.6, 0.2, -0.2)`, with relative error
     `< 1e-23`.
5. **Consistency with the modulus bounds (new check (2i)).** At `u = 0` the signed exponent `1/(8 sqrt2) = 0.0884`
   lies below the sharp modulus exponent of the same 1D integrand, `sin^2(3pi/8)/8 = 0.1067`. That modulus exponent
   is `max_a [sin(3pi/8) r0 a/2 - eps a^2/2]`. This is as it must be, since `|int| <= int |.|`.
   - The 056/057 constants `c0(u)` and `Gamma0(u)` use the HS-normalised `H` (`Tr H^2 = 1`) and the non-sharp bound
     `|O_k| >= e^{b rho/2}/(2 sqrt2)`. They are unaffected by the factor 2, and they stay valid as lower bounds.

### 2. Normalisation of the reduced code (option (i))

**Why option (i) rather than (ii).**
- Option (ii) was to confirm that the `a_k` are Pauli components, then apply (c). Snippet (c) states only that the
  code's soft-mode `Q` is twice the `Q` of Definition (A) at `g_YM = 1`. That statement is true (check (C1b)), but it
  is incomplete as a normalisation.
- The code also fixes the quartic coupling, at `LAM = 0.5`. For Pauli components the quartic term of Definition (A)
  is `S_b = (1/4g^2)(e2 - sum_k a_k^2 T_k)` in the eigenframe chart; this is the in-tree formula of the
  linear-contour paragraph, L1557. So `LAM = 1/(4g^2)`, which is `g^2 = 1/2`, not 1.
- The full matching (C3) has a unique solution, `eps_A = 2 eps_code`, `gamma_A = gamma_code`, `g_YM^2 = 1/2`.
- So the numbers can be stated in Definition (A) units without ambiguity. This is more informative than a label
  saying only that they are in a different normalisation, and it covers the 054 range in the same way.
- Option (i) was therefore chosen.

**Pauli components confirmed, by two independent routes** (`convert_r3.py`).
- **The insertion (C4).** `n2_slice_r1.py` uses `gc = e^{3pi i/8} r0/2` in `2cos(gc|a|)`. That is the eigenvalue of
  `k^0 a sigma^3/2`. An HS component (`a sigma^3/sqrt2`) would give `r0/sqrt2`.
- **The exponent (C1 = C2).** Definition (A) is evaluated on explicit 2x2 matrices, with
  `A_0 = e^{-i alpha} sum_k a_k sigma^k/2` and spatial `A_i = e^{i beta} sqrt(w_i) sigma^i/2` (Gram `diag(w)`).
  With `eta`, `S_b`, `S_gamma` and the regulator as in L1523, it equals the coded exponent identically in
  `(a_k, w_k, alpha, beta)`, and only under the map above.
- `n2_exp_mech.py` (054) uses the same exponent (L73-L75, `LAM = 0.5`), so the same map applies to the 054 range.

**Conversion** (`convert_r3.out`):

| quoted (code) | Definition (A), `g_YM^2 = 1/2` |
|---|---|
| ladder end `eps = 3e-3` | `6e-3` |
| exact insertion `eps >= 0.1` | `0.2` |
| corner value `0.0441942/eps` at `r0=1` | `0.0883883/eps = r0^2/(8 sqrt2 eps)` |
| 054 proxy range `eps in [0.01,1]` | `[0.02,2]` |
| `gamma = -0.2, -0.05` at `u = 0.6` | unchanged (`gamma/g^2 = -0.4, -0.1`) |
| ratios 2.0-4.1, ->2, 0.74-1.78; fit slope 0.0000 | unchanged |

Two cross-checks of the conversion:
- The code's corner value `0.0442/eps_c` and the corrected formula `r0^2/(8 sqrt2 eps_A)` agree under
  `eps_A = 2 eps_c` (C5a).
- The frozen saturation factors computed in Definition (A) at `g^2 = 1/2` (`1.4439` and `4.3469`) equal the
  code-normalisation values printed by `n2_slice_r1.py` (C5b).

So the r1/r2 reduced-model numbers were internally consistent. Only their unit was unstated.

### 3. Finding-by-finding

| Finding | Action |
|---|---|
| 1 (a) | Applied verbatim. |
| 1 (b) | Applied verbatim. |
| 1 (i)/(ii) | Option (i). Four numbers converted, and the normalisation stated once at the head of the reduced-model sentence: "Definition~(A) with \(g_{\mathrm{YM}}^2=1/2\), the normalisation of every value of \(\epsilon\) and \(\gamma\) below". "pointwise corner value \(0.044/\epsilon\)" becomes "corner value \({(r^0)}^2/(8\sqrt2\,\epsilon)\approx0.088/\epsilon\) at \(r^0=1\) of the one-dimensional branch model". "pointwise" is dropped as in (c), and the formula is given so that the reader can check it. (c) is not applied, because (i) replaces it. |
| 1, 054 range | Converted within (f): "\(\epsilon\in[0.02,2]\) of Definition~(A) with \(g_{\mathrm{YM}}^2=1/2\)". |
| 2 (d) | Applied verbatim. The E1 file is now the full replacement of anchor A1 (inserted sentence plus the reworded retained sentence). |
| 3 (e) | Both replacements verbatim, in E3. |
| 4 (f) | Applied verbatim, except that the range is converted, as above. |
| 5 | Disclosure below. |
| 6 (g) | Applied verbatim. `check_r3.py` (6a) and (6b) confirm the limit `b_u^2/(16 beta) -> Gamma_0/|gamma|`. At `eps > 0`, `b_u^2/(16 beta) < Gamma_0/|gamma|`, so the r2 "\(\ge\)" gave no lower bound. |

### 4. Disclosure: the moved correction (055, r3) against the original 057 text

**Original 057 tail (gpu plain ACCEPT):**

> In the one-dimensional branch model the coefficient of \(\tilde A_0\) in \(k^\mu A_\mu\) on \(\mathcal R_u\) at pure
> temporal slice momentum is \(\mathrm e^{3\pi\mathrm i(1-u)/8}r^0/2\), not its value at \(u=0\); with this
> contour-dependent coefficient the soft-mode growth exponent at \(\gamma=0\) is \({(r^0)}^2/(16\sqrt2\,\epsilon)\) and
> the fixed-\(\gamma\) saturation exponent is \(-g_{\mathrm{YM}}^2{(r^0)}^2/(8\sqrt2|\gamma|)\), both independent of
> \(u\), so the saturation factor \(\mathrm e^{{(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)}\) and its growth as
> \(\gamma\to0^-\) for \(3\pi u/4-\pi/4>0\) are properties of the frozen-coefficient model, not of the contour family.
> Problem~E remains open and PROGRAMME-CONDITIONAL.

**Every difference in the r3 text (055 sub-block):**

1. **Location.** The text moves from the end of 057 into the 055 sub-block, directly after the frozen-model sentence.
   057 keeps only the block closer (E4).
2. **Coefficient.** "is \(\mathrm e^{3\pi\mathrm i(1-u)/8}r^0/2\)" becomes "is \(\mathrm e^{3\pi\mathrm i(1-u)/8}r^0\)".
   The coefficient of \(\tilde A_0\) in \(k^\mu A_\mu\) is \(k^0\mathrm e^{-3\pi\mathrm iu/8}\); the \(/2\) belongs to
   \(\gamma_{\mathrm c}\), the eigenvalue factor of \(a\sigma^3/2\). This is check (2e). The change was already in r2,
   undisclosed.
3. **Coefficient made explicit.** "with this contour-dependent coefficient" became, in r2, "with this
   contour-dependent coefficient in \(\gamma_{\mathrm c}\)". In r3 it is "with
   \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i(1-u)/8}r^0/2\)", which is snippet (b).
4. **Exponents.** \(16\sqrt2\) becomes \(8\sqrt2\), and \(8\sqrt2\) becomes \(4\sqrt2\). This is the r3 factor-2
   correction (finding 1). The original 057 values, also carried in r2, are those of the unstated code normalisation.
5. **The explicit saturation factor** \(\mathrm e^{{(r^0)}^2\sin(\dots)/(8|\gamma|)}\) is replaced by "the saturation
   factor above". In r3 the factor above is \(\mathrm e^{g_{\mathrm{YM}}^2{(r^0)}^2\sin(\dots)/(4|\gamma|)}\), from
   snippet (a): the factor 2 is corrected and \(g_{\mathrm{YM}}\) is made explicit. The original had
   \(g_{\mathrm{YM}}=1\) implicit.
6. **Added clause.** "; with the contour-dependent coefficient the exponential factor of the signed one-dimensional
   integral tends at fixed \(\gamma<0\) to a constant below one for every \(u\in(0,2/3)\)". This follows from (2d),
   since the exponent is negative, and is unaffected by the factor 2.
7. **Closer removed.** The original closer "Problem~E remains open and PROGRAMME-CONDITIONAL." is removed here. The
   single block closer is at the end of 057.
8. **Context added before it, by snippet (a).** The definition of \(Q\) and of the soft mode
   \(\tilde A_0=a\sigma^3/2\), which the original 057 text and the original 055 left undefined.

## Claim classification

- **Established identities.**
  - `Tr(a sigma^3/2)^2 = a^2/2`.
  - The `Q` of Definition (A).
  - The branch formula.
  - The four corrected exponents.
  - Their u-independence on the contour.
  - The `beta` limit.
  - The normalisation map of the reduced code, which is unique.
  - The r2 identities (eigenvalues, `lambda_max(B)`, `b^2/(16A)`, the hypotheses of (v)), which are unchanged.
- **Derived within the hypothesis class.** Unchanged from r2: the 054 divergence off the slice, the limit via (v), the
  fixed `gamma < 0` extension, and the 056/057 modulus obstructions.
- **Model-level.** Both sets of 1D exponents are statements about the one-dimensional branch model, not about the full
  `N=2` integral.
- **Numerical.** The reduced-model ratios (factorized surrogate, frozen coefficient) and the `cosh` proxy. They are
  now stated in Definition (A) units.
- **Conjecture.** Phase-space suppression (hedged, unchanged).
- **Unresolved.**
  - The slice at `k != 0`, `r0 != 0`.
  - The `gamma -> 0^-` bridge.
  - `N >= 3`.
  - `N -> infinity` first.
  - Assumption~\ref{ass:lorentzian}.

## Proposed changes

All edits are in `chapters/appH-microscopic-proofs.tex`. The anchors are re-verified on the current tree (sha256
`6a83d79e...`); each occurs exactly once (`build_r3.out`).

- **E1.**
  - Anchor A1: `so that the domination above fails for them. It does not exclude a real-time reading obtained by
    continuation.` (count 1).
  - Replace it by the content of `E1_053_sentence.r3.tex`. This inserts the r2 sentence and rewords the retained
    sentence as in (d). Every other sentence of the 053 closing paragraph stays.

```latex
so that the domination above fails for them. The paragraph on exponential observables at \(N=2\) below sharpens this at \(N=2\), \(\gamma=0\), regulator (A) and the contours \(\mathcal R_u\): the right-hand side diverges in modulus for every nonzero real \(k\) and every \(k\) off one slice, the identity is unresolved on that slice at \(k\ne0\), and the failure is absent at fixed \(\gamma<0\). The result above does not exclude a real-time reading obtained by continuation.
```

- **E2 + E3 + E4.**
  - Anchor A2, the CRLF byte string (count 1):
    `Problem~E stays open with Assumption~\ref{ass:lorentzian} retained.` CRLF CRLF `\paragraph{Status.}` CRLF
    `Remains Assumption~\ref{ass:lorentzian}.` CRLF.
  - Insertion rule as in r2: after the blank line following "retained.", insert E2, then a blank line, E3, a blank
    line, E4, a blank line, then `\paragraph{Status.}`.
  - Full texts are in `E2_insert_054_055.r3.tex` (10230 B), `E3_056_adjusted.r3.tex` (2457 B) and
    `E4_057_adjusted.r3.tex` (3673 B).
  - E2-E4 are integrated jointly.
- **r3 changes against r2.** Each is applied by `build_r3.py` with an exact-once assertion:
  - (a), (b), (f) and the four option-(i) conversions in E2;
  - (e1) and (e2) in E3;
  - (g) in E4.
- **The r3 055 passage that changed** (from E2; the rest of E2 is the r2 text):

```latex
For \(r^0\ne0\) write the soft temporal mode as \(\tilde A_0=a\sigma^3/2\), on which the regulator and the mass give \(\mathrm e^{-Qa^2}\) with \(Q=\tfrac12\mathrm e^{-3\pi\mathrm iu/4}(\epsilon-\mathrm i\gamma/(2g_{\mathrm{YM}}^2))\). The one-dimensional branch integral \(\int_{\mathbb R}\mathrm e^{-Qa^2}\,2\cos(\gamma_{\mathrm c}|a|)\,\mathrm da=2\sqrt{\pi/Q}\,\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\), with \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\) frozen at its value on the Hermitian contour, gives in that frozen-coefficient model pointwise modulus growth \(\mathrm e^{{(r^0)}^2\cos(3\pi u/4-\pi/4)/(8\epsilon)}\) for the soft temporal mode at \(\gamma=0\), saturating as \(\epsilon\to0^+\) at fixed \(\gamma<0\) to a constant of order \(\mathrm e^{g_{\mathrm{YM}}^2{(r^0)}^2\sin(3\pi u/4-\pi/4)/(4|\gamma|)}\), which diverges as \(\gamma\to0^-\) when \(3\pi u/4-\pi/4>0\) and decays when it is negative. In the one-dimensional branch model the coefficient of \(\tilde A_0\) in \(k^\mu A_\mu\) on \(\mathcal R_u\) at pure temporal slice momentum is \(\mathrm e^{3\pi\mathrm i(1-u)/8}r^0\), not its value at \(u=0\); with \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i(1-u)/8}r^0/2\) the soft-mode growth exponent at \(\gamma=0\) is \({(r^0)}^2/(8\sqrt2\,\epsilon)\) and the fixed-\(\gamma\) saturation exponent is \(-g_{\mathrm{YM}}^2{(r^0)}^2/(4\sqrt2|\gamma|)\), both independent of \(u\), so the saturation factor above and its growth as \(\gamma\to0^-\) for \(3\pi u/4-\pi/4>0\) are properties of the frozen-coefficient model, not of the contour family; with the contour-dependent coefficient the exponential factor of the signed one-dimensional integral tends at fixed \(\gamma<0\) to a constant below one for every \(u\in(0,2/3)\). In the reduced \(N=2\) integral (Definition~(A) with \(g_{\mathrm{YM}}^2=1/2\), the normalisation of every value of \(\epsilon\) and \(\gamma\) below, contours \(\mathcal R_u\), \(\epsilon\to0^+\) last) with the factorized surrogate of this insertion along the soft temporal mode, coefficient frozen as above (it coincides with the contour-dependent one at \(u=0\)), at pure temporal slice momenta (the exact insertion, evaluated at \(u=0\) for \(\epsilon\ge0.2\) only, gives ratios between \(2.0\) and \(4.1\)), the modulus ratio \(|Z_\epsilon[O_k]|/|Z_\epsilon[1]|\) stays of order one and tends to \(2\) along the ladder down to \(\epsilon=6\cdot10^{-3}\) (fit slope \(0.0000\) of \(\ln\)-ratio against \(1/\epsilon\), against the corner value \({(r^0)}^2/(8\sqrt2\,\epsilon)\approx0.088/\epsilon\) at \(r^0=1\) of the one-dimensional branch model), and at \(u=0.6\) with \(\gamma=-0.2,-0.05\) it stays between \(0.74\) and \(1.78\):
```

- **The r3 054 passage that changed (f):**

```latex
grows without bound as \(\epsilon\to0\): the rank-one corner estimate of the paragraph on the slice bridge band, applied along a ray with \(b_u(\hat\rho;k)\ne0\), gives growth at least like \(\mathrm e^{c/\epsilon}\) up to polynomial factors (a large-radius \(\cosh\) proxy of \(|O_k|\) in a reduced chart increases on the sampled range \(\epsilon\in[0.02,2]\) of Definition~(A) with \(g_{\mathrm{YM}}^2=1/2\), numerical).
```

- **E3 (056) and E4 (057).** They carry (e) and (g) verbatim. The quoted forms are in `build_r3.py` (E3/E4 blocks).
- **Labels.** The only `\ref` is `ass:lorentzian` (defined once, ch04). The citation keys are
  `ChouNishimuraTripathi2025` and `AsanoNishimuraPiensukYamamori2025` (in bib, unchanged). No `\label` is added.
  There are 0 non-ASCII characters.
- **Stale passages.** None elsewhere. Grep finds no text outside these inserts that quotes the 055 exponents or the
  reduced-model numbers.

## Verification scripts

Run all of these from the repository root.

1. `python -I proposals/local-gpu/054-055-r2/check_r3.py` produces `check_r3.out`. Expected: 22 PASS lines and
   `OVERALL: ALL CHECKS PASS`. Key invariants:
   - (2g) `Q = (1/2)e^{-3pi i u/4}(eps - i gamma/(2g^2))`, from the trace;
   - (2a) `cos(...)/(8 eps)`;
   - (2b) `g^2 sin(...)/(4|gamma|)`;
   - (2c) `r0^2/(8 sqrt2 eps)`;
   - (2d) `-g^2 r0^2/(4 sqrt2|gamma|)`;
   - (2f) the corner value `0.0883883`;
   - (2h) the quadrature, relative error `< 1e-23`;
   - (6a)/(6b) the `beta` limit.
2. `python -I proposals/local-gpu/054-055-r2/convert_r3.py` produces `convert_r3.out`. Expected: 8 PASS lines,
   `OVERALL: ALL CHECKS PASS`, and the unique solution `{eps_A: 2 eps_c, g2: 1/2, gamma_A: gamma_c}`.
3. `python -I proposals/local-gpu/054-055-r2/gk_normcheck_r2.py` produces `gk_normcheck_r2.rerun_r3.out`. Expected:
   four lines ending in `0`, and `numeric |I| = 7.41732077747273  predicted 7.41732077747273`.
4. `python -I proposals/local-gpu/054-055-r2/build_r3.py [--apply-to DIR_OUTSIDE_REPO]` produces `build_r3.out`.
   Expected:
   - 10 `applied` lines;
   - closers 1;
   - anchors A1 and A2 with count 1 each;
   - sha256 values: E1 `4963f091...`, E2 `580516f7...`, E3 `dbc2cb2a...`, E4 `914dc9fe...`;
   - the applied copy: 648097 B, CRLF 3428, bare-LF 0, sha256 `fa3e3181...`;
   - `BUILD_R3 OK`.
5. Build of the applied copy outside the repository: `build_check_r3.out`. See the "Build" line below.
6. The r2 package scripts are unchanged. Their outputs (`rerun_*.out`) are the source of every reduced-model number.
   Only the unit statement changes.

**Build:** `build_check_r3.out`. A copy in the session scratchpad (outside the repository) with the applied appH (sha256 `fa3e3181...`) was built with pdflatex, bibtex, pdflatex and pdflatex. Every pass exited 0, with 0 undefined references, 0 multiply defined, 386 pages.

## Decisions Taken

1. **Option (i) over (ii).** (c) fixes only the soft-mode `Q`. The code also fixes the quartic coupling
   (`LAM = 0.5`, so `g_YM^2 = 1/2`), so a reader of (c) would infer a model at `g_YM = 1` that the code does not
   implement. Option (i) states the exact model in the manuscript's own definition. Rejected: (ii)/(c), which is
   correct but incomplete. Also rejected: rescaling to `g_YM = 1` by `A -> 2^{-1/4}A`. That would also rescale `r0`
   (`r0 = 1` becomes `2^{-1/4}`), which is harder to read and gains nothing, since `r0^2/eps` and `g^2 r0^2/|gamma|`
   are invariant.
2. **One normalisation statement per sub-block.** It is given once at the head of the reduced-model sentence in 055
   and once in the 054 proxy parenthesis, not on every number.
3. **E1 file format.** The E1 r3 file is the full replacement string of anchor A1, because (d) modifies a retained
   tree sentence next to the insertion.

## Milestone assessment

M3 (an accepted claim found wrong): the 057 exponents, now in 055, were a factor 2 too small relative to
Definition (A). They are corrected here, and the qualitative conclusions are unchanged. Otherwise this round is
routine. No breakthrough is claimed.

## Status-label recommendation

The critical-path set is A, B, C, D1, E, F, G-derived and N. Problem E stays OPEN, CRITICAL PATH for the
matrix-derived label, PROGRAMME-CONDITIONAL. No label change is proposed.

## Author decision needed

None.

## Remaining open step

The remaining steps are unchanged from r2, ranked:
1. Signed (oscillation-based) control of the slice left-hand side at full `N=2`, uniform in `eps`, for `r0 != 0`.
2. The `gamma -> 0^-` bridge at fixed `u`. At branch level, the contour-coefficient factor is damped for every
   `u in (0,2/3)`, with exponent `-g^2 r0^2/(4 sqrt2|gamma|)`. Only the modulus obstruction of 057 remains.
3. The pure-spatial half of the slice.

Beyond these: `N >= 3`, `N -> infinity` first, and the signature itself (Assumption~\ref{ass:lorentzian}).

## Special instructions for the gatekeeper

- **Re-derive these.**
  - The four exponents with `Q = (1/2)e^{-3pi i u/4}(eps - i gamma/(2g^2))`.
  - The code-normalisation map (C3). It depends on reading `LAM` as `1/(4g^2)` through the Pauli-component formula
    `S_b = (1/4g^2) sum_{a<b}[...]` of L1557.
- **Check the conversions:** 0.1 -> 0.2, 3e-3 -> 6e-3, 0.044 -> 0.088, [0.01,1] -> [0.02,2], with `gamma`
  unchanged.
- **E2-E4 are integrated jointly.** Re-check the anchors on the tree current at integration.
- **Do not assert:** the slice identity at `k != 0`, any `gamma -> 0^-` bridge, any domination lemma, any signature,
  or any label change.
- **Full scan.** It is still owed before a final ACCEPT. The tree is unchanged since r2.
