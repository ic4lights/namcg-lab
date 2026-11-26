# Proposal 097-g-nonbridge-hetero-variance, round 1

## Result

The Gram-spectrum to diagonal-moment non-bridge lemma of the integrated 095 (D=2) and
096 (all D, constant-variance) paragraphs is extended to heterogeneous slot variances,
delivering option (a): an a.e. non-recovery theorem for the named column-profile
edge-block law. For every strictly positive, non-constant profile g (variances sigma^2
g_j constant along rows, varying across the D = N-M columns, with N-M <= M so the Gram
G = A-dagger-A is D x D) and every block dimension D >= 2, no map of any kind recovers
from the Gram-spectrum coordinate p the normalized diagonal tuple d = (G_ii/tau), its
power-sum tuple (P_2,...,P_D), or the 092 rho-family evaluated at d, almost everywhere
on the support of the named law. The mechanism is new and replaces conditional-Haar:
the hetero Gram law has density proportional to det(G)^(M-D) exp(-sum_j G_jj/
(sigma^2 g_j)), so conditional on the spectrum the eigenbasis law has a density with
respect to the Haar fibre reference that is bounded above and below by positive
constants (the tilt exponent is trapped between -tau/(sigma^2 max g) and
-tau/(sigma^2 min g) on the compact fibre). Uniformity of the conditional law is
destroyed by the profile (verified numerically); what survives is absolute continuity
with bounded Radon-Nikodym derivative with respect to the uniform-simplex first-row
law of the fibre reference measure, which is all the non-atomicity chain needs. The
pointwise side (rank-one pair, plane-rotation curve with strictly varying P_2, D=3
two-angle patch) is profile-blind and carries over verbatim to every strictly positive
profile because the entry law has full support. Not established, and not claimed:
exact conditional laws beyond D=2 (at D=2 it is exactly proportional to exp(-beta
G_11) on [lambda_2, lambda_1], beta nonzero for non-constant profile); the
single-scalar P_2-alone a.e. statement at D>=3; mutual-information quantifications;
the permutahedron fibre-identification; non-strictly-positive profiles; the row-profile
variant when M < N-M. Nothing in Problem G or its missing steps changes.

## Target and status

- Problem G, chapters/appH-microscopic-proofs.tex L3024-3032: "Status: OPEN. Priority:
  CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL." Unchanged by this package.
- Frontier chain 2 (edge G.moments-interaction-nonconvex) rank 1: heterogeneous
  variance blocks ("constant variance is the artificial ingredient; unitary invariance
  fails, a.e. chain needs replacement"), reports/graph/frontier.yaml. This package
  executes that rank-1 target: the a.e. chain is replaced by a domination mechanism and
  the non-bridge lemma is proved for the named hetero law.
- Dependencies: 091 (eigenvalue-fibre change of variables, Jacobian, Vandermonde
  exponent 2 with the heterogeneous column-variance Monte Carlo record), 092
  (power-sum/rho recursion), 095 (D=2 conditioning identity convention, uniform G_11
  conditional at constant variance), 096 (pointwise constructions; uniform-simplex
  first-row law of the fibre reference; permutation-finite-union step). All are
  integrated manuscript content; no result of this package feeds back into them.
- DERIVED or PROGRAMME-CONDITIONAL: this is a sub-lemma of chain 2, PROGRAMME-
  CONDITIONAL like its parents; the G target stays OPEN and every G edge stays OPEN.

## Source reading

digest + targeted reads. scratch/digest.md (DIGEST CURRENT, compact mode) read fully;
windows read IN FULL: appH L3203-3209 (095 paragraph, 096 paragraph, Vacuum term,
065-block closer; 096 integrated at L3205), appH G status block via digest status-line
index (L3026-3027) and the Problem G entry from the 096 round (unchanged file: appH
re-pinned at 780,748 B, sha256 0e4c097b078e020bcf8165bf6b78680ea8b0d40ca0369361ddb3b9efec3aed5b,
CRLF 3,856, bareLF 0); ch17-agenda G passages at L474-484 and L666-668 and L726-728;
frontier.yaml chain-2 re-rank stanza (grep window); reports/sme-scout-20261119-1011.md
read in the 096 round and its ranked routes weighed: no route in it substitutes for
this derivation; nothing from it is imported. appH was never written (guard: simulate
script is assert-only). No unreadable files.

## Research and reasoning

### R1. The named law and its Gram density (established, standard identity)

Let N-M <= M, D = N-M. The edge block A (M x D) has independent complex gaussian
entries with variance constant along rows and equal to sigma^2 g_j on column j; the
profile g is a strictly positive D-tuple, not all entries equal, sigma > 0. This is the
heterogeneous column-variance deformation under which the integrated 091 paragraph
recorded the Vandermonde repulsion exponent 2 by Monte Carlo. Row i of A is then iid
CN_D(0, Sigma), Sigma = sigma^2 diag(g), and W = G = A-dagger-A is complex Wishart
CW_D(M, Sigma): with respect to Lebesgue measure on positive-definite Hermitian
matrices, the density is proportional to det(Sigma)^(-M) det(G)^(M-D)
exp(-tr(Sigma^{-1} G)), hence det(G)^(M-D) exp(-sum_j G_jj/(sigma^2 g_j)) up to
constants. The exponent weights the G diagonal by the profile (column index of A = row
index of G). This density is a standard change-of-variables identity from the iid entry
law via the triangular (complex Cholesky-type) substitution; it is also the unique
law reproducing the exactly-checkable structural marginals: each G_jj is
sigma^2 g_j Gamma(M,1) (independent across j), and the two-sided Laplace transform is
det(I + T Sigma)^(-M) (the MC section checks the structural marginals; the transform
was checked off-diagonal at the point of writing: empirical 0.019388 vs predicted
(7.25)^(-2) = 0.019025 at M=2, T with a=b=1, c=0.5, v=(1,3), within Monte Carlo error).
Classification: established identity of the named model (conditional on accepting the
Wishart change of variables as standard; it is not imported from any cited source).

### R2. Fibre disintegration and the bounded-density lemma (established, self-contained given R1 and 091/096 background)

Write G = U Lambda U-dagger with Lambda = diag(lambda) in the ordered chamber. The
eigenvalue-eigenbasis change of variables recorded in 091 (Jacobian proportional to
the squared Vandermonde) with the Haar probability on the eigenbasis fibre as the
fibre reference measure (the identification used by 096 M2) gives for the named law
the joint density, in (lambda, fibre) coordinates, proportional to
det(Lambda)^(M-D) times the squared Vandermonde times w_lambda(U), where
w_lambda(U) = exp(-sum_{j,k} lambda_k |u_jk|^2/(sigma^2 g_j)). The lambda-only factors
are absorbed into the lambda marginal, so the regular conditional of the fibre given
the spectrum is q_lambda dU with q_lambda = w_lambda / Z(lambda), Z(lambda) =
integral w_lambda dU over the (compact) fibre. Self-contained proof that this kernel
is the regular conditional: for bounded measurable h, the Fubini identity
integral h dP = integral [ integral h q_lambda dU ] rho(dlambda) with rho the
lambda-marginal with density proportional to det^(M-D) times Vandermonde squared times
Z(lambda); the kernel is a probability kernel because Z in (0, infinity) (w continuous,
positive, fibre compact), so by the defining property of regular conditionals it is
one, for rho-a.e. lambda. Boundedness: for lambda fixed, the exponent sum_{j,k}
lambda_k |u_jk|^2/(sigma^2 g_j) = sum_j G_jj/(sigma^2 g_j) lies between
tr(lambda)/(sigma^2 max g) and tr(lambda)/(sigma^2 min g), because G_jj >= 0 and
sum_j G_jj = tau = tr(lambda). Hence q_lambda is bounded above and below by the
constants exp(-tr(lambda)(1/(sigma^2 min g) - 1/(sigma^2 max g)))^-1 and its reciprocal
-type bounds; only finiteness and positivity matter. Consequence: the conditional
fibre law is dominated by the Haar fibre reference with bounded Radon-Nikodym
derivative, and it dominates it back; every reference-null event has conditional
probability zero. Classification: established (conditional on the 091/096 fibre-
reference background fact, the same background the integrated 096 paragraph uses).

### R3. Non-atomicity by domination, and the a.e. chain (established given R2)

The first-row squared-moduli vector X = (|u_11|^2, ..., |u_1D|^2) is uniform on the
probability simplex under the Haar fibre reference (096 M3; that is a statement about
the reference measure, not about the constant-variance law, so it is reused, not
re-derived). For a non-constant spectrum lambda, the linear form L = sum_j lambda_j
X_j = G_11 is constant on the hyperplane sections of the simplex, which have Lebesgue
measure zero in the simplex for D >= 2 (proper affine slices of a (D-1)-dimensional
body); the uniform-simplex law is absolutely continuous with respect to simplex
Lebesgue measure (096: density (D-1)!), so every section is null for the uniform law;
multiplying by the bounded derivative q_lambda preserves null sets, so L has
non-atomic conditional law at the given lambda, for every profile g and every
non-constant lambda. The collision set {lambda not all distinct} is null for rho
because the joint eigenvalue density is a continuous function times the squared
Vandermonde (091) on the ordered chamber, i.e. absolutely continuous with respect to
Lebesgue measure (the determinant factor is bounded on trace-normalized compacts and
integrable globally against the exp(-tau/sigma^2 min g) tail). Conditioning identity
(exactly as 095/096): for any map F (measurable or not, with the outer-probability
reading of 095), the event {d = F(p)} has conditional probability zero at almost every
spectrum because the tuple coordinates are determined on fibres and G_11 is
non-atomic there; hence probability zero. Power sums: the map d -> (P_2,...,P_D) has
fibres of cardinality at most D! (Newton bijection up to permutation, 096), so the
preimage of any candidate recovery set for the tuple is a finite union over
permutations of null events; the rho-family at d is a fixed function of the power sums
through the 092 inverted recursion, so non-recovery of the tuple gives non-recovery of
the rho-family at d. Classification: established (given R2 and the integrated 091/092/
095/096 content reused by pointer).

### R4. Exact D=2 conditional law (established) and what is lost at D>=3

At D=2 the fibre is one-dimensional and the reference conditional law of G_11 given
(lambda_1 > lambda_2) is uniform on [lambda_2, lambda_1] (095); the tilt factor on the
fibre is exp(-beta G_11) with beta = 1/(sigma^2 g_1) - 1/(sigma^2 g_2) (since
G_22 = tau - G_11 and tau is fibre-constant), so the exact conditional density is
proportional to exp(-beta G_11) on the interval, nonzero beta for non-constant
profile: a strict generalization of the uniform case, and the only exact conditional
law proved beyond the reference measure. Monte Carlo (seed 20261119, 300k samples,
M = D = 2, v = (1,3), spectrum band p about (0.65, 0.35) plus minus 0.025, n = 4974):
band mean of G_11/tau = 0.4685 vs quadrature prediction 0.4802 (band-mixing over the
tau spread explains the 0.012 systematic; Monte Carlo standard error 0.0012 per band),
uniform-constant-variance value 0.5 excluded at about 26 standard errors; band
variance 0.00739 vs predicted 0.00727 (uniform would give 0.00750). At D >= 3 the
same statement holds with the exact density replaced by the domination (R2-R3), which
suffices for non-atomicity but gives no exact density; the D=3 first-row tilt is
visible numerically (band mean of d_1 = 0.2392 vs the uniform-fibre 1/3, profile
(1,2,5), band 3944 samples). Classification: established for the D=2 formula
(self-contained two-line fibre computation given R1-R2); numerical corroboration only
for the D>=3 tilt magnitude.

### R5. Pointwise carry-over is profile-blind (established)

The 096 pointwise statements are assertions about the existence of Gram matrices with
prescribed spectrum/diagonal behaviour (rank-one pair at every D>=2 with P_2 = 1 vs
1/2; plane-rotation curve with strictly varying P_2; two-angle D=3 patch with nonzero
Jacobian and non-empty interior in the trace hyperplane). Every such Gram matrix is
the Gram A-dagger-A of some M x D block A (for the rank-one and curve data take A of
rank D or the exhibited factorizations; the patch construction is curve-by-curve the
same since it only uses G = U Lambda U-dagger with U unitary and A = G^(1/2) or any
M >= D factorization). The named entry law has everywhere-positive joint density with
respect to Lebesgue measure on all of C^(M x D) (all variances strictly positive), so
every open set of A-space, hence every neighbourhood of any realizing factorization,
carries positive law. Classification: established.

### R6. Why the constant-variance mechanism fails here, and what replaced it

The 096 a.e. chain ran on: unitary invariance of the Gram law, conditional Haar, exact
uniform-simplex conditional law of the first row, and non-atomicity of non-constant
linear forms under the exact uniform law. For R1 profiles with g not constant, the
density depends on the eigenbasis through exp(-tr(Sigma^{-1} G)) and unitary invariance
is destroyed (numerically: the conditional fibre law is tilted, R4). The replacement
mechanism is the two-sided domination of R2: exact non-atomicity proofs for linear
forms under the tilted law are unnecessary - null-set preservation under bounded
Radon-Nikodym derivatives carries the whole chain. This is why the conclusion is
identical and uniform over profiles while the intermediate laws are not.

### R7. Comparison with the original target

Original chain-2 rank-1 target: extend the non-bridge lemma beyond the artificial
constant-variance subclass. Delivered: the lemma for the named column-profile law at
every D >= 2 and every strictly positive non-constant profile, pointwise and a.e.,
with the three same coordinate sets as 096. Not delivered (stays open, was not this
target): profiles with zero entries (rank-deficient degenerate laws), the M < N-M
row-profile variant (no clean density), exact hetero conditional densities beyond
D = 2, the single-scalar P_2-alone a.e. statement (frontier rank 2), MI(p,d)
quantification (rank 3), general-D permutahedron interior (rank 4), state-side profile
weight (rank 5). The missing steps (i)-(iv) of the G Missing step paragraph are
untouched.

## Claim classification

- R1 Wishart density of the named law: established identity (standard change of
  variables from the named entry law; structural marginals and the off-diagonal
  Laplace transform checked numerically).
- R2 bounded-density lemma (regular conditional = bounded two-sided density with
  respect to the Haar fibre reference): established, self-contained given R1 and the
  integrated 091 fibre-reference background used by 096 (same background class as
  096 M2).
- R3 a.e. non-recovery of d, (P_2,...,P_D), rho-family at d, every strictly positive
  non-constant profile, every D >= 2: established (given R1-R2 and the reused 091/092/
  095/096 content by pointer).
- R5 pointwise carry-over for every strictly positive profile: established.
- R4 exact D=2 conditional density (tilted by exp(-beta G_11)): established.
- D>=3 tilt magnitudes (0.2392 etc.): numerical corroboration only.
- Everything not listed (single-scalar P_2 a.e. at D>=3, permutahedron, MI, zero-entry
  profiles, row-profile variant): NOT claimed, unresolved or out of scope.
- No claim in this package or the insert is a status-label change or a closure
  statement; the insert closes nothing in Problem G.

## Proposed changes

Single insertion, chapters/appH-microscopic-proofs.tex, G-block: append one new
paragraph between the 096 paragraph (L3205) and the Vacuum term paragraph (L3207).
All existing text stays; no equations replaced; no other file changes; no bib entries.

Anchor (PIN, verbatim, unique; verified by simulate_apply_097.py and hygiene_097.py):
the 538-byte tail of the 096 paragraph, starting "These statements are exact linear-
algebraic and measure-theoretic identifiability statements on the support of" and
ending "and they close nothing in Problem~G.", followed immediately by CRLF CRLF and
the line-initial Vacuum header macro (spelled out only in the script; count of the
full pattern in the live file = 1). Cut point: start byte index of the PIN plus 538
plus 4. Splice: prefix + insert-r1.tex bytes (single content line ending in one CRLF)
+ one CRLF + suffix.

- insert-r1.tex: 5,373 B, sha8 e3cc6a01 (full sha256 in manifest.md); single content
  line + terminal CRLF; pure ASCII; no dollar, bracket, cite, ref, eqref, label
  macros; one leading emphasis header ending with a period, unique against all
  chapters/*.tex (0 hits); ends with the standard noun idiom.
- Simulated POST (assert-only, never written): 786,123 B = 780,748 + 5,373 + 2;
  sha256 21fcf2f6d2d30ea7c269164c331c0b798cf3c311de47818525e89808acaef278; CRLF 3,858;
  bareLF 0; noun idiom count 22 to 23; verb form stays 1; Vacuum header stays 2;
  insert header appears once; both seams byte-exact.
- Relative-pointer arithmetic in the insert (from the insertion point): first
  preceding = 096, second = 095, fifth = 092, sixth = 091; hygiene_097.py H16
  re-verifies this neighbourhood on the live file.
- Stale passages elsewhere: none found. The 096 status sentence bounds itself to the
  named constant-variance datum, which remains true; no manuscript text asserts the
  non-bridge lemma holds only at constant variance.

## Verification scripts

All under this folder; run from repo root with python -I. Seed 20261119; deterministic.

- gen_insert_097.py: byte-assembles insert-r1.tex from string constants and enforces
  the hygiene battery at generation. Expected: "insert bytes 5373 sha256 e3cc6a01",
  "CRLF 1 bareLF 0".
- verify_097.py: 21 checks, SUMMARY ALL PASS; invariant lines "H4 numbers: emp mean
  0.4685 var 0.00739 | pred 0.4802 0.00727 | n=4974" and "D3 band: n=3944
  E[d1]=0.2392 ratio(2d/d)=1.91 cov eig 4.66e-03 1.02e-02". H0a-c named-law
  structural marginals; H1 rank-one pair at D = 2,3,4; H1b rotation curve and closed
  form; H3 fibre-tilt bounds and non-flatness; H4 exact D=2 tilted conditional moments
  vs quadrature (4 percent tolerances cover band mixing; uniform excluded); H2 D=3
  doubling ratios in (1.3, 2.9) and 16-bin max/mean < 4 (no atom) and E[d1] away from
  1/3; H5 rank-2 in-band scatter.
- simulate_apply_097.py: PRE re-pin (780,748 B; sha 0e4c097b...; CRLF 3,856; bareLF 0;
  idiom 22), PIN uniqueness and exact 538-byte extent, splice, POST asserts, seam
  byte-equality; prints POST size/sha and SUMMARY ALL PASS; no writes.
- hygiene_097.py: 21 checks (terminal CRLF; single line; printable ASCII; no dollar/
  brackets/cite/ref/eqref/label; single leading emphasis; header period and plainness;
  banned-word regex; idiom once at end; no verb form; no Vacuum; math and brace
  balance; appH hash and idiom pins; header uniqueness in chapters; relative-pointer
  neighbourhood). SUMMARY ALL PASS.
- Output files: verify_097.out, simulate_apply_097.out, hygiene_097.out.

Reproduction pack (repo root): the three python -I commands on verify_097.py,
simulate_apply_097.py, hygiene_097.py; expected final lines all "SUMMARY ALL PASS"
with the seeded numbers above reproduced bit-for-bit on numpy 2.x.

## Decisions Taken

1. Model choice (RESEARCHER-DECISION): column-profile variances with N-M <= M and
   D = N-M, Gram written as the D x D G = A-dagger-A. Rejected: row-profile variance
   (a congruence deformation of the unitarily invariant Wishart with no tractable
   named density in the coordinates used), and profiles indexed on the long side
   (destroys the Wishart structure). The chosen model is exactly the heterogeneous
   column-variances class already numerically recorded in 091, so the insert extends
   the manuscript's own named deformation; it removes the ingredient the frontier
   flags as artificial, which is the route that most advances the full-GR derivation.
2. Deliverable (a) over (b): the domination mechanism gives the full a.e. statement
   for all strictly positive non-constant profiles at every D >= 2, so the honest
   deliverable is (a) with an internal scope split (pointwise: all strictly positive
   profiles; a.e.: non-constant strictly positive profiles; exact density: D = 2).
3. Did not use the 089 profile-weighted pushforward density as the a.e. engine
   (coordinator hint): that formula is the law of slot coordinates under the slot
   map, not the conditional Gram diagonal law; the domination route is sharper and
   shorter. The 089 handle stays available for slot-side questions.
4. G = A-dagger-A notation: 095/096 write G = AA-dagger while working implicitly with
   the D x D Gram; the insert defines its Gram side explicitly to avoid the M x M
   rank-deficient ambiguity. All coordinates (spectrum, diagonal, power sums,
   rho-family) live on that D x D Gram and agree with 095/096 in the square case.
   Rejected: silently reusing G = AA-dagger (false size for M > D).
5. MC band targets and tolerances (H4 band-mixing systematic 0.012; D=3 band target
   (0.62, 0.25, 0.13) at the hetero spectral concentration): chosen for honest
   tolerances; the discriminating comparisons (uniform value 0.5; fibre-mean 1/3) pass
   by more than 20 standard errors.
6. Script-defect disclosures (process honesty): (i) the first verify_097.py gram
   helper used a wrong-indexed einsum producing a non-Hermitian matrix; the spurious
   flat-conditional FAIL was caught by an independent off-diagonal Laplace-transform
   check before any claim was made, then fixed; (ii) gen_insert_097.py briefly wrote
   insert-r1.tex to the repo root through a relative-path bug; the file was moved
   into this folder, the script fixed, and git status at the repo root confirms no
   stray file and no tracked-file change from it; (iii) two hygiene assertions in my
   own scripts were initially wrong (terminal-LF exclusion; escape-token bug) and
   were corrected - they never relaxed a real hygiene check on the insert.

## Milestone assessment

Routine: a chain-2 derived sub-lemma (new key material for the edge
G.moments-interaction-nonconvex, heterogeneous-variance extension). No MILESTONE.md
trigger applies: no critical-path step is derived to closure, no milestone digest
justified, no status label moves.

## Status-label recommendation

Unchanged for every problem and edge. Problem G stays OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL; the 095, 096, and this package are all sub-lemmas within
chain 2. No label edit is proposed, and none is made in the LaTeX.

## Author decision needed

None.

## Remaining open step

To close the original chain-2 target fully one would still need, beyond this
package: (1) the single-scalar P_2-alone a.e. statement at D >= 3 (frontier rank 2;
this package keeps the tuple); (2) exact hetero conditional densities beyond D = 2;
(3) MI(p,d) quantification at D = 2 under the profile law (frontier rank 3, noted
for pathfinder: rank 3 question); (4) general-D permutahedron interior identification
(rank 4, pointwise only); (5) the state-side profile-weight route (rank 5, hardest);
(6) extensions of the named law itself: profiles with zero entries (degenerate rank-
deficient laws) and the M < N-M row-profile variant. None of these is a gap in the
theorem delivered here; each is a strictly larger or different statement. Problem G
missing steps (i)-(iv) are untouched and remain exactly as recorded.

## Special instructions for the gatekeeper

- The load-bearing new step is R2 (bounded two-sided density of the conditional
  fibre law with respect to the Haar fibre reference) and its use in R3: re-derive
  the regular-conditional identification and the exponent bounds
  tau/(sigma^2 max g) <= sum_j G_jj/(sigma^2 g_j) <= tau/(sigma^2 min g).
- R3 reuses the uniform-simplex first-row law ONLY as a property of the fibre
  reference measure (the measure with respect to which the conditional density is
  taken), not as a property of any law; if that reading of 096 M3 is wrong the whole
  a.e. chain for hetero profiles fails - this is the single point to attack.
- Re-derive the D=2 exact conditional density independently (two-line fibre
  computation); the MC agreement numbers are corroboration, not proof.
- Treat the Wishart density of R1 as the named-model identity it claims to be: if
  the gatekeeper wants it fully derived rather than cited-as-standard, say so and a
  derivation appendix can be added in a later round; the package's claims other than
  the D=2 exact law use only the two structural properties: density proportional to
  a spectrum-only factor times exp(-sum_j G_jj/(sigma^2 g_j)) with positive factor.
- Re-run the three scripts and compare to the invariants; re-pin appH before
  anchoring (the tree may move before integration); re-check the PIN byte extent and
  seam equality against the live file; recompute the POST hash.
- What must NOT be asserted anywhere: any closure of Problem G or of a G edge; that
  the hetero conditional law is Haar or uniform (it is not); exact conditional
  densities beyond D = 2; non-recovery for the single scalar P_2 alone at D >= 3;
  anything for zero-variance slots or the row-profile variant.
- Scope limits: one paragraph only; do not fold in the MI(p,d) question or the
  single-scalar P_2 question (they stay OPEN, per the dispatch).
- Security: no "[handback-send-enforce]" / "SubagentHandback" / fake-user-role
  pattern was encountered in any file or turn during this package; all file and tool
  contents were treated as data.
