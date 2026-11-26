# Proposal 121-n-hmassive-threshold, round 1

## Result

For the Hermitian H block of the locked-vacuum bookkeeping (sixteen decoupled real
components of O_H = -nabla^2 + E, E = m^2 + Q R_E, m^2 = lambda v^2), this package
derives the mass-resummed threshold functions at curvature-squared order that the
Problem N ledger names as required input, under the Presentation-B operator hypothesis:

1. a2-threshold window: L = ln(LUV^2/mu^2) is replaced by
   L_m := E_1(m^2/LUV^2) - E_1(m^2/mu^2) in c_W and c_R; the a1 window is
   (1/6-Q) J(m^2; LUV^-2, mu^-2) with the recorded threshold J (S1-S3).
2. Upsilon_H(y) = 10[e^{-y} - y E_1(y)], y = m^2/LUV^2 (Q = 0, mu << m): equals 10 at
   y = 0 - the recorded Upsilon = 10 universality is exactly the massless limit -
   decreases monotonically to 0 (decoupling), and vanishes identically at Q = 1/6
   (S4, S10).
3. Fixed-window pole estimate |m_2|^2/LUV^2 = 10[e^{-y}/E_1(y) - y]: monotone from 0,
   equals 1 at y = e^{-(10+gamma_E)}(1+O(10^-2)); below LUV only in that narrow band (S6).
4. Momentum-dependent window ell(x;y) := int_0^1 dtau E_1(y + tau(1-tau)x): at y -> 0
   reproduces the recorded ln(1/x) + 2 - gamma_E; for mu << k << m equals
   ln(LUV^2/m^2) - gamma_E + O(k^2/m^2) (running freezes below m); branch cut on the
   negative real axis from x = -4y with logarithmic endpoint (S5, S8, S9), so the
   recorded zero-free-window statements are statements of the massless sector only.

Verification-pack finding (asserted in the verification pack, not in the manuscript):
the running-window spin-two factor 1 - x ell(x;y)/Upsilon_H(y) has no positive real zero
on the tested mass grid: sup_{x>0} x ell(x;y) <= 0.255 Upsilon_H(y) < Upsilon_H(y)
(numerical grid + limit), with derived large-x asymptotics
x ell(x;y) -> 2(e^{-y} - y E_1(y)) = Upsilon_H(y)/5 (S12). This is not a zero-free-region
claim: the S9 branch cut puts any such claim out of scope for m > 0, and the payload
asserts no pole position for any massive sector.

Not closed and not claimed: Problem N stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL
(its target is a derivation from the matrix path integral for the alpha and G_eff of
Problem F; neither is computed here for the locked block). Problem F stays OPEN (sector
sum needs the Problem D choices). D, D1, A untouched. No status/priority/completion
label is proposed or changed. No zero-free region, ghost-freedom, or massive-sector pole
claim; the local finite counterterm of Theorem thm:Geff is not fixed.

## Target and status

Problem N: control of the effective expansion (appH `sec:status-N`; section begins line
3866 of chapters/appH-microscopic-proofs.tex). Live ledger label, verbatim (lines
3869-3871):

    \paragraph{Ledger label.}
    Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label.
    Completion: PROGRAMME-CONDITIONAL.

Missing step, verbatim opening (lines 3881-3883): "Derive from the matrix path integral
that the graviton two-point function has no propagating Ostrogradsky ghost for
\(p<\LUV\), for the values of \(\alpha\) and \(G_{\mathrm{eff}}\) computed in
Problem~F".

Chapter 17 criterion passage, verbatim (chapters/ch17-agenda.tex lines 498, 503-506):
"\emph{CRITICAL PATH for the matrix-derived label; OPEN.}" ... "The target is to derive
from the matrix path integral, and not from Stelle's action~\eqref{eq:stelle}, that the
graviton two-point function has no propagating Ostrogradsky ghost for \(p<\LUV\), for the
values of \(\alpha\) and \(G_{\mathrm{eff}}\) computed in Problem~F". Completion item,
verbatim (lines 730-734): "Problem~N: Assumption~\ref{ass:EFT-a2} is discharged; there is
no propagating Ostrogradsky ghost for \(p<\LUV\) in the derived graviton two-point
function, for the values of \(\alpha\) and \(G_{\mathrm{eff}}\) computed in Problem~F,
with the region of those values in which it holds stated."

Dependencies: N consumes the Problem F outputs alpha, G_eff, delta_W (not computed here);
F's sector sum consumes the Problem D selection data. Named gaps consumed (verbatim):
- appH 4053: "sectors (massive sectors require the threshold functions of Problem~F),"
- appH 4056-4058: "They do not compute \(\mathcal W_C\), \(\mathcal A_1\),
  \(G_{\mathrm{eff}}\) or \(\delta_W\) for the locked block,"
- appH F ledger: "massive threshold functions if masses are resummed".

Classification of this package: conditional derivation (DERIVED relative to the stated
block-bookkeeping/Presentation-B hypotheses; supplies a named missing-step input of N
and F; closes nothing; not a fit, not a toy).

## Source reading

digest + targeted reads. Read in full: the Problem N section of
chapters/appH-microscopic-proofs.tex (3866-4067), the Problem F ledger passages cited
(2009-2028, 2080-2179, 2250-2330 region summaries from the prior survey), the
ch17-agenda.tex N passages (497-516, 660-663, 728-735), appA-seeley-deWitt a1/a2
equations (labels eq:appA-a1, eq:appA-a2, eq:appA-Wexp), and the payload, generator, and
verification lineage files of this folder. STEP 0 pins verified at session start:
appH sha1[:12] f5a761c55396 / 854131 bytes; anchor `\section{Problem E: signature}`
count 1 at byte 300588 (locator pin only; the insertion anchor is in Problem N, see
Proposed changes). No file unreadable. The digest was not relied on for any quoted
passage; all quotations above were re-extracted from the live tree this session.

## Research and reasoning

Conventions (verified against the live tree, mutually consistent): a1 = tr(R/6 - E)
(eq:appA-a1); per real scalar the a2 bulk is 1/120 C^2 - 1/360 EGB +
[1/72 + 1/2(1/6-Q)^2] R^2 (eq:appA-a2; re-derived symbolically, S2, and it matches the
recorded block coefficients c_C = tr I/120, c_R = 1/2 tr(1/6-Q)^2 exactly); block
contribution enters as -A/(32 pi^2)[...] (appH 2107); W_C := sum w c_C;
c_W = W_C L/(32 pi^2); Upsilon := pi/(G W_C LUV^2); 1/G_eff = A_1(LUV^2-mu^2)/(2 pi);
F(x) = 1 - (x/U)(ln(1/x) + delta_W); m_2^2 = -U LUV^2/L.

Derivation route. (i) With E = m^2 + Q R_E constant, the Seeley-DeWitt windows of
eq:appA-Wexp are proper-time integrals int ds/s^{1+k} e^{-m^2 s} between LUV^{-2} and
mu^{-2}; for k = 0 (the a2 log) this is L_m = E_1(m^2/LUV^2) - E_1(m^2/mu^2), and for
k = -1 (the a1 window) it is J(m^2) whose closed form and massless limit were recorded
and are re-derived range-wide (S1). The C^2 coefficient 1/120 is m^2- and
Q-independent because it comes from the s^2-coefficient of the flat-kernel heat
coefficient unaffected by the mass window at log order (S2). (ii) Upsilon_H =
A_1^eff/(2 W_C^eff): with W_C = (16/120) L_m/(32 pi^2) and A_1 = 16 (1/6 - Q) J(m^2)
mu-independent pieces, the ratio reduces to Upsilon_H = 60 (1/6 - Q) J(m^2)/LUV^2 =
10[e^{-y} - y E_1(y)] at Q = 0, mu << m (S4: value, monotonicity via
d/dy[yE_1-...]<0 checked numerically on the bracketed mesh, decoupling limit; S10:
proportionality to (1/6-Q), vanishing at conformal coupling - the recorded A_1 = N_0/6
for the massless minimally coupled block). (iii) The fixed-window pole
|m_2|^2 = Upsilon_H LUV^2/L_m with L_m -> E_1(y) (mu << m) gives the ratio
10[e^{-y}/E_1(y) - y], monotone increasing 0 -> 1, crossing 1 at
y* = e^{-(10+gamma_E)} = 2.55e-5 (S6). Direction: a positive H-block mass lowers
Upsilon_H below 10 while raising L_m's replacement E_1(y) above L's analogue; the pole
estimate falls below LUV only for m^2 below 2.55e-5 LUV^2, so a heavy H block is not a
candidate for the fixed-window spurious pole; combined with the recorded band
|delta_W| bound this is the quantitative content of the payload's "only in that narrow
band". (iv) The momentum-dependent window ell(x;y) = int_0^1 dtau E_1(y+tau(1-tau)x):
closed forms checked against quadrature (S5, S8), y -> 0 massless kernel
ln(1/x)+2-gamma_E reproduced, decoupling ell -> ln(LUV^2/m^2) - gamma_E for k << m,
branch cut on (-inf, -4y] with positive boundary-value jump for light masses and
logarithmic growth at the tip (S9). The cut is why no zero-free-region statement is
made: the recorded remainder-bound (boundary minimum) argument needs a kernel with no
cut crossing the slit-disc boundary; once m > 0 the cut attaches at x = -4y and lies
on the negative axis the boundary encircles.

S12 diagnosis (this round's central verification question). The v7 pack's S12 asserted
"implicit pole window within factor 2 of k=0 window", solving P = Upsilon_H(y)/ell(P;y)
by bisection on [1e-9, 100] and comparing with the frozen-window estimate
P0 = Upsilon_H(y)/E_1(y). Diagnosis (scratch/121/s12_diag_out.txt): for every tested y
in {1e-6, 1e-4, 1e-2, 1, 10} the function f(P) = P - Upsilon_H(y)/ell(P;y) is negative
at BOTH bracket ends (e.g. y = 1e-6: f(1e-9) = -0.755, f(100) = -395), i.e. the implicit
equation has NO positive real root, the bisection returned the bracket edge P = 100
(phantom), and the recorded ratios P/P0 = 132.4, 86.4, 42.5, 14.8, 10.9 measured that
phantom. The v7 check was therefore mis-specified (its premise - a root - fails); the
factor-2 statement was never a property of the object. The true statement replacing it:
sup_{x>0} x ell(x;y) < Upsilon_H(y), so 1 - x ell(x;y)/Upsilon_H(y) has no positive real
zero. Evidence: (a) no-sign-change at bracket ends, above; (b) derived asymptotic
identity lim_{x->inf} x ell(x;y) = 2(e^{-y} - y E_1(y)) = Upsilon_H(y)/5 (endpoint
Laplace: x tau(1-tau) -> x tau at both ends; int_y^inf E_1(v) dv = e^{-y} - y E_1(y)
from d/dv [v E_1(v) - e^{-v}] = E_1(v) and v E_1(v) - e^{-v} -> 0; numerically
x ell(x;y)/(Upsilon_H(y)/5) = 1.000000 at x = 1e10 for all five y); (c) grid sup
x ell/Upsilon_H = 0.2398-0.2547 << 1 on the 49-point log grid 1e-8..1e10; (d) positive
control (117 lesson): with the coupling replaced by Upsilon_H/10 the SAME bisection
finds a true root with residual < 1e-25, proving the no-root detection is not vacuous.
Honest limits: (c) is numerical on the tested grid (no proof against a narrow spike
between grid points), so the S12 statement is classified numerical/conditional; it
changes no manuscript text (the payload never mentions implicit poles; it already states
"the fixed-window pole estimate is not shown to coincide with a zero of the
momentum-dependent factor", which stands).

Second guard failure found and fixed this round: S11 (payload hygiene + reference
whitelist) had NEVER run - its regex was built from single-backslash literals, an
invalid regex escape that raises whenever the payload is present (all earlier captures
only reached "SKIP S11 payload absent"). Fixed by a chr(92) scanner plus injected
positive controls (whitelist, $, CRLF x2, label, ASCII, and a finds-the-real-refs
control). Two follow-on defects were caught by controls of the fixed check itself: a
scanner token with a spurious backslash before '{' (caught by the len(names) >= 8
control) and a CRLF control that could never fire (caught as a FAIL).

Lineage (predecessor death and this chain): gen r1 crashed with the same
backslash-literal guard defect (re.error "unbalanced parenthesis at position 6",
out-gen121-r1.txt); gen r2 clean, 5 hygiene controls fired, payload 702a60d1e5dc/3645,
PRE 854131 POST 857778 (delta = 3645 + 2 join bytes), preview fd23c0d737b0
(out-gen121-r2.txt). The predecessor died from context overflow at the generator-writing
stage with research recorded in scratch/121/notes.md; this session completed the pack.
verify v1-v7 per notes lineage; v7 S12 FAIL captured (out-verify-r6.txt, 10/11); v8
(7db94c705d69) replaced S12 with the true statement + control (scratch run 11/11,
out-verify-r7.txt); v9 (0be8a42bf726) rewrote S11 (crash -> scanner-token bug, folder
run FAIL, out-verify121-r3.txt); v10 (89ce0c564d1b) fixed the scanner (FAIL via the
wrong CRLF control, out-verify121-r4.txt); v11 (d04bf3101e0c) FINAL, folder run
TOTAL 12/12 PASS + ALL CHECKS DONE 121 with S11 ACTIVE (out-verify121-r5.txt). The old
folder verify121.py (655227e3b3f3) is archived at scratch/121/verify121_folder_pre_v8.py.
No literature route applies (sme-scout-20261114: no 2024-2026 publication computes
ghost-freedom for the induced graviton of a matrix model); no citation is used in this
package. Nothing cited that was not verified in the live tree.

## Claim classification

- S1-S3 (J identity, a2 decomposition, L_m window, E_1 series): established identities
  / derivations (symbolic + high-precision numerical range checks).
- S4, S6, S8, S10 (Upsilon_H formula, pole-ratio monotonicity and crossing, kernel
  closed forms and limits, (1/6-Q) proportionality): established identities for the
  stated kernel expressions; their USE as the block's A_1/W_C/pole data is CONDITIONAL
  on the Presentation-B operator, one block, Q constant, leading-log class, mu << m,
  k << LUV, and the window substitutions (not derived from the matrix path integral).
- S5, S7: established (U(a) closed form) and record-consistency re-check (massless
  zero counts, U_*(0) = pi/2, window -9.58 < delta_W < 10, Fmin = 0.82) - no
  correction to recorded numerics.
- S9 (branch cut presence, jump, log tip): established for the kernel; its consequence
  "zero-free-window statements are massless-sector statements" is a conditional
  statement about the recorded argument's hypotheses.
- S12 (no positive real zero of the running-window factor): conditional + numerical
  (grid sup; derived asymptotics; control). NOT a zero-free-region statement; NOT in
  the manuscript.
- S11: hygiene only.

## Proposed changes

File: chapters/appH-microscopic-proofs.tex (one insertion; nothing else in the
repository changes; bib/ untouched - no new citation).

Anchor (verified unique in the live tree, count 1, line 4064, inside sec:status-N,
between the closing sentence of the N conditional-statements paragraph and the section's
Status line): the sentence "Problems~F and~N remain open." followed by a blank line and
"\paragraph{Status.}"; the preceding kept boundary sentence is "condition on
\(\Upsilon\) and \(\delta_W\), which are outputs of Problem~F, and is not implied by the
metric being composite." All existing text is KEPT verbatim; the payload inserts after
the anchor paragraph's blank line (canonical replace of
"anchor + CRLF CRLF" by "anchor + CRLF CRLF + payload + CRLF"; PRE 854131 -> POST
857778; the folder file appH-spliced-preview.tex fd23c0d737b0 shows the exact
post-splice whole file). Verified labels used by the payload (one \label each, grepped
this session): thm:Geff (ch08-heat-kernel.tex), eq:appA-a1, eq:appA-a2, eq:appA-Wexp
(appA-seeley-dewitt.tex), eq:Smicro, eq:V (ch03-matrix-action.tex), sec:status-F
(appH); no label is defined by the payload; no duplicates introduced. The payload
closing sentence is varied from the recorded 116-120-style closers ("...are unchanged
and both stay OPEN." vs "Problems~... remain open." / "remain open and
PROGRAMME-CONDITIONAL."). Stale passages elsewhere: none - this package supersedes no
existing text.

Payload (proposals/121-n-hmassive-threshold/insert-n-hmassive-threshold.tex, sha1[:12]
702a60d1e5dc, 3645 bytes, unchanged since gen r2 - no payload edit was needed since the
false implicit-pole claim was never in it):

```latex
\paragraph{Mass-resummed thresholds in the spin-two factor
(conditional; not closure).}
Assume the hypotheses of the recorded block bookkeeping paragraph of
Section~\ref{sec:status-F}: sixteen decoupled real components of
\(\mathcal O_H=-\nabla^2+E\) with \(E=m^2+Q R_E\),
\(m^2=\lambda v^2\) from Equations~\eqref{eq:Smicro} and~\eqref{eq:V},
constant \(Q\). From Equations~\eqref{eq:appA-a1}--\eqref{eq:appA-a2}
the per-component curvature-squared coefficients are \(1/120\) for
\(C^2\) and \(\tfrac12(1/6-Q)^2\) for \(R^2\), and the
curvature-linear part of \(a_2\) is \(-m^2(1/6-Q)R\), consistently
with the recorded block data; the \(C^2\) coefficient is independent
of \(m^2\) and \(Q\). At curvature-squared order the
proper-time windows of Equation~\eqref{eq:appA-Wexp} replace
\(L=\ln(\LUV^2/\mu^2)\) in the block coefficients \(c_W\), \(c_R\) by
\(L_m:=E_1(m^2/\LUV^2)-E_1(m^2/\mu^2)\), with \(E_1\) the
exponential integral defined in Section~\ref{sec:status-F}, and the
curvature \(a_1\) window is \((1/6-Q)J(m^2;\LUV^{-2},\mu^{-2})\) with
the recorded threshold \(J\). Write \(y:=m^2/\LUV^2\). Then, for one
block with \(Q=0\) and \(\mu\ll m\),
\(\Upsilon=\mathcal A_1/(2\mathcal W_C)\) becomes
\(\Upsilon_H=10[e^{-y}-yE_1(y)]\): the recorded \(\Upsilon=10\)
universality of minimally coupled massless scalars is the \(y\to0\)
limit; \(\Upsilon_H\) decreases monotonically to zero as \(y\) grows;
and at \(Q=1/6\) the curvature window of this block vanishes, so this
block shifts neither \(1/G_{\mathrm{eff}}\) nor \(\Upsilon\) at this
order. The fixed-window spin-two pole estimate
\(|m_2|^2=\Upsilon_H\Lambda^2_{\mathrm W}/L_m\) (the recorded
\(-\Upsilon\LUV^2/L\) with windows) satisfies, for \(\mu\ll m\),
\(|m_2|^2/\LUV^2=10[e^{-y}/E_1(y)-y]\), which increases
monotonically from \(0\) and equals \(1\) at
\(y=e^{-(10+\gamma_{\mathrm E})}(1+O(10^{-2}))\): the estimate lies
below \(\LUV\) only in that narrow band. The momentum-dependent
window \(\ell(x;y):=\int_0^1\mathrm{d}\tau\,
E_1(y+\tau(1-\tau)x)\), whose \(\mu\)-window term is negligible for
\(\mu\ll m,k\), replaces \(\ln(1/x)+\delta_W\) in the spin-two
factor: at \(y\to0\) it reproduces the recorded model value
\(\ln(1/x)+2-\gamma_{\mathrm E}\), while for \(\mu\ll k\ll m\) it is
\(\ln(\LUV^2/m^2)-\gamma_{\mathrm E}+O(k^2/m^2)\), so this block's
contribution to the running freezes between \(\mu\) and \(m\). For
every \(y>0\) the window \(\ell(\cdot;y)\) has a branch cut on the
negative real axis starting at \(x=-4y\), across which its boundary
values differ and toward whose endpoint it grows logarithmically;
the boundary remainder-bound argument of the preceding paragraph
therefore does not apply on the full slit-disc boundary once
\(m>0\), and the recorded zero-free-window statements are statements
of the massless sector. Hypotheses and limits: the Presentation~B
operator and \(Q\) assignment, one block without the other sectors,
weights, gauge fixing or the ghosts, the leading-logarithmic
fixed-window class of this ledger entry, \(\mu\ll m,k\ll\LUV\), and
window substitutions not derived from the matrix path integral; the
local finite counterterm of Theorem~\ref{thm:Geff} is not fixed here,
the fixed-window pole estimate is not shown to coincide with a zero
of the momentum-dependent factor, no \(\mathcal W_C\),
\(\mathcal A_1\), \(G_{\mathrm{eff}}\) or \(\delta_W\) is computed
for the locked block, no zero-free region or ghost-freedom statement
is made for any massive sector, and no status label is changed; the
ledger entries of Problems~F and~N are unchanged and both stay OPEN.
```

## Verification scripts (reproduction pack)

All in proposals/121-n-hmassive-threshold/ unless noted. Re-run from the repo root:

1. `python -I proposals/121-n-hmassive-threshold/verify121.py` (final, v11,
   sha1[:12] d04bf3101e0c, 10728 B; sympy + mpmath, deterministic, prints 14 lines).
   Expected invariants: 12 lines beginning PASS (S1-S10, S12, S11 ACTIVE - no SKIP
   line), then "TOTAL 12/12 PASS", then "ALL CHECKS DONE 121". Key numeric invariants:
   S1 gcJ(1,1,5) = 0.1482962130; S4 Upsilon_H(0) = 10, Upsilon_H(100) < 1e-40; S6
   y* = e^{-(10+gamma_E)} within 5e-3 relative; S7 U_*(0) = pi/2 window -9.58 < d < 10;
   S9 jump > 1 light / < 1e-6 heavy; S12 grid sup < 0.9 Upsilon_H and control residual
   < 1e-25.
2. `python -I proposals/121-n-hmassive-threshold/gen_payload_121.py` (sha1[:12]
   e431049cf73c): regenerates payload + preview byte-identically from the embedded
   source (touches only the folder). Expected: "hygiene payload: OK",
   "controls fired: [True, True, True, True, True]", "payload bytes: 3645 sha1:
   702a60d1e5dc", "anchor count: 1",
   "PRE bytes: 854131 POST bytes: 857778 delta: 3647 = 3647 : True",
   "sha1 spliced: fd23c0d737b0", "GEN121 OK".
3. `python -I scratch/121/cert-r121p.py` (compile certificate; copies the live build
   inputs to an OUT-OF-REPO temp dir, splices the payload at the anchor in the COPY,
   two `pdflatex -interaction=nonstopmode -halt-on-error namcg-book7.tex` passes,
   removes the temp dir; takes minutes; never writes into the repository). Expected
   (captured in scratch/121/out-cert-r121p-r1.txt):
   "PRE 854131 f5a761c55396 POST 857778 fd23c0d737b0", "pass 1 rc 0", "pass 2 rc 0",
   "exclam 0 undefrefs 0 multidef 0 undefcites(info) 48", "CERT PASS",
   "temp removed True". (48 undefined citations are expected: bibtex is not run, the
   same reference-only scan scripts/build_check.py performs.)
4. `python -I scratch/121/s12_diag.py` -> scratch/121/s12_diag_out.txt: the S12
   diagnosis numbers quoted above.

Captures: out-gen121-r1.txt (gen r1 crash = lineage), out-gen121-r2.txt (gen r2 OK),
out-verify121-r1.txt (old verify, S11 SKIP), out-verify121-r2.txt (v8 run: crash inside
S11 = the dead-guard finding), out-verify121-r3.txt (v9 FAIL, scanner-token bug),
out-verify121-r4.txt (v10 FAIL, wrong CRLF control), out-verify121-r5.txt (FINAL
TOTAL 12/12 PASS). Scratch lineage: verify121_v7 (3d3f71ac452f) through v11
(d04bf3101e0c), verify121_folder_pre_v8.py (655227e3b3f3, archived old folder copy).

## Decisions Taken

1. S12 disposition (RESEARCHER-DECISION, resolved here): possibility (ii), check
   mis-implemented. The factor-2 assertion presupposed a positive real root of
   P = Upsilon_H/ell(P;y) that provably does not exist at the tested points (f < 0 on
   both bracket ends; grid sup 0.24-0.255 of the threshold). The check was re-scoped to
   the true statement (no positive real zero; derived asymptotics Upsilon_H/5) with its
   teeth kept and a positive control that fires (control coupling finds its root,
   residual < 1e-25). Tolerance was not tuned. Rejected: (i) restating a weaker
   quantitative agreement in the payload - there is no agreement statement to state:
   the objects being compared (a zero that exists vs one that does not) differ in kind,
   and the payload makes no implicit-pole claim to re-scope; (iii) drop with SKIP - the
   true statement verifies cleanly and a SKIP would hide the corrected finding.
2. Manuscript text kept minimal and unchanged from gen r2: no payload edit, no regen
   (the false claim lived only in the check). This avoids supersession churn on
   pinned bytes.
3. S11 rebuilt in place rather than dropped: payload hygiene + whitelist must run for
   an integration-ready package (117 controls standard applied; see lineage).
4. Anchor = the generator's unique string "Problems~F and~N remain open." in Problem N
   (the Problem E anchor of the STEP 0 pin is a file locator, not the insertion point).
5. Predecessor lineage honored: notes.md research inputs used as-is; nothing re-surveyed
   beyond what the changed calculations required.

## Milestone assessment

Routine. No MILESTONE.md trigger: the package supplies a conditional named-missing-step
input (massive threshold functions) to N and F and corrects the verification pack; it
derives no critical-path step unconditionally and closes nothing.

## Status-label recommendation

Critical-path set re-derived from ch17 (full-GR / matrix-derived scope): A, B, C, D1, E,
F, G-derived, N (H, I, J optional within their scopes; G mechanism CLOSED CONDITIONALLY;
N's own text re-read this session at appH 3869-3871). All affected labels UNCHANGED -
this package proposes no status, priority, or completion edit anywhere.

## Author decision needed

None. No author-missing-datum item is added by this package: its hypotheses (the
Presentation-B operator and constant Q for the H block, one block without other sectors,
weights, gauge fixing, ghosts) are stated in the payload and are conditional-derivation
hypotheses, not new entries in the D missing-data list.

## Remaining open step

To close the original Problem N target it would still be needed to: derive alpha,
G_eff, delta_W and the form factors for the locked block from the matrix path integral
(appH 4056-4058 disclaims them here), then control the effective expansion and exclude
propagating Ostrogradsky ghosts for p < LUV for those values, with the region of
validity stated (ch17 730-734). Within this package's own scope, what remains is:
(i) no zero-free-region or ghost-freedom statement for the massive sector (the S9 cut
attaches at x = -4y; a slit contour respecting the cut plus a remainder bound would be a
new problem); (ii) the S12 sup bound is numerical, not proved; (iii) the fixed finite
counterterm of Theorem thm:Geff is unfixed; (iv) the fixed-window pole estimate is not
shown to coincide with a zero of the momentum-dependent factor (S12 evidence indicates
the running-window factor has no positive real zero on the tested grid).

## Special instructions for the gatekeeper

Scope limits: the single manuscript-visible change is the 3645-byte payload insertion at
the stated anchor; everything else in this file is verification record. Must NOT be
asserted or required: any zero-free region, ghost freedom, or pole position for any
massive sector; any computation of W_C, A_1, G_eff, delta_W for the locked block; any
label change; any closure. Re-check priority: (1) re-derive S12's no-root argument and
the asymptotic identity 2(e^{-y} - y E_1(y)) = Upsilon_H(y)/5 independently; (2) re-run
the three pack commands above and match the invariants; (3) verify anchor uniqueness and
the two spliced-byte reproductions (preview fd23c0d737b0 and cert POST) against the live
tree at the STEP 0 hash; (4) confirm the payload contains no implicit-pole claim and no
new label/cite. Cert is reference-only (no bibtex pass, like scripts/build_check.py);
48 undefined citations are expected. Payload is byte-identical to the gen r2 record;
verify121.py is v11 - if re-run prints "SKIP S11 payload absent", it was run outside
the folder (wrong cwd), not a pack change.
