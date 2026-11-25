# Proposal 118-presentation-a-potential-selection, round 1 (stage B of a split chain)

**Package.** `proposals/118-presentation-a-potential-selection/`. Round 1, stage B. Deliverables:
this `proposal-r1.md` plus an append to `scratch/118/notes.md`. No manuscript text, no generator,
no certificate, no manifest (stage C). Verification pack: `verify_r118_r2.py` (reproduction pack
below; 13/13 PASS).

**State.** 2026-11-23; branch `local/gpu`, HEAD `8b9ff39`; `chapters/appH-microscopic-proofs.tex`
sha1 `ce91063fddcaa5599429519f4bc2c478e0d919e8` (839337 B, working tree as delivered by items
114-117); `python -I scripts/make_digest.py --check` prints `DIGEST CURRENT`. All scripts run with
`python -I -B`.

**Scope as dispatched.** Derive or constrain the Presentation-A selection of `eq:V` - what the
matrix-coordinate action `eq:Smatrix` gives, under the infrared dictionary `ass:dictionary`, for
the quartic Higgs-type potential `eq:V` and its parameters (lambda, v, vacuum manifold
`eq:vacuum-manifold`) used by appH items 114-117.

## Result

The Presentation-A selection question for `eq:V` is **constrained, not closed**. Consequential
findings (tiers per result below; rule 3: nothing in this package closes Problem D, D1 or A; the
status of appH items 114-117 is unchanged; rule 2: no status label is changed or proposed to
change anywhere in this package; spacetime stays emergent - every object is a matrix coordinate or
an internal matrix, no fundamental metric is proposed or pursued):

1. **Invariant-theoretic constraint.** The most general real quartic matter potential for the
   bifundamental `Phi` allowed by the stated field content (eq:Phi-transform, ch03 L276-289) is
   the two-parameter family `V = c3 Tr X^2 + c2 (Tr X)^2 + c1 Tr X + c0`, `X = Phi^dagger Phi`.
   `eq:V` is the slice `(c3,c2,c1,c0) = (lambda/4, 0, -lambda v^2/2, lambda v^4)` (internal
   dimension 4) - exact normal-form identity. The selection question sharpens from "why eq:V" to
   "why this slice" (the ratio c2/c3 and the signs).
2. **Family-wide extension of the 114-117 geometry.** Throughout the strictly bounded-below class
   of that family (`c3>0`, `c3+4c2>0` - the same region as strict convexity in `x = sigma^2`):
   unique vacuum `Phi^dagger Phi = s I`, `s = -c1/(2(c3+4c2))`; `inf` over `{det Phi = 0}` is the
   stratum-3 value at singular values `(0,w,w,w)`, `w^2 = -c1/(2(c3+3c2))`; and the threshold
   `Delta = (c1^2/4)[1/(c3/4+c2) - 1/(c3/3+c2)]` is strictly positive through the whole bounded
   class (corridor gap `c3/12`). On the `eq:V` slice: `s = v^2`, `V_vac = 0`, `Delta = lambda
   v^4/4` - the appH L1711 defect threshold re-derived as a slice of a family theorem; off-slice
   the face minimizer moves (`w != s`), so threshold positivity is universal in the class while
   its value is slice-dependent.
3. **Moyal channel-distinctness constraint.** From the star product fixed at sec:ch3-relate (ch03
   L375-381): the n-point vertex phase `exp(-(i/2) Sum_{i<j} k_i wedge k_j)` is exactly cyclic on
   the momentum-conservation shell (n=3,4,5), reduces at 4 points to `k1^k2 + k3^k4 = k2^k3 +
   k4^k1` and is nonzero; the three quartic channel factors `cos(theta p/2)`, `cos(theta q/2)`,
   `cos(theta(p+q)/2)` are pairwise distinct and degenerate flatly at `theta = 0`, with `1 -
   cos(theta p/2) = theta^2 p^2/8 + O(theta^4)` (even orders only). A local channel-blind
   Tr-polynomial vertex, `eq:V` included, can match the Presentation-A quartic vertex only as the
   `theta -> 0` truncation with first deviation O(theta^2): the precise sense in which `eq:V` is
   a truncation output, never an exact finite-Theta output, of the stated Presentation A.
4. **Beyond-quartic bounding.** The defect-threshold property fails outside the quartic class:
   `V = eps (Tr X)^4 - Tr X^2` (eps = 0.3) is bounded below and its global minimum lies ON
   `{det Phi = 0}` (rank-1 singular values, value `-1/(4 eps)`), strictly below every
   equipartition point. "Defects cost lambda v^4/4" is a theorem of the quartic class (the c3/12
   corridor argument), not of bounded matrix potentials in general.

## Target and status

- **Problem (as dispatched).** The Presentation-A selection of `eq:V`. This is a named missing
  input, not a separate Appendix H problem letter: it is recorded in the ledger as the open item
  of Section `sec:ch3-relate` feeding Problem D (appH L765 "Problem D: local Lorentz"; L769
  "Status: OPEN. Priority: CRITICAL PATH. Completion:") and as what gates the citability of the
  Presentation-B measures of items 114-117 (appH L1713, L1715). Problem A is the derivation of
  the dictionary itself (ch17 L377-392, "OPEN; CRITICAL PATH for the matrix-derived label").
- **Current status (live-tree, re-read this round).** Problem D: OPEN, CRITICAL PATH,
  PROGRAMME-CONDITIONAL (appH L768-772). Problem A: OPEN, CRITICAL PATH for the matrix-derived
  label (ch17 L377-378). Problem D1 item of the completion list: ch17 L715-720. D2 reminder: ch17
  L737-745 ("Problem~D stays OPEN and CRITICAL PATH"). ch17 L361: "Problem~D is unresolved."
- **Original target (for the record).** Derive from `eq:Smatrix`, under the dictionary, the
  potential `V(Phi^dagger Phi) = (lambda/4) Tr(Phi^dagger Phi - v^2 I)^2` (eq:V, ch03 L240-245)
  with `(lambda, v)` expressed in matrix-action data, and the vacuum manifold `eq:vacuum-manifold`
  (ch03 L247-250). DERIVED vs PROGRAMME-CONDITIONAL: nothing in this package is a derivation of
  the selection; the package is a constraint-plus-sub-lemma package feeding the named missing
  step. Every result below carries its rule-6 tier.
- **Dependencies (residual assumptions the results consume).** `ass:dictionary` as a matching
  condition (ch03 L345-363: "this is a matching condition, not an established result", L360-361);
  the eq:Phi-transform field content (ch03 L287-288: "It is a choice of field content. It is not
  derived from Presentation~A alone"); quartic (renormalizable, degree-(2,2)) truncation;
  c-number Theta of Definition def:matrix-coords / eq:NC; internal dimension 4 for the eq:V slice.

## Mission connection

Quotations, each re-grepped against the live tree (offsets are character indices into the line):

- appH **L1715** (offset 4372): "and the selection of Equation~\eqref{eq:V} by Presentation~A
  (Section~\ref{sec:ch3-relate}) remains the upstream input that gates what any Presentation-B
  measure can be cited as; Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg} remain assumed,
  so Problem~D remains OPEN and PROGRAMME-CONDITIONAL." (final clause quoted from the same line;
  the sentence continues to the line end). This is the sentence the dispatch cites; the package
  attacks exactly this upstream input by sharpening and constraining it.
- appH **L795-808**, Problem D "Missing step." (live-read in full): "Derive \(\mathrm{SO}(3,1)\)
  from the matrix algebra alone, or state that Presentation~A is not ontologically prior (the
  present text does the latter), and derive the effective dynamics of the independent diagonal
  connection or retain it as unresolved field content." (L796-800); "The locked frame and its
  non-degeneracy must also be derived rather than assumed (Assumptions~\ref{ass:frame-lock}
  and~\ref{ass:nondeg})." (L801-802); "specifying the full operator content does not close D or
  meet the matrix-derived criterion." (L804-805).
- appH **L1713** (offset 3682): "the selection of Equation~\eqref{eq:V} by Presentation~A remains
  the missing input of Section~\ref{sec:ch3-relate};"
- appH **L1711** (offset 720), the item-114 formula this package re-derives as a slice:
  "\(\inf\{\mathcal V:\det\Phi=0\}=\lambda v^4/4\), attained exactly at singular values
  \((0,v,v,v)\)".
- ch03 **L365-366**: "Assumption~\ref{ass:dictionary} is the most important unproved bridge in
  the microscopic setup."; ch03 **L358-361**: "Under this dictionary the quadratic commutator
  term in~\eqref{eq:Smatrix} is required to generate the kinetic term in~\eqref{eq:Smicro},
  including its sign in the signature \((-,+,+,+)\); this is a matching condition, not an
  established result."
- ch03 **L398-401** (Moyal remark scope, which bounds result R7): "This verifies the
  coordinate-background kinematic identity, but not the full dictionary \eqref{eq:dictionary} for
  fluctuating matrix coordinates, a gauge connection, or nonconstant \(\Theta\)."
- ch03 **L243-244** (eq:V): "V(\Phi^\dagger\Phi) =\frac{\lambda}{4} \mathrm{Tr}\bigl(
  \Phi^\dagger\Phi-v^2\mathbb{I}\bigr)^2."; **L249** (eq:vacuum-manifold):
  "\Phi^\dagger\Phi=v^2\mathbb{I}"; **L313-314** (eq:Phi-eom potential term): "\frac{\lambda}{2}
  \Phi \bigl(\Phi^\dagger\Phi-v^2\mathbb{I}\bigr)"; **L287-288**: "It is a choice of field
  content. It is not derived from Presentation~A alone".
- ch04 **L171-174** (ass:nondeg): "On the region of spacetime under consideration, \(e^A_\mu\)
  has non-vanishing determinant."

## Source reading

Digest + targeted reads; digest status `DIGEST CURRENT`; no unreadable files. Digest grep entries
used for navigation: scratch/digest.md L70 (appH L765 section "Problem D: local Lorentz"), L231
(label sec:status-D at appH:766), L262-264 (eq:Smatrix scope lines at appH L1636/1675/1702), L265
(L1711 eq:V paragraph), L306 and L313 (ch17 L344, L740), L188 ("chapters/ch03-matrix-action.tex
(unchanged, 916 lines)").

Live passages read IN FULL this round: appH L795-809; appH L1711, L1713, L1715 (exact quoted
windows extracted live by python, not from cache); ch17-agenda L355-400 (Problem D closure
context L355-370 incl. L361; Problem A passage L377-392 incl. eq:dict-again L384-389);
ch17-agenda L645-720 (order of work L650-676; "What finished would mean" L693-720); ch17-agenda
L720-754 (D2 paragraph L737-745); ch03 L335-410 (sec:ch3-relate; ass:dictionary + eq:dictionary
L345-363; Moyal-check remark incl. the live star product L371-401; K-Theta display L403-410);
ch03 L218-267 (eq:Smicro L220-228; eq:V L240-245; eq:vacuum-manifold L247-250; eq:VEV L253-256;
ass:frame-lock L264-267); ch03 L300-321 (eq:Phi-eom L308-316); ch04 L85-96 (eq:vev-is-frame
L90-95); ch04 L166-181 (ass:nondeg L170-175). Label-to-line grep across chapters/ for every label
used: eq:Smatrix ch03:143, eq:Smicro ch03:221, eq:V ch03:241, eq:vacuum-manifold ch03:248, eq:VEV
ch03:254, ass:frame-lock ch03:265, eq:Phi-eom ch03:310, ass:dictionary ch03:346, eq:vev-is-frame
ch04:91, ass:nondeg ch04:171. Cached excerpts in scratch/118/ were used for navigation only; no
quotation in this proposal is taken from them.


## Numbered results

Each entry gives (a) the exact mathematical statement as checked, (b) its rule-6 tier, (c) the
verify-pack check id (C1-C10, N11-N13) that tests it and its stated parameter range (ranges as
printed in the r2 COVERAGE lines plus the check code).

**R1 - Normal-form identity and parameter map of eq:V.**
(a) For `x_i = sigma_i(Phi)^2` and any N: `Sum_i (lambda/4)(x_i - v^2)^2 = Sum_i [(lambda/4)
x_i^2 - (lambda v^2/2) x_i] + N lambda v^4/4`; equivalently eq:V is the standard-form quartic
with `(c4, c2, c0) = (lambda/4, -lambda v^2/2, N lambda v^4/4)`; the constant must match the
number of squared terms (teeth: an N-indexed constant over 4 squares differs exactly at N=7; an
independent explicit 6-coordinate identity with `c0 = 6 c4 v^4`); and `-c2/(2 c4) = v^2`.
(b) Established identity (exact symbolic polynomial check) with numerical re-check.
(c) C1 (symbolic, generic `lambda, v > 0`; N=4 exact, N=7 mismatch tooth, explicit N=6 build);
C9 (200 random `lambda in (0.01,10)`, `v in (0.01,5)`, `sigma in [0,5)^4`; abs tol 1e-10 relative
for `v^2`, rel 1e-8 for the identity). Live anchors: eq:V ch03 L241-244; the singular-value form
at appH L1711.

**R2 - Gradient identity; vacuum stationarity; match to eq:Phi-eom.**
(a) For `V(Phi) = (lambda/4) Tr X^2 - (lambda v^2/2) Tr X` with `X = Phi^dagger Phi`, the
conjugate-Wirtinger gradient is `G = (lambda/2) Phi (X - v^2 I)`; verified componentwise by
central differences (real and imaginary directions, h = 1e-6, 40 random complex 4x4 Phi with
amplitude sweeps): `max |0.5(delta_re + i delta_im) - G| < 2e-4`. This is exactly the potential
term of eq:Phi-eom (ch03 L310-315), the display `\frac{\lambda}{2}\Phi
(\Phi^\dagger\Phi-v^2\mathbb{I})` (L313-314), up to the sqrt(-g) factor, consistent with
eq:Phi-eom = kinetic minus this. Consequently every point of eq:vacuum-manifold
`Phi^dagger Phi = v^2 I` (ch03 L248-249) is stationary (explicit check at `Phi = v I`, lambda in
{0.5, 1.0, 3.7}, v in {0.3, 1.0, 2.5}, atol 1e-14). Disclosure: the explicit vacuum sub-loop
substitutes `X = v^2 I` and `v^2 I`, so its vanishing is by construction; the derived content is
the gradient identity, from which vacuum stationarity is the corollary
`Phi^dagger Phi = v^2 I => G = 0` for every point of the manifold, not only the diagonal slice.
(b) Established derivation (numerically verified identity; corollary by substitution). (c) C2
(ranges as in (a); seeded RNG 118).

**R3 - Honest full sign classification of the single-site normal form; SOS decomposition;
separability; power-mean teeth.**
(a) With `f(s) = c4 s^4 + c2 s^2` (s >= 0) and `s*^2 := -c2/(2 c4)` (c4 != 0): exact identity
`Sum_{i=1..4} f(s_i) - 4(-c2^2/(4 c4)) = c4 Sum_i (s_i^2 - s*^2)^2`; hence `c4>0 and c2<0`
(Mexican-hat region) has global minimum at all `s_i = s*`, value `-c2^2/c4`, with the sum-of-
squares rate. Full classification, tested region-by-region: `c4<0`, or `c4=0 and c2<0`: unbounded
below; `c4>0 and c2>=0`, or `c4=0 and c2>0`: minimum at 0; `c4=c2=0`: identically zero; `c4<0 and
c2>0`: an interior stationary point exists but is a hilltop (located as a maximum - tooth). eq:V
lies in the Mexican-hat region for `lambda, v > 0` (by R1: `c4 = lambda/4 > 0`, `c2 = -lambda
v^2/2 < 0`). The separable N-site sum attains its minimum with each site independently at
argmin f (vacuum set `(argmin f)^N`), the structural fact behind eq:vacuum-manifold being "all
sigma_i equal v"; power-mean teeth: for `x_i >= 0` with `Sum x_i = tau`: `Sum x_i^2 >= tau^2/4`
and `Sum x_i^3 >= tau^3/16`, equality iff uniform.
(b) Established elementary derivation (exact symbolic identity; exhaustive 3x3 sign grid).
(c) C3r (symbolic identity generic nonzero `(c4,c2s)`; 18-point closed grid over all nine
`(c4,c2)` sign regions incl. the `c4=0` rows, magnitudes {2, 0.37, 0, 0.11, 3}, s-grid 24001
points on [0,60]; 60 random Mexican-hat minima, `c4 in (0.05,4)`, `c2 in (-4,-0.05)`); C7
(power-mean teeth at 400 random simplex points, tau = 4; region scans at (a,b) in {(1,-1), (1,1),
(1,0), (0.25,-3), (4,-0.1), (0,1)}). Inert conjuncts disclosed in Provenance (one trivially-true
term each in the C3r hilltop branch and in the C7 region scan; nothing load-bearing rests on
them).

**R4 - Invariant classification: what quartic terms Presentation A can write.**
(a) Single-matrix GL(n)-conjugation invariant polynomials of degree d on complex n x n matrices:
`dim = number of partitions of d into parts <= n` (equivalently at most n parts). Verified by the
rank of the linearized gl(n) action (integer matrices, rank tol 1e-9) at (n,d) in {(2,1),(2,2),
(2,3),(2,4),(3,4),(4,1),(4,2),(4,4)} with values (1,2,2,3), 4, 5, 2, 1; Cayley-Hamilton teeth:
naive p(d) fails at n=2, d=3,4 (2,3 vs 3,5); dim(n=4,d=4)=5 vs dim(2,4)=3 vs dim(3,4)=4. The
kernel at n=4, d=2 is exactly spanned by the two independent vectors of the words `Tr Z^2`,
`(Tr Z)^2` (membership Kv=0, independence rank 2, dim = 2). Bifundamental teeth: `Tr X^2` is
invariant under independent (U,V) in U(4)xU(4), `Phi -> U Phi V^dagger` (|delta| < 1e-8/1e-7 over
20/60 random unitaries), while the word `Re Tr(Phi^2 (Phi^dagger)^2)` is not (|delta| > 1e-6);
word identities `Tr(Phi^dagger Phi Phi^dagger Phi) = Tr(Phi Phi^dagger Phi Phi^dagger) = Sum
sigma^4 >= 0` (200 random 4x4 complex, 1e-9) hold also for rectangular 4x3, with the tooth that
the `Phi^dagger Phi^dagger` word is undefined for rectangular; eq:V is a spectral function,
`Tr(X-v^2)^2 = Sum (sigma^2 - v^2)^2` (1e-9), and U(4)xU(4)-invariant (60 random, 1e-7).
Consequence: the real degree-(2,2) bifundamental invariants are exactly `span{Tr X^2, (Tr X)^2}`
(combinatorial argument D4), so the quartic matter potential canonically allowed to the stated
Presentation-A field content is the two-parameter family, and eq:V is one slice of it (R1).
(b) Dimensions and kernel statements: established (classical invariant theory of matrix
conjugation; here confirmed numerically at the listed points; the general fact is background,
cross-checked in this round against no primary source - flagged accordingly; the degree-(2,2)
bifundamental count is argued self-containedly in D4 and spot-checked by the C5r/C6/C10 teeth).
The consequence "Presentation A canonically admits exactly this two-parameter quartic family" is
conditional on the stated field content (eq:Phi-transform), quartic truncation, and the compact
unitary reading of the internal group.
(c) C5r, C6, C10 (ranges as in (a)).

**R5 - The general quartic family: convexity, vacuum, strata, threshold.**
(a) `V(x) = c3 Sum x_i^2 + c2 (Sum x_i)^2 + c1 Sum x_i + c0` on `x_i = sigma_i^2 >= 0`, 4 sites:
Hessian `= 2 c3 I + 2 c2 J` with eigenvalues `{2 c3 (x3), 2 c3 + 8 c2}`, `det = 16 c3^3 (c3 + 4
c2)` (exact symbolic); strict convexity iff `c3>0 and c3+4c2>0`, the same region as strict
boundedness below (unbounded teeth `c2 < -c3/4`: equipartition-ray values at t = 1,3,9,27,81 drop
below -1e2). Unique stationary point `x = s 1`, `s = -c1/(2(c3+4c2))`, value `V4 = c0 - c1^2/(c3
+ 4c2)` (unique solve). Stratum-k points (k equal nonzero coordinates): `y^2 = -c1/(2(c3+k c2))`,
`V_k = c0 - k c1^2/(4(c3+k c2))`, k = 1,2,3 (unique solves). `V_k` strictly decreases in k since
`d/dk [k/(c3+k c2)] = c3/(c3+k c2)^2 > 0`, so the inf over `{det Phi = 0}` (x1 = 0 face) is the
stratum-3 value `V3` at `(0,w,w,w)`, `w^2 = -c1/(2(c3+3c2))`. Threshold
`Delta := V3 - V4 = (c1^2/4)[1/(c3/4+c2) - 1/(c3/3+c2)]` (exact symbolic) is strictly positive
THROUGHOUT the bounded class: boundedness gives `c3/4+c2 >= 0` and the corridor gap
`c3/3+c2 - (c3/4+c2) = c3/12 > 0` rules out sign reversal of either denominator (corridor
nonexistence, checked). Face-boundary gradient quantity at the vacuum: `2 c2 tau + c1 = c1
c3/(c3+4 c2) = -2 c3 s` (exact). Numerically (N11): at 11 bounded-class points, full 51^4 grid
minima on [0,2.5]^4 (h = 0.05) match `V(s 1)` and all four coordinates (tols `2.5(c3+4|c2|h^2
+ 1e-9)`, `2.5h`); face-restricted (x4 = 0) minima match `V3` and the top-3 coordinates (tol
`3h`); the Delta identity at 1e-9 and Delta > 0 at 11 points; whenever Delta > 8 tol the face
minimum exceeds the vacuum value; `w != s` at (c3,c2,c1) = (1,-0.20,-0.4), (1,-0.245,-1.7),
(2,0.25,-0.4); c0 = 0.13 at the numeric points.
(b) Established derivation (exact symbolic, cross-verified by independent numerical grids).
(c) N12 (symbolic, generic real `c3,c2,c1,c0`); N11 (11 points (c3,c2,c1) = (1,0.5,-1.7),
(1,0.5,-0.4), (1,-0.20,-0.4), (1,-0.245,-0.02), (1,-0.10,-0.4), (0.4,0,-0.4), (0.4,0,-1.7),
(2,0.25,-0.4), (0.7,-0.13,-0.13), (1.3,-0.22,-0.05), (0.4,0,-0.02); unbounded teeth
(1,c2,-0.7), c2 in {-0.26,-0.4,-1.0}).

**R6 - eq:V slice: exact recovery of the appH L1711 threshold.**
(a) Substituting `(c3,c2,c1,c0) = (lambda/4, 0, -lambda v^2/2, lambda v^4)` into R5, symbolically:
`s = v^2`, `V4 = 0`, `Delta = lambda v^4/4`. I.e. `inf{V : det Phi = 0} - min V = lambda v^4/4` -
the appH L1711 defect threshold (live-quoted above) re-derived as the `c2 = 0` slice of the family
theorem; the face minimizer `(0, w, w, w)` with `w^2 = v^2` reproduces the recorded singular
values `(0, v, v, v)`. (b) Established derivation (exact symbolic substitution; three separate
`simplify(...) == 0` targets, generic `lambda, v > 0`). (c) N12 (okD block).

**R7 - Moyal vertex phases from the live star product.**
(a) For the star product of ch03 L375-381 with constant real antisymmetric Theta, plane-wave
vertices carry phases `exp(-(i/2) S)`, `S = Sum_{i<j} k_i wedge k_j`, `k wedge q = Theta^{mu nu}
k_mu q_nu`: (i) `S(k,-k) = 0` exactly (two-point); (ii) S is invariant under cyclic rotation of
legs on the conservation shell `Sum k = 0` - verified exactly for n = 3,4,5 - and the invariance
FAILS off the shell (tooth: k0 shifted by 1 off-shell gives nonzero difference), so cyclicity
uses momentum conservation exactly; (iii) at 4 points under conservation, `S = k1 wedge k2 + k3
wedge k4 = k2 wedge k3 + k4 wedge k1` (both differences symbolically 0), and S is nonzero for
generic data (random integer configurations with `|k3 wedge k4| > 0` found); (iv) small-phase
bounds `1 - cos(S/2) <= S^2/8`, `|sin(S/2)| <= |S|/2`, `[1 - cos(S/4)]/[1 - cos(S/2)] -> 1/4`
(within 5% whenever `1 - cos(S/2) > 1e-10`). (v) Exact exponentiation of the pairing generator E
(E[1,2] = p, E[2,1] = -p, sites 0,3 decoupled): `exp(-theta E)` has entries `cos(theta p)`,
`sin(theta p)` on the (1,2) block and identity on 0,3 (all entries symbolic). (vi) The three
quartic channel factors `cos(theta p/2)`, `cos(theta q/2)`, `cos(theta(p+q)/2)` are pairwise
distinct (symbolic nonzero differences), coincide flatly at `theta = 0` (limit, O(theta) series
and first theta-derivative all zero), and `1 - cos(theta p/2) = theta^2 p^2/8 + O(theta^4)` (exact
series). Consequence (constraint, not selection): the Presentation-A quartic vertex at fixed
Theta is channel-dependent, and any local channel-blind Tr-polynomial vertex (eq:V included)
agrees with it only up to corrections starting at order Theta^2 times momenta^2; no choice of
parameters in the R4 family absorbs the phases.
(b) Established derivation from the stated (live) Moyal product (checks run on a canonical 2D
symplectic block; see D6 for why the block check exhausts the identities: they are polynomial
identities in the components of the antisymmetric form, and every real antisymmetric 2-form
decomposes into canonical 2-blocks). The premise that this star product governs the fluctuation
vertices of eq:Smatrix is dictionary-level input; the package stays inside the recorded scope of
the constant-Theta Moyal check (ch03 L398-401). Conditional as to any selection claim.
(c) C4 (symbolic generic 2D momenta at n in {3,4,5}; 60 random integer-momentum configurations,
theta in (-0.15, 0.15)); N13 (symbolic p, q, theta).

**R8 - Bounded but split: the defect threshold fails beyond quartic.**
(a) `V(s^2) = eps (Sum_i sigma_i^2)^4 - Sum_i sigma_i^4` at eps = 0.3 (a degree-6 bifundamental
invariant; bounded below since `Sum x_i^2 <= (Sum x_i)^2` gives `V >= eps tau^4 - tau^2`) has its
global minimum on `{det Phi = 0}`: `min_t [eps t^4 - t^2] = -1/(4 eps)` at rank-1 (t^2 = 1/(2
eps)), located on a t-grid of 200001 points to 1e-3; strictly below every equipartition point
(`V_rank1 < V_eq` at tau = 4; 60000 random simplex candidates plus explicit near-rank-1 candidates
find nothing above `V_eq - 0.49 (V_eq - V_rank1)`; an explicit near-rank-1 configuration with
`min sigma < 1.5e-3` has `V < V_eq - 1`). Conclusion: the defect-threshold property of R5/R6 is a
property of the quartic class (corridor-gap argument), not of bounded matrix potentials in
general - beyond quartic the defect configuration can be the vacuum (vacuum splitting onto
`det Phi = 0`).
(b) Established counterexample (explicit; verified). (c) C8 (eps = 0.3, tau = 4 simplex, 60000
random points, t in [0.01, 20] at 200001 points).

## Derivations

D1 - Normal form (R1). Expanding each square: `(lambda/4)(x - v^2)^2 = (lambda/4)x^2 -
(lambda v^2/2)x + lambda v^4/4`; summing over the four eigenvalues `x_i = sigma_i^2` of
`X = Phi^dagger Phi` gives `eq:V = (lambda/4) Tr X^2 - (lambda v^2/2) Tr X + 4 (lambda v^4/4)`,
and the live `eq:V` (ch03 L243-244) has exactly this form with constant `lambda v^4` (the trace
of `v^4 I_4`), i.e. the family slice `(c3,c2,c1,c0) = (lambda/4, 0, -lambda v^2/2, lambda v^4)`.
The N-teeth in C1 confirm the constant is `N lambda v^4/4` in general (mismatch tooth at N=7 vs
an N-indexed constant over 4 squares; explicit independent N=6 identity). Inverting the map:
`v^2 = -c2/(2 c4)` with `c4 = lambda/4`, `c2 = -lambda v^2/2` (C1, C9).

D2 - Gradient (R2). With `V = (lambda/4) Tr(X^2) - (lambda v^2/2) Tr X`, `X = Phi^dagger Phi`,
the conjugate-Wirtinger derivative (sum over the three positions of the differentiated factor in
`Tr(XXX)`-type words, cyclicity collecting them) is `dV/dPhi^dagger = (lambda/4)(2 Phi X) -
(lambda v^2/2) Phi = (lambda/2) Phi (X - v^2 I)`. C2 verifies this componentwise against central
differences in both real and imaginary directions (max error < 2e-4 << coefficient scale), on
random complex 4x4 inputs; the display matches the potential term of eq:Phi-eom verbatim
(ch03 L313-314). Vacuum manifold points give `X = v^2 I` hence zero gradient; this is the
corollary, and the explicit `Phi = v I` loop (C2) only instantiates it (disclosed as
definitional).

D3 - SOS and sign classification (R3). Completing the square in `s^2`:
`f(s) + c2^2/(4 c4) = c4 (s^2 + c2/(2 c4))^2 = c4 (s^2 - s*^2)^2`, summing over the 4 sites
gives the tested identity (C3r, symbolic generic nonzero `c4, c2s`). The classification is then
elementary: bounded below iff `c4 > 0`, or `c4 = 0 and c2 >= 0`; within `c4 > 0` the minimum is
at `s = 0` iff `c2 >= 0`, else at `s*`; the `c4 < 0, c2 > 0` region has an interior stationary
point which is a maximum (hilltop - the r1 check's error, see Provenance). Separability of the
N-site sum turns the vacuum set into the product `(argmin f)^N`; with the singular-value
parametrization `Phi -> U diag(sigma) V^dagger` this is the statement that `eq:vacuum-manifold`
(ch03 L249) is exactly the locus `sigma_i equiv v`. Power-mean bounds: `Sum x_i^2 >= (Sum x_i)^2
/4` (Cauchy-Schwarz) and the `p=3` analogue (holder/power-mean); C7 checks both on random
simplex points and equality cases.

D4 - Invariant classification (R4). (i) Conjugation: the linearized gl(n) action on the degree-d
word space has cokernel dimension = number of partitions of d into at most n parts (Cayley-
Hamilton relations enter above degree n); C5r computes the ranks numerically at the eight listed
(n,d) points with three teeth (p(d) mismatches at n=2 d=3,4; dim(4,4)=5 vs dim(2,4)=3 vs
dim(3,4)=4). The general statement is classical background; in this round it was NOT verified
against a primary source (rule 7: no citation given; flagged in R4(b)), and every number used
below is a checked point value. (ii) Bifundamental quartic: a degree-(2,2) polynomial in
`(Phi, Phi^dagger)` that is invariant under independent left and right unitaries must contract
each `Phi` with a `Phi^dagger`; with two fields of each kind the complete contraction patterns
are exactly the two: the crossed single-trace contraction `Tr(Phi^dagger Phi Phi^dagger Phi) =
Tr X^2` (C6 identity, = `Sum sigma^4 >= 0`) and the double-trace `(Tr X)^2` (pairing argument;
self-contained). The tempting additional word `Tr(Phi^2 (Phi^dagger)^2)` fails U(4)xU(4)
invariance numerically (C10/C5r teeth, |delta| > 1e-6 vs < 1e-7). So the real quartic bifundamental
space is `span{Tr X^2, (Tr X)^2}` and, adding the (invariant) linear and constant terms `Tr X`,
`1`, the general quartic matter potential for the stated field content is the two-parameter
family. `eq:V` lives in it (R1); the extra freedom is the ratio `c2/c3`, which `eq:V` sets to 0.

D5 - Family geometry (R5, R6). On `x_i >= 0` (open cone) with `V = c3 Sum x_i^2 + c2 (Sum x_i)^2
+ c1 Sum x_i + c0`: Hessian entries `d^2V/dx_i dx_j = 2 c3 delta_ij + 2 c2`, so `H = 2 c3 I +
2 c2 J`; the all-ones matrix `J` has eigenvalues `0` (multiplicity 3) and `4`
(`J 1 = 4 1`), so the all-ones direction of `H` carries `2 c3 + 2 c2 * 4`
, giving `eig(H) = {2 c3 (x3), 2 c3 + 8 c2}` and `det H = (2c3)^3
(2c3 + 8c2) = 16 c3^3 (c3 + 4 c2)` (all exact; N12 asserts, with the hand value matching 16 -
the "8" in the N12 COVERAGE print is a prose typo, see Provenance). Strict convexity on the
cone is then equivalent to `c3 > 0 and c3 + 4 c2 > 0`. Boundedness below on the cone: by
Cauchy-Schwarz `Sum x_i^2 >= (Sum x_i)^2/4`, so if `c3 > 0` and `c3/4 + c2 >= 0` the quartic
part is `>= (c3/4 + c2)(Sum x_i)^2 >= 0` and coercive when strict; along the equipartition ray
`x = t 1` the quartic part is `4(c3 + 4c2) t^2` (strict-class teeth tested in N11: `c2 <
-c3/4` drives values below `-1e2` along the ray). For the interior stationary point: `dV/dx_i =
2 c3 x_i + 2 c2 tau + c1` (`tau = Sum x_i`) forces all coordinates equal, `x = s 1`,
`(2 c3 + 8 c2) s + c1 = 0`, `s = -c1/(2(c3+4c2))`; `V(s 1) = 4(c3+4c2)s^2 + 4 c1 s + c0 = c0 -
c1^2/(c3+4c2)`. In the strict class with `c1 < 0` (the branch containing the eq:V slice, `c1 =
-lambda v^2/2 < 0`, and all 11 N11 numeric points), `s > 0` and convexity makes this the unique
global min. Stratum k (coordinates `y x k` and `4-k` zeros): the stationary equation on that
face is `2(c3 + k c2) y + c1 = 0`, `y^2 = -c1/(2(c3 + k c2))` (positive for `c1 < 0`, since
`c3 + k c2` is linear in k between `c3 > 0` and `c3 + 4 c2 > 0`, hence positive for k in [0,4]),
`V_k = k(c3 + k c2) y^2 + c1 k y + c0 = c0 - k c1^2/(4 (c3 + k c2))` (k = 1,2,3, and the k = 4
formula reproduces the vacuum value). `d/dk [k/(c3 + k c2)] = c3/(c3 + k c2)^2 > 0`, so `V_k`
strictly decreases in k: the minimum over the face `{x_1 = 0}` (convex; its minima on lower
strata are larger) is `V_3` at `(0, w, w, w)`, `w^2 = -c1/(2(c3+3c2))`, so `inf{V : det Phi = 0}
= V_3`. Then `Delta = V_3 - V_4 = (c1^2/4)[1/(c3/4 + c2) - 1/(c3/3 + c2)]` (exact symbolic;
using `c3 + k c2 = k(c3/k + c2)`), and in the strict class `c3/4 + c2 = (c3 + 4c2)/4 > 0` while
`c3/3 + c2 = (c3/4 + c2) + c3/12 > 0` (corridor gap `c3/12` - no sign flip is possible, checked
symbolically as "no `c2` with `c3/4 + c2 >= 0` and `c3/3 + c2 <= 0`"), so `Delta = (c1^2/4)
(c3/12) / [(c3/4+c2)(c3/3+c2)] > 0` throughout the strict class (c1 != 0). Eq:V slice:
substituting `(lambda/4, 0, -lambda v^2/2, lambda v^4)` gives `s = v^2`, `V_4 = 0`, `Delta =
lambda v^4/4` and `w^2 = v^2` (three exact N12 targets) - the appH L1711 threshold and its
`(0,v,v,v)` attainment point, re-derived. Face-boundary identity checked in N12: `2 c2 (4s) +
c1 = c1 c3/(c3 + 4 c2) = -2 c3 s` (exact).

D6 - Moyal phases (R7). The live star product (ch03 L375-381) is the bivector (Moyal) product;
integrating `n` plane waves `exp(i k_i x)` against it (Wick contraction of the bivector between
each ordered pair i < j) yields the vertex factor `exp(-(i/2) Sum_{i<j} k_i wedge k_j)`, `k wedge
q = Theta^{mu nu} k_mu q_nu` (C4 checks this construction's consequences rather than re-deriving
the contraction: cyclicity, reduction, bounds). Cyclicity: rotating `(k1,...,kn) -> (kn,k1,...)`
changes `S` by `k_n wedge (k1 + ... + k_{n-1}) = -k_n wedge (Sum_i k_i)`, zero exactly on the
conservation shell (symbolic in C4 for n = 3,4,5; off-shell tooth confirmed nonzero). 4-pt
reduction: with `k4 = -k1-k2-k3`, `k1 wedge (k3 + k4) = -k1 wedge (k1 + k2) = -k1 wedge k2` and
`k2 wedge (k3 + k4) = -k2 wedge (k1 + k2) = k1 wedge k2`, so the six-term sum collapses to `k1
wedge k2 + k3 wedge k4`; the second equality `= k2 wedge k3 + k4 wedge k1` is the same identity
after one rotation (both differences symbolically 0 in C4). Reality of the quartic vertex makes
channels enter as real parts, i.e. cosines of the half-phases; with the pairing scalars p, q of
the two independent momentum channels (and `p + q` the third), N13 verifies symbolically that
`cos(theta p/2)`, `cos(theta q/2)`, `cos(theta(p+q)/2)` are pairwise distinct (nonzero symbolic
differences), flatly degenerate at `theta = 0` (limit 1, vanishing O(theta) series and first
derivative), and `1 - cos(theta p/2) = theta^2 p^2/8 + O(theta^4)` (exact series, even orders
only). Since a Tr-polynomial local vertex carries channel-independent coefficients, matching the
phase functions in all three channels requires `theta p ~ 0` for all channels - the O(theta^2)
truncation reading of R7. Block reduction: `S` is linear in `Theta^{mu nu}` and any real
antisymmetric 2-form is orthogonally congruent to a direct sum of canonical 2-blocks `theta_j J`
plus a kernel; the vertex factor exponentiates blockwise (`S` is the sum of the block
contributions), so every listed identity, being checked for a single canonical block with free
scalar strength (theta), holds for all constant real `Theta`. (The ch03 display fixes this
`Theta` as c-number; operator-valued or nonconstant `Theta` is outside the live Moyal-check
scope, ch03 L398-401.)

D7 - Beyond-quartic split (R8). `V = eps (Sum x_i)^4 - Sum x_i^2` at eps = 0.3: bounded below
since `Sum x_i^2 <= (Sum x_i)^2` gives `V >= eps tau^4 - tau^2` with `min_tau (eps tau^4 - tau^2)
= -1/(4 eps)` at `tau^2 = 1/(2 eps)`, attained on the simplex by concentrating all mass in one
coordinate (`x = (1/(2eps), 0, 0, 0)`, rank-1, `det Phi = 0`). Equipartition gives
`V = eps tau^4 - tau^2/4`, at C8's tau = 4 the value 72.8, strictly above `-1/(4 eps)`. C8
verifies: the t-grid minimum matches `-1/(4eps)` to 1e-3, the 60000-point simplex scan plus
explicit near-rank-1 candidates never rise above `V_eq - 0.49(V_eq - V_rank1)`, and an explicit
near-rank-1 configuration strictly beats equipartition. Both terms are U(4)xU(4) invariants of
the stated field content (degree 6 and 2), so this is inside the Presentation-A invariant class
but outside the quartic class: the threshold statement of R5/R6 does not extend beyond quartic
order.

## What is derived vs what remains assumed

Derived in this package: the identities, classifications, family theorems and counterexample of
R1-R8 at their tiers (established-identity/derivation tier for the algebra and geometry; the
counterexample established as counterexample). Remains assumed, and used as inputs:
(1) `ass:dictionary` as a matching condition, not a theorem (ch03 L358-361; "the most important
unproved bridge", L365-366) - every statement relating `eq:Smatrix` to `eq:Smicro`/`eq:V` here is
a statement under that assumption; (2) the eq:Phi-transform field content ("It is a choice of
field content. It is not derived from Presentation~A alone", ch03 L287-288) - the R4 family
enumeration is relative to that content; (3) quartic (degree-(2,2)) truncation - R8 shows the
threshold geometry is NOT stable outside it; (4) constant c-number `Theta` and the recorded
Moyal-check scope (ch03 L398-401) for R7; (5) internal dimension 4 where the eq:V slice is
evaluated. What is NOT derived: any selection of the slice `c2 = 0` or of `(lambda, v)` from
`eq:Smatrix` data; the dictionary itself; the vacuum manifold as a dynamical attractor. Rule 3:
nothing in this package closes D, D1 or A, and nothing in appH items 114-117 changes status - the
L1711 result is re-derived (as a slice), not superseded, and the L1715 gating sentence stands:
the selection remains the upstream input. What this package adds to the ledger question: the
selection question is now sharply the slice question (`c2/c3` and the truncation), the recorded
threshold facts are family theorems stable on the whole bounded quartic class, the truncation
character of `eq:V` is quantitatively pinned (O(Theta^2)), and the quartic-class boundary is
witnessed (R8).

## Provenance

- **Chain deaths.** Two earlier researcher agents on this package died to API context-limit
  errors before writing `proposal-r1.md`. Stage A (finisher agent, 2026-11-23) completed the
  verify pack to `TOTAL 13/13 PASS` and left `scratch/118/notes.md`; stage B (this document) did
  the source reads and the proposal. No manuscript text, generator, certificate or manifest was
  produced (stage C scope by dispatch).
- **Check-bug adjudications** (all CHECK-code bugs; no claim was weakened; details in
  `scratch/118/notes.md`):
  - **C3 -> C3r (R2-3).** r1 tested `mexican-hat iff (interior stationary point exists and > 0)`,
    which is also true for the hilltop region `(c4 < 0, c2 > 0)`; C3 FAILed legitimately. C3r
    states the honest full nine-region classification (bounded below iff `c4 > 0` or `c4 = 0,
    c2 >= 0`; Mexican hat iff `c4 > 0, c2 < 0`; hilltop tooth located as a maximum).
  - **C5 -> C5r (R2-1, R2-2).** NameError (`(i,j)` keys leaking loop names; renamed `ii,jj`) and
    wrong expected dimensions: `p(d)` was used, but the GL(n)-conjugation invariant dimension in
    degree d is partitions of d into AT MOST n parts (Cayley-Hamilton); expectations corrected,
    teeth added (n=2 d=3,4 mismatch; dim(4,4)=5, dim(3,4)=4).
  - **N11 r2b fix.** `grid_min` stacked the four coordinate arrays on axis 0 while the evaluator
    reduced on axis -1, so the grid evaluated a different (factor-51 summed) function; fixed to
    `np.stack(..., axis=-1)`. The analytic predictions (s, w, Delta formulas) were independently
    hand-derived and are unchanged; tolerances, points and teeth unchanged.
- **Pins.** Superseded round-1 provenance kept for the record: `verify_r118.py` sha1
  `c2a6bcf98a5e9a55398976879747495af7503c94` (16868 B), `out-r118.txt` sha1
  `0d95d699c0fb890408fef1de54bb3d432c8037fe` (823 B; records C3 FAIL, C5 NameError). Active
  verification pack: `verify_r118_r2.py` sha1 `9fb20e50fc198ae8912377bdb4a8893363087a9a`
  (25294 B), pinned output `out-r118r2.txt` sha1 `0ba8a0d7ec87325aeeaedac5a2d024dd5c0cfb3b`
  (3132 B; all pins recomputed by sha1sum this round on the on-disk files).
- **Stage-B re-run (reproduction pack executed).** `python -I -B verify_r118_r2.py` (background,
  redirected to `scratch/118/rerun-stageb.txt`): exit 0, all 13 PASS lines, `TOTAL 13/13 PASS`,
  `ALL CHECKS DONE 118`; output sha1 `4627add7038ac3be739069ffb24fa31891d35775`, 2841 B.
  **Disclosed discrepancy:** the re-run bytes differ from the pinned `out-r118r2.txt` ONLY in
  line 17 (the N11 COVERAGE line): the pinned file carries an extra trailing sentence ("r2b fix:
  grid_min stacked ... unchanged.", 291 B = exactly 3132 - 2841; CR-stripped diff shows that one
  line) that the on-disk script does not print. Every PASS line, every COVERAGE substance and the
  TOTAL reproduce. The stage-A notes pin the two files mutually at these hashes, so the pair is
  internally inconsistent in that one prose line. Stage C must re-pin the output (or restore the
  sentence in the script); this stage deliberately did not touch either file.
- **Parameter coverage (consolidated from the COVERAGE lines of the r2 run).** C1,C2,C4,C6,C7,
  C8,C9,C10: check code identical to round 1 (C6-C10 first fully executed in r2 - round 1
  crashed at C5); ranges as listed per-check in R1-R8 above; no default-value-only checks. C3r,
  C5r, N11, N12, N13: as listed in R3-R7 and in the r2 COVERAGE lines.
- **New disclosures from this round's code read.** (a) The byte discrepancy above. (b) N12
  COVERAGE prose prints "det 8c3^3(c3+4c2s)" while the check code asserts `det == 16*c3**3*(c3 +
  4*c2s)` (verify_r118_r2.py L435) and the hand-computed determinant is `(2c3)^3 (2c3+8c2) = 16
  c3^3 (c3+4c2)` - a typo in the summary print (L521), not in the check. (c) Inert conjuncts:
  C7's region-scan chain contains the trivially-true conjunct `(-(6.0)**2 < 0)` (L303) and C3r's
  hilltop branch contains `(not mex)` (L111, identically true when `a < 0`); both are inert
  guards, and no claim in this proposal rests on them - the load-bearing tests adjacent to them
  (region scan values; hilltop argmax location, L110-112) carry the content. (d) C2's explicit
  vacuum sub-loop is a definitional substitution (disclosed in R2).

## Decisions Taken

1. **Deliverable boundary held strictly.** No payload/generator/certificate/manifest, per
   dispatch; the manuscript-bound paragraph is deferred to stage C as a stage-C product. Rejected
   alternative: drafting payload text here (would preempt stage C's anchor re-verification).
2. **Write-split recovery.** After a single Write of the full proposal failed at ~13 KB with a
   tool JSON parse error (consistent with the run's documented tool-echo/size deaths), the file
   was assembled from part writes and byte-appends; content is identical in substance.
3. **R4 background tiering.** The general conjugation-invariant dimension theorem is tiered
   "classical background, point-values verified numerically, not cross-checked against primary
   literature this round" instead of attaching an unverified Procesi-style citation (rule 7).
   The degree-(2,2) bifundamental count, which the family claim actually leans on, is given a
   self-contained pairing argument (D4) plus teeth.
4. **Byte discrepancy disclosed, not smoothed.** Kept the pinned output untouched and disclosed
   the one-line divergence with the exact byte arithmetic and the mechanism; stage C re-pins.
   Rejected: silently re-pinning here (would desync the stage-A notes' mutual pin pair and hide
   the discrepancy from the gatekeeper).
5. **Result framing.** Headline is "constrained, not closed": the package does not derive the
   selection, and R7 is presented as a constraint on what any selection could produce, never as
   a selection mechanism - to keep the L1715 gating sentence intact and the tiers honest.
6. **No RESEARCHER-DECISION deferred to the author** (none arose beyond the above; none needed).

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step is derived to completion, no missing link
is closed without new unsupported inputs (the selection remains open; the dictionary remains the
gating assumption). Value is sub-lemma/constraint grade: family-wide strengthening of the
recorded item-114 threshold geometry, a sharp restatement of the selection target (slice +
truncation), a pinned O(Theta^2) truncation constraint, and a class-boundary counterexample.

## Status-label recommendation

Re-derived from the live ch17 completion list (L703-735): the current full-GR / matrix-derived
criterion names A, B, C, D1, E, F, G-derived and N; A at L704-706 ("OPEN; CRITICAL PATH for the
matrix-derived label"), D1 at L715-720. Problem D: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL
(appH L768-772; ch17 L740 "Problem~D stays OPEN and CRITICAL PATH"). **All labels unchanged by
this package** (expected: none changed; rule 2 respected - no label edit is proposed in any
LaTeX, because this package proposes no LaTeX).

## Author decision needed

None. (No scope, label, or core-assumption change is proposed; spacetime remains emergent
throughout - all objects are internal matrices or matrix coordinates, and no fundamental metric
appears anywhere in the package.)

## Remaining open step

To close the ORIGINAL target (select `eq:V` and `(lambda, v)` from `eq:Smatrix` under
`ass:dictionary`) what is still missing is: (i) a derivation that fixes the double-trace ratio
`c2/c3` (the family direction eq:V sets to zero) - no within-package route exists yet; candidate
attack surfaces, none yet executed, are a one-loop effective-potential computation on the matrix
side, saddle-point/large-N selection, or a dictionary-level theorem upgrading the matching
condition; (ii) any quantitative selection of `v` needs the same inputs plus the scale
identification; (iii) R7 shows any such derivation must reproduce channel-independent quartic
couplings in a limit, so it lives at `Theta -> 0` or in a mechanism that cancels the phases - if
nonconstant or operator `Theta` is ever needed, the Moyal-remark scope (ch03 L398-401) must first
be extended. **Stage C ships:** the appH-bound paragraph (wording of R5/R6/R7/R8 consequences
with tiers, anchored to the L1713/L1715 passages), its generator, two-pass compile certificate,
manifest with POST pins against baseline appH sha1 `ce91063fddcaa5599429519f4bc2c478e0d919e8`
(839337 B), and a re-pinned verify output (see Provenance discrepancy).

## Special instructions for the gatekeeper

- **Reproduction pack.** From `proposals/118-presentation-a-potential-selection/`:
  `python -I -B verify_r118_r2.py > out.txt 2>&1` (repo default python under `python -I -B`;
  runtime a few minutes). Expected invariants: 13 `PASS` lines (C1, C2, C3r, C4, C5r, C6, C7,
  C8, C9, C10, N11, N12, N13), `TOTAL 13/13 PASS`, `ALL CHECKS DONE 118`, exit 0. Byte-comparison
  to `out-r118r2.txt` fails ONLY at line 17 (N11 COVERAGE trailing sentence; mechanism and
  arithmetic in Provenance) - please confirm via a CR-stripped line diff that this is the ONLY
  divergence, and judge whether to require a re-pin or a script edit in stage C.
- **Independent re-derivations worth doing (the three highest-leverage):** (1) D5's strata/
  threshold chain: `V_k = c0 - k c1^2/(4(c3 + k c2))`, monotonicity via `d/dk[k/(c3+kc2)]`, and
  `Delta = (c1^2/4)(c3/12)/[(c3/4+c2)(c3/3+c2)] > 0` on `c3 > 0, c3+4c2 > 0` (test the c1-sign
  proviso: the interpretation as vacuum/inf needs `c1 < 0`; the algebraic identities are
  generic); (2) C5r's dimension formula against your own linear algebra at n=2 (e.g. Cayley-
  Hamilton giving `dim(2,3) = 2`); (3) C4's phase cyclicity and 4-pt reduction by hand from
  `S = Sum_{i<j} k_i wedge k_j` on the conservation shell.
- **Re-grep every quotation** in "Mission connection" at its quoted line (appH 765/769/795-808/
  1711/1713/1715; ch03 243-244, 249, 287-288, 313-314, 358-361, 365-366, 375-381, 398-401; ch04
  171-174; ch17 361, 377-378, 704-706, 715-720, 737-745) - they were taken live this round but
  the tree moves between integrations.
- **Scope limits to enforce.** Must NOT be asserted: that eq:V or any slice of the family is
  derived from `eq:Smatrix`; that the Moyal vertex computes fluctuation vertices beyond the
  recorded constant-Theta check scope (ch03 L398-401); that R6 supersedes rather than re-derives
  appH L1711; any closure/label change (D, D1, A all stay exactly as recorded). R4's general
  dimension theorem is background tier - challenge it if you can verify a primary source either
  way. The inert conjuncts (C7 L303, C3r L111) and C2's definitional subloop must not be counted
  as verification, and the N12 "det 8" print must not be treated as a code error (code is 16).

## Tier summary

| Result | Statement core | Tier |
|---|---|---|
| R1 | normal form + parameter map of eq:V | established identity (symbolic) |
| R2 | gradient = eq:Phi-eom potential term; vacuum stationarity | established derivation; vacuum loop definitional (disclosed) |
| R3 | SOS identity, full sign classification, separability, power means | established elementary derivation |
| R4 | quartic bifundamental invariants = span{Tr X^2, (Tr X)^2}; family | established at checked points + self-contained pairing argument; general theorem background (not literature-verified); family-as-Presentation-A-content conditional on eq:Phi-transform + truncation |
| R5 | family convexity/vacuum/strata/Delta > 0 | established derivation (symbolic + grid cross-check) |
| R6 | eq:V slice re-derives Delta = lambda v^4/4, s = v^2, V_vac = 0 | established derivation (slice of R5) |
| R7 | channel-distinct phases; eq:V = Theta^2-accurate truncation | established from live star product; selection-bearing content conditional on dictionary scope (L398-401) |
| R8 | beyond-quartic bounded split counterexample | established counterexample |

## Pins addendum (stage C)

Appended 2026-11-23 (stage C); the proposal text above is otherwise untouched.

- `verify_r118_r2.py` re-pinned: sha1 `5950fbff30b64fb66ed3813c3fbb39bd6180b632`, 25297 B.
  Single-string COVERAGE fix only (N12 prose line: "det 8c3^3(c3+4c2s)" -> "det 16 c3^3 (c3+4c2s)",
  matching the asserted value `16*c3**3*(c3 + 4*c2s)` at line 435); no check logic touched.
  Supersedes `9fb20e50fc198ae8912377bdb4a8893363087a9a` (25294 B).
- `out-r118r2.txt` re-pinned: sha1 `756bd4a8c4f757902dc2a031ef0925a7633964a5`, 2844 B. Raw capture
  of two consecutive `python -I -B verify_r118_r2.py` runs, byte-identical, exit 0 both, ending
  `TOTAL 13/13 PASS` / `ALL CHECKS DONE 118`. Supersedes the hand-edited
  `0ba8a0d7ec87325aeeaedac5a2d024dd5c0cfb3b` (3132 B; carried an extra trailing N11 sentence the
  script never printed) and the stage-B re-run capture `4627add7038ac3be739069ffb24fa31891d35775`
  (2841 B; pre-typo-fix).
- Payload `insert-potential-selection-r1.tex`: sha1 `bbe4e535dd31c76a82ea89ff1b20980eb979f9bf`, 4024 B;
  generator `gen_payload_118.py` sha1 `bba66dd1aeae1d2aa43c08e5d0560ce3038f8f78` (9426 B), regeneration
  asserted byte-identical; certificate `cert-r118p.py` sha1 `b711792287c81887574084b770900bc037533c41` (4938 B).
- Baseline (re-counted at stage C start): HEAD `8b9ff39`; appH sha1 `ce91063fddcaa5599429519f4bc2c478e0d919e8`,
  839337 B. Anchor `\section{Problem E: signature}`: count 1, byte offset 286080. POST (canonical splice,
  payload + CRLF join): sha1 `c24902b31abafc126a7e59485f2b706d2f2b17d4`, 843363 B = 839337 + 4024 + 2.
- `manifest.md` in this folder carries the full pin table, ref-label counts, coverage consolidation,
  payload tier table and stage provenance.
