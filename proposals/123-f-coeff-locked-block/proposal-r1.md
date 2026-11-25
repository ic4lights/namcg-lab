# Proposal 123-f-coeff-locked-block, round 1

## Result

For a named Alternate-scope truncation of Problem F (Presentation B field
content with imposed local Lorentz symmetry, the locked frame, a fixed
background metric per Assumption ass:aux-metric, a stated sector list, and a
named proper-time scheme), the weighted sector sum of Theorem thm:Geff is
evaluated at the curvature-linear a_1 level: the diffeomorphism Faddeev--Popov
ghost in harmonic (de Donder) gauge contributes, per sector, the proper-time
datum a_1(ghost fibre) = (4/6 + 1)R = (5/3)R with ghost weight -2 against the
recorded sector-sum convention; the truncated counts and curvature-linear
coefficient are N0_trunk = 18 + n_K (ghost count shift -8) and
A1_R = 16(1/6 - Q) + n_K(1/6 - Q_K) - 5/3 - e_h; at Q = 1/6 and n_K = 0 the
residual A1_R = -5/3 - e_h persists and vanishes only for e_h = -5/3, so the
recorded Q = 1/6 vanishing is a block-level statement that does not extend to
the ghost-completed truncation; the windowed a_1 coefficient is derived with
the recorded threshold window J for the massive block and Lambda_UV^2 - mu^2
for each massless sector. All identities were verified symbolically
(scripts 1-3 below, green captures, byte-reproducible). The paragraph closes
nothing: D, D1, F, N remain OPEN and PROGRAMME-CONDITIONAL, the curvature-
squared coefficients W_C and delta_W are not fixed, and the ghost a_2
connection-curvature terms are not evaluated.

## Target and status

- Problem: F (coefficients A, B, C), Appendix H, chapters/
  appH-microscopic-proofs.tex, section sec:status-F (live bytes at pin
  d2af19df0f99..., 863,831 B; F section spans live lines 1995-3221).
- Current status (verbatim from the live ledger paragraph, live L1998-2006):

      \paragraph{Ledger label.}
      Status: OPEN. Priority: CRITICAL PATH. Completion:
      PROGRAMME-CONDITIONAL. Reduced-scope result: treating
      \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy
      the matrix-derived criterion.

      The conditional, truncated heat-kernel identity is
      Theorem~\ref{thm:Geff}; it is not a computed \(A,B,C\)
      parameterization or physical value of \(G_{\mathrm{eff}}\).
- Missing step (verbatim, live L2008-2015):

      \paragraph{Missing step.}
      Specify the gauge-fixed fluctuation, Goldstone, diffeomorphism-ghost,
      and local-Lorentz-ghost operators and weights; per-sector proper-time
      limits; massive threshold functions if masses are resummed; the
      continuation; and the finite-counterterm scheme. Then evaluate the
      weighted \(a_1\) and curvature-linear \(a_2\) contributions in that
      scheme. Until this is completed, Problem~F remains open, and the
      asserted \(N_{\mathrm{eff}}=+2\) count does not close it.

- Scope of this package: Alternate-scope, per the ch17 paragraph
  "Alternate scope: model work outside the critical-path sequence"
  (chapters/ch17-agenda.tex live L678-686), whose operative clause is:
  "Taking Presentation B with imposed local Lorentz symmetry (D2), an
  externally justified boundary result (G-external), or
  G_{\mathrm{eff}} as an input may make a scope-limited Presentation-B model
  calculable and testable, for example by specifying full quadratic and ghost
  operators and computing Problem F for a stated truncation. Such work leaves
  Problems D, F, G and the matrix-derived completion criterion open, must
  name its imposed premises, and is not a step in the sequence above."
  The payload names its imposed premises and makes no critical-path status
  claim. Classification for the critical-path ledger: PROGRAMME-CONDITIONAL
  partial input to the per-sector missing-step items (ghost operator and
  weight, per-sector proper-time limits, a_1 weighted sum); the Goldstone and
  local-Lorentz-ghost operators, the continuation, a_2 beyond the recorded
  block endomorphism data, and any matrix-derived field content remain open.
- Dependencies: consumes (does not rederive) the recorded H-block threshold
  window J and mass-resummed data of the F-section paragraph "Mass-resummed
  curvature threshold for the Hermitian block" (live L2124+) and the recorded
  Upsilon = A_1/(2 W_C) data of the locked-block spin-two window paragraph in
  the N section (live L4068-4126), whose closer reads (verbatim, live bytes):
  "for the locked block, no zero-free region or ghost-freedom statement is
  made for any massive sector, and no status label is changed; the ledger
  entries of Problems~F and~N are unchanged and both stay OPEN."

## Source reading

digest + targeted reads. Files read in full or in narrow ranges at live pin
d2af19df0f998ce150c12ea11af9ea8c0387435f / 863,831 B (STEP-1 check passed
this session): appH-microscopic-proofs.tex L1995-2021, L3214-3224, targeted
greps in L1995-3221 (paragraph-title list, closer register, recorded Q = 1/6
and Upsilon tokens), L4068-4126 (121 paragraph, tails and greps);
ch17-agenda.tex L678-691; label-definition counts across chapters/*.tex for
the 13 whitelist labels (each defined exactly once in .tex sources; the
second grep hit per label is a stale .aux file). No file was unreadable. No
external literature is used or cited by the payload (payload forbids \cite by
hygiene check); standard facts invoked (Berezin Gaussian integral,
minimal-Laplace a_1 formula) are re-verified symbolically in the scripts
rather than imported by citation, so there are no unverified citations.

## Research and reasoning

Truncation and named premises (all supplied, none derived): Presentation B
field content with imposed local Lorentz symmetry; the locked frame; fixed
background metric (Assumption ass:aux-metric); sectors: Hermitian block H
(16 real components, O_H = -nabla^2 + E, E = lambda v^2 + Q R_E, m^2 =
lambda v^2 of eq:V), n_K retained real scalars with E_K = Q_K R_E, tensor
block supplied as a Laplace-type input (10 symmetric-tensor components,
E_ten = e_h R_E), and the diffeomorphism ghost supplied as an infrared input
as recorded in the pointwise gauge-sector Faddeev--Popov paragraph of
sec:status-D. The internal and local-Lorentz Faddeev--Popov determinants of
that paragraph are pointwise endomorphism factors in a zeroth-order gauge and
are excluded from the kinetic sector sum (stated, not claimed as derived).

Scheme (named, not derived): harmonic (de Donder) gauge F^mu = g^{ab}
Gamma^mu_{ab} for the diffeomorphism sector; weights relative to a real
bosonic determinant per eq:appA-sector-sum; per-sector proper-time limits
s_min = Lambda_UV^-2, s_max = mu^-2 of eq:appA-Wexp; massive block carries
the recorded window J(lambda v^2; Lambda_UV^-2, mu^-2), massless sectors
carry Lambda_UV^2 - mu^2; no further local finite counterterm at this order.

Derivations (symbolically verified; script 1 =
verify_ghost_op_123.py, script 2 = verify_bookkeeping_123.py, script 3 =
verify_threshold_window_123.py):

1. Ghost operator and a_1 datum (script 1). Linearizing
   F^mu[g + eps L_xi g] at eps = 0 gives
   M xi^mu = g^{ab} nabla_a nabla_b xi^mu + R^mu_nu xi^nu in the curvature
   conventions of eq:christoffel--eq:riemann (Wald signs as recorded in
   ch02), principal symbol g^{ab} delta^mu_nu, overall sign calibrated by the
   unit sphere at R = +2 (SPHERE_R check). Hence the positive Euclidean
   operator -M is Laplace-type with E_gh = -Ric, and with the recorded
   a_1 = tr(R/6 - E) of eq:appA-a1 the ghost fibre carries
   a_1 = 4R/6 + R = (5/3)R. (Independent hand check this session:
   tr((R/6) id_4) = 4R/6; tr(-E_gh) = tr(Ric) = R; sum (5/3)R.)
2. Ghost weight (scripts 1-2). Grassmann Gaussian integration gives
   integral d(cbar) dc exp(-cbar M c) = det M exactly, checked at 2x2 and
   3x3 (BEREZIN_DET2/DET3); against eq:appA-sector-sum the ghost weight is
   -2 (WGHOST_M2), consistent with the recorded "ghost operator of weight
   (-2)" in appH (checker REC_GHOSTM2W).
3. Counts and curvature-linear coefficient (script 2). With weight -2 and 4
   components the ghost shifts the constant count by -8 (DELN0_GHOST), so
   N0_trunk = 16 + n_K + 10 - 8 = 18 + n_K (N0_TRUNK), and
   A1_trunk = 16(1/6 - Q) + n_K(1/6 - Q_K) + (10/6 - e_h) - 10/3 =
   16(1/6 - Q) + n_K(1/6 - Q_K) - 5/3 - e_h (A1_TRUNK; independent hand
   check this session: tensor 10/6 - e_h; ghost weight -2 x (4/6) = -4/3 from
   the R/6 term and -2 x (+1) = -2 from tr E, total -10/3). The windowed
   coefficient of R_E in the sign convention of the block bookkeeping
   paragraph is
   -(1/(32 pi^2)) [ 16(1/6 - Q) J(lambda v^2; Lambda_UV^-2, mu^-2)
                    + (n_K(1/6 - Q_K) - 5/3 - e_h)(Lambda_UV^2 - mu^2) ]
   (CR_WINDOWED). Convention controls pin the normalization to the recorded
   formulas: CTRL_BOSON (single boson: -N0/(192 pi^2)(Lambda_UV^2 - mu^2)),
   CTRL_Y10 (recorded Upsilon = 10 from A_1 = N0/6 and W_C = N0/120), and
   CTRL_HBLOCK_A1/A2 (recorded H-block A_{1,R,H} = 16(1/6 - Q) and
   A_{2,R,H} = -lambda v^2 A_{1,R,H}).
4. Q = 1/6 vanish structure (script 2). At Q = 1/6, n_K = 0:
   A1 = -5/3 - e_h (QCONFORMAL), zero iff e_h = -5/3
   (QCONFORMAL_ZERO_IFF; A1 = 1 at Q = Q_K = n_K = e_h = 0, matching
   16/6 - 5/3 = 1). This sharpens the recorded statement whose live text
   already reads "Both coefficients vanish at Q = 1/6; this concerns only
   this block's R_E-coefficient ...": the vanishing does not extend to the
   ghost-completed truncation, where the ghost endomorphism leaves -10/3.
5. Threshold/window identities (script 3; consumes the recorded J definition
   and Upsilon data, does not rederive them): J0_MASSLESS
   (J(0; Lambda_UV^-2, mu^-2) = Lambda_UV^2 - mu^2), J_SERIES (small-mass
   J = (Lambda_UV^2 - mu^2) - m^2 ln(Lambda_UV^2/mu^2) + O(m^4 ln m^2)),
   MU_ZERO_T1 squeeze form, MU_ZERO_J, UPSILON_H
   (windowed 10 J/Lambda_UV^2 -> 10(e^-y - y E_1(y)), y = lambda v^2 /
   Lambda_UV^2), UPSILON_DER (derivative -10 E_1(y) < 0), UPSILON_Y0 (y -> 0
   limit = recorded universal 10), POLE_RATIO, Q16_WINDOWED.

Invalid-inference guards honored: no A, B, C comparison (eq:Geff-structure)
is made, no G_eff value is produced, W_C and delta_W are not fixed (ghost
a_2 curvature-squared / connection-curvature terms of eq:appA-a2 on the
tangent bundle are not evaluated), the continuation and Lorentzian sign are
not fixed, and no status label is changed anywhere.

## Claim classification

- Established identities (symbolic derivations within stated conventions;
  scripts 1-3 reproduce): ghost linearization M = Lap + Ric with principal
  symbol and sphere-calibrated sign; a_1(ghost fibre) = (5/3)R from the
  recorded a_1 formula; det-from-Grassmann and weight -2; N0_trunk = 18 + n_K
  and DELN0_GHOST = -8 (count arithmetic of the stated sector list);
  A1_trunk identity; QCONFORMAL values; threshold/window identities in item
  5 (identities in the recorded J and Upsilon forms).
- Conditional derivations under the named truncation and scheme (harmonic
  gauge, Presentation B content, supplied Q, Q_K, e_h, n_K, Laplace-type
  tensor block, ghost as infrared input, recorded proper-time windows, no
  further local finite counterterm at this order): the windowed a_1
  coefficient CR_WINDOWED; the Q = 1/6 non-extension statement; the
  per-sector a_1 datum as a contribution to Problem F's sector sum.
- Inputs (supplied premises, none derived here): Presentation B content with
  imposed local Lorentz symmetry; locked frame; fixed background metric;
  sector list and the numbers Q, Q_K, e_h, n_K; tensor block Laplace-type
  form; ghost as infrared input; harmonic-gauge choice; window scheme.
- Excluded, not claimed: DELRHO = +8(Lambda_UV^4 - mu^4)/(64 pi^2) is
  computed inside script 2 but EXCLUDED from the payload because no 64 pi^2
  convention occurs anywhere in chapters/ (rule 8 of CLAUDE.md, no invented
  numerals; journal milestone 24b DELIBERATE SCOPE CHOICES). W_C, delta_W,
  ghost a_2, the continuation, the Lorentzian sign, A/B/C comparison, any
  G_eff value: not evaluated, not claimed.
- Unresolved (F's original target): the same-sector data with matrix-derived
  content and derived gauge fixing, the remaining missing-step items listed
  verbatim above, and the a_2 curvature-squared evaluation.

## Proposed changes

File: chapters/appH-microscopic-proofs.tex (integrator-only edit; this
proposal does not edit it).

- Landing anchor (live L3220, final sentence of the final F-section
  paragraph; VERBATIM from live bytes, occurrence count of
  anchor + CRLF + CRLF = 1, verified by generator ANCHOR_UNIQUE and checker
  ANCHOR_UNIQUE at this session's re-run):

      These statements are for the hypotheses and the channel convention stated here; they retire the recorded item on the response of the fibre levels to \(ar h\) only for this channel component, they change no status label, and Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.

- Boundary: the anchor sentence ends at live L3220; it is followed by a blank
  line and then "\section{Problem G: HBEV}" at live L3222. All existing text
  is kept; nothing is replaced or removed.
- Insertion: exactly one \paragraph{...} block, inserted after the anchor
  paragraph, via the canonical convention
  replace(anchor + CRLF + CRLF, anchor + CRLF + CRLF + payload + CRLF, 1).
- Payload (payload-123.txt, sha1[:12] 5548ee218f2c, 5,488 B incl. single
  trailing CRLF, one line, ASCII, no \label/\cite/$/\begin/\end/\[/\],
  braces balanced, all refs inside the verified whitelist):

      \paragraph{Alternate-scope weighted sector data for the locked inventory in harmonic gauge (conditional; Alternate-scope; not closure).} Pursued under the Alternate-scope paragraph of Chapter~\ref{ch:agenda}, this paragraph evaluates the weighted sector sum of Theorem~\ref{thm:Geff} for a stated truncation of Problem~F. Truncation and named premises: the Presentation~B field content with imposed local Lorentz symmetry, the locked frame, and a fixed background metric as in Assumption~\ref{ass:aux-metric}; sectors with kinetic operators are the Hermitian block \(H\) of sixteen real components with \(\mathcal O_H=-\nabla^2+E\), \(E=\lambda v^2+Q R_E\) with \(m^2=\lambda v^2\) of Equation~\eqref{eq:V}, a retained input set of \(n_K\) real scalar components indexed by the \(K\) labels of this section with \(E_K=Q_K R_E\), the tensor block as an input Laplace-type block of ten symmetric-tensor components with \(E_{\mathrm{ten}}=e_h R_E\), and the diffeomorphism ghost, supplied as an infrared input as recorded in the paragraph on Faddeev--Popov determinants of the pointwise gauge sectors of Section~\ref{sec:status-D}; the internal and local-Lorentz Faddeev--Popov determinants of that paragraph are pointwise endomorphism factors in a zeroth-order gauge and are excluded from the kinetic sector sum. Scheme (named, not derived): harmonic (de Donder) gauge \(F^\mu=g^{ab}\Gamma^\mu_{ab}\) for the diffeomorphism sector, weights relative to a real bosonic determinant as in Equation~\eqref{eq:appA-sector-sum}, per-sector proper-time limits \(s_{\min}=\LUV^{-2}\) and \(s_{\max}=\mu^{-2}\) of Equation~\eqref{eq:appA-Wexp}, the massive block carrying the recorded threshold window \(J(\lambda v^2;\LUV^{-2},\mu^{-2})\) of the mass-resummed paragraph of this section and each massless sector carrying \(\LUV^2-\mu^2\), and no further local finite counterterm at this order. Results (identities within the stated scheme, verified symbolically): (i)~the ghost operator \(M\xi^\mu:=\frac{\mathrm d}{\mathrm d\varepsilon}\big|_0 F^\mu[g+\varepsilon\mathcal L_\xi g]\) equals \(g^{ab}\nabla_a\nabla_b\xi^\mu+R^\mu{}_\nu\xi^\nu\) in the curvature conventions of Equations~\eqref{eq:christoffel}--\eqref{eq:riemann}, with principal symbol \(g^{ab}\delta^\mu_\nu\) and overall sign calibrated by the unit sphere at \(R=+2\); hence the positive Euclidean operator \(-M\) is Laplace-type with endomorphism \(E_{\mathrm{gh}}{}^\mu{}_\nu=-R^\mu{}_\nu\) and, by \(a_1=\mathrm{tr}(R/6-E)\) of Equation~\eqref{eq:appA-a1}, the ghost fibre carries \(a_1=(\tfrac46+1)R=\tfrac53R\); (ii)~Grassmann Gaussian integration gives \(\int\mathrm d\bar c\,\mathrm dc\,e^{-\bar c M c}=\det M\) exactly (checked at sizes \(2\times2\) and \(3\times3\)), so against Equation~\eqref{eq:appA-sector-sum} the ghost weight is \(-2\); (iii)~the truncated counts and curvature-linear coefficient are \(\mathcal N_0=18+n_K\) (ghost shift \(-8\)) and \(\mathcal A_{1,R}=16(\tfrac16-Q)+n_K(\tfrac16-Q_K)-\tfrac53-e_h\), the tensor block contributing \(\tfrac{10}{6}-e_h\) and the ghost \(-\tfrac{10}{3}\), and the windowed coefficient of \(R_E\) in the sign convention of the block bookkeeping paragraph is \(-\frac{1}{32\pi^2}\bigl[16(\tfrac16-Q)J(\lambda v^2;\LUV^{-2},\mu^{-2})+(n_K(\tfrac16-Q_K)-\tfrac53-e_h)(\LUV^2-\mu^2)\bigr]\), where the massless window is the recorded threshold at zero mass, \(J(0;\LUV^{-2},\mu^{-2})=\LUV^2-\mu^2\), and at small mass \(J=(\LUV^2-\mu^2)-m^2\ln(\LUV^2/\mu^2)+O(m^4\ln m^2)\), which reproduces the recorded fixed-window block expression; (iv)~at \(Q=\tfrac16\) and \(n_K=0\) the truncated \(\mathcal A_{1,R}=-\tfrac53-e_h\) persists and vanishes only for \(e_h=-\tfrac53\): the recorded \(Q=\tfrac16\) vanishing of the block bookkeeping paragraph is a statement about the \(H\)-block coefficient and does not extend to the ghost-completed truncation, where the ghost endomorphism leaves \(-\tfrac{10}{3}\); (v)~consuming, and not rederiving, the recorded mass-resummed window data, for the \(Q=0\) block with \(\mu\ll m\) the windowed ratio \(10\,J/\LUV^2\) of the recorded \(\Upsilon=\mathcal A_1/(2\mathcal W_C)\) tends to \(10(e^{-y}-yE_1(y))\) with \(y=\lambda v^2/\LUV^2\), whose derivative \(-10E_1(y)\) is negative and whose \(y\to0\) limit is the recorded universal \(10\). Status of items: the ghost operator, weight, endomorphism and \(a_1\) contribution, the counts and the windowed \(a_1\)-coefficient are derivations within the named scheme; the field content, \(Q\), \(Q_K\), \(e_h\), \(n_K\), the Laplace-type tensor-block form and the ghost as an infrared input are supplied premises of the Alternate-scope truncation named above; the curvature-squared coefficients of the vector ghost (the connection-curvature terms of Equation~\eqref{eq:appA-a2} on the tangent bundle) are not evaluated, so \(\mathcal W_C\) and \(\delta_W\) are not fixed for the truncation, \(\mathcal A_2\) is not evaluated beyond the recorded block data, the continuation and the Lorentzian sign are not fixed, no comparison with \(A,B,C\) of Equation~\eqref{eq:Geff-structure} is made, and no value of \(G_{\mathrm{eff}}\) is obtained; the truncation does not discharge the frame, selection or non-degeneracy inputs of Problem~D1 and supplies only part of the per-sector items of the missing-step paragraph of this section. This paragraph closes none of Problem~D, Problem~D1, Problem~F or Problem~N, all of which remain OPEN and PROGRAMME-CONDITIONAL, and it changes no status label.

- Closer-register check: the payload's status sentence ("This paragraph
  closes none of Problem~D, Problem~D1, Problem~F or Problem~N, all of which
  remain OPEN and PROGRAMME-CONDITIONAL, and it changes no status label.")
  is wording-distinct from the landing anchor ("...they change no status
  label, and Problems~C, F and~N remain open and
  PROGRAMME-CONDITIONAL.") and from the two sibling F-closer forms counted
  in live L1995-3221 ("Problems~B and~F remain open and
  PROGRAMME-CONDITIONAL.", 4 occurrences; "Problems~C, F and~N remain open
  and PROGRAMME-CONDITIONAL.", 3 occurrences) and from the 121 closer quoted
  under Target and status.
- Stale passages elsewhere: none. No other file changes. BibTeX: none (no
  citations added).
- Ref/eqref whitelist used by the payload (12 labels; each defined exactly
  once in chapters/*.tex at this pin; the generator/checker verify each used
  label is defined in appH or ch02/ch03/ch08/ch17/appA): thm:Geff,
  ass:aux-metric, sec:status-D, eq:Geff-structure, eq:V, eq:appA-a1,
  eq:appA-a2, eq:appA-sector-sum, eq:appA-Wexp, eq:christoffel, eq:riemann,
  ch:agenda. (eq:a0a1 was additionally verified in development but is not
  used by the payload.)

Splice arithmetic: POST size 869,321 = 863,831 (live) + 5,488 (payload) + 2
(join CRLF); POST sha1 (full)
704f3765797a89371fa683089b560e6a496f5df6. preview-splice-123.txt
(5f45bad05587, 6,132 B) is a splice-WINDOW sample (400 B before + payload +
200 B after, with markers), NOT a full-file preview; the full POST is
attested only by the checker POST_SHA1 check and must be recomputed
independently from live bytes by the gatekeeper and integrator before any
edit.

Compile certificate (cert-summary-123.txt): run_cert_123.py copied the build
inputs to a %TEMP% directory (repository untouched), substituted the spliced
appH with hash assertion at POST (line 1: "SUBSTITUTED appH sha1 704f3765797a
size 869321"), and ran pdflatex/bibtex/pdflatex/pdflatex: all four rc = 0;
pl2.log and pl3.log: 0 '^!' lines, 0 undefined, 0 multiply-defined; STABLE =
True; PDF produced, 3,272,848 B; CERT VERDICT: PASS. (pl1.log shows 1606
undefined references, expected pre-bibtex.) Audit files:
cert-pl3-full-123.log, cert-pl3-tail-123.txt, cert-bib-123.log.

Provenance (session history): this package spans three sessions; two
predecessor sessions died of environment context overflow. Their surviving
artifacts are exactly those tabulated in manifest.md: the script 1-3 capture
and hash history (including the 0 B truncation artifacts
out-script1-run1.txt and tmpD.txt kept as evidence of the harness cleanup
that lost the green-by-notification runA2 capture bytes), the checker
token-bug fixes made in place (r0 checker bytes not preserved), and the
run_cert_123.py in-place edit after the certificate run. This session
re-verified the STEP-1 live pin (d2af19df0f99..., 863,831 B), attempted
script 1 twice with the survivor protocol; both runs were killed at 19:18
under an explicit author fix-order (0-byte tombstones
out-script1-runC.txt/out-script1-runD.txt; see Verification scripts and
manifest.md lineage note 2), re-ran the generator and the checker deterministically
(out-gen-run3.txt, out-checker-run3.txt; payload and preview hashes
unchanged after rewrite), and wrote manifest.md (full lineage and per-file
hashes) together with this record.

## Verification scripts

All in this proposal folder. Reproduction pack (run from the folder; re-run
this session where noted):

1. verify_ghost_op_123.py (sha1[:12] 454d22922dd9, 15,256 B; sympy; run as
   plain `python verify_ghost_op_123.py`; runtime minutes). Expected:
   SCRIPT1 VERDICT PASS; emitted invariants: CG_GHOST = +1 (the residual of
   M - lap - Ric vanishes polynomially), O_GHOST_EG = -Ricci (O = -M is
   Laplace-type with E_ghost = -R^mu_nu, hence a_1 = (4/6 + 1)R = (5/3)R),
   CH_HODGE = +1 ((d delta + delta d) = -lap + Ric on 1-forms),
   PRINCIPAL_SYMBOL_OK, RICCI_TERM_NONTRIVIAL, HODGE_RICCI_NONTRIVIAL,
   SPHERE_R_CHECK (sign calibration at R = +2). The Berezin determinant
   checks and the weight -2 check are in script 2 (BEREZIN_DET2/DET3,
   WGHOST_M2). Capture status (final): NOT obtained this session. Two
   full-compute launches (runC 16:10, runD 16:19; python 18392/1452) were
   killed at 19:18 under an explicit author fix-order after ~3 h each at
   ~3.8 GB with sympy stdout fully buffered; the 0-byte files
   out-script1-runC.txt / out-script1-runD.txt (19:18:02) are kill
   tombstones. History: runA2 green-by-notification with capture bytes
   lost to harness truncation; out-script1-run1.txt is a 0 B truncation
   artifact, kept. Disposition: the gatekeeper may re-derive script 1's
   central computation (ghost-fibre a_1 = (5/3)R in harmonic gauge)
   independently per the proposal 120 verifier precedent, or re-run the
   frozen script 454d22922dd9 at its discretion; the payload claims rest
   on the symbolic identities, hand-checked independently this session,
   and on scripts 2-3, whose green captures are byte-reproducible.
2. verify_bookkeeping_123.py (sha1[:12] df307b2e7750, 9,130 B; sympy).
   Expected: SCRIPT2 VERDICT PASS with checks BEREZIN_DET2/DET3, WGHOST_M2,
   A1_TRUNK, N0_TRUNK, QCONFORMAL, QCONFORMAL_ZERO_IFF, DELN0_GHOST, DELRHO
   (internal only, excluded from payload), CR_WINDOWED, CTRL_BOSON, CTRL_Y10,
   CTRL_HBLOCK_A1/A2, and "A1 value at Q=QK=0, nK=0, e_h=0: 1". Captures:
   out-script2-run1 == run2 (877 B, FAIL, float artifacts), then run3 ==
   runC == runD (843 B, all PASS, exact rationals).
3. verify_threshold_window_123.py (sha1[:12] c0a811a2eb38, 4,855 B; sympy).
   Expected: SCRIPT3 VERDICT PASS (J0_MASSLESS, J_SERIES, MU_ZERO_T1,
   MU_ZERO_J, UPSILON_H, UPSILON_DER, UPSILON_Y0, POLE_RATIO, Q16_WINDOWED).
   Captures out-script3-run1 == run2 (380 B).
4. make_payload_123.py (sha1[:12] 25063ff68713, 10,858 B; stdlib; run
   `python -I make_payload_123.py`). Determinism re-run this session
   (out-gen-run3.txt): 8 injected controls fired; PIN OK d2af19df0f99
   863831; REFS OK used=12; LABELS OK; ANCHOR unique; PRE d2af19df0f99
   863831; PAY 5548ee218f2c 5488; POST 704f3765797a 869321; POST sha1 full
   704f3765797a89371fa683089b560e6a496f5df6; GEN VERDICT: PASS.
5. check_payload_123_r1.py (sha1[:12] 462ed5b332ac, 5,156 B; stdlib; run
   `python -I check_payload_123_r1.py`). Determinism re-run this session
   (out-checker-run3.txt, f7fa29b9253b, 1,154 B, byte-identical to
   run1/run2): all checks PASS including LIVE_PIN, PAYLOAD_HASH, hygiene +
   injected controls, REFS_IN_WL, LABELS_DEFINED, ANCHOR_UNIQUE, POST_LEN,
   POST_SHA1, NO_DOUBLE_INSERT, the REC_* manuscript-record checks (each
   consumed numeral of the payload tied to a token in live appH/ch17 bytes,
   with counter-teeth CTRL_REC_DEAD), and PAY_HAS_* payload-internal
   arithmetic literals; CHECKER VERDICT: PASS. (REC_GHOSTM2W prints twice by
   construction: dict entry plus a redundant raw-string line.)

## Decisions Taken

- Capture protocol for script 1: foreground launch with redirect to a temp
  file plus in-same-command copy to the final out-* name (journal-documented
  survivor protocol; background-launched python dies and completion cleanup
  truncates redirect targets to 0 B). Rejected: background launch (caused the
  lost runA2 capture bytes). The 0 B artifacts out-script1-run1.txt and
  tmpD.txt are kept in place as evidence of the truncation.
- Run D launched concurrently with run C after verifying script 1 is write-
  free and contains no clock/random sources (grep), so determinism of the
  cmp comparison is unaffected; rejected serial execution to fit the session
  budget after two predecessor deaths.
- DELRHO (64 pi^2 convention) excluded from the payload: the numeral
  convention does not occur in chapters/ and rule "do not invent numbers"
  forbids introducing it into the manuscript; the computation stays in
  script 2 as recorded internal data.
- Alternate-scope framing chosen (ch17 L678-686) rather than any
  critical-path progress claim, so that the named-premise requirement of
  that paragraph is met and no status implication is implied.
- Did not "fix" the two recorded artifacts: run_cert_123.py was edited in
  place after the cert run (journal-cited hash 8f8b9e78379e, disk
  f54de3d0e12e; supersede-by-copy deviation, bytes of the cert-time version
  not preserved), and the checker keeps its doubled REC_GHOSTM2W line;
  byte-freeze respected, both recorded in manifest.md lineage.
- tmpcap123-GEN.txt / tmpcap123-CHK.txt / tmpcap123-C.txt / tmpcap123-D.txt
  retained as redundant temp copies (documented in manifest) rather than
  deleted, preserving the audit trail of the capture protocol.
- Journal-quoted hash 5e64dfef8ba2 was resolved as the sha1 of the green
  capture out-script2-run3.txt, not of verify_bookkeeping_123.py
  (df307b2e7750); disk is authoritative, recorded in journal milestone 24c.

## Milestone assessment

Routine. No critical-path step is derived; the package records Alternate-
scope conditional per-sector a_1 data with the ghost completed for the named
truncation, plus the Q = 1/6 non-extension sharpening and reproducible
identity captures. No MILESTONE.md trigger is believed to apply.

## Status-label recommendation

Critical-path list re-derived from live Appendix H ledger paragraphs and the
ch17 criterion: A, B, C, D, D1, E, F, G-derived and N at the full-GR /
matrix-derived scope (D and D1 carry their own OPEN ledger entries; H, I, J
optional within stated scopes, ch17 live L688-691). This package changes no
label: expected outcome NONE. Problem F stays OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL; D, D1, C, N unchanged.

## Author decision needed

None.

## Remaining open step

To close Problem F's original target for the stated programme one would
still need, without the Alternate-scope premises: matrix-derived (not
supplied) field content, frame and sector list; the gauge-fixed fluctuation,
Goldstone and local-Lorentz-ghost operators and weights; a derived (not
chosen) gauge-fixing and counterterm scheme; the continuation and Lorentzian
sign; the curvature-squared a_2 data including the ghost connection-curvature
terms of eq:appA-a2 (fixing W_C and delta_W); and the comparison with A, B, C
of eq:Geff-structure yielding G_eff. Gating per Appendix H: the locked-frame
and selection inputs are themselves Problem D/D1 missing steps, and this
paragraph's Q = 1/6 non-extension result shows that any future vanishing
statement must carry the ghost-completed coefficient, not the block-only one.

## Special instructions for the gatekeeper

- Byte-freeze in force: payload-123.txt, make_payload_123.py,
  check_payload_123_r1.py and all verify_*.py must not be edited; verify
  hashes against manifest.md.
- Recompute POST independently from live appH at pin d2af19df0f99... using
  the canonical convention above; do NOT treat preview-splice-123.txt as the
  full spliced file (it is a 400 B / payload / 200 B window sample).
- Scope limits that must be preserved verbatim in integration: the named
  premises sentence, the "Status of items" sentence, and the closing
  non-closure sentence of the payload. The payload must not be paraphrased
  into a critical-path F claim; it is Alternate-scope per ch17 L678-686.
- Re-check anchor uniqueness against the live tree at integration time
  (another chain may have moved L3220; the checker re-runs on live bytes).
- Scripts 1-3 are sympy scripts (run with plain python; several minutes for
  script 1); the generator and checker are stdlib-only (run with python -I
  per the reproduction pack). pl1's 1606 pre-bibtex undefined references are
  expected; the certificate verdict rests on pl2/pl3 zeros.
- DELRHO and the ghost a_2 data are deliberately absent from the payload;
  their presence in script 2 output is not a manuscript claim.
