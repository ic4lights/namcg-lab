# Proposal 128-f-eh-locked-tensor, round 1

## Result

Under hypothesis H1 - the ten-component tensor block of the locked action is the quadratic
Einstein-Hilbert action of the metric sector about the fixed background of
Assumption~\ref{ass:aux-metric}, gauge-fixed by the harmonic functional
F^a = g^{bc} Gamma^a_{bc} named in the Alternate-scope truncation paragraph (appH line 3224
of the live file) - the package derives, exactly and symbolically, the value of the
matter-curvature vertex of the block:

  tr K = (29/6) R_E        (total-fibre-trace convention, Equations eq:christoffel-eq:riemann,
                            unit-sphere calibration R = +2)

where K is the fibre endomorphism extracted from the quadratic Einstein-Hilbert density at a
point where the background Gamma vanishes (constant-fibre Hessian). It further proves the
exact structural reduction

  e_h = 29/6 + sigma_gf + sigma_pt,

where sigma_gf = tr E_gf / R_E is the zero-order (curvature-linear) trace of the named
harmonic gauge fixing, and sigma_pt is an addition by curvature-linear endomorphisms whose
fibre bilinear form vanishes on the nine-dimensional traceless fibre, classified exactly
among self-adjoint curvature-linear natural additions as span{H -> g(Ric:H),
H -> (Ric) tr(H) g, H -> R g tr(H)} with fibre traces R_E, R_E, 4 R_E. Consequently
e_h is determined by the tensor-block data of H1 IF AND ONLY IF both remainder terms are
fixed, and no flat-background datum can fix either (they vanish with the curvature into the
common Fierz-Pauli flat limit). Consuming the reduction in the Alternate-scope paragraph:
its condition (iv) (Q = 1/6, n_K = 0 vanishing) becomes the explicit requirement
sigma_gf + sigma_pt = -13/2 (under strict H1, sigma_pt = 0, so sigma_gf = -13/2 remains a
concrete computable single real). Success tier (rule 6): derived constant + conditional
derivation with every hypothesis named + honest iff reduction evaluated as far as it goes.
Nothing is closed; Problem F remains OPEN.

Convention note (review-123-r1 finding 1): all value claims here use the TOTAL-TRACE
reading tr E_ten = e_h R_E (the reading used by the item-123 record and its script 2). The
per-component convention of appH lines 2093-2114 would give 10/6 - e_h for the a1
coefficient; no number in this package is stated in that convention.

## Target and status

- Problem: Appendix H, Problem F (live chapters/appH-microscopic-proofs.tex lines
  1997-3225, file pin 6839a5cab30e / 883075 B): "Status: OPEN. Priority: CRITICAL PATH.
  Completion: PROGRAMME-CONDITIONAL."
- Frontier edge: F.eh-locked-tensor - derive the value of e_h := tr E_ten / R_E (total fibre
  trace reading) from the tensor-block endomorphism of the locked action, so the Problem-F
  a1 evaluation and the windowed coefficient (item-123 record, appH line 3224) consume a
  derived input rather than a stated parameter.
- Dependencies: item-123 Alternate-scope bookkeeping (A1_R = 16(1/6-Q) + n_K(1/6-Q_K)
  - 5/3 - e_h, ghost a1 = 5R/3 at weight -2, N0 = 18 + n_K); the ghost sector is a RECORD
  INPUT not re-derived (the record stated E_gh = -Ric is only reproduced, GHOST_A1_COEFF
  = 5/3); eq:christoffel/eq:riemann conventions.
- Classification: PROGRAMME-CONDITIONAL. The package converts the supplied parameter e_h
  into a derived matter kernel 29/6 plus two named remainder objects; the original target
  (the value of e_h) remains OPEN. DERIVED: only the H1-matter-kernel half.

## Source reading

digest + targeted reads. The digest was STALE for appH (dirty tree, journal line 2), so
LIVE targeted reads were used: appH 1997-2265 (Problem F entry), appH 3216-3225 (item-123
Alternate-scope paragraph, line 3224), appH 2485-2530 (EH-not-generated paragraph),
appH 2093-2114 (per-component convention), ch17-agenda 395-430, ch03 1-120, ch07 1-90 and
130-175, ch01 140-200, ch02 38-70, appA 55-150, review-123-r1/r2 relevant ranges,
proposal-123 r2 e_h lines, verify_bookkeeping_123.py e_h lines (READ ONLY), frontier.yaml
F.eh-locked-tensor and F.a2-windowed entries, reports/ledger.md F section. All labels used
by the payload were verified present exactly once across chapters/*.tex:
ass:aux-metric, eq:christoffel, eq:riemann, eq:FP, sec:ch1-checklist (and the wider label
set in journal cont.3). No unreadable files. No literature was imported: no external
citation is used or needed in the payload (nothing cited, so nothing to verify externally).

## Research and reasoning

Method (jet/constant-fibre extraction, exact symbolic, script 2 verify_eh_128.py).
Background gbar = e^{2w} delta, w = (1/2) C_{mu nu} x^mu x^nu, C symmetric constant
(10 free parameters = 10 independent background-curvature data at x=0: NOT a toy in the
relevant sense - the generic 20-component curvature is restricted, see the naturality
argument below), perturbation g = gbar + eps H, H a constant symmetric fibre direction.

1. At x=0: gbar = I, d gbar = 0, and since Gamma depends only on g^{-1} and d g with
   d H = 0 and d gbar|_0 = 0, Gamma(g)|_0 = 0 EXACTLY for all eps. Hence the Gamma-Gamma
   part of Riemann vanishes at 0 at all orders and d_l Gamma^r_{mu nu}|_0 =
   C_{l nu} delta_{mu r} + C_{l mu} delta_{nu r} - C_{l r} delta_{mu nu} exactly.
   Outputs RIC0_OK = True for Ric0 = -2C - (tr C) I and R0 = -6 tr C, signs calibrated by
   script 1 against the manuscript conventions (eq:christoffel, eq:riemann):
   SPHERE_R = 2, Ric_11|_{S^2} = sin^2(theta) (unit sphere R = +2), and the a1 identity
   a1 = tr(R/6 - E) (GAUGE_a1_S2 = 8/3, ratio 4/3 reproduces the dim-shrunk 123 ghost a1).
2. The eps^2 term of the density at x=0 has the form (1/2) H (N + E) H; E is a
   multiplication operator, so the fibre Hessian at 0 of the quadratic density in constant
   fibres IS the (symmetrised) E-kernel: E = Hess_fib(dens2)/2. F0CHECK = True checks the
   pure-trace consistency EH_SCALAR_OK = 0 (the E-kernel acts naturally on trace
   directions). GF_SHIFT = 0: F(gbar + eps H)|_0 = g^{ab} Gamma|_0 = 0 exactly to all
   orders in eps (constant H), so the gauge-fixing density contributes NOTHING to the
   constant-fibre H^2 kernel at 0; the gauge fixing enters E only through the zero-order
   remainder left after the first-order-operator residue (proportional to C dot dH, which
   is nonzero at 0) is removed in the Laplace-form reduction. That remainder is not
   evaluated here and is exactly sigma_gf R_E.
3. Derived value: EH_LICH = tr K / R0 = 29/6, C-independent (a natural scalar linear in
   curvature; by naturality R is the only such scalar, so the value holds for the whole
   class, conditional on the Laplace-type curvature-linear hypothesis in H1). Three
   independent audits, all green (out-e_h-128.txt, rc = 0):
   (a) exact decomposition of the fibre endomorphism on the six curvature-linear natural
       structures Rm., Ric., .Ric, g(Ric:.), (Ric)tr(.)g, R g tr(.) with structure fibre
       traces STRUCT_TR = {-1/2, 5/2, 5/2, 1, 1, 4} (hand-verified independently by
       projector contractions); the decomposition solves exactly at two random C-points
       (E_DECOMP; residual zero by construction of linsolve over the 100 component
       equations); the one free parameter is the ric1/ric2 split, the kernel direction
       ric1 - ric2 of the structure map on symmetric fibres, which has zero bilinear form
       and zero fibre trace, so every trace statement is solution-independent;
       EH_COMBO_CHECK = 0 twice (the structure combination reproduces 29/6);
   (b) FIBRE_TRACE_FROM_BASIS: the trace computed on an orthonormal fibre basis (6
       off-diagonal units + Gram-Schmidt diagonal triple) equals tr E exactly, DELTA = 0;
   (c) the traceless-fibre (TT) quadratic form of K: E_TTQF / R = 9/2, and
       TT_PAIRING_INVARIANT = True True (g(Ric:.) and R g tr(.) pair to zero on the
       traceless fibre; (Ric)tr(.)g vanishes trivially since tr H = 0 there).
   Rank note: on this family the six structures have rank 5 on symmetric fibres; the
   missing direction is the zero-bilinear-form one, which is why linsolve (not a square
   solve) is used and why a single free parameter is expected, not a defect.
4. Structural completion (sigma_pt): among self-adjoint curvature-linear natural
   endomorphisms (built from g, Rm, Ric), an addition pairing to zero on the
   nine-dimensional traceless fibre must have vanishing Rm., Ric., .Ric, (Ric)tr blocks
   (each has nonzero TT pairing on the family), leaving exactly the three pure-trace
   structures listed, fibre traces (1,1,4) R_E. These leave the traceless-fibre
   propagation untouched and shift e_h by an unrestricted real.
5. Reduction and consumption. By (2), (3), (4), e_h = 29/6 + sigma_gf + sigma_pt. The
   record tensor a1 piece is 10/6 - e_h (total-trace reading; script 3 re-derives the
   whole 123 sector algebra with e_h symbolically: A1_MATCH_123, N0_MATCH_123,
   WINDOW_MATCH all True), so the tensor-plus-ghost trunk at Q = 1/6, n_K = 0 is
   -5/3 - e_h = -13/2 - sigma; condition (iv) (vanishing) becomes sigma = -13/2
   (out-ehsum-29-6.txt: A1_derived_Q16nK0 = -13/2 at sigma = 0, COND_IV_HOLDS = False;
   controls: e_h = 0 gives -5/3, e_h = -5/3 gives 0 with COND_IV_HOLDS True). Cross-check
   inside script 2: Q16_TRUNK = 8/3 - e_h = -13/6 (scalar piece 16/6 kept) matches the
   bookkeeping identity.
6. Honest iff: e_h is determined by the H1 block data iff sigma_gf and sigma_pt are
   fixed. Flat data cannot fix them (curvature-suppressed into the common Fierz-Pauli
   flat limit, eq:FP; consistent with the recorded statement that tensor-block terms
   beyond the displayed action are an additional input). Under strict H1 (no extra
   endomorphism terms) sigma_pt = 0 by definition and the single open datum is sigma_gf,
   computable in principle from the zero-order part of the Laplace reduction of the named
   gauge fixing at the same class of points; the record condition (iv) would then be the
   assertion sigma_gf = -13/2.

Comparison with the original target: the dispatch asked for a value/formula for e_h or a
conditional derivation with hypotheses named, or an honest iff reduction. Delivered: the
derived H1 matter kernel 29/6 (total-trace convention), the exact remainder
decomposition, and the iff; the full numerical value of e_h is NOT obtained, and no claim
here closes Problem F or supplies a1 without the remaining inputs.

## Claim classification

- tr K = (29/6) R_E under the H1-kernel definition, on the conformal family, with the
  named conventions: DERIVATION (exact symbolic; script 2; audits (a)(b)(c)).
- Extension of the trace value from the 10-parameter conformal family to the H1 class:
  CONDITIONAL (standard naturality: the trace is a curvature-linear natural scalar; R is
  the only such scalar in dimension 4; conditional on H1 Laplace-type curvature-linear
  endomorphism).
- Gamma-Gamma vanishing at 0 and d Gamma at 0 identities: ESTABLISHED IDENTITY (exact).
- GF_SHIFT = 0 (zero constant-fibre kernel contribution of F^2 at Gamma=0 points):
  ESTABLISHED DERIVATION (exact; F(gbar + eps H)|_0 = 0 to all orders for constant H).
- "The gauge fixing enters e_h only through the Laplace-reduction zero-order remainder":
  CONDITIONAL (mechanism stated with its hypothesis: the block is Laplace-type; the
  remainder is not evaluated, and the package asserts nothing about its value).
- Pure-trace span = {g(Ric:.), (Ric)tr(.)g, R g tr(.)} and their fibre traces (1,1,4) R_E:
  DERIVATION (self-adjoint curvature-linear natural algebra; TT-pairing non-degeneracy of
  the complementary structures tested on the family; the middle structure vanishes
  trivially).
- e_h = 29/6 + sigma_gf + sigma_pt: CONDITIONAL consequence of H1 + the Laplace-type
  assumption (definitional given those hypotheses and the definitions of the sigmas).
- e_h determined iff the sigmas are fixed; flat data insufficient: DERIVED (from the
  structure of the decomposition).
- Ghost a1 = 5 R_E/3: INPUT from the record, only REPRODUCED (GHOST_A1_COEFF = 5/3 from
  the record stated E_gh = -Ric, weight -2, 4 components); the ghost operator itself is
  not re-derived (a previous draft asserted -delta_xi F = box xi + Ric xi; that assertion
  is WITHDRAWN from the payload and unverified here).
- H1 itself (tensor block = gauge-fixed quadratic Einstein-Hilbert): STATED INPUT
  (conjecture relative to the locked action; the manuscript records that the
  Einstein-Hilbert term is not generated by the matrix completion - appH 2485-2530 - so
  H1 is an additional hypothesis, and the payload says so).
- sigma_gf, sigma_pt values; condition (iv) holding: UNRESOLVED.
- Numerics 29/6, 9/2, -13/2, -13/6, 5/3: all reproduced by the scripts (no number
  asserted that no script outputs; 9/2 and -13/6 appear only in scripts and this
  proposal; the payload 5R_E/3 is the record own value, reproduced).

## Proposed changes

File: chapters/appH-microscopic-proofs.tex (the ONLY file touched).

Anchor (insert immediately BEFORE it; uniqueness on live bytes pinned 6839a5cab30e /
883075: count 1, verified by script make_payload_128.py, out-make-payload-128.txt
ANCHOR_COUNT = 1):

    \paragraph{Alternate-scope weighted sector data

Boundary: the inserted paragraph precedes that line, which is line 3224 (the item-123
Alternate-scope paragraph), and stays byte-identical. Everything else in the file is
kept; nothing is replaced, deleted, or reworded; no stale passage elsewhere needs editing
(the Alternate-scope paragraph statement that e_h is a supplied parameter remains true -
the new paragraph refines, not contradicts, it).

Payload = container file proposals/128-f-eh-locked-tensor/payload-P1.txt, byte pin
sha1_12 54f62d402998 / 4200 bytes = the single line below plus a terminating CRLF CRLF
(the terminator keeps the blank-line join and makes the replace(anchor, payload+anchor)
splice satisfy POST = PRE + len(payload) exactly; verified, POST_PIN fa04730cc359 /
887275 = 883075 + 4200):

```latex
\paragraph{Tensor-block endomorphism trace in the Einstein--Hilbert completion of the locked tensor block (conditional; not closure).} Hypothesis H1 (stated, not derived): the ten-component tensor block of the locked action is the quadratic Einstein--Hilbert action of the metric sector about the fixed background of Assumption~\ref{ass:aux-metric}, gauge-fixed by the harmonic functional \(F^\mu=g^{ab}\Gamma^\mu_{ab}\) named in the Alternate-scope truncation paragraph of this section, in the curvature conventions of Equations~\eqref{eq:christoffel}--\eqref{eq:riemann} with the unit-sphere calibration \(R=+2\). Write \(e_h\) for the total-fibre-trace reading \(\mathrm{tr}\,E_{\mathrm{ten}}=e_h R_E\) of the Laplace-type endomorphism of the block used in that paragraph. Two statements hold under H1. First, the curvature vertex \(K\) extracted from the Einstein--Hilbert density at a point where the background \(\Gamma\) vanishes (the coefficient of the quadratic term in a constant fibre direction, which is the part of the block independent of the gauge fixing) obeys \(\mathrm{tr}\,K=\tfrac{29}{6}\,R_E\) exactly: this is obtained by exact symbolic expansion on the conformal family \(\bar{g}=e^{2\omega}\delta\), \(\omega=\tfrac{1}{2}C_{\mu\nu}x^\mu x^\nu\) at \(x=0\), where \(\Gamma=0\) and the symmetric matrix \(C\) supplies ten independent background-curvature data; the trace is independent of \(C\) (a natural scalar linear in curvature), the fibre endomorphism decomposes exactly on the curvature-linear natural structures \(\mathrm{Rm}\cdot\), \(\mathrm{Ric}\cdot\), \(\cdot\,\mathrm{Ric}\), \(g(\mathrm{Ric}:\cdot)\), \((\mathrm{Ric})\,\mathrm{tr}(\cdot)\,g\), \(R\,g\,\mathrm{tr}(\cdot)\) with fibre traces \(-R_E/2\), \(5R_E/2\), \(5R_E/2\), \(R_E\), \(R_E\), \(4R_E\), and the full fibre trace is reproduced basis-independently on an orthonormal fibre basis. Second, \(e_h=\tfrac{29}{6}+\sigma_{\mathrm{gf}}+\sigma_{\mathrm{pt}}\): \(\sigma_{\mathrm{gf}}=\mathrm{tr}\,E_{\mathrm{gf}}/R_E\) is the zero-order trace of the named harmonic gauge fixing, whose constant-fibre density vanishes at such a point identically (\(F=0\) there to all orders in the fluctuation) and whose contribution arises only through the zero-order remainder left after the block is reduced to Laplace form, a term not evaluated here; and \(\sigma_{\mathrm{pt}}\) runs over curvature-linear endomorphism additions whose fibre bilinear form vanishes on the nine-dimensional traceless fibre, which among self-adjoint curvature-linear natural additions are exactly \(H\mapsto g(\mathrm{Ric}:H)\), \(H\mapsto(\mathrm{Ric})\,\mathrm{tr}\,H\,g\) and \(H\mapsto R\,g\,\mathrm{tr}\,H\) (fibre traces \(R_E\), \(R_E\), \(4R_E\), the middle one vanishing on the traceless fibre trivially), leaving the traceless-fibre propagation of the block untouched. Hence \(e_h\) is determined by the tensor-block data of H1 if and only if both the pure-trace zero-order completion and the gauge-fixing zero-order remainder are fixed; no flat-background datum can fix them, since they vanish with the curvature and share the flat limit, the massless Fierz--Pauli block of Equation~\eqref{eq:FP} whose curved-background counterpart Section~\ref{sec:ch1-checklist} item 3 requires of \(T_{\mu\nu}\), consistently with the recorded statement that tensor-block terms beyond the displayed action are an additional input. Consumption: in the Alternate-scope truncation below the supplied parameter becomes \(e_h=\tfrac{29}{6}+\sigma\) with \(\sigma=\sigma_{\mathrm{gf}}+\sigma_{\mathrm{pt}}\), the tensor-plus-ghost trunk at \(Q=\tfrac16\), \(n_K=0\) becomes \(-\sigma-\tfrac{13}{2}\), and condition (iv) of that paragraph becomes the explicit requirement \(\sigma=-\tfrac{13}{2}\). The ghost coefficient \(5R_E/3\) of that paragraph is reproduced from the paragraph's own stated ghost endomorphism and is not re-derived here. Not claimed: that H1 follows from the displayed action; the separate values of \(\sigma_{\mathrm{gf}}\) or \(\sigma_{\mathrm{pt}}\); that condition (iv) holds; any \(a_1\) or \(a_2\) evaluation beyond the Alternate-scope paragraph; any closure. This paragraph closes no problem and changes no label.
```

Verified labels used by the payload: ass:aux-metric, eq:christoffel, eq:riemann, eq:FP,
sec:ch1-checklist (each exactly once in the manuscript; no new labels introduced; no
\cite added). The payload contains no status/priority/completion wording, no $ math
delimiters (display uses \( \)), no raw tabs, no bare CR/LF (hygiene controls in the
generator, all four fired on injected violations).

## Verification scripts

All run from the repository root as `python -I proposals/128-f-eh-locked-tensor/NAME`
(python 3; sympy for script 2). Reproduction pack (expected invariant outputs, all
reproduced in the captured out-*.txt files):

- verify_conventions_128.py -> out-conventions-128.txt:
  SPHERE_R = 2; SPHERE_Ric_11 - sin^2 = 0; GAUGE_a1_S2 = 8/3 with ratio 4/3;
  A1_TENSOR_R = True.
- verify_eh_128.py (11401 B, sha1_12 86e8f227ceb1) -> out-e_h-128.txt, rc = 0:
  RIC0_OK True; F0CHECK True; GF_SHIFT 0; E_SYMM True; EH_LICH = 29/6;
  EH_SCALAR_OK = 0; E_TTQF_over_R = 9/2; STRUCT_TR {-1/2,5/2,5/2,1,1,4};
  E_DECOMP exact (free ric1/ric2 split, rank-5 kernel) at 2 random C-points (seed 128);
  EH_COMBO_CHECK = 0 (x2); TT_PAIRING_INVARIANT True True; FIBRE_TRACE_FROM_BASIS
  DELTA = 0; GHOST_A1_COEFF = 5/3; Q16_TRUNK = -13/6; SCRIPT2_DONE.
  Runtime note: exact eps-polynomial truncation (Gamma is degree 2 in eps exactly for
  constant H); a naive 4x4 symbolic inverse version timed out (journal cont.3).
- verify_ehsum_128.py -> out-ehsum-29-6.txt (usage:
  `python -I proposals/128-f-eh-locked-tensor/verify_ehsum_128.py 29/6`):
  A1_MATCH_123 = True; N0_MATCH_123 = True; WINDOW_MATCH = True; COND_IV_EH = [-5/3];
  A1_derived_Q16nK0 = -13/2; SIGMA_for_cond_iv = -13/2; COND_IV_HOLDS = False; PASS3.
  Controls: out-ehsum-0.txt (e_h = 0), out-ehsum-iv.txt (e_h = -5/3, COND_IV_HOLDS True).
  This script is SELF-CONTAINED: it re-derives the 123 sector algebra without importing
  123 code. NOTE: proposals/123-f-coeff-locked-block/verify_ghost_op_123.py was NEVER
  RUN (author kill-order); only its text was read.
- make_payload_128.py -> out-make-payload-128.txt: GEN PASS; ANCHOR_COUNT = 1;
  CTRL_FIRES (True,True,True,True) (label token, bare LF, brace imbalance, raw TAB);
  occurrence asserts \tfrac{29}{6} x3, \tfrac{13}{2} x2; PAY 54f62d402998/4200;
  PRE 6839a5cab30e/883075; POST fa04730cc359/887275 = PRE+PAY.
  Generator history (journal cont.6-7): the first run emitted a literal TAB before "rac"
  in every \tfrac (Python single-backslash escape) - compile-clean but typographically
  wrong; fixed and guarded; SUPERSEDED pin 18a641ad797e/4195 must not be used.
- cert_payload_128.py -> out-cert-128.txt: the payload paragraph compiled standalone
  (amsmath article in a temp dir OUTSIDE the repository, deleted afterwards): CERT PASS,
  rc = 0, ERR_LINES = 0, 5 undefined-reference warnings = exactly the payload 5
  \ref/\eqref (expected standalone). A full manuscript build was NOT run by this agent
  (building inside the repository is outside the researcher remit); the splice is
  byte-exact (POST accounting), and the integrator scripts/build_check.py run is the
  compile certificate for the spliced file.
- journal.md: full working log including bug fixes (apply_structure multiplicity,
  Gram-Schmidt orthonormal fibre basis, linsolve for the rank-5 decomposition, the
  riem-slot permutation bug of an earlier draft, and the TAB trap above).

## Decisions Taken

- Fixed the convention to the TOTAL-TRACE reading tr E_ten = e_h R_E (dispatch convention
  trap, review-123-r1 finding 1); rejected stating values per-component (would read
  10/6 - e_h and collide with the record).
- Headline reframed from "e_h = 29/6" to "e_h = 29/6 + sigma_gf + sigma_pt": the earlier
  draft identified the constant-fibre density kernel with the full Laplace E, which is
  false - GF_SHIFT = 0 constrains only the density kernel, not the zero-order remainder of
  the Laplace reduction. Rejected alternatives: (i) asserting sigma_gf = 0 from GF_SHIFT
  = 0 (invalid); (ii) inserting an un-rederived ghost identity -delta_xi F = box xi +
  Ric xi into the manuscript (dropped; only the record own ghost datum is reproduced);
  (iii) claiming the two-structure pure-trace span (the (Ric)tr(.)g structure also pairs
  to zero on TT - the span is three structures).
- Kept the conformal family + naturality instead of a generic 20-curvature jet: cheaper,
  exactly symbolic, and the rank/audit story is verifiable; rejected full-generic (no
  gain in evidence for e_h, large runtime).
- Insertion point: immediately BEFORE the Alternate-scope paragraph (the payload says
  "below" for it); rejected after (reads worse and separates the consumption sentence from
  its referent).
- Overwrote my own round-1 stub proposal-r1.md (this file); proposal-tail-draft.md is
  superseded, kept only as a log artifact.
- Did not run 123 verify_ghost_op_123.py (kill-order); wrote self-contained script 3
  instead.

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step is closed (the e_h target remains
open with named remainders), no label changes, no new derived full-GR input. Positive
derivation-grade data (the 29/6 matter kernel + exact remainder structure) for the named
missing step F.eh-locked-tensor, at the conditional tier.

## Status-label recommendation

Re-derived from live sources: critical-path OPEN set at the current full-GR scope includes
A, B, C, D1, E, F, G-derived, N (ch17 395-430; appH Problem F ledger unchanged). Affected
labels: NONE. Problem F stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. The frontier
edge F.eh-locked-tensor is partially advanced (derived half + named residual), not closed.

## Author decision needed

None. (The routine choices - convention, insertion point, remainder naming sigma_gf /
sigma_pt, family+jet route vs generic jet - are recorded in Decisions Taken.)

## Remaining open step

To close the original target (value of e_h for the locked-action tensor block) one needs,
beyond this package:
1. H1 itself, or its replacement: which quadratic form the locked-action tensor block
   actually is (the manuscript records the Einstein-Hilbert term as NOT generated - appH
   2485-2530 - so either the matrix completion supplies the missing tensor-block terms, or
   H1 is an explicit additional input);
2. sigma_gf: the exact zero-order (curvature-linear) part of E after the harmonic
   gauge-fixed quadratic block is reduced to Laplace form, evaluated at Gamma = 0 points
   of the same family (a single computable real; the v4.1 machinery plus the first-order
   residue subtraction is sufficient; the ghost-side recheck via 123 script 2 is excluded
   by the kill-order);
3. sigma_pt: shown to vanish iff the H1 block has no extra curvature-linear endomorphism
   terms (trace-coupled R^2 / Ricci terms in the locked action would fix it instead);
4. only after 2-3: the windowed a2/a1 evaluation that consumes e_h as data (edge
   F.a2-windowed) may use e_h = 29/6 + sigma with sigma determined or retained.
Condition (iv) of the record is, after this package, the explicit claim
sigma_gf + sigma_pt = -13/2 - it is neither established nor refuted here.

## Special instructions for the gatekeeper

- Do NOT run proposals/123-f-coeff-locked-block/verify_ghost_op_123.py (author
  kill-order). Script 3 is self-contained and reproduces the 123 algebra; run it with 0,
  -5/3 and 29/6 as controls (expected A1_derived_Q16nK0: -5/3, 0, -13/2;
  COND_IV_HOLDS only at -5/3).
- Re-derive by hand: RIC0/R0 on the conformal family (Ric0 = -2C - (tr C) I,
  R0 = -6 tr C) and the unit-sphere calibration (script 1); GF_SHIFT = 0 (constant-H,
  Gamma|_0 = 0 argument); at least one STRUCT_TR value (e.g. riem -> -1/2 via the
  projector contraction P^{mu nu rs} R^r_{s mu nu}); and 29/6 via the structure
  combination at one C-point from E_DECOMP + STRUCT_TR.
- Must NOT be asserted from this package: any value of e_h beyond 29/6 for the H1 matter
  kernel; that condition (iv) holds; that Problem F or F.eh-locked-tensor is closed; any
  use of the per-component convention for the numbers here; anything about the ghost
  operator beyond reproducing the record stated datum.
- Grep the payload container for a raw TAB (expected none) and for the literal strings
  backslash-tfrac{29}{6} (3 occurrences) and backslash-tfrac{13}{2} (2) - the tab-trap
  history is in journal cont.7; re-check anchor count = 1 and POST = PRE + 4200 against
  the tree at integration time (appH may have moved after other chains integrate; the
  integrator must re-anchor).
- The spliced-file full build belongs to the integrator (scripts/build_check.py); this
  agent ran no build inside the repository and wrote nothing outside
  proposals/128-f-eh-locked-tensor/.
