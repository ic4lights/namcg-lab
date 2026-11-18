# Proposal 081-g-edge-moments, round 1

## Result

Within the Gaussian state model of the appH "Row length" paragraph (Problem G,
065-block), the identification of the moments of the classicalised rank-one
edge charge Q with the edge datum of the block cut is an **exact conditional
equivalence with one quantified profile obstruction**:

1. Pointwise, at the leading-order convention Im(u|w) = 0, the nonzero
   spectrum of Q is exactly {+/- ell} with ell = 2|w_perp| the row length, so
   Tr Q^(2p) = 2 ell^(2p) and all odd charge moments vanish; band-separated
   cap sequences add (s2 PARTA, deviation 6.460e-15 over 200 configurations).
2. Gaussian-averaged with block-row profile g, total weight W and edge datum
   s^2, <Tr Q^(2p)> = 2 (4 s^2 W)^p rho_p(g), rho_p(g) = p! h_p(g)/W^p exact
   (s2 PARTB, exact rational residual 0). The second moment gives
   8 s^2 W = 2 <ell^2> and matches <ell^2> = 4 s^2 W of the Row length
   paragraph exactly (rho_1 = 1): the second-moment identification is exact
   in the model.
3. For p >= 2 the edge-data single-scale prediction is multiplied by the
   exact profile factor rho_p > 1 with rho_p - 1 >= C(p,2)/D_eff,
   D_eff = W^2/sum g^2; rho_2 = 1 + 1/D_eff and rho_3 = 1 + 3/D_eff +
   2 s_3/W^3 exactly, 1 < rho_p <= p! with both ends sharp, and
   rho_p = sum_{lambda |- p} (p!/z_lambda) prod_k (s_k/W^k)^{m_k} (s3,
   0 failures on 1000 random profiles). So the fourth charge moment exceeds
   the edge-data prediction by exactly 1/D_eff and the identification fails
   at every finite profile; it is recovered at leading order only as
   D_eff -> infinity (fuzzy-proxy D_eff table: 105.8 -> 365132.5 for
   l_c = 10..640; fourth-moment excess 4.0e-3 -> 2.6e-4 between l_c = 40 and
   160).
4. The 080 per-factor moment-signature identity (excesses 9/17 and 81/145 at
   (q1,q2) = (2,1), (n1,n2) = (1/4,2/9)) is reproduced from the full 6x6
   charge spectrum as the h_f = 0 case of the same map (s2 PARTD, ratios to
   26/17 and 226/145 agree to 1.110e-16).

Audit outcome for the prior-pass drafts (both were never passing their own
asserts; they are retained unmodified and superseded): s1_spectrum_wick.py
used a j-DEPENDENT factor 2^(2p+1-j); the correct spectral trace is
j-INDEPENDENT 2^(2p+1) — at p = 1 the draft gives 12a^2 + 4r against the
correct 16a^2 + 8r (re-derived independently in s1_spectrum_wick_r2.py, which
is exact symbolically for p = 1..6 even, p = 0..4 odd); its saved
s1_spectrum_wick.out is an AssertionError traceback at line 87.
s3_profile_concentration.py asserted rho_p <= prod(1+i/D_eff), which is
FALSE — counterexample g = (9/10, 1/10), p = 3: rho_3 = 123/25 > 3003/625,
excess 72/625; the superseded script fails its own assert with 384 violations
on its own profile list (reproduced exactly, seed 81003, in
s3_profile_concentration_r2.py).

Nothing is closed: Problem G and all its missing steps (i)-(iv) remain as
recorded; this package converts the 072-review gap "(4) closing the
E-moments<->Q-moments identification within the Gaussian-state model" from an
unquantified gap into a **conditional equivalence with a derived obstruction**
(exact at the second moment; strictly obstructed at every finite profile;
recovered at leading order in the concentrated-profile regime). Closes
nothing per rule 3.

## Target and status

Frontier edge `G.edge-moments` (reports/graph/frontier.yaml, chain-2 rank 1):
closing the E-moments<->Q-moments identification inside the Gaussian-state
model of the 065-block. Manuscript status, verbatim from
chapters/appH-microscopic-proofs.tex L3026-3029 and L3036-3041: "Status:
OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL.
Reduced-scope results: G-model and G-external support at most a
scope-limited model; G remains OPEN and neither satisfies the
matrix-derived criterion." / "The mechanism is CLOSED CONDITIONALLY under
the stated boundary entropy; derivation of the infrared entropy density and
stationarity from the matrix theory is OPEN. A boundary-model or externally
justified result is programme-conditional and supports only a
scope-limited model." Original target (Problem G, matrix-derived criterion):
derivation of the infrared entropy density and stationarity from the matrix
theory; the Missing step paragraph (L3119-3127) lists (i) derivation of the
Presentation-A cut / partial-M identification, (ii) the interacting
condensate sector of eq (eq:Smatrix), (iii) the stationarity condition
eq (eq:bdy-EE), (iv) the mass-dimension-one boundary-to-bulk conversion.
This package is DERIVED only inside its named hypothesis class (below) and
is PROGRAMME-CONDITIONAL for Problem G: it does not touch (i)-(iv).
Dependencies: the 065-block paragraphs L3132-3175 (row length, selection
rule, 072/076/077/078/079/080), the Gaussian state model of the Row length
paragraph, the 072 review gap list.

## Source reading

digest + targeted reads. scratch/digest.md was compact for this pass. Files
read in full for the parts relied on: chapters/appH-microscopic-proofs.tex
Problem G section (L3022-3180: ledger L3026-3041, bounded-obstruction
paragraph L3043+, Missing step paragraph L3119-3127, full 065-block
L3132-3175 including the Row length paragraph L3147 with
ell = 2|w_perp| and <ell^2> = 4 s^2 W, the selection-rule paragraph L3153-3161,
076 L3167 with w_f = k_f m_f (1 - m_f), 077 L3169, 078 L3171, 079 L3173,
080 L3175 with the signature-excess formula and 9/17, 81/145, the anchor
line L3177 and the block closer L3179); chapters/ch17-agenda.tex L474-495
(Problem G: CRITICAL PATH); reports/graph/frontier.yaml L402-417 and
chain-2 notes L838+; proposals/072-g-edge-resum-dominant-rep/review-r1.md
L35 (avenue (4)); reports/ledger.md G entries; prior proposal files 076-080
headers. Bibliography: no new citation is used or proposed (the Steinacker
record at the anchor line is untouched). Unreadable files: none.

## Research and reasoning

Hypothesis class (named exactly, restated in the insert's closing sentence):
(i) rank-one block-cut edge datum Q = -2i(|u)(w| - |w)(u|) of the Row length
paragraph with (u|u) = 1, a = Im(u|w), r = |w_perp|^2; (ii) Gaussian state:
a real centered Gaussian with V = <a^2>, independent of r, and
r = s^2 sum_i g_i E_i with E_i iid Exp(1), g = block-row profile, W = sum g —
this is the model under which the manuscript states <ell^2> = 4 s^2 W, since
<r> = s^2 W gives <ell^2> = 4 s^2 W; (iii) leading-order convention neglecting
Im alpha (the manuscript's own convention at L3147); (iv) band-separated caps
(the two-cap spectrum is the union of the single-cap pairs) and fixed depths /
fixed multiplicities; (v) fuzzy variance profiles f(l) are model proxies, not
derived geometry; (vi) inside the transplanted rule with its
single-dominant-diagram hypothesis and diagonal-cut convention, both at
leading semiclassical order.

Derivation. Q has rank at most 2 on span{|u>, |w>}. Writing w = (u|w) u + w_perp,
Writing w = (u|w) u + w_perp,
c = (u|w), r = |w_perp|^2 and a = Im c, the matrix of Q in the orthonormal
basis {|u>, w_perp/|w_perp|} is [[-4a, -2i|w_perp|], [2i|w_perp|, 0]]
(compute Q|u> and Q|w_perp> column by column): trace -4a, determinant -4r, so
the characteristic polynomial on the rank-two block is
lambda^2 + 4 a lambda - 4 r and the two nonzero eigenvalues are lambda_+/- = -2a +/- 2 sqrt(a^2 + r) as recorded at L3147.
Then Tr Q^(2p) = lambda_+^(2p) + lambda_-^(2p): the sqrt terms cancel and the
binomial sum collapses to the j-INDEPENDENT closed form
  Tr Q^(2p) = sum_{j=0}^{p} C(2p, 2j) 2^(2p+1) a^(2p-2j) (a^2 + r)^j,
because lambda_+^n + lambda_-^n = sum_j C(n, 2j) (2 sqrt(a^2+r))^(2j) (-2a)^(n-2j)
= sum_j C(n, 2j) 2^n (a^2+r)^j a^(n-2j). Similarly the odd trace is
  Tr Q^(2p+1) = - sum_{j=0}^{p} C(2p+1, 2j) 2^(2p+2) a^(2p+1-2j) (a^2+r)^j,
odd in a. Both verified symbolically in sympy against the eigenvalue pair for
p = 1..6 / 0..4 (s1_r2 PART1), and numerically against full spectra
(6.220e-15). The draft's 2^(2p+1-j) is wrong at every p >= 1; the discrepancy
at p = 1 is (16a^2 + 8r) - (12a^2 + 4r) = 4a^2 + 4r, matching the
orchestrator's test vector.

Gaussian average. a is independent of r and centered, and <r^m> = m! h_m(g s^2)
because a sum of independent scaled Exp(1) has power sums giving the complete
homogeneous symmetric polynomial h_m (Leray / generating-function identity,
verified exactly in scratch check and in s1_r2 PART2 against exact bivariate
moment integration). Wick's theorem on a^(2k) = (2k-1)!! V^k then yields the
closed form (star) in the s1_r2 docstring, exact to sympy zero at
mu = (2,3), V = 7/3, p = 1..4. At a = 0 the spectrum
collapse is exact and pointwise: Tr Q^(2p) = 2 ell^(2p) with ell^2 = 4r
(PARTA), so <Tr Q^(2p)> = 2 (4 s^2)^p <(sum g_i E_i)^p> and
<(sum g_i E_i)^p> = p! h_p(g) (s2 PARTB, exact rational at s^2 = 5/3).
This
gives <Tr Q^(2p)> = 2 (4 s^2 W)^p rho_p(g), rho_p = p! h_p(g)/W^p >= 1 with
equality iff p <= 1 (since p! h_p - W^p =
sum_{|alpha|=p} (p! - p!/alpha!) g^alpha > 0 for p >= 2 and g on at least two
slots), and the partition identity
rho_p = sum_lambda (p!/z_lambda) prod (s_k/W^k)^{m_k} from
h_p = sum_{lambda |- p} p_lambda / z_lambda: every partition term is positive,
hence 1 < rho_p; the p = 2 term of the partition sum is exactly
s_2/W^2 = 1/D_eff, giving rho_2 = 1 + s_2/W^2 = 1 + 1/D_eff, and
rho_3 = 1 + 3 s_2/W^2 + 2 s_3/W^3 (both verified as exact identities on 1000
the p = 3 partition sum gives exactly rho_3 = 1 + 3 s_2/W^2 + 2 s_3/W^3 (both
verified as exact identities on 1000 profiles, s3). Keeping only the p = 2
partitions: the single partition lambda = 2 * 1^(p-2) has p!/z_lambda =
C(p,2) and contributes exactly C(p,2) s_2/W^2 = C(p,2)/D_eff, all other
partition terms being positive) gives rho_p - 1 >= C(p,2)/D_eff.
Upper end: every monomial of h_p is a term of (g_1+...+g_D)^p = W^p, so
h_p <= W^p and rho_p <= p!, with equality for p >= 2 iff one slot carries all
the weight (where W^p = h_p = g_1^p). The uniform
profile g_i = 1/D gives rho_p = prod_{i=1}^{p-1} (1 + i/D) exactly (Newton
identities / rising-factorial ratio; exact check at D = 120, s3).

Comparison with the identification target. The E-moments (edge-data moments)
enter the transplanted selection rule through the claim that the charge
moments of Q are computed from the edge datum; in the manuscript's
leading-order convention the second-moment statement <ell^2> = 4 s^2 W
(L3147) is exactly the p = 1 case of item 2 (rho_1 = 1). What was missing
(072 review, avenue (4)) is whether the whole sequence is fixed by the edge
datum, i.e. whether <Tr Q^(2p)> = 2 (4 s^2 W)^p for all p. Within the named
class the answer is exact and negative: the ratio to that single-scale
prediction is exactly rho_p(g) > 1 at every p >= 2 and every non-degenerate
finite profile, bounded below by 1 + C(p,2)/D_eff. So the identification
holds exactly at p = 1, is obstructed with a computed coefficient at p = 2
(excess exactly 1/D_eff), and is recovered to leading order (relative error
O(1/D_eff) at fixed p) only in the concentrated-profile limit D_eff ->
infinity; for the fuzzy variance proxies f = nu l/2 (model proxies for the
variance profile of fuzzy-sphere-type blocks, not derived geometry) D_eff
grows with the cutoff from 105.8 (l_c = 10) through 1488.0 (l_c = 40) to
23016.9 (l_c = 160) and 365132.5 (l_c = 640), and the fourth-moment excess
drops 0.057766 -> 0.004037 -> 0.000261, tracking 6/D_eff as the bound
predicts. Whether the true block-row profiles of the matrix model are in the
concentrated regime is not derived: the profiles used here are proxies
assigned by hand, and W and g themselves are inputs of the state model, not
derived quantities (the state that fixes them is one of the open links).

080 reproduction. The per-factor signature-excess paragraph (L3175) states
the mixed/multiplicity-1 moment ratios 26/17 and 226/145 (excesses 9/17 and
81/145) at (q1,q2) = (2,1), (n1,n2) = (1/4,2/9) as a statement about the
full block. s2 PARTD builds the 6x6 charge Q = -2i(U R^dagger - R U^dagger)
from the 080 construction at A = 0, H = 0 (R = V K^(1/2) with V the
complement isometry, C0 = U^dagger R = 0, Z0 = K), obtains the spectrum
{+/- 2 sqrt(n_f)} with multiplicity q_f (max deviation 1.110e-16) and the
ratios 1.529411764706 and 1.558620689655 against 26/17 and 226/145. This
confirms the paragraph's "formula of the fourth paragraph above with n_f in
place of w_f" claim inside the h_f = 0 subclass, and it is the
multiplicity-weighted instance of the same moment map: for the union-of-pairs
spectrum the p-th even moment is sum_f q_f 2 (4 n_f)^p, and the ratio to the
unit-multiplicity sum is sum_f q_f n_f^p / sum_f n_f^p - here 26/17 and
226/145 (exact rationals, independent check by fractions arithmetic).

Literature: no external result is imported. The rank-one charge spectrum
re-derives the pair recorded at L3147 of the manuscript itself (attributed
there to the Fliss-Frenkel-Hartnoll-Soni Equation (4.4) edge charge); the
h_p / Exp-mixture identities and the partition identities are classical
symmetric-function identities (complete homogeneous symmetric polynomials,
h_p = sum_lambda p_lambda/z_lambda) checked here by exact computation rather
than cited. None of these literature identities was independently verified
against a published source in this pass: not independently verified as
attributions, verified as identities by the shipped exact computations.

No structural change to the NAMCG core is proposed. Spacetime remains
emergent: all objects are matrix/algebra data and the insert adds no
background or metric premise.

## Claim classification

- Spectrum pair lambda_+/- and the even/odd spectral trace polynomials
  (j-independent 2^(2p+1) / 2^(2p+2)): established identity (exact sympy
  verification p = 1..6 / 0..4, numeric 6.220e-15 on full spectra).
- Pointwise Tr Q^(2p) = 2 ell^(2p) and vanishing odd moments at a = 0;
  additivity over band-separated caps: established within the class
  (PARTA, 6.460e-15).
- <r^m> = m! h_m under the Exp-mixture model; Wick closed form (star):
  established identity under the stated Gaussian/Exp model (exact sympy).
- <Tr Q^(2p)> = 2 (4 s^2 W)^p rho_p(g), rho_p = p! h_p/W^p: conditional
  result, conditional on the Gaussian state model with profile g (exact
  rational check).
- rho_1 = 1 and the match to <ell^2> = 4 s^2 W: established conditional on
  the model; agreement with the manuscript's stated coefficient: comparison
  with repo text L3147.
- 1 < rho_p <= p!, rho_2 = 1 + 1/D_eff, rho_3 = 1 + 3/D_eff + 2 s_3/W^3,
  partition identity, rho_p - 1 >= C(p,2)/D_eff, uniform-profile product:
  established identities/inequalities with elementary proofs given above;
  sampled exhaustively on 1000 + 102 + proxy profiles, 0 violations.
- Fuzzy-proxy D_eff table and fourth-moment excess numbers: numerical,
  model-proxy inputs (input), not derived geometry; agreement with the
  bound 6/D_eff (conditional).
- 080 ratios 26/17, 226/145 from full spectra: established within the 080
  h_f = 0 subclass (exact rational identities + numeric spectra).
- "The identification is derived only at the second moment / obstructed for
  p >= 2 / recovered at leading order as D_eff -> infinity": exact logical
  consequence of the established items inside the named class; the
  extension beyond the class (general states, derived W and g, non-Gaussian
  correlations, selection rule, its transplant, missing steps (i)-(iv)) is
  unresolved.
- The assertion that the superseded scripts were wrong: established
  (reproduced failures, s3_r2 audit section).
- No claim is made about the emergent metric, the vacuum, or the state that
  fixes W and g: unresolved by design.

## Proposed changes

chapters/appH-microscopic-proofs.tex, one paragraph insertion. Anchor: the
unique line in the Problem G section that begins
`\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}` (live line 3177;
the string `\emph{Vacuum term.}` also begins a line at live line 3006 in the
Problem F block - not the anchor - so the package pins the anchor by the
unique preceding 080-paragraph tail
"per-factor depths only in the fixed-depth regime of the selection-rule
reading, and they close nothing in Problem~G."). Boundary: the paragraph
lands blank-CRLF-separated immediately after the 080 paragraph (L3175) and
immediately before the anchor line; everything above (through L3175) and
below (L3177-3179 closer) is kept unchanged. No other sentence is replaced;
no stale passage was found that contradicts the insert (the 072 paragraph's
recorded gap remains accurate; it is refined, not contradicted, so nothing
else is edited). Insert text (file insert-r1.tex, 3609 bytes, sha256
06e34e715a77c285f10337c55602cbd7e608e154dd5966424c611b1cea32fdd5, single
content line + terminal CRLF, zero occurrences of $, [, ], \cite, \ref,
\label, \eqref, and of the banned words except the closing idiom):

```latex
\emph{Charge-to-edge moment identification in the Gaussian rank-one class.} Within the Gaussian state model of the Row length paragraph - independent momenta with a variance profile, a cap block with block-row profile \(g\) of total weight \(W\) and edge datum \(s^{2}\), and the leading-order convention neglecting \(\operatorname{Im}\alpha\) - the identification of the moments of the classicalised edge charge with the edge data of the block cut, which the transplanted selection rule uses as input, is an exact moment map with one quantified profile obstruction. At the leading-order convention the nonzero eigenvalues of a single cap's charge are exactly \(\pm\ell\) with \(\ell=2|w_\perp|\) the row length, so the charge moment sequence is exactly \(2\ell^{2p}\) and all odd charge moments vanish, pointwise in the configuration; for the two band-separated caps of one axis the spectrum is the union of the two pairs and the moment sequences add. Over the Gaussian state, the averaged second moment is \(2(4s^{2}W)=8s^{2}W\), consistent through \(W\) alone with \(\langle\ell^{2}\rangle=4s^{2}W\) of the Row length paragraph, so the identification at the second moment - the one that fixes the row length - is exact in the model and carries no state dependence beyond the row-sum \(W\). Beyond second order the identification is obstructed exactly and strictly: with \(D_{\mathrm{eff}}=(\sum g)^{2}/\sum g^{2}\) and \(\rho_{p}(g)=p!\,h_{p}(g)/(\sum g)^{p}\), the averaged \(2p\)-th moment equals the edge-data single-scale prediction multiplied by \(\rho_{p}(g)\), and \(\rho_{p}-1\) is bounded below by \(C(p,2)/D_{\mathrm{eff}}\), equals \(1/D_{\mathrm{eff}}\) at \(p=2\), equals \(3/D_{\mathrm{eff}}+2s_{3}/(\sum g)^{3}\) at \(p=3\) with \(s_{3}=\sum_i g_i^{3}\), obeys \(1<\rho_{p}\le p!\) with the upper end attained at a single row, and has the exact partition form \(\rho_{p}=\sum_{\lambda\vdash p}(p!/z_{\lambda})\prod_{k\ge1}\bigl(s_{k}/(\sum g)^{k}\bigr)^{m_{k}}\) in terms of the power sums \(s_{k}\) and the multiplicities \(m_{k}\) of the parts of \(\lambda\vdash p\). The identification from edge data alone is therefore exact at the second moment, fails at the fourth by exactly \(1/D_{\mathrm{eff}}\), and is recovered at leading order only as \(D_{\mathrm{eff}}\to\infty\): for the fuzzy variance proxies \(f=\nu l/2\) the effective dimension grows with the cutoff, from \(1488\) at \(l_c=40\) to \(23017\) at \(l_c=160\), while the fourth-moment excess drops from \(4.0\times10^{-3}\) to \(2.6\times10^{-4}\) (numerical, on the exact rational profiles). The per-factor moment-signature identity of the mixed-multiplicity paragraph is the zero-imaginary-part case of the same map, reproduced from full charge spectra with excesses \(9/17\) and \(81/145\) at \((q_{1},q_{2})=(2,1)\), \((n_{1},n_{2})=(1/4,\,2/9)\). These statements are for the rank-one edge-datum family with independent Gaussian momenta and block-row profiles, at the leading-order convention neglecting \(\operatorname{Im}\alpha\), with band-separated caps and fixed multiplicities, inside the transplanted rule with its single-dominant-diagram hypothesis at leading semiclassical order and its diagonal-cut convention; the obstruction factor is exact for every finite profile, the identification from edge data holds exactly only at the second moment and at leading order in the concentrated-profile regime, they do not fix the state that sets \(W\) and \(g\), they leave the selection rule, its transplant and the missing steps (i)-(iv) of the Missing step paragraph unchanged, and they close nothing in Problem~G.
```

New labels: none added; no \ref used. The insert references paragraphs by
their headers ("Row length paragraph", "mixed-multiplicity paragraph",
"Missing step paragraph"), which exist verbatim in the live section.

## Verification scripts

All in this folder; run from the repository root with `python -I`
(numpy/sympy available in the project interpreter; all seeds fixed, no
network). All four .out files are byte-reproducible (verified twice with
`cmp`).

- s1_spectrum_wick_r2.py -> s1_spectrum_wick_r2.out.
  Invariants: "PART1 ... numeric max rel dev = 6.220e-15"; "PART2 ... exact
  equality (sympy, deviation 0)"; "PART3 ... pair sum of Tr Q^3 = 0.000e+00";
  last line "PASS s1". Checks the corrected j-independent spectrum
  polynomials (symbolic + numeric), the Wick closed form against exact
  bivariate integration, and odd-moment vanishing.
- s2_eq_moment_identity.py -> s2_eq_moment_identity.out (central script).
  Invariants: PARTA max dev 6.460e-15; PARTB "exact rational 0" with
  rho_1..rho_4 = [1, 25/18, 5/2, 301/54], D_eff = 18/7; PARTC "violations 0"
  and the fuzzy rows D_eff = 105.8 / 1488.0 / 23016.9 with excesses
  0.057766 / 0.004037 / 0.000261; PARTD ratios 1.529411764706 and
  1.558620689655 equal to 26/17 and 226/145, spectrum dev 1.110e-16; last
  line "PASS s2".
- s3_profile_concentration_r2.py -> s3_profile_concentration_r2.out.
  Invariants: rho_6(single) = 720; uniform D=120 rho_4 = 302621/288000 =
  prod(1+i/120); 1000-profile all-zero failure line; counterexample line
  "excess = 72/625 > 0"; "violations of the superseded bound = 384"; D_eff
  tables; last line "PASS s3".
- simulate_apply_081.py -> simulate_apply_081.out (read-only).
  PRE asserts: size 725541, sha256 f8797f82...df63ea1, CRLF 3826, bareLF 0,
  anchor count == 2 (L3006 Problem F, L3177 Problem G) with the L3177
  occurrence pinned by the unique 080 tail, header collision count 0.
  POST (computed, not written): size 729152, sha256
  5d52b67252b152751709dd2f7d22ccdd29e77df131d60fd43432d7583463a303, CRLF
  3828, bareLF 0. Prints "SIMULATED OK" and "no write performed". If the
  live file drifts from the PRE pins the script exits 1 with "LIVE PRE
  DRIFT".
- insert-r1.tex: the paragraph to be inserted, exactly as above;
  3609 bytes, sha256 06e34e71...; generator scratch/mkinsert081.py shows
  the forbidden-token scan result "NONE".

Superseded lineage (retained unmodified; never passed their asserts; do not
use for any claim): s1_spectrum_wick.py (5026 B, sha8 a81b490c) with its
stale s1_spectrum_wick.out (459 B, sha8 0207ecc6, an AssertionError
traceback at its line 87); s3_profile_concentration.py (4656 B, sha8
5a5efa00), whose headline bound is false (see Result). The draft s3 was
executed read-only once during the audit to reproduce its failure mode; its
files were not modified.

## Decisions Taken

1. Route: report the E<->Q identification as an exact conditional
   equivalence with a derived obstruction (exact at p = 1; strict
   obstruction rho_p >= 1 + C(p,2)/D_eff for p >= 2; leading-order recovery
   as D_eff -> infinity) rather than asserting the unconditional
   identification the gap suggested or leaving it purely as a gap. Favors
   the infrared derivation: it converts avenue (4) of the 072 review into a
   quantified, falsifiable statement inside the class and pinpoints the
   ingredient that would close it (a profile with D_eff -> infinity, or
   moments of the actual state beyond the Gaussian class).
2. Anchor multiplicity: the orchestrator's pin said the anchor line was
   unique; the live file has two line-start `\emph{Vacuum term.}` lines
   (L3006 in Problem F, L3177 in Problem G). The byte pins (size/sha/CRLF)
   match exactly, so this is a description error, not drift. Resolution:
   pin the L3177 occurrence by its unique preceding 080-paragraph tail and
   assert global count == 2. Chosen over moving the anchor (L3177 is the
   contract: after the 080 paragraph, before Vacuum term) and over
   asserting at the offset alone (the tail pin also guards against
   integration order changes upstream).
3. Superseded drafts kept on disk unmodified with a lineage record rather
   than deleted, so the gatekeeper can re-verify the audit claims (the j-dependent factor
   2**(2*p+1-j) at lines 41, 102 and 114 of the draft s1 — the odd coefficient
   wrong in exponent and sign too — and the false bound of draft s3) against the original
   bytes.
4. The uniform-profile minimiser claim (rho_p >= prod(1+i/D) for profiles of
   fixed block size) is sample-verified only (1000 profiles, 0 violations);
   it is reported in the scripts and this proposal but deliberately excluded
   from the manuscript insert, which only states what is proven
   (1 < rho_p <= p!, the defect lower bound, the uniform exact product).
5. Fuzzy variance profiles f(l) are model proxies assigned by hand for
   D_eff growth; they are reported as numerics in the insert with
   "numerical, on the exact rational profiles" and never presented as
   derived geometry.

## Milestone assessment

Routine. No MILESTONE.md trigger applies: no critical-path step is derived
from the matrix theory and no missing link is closed without new
unsupported inputs. The package records a conditional equivalence, a
derived obstruction inside a named class, and an audit that invalidates two
draft scripts.

## Status-label recommendation

Derived from ch17-agenda.tex (CRITICAL PATH entries at L123, L140, L330/344,
L378, L395, L404, L475, L498): A, B, C, D (D1), E, F, G, N, matching the
ledger snapshot. Affected labels: none. This package changes no status,
priority or completion label (rule 2); Problem G stays OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

To close the original target (Problem G matrix-derived criterion): the
missing steps (i)-(iv) of the Missing step paragraph (L3119-3127) are
unchanged and untouched by this package. Specifically for this edge:
(a) the state and profile that fix W and g in the matrix model — until they
are derived, W and g (hence every rho_p, including D_eff) are model inputs;
(b) whether the actual block-row profiles are in the concentrated regime
D_eff -> infinity, which is what would restore the higher-moment
identification at leading order — the fuzzy proxies here are hand-assigned
and give no such proof; (c) extension beyond the Gaussian rank-one class:
non-Gaussian ground-state correlations (missing step (ii)), finite V =
<a^2> corrections retained rather than dropped at the leading-order
convention, and Im alpha != 0 (the odd trace polynomial shows odd moments
are O(a) and vanish only at a = 0, so a non-centred or coupled a-sector
would inject odd-charge contributions the present map sets to zero); (d)
the uniform-minimiser inequality, currently sample-verified only, would
need a proof if a later package wants it as a lemma. None of these is
claimed or needed for the insert as written.

## Special instructions for the gatekeeper

Scope limits for the inserted paragraph: it must not be read as closing the
E<->Q identification for Problem G (it closes it only at the second moment
and at leading order in the concentrated regime, inside the named class);
it must not be read as deriving W, g, the state, the selection rule or its
transplant; the D_eff/fuzzy numbers are model-proxy numerics from the shipped
scripts. Re-check, please: (1) the spectrum polynomials (re-derive the pair
lambda_+/- and the j-independent factor independently — the buggy draft is
retained for contrast, lines 41/102/114); (2) rho_p - 1 >= C(p,2)/D_eff and
the p = 2, 3 identities by your own algebra (the partition proof is one
line); (3) the anchor contract: assert the live PRE bytes match the pins,
note the two line-start "Vacuum term." occurrences (L3006 Problem F is not
the anchor; L3177 is, pinned by the unique 080 tail), and confirm the
simulated POST differs from PRE only by the insert bytes + one CRLF; (4)
re-run all four scripts with `python -I` from the repo root and compare to
the shipped .out files (byte-identical expected); (5) the insert's
forbidden-token and banned-word scan (expect all zero, closing idiom "they
close nothing in Problem~G." allowed); (6) do not import any label change
from this package.
