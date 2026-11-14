# Proposal 067-product-sphere-edge, round 2

Revision of `proposal-r1.md` after `review-r1.md` (ACCEPT WITH REQUIRED REVISIONS, findings F1-F6, snippets S1-S4).
The exact lemmas and their derivations (r1 sections 2-5) are unchanged and are not repeated; this file records what
changed, the new evidence, and the full required sections. The manuscript text to integrate is
`appH_insert_r2.tex` (r1's `appH_insert.tex` is kept untouched for the diff).

## Change list (finding -> fix)

| Finding | Severity | Fix in r2 | Where |
|---|---|---|---|
| F1 | major | Range statement removed. Text now states the seven sampled pairs (S1), with the upper end of the sub-additivity factor corrected from 0.98 to 0.99 (the sampled maximum is 0.98203, see below), and adds the extrema actually found on a full 8 x 7 x 2 grid (new script e5), explicitly "values at the points evaluated, not bounds over a range". | insert, Dimension; `e5_dimension_grid.py` |
| F2 | major | Evidence alternative taken, and the wording restricted to what the pack shows. New Monte Carlo (e6 Part B) on blocks with inequivalent edge sites: oblique half-planes and product blocks, N = 12 and 16, two states, nu_2/nu_1 = 1 and 3 (32 cases). Bearing (i) is restricted to the cap x sphere and the sampled half-planes; product blocks are stated as an estimate with a deficit of up to 22%; everything else is stated as untested. (ii) opens "With that proviso" (S2). | insert, Rows and Bearing (i), (ii); `e6_rows_scan.py` |
| F3 | major | S3 added verbatim at the end of Bearing (iv). The md now says in Result, Target and the fork table that 067 does not leave the 065 class clause "compact internal factor with positive contraction" and that G.spacetime-block (065 avenue 1) remains untried. | insert, Bearing (iv); md throughout |
| F4 | minor | S4: "at the same \(M\)" inserted in Bearing (iii) (and it is also in the F1 sentence). | insert, Bearing (iii) |
| F5 | minor | md gloss corrected: 065 avenue 1 is "a spacetime-block subsystem (a 4D region x fibre, with a 3D edge)"; 067 is a compact proxy that tests only the edge-dimension aspect of it. | md, Result |
| F6 | optional | N = 8, 12, 16 scan added to the pack (e6 Part A) and quoted in Rows. | insert, Rows; `e6_rows_scan.py` |
| Observation (duplicate closing sentence) | none | no action, as the review states. | - |

One deviation from the review's snippets, with reason. S1 says "by a factor between 0.69 and 0.98 in these cases".
The sampled values are 0.69173 ... 0.98203 (e5 block (b); e4 prints the latter as 0.9820), so 0.98 is exceeded in
the fourth decimal. The text says "between 0.69 and 0.99". No other departure from S1, S3, S4. S2 is extended
by the new evidence rather than used verbatim (the review allows either).

A typesetting change with no content: the lists of pairs are set as separate inline formulas, because the S1 list as
a single formula produced one overfull hbox of 96 pt in the scratch build (see `build_r2.txt`).

## Result

Follow-up of 065 (bounded no-go for the relational block entropy of Fliss-Frenkel-Hartnoll-Soni, arXiv:2408.05274,
on a compact fuzzy factor). 065's open avenue 1 is "a spacetime-block subsystem (a 4D region x fibre, with a 3D
edge)". **067 is not that avenue.** It is a compact proxy for one aspect of it: it keeps the 065 clause "compact
internal factor with positive contraction" and relaxes (a) the dimension of the factor, 2 -> 4, so that the edge of a
block is three-dimensional, and (b) the clause "single projector or coaxial cap pair" -> toric blocks. The setting is
the product of two deformed fuzzy spheres, X^I = (A_1 J (x) 1, 1 (x) A_2 J), with delta_IJ. The block is a region of
that compact factor, not of the emergent spacetime; its edge is not dM. G.spacetime-block remains untried.

**Mixed outcome within that class: one cause of the 065 no-go is removed (for the tested blocks), two persist, and
the measure is identified.**

Established, exact at finite N (unchanged from r1; verified by the gatekeeper in r1):
1. **Edge operator.** For a toric block without the pattern inside/outside/inside on three consecutive sites,
   E = sum_I Theta X^I Thetabar X^I Theta is diagonal, with entry the sum over links to outside sites of
   k_f i(N-i), k_f = (sigma_{f,1}^2 + sigma_{f,2}^2)/4. Rank of the edge map = number of edge sites.
   s^2 = Tr E; T = Tr E^{1/2} is the trace norm of the edge map.
2. **Closed forms.** Cap x whole second sphere: rank N, T = N s_1, s^2 = N s_1^2, independent of A_2. Product
   block: rank M_1 + M_2 - 1, s^2 = M_2 s_1^2 + M_1 s_2^2, T = (M_2-1)s_1 + (M_1-1)s_2 + sqrt(s_1^2+s_2^2).
3. **Pointwise identity.** rho sqrt(K(df,df)) is the 3-volume density of {f = 0} in
   gt = (sqrt g/rho)^{2/3} K^{-1}; K(df,df) = sum_I {f, x^I}^2.
4. **Charge reduction.** Q = -2i(Y - Y^dagger); nonzero spectrum = that of an explicit 2r x 2r matrix; for
   torus-invariant Gaussian momenta <Y Y^dagger> is diagonal on the edge sites with entries Et_u = sum over links of
   kappa D_v; for cap x sphere it is s_1^2 W times the identity.

Established in the Poisson limit (kinematic), unchanged:
5. **Measure.** sqrt2 T >= P_K, equality iff aligned or diagonal edge with constant speed. Scaling exponents
   under (A_1, A_2) -> lam: T and P_K (1, 0); induced 3-volume (1, 2); K^{-1} 3-volume (-1, -2).
6. **Crystalline T-density** for oblique half-planes: (n_1-n_2) sqrt(e_1) + n_2 sqrt(e_1+e_2) >=
   sqrt(n_1^2 e_1 + n_2^2 e_2); excess 11% in the sampled cases.

Numerical (changed in r2):
7. **Rows.**
   - Cap x sphere (all edge sites equivalent): boxes per side = 0.85-0.95 of 2 sqrt(W) T at N = 16 (e3); with
     l_c1 = N-1, l_c2 = 3 the ratio is 0.90, 0.93, 0.94 at N = 8, 12, 16 while the ratio to 2 sqrt(W) s is 2.6, 3.2,
     3.8 (e6 Part A). So it follows T, not s.
   - Inequivalent edge sites (new, e6 Part B). Local estimate L = 2 sum_u sqrt(Et_u); non-local comparison
     G = 2 sqrt(r sum_u Et_u) >= L.
     - Half-planes (b/a = 0.41, 1/sqrt3; M = N^2/2, r = N; 16 cases): L/G in 0.86-0.99; boxes = 0.92-0.96 of L,
       0.81-0.94 of G. Changing nu_2/nu_1 from 1 to 3 at fixed block and state moves the ratio to L by at most 0.02
       and the ratio to G by 0.07-0.11 (statistical error per ratio <= 0.008). This discriminates: the box count
       tracks the local sum of square roots, not the non-local combination.
     - Product blocks (M/r between 2 and 3; 16 cases): L/G in 0.80-0.99; boxes = 0.78-0.91 of L, 0.67-0.85 of G.
       Here L is an estimate with a deficit of up to 22%, and the ratio to L itself moves by up to 0.08 with the
       state; the discrimination is weaker (G still varies more). These blocks are shallow (M/r <= 3), where the
       edge-site part of the row sums is not small.
8. **Dimension.** At the seven sampled (r, ell) pairs, M = 4000 and 16000: slope d log d / d log M = 2 r ell
   within 2% (the six with ell <= 40); log d = 2 r ell [log(M/(r+ell)) + c], 0.80 < c < 0.97; sub-additivity factor
   0.69-0.99. On the 8 x 7 x 2 grid of e5: c in [0.793, 1.041], factor in [0.551, 0.998] for r > 1, slope in
   [0.954, 1.020]; log d(r) < r log d(1) at the same M at all 98 grid points with r > 1. The r1 range statement was
   false (c = 1.041 at (1, 400, 4000); c = 0.793 at (4, 4, 4000); factor 0.551 at (160, 4, 4000)), as the review
   found. The qualitative conclusions (c of order one, rank through M/(r+ell), sub-additivity at the same M) hold
   at every grid point.

**Consequences for G-derived (conditional on the imported leading-order FFHS entropy, at fixed frame, inside the
compact positive-contraction class).**
- (a) *Removed, for the tested blocks:* 065's cause "single row / one-dimensional edge". For cap x sphere and the
  sampled half-planes the coefficient of the logarithm is, to 4-15%, a sum over the sites of a 3D edge of a locally
  determined quantity. For shallow product blocks this holds only as an estimate to 22%. Not tested: other shapes,
  larger N, larger M/r with inequivalent sites.
- (b) *Identified:* the measure of that sum, T weighted by the state. Not the induced area; a 3-volume (of gt)
  only for aligned or diagonal edges with constant speed.
- (c) *Persisting:* rank dependence through log(M/(r+ell)) and non-additivity in r at the same M; fixed-frame
  anisotropy; supplied state, cut-offs and frame; **compact factor with positive contraction, block not a region of
  the emergent spacetime, edge not dM**; no map to eq:g-from-e.

No entropy density on dM, no stationarity and no Lambda_eff are derived. G stays OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL.

## Target and status

- **Problem.** G (HBEV), G-derived level.
- **Appendix H, sec:status-G (L2850-2894 at HEAD 54a2dcb), verbatim.** "Status: OPEN. Priority: CRITICAL PATH.
  Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and G-external support at most a scope-limited
  model; G remains OPEN and neither satisfies the matrix-derived criterion."
- **Chapter 17 (L474-495), verbatim.** "CRITICAL PATH; mechanism CLOSED CONDITIONALLY, derivation OPEN."
- **Original target.** Matrix-derived S_ent(h_ij, phi) on dM (ass:Sent-density), matrix-derived boundary
  stationarity (ass:bdy-EE), and Lambda_eff from eq:Leff.
- **Dependencies.** G_eff (F); the replica construction, hence ass:dictionary (A); the emergent metric eq:g-from-e
  (D1); the dimensional conversion noted in ch12.
- **This package.** PROGRAMME-CONDITIONAL; conditional lemmas plus a bounded no-go continuation inside the 065
  class clause "compact internal factor with positive contraction". No status change.
- **Discrepancies.** None new (the 065 author item on the missing "Missing step" paragraph of sec:status-G is
  unchanged and not edited here).

## Source reading

Digest + targeted reads; no full scan (none required: no definition, assumption, scope or status passage changes).
`python scripts/make_digest.py --check` printed `DIGEST CURRENT` at HEAD 54a2dcb; `git status` shows `chapters/`
and `bib/` clean. For this round I read in full: `review-r1.md`, `proposal-r1.md`, `appH_insert.tex`,
`e3_charge_rows.py`, `e4_dimension.py`, `apply_check.py` and their outputs, `build_r1.txt`; the G.spacetime-block
entry of `reports/graph/frontier.yaml` (L347-362, by grep). The manuscript passages read in r1 (appH sec:status-G
whole; ch17 L465-500; ch12 def:HBEV, ass:Sent-density, ass:bdy-EE; ch03 def:matrix-coords-ext, ass:dictionary) are
unchanged at the same HEAD and the appH baseline hash is re-asserted by `apply_check_r2.py`. No file was unreadable.

## Research and reasoning

Sections 1-5 of r1 stand (edge-operator lemma, pointwise identity, measure, charge reduction, Weyl formula); the
gatekeeper re-derived them by hand. New in r2:

### R2.1 Dimension on a grid (F1; e5)

Same exact Weyl product as e4 (adjoint check dim = M^2 - 1 repeated), evaluated at r in {1,2,4,8,16,40,80,160},
ell in {4,8,16,40,100,200,400}, M in {4000, 16000}. Extrema found:

| quantity | min (at r, ell, M) | max (at r, ell, M) |
|---|---|---|
| slope/(2 r ell) | 0.95367 (1, 400, 4000) | 1.01987 (160, 4, 4000) |
| c | 0.79288 (4, 4, 4000) | 1.04099 (1, 400, 4000) |
| log d(r)/(r log d(1)), r > 1 | 0.55117 (160, 4, 4000) | 0.99840 (2, 400, 16000) |

Seven quoted pairs: c in [0.80654, 0.96041]; factor in [0.69173, 0.98203]; slope (ell <= 40) in [0.99521,
1.01565]. The script asserts exactly the sampled statements made in the text and prints that the r1 range statement
fails on the grid. Reading: c -> 1 + O(ell/M) for r = 1 (FFHS's log(eM/ell), with the correction visible at
ell = 400, M = 4000) and c near 3/2 - log 2 = 0.807 for r comparable to ell; this asymptotic reading is an estimate
and is not in the manuscript text.

### R2.2 Rows for inequivalent edge sites (F2, F6; e6)

Exact input (r1 section 4, verified): for torus-invariant Gaussian momenta <Y Y^dagger> = diag(Et_u),
Et_u = sum_{links u->v} kappa D_v, D_v = sum_{j in Omega} <|Pi_vj|^2>. For a separable variance
f = f_a(l_1) f_b(l_2), <|Pi_{(v1 v2),(j1 j2)}|^2> = G_a[v1, j1] G_b[v2, j2] with
G_x[v, j] = sum_l f_x(l) (P_l)_{(vj),(vj)}, so D = G_a Omega G_b^T as an N x N array; the "sym" state is the sum of
two independent Gaussians with the factors exchanged, and D is additive. e6 asserts in every case that the sampled
<Tr Y Y^dagger> agrees with sum_u Et_u within 5% (observed 1-2%), which checks the sampler against the exact
second moment.

If the positive part of the spectrum of Q were 2 x (singular values of a matrix with independent rows of squared
norm Et_u), the sum of positive eigenvalues would be close to L = 2 sum_u sqrt(Et_u) up to the Jensen gap and the
alpha-block; this is the "local" hypothesis. The alternative G = 2 sqrt(r sum_u Et_u) is what one gets if only the
total second moment and the rank matter (all singular values equal); L <= G by Cauchy-Schwarz with equality iff the
Et_u are equal. For cap x sphere L = G, which is why r1's Monte Carlo could not tell them apart (F2). The new runs
vary L/G between 0.80 and 0.99 by changing nu_2/nu_1 and the state.

Outcome (60 samples each; errors are standard errors of the mean):
- Part A reproduces the gatekeeper's own N-scan (0.89, 0.92, 0.94 and 2.5, 3.2, 3.8) within errors: 0.9045 +-
  0.0145, 0.9270 +- 0.0096, 0.9400 +- 0.0094 and 2.56, 3.21, 3.76.
- Half-planes: the ratio to L is stable at 0.928-0.959 across L/G from 0.869 to 0.988, while the ratio to G falls
  from about 0.92-0.93 (L/G near 0.98) to 0.81-0.85 (L/G near 0.87). Pairwise at fixed block and state
  (nu_2/nu_1 = 1 -> 3): ratio to L changes by -0.003 to +0.017; ratio to G drops by 0.075 to 0.104; the standard
  error of each ratio is 0.003-0.008. This is a discrimination at more than 5 sigma in each of the 8 pairs.
- Product blocks: ratio to L 0.783-0.902, ratio to G 0.672-0.844. The most inhomogeneous case (4 x 9, sym,
  nu_2/nu_1 = 3, max/min Et = 21, L/G = 0.805) has 0.902 +- 0.013 of L and 0.727 of G. L is the better estimate,
  but the ratio to L varies by up to 0.08 within a block, so for these shallow blocks (M/r = 2.25-3.0) the
  statement is an estimate only. My reading is that the deficit is the edge-site part of the row sums
  (W_perp/W of e3), which is large when the block is two to three sites deep; this reading is not tested and is not
  in the manuscript text.
- Over all 32 cases the correlation of the ratio with L/G is -0.29 for L and +0.51 for G.

What this supports and what it does not. It supports "sum over edge sites of a locally determined quantity" for
cap x sphere and for the sampled deep half-planes, to 4-15%. It does not establish it for product blocks beyond a
22% estimate, nor for other shapes, larger N, or the constrained ensemble (Tr Q = 0 is not imposed). The
crystalline-anisotropy statements of the Measure paragraph are exact statements about T; they bear on the entropy
through this identification, which is now tested on oblique half-planes (the blocks to which the crystalline density
applies) and not beyond.

### R2.3 Class statement (F3, F5)

Hypothesis class of the result, exactly: compact internal factor S^2_N x S^2_N with positive contraction delta_IJ;
toric blocks at one fixed frame without the excluded pattern; Gaussian proxy momenta with torus-invariant variances;
FFHS block algebra at leading semiclassical order with one dominant irrep; equal rows for the dimension. Relative to
065, the clauses relaxed are the dimension of the factor and "single projector or coaxial cap pair". The clause
"compact internal factor with positive contraction" is retained: the block is a region of the factor, not a
"4D region x fibre" of the emergent spacetime, and its edge is not dM.

### Fork: hypotheses of the remaining obstruction (updated)

| # | Hypothesis | Relaxation | Explored | Outcome |
|---|---|---|---|---|
| H1 | one-dimensional edge, rank-one edge map (065) | 4D compact factor, 3D edge | yes | removed for the tested blocks: rank = number of edge sites; boxes follow the local sum L (half-planes: decisive at these sizes; product blocks: 22% estimate) |
| H2 | "area" = induced area | compare g, K^{-1}, conformal classes | yes | P_K-type: 3-volume of gt only in aligned, constant-speed cases |
| H3 | fixed toric frame, sharp projector | oblique toric blocks | partly | crystalline anisotropy up to 11%; frame average and non-toric projectors not done |
| H4 | rank dependence | multi-row diagrams | yes | weakened to log(M/(r+ell)), not removed; sub-additive in r at the same M |
| H5 | supplied state | e^{-S/2}; OS reconstruction | no | open |
| H6 | compact factor, positive contraction; block not a region of spacetime | genuine spacetime block (region of the non-compact / Lorentzian leaf x fibre) | no (only: Q has no contraction; delta enters via the variance) | open; this is 065 avenue 1 = G.spacetime-block, untried |
| H7 | no map to eq:g-from-e | A, D1 | no | open |
| H8 | leading-order FFHS saddle, one irrep | subleading orders; other subsystem algebra; vacuum term of 2303.08012 | no | open |

Ranked open avenues (ranking adopted from the review, which puts the spacetime block first because it is the only
clause that separates the proxy from the target):
1. **G.spacetime-block** (H6): a region of the non-compact / Lorentzian leaf x fibre. Needs a state where the
   weight is not positive. The edge-operator lemma extends to any configuration tridiagonal in a joint eigenbasis;
   the Gaussian proxy state does not.
2. **Depth-cancelling combinations** (H4): mutual-information-type combinations for adjacent toric blocks.
3. **Frame average / minimisation and non-toric projectors** (H3): does the crystalline anisotropy survive.
4. **Within-core state** (H5): e^{-S/2} or OS reconstruction on fibre modes.
5. **Fixed-volume partition function** (scout 20261114 R4), independent of the factorisation map.
6. **Subleading orders, alternative subsystem algebra, vacuum term** (H8).
Additional within-avenue item raised by r2: deeper product blocks (M/r >> 3) at larger N, to see whether the 22%
deficit closes; and the Tr Q = 0 constrained ensemble.

### Literature

Only arXiv:2408.05274 (key FlissFrenkelHartnollSoni2025, already in `bib/namcg.bib`), for Eq. (4.4) and the
leading-order entropy, as verified from the source in 065; not re-fetched this round. No new reference. Scout leads
1310.8345, 2512.03163, 2212.10607, 2303.08012: not independently verified, not cited in the manuscript text.

### Comparison with the original target

The target is a local density on dM of the emergent spacetime from the replica construction, plus stationarity. This
package works on a compact positive-contraction proxy and shows an edge-extensive coefficient with an identified
measure for the tested blocks, with persisting depth, frame and state dependence. It derives no part of the target.

## Claim classification

| Claim | Class |
|---|---|
| Edge-operator lemma; rank; closed forms | established (exact, finite N) |
| Pointwise identity for gt; scaling exponents | established (exact) |
| sqrt2 T/P_K = rms/mean >= 1 (cap x sphere); half-plane densities and Minkowski inequality | established (Poisson-limit kinematics / counting) |
| Charge reduction; <Y Y^dagger> diagonal; uniform W for cap x sphere | established (exact, stated Gaussian class) |
| boxes ~ 2 sqrt(W) T for cap x sphere, N = 8, 12, 16 | numerical (5-15%) |
| boxes ~ L for half-planes at N = 12, 16 (and not ~ G) | numerical (4-8%; discrimination from G at > 5 sigma per pair) |
| boxes ~ L for product blocks with M/r in [2.25, 3] | numerical estimate only (9-22% deficit) |
| inequivalent edges of other shapes, larger N, larger M/r, Tr Q = 0 ensemble | untested |
| Weyl-dimension values at the seven pairs and on the grid | numerical (exact formula evaluated at stated points; no range claim) |
| "log d_mu is not an integral of a local edge density" | conditional (leading-order FFHS entropy, fixed frame, equal rows) |
| state, cut-offs, frame | supplied inputs |
| block is a region of a compact factor, not of emergent spacetime | scope fact of the construction (not a result) |
| relation of gt to eq:g-from-e; frame minimisation; spacetime block | unresolved |

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`. One insertion, nothing replaced or removed.

**Anchor (occurs once; checked by `apply_check_r2.py` against the current tree, baseline 624232 bytes, sha256
c2dac013...):** the closing sentence of the 065 paragraph followed by the Problem H header,

    ...Assumptions~\ref{ass:Sent-density} and~\ref{ass:bdy-EE} are not discharged, and Problem~G remains open and PROGRAMME-CONDITIONAL.
    <blank line>
    \section{Problem H: modular origin of the interpolating function}

Insert after that sentence (line 2894) a blank line and the block; the existing blank line and the Problem H header
follow. All existing text of sec:status-G is kept.

**Authoritative text:** `proposals/067-product-sphere-edge/appH_insert_r2.tex` (LF, ASCII, 13248 bytes, sha256
f0fa634cbae16d6c41366f72a8c4e3f834b26fbe31d37532204eb513b6c014ee); the integrator converts to CRLF. Resulting appH:
637508 bytes, sha256 bd0616ecccb2f2ce6b7ff8cb4fc61864ad9a9b8f9df0e8e208363832f69eed7c, 3405 CRLF, 0 bare LF.
`make_insert_r2.py` rebuilds it from the r1 insert by five exact single-occurrence replacements and prints the diff
(`make_insert_r2_output.txt`). The first paragraph, Edge operator, Measure and the closing scope/status paragraph
are byte-identical to r1. The changed passages, in full:

*Rows* - the r1 sentence "In this regime the number of boxes ... and not \(s\)." is replaced by:

```latex
With \(M_1=N/2\), \(l_{c1}=N-1\) and \(l_{c2}=3\) the same ratio is \(0.90\), \(0.93\), \(0.94\) at \(N=8,12,16\), and the ratio to \(2W^{1/2}s\) is \(2.6\), \(3.2\), \(3.8\) (numerical). For this block the number of boxes of the diagram on each side is therefore close to \(2W^{1/2}T\): it follows \(T\), which here is \(N^{1/2}s\), and not \(s\). When the edge sites are not equivalent, the corresponding estimate is \(L\equiv2\sum_u\langle YY^\dagger\rangle_{uu}^{1/2}\), the sum being over the \(r\) edge sites; it is at most \(G\equiv2\,(r\operatorname{Tr}\langle YY^\dagger\rangle)^{1/2}\), which is not a sum over the edge sites, with equality only for equal entries. Take \(N=12\) and \(16\), \(A_f=\nu_f1\) with \(\nu_2/\nu_1=1\) and \(3\), and the variance \(f\) above with \(l_{c1}=N-1\), \(l_{c2}=3\), or the sum of this \(f\) and the same with \(l_1\) and \(l_2\) exchanged. For the half-plane blocks with \(b/a=0.41\) and \(3^{-1/2}\) that contain half of the sites, \(M=N^2/2\) and \(r=N\), the ratio \(L/G\) lies between \(0.86\) and \(0.99\) in the sixteen cases, and the sum of the positive eigenvalues of \(Q\) is between \(0.92\) and \(0.96\) of \(L\) and between \(0.81\) and \(0.94\) of \(G\); the change of \(\nu_2/\nu_1\) from \(1\) to \(3\) changes its ratio to \(L\) by at most \(0.02\) and its ratio to \(G\) by \(0.07\) to \(0.11\). For the product blocks with \((M_1,M_2)\) equal to \((6,3)\) and \((3,7)\) at \(N=12\), and to \((8,4)\) and \((4,9)\) at \(N=16\), where \(M/r\) is between \(2\) and \(3\), \(L/G\) lies between \(0.80\) and \(0.99\), and the sum is between \(0.78\) and \(0.91\) of \(L\) and between \(0.67\) and \(0.85\) of \(G\) (numerical, \(60\) samples, statistical errors at most \(0.02\), momenta not constrained to \(\operatorname{Tr}Q=0\)).
```

*Dimension* - whole paragraph:

```latex
\emph{Dimension.} For the highest weight of \(U(M)\) with \(r\) rows of length \(\ell\) and \(r\) rows of length \(-\ell\), the Weyl dimension formula, evaluated at \((r,\ell)=(1,40)\), \((4,40)\), \((16,40)\), \((40,40)\), \((160,40)\), \((40,4)\) and \((40,400)\) with \(M=4000\) and \(16000\), gives \(\mathrm d\log d/\mathrm d\log M=2r\ell\) to within \(2\%\) in the six cases with \(\ell\le40\), and \(\log d=2r\ell\,[\log(M/(r+\ell))+c]\) with \(0.80<c<0.97\) in all of them; for \(r>1\) this is below \(r\) times the value for one row on each side at the same \(M\), by a factor between \(0.69\) and \(0.99\) in these cases. At the points with \(r\) equal to \(1\), \(2\), \(4\), \(8\), \(16\), \(40\), \(80\) or \(160\) and \(\ell\) equal to \(4\), \(8\), \(16\), \(40\), \(100\), \(200\) or \(400\), with the same two values of \(M\), \(c\) lies between \(0.79\) and \(1.05\) and the factor, for \(r>1\), between \(0.55\) and \(1\) (numerical; values at the points evaluated, not bounds over a range). For the cap times the whole second sphere, \(M=M_1N\) and \(r=N\): at \(M_1=50\), \(\ell=30\), \(\log d/(2N\ell)\) rises from \(3.38\) at \(N=10\) to \(4.60\) at \(N=160\), against \(\log M_1=3.91\) (numerical). The rank of the block thus enters through \(M/(r+\ell)\), which for \(\ell\ll N\) is the depth \(M_1\) of the block behind its edge.
```

*Bearing* - whole paragraph:

```latex
\emph{Bearing on Assumption~\ref{ass:Sent-density}.} (i) For the cap times the whole second sphere, whose edge sites are all equivalent, and for the half-plane blocks sampled, the number of boxes, the coefficient of the logarithm in \(\log d_\mu\), is, within the accuracy of the numerical comparisons above, a sum over the sites of a three-dimensional edge of a quantity fixed by the links at that site and by the row sums \(D_v\) of the state; the single row of the preceding paragraph was special to a one-dimensional edge. For the product blocks sampled the same sum is an estimate with a deficit of up to \(22\%\), and blocks of other shapes, larger \(N\) and larger \(M/r\) with inequivalent edge sites are not tested. (ii) With that proviso the measure of that sum is \(T\) weighted by the state. It coincides with a volume, that of \(\tilde\gamma\) up to the factor \(\sqrt2\,(2\pi)^2\), only for an edge along a lattice direction or along the diagonal, with constant speed along the flow; \(\tilde\gamma\) is not the induced tensor, is not \(K^{-1}\), and is not identified with the metric of Equation~\eqref{eq:g-from-e}, whose relation to the matrix configuration rests on Assumption~\ref{ass:dictionary} and Problem~D. (iii) The dependence on the rank remains, through \(\log(M/(r+\ell))\), and the value for \(r\) rows is not \(r\) times the value for one row at the same \(M\), so at this order \(\log d_\mu\) is not the integral over the edge of a density fixed by local data of the edge (conditional on the leading-order entropy of~\cite{FlissFrenkelHartnollSoni2025}, at fixed frame). (iv) The row sums \(D_v\), the cut-offs and the frame are supplied, as in the preceding paragraph, and the factor is compact with a positive contraction: as in (i) of the preceding paragraph, the block is a region of this factor and not of the emergent spacetime, and its edge, though three-dimensional, is not the boundary \(\partial M\) of Definition~\ref{def:HBEV}.
```

**Labels referenced (each exists exactly once; re-checked by `apply_check_r2.py`):** ass:Sent-density, ass:bdy-EE,
def:HBEV (ch12); def:matrix-coords-ext, ass:dictionary (ch03); eq:g-from-e (ch04). No new label. Cite key
FlissFrenkelHartnollSoni2025 exists once in `bib/namcg.bib`. No bib change.

**Stale passages elsewhere:** none in the manuscript. The 065 paragraph's bearing (i) ("its edge is not the boundary
dM") is true for the cap and, by the new clause in (iv), is now stated for the toric block as well. For the
ledger / frontier (not edited by me): 067 should be recorded as a compact proxy with `G.spacetime-block` still
untried, as the review asks.

**Build.** Scratch build outside the repository with the would-be appH: pdflatex, bibtex, pdflatex, pdflatex all
exit 0; 384 pages; 0 undefined, 0 multiply defined; 24 overfull hboxes (same as r1 and 065). See `build_r2.txt`.

## Verification scripts

All in `proposals/067-product-sphere-edge/`; run from the repository root with the system `python`; stdout only
(except `make_insert_r2.py`, which writes `appH_insert_r2.tex` in the proposal folder). e1-e4 are unchanged from r1
and were re-run by the gatekeeper with identical output.

| Command | Checks | Expected invariant output |
|---|---|---|
| `python proposals/067-product-sphere-edge/e1_edge_operator.py` | unchanged (r1) | `PASS e1`, identical to `e1_edge_operator_output.txt` |
| `python proposals/067-product-sphere-edge/e2_perimeter.py` | unchanged (r1) | `PASS e2`; `T/(P_K/sqrt2)=1.11267`, `1.09592` |
| `python proposals/067-product-sphere-edge/e3_charge_rows.py` | unchanged (r1) | Part 3 column 0.8537, 0.9438, 0.9346, 0.9512; `PASS e3` |
| `python proposals/067-product-sphere-edge/e4_dimension.py` | unchanged (r1) | c 0.8065-0.9604; ratio 0.6917-0.9820; `PASS e4` |
| `python proposals/067-product-sphere-edge/e5_dimension_grid.py` (about 1 min) | NEW (F1): grid of 112 points; extrema; asserts the sampled statements of the text; sub-additivity at all grid points | `(a)` c min 0.79288 at (4,4,4000), max 1.04099 at (1,400,4000); ratio min 0.55117 at (160,4,4000), max 0.99840 at (2,400,16000); `(b)` c 0.80654-0.96041, ratio 0.69173-0.98203; `(c)` slope 0.99521-1.01565; `(d) ... FAILS as a range statement`; `PASS e5` |
| `python proposals/067-product-sphere-edge/e6_rows_scan.py` (about 2 min, seeded 67006) | NEW (F6, F2): Part A N-scan for cap x sphere; Part B 32 cases with inequivalent edge sites; sampler asserted against the exact second moment in every case | Part A: 0.9045, 0.9270, 0.9400 and 2.5584, 3.2112, 3.7601; Part B summary: `L/G in [0.805, 0.988]`, `ratio to L in [0.783, 0.959]`, `ratio to G in [0.672, 0.933]`, correlations `-0.286` / `+0.511`; `PASS e6` (identical to `e6_rows_scan_output.txt`) |
| `python proposals/067-product-sphere-edge/make_insert_r2.py` | builds the r2 insert from r1 by five asserted single-occurrence replacements; prints the diff | `applied F1` ... `applied F3`; `appH_insert_r2.tex: 13248 f0fa634c...` |
| `python proposals/067-product-sphere-edge/apply_check_r2.py` | baseline hash of the current appH, unique anchor inside sec:status-G, insertion, CRLF, refs, cite, balance, no process language, one status sentence | `anchor occurrences: 1`; `result appH: 637508 bd0616ec...`; `APPLY CHECK PASS` (saved: `apply_check_r2_output.txt`) |

Numbers in the insert against outputs (r2 additions): 0.90/0.93/0.94 and 2.6/3.2/3.8 (e6 Part A); half-planes
L/G 0.8694-0.9882, to L 0.9279-0.9586, to G 0.8131-0.9329, pair differences to L <= 0.0169, to G 0.0747-0.1038;
product blocks L/G 0.8053-0.9854, to L 0.7827-0.9024, to G 0.6720-0.8443, M/r 2.25-3.0, max standard error 0.0198
(e6 Part B rows); grid 0.79/1.05 and 0.55/1 (e5 (a)); 0.69/0.99 (e5 (b)).

## Decisions Taken

1. **F1: sampled values plus grid extrema**, rather than S1 alone. Reason: the grid shows where the r1 sentence
   failed and that the qualitative conclusions hold at every point; quoting it costs one sentence. Rejected: a
   fitted range statement (no proof of bounds).
2. **F1: "0.99" instead of S1's "0.98".** The sampled maximum is 0.98203.
3. **F2: evidence route, with restricted wording.** Reason: the identification of the box count with a local sum is
   what connects the exact T results to the entropy; a test on oblique half-planes is exactly the missing link for
   the crystalline statement, and it favours the infrared derivation's question (is the coefficient edge-local) by
   answering it where it can be answered. Rejected: S2 verbatim ("not tested here"), which would be less informative
   and, with e6 in the pack, no longer accurate; and any general claim for the factor (not supported: product blocks
   reach only 22%).
4. **Product-block deficit is reported, not explained in the manuscript.** My reading (shallow blocks) is untested.
5. **New scripts instead of editing e3/e4**, so that the r1 outputs the gatekeeper reproduced remain valid.
6. **Avenue ranking**: the review's order is adopted (spacetime block first). r1 had ranked depth-cancelling
   combinations first; the review's reason (the compactness clause is the one that separates proxy from target) is
   sound.
7. Unchanged from r1: T reported alongside s; gt stated as an identity with no literature name; 065 paragraph not
   edited; no status-passage edit.

## Milestone assessment

Routine. Conditional sharpening and bounded no-go continuation inside the compact positive-contraction class. No
critical-path step is derived (not M1); no manuscript-open class of routes is ruled out (not M2); no merged claim is
found wrong (not M3); no label or scope change (not M4, M5). Not a breakthrough candidate.

## Status-label recommendation

Critical-path set from ch17 and appH at HEAD: A, B, C, D (D1), E, F, G (derived level), N, all OPEN. Affected label:
G only; **unchanged** (OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL). No label edit is proposed.

## Author decision needed

None.

## Remaining open step

To close G-derived one still needs, from the matrix theory: (1) a subsystem or partition-function construction for a
region of the emergent spacetime (not of a compact internal factor) whose entropy is a local density on its
boundary, with no dependence on depth/rank and none on a supplied frame; (2) a state or weight fixed by the
integral; (3) identification of the measure with sqrt|h| of eq:g-from-e (needs A and D1); (4) the expansion
eq:Sent-exp with its coefficients; (5) boundary stationarity ass:bdy-EE; (6) Lambda_eff from eq:Leff including the
ch12 dimensional conversion. Next packages, in order: G.spacetime-block; depth-cancelling combinations; frame
average; within-core state.

## Special instructions for the gatekeeper

- Changed text is confined to: the end of Rows, the Dimension paragraph, and Bearing (i)-(iv). Everything else in
  the insert is byte-identical to r1 (`make_insert_r2_output.txt` shows the diff).
- F2 is the item to re-check. Bearing (i) claims the local-sum statement only for cap x sphere and "the half-plane
  blocks sampled"; for product blocks it says "estimate with a deficit of up to 22%"; the rest is "not tested".
  Please check each interval in the Rows addition against the rows of `e6_rows_scan_output.txt` (all intervals are
  rounded outward), and the pairwise statement (nu_2/nu_1 = 1 -> 3: at most 0.02 on L, 0.07 to 0.11 on G) for the
  eight half-plane pairs.
- G is described in the text only as "not a sum over the edge sites"; it is a comparison quantity, not a proposed
  alternative formula.
- The half-plane blocks of e6 are a i_1 + b i_2 < c with c = 0.705 (N-1) for b/a = 0.41 and c = 0.79 (N-1) for
  b/a = 1/sqrt3; both give M = N^2/2 and r = N at N = 12 and 16 (printed in the output). The text identifies them by
  "contain half of the sites".
- Do not read (i) as a derivation of a boundary density: it concerns the coefficient |mu| only, for a supplied
  Gaussian state, unconstrained Tr Q, N <= 16.
- S1 is modified in one number (0.98 -> 0.99) for the reason stated; S3 and S4 are verbatim.
- The asymptotic readings in R2.1 and the "shallow block" reading in R2.2 are mine and are not in the manuscript
  text.
- No full scan was done and none is claimed. Proposed integration ordinal 64; next 5th-item scan at 65.
- `apply_check_r2.py` writes nothing into the repository; with an argument it writes the would-be appH to a
  directory outside it. The scratch build directory (session scratchpad, `build067r2`) was not removed: the cleanup
  command was denied by the permission system. It is outside the repository.
