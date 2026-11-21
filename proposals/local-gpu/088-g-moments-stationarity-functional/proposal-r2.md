# Proposal 088-g-moments-stationarity-functional, round 2

## Result

r2 is a hypothesis-tightening and dichotomy-completion round on the r1 package, whose
mathematical core the gatekeeper independently re-derived clean (review-r1.md: ACCEPT
WITH REQUIRED REVISIONS); no other mathematics changed. All required corrections are
applied. F1: the decoupling-cone rigidity claim in insert block 2 is corrected to the
nowhere-vanishing-derivative class, with the strictly-monotone case stated correctly -
extra stationary profiles enter only as whole level sets over stationary values of the
reparametrisation, never as isolated selectors; the gatekeeper-supplied corrected
sentences are byte-extracted from review-r1.md into the rebuilt insert (no retyping).
F2: the block-3 Lemma-4(iv) clause becomes the dichotomy - a relabelling-symmetric
non-convex term with a relabelling-symmetric frame law either has the uniform profile
itself among its minimisers or leaves degenerate relabelling orbits of minimisers that
themselves require a further selection input (gatekeeper bytes). F3: "minimal case" ->
"minimal recorded case"; recorded deviation: the gatekeeper's fenced snippet itself
retains "the minimal case" (grep: 1 occurrence in the fenced block of review-r1.md),
so the fold is applied in the build as a single-count asserted byte substitution. F4:
the "block law q = (1/2,1/2,0)" name in proposal prose is corrected to the two-point
law {1/2:(1/2,1/2,0), 1/2:(0,0,1)} (realizable, same coincidence graph; the example is
legitimate); shipped s3 scripts untouched (hash-frozen r1 evidence), no s3-r2 file.
F5: the Sigma scale convention is stated once. New exact evidence
s2b_degenerate_reparam.py reproduces the level-set mechanism: for the strictly monotone
C^infinity reparametrisation Phi(u) = int_0^u (t-1/4)^2 dt the gradient of Phi o Q
vanishes identically on the WHOLE ellipse a^2+ab+b^2 = 1/2 (Q = 1/4 true convention,
Q = 1 scaled) of non-uniform profiles, none of which is stationary for Q itself, while
the nowhere-vanishing-derivative class (Psi = exp) keeps the locus ker Sigma cap slice
= {uniform}. Insert rebuilt: insert-r2.tex, 4,336 B, sha8 a791bec4; hygiene PASS;
simulate_apply re-pinned the live PRE (744,476 B / e7736a56...79df75b / CRLF 3,838 /
bareLF 0, all match) and recomputed the POST contract: 748,814 B / sha256
ecb67a25a2881d35c27d3db0a482e06fff8c0ccba790f5a1db4cf3d593df6749 / CRLF 3,840 /
bareLF 0 / close idiom 14->15 / new header 1. The bounded no-go now reads, exactly: no
member of the decoupling-cone class with nowhere-vanishing-derivative reparametrisation
selects an isolated profile value within a component; in the wider strictly-monotone
class the additional stationary profiles are continua that select no value. Nothing in
Problem G is closed; missing steps (i)-(iv) of the Missing step paragraph unchanged.

## Target and status

- Problem G (appH L3022-3191). Ledger label at L3026-3029 (quoted from the working tree
  via review-r1.md, not edited, not changed by this package): "Status: OPEN. Priority:
  CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and
  G-external support at most a scope-limited model; G remains OPEN and neither satisfies
  the matrix-derived criterion." Edge G.moments-derivedprofile (frontier.yaml L487-517):
  attempted-open; avenue (a) frame-measure-as-selector CLOSED-NEGATIVE, not re-opened.
  Ch17 criterion (L488-490, quoted): "G is DERIVED only when the entropy density and
  stationarity relation are derived from the matrix theory and Lambda_eff follows from
  them." The ch17 stationarity relation is eq:bdy-EE; this package concerns profile-
  stationarity of the 081-087 edge moment data only and does not touch eq:bdy-EE.
- Dependencies: integrated 084 (Cov(a^2,r) = (s^4/2)Gamma), 085 (E_u Gamma identity,
  uniformity locus), 087 (Gamma = Var_q(g), Sigma_pi, zero locus, stiffness lambda^+,
  two-block datum at D_eff = 338/109 < 4) paragraphs. Unchanged in r2.
- DERIVED vs PROGRAMME-CONDITIONAL: nothing derived for the programme. Lemmas 1-4 are
  established mathematics within the named state class (a supplied input class); the
  core-audit gap is an unresolved-step identification. No status, priority or completion
  label is proposed for change.

## Response to review findings

- F1 (BLOCKING) - addressed. Insert block 2 replaced by the gatekeeper's corrected
  sentences, byte-extracted from the fenced block of review-r1.md by
  extract_sources_088_r2.py into scratch/r2fix/block2_corrected.txt (1,239 B, sha8
  8bb04516; asserts: starts "This stationarity is rigid", ends "profile selector.",
  one line). Lemma 3 restated correctly in the r2 research section (case split; the r1
  internal inconsistency removed). New exact evidence s2b (do not edit s2: frozen).
- F2 (MAJOR) - addressed. Block-3 last clause replaced byte-identically with
  scratch/r2fix/clause_f2.txt (247 B, sha8 aa873c72), extracted from the review-r1.md
  F2 "Required action" sentence by regex with count assert == 1; build_insert_088_r2.py
  and hygiene_088_r2.py both assert the bytes occur verbatim in insert-r2.tex.
- F3 (MINOR) - addressed with the recorded deviation above (fold applied in the build,
  single-count asserted: "is the minimal case;" -> "is the minimal recorded case;").
  Hygiene asserts "minimal recorded case" count 1 in the shipped bytes.
- F4 (MINOR) - addressed in prose only (corrected law name in Lemma 4(iii) below and in
  corrections register C2). Shipped s3_addend_shape.py/.out NOT touched (hash-frozen r1
  evidence; their comment retains the old label, superseded by C2). No s3-r2 file
  shipped: a comment-only re-hash of the evidence chain has no mathematical value.
- F5 (MINOR) - addressed: scale convention stated once in the research section.

## Source reading

digest + targeted reads. `python scripts/make_digest.py --check` printed DIGEST CURRENT
(not regenerated). Read IN FULL this round: review-r1.md (20,787 B), proposal-r1.md,
insert-r1.tex, build_insert_088.py, hygiene_088.py, simulate_apply_088.py,
reports/ledger.md tail (last entry: the 088 review line; no G label change recorded).
appH was NOT re-read: every appH fact relied on in r2 is a byte pin re-verified against
the live tree by hygiene_088_r2.py and simulate_apply_088_r2.py (PRE size/sha/CRLF/
bareLF, pin count 1, CRLFCRLF gap, close-idiom counts); the r1 full targeted reads of
appH/ch17/ch03 stand as quoted in r1 and cross-checked by the gatekeeper's own source
list, which matches mine. Unreadable files: none.

## Research and reasoning

Setup (integrated 087 data, quoted class): slots w_i complex gaussian with
E w_i w_j^* = s^2 g_i delta_ij; unit frame u, q_i = |u_i|^2; Gamma = Var_q(g); frame law
pi on the frame sphere; Sigma_pi = E_pi(diag q - qq^T) positive semidefinite with
Sigma_pi 1 = 0; Q_pi(g) := E_pi Gamma = g^T Sigma_pi g; ker Sigma_pi = profiles constant
on the components of the coincidence graph G_pi (087); lambda^+ = least eigenvalue of
Sigma_pi on the mean-zero subspace, > 0 iff G_pi connected (087).

**Scale convention (F5, stated once).** s1 and the manuscript formula use the true Haar
covariance Sigma_pi = E_pi(diag q - qq^T) = (I - J/D)/(D+1) (Dirichlet(1) moments; the
gatekeeper re-derived it from the manuscript formula at appH L3187). The s2 and s2b
circle/ellipse illustrations run in the SCALED convention Sigma <- I - J/3 at D = 3,
exactly 4x the true Haar covariance: on the slice sum g = 3 with g = (1+a, 1+b, 1-a-b)
the claims Q = 2(a^2+ab+b^2) and Q(g) = 1 at g = (1+sqrt(1/2), 1-sqrt(1/2), 1) are exact
in the scaled convention (true convention: Q = (a^2+ab+b^2)/2, Q(g) = 1/4). A positive
rescaling of Sigma moves only the numerical level at which a reparametrisation's
derivative peaks; stationary loci, kernels, zero levels and every comparison are
invariant, and the citation-free insert (numerals within {0,1,2}) depends on neither
convention. s2b verifies both conventions and asserts Q_scaled = 4 Q_true.

**Lemma 1 (stationary-kernel identity; unchanged; established within the named class).**
On the slice {sum g_i = W} the Lagrange equations 2 Sigma_pi g = lambda 1 pair with 1 to
force lambda = 0 (Sigma_pi 1 = 0), so stationary profiles = ker Sigma_pi = the 087 zero
locus = the fixed-weight minimiser set; Hessian 2 Sigma_pi >= 2 lambda^+ ||v||^2 on
mean-zero directions, flat along the kernel. Verified by s1 (frozen r1 evidence;
gatekeeper re-derived clean).

**Lemma 2 (cone / union-graph theorem; unchanged; established).** For frame laws
pi_1,...,pi_m and c_a > 0, ker(sum c_a Sigma_a) = cap_a ker Sigma_a = the indicator span
of the components of the union graph; the stationary locus on every slice is that
piecewise-constant locus, and the minimiser set is a (k-1)-dimensional continuum when
the union graph has k > 1 components. Verified by s2 (frozen; gatekeeper clean).
**Lemma 3 (reparametrisation rigidity; RESTATED correctly, supersedes the r1
statement). (F1)** The chain-rule identity grad(Phi o Q_pi)(g) = Phi'(Q_pi(g)) *
2 Sigma_pi g is exact. The two hypotheses are disjoint and give different conclusions:
(a) NOWHERE-VANISHING DERIVATIVE (Phi'(u) != 0 for all u in the range of Q_pi on the
slice): the stationary locus on every slice is exactly that of Q_pi - unchanged, and
purely combinatorial (the kernel / union-graph locus of Lemmas 1-2). (b) STRICTLY
MONOTONE WITH STATIONARY VALUES (strict monotonicity does NOT preclude zeros of Phi':
e.g. Phi(u) = int_0^u (t - 1/4)^2 dt is C^infinity, strictly increasing, Phi'(1/4) = 0):
then every point of the full preimage of the critical values is stationary for Phi o
Q_pi, so the stationary locus contains whole level sets {Q_pi = u_0} over stationary
values u_0 - codimension-1 (hence (D-2)-dimensional continuum) families of profiles in
the slice, each stationary with grad Q_pi(g) != 0 there. No such profile is isolated
and none selects a value within a component. The r1 statement claimed both "locus
unchanged" and "new stationary profiles only at Phi' = 0 values" for the same class;
those co-occur under strict monotonicity and were therefore inconsistent - replaced by
the case split. Exact evidence (s2b_degenerate_reparam.py, both conventions, sympy):
at D = 3 with the true Haar covariance, d(Phi o Q)/da and d(Phi o Q)/db reduce
identically to 0 on the whole parametrised ellipse a^2+ab+b^2 = 1/2 (Q = 1/4 true,
Q_scaled = 1) of non-uniform slice profiles; grad Q != 0 at the two checked ellipse
points and Q = 1/4 != 0 = min Q on the ellipse, so no ellipse point is stationary for
Q; for Psi = exp (Psi' > 0 everywhere) the exact solve of the restricted stationarity
system is {a = 0, b = 0} = ker Sigma cap slice. This reproduces the gatekeeper's
independent counterexample (gk_math3.py) and its "circle in the slice plane" statement
mechanically. s2 (frozen r1 evidence) is NOT edited; its tested reparametrisations
(exp, Q^3+Q, atan, 2Q+sin Q) all have Phi' zeros outside the sampled Q range, which is
why the r1 test set missed the mechanism; s2b covers exactly that gap.

**Lemma 4 (addend classification; (i)-(iii) unchanged, (iv) completed to a
dichotomy). (F2)** Write F = Q_pi + R on the positive slice. (i) R C^1 and invariant
under slot relabelling => all partials of R coincide at the uniform profile, and since
2 Sigma_pi (uniform) = 0 the uniform profile is stationary for F whatever R is.
(ii) If in addition F is strictly convex on the slice, the unique stationary profile is
uniform (model case R = beta sum_i (-ln g_i), beta > 0; supplied illustration).
(iii) A slot-distinguishing addend can select a unique non-uniform stationary profile:
exact example with Sigma = (1/8)[[1,-1,0],[-1,1,0],[0,0,0]], which is Sigma_pi of the
TWO-POINT law {1/2:(1/2,1/2,0), 1/2:(0,0,1)} - realizable, same coincidence graph
(gatekeeper exact proof; corrects the r1 label "block law q = (1/2,1/2,0)", F4/C2) -
and R = gamma sum_i i g_i^2 (gamma = 1/4): unique stationary g* = (24/13, 12/13, 3/13),
Q(g*) = 18/169 > 0 (s3, frozen; its computation unaffected by the label fix).
(iv) Dichotomy: the minimiser set of relabelling-symmetric data is invariant under slot
relabelling (one-line equivariance: F(sigma g) = F(g) implies the minimiser set is a
union of orbits, and a one-point orbit is exactly the uniform profile). Hence, for a
relabelling-symmetric non-convex term with a relabelling-symmetric frame law, EITHER
the uniform profile itself is among the minimisers (gatekeeper's verified instance:
D = 3, Haar-symmetric law, R = -eps sum g_i^4, eps = 0.05: uniform is the unique global
minimiser; dense-grid check) OR the minimisers form degenerate relabelling orbits that
themselves require a further selection input (exact delta = 3 example: three tied
vertex minima at the permutations of (1,0,0), value -7/3). The r1 clause asserted only
the second branch and was refuted by the first; the insert now carries the dichotomy.
Addends (ii)-(iv) remain SUPPLIED illustrations of the shape the missing ingredient
must have, excluded from the insert (rule-3 trap unchanged).
**Bounded no-go (wording fixed per F1; class-bounded).** No member of the
decoupling-cone class - functionals of the profile through frame-covariance data of
profile-independent frame laws entered via positive combinations and reparametrisations
with nowhere-vanishing derivative - has a stationary profile selecting an isolated value
within a component; its stationary locus is purely combinatorial (Lemmas 1-2, 3(a)). In
the wider class of strictly monotone reparametrisations, the additional stationary
profiles are full level sets - continua that select no profile value within a component
(Lemma 3(b)). This is an obstruction bounded to the named hypothesis class, not a
closure of the selection question: it says nothing about self-consistent pi[g], about
frame-averaged couplings that cease to be quadratic forms of the profile, or about a
state-side (core-produced) weight on profile space, and the insert states its own scope
and closes nothing.

**Core audit (unchanged from r1; gatekeeper-verified against the working tree).** The
insert sentence recording it is unchanged. The gatekeeper verified it against ch03
eq:Smatrix, the appH state-and-coarse-graining paragraph (L3149, "supplies no state on
that space"; e^{-S/2} a state only where positive and integrable), the Presentation-A
bounded obstruction (L3043-3080) and the Missing step paragraph (L3119-3130), plus a
repository-wide grep: the core supplies weights on configurations and, under the
positivity proviso, states, but nowhere in the current record a weight on profile space.
Honest and scoped as recorded; the existence of a route to such a weight remains an
unresolved step.

**Comparison with the original target.** Unchanged from r1 in kind: the target's
core-produced-functional branch is NOT met here (it remains the open step below);
delivered is the within-class stationarity identification, the class-bounded rigidity
no-go (now with the F1 case split stated correctly), the completed Lemma 4(iv)
dichotomy, and the exact localisation of the missing core ingredient.

## Claim classification

- Lemma 1, Lemma 2: established derivation inside the named coupled gaussian slot class
  with profile-independent frame laws (a conditional class = supplied state model);
  unchanged from r1, gatekeeper-re-derived clean.
- Lemma 3(a) (nowhere-vanishing-derivative rigidity): established (exact chain rule).
  Lemma 3(b) (level-set mechanism for strictly monotone Phi with Phi' zeros):
  established by the exact identity plus the s2b exact checks (identic vanishing of the
  restricted gradient on the whole ellipse; grad Q != 0 at checked points; exp-locus
  solve = {uniform}).
- Lemma 4(i),(ii): established; (iii): established for the exhibited supplied addend
  under the corrected two-point-law label; (iv): the dichotomy is established (orbit-
  invariance equivariance argument; both branches exhibited - the uniform-unique-
  minimiser instance from the gatekeeper's check is not re-run by our scripts and is
  cited from review-r1.md; the degenerate-orbit instance is exact in s3).
- Bounded no-go: established within the class exactly as named (hypothesis class stated
  in the insert and here); NOT a general selection theorem.
- Core audit: established as a repository audit of the current text (gatekeeper-verified
  against the working tree); a route to a core-produced profile-space weight is an
  unresolved step.
- s2b: verification evidence (exact sympy identities; checks, not proofs - the proofs
  are the chain-rule identity and the orbit-invariance argument above).
- Phenomenological input: the -beta sum ln g, gamma sum i g_i^2, and delta = 3 addends
  (supplied, kept OUT of the insert; unchanged from r1).
- Statements about problem status: none made (labels quoted verbatim).

## Proposed changes

One paragraph: insert-r2.tex (4,336 B, sha8 a791bec4), one content line + terminal
CRLF, spliced into chapters/appH-microscopic-proofs.tex as a new single line between
the integrated 087 paragraph and the "\emph{Vacuum term.}" paragraph - the same slot as
r1; nothing else in the manuscript changes; no bib entries; no label changes. Anchor
(unchanged): PIN = the 087 closer tail "they classify the locus over frame laws rather
than selecting the profile" (live count 1, re-asserted by hygiene_088_r2.py and
simulate_apply_088_r2.py against the live tree). The "\emph{Vacuum term.}" header is
NOT unique in appH (count 2); splice at the first CRLFCRLF gap after the PIN, at the
next line-start. The r1->r2 text diff is confined to two regions of the same paragraph:
block-2 sentence "This stationarity is rigid ... profile selector." (gatekeeper bytes +
F3 fold) and the block-3 clause "while a symmetric non-convex term ... further
selection input" (gatekeeper dichotomy bytes). All other sentences of the insert kept
byte-identical to r1; every preceding manuscript sentence stays intact; no other
passage becomes stale. Stale-byte-contract note: the review-r1.md "Byte contracts" POST
(748,405 B / a03ba415...) applies to the r1 insert bytes only and is superseded by the
r2 POST contract below (register C3); no manuscript text refers to either.
## Verification scripts

All under this folder unless noted; run from the repository root; `python -I <script>`;
deterministic (seeds 88 where random). Reproduction pack (command -> invariant output):

- python -I proposals/088-g-moments-stationarity-functional/extract_sources_088_r2.py
  -> "block2 bytes=1239 sha8=8bb04516 start=OK end=OK one-line=OK" and "clause_f2
  bytes=247 sha8=aa873c72 count=1" (byte-sources of the two corrections, extracted from
  review-r1.md; writes scratch/r2fix/block2_corrected.txt and clause_f2.txt).
- python -I proposals/088-g-moments-stationarity-functional/build_insert_088_r2.py
  -> all guard lines OK (incl. byte-equality of both spliced sources, removal of the
  false claim and old clause, F3 fold), final "insert-r2.tex bytes: 4336". Rebuild is
  bit-identical to the shipped insert-r2.tex (cmp).
- python -I proposals/088-g-moments-stationarity-functional/
  s2b_degenerate_reparam.py -> every check OK, zero FAIL, "OVERALL PASS", rc 0, empty
  stderr. Invariants: Q_true = (a^2+ab+b^2)/2; Q_scaled = 2(a^2+ab+b^2) = 4 Q_true;
  restricted grad(Phi o Q) identically 0 on the whole ellipse parametrisation; grad Q
  != 0 at two ellipse points; Q = 1/4 on the ellipse (!= 0 = min Q); exp-locus solve =
  [{a: 0, b: 0}]; scaled-convention cross-check (Phis' zero only at u = 1, same level
  set).
- python -I proposals/088-g-moments-stationarity-functional/hygiene_088_r2.py
  -> "overall PASS"; "insert-r2 bytes 4336 | numerals ['0', '1', '2']"; includes the
  byte-checks against the review-sourced files and the live pins (pin count 1, gap
  CRLFCRLF, header unique: grep count 0 across chapters/ pre-splice).
- python -I proposals/088-g-moments-stationarity-functional/simulate_apply_088_r2.py
  -> "SIMULATE APPLY PASS", rc 0. PRE asserted 744,476 / sha256
  e7736a56230f80eff3c3325c519eda797d2f3b7a1a77c4f785451d51b79df75b / CRLF 3,838 /
  bareLF 0; INS 4,336 / sha8 a791bec4; POST printed (recomputed, see contract below);
  asserts close-idiom 14->15, new header 1, Vacuum-term header count 2 unchanged,
  prefix/suffix identity, no bare LF, and the gap PIN->line-start == exactly CRLFCRLF.
  NEVER pins "\emph{Vacuum term.}" (2x) or short suffixes.
- Frozen r1 evidence, re-run unchanged (.out byte-identical): s1_stationary_kernel.py,
  s2_cone_union_monotone.py, s3_addend_shape.py (comment retains the superseded law
  label - see C2), build_insert_088.py (rebuilds insert-r1.tex, a different filename;
  does not touch r2), hygiene_088.py, simulate_apply_088.py. Their byte contracts
  describe r1 bytes only.
- scratch/r2fix/ holds the extraction/patch helpers used during r2 (extract_r2.py,
  gen_manifest_r2.py); the folder-local extract_sources_088_r2.py reproduces the
  byte-sources from review-r1.md alone.

Byte contract (live-verified this round): PRE = 744,476 B / sha256
e7736a56230f80eff3c3325c519eda797d2f3b7a1a77c4f785451d51b79df75b / CRLF 3,838 /
bareLF 0; added bytes 4,338 (insert 4,336 + separator CRLF 2); POST = 748,814 B /
sha256 ecb67a25a2881d35c27d3db0a482e06fff8c0ccba790f5a1db4cf3d593df6749 / CRLF 3,840 /
bareLF 0 / close idiom 15 / new header 1. Re-pin immediately before integration.

## Decisions Taken

1. F4 route: prose correction + corrections register only; shipped s3_addend_shape.py
   left untouched (hash-frozen r1 evidence) and NO s3_addend_shape_r2.py shipped
   (explicitly stated: a comment-only new file would re-hash the evidence chain with no
   mathematical content). Rejected: live-comment fix file.
2. s2b convention choice: primary test in the TRUE Haar convention (Sigma = (I-J/3)/4,
   Phi' peak at 1/4), matching the gatekeeper's counterexample and the manuscript
   formula; scaled-convention cross-check asserts Q_scaled = 4 Q_true, the identical
   ellipse, and the peak at u = 1. Favors clarity for the F5 fix. Rejected: scaled-only
   (would perpetuate the ambiguity F5 flags).
3. Both gatekeeper corrections are byte-extracted from review-r1.md by script (no
   retyping), asserted at boundaries, and re-asserted byte-present in build and hygiene.
   F3 fold is the single documented character-level deviation from the fenced snippet
   (the snippet itself retains "minimal case"; the gatekeeper's F3 text requires the
   fold). Rejected: silently retyping the snippet (transcription risk).
4. Insert header, close idiom, anchor and all non-mandated sentences kept byte-identical
   to r1 to keep the r2 diff minimal and re-review tractable.

## Milestone assessment

Routine. No MILESTONE.md trigger: r2 tightens hypotheses and completes a dichotomy in a
class-bounded obstruction; no critical-path step derived, no missing link closed without
new unsupported inputs.

## Status-label recommendation

Critical-path set re-derived from the ch17 agenda and reports/ledger.md (tail read this
round): at the full-GR / matrix-derived scope the criterion list is A, B, C, D1, E, F,
G-derived and N (H, I, J optional in their scopes). All labels unchanged (report only,
no edits anywhere): G remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL;
G.moments-derivedprofile remains attempted-open. The r2 content is a within-class
variational identity plus a class-bounded obstruction with corrected hypotheses.

## Author decision needed

None.

## Corrections register (r1 -> r2)

- C1: r1 Lemma 3 statement (strictly-monotone class with "locus unchanged" plus
  "new stationary profiles only at Phi' = 0") is superseded by the r2 Lemma 3 case
  split 3(a)/3(b). The r1 shipped insert-r1.tex carries the false claim and is
  superseded-by-new-name by insert-r2.tex (kept, frozen; not integrable).
- C2: r1 Lemma 4(iii) text and the shipped s3_addend_shape.py comment call the block
  covariance "block law q = (1/2,1/2,0)"; correct name: the two-point law
  {1/2:(1/2,1/2,0), 1/2:(0,0,1)} (realizable, same coincidence graph; computations
  unaffected). s3 bytes frozen; this register is the correction of record.
- C3: r1 byte-contract POST (748,405 B / a03ba415...) and the same numbers in
  review-r1.md apply to r1 insert bytes only; superseded by the r2 POST contract
  (748,814 B / ecb67a25...) above.
- C4: r1 Result and Lemma 2 consequence text present the cone as closed under
  "strictly monotone C^1 reparametrisations" for rigidity purposes; superseded by the
  r2 class split (rigidity: nowhere-vanishing derivative; wider class: level-set
  continua that select nothing).

## Remaining open step

Unchanged from r1. The target's first branch (a NAMCG-core functional) needs a weight
on profile space produced by the core: concretely, the pushforward of a core weight
(Euclidean contraction on a compact factor where positive and integrable, per the
integrated state paragraph; or a state supplied by Problem A/E content) under the
block-cut profile map g(X) = block-row variance profile, with log-density non-degenerate
along the ker Sigma_pi directions (by the r2 Lemma 4 dichotomy: relabelling-
non-symmetric, or non-convex with the uniform profile excluded from the minimiser set),
and its stationary locus compared with the Gamma-zero-locus. Even then, the selection
reading and the G missing steps (i)-(iv) remain exactly where the Missing step
paragraph states them. F1 closes no avenue: strictly monotone reparametrisation escapes
are not avenues (extra stationary profiles are continua, s2b); ranked open avenues
unchanged: (1) state-side pushforward (unique route to the missing term, now further
constrained by the completed dichotomy); (2) pi[g] self-consistency (087 R1; outside the
profile-independence hypothesis; any fixed point can only refine the locus to a union
graph, Lemma 2); (3) non-Gaussian slot laws while the frame-averaged coupling remains a
covariance quadratic form (Lemmas 1-2 verbatim).

## Special instructions for the gatekeeper

1. Byte-provenance first: re-run extract_sources_088_r2.py and diff
   scratch/r2fix/block2_corrected.txt / clause_f2.txt against review-r1.md yourself;
   the only deviation from the fenced snippet is the single F3 fold (asserted
   single-count in the build); everything else must be byte-identical.
2. The r1->r2 insert diff is confined to the two mandated regions (the build replaces
   exactly the two marker-located substrings; all other sentences byte-identical to the
   frozen insert-r1.tex). The mathematical core was verified clean in r1 - re-derive
   only the r2 Lemma 3 case split (chain rule, two lines) and the Lemma 4(iv)
   orbit-invariance dichotomy (one-line equivariance), and confirm the s2b exact checks.
3. Re-verify the splice against the PIN, the recomputed POST contract, and the hygiene
   allowlists; re-run every .out with python -I (the frozen r1 .out files must remain
   byte-identical; s2/s3 NOT edited).
4. The bounded no-go must be read exactly class-bounded as worded (Lemma 3(a) class;
   wider class gives continua only); the insert asserts no closure and keeps steps
   (i)-(iv) unchanged. Flag as BLOCKING any integration edit moving Lemma 4 addends
   into the insert or reading them as core content.
5. Do not treat r2 as re-opening avenue (a) or engaging the ch17 G criterion
   (eq:bdy-EE / entropy density / Lambda_eff untouched); no definition, assumption,
   scope statement or status passage is edited; 3(c) full scan not triggered by content.
