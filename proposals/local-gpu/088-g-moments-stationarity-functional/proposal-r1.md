# Proposal 088-g-moments-stationarity-functional, round 1

## Result

Within the named coupled gaussian slot law of the integrated 084/085/087 paragraphs
(appH L3183-L3187), the Gamma-zero-locus — profiles constant on the connected
components of the coincidence graph of the frame law — is proved to be **exactly the
stationarity locus, at fixed slot count and fixed total weight, of the
frame-averaged decoupling functional itself**, Q_pi(g) = E_pi Gamma = g^T Sigma_pi g,
with the Hessian bound on mean-zero directions tied to the integrated 087 stiffness
lambda^+ (Lemma 1). The stationarity identification is then proved **rigid over the
whole decoupling-cone class** of functionals built from such frame-covariance data of
profile-independent frame laws by positive combinations and strictly monotone C^1
reparametrisations: the stationary locus of any member is the piecewise-constant locus
of the union of the coincidence graphs (Lemmas 2-3), so no member can stationarily
select a strict non-uniform profile, and the minimiser set is a continuum whenever a
graph is disconnected. A bounded addend classification (Lemma 4) localises the missing
ingredient: any slot-relabelling-symmetric C^1 addend leaves the uniform profile
stationary, and a strictly convex sum selects it uniquely; a unique non-uniform
stationary profile requires an extra term that distinguishes the slots or a non-convex
structure whose degenerate relabelling orbits need a further input. A repository audit
(what the core supplies) finds **no functional on profile space produced by the core
action**: the core action (eq:Smatrix) is a functional of configurations; the profile g
lives in the block-cut state model; the matrix integral supplies weights on
configurations and, under the positivity proviso of the integrated state-and-
coarse-graining paragraph, a state, but no weight on profile space. The package is
therefore the honest alternative named in the target: the stationarity identification
is completed for the integrated decoupling functional, a bounded obstruction is proved
for the full decoupling-cone hypothesis class, and the missing core ingredient is
localised exactly (a core-produced weight on profile space, non-degenerate along the
kernel directions). Nothing in Problem G is closed; missing steps (i)-(iv) untouched.

## Target and status

- Problem G (appH L3022-3191). Ledger label at L3026-3029 (quoted, not edited, not
  changed by this package): "Status: OPEN. Priority: CRITICAL PATH. Completion:
  PROGRAMME-CONDITIONAL." Edge `G.moments-derivedprofile` (frontier.yaml L487-517):
  attempted-open post-INTEGRATION-18; avenue (a) frame-measure-as-selector CLOSED-
  NEGATIVE, not re-opened here. Ch17 criterion (L488-490, quoted): "G is DERIVED only
  when the entropy density and stationarity relation are derived from the matrix theory
  and Lambda_eff follows from them." Note: the ch17 stationarity relation is
  eq:bdy-EE (boundary-metric stationarity); this package concerns the profile-
  stationarity of the 081-087 edge moment data and does not touch eq:bdy-EE.
- Dependencies relied on: the integrated 084 paragraph (Cov(a^2,r) = (s^4/2)Gamma,
  Gamma = sum q_i(g_i-mu)^2), the 085 paragraph (E_u Gamma identity, uniformity locus),
  the 087 paragraph (Gamma = Var_q(g), Sigma_pi = E_pi(diag q - qq^T), zero locus =
  piecewise constants on coincidence-graph components, stiffness bound with lambda^+ =
  least eigenvalue of Sigma_pi on mean-zero profiles, two-block datum E_pi Gamma = 0 at
  D_eff = 338/109 < 4). All quotable only inside their named classes.
- DERIVED vs PROGRAMME-CONDITIONAL: nothing derived for the programme. Lemmas 1-4 are
  established mathematics **within the named state class** (a supplied input class);
  the core-audit gap is an unresolved-step identification. No status, priority or
  completion label is proposed for change.

## Source reading

digest + targeted reads (digest compact, DIGEST CURRENT at dispatch, dirty-chapters:
yes, appH live hash e7736a56230f matches digest file-hash). Read in full: appH
L3022-3191 (entire Problem G section, incl. Missing step paragraph L3119-3130 and the
state-and-coarse-graining paragraph L3149); ch17-agenda L470-495 (G criterion and
completion levels); frontier.yaml G.moments-derivedprofile block (L487-517);
reports/sme-scout-20261118-1644.md in full; proposals/087-g-derivedprofile-selection:
insert-r2.tex (head+tail), hygiene_087_r2.py (banned-word list), review-r3.md verdict
line; ch03-matrix-action eq:Smatrix region. Unreadable files: none.

## Research and reasoning

Setup (integrated 087 data, quoted class): slots w_i complex gaussian with
E w_i w_j^* = s^2 g_i delta_ij; unit frame u, q_i = |u_i|^2; Gamma = Var_q(g); frame
law pi on the frame sphere; Sigma_pi = E_pi(diag(q) - qq^T), positive semidefinite,
Sigma_pi 1 = 0; Q_pi(g) := E_pi Gamma = g^T Sigma_pi g; ker Sigma_pi = {profiles
constant on components of the coincidence graph G_pi} (087); lambda^+ = least eigenvalue
of Sigma_pi on the mean-zero subspace, > 0 iff G_pi connected (087).
**Lemma 1 (stationary-kernel identity; established within the named class).** On the
slice {sum_i g_i = W} (any W; on the interior {g_i > 0} likewise), the stationary
profiles of Q_pi are exactly ker Sigma_pi, hence exactly the 087 zero locus, hence at
fixed weight exactly the minimiser set (min Q_pi = 0 on the slice, since the kernel
meets the slice). Proof: the Lagrange equations are 2 Sigma_pi g = lambda 1; pairing
with 1 gives 2 1^T Sigma_pi g = lambda D, and 1^T Sigma_pi = (Sigma_pi 1)^T = 0 forces
lambda = 0; so Sigma_pi g = 0; positive semidefiniteness gives g^T Sigma_pi g = 0 and
conversely. The Hessian is 2 Sigma_pi, so on mean-zero slice directions the second
variation is >= 2 lambda^+ ||v||^2 (tie to the integrated 087 stiffness) and vanishes
exactly along the kernel. Q_pi depends on pi only through Sigma_pi, so the whole
variational structure is second-frame-moment data. Verified by s1 (exact: annihilator
identity, kernel = component-indicator span for four laws including the 087 two-block
law, linsolve of the Lagrange system returns lambda = 0 and piecewise-constant solutions;
Dirichlet(1) moments reproduce the Haar Sigma = (I - J/D)/(D+1) exactly at D = 3,4,5;
deterministic Monte-Carlo frame check maxerr 3.63e-04, seed 88).

**Lemma 2 (cone / union-graph theorem; established).** For frame laws pi_1,...,pi_m and
c_a > 0, F = sum_a c_a Q_{pi_a} has ker(sum c_a Sigma_a) = cap_a ker Sigma_a =
{profiles constant on components of the union graph of the G_{pi_a}}, so the stationary
locus of F on every slice is the piecewise-constant locus of the union graph; the
minimiser set is a (k-1)-dimensional continuum when the union graph has k > 1
components. Consequence (bounded obstruction, named hypothesis class): every functional
in the decoupling-cone class — functionals of the profile through frame-covariance data
of profile-independent frame laws entered via positive combinations and strictly
monotone C^1 reparametrisations — has a purely combinatorial stationary locus; none
selects profile values within a component; the 087 two-block datum is the minimal case.
Proof: sum of PSD maps; x^T(sum c_a Sigma_a)x = 0 iff every term vanishes. Verified by
s2 (exact: nullspace of c_1 S_A + c_2 S_B equals the union-graph indicator span for two
exact coefficient pairs; Lagrange system of the combination returns lambda = 0 and the
union locus).

**Lemma 3 (monotone-reparametrisation rigidity; established).** grad(Phi o Q_pi)(g) =
Phi'(Q_pi(g)) * 2 Sigma_pi g exactly; for strictly monotone Phi the stationary locus on
the slice is unchanged; new stationary profiles arise only at values u with
Phi'(u) = 0, and these can form whole spheres: explicit counterexample at the Haar law,
D = 3, Phi(u) = (u-1)^2, slice sum g = 3: every g with Q = 1 (an exact circle
Q(v) = 2(a^2 + ab + b^2) on the mean-zero plane, e.g. g = (1 + sqrt(1/2), 1 - sqrt(1/2), 1))
is stationary for Phi o Q with grad Q != 0. So the non-degeneracy of the
reparametrisation is exactly the hypothesis needed. Verified by s2 (gradient collinearity
exact for exp / cubic / atan / lin+sin; explicit counterexample point and circle).

**Lemma 4 (addend classification; established for the stated sub-cases).** Write
F = Q_pi + R on the positive slice. (i) If R is C^1 and invariant under slot
relabelling, all partials of R coincide at the uniform profile (exact test on four
symmetric polynomials, s3), and since 2 Sigma_pi (uniform) = 0 the uniform profile is
stationary for F whatever R is. (ii) If in addition F is strictly convex on the slice
(the model case R = beta sum_i (-ln g_i), beta > 0, with Q the Haar-type form: projected
Hessian positive definite over 4000 random interior points, min eig 2.31; projected
gradient flow from three starts lands on uniform within 5e-14, seed 88), the unique
stationary profile is the uniform one. (iii) An addend that distinguishes the slots can
select a unique non-uniform stationary profile: exact example with block law q =
(1/2,1/2,0), R = gamma sum_i i g_i^2 (gamma = 1/4): unique stationary g* = (24/13,
12/13, 3/13), Q(g*) = 18/169 > 0, projected Hessian min eig 0.606 (s3). (iv) With a
relabelling-symmetric law, a symmetric non-convex addend leaves degenerate permutation
orbits of minimisers (grid minimisation of g^T(I - J/3)g - 3 sum g_i^4 on the simplex:
three equal minima, the permutations of (1,0,0)), so a further selection input is then
required. The addends in (ii)-(iv) are SUPPLIED illustrations of the shape the missing
ingredient must have; none is core content (rule-3 trap: the free-energy postulate and
its selection reading are kept out of the insert).
**Core audit (what the NAMCG core supplies as the object a functional could be derived
from).** ch03 eq:Smatrix: S_matrix = -(1/4g_YM^2) Tr([X^mu,X^nu][X_mu,X_nu]) + (1/3!)
Tr(C_{mu nu lambda}[X^mu,X^nu]X^lambda) + S_matter — a functional of the matrix
configurations only. The profile g is not a core coordinate: it is the slot-variance
profile of the block-cut edge state model (integrated 081 onward). The integrated
state-and-coarse-graining paragraph (L3149) records that the matrix integral defines the
configuration space and gauge action but "supplies no state on that space"; a state
arises from e^{-S/2} only where the weight is positive and integrable (compact factor,
Euclidean contraction), and not for the Lorentzian regulated weight. The integrated
Presentation-A bounded obstruction (L3043-3080) records that Presentation-A data supply
no region, cut or cover structure without a dictionary-type identification. Hence:
nowhere in the repository is a weight on profile space produced from the core — there is
no pushforward of the configuration measure under the (state-model) profile map, and no
core-derived trial-family free energy. Combined with Lemmas 1-4 this pins the missing
ingredient precisely: a weight on profile space, produced by the core and either
relabelling-non-symmetric or (with a relabelling-asymmetric frame law) non-convex,
non-degenerate along the kernel directions — i.e. derivation work on the state side
(087 avenue R1 neighbourhood), not on the frame-law side (closed-negative, untouched).

**Literature.** The SME scout report reports/sme-scout-20261118-1644.md (read in full)
routes: R1 Steinacker-line one-loop effective-action stationarity in background/profile
variables is the published prototype of "a functional the microscopic theory produces on
the profile variables" — the shape Lemma 4 demands; R2 TGFT mean-field/Gibbs-variational
selection matches the Lemma 4(ii) strict-convexity pattern (which answers uniform-only);
R3 Eguchi-Kawai center-stability matches the disconnected-orbit branch pattern of
Lemma 4(iv). I did not fetch or verify any of these papers this session; they are cited
here only as pointers via the scout file (whose own verification status per item is
stated there), and the two entries the scout marks "not independently verified" (Erdos-
Knowles-Yau-Yin 2014; Kiefer 1959 / Donsker-Varadhan / Ben Arous-Guionnet) are not
mentioned anywhere in this package. The manuscript insert is citation-free, as in
081-087. No number or citation in this package comes from outside the repository except
the scout-file pointers (reproduced, not imported as results).

**Comparison with the original target.** The target asked: prove the Gamma-zero-locus is
the stationarity locus of a functional DERIVED from the NAMCG core — or deliver the
honest alternative. Delivered: (a) the zero locus is exactly the stationarity locus of
the decoupling functional E_pi Gamma (within the named class; that functional is the
integrated 084-087 state-model object, not core-produced); (b) a bounded obstruction for
the full decoupling-cone class, including every monotone reparametrisation (so the
"postulate a free energy of the decoupling datum and read off selection" move is
provably incapable of value selection within that class); (c) the exact localisation of
the missing core ingredient. The target's core-produced-functional branch is NOT met
here; it remains the open step below. This is the "conditional package + bounded
obstruction + gap classification" alternative.

## Claim classification

- Lemma 1 (stationary-kernel identity; Hessian tie to lambda^+; dependence on pi only
  via Sigma_pi): established derivation, inside the named coupled gaussian slot law with
  profile-independent frame laws (a conditional class = supplied state model).
- Lemma 2 (cone/union-graph theorem; continuum of minimisers when disconnected):
  established derivation (same class); its use as obstruction over "the decoupling-cone
  class" is established for the class as defined in the insert.
- Lemma 3 (reparametrisation rigidity; spurious-circle counterexample): established.
- Lemma 4(i),(ii) (symmetric addend leaves uniform stationary; strict convexity gives
  uniqueness): established; the specific R = beta sum(-ln g) instance is a supplied
  regularisation (phenomenological input, illustration only). Lemma 4(iii),(iv):
  established for the exhibited supplied addends (input class, illustrative shape only;
  NOT core content, NOT a selection mechanism).
- Core audit ("no weight on profile space produced by the core anywhere in the record"):
  established as a repository audit of the current text (cited integrated passages); the
  existence of a route to such a weight is an unresolved step.
- Statements about problem status: none made (labels quoted verbatim from the ledger).
## Proposed changes

One paragraph, insert-r1.tex (3,927 B, sha8 cb681d3c), spliced into
chapters/appH-microscopic-proofs.tex as a new single line between the integrated 087
paragraph and the "\emph{Vacuum term.}" paragraph at L3189. No other text changes; no
bibliography entries; no other passage becomes stale (the insert adds, changes no
equation or claim elsewhere). Anchor: pin = the 087 closer tail "they classify the
locus over frame laws rather than selecting the profile" (live count 1, verified). The
header string "\emph{Vacuum term.}" is NOT unique in appH (count 2; the other instance
is in the Problem F block) — the integrator must splice by the pin, at the first
CRLFCRLF gap after the pin, at the next line start. The insert keeps every preceding
sentence intact; it replaces nothing. Insert hygiene (build-time and independent re-run):
single content line + terminal CRLF, no $ [ ] \cite \ref \eqref \label, zero words from
{status, priority, completion, open, critical, programme, derived}, one \emph header
(unique across chapters), balanced braces/parens, close idiom, numerals within {0,1,2}.

## Verification scripts

All under this folder; run from the repository root; python -I; deterministic (seeds 88).
- s1_stationary_kernel.py -> s1_stationary_kernel.out: expected PASS lines for the
  annihilator identity, kernel = component-indicator span (4 laws), Lagrange lambda = 0,
  exact Haar Sigma at D = 3,4,5, MC frame check maxerr < 3e-3.
- s2_cone_union_monotone.py -> s2_cone_union_monotone.out: union-graph kernel match
  (2 coefficient pairs, nullity 2), combination Lagrange result
  g0 = g1 = g2 = g3 = g4, g5 free; monotone-factorisation collinearity for 4 Phi;
  explicit spurious-stationary circle.
- s3_addend_shape.py -> s3_addend_shape.out: equal partials at uniform for 4 symmetric
  polynomials; projected-Hessian PD (min eig 2.31); three flows to uniform (< 1e-6);
  asymmetric-addend exact g* = (24/13, 12/13, 3/13), Q = 18/169 > 0; symmetric non-convex
  orbit: 3 permutation minima at (1,0,0).
- build_insert_088.py (rebuilds insert-r1.tex; guard lines must print OK; prints
  "insert-r1.tex bytes: 3927"); hygiene_088.py -> hygiene_088.out (overall PASS);
  simulate_apply_088.py -> simulate_apply_088.out (SIMULATE APPLY PASS).
Byte contract (live-verified this session): PRE = 744,476 B / sha256
e7736a56230f80eff3c3325c519eda797d2f3b7a1a77c4f785451d51b79df75b / CRLF 3,838 / bareLF 0;
added bytes 3,929 (insert 3,927 + separator CRLF 2); POST = 748,405 B / sha256
a03ba4156588da8d153be4e9a6bd65e720b49a8d60a8e97e984420f041c9b5c2 / CRLF 3,840 / bareLF 0.

## Decisions Taken

1. Deliver the within-class stationarity identification + cone obstruction + exact gap
   localisation rather than postulating any core free energy: the only fully supported
   route to the target's "or deliver the honest alternative" branch (rules 3, 6).
   Rejected: writing a Gibbs-variational or entropy-regularised functional into the
   insert (= free-energy postulate read off as selection; the 085 closer already flags
   the selection premise as supplied input). The regularisation examples stay as Lemma 4
   illustrations, classified as supplied inputs.
2. Anchor via the 087 pin because the "Vacuum term." header is not unique — recorded in
   the proposal and in simulate_apply_088.out.
3. Insert citation-free (repo-only numerals {0,1,2}); literature stays in this prose and
   remains scout-mediated, not verified by me.
4. Named the class "decoupling cone" inside the insert (self-contained definition).
5. Deferred to later packages (open avenues below): pi[g] self-consistent frame laws
   (087 R1), non-Gaussian slot laws (R2), the pushforward computation itself (the
   missing ingredient), SDP/loop-equation constraint route (R4).

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step derived, no missing link closed
without new unsupported inputs.

## Status-label recommendation

Unchanged (report only, no edits): G remains OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL; G.moments-derivedprofile remains attempted-open; the new
content is a within-class variational identity plus a class-bounded obstruction.

## Author decision needed

None.
## Remaining open step

To reach the target's first branch (a NAMCG-core functional): produce a weight on
profile space from the core — concretely, the pushforward of a core weight (Euclidean
contraction on a compact factor where positive and integrable, per the integrated state
paragraph; or a state supplied by Problem A/E content) under the block-cut profile map
g(X) = block-row variance profile, and show its log-density is non-degenerate along the
ker Sigma_pi directions (i.e. relabelling-non-symmetric or non-convex as Lemma 4
demands), then determine whether its stationary locus meets the Gamma-zero-locus. Even
then, the selection reading and the G missing steps (i)-(iv) remain exactly where the
Missing step paragraph states them. Ranked open avenues after this package: (1) the
pushforward/state-side construction above (unique route to the missing term); (2) pi[g]
self-consistency (087 R1) — outside this package's profile-independence hypothesis, now
constrained by Lemma 2 (any fixed-point can only refine the locus to a union graph);
(3) non-Gaussian slot laws (087 R2) — Lemma 1 survives verbatim for any law where Q_pi
remains the induced covariance quadratic form, so the rigidity results extend as long as
the frame-averaged coupling stays a quadratic form of the profile.

## Special instructions for the gatekeeper

1. Re-derive the forced-multiplier step (pairing 2 Sigma_pi g = lambda 1 with 1) and the
   kernel-intersection identity in Lemma 2; they are two lines each and carry the package.
2. Check the insert for over-claiming: it must be read as a statement about the named
   state class and the decoupling-cone class, NOT as deriving the functional from the
   core — the fifth sentence of the fourth block explicitly records what the core does
   and does not supply.
3. Verify the splice against the pin (the "Vacuum term." trap: count 2 in appH), the
   POST bytes, and the hygiene allowlists; re-run all .out files with python -I.
4. The Lemma 4 addends are supplied illustrations; flag as BLOCKING any integration edit
   that moves them into the insert or reads them as core content.
5. Do not treat this package as re-opening avenue (a) (frame measure as selector): the
   cone theorem generalises 087's measure-blindness, it does not relax it.
