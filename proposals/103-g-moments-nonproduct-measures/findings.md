# 103-g-moments-nonproduct-measures, round 1: findings

Round 1 completes the item whose mathematics survived on disk from the previous
run (s1_wick_pushforward_D2.py/.out, s2_selection_bifurcation.py/.out,
s3_generalD_checks.py/.out). This round writes up those artifacts only; no new
numbers were computed beyond re-running the three surviving scripts. All numbers
in this file and in insert-r1.tex are taken verbatim from the three .out files
(rule 7).

## 1. Target and source context

- Frontier edge G.moments-nonproduct-measures, chain 2, co-rank 2 order 1,
  state "untried", the dispatchable head post-33 (src:
  scratch/103_frontier_excerpt.txt, hits at 76580, 191583, 191962, 385369:
  "DISPATCHABLE HEAD = G.moments-nonproduct-measures (co-rank 2 order 1,
  untried, positive-aimed)"). Required symbols (excerpt hit at 191962):
  "non-product joint law on slot-simplex x frame space", "its induced
  profile-pushforward weight", "non-degeneracy along the 088 kernel directions".
- Named as REVIEW-089 surviving relaxation (1) "non-product slot-frame-coupled
  measures - the axis untouched by the integrated 085/087/089 measures (Haar /
  slot-independent / product)" (excerpt hits at 25707, 187487).
- appH read IN FULL this round: L3119-3131 (Problem G Missing step paragraph,
  items (i)-(iv)); L3191 (integrated 089 Pushforward weights paragraph); L3221
  (G-block closer). Prefixes (110 chars) of L3185-3221 and an ordinal
  cross-reference scan of L3185-3221 and L3223-3309 were printed by script
  (prefixes/offsets only, per context discipline). No other appH content was
  read; reports/graph/frontier.yaml was NOT read.
- Live appH at time of writing: 801632 B, sha256-16 e37ca5385996df34,
  CRLF 3868, bareLF 0, no BOM (re-asserted by simulate_apply_103.py).
- Pointers from the excerpt (not re-verified line-by-line): 089 integrated at
  appH L3191; 102 integrated at appH L3197 as the flat-Dirichlet statistics
  mid-block supplement; block layout 090@3193, 091@3195, 102@3197, 092@3199,
  ..., 101@3217, Vacuum-term header L3219, block closer L3221 (re-verified by
  the prefix scan).

## 2. Route statement (reconstructed from the three script docstrings)

(A) s1: Bessel ray integral int_0^oo tau e^{-b tau} I_0(c tau) dtau =
b/(b^2-c^2)^{3/2} (30-digit mpmath quadrature, b>c>0); the closed-form
correlated-gaussian slot-pushforward density at D=2, f(p) = det*b/(b^2-c^2)^{3/2}
with b = g2 p + g1 (1-p), c = 2|rho| sqrt(p(1-p)), det = g1 g2 - |rho|^2, where
g_i are the slot variances and rho the complex slot coherence; rho->0 reduction
to the 089 product density g1 g2/(g2 p + g1(1-p))^2; normalization;
equal-variance closed form (1-r^2)/(1-4 r^2 p(1-p))^{3/2} with
r = |rho|/sqrt(g1 g2). Complex-Wick contingency-table moments; Laplace identity
E exp(-t.E) = det(I+T Sigma)^{-1}. Monte Carlo of the profile pushforward
(seed 1031), phase-blindness in arg(rho).
(B) s2: selection structure. Equal variances: unique maximum at the barycenter
for every r in (0,1), flat at r=0; coincidence enhancement
P(|2p-1|<eps) = eps/sqrt(1-r^2) + O(eps^3). Unequal variances (1,2): vertex
log-slope criterion and interior-maximum threshold |rho|^2 > 1/3, normalized
coherence threshold rhat* = 0.408248290463863; fine-grid argmax table.
(C) s3: general-D checks. Ray formula recovers the 089 closed form at diagonal
covariance at D=2 and D=3; D=3 equicorrelated Wick moment 1+3t^2+2t^3;
D=3 profile statistics vs flat Dirichlet.

Independent re-derivation performed this round (pen-and-paper, consistent with
s1): for proper complex gaussian slots with E[w w^dagger] = Sigma, the change
w_i = sqrt(E_i) e^{i theta_i} leaves the angular integral
I_0(2|rho| sqrt(E1 E2)/det) against the weight exp(-(g2 E1 + g1 E2)/det); the
fibre map E_i = T p_i contributes T, and the Bessel ray integral gives f(p)
exactly as printed in s1 (B). This confirms the surviving derivation is
internally consistent; it is not imported as a proof.

## 3. Verbatim key lines from the .out files

s1_wick_pushforward_D2.out (selection):

    b=3 c=1: lhs 0.13258252147247766083 rhs 0.13258252147247766083 reldiff 0.00e+00
    b=5 c=4.9: lhs 5.0759485619152392793 rhs 5.0759485619152518481 reldiff 2.48e-15
    rho=0 reduction: max over 41-point p-grid of |f-f0| at (g1,g2)=(3,7), 30-digit: 3.94430452610505902705864282641e-31
    normalization int_0^1 f dp at (g1,g2,|rho|)=(1,2,1/2): 1.0
    normalization at (1,1,7/10): 1.0
    equal-variance form (1-r^2)/(1-4r^2 p(1-p))^{3/2} exact: True
    f(1/2) at equal variance == 1/sqrt(1-r^2): True
    f(0) at equal variance: 1 - r**2  f(1): 1 - r**2
    E[E1 E2]      = rho**2 + sigma1*sigma2
    E[E1^2 E2]    = 2*sigma1*(2*rho**2 + sigma1*sigma2)
    E[E1^2 E2^2]  = 4*rho**4 + 16*rho**2*sigma1*sigma2 + 4*sigma1**2*sigma2**2
    E[E1 E2 E3] at D=3 (exact data) = 1517/1000
    binwise max rel dev (rho real), central 90% bins: 0.0799
    binwise max rel dev (rho e^{i pi/3}), central 90% bins: 0.0656
    binwise max rel dev (rho e^{i 0.37 pi}), central 90% bins: 0.0943
    equal-variance r=0.7 binwise max rel dev, central 90% bins: 0.0711
    MC E[s2] r=0 equal var (expect 2/3 = 2/(D+1) of the flat-Dirichlet statistics paragraph): 0.66619
    Laplace E exp(-t.E) MC 0.19303841 det(I+T Sig)^{-1} 0.19307080 reldev 1.68e-04
    S1 DONE

s2_selection_bifurcation.out (selection):

    f'(1/2) at equal variance (symbolic, all r): 0
    d/dz of equal-variance density (symbolic): 6*r**2*(1 - r**2)/(-4*r**2*z + 1)**(5/2)  > 0 for r>0, z<1/4
    => density strictly increasing in p(1-p): unique max at p=1/2 for every r in (0,1);
       at r=0 the density is f=1 (flat): 1
    r=1/2 eps=0.01: P(|2p-1|<eps) quad 0.0115468129385 leading eps/sqrt(1-r^2) 0.0115470053838 ratio 0.99998333
    r=9/10: E[s2] 0.57456906928725092161 (dps30 diff 1.3e-32) ; E[rho_2]=1+E[s2]=1.5745690692872509216 ; E[s2^2]=0.34077142438177776564 ; E[s2]-2/3=-0.09209759738
    d/dp log f at p=0+ (g=(1,2), |rho|=r): 6*r**2 - 2  > 0 iff |rho|^2 > 1/3
    => interior maximum exists iff |rho|^2 > g1(g2-g1)/3 = 1/3, i.e. normalized coherence rhat^2 > (g2-g1)/(3 g2) = 1/6, rhat* = 0.408248290463863
    0.50   0.00000        0.87500              1.75000
    0.70   0.09909        0.79034              1.51000
    S2 DONE

s3_generalD_checks.out (selection):

    D=2: matches (D-1)!/(G (sum p_i/g_i)^D): True
    D=3: matches (D-1)!/(G (sum p_i/g_i)^D): True
    E[E1 E2 E3] exact = 2*t**3 + 3*t**2 + 1  (closed form 1+3t^2+2t^3 match: True )
    t=0.5: exact 2.000000 MC 2.001202 reldev 6.01e-04
    t=0.0: MC E[s2]=0.50003  E[rho_2]=1+E[s2]=1.50003  E[s2^2]=0.26671
    t=0.5: MC E[s2]=0.47725  E[rho_2]=1+E[s2]=1.47725  E[s2^2]=0.24203
    S3 DONE

## 4. Rule-6 classification

- established identity/derivation: the Bessel ray integral (30-digit quadrature;
  standard table form); the D=2 correlated pushforward closed form and its
  rho=0 reduction (symbolic), normalization (30-digit quadrature, two parameter
  points); equal-variance closed form, f(1/2)=1/sqrt(1-r^2), f(0)=f(1)=1-r^2,
  strict monotonicity in p(1-p) (symbolic derivative positive) hence unique
  barycenter maximum for every r in (0,1); coincidence coefficient
  eps/sqrt(1-r^2) (exact leading term, quadrature ratio -> 1); E[s2] < 2/3 for
  every r>0 at equal variance (implied by the symbolic monotonicity, since
  s2 = 1 - 2p(1-p)); the contingency-table complex-Wick moment formulas and the
  D=3 equicorrelated moment 1+3t^2+2t^3 (symbolic permanental sum, MC-checked);
  Laplace identity det(I+T Sigma)^{-1} (standard complex-gaussian identity,
  MC-checked 1.7e-4); ray-formula recovery of the 089 diagonal closed form at
  D=2,3 (symbolic); the vertex right-log-slope 6|rho|^2 - 2 at (g1,g2)=(1,2)
  (symbolic limit) and the destabilization value |rho|^2 = 1/3, normalized
  0.408248290463863.
- conditional result: the whole family is conditional on the named correlated
  gaussian slot class (E[w w^dagger] = Sigma with input g1, g2, rho); the
  general-g threshold form |rho|^2 > g1(g2-g1)/3 printed by s2 is verified
  symbolically only at (1,2) (see 6.1 and 6.3); the "interior maximum exists
  iff" reading of the slope criterion additionally needs unimodality, not
  proved (see 6.2).
- numerical/MC check (consistency, not proof): pushforward binwise deviations
  0.066-0.094 (200 bins, 4e5 samples), Wick-moment reldevs <= 8.2e-3,
  coincidence-probability ratios, the argmax table (the interior maximum is
  recorded as the global grid argmax at |rho|=0.7, argmax 0.09909), and the
  D=3 profile-statistics shift toward uniformity (E[s2] 0.50003 -> 0.47725).
- input: the coherence rho, the variances g_i, and the gaussian slot class
  itself. The repository does not by itself supply where the slot correlations
  come from; nothing upstream produces rho.
- unresolved step: any core derivation of the correlated slot law; the frame
  factor of the edge required symbols; non-degeneracy along the 088 kernel
  directions; the general-g threshold and the D=2 density beyond two slots.
- conjecture/mechanism: the bifurcation is a selection MECHANISM within the
  named conditional family (vertex-to-interior switch driven by input label
  asymmetry plus coherence). It is NOT a profile-selection statement about the
  core, and not a statement that the core produces a selected profile.

## 5. Relation to the recorded bounded classes (evades / inherits)

- 089 bounded class (integrated text at appH L3191, read in full): the bound is
  stated "for the wider class of product slot laws in which the squared slot
  magnitudes are independent and the law of each is fixed by s^2 times the slot
  variance". Every derived member here has dependent squared slot magnitudes
  (the joint density carries the I_0(2|rho| sqrt(E1 E2)/det) factor, absent iff
  rho = 0), so the class hypothesis (independence) fails by construction: as a
  matter of class fact this package derives weights OUTSIDE the 089 product
  class, and one derived property is impossible inside it - at equal variances
  the correlated pushforward is strictly non-flat (peaked at the barycenter at
  height 1/sqrt(1-r^2)), while the 089 exponential product weight at uniform
  input is flat. EVASIVE (positive-aimed data outside the bounded class).
- What is nevertheless INHERITED from the 089 audit: the same fibre map is used,
  and the family is indexed by input labels (g1, g2, rho); reading f as a weight
  on profile space re-imports those labels. The structural obstruction "no
  weight beyond the profile data already supplied" is not defeated - it is
  relocated from (g) to (g, rho). The core-provenance gap (the missing
  core-produced weight, 088 audit sentence) is untouched.
- 090 orbit-rigidity class (S_D-invariant profile weights): the equal-coherence
  equal-variance members are relabelling-invariant and their unique maximum is
  the barycenter - exactly the rigidity alternative, no single non-uniform
  profile is selected. The unequal-variance members break exchangeability
  through the input labels and realize the label-asymmetry escape branch, but
  only within the named family (the asymmetry is input). Consistent with, not a
  counterexample to, the recorded no-go.
- 094-101 fibre-side class: not entered; no Gram-spectrum/fibre claim is made.

## 6. OPEN list (explicit, incl. route ambiguities) for the gatekeeper

1. s2 DOCSTRING/OUTPUT DISCREPANCY: the header comment of
   s2_selection_bifurcation.py (lines 9-10) states the criterion as
   |rho|^2 > g1(g2-g1)/6 and r*^2 = (g2-g1)/(6 g2); the symbolic output and the
   printed conclusion say 6*r**2 - 2, |rho|^2 > g1(g2-g1)/3 = 1/3,
   rhat^2 > (g2-g1)/(3 g2) = 1/6, rhat* = 0.408248290463863. The printed .out
   values are internally consistent (re-derived this round from f: the slope of
   log f at p=0+ with (g1,g2)=(1,2) is 6|rho|^2-2); the docstring is stale. The
   .out files are the record; the manuscript insert uses only the .out values.
2. "interior maximum exists IFF |rho|^2 > 1/3": the .out prints this iff, but
   only the vertex-instability direction (positive right-slope) is proved
   symbolically; the converse needs unimodality of f, not established. The
   global vertex-to-interior switch is recorded only numerically (argmax table).
   The insert claims destabilization at |rho|^2 = 1/3 plus the numerical argmax
   record, not the iff.
3. The general-g threshold form g1(g2-g1)/3 is printed, verified symbolically
   only at (1,2). The insert states the threshold only at (g1,g2)=(1,2).
4. Phase-blindness (the density depends on rho only through |rho|) is exact in
   the closed form and MC-checked at three phases; no separate analytic proof
   for the full density is given (it is immediate from the angular integral,
   whose shape is stated in the insert).
5. E[E1 E2] = g1 g2 + |rho|^2: the s1 symbolic line is for real positive rho
   (rho**2); the |rho|^2 form for complex rho is the standard complex-Wick
   result, checked directly at D=3 with complex covariance (E[E1 E2 E3] =
   1517/1000, MC 6.6e-3) and implied at D=2 by the phase-blind density.
   Classified established with this evidence.
6. The edge required symbols are only PARTLY supplied: a non-product slot law
   and its induced profile-pushforward weight (D=2 closed form; D=3 via moments
   only), but NO joint law on slot-simplex x frame space (the frame measure is
   not entered) and no assessment of non-degeneracy along the 088 kernel
   directions. The edge is attempted-open; G stays OPEN; the derived class is a
   conditional derivation class, not core output.
7. The wording of the Hewitt-Savage constraint in the frontier record
   ("exchangeability forces mixture-of-products at finite N", excerpt hit at
   290728) is, as recorded, stricter than the standard theorem (which concerns
   infinite exchangeability); the equal-coherence family here is exchangeable
   AND non-product at finite D=2 and is therefore not excluded by the correct
   content of the theorem. No manuscript change is proposed (that constraint
   statement is not in appH); noted for the record only.
8. Anchor: the orchestrator offered "after L3191" or "after L3197". A pure
   insertion at either slot silently re-points downstream "Nth preceding
   paragraph" ordinals (L3193 "preceding paragraph"; L3199 "seventh/third/tenth
   preceding"; L3203 "fourth/third"; L3205 "fourth/second/third/sixth"; L3207,
   L3209, L3211, L3215 similarly - from the scripted scan). The only
   pure-insertion slots that break no ordinal are after L3217 (paragraph 101,
   before the Vacuum-term paragraph) and after L3219. Chosen: after L3217
   (inside the orchestrator-approved span "after the integrated 102 paragraph
   and before the block closer", and inside the measures/pushforward discussion
   rather than after the citation-type Vacuum-term note). The insert names
   neighbour paragraphs by title-fragments ("the Pushforward weights
   paragraph", "the flat-Dirichlet statistics paragraph", "the fixed-trace
   beta-deformation paragraph", "the variational-rigidity paragraph", "the
   Missing step paragraph"), never by ordinals, so its own references are
   insertion-robust.

## 7. Reproduction pack

Run from repo root (fixed seeds default_rng(1031/1032/1033); the PCG64 stream
is numpy-version-stable, so outputs reproduce byte-for-byte):

    python -I proposals/103-g-moments-nonproduct-measures/s1_wick_pushforward_D2.py
    python -I proposals/103-g-moments-nonproduct-measures/s2_selection_bifurcation.py
    python -I proposals/103-g-moments-nonproduct-measures/s3_generalD_checks.py

Expected invariants (from the DONE lines and key lines of the .out files):
- s1 ends "S1 DONE"; invariants: Bessel reldiffs 0.00e+00 / 2.48e-15 /
  0.00e+00; rho=0 reduction max 3.94430452610505902705864282641e-31; both
  normalization lines exactly 1.0; "equal-variance form ... exact: True";
  "f(1/2) ... == 1/sqrt(1-r^2): True"; MC Wick-moment reldevs <= 8.20e-03;
  Laplace reldev 1.68e-04; MC E[s2] r=0 equal var 0.66619 (flat value 2/3).
- s2 ends "S2 DONE"; invariants: f-prime at 1/2 equals 0; monotonicity
  derivative 6*r**2*(1 - r**2)/(-4*r**2*z + 1)**(5/2); vertex slope 6*r**2 - 2;
  "rhat* = 0.408248290463863"; argmax rows "0.50   0.00000" and
  "0.70   0.09909"; E[s2]-2/3 values 0.0 / -0.01874823366 / -0.04228872334 /
  -0.09209759738; quadrature/MC coincidence ratios within 6e-3 of 1.
- s3 ends "S3 DONE"; invariants: "matches (D-1)!/(G (sum p_i/g_i)^D): True" for
  D=2 and D=3; "closed form 1+3t^2+2t^3 match: True"; t=0.5 moment reldev
  6.01e-04; "t=0.0: MC E[s2]=0.50003" within MC noise of 0.5, "t=0.5: 0.47725"
  (uniformity shift).
- Hygiene: python -I proposals/103-g-moments-nonproduct-measures/hygiene_103.py
  -> "HYGIENE PASS", exit 0 (hygiene_103.out).
- Splice simulation: python -I
  proposals/103-g-moments-nonproduct-measures/simulate_apply_103.py
  -> "SIMULATION PASS", exit 0; PRE asserts 801632/e37ca5385996df34/3868/0/none;
  PIN count 1; POST written only to scratch/103_sim_post.tex
  (simulate_apply_103.out).
