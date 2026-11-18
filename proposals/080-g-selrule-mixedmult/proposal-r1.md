# Proposal 080-g-selrule-mixedmult, round 1

## Result

For q = q_1+...+q_s coincident copies of a compact factor grouped into s blocks, block-scalar
pencil data H = (+)_f h_f 1_{q_f}, K = (+)_f n_f 1_{q_f} with n_f > 0 realize, exactly and for
every q and N >= 2, a mixed-multiplicity nonzero spectrum: the multiset union of q_f copies of
the Row length pair at (h_f, n_f), with per-factor involution lambda |-> -4 n_f / lambda, per-factor
row length 2 n_f^{1/2} and per-factor pair splitting 4 (h_f^2 + n_f)^{1/2}. This is the exact
general-q spectrum of the integrated equalized paragraph (appH L3171) extended from uniform depth
to per-factor depths, and it is realized at the data level by an explicit edge-row block
R = U(A + iH) + V K^{1/2}, escaping the per-copy-invariance negation of the integrated
selection-rule paragraph (L3167) exactly at its hypothesis (invariance across the whole copy
space relaxed to invariance within each factor block). At q = 2 the exact double-pair criterion
of L3169 is recovered on the positive-Gram locus: the two quartic-coefficient conditions
8c = a(4b - a^2) and 64d = (4b - a^2)^2 hold jointly iff h_1 = h_2 and n_1 = n_2 for n_f > 0
(the second factors as 1024 n_1 n_2 - 256((h_1 - h_2)^2 + n_1 + n_2)^2), with the spurious
algebraic branch n_f = -h_f^2 excluded by K >= 0. At h_f = 0 the mixed-to-multiplicity-1 moment
ratio equals 1 + rho_p with the integrated signature-excess formula rho_p = sum_f (q_f - 1) n_f^p /
sum_f n_f^p (9/17 at p = 1, 81/145 at p = 2 at (q_1,q_2) = (2,1), (n_1,n_2) = (1/4, 2/9), and 1 at
equal depths - exact rational arithmetic), and at h_f != 0 the same ratio holds exactly with pair
2p-moments 8(2h_f^2 + n_f) and 32(8h_f^4 + 8h_f^2 n_f + n_f^2) as weights. The package closes
nothing: it is a class of exact spectra and criteria within the rank-one edge-datum family, at
fixed depths only.

## Target and status

- Frontier edge: `G.selrule-mixedmult` (chain 2, rank 1, state untried in
  reports/graph/frontier.yaml): mixed-multiplicity per-factor-depth spectra beyond the uniform-q
  classes of the integrated selection-rule, state-realization and equalized-spectrum paragraphs.
- Manuscript target: Problem G (appH sec:status-G): status OPEN, priority CRITICAL PATH,
  completion classification PROGRAMME-CONDITIONAL, missing steps (i)-(iv) at appH L3119-3130;
  Chapter 17 criterion at ch17-agenda.tex L474-495. This proposal adds no closure: it supplies
  the per-factor-depth spectral input the frontier asked for, inside the fixed-depth regime.
- Dependency respected: the avenue-(3) constraint inherited from
  proposals/076-g-edge-uqstack-selrule/review-r1.md "Ranked avenues for the next researcher
  round" (L45, unchanged in review-r2.md L32): the fixed-q leading-order validity condition -
  any statement tying q to N-scaling must respect it. I treat it in two ways: the algebra is
  stated as exact for every fixed q, and the selection-rule reading (multiplicity = equal rows)
  is asserted only at fixed depths q_f, explicitly leaving depths growing with N untreated.
  grep confirmed the fixed-q condition text is NOT in the integrated manuscript, so the insert
  states the proviso as its own scope clause rather than quoting an absent passage.
- Not touched: 079's separate open edges (two-sided diagrams, minimisation over frames); the
  two-sided +/- reading; the typicality question; the general (H, K) criterion at q > 2.
- DERIVED vs PROGRAMME-CONDITIONAL: everything here is within the rank-one edge-datum family of
  the transplanted selection rule's reading class, i.e. programme-conditional evidence for G;
  nothing is a derivation of the selection rule or of G.

## Source reading

digest + targeted reads. scratch/digest.md: DIGEST CURRENT, head d8b29f8, tree-hash 5d7c72483689650b,
dirty-chapters: yes (078 and 079 integrated but uncommitted on local/gpu - the PRE pins below
match the working tree, not HEAD). Read in full: appH L3022-3181 (Problem G ledger, status,
missing step, and the whole 065-evidence block L3153-3177); ch17-agenda.tex L470-499;
proposals/078-g-selrule-imalpha/review-r1.md (ACCEPT; the relaxation clause "any relaxation -
q-dependent K, non-tensor-product U, or K != nI - is outside its hypotheses and remains open" is
the licence for this package); proposals/079-g-frameavg-residual/review-r1.md (ACCEPT; PRE/POST
byte contract for appH = current pins; open-list: two-sided diagrams and minimisation over
frames stay separate); proposals/076-g-edge-uqstack-selrule/review-r1.md L45 (avenues (1)-(6)
verbatim); proposals/077-g-selrule-copyinv/review-r2.md L47 (names mixed-multiplicity
per-factor-depth spectra as the target); reports/graph/frontier.yaml G.selrule-mixedmult row and
chain-2 notes; reports/sme-scout-20261117-1309.md Edge-3 lines. No unreadable files.

## Research and reasoning

1. Reused lemma (established, integrated appH L3171, from 078): for the pencil
   T = -2i([[C0^dag, Z0], [-1_q, -C0]]) of the rank-one edge-datum family, for every q
   det(lambda I_2q - T) = det(lambda^2 I_q + 4 lambda H - 4 K) with H = Im C0 and
   K = Z0 - C0^dag C0 = R^dag(1 - U U^dag)R >= 0; Re C0 is invisible. Used verbatim, not
   reproved.
2. New derivation. Take H and K block-scalar over a partition q = q_1 + ... + q_s:
   H = (+)_f h_f 1_{q_f}, K = (+)_f n_f 1_{q_f}, n_f > 0. Then
   lambda^2 I_q + 4 lambda H - 4 K = (+)_f (lambda^2 + 4 lambda h_f - 4 n_f) 1_{q_f}, a block
   diagonal matrix of scalars, so its determinant is prod_f (lambda^2 + 4 lambda h_f - 4 n_f)^{q_f}
   exactly (block-diagonal determinant; no commutativity or genericity hypothesis). Symbolically
   checked in s1-A for q = 2 partitions (1,1), (2) and q = 3 partition (2,1), including the full
   2q x 2q pencil determinant with general real Re C0 entering C0 and Z0 = K + C0^dag C0.
3. Roots. lambda^2 + 4 h_f lambda - 4 n_f = 0 gives lambda = -2 h_f +- 2 (h_f^2 + n_f)^{1/2}
   (real, opposite signs since the constant term -4 n_f < 0), each with multiplicity q_f. The
   two roots of factor f have product -4 n_f, hence the per-factor involution
   lambda |-> -4 n_f / lambda, the block-scalar case of the 078 involution with per-factor depth.
   The pair formula with (Im alpha, ||w_perp||^2) = (h_f, n_f) matches the Row length paragraph
   of the integrated text; the per-factor row length is 2 n_f^{1/2} and the pair splitting
   4 (h_f^2 + n_f)^{1/2}.
4. Realizability (data-level, s1-B). Given any partition, any (h_f, n_f) with n_f > 0, any
   Hermitian A and any isometry u in C^N with N >= 2: build the qN x q isometry U = 1_q (x) u
   and a qN x q isometry V with U^dag V = 0 (QR of a random 2q-column block, then Gram-Schmidt
   against col U; possible since qN - q >= q for N >= 2). Set C0 = A + iH and
   R = U C0 + V K^{1/2}. Then U^dag R = C0; R^dag R = C0^dag C0 + K (cross terms vanish:
   U^dag V = 0), so Z0 = R^dag R holds with the target K; and
   R^dag(1 - U U^dag)R = K^{1/2} V^dag V K^{1/2} = K. So the edge datum realizes exactly the
   target (H, K). The full charge Q~ = -2i(U R^dag - R U^dag) then has, by steps 1-2, the mixed
   spectrum. Numerically: 96 cases over partitions (1,1), (2), (2,1), (3), (2,2), (3,1), (4,1),
   (3,2) and N = 2, 3, 5, 8: rank(Q~) = 2q always, spectra agree with the pair formula to
   8.9e-15 and with the involution image to 1.4e-14. This is a construction, not typicality:
   077 (appH L3169) showed exact spectral structure is not typical in iid Gaussians.
5. Escape of the 076 negation. The integrated L3167 paragraph proves that, for tensor-product
   lifts with momenta copy-invariant across the whole copy space, all nonzero eigenvalues have
   multiplicity exactly q (uniform depth) and, in the product testbed, the per-factor stacked
   diagram (l_1^{q_1}, l_2^{q_2}) with q_1 != q_2 is never read from the multiplicity. Its
   hypothesis is invariance under all copy permutations; steps 2-4 keep only invariance within
   each factor block, and the resulting charge spectrum has genuinely mixed depth. So the
   negation does not extend to this subclass; the missing input named by the frontier (a charge
   spectrum whose multiplicity structure is per-factor) is realized, at fixed depths, by explicit
   edge blocks.
6. q = 2 criterion (s2). A real monic quartic lambda^4 + a lambda^3 + b lambda^2 + c lambda + d
   is a perfect square of a real monic quadratic iff 8c = a(4b - a^2) and 64d = (4b - a^2)^2:
   matching coefficients of (lambda^2 + s lambda + t)^2 forces s = a/2, t = (4b - a^2)/8, and the
   remaining two coefficients give the conditions (s2-A substitution identity; gcd 1 so these are
   the full locus). On block-diagonal data the quartic is the product of the two factor
   quadratics with A1 = 4(h_1 + h_2), B1 = 16 h_1 h_2 - 4(n_1 + n_2),
   C1 = -16(h_1 n_2 + h_2 n_1), D1 = 16 n_1 n_2, and the exact identity
   4 B1 - A1^2 = -16((h_1 - h_2)^2 + n_1 + n_2) (s2-B-prime) makes the double-pair sign condition
   4b - a^2 < 0 automatic when n_f > 0. Condition 2 factors as
   -256[ ((h_1 - h_2)^2 + n_1 + n_2)^2 - 4 n_1 n_2 ]; for n_1, n_2 > 0 this vanishes iff
   (h_1 - h_2)^2 + n_1 + n_2 = 2 (n_1 n_2)^{1/2}, i.e. (h_1 - h_2)^2 + (n_1^{1/2} - n_2^{1/2})^2
   = 0, i.e. h_1 = h_2 and n_1 = n_2; condition 1 = 64(h_1 - h_2)(h_1^2 - h_2^2 + n_1 - n_2)
   vanishes as well there, and coincidence implies both conditions directly. Exact-rational
   sampling: 200 random positive-rational tuples, 0 off-locus hits; 30/30 on-locus passes.
   Outside n_f > 0 there is a second algebraic branch n_f = -h_f^2 (substituting it makes both
   conditions vanish identically); it has K not positive semidefinite except at the excluded
   boundary K = 0, so the reduction to the L3169 criterion is asserted only on the positive-Gram
   locus - which is the honest scope, since data coming from R satisfy K = R^dag(1 - UU^dag)R >= 0
   automatically. Separation from double roots: the 078 example (rows (3,7), (5,11), quartic
   (lambda-2)^2 (lambda+14)(lambda+22)) gives condition values 2560 and -45056 (both nonzero),
   confirming at coefficient level that a double root need not be a double pair; and 0 of 2000
   random general (H, K) q = 2 pencil samples meet both conditions.
7. Moment excess (s3). The pair 2p-moments are S_1(h,n) = 8(2h^2 + n) and
   S_2(h,n) = 32(8h^4 + 8h^2 n + n^2) (symbolic, s3-A); at h = 0, S_p = 2 (4n)^p. Hence the
   mixed-multiplicity spectrum moment sum_j e_j^{2p} = sum_f q_f S_p(h_f, n_f) and the
   multiplicity-1 moment = sum_f S_p(h_f, n_f), so (mixed - 1)/1 = sum_f (q_f - 1) S_p /
   sum_f S_p exactly; at h = 0 with w_f = n_f this is the integrated rho_p formula of L3167, and
   at (q_1, q_2) = (2,1), (n_1, n_2) = (1/4, 2/9) it gives exactly 9/17 (p = 1), 81/145 (p = 2),
   and 1 at equal depths (exact Fraction arithmetic; the numbers match the integrated text, which
   is the consistency the frontier asked for). Verified from full charge spectra at general h_f
   to 4.1e-15 (s3-C). This is an identity of moment signatures only: the mixed-multiplicity charge
   spectrum carries exactly the stacked-versus-multiplicity-1 excess; it is not a selection claim.
8. Diagnostics (s3-B). With the relative gap D = max_{k=1,2}(e_{kq} - e_{(k-1)q+1})/max_j|e_j| of
   L3169: on the mixed class D = 0 iff all pair data (h_f, n_f) coincide - at genuine mismatch the
   multiset of lower (resp. upper) pair elements of the extreme pair has total multiplicity < q,
   so one of the two defining gaps is strictly positive (pigeonhole; numerically equal-data
   D <= 1.44e-15, mixed-data D >= 9.554e-2 over 40 samples) - so non-uniform per-factor depth is
   visible in the spectrum at leading order. The fourth-moment excess
   U_2 = Tr Q~^4 / (2q (Tr Q~^2 / 2q)^2) - 1 >= 0 by Cauchy-Schwarz on the 2q nonzero eigenvalues,
   vanishing exactly when all moduli are equal (as L3169 states); on the mixed samples
   min U_2 = 0.30.
9. Fixed-q scope. The factorization and spectrum are exact algebra for every fixed q and N >= 2;
   the multiplicity-as-rows reading is asserted only at fixed depths q_f, consistent with the
   fixed-depth proviso of the integrated stacked-rows and selection-rule paragraphs, and the
   insert states that depths growing with N are untreated. No number or statement in the package
   ties q to N-scaling.
10. Literature. No new citation is imported. The SME scout Edge-3 (saturation /
   Littlewood-Richardson filtering of Kronecker spectra, Knutson-Tao line) was weighed and not
   used: it constrains spectra of product-type (tensor-product) operators, while the present
   class is not product-type (its escape is exactly the failure of copy-space invariance), and
   the scout records (N6) that there is no constructive Kronecker eigenvalue-statistics
   literature to import. The Knutson-Tao records cited by the scout were not independently
   verified by me; they are marked not independently verified and appear nowhere in the insert.

## Claim classification

- det(lambda I - T) = det(lambda^2 I + 4 lambda H - 4 K) and Re C0 invisibility: established,
  integrated (078), reused as a lemma.
- prod_f factorization, mixed spectrum, per-factor involution / length / splitting: established
  (exact block-diagonal determinant; symbolic s1-A, full-size numeric s1-B).
- Realizability of every block-scalar datum by explicit R at every q, N >= 2: established as a
  data-level construction (construction + 96-case numeric check). Ensemble typicality:
  unresolved, and non-typical for iid per 077.
- q = 2 perfect-square conditions; their joint locus = (h_1 = h_2, n_1 = n_2) on n_f > 0; the
  branch n_f = -h_f^2 outside K >= 0: established (symbolic factoring, exact identity, exact
  rational sampling).
- 2560 / -45056 separation of the 078 double root from the double-pair locus; 0/2000 random
  general (H, K) hits: established (exact values) / sampled (the 2000).
- Moment ratio identity with weights S_p and exact values 9/17, 81/145, 1: established (symbolic
  weights, exact rationals); full-spectrum agreement 4.1e-15: sampled.
- D = 0 iff pair data coincide on this class; U_2 >= 0 with equality iff equal moduli:
  established (pigeonhole / Cauchy-Schwarz) with numeric confirmation.
- Reading spectral multiplicity as q_f equal rows: conditional input inherited from the
  transplanted selection rule, asserted at fixed depths only (proviso unchanged).
- Depths scaling with N; general (H, K) criterion at q > 2; two-sided +/- reading; typicality in
  ensembles; G missing steps (i)-(iv): unresolved, untouched here.

## Proposed changes

File: chapters/appH-microscopic-proofs.tex — one paragraph inserted, nothing else.
- Anchor: the unique line-start passage
  `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023} states that the vacuum energy there`
  (live tree L3175; occurrence count 1 for the line-start form, asserted by
  simulate_apply_080.py). The new paragraph lands blank-separated immediately before it, i.e.
  after the 079 paragraph (L3173), following the same stacking convention as paragraphs 072-079.
- Exact text: proposals/080-g-selrule-mixedmult/insert-r1.tex, a single content line with
  terminal CRLF, one \emph header, zero occurrences of $, [, ], \cite, \ref, \label, \eqref, and
  zero occurrences of the words status, priority, completion, open, critical, programme, derived
  (case-insensitive) except the closing idiom "... they close nothing in Problem~G."
- Kept: every existing line of appH unchanged; no deletions, no rewording. The paragraphs the
  insert refers to positionally (second/third/fourth above = 078/077/076) are physically before
  the insertion point, so their own positional references are unaffected.
- Stale passages elsewhere: none identified; no other file changes; no bib entries added
  (bib/namcg.bib untouched; no new citations needed).
- Byte contract (simulated, read-only): PRE appH size 720144, sha256
  a10eca5184d853b8baa0ffac185c67265e6414672e93025dad05a4e08028012f, CRLF 3824, bare LF 0, anchor
  at L3175, header absent. POST: size 725384, sha256
  e6a0335e1c19f0afa9f6fbc875baeec6c9f252482926596ba1f2ca36cf6a211c, CRLF 3826, bare LF 0, anchor
  at L3177, header line at L3175 (post-apply numbering), header count 1.

## Verification scripts

All under proposals/080-g-selrule-mixedmult/, deterministic seed 20261117, run from the repository
root with `python -I`, stdout byte-reproducible (reruns sha256-identical, empty stderr; the .out
files shipped alongside the scripts).
- `python -I proposals/080-g-selrule-mixedmult/s1_spectrum_mixed.py` ->
  expected invariants: line "A symbolic block-scalar factorizations ..." followed by
  ('q2_1_1', True, True) ('q2_2', True, True) ('q3_2_1', True, True), and the line
  "B cases=96 worst-spectrum-dev=8.882e-15 worst-involution-dev=1.421e-14 rank2q_ok=True".
- `python -I proposals/080-g-selrule-mixedmult/s2_q2_criterion.py` ->
  expected: "A perfect-square substitution identity: True | gcd of conditions: 1"; the two
  factored conditions on stdout; "C 078-example quartic identity (0 means match): 0 |
  condition values (nonzero both): 2560 -45056"; "B' identity 4B1-A1^2=-16((h1-h2)^2+n1+n2): True
  | off-locus mismatches: 0 on 200 random tuples; on-locus pass: 30 /30";
  "D general q=2 samples=2000 perfect-square(double-pair) hits=0 (expect 0)".
- `python -I proposals/080-g-selrule-mixedmult/s3_mixed_moments.py` ->
  expected: "A pair moments: S1 = 8*(2*h**2 + n) | S2 = 32*(8*h**4 + 8*h**2*n + n**2)";
  "A exact excesses p=1,2: [Fraction(9, 17), Fraction(81, 145)] | moment identity (mixed-1)/1 ==
  rho_p: True | equal-depth (2,2) value p=1,2: [Fraction(1, 1), Fraction(1, 1)]";
  "B mixed-data min D = 9.554e-02 | equal-data max D = 1.441e-15 | min U2 over 40 mixed samples =
  3.012e-01 (expect > 0; U2 >= 0 always)"; "C general-h weight identity: max
  |excess_from_spectra - excess_from_S_p weights| = 4.108e-15 over 30 samples x p=1,2".
- `python -I proposals/080-g-selrule-mixedmult/simulate_apply_080.py` ->
  expected: "PRE  size=720144 sha=a10eca5184d853b8 CRLF=3824 bareLF=0 anchorLine=3175
  headerCount=0"; "POST size=725384 sha=e6a0335e1c19f0af CRLF=3826 bareLF=0 anchorLine=3177
  headerLine=3175 headerCount=1"; "OK: no write performed; appH unchanged after simulation"
  (the script re-reads appH and re-checks its sha at the end).

## Decisions Taken

- (RESEARCHER-DECISION, frontier named_as + scout pointer) Route: block-scalar per-factor data
  with an explicit realizability construction, rather than the scout Edge-3 saturation /
  Littlewood-Richardson filter. Chosen because the construction gives exact per-factor spectra
  with no imported literature and no new assumptions, and because Edge-3 targets product-type
  Kronecker data, which this class is not. Rejected alternatives: import Knutson-Tao-type
  saturation as a filter (would import an unverified literature result and bind to a class we
  do not occupy); re-attempting the product Gaussian class (076's negation already closes it;
  frontier forbids re-attempt there).
- (RESEARCHER-DECISION, found mid-derivation) The two q = 2 coefficient conditions have a second
  algebraic branch n_f = -h_f^2 off the positive-Gram locus, so the reduction to the L3169
  criterion is stated only on n_f > 0. Chosen because data of the edge-datum family satisfy
  K = R^dag(1 - UU^dag)R >= 0 automatically, so the branch is never realized; asserting the
  unqualified reduction would have been a false claim. Rejected: restricting to generic h
  (would not exclude the branch), or dropping the criterion from the insert (would lose the
  connection to 077).
- (RESEARCHER-DECISION) The fixed-q validity condition from the 076 review is absent from the
  integrated text (grep), so the insert states the fixed-depth proviso as its own scope clause
  instead of quoting a passage; and the algebra-vs-reading split (exact for every fixed q; the
  row reading at fixed depths only; depths growing with N untreated) was chosen over
  silently restricting the algebra to small q.
- Header wording "block-equalized" (per-factor equalization) distinguishes the class from the
  integrated "norm-equalized" (uniform) paragraph; collision count for the header string in
  appH is 0 (asserted in simulate_apply_080.py).

## Milestone assessment

Routine. No critical-path step is closed; this is class-level evidence within Problem G's
reading class, of the same character as the 077 and 078 integrations, which were not
milestones. No milestone trigger in MILESTONE.md is claimed.

## Status-label recommendation

Critical-path list derived from ch17-agenda.tex L474-495 and the appH ledger: A, B, C, D1, E, F,
G-derived, N (H, I, J optional in scope). Affected labels: none. Problem G remains OPEN /
CRITICAL PATH / PROGRAMME-CONDITIONAL; no label change is proposed.

## Author decision needed

None.

## Remaining open step

For the frontier target itself: per-factor depths are now realized exactly in the rank-one
edge-datum family at fixed depths, but (a) whether any natural state or ensemble produces
block-scalar (H, K) data with unequal blocks at leading semiclassical order (typicality - 077
showed iid does not, and this package does not claim otherwise); (b) the criterion for double
pairs at q > 2 with general (H, K); (c) the two-sided +/- reading; (d) any statement for depths
growing with N, which the fixed-q proviso forbids here. For Problem G proper, none of the
missing steps (i)-(iv) (appH L3119-3130) is addressed; the insert closes nothing.

## Special instructions for the gatekeeper

- Do not read the insert as a selection or typicality statement: item 7 of the reasoning is an
  identity of moment signatures; the insert says so.
- Re-derive: the block-diagonal determinant step (trivial); the s2 factoring
  4B1 - A1^2 = -16((h_1-h_2)^2 + n_1 + n_2) and the positive-locus argument
  (h_1-h_2)^2 + n_1 + n_2 >= 2 sqrt(n_1 n_2) with equality iff coincidence; the branch
  n_f = -h_f^2 check (substitute into both conditions). Re-run all four scripts from the
  repository root with `python -I` and diff against the shipped .out files.
- Verify the byte contract against the live tree before integration: 078 and 079 are integrated
  but uncommitted, so appH on disk (720144 B, sha a10eca51...) is the integration target; if the
  tree moves, re-derive PRE/POST.
- Hygiene: my scan reported zero occurrences of status, priority, completion, open, critical,
  programme, derived (case-insensitive, as substrings) in insert-r1.tex, including the closing
  idiom; exactly one \emph, one CRLF-terminated line, no $, brackets, or ref commands. Confirm
  independently.
- No bib changes; no other file changes; nothing outside this proposal folder was written.
- The scout-cited Knutson-Tao records were not verified by me and are not used; if the
  gatekeeper wants Edge-3 pursued, that is a separate package.
