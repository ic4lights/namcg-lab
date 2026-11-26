# Proposal 087-g-derivedprofile-selection, round 1

## Result

This package resolves what frame-law choice can and cannot do for profile
selection inside the named coupled gaussian slot law of the appH induced-
coupling block (chain-2 rank-1 edge `G.moments-derivedprofile`, continuation
via 085 review-r1 avenues (a)-(c)). Established: (i) the frame-averaged
decoupling content is exactly a variance, `Gamma = Var_q(g)` under the frame
weights `q_i = ||u_i||^2`, so the uniform profile decouples at every frame and
under every frame law; (ii) for every probability measure `pi` on the frame
sphere the averaged coupling is `E_pi Gamma = g^T Sigma_pi g` with `Sigma_pi`
psd, and its zero locus is exactly the set of profiles constant on the
connected components of the coincidence graph of `pi` - so the Haar result of
the integrated 085 block is the isotropic case, a single-frame measure
recovers the 084 fixed-frame criterion exactly, and **no frame law whatsoever
produces a decoupling locus finer than the uniform profile**: a disconnected
coincidence graph only coarsens the locus to piecewise-constant profiles
(exact example: `g = (3/4, 3/4, 5/2, 5/2)` under the two-block frame average,
`E_pi Gamma = 0` while `D_eff = 338/109 < 4`); (iii) exact closed forms for
the integrated fuzzy proxies: `D_eff/D -> 8/9` with strictly positive
shortfall `-> 1/9` at every cutoff `L >= 2` (proxies strictly off the
uniformity locus), fixed-nu averaged decoupling **fails** at leading order
(`E_u Gamma = nu^2 (L^2/72 + L/36 - 5/48) + O(L^-1)`-remainder positive),
fixed-`W` decoupling `~ W^2/(8 D^2) (1 + 3/(2L) + O(L^-2))` coexists with
off-uniformity; (iv) a stiffness tie `E_pi Gamma >= lam+ W^2 (1/D_eff - 1/D)`
with `lam+` the least nonzero eigenvalue of `Sigma_pi`, strictly positive
exactly in the connected case, and mixtures `((1-eps) delta_{e1} + eps Haar)`
degenerate the stiffness (`lam+ = eps/(D+1)`) **without moving the locus**.
Constraining datum for rank 1: averaged decoupling selects the partition, not
the profile values; any decoupling-based selection mechanism cannot fix
profile values inside the named class. The edge `G.moments-derivedprofile`
stays OPEN and ATTEMPTED-PARTIAL; this package closes nothing (rules 2, 3).

## Target and status

- Problem G (appH, verbatim at L3026-3029): "Status: OPEN. Priority: CRITICAL
  PATH. Completion: PROGRAMME-CONDITIONAL." Missing steps (i)-(iv) at
  L3119-3130 are untouched by this package.
- Chain-2 rank-1 edge `G.moments-derivedprofile` (frontier.yaml
  post-integration-17 note): rank 1 HELD, state attempted-open /
  ATTEMPTED-PARTIAL, continuation via 085 review-r1 ranked avenues (a)
  model-derived non-Haar frame measure, (b) sign-symmetric non-Gaussian slot
  laws, (c) fixed-`W` normalized recovery comparison; avenue (e) rank-3
  `G.moments-finiteV` is the designated fallback.
- This package addresses avenue (a) in full measure-generality *within the
  named slot law* (the classification holds for every frame measure, so the
  matrix model's measure, whatever it is, is covered: its locus is the
  coincidence-graph locus), and avenue (c) in exact closed form. Avenue (b)
  is NOT addressed here (the variance representation is specific to the 084
  coupled gaussian slot law) and remains open; avenue (d) (external SME
  mechanisms, not independently verified) is not touched.
- Discrepancy flags: (1) `make_digest.py --check` printed `DIGEST STALE (head
  changed)` against the dispatch's "DIGEST CURRENT" pin; all targeted reads
  were taken from live appH bytes whose sha256 matches the live pin
  31b345ed..., so nothing relies on the stale digest. (2) The dispatch pinned
  the count of `sets \(W\) and \(g\),` at 5; the live tree count is 4 (the
  shipped and re-run assertion `== 4` passes). (3) The dispatch's POST pin
  744,376 B / d65eb64f... is superseded by a splice defect found this round;
  see "Proposed changes".

## Source reading

digest + targeted reads. Digest status: `DIGEST STALE (head changed)` per
`python scripts/make_digest.py --check` (not regenerated, per dispatch);
navigation done from live bytes of the pinned appH. `chapters/` files were
never read whole. Read in full: `insert-r1.tex` (5,280 B); the six shipped
`.out` evidence files; `simulate_apply_087.py` (in full) and
`simulate_apply_087_fix.py` (authored this round); appH L3026-3029 (G status,
verbatim in Target and status), L3119-3130 (Missing step (i)-(iv)), L3173-
3189 (chain-2 block heads: 079 frame-uniformity L3173, 080 mixed-multiplicity
L3175, 081 charge-to-edge L3177, 082 uniform-minimiser L3179, 083 odd-sector
L3181, 084 induced-coupling L3183, 085 uniformity-locus L3185, Vacuum term
L3187, block closer L3189; long single-line paragraphs were read truncated
to 400 columns per line - full text of the 085 block relied on only for its
tail pin, extracted byte-exactly below). Read `proposals/085-g-moments-
uniformity-locus/review-r1.md` ranked-avenues block (end of its "Scope of
what is established") and `review-r2.md` "Scope of what is established" +
final integration instructions (085 recipe: splice at the Vacuum line-start,
insert bytes plus one CRLF; POST 739,096 / 31b345ed / CRLF 3,836 /
close-idiom 13 confirmed live). `reports/graph/frontier.yaml` grep rows for
`G.moments` (chain-2 notes, post-integration-17 note: rank 1 held, avenues
(a)-(c), fallback (e)). No previous-proposal route was repeated: 085 treated
Haar only; 087 is the measure-general classification the 085 review itself
requested.

## Research and reasoning

Setup. Within the named coupled gaussian slot law of the 084 block (appH
L3183): slots independent complex gaussian with variances s^2 g_i, unit frame
u, slot weights q_i = ||u_i||^2, and the induced coupling mu, Gamma defined
there; profiles g at fixed D and W = sum g_i > 0. A frame law is a
probability measure pi on the unit frame sphere u, assumed independent of the
profile g and of N.

S1 (s1_variance_graph.py; .out dba73a0c). Writing out the 084 definition, the
coupling at a frame is exactly the profile variance under the frame weights:
Gamma = sum q_i g_i^2 - (sum q_i g_i)^2 = Var_q(g) - an algebraic identity in
the slot law (200 exact rational cases checked). Hence Gamma >= 0 at every
frame and Gamma = 0 iff g is constant on supp(q) - the uniform profile
therefore decouples at every frame under every law, a profile-only fact
(law- and measure-free). Averaging over pi, E_pi Gamma = g^T Sigma_pi g with
Sigma_pi = E_pi(diag(q) - q q^T) psd and Sigma_pi 1 = 0; the zero-averaged-
locus is the nullspace of Sigma_pi. Claim (established; proof): g is in the
nullspace iff g is constant on the connected components of the coincidence
graph G(pi) on the slots with edge ij whenever pi(q_i q_j > 0) > 0. Sketch:
E_pi Gamma = 0 with Gamma >= 0 at every frame forces Gamma = 0 for pi-a.e.
frame; Gamma = Var_q(g) = 0 holds at a frame iff g is constant on supp(q); so
g_i = g_j for pi-a.e. frame with q_i q_j > 0, i.e. on every coincidence edge
(a positive-measure event), and connectivity propagates constancy; the
converse (constancy on components gives E_pi Gamma = 0) is immediate. Verified: nullspace ==
span{1_C} in 60 random exact finite-support rational cases; locus probes
(E_pi Gamma = 0 iff piecewise-constant on components) in 360 exact cases.
At pi = delta_u (single frame) the coincidence graph is the support clique of
u, so the locus is constancy of g on supp(u) - exactly the 084 fixed-frame
criterion (recovered iff, not merely contained). This is avenue (a) answered
in full measure-generality inside the named law: whichever frame measure the
matrix model supplies, its decoupling locus is its coincidence-graph locus;
connected case -> uniform only; disconnected -> a coarsening to
piecewise-constant profiles, never a refinement.

S2 (s2_haar_stiffness.py; .out 70abf974). For Haar pi the frame covariance is
exactly Sigma_Haar = (I - J/D)/(D+1) (J all-ones): exact matrix computation
D = 2..8 and symbolic check of the quadratic form against the integrated 085
identity g^T Sigma g = (D sum g_i^2 - W^2)/(D(D+1)); spectrum {0, (D+1)^-1
(mult. D-1)}. The 085 Haar-only statement is thus the isotropic member of the
S1 classification. Mixtures (1-eps) delta_{e1} + eps Haar give Sigma =
eps (I - J/D)/(D+1) exactly (eps = 1/1000, D = 3,4,5): the stiffness lambda+
= eps/(D+1) degenerates as eps -> 0 while the locus stays the single uniform
profile for every eps > 0 - stiffness and locus are independent data, so no
"make the measure nearly deterministic" limit moves the locus. Universal per-
frame upper bounds: Var_q(g) <= (max_i g_i - min_i g_i)^2 / 4 (Popoviciu) and
Var_q(g) <= ||g - c 1||^2 / 2 for any constant c, 4000 random exact cases,
worst sampled ratio 1/2 attained at half-half weights.

S3 (s3_proxy_closedforms.py; .out e5a483ee). For the integrated fuzzy
variance proxies f = nu l/2 of the 081 block at cutoff l_c = L with slot
count D = L(L+2), the profile data are exactly rational: W = L(L+1)(4L+5)/12,
sum g_i^2 = L(L+1)(3L^2+5L+1)/24 (exact for L = 1..20 by sympy rational
check), so D_eff = W^2 / sum g_i^2 = L(L+1)(4L+5)^2 / (6(3L^2+5L+1)) and
1 - D_eff/D = (2L^3 + 10L^2 + L - 13)/(18L^3 + 66L^2 + 66L + 12), strictly
positive for every L >= 2 with limit 1/9: the proxies are strictly off the
uniformity locus at every cutoff, and D_eff/D -> 8/9 - the 8/9 limit of the
085 review's numerical ramp is here an exact closed-form consequence. Frame-
averaged (Haar, i.e. isotropic Sigma) coupling in closed form: E_u Gamma =
nu^2 L(L-1)(2L^2+12L+13)/(144(L+1)(L+2)) exactly, with exact decomposition
E_u Gamma = nu^2 (L^2/72 + L/36 - 5/48) + (24L+30) nu^2/(144(L+1)(L+2)),
remainder positive - at fixed nu the averaged coupling GROWS as nu^2 L^2/72:
fixed-nu averaged decoupling fails at leading order (avenue (c) answered in
the unfavorable direction for that normalization). At fixed W, E_u Gamma =
W^2 (2L^3+10L^2+L-13)/(L(L+1)^3(L+2)(4L+5)^2) = W^2/(8D^2) x (1 + 3/(2L) +
O(L^-2)), the closed-form correction to D^2 E_u Gamma / W^2 - 1/8 being
(24L^4 - 25L^3 - 299L^2 - 323L - 25)/(8(L+1)^3 (4L+5)^2), strictly positive
from L = 5 on (negative at L = 2,3,4), with L x (relative correction) -> 3/2
exactly: fixed-W averaged decoupling and a strictly off-uniform limit
COEXIST at leading order - a sequence can decouple on average in the fixed-W
normalization while keeping 1 - D_eff/D -> 1/9 > 0, so averaged decoupling at
fixed W carries no locus information. Cross-checks against shipped material:
fixed-nu ramp 23.233/91.009/359.9/1431 at L = 40/80/160/320 (rel. dev. <
2e-3) matches the ramp shipped in the 085 gatekeeper pass; fixed-W ramp
4.57e-8 / 1.18e-11 at L = 40/320 likewise; D_eff reproduces the integrated
L3177 numerals 1488 (L = 40) and 23017 (L = 160), and 1/D_eff = 6.720e-04 /
4.345e-05 against the integrated 6.7e-4 / 4.3e-5 - no new numerals enter the
manuscript that are not derivable from the shipped scripts.

S4 (s4_selection_content.py; .out 53fcf550). The selection content of the
classification, exactly: (1) off-uniform averaged decoupling exists - g =
(3/4, 3/4, 5/2, 5/2) with pi the two-block frame average (frames supported in
the first pair and frames supported in the second pair) gives E_pi Gamma = 0
exactly while D_eff = 338/109 < D = 4: averaged decoupling selects the
PARTITION, not the profile values - the key constraining datum, any
decoupling-based selection mechanism cannot fix profile values inside the
named class; (2) uniform profile: Gamma = 0 at every frame and under every
measure (profile-only, law- and measure-free); (3) stiffness tie: for
connected coincidence graph, E_pi Gamma = g^T Sigma_pi g >= lambda+ ||g - c
1||^2 = lambda+ W^2 (1/D_eff - 1/D), exact in 40 random connected exact
cases - decoupling rate under a fixed frame law forces D_eff toward D with a
measure-dependent stiffness lambda+, quantitative form of the 085
"recovery strictly weaker" statement.

Positioning for rank 1 (what this does and does not do). DOES: extends the
085 Haar-locus theorem to every frame law (coincidence-graph classification),
so avenue (a) is decided within its hypothesis class - a model-supplied frame
measure cannot refine the decoupling locus below uniformity; converts avenue
(c) into exact asymptotics in both normalizations; supplies the exact datum
that decoupling-based selection selects partitions, not profile values; and
supplies the stiffness inequality tying averaged decoupling to effective-
dimension recovery. DOES NOT: derive or select any profile; supply the state
that sets W, g, s or the frame u (still an input the repository does not
provide); touch G missing steps (i)-(iv); address the non-Gaussian slot-law
relaxation (avenue (b)) or the finite-V sector (avenue (e)); close or narrow
any status label. Relaxations the no-go-style datum does NOT rule out (ranked
forks, each with its hypothesis stated): (R1) frame laws DEPENDENT on the
profile or state - the classification assumes pi independent of g and N, a
matrix-model frame measure varying with the state escapes it; (R2) other slot
laws (avenue (b)): the variance representation Gamma = Var_q(g) is specific
to the 084 coupled gaussian law, so the classification binds only there; (R3)
selection functionals other than averaged decoupling whose integrand zero-set
is not the piecewise-constant-on-components set (the classification covers
every requirement with that zero structure, by the same nullspace argument);
(R4) external profile mechanisms (avenue (d), not independently verified).
Escape-wording test for the gatekeeper: the manuscript text proposed below
says the decoupling requirement "is measure-blind as a selector" and that
selection "must come from the state that sets W, g, s and the frame" - both
are claims inside the named class plus the repository-state observation, not
a closure of G.moments-derivedprofile, which stays OPEN/ATTEMPTED-PARTIAL.

## Claim classification

- Gamma = Var_q(g) at every frame; uniform profile Gamma = 0 law- and
  measure-free; per-frame upper bounds Popoviciu and half-squared-norm:
  established identities/derivations (inside the 084 named coupled gaussian
  slot law for the representation; the bounds are pure probability once the
  representation holds).
- Coincidence-graph zero-locus classification of E_pi Gamma = 0 for every
  frame law pi; single-frame specialization recovering the 084 fixed-frame
  criterion iff: established derivation (proof sketch given above; exact
  finite-support case-verification; the general-measure step is the standard
  nonnegative-integrand argument, no measurability pathology at finite D).
- Sigma_Haar = (I - J/D)/(D+1) and equality with the integrated 085 identity;
  mixture degeneracy lam+ = eps/(D+1) with fixed locus; stiffness tie
  E_pi Gamma >= lam+ W^2 (1/D_eff - 1/D): established derivations (exact
  symbolic/rational verification as logged).
- Closed proxy forms W, sum g_i^2, D_eff, 1 - D_eff/D > 0 for L >= 2, limit
  8/9, fixed-nu growth nu^2 L^2/72 with positive remainder, fixed-W
  W^2/(8D^2)(1 + 3/(2L) + O(L^-2)) with closed correction positive from
  L = 5: established rational identities conditional on the named proxy
  convention f = nu l/2, D = L(L+2) of the 081 block.
- Off-uniform example g = (3/4,3/4,5/2,5/2), E_pi Gamma = 0, D_eff = 338/109
  < 4: established exact example.
- "Averaged decoupling selects the partition, not the profile values";
  "decoupling is measure-blind as a selector; selection must come from the
  state input": established consequence inside the named class + named-
  independence hypothesis; the "state that sets W, g, s, the frame" clause is
  the repository-state observation (unresolved input), not a derivation.
- Ramp matches to shipped 085-gatekeeper numerals and to integrated L3177
  numerals: consistency checks (established numerically, rel. dev. logged);
  the shipped ramp values are not manuscript content and stay out of the
  insert.
- Avenue (b) non-Gaussian extension, avenue (d) external mechanisms, profile
  dependence of pi (R1): unresolved / not addressed - explicitly conjecture-
  or-mechanism territory, kept out of the manuscript text except as the
  disclaimers the insert carries.

## Proposed changes

One file, one insertion: `chapters/appH-microscopic-proofs.tex`. Nothing
else in the repository changes (no bib entries; the insert cites nothing: no
\cite, \ref, \eqref or \label in it - hygiene-verified; no labels to check).
No equations of existing paragraphs are modified; the insert is a new
\emph-headed block in the chain-2 (G moment) sequence, between the integrated
085 block (L3185) and the G-side "\emph{Vacuum term.}" (L3187).

Anchor (unique, full-085-closer tail pin, byte-exact):
"they do not fix the state that sets \(W\), \(g\), \(s\) or the frame
\(u\), leave the missing steps (i)-(iv) of the Missing step paragraph
unchanged, and they close nothing in Problem~G." - count 1 in the live tree
(re-verified by re-run this round). NEVER anchor on the short suffix "do not
fix the state that sets" (count 6) or the variant "sets \(W\) and \(g\),"
(count 4; the dispatch's note said 5 - the live count is 4, assertion
reproduced). The block is spliced at the LINE-START of the G-side
"\emph{Vacuum term.}": d[:j] ends in the gap CRLFCRLF (085 line + blank line
L3186), then insert bytes (5,280 B, content + terminal CRLF, single content
line) plus one CRLF (2 bytes, the new blank line), then the Vacuum line -
byte-for-byte the 085 review-r2 integration recipe ("insert bytes plus one
CRLF immediately before the line-start \emph{Vacuum term.}", which for 085
gave added 3,399 + 2 = 3,401 B and CRLF +2: same arithmetic here).

SPLICE DEFECT IN THE SHIPPED SIMULATOR (found this round; shipped file kept
unmodified for the audit trail): the dead-pass simulate_apply_087.py splices
at i = right after the PIN, i.e. BEFORE the CRLFCRLF gap - the new block then
shares physical line L3185 with the 085 block (boundary probe
"...Problem~G.\emp" confirms), with no blank line before it: LaTeX would
render it INSIDE the 085 paragraph, against the blank-line-separated block
convention of every chain-2 entry (081-085). Its stdout reproduced
byte-identically on re-run (it is deterministic), but its POST contract 744,
376 B / d65eb64f... must NOT be used - it encodes the wrong splice; the
dispatch's POST pin repeats that superseded number. Authoritative script:
simulate_apply_087_fix.py (added this round; exit 0, asserts all pins and all
four boundary probes pass).

BYTE CONTRACT (authoritative, from simulate_apply_087_fix.py re-run this
round). PRE: 739,096 B / sha256 31b345ed5e957910bacd3c02ebae87edfbeb5f0effa77
c98149f6eafc2a2679d / CRLF 3,836 / bareLF 0 (live, re-verified). Insert:
insert-r1.tex, 5,280 B / sha8 3fc233c9, regenerated byte-identically by
build_insert_087.py. POST: **744,378 B / sha256 38db6497530b15663f6d206912df
ce0e59662941eb1dc3d46912ae7d43d640bd / CRLF 3,838 / bareLF 0 / close-idiom
count 14 (was 13, +1) / new header "Measure dependence of the frame-averaged
decoupling locus" count 1 / \emph{Vacuum term.} count 2 unchanged**; POST
size = PRE + 5,280 + 2. Boundary invariants the script asserts: PIN followed
by CRLFCRLF (085 separation kept); CRLFCRLF immediately before the new header;
CRLFCRLF + Vacuum after the insert. After integration: run
python scripts/build_check.py (insert adds no macros, no refs: build risk
nil, build mandatory) and refresh the digest.

## Verification scripts and reproduction pack

All scripts under proposals/087-g-derivedprofile-selection/, run from the
repository root as `python -I proposals/087-g-derivedprofile-selection/<name>`
(each opens appH read-only in 'rb'; no script writes to chapters/; the two
simulators print and assert only). All six shipped scripts were re-run this
round with stdout byte-identical to the shipped .out (dispatch sha8 pins
re-measured, all match; appH sha unchanged before/after all runs).

- build_insert_087.py - regenerates insert-r1.tex; re-run reproduces 5,280 B
  / sha8 3fc233c9. Invariant: prints "insert bytes 5280".
- s1_variance_graph.py / .out (dba73a0c) - variance identity (200 exact
  cases), nullspace-vs-span{1_C} check (60 exact cases), zero-locus probes
  (360), delta_u specialization. Invariants: four "OK" lines + "S1 DONE".
- s2_haar_stiffness.py / .out (70abf974) - Dirichlet(1) moments (symbolic
  beta integral D=2,3,4), Sigma_Haar exact D=2..8 + symbolic quadratic-form
  match to the 085 identity, mixture degeneracy (eps=1/1000, D=3,4,5),
  universal variance bounds (4000 cases, worst ratio 0.5). Invariants: "S2
  DONE"; lam+ = eps/(D+1).
- s3_proxy_closedforms.py / .out (e5a483ee) - exact rational proxy sums
  (L=1..20), D_eff and shortfall formulas (positivity for L>=2, limit 1/9),
  fixed-nu decomposition (leading L^2/72), fixed-W form with closed
  correction (positive from L=5), shipped-ramp cross-checks, integrated L3177
  numerals 1488/23017 and 6.720e-04/4.345e-05 vs integrated 6.7e-4/4.3e-5.
  Invariants: "strictly positive for L >= 2"; leading term L^2/72; "S3 DONE".
- s4_selection_content.py / .out (53fcf550) - exact off-uniform example with
  E_pi Gamma = 0 and D_eff = 338/109; uniform-profile identity; stiffness tie
  (40 exact connected cases). Invariants: "E_pi Gamma = 0 exactly", "S4 DONE".
- hygiene_087.py / .out (f8a7016a) - insert-r1.tex hygiene: single content
  line + terminal CRLF, no control bytes, UTF-8 no BOM, no $ [ ] \cite \ref
  \eqref \label, no status/priority/completion/open/critical/programme/
  derived words, exactly one \emph header, header unique across chapters/,
  brace/paren balance, ends with the close idiom, every numeral inside a
  derivable allowlist. Overall PASS, 5,280 B.
- simulate_apply_087.py / .out (b1e2855a) - SHIPPED SPLICE DEFECTIVE (same-
  line splice; see Proposed changes); stdout reproduced byte-identical on
  re-run; its POST (744,376 / d65eb64f) is DEAD - do not integrate against it.
- simulate_apply_087_fix.py / .out (added this round) - authoritative splice:
  asserts PRE pins, PIN count 1, short-suffix count 6, variant count 4,
  Vacuum count 2, close-idiom count 13, gap CRLFCRLF, G-side VT is next VT
  after the pin, insert shape (starts with \emph{, exactly one CRLF at end);
  invariants: POST 744,378 B / sha256 38db6497530b15663f6d206912dfce0e5966
  2941eb1dc3d46912ae7d43d640bd / CRLF 3,838 / bareLF 0 / close-idiom 14 /
  header 1 / Vacuum 2; boundary probes print CRLFCRLF at all three joints;
  ends "no write performed".

## Decisions Taken

1. POST d65eb64f SUPERSEDED (routine, presentation/contract choice; favors
   derivability): replaced the dead-pass same-line splice with the 085-recipe
   Vacuum-line-start splice after verifying the chain-2 blank-line block
   convention byte-by-byte (085 arithmetic: 3,399 + 2 = 3,401, CRLF +2).
   Rejected alternatives: (i) keep the shipped splice - would render inside
   the 085 paragraph, a visible manuscript defect the gatekeeper would (and
   should) reject; (ii) splice after the gap with a different blank-line
   count - breaks the uniform one-blank-line convention.
2. Kept the shipped simulate_apply_087.py untouched and added
   simulate_apply_087_fix.py rather than editing the shipped file, so the
   audit trail of the dead pass survives; the manifest marks the fix script
   authoritative.
3. Classified the coincidence-graph classification as established (proof
   given) rather than "numerically verified" - the general-measure case
   follows from the nonnegativity argument at finite D; case checks are
   corroboration, not the argument.
4. Kept the shipped-ramp numerals (085 gatekeeper pass) and the exact
   6.720e-04/4.345e-05 values OUT of the insert (rule 7: they are cross-
   checks here; the insert's numerals are the closed forms, the exact example
   values, and the integrated L3177 numerals it reproduces).
5. Named avenues (a)/(c) as addressed and (b)/(d) as not, rather than
   claiming the whole avenue list, because the variance representation is
   specific to the 084 gaussian slot law.

## Milestone assessment

Routine. No M1-M5 trigger: no critical-path step derived from the matrix
theory; no missing link closed without new inputs; no scope or label change;
the package constrains (and honestly narrows) one selection route inside its
hypothesis class. Not BREAKTHROUGH.

## Status-label recommendation

Re-derived the applicable critical-path set from ch17-agenda + Appendix H +
ledger/frontier (post-INTEGRATION-17): A, B, C, D1, E, F, G-derived, N open
in the full-GR / matrix-derived scope; Problem G OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL (appH L3026-3029, quoted); chain-2 rank-1 edge
`G.moments-derivedprofile` attempted-open / ATTEMPTED-PARTIAL. ALL LABELS
UNCHANGED by this package (rule 2: no label edits proposed; the insert
carries no status language - hygiene-verified). Recommend the frontier edge
state stay attempted-open / ATTEMPTED-PARTIAL (integrator note, not a
manuscript label): avenue (a) now decided within its hypothesis class, (c)
closed in both normalizations; (b), (d), (e) and relaxation R1 (state-
dependent frame law) remain open leads.

## Author decision needed

None. (Nothing here changes the NAMCG core, Chapter 17 scope, the critical-
path set, or any status/completion label; spacetime stays emergent - the
frame-sphere measure is a statistical object of the edge-data model, not a
background structure.)

## Remaining open step

What would still be needed to close the original target (rank-1 edge
`G.moments-derivedprofile`, i.e. a DERIVED profile/state fixing W, g, s, and
the frame, and thereby make rho_p, D_eff and the couplings outputs):
(1) a matrix-model-supplied state or selection principle producing the slot
profile g and the frame u - not supplied by anything in the repository, and
this package proves it cannot be replaced by any profile-independent frame
average of the decoupling criterion inside the named law; (2) the avenue (b)
extension: whether a sign-symmetric non-Gaussian slot law admits a coupling
whose averaged zero-locus is finer than the coincidence-graph locus (the
variance representation fails there, so the classification need not bind);
(3) the R1 relaxation: a state-dependent frame law pi[g] escaping the
independence hypothesis; (4) the rank-3 fallback `G.moments-finiteV`
(avenue (e)) if in-class avenues (b)/(R1) are exhausted; (5) for Problem G
as such, unchanged missing steps (i)-(iv) (appH L3119-3130). This package
changes none of these statuses; it removes one route (frame-law selection)
from the search space inside its hypothesis class and sharpens the shape of
any surviving route.

## Special instructions for the gatekeeper

1. Scope limits of the insert text: everything is for the named coupled
   gaussian slot law of the 084 block at fixed D and W, frame laws
   independent of the profile and of N; closed proxy forms carry the named
   f = nu l/2, D = L(L+2) convention. Do not let it be read as slot-law-
   general or as a closure of anything: the final sentence is a scoped
   disclaimer and must be kept verbatim.
2. Do NOT integrate against the shipped simulate_apply_087.py output (POST
   744,376 / d65eb64f): it encodes the same-line splice defect (reproduced,
   documented, boundary probe "...Problem~G.\emp"). Integrate against
   simulate_apply_087_fix.py (POST 744,378 / 38db6497... / CRLF 3,838).
   Re-pin before splicing: if the tree moved, recompute; the full-085-closer
   tail pin must count 1, and the G-side Vacuum term must be the next
   \emph{Vacuum term.} after the pin with gap CRLFCRLF.
3. Re-check items: the S1 nullspace argument (the short proof above is the
   intended argument; the insert states the classification without proof,
   as the block's other entries do); the Haar covariance and the 085-identity
   match (s2); the s3 positivity of 2L^3+10L^2+L-13 for L>=2 and of the
   fixed-W closed correction from L=5 (signs are the live risk); the exact
   s4 example (hand-check re-verified this round against the script: W =
   3/4+3/4+5/2+5/2 = 13/2, W^2 = 169/4, sum g_i^2 = 2*9/16+2*25/4 = 109/8,
   D_eff = W^2/sum g_i^2 = (169/4)(8/109) = 338/109 = 3.1009... < 4; the
   E_pi Gamma = 0 holds by the s1 component-constancy criterion - g is
   constant on each of the two blocks; D_eff is the 081-block definition
   W^2/sum g_i^2, the same one used in the s3 proxy formulas).
4. Must not be asserted from this package: profile derivation or selection;
   closure or narrowing of G.moments-derivedprofile or Problem G; any slot-
   law-generality of the variance representation; any claim about the true
   matrix-model frame measure beyond "whatever it is, its locus is its
   coincidence-graph locus, inside the named law".
5. Hygiene: run hygiene_087.py; its allowlist of numerals and the no-status-
   word scan are part of the contract (rule 2 compliance in manuscript text).
