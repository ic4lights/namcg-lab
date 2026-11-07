# Proposal 056-slice-lhs-full-n2-bridge, round 2

## Result
Unchanged central results of r1, re-affirmed by the gatekeeper's independent re-derivations (exact
Stokes band delta > lambda_* epsilon with lambda_* = sqrt(2+sqrt2); slice bound |O_k| <= 2 at R_1;
convergence of the damped u=1 family conditional on the 053 chain legs; corner modulus lower bound;
band incompatibility; exact 1D model |1-J/I| -> 1), now with the manuscript line corrected to be true:
the r2 insert is the gatekeeper's corrected snippet adopted BYTE-EXACTLY (F1 false displayed identity
removed; tube scale O(epsilon) per F2; explicit gamma=0 hypothesis class per F3; m6 style
normalization to appH conventions). Round 2 adds: the fixed-eps crossing epsilon* = 0.0115103
(u=0.3, poly=1, link_r1.py SEC C, resolving m3), the exact complex linking ratio |1-J/I| = 1.04271 at
eps=0.01 inside the sandwich bound 1.11078 while the mp.quad figure 1.19697 exceeds it (m2: the quad
column is now explicitly a truncation check), the corrected model-growth label sqrt(2)/32 =
0.044194174 (m1), a deterministic off-slice contrast with |O_k| = 2cosh(2) = 7.5243914 > 2 (m5), and
an out-of-repo build of the applied copy: 359 pages, zero undefined/multiply references in the final
pass (build_r2_summary.txt).

## Target and status
Problem E (Lorentzian signature, Assumption ass:lorentzian). Appendix H (verbatim in review):
"Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion:
PROGRAMME-CONDITIONAL." ch17: "OPEN; CRITICAL PATH for the matrix-derived label". Original target:
derive the displayed Lorentzian limit identity (appH L1502-1505) for the physically relevant slice
insertions at N=2 (054's "unresolved on that slice at k != 0"). Dependencies: 053 chain (polynomial,
k<14 window), 054 trichotomy, 055 slice modulus facts. Nothing closes; the r2 package records positive
lemmas plus the bounded no-go, exactly as accepted in r1.

## Source reading
digest + targeted reads (compact digest). Re-read this round: review-r1.md in full (the binding
review); appH Problem E block per r1 reads (pins below). Pins re-verified by me in apply_check_r2.out:
chapters/appH-microscopic-proofs.tex 540349 B, sha256 5766105967f830ae8817cc50636d881315ddaa62070e5dfd875727b675fc4cce,
CRLF 3209, bare-LF 0; anchor b'\r\n'*4 + \paragraph{Status.} + CRLF + "Remains
Assumption~\ref{ass:lorentzian}." count EXACTLY 1, offset 254357 (decoy at 539932 carries ass:EFT-a2).

## Addressing every review finding
- F1 (blocking): the false displayed identity rho_X^2 = sum_a (k^mu tilde A^a_mu)^2 >= 0 (complex
  squares are not >= 0) is GONE: the adopted snippet states the correct form, with the contour field
  reducing on R_1 to the Hermitian r-form, rho_X^2 = sum_{a=1}^{3} (r^mu tilde A^a_mu)^2 >= 0 with r
  the rotated real slice momentum — exactly what bridge_r1.py SEC 2 verifies (matrix-vs-contraction
  identity, reality and >= 0 asserted on the slice). Addressed by byte-exact adoption (see below).
- F2 (major): the tube scale is O(epsilon), not O(sqrt(eps)). Reasoning restated: with
  S_E containing kappa tau^2 rho^2, a tube tau = Theta(sqrt(eps)) at the maximizing radius
  rho* = b_u/(4 eps cos(3 pi u/4)) = Theta(1/eps) incurs a quartic penalty Theta(1/eps) (numerically
  ~1.09 at eps=0.01, kappa=1, growing as 1/eps per the gatekeeper), which would replace c0(u) by
  c0(u)/(1 + kappa sin(pi u/2)/K); the O(epsilon) tube makes the penalty O(1) at rho*, so the exact
  c0(u) holds up to subleading terms and the /poly factor absorbs the O(1) factor. The no-go needs
  only some c~(u) > 0 and survives either way. The adopted snippet says "transverse scale
  O(\epsilon)"; link_r1.py SEC C comment corrected; SEC C code (regulator-only c0u) unchanged.
- F3 (major): the no-go sentence now carries the class qualifier: "within the class N=2, regulator
  (A), gamma=0, slice momenta with r^0 != 0, and linking by absolute-value estimates along the family
  R_u, no rate delta(epsilon) and no contour slide bridges the undamped slice insertion (a fixed
  negative mass contributes only a phase at u=0)". This no longer contradicts merged L1512 (fixed
  gamma<0 extends the identity to every k numerically): the mass clause is confined to u=0 (pure
  phase, modulus 1 on the flat contour) and to the gamma=0 class. Addressed by byte-exact adoption.
- F4 (major, framing): Decisions Taken revised (below): the gamma->0^- bridge at u < 1/3 is recorded
  as an OPEN, in fact the most promising unobstructed avenue: fixed gamma<0 already bridges every k
  (L1512, numerical); at fixed u>0 the mass gives Gaussian damping; the 055 branch saturation constant
  sin(3 pi u/4 - pi/4)/(8|gamma|) DECAYS for u < 1/3; the r1 no-go class is gamma=0, so a
  gamma-uniform estimate is untouched by it. It must not be dropped from the loop.
- m1: link_r1.py model-growth label corrected to |I| = 2 sqrt(pi/eps) exp(-Re(gc^2)/(4 eps)),
  -Re(gc^2)/4 = sqrt(2)/32 = 0.044194174; script re-run, new output link_r1_r2.out; r1 outputs kept
  unchanged as historical records.
- m2: SEC B quad column header now reads "TRUNCATION CHECK ONLY, mp.quad unreliable on growing
  oscillatory tails"; an exact complex column |1-J/I| and the sandwich bound 1 + |J|/|I| are printed
  (0.01: exact 1.04271 <= 1.11078; quad 1.19697 exceeds it, confirming it as artifact). Conclusions
  rest on the closed forms.
- m3: the r1 prose "empty for eps <= 0.015" replaced: incompatibility is asymptotic (eps small
  enough); numerically the crossing (poly=1, u=0.3) is epsilon* = 0.0115103 (bisection, printed in
  link_r1_r2.out). Not in manuscript text.
- m4: apply-rule prose corrected: realized CRLF delta is +3 (3209 -> 3212), not +6; byte delta is
  2502 = 6 + len(line) with len(line) = 2496; verified in apply_check_r2.out.
- m5: bridge_r1.py SEC 2 contrast replaced by a deterministic example: k = (0, 2i, 0, 0), A^1_1 = 2
  gives rho_X^2 = -16, rho_X = 4i, |O_k| = 2 cosh 2 = 7.5243914 > 2 (bridge_r1_r2.out). Script
  re-run; r1 output kept.
- m6: resolved by adopting the gatekeeper snippet, which uses \( \), \epsilon, \mathrm e, \mathrm i,
  \mathcal R_\theta / \mathcal R_u, \tilde A, and no "anti-Wick" (grep-confirmed on the adopted line:
  0 dollar signs, 0 "anti-Wick").

## Insert r1 -> r2 diff (documentation)
Adopted: `appH_insert.tex` = gatekeeper `## Corrected snippet` from review-r1.md extracted
byte-exactly (extract_snippet.py; single line 2496 chars + trailing LF; file 2497 B;
sha256 60fb51ee0124aba3e1765744116b18fdeae7a9315b5c8eb2429af550bf7b082e). No paraphrase. r1 line was
2099 chars (gatekeeper realized 542454 B for it); delta r1 -> r2 = +397 chars. Substantive changes:
(i) corrected rho_X^2 identity (F1); (ii) transverse scale O(sqrt(eps)) -> O(epsilon), explicit
Tr H^2 = 1 (F2); (iii) no-go sentence carries the gamma=0 class and the u=0 phase parenthetical (F3);
(iv) asymptotic wording "as \epsilon \to 0^+" for the band incompatibility (m3); (v) style: math
delimiters \(\), \epsilon, \mathrm e/\mathrm i, \mathcal R, "Pfaffian window"; removed the term
"anti-Wick" (m6); (vi) closing sentence unchanged and required ("Problem~E remains open and
PROGRAMME-CONDITIONAL."). Anchor rule and pins unchanged (see apply_check_r2.out): apply replaces the
single 4-CRLF Status anchor with CRLF CRLF + CRLF-normalized insert + original anchor; expected
applied 542851 B, sha256 185bdcee9ae824e9c7fa7211c4280f56beb7f7210392f336592877f33112e73b, CRLF 3212,
bare-LF 0 — reproduced independently by my apply_check.py report run (all True) AND by applying to an
out-of-repo copy (see Build attempt).

## Claim classification
Unchanged from r1 (see proposal-r1.md, Claim classification), with the insert's displayed identity now
true (established: on R_1, k^mu A_mu = r^mu tilde A_mu Hermitian, rho_X^2 = sum_a (r.tilde A)^2 >= 0;
055 merged text and bridge SEC 2). New this round: epsilon* = 0.0115103 (numerical computation,
model-level table); |1-J/I| exact-column values (established closed-form model computation); off-slice
|O_k| > 2 example (established explicit computation; the analytic fact was already merged at L1512).

## Proposed changes
One paragraph inserted before the Status anchor in chapters/appH-microscopic-proofs.tex (exact rule
and pins above; nothing else touched; no bib change; no \ref/\cite; no label added; anchor count 1
verified this round). All 053/054/055 paragraphs and Status remain byte-identical.

## Verification scripts
In proposals/056-slice-lhs-full-n2-bridge/ (run with python -I):
- extract_snippet.py: byte-exact extraction of the review snippet into appH_insert.tex (prints
  len(line)=2496 matching the gatekeeper's delta 2502 prediction, and the file sha).
- patch_r2.py: the m1/m2/m3/m5 script edits (asserted replacements; fails loudly if anchors move).
- link_r1.py + link_r1.out (r1 record), link_r1_r2.out (r2: corrected SEC B columns, sqrt2/32 label,
  F2 tube comment, epsilon* = 0.0115103).
- bridge_r1.py + bridge_r1.out (r1 record), bridge_r1_r2.out (r2: deterministic |O_k| = 7.5243914 > 2
  contrast; SEC 1-5 otherwise byte-stable).
- apply_check.py + apply_check_r2.out (report mode: pins, anchor count 1 at 254357, applied
  542851 B / sha 185bdcee... / CRLF 3212 / bare-LF 0 all reproduced; context line shows the new
  paragraph follows the 055 paragraph's closing sentence).
- build_r2_summary.txt (out-of-repo build record; logs stay in the copy).
Gatekeeper note: the r1 worry that link_r1.out was stale is WITHDRAWN — confirmed false (byte-identical
reproduction), per the review's special-instruction adjudication.

## Decisions Taken
- Adopted the gatekeeper's corrected snippet verbatim over self-revising the r1 line (fastest,
  safest, gatekeeper-verified; also guarantees m6 normalization).
- KEPT OPEN, ranked first among unobstructed routes (F4): the gamma->0^- bridge at u < 1/3 — fixed
  gamma<0 already bridges every k (L1512, numerical); saturation constant decays for u < 1/3
  (sin(3 pi u/4 - pi/4) < 0); our no-go is inside gamma=0 and does not touch a gamma-uniform
  estimate. What would close it: an epsilon-uniform (and then gamma-uniform) modulus or oscillatory
  estimate on R_u for fixed u in [0, 1/3) linking the fixed-gamma<0 regulated family to the gamma=0
  LHS with errors o(1) as gamma -> 0^+.
- Rejected (unchanged from r1): modulus-based two-regulator bridging (bounded no-go); window-majorant
  closure at u<1 (false); flagging 053's delta-factor sentence (withdrawn, confirmed by gatekeeper:
  053 is correct, no PRIOR-CLAIM-ERROR).

## Milestone assessment
Routine. No milestone trigger: no critical-path step closed; positive lemmas plus bounded no-go,
already accepted at r1.

## Status-label recommendation
Critical-path set re-derived (ch17 + Appendix H): A, B, C, D1, E, F, G-derived, N. No label changes.
Problem E: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL (unchanged).

## Author decision needed
None.

## Remaining open step
To close the slice case of the displayed identity at N=2 (r^0 != 0): (rank 1) a gamma-uniform estimate
for the fixed-gamma<0 bridge at u < 1/3 (F4 avenue), or (rank 2) a non-modulus oscillatory domination
lemma on the flat contour / R_u (055's reduced-model cancellation at ln-slope 0 vs corner growth
0.044/eps motivates it), or (rank 3) contours outside the linear R_u family (thimbles) — the Stokes
band lemma is only about this family. The pure-spatial r^0=0 half needs the rank-2 machinery (ray
freeness at commuting rays does not control |O_k| in modulus off R_1).

## Special instructions for the gatekeeper
Verify: (1) appH_insert.tex is byte-identical to review-r1.md's fenced Corrected snippet (run
extract_snippet.py or diff); (2) apply_check_r2.out reproduces applied 542851 B / sha 185bdcee... /
CRLF 3212 / bare-LF 0 from the current source (the source is unchanged this round — no integration
happened); (3) link_r1_r2.out SEC B exact column inside the sandwich bound and the quad column
outside it (artifact demonstration); (4) epsilon* = 0.0115103; (5) bridge_r1_r2.out SEC 2 off-slice
|O_k| = 7.5243914. Must NOT be asserted: any closure of the slice identity; extension of the no-go
outside (regulator (A), gamma=0, N=2, slice r^0 != 0, modulus linking on R_u); any weight for the
SEC B quad column. The F2 tube: at tau = O(epsilon) the quartic penalty at rho* is O(1) — check the
c0(u)/(1+kappa sin(pi u/2)/K) degradation claim for the sqrt(eps) tube if desired.
Build evidence: integrator must run scripts/build_check.py (authoritative); my out-of-repo build is
recorded in build_r2_summary.txt (359 pages; final pass: 0 undefined reference/citation, 0 multiply
defined, 0 LaTeX Warning; exit codes all 0).

## Build attempt (r2)
Performed exactly once, out of repo: tree copied to C:/Users/redgi/tmp/056_apply_r2 (prior tmp copies
untouched; the repository manuscript untouched). Insert applied to the copy's appH:
542851 B, sha256 185bdcee9ae824e9c7fa7211c4280f56beb7f7210392f336592877f33112e73b, CRLF 3212 (exact
match to the gatekeeper's predicted pins). Passes: pdflatex; bibtex namcg-book7; pdflatex; pdflatex
(-interaction=nonstopmode -halt-on-error; no latexmk). Result: PDF 359 pages; final-pass log scans:
0 "undefined reference/citation", 0 "multiply defined", 0 "LaTeX Warning"; all pass exit codes 0.
Details in build_r2_summary.txt.
