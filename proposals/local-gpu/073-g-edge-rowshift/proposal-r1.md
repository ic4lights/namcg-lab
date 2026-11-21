# Proposal 073-g-edge-rowshift, round 1

Round 2 (wording-only revision per review-r1.md): blocking finding 1 applied to insert-r1.tex
(the error quantity is attached to \(\Delta\), not to \(\Delta/N\)); findings 2/3/5 recorded
below; s1-s5 math unchanged, scripts not re-run; byte contract and manifest re-frozen.

## Result

Within the 072 dominant-representation hypothesis class (H1)-(H4), inherited verbatim, the
fixed-frame hook-content excess Delta of the product fuzzy-sphere testbed is mapped under
perturbations of the row lengths of the saddle diagram. Writing M_f = m_f N and the perturbation
box B_C(ell) = {(ell1',ell2') valid two-row partitions : |ell_i' - ell_i| <= C} (l-infinity norm):

1. **Uniform continuum limit.** Delta(Nu1, Nu2)/N -> Lambda(u1,u2) := sum_{f=1,2}
   [G(m1+m2, u_f) - G(m_f, u_f)], G(m,u) = (m+u)log(m+u) - m log m - u, with the explicit residual
   |Delta - N*Lambda| <= 2K1' + 2K2' + log(ell1+1) + 2, K1' = log(M/(M1-1)),
   K2' = log((M-1)/(M2-1)), verified on all 75 random sampled diagrams up to N = 3200
   (worst residual-minus-bound -6.163; `s5` section 1). Lambda is positive and strictly
   increasing in each argument for every nonzero pair of fractions (elementary).
2. **Theta(N) survival for sublinear perturbations.** min_{B_C} Delta / N -> Lambda(u1,u2) for
   fixed C and for C = round(sqrt(N)) (0.506367 at N = 3200, Lambda = 0.523248); hence
   min_{B_C} Delta = Theta(N) for every C = o(N). The deficit N*Lambda - min is linear in C at
   leading order with slope sum_f log((m1+m2+u_f)/(m_f+u_f)) = 2 log(3/2) = 0.810930 at the
   symmetric saddle; asserted < 5% at C = 10, N = 3200 (measured 0.07% from printed values; 0.0386% at machine
   precision per review-r1 finding 5; both well inside 5%);
   table N(Lambda - min/N) = 8.31 / 15.61 / 89.57 at C = 1 / 10 / 100, N = 3200, against
   0.81 / 8.11 / 81.09 first-order (`s5` section 2-3). The far-corner argmin is exact-enumeration
   confirmed at N = 400, c in {0.1, 0.3, 0.45}, and printed as the corner at C = 100, N = 3200
   (rows (1500,1500)) and at t = 0.5 ((700,700)).
3. **Exact sign/combinatorics of single-box moves (`s4` sections 1-3).** Row-1 and ridge
   (both-rows) increments of the dim-ratio are strictly positive (4080 exact rational checks +
   assert; one-line positivity proof below); the row-2 increment is negative exactly when
   (ell1 - ell2)(M1 - 1) < M2 + ell2 (1,023,120 exact integer comparisons, 0 failures); negative
   increments are confined to the near-diagonal gap band d < d* = (M2+ell2)/(M1-1) and are
   bounded below by -log 2: min over d >= d* is +4.939491e-04, most negative anywhere -0.676053
   at (M1,M2,ell1,ell2) = (2,29,30,29), vs -log 2 = -0.69315.
4. **N-independent Lipschitz bound (`s4` section 4).** |Delta' - Delta| <= C(K1+K2+1) +
   log(2C+1), K1 = log(1+M2/M1), K2 = log(1+(M1-1)/M2), brute-forced over all perturbations
   inside the C-box (C <= 5) of 300 random base diagrams per (M1,M2) on a rank grid, rows up to
   (M1+M2)/2 + 4: 315,084 pairs, worst slack +1.816865.
5. **Linear breakdown (`s5` section 4).** For C = cN the box minimum is bounded above by the
   far corner N*Lambda(0.5-c, 0.5-c) at the symmetric saddle (t=1): corner/N 0.434531 /
   0.240145 / 0.064185 vs Lambda 0.438624 / 0.243769 / 0.066933 at c = 0.1 / 0.3 / 0.45,
   N = 1600; and (0,0) belongs to B_C if and only if C >= ell1 (exact combinatorics), so at
   c = 1/2 the box contains the trivial diagram: exact box minima 0.0e+00 at (0,0) at
   N = 400 and 1600 (assert < 1e-12). Killing only one row leaves a strictly positive limit:
   Delta(ell1, 0)/N = 0.188909 vs Lambda(u1, 0) = 0.188937 at N = 1600, m = (1/2, 1/3).
   Worst single-row removal of a budget B = 40 (asymmetric fractions): loss(row2) = 18.9499 >
   loss(half-half) = 15.4800 > loss(row1) = 13.4840, against first-order predictions 19.3326 /
   11.5073 for the single rows (`s5` section 5).
6. **Rank ratio off the saddle (`s5` section 6).** rho = (sum M/(M+c-r))/|mu| stays in
   (0.73, 0.93) over row fractions 0.05-0.8 at N = 3200 (saddle 0.8111, u=(0.2,0.05) 0.9246,
   u=(0.8,0.8) 0.7349); rho -> 1 as u -> 0 (uniformly, since (c-r)/M -> 0), so Theta(|mu|) rank
   dependence is fraction-uniform but the constant 0.8111 is saddle-specific.

This is a class-restricted sharpening of the 072 selection-independence statement: it extends the
Theta(N) excess from the exact saddle to every diagram within o(N) of it and maps the breakdown at
linear perturbations. It closes nothing. Problem G stays OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL, untouched.

## Target and status

- Target: frontier edge `G.edge-rowshift`, avenue (1) of the 072 gatekeeper review ("lift the
  saddle restriction to bounded row perturbations ... O(1)-per-unit increments suggest
  Theta(N)-robustness under O(1) row shifts - cheapest extension").
- Problem G ledger, appH L3026-3029, re-read live this round, verbatim: "Status: OPEN. Priority:
  CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and
  G-external support at most a scope-limited model; G remains OPEN and neither satisfies the
  matrix-derived criterion." Unchanged by this package; no label, priority or completion
  classification is touched anywhere.
- Character of the result: DERIVED is NOT claimed. Everything is conditional within the 072
  hypothesis class (H1)-(H4) and concerns the testbed defect Delta; the identification of Delta
  with the fixed-frame excess of the leading-order entropy is inherited from 065/072 unchanged.
  Nothing in this package changes the status of the missing steps (i)-(iv) of Problem G or of any
  Chapter 17 criterion.

## Source reading

digest + targeted reads. `scratch/digest.md` in full (compact; `python scripts/make_digest.py
--check` printed `DIGEST CURRENT`; head eb8fc7d; dirty-chapters: yes - the dirty flag is the
integrated, author-uncommitted 072 text, as expected and stated by the orchestrator). Targeted
appH reads with offset/limit only (file never read whole): L3003-3008 (fibre-point Vacuum term -
the reason the short anchor is ambiguous), L3024-3029 (Problem G ledger), L3128-3165 (the full
065 block including the integrated 072 paragraph L3153-3159, its scoped closer L3159, the block
closer L3163, and the Vacuum-term paragraph L3161). Full reads: `proposals/072-g-edge-resum-dominant-rep/review-r1.md`;
`proposals/072-g-edge-resum-dominant-rep/proposal-r1.md` L118-162 (H1-H4, saddle setup, byte
contract); all five 073 scripts and their `.out` files in full; `proposals/072-g-edge-resum-dominant-rep/simulate_apply.py`
and `insert-r1.tex` (byte-contract template; confirmed 072's shipped insert is LF and mine is
CRLF by directive, with simulate adapted). Greps: new paragraph header unique; long-form anchor
count 1. Unreadable files: none. Digest was read in full; no file was skipped that this package
relies on.

## Research and reasoning

### Hypothesis class and the row-perturbation extension (precise)

(H1)-(H4) are those of 072 proposal-r1 L134-142: (H1) 067 product testbed X^I on S^2_N x S^2_N
with block rank M = M1 + M2, M_f = m_f N fixed fractions, k_f = 1 in all runs here; (H2) leading
semiclassical order with one dominant representation (065 class), diagram selected by the
transplanted Frenkel moment rule; (H3) saddle rows ell_i = round(t s_i), s_f = sqrt(k_f M_f(N-M_f)),
t fixed as N -> infinity; (H4) two-row partitions ell1 >= ell2 >= 0. The defect is the 072 Lemma-2
closed form (exact):

    Delta(M1,M2; ell1,ell2) = sum_{c<=ell1} log((M-1+c)/(M1-1+c))
                            + sum_{c<=ell2} log((M-2+c)/(M2-1+c)) - log((ell1+1)/(ell1-ell2+1)).

**Row-perturbation extension (this package):** the box B_C(ell) of all valid two-row diagrams
with |ell_i' - ell_i| <= C (l-infinity norm on row lengths), with three uniformity regimes in N:
(i) fixed C (independent of N), (ii) C = C_N = o(N) (checked at C = round(sqrt(N))),
(iii) C = cN linear (breakdown regime). "Uniform" means: the convergence/error statements hold
simultaneously for all diagrams of the class at given M1, M2 (with the residual bound depending
only on the rank fractions and log(ell1+1)), not along a single diagram sequence.

### s1-s3: regression against the 072 anchors (with review-r1 findings 2-3 fixed)

s1-s3 are copies of the 072 scripts with docstring/comment fixes only (s2 section (5) label now
states the direction the code counts, "576 of 576 with T1<T2"; s3 stale seed-72001 comment and
the wrong "ratio -> 1" docstring expectation removed). All reproduce 072 byte-identically:
s1 max addrel 2.111e-16, max kroneck/site/spec 1.421e-14, rank dev 0 (12 cases, N = 6, 9, 12);
s2 1155 exact-rational checks 0 failures, grid min Delta 4.054651e-01 at (2,2,1,1) = log(3/2),
min ell2-increment -6.657482e-01 at (2,24,13,12); s3 Delta/N = 0.520906, naive-form ratio
0.751508, corner xN = 2.4396, rank ratio 0.8111 at N = 3200. These confirm the 072 Lemma-1 edge
spectrum, the closed form and the saddle scaling as the base this package extends.

### s4: exact increments and the sign criterion (established algebra + finite verification)

From the closed form, single-box increments of the dim-ratio D = dim_{M1+M2}(ell1,ell2) /
(dim_{M1}(ell1) dim_{M2}(ell2)) telescope in one line:

    row-1 move:   D'/D = (M+ell1)(d+2)(ell1+1) / ((M1+ell1)(d+1)(ell1+2)),   d = ell1 - ell2,
    row-2 move:   D'/D = (M+ell2-1) d / ((M2+ell2)(d+1))                     (needs d >= 1),
    ridge move:   D'/D = row-1 ratio x (M+ell2-1)(d+1) / ((M2+ell2)(d+2)).

s4 section (2) verifies these against exact `Fraction` hook-content dimensions: 4080 checks, 0
failures, plus asserts that the row-1 and ridge ratios exceed 1 at every grid point.
Row-1 positivity holds for all valid arguments: the numerator of (row-1 ratio) - 1 is at least
(M1+ell1)(d+2)(ell1+1) - (M1+ell1)(d+1)(ell1+2) + M2(d+2)(ell1+1) = (M1+ell1)(ell1-d) +
M2(d+2)(ell1+1) > 0, since ell1 - d = ell2 >= 0 and M2 >= 1. (Ridge positivity then follows only
partially - the extra factor can be < 1; the general ridge claim is therefore finite-verified
(assert over the 4080-point grid), not proved here.)

Sign criterion: the row-2 ratio is < 1 iff (M+ell2-1)d < (M2+ell2)(d+1) iff (M-M2-1)d < M2+ell2
iff (M1-1)d < M2+ell2 (exact integer cross-multiplication; the two integer inequalities are
identical after expansion). s4 section (3) verifies the equivalence at all 1,023,120 grid points
(M1,M2 = 2..29, ell2 = 1..29, ell1 = ell2+1..60), 0 failures. Consequences (exact implications,
asserted at the grid extremes): negative row-2 increments require gap d < (M2+ell2)/(M1-1)
(the near-diagonal band, which for m1 < m2 is of width O(N/M1) = O(1) per unit - for m fractions
of order 1 the band is O(1) wide, and 072's counterexample (2,24,13,12) sits in it); for
d >= d* = 1 + (M2+ell2)/(M1-1) the increment is > 0 (grid minimum +4.939491e-04 at (2,29,60,15),
the saturation point d = d* there); and since (M+ell2-1)/(M2+ell2) >= 1 (M1 >= 1) and
d/(d+1) >= 1/2 for d >= 1, every row-2 ratio is >= 1/2, i.e. every single-box decrease is >=
-log 2 = -0.693147 (observed extreme -0.676053 at (2,29,30,29), d = 1, ratio 59/116). This is
the exact mechanism behind the 072 honest negative (Delta NOT monotone in ell2): single-box moves
can decrease Delta, but only near the diagonal gap band and never by more than log 2.

Uniform Lipschitz bound (s4 section 4): brute force over all perturbations with C in {1,2,3,5}
of 300 random base diagrams (rng seed 73004, without replacement) per (M1,M2) in {2,3,5,8,24} x
{2,5,13,24}, rows up to (M1+M2)/2 + 4: 315,084 pairs, bound
|Delta' - Delta| <= C(K1+K2+1) + log(2C+1) holds everywhere, worst slack +1.816865 at
(M1,M2,ell1,ell2,ell1',ell2',C) = (3,24,1,1,2,0,1). Note: a weaker O(C) bound
|Delta' - Delta| <= C(K1+K2+2) follows from the increment identities by a single-box path
argument (per-move bounds: row-1 |log ratio| <= K1 + log 2, row-2 |log ratio| <= max(K2, log 2);
hook terms telescope along a path of <= C row-1 plus <= C row-2 moves inside the box, which is
lattice-connected in partitions), with no log(2C+1) refinement. The stated bound with the
log(2C+1) hook correction is the numerically supported form; I do not present a closed-form proof
of that exact constant. The s4 docstring phrase "brute force over ALL pairs" overstates: bases
are the 300-diagram random samples; all perturbations *of those bases* are enumerated. This
proposal re-labels accordingly; the script output (which prints only the honest pair count) is
byte-frozen and was not changed.

s4 section (5): the corner-mode relative weight delta_p = ((s1^2+s2^2)^p - s1^{2p} - s2^{2p}) /
Tr E^p contains no row argument (row-independence by construction of the 072 Lemma-1 spectrum),
N*delta_2 = 2.3943 / 2.4289 / 2.4377 / 2.4396 for N = 100/400/1600/3200, m = (1/2,1/3), k = 1
(identical to s3 section (2)). So the selection input stays additive up to the O(1/N) corner
mode uniformly in the row perturbation: perturbing rows cannot change the selection data.

### s5: continuum profile, uniform survival, linear breakdown

Riemann-sum limit (derivation). The summands f1(c) = log((M-1+c)/(M1-1+c)) and
f2(c) = log((M-2+c)/(M2-1+c)) are strictly decreasing in c, so
|sum_{c=1}^{l} f - int_0^l f| <= f(0) <= K' (K1' = log(M/(M1-1)), K2' = log((M-1)/(M2-1))).
With M_f/N -> m_f the integrals shift from the discrete to the continuum ratios by O(l/N) = O(1)
in total (the integrand difference is O(1/N) uniformly, argument Omega(N)), and
int_0^{Nu} log((a+x)/(m+x)) dx = N[G(a,u) - G(m,u)] exactly, G as above. The hook term obeys
|log((ell1+1)/(ell1-ell2+1))| <= log(ell1+1). Summing the four errors gives the coded bound
|Delta - N Lambda| <= 2K1' + 2K2' + log(ell1+1) + 2; s5 section (1) verifies it on all 75 random
diagrams (u1 in (0.02,0.7), u2 in (0,u1), N in {400,1600,3200}, three m pairs), worst
residual-minus-bound -6.163. Hence pointwise Delta/N -> Lambda(u1,u2) for all fixed fractions
(including u2 = 0, where the hook term vanishes), and the bound is uniform over all diagrams at
given M1, M2.

Positivity and monotonicity of Lambda (elementary, established):
d Lambda/d u_f = log((m1+m2+u_f)/(m_f+u_f)) > 0 since m1+m2 > m_f; Lambda(0,0) = 0; Lambda > 0
whenever (u1,u2) != (0,0) (each term is an integral of a positive function).

Box-minimum convergence (derivation, given the uniform bound): for fixed C, Lambda is monotone
in each argument, so min over B_C of N*Lambda is its far-corner value N*Lambda(u1 - C/N, u2 -
C/N); the uniform bound converts min-of-Lambda to min-of-Delta with error o(N); the far corner
is in the box, giving the matching upper bound. Hence min_{B_C} Delta / N -> Lambda(u1,u2) for
every fixed C, and since the derivation of the lower bound needs only C/N -> 0 (bound residual
(2K1'+2K2'+log(ell1+1)+2)/N -> 0 and Lambda-continuity), it holds for every C = C_N = o(N).
Numerics: fixed-C table at the saddle for three (m, t) classes (`s5` section 2) and C =
round(sqrt(N)) -> Lambda from below (0.468594 / 0.498548 / 0.506367 at N = 400/1600/3200 vs
Lambda = 0.523248) (`s5` section 3). The coded asserts also verify at every (class, N, C):
min >= Delta(saddle) - C(K1+K2+1) - log(2C+1) (the s4 bound), min <= corner + 1e-9, and
min >= N*Lambda(corner) - 2*ebound.

Deficit slope (first order in C): d/dC of the far-corner deficit = partial_1 Lambda +
partial_2 Lambda = log((a+u1)/(m1+u1)) + log((a+u2)/(m2+u2)); at the symmetric saddle
(m1 = m2 = 1/2, t = 1, u = 1/2): 2 log(3/2) = 0.810930 - the printed pred1st constant. Assert:
slope (Delta(saddle) - min)/(C*N) matches (2log(3/2))/N to < 5% at C = 10, N = 3200 (values give
0.07% at printed 6-digit precision (0.0386% at machine precision per review-r1 finding 5),
rounding error <= 0.04%, so "0.1%" is defensible but the
asserted, machine-checked statement is 5%). The observed offset N(Lambda - Delta(saddle)/N) =
8.31 (N = 3200) is the O(log N) hook + Riemann offset, log(1601) = 7.38 plus constants, and it
is the same offset at C = 100 (89.57 - 81.09 = 8.48), i.e. C-independent as the bound predicts.

Linear breakdown (C = cN). Exact combinatorics: (0,0) in B_C(ell) iff C >= ell1 (both coordinates
must be reachable), so at the symmetric saddle (ell1 = N/2 at t = 1) the box contains the trivial
diagram iff c >= 1/2, and the exhaustive box minimum is exactly 0 at (0,0) for c = 1/2,
N = 400, 1600 (assert < 1e-12). For c < 1/2 the minimum is bounded above by the far corner with
limit Lambda(1/2 - c, 1/2 - c) -> 0 as c -> 1/2: corner/N 0.425706 / 0.232712 / 0.059316 (N=400,
exact box min, argmin printed at the corner (160,160)/(80,80)/(20,20)) and 0.434531 / 0.240145 /
0.064185 (N=1600, corner) vs Lambda 0.438624 / 0.243769 / 0.066933 at c = 0.1 / 0.3 / 0.45.
Note the finite-N boundary case: at t = 0.5, N = 400 (rows (100,100)), the C = 100 box already
reaches the trivial diagram and min = 0 - the fixed-C table degenerates whenever C >= ell1, the
same combinatorics; this is an honest illustration that "fixed C" means fixed relative to the
rows, and the uniform statement is the asymptotic one. Asymmetric removal: Delta(ell1, 0)/N =
0.188909 vs Lambda(u1, 0) = 0.188937 at N = 1600, m = (1/2,1/3) (assert product diff < 5, actual
0.045): killing one row leaves Theta(N) - the defect vanishes (in the enumerated regime) only
when both rows are driven to zero. Sharp trade (`s5` section 5, single case, B = 40 < gap 46):
loss(row2) = 18.9499 > loss(half-half) = 15.4800 > loss(row1) = 13.4840; asserted lR2 > lR1:
the worst one-row removal is the row paired with the larger other-factor rank (row 2 is paired
with M1 = N/2 > M2 = N/3), matching the larger derivative partial_2 Lambda = 0.4832 vs
partial_1 Lambda = 0.2877 at those fractions (first-order predictions 19.3326 / 11.5073 -
row 2 within 2%, row 1 17.2% off (measured 13.4840 vs 11.5073, review-r1 finding 2) because its derivative correction O(C/ell) and hook offset are
larger at small gap; the half-half split is the milder trade).

### Comparison with the original target

The frontier target asked: show/map for which perturbation sizes the Theta(N) growth survives and
where it breaks, within the product dominant-representation class. This package delivers the
complete map *for the testbed defect Delta*: survives with full limiting fraction Lambda(u) for
every C = o(N); degrades continuously for C = cN with far-corner limit
Lambda(u1 - c, u2 - c) > 0 for every c < u1; the coefficient tends to 0 as c -> u1 = 1/2 (symmetric
t = 1); vanishes exactly at C >= ell1, the trivial diagram entering the box, while one-row
annihilation alone never kills it. The no-go at ~N/2 is the honest boundary the orchestrator
anticipated ("breakdown at perturbation ~N/2"): confirmed and made exact (C >= ell1 iff trivial
diagram in box; symmetric t=1 threshold c = 1/2).

### Relationship to 072

Same testbed, same hypothesis class (H1)-(H4), same closed form (072 Lemma 2); s1-s3 reproduce the
072 byte anchors (with the two review-r1 minor docstring fixes applied); s4-s5 add the new layer.
This package extends the L3158 statement ("within the dominant-representation class ... the
non-additivity ... is not an artefact of the fixed probe diagram") from the exact saddle to all
diagrams within o(N) of it, and adds the exact single-box sign/combinatorics and the breakdown
map. It changes none of the 072 caveats: frames, two-sided diagrams, minimised block entropy,
p_r log p_r, the block-cut selection-rule derivation, and the E-moments<->Q-moments
identification all remain as 072 left them. 072 review findings 1-5 are respected: no "(1)/(2)/(3)"
numbering anywhere in the insert (finding 4 - the insert uses no numbering at all); the byte
contract arithmetic is restated from the live simulate run, not copied (finding 1); the s2/s3
labels are the fixed ones (findings 2-3); the new paragraph carries its own scoped closer (finding
5).

### Literature

No new citation is load-bearing: the package uses only the hook-content dimension formula for
GL(M) irreducibles (the same classical input 065/072 already used and that the 072 gatekeeper
re-derived) and elementary calculus. The Frenkel selection rule is not re-cited here because the
robustness result is a statement about the selected diagram's defect under row perturbation, not
about the rule (see Decisions). Nothing cited that is not verified; no new BibTeX entries.

## Claim classification

1. **Established identity/derivation:** hook-content closed form for Delta (072, re-verified
   byte-identically: 1155 exact-rational checks); increment identities for the dim-ratio
   (algebra from the closed form; 4080 exact Fraction checks); row-2 sign criterion
   (M1-1)(ell1-ell2) < M2+ell2 (exact algebra; 1,023,120 integer comparisons); confinement
   (negative row-2 increments only for gap d < (M2+ell2)/(M1-1)) and lower bound -log 2 (exact
   implications); row-1 increment strictly positive for all valid arguments (one-line proof +
   grid assert); Delta(ell1, 0) > 0 for all ell1 >= 1 (each product factor > 1); Lambda formula
   and its positivity/strict monotonicity (elementary calculus on the Riemann integral); pointwise
   Delta/N -> Lambda and the residual bound (Riemann comparison for decreasing summands -
   derivation above - with the coded constant checked numerically); box-min convergence for fixed
   C and C = o(N) (derivation from the uniform bound + Lambda monotone/continuous); the
   breakdown combinatorics (0,0) in B_C iff C >= ell1 (trivial); (0,0) membership <=> c >= 1/2 at
   the symmetric saddle; selection-data row-independence (no row argument in delta_p).
2. **Conditional under (H1)-(H4) (072 class), and only as a statement about the testbed defect:**
   the whole package, since Delta is the class-internal model of the fixed-frame excess; the
   Theta(N)-survival and breakdown statements inherit this conditionality.
3. **Numerically verified (reproduced, finite; supports but does not prove the general case):**
   the residual bound at 75 sampled diagrams and all s5(2) box asserts; the stated uniform
   Lipschitz bound with the log(2C+1) hook correction at 315,084 sampled-base pairs (weaker
   O(C) bound derived; exact stated form not proved in closed form); far-corner argmin (exact
   enumeration at N = 400, c in {0.1,0.3,0.45}; printed at C = 100, N = 3200); exact zero
   minimum at c = 1/2 at N = 400, 1600 (exhaustive over the box); slope within 5% (asserted),
   0.07% from printed values (0.0386% at machine precision, review-r1 finding 5); loss-trade ordering and rho table (single N); the s4(3) confinement
   grid minimum +4.939491e-04 (grid M1, M2 <= 29, l1 <= 60).
4. **Finite-grid only (general case unproved):** Delta > 0 on all two-row partitions with
   ell2 >= 1 (s2 grid min 4.054651e-01; positivity at ell2 = 0 is established); ridge-increment
   positivity beyond the 4080-point grid assert.
5. **Conjecture / inherited input (unchanged from 072):** the block-cut transplant of the
   selection rule; that the saddle diagram is the selected diagram; any statement about the
   minimised block entropy. This package adds no new conjectures.
6. **Mechanism/argument (unchanged from 072):** the O(N^2)-separation conclusion; the physical
   reading of the box minimum as "the excess the fixed saddle data force, whatever the selected
   diagram within o(N)".

## Proposed changes

File `chapters/appH-microscopic-proofs.tex` only. No `bib/` change (no citation is load-bearing;
see Decisions). No ch17 change. No label/status/priority touch.

**Anchor** (inside the 065 block, adjacent to the 072 paragraph - exactly the 072 integration
point, so the new paragraph sits between the 072 scoped closer and the Vacuum-term paragraph):

- Boundary before (kept verbatim): the 072 closer ends "...they leave items (i)-(iii) of the
  preceding paragraph unchanged, and they close nothing in Problem~G." (L3159, kept).
- Boundary after (kept verbatim, occurs exactly once, live-asserted count = 1; the short form
  `\emph{Vacuum term.}` occurs twice and is never used):
  `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}` (L3161).
- Anchor used by `simulate_apply.py`: `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}`
  with the leading CRLF (line-start form). Live counts in the run: short 2, long 1, line-start 1.

**What is inserted** (one new paragraph, CRLF file `insert-r1.tex`, 2179 B, sha256
5722f69e6bd67ac99eeb7fa028e7b164c683c9d9325fe5cb28387a6f954d3c8a):

```latex
\emph{Robustness of the fixed-frame excess to bounded row perturbations.} Under the same hypotheses, the two-row defect \(\Delta\) of the preceding paragraph admits a uniform description under perturbations of the row lengths of the saddle diagram: with \(M_f=m_fN\) and saddle rows \(\ell_i=t\,s_i\), the ratio \(\Delta/N\) converges, uniformly over the valid two-row diagrams within a bounded distance of a diagram at fixed fractions \(u_f=\ell_f/N\), to \(\Lambda(u_1,u_2)=\sum_{f=1}^2\bigl[G(m_1+m_2,u_f)-G(m_f,u_f)\bigr]\) with \(G(m,u)=(m+u)\log(m+u)-m\log m-u\), with an error in \(\Delta\), and hence of that order divided by \(N\) in \(\Delta/N\), bounded by a constant of order \(\log(\ell_1+1)\) (numerical at \(N\le3200\)), and \(\Lambda\) is positive and strictly increasing in each argument at any nonzero pair of fractions. Hence the minimum of \(\Delta\) over all valid two-row diagrams with \(|\ell_i'-\ell_i|\le C\) is \(\Theta(N)\) for every \(C=o(N)\), with deficit from the saddle value linear in \(C\) at leading order and slope \(\sum_f\log\frac{m_1+m_2+u_f}{m_f+u_f}\) (numerical at \(C\le100\), slope to within \(5\%\) at \(C=10\), \(N=3200\)). The growth is not robust to linear perturbations: at \(C=cN\) the box minimum is bounded above by \(N\Lambda\) at the far-corner fractions, and at the symmetric saddle \(t=1\), \(m_1=m_2=1/2\) the box contains the trivial diagram exactly at \(c=1/2\) and its minimum vanishes there (numerical, exhaustively over the box at \(N=400\) and \(1600\)), while the removal of one whole row leaves a strictly positive limit (\(\Delta(\ell_1,0)/N=0.189\) at \(N=1600\), \(m_1=1/2\), \(m_2=1/3\), numerical). These statements are for the two-row hook-content defect of the product testbed within the same dominant-representation class as the preceding paragraph - compact factor with positive contraction, fixed frame, leading semiclassical order at the leading-order entropy, one diagram selected from the moments of the edge data, two rows, saddle row fractions held fixed under the perturbation - and they concern perturbations of the selected diagram at fixed saddle data, not the selection of the diagram itself.
```

**What is kept:** everything else in the file, including the 072 paragraph L3153-3159 and both
closers (L3159 and L3163), unchanged. No equation is moved or renumbered. The insert contains no
`\ref`, `\eqref`, `\label`, `$`, `\cite`, display math, no "(1)/(2)/(3)" numbering (the internal
numbering referenced in the manuscript text is only the Bearing paragraph's own (i)-(iii), which
this insert does not use), and no monotonicity claim about Delta in ell2 (the insert's "strictly
increasing" is a statement about the limit profile Lambda only).

**Byte contract** (from the reproduced `simulate_apply.out`, round-2 re-freeze after the
review-r1 finding-1 wording fix; live re-verification by the integrator is mandatory): appH
PRE 695,658 B / sha256 a41055028eb6a93e04d4ca509f335f8ca285ead761845137cd01aac7432550c4
/ CRLF 3,810 / bareLF 0 (asserted in the script; PRE pins printed byte-identical to round 1);
POST 697,839 B / sha256 437df96e4be9a5428840c42308fa770c5bc9c3e8aa39c0a03bab672d9e0f111c /
CRLF 3,812 / bareLF 0 (round-1 POST 697,767 B / ff90a68a... superseded by the corrected
insert); delta +2,181 B = insert body 2,177 B + 2 CRLF (line terminator + blank separator
line; the insert file is 2,179 B including its own terminal CRLF, which is the
paragraph-line terminator); CRLF delta +2; bareLF delta 0. bib unchanged: PRE = POST = 37,463 B / sha256
4d6d7b2a668fdaa64663e624b3f296d833c3bbcaa06a74ec5012a7f494ce0de6 / CRLF 1,239 / bareLF 0.

**Stale passages elsewhere:** none requiring edits. Note only (no action): the block closer L3163
("These statements are for a compact factor ... one dominant representation ...") enumerates the
065-block scope; read as covering all paragraphs between the Bearing paragraph and itself it
would understate the scope of this insert (which extends o(N) beyond the exact saddle) -
under-coverage is conservative and the insert's own closer names its scope, so no text edit is
proposed (mirrors 072 review finding 5).

## Verification scripts

All in this folder; reproduce with `python -I` from the repository root, stdout redirected:

- `python -I proposals/073-g-edge-rowshift/s1_moment_decomposition.py` -> 12-case edge-operator
  spectrum/moments regression. Expected invariant: `PASS s1`; max addrel 2.111e-16, max
  kroneck/site/spec 1.421e-14, rank dev 0.
- `python -I proposals/073-g-edge-rowshift/s2_hook_content.py` -> closed-form + increment + sign
  regression (exact rationals + sympy). Expected: `PASS s2`; `1155 checks, 0 failures`; grid min
  4.054651e-01 at (2,2,1,1); min increment -6.657482e-01 at (2,24,13,12).
- `python -I proposals/073-g-edge-rowshift/s3_saddle_residual.py` -> saddle scaling regression.
  Expected: `PASS s3`; Delta/N = 0.520906, ratio 0.751508, xN corner 2.4396, rank ratio 0.8111
  at N = 3200.
- `python -I proposals/073-g-edge-rowshift/s4_uniform_rowshift.py` (seconds; review-r1 finding 3) -> NEW exact
  increments / sign criterion / uniform bound / corner row-independence. Expected: `PASS s4`;
  480 + 4080 + 1,023,120 exact checks, 0 failures each; min row-2 inc (d >= d*) 4.939491e-04;
  worst row-2 inc -0.676053; 315,084 pairs, worst slack 1.816865; N*delta_2 table
  2.3943 -> 2.4396.
- `python -I proposals/073-g-edge-rowshift/s5_scaling_and_breakdown.py` (seconds; gatekeeper-timed ~1 s wall per review-r1 finding 3) -> NEW profile
  bound, box minima, sqrt-N class, linear breakdown, trade, rho table. Expected: `PASS s5`;
  worst residual-minus-bound -6.163; Lambda 0.523248; min/N at C=100: 0.495256 (N=3200);
  argmin (1500,1500); sqrt-N: 0.506367; c=0.50 min 0.0e+00 at (0,0); Delta(l1,0)/N = 0.188909;
  losses 13.4840/18.9499/15.4800; rho table.
- `python -I proposals/073-g-edge-rowshift/simulate_apply.py` -> read-only byte contract;
  expected appH post 697,839 B / sha 437df96e... / CRLF 3812 / bareLF 0; bib post == pre.

Reproduction performed this round (python -I, fresh, byte-compared with `cmp`):

    cmp s1.out s1.repro.out  -> IDENTICAL
    cmp s2.out s2.repro.out  -> IDENTICAL
    cmp s3.out s3.repro.out  -> IDENTICAL
    cmp s4.out s4.repro.out  -> IDENTICAL
    cmp s5.out s5.repro.out  -> IDENTICAL
    cmp simulate_apply.out (re-run) -> IDENTICAL

The `.repro.out` files are left in the folder for the gatekeeper.

## Decisions Taken

1. **No manuscript citation.** Rejected citing `Frenkel2023EdgeModes`: the robustness result uses
   only the hook-content defect, not the selection rule; citing would misattribute the dependency
   and the key is already present in the adjacent 072 text.
2. **Anchor = long-form Vacuum-term line (the 072 integration point).** Alternatives considered:
   anchoring after "...close nothing in Problem~G." (same effect but re-validates a longer mutable
   string); placing after the block closer L3163 (would put the paragraph outside the 065/072
   block and break adjacency). Rejected.
3. **Insert written in CRLF** per task directive (differs from 072's LF-insert + in-simulate
   conversion); `simulate_apply.py` asserts CRLF directly (bareLF = 0). Insert is one physical
   line + CRLF terminator, ASCII only, no trailing whitespace.
4. **Quantified slope claim in the insert weakened to the machine-asserted 5%**; the tighter
   0.07% measured from 6-digit prints (0.0386% at machine precision, review-r1 finding 5) is
   recorded in this proposal with its rounding-error bound (<= 0.04%), not in the manuscript
   text.
5. **s4 docstring overstatement "ALL pairs" re-labelled** (sampled bases x full perturbation
   box); scripts left byte-frozen so the reproduction stays exact; the printed outputs never made
   the overstated claim.
6. **Classified the s4(4) stated bound as numerically supported (weaker form derived)** rather
   than claiming the log(2C+1) form as derived; claiming it as a proof would outrun the code and
   the path argument I could close.
7. **Reported against the orchestrator's run-summary nuance:** exact box-min-vs-corner
   enumerations in s5(4) exist at N <= 400 only (the summary said "N <= 800"); the .out is
   authoritative and unchanged.

No decision above changes any label, scope or core assumption; none affects emergence of
spacetime.

## Milestone assessment

Routine. No MILESTONE.md trigger applies: no critical-path step is derived, no missing link is
closed without supplied inputs; this is a conditional, class-restricted sharpening with honest
boundaries.

## Status-label recommendation

Derived from the agenda + ledger this round: critical path = A, B, C, D, E, F, G, N (G:
OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL, per L3026-3029 re-read). Affected labels: none.
This package changes no status, priority or completion classification; Problem G stays
OPEN/CRITICAL PATH/PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

To close the original 073 target fully one would still need: (a) a closed-form proof of the
stated uniform Lipschitz bound constant log(2C+1) for all diagrams (currently: derived weaker
O(C) bound + 315k-point brute force); (b) positivity of Delta for all two-row partitions with
ell2 >= 1 beyond the s2 grid; (c) at linear scale, the box-min = far-corner identity is
exact-enumerated only at N <= 400 (c <= 0.45) and at C = 100, N = 3200; (d) all statements remain
conditional on the 072 class (H1)-(H4) and on the testbed identification of Delta with the
fixed-frame excess. For Problem G itself nothing changes: the missing steps (i)-(iv), mismatches
(1)-(2) in full generality, the frame average, the two-sided diagrams, the minimised block
entropy, the E<->Q moment identification and the p_r log p_r piece all remain as 072's review
left them (avenues (2)-(5) still open, unchanged in priority; avenue (1) is now mapped within the
class).

## Special instructions for the gatekeeper

- Scope limits: do not let any sentence be read as (i) a monotonicity claim for Delta in ell2
  (false; the 072 counterexample stands and is reproduced by s2), (ii) any statement about the
  minimised block entropy or the frame average, (iii) closure of anything in Problem G, or
  (iv) a claim about the *selection* of the perturbed diagram (the insert states the restriction
  to fixed saddle data explicitly).
- Re-derive, in order: the row-1/row-2/ridge increment identities from the 072 closed form (one
  line each); the sign-criterion equivalence (M+l2-1)(d) < (M2+l2)(d+1) <=> (M1-1)d < M2+l2; the
  antiderivative G and the two Riemann comparison bounds; the box-min convergence squeeze; the
  combinatorics "(0,0) in B_C iff C >= ell1". These are the load-bearing analytic claims; the
  scripts only check them at finite extent.
- Check that my classification's honesty holds, in particular: s4(4) "ALL pairs" overstatement
  (bases are 300 sampled per (M1,M2), seed 73004) - if the gatekeeper finds the weaker derived
  O(C) bound claim in this proposal wrong, downgrade accordingly; and the 0.07% slope statement's
  rounding bound (<= 0.04%).
- Re-verify the long-form anchor counts live (short 2 / long 1 / line-start 1) before any
  integration; the 072 text is integrated, so the context differs from 072's own simulate run;
  then run `scripts/build_check.py` after integration.
- Do not import any 065-internal "(1)/(2)/(3)" numbering (072 finding 4); this insert uses none.
- Reproduction is deterministic (`python -I`; rng seeds fixed 72001/73004/73005); no network or
  file writes by any script.
