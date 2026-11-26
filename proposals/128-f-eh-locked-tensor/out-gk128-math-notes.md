## GK128 PASS1 journal (math)
[START] task T0 hash gate: proposal-r1.md a32a2e7fc025/26886 OK; appH 6839a5cab30e/883075 OK; ch03 9b1de0928d53/37978 OK; payload-P1.txt 54f62d402998/4200 OK. PASS.
[START] proposal-r1.md read IN FULL (343 lines, two reads: 1-180, 180-343). Folder listed; all pins matched on first check.
## T-anchor/T5-record (live appH 6839a5cab30e)
Anchor: paragraph{Alternate-scope weighted sector data = appH line 3224, unique (grep full-file, 1 match). Live line is byte-consistent with proposal anchor quote. Insertion = immediately before it; no conflict with section Problem G at 3226-3230.
Problem F ledger verbatim (appH 2001-2004): Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. matches proposal quote.
Record content verified at line 3224: gauge F^mu = g^{ab} nabla... harmonic (de Donder) F^mu = g^{ab} Gamma^mu_{ab} NAMED exactly as proposal states; tr E_ten = e_h R_E total-fibre reading stated; A_{1,R} = 16(1/6-Q) + n_K(1/6-Q_K) - 5/3 - e_h; tensor block contributes 10/6 - e_h; ghost a1 = (4/6+1)R = 5R/3 at weight -2 giving -10/3; N0 = 18+n_K (ghost shift -8); condition (iv) = at Q=1/6,n_K=0: A_{1,R} = -5/3-e_h vanishes only for e_h = -5/3. Trunk -5/3-e_h CONFIRMED as record identity. Arithmetic: -5/3 - (29/6+sigma) = -39/6 - sigma = -13/2 - sigma; (iv) => sigma = -5/3-29/6 = -39/6 = -13/2 CONFIRMED; COND_IV_HOLDS=False at e_h=29/6 consistent (-5/3 != 29/6). Q16_TRUNK=8/3-e_h=-13/6 arithmetic OK (internal script cross-check, not a manuscript claim; exact sector partition not reconstructed).
EH-not-generated paragraph: appH ~2485-2530 + 2522-2530: within flat-scaffold class neither displayed action nor quantum corrections give linearized diff invariance / induced EH / FP block; hypotheses listed and relaxable. Also appH 2039-2041: tensor-block terms beyond displayed action are an additional input. H1 disclosure honest; hypothesis strength vs record honestly stated by proposal.
ch1-checklist item 3 (ch01 169-172): IR kinetic operator of T_{mu nu} must be Lichnerowicz/Einstein operator with m_T^2=0 - payload phrasing (curved-background counterpart of eq:FP block required of T_{mu nu}) is a fair characterization.
eq:christoffel/eq:riemann (ch02 42-63): Gamma = 1/2 g^{rho sigma}(dmu g_{nu sigma}+dnu g_{mu sigma}-dsigma g_{mu nu}); R^rho_{sigma mu nu} = dmu Gamma^rho_{nu sigma} - dnu Gamma^rho_{mu sigma} + GammaGamma - GammaGamma; R_{mu nu} = R^rho_{mu rho nu}; R = g^{mu nu}R_{mu nu}. These are the conventions used in my independent derivation below.
Labels: ass:aux-metric, eq:christoffel, eq:riemann, eq:FP, sec:ch1-checklist each defined EXACTLY ONCE across chapters/ (counted by substring on label-def). Payload uses no new labels, no cite.

=====================================================================
GK128 PASS-1 BLOCK 3 (T1): tr K = (29/6) R_E -- CLAIM-ERROR-CANDIDATE
---------------------------------------------------------------------
Independent re-derivation (my own scratch/gk128_* scripts, not researcher's):
Setup: g = gbar + eps H, gbar = e^{2w} delta, w = 1/2 x C x (j1=0 at 0,
j2[l,m,u,v] = 2C_{lm} delta_{uv}); constant-fibre H; eq:christoffel /
eq:riemann slots as in ch02 (38-70). Two implementations: full Matrix.inv
(scratch/gk128_t1.py, job bjp8s05mi, completed) and truncated inverse
I - eps H + eps^2 H^2 (gk128_t1c/t1g.py; exact through O(eps^2) since
Gamma|_0 = 0 kills all j1 terms).
CALIBRATIONS (both implementations, exact):
  R0 = -6 trC; Ric0 = -2C - (trC) I  [matches conformal critical-point
  formula Ric = (2-n)C - (trC) delta; n=2 check consistent].
RESULT (fast path, L2 = eps^2 coeff of sqrt(det(1+epsH)) R(eps)):
  L2 is S4-symmetric in (c11,c22,c33), bilinear in (h,C).
  Fibre trace by direct ON-basis identity tr E = sum_i E(B_i,B_i)
  = 2 sum_i L2(B_i), B ON basis (tr(B^2)=1):
      tr E = -18 trC = 3 * R0 exactly; 10-dim total fibre, metric-induced
      inner product -- SAME convention as record tr E_ten = e_h R_E.
  Symbolic (gk128_t1g.py): trE==3*R0 True; ==29/6*R0 False; ==6*R0 False.
  => NOT (29/6) R_E.
The asymmetric trace -105/4 c00 - 81/4(c11+c22+c33) from E10 Hessian-trace
bookkeeping in both my implementations is provably wrong (an SO(4)-scalar
trace linear in C must be proportional to trC); the ON-basis sum is exact
for any symmetric bilinear form: bookkeeping defective, not the result.
ALTERNATIVES TESTED: raw kernel -> 3 R; Lichnerowicz-type combos via
hand-verified structure traces (-1/2,5/2,5/2,1,1,4)R -> {6,-6,4,-4,...} R;
none = 29/6; half-density weights do not bridge (factor 58/9).
CAVEAT (not excluded): if their K absorbs non-minimal-kinetic-to-Laplace
reduction terms, that step is not stated and 29/6 is unreplicable as
written. IMPLICATION: if base is 3, e_h = 3 + sigma_gf + sigma_pt and
(iv) forces sigma = -14/3, not -13/2. VERDICT T1: CLAIM-ERROR-CANDIDATE
(blocking). Brute-force 2D real-exp-metric check (gk128_brute.py, job
bx12rbg1e) running at block time.
=====================================================================
GK128 PASS-1 BLOCK 4 (T2): GF_SHIFT = 0 -- CONFIRMED
---------------------------------------------------------------------
Constant H: g|_0 = delta + eps H, partial g|_0 = 0 => Gamma(g)|_0 = 0 for
ALL eps; F(g+epsH)|_0 = 0 identically => F^2 density has NO constant-
fibre H^2 kernel at x=0. CONFIRMED (established derivation).
=====================================================================
GK128 PASS-1 BLOCK 5 (T3): structure traces + pure-trace span -- CONFIRMED
---------------------------------------------------------------------
Hand re-derivation of the six self-adjoint curvature-linear natural fibre
traces (total 10-dim, delta-fibre): {Rm., Ric., .Ric, g(Ric:), (Ric)tr g,
R g tr} -> (-1/2, 5/2, 5/2, 1, 1, 4) R. Pure-trace span = {g(Ric:H),
(Ric)(tr H) g, R (tr H) g}, traces (1,1,4) R_E: CONFIRMED. 6-dim
naturality enumeration plausible, not exhaustively proved (minor).
=====================================================================
GK128 PASS-1 BLOCK 6 (T4): iff reduction -- WORDING FINDING (MINOR)
---------------------------------------------------------------------
True statement: e_h depends on the gauge sector only via the SUM
sigma_gf + sigma_pt; with sigma_gf = 0 derived, the only remainder is
sigma_pt. Payload phrasing "if and only if BOTH ... are fixed" overstates
the converse. Correct: "iff the combination sigma_gf + sigma_pt is fixed
(sigma_gf = 0 derived)". "Flat data cannot fix them": honest framing
accepted for the endomorphism part.
=====================================================================
GK128 PASS-1 BLOCK 7 (T5): condition (iv) arithmetic -- CONFIRMED
(conditionally on T1's base)
---------------------------------------------------------------------
(iv) verbatim (appH ~3224): at Q=1/6, n_K=0, A_{1,R} = -5/3 - e_h
vanishes only for e_h = -5/3. Given base 29/6: sigma = -5/3-29/6 = -13/2
exact; COND_IV_HOLDS False at e_h=29/6 consistent; Q16_TRUNK = 8/3-29/6
= -13/6 OK. If T1 (3) holds instead: sigma_target = -14/3 and payload
-13/2 is wrong. Anchor paragraph header unique at appH line 3224;
Problem F status verbatim at 2001-2004.
=====================================================================
GK128 PASS-1 BLOCK 8 (T6): tiers / rule 3 / rule 7 / hygiene
---------------------------------------------------------------------
Payload-P1.txt (mine, 4200B): CRLF x2, LF-only 0, TAB 0, tfrac29/6 x3,
tfrac13/2 x2, no process language, no label, 5 ref, disclaimers present;
matches declared counts. Rule 3 no closure wording: OK. TIER
MISSTATEMENT: 29/6 chain labelled DERIVATION fails independent
reproduction (T1) -> unsupported until researcher supplies the operator
recipe. H1 payload framing stays conditional vs appH 2485-2530 (EH not
generated): acceptable. ch01 item-3 characterization fair.
=====================================================================
GK128 PASS-1 BLOCK 9 (T7): total-trace convention -- NO ARTIFACT
---------------------------------------------------------------------
trE = -18 trC used 10-dim metric-induced ON fibre basis -- same total-
fibre convention as record e_h. Ghost 5R/3 INPUT not re-derived. 3 vs
29/6 is not a convention artifact.
=====================================================================
GK128 PASS-1 BLOCK 10: SOURCES READ
---------------------------------------------------------------------
proposal-r1.md 1-343; appH 1997-2131, 2485-2532, 3214-3231; ch02 38-70;
ch01 155-182; payload-P1 full. digest + targeted reads; NO full scan.
Hash gate PASS (a32a2e7fc025/26886; 6839a5cab30e/883075; 9b1de0928d53/
37978; 54f62d402998/4200). Reproduction pack LISTED, not run:
verify_conventions_128.py; verify_eh_128.py (86e8f227ceb1);
verify_ehsum_128.py {0,-5/3,29/6}; make_payload_128.py;
cert_payload_128.py. NOT run: 123 verify_ghost_op_123.py (kill-order).
