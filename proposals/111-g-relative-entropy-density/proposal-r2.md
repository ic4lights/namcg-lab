# Proposal 111-g-relative-entropy-density, round 2

## r1 -> r2 changelog (review-r1.md sha1-10 48118920cf; record-level corrections
only, no new mathematics; all formulas, the (star) equation, and every battery
number other than the F3 restatement are byte-identical to r1)

- F1 (blocking, manifest): manifest.md restated from actual disk bytes;
  p2_fock_srel.py pin corrected to b6bac2a036 (1565 B, bytes unchanged on disk).
  The r1 manifest entry 0904f2f7d8 was stale; the gatekeeper (review-r1 F1)
  verified the on-disk file runs and reproduces every P2 number.
- F2 (major): c0 normalization label corrected in Result para 1 and C4 (missing
  minus sign): now c0 = -ln Z0 = sum_j ln(2 sinh(h(nu_j)/2)), matching C6
  Z0 = exp(-c0), the (star) sign, and the battery dZ definition. No formula
  changed; every remaining ln-Z0 occurrence (C6 proof lines, C3 Z(G) definition,
  Test A row "ln Z vs c0" content note) was checked and is correct-convention
  as written.
- F3 (minor): battery table Test A row dSfock bound restated to "<= 9.7e-07"
  (observed worst 9.66e-07 at (17,0.70,1), run_modular.out line 2; the three
  observed values are 9.66e-07 / 1.47e-07 / 1.02e-07; tolerance 5e-3 unchanged).
- F4 (minor): Missing-step quotation now carries the source symbol: "the boundary
  \(\partial M\) under which" (appH-microscopic-proofs.tex
  L3199), replacing the silent one-word rendering of that symbol.
- F5 (minor): the (star) sentence (C6) now carries one clarifying clause: G1 is
  the uncentered symmetrized second moment G_ij = Tr rho1 (R_i R_j + R_j R_i)/2
  per H2 (equivalently, rho1 of zero mean). No new mathematics.
- F6 (minor, deliberately NOT taken): the p1_symbolic_a0.py comment "sq O sq = G
  at n=1" (false as written; correct: sq O sq = det(sq)*O; the encoded Kf_term
  and all printed outputs are correct and were independently re-derived by the
  gatekeeper) is left untouched so the pinned hash 8d2bd3624d stays verifiable;
  comment correction deferred to a future battery revision.


Basis line: digest + targeted reads; full 30-file split scan completed 2026-11-22
(reports/ledger.md SCAN-20261122) at pre-ordinal-40 state; sole delta since = certified
ordinal-40 insertion at appH L732-740, read here in full; digest CURRENT at head 23266972
(dirty-chapters: yes = that uncommitted integration only); battery stabilization per
reports/ledger.md R111-STABILIZED.

Battery fixed input verified this pass: sha1-10 prefixes _common.py 52497c0c45, check_modular.py cd982322f9, run_modular.out 7247af5bf4 all match; full re-run
byte-identical to run_modular.out (2250 bytes, 26 lines, 18 checks, final line ALL CHECKS
PASS). Quarantined files (run_modular_deadpass.log, diag1.py, diag2.py, probe2.py, probe3.py)
not cited, not run.

## Result

What is established here is a VERIFIED BUILDING BLOCK plus one exact derivation, feeding
Problem G missing step (i) and defining the evaluation target of step (ii). Nothing is
closed; Problem G remains exactly as recorded in Appendix H.

1. (Established derivation, 3-line proof below.) Let sigma0 = exp(-R A0(G0) R/2)/Z0 be the
   faithful Gaussian state with covariance G0 (symplectic spectrum nu_j > 1/2), A0 the
   closed-form modular exponent of the construction, c0 = -ln Z0 = sum_j ln(2 sinh(h(nu_j)/2)) the normalization. Then for
   ANY state rho1 with covariance G1,
       S(rho1||sigma0) = -S(rho1) + (1/2) Tr(A0 G1) - c0,
   and when rho1 is Gaussian with covariance G1, S(rho1) is the symplectic-spectrum sum
   sum_j s(nu_j). The identity is exact algebra: log sigma0 is the quadratic form, the
   quadratic form's expectation is the trace pairing with the symmetrized covariance, and
   Z0 = exp(-c0). Gaussianity is required only of the reference.

2. (Battery, fixed input.) The closed-form A0 and c0 are Fock-anchored on actual chain-cut
   ground states on the certified grid: 18 checks pass, byte-reproducible.

3. (Fresh probe P1, symbolic.) At n=1 the modular exponent collapses exactly to
   A0 = -(h/nu) O G O = (h/nu) cof(G) with h = ln((nu+1/2)/(nu-1/2)), so A0 > 0 exactly at
   n=1: it is a congruence of G > 0 by the orthogonal O times the positive scalar h/nu.
   Verified as an exact sympy zero (4 True outputs).

4. (Fresh probes P2/P3, honest limitation.) A Fock-matrix ground-truth comparison of the
   full relative entropy for a second Gaussian state G1 distinct from G0 agrees only to
   3.4e-3 .. 1.45e-2; P3 decomposes the gap: the (1/2)Tr(A0 G1) - c0 term matches to 1e-6
   while the entropy term carries the whole discrepancy (3.7e-3, 6.2e-3). Diagnosis
   (reported, not debugged, per dispatch): the Fock-built test state exp(-P K1 P)/Z is
   Gaussian only up to a truncation distortion of the same size as the already-documented
   Test B relative-covariance tolerance (relcov <= 3e-2), i.e. the gap is a property of the
   anchor construction, not of claim 1, whose proof does not use it. Named gap G-R (below).

## Target and status

Problem G: HBEV / infrared boundary entropy. Appendix H section sec:status-G
(chapters/appH-microscopic-proofs.tex L3099). Ledger label quoted verbatim (L3102-3106):
"Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope
results: G-model and G-external support at most a scope-limited model; G remains OPEN and
neither satisfies the matrix-derived criterion." Chapter 17 (ch17-agenda.tex L475):
"CRITICAL PATH; mechanism CLOSED CONDITIONALLY, derivation OPEN." G completion levels
passage (L486-496) read: only matrix-derived entropy density + stationarity derive G.
Missing step paragraph (appH, quoted in full at read; the four items verbatim):
closing the matrix-derived criterion requires "(i) a derivation, not a retained dictionary,
of the identification between a Presentation-A boundary cut and the boundary \(\partial M\) under which
the cut entropy becomes the local density (eq:Sent-exp); (ii) the interacting condensate
sector of (eq:Smatrix), the cubic term, matter and non-Gaussian ground-state correlations,
which carry the alpha_1 and alpha_2 structures; (iii) a derivation of the stationarity
condition (eq:bdy-EE) of Assumption ass:bdy-EE; and (iv) the mass-dimension-one
boundary-to-bulk conversion recorded in the dimensional status remark of the HBEV chapter,
without which (eq:Leff) stays schematic." This package feeds (i) and (ii) only.

The section's bounded-obstruction paragraph records that on Presentation-A data the replica
density is undefined (no manifold, no boundary, no tubular neighbourhood, no branched
cover, no trace factorization) and names exit "(i) A Presentation-A cut: spectral
projections of the coordinate operators ... for quadratic fluctuations the cut trace is
defined by Fock factorization over the restricted one-particle space; the output is a
functional of the quadratic kernel of the action and of the cut projector, not a cover
path integral and not a diffeomorphism scalar". The construction below is exactly an
exit-(i)-type object, at the relative-entropy level.

Dependencies: none of A, B, C, D1, E, F, N is consumed. Nothing here depends on or touches
the G-model / G-external reduced results.

## Source reading

Digest + targeted reads (basis line above). Read in full: appH Problem G section L3099-3301
including the missing-step paragraph and the edge-entropy/moments paragraphs; appH L720-749
(ordinal-40 bilocal insertion, read for the status-passage discrepancy check only);
ch17-agenda.tex L472-500; stab-notes.md in full; _common.py core (lines 20-140) and
check_modular.py test bodies (lines 25-102); run_modular.out in full; ledger lines for
items 087-090, 093 and the R111 dispatch lines. Files read via sed windows; no file
unreadable.

## Setup and hypotheses (explicit)

H1. Quadratic setting: a real scalar chain of L sites (ring), nearest-neighbour
positive contraction with mass parameter mu > 0; unique gapped Gaussian ground state;
single-particle data (C, Pim) from chain_ring(L, mu). This is a benchmark quadratic
truncation of the matrix action, NOT the matrix theory itself: no interaction, no matrix
degrees of freedom, no cutoff removal. Classification: phenomenological/input model for
the programme; the construction below is exact within it.
H2. Cut: N contiguous sites (sites 6..6+N-1), one-particle restriction to the cut, block
covariance G0 = G_block(C, Pim) of size 2N x 2N with G = (1/2){R,R}, R = (q,p): the cut
data of the exit-(i) paragraph. No geometry, no manifold structure is used or claimed.
H3. Faithfulness: symplectic spectrum nu_min > 1/2 strictly, guaranteed numerically by the
imaginary-leak assert of A_of_G (relative leak <= 1e-6) on the certified grid only.

## Construction (all objects are data of the cut: kernel + projector)

Given a physical covariance G (2N x 2N, nu_min > 1/2):
  C1. nu(G): symplectic spectrum (moduli of the eigenvalues of i O G, computed via the
      Hermitian Kh = -i sq O sq with sq the symmetric square root of G; eigenvalues +-nu).
  C2. h(nu) = ln((nu + 1/2)/(nu - 1/2))  (modular frequencies; h > 0, diverges as nu -> 1/2).
  C3. A0(G) = -i (isq Kf sq) O,  Kf = HV diag(sign(hw) h(|hw|)) HV^dagger,
      the matrix such that sigma_G = exp(-R A0(G) R / 2) / Z(G) has covariance G
      (modular exponent of the Gaussian state; closed form, _common.A_of_G_raw).
  C4. c0(G) = -ln Z(G) with the two certified closed forms
      c0 = sum_j ln(2 sinh(h(nu_j)/2))  (modes)   and   c0 = -(1/4) sum ln eig(-(G O)^2 - 1/4)
      (eigenvalue product); Test D certifies agreement to 1e-10 (0.814120352312 = 0.814120352312).
  C5. S(G) = sum_j s(nu_j), s(nu) = (nu+1/2)ln(nu+1/2) - (nu-1/2)ln(nu-1/2), with the
      equivalent modular form s = (nu-1/2)h - ln(1 - e^{-h}) (Test A dSmod line).
  C6. Relative entropy against the faithful Gaussian reference sigma0 = sigma_{G0}: for ANY
      state rho1 with covariance G1, where G1 is the uncentered symmetrized second moment G_ij = Tr rho1 (R_i R_j + R_j R_i)/2 per H2 (equivalently, rho1 of zero mean),
          S(rho1||sigma0) = -S(rho1) + (1/2) Tr(A0(G0) G1) - c0(G0).       (star)
      Proof. log sigma0 = -(1/2) R A0 R - ln Z0 exactly (C3-C4 define a faithful Gaussian,
      Z0 = exp(-c0) > 0). Then S(rho1||sigma0) = -S(rho1) - Tr rho1 log sigma0
      = -S(rho1) + (1/2) Tr rho1 (R A0 R) + ln Z0; for symmetric A0 the quadratic-form
      expectation in any state with symmetrized covariance G1 is (1/2) Tr(A0 G1)
      (contract the two R's; the antisymmetric part drops against symmetric A0).
      All terms finite since nu_min > 1/2 gives bounded A0. No step uses Gaussianity of
      rho1. Classification: established derivation (elemental; see also literature note).
  C7. When rho1 is Gaussian with covariance G1, S(rho1) = S(G1) by C5, and (star) is a
      closed functional of the two covariances. This is the object the density route uses.

## Battery summary (fixed input, re-run byte-identical this pass)

| Test | Content (one line) | Certified grid | Best / worst observed |
|---|---|---|---|
| A | Fock anchor of the modular exponent on real chain-cut ground states: covariance round-trip, ln Z vs c0, entropy triple-identity (form/spectrum/modes), Fock-vn entropy | (L,mu,N) = (17,0.70,1), (19,0.40,2), (23,0.25,3); nmax=12 | dG 2.6e-08..8.8e-07; dZ 5.7e-09..7.2e-08; dSfl <= 1.0e-12; dSmod <= 5.6e-17; dSfock <= 9.7e-07 |
| B | Same round-trip for general random physical covariances (Fock-truncation distortion documented) | n = 1,2,3 x seeds 1,2,3; nmax 20/12/11 | relcov <= 1.40e-02 (< 3e-2 tol); dsym = 0; dfirst <= 1.8e-15 |
| C | Positivity A0 > 0 | 12 random covariances n<=4 + cuts (31,0.05,8), (31,0.20,8), (27,0.05,6) | minEig(A0) = 3.185e-01, 1.075e+00, 3.584e-01 > 0; leak <= 5.4e-07 |
| S1 | Documented exclusion tripwire (resolution limit, NOT a FAIL) | cut (41, 0.01, 12) | leak 1.29e-03 > 100x the 1e-6 certified tol |
| D | c0 closed forms agree and are real | random G(3, seed 42) | 1.2e-12 relative |
Totals line verbatim: "RESULTS: 18 checks, 0 failures / FAILURES: none / ALL CHECKS PASS".
Resolution limit carried honestly (fixed-input limitation, per rule 3 not a closure and not
a FAIL): mu = 0.01 cuts and any cut with about 8 or more near-pure modes (N >= 12 sampled)
are EXCLUDED from the certified grid. Cause: h(nu) = ln((nu+.5)/(nu-.5)) is unresolvable in
double precision once nu_min - 0.5 falls below the eigenvalue floor (measured leak 1.29e-03
at (41,0.01,12); nu_min - 0.5 = 5.7e-12 already at the floor at (31,0.05,8)); no clipping
was applied because clipping cannot restore resolved h. Removal needs higher-precision
linear algebra (FOR r2 item 4).

## Fresh probes (3 used, budget 3; outputs <= 6 scalar lines each)

P1 (p1_symbolic_a0.py, sympy, exact). At n=1 the C3 closed form collapses to
A0 = -(h/nu) O G O = (h/nu) cof(G), nu = sqrt(xp - r^2). Since O is orthogonal with
det 1, -(OGO) = O G O^T is a congruence of G, so A0 > 0 EXACTLY at n=1 whenever G > 0;
and h > 0 iff nu > 1/2. Observed: 4 True (identity zero, congruence form, det cof = det G,
trace cof positive). This is a derivation, not a check: it settles positivity at n=1 and
explains (conceptually, not as proof for n>1) why Test C sees minEig(A0) bounded away
from 0.
P2 (p2_fock_srel.py). Full S(rho1||sigma0) on certified cut (17,0.7,1), direct Fock-matrix
Tr rho1(log rho1 - log rho0) versus (star): direct 0.6531/0.6184/1.7168, form 0.6565/
0.6244/1.7313, gaps 3.41e-03 / 6.00e-03 / 1.45e-02 (seeds 7,8,9, nu_hi = 1.3 family,
nmax = 12); self-distance exact (0.0e+00 direct, -3.3e-16 form); positivity holds for 5
random G1 (min 2.0520e-01).
P3 (p3_fock_srel_cold.py). Decomposition of the P2 gap at nmax = 16, cold family
nu in [0.55,0.65]: K0 term |form - direct| = 1.4e-06, 3.1e-08; entropy term gap =
3.7e-03, 6.2e-03. The entire discrepancy is entropy-side.
Interpretation (named gap G-R, classification: unresolved technical step, NOT a defect of
(star)): the Fock-built second state exp(-P K1 P)/Z is Gaussian only up to a truncation
distortion (non-Gaussian by O(1e-2) in covariance, the same documented Test B tolerance),
and relative entropy sees that distortion through S(rho1) while the K0 pairing is blind to
it at 1e-6. The proof of (star) consumes only covariances and S(rho1), so (star) is not
falsified; the two-state Fock anchor is certified only within G-R. Fix route (FOR r2.1):
compare (star) against the Araki-Wood type closed form for the relative entropy of two
Gaussians, eliminating the Fock construction of rho1 entirely.

## Contribution to the missing steps (tiered)

Step (i) - FED as verified building block (input tier). (star) plus the certified A0, c0
supply, on Presentation-A cuts of a quadratic model, the relative-entropy functional
S(rho1||sigma0) as an explicit functional of the quadratic kernel and the cut projector -
the exact output type the exit-(i) paragraph names. The relative-entropy combination is
the form the density route needs: the reference-subtracted quantity is positive, vanishes
only at the reference, and its cut per-site limit is a candidate density input that step
(i) must then identify with the local form (eq:Sent-exp). What remains for (i): the
identification itself (dictionary-derived, not retained), locality of the per-site limit,
and removal of H1-H3 - ALL OPEN here.
Step (ii) - FED as target definition + verified free reference (input tier). For an
interacting/non-Gaussian reduced state rho_int, (star) splits
S(rho_int||sigma0) = -S(rho_int) + [known free-data term]: the bracket is computable from
certified free data, so the whole alpha_1/alpha_2 content is isolated in S(rho_int).
No interacting evaluation is performed here: (ii) stays OPEN.
Steps (iii), (iv) - NOT fed. No stationarity computation, no boundary-to-bulk conversion.

## Bounded-negative exits (how this avoids existing hypothesis classes)

Ledger discrepancy noted: the dispatch labels item 090 as orbit-rigidity; the ledger records
090 as g-interaction-induced-simplex-profiles and orbit rigidity as 093 (chain-2 rank-1
edge G.moments-interaction-nonconvex). Both classes are covered below.
1. Decoupling-cone class (items 087/088/089; hypotheses in the integrated Problem G
paragraphs: profile/simplex families of the rank-one edge datum, frame averaging over
Haar-typical frames, fixed D and fixed W, moment coordinate a/r decoupling, frame-averaged
induced coupling, stationarity-profile selection). The present construction asserts no
frame selection, no profile family, no averaging and no stationarity: it is a statement
about Gaussian states and their relative entropy at a FIXED quadratic kernel and FIXED cut
projector. It lies outside the hypothesis class of those no-gos; it is neither obstructed
by them nor a counterexample to them.
2. Orbit-rigidity class (item 093; hypotheses: rigidity of the moment coordinate near
coincidence walls in the interaction-profile setting). The construction carries no moment
coordinate and no coincidence wall: it is quadratic in the covariance data. Outside scope.
3. The replica-density obstruction of the section's bounded-obstruction paragraph (no
manifold, no branched cover, no region trace factorization on Presentation-A data) is not
circumvented by pretending otherwise: the construction never uses replicas, covers or a
factorization of the full-theory trace; it is the Fock-factorized cut object of exit (i)
and it inherits exit (i)'s recorded limitation: functional of kernel + projector, not a
diffeomorphism scalar, cut-choice dependent.

## Literature (checked vs not checked)

Verified live (WebFetch of the arXiv record, 2026-11-22): arXiv 1512.06431 = Jafferis,
Lewkowycz, Maldacena, Suh, "Relative entropy equals bulk relative entropy" (modular
Hamiltonian gravity dual; relative entropy of nearby states equals bulk relative entropy
at leading order in the bulk gravitational coupling). The frontier-record description
"Jafferis-Jacobson g-relative-entropy line" mischaracterizes this record (wrong coauthors,
wrong title): cite as JLMS or drop. Nothing is imported from it; it is cited only as
motivation that relative entropy of nearby states is the natural comparator once the
reference state is fixed.
Not independently verified (record not fetched this pass; no result imported; (star) is
proved above, so the citation is decorative): the Gaussian relative-entropy formula
belongs to the standard quantum-information literature (Araki-Yamagami, asymptotic
behaviour of Gaussian measures and relative entropy; Gaussian modular Hamiltonians in the
free-field literature). Marked not independently verified.

## Claim classification (rule 6)

1. (star) with proof in C6: established identity/derivation (elementary, self-contained).
2. C1-C5 closed forms and their equalities: established where symbolic (n=1, P1); on the
   certified grid: conditional results verified numerically (18-check battery, explicit
   tolerances, double precision).
3. General-n positivity of A0: conditional (modular-theory argument given; numerically
   certified only on the Test C grid; exact only at n=1).
4. All chain-cut values (dG, dZ, entropies, leaks, minEigs): conditional numerical results
   under H1-H2 at the stated truncations (finite L, finite N, nmax, double precision).
5. The chain as a stand-in for the matrix model: phenomenological input for the programme;
   NOT a matrix-derived object.
6. The reading of S(rho1||sigma0)/per-site as a route to the density of
   Assumption ass:Sent-density: mechanism/conjecture tier; NO identification derived.
7. Gap G-R (two-state Fock anchor distortion): unresolved technical step, localized by P3.

## What this does NOT establish

Not a closure of anything: no derivation of the cut-to-boundary identification (residue of
(i)); no interaction, no alpha_1/alpha_2 values (ii); no stationarity (iii); no
boundary-to-bulk conversion (iv); no thermodynamic or continuum limit (all statements are
finite-L, finite-N, nmax-truncated, double-precision); no per-site density value or
locality statement; no connection to the boundary functional or to (eq:Leff); no
Bekenstein-Hawking or modular-flow input imported; no claim that the chain ground state
represents the matrix ground state; no status, priority or completion wording for G,
which remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL exactly as recorded.

## Manuscript landing note (no manuscript text written here)

Future single scoped paragraph in chapters/appH-microscopic-proofs.tex, Problem G section
(sec:status-G), positioned after the "Missing step." paragraph and before the
"Edge entropy of a matrix block ..." paragraph: records the relative-entropy functional
(star) on Presentation-A cuts as a verified building block (exact algebra + certified
reference anchor), states resolution limit and gap G-R, feeds missing steps (i)-(ii) at
input tier, closes with one scoped status sentence. No label changes; no equation
relocations; anchors and uniqueness to be re-verified by the integrator at insert time.

## Verification scripts and reproduction pack (all in this folder)

Battery (fixed input): python -I check_modular.py   (~90 s).
  Expected invariants: final lines exactly "RESULTS: 18 checks, 0 failures",
  "FAILURES: none", "ALL CHECKS PASS"; whole output byte-identical to run_modular.out
  (sha1-10 7247af5bf4). Note: the dispatch exec one-liner needs __file__ injected
  (g = {'__file__': 'check_modular.py', '__name__': '__main__'}); used this pass, result
  byte-identical (evidence: rerun.out, sha1-10 7247af5bf4). No code modified.
P1: python -I p1_symbolic_a0.py -> 4 True lines.
P2: python -I p2_fock_srel.py -> gaps 3.41e-03 / 6.00e-03 / 1.45e-02; self 0.0e+00;
    min positive 2.0520e-01.
P3: python -I p3_fock_srel_cold.py -> gapK 1.4e-06 / 3.1e-08, gapS 3.7e-03 / 6.2e-03.
Tool output is a check, not a proof; the proof of (star) is the C6 derivation and the
n=1 positivity proof is the P1 congruence argument.

## Decisions Taken

1. Battery treated as fixed input per dispatch; verified by hashes + byte-identical re-run
   only, zero numerics debugging (the three prior deaths were numerics spirals).
2. The P2 discrepancy was localized with one probe (P3) and then STOPPED: reported as gap
   G-R with a named fix route, not chased numerically. Chosen because (star)'s proof is
   independent of the Fock construction of rho1, so more numerics cannot change the
   classification; a clean symbolic two-state anchor is the derivation-first fix (r2.1).
3. Citation 1512.06431 kept but corrected to JLMS with the frontier-record
   mischaracterization flagged (verified option) instead of dropped (less informative).
4. Headline framing chosen: verified building block feeding (i)+(ii) at input tier, not a
   stationarity (iii) story - the honest maximal positive claim from this battery.
5. 090/093 ledger/dispatch label discrepancy recorded; exits cover both hypothesis classes.

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step derived, no missing link closed;
a verified building block plus named gaps is input-tier progress on (i)/(ii).

## Status-label recommendation

Unchanged. Re-derived from ch17 L475 and appH L3102-3106: G is OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL; critical-path set for the full-GR scope re-read as A, B, C, D1, E,
F, G-derived, N. This package proposes no label change for any problem.

## Author decision needed

None. (No label, scope or core change is proposed; spacetime stays emergent throughout:
no route here assumes a fundamental metric.)

## Remaining open step

To move step (i) from building block to derivation, the exact residue is: (a) a
dictionary-derived identification of a Presentation-A cut with the emergent boundary under
which the per-site limit of S(rho1||sigma0) takes the local form (eq:Sent-exp); (b) proof
or disproof that the per-site limit exists and is local for contiguous cuts as N, L -> inf
(here only finite data points exist); (c) the interacting reduced state rho_int to evaluate
the (ii) split on, currently unavailable; (d) removal of gap G-R for the two-state anchor
(FOR r2.1) and of the resolution limit for near-pure cuts (FOR r2.4). None of (a)-(d) is
settled here; (a) is the gating residue and is stated OPEN.

## Special instructions for the gatekeeper

- Scope limits: this package asserts a verified building block at input tier only; treat
  any reading of it as a closure of (i)-(iv), a G-model/G-external-equivalent result, or a
  matrix-derived statement as OUT OF SCOPE and flag it.
- Re-check first: the byte-identical battery re-run (commands in reproduction pack); the
  C6 three-line derivation of (star) - in particular the claim that only the reference
  needs to be Gaussian and that the quadratic-form pairing uses only symmetry of A0; the
  P1 sympy identity (exact, fast); whether the P3 decomposition supports the localization
  of gap G-R to the entropy side.
- Verify the JLMS citation against the arXiv record yourself if the manuscript ever cites
  it; the mischaracterization flag must not be softened.
- Do not require resolution of the excluded near-pure grid: documented resolution limit,
  removal is r2 work.
- The dispatch-to-manuscript line "relative entropy of Gaussian states ... -S1 + 1/2
  Tr(A0 G1) - c0 structure with Fock-anchored verification" is realized with one honesty
  correction: Fock anchoring is tight for the reference state and only G-R-tight for a
  second Gaussian test state.

## FOR r2 (ranked, derivation-first)

1. Two-state anchor without Fock distortion: derive/verify the Gaussian-Gaussian closed
   form of S(sigma_G1 || sigma_G0) (Araki-Wood type) and cross-check (star) symbolically at
   n=1 and numerically at n<=3; closes gap G-R for Gaussian rho1 and upgrades (star)'s
   two-state tier from algebra-plus-distorted-anchor to fully certified.
2. Positivity lemma for general n: prove A0(G) > 0 for all physical G from the functional
   calculus (candidate route: operator-monotonicity/congruence argument generalizing P1;
   check against the literature on modular Hamiltonians of gauge-invariant... (free)
   Gaussian states). Converts Test C from grid-certified to theorem.
3. Per-site density ladder: S(rho1||sigma0) per site for contiguous N-cuts at growing N
   (fixed L, several mu), as the candidate interface of the density route; conditional
   numerical input, explicitly no locality claim.
4. Precision upgrade (mpmath or double-double symplectic eigensolve) to bring
   (41, 0.01, 12)-class cuts onto the certified grid and remove the resolution limit.
5. Gaussian-variational probe of the (ii) split: bound -S(rho_int) by minimizing the
   (star) bracket over a Gaussian family on a deformed quadratic kernel (cubic truncated
   interaction), producing an input-tier estimate of the interacting relative-entropy
   density contribution. Only if gradeable without new unsupported inputs.

## Manifest

See manifest.md (updated this pass): sha1-10 + bytes for every shipped file; quarantined
files listed NOT CITED.
