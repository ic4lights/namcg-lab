# Proposal 084-g-moments-coupledmixed, round 1

## Result

For Problem G's moment programme (frontier chain-2 rank 2, `G.moments-coupled-mixed`) the package
names the coupling and computes it exactly. The named coupling is not an ansatz: it is the joint law
of \(a=\operatorname{Im}\alpha\) and \(r=|w_\perp|^{2}\) induced by the SAME independent Gaussian slot
momenta of the Row length paragraph (appH L3147). Five results, all verified symbolically and by
Monte Carlo (scripts s1-s4, all green):

1. **Mixed master map (algebra, no independence).** For every joint law of real \(a\) and \(r\ge0\),
   \(\langle\operatorname{Tr}Q^{m}\rangle=(-1)^{m}2^{m+1}\sum_{k\le m/2}\binom{m}{2k}\sum_{j=0}^{k}\binom{k}{j}
   \mathbb{E}\,a^{m-2k+2j}r^{k-j}\): the 083 map survives verbatim with \(A_nH_{k-j}\) replaced by mixed
   moments; independence was never used in the map itself. Explicit: \(\langle\operatorname{Tr}Q^{4}\rangle
   =32(\mathbb{E}r^{2}+8\,\mathbb{E}a^{2}r+8\,\mathbb{E}a^{4})\).
2. **Closed coupled data.** Under the induced law the pair contractions are
   \(\mathbb{E}a^{2}=s^{2}\mu/2\), \(\mathbb{E}\,a\,w_i=(\mathrm{i}s^{2}/2)g_iu_i\),
   \(\mathbb{E}w_iw_j^{*}=s^{2}g_i\delta_{ij}\) with \(\mu=\sum_ig_i|u_i|^{2}\), so every mixed moment is
   a Wick polynomial in finite data. \(\mathbb{E}\,ar=0\), but
   \(\mathbb{E}\,a^{2}r-(s^{2}\mu/2)\,\mathbb{E}r=(s^{4}/2)\Gamma\), \(\Gamma=\sum_i|u_i|^{2}(g_i-\mu)^{2}\ge0\).
3. **Characterization.** On this gaussian class, \(a\perp r\) if and only if \(\Gamma=0\), i.e.\ if and
   only if \(g\) is constant on \(\operatorname{supp}u\): 083's independence hypothesis holds in the
   literal model exactly in the uniform-support case - the same uniform profile that is 082's sharp
   minimiser of the obstruction factor.
4. **Correction budget.** The variance tie \(\mathbb{E}a^{2}=s^{2}\mu/2\) and \(\mathbb{E}r=s^{2}(W-\mu)\)
   keep \(\langle\operatorname{Tr}Q^{2}\rangle=8s^{2}W\) unchanged under the coupling; the first
   correction is at the fourth moment, where the coupled value exceeds the product-law value by exactly
   \(128s^{4}\Gamma\). For a uniform frame \(u\), \(\Gamma=(W^{2}/D)(D_{\mathrm{eff}}^{-1}-D^{-1})\), so the
   coupling correction is controlled by 081's effective dimension and vanishes exactly at the uniform
   profile.
5. **Odd-sector upgrade.** \(w\mapsto-w\) (momentum sign flip) sends \(Q\mapsto-Q\); hence every averaged
   odd charge moment vanishes for ANY sign-symmetric slot law - no independence, no gaussianity. 083's
   centred vanishing is a flip symmetry, not an independence statement.

Nothing on the critical path is closed; W, g, s and the frame u remain inputs of the named state class.

## Target and status

- Target: frontier `reports/graph/frontier.yaml` chain-2 rank 2 `G.moments-coupled-mixed` (rows
  L505-522): "requires a named coupling law between Im α and the slot radii plus mixed moments ...
  no coupling is named in the repository ... the 083 map survives verbatim with A_nH_{k-j} replaced
  by mixed moments". This package names the coupling (the canonical induced one) and computes the
  mixed moments.
- Rank 1 `G.moments-derivedprofile` was assessed and NOT taken as the derivation target this round;
  the assessment, its hypothesis decomposition and the open avenues are in "Decisions Taken" 1 and
  "Remaining open step". Per the dispatch, rank 1 was to be attacked only via "the strongest package
  that constrains it"; this package carries such constraints (variance tie; r-marginal law with
  compressed weights) and registers them.
- Problem G status as read live from appH L3026-3029: `Status: OPEN. Priority: CRITICAL PATH.
  Completion: PROGRAMME-CONDITIONAL`; ch17 criterion (L474-495): entropy density + boundary
  stationarity from matrix theory. Nothing here engages those labels.
- Classification of this package: DERIVED inside the named coupled gaussian class (exact algebra plus
  exact Wick evaluation, scripts green); PROGRAMME-CONDITIONAL for G; inputs: profile g, edge datum
  s², frame u, slot-count D. Does not close, narrow or re-scope G.

## Source reading

Digest + targeted reads. `python scripts/make_digest.py --check` was reported DIGEST CURRENT by the
orchestrator at dispatch; digest consulted for navigation only. Read in full: appH L3140-3159 (Row
length, State and coarse-graining, Bearing, Selection-independence, Robustness paragraphs, live text)
and L3175-3188 (081/082/083 integrated paragraphs, Vacuum term, block closer, Problem H header); the
083 ledger/status passages L3025-3041 and the Missing-step paragraph L3119-3130 (carried from earlier
in the run); `chapters/ch17-agenda.tex` L474-495; `reports/graph/frontier.yaml` chain-2 rows for
`G.moments-derivedprofile` (L487-504), `G.moments-coupled-mixed` (L505-522), `G.moments-finiteV`
(L523-540); `proposals/083-g-moments-aoddsector/review-r2.md` (full, incl. scope section and byte
contract), `proposals/083-g-moments-aoddsector/s2d_oddmap.py`, `proposals/083-g-moments-aoddsector/
simulate_apply_083.py`, `proposals/081-g-edge-moments/s1_spectrum_wick_r2.py` (convention anchor:
a = Im(u|w), r = |w|^2 - |(u|w)|^2 = |w_perp|^2, spectrum -2a +/- 2(a^2+r)^{1/2});
`reports/sme-scout-20261118-0228.md` (full). Earlier proposals 081/082/083 reviews consulted for
scope language and integration precedent. No unreadable files.

## Research and reasoning

**Model class (from the integrated Row length paragraph, L3147, no new premises).** The paragraph
gives Q = -2i(|u)(w| - |w)(u|), w = sum_a c^a (v|Pi^a) restricted to the block, alpha = (u|w),
w_perp = w - alpha u, spectrum -2 Im alpha +/- 2(Im^2 alpha + |w_perp|^2)^{1/2}, for a Gaussian state
in which the Pi^a are independent with variance profile f(l). Inside the block, the row vector w is
therefore a complex gaussian whose slot coordinates are independent with variances s^2 g_i (the
block-row profile g of the 081 paragraph), and u is the fixed unit frame vector of the rank-one datum
(a supplied input of the Presentation-A class, as in 081). Everything below is computed in this class;
the slot-count is D, W = sum g_i.

**Step 1 - the map is algebra (s1).** From the spectrum, Tr Q^m = e_+^m + e_-^m with
e_pm = -2a +/- 2 sqrt(a^2+r), a polynomial in (a, r) with integer coefficients (odd powers of the
root cancel). Collecting, Tr Q^m = (-1)^m 2^{m+1} sum_k C(m,2k) sum_j C(k,j) a^{m-2k+2j} r^{k-j}.
No probabilistic input: this is the 083 master map with A_n H_{k-j} -> E[a^n r^j]. s1 verifies the
identity for m = 1..9 and prints the exact coefficient vectors; at m=2: 16 a^2 + 8 r; at m=4:
32(r^2 + 8 a^2 r + 8 a^4), i.e. coefficients (M40, M21, M02) = (256, 256, 32).

**Step 2 - induced pair data (s2, exact Isserlis).** alpha = sum_i conj(u_i) w_i with
E[w_i w_j^*] = s^2 g_i delta_ij and E[w_i w_j] = 0 gives E|alpha|^2 = s^2 mu, mu = sum g_i|u_i|^2.
Since a = (alpha - alpha^*)/(2i): E[a^2] = E|alpha|^2/2 = s^2 mu/2 (variance tie); E[a w_j] =
-E[alpha^* w_j]/(2i) = (i s^2/2) g_j u_j; E[a w_j^*] = -(i s^2/2) g_j conj(u_j). These three plus
E[w_i w_j^*] are ALL pair contractions of (a, w_1,..,w_D, conj(w_1),..), so every mixed moment
E[a^n r^j], j-power of r = sum|w_i|^2 - |alpha|^2, is a finite Wick sum - the coupled map is closed.

**Step 3 - the coupling functional (s2, ds1/ds2 exact rational datasets).** E[a r] = 0 (third-order
Isserlis, identically). E[a^2 r]: pair the two a's with each other (contribution (s^2 mu/2) E r) or
cross (sum_j 2|E[a w_j]|^2 from |w_j|^2, minus the |alpha|^2 part (s^4/2) mu^2):
E[a^2 r] - (s^2 mu/2) E[r] = (s^4/2)(sum_i g_i^2|u_i|^2 - mu^2) = (s^4/2) Gamma,
Gamma = sum_i |u_i|^2 (g_i - mu)^2 >= 0 (weighted variance of g on supp u). s2 confirms both
identities exactly for two non-uniform datasets (D=2 complex frame, Gamma = 4/25; D=3 real frame,
Gamma = 53/729) and zero for a uniform-g dataset.

**Step 4 - independence iff uniform-on-support (theorem; moment checks in s2 ds3).** (<=) If
g = const on supp(u): E[alpha^* w_perp,j] = conj(u_j) s^2 (g_j - mu) = 0 and E[alpha w_perp,j] = 0,
so the joint complex-gaussian vector (alpha, w_perp) has block-diagonal covariance and vanishing
pseudo-covariances (E alpha^2 = 0): alpha and w_perp are independent; a is a function of alpha,
r of w_perp. (=>) independence forces Cov(a^2, r) = 0, i.e. (s^4/2) Gamma = 0, i.e. g constant on
supp(u). So the product law of the 081/082/083 class is exactly the uniform-support locus of the
literal model - a named, exact boundary between the repository's Gaussian state class and its own
Row length paragraph.

**Step 5 - moment budget (s2, s3, s4).** With E[a^2] = s^2 mu/2 and E r = s^2 (W - mu):
<Tr Q^2> = 16 E a^2 + 8 E r = 8 s^2 W - unchanged by the coupling, and identical to the 081
second-moment identification (s3 measures 32.5623 vs 32.5888, |z| = 1.33). At m = 4, using
E a^4 = 3 V^2 (a is exactly gaussian, a linear form of gaussians): coupled <Tr Q^4> equals the
product-law value plus 32 * 8 * Cov(a^2, r) = 128 s^4 Gamma exactly (s2 symbolically, s3 Monte
Carlo: measured gap 3.66 vs predicted 2.95, |z| = 1.07 on 600k samples, D = 6). For the uniform
frame, Gamma = (1/D) sum(g_i - W/D)^2 = (W^2/D)(1/D_eff - 1/D) with D_eff = W^2/sum g_i^2 of 081
(s4, exact rational check, D = 3, 4), so both 081's fourth-moment obstruction 1/D_eff and this
coupling correction are governed by the same profile non-uniformity and both vanish exactly at
082's uniform profile.

**Step 6 - flip symmetry replaces the independence in the odd sector (s1 flip rows, s3 odd rows).**
The slot law of the class is invariant under w -> -w (momentum sign flip, Pi -> -Pi); Q is linear in
(w, w^*), so Q -> -Q pointwise and Tr Q^m -> (-1)^m Tr Q^m. Averaging over any sign-symmetric law
gives zero for every odd m. s1 checks TrQ^m(-a, r) = (-1)^m TrQ^m(a, r) symbolically for m = 1..9
(flip fail count = 0); s3 measures <Tr Q> = 2.88e-4 (|z| = 0.09) and <Tr Q^3> = 9.77e-2 (|z| = 0.49,
large per-sample variance) at D = 6, coupled. This strictly extends 083's centred vanishing: that
needed a symmetric a-law AND independence from r; the flip gives it with neither. Non-centred slot
means or 083-type slot displacements break the flip exactly as they should - 083's odd content is
then the symmetry-breaking term, consistent, not contradicted.

**Step 7 - marginal law of r: compressed slot weights (recorded for chain-2 rank 1).** w is complex
gaussian, so r = w^* P w with P = 1 - u u^* a rank-(D-1) projector is a gaussian quadratic form: its
law is the Exp-slot sum with weights nu_j = the nonzero eigenvalues of D_g^{1/2} P D_g^{1/2},
sum nu_j = s^2 (W - mu); the slot count drops from D to D-1. For non-uniform g these are NOT the
weights s^2 g_i that appear in the 081/083 kernel - that kernel is the Gamma = 0 marginal - so any
finiteV/derivedprofile convention built on the kernel must use nu off the uniform locus. (Standard
complex-gaussian quadratic-form fact, applied not re-proved; s2 evaluates E r and E r^2 for its
datasets by direct Isserlis and they match s^2(W-mu) and the nu-weights prediction.)

**Step 8 - relation to the integrated 083 paragraph (no edit, no stale text).** 083 remains true on
its stated product-law hypothesis. This package shows the product law is exactly the Gamma = 0
locus of the literal Row length model, so whenever g is non-uniform on supp(u) - any non-flat
profile with full-support frame - the repository's own gaussian momenta give a coupled law that
083's hypothesis excludes. Inside the centred coupled class the mean abar of 083 vanishes unless a
slot mean is supplied, and the slot shifts c_i are incompatible with the flip unless their law is
sign-symmetric. Consequences for chain-2 rank 1 (derivedprofile), recorded here because the dispatch
asked for the strongest package constraining it: the free data of the named state class shrinks -
the variance parameter is not free (tie E a^2 = s^2 mu/2), the r-kernel weights are nu(g, u) not
s^2 g, and the state input reduces to (f, l_c, frame u) as the State and coarse-graining paragraph
already says. Still nothing derives g or W from the matrix theory: this is a constraint on the
parameterisation of the state class, not a selection of it.

**Literature.** No new external input is used and no citation is introduced (rule 7: nothing to
verify, nothing unverified). Isserlis/Wick and the complex-gaussian quadratic-form law are classical
and already underlie the verified scripts of 081. Scout routes R1/R2 (profile-proxy papers,
sme-scout-20261118-0228) were considered and rejected as derivation inputs: they are analogy-level
and the frontier row itself records the profile as supplied by nothing upstream; R10/R11 carry the
EMERGENCE CAUTION and were not used; Xu-Yao majorization (R6) is not used anywhere here.

## Claim classification

- Mixed master map for every joint law of (a, r): established identity (s1, m <= 9, pattern to all
  orders from the spectrum polynomial).
- Pair contractions E a^2 = s^2 mu/2, E a w_j = (i s^2/2) g_j u_j, E w_i w_j^* = s^2 g_i delta_ij:
  established derivation inside the named slot law.
- E[ar] = 0; Cov(a^2, r) = (s^4/2) Gamma; <TrQ^2> = 8 s^2 W tie; <TrQ^4> coupled = product +
  128 s^4 Gamma: established derivations, exact-checked (s2 rational, s3 Monte Carlo).
- a independent of r iff Gamma = 0 iff g constant on supp(u) (within the class): established, both
  directions proved; factorization spot-checked in s2 (uniform-g dataset, fail = 0).
- Odd averaged moments vanish for any sign-symmetric slot law: established (pointwise flip +
  averaging).
- r-marginal = Exp-slots with weights nu, D-1 slots: established standard fact applied to the class;
  the identification "the nu, not s^2 g, are the off-uniform kernel weights" conditional on the
  named slot law.
- Uniform-frame identity Gamma = (W^2/D)(1/D_eff - 1/D): established algebraic identity (s4, exact
  rational).
- Reading the Row length paragraph's w as slot-independent complex gaussians with variances s^2 g_i:
  conditional - it is the 081 model idealization applied to the integrated L3147 object; inherits
  081's scope caveats (state, l_c, frame supplied; the f(l) spin structure compressed to the block
  row).
- Any statement that the matrix theory selects g, W or u: NOT claimed (unresolved upstream).

## Proposed changes

**File: `chapters/appH-microscopic-proofs.tex` - one insertion, zero edits, zero deletions.**

Anchor. The 083 paragraph (L3181) ends with the sentence that occurs exactly once in the file
(verified by search, count = 1):

> The mean, the variance and the slot shifts are inputs of the named state class, they do not fix the state that sets \(W\) and \(g\), leave the missing steps (i)-(iv) of the Missing step paragraph unchanged, and they close nothing in Problem~G.

it is followed by exactly one blank line (CRLFCRLF, asserted) and then, at line start,
`\emph{Vacuum term.}` (L3183). The other occurrence of `\emph{Vacuum term.}` (L3006, Problem F) is
NOT the anchor; the simulate script pins the G-side one by searching only after the 083 tail. The
new paragraph is spliced between them: insert bytes + one CRLF immediately before the line-start
`\emph{Vacuum term.}`. Everything existing is kept, including the whole 083 paragraph (true under
its stated hypothesis; the new paragraph states the relation, so no stale passage arises anywhere -
checked: no other passage in the block asserts independence as a property of the literal model).
Post-splice geometry: new paragraph at L3183, Vacuum term L3185, block closer L3187, Problem H
section header L3189. No `\ref`, `\cite` or `\label` is added or touched (the insert contains
none), so no label verification burden and no duplicate-label risk.

Insert file: `proposals/084-g-moments-coupledmixed/insert-r1.tex` - single content line + terminal
CRLF, 2,332 B, sha8 0a7396c4, UTF-8 no BOM. Verbatim content:

```latex
\emph{Induced coupling of the imaginary-part and slot data of the rank-one Gaussian edge charge.} The preceding paragraph assumes a Gaussian \(\operatorname{Im}\alpha\) independent of the slot radii; the same Gaussian momenta of the Row length paragraph induce a definite coupling, and here is what survives without independence. Take slots \(w_{i}\) independent complex gaussian with \(\mathbb{E}\,w_{i}w_{j}^{*}=s^{2}g_{i}\delta_{ij}\) and a fixed unit frame vector \(u\), set \(\alpha=(u|w)\), \(a=\operatorname{Im}\alpha\), \(r=|w|^{2}-|\alpha|^{2}\), \(\mu=\sum_{i}g_{i}|u_{i}|^{2}\) and \(\Gamma=\sum_{i}|u_{i}|^{2}(g_{i}-\mu)^{2}\). The averaged map of the preceding paragraph holds verbatim with \(A_{n}H_{k-j}\) replaced by the mixed moments \(\mathbb{E}\,a^{n}r^{j}\): it is algebra, independence enters nowhere in it, and the mixed moments are Wick polynomials in the pair contractions \(\mathbb{E}\,a^{2}=s^{2}\mu/2\), \(\mathbb{E}\,a\,w_{i}=(\mathrm{i}s^{2}/2)g_{i}u_{i}\), \(\mathbb{E}\,w_{i}w_{j}^{*}=s^{2}g_{i}\delta_{ij}\), so the coupled map closes on finite data. \(\mathbb{E}\,a\,r=0\), but \(\mathbb{E}\,a^{2}r-(s^{2}\mu/2)\,\mathbb{E}\,r=(s^{4}/2)\Gamma\), and within this gaussian class \(a\) and \(r\) are independent if and only if \(\Gamma=0\), i.e.\ if and only if \(g\) is constant on the support of \(u\) - the product law of the preceding paragraph is the uniform-support case of the induced law. The tie \(\mathbb{E}\,a^{2}=s^{2}\mu/2\) keeps \(\langle\operatorname{Tr}Q^{2}\rangle=8s^{2}W\) of the third paragraph above, the first correction appears at \(\operatorname{Tr}Q^{4}\), where the coupled value exceeds the product-law value by \(128s^{4}\Gamma\), equal for a uniform frame to \(128s^{4}(W^{2}/D)(D_{\mathrm{eff}}^{-1}-D^{-1})\) and therefore zero exactly at the uniform profile of the second paragraph above. Flipping the sign of the momenta sends \(Q\) to \(-Q\), so the averaged odd moments vanish for any sign-symmetric slot law, coupled or not, and the centred vanishing of the preceding paragraph needs no independence. These statements tie the variance parameter of the named state class to the profile and the frame, they do not fix the state that sets \(W\) and \(g\), leave the missing steps (i)-(iv) of the Missing step paragraph unchanged, and they close nothing in Problem~G.
```

Hygiene of the insert (all machine-checked): one `\emph{...}` header only; zero `$`, `[`, `]`,
`\cite`, `\ref`, `\label`, `\eqref`; zero status/priority/completion/critical/open/programme/derived
words; ends with the block close idiom "close nothing in Problem~G." (count PRE 11 -> POST 12);
positional cross-references follow the integrated 081/082/083 convention (preceding paragraph =
083, second paragraph above = 082, third paragraph above = 081, Row length paragraph = L3147).

## Verification scripts

All scripts live in `proposals/084-g-moments-coupledmixed/`; run from the repository root with
`python -I` (isolated mode - protects against any planted module on the path). Each has a saved
`.out` from the run recorded in `manifest.md`.

- `s1_coupled_map.py` - sympy: spectrum polynomial Tr Q^m in (a, r) (x = a, t^2 = r via the explicit
  2x2 Q of 081/083 convention), mixed-map identity and flip identity for m = 1..9, coefficient print.
- `s2_induced_joint.py` - sympy exact rational Isserlis on three datasets (ds1 D=2 complex frame
  Gamma=4/25; ds2 D=3 real frame Gamma=53/729; ds3 uniform-g Gamma=0): checks ar0, Vtie, E_r,
  cov_a2r, a4, tr4_excess, gam and the uniform-g factorization to checked orders.
- `s3_monte_carlo.py` - numpy MC, seed 20261118, D=6, N=600000, s^2=1.7: nine est-vs-pred z-rows and
  the coupled-vs-product tr4 gap row, all |z| < 5 required.
- `s4_uniform_frame.py` - sympy exact rational: Gamma = (W^2/D)(1/D_eff - 1/D) for D = 3, 4 random
  rational profiles; D=2 general-weight square form; Gamma(g1=g2) = 0.
- `simulate_apply_084.py` - READ-ONLY byte simulation of the integration: pins PRE appH
  (733,361 B, sha c35bfed0...), pins the 083 tail (count 1) and the CRLFCRLF gap, splices insert +
  one CRLF before the line-start `\emph{Vacuum term.}`, prints POST size/sha, CRLF count, close-idiom
  counts; writes nothing.

Reproduction pack (exact commands -> expected invariant outputs):

    python -I proposals/084-g-moments-coupledmixed/s1_coupled_map.py
      -> "m=4 coeffs M(n,j): {(4, 0): 256, (2, 1): 256, (0, 2): 32}";
         "S1 invariant 1: mixed-map fail count = 0"; "S1 invariant 2: flip fail count = 0"; "S1 OK"
    python -I proposals/084-g-moments-coupledmixed/s2_induced_joint.py
      -> "ds1 D=2 complex-u Gamma=4/25 {... all True}"; "ds2 D=3 real-u Gamma=53/729 {... all True}";
         "ds3 uniform-g Gamma=0 {... gam': False}"; "S2 OK"
    python -I proposals/084-g-moments-coupledmixed/s3_monte_carlo.py
      -> "<trQ2> = 8 s2 W   est  32.5623 pred  32.5888  |z| 1.33";
         "Gamma = 0.0079777 ; measured tr4 gap = 3.66061 ; predicted 128 s^4 Gamma = 2.95111 ; gap |z| vs pred 1.07"; "S3 OK"
    python -I proposals/084-g-moments-coupledmixed/s4_uniform_frame.py
      -> "D=3 profile ['1/2', '2/3', '5/7']: Gamma = 67/7938, identity vs (W^2/D)(1/D_eff-1/D): True";
         "S4 invariant: identity fail count = 0"; "S4 OK"
    python -I proposals/084-g-moments-coupledmixed/simulate_apply_084.py
      -> "PRE OK size 733361 sha8 c35bfed0"; "POST size 735695 sha8 a13240a7 CRLF 3834 bareLF 0";
         "close-idiom count PRE 11 POST 12"; "insert bytes 2332 sha8 0a7396c4"; "no write performed"

s3 is deterministic given the seed; if numpy RNG streams ever change, the invariants to check are
the |z| bounds (all < 5), not the printed digits. Tool output is a check, not a proof; the proofs
are the derivations in "Research and reasoning".

## Decisions Taken

1. **Target: chain-2 rank 2 (coupled-mixed) as the derivation, rank 1 (derivedprofile) constrained,
   not derived.** RESEARCHER-DECISION resolved autonomously. Rank 1's original target - obtain the
   entropy profile from the matrix theory - requires the selection of g (or of the state), and
   nothing upstream supplies it: it sits at missing-step-(ii) level, and the frontier row itself
   records the profile as supplied by nothing upstream; a derivation cannot start there this round.
   Decomposition of the rank-1 obstruction by hypothesis: state input (supplied), slot law (gaussian
   idealization), profile selection (absent), frame (supplied), presentation (kernel). This package
   attacks the slot-law hypothesis (relaxed from product to induced law) and tightens the state
   parameterisation (variance tie, nu-weights) - the dispatch's "strongest package that constrains
   it". Rejected alternatives: (i) presenting a literature proxy profile as derived (would be a fit,
   not a derivation, and rule-invalid); (ii) a scope change making the profile optional (core change,
   not proposed). Open avenues for rank 1, ranked: matrix-theory selection mechanism for f(l) (the
   real target, upstream, unresolved); non-gaussian slot laws (flip and map survive; only Wick
   closure is lost - replaced by finite higher cumulants); finite-V/D_eff scaling bridge to 082;
   frame-averaging of u. None closed here.
2. **The named coupling is the canonical induced law, not an ansatz.** RESEARCHER-DECISION. The
   only coupling faithful to the Row length paragraph is the joint law of (a, r) induced by the same
   gaussian momenta - it adds zero free parameters and yields an exact Gamma-functional with an
   iff-characterization of the independence locus. Rejected: (i) an ad-hoc linear-correlation or
   Gaussian-copula law for (a, r) (unphysical: a and r are not jointly gaussian; E[ar] = 0 exactly
   while Cov(a^2, r) != 0 - a linear-correlation ansatz would name the wrong thing); (ii) keeping
   independence and just recomputing (zero content, and false off the uniform locus); (iii) a
   maximal-entropy coupling with fixed marginals (adds an arbitrary entropy criterion; the induced
   law is what the model gives).
3. **Presentation: new paragraph, 083 untouched.** 083's claims are correct under its stated
   hypothesis; the honest relation is "083 = the Gamma = 0 locus", stated in a new paragraph in the
   same house pattern as 082 extended 081. Rejected: editing 083's text (rewriting an accepted
   conditional result to weaken it would misrepresent it; rewriting to strengthen the hypothesis
   mention was unnecessary - the new paragraph carries the cross-reference).
4. **Cross-reference style.** Positional phrases per integrated convention, verified against 083's
   own use ("the second paragraph above" = 081). Anchor: full 083 tail sentence (count 1) + the
   gap assert, never the 4x-repeated suffix "do not fix the state that sets" (ambiguous).

## Milestone assessment

Routine. No MILESTONE.md trigger applies: the package is a conditional-class derivation inside the
same named gaussian state class as 081/082/083 (exact algebra plus exact Wick evaluation); it closes
no critical-path step, closes nothing in Problem G, and introduces no new object at the core level.
It is frontier progress on chain-2 rank 2 (coupling named, mixed moments computed, independence
locus characterized exactly) and a registered constraint on rank 1.

## Status-label recommendation

Derived live: Chapter 17 full-GR criterion (L474-495) lists A, B, C, D1, E, F, G-derived, N; the
Appendix H Problem G entry (L3026-3029) reads Status: OPEN / Priority: CRITICAL PATH / Completion:
PROGRAMME-CONDITIONAL, and the Missing step paragraph (i)-(iv) is unchanged by this package.
**All labels unchanged** - this proposal requests no status, priority or completion-classification
edit anywhere (rules 2, 3). G stays OPEN/CRITICAL PATH/PROGRAMME-CONDITIONAL.

## Author decision needed

None. All choices taken were routine (route, method, presentation, wording) and recorded in
"Decisions Taken"; nothing here touches the NAMCG core, Chapter 17 scope, the critical-path set or
any label; spacetime remains emergent throughout (the frame u and metric data stay derived-side
inputs of the named state class; no fundamental metric is introduced).

## Remaining open step

Problem G's original target (entropy density + boundary stationarity of the emergent profile from
the matrix theory, ch17 criterion) is untouched: missing steps (i)-(iv) of the Missing step
paragraph all remain open, and this package's class inputs (g, W, s^2, frame u, D) stay supplied.
What the coupled-mixed target still lacks is nothing - it is now computed for the induced gaussian
law; its natural extensions (each a new package) are: (a) non-gaussian sign-symmetric slot laws
(map and flip survive; mixed moments need the slot law's higher cumulants - no closure claimed);
(b) chain-2 rank 1 proper: a matrix-theory selection of the profile f(l) (the upstream problem,
ranked first in Decisions Taken 1); (c) finite-V scaling bridge of the 128 s^4 Gamma term against
the 1/D_eff obstruction at the profile level; (d) frame u averaging. The Γ = 0 locus means every
081/082/083 statement survives verbatim at the uniform profile - the coupled correction is exact
and quantitative, not a retraction.

## Special instructions for the gatekeeper

- Re-derive independently: (1) the m = 4 coefficient vector (256, 256, 32) on (M40, M21, M02), i.e.
  <TrQ^4> = 32(E r^2 + 8 E a^2 r + 8 E a^4), from the explicit 2x2 Q - a one-line trace check;
  (2) Cov(a^2, r) = (s^4/2) Gamma by direct Isserlis (the cross-Wick route in Step 3 is short -
  verify the sign and the factor 1/2 against E a^2 = s^2 mu/2); (3) the iff: check the complex
  gaussian criterion used (block-diagonal covariance AND vanishing pseudo-covariances E[alpha^2] =
  E[alpha w_perp,j] = 0) - this is where a hidden assumption could live.
- The insert asserts no closure; verify the insert contains no banned token/word and no status word,
  that its positional cross-references resolve (083 = preceding, 082 = second above, 081 = third
  above in the post-splice file), and that the 083 paragraph is byte-unchanged.
- Byte contract: PRE must be 733,361 / c35bfed0... at integration time; if the tree moved, re-pin
  before applying (the 083 tail pin, not the Vacuum-term line number, is the contract).
- Do not let any passage in the integrated text (this or any other proposal) be read as closing or
  narrowing G, and do not import "the model IS gaussian slots" as an established core fact: it is
  the 081 idealization applied to the L3147 object (conditional class).
- s3 digit-level invariants depend on the numpy RNG stream; check the |z| bounds, not the digits.
