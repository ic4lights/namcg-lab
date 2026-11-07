# Proposal 055-anti-wick-slice-nonzero-k, round 2

Round 2 responds to `review-r1.md` (VERDICT: ACCEPT WITH REQUIRED REVISIONS). All four
insert corrections (F1–F4) are applied EXACTLY as the gatekeeper's "Corrected snippet"
substitutions; F5–F7 (artifact corrections) are done; every r2 number is regenerated from
the current working tree. No new mathematics is introduced; the evidence classification is
corrected (the saturation constant of item 3 decays as \(\gamma\to0^-\) for \(u<1/3\)).

## Result

Within the hypothesis class of the merged proposal-054 paragraph (appH line 1512: \(N=2\),
\(O_k=\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\), \(k\in\mathbb C^{10}\), \(\gamma=0\),
regulator (A), contours \(\mathcal R_u\), \(\epsilon\to0^+\) last), the package narrows the
window that 054 left unresolved ("unresolved on that slice at \(k\ne0\)") and gives model-level
control of the left-hand side on that slice:

1. **Established (exact).** The Cauchy–Binet identity
   \(\rho_X^2=\sum_{a=1}^{3}(k^\mu A^a_\mu)^2\) (FULL Pauli range; the r1 range
   \(a=1..2\) was false — gatekeeper F1) for \(N=2\) makes the boundedness of the
   right-hand side of the displayed limit identity on the anti-Wick slice structural: on
   \(\mathcal R_1\) the contraction \(k^\mu A_\mu\) reduces to the Hermitian real-linear
   form \(r^\mu\tilde A_\mu\), so \(\rho_X\) is real and \(|O_k|\le2\) pointwise. The
   identity is now verified NON-tautologically: characteristic polynomial of
   \(\sum_{a=1}^3 w_a\sigma^a/2\) is \(\lambda^2-\sum_{a=1}^3w_a^2/4\) (symbolic), and a
   random complex-data check compares the MATRIX side \(\rho_X^2=(\lambda_+-\lambda_-)^2
   =-4\det(k^\mu A_\mu)\) (traceless) against the CONTRACTION side
   \(\sum_{a=1..3}{(k^\mu A^a_\mu)}^2\): max relative deviation \(4.596\cdot10^{-51\!}\)
   over 8 trials at 50 dps; the \(a=1..2\) truncation fails generically (max rel dev
   \(2.094\)) and at the explicit counterexample \(A_0=\sigma^3/2,\ k^0=1\):
   \(-4\det=1\) but truncated sum \(=0\).
2. **Established (model-level, within the rank-one commuting-ray class of 054).** Inside the
   slice at \(u=0\) the commuting-ray growth functional is
   \(B=\mathbf v\mathbf v^{\mathrm T}-\mathbf u\mathbf u^{\mathrm T}\), supported on
   \(\operatorname{span}\{\mathbf e_0,\hat{\mathbf r}\}\), of rank \(\le2\), with
   \(\lambda_{\max}(B)=[{(r^0)}^2-r^2+\sqrt{{(r^0)}^4+6{(r^0)}^2r^2+r^4}]/(2\sqrt2)>0\) iff
   \(r^0\ne0\). For pure spatial slice momenta (\(r^0=0\)) there is no commuting ray with
   growth (054's strict-growth criterion is unattainable there), the neutral set is
   \(\hat{\mathbf r}\cdot\hat\rho=0\) and \(B\) is strictly negative off it. The possible
   commuting-ray obstruction to the \(\epsilon\to0^+\) left-hand side therefore concentrates
   on the half of the slice with \(r^0\ne0\).
3. **Established (exact branch identity) + conditional (its role as worst case), with the
   corrected \(u\)-scope (F3).** The one-dimensional branch integral
   \(\int_{\mathbb R}\mathrm e^{-Qa^2}2\cos(\gamma_{\mathrm c}|a|)\,\mathrm da
   =2\sqrt{\pi/Q}\,\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\),
   \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\), gives pointwise modulus growth
   \(\mathrm e^{{(r^0)}^2\cos(3\pi u/4-\pi/4)/(16\epsilon)}\) at \(\gamma=0\), saturating at
   fixed \(\gamma<0\) to \(\mathrm e^{{(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)}\). The sign
   of \(\sin(3\pi u/4-\pi/4)\) splits the contour family: it is negative for
   \(0\le u<1/3\) (\(-0.7071\) at \(u=0\), \(-0.0785\) at \(u=0.3\)), zero at \(u=1/3\),
   positive for \(u>1/3\) (\(+0.5878\) at \(u=0.6\)). So the saturation constant DIVERGES as
   \(\gamma\to0^-\) only for \(u>1/3\); for \(u<1/3\) — including the \(u=0\) E1 regime — it
   DECAYS (to 0), and the pointwise branch factor is not an obstruction to a \(\gamma\to0^-\)
   bridge there. For \(u>1/3\) pointwise domination is NOT uniform in \(\gamma\): any
   transfer of the 054 fixed-\(\gamma<0\) success to \(\gamma=0\) in that sub-range cannot
   rest on pointwise/Gaussian domination along the soft temporal branch.
4. **Numerical (reduced \(N=2\) model).** With the exact slice insertion in the reduced
   \(N=2\) integral (regulator (A), \(\mathcal R_u\), \(\epsilon\to0^+\) last), at pure
   temporal slice momenta the modulus ratio \(|Z_\epsilon[O_k]|/|Z_\epsilon[1]|\) stays of
   order one and tends to \(2\) along the ladder down to \(\epsilon=3\cdot10^{-3}\) (fit slope
   \(0.0000\) of the log-ratio against \(1/\epsilon\) versus the pointwise corner value
   \(0.044/\epsilon\) at \(r^0=1\), \(0.177/\epsilon\) at \(r^0=2\)). At \(u=0.6\),
   \(\gamma=-0.2,-0.05\), the measured ratios fill \([0.74696,1.7788]\) (insert: "between
   \(0.74\) and \(1.78\)"; the r1 "[0.75, 2.2]" was wrong, F2), and the predicted saturation
   factors \(1.444,4.347\) do not materialize (measured ratios vs the \(\gamma=0\) row:
   \(0.375\)–\(0.892\)). In the reduction the commuting-ray growth
   \(\mathrm e^{c_2(k)/\epsilon}\) and the pointwise saturation factor are both consistent
   with phase-space suppression near the soft corner — mechanism identified, NO domination
   lemma claimed (F4). The slice window is therefore NOT closed at full \(N=2\) — the reduced
   chart is a commuting-sector reduction — but no obstruction to its control appears at model
   level, and the mechanism that would have to be beaten (pointwise branch growth, \(u>1/3\)
   only) is pinned down.

Nothing is closed: Problem E remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL, and
Assumption~\ref{ass:lorentzian} is not discharged.

## Target and status

- Problem E (signature), `chapters/appH-microscopic-proofs.tex` Section "Problem E: signature"
  (`\label{sec:status-E}`). Ledger label quoted verbatim (lines 1486–1489): "Status: OPEN.
  Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A
  scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or
  matrix-derived Lorentzian signature." Re-verified against the CURRENT working tree
  (appH 537324 B sha256 943816e923a844521faf56fc88774cd0827eca501f69bb7b12dc9f4af18e8571,
  CRLF 3206, bare-LF 0 — unchanged since r1; `bib/namcg.bib` 25976 B sha256
  a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b unchanged).
- Chapter 17 (`chapters/ch17-agenda.tex` lines 394–399): "Problem E: Lorentzian signature.
  OPEN; CRITICAL PATH for the matrix-derived label."; completion item (lines 718–719):
  "Problem~E: Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})."
- Original target of the E ledger line relevant here: the displayed \(\epsilon\to0^+\) limit
  identity of the "Limit at finite \(N\)" paragraph extended beyond polynomial \(O\). The
  merged 054 paragraph (appH line 1512) established, within its class, that the identity
  FAILS for every nonzero real \(k\) and every non-real \(k\) off the slice
  \(\{k^0\mathrm e^{-3\pi\mathrm i/8},\,k^i\mathrm e^{\pi\mathrm i/8}\in\mathbb R\}\), HOLDS
  at \(k=0\), and is UNRESOLVED on the slice at \(k\ne0\).
- Rank-1 target of this package: settle/control the slice window (LHS control). Rank-2 (same
  derivation): what the fixed \(\gamma<0\) success implies for \(\gamma=0\) slice control
  (\(\gamma\to0^-\) uniformity). Rank-3 (regulator/\(N\) extension) not attempted.
- DERIVED vs PROGRAMME-CONDITIONAL: everything here is PROGRAMME-CONDITIONAL evidence inside
  the 054 hypothesis class; conditional on the reduced \(N=2\) chart for item 4 and
  model-level (rank-one rays / single branch) for items 2–3. No label changes are proposed
  and none is made anywhere in this package.

## Source reading

digest + targeted reads (compact digest CURRENT per orchestrator at run start). Read in
full: `chapters/appH-microscopic-proofs.tex` lines 1480–1519 (Problem E ledger block:
contours paragraph, flat-direction bound, finite-\(N\) limit paragraph, definition (C), 053
closing paragraph at line 1510, merged 054 paragraph at line 1512, Status at 1515–1516);
`chapters/ch17-agenda.tex` lines 392–401 and 697–719; `proposals/054-nonpolynomial-observables-lorentzian-n2/`
paragraph text as merged; `proposals/053-lorentzian-integral-limit-order/` anchor machinery;
this folder's `proposal-r1.md` (31436 B, sha 19f15a14…), `review-r1.md` (13004 B, sha
4d91375f…), all r1 and r2 `.out` artifacts; `MILESTONE.md`; `reports/ledger.md` tail. No
unreadable files. No citation is imported anywhere in this package (the insert contains no
`\cite`), so `bib_additions.bib` remains intentionally absent.

## Findings disposition (review-r1)

- **F1 (blocking) — CLOSED.** The insert's Cauchy–Binet range was corrected to
  \(a=1..3\) (span 1 of `patch_insert_r2.py`, applied byte-exactly as the gatekeeper's
  substitution). Script sec.1 re-run with the FULL range and a NON-tautological check
  (`slice_ray_r2.out`): charpoly\((\lambda I-\sum_{a=1}^3w_a\sigma^a/2)=
  \lambda^2-\sum_{a=1}^3w_a^2/4\) (symbolic, difference 0); random complex 50-dps matrix-side
  vs contraction-side comparison \(-4\det(k\!\cdot\!A)=\sum_{a=1..3}{(k^\mu A^a_\mu)}^2\)
  max rel dev \(4.596\cdot10^{-51}\); \(a=1..2\) truncation fails generically (max rel dev
  \(2.094\)); counterexample \(A_0=\sigma^3/2,k^0=1\): \(-4\det=1.0\) vs truncated sum 0.
  Disclosure: the r1 numeric sec.1 "PASS" was doubly vacuous — besides the tautology (F7),
  mpmath 1.3.0's three-argument constructor `mp.matrix(m, n, S)` silently builds a ZERO
  matrix for list/dict/callable `S`, so any matrix built that way contributed zeros. The r2
  script uses the working nested-rows form `mp.matrix([row1, row2])` and documents the trap
  in a comment. This is why the r2 numbers (identity \(4.6\mathrm e\!-\!51\), truncation
  failure \(2.094\), counterexample \(1.0\)) are now genuine.
- **F2 (major) — CLOSED.** Insert now reads "it stays between \(0.74\) and \(1.78\)". The
  underlying numerics are unchanged (`n2_slice_r1.out` byte-identical to r1: sha e17a86cf…):
  the \(\gamma=-0.2\) row min is \(0.74696\) (so the r1 claim that "0.75 covers 0.747" was
  simply wrong — acknowledged), the \(\gamma=-0.05\) row max is \(1.7788\), and \(2.1574\)
  belongs to the \(\gamma=+0.00\) row which the sentence does not include. True stated range
  \([0.74696,1.7788]\subset[0.74,1.78]\).
- **F3 (major) — CLOSED.** Insert now reads "... , which diverges as \(\gamma\to0^-\) when
  \(3\pi u/4-\pi/4>0\) and decays when it is negative." Sign table (established, elementary
  sign analysis of the exact exponent): \(\sin(3\pi u/4-\pi/4)=-0.7071\) (\(u=0\)),
  \(-0.0785\) (\(u=0.3\)), \(0\) (\(u=1/3\)), \(+0.5878\) (\(u=0.6\)). Consequence carried
  into Result item 3 and the ranked avenues: for \(u<1/3\) the saturation constant decays as
  \(\gamma\to0^-\), so the branch factor does NOT obstruct the bridge in the E1 regime.
  (The gatekeeper's own parenthetical "\(-0.707{(r^0)}^2/(4|\gamma|)\)" at \(u=0\) is a
  typo for \(-0.7071{(r^0)}^2/(8|\gamma|)=-0.0884{(r^0)}^2/|\gamma|\); the sign — the point
  of the finding — is as the gatekeeper states. I re-derived the exponent from
  \(-\gamma_{\mathrm c}^2/(4Q)\), \(Q\to(\,|\gamma|/2)\mathrm e^{\mathrm i(\pi/2-3\pi u/4)}\),
  giving \(-{(r^0)}^2\cos(3\pi u/4+\pi/4)/(8|\gamma|)={(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)\).)
- **F4 (major, wording) — CLOSED.** Mechanism clause hedged exactly per the corrected
  snippet: "consistent with phase-space suppression of the corner branch growth near the
  soft corner by Vandermonde and measure powers, though no domination lemma is claimed."
- **F5 (minor) — CLOSED.** `slice_ray_r1.py` sec.3 print label now reads "(ratio 4 vs ray
  value; Pauli normalization, \((r^0)^2\) scaling)": the displayed ratio is
  \(0.1767766953/0.0441941738=4\) (the \(\operatorname{Tr}\sigma^a\sigma^a/4=1/2\) Pauli
  factor with \((r^0)^2\) scaling), not "factor 2".
- **F6 (minor) — CLOSED.** The stale `apply_copy_r1.out` line ("540234") was superseded: r2
  apply artifacts regenerated from the NEW insert — expected realized size
  \(537324+3021+4=540349\) (computed from the r2 CRLF insert, not the r1 540236 figure);
  realized in the copy: 540349 B, CRLF 3209, bare-LF 0, sha256
  5766105967f830ae8817cc50636d881315ddaa62070e5dfd875727b675fc4cce. r1 artifacts kept as
  historical record, stale by design.
- **F7 (minor) — CLOSED.** sec.1 check is now non-tautological (see F1): the matrix side is
  built from the full Pauli range and compared against the contraction side, plus the
  explicit counterexample; the mpmath constructor trap that made the r1-style numeric check
  silently vacuous is fixed and documented.

## Research and reasoning

### A. Cauchy–Binet and the structural RHS bound (established)

At \(N=2\), write \(A_\mu=\sum_{a=1}^{3}A^a_\mu\sigma^a/2\) (manuscript convention, appH
line 1500) and \(\mathcal G_{\mu\nu}=\sum_{a=1}^{3}A^a_\mu A^a_\nu\). Then
\(\rho_X^2=k^\mu k^\nu\mathcal G_{\mu\nu}=\sum_{a=1}^{3}{(k^\mu A^a_\mu)}^2\): a polynomial
identity (symbolic difference 0), AND — the substantive r2 check — the matrix side agrees:
\(k^\mu A_\mu\) is traceless with eigenvalues \(\pm\sqrt{\sum_a w_a^2}/2\) (charpoly check),
so \(\rho_X^2=(\lambda_+-\lambda_-)^2=-4\det(k^\mu A_\mu)\) equals the contraction side to
\(4.6\cdot10^{-51}\) relative on random complex data. The \(a=1..2\) truncation is FALSE
(counterexample above): the \(a\)-sum must run over all three Pauli directions, which is also
what the manuscript's own expansion and the merged 054 paragraph use
(\(\rho_X^2=k^\mu k^\nu\mathcal G_{\mu\nu}\), \(\mathcal G\) summing \(a=1..3\)). For slice
\(k\) on \(\mathcal R_1\) the contour factors cancel: \(k^0A_0=r^0\tilde A_0\),
\(k^iA_i=r^i\tilde A_i\) (verified symbolically: \(\mathrm e^{3\pi\mathrm i/8}\mathrm
e^{-3\pi\mathrm i/8}=\mathrm e^{-\pi\mathrm i/8}\mathrm e^{\pi\mathrm i/8}=1\)), so
\(k^\mu A_\mu=r^\mu\tilde A_\mu\) is Hermitian for real \(r\), \(\rho_X\in\mathbb R\),
\(O_k=2\cos(\rho_X/2)\), \(|O_k|\le2\) pointwise. This upgrades the 054 assertion "there
\(|O_k|\le2\) and that side converges by the \(k<14\) Pfaffian window" from stipulated to
structural; it does not touch the LHS.

### B. Slice-ray trichotomy at \(u=0\) (established within the rank-one class)

Unchanged from r1 and re-verified by re-run (`slice_ray_r2.out` sec.2 identical to r1):
054's commuting-ray alternative takes \(\tilde A_\mu=\rho_\mu H\), \(\operatorname{Tr}H^2=1\),
growth iff some unit \(\hat\rho\) has \(|\operatorname{Im}\kappa|>|\operatorname{Re}\kappa|\),
\(\kappa=k\cdot\hat\rho\). On slice \(k\) at \(u=0\):
\(\mathbf u=(\cos(3\pi/8)r^0,\cos(\pi/8)\vec r)\),
\(\mathbf v=(\sin(3\pi/8)r^0,-\sin(\pi/8)\vec r)\), growth sign = sign of
\(B=\mathbf v\mathbf v^{\mathrm T}-\mathbf u\mathbf u^{\mathrm T}\) on unit \(\hat\rho\);
\(\operatorname{supp}B=\operatorname{span}\{\mathbf e_0,\hat{\mathbf r}\}\), block
\((1/\sqrt2){\small\begin{pmatrix}{(r^0)}^2&-r^0r\\-r^0r&-r^2\end{pmatrix}}\),
\(\lambda_{\max}=[{(r^0)}^2-r^2+\sqrt{{(r^0)}^4+6{(r^0)}^2r^2+r^4}]/(2\sqrt2)\);
\(\lambda_{\max}>0\iff r^0\ne0\) (whole proof: radicand minus \((r^2-(r^0)^2)^2\) is
\(8(r^0)^2r^2>0\), verified symbolically); at \(r^0=0\) the block is negative semidefinite
and the neutral set is the 9-dim \(\vec r\cdot\hat\rho=0\) with
\(B=-\cos(\pi/4)(\vec r\cdot\hat\rho)^2/r^2<0\) off it. So within the commuting-ray class the
LHS obstruction can only come from \(r^0\ne0\): a genuine narrowing of 054's "unresolved on
that slice at \(k\ne0\)".

### C. Exact branch integral, pointwise exponents, and the corrected \(u\)-scope

Unchanged closed form \(\int_{\mathbb R}\mathrm e^{-Qa^2}2\cos(\gamma_{\mathrm c}|a|)
\,\mathrm da=2\sqrt{\pi/Q}\,\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\) (complex; the erf terms
cancel between half-lines — NOT \(2\operatorname{Re}\) of one branch),
\(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\), verified to rel \(5\cdot10^{-51}\)
against the Gaussian-moment series and to \(0\) against quadrature. With
\(Q=\mathrm e^{-2\mathrm i\alpha}(\epsilon-\mathrm i\gamma/2)\), \(\alpha=3\pi u/8\):
\(\gamma=0\) growth exponent \({(r^0)}^2\cos(3\pi u/4-\pi/4)/(16\epsilon)\); fixed
\(\gamma<0\) saturation exponent \({(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)\) (gatekeeper
re-derived EXACTLY, incl. the \(16/8\) consistency). NEW in r2 (F3): the sign split of
\(\sin(3\pi u/4-\pi/4)\) — negative on \(0\le u<1/3\), zero at \(u=1/3\), positive on
\(u>1/3\). Rank-2 reading, corrected: the pointwise-domination obstruction to the
\(\gamma\to0^-\) bridge exists ONLY for \(u>1/3\) (there the required factor blows up like
\(\mathrm e^{\text{pos}/|\gamma|}\)); for \(u<1/3\) the branch saturation factor tends to 0
as \(\gamma\to0^-\), so along this branch nothing blows up and the bridge is limited only by
the remaining (regulator/mass-term and transverse) factors. Normalization note unchanged:
code normalization \({(r^0)}^2/(16\sqrt2\,\epsilon)=0.0442/\epsilon\) vs 054 ray value
\((b^2-a^2)/(8c\epsilon)=0.1768/\epsilon\) at \(r^0=1\) — ratio 4 (F5; Pauli factor
\(\operatorname{Tr}\sigma^a\sigma^a/4=1/2\) with \((r^0)^2\) scaling); the insert uses the
manuscript's exact \(2\cos(\rho_X/2)\) (16-)normalization.

### D. Reduced \(N=2\) numerics (numerical, reduced model; unchanged machine, corrected labels)

The 053/054 reduced chart (three complex commuting-sector variables
\((w_1,w_2,w_3)=(\mathrm e^{s},\mathrm e^{s-v},\mathrm e^{s-v-z})\), regulator (A), contours
\(\mathcal R_u\), mass \(\gamma\), Vandermonde/Pfaffian and Jacobian factors as in 053),
insertion modes "bare"/"trivial"/"exact"(Taylor, \(\epsilon\ge0.1\) only)/"factor"(factorized
branch surrogate validated against exact mode and against \(\operatorname{Tr}I=2\) at
\(r^0\to0\)). `n2_slice_r1.py`/`n2_slice_r1.out` are BYTE-IDENTICAL to r1 (the r1 gatekeeper
re-ran the script and confirmed all 26 data lines reproduce): E1 ladder ratios
\(1.986\!\to\!2.000\) with fit slope \(0.0000\) vs pointwise corner \(0.0442/0.1768\); E2
\(\gamma=-0.2\) row \(0.94696,1.2550,0.74696,1.2213\) and \(\gamma=-0.05\) row
\(1.6237,1.7661,1.5708,1.7788\), predicted saturation \(1.444,4.347\) not realized (measured
vs \(\gamma=0\): \(0.375\)–\(0.892\)); E3 pure-spatial carrier proxy grows polynomially
(\(\approx\epsilon^{-1.1}\)), not exponentially. Mechanism near the soft corner
\(\Lambda=w_2+w_3\to0\): Vandermonde\(\times\)Jacobian\(\times\)measure powers
\(\Lambda^{5}\)–\(\Lambda^{8}\) (chart power counting); stated as an identified mechanism,
hedged in the insert per F4. Honesty limits unchanged: same-grid modulus RATIOS only
(absolute \(|Z_\epsilon|\) at small \(\epsilon\) is oscillation-resolution-limited);
commuting-sector reduction, not the full \(4N^2\)-real-dimensional integral.

### E. Comparison with the original target

As in r1: (i) RHS boundedness on the slice is structurally explained (A); (ii) the candidate
LHS obstruction inside the slice is localized to \(r^0\ne0\) commuting rays (B); (iii) the
only pointwise growth channel is pinned to a closed-form branch factor whose
\(\gamma\)-non-uniformity exists only for \(u>1/3\) (C); (iv) in the reduced model the LHS
ratio is bounded (\(\to2\)) with fit exponent 0 and the fixed-\(\gamma<0\) saturation is not
realized (D). NOT achieved: an analytic LHS bound for the full \(N=2\) slice integral at
\(r^0\ne0\); no status change is claimed.

## Claim classification

- Cauchy–Binet identity at \(a=1..3\) (contraction and matrix side); \(u=1\) Hermiticity of
  \(r^\mu\tilde A_\mu\); \(|O_k|\le2\) on the \(\mathcal R_1\) slice; rank\((B)\le2\);
  \(\lambda_{\max}\) formula and sign lemma; branch closed form
  \(2\sqrt{\pi/Q}\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\); pointwise exponents
  \(\cos(3\pi u/4-\pi/4){(r^0)}^2/(16\epsilon)\),
  \(\sin(3\pi u/4-\pi/4){(r^0)}^2/(8|\gamma|)\); sign table of \(\sin(3\pi u/4-\pi/4)\):
  established (symbolic/analytic + 50-dps numeric, `slice_ray_r1.py`/`slice_ray_r2.out`).
- "Pure spatial slice momenta admit no commuting growth ray; neutral set
  \(\hat{\mathbf r}\cdot\hat\rho=0\)": established, but a statement INSIDE the rank-one
  commuting-ray model class of 054 (conditional on that class for the LHS question).
- Reduced-chart results (E0–E3), corrected ratio interval \([0.74696,1.7788]\), saturation
  non-materialization, fit slopes: numerical (reduced model, finite grids; `.out`
  reproducible byte-identically).
- "Saturation constant decays as \(\gamma\to0^-\) for \(u<1/3\)": established sign statement
  about the exact model-level exponent; it is NOT a derived bridge — the full bridge remains
  unresolved.
- Phase-space suppression near the soft corner: mechanism identified from chart power
  counting + numerics; conjecture (no domination lemma proved; insert hedges accordingly).
- Full \(N=2\) slice LHS at \(r^0\ne0\), and any \(\gamma\to0^-\) domination theorem:
  unresolved.

## Proposed changes

One file: `chapters/appH-microscopic-proofs.tex`. One insertion, between the merged 054
paragraph (line 1512) and the Problem E Status paragraph (lines 1515–1516). Nothing else in
the manuscript is changed; no `\ref`, `\cite` or `\label` is introduced (verified: the insert
contains none), so no bibliography additions.

- Anchor (exact bytes, verified count 1 in the CURRENT tree by `apply_check.py` →
  `apply_check_r2.out`):
  `\r\n\r\n\r\n\paragraph{Status.}\r\nRemains Assumption~\ref{ass:lorentzian}.`
  (three CRLFs: end of 054 paragraph line, blank, blank; then the Status paragraph).
- The r2 insert (`appH_insert.tex`, LF file 3020 B sha256
  fbc868e6e4a584e740aba2bba4e74e33940fa5d64b3f728e719885e294faea28; CRLF form 3021 B sha256
  e3f0057f3b4457fdf211a6a87b32ee60b61dcbf699f13760a52d726958ad1584) equals the archived r1
  insert (`appH_insert.r1.tex`, 2907 B sha256
  c7b5831e0fa10255e9b37e3d8a206b779ebf63dee97f21b14a570d42cb04923d) with EXACTLY four spans
  substituted (the gatekeeper's Corrected-snippet items 1–4; per-span byte deltas
  \(0,+1,+59,+53\), total \(+113\)):
  1. `\rho_X^2=\sum_{a=1}^{2}{(k^\mu A^a_\mu)}^2` → `...\sum_{a=1}^{3}...`
  2. `it stays between \(0.75\) and \(2.2\)` → `it stays between \(0.74\) and \(1.78\)`
  3. `...\({8|\gamma|)}\) that diverges as \(\gamma\to0^-\).` → `...\({8|\gamma|)}\), which
     diverges as \(\gamma\to0^-\) when \(3\pi u/4-\pi/4>0\) and decays when it is negative.`
  4. `the corner branch growth being phase-space suppressed near the soft corner by
     Vandermonde and measure powers.` → `consistent with phase-space suppression of the
     corner branch growth near the soft corner by Vandermonde and measure powers, though no
     domination lemma is claimed.`
  All other sentences byte-identical to the r1 insert that the gatekeeper judged "the
  smallest accurate record of the verified results".
- Application rule (unchanged from r1): the anchor is replaced by CRLF CRLF +
  insert(CRLF form) + the original anchor: one blank line after the 054 paragraph, the new
  paragraph, the original two blank lines before `\paragraph{Status.}`. The 054 paragraph and
  the Status paragraph stay verbatim.
- Realized in the fresh out-of-repo copy `C:/Users/redgi/tmp/055_apply_r2`: appH 540349 B
  (= 537324 + 3021 + 4), CRLF 3209, bare-LF 0, sha256
  5766105967f830ae8817cc50636d881315ddaa62070e5dfd875727b675fc4cce; the 055 paragraph marker
  occurs once; the Status tail occurs once; `namcg-book7.tex` and bib untouched.
- Build of that copy (`build_check_r2.out`): pdflatex passes 1/2/3 exit 0/0/0; pass2 and
  pass3: 359 pages, 0 undefined references, 0 multiply-defined, 0 `!` errors; pass3 has 0
  LaTeX warnings (pass2's single warning was "Label(s) may have changed"). The r1 copy
  `C:/Users/redgi/tmp/055_apply_r1` corresponds to the r1 text and was left in place
  (author cleanup), as directed.
- Stale-passage check: unchanged from r1 — line 1510's "The next paragraph sharpens this…"
  still refers to the 054 paragraph (immediately next); the 054 sentence "unresolved on that
  slice at \(k\ne0\)" is not contradicted; no other file needs or gets a change.

The full r2 insert paragraph (identical to `appH_insert.tex`):

```latex
\emph{The slice at \(k\ne0\): refinement of the window and model-level growth control.} On the slice \(k^0\mathrm e^{-3\pi\mathrm i/8}=r^0\in\mathbb R\), \(k^i\mathrm e^{\pi\mathrm i/8}=r^i\in\mathbb R\) the Cauchy-Binet identity \(\rho_X^2=\sum_{a=1}^{3}{(k^\mu A^a_\mu)}^2\) is exact at \(N=2\), and on \(\mathcal R_1\) the contraction \(k^\mu A_\mu\) reduces to the Hermitian real-linear form \(r^\mu\tilde A_\mu\), so \(\rho_X\) is real and \(|O_k|\le2\) pointwise there; right-hand-side boundedness on the slice is structural. The commuting-ray alternative also refines inside the slice: at \(u=0\), writing the growth functional as \(B=\mathbf v\mathbf v^{\mathrm T}-\mathbf u\mathbf u^{\mathrm T}\) with \(\mathbf u=(\cos(3\pi/8)r^0,\cos(\pi/8)\vec r\,)\), \(\mathbf v=(\sin(3\pi/8)r^0,-\sin(\pi/8)\vec r\,)\), the matrix \(B\) is supported on \(\operatorname{span}\{\mathbf e_0,\hat{\mathbf r}\}\), has rank at most two, and \(\lambda_{\max}(B)=[{(r^0)}^2-r^2+\sqrt{{(r^0)}^4+6{(r^0)}^2r^2+r^4}]/(2\sqrt2)\), which is positive iff \(r^0\ne0\); for pure spatial slice momenta (\(r^0=0\)) there is no commuting ray with growth, the neutral set is \(\hat{\mathbf r}\cdot\hat\rho=0\), and \(B\) is negative off it. For \(r^0\ne0\) the one-dimensional branch integral \(\int_{\mathbb R}\mathrm e^{-Qa^2}\,2\cos(\gamma_{\mathrm c}|a|)\,\mathrm da=2\sqrt{\pi/Q}\,\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\), \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\), gives pointwise modulus growth \(\mathrm e^{{(r^0)}^2\cos(3\pi u/4-\pi/4)/(16\epsilon)}\) for the soft temporal mode at \(\gamma=0\), saturating as \(\epsilon\to0^+\) at fixed \(\gamma<0\) to a constant of order \(\mathrm e^{{(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)}\), which diverges as \(\gamma\to0^-\) when \(3\pi u/4-\pi/4>0\) and decays when it is negative. In the reduced \(N=2\) integral (regulator (A), contours \(\mathcal R_u\), \(\epsilon\to0^+\) last) with this insertion at pure temporal slice momenta, the modulus ratio \(|Z_\epsilon[O_k]|/|Z_\epsilon[1]|\) stays of order one and tends to \(2\) along the ladder down to \(\epsilon=3\cdot10^{-3}\) (fit slope \(0.0000\) of \(\ln\)-ratio against \(1/\epsilon\), against the pointwise corner value \(0.044/\epsilon\) at \(r^0=1\)), and at \(u=0.6\) with \(\gamma=-0.2,-0.05\) it stays between \(0.74\) and \(1.78\): in the reduction neither the commuting-ray growth \(\mathrm e^{c_2(k)/\epsilon}\) nor the pointwise saturation factor materialises, consistent with phase-space suppression of the corner branch growth near the soft corner by Vandermonde and measure powers, though no domination lemma is claimed. These are reduced-model computations with oscillation-limited resolution at \(\gamma=0\); whether the left-hand side is controlled on the slice at \(k\ne0\) with \(r^0\ne0\) remains open at full \(N=2\), the \(\gamma\to0^-\) bridge from fixed-\(\gamma<0\) success remains open, and the pure-spatial half of the slice is now ray-free; Problem~E remains open and PROGRAMME-CONDITIONAL.
```

Style conformance: as in r1 — `\(\)` math, `\epsilon`, `\mathcal R_u`, `\vec r`,
`\hat\rho`, `\operatorname`, `\mathrm e` match the 054 paragraph's macros; ASCII-only; one
paragraph; single scoped closing status sentence; no process language.

## Verification scripts

All in this folder; run with `python -I`; saved outputs alongside:

- `patch_insert_r2.py` (3013 B, sha256 5976453815fe01c0d08cde0b80e25b2dae4df780a6541fe5f0a541939440173e)
  → `patch_insert_r2.out` (398 B, sha256 46b7385dcef8d66aadd2f2466adbe8ca58d8eb6c12039ab4414bb85f9313d9a8):
  applies the four F1–F4 spans r1→r2 with pins (r1 2907 B c7b5831e…), count==1 asserts per
  OLD span, NEW-present/OLD-absent asserts, reconstruction test, size-delta check
  (\([0,+1,+59,+53]\), total \(+113\)); regenerates identical bytes on re-run (idempotence);
  prints r2 LF 3020 B fbc868e6…, CRLF 3021 B e3f0057f…. Raw byte literals use SINGLE
  backslashes (the 054-style double-backslash anchor bug is avoided and asserted away).
- `slice_ray_r1.py` (r2 content: 10991 B, sha256 7648545ebd110127bc64bcb2e4662ab680de9536bb9535bba126daf667521b7b)
  → `slice_ray_r2.out` (2802 B, sha256 ccadfb72c693774bd7c81e238634e247d19a3543837c1d2b8873a313610ac0f1;
  re-run byte-identical): sec.1 full-range charpoly check (0), non-tautological matrix-side
  vs contraction-side check (max rel \(4.596\cdot10^{-51}\)), \(a=1..2\) generic failure
  (\(2.094\)), counterexample (\(-4\det=1.0\) vs 0), \(a=1..3\) polynomial identity (0),
  \(u=1\) coefficient check (\(r^0,r^1\)); sec.2 unchanged from r1 (block, \(\lambda_{\max}\)
  diffs 0, sign-lemma samples, \(8b^2{r^0}^2\), rank/nullspace, \(r^0=0\) values); sec.3
  branch checks unchanged (rel errs \(0,5\cdot10^{-51},1.6\cdot10^{-48}\), quadrature 0)
  with the F5 label fix ("ratio 4 vs ray value; Pauli normalization, \((r^0)^2\) scaling").
  The r1 output `slice_ray_r1.out` (2295 B, 6d96793d…) is kept for traceability; its sec.1
  numeric line is superseded (F1/F7 + mpmath constructor disclosure).
- `n2_slice_r1.py` (15230 B, sha256 8d1523d74be8fe47545af7aa35afd68e29f78dab7348654f6ea9e5ad1ae3d42f)
  → `n2_slice_r1.out` (2851 B, sha256 e17a86cf8e9c9c32c60de0da0c9833d0fe79df4db6c5aee0adba68a97116384d):
  UNCHANGED (byte-identical to r1; the F2 fix is in the insert wording, the numerics
  untouched). E2 rows: \(\gamma=-0.2\): 0.94696/1.2550/0.74696/1.2213; \(\gamma=-0.05\):
  1.6237/1.7661/1.5708/1.7788; predicted saturation 1.444/4.347 vs measured 0.375–0.892.
- `apply_check.py` (6015 B, sha256 0f57fabba3c56092e463ec060ad7f06942aeb62453fc09ba4d13b77958e447b8,
  unchanged; reads `appH_insert.tex` from disk, so r2 outputs come from the r2 insert):
  report mode → `apply_check_r2.out` (958 B, sha256 48cd86728e4be6e06bc9bcbddd0389f5fddf5559e3ec58269e4e97fa10ab0dc0):
  pins True/True (current tree), 054-marker 1, 055-marker 0, anchor count 1, insert ASCII,
  no cite/ref/label, expected realized size 540349. `--copy C:/Users/redgi/tmp/055_apply_r2`
  → `apply_copy_r2.out` (1318 B, sha256 3a02062331995cc4d11341def5e5f8d7a8d3e70669e01e5d6d6458cfc8e37a42):
  applied appH 540349 B, CRLF 3209, bare-LF 0, sha256 5766105967f830ae8817cc50636d881315ddaa62070e5dfd875727b675fc4cce.
- `build_summary_r2.py` (1223 B, sha256 deaaacb3b30fa5533856ab4165c5d9de625576dbfb0d65a7b10f51207ea08e1a)
  → `build_check_r2.out` (573 B, sha256 ad6c6c1e1aae3b9d9f2c1cf3aee82000c44ed1deae8447a5e92c39a89d94bec2):
  pass1 exit 0 (353 pp, 1149 undefined — cold aux), pass2 exit 0 (359 pp, 0 undefined, 0
  multiply, 1 warning "Label(s) may have changed"), pass3 exit 0 (359 pp, 0 undefined, 0
  multiply, 0 warnings, 0 errors); final PDF 2666262 B sha256
  89c71a79107f9542fb68984ceae08576420f30132214d622453648b3cd82d6f7.
- r1 superseded artifacts kept: `apply_check_r1.out` (958 B, 03dd4b6a…), `apply_copy_r1.out`
  (1318 B, dcd5c40f…), `build_check_r1.out` (361 B, 0688c14a…), `proposal-r1.md` (31436 B,
  19f15a14…), `review-r1.md` (13004 B, 4d91375f…), `appH_insert.r1.tex` (2907 B, c7b5831e…).

## Decisions Taken

1. **Adopted the gatekeeper's four substitutions verbatim** (byte-span patcher
   `patch_insert_r2.py`) rather than rewording: they are the minimal accurate fixes and the
   gatekeeper explicitly judged all other insert sentences final. Rejected: independent
   rewording (risks divergence from the accepted corrected snippet).
2. **F2 interval: chose option (a) of the review note** — "between \(0.74\) and \(1.78\)"
   for the stated \(\gamma=-0.2,-0.05\) rows. Rejected option (b) (restating the \(\gamma\)
   list to include the \(\gamma=0\) row): the \(\gamma=0\) value 2.1574 belongs to the
   growth-slope discussion, not the saturation sentence, and widening the sentence's scope
   would blur the E2 claim structure.
3. **F7 fixed beyond a re-run**: replaced the tautological symbolic-only check with a
   non-tautological matrix-side (via \(-4\det\)) vs contraction-side comparison plus the
   explicit counterexample. Disclosure kept in the proposal and in the script comment: the
   first r2 attempt was silently wrong because mpmath 1.3.0's 3-arg `mp.matrix(m,n,S)`
   builds ZERO matrices from list/dict/callable inputs (and `mp.matrix(2,2,flat_list)`
   likewise); the fix is the nested-rows constructor. A defensive numpy→`mp.mpc(float,float)`
   helper was kept even though direct `mp.mpc(np.complex128)` works in 1.3.0 — harmless and
   removes a conversion ambiguity. Rejected: keeping the symbolic-only tautological check.
4. **Third pdflatex pass added** to clear the pass-2 "Label(s) may have changed" warning and
   stabilize pagination (359 pp identical in passes 2 and 3). Rejected: reporting the
   2-pass result with the residual warning.
5. **Kept r1 artifacts and `C:/Users/redgi/tmp/055_apply_r1` in place** (author cleanup per
   instruction); r2 outputs are new files, never overwritten r1 records. The old `054`
   warning-style rb-string trap was avoided and asserted (single-backslash raw literals).
6. r1 decisions 1–5 (factorized surrogate as the ladder mode; same-grid ratios only;
   Hörmander lead abandoned/no citation; 16-normalization in the insert; E3 out of the
   insert) stand unchanged.

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step is derived; the slice window stays
open; the package remains structural narrowing + model-level evidence inside the 054 class.

## Status-label recommendation

Current critical-path set re-derived from ch17 (A, B, C, D1, E, F, G-derived, N; H/I/J
optional): unchanged by this package. Problem E stays OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL (appH L1486–1489 re-verified verbatim against the current tree). No
label changes proposed.

## Author decision needed

None.

## Remaining open step

Ranked avenues (gatekeeper review-r1 ranking adopted):

1. **Uniform-bound promotion:** prove the reduced-model "ratio \(O(1)\), fit slope 0" as a
   uniform bound for the FULL \(N=2\) slice integral at \(r^0\ne0\) — a transverse domination
   lemma implementing the observed phase-space suppression (Vandermonde/Pfaffian
   \((\det\mathcal G)^4\) and Jacobian powers \(\Lambda^5\)–\(\Lambda^8\) vanishing near each
   rank-one ray, uniformly in \(\epsilon\)). This alone would extend the limit identity to the
   slice.
2. **\(\gamma\to0^-\) bridge for \(u<1/3\):** by F3 the branch saturation constant DECAYS as
   \(\gamma\to0^-\) there, so no branch-factor obstruction exists; only the regulator mass
   term and transverse factors must be controlled. Unobstructed and under-explored.
3. **Pure-spatial sub-window:** the \(r^0=0\) half is now ray-free at the commuting-ray level
   (E3 proxy: polynomial not exponential growth), so only \(r^0\ne0\) slice rays remain for
   a full treatment.
4. Non-factorized exact insertion at small \(\epsilon\) by resummation (currently
   \(\epsilon\ge0.1\)); non-commuting-mode extension toward the full \(N=2\) slice integral.
5. Explicitly NOT attempted (rank 3): regulator-class and \(N\ge3\) extensions.

## Special instructions for the gatekeeper

- The r2 insert is the r1 insert with EXACTLY four spans changed (`patch_insert_r2.py`
  pins/asserts/reconstructs this); diff `appH_insert.r1.tex` vs `appH_insert.tex` to confirm
  the four spans and nothing else.
- Re-run `slice_ray_r1.py` (deterministic; byte-identical to `slice_ray_r2.out`) and
  `n2_slice_r1.py` (unchanged, ~47 s; byte-identical to `n2_slice_r1.out`).
- When re-deriving the matrix-side check note the mpmath 1.3.0 trap: `mp.matrix(m,n,S)`
  (3-arg) and `mp.matrix(2,2,flat)` silently produce ZERO matrices; use
  `mp.matrix([[...],[...]])`. A check built on the broken constructor is vacuously true if
  both sides are zero.
- Re-derive by hand: charpoly of \(\sum w_a\sigma^a/2\);
  \(-4\det(k\!\cdot\!A)=\sum_{a=1..3}{(k^\mu A^a_\mu)}^2\) for traceless \(2\times2\);
  the sign of \(\sin(3\pi u/4-\pi/4)\) at \(u=0,0.3,1/3,0.6\); ratio
  \(0.1767766953/0.0441941738=4\); the saturation exponent
  \({(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)\) from \(-\gamma_{\mathrm c}^2/(4Q)\) at
  \(\epsilon\to0\), fixed \(\gamma<0\).
- Pins to re-verify (current tree): appH 537324 B sha 943816e923a844521faf56fc88774cd0827eca501f69bb7b12dc9f4af18e8571
  (CRLF 3206, bare-LF 0); bib 25976 B sha a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b;
  anchor count 1; insert LF 3020 B fbc868e6…, CRLF 3021 B e3f0057f…; expected applied size
  540349 (= 537324+3021+4), realized 540349 B CRLF 3209 bare-LF 0 sha 57661059….
  `--copy` refuses an existing DIR: use a fresh DIR if rebuilding.
- Must NOT be asserted: that the slice window is closed; that the full-\(N=2\) LHS is
  controlled; that the \(\gamma\to0^-\) bridge is derived for any \(u\); that the reduced-chart
  results are results for the full integral; that pure-spatial ray-freeness settles the LHS
  for \(r^0=0\) beyond the commuting-ray class (E3 is a proxy); that the saturation constant
  diverges at \(u=0\) (it DECAYS — F3); that the [0.74, 1.78] interval includes the
  \(\gamma=0\) row (2.1574).
- Numerical claims in the insert trace to: `n2_slice_r1.out` E1/E2 lines (interval
  [0.74696, 1.7788]; "tends to 2 … down to 3e-3" covers 1.9998/1.9999 (\(r^0=1\)) and
  1.9993/1.9998 (\(r^0=2\)); corner 0.0442/0.1768) and `slice_ray_r2.out` (exponents,
  normalization ratio 4). No number in the insert comes from anywhere else.
- Proposed ordinal: the review kept it at 53; full scan not due until 55.
