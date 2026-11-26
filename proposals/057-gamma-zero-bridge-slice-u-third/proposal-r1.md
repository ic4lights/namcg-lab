# Proposal 057-gamma-zero-bridge-slice-u-third, round 1

## Result

Follow-up package to proposal 056, executing the gatekeeper's ranked avenue 1: control the Lorentzian
slice left-hand side at k != 0, r0 != 0, gamma = 0 by passing gamma -> 0^- from the fixed-gamma<0 case on
the contour family R_u, u < 1/3 (gatekeeper criterion: an epsilon-uniform then gamma-uniform estimate with
error o(1) as gamma -> 0^+). Outcome is (b)+(c): a reproducible bounded no-go for the modulus route to this
bridge, plus a conditional chain.

1. Reduction (derivation). With I_eps^(gamma)[O] the regulated integral (A) with mass S_gamma on R_u,
   Delta(eps,gamma) = I_eps^(0)[O_k] - I_eps^(gamma)[O_k] satisfies
   |Delta(eps,gamma)| <= (|gamma|/2g_YM^2) * Jtilde(eps,u),
   where Jtilde is the gamma=0 modulus functional on R_u with insertion Tr A~_0^2 + sum_i Tr A~_i^2.
   Hence Delta -> 0 as gamma -> 0^- at each fixed eps: the pointwise-in-eps half of the bridge holds.
2. Obstruction on the gamma side of the link (bounded no-go). The same rank-one ray and transverse tube as
   in the merged 056 paragraph give Jtilde(eps,u) >= rho_*^2 e^{c0(u)/eps}/poly with the SAME constant
   c0(u) = sin^2(3 pi (1-u)/8) (r0)^2 / (16 cos(3 pi u/4)) > 0, u in (0,2/3). So no absolute-value bound
   for Delta is o(1) uniformly on any ladder eps -> 0^+: within the class N=2, regulator (A) with mass,
   fixed contours R_u, u in (0,2/3), slice momenta with r0 != 0, and linking by modulus estimates, the
   gamma -> 0^- bridge is obstructed at every u, not only at u >= 1/3. Closing the bridge requires signed
   (oscillation-based) control of the gamma=0 slice functional uniform in eps, i.e. the same missing
   ingredient the 056 obstruction identifies.
3. Obstruction on the fixed-gamma side (mass-side modulus). Maximizing
   b_u rho/2 - beta(eps,gamma) rho^2, beta = eps cos(3 pi u/4) + |gamma| sin(3 pi u/4)/(2 g_YM^2),
   gives the soft-mode modulus exponent b_u^2/(16 beta): along ladders it interpolates between
   c0(u)/eps (eps-side) and Gamma0(u)/|gamma| (gamma-side), with
   Gamma0(u) = g_YM^2 sin^2(3 pi (1-u)/8) (r0)^2 / (8 sin(3 pi u/4)) > 0 for every u in (0,2/3),
   strictly decreasing in u (Gamma0(1/3) = 0.0883883 (r0)^2 at g_YM = 1, and Gamma0 -> infinity as u -> 0).
   The mass-side modulus also blows up super-polynomially as gamma -> 0^- at every u, most strongly at
   SMALL u: the u < 1/3 band does not relieve the modulus route, it inverts its worst direction.
4. Positive derivation (fixed gamma < 0). The merged parenthetical that the limit identity at fixed
   gamma < 0 "extends to O_k for every k in C^10 (numerical)" is now a derivation at N=2: the mass gives
   real-part damping coefficients c_T0 = eps cos(3 pi u/4) + |gamma| sin(3 pi u/4)/(2 g_YM^2) and
   c_Ti = eps cos(pi u/4) + |gamma| sin(pi u/4)/(2 g_YM^2), bounded below by
   |gamma| sin(3 pi u/4)/(2 g_YM^2) and |gamma| sin(pi u/4)/(2 g_YM^2) independently of eps for fixed
   u in (0,2/3); the Stokes boundary term on balls times [0,u] decays and both sides are dominated
   (Pfaffian polynomial at N=2, insertion growth e^{c(k) rho} beaten by the full-component Gaussian).
5. Model correction (frozen coefficient). On R_u at pure temporal slice momentum the coefficient of A~_0
   in k^mu A_mu is e^{3 pi i (1-u)/8} r0/2, not its u=0 value e^{3 pi i/8} r0/2 (k^0 = r0 e^{3 pi i/8} on
   the slice, A_0 = e^{-3 pi i u/8} A~_0). With the contour-dependent coefficient the one-dimensional
   branch model gives soft-mode growth exponent +(r0)^2/(16 sqrt2 eps) at gamma=0 and fixed-gamma
   saturation exponent -(r0)^2/(8 sqrt2 |gamma|), both independent of u. The merged saturation factor
   e^{(r0)^2 sin(3 pi u/4 - pi/4)/(8|gamma|)} and its growth as gamma -> 0^- for u > 1/3 are properties
   of the frozen-coefficient model, not of the contour family.
6. Model-level chart probe (055 chart, new mode 'factoru' with the contour-dependent coefficient):
   the signed bridge difference D(eps,gamma) = |Z_eps[O_k;gamma] - Z_eps[O_k;0]| / |Z_eps[1;0]| is
   O(|gamma|) with an eps-independent constant (slopes of ln C against 1/eps within +-5e-4, ladder
   eps = 0.03, 0.01, 0.003, u = 0.3, 0.6), and the reduced chart does NOT display the modulus divergence
   e^{c0/eps}: Zmod/|Z| stays between 1.77 and 4.52. The reduced chart neither proves nor refutes
   eps-uniformity; it is oscillation-limited and its branch factor does not realize the tube weight of
   the full-integral lower bound.

No critical-path status label is changed; Problem E remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Target and status

- Problem: E (Lorentzian signature), `chapters/appH-microscopic-proofs.tex`, section
  `\label{sec:status-E}` (L1482-1522); ch17-agenda L394-399.
- Exact current status (re-read this round): "Status: OPEN. Priority: CRITICAL PATH for the
  matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining
  Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian
  signature." ch17: "OPEN; CRITICAL PATH for the matrix-derived label ... rotating because the infrared
  world is Lorentzian is not a derivation." No discrepancy between appH and ch17.
- Original target: derive Lorentzian signature from the matrix theory (discharge
  Assumption~\ref{ass:lorentzian}); the slice-bridge subtarget is the gatekeeper's avenue 1 after 056:
  "epsilon-uniform then gamma-uniform estimate on the contour family R_u, u in [0,1/3), with error o(1)
  as gamma -> 0^+" (proposals/056-slice-lhs-full-n2-bridge/review-r2.md).
- Dependencies: the merged 056 paragraph "Slice bridge band and modulus obstruction" (L1516: b_u, c0(u),
  M_u(eps) lower bound, lambda_* = sqrt(2+sqrt2)); the merged 055 paragraph "The slice at k != 0"
  (L1514); the fixed-gamma<0 contour sentence (L1506) and the exponential-observables paragraph (L1512).
- This package: PROGRAMME-CONDITIONAL evidence. It bounds the gamma->0^- bridge route inside its
  hypothesis class and supplies sub-lemmas (Leg A derivation, Leg E correction); it closes nothing.

## Source reading

digest + targeted reads. Digest noted as compact/working-tree; targeted full reads: appH Problem E
section L1478-1525 (in full), ch17-agenda L392-405, reports/sme-scout-20261106-2023.md (in full), proposals/056-slice-lhs-full-n2-bridge/
review-r2.md (in full), proposals/056-slice-lhs-full-n2-bridge/bridge_r1.py (SEC3/SEC4),
proposals/055-anti-wick-slice-nonzero-k/n2_slice_r1.py (L1-259). The scout's ranked routes (2501.17798
saddle differences, 2404.14045 classicalization, 2604.25564 boost-fixed CLM) were assessed as not
importable for this bridge; EMERGENCE-RISK of this package: none (spacetime stays emergent; no route
here assumes a fundamental metric). No unreadable files. reports/ledger.md working-tree truncation
(ends at 037; full ledger at commit efab2bb) noted in the scout report; not touched.

## Research and reasoning

Set-up (as merged): I_eps[O] = int dA O Pf M e^{iS_b - eps sum Tr A_mu^2} (regulator (A)); contours
R_u: A_0 = e^{-3 pi i u/8} A~_0, A_i = e^{pi i u/8} A~_i, A~ Hermitian traceless; slice k^0 = r0
e^{3 pi i/8}, k^i = r^i e^{-pi i/8}, r^mu real, r0 != 0; O_k = Tr e^{i k A} = 2 cos(rho_X/2) at N=2;
mass S_gamma = -(gamma/2g^2) Tr A_mu A^mu, gamma < 0 written |gamma| = -gamma.

Step 1 (signs; script 1 SEC1, symbolic). Tr A_0^2 = e^{-3 pi i u/4} T0, sum Tr A_i^2 = e^{pi i u/4} Ti,
T0 = Tr A~_0^2 >= 0, Ti = sum Tr A~_i^2 >= 0. Then
Re iS_gamma = (gamma/2g^2)[sin(3 pi u/4) T0 + sin(pi u/4) Ti] <= 0 for gamma < 0 (mass DAMPS on R_u;
identical to the merged L1512 form), and Re(-eps sum Tr A_mu^2) = -eps[cos(3 pi u/4) T0 + cos(pi u/4) Ti].
Symbolic equality checked. Damping margins c_T0(eps,u), c_Ti(eps,u): min over u-grid [0,1] at
(eps=0.01,|gamma|=0.2) is 0.01 > 0; at (0.05,0.2) it is 0.035355339 > 0.

Step 2 (Leg A, fixed gamma < 0, derivation at N=2). With c_T0, c_Ti > 0 and eps-independent lower
bounds for fixed u in (0,2/3), the integrand modulus is bounded by
poly(||A~||) e^{c(k) rho} e^{-c_T0 T0 - c_Ti Ti}: a full-component Gaussian dominates the polynomial
Pfaffian (at N=2, Pf M = c_P (det G)^4) and the exponential insertion for every k in C^10, so (i) the
Stokes boundary term on balls times [0,u] is polynomial times e^{-min(c_T0,c_Ti) R^2} -> 0 and (ii)
dominated convergence gives the eps -> 0^+ limit with mass retained, at any u in (0,2/3) and (by the
merged contour sentence, u -> 1 with the mass) with the Euclidean-side value. The merged "(numerical)"
is thus upgraded to a derivation at N=2. For N >= 3 the same domination works provided Pf M(A(u,A~))
is polynomial (it is, M linear in A) but rests on the merged conditional reading of the Pfaffian bounds;
classified conditional there. No claim is made for gamma = 0 or gamma > 0.

Step 3 (Leg C, reduction, derivation). Delta(eps,gamma) = int_{R_u} (base) (1 - e^{iS_gamma}) dA~, base
= the gamma=0 integrand (with O_k). Since Re iS_gamma <= 0, |e^{iS_gamma} - 1| <= |S_gamma| (verified
numerically at 400 seeded points for |e^z - 1| <= |z|, Re z <= 0), and |Tr A_mu A^mu| <= T0 + Ti on R_u
(triangle; sampled values 0.312869, 1.17557, 1.78201, 2.0 <= 2 at u = 0.1,0.4,0.7,1). Hence
|Delta| <= (|gamma|/2g^2) Jtilde(eps,u), Jtilde = int |base| (T0 + Ti) dA~. Pointwise in eps,
|Delta| -> 0. Degree bookkeeping: (det G~)^4 window degree 8, insertion degree 2, 8+2 = 10 < 14, so the
mass-free window applies to the base modulus in the polynomial truncation.

Step 4 (Leg C lower bound, reuses the merged 056 estimate). On the rank-one corner A~_0 = rho H,
Tr H^2 = 1, transverse scale O(eps): |O_k| >= e^{b_u rho/2}/(2 sqrt2), b_u = sin(3 pi(1-u)/8)|r0|
(merged 056, gatekeeper-verified), insertion T0 = rho^2, regulator damping e^{-eps cos(3 pi u/4) rho^2};
maximizing b_u rho/2 - eps cos(3 pi u/4) rho^2 over rho gives b_u^2/(16 eps cos(3 pi u/4)) =
c0(u)/eps, c0(u) = sin^2(3 pi(1-u)/8)(r0)^2/(16 cos(3 pi u/4)) (symbolic identity with the merged
c0(u); numeric c0(0.3) = 0.0443209 matches the gatekeeper-verified value). Therefore
Jtilde(eps,u) >= rho_*^2 e^{c0(u)/eps}/poly and the link bound |gamma| Jtilde/(2g^2) DIVERGES as
eps -> 0 at fixed u: the modulus route gives no o(1) uniformly in eps, at every u in (0,2/3).
(c0(u) > 0 for u < 2/3; the formula flips sign at u = 2/3 where the regulator stops damping A~_0,
consistent with the merged u >= 2/3 divergence.)

Step 5 (structural reading of avenue 1). Because the fixed-gamma<0 side has its limit by Leg A, an
eps-UNIFORM bridge estimate |I_eps^(0) - I_eps^(gamma)| <= eta(gamma), eta -> 0 as gamma -> 0^+,
uniform in eps, would make {I_eps^(0)} Cauchy as eps -> 0 and hence settle the gamma=0 slice limit
itself. So avenue 1 is only a sufficient route, and every modulus realization of it fails by Step 4:
the whole obstruction sits on the gamma=0 signed side. What is NOT excluded: signed estimates.
(Non-uniformity of the bound is not non-existence of the limit; the pointwise Delta -> 0 of Step 3
is true.)

Step 6 (Leg D, mass-side modulus, derivation). With mass, the soft-mode ray exponent is
b_u rho/2 - beta(eps,gamma) rho^2, beta = eps cos(3 pi u/4) + |gamma| sin(3 pi u/4)/(2 g^2)
>= |gamma| sin(3 pi u/4)/(2 g^2) =: beta0, independent of eps (so fixed-gamma moduli are eps-uniform).
Max over rho: b_u^2/(16 beta) <= b_u^2/(16 beta0) = Gamma0(u)/|gamma|,
Gamma0(u) = g^2 sin^2(3 pi(1-u)/8)(r0)^2/(8 sin(3 pi u/4)). Note the factor 1/16:
max_rho (b rho/2 - beta rho^2) = b^2/(16 beta) (an earlier draft had 1/4; corrected before the run).
Ray region gives the matching lower e^{Gamma0(u)/|gamma|}/poly. Table (g=1, r0=1): Gamma0 = 0.407616
(0.1), 0.180210 (0.2), 0.103786 (0.3), 0.0883883 (1/3), 0.065169 (0.4), 0.0417612 (0.5), 0.0260846
(0.6), 0.0150209 (0.7), 0.0071627 (0.8), 0.0020253 (0.9); symbolic derivative negative on a grid over
(0.1,0.7): Gamma0 strictly decreasing, Gamma0 -> infinity as u -> 0^+. Joint-ladder check at u=0.3,
|gamma| = 0.05: general exponent b^2 r0^2/(16 beta(eps)) = 0.621158 (eps=0.05), 1.413650 (0.01),
1.982860 (0.001) -> Gamma0/|gamma| = 2.075720 (eps -> 0); the eps-only side is c0/eps = 14.7736
(eps=0.003), 88.6417 (0.0005). Conclusion: every modulus bound on the bridge diverges
super-polynomially along every ladder (eps,gamma) -> (0,0) at fixed u in (0,2/3); the u < 1/3 band is
where the MASS side is worst (Gamma0 largest), inverting the hoped-for direction.

Step 7 (Leg E, contour phase, exact). On R_u at slice momentum, k^mu A_mu = e^{3 pi i(1-u)/8} r0 A~_0 +
e^{-pi i u/8}... (spatial: k^i A_i = e^{-pi i u/8} r^i e^{pi i u/8} A~_i = r^i A~_i), so the temporal
coefficient is e^{3 pi i(1-u)/8} r0 (and gamma_c = e^{3 pi i(1-u)/8} r0/2 with the sigma^a/2 basis).
The branch closed form int_R e^{-Q a^2} 2 cos(gamma_c a) da = 2 sqrt(pi/Q) e^{-gamma_c^2/(4Q)} was
checked against mpmath quad at two (u,eps,gamma) points (reldev 2.296e-16, 1.451e-16). Exponents:
gamma=0, Q = eps e^{-3 pi i u/4}: Re(-gamma_c^2/(4Q)) = (r0)^2/(16 sqrt2 eps), u-independent
(the u=0 value coincides with the merged 0.044/eps); eps -> 0 at fixed gamma: Q -> i|gamma|/(2g^2)
e^{-3 pi i u/4}, Re(...) = -g^2 (r0)^2/(8 sqrt2 |gamma|) < 0, u-independent (saturation DECAYS). The
merged u-dependent factors cos(3 pi u/4 - pi/4)/16eps and sin(3 pi u/4 - pi/4)/(8|gamma|) arise from
freezing gamma_c at e^{3 pi i/8} r0/2 (the 055 script line `gc2 = (np.exp(1j*3*np.pi/8)**2)*(r0**2)/4.0`
applied at all u). The merged L1514 text correctly labels its model, so this is recorded as a model-
level correction in the new paragraph, not as a fix to a false sentence.

Step 8 (chart probe, model level only). Script 2 copies the 055 reduced N=2 chart (nodes, Vandermonde
measure, p=4, D=10, LAM=0.5, exact branch moment machinery) and adds mode 'factoru' with
gc2 = (e^{3 pi i(1-u)/8})^2 r0^2/4. P0 sanity: at r0 = 1e-6 the factoru/bare ratio is 2.0000000000
(= Tr I). P1 at u=0.3, gamma ladder 0,-0.2,-0.1,-0.05,-0.02: ratios |Z[O_k]|/|Z[1]| in
[1.9624, 1.9675], ln-ratio slope vs 1/eps at gamma=0 equal 0.0000; u=0.6: [1.8824, 1.9341]. So neither
the true-phase e^{(r0)^2/(16 sqrt2 eps)} growth nor the frozen growth materializes in the chart
(consistent with 056's remark on phase-space suppression by Vandermonde and measure powers; not a
domination lemma). P2 signed: D(eps,gamma) at u=0.3: e.g. gamma=-0.05: 0.72640, 0.62977, 0.70018;
C = D/|gamma| = 14.528, 12.595, 14.004, slope ln C vs 1/eps = 0.0000 (all slopes within +-5e-4;
u=0.6 similar, C ~ 7-11). Model level: the signed link constant shows NO growth against 1/eps on the
sampled ladder — the chart is consistent with an eps-uniform signed link, while its modulus diagnostic
Zmod/|Z| = 1.771, 2.807, 3.393 (u=0.3) and 4.021, 3.840, 4.523 (u=0.6) stays far below e^{c0/eps}.
Interpretation: the reduced chart's branch factor and diagonal measure do not realize the tube weight
of the full-integral lower bound; the probe is diagnostic only and must not be cited as evidence for
or against eps-uniformity of the full integral.

Comparison with the original target: the gatekeeper's closing criterion (eps-uniform then gamma-uniform
o(1)) is NOT met; it is shown unreachable by any modulus estimate at any fixed u in (0,2/3)
(within the class), and the surviving route is signed control at gamma=0 — which is the 056 obstruction
itself, now seen to be the unique survivor of the gamma->0^- route too.

## Claim classification

- Sign/window identities (SEC1): established identity (symbolic verification).
- |e^z-1| <= |z| (Re z <= 0), |Tr A_mu A^mu| <= T0 + Ti on R_u: established (elementary; numerically sampled).
- Leg A fixed-gamma<0 extension to O_k, every k in C^10: derivation at N=2 (Gaussian domination +
  Stokes + dominated convergence); conditional at N>=3 (rests on M linear in A / Pfaffian polynomial
  and the merged conditional Pfaffian reading).
- Leg C upper bound |Delta| <= |gamma| Jtilde/(2g^2): derivation.
- Jtilde >= rho_*^2 e^{c0/eps}/poly: conditional result built on the merged 056 ray/tube bound
  (|O_k| >= e^{b_u rho/2}/(2 sqrt2), gatekeeper-verified) plus elementary insertion bookkeeping.
- Pointwise Delta -> 0 at fixed eps: derivation. Non-existence of an eps-uniform MODULUS estimate:
  derivation within the modulus-estimate hypothesis class (a bounded no-go, class stated below).
- Avenue-1 structural reading (uniform bridge => slice limit exists): derivation (Cauchy argument).
- Leg D exponent b_u^2/(16 beta), Gamma0(u) formula, monotonicity: established (elementary
  maximization; symbolic derivative, grid check).
- Leg E closed form and exponents: established identities (symbolic + quad cross-check);
  "frozen-coefficient artifact" is a derived identification.
- Chart P0-P3: numerical model-level diagnostics (conditional on the 055 chart truncation).
- Everything else: no claim beyond the merged text.

## Proposed changes

One insertion, `chapters/appH-microscopic-proofs.tex`, Problem E section, immediately before the
Problem E `\paragraph{Status.}` (i.e. after the merged "Slice bridge band and modulus obstruction"
paragraph, L1516). Nothing else in the manuscript is changed; no bib entries are added or needed.

- Anchor (verified count == 1, apply_check_r1.out; byte form): 4x CRLF + `\paragraph{Status.}` + CRLF +
  `Remains Assumption~\ref{ass:lorentzian}.` at offset 256859 in the current appH. The decoy
  `Remains Assumption~\ref{ass:EFT-a2}.` occurs once and is untouched by the rule.
- Rule: `src.replace(anchor, b'\r\n\r\n' + T_CRLF + anchor, 1)` where T is the insert text,
  LF-normalized then CRLF-converted. All existing text (including the merged "(numerical)" at L1512
  and the frozen-model sentence at L1514) is KEPT; nothing is removed or reworded.
- The insert is one `\paragraph{...}` block ending with exactly one scoped status sentence
  "Problem~E remains open and PROGRAMME-CONDITIONAL."; inline `\( \)` math only; ASCII-only; no
  `\ref`/`\cite`/`\label`; matches merged notation (`\(I_\epsilon^{(\gamma)}[O]\)` is defined in the
  first sentence).
- Insert text: exactly the content of `appH_insert.tex` in this folder (sha256 of LF form
  a7f80bea2d3546fb60ba168acdf6f5f980b37790412f19ceae9392b24b7db022; CRLF form 4018 bytes, sha256
  7cebec5b06b329cc6e9f9f56ca34ae07815fed23d0e8f0fb58bdd430ffd7fe17). It contains: the reduction and its
  epsilon-uniformity failure with c0(u); the mass-side Gamma0(u) obstruction with the (1/3)-band
  inversion; the fixed-gamma<0 derivation for O_k; the contour-coefficient correction
  e^{3 pi i(1-u)/8} r0/2 with the u-independent exponents and the artifact statement.
- Stale passages NOT edited (recorded here for the gatekeeper/integrator, deliberately left alone):
  (a) L1512 "(numerical)" for the fixed-gamma<0 O_k extension — now derivable; the new paragraph
  states the derivation; no deletion proposed (smallest-text rule).
  (b) L1514 saturation factor e^{(r0)^2 sin(3 pi u/4 - pi/4)/(8|gamma|)} — correct for the frozen
  model as labeled; the new paragraph supplies the contour-dependent correction.

## Verification scripts

All in this proposal folder; run with `python -I` (mpmath 1.3.0, sympy, numpy). Every saved .out was
regenerated by a final re-run and the re-runs are BYTE-IDENTICAL (`cmp` evidence in the run log):

1. `bridge_gamma.py` -> `bridge_gamma_r1.out`: SEC1 mass/regulator real-part window identities and
   Leg A damping margins (0.01 and 0.035355339); SEC2 elementary inequalities (400 seeded points,
   max ratios <= 1) and the triangle bound on R_u; SEC3 branch closed form vs mpmath quad (reldev
   2.296e-16, 1.451e-16) and symbolic TRUE vs FROZEN exponents (TRUE: +1/(16 sqrt2 eps) at gamma=0,
   -1/(8 sqrt2 |gamma|) at fixed gamma; FROZEN: cos(3 pi u/4 - pi/4)/16eps etc.); SEC4 c0(u) identity
   with the merged constant, Gamma0(u) table and strict decrease, ladder exponents (c0/eps up to
   88.6417; Gamma0/|gamma| = 2.07572; interpolation 0.621158/1.413650/1.982860); SEC5 degree check
   8+2 = 10 < 14.
2. `chart_bridge.py` -> `chart_bridge_r1.out`: self-contained copy of the 055 reduced N=2 chart with
   new mode 'factoru' (contour-dependent gc2); P0 sanity 2.0000000000; P1 ratio tables and zero slopes;
   P2 signed D(eps,gamma) and C = D/|gamma| with slopes within +-5e-4; P3 Zmod/|Z| diagnostics,
   u = 0.3 and 0.6, eps ladder 0.03/0.01/0.003, gamma ladder 0,-0.2,-0.1,-0.05,-0.02.
3. `apply_check.py` -> `apply_check_r1.out` (REPORT MODE ONLY; writes nothing): current appH 542851 B,
   sha256 185bdcee9ae824e9c7fa7211c4280f56beb7f7210392f336592877f33112e73b, CRLF 3212, bare LF 0;
   anchor count 1 at offset 256859 (= predicted 254357 + 2502 from the 056 pins); decoy count 1;
   insert hygiene (0 non-ASCII, 0 `$`, 0 ref/cite/label, exactly 1 status sentence); computed
   post-apply size 546873 (delta 4022), sha256 1c9881219733d74538e89b8e92072ca4e83467fcf26eec4466dab2f7b9b99fbb,
   post-apply CRLF 3215, bare LF 0.
4. Out-of-repo application build at `C:/Users/redgi/tmp/057_apply_r1` (repo subset copy: main tex,
   chapters, bib, figs, frontmatter; insert applied there, resulting appH sha 1c988121... matches the
   predicted value above): pdflatex, bibtex, pdflatex, pdflatex, all exit 0; final log: 0 matches of
   "undefined", 0 of "multiply", 361 pages, 0 bibtex warnings; PDF 2680711 B sha256
   2a8600d4036f75a54902b443cbcc5692bd8e8aadc14a8acf630e4e32241a8910. Summary saved as
   `build_summary_r1.out`. The repo manuscript was not touched. NOTE: deletion of the tmp copy was
   denied by the permission system; the copy is outside the repository and can be removed by the
   integrator/author at `C:/Users/redgi/tmp/057_apply_r1`.

## Decisions Taken

- (Route) Submitted the bounded modulus no-go + conditional chain instead of forcing a positive
  eps-uniform estimate: the lower bound Jtilde >= e^{c0/eps}/poly makes any modulus bridge estimate
  diverge; a positive estimate by moduli would contradict it. Rejected alternative: softening the
  criterion to pointwise-in-eps (rejected: the merged 056 no-go would then be misread as closable).
- (Scope) Proved the reduction at every fixed u in (0,2/3), not only u < 1/3: strictly stronger, and
  it exposes the Gamma0 inversion that the u < 1/3 framing hides. Rejected: u < 1/3-only statement.
- (Correction handling) Did NOT edit the merged "(numerical)" (L1512) or the frozen-model sentence
  (L1514); both are not false as written (the first is conservative, the second labels its model).
  Recorded the corrections in the new paragraph. Rejected: rewriting merged text (violates the
  smallest-text rule).
- (Evidence) Added the reduced-chart 'factoru' probe rather than full 10-matrix numerics: cheap,
  reuses the verified 055 structure, and its negative/moderate diagnostics honestly delimit what the
  model shows. Rejected: presenting chart P2 (C eps-independent) as bridge evidence.
- (Notation) Defined `\(I_\epsilon^{(\gamma)}[O]\)` inside the insert (no new labels/refs).
- (Bug fixes found during development, recorded): Gamma0 factor 4 error (b^2/(4 beta) -> b^2/(16
  beta)) corrected before final runs; the SEC2 inequality |e^{-z}-1| <= |z| e^{-Re z} direction fixed;
  chart `nodes()` missing weight multiplication fixed (the earlier .out was a failed run and was
  regenerated).

## Milestone assessment

Routine. No MILESTONE.md trigger: the critical-path step (Lorentzian derivation / slice limit at
gamma=0) is not closed; the package is a bounded no-go for one route plus sub-lemmas and a corrected
model claim. No candidate breakthrough claimed.

## Status-label recommendation

Re-derived critical-path list from ch17-agenda (current): A, B, C, D1, E, F, G-derived, N (H, I, J
optional). Affected labels: NONE. Problem E stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
No LABEL-CHANGE-PROPOSED items.

## Author decision needed

None. (No structural change to the NAMCG core is proposed; spacetime remains emergent throughout.)

## Remaining open step

To close the gamma->0^- bridge at fixed u (and thereby the slice question at k != 0, r0 != 0):
1. SIGNED (oscillation-based) estimates for the gamma=0 slice functional on R_u, uniform in eps: e.g.
   non-stationary-phase / van der Corput type control of int base(1 - e^{iS_gamma}) exploiting the
   oscillation of e^{iS_b} along the rank-one tube, with error o(1) as gamma -> 0; or a thimble/Lefschetz
   decomposition of the gamma=0 integrand at N=2 outside the modulus class.
2. A full signed N=2 computation of the slice functional on R_u (10-matrix, not the reduced chart) to
   calibrate whether the tube divergence of the modulus is cancelled by oscillation, and why the
   reduced chart underrepresents the tube weight.
3. For the merged fixed-gamma<0 O_k statement at N >= 3: keep the conditional Pfaffian reading or
   extend Leg A's Gaussian-domination argument explicitly.
4. Pure spatial slice (r0 = 0) is ray-free (056); the r0 != 0 half remains exactly where it was,
   modulo this package's identification that any bridge must pass through signed control at gamma=0.

Avenues still open (ranked): (1) signed/oscillation estimates (the only survivor inside the class);
(2) full-N=2 signed numerics/thimbles; (3) alternative regulator M (merged regulator-independence is
proved only for polynomial O — non-polynomial growth may differ); (4) other sectors/observables
(pure spatial slice already ray-free); (5) presentation-level: derive the slice limit as a boundary
value from the mass side without a uniform estimate (equivalent to step 1). Hypotheses of THIS no-go:
N=2; regulator (A) + mass (A)-mass; contours R_u with u in (0,2/3) FIXED (no delta-lambda slide, that
was 056); slice momenta r0 != 0 (pure temporal sampled); linking the two mass sides through absolute
values of integrals/integrands; eps -> 0^+ last, gamma -> 0^- after or alongside. Signed estimates,
N >= 3 first-principles Pfaffian control, gamma > 0, N -> infinity first, and observables beyond O_k
are OUTSIDE the no-go.

## Special instructions for the gatekeeper

- Must not be asserted: that the gamma->0^- bridge fails (only its MODULUS realization fails; the
  pointwise Delta -> 0 at fixed eps IS proved); that the slice limit fails or exists; that the chart
  probe settles anything (model truncation, see Step 8); that Leg A settles the gamma=0 side; that
  anything applies to N -> infinity taken first or to gamma > 0.
- Re-derive first (cheapest checks): (i) Leg E single line: slice k^0 = r0 e^{3 pi i/8}, A_0 =
  e^{-3 pi i u/8} A~_0 => coefficient e^{3 pi i(1-u)/8} r0; then exponents + (r0)^2/(16 sqrt2 eps)
  and - (r0)^2/(8 sqrt2 |gamma|) via Re(-gamma_c^2/(4Q)); (ii) the 1/16 factor:
  max_rho (b rho/2 - beta rho^2) = b^2/(16 beta); (iii) Gamma0(u) = g^2 b_u^2/(8 sin(3 pi u/4)) and
  its strict decrease; (iv) |e^z-1| <= |z| for Re z <= 0 and |Tr A_mu A^mu| <= T0 + Ti on R_u;
  (v) c0(u) identity with the merged L1516 constant (numeric 0.0443209 at u=0.3, r0=1).
- Leg C is a reduction, not a new bound: it reuses the merged 056 ray/tube lower bound; verify reuse
  fidelity (insertion T0 = rho^2 on the ray, transverse scale O(eps), poly bookkeeping).
- PRIOR-CLAIM note (not an error flag): merged L1512 "(numerical)" is now derived at N=2 by Leg A;
  merged L1514 frozen-coefficient saturation divergence is a model artifact — verify by the true-phase
  exponents, not by numerics.
- apply_check.py must stay report-mode; the only applied copy was the out-of-repo tmp build
  (build_summary_r1.out; log clean, 361 pages). Anchor count must be 1; decoy untouched.
- Re-run all three scripts; .out files reproduce byte-identically.
- No bib changes; no new labels; no \ref in the insert.

## Pins

- appH (pre-apply, current working tree): 542851 B, sha256 185bdcee9ae824e9c7fa7211c4280f56beb7f7210392f336592877f33112e73b, CRLF 3212, bare LF 0.
- Anchor offset 256859, count 1. Decoy `ass:EFT-a2` count 1, untouched.
- Insert: `appH_insert.tex` 4017 B (LF), sha256 a7f80bea2d3546fb60ba168acdf6f5f980b37790412f19ceae9392b24b7db022; CRLF 4018 B, sha256 7cebec5b06b329cc6e9f9f56ca34ae07815fed23d0e8f0fb58bdd430ffd7fe17.
- Post-apply (in-memory and in tmp build): 546873 B (+4022), sha256 1c9881219733d74538e89b8e92072ca4e83467fcf26eec4466dab2f7b9b99fbb, CRLF 3215, bare LF 0, anchor count 1.
- bib/namcg.bib unchanged (25976 B, sha256 a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b); no bib entries proposed.
- Out-of-repo build: C:/Users/redgi/tmp/057_apply_r1 (deletion permission-denied; outside repo), 4 passes exit 0, 0 undefined / 0 multiply-defined, 361 pages, PDF sha256 2a8600d4036f75a54902b443cbcc5692bd8e8aadc14a8acf630e4e32241a8910.
- 056 pins honored: merged 056 paragraph untouched; c0(u), b_u, lambda_* reused as verified.
