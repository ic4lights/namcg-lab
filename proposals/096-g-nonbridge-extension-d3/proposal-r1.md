# Proposal 096-g-nonbridge-extension-d3, round 1

## Result

**Negative non-bridge lemma extended to every block dimension.** Within the named constant-variance
gaussian edge-block subclass (appH L3195: iid complex gaussian edge block A, Gram G=AA\(\dagger\),
D=min(M,N-M), spectrum coordinate p_i=lam_i/tau), for **every** D>=2:

1. **a.e. (measure) side, established for all D>=2.** The conditional law of the normalized
   diagonal tuple d=(G_11,...,G_DD)/tau given p is non-atomic for almost every spectrum value,
   hence **no map of any kind** (measurable, relabelling-equivariant, or arbitrary) recovers
   d, or its power-sum tuple (P_2,...,P_D) with P_k=sum_i d_i^k, or the rho-family of the
   integrated 092 paragraph evaluated at d, from p, almost everywhere on the support of the law.
   This upgrades the integrated 095 a.e. chain (identical conditioning structure) by replacing
   its D=2 Beta(1,1) ingredient with: Haar first-row squared moduli are uniform on the simplex
   (Dirichlet(1^D), proved self-containedly), and every non-constant linear form of a uniform
   simplex vector has a non-atomic law — proved self-containedly for **general D** by the
   stick-breaking induction (Beta(1,D-1) break, independent remainder; base D=2 uniform), with
   the D=3 explicit piecewise-linear density on record.
2. **Pointwise (fibre) side, established.** (a) The rank-one spectrum (tau,0,...,0) carries two
   Gram data with different diagonals, at every D>=2 ((1,0,...,0) vs (1/2,1/2,0,...), power sums
   1 vs 1/2). (b) Every fibre over a spectrum with at least two distinct eigenvalues contains a
   one-parameter real-analytic curve of Gram matrices with moving diagonal (plane rotation in the
   eigenbasis of a distinct pair; P_2 along it is sum_j lam_j^2 - 2(lam_i-lam_j)^2 sin^2 theta
   cos^2 theta, strictly varying) — at every D>=2. (c) At **D=3** the diagonal image of every
   such fibre contains a two-dimensional patch with non-empty interior in the trace hyperplane
   (two-angle rotation Jacobian (lam_2-lam_1)(lam_3-(lam_1+lam_2)/2) at both angles pi/4, nonzero
   after a relabelling that every non-constant triple admits).
3. The identification of the fibre diagonal image with the full Schur-Horn permutahedron is NOT
   claimed and not needed; it stays unproved (self-contained general-D interior statement not
   executed). No literature is cited anywhere in the insert.

Problem G stays OPEN and PROGRAMME-CONDITIONAL; this package closes nothing and changes no label.

## Target and status

- Problem G, `chapters/appH-microscopic-proofs.tex` L3025-3029 (verbatim): "Status: OPEN.
  Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and
  G-external support at most a scope-limited model; G remains OPEN and neither satisfies the
  matrix-derived criterion." Labels frozen; nothing here edits or moves them.
- Target (frontier chain-2 rank 1, edge `G.moments-interaction-nonconvex`, verbatim from the
  2026-11-19 dispatch): "D>=3 extension of the Gram->moment non-bridge lemma to the full
  rho-tuple via a self-contained Schur-Horn/permutahedron proof (rank-one atomic-Gram datum
  already obstructs at every D>=2; no literature citation without the self-contained proof)".
  The dispatch also required the a.e. general-D upgrade of the 095 argument, full rho-tuple
  coverage, and the established-vs-conjectured split.
- Dependencies: integrated 091 (L3195 named subclass, spectrum Jacobian), 092 (L3197 rho-family
  and power-sum recursion), 095 (L3203 D=2 non-bridge lemma + repaired a.e. conditioning chain).
  Does NOT touch the 094 integrability line (DO-NOT-RE-ATTEMPT respected), does not deform the
  core measure, introduces no metric (spacetime stays emergent).
- DERIVED vs PROGRAMME-CONDITIONAL: negative sub-lemma for the exactness route; conditional
  content, closes nothing.

## Source reading

DIGEST CURRENT confirmed at start by `python scripts/make_digest.py --check` (checked, not run).
Digest + targeted reads. Read IN FULL this round: `chapters/appH-microscopic-proofs.tex` windows
L3185-3208 (089-095 G-block incl. the 095 paragraph L3203 and the Vacuum term L3205) and L3020-3033
(G ledger header); `proposals/095-g-gram-moment-identification/proposal-r2.md` (32,509 B / sha8
6dc042e2); `proposals/095-g-gram-moment-identification/review-r2.md` (10,551 / 1a49a220, its
avenue-1 ranking is this package); `reports/sme-scout-20261119-1011.md` (15,351 / 13bc64a5, route
2 + "Implications for the next target"). `reports/graph/frontier.yaml` only via grep windows
(edge `G.moments-interaction-nonconvex` stanza, L552-556 region; chain/edge lists). No unreadable
files. Live appH measured by the scripts: 776,019 B / sha256
600588c1d1087232ace2cea1cdecf13fb38885cf7a2126a72eedfdc1234bfa0d / CRLF 3,854 / bareLF 0 (the
095-integrated tree, as dispatched).

## Research and reasoning

Setting (from L3195/L3203 as integrated): A an Mx(N-M) edge block with iid CN(0,sigma^2) entries,
G=AA\(\dagger\) DxD with D=min(M,N-M)>=2, tau=Tr G, eigenvalues lam_1>=...>=lam_D>=0, p_i=lam_i/tau,
d_i=G_ii/tau (d lives on the probability simplex), P_k(d)=sum_i d_i^k. The 092 paragraph (L3197)
records the exact triangular recursion between (P_2,...,P_D) and the rho-family at the profile
argument, so non-recovery of one is non-recovery of the other; this package works with the power
sums, which are the natural coordinates.

### Pointwise side

**P1 rank-one pair (all D>=2, established derivation).** G_1 = tau e_1 e_1\(\dagger\) and
G_2 = tau v v\(\dagger\), v=(e_1+e_2)/sqrt(2), both have characteristic polynomial
x^(D-1)(x-tau) (rank one with trace tau), diagonals tau(1,0,...,0) and tau(1/2,1/2,0,...), and
power sums P_2 = 1 vs 1/2 of the normalized diagonal. Verified symbolically at D=3,4 (`verify_096.py` S1:
charpoly difference == 0, P2 difference == 1/2 exactly). Both are Gram matrices of rank-one
edge-block data.

**P2 rotation curve (all D>=2, established derivation).** Fix a spectrum lam and a pair
lam_i != lam_j. Let U(theta) be the identity except the real 2x2 rotation by theta on the
(i,j)-coordinate plane, G(theta)=U(theta) diag(lam) U(theta)\(\dagger\). The spectrum is exactly
fixed (conjugation; symbolically checked: charpoly difference identically zero, S2). The diagonal:
d_i(theta)=lam_i+(lam_j-lam_i)sin^2 theta, d_j(theta)=lam_j-(lam_j-lam_i)sin^2 theta, others
fixed; and P_2(theta)=sum_j lam_j^2 - 2(lam_i-lam_j)^2 sin^2 theta cos^2 theta (verified
symbolically, S2 `S2.P2_curve_form`), strictly varying for theta in (0,pi/2). So the diagonal
image of every non-constant fibre contains a non-constant real-analytic curve; in particular the
diagonal tuple is not determined pointwise by the spectrum anywhere on that fibre. Realizability
of fibre points inside the subclass: any G>=0 of rank <= D factors as AA\(\dagger\) (spectral
factorization; Cholesky when positive definite) and the named gaussian law of A has full support
on such A — a support-level statement exactly as in the accepted 095 step 1 (these exact fibre
points form a null set; they are counterexamples to determinacy on the support, not to the a.e.
statement, which is proved separately below).

**P3 D=3 patch (established derivation).** For lam in R^3 and U=R_23(phi) R_12(theta) (product of
the two plane rotations), d_1(theta)=lam_1 cos^2 theta+lam_2 sin^2 theta and
d_2(theta,phi)=(lam_1 sin^2 theta+lam_2 cos^2 theta)cos^2 phi+lam_3 sin^2 phi, d_3=tau-d_1-d_2.
The Jacobian of (d_1,d_2) w.r.t. (theta,phi) is triangular because d_1 is phi-free:
det = (lam_2-lam_1) sin 2theta * (lam_3-lam_1 sin^2 theta-lam_2 cos^2 theta) sin 2phi, which at
theta=phi=pi/4 equals (lam_2-lam_1)(lam_3-(lam_1+lam_2)/2) — verified symbolically with generic
lam and anchored numerically (`verify_096.py` S3, both checks simplify to 0). Relabelling
coverage for every non-constant triple (permutation conjugation only permutes d, so the
construction may be applied to any relabelling): (i) if lam_3=(lam_1+lam_2)/2 with lam_1 != lam_2,
relabel to (lam_1,lam_3,lam_2): then lam_3 != lam_1 (else lam_1=lam_2) and the new third entry
satisfies lam_2-(lam_1+lam_3)/2=(lam_2-lam_1)/2 != 0; (ii) exactly two distinct values with
multiplicities (2,1), say (a,a,b): relabel to (a,b,a): product=(b-a)(a-(a+b)/2)=-(a-b)^2/2 != 0;
(iii) multiplicities (1,2), say (a,b,b): relabel to (b,a,b): product=(a-b)(b-(a+b)/2)=(a-b)^2/2 != 0.
Checked exhaustively on a 15^3 rational grid (`S3b`, no counterexample). Rank 2 at that point
plus the inverse function theorem gives that the image of (theta,phi) -> (d_1,d_2) contains an
open neighbourhood in R^2, hence the diagonal image contains a 2-dimensional patch with non-empty
interior in the trace hyperplane sum d_i = tau (relative topology).

### Measure side (general D)

**M1 unitary invariance (established).** Left multiplication of A by any fixed V in U(M) (when
D=M-rows case: act on the rows; in general the side of size max(M,N-M)) conjugates G -> VGV\(\dagger\)
and preserves the iid CN(0,sigma^2) law of the entries, so the law of G is invariant under unitary
conjugation. D-independent (same step as the accepted 095 step 3).

**M2 conditional Haar given the spectrum (established, modulo standard background).** The
spectrum map is invariant and separates orbits (spectral theorem); each fibre
{G >= 0 : spec = lam} is the compact homogeneous space U(D)/(U(m_1) x ... x U(m_r)) conjugating
diag(lam) (m_a = multiplicities), which carries a unique conjugation-invariant probability
measure (normalized orbit/Haar measure). A regular conditional law of G given p exists (support
in a Polish space); by M1 and uniqueness of regular conditionals it is, for almost every
spectrum value, the unique invariant probability on the corresponding fibre, i.e.
G = U diag(lam) U\(\dagger\) with U Haar. The eigenvalue-collision set carries no mass under the
named law (the eigenvalue law is absolutely continuous on the ordered chamber — the Vandermonde-
squared chart Jacobian of that law is the integrated 091 record, L3195, and the named density is
locally bounded there). Standard background used: spectral theorem; existence/uniqueness of the
invariant probability on a compact homogeneous space; regular conditional probabilities on
Polish spaces — named as standard, not cited. The identical step was gatekeeper-accepted at D=2
in 095 review-r1/review-r2; the argument above is dimension-free.

**M3 uniform simplex row law (established, self-contained).** z in C^D with iid CN(0,1) entries is
U(D)-invariant in law; writing z_j = sqrt(E_j) e^{i theta_j}, E_j=|z_j|^2 are iid Exp(1) (polar
change of variables on C: density (1/pi) e^{-(x^2+y^2)} dxdy -> (1/2)e^{-e} de ... with the
normalization giving E_j Exp(1) exactly under the standard CN(0,1) convention used here) and
theta_j uniform, independent. The normalized vector X_j=E_j/sum_k E_k is the squared-modulus
vector of the normalization of z, whose law is the unique U(D)-invariant probability on the
complex sphere, i.e. the Haar first row's squared-moduli law. Change of variables
(E_1,...,E_D) -> (T, s_1,...,s_{D-1}), E_i=T s_i, sum s=1: joint of E is e^{-sum E}; the map
(E_1,E_2,E_3)=(T s_1, T s_2, T(1-s_1-s_2)) has Jacobian T^{D-1} (= T^2 at D=3, verified
symbolically, S4 `S4.simplex_density`), so the joint of (T,s) is e^{-T} T^{D-1} on
(0,inf) x simplex: T ~ Gamma(D) and s has the constant density (D-1)! on the simplex (integrating
T gives Gamma(D)=(D-1)!; at D=3 the simplex density is 2, S4). Hence the first-row squared
moduli are uniform on the simplex — Dirichlet(1,...,1) — for every D.

**M4 non-atomicity of non-constant linear forms (established, all D).** For lam non-constant and
X uniform on the simplex, L=sum_j lam_j X_j.
- Two-valued lam (values a>b with multiplicity r of a): L = b + (a-b) S, S = sum over r
  coordinates; in the exponential model S = (E_1+...+E_r)/(sum all), and the change of variables
  (sum of r gammas, sum of D-r gammas) -> (total, fraction) with the T^{D-1} bookkeeping gives
  fraction ~ Beta(r, D-r), whose density is strictly positive on (0,1); L is an affine image,
  non-atomic. At D=3 equal-outer cases this is the Beta(2,1) density 2t (or mirrored 2(1-t)).
- Three-distinct D=3, ordered lam_1>lam_2>lam_3, mu=(lam_2-lam_3)/(lam_1-lam_3) in (0,1):
  tilde L = (L-lam_3)/(lam_1-lam_3) = X_1 + mu X_2. The CDF is 2x the simplex area below the line
  x_1 + mu x_2 = t: F(t)=t^2/mu for 0<t<=mu, F(t)=1-(1-t)^2/(1-mu) for mu<t<1 (both pieces
  verified as exact triangle-area computations, S5 `S5.cdf_match`); density
  f(t)=2 min(t/mu,(1-t)/(1-mu)), continuous at mu (f=2 there), integrating to mu+(1-mu)=1
  (S5 `S5.normalizes`). Positive on (0,1), so non-atomic.
- General D (stick-breaking, full induction): write X=(B,(1-B)X'), B=E_1/(E_1+R),
  R=E_2+...+E_D, X' the normalized (E_2,...,E_D). Independence: (C,R)=(E_1,R) have product
  gamma densities e^{-c} dr e^{-r}; (C,R) -> (B=C/(C+R), T=C+R) has Jacobian T and factors into
  [T^{D-1}e^{-T}] x [(D-1)(1-b)^{D-2}] — B ~ Beta(1,D-1) independent of T, and X' depends only
  on (E_2,...,E_D), i.e. on T and an independent uniform simplex point (same M3 computation in
  dimension D-1); numerically confirmed at D=4 (S6: mean 0.25, variance 3/80=0.0375 Beta(1,3);
  correlation |corr(B(1-B),X'_1)|<0.02). Induction: conditional on B=b (a.s. b in (0,1)),
  L = lam_1 b + (1-b) L', L' a linear form of X'. If (lam_2,...,lam_D) is non-constant, L' is
  non-atomic by the induction hypothesis, so P(L=c | B=b)=0 for a.e. b and P(L=c)=0. If
  (lam_2,...,lam_D) is constant = q != lam_1, L = lam_1 B + q(1-B) is a non-constant affine
  image of the non-atomic B. The all-constant case is excluded. Base D=2: L is affine in
  B ~ Uniform(0,1) (Beta(1,1)), the 095 D=2 case. Non-atomicity for every D and every
  non-constant lam is thereby fully proved (no induction step left open). Numerically the
  band-probability scaling is linear at D=3 (S7: P(|L-c|<eps) ratios ~2 across eps=1e-3/2e-3/4e-3,
  both distinct and equal-pair spectra), as expected for a bounded density.

**Theorem T (a.e. non-recovery, all D>=2, established derivation).** By M2, conditional on
p=(lam/tau) (a.e. non-constant by the collision-null-set fact), d is the image of the Haar orbit;
its first coordinate G_11/tau = sum_j lam_j |u_1j|^2 has by M3+M4 a non-atomic conditional law.
Hence the conditional law of the whole tuple d is non-atomic (a point mass of d would project to
one), and for any map F, P(d = F(p)) = E[ P(d = F(p) | p) ] = 0, since F(p) is p-measurable as a
value; for non-measurable F read the probability as outer probability (identical remark to the
accepted 095 step 3). For the power-sum tuple: the full power sums (P_1=1,...,P_D) determine the
multiset {d_i} exactly (Newton's identities: power sums <-> elementary symmetric functions <->
the monic polynomial with roots d_i), so d -> (P_2,...,P_D)(d) has at most D! preimages per
value; a point probability of the tuple is a probability of at most D! points of d, all zero.
The rho-family at d is carried by the exact power-sum recursion of the integrated 092 paragraph,
so the same statement transfers. This is the full general-D upgrade of 095's chain with 095's
conditioning structure untouched.

**Single-statistic caveat.** Non-recovery of the single number P_2 at D>=3 is NOT claimed: its
conditional nonatomicity is a quadratic-form statement not covered by M4 (at D=2 it is exactly
the 095 result). The insert claims only the tuple statements and P2-along-the-curve (pointwise).

Comparison with the original target: rank-one obstruction at every D>=2 — delivered (P1).
Generic-spectrum positive-dimensional fibre image — delivered (curve for all D via explicit
rotations, no Schur-Horn citation; patch with interior at D=3 via Jacobian + IFT). a.e. full-tuple
general-D upgrade — delivered, measure side fully proved for all D (the induction was completed,
not sketched). Self-containment — delivered: the insert cites nothing; the only external inputs
are standard background facts (spectral theorem, Haar existence/uniqueness on compact groups,
regular conditionals, inverse function theorem), each named and non-load-bearing on literature
sources. The full permutahedron identification was NOT proved and is declared outside the
insert's content.

Literature: none used in the insert (frontier rule). 095 r2's Schur-Horn flags (not
independently verified) are not imported; nothing rests on them.

## Claim classification

- P1 rank-one pair, P2 rotation curve and P2-along-curve formula, P3 Jacobian closed form,
  relabelling coverage, D=3 patch: **established derivation** (symbolic verification S1-S3b;
  IFT step is standard calculus).
- M1 unitary invariance: **established derivation** (iid gaussian left-mixing).
- M2 conditional Haar: **established derivation modulo named standard background** (spectral
  theorem; unique invariant probability on compact homogeneous fibre; regular conditionals);
  eigenvalue AC law **conditional on the integrated 091 chart record** (used only for
  collision-nullity).
- M3 uniform simplex row law: **established derivation** (self-contained; S4).
- M4 nonatomicity all D (two-valued Beta, D=3 explicit density, stick-breaking induction):
  **established derivation** (S5-S7 numerical confirmations accompany, do not replace, proofs).
- Theorem T a.e. non-recovery of d, (P_2,...,P_D), and the rho-family at d, all D>=2:
  **established derivation** (chain M1->M2->M3->M4 + 095-accepted conditioning identity).
- Non-recovery of the single scalar P_2 at D>=3: **not claimed** (open).
- Fibre diagonal image = full Schur-Horn permutahedron at general D: **not proved; conjecture/
  mechanism** (classical theorem route, deliberately uncited).
- Realizability of exact fibre points by edge-block configurations: **established at support
  level** (factorization + full support of the named law; these points are null).

## Proposed changes

Files touched: `chapters/appH-microscopic-proofs.tex` only; one pure insertion. The artifact is
the bytes of `insert-r1.tex` (4,727 B / sha8 35c4a723; 4,725 content bytes + terminal CRLF). Do
not retype the insert; integrate from the file bytes only. (No superseded drafts exist.)

- Anchor: the 095 tail sentence read verbatim from live appH line 3203 (starts "These statements
  are exact linear-algebraic identifiability statements", ends "close nothing in Problem~G.",
  471 bytes) + CRLFCRLF + line-initial `\emph{Vacuum term.}` — compound PIN count exactly 1
  (asserted by the script).
- Splice: `appH[:cut] + insert_bytes + ONE CRLF + appH[cut:]`, cut = byte index of the
  line-initial `\emph{Vacuum term.}` (= PIN index + 471 + 4); the preceding blank line is
  preserved; the insert + its own terminal CRLF + the splice CRLF give a blank line between the
  new paragraph and Vacuum, so the new paragraph is standalone. No existing equation, sentence,
  label or status text is modified; nothing else in the repository references this passage.
- Expected POST (printed by `simulate_apply_096.py`): size 780,748 = 776,019 + 4,727 + 2; sha256
  0e4c097b078e020bcf8165bf6b78680ea8b0d40ca0369361ddb3b9efec3aed5b; CRLF 3,856; bareLF 0;
  close-idiom noun 21 -> 22; verb "closes nothing" 1; `\emph{Vacuum term.}` 2; new header count
  0 -> 1 (header unique across chapters/ pre-splice, verified count 0).
- No new labels, refs, or bib entries; no `\cite`/`\ref`/`\eqref`/`\label`/`$`/`[`/`]` in the
  insert (checked). Stale passages created: none — the 095 paragraph and the 091 "not supplied"
  sentences stay true as records of their integration time; the closer at L3207 stays true.

## Verification scripts

All under this folder; run from repo root with `python -I`; deterministic (fixed sympy expressions;
numpy seed 20261119). Reproduction pack (order): (1) `verify_096.py`, (2) `simulate_apply_096.py`,
(3) `hygiene_096.py`.

- `verify_096.py` -> `verify_096.out` — S1 rank-one charpoly/diagonal pairs at D=3,4; S2 rotation
  charpoly fixed + curve non-constancy + P2-curve formula + pi/4 anchor; S3 D=3 two-angle
  Jacobian closed form (numeric and generic-symbolic, both simplify to 0); S3b relabelling
  coverage on a 15^3 rational grid; S4 simplex change-of-variables density (Jacobian T^2, density
  2, total 1) + MC Haar-row moments; S5 D=3 piecewise-linear density: normalization 1, CDF
  derivative match, endpoints, MC CDF agreement; S6 stick-breaking Beta(1,3) marginal +
  independence at D=4; S7 band-probability linear scaling (non-atomicity numerics, two spectrum
  types); S8 tuple spread under the named law at D=3 in a spectrum band (widths 0.183/0.166 of
  P_2/P_3). **Expected:** all 24 `chk` lines PASS; `S8.count 715779 S8.widthP2 0.1830 S8.widthP3
  0.1664`; final line `SUMMARY ALL PASS`.
- `simulate_apply_096.py` -> `simulate_apply_096.out` — read-only splice simulation; re-measures
  and asserts live PRE (776,019 / sha256 600588c1...fa0d / CRLF 3,854 / bareLF 0), prints the
  471-byte PIN tail head/tail and asserts PIN count 1, cut line-initiality, then POST: **expected**
  `POST_SIZE 780748`, `POST_SHA256 0e4c097b078e020bcf8165bf6b78680ea8b0d40ca0369361ddb3b9efec3aed5b`,
  `POST_CRLF 3856`, bareLF 0, idiom 21->22, verb 1, Vacuum 2, prefix/suffix identity;
  `INSERT_SIZE 4727 INSERT_SHA8 35c4a723`; `SUMMARY ALL PASS`. No writes.
- `hygiene_096.py` -> `hygiene_096.out` — insert hygiene: one content line + terminal CRLF, pure
  ASCII, no `$`/`[`/`]`/`\cite`/`\ref`/`\eqref`/`\label`, exactly one `\emph{` header ending in a
  period, banned status/closure vocabulary scan (status|priority|completion|open|critical|
  programme|derived, word-boundary, case-insensitive), idiom exactly once and at end, math
  and brace balance, appH PRE identity + idiom counts (21/1/2), header uniqueness across
  `chapters/*.tex` (0 hits). **Expected:** `INSERT_SIZE 4727 INSERT_SHA8 35c4a723`,
  `SUMMARY ALL PASS`.

## Decisions Taken

1. **Claim scope set to what was actually proved**: a.e. non-recovery of the full tuple claimed
   for all D>=2 (measure side fully inducted), fibre-patch content restricted to D=3, single-
   statistic P2 non-recovery at D>=3 dropped (not proved). Rejected: claiming "at D>=3" for the
   a.e. theorem (understated a proved general result) and claiming the permutahedron interior at
   general D (not proved). Favors the derivation: strongest honestly-proved negative.
2. **Exponential-construction proof of M3** (self-contained gamma algebra) over the sphere-
   invariance/uniqueness route (needs uniqueness of the rotation-invariant measure); both prove
   the same fact, the first is fully elementary.
3. **Constructive rotation+IFT route for the fibre-dimension content** over any Schur-Horn-style
   statement; complies with the frontier "no literature citation without the self-contained proof"
   by citing nothing. Rejected: importing Schur-Horn with an unverified citation.
4. **Kept the 095 paragraph, the 091 "not supplied" record, and all labels untouched**; the new
   paragraph records the extension in place of editing history.
5. **Power sums as the tuple coordinates** (Newton bijection to the rho-family via the recorded
   092 recursion), rejecting a direct rho-family computation (identical content, extra conversion
   steps to verify).

## Milestone assessment

Routine. A bounded negative sub-lemma extension (general-D a.e. non-bridge for the full diagonal
moment tuple + D=3 fibre-patch geometry) on the chain-2 edge; no milestone trigger; no
critical-path step closed.

## Status-label recommendation

Critical-path set re-derived from the agenda/ledger as quoted: A, B, C, D1, E, F, G-derived, N
(G itself OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL). **All labels unchanged** by this package.

## Author decision needed

None.

## Remaining open step

For the original G exactness route nothing closes; for the chain-2 edge the ranked avenues are:
1. General-D fibre diagonal image: interior in the trace hyperplane (permutahedron identification)
   via a completed self-contained induction extending the D=3 Jacobian — the last unproved
   pointwise strengthening; not needed for Theorem T.
2. Single-statistic non-recovery (P_2 alone) at D>=3 under the named law: needs conditional
   nonatomicity of a quadratic form of the uniform simplex vector.
3. Quantitative profile-information gap (mutual information between p and d) under the named law
   at D>=3 — now computable in principle given M3/M4.
4. Heterogeneous-variance edge blocks: does the non-bridge persist when the block variance
   profile is non-constant (breaks unitary invariance of the Gram law — the a.e. chain needs
   replacement; pointwise claims P1-P3 are unaffected).
5. State-side profile weight (the actual missing ingredient per 089-091; hardest, untouched).

## Special instructions for the gatekeeper

- The insert asserts strictly less than the record proves: no permutahedron claim, no single-P2
  claim at D>=3, no D=1 content; check the insert's claims are a subset of the classification
  above, and that the relative-paragraph pointers (fifth = L3195, fourth = L3197, first = L3203,
  from the new insertion point) are correct after your anchor re-verification against the live tree.
- Re-derive independently: (a) the D=3 Jacobian det at (pi/4,pi/4) = (lam2-lam1)(lam3-(lam1+lam2)/2)
  and the two relabelling exception cases; (b) the D=3 density via the two-triangle CDF and its
  normalization; (c) the stick-breaking independence Jacobian; (d) the finite-fiber (Newton) step
  for the power-sum tuple.
- Byte contract: re-measure PRE (776,019 / 600588c1...fa0d / CRLF 3,854 / bareLF 0) and STOP if
  moved; artifact `insert-r1.tex` 4,727 B / sha8 35c4a723 — take bytes from the file only.
- appH contains non-ASCII UTF-8; splice scripts compare bytes.
- Hygiene banned-word scan includes "open": the insert uses "non-empty interior" precisely to
  avoid that word; do not "fix" it to "open".

## Security

- Injection scan of all files read this round and written to this folder for the known enforcement
  markers ("[handback-send-enforce]", "SubagentHandback") and instruction-shaped strings: no hits
  in any file written here; the two known self-disclosure mentions inside 095's own Security
  section are quoted data, already disclosed there; nothing found inside data was obeyed.
- All writes confined to `proposals/096-g-nonbridge-extension-d3/`; no git write commands; nothing
  in `chapters/`, `bib/`, `reports/`, or any other proposal folder was modified; digests and
  scripts only read (`make_digest.py --check` checked, never run).
