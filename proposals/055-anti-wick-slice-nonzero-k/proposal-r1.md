# Proposal 055-anti-wick-slice-nonzero-k, round 1

## Result

Within the hypothesis class of the merged proposal-054 paragraph (appH line 1512: \(N=2\),
\(O_k=\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\), \(k\in\mathbb C^{10}\), \(\gamma=0\),
regulator (A), contours \(\mathcal R_u\), \(\epsilon\to0^+\) last), the package narrows the
window that 054 left unresolved ("unresolved on that slice at \(k\ne0\)") and gives model-level
control of the left-hand side on that slice:

1. **Established (exact).** The Cauchy–Binet identity \(\rho_X^2=\sum_{a=1}^{2}(k^\mu A^a_\mu)^2\)
   for \(N=2\) makes the boundedness of the right-hand side of the displayed limit identity on
   the anti-Wick slice structural: on \(\mathcal R_1\) the contraction \(k^\mu A_\mu\) reduces
   to the Hermitian real-linear form \(r^\mu\tilde A_\mu\), so \(\rho_X\) is real and
   \(|O_k|\le2\) pointwise (symbolic verification, script 1).
2. **Established (model-level, within the rank-one commuting-ray class of 054).** Inside the
   slice at \(u=0\) the commuting-ray growth functional is
   \(B=\mathbf v\mathbf v^{\mathrm T}-\mathbf u\mathbf u^{\mathrm T}\), supported on
   \(\operatorname{span}\{\mathbf e_0,\hat{\mathbf r}\}\), of rank \(\le2\), with
   \(\lambda_{\max}(B)=[{(r^0)}^2-r^2+\sqrt{{(r^0)}^4+6{(r^0)}^2r^2+r^4}]/(2\sqrt2)>0\) iff
   \(r^0\ne0\). For pure spatial slice momenta (\(r^0=0\)) there is no commuting ray with
   growth (054's strict-growth criterion is unattainable there), the neutral set is
   \(\hat{\mathbf r}\cdot\hat\rho=0\) and \(B\) is strictly negative off it. The possible
   commuting-ray obstruction to the \(\epsilon\to0^+\) left-hand side therefore concentrates on
   the half of the slice with \(r^0\ne0\).
3. **Established (exact branch identity) + conditional (its role as worst case).** The
   one-dimensional branch integral
   \(\int_{\mathbb R}\mathrm e^{-Qa^2}2\cos(\gamma_{\mathrm c}|a|)\,\mathrm da
   =2\sqrt{\pi/Q}\,\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\),
   \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\), gives pointwise modulus growth
   \(\mathrm e^{{(r^0)}^2\cos(3\pi u/4-\pi/4)/(16\epsilon)}\) at \(\gamma=0\), saturating at
   fixed \(\gamma<0\) to \(\mathrm e^{{(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)}\), which
   diverges as \(\gamma\to0^-\): the pointwise domination is NOT uniform in \(\gamma\)
   (rank-2 input: any transfer of the 054 fixed-\(\gamma<0\) success to \(\gamma=0\) cannot
   rest on pointwise/Gaussian domination along the soft temporal branch; it must use
   suppression from the remaining directions).
4. **Numerical (reduced \(N=2\) model).** With the exact slice insertion in the reduced
   \(N=2\) integral (regulator (A), \(\mathcal R_u\), \(\epsilon\to0^+\) last), at pure
   temporal slice momenta the modulus ratio \(|Z_\epsilon[O_k]|/|Z_\epsilon[1]|\) stays of
   order one and tends to \(2\) along the ladder down to \(\epsilon=3\cdot10^{-3}\) (fit slope
   \(0.0000\) of the log-ratio against \(1/\epsilon\) versus the pointwise corner value
   \(0.044/\epsilon\) at \(r^0=1\), \(0.177/\epsilon\) at \(r^0=2\)). At \(u=0.6\),
   \(\gamma=-0.2,-0.05\), the ratios stay between \(0.75\) and \(2.2\) and the predicted
   saturation factors \(1.44,4.35\) do not materialize. In the reduction the commuting-ray
   growth \(\mathrm e^{c_2(k)/\epsilon}\) and the pointwise saturation factor are both
   phase-space suppressed near the soft corner.
   The slice window is therefore NOT closed at full \(N=2\) — the reduced chart is a
   commuting-sector reduction — but no obstruction to its control appears at model level, and
   the mechanism that would have to be beaten (pointwise branch growth) is pinned down.

Nothing is closed: Problem E remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL, and
Assumption~\ref{ass:lorentzian} is not discharged.

## Target and status

- Problem E (signature), `chapters/appH-microscopic-proofs.tex` Section "Problem E: signature"
  (`\label{sec:status-E}`). Ledger label quoted verbatim (lines 1486–1489): "Status: OPEN.
  Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A
  scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or
  matrix-derived Lorentzian signature."
- Chapter 17 (`chapters/ch17-agenda.tex` lines 394–399): "Problem E: Lorentzian signature.
  OPEN; CRITICAL PATH for the matrix-derived label."; completion item (lines 718–719):
  "Problem~E: Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})."
- Original target of the E ledger line relevant here: the displayed \(\epsilon\to0^+\) limit
  identity of the "Limit at finite \(N\)" paragraph extended beyond polynomial \(O\).
  The merged 054 paragraph (appH line 1512) established, within its class, that the identity
  FAILS for every nonzero real \(k\) and every non-real \(k\) off the slice
  \(\{k^0\mathrm e^{-3\pi\mathrm i/8},\,k^i\mathrm e^{\pi\mathrm i/8}\in\mathbb R\}\), HOLDS at
  \(k=0\), and is UNRESOLVED on the slice at \(k\ne0\).
- Rank-1 target of this package: settle/control the slice window (LHS control: transverse
  domination, stationary-phase/Pfaffian suppression, exact \(N=2\) reduction, or a bounded
  negative result on a named \(k\) subclass). Rank-2 (same derivation): what the fixed
  \(\gamma<0\) success implies for \(\gamma=0\) slice control (\(\gamma\to0^-\) uniformity).
  Rank-3 (regulator/\(N\) extension) not attempted, as instructed.
- DERIVED vs PROGRAMME-CONDITIONAL: everything here is PROGRAMME-CONDITIONAL evidence inside
  the 054 hypothesis class; it is conditional on the reduced \(N=2\) chart for item 4 and is
  model-level (rank-one rays / single branch) for items 2–3. No label changes are proposed.

## Source reading

digest + targeted reads. `scratch/digest.md` (DIGEST CURRENT at run start), read in full:
`chapters/appH-microscopic-proofs.tex` lines 1480–1519 (Problem E ledger block including the
contours paragraph, the flat-direction bound, the finite-\(N\) limit paragraph, definition (C),
the 053 closing paragraph at line 1510 and the merged 054 paragraph at line 1512);
`chapters/ch17-agenda.tex` lines 392–401 and 697–719; the merged proposal-054 folder
(`proposal-r2.md`, `review-r2.md`, `apply_check.py`) and proposal 053's `apply_check.py` /
`make_copy_r3.py` for the anchor machinery; `MILESTONE.md` triggers; `reports/ledger.md`
tail. Pins re-verified at run time: appH 537324 B sha256
943816e923a844521faf56fc88774cd0827eca501f69bb7b12dc9f4af18e8571, CRLF 3206, bare-LF 0;
bib 25976 B sha256 a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b.
No unreadable files. Literature lead on Hörmander-type domination theorems was ABANDONED
(could not verify a specific applicable statement); no citation is imported anywhere in this
package, so `bib_additions.bib` is intentionally absent (the insert contains no `\cite`).

## Research and reasoning

### A. Cauchy–Binet and the structural RHS bound (established)

At \(N=2\), write \(A_\mu=\sum_a A^a_\mu\sigma^a/2\) and
\(\mathcal G_{\mu\nu}=\sum_{a}A^a_\mu A^a_\nu\) (the manuscript's \(\mathcal G\) in the
"flat directions" paragraph). Then
\(\rho_X^2=k^\mu k^\nu\mathcal G_{\mu\nu}=\sum_{a=1}^{2}{(k^\mu A^a_\mu)}^2\): a polynomial
identity, verified symbolically in `slice_ray_r1.py` section (1) (difference simplifies to 0).
For slice \(k\) (\(k^0\mathrm e^{-3\pi\mathrm i/8}=r^0\),
\(k^i\mathrm e^{\pi\mathrm i/8}=r^i\in\mathbb R\)) on \(\mathcal R_1\) the contour factors
cancel: \(k^0 A_0=r^0\tilde A_0\), \(k^iA_i=r^i\tilde A_i\) (verified symbolically), so
\(k^\mu A_\mu=r^\mu\tilde A_\mu\) is Hermitian, \(\rho_X^2\ge0\), \(\rho_X\in\mathbb R\) and
\(O_k=2\cos(\rho_X/2)\) satisfies \(|O_k|\le2\) pointwise. This is the mechanism behind the
054 assertion "there \(|O_k|\le2\) and that side converges by the \(k<14\) Pfaffian window";
it upgrades that assertion from stipulated to structural, and it does not touch the LHS.

### B. Slice-ray trichotomy at \(u=0\) (established within the rank-one class)

054's commuting-ray alternative takes \(\tilde A_\mu=\rho_\mu H\), \(\operatorname{Tr}H^2=1\),
and finds growth when some unit \(\hat\rho\) has
\(|\operatorname{Im}(k\cdot\hat\rho)|>|\operatorname{Re}(k\cdot\hat\rho)|\) (growth exponent
\((|\operatorname{Im}\kappa|^2-|\operatorname{Re}\kappa|^2)/(8c\epsilon)\)-type,
\(\kappa=k\cdot\hat\rho\)). Restrict to slice \(k\) at \(u=0\): then
\(\kappa(\hat\rho)=\mathbf u\cdot\hat\rho+\mathrm i\,\mathbf v\cdot\hat\rho\) with
\(\mathbf u=(\cos(3\pi/8)r^0,\cos(\pi/8)\vec r)\),
\(\mathbf v=(\sin(3\pi/8)r^0,-\sin(\pi/8)\vec r)\), and the growth sign is that of the
quadratic form \(B=\mathbf v\mathbf v^{\mathrm T}-\mathbf u\mathbf u^{\mathrm T}\) on unit
\(\hat\rho\). \(B\) is supported on \(\operatorname{span}\{\mathbf e_0,\hat{\mathbf r}\}\); in
that basis its block is \((1/\sqrt2)\!\begin{pmatrix}{(r^0)}^2&-r^0r\\-r^0r&-r^2\end{pmatrix}\)
(\(r=|\vec r|\)), so \(\operatorname{rank}B\le2\) and
\(\lambda_{\max}=[{(r^0)}^2-r^2+\sqrt{{(r^0)}^4+6{(r^0)}^2r^2+r^4}]/(2\sqrt2)\).
Sign lemma: \(\lambda_{\max}>0\iff r^0\ne0\): for \(r^0b\ne0\) the radicand minus
\((r^2-(r^0)^2)^2\) is \(8(r^0)^2r^2>0\) (verified symbolically), so the root dominates
\(r^2-(r^0)^2\); at \(r^0=0\), \(\lambda_{\max}=0\) and the block is negative semidefinite
(\(-\cos(\pi/4)r^2\) on \(\hat{\mathbf r}\), 0 on \(\mathbf e_0\)); at \(r=0\),
\(\lambda_{\max}={(r^0)}^2/\sqrt2>0\). Numeric eigenvalue cross-checks (rank, nullspace dim,
max diff 0 over 10-dim samplings) in `slice_ray_r1.py` section (2). Consequences inside the
054 window: for pure spatial slice momenta the strict-growth ray does not exist — the neutral
set is the 9-dim subspace \(\vec r\cdot\hat\rho=0\) and \(B=-\cos(\pi/4)(\vec r\cdot\hat\rho)^2
<0\) off it (decay). So within the commuting-ray class the LHS obstruction can only come from
\(r^0\ne0\). This is a genuine narrowing of 054's "unresolved on that slice at \(k\ne0\)".

### C. Exact branch integral and the pointwise exponents (established identity; worst-case reading conditional)

In the reduced chart of 053/054 the soft temporal branch of the slice insertion is the
one-dimensional integral
\(\int_{\mathbb R}\mathrm e^{-Qa^2}2\cos(\gamma_{\mathrm c}|a|)\,\mathrm da\) with
\(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\) (so \(2\cos(\gamma_{\mathrm c}|a|)
=O_k\) along the ray, \(\rho_X/2=\gamma_{\mathrm c}|a|\): consistent with
\(\rho_X^2=\mathrm e^{3\pi\mathrm i/4}{(r^0)}^2a^2\) from A). Closed form
\(2\sqrt{\pi/Q}\,\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\) (erf terms cancel between the two
half-lines; NOT \(2\operatorname{Re}\) of one branch). Verified to relative \(10^{-48}\)
against the term-by-term Gaussian moment series at 50-digit precision, and against quadrature
(`slice_ray_r1.py` section (3)). With \(Q=\epsilon\mathrm e^{-2\mathrm i\alpha}\),
\(\alpha=3\pi u/8\): modulus growth of the branch factor
\(\mathrm e^{{(r^0)}^2\cos(3\pi u/4-\pi/4)/(16\epsilon)}\) at \(\gamma=0\); with the mass
\(Q=\mathrm e^{-2\mathrm i\alpha}(\epsilon-\mathrm i\gamma/2)\) (mass convention of the
reduced model, cf. the 054 real exponent
\((\gamma/2g_{\mathrm{YM}}^2)[\sin(3\pi u/4)\operatorname{Tr}\tilde A_0^2+\dots]\), \(g_{\mathrm{YM}}=1\)
in the chart): as \(\epsilon\to0^+\) at fixed \(\gamma<0\) the exponent saturates to
\({(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)\), diverging as \(\gamma\to0^-\). Normalization
note (verified numerically): the code-normalization exponent \({(r^0)}^2/(16\sqrt2\,\epsilon)
=0.0442/\epsilon\) at \(u=0,r^0=1\) equals 054's ray value \((b^2-a^2)/(8c\epsilon)
=0.1768/\epsilon\) with \(\operatorname{Tr}H^2=1\) up to the Pauli normalization factor
\(\operatorname{Tr}(\sigma^a\sigma^a/4)=1/2\) — the manuscript paragraph quotes the exact
\(N=2\) \(2\cos(\rho_X/2)\) normalization (16), and the two are consistent.

Rank-2 implication (established at branch-model level): the 054 theorem at fixed
\(\gamma<0\) dominates \(O_k\) by a Gaussian of strength \(|\gamma|\); along the slice branch
the required pointwise growth factor \(\mathrm e^{\text{const}/|\gamma|}\) diverges as
\(\gamma\to0^-\), so a naive \(\gamma\to0^-\) transfer of the domination fails POINTWISE. Any
transfer must be through integrated (phase-space) domination, not pointwise domination.

### D. Reduced \(N=2\) numerics (numerical, reduced model)

Machine: the 053/054 reduced \(N=2\) chart — three complex commuting-sector variables
\((w_1,w_2,w_3)=(\mathrm e^{s},\mathrm e^{s-v},\mathrm e^{s-v-z})\) (\(d=9\) spatial, \(p=4\)),
regulator (A), contours \(\mathcal R_u\), mass \(\gamma\), Vandermonde/Pfaffian and Jacobian
factors as in 053; observables inserted exactly at the quadrature nodes. Insertion modes:
"bare" (\(O=1\)), "trivial" (\(O=\operatorname{Tr} I=2\)), "exact" (term-by-term Taylor
insertion, reliable only for \(\epsilon\ge0.1\) where partial sums stay in float range;
maxterm recorded), "factor" (factorized branch surrogate
\(2\cos(\gamma_{\mathrm c}|a_1|)\) inserted on the soft axis with the remaining Gaussian
axes done analytically by the closed form of C, implemented via the recursion
\(q_{j+1}=x^2\,\partial_x(\mathrm e^{-\gamma_{\mathrm c}^2x/4}q_j)\)-type derivatives of
\(2\sqrt{\pi}x^{1/2}\mathrm e^{-\gamma_{\mathrm c}^2x/4}\), \(x=1/Q\)). Validations (E0):
trivial/bare \(=2.0000000000\) (must be \(\operatorname{Tr} I\)); factor/bare and exact/bare
\(\to2\) as \(r^0\to0\) (\(2.0000000000\), \(1.948\) on the coarser grid used for exact).

Results (`n2_slice_r1.out`):
- E1 (\(u=0,\gamma=0\), pure temporal slice \(k\), \(r^0=1,2\)): factor/bare \(|Z|\) ratio is
  \(1.986,1.997,1.998,2.000,2.000,2.000\) along \(\epsilon=1,0.3,0.1,0.03,0.01,0.003\);
  \(\ln(\text{ratio})=A/\epsilon+B\) fits give \(A=0.0000\) (\(-0.0000\) for
  \(\epsilon\le0.03\)) versus pointwise corner \(A=0.0442\) (\(r^0=1\)) and \(0.1768\)
  (\(r^0=2\)); exact-mode ratios \(2.0\)–\(4.0\) at \(\epsilon\ge0.1\) cross-check the
  surrogate. No \(\mathrm e^{C/\epsilon}\) LHS growth in the reduction.
- E2 (\(u=0.6\), \(r^0=1\), factorized): \(\gamma=0\) fit slope \(0.0003\) vs pointwise
  \(0.0506\); \(\gamma=-0.2,-0.05\) ratios stay in \([0.75,1.8]\); the predicted
  saturation factors \(1.444,4.347\) do NOT materialize (measured ratios vs \(\gamma=0\):
  \(0.38\)–\(0.89\)). At model level the \(\gamma\to0^-\) bridge shows no obstruction.
- E3 (pure-spatial carrier proxy at \(u=0\), insertion modulus \(\ge1\), \(\gamma=0\)):
  \(|Z|\) ratio grows polynomially (\(\approx\epsilon^{-1.1}\) on the sampled range), not
  exponentially — consistent with the ray-free structure of B at \(r^0=0\).
Mechanism: near the soft corner \(\Lambda=w_2+w_3\to0\) (where the pointwise branch growth
lives) the Vandermonde\(\times\)Jacobian\(\times\)measure powers behave as \(\Lambda^{5}\)–
\(\Lambda^{8}\), and the crossover between pointwise growth and measure suppression,
\(\text{const}/\epsilon < m\,\ln(1/\epsilon)\) in the \(\epsilon\)-scaling, is never reached on
the tested ladder: the growth is phase-space suppressed. (Power counting from the chart;
the \(\Lambda\)-powers are the chart's, recorded here as the identified mechanism, not a
proof.)
Honesty limits: this is a commuting-sector reduction, not the full \(4N^2\)-real-dimensional
\(N=2\) integral; at \(\gamma=0,u=0\) the ABSOLUTE \(|Z_\epsilon|\) grows like
\(\epsilon^{-8.5}\)-type powers that are oscillation-resolution artifacts (highly oscillatory
\(\mathrm e^{\mathrm i\lambda\sum_{\mu\nu}A_\mu A_\nu}\) weight at small \(\epsilon\)); only
same-grid RATIOS are reported, and ratios of \(|Z|\) at identical grids cancel those
prefactors. Stated as such in the insert.

### E. Comparison with the original target

Original target: control (settle) the LHS of the displayed limit identity on the anti-Wick
slice at \(k\ne0\) within the 054 class. What is achieved: (i) the RHS half of the window is
now structurally explained (A); (ii) the candidate LHS obstruction inside the slice is
localized to \(r^0\ne0\) commuting rays (B); (iii) the only pointwise growth channel is pinned
to a closed-form branch factor with explicit exponents, and its \(\gamma\)-non-uniformity is
quantified (C); (iv) in the reduced \(N=2\) model the LHS ratio is bounded (\(\to2\)) along
the \(\epsilon\)-ladder with fit exponent \(0\) at the pointwise corner, and the fixed-\(\gamma
<0\) saturation is not realized — i.e. model-level evidence that the window is controllable
and where the proof must go. What is NOT achieved: an analytic LHS bound for the full \(N=2\)
slice integral at \(r^0\ne0\); no status change is claimed or proposed.

## Claim classification

- Cauchy–Binet identity; \(u=1\) Hermiticity of \(r^\mu\tilde A_\mu\); \(|O_k|\le2\) on
  \(\mathcal R_1\) slice; rank\((B)\le2\); \(\lambda_{\max}\) formula and sign lemma; branch
  closed form \(2\sqrt{\pi/Q}\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\); pointwise exponents
  \(\cos(3\pi u/4-\pi/4){(r^0)}^2/(16\epsilon)\) and
  \(\sin(3\pi u/4-\pi/4){(r^0)}^2/(8|\gamma|)\): established (symbolic/analytic, scripts 1).
- "Pure spatial slice momenta admit no commuting growth ray; neutral set
  \(\hat{\mathbf r}\cdot\hat\rho=0\)": established, but a statement INSIDE the rank-one
  commuting-ray model class of 054 (conditional on that class for the LHS question).
- Reduced-chart ratio results (E0–E3), saturation non-materialization, fit slopes: numerical
  (reduced model, finite grids, stated tolerances; `.out` reproducible).
- Phase-space suppression near the soft corner (\(\Lambda^5\)–\(\Lambda^8\) powers, crossover
  scaling): mechanism identified from the chart + numerics; conditional (no domination lemma
  proved).
- Rank-2 transfer implication ("pointwise domination cannot bridge \(\gamma\to0^-\);
  integrated domination must"): established at branch-model level; the full-integral version
  is unresolved.
- Everything for the full \(N=2\) slice LHS at \(r^0\ne0\), and any \(\gamma\to0^-\)
  domination theorem: unresolved.

## Proposed changes

One file: `chapters/appH-microscopic-proofs.tex`. One insertion, between the merged 054
paragraph (line 1512) and the Problem E Status paragraph (lines 1515–1516). Nothing else in
the manuscript is changed; no `\ref`, `\cite` or `\label` is introduced (verified: the insert
contains none), so no bibliography additions (`bib_additions.bib` intentionally absent).

- Anchor (exact bytes, verified count 1 in the current tree by `apply_check.py`):
  `\r\n\r\n\r\n\paragraph{Status.}\r\nRemains Assumption~\ref{ass:lorentzian}.`
  (the three CRLFs are: end of the 054 paragraph line, blank line, blank line; then the
  Status paragraph).
- The insert (`appH_insert.tex`, LF file 2907 B sha256
  c7b5831e0fa10255e9b37e3d8a206b779ebf63dee97f21b14a570d42cb04923d; CRLF form 2908 B sha256
  639fafdb5d2d2ec02111781745bb73cc1559eb049d148871d99807ffa2acb4f5) replaces the anchor by
  CRLF CRLF + insert(CRLF form) + the original anchor: one blank line after the 054
  paragraph, the new paragraph, and the original two blank lines before
  `\paragraph{Status.}`. The 054 paragraph and the Status paragraph stay verbatim.
- Realized in the out-of-repo copy: appH 540236 B, CRLF 3209, bare-LF 0, sha256
  c6ab08f319fefee3267ee98cfbcbd9805032c1e901d55b8bad1587f6515ff1af; the 055 paragraph marker
  occurs once; the Status tail occurs once.
- Stale-passage check: the line-1510 sentence "The next paragraph sharpens this at \(N=2\)
  and \(\gamma=0\)..." still refers to the 054 paragraph (immediately next); unaffected. The
  054 sentence "is unresolved on that slice at \(k\ne0\)" is not contradicted — the insert
  narrows and adds model-level evidence but keeps the slice at \(r^0\ne0\) open, and its own
  closing sentence repeats "Problem~E remains open and PROGRAMME-CONDITIONAL." No other file
  (`ch17-agenda.tex`, ledger sections, Ch.~17 criterion) needs or gets a change.

The full insert paragraph (for the gatekeeper; identical to `appH_insert.tex`):

```latex
\emph{The slice at \(k\ne0\): refinement of the window and model-level growth control.} On the slice \(k^0\mathrm e^{-3\pi\mathrm i/8}=r^0\in\mathbb R\), \(k^i\mathrm e^{\pi\mathrm i/8}=r^i\in\mathbb R\) the Cauchy-Binet identity \(\rho_X^2=\sum_{a=1}^{2}{(k^\mu A^a_\mu)}^2\) is exact at \(N=2\), and on \(\mathcal R_1\) the contraction \(k^\mu A_\mu\) reduces to the Hermitian real-linear form \(r^\mu\tilde A_\mu\), so \(\rho_X\) is real and \(|O_k|\le2\) pointwise there; right-hand-side boundedness on the slice is structural. The commuting-ray alternative also refines inside the slice: at \(u=0\), writing the growth functional as \(B=\mathbf v\mathbf v^{\mathrm T}-\mathbf u\mathbf u^{\mathrm T}\) with \(\mathbf u=(\cos(3\pi/8)r^0,\cos(\pi/8)\vec r\,)\), \(\mathbf v=(\sin(3\pi/8)r^0,-\sin(\pi/8)\vec r\,)\), the matrix \(B\) is supported on \(\operatorname{span}\{\mathbf e_0,\hat{\mathbf r}\}\), has rank at most two, and \(\lambda_{\max}(B)=[{(r^0)}^2-r^2+\sqrt{{(r^0)}^4+6{(r^0)}^2r^2+r^4}]/(2\sqrt2)\), which is positive iff \(r^0\ne0\); for pure spatial slice momenta (\(r^0=0\)) there is no commuting ray with growth, the neutral set is \(\hat{\mathbf r}\cdot\hat\rho=0\), and \(B\) is negative off it. For \(r^0\ne0\) the one-dimensional branch integral \(\int_{\mathbb R}\mathrm e^{-Qa^2}\,2\cos(\gamma_{\mathrm c}|a|)\,\mathrm da=2\sqrt{\pi/Q}\,\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\), \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\), gives pointwise modulus growth \(\mathrm e^{{(r^0)}^2\cos(3\pi u/4-\pi/4)/(16\epsilon)}\) for the soft temporal mode at \(\gamma=0\), saturating as \(\epsilon\to0^+\) at fixed \(\gamma<0\) to a constant of order \(\mathrm e^{{(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)}\) that diverges as \(\gamma\to0^-\). In the reduced \(N=2\) integral (regulator (A), contours \(\mathcal R_u\), \(\epsilon\to0^+\) last) with this insertion at pure temporal slice momenta, the modulus ratio \(|Z_\epsilon[O_k]|/|Z_\epsilon[1]|\) stays of order one and tends to \(2\) along the ladder down to \(\epsilon=3\cdot10^{-3}\) (fit slope \(0.0000\) of \(\ln\)-ratio against \(1/\epsilon\), against the pointwise corner value \(0.044/\epsilon\) at \(r^0=1\)), and at \(u=0.6\) with \(\gamma=-0.2,-0.05\) it stays between \(0.75\) and \(2.2\): in the reduction neither the commuting-ray growth \(\mathrm e^{c_2(k)/\epsilon}\) nor the pointwise saturation factor materialises, the corner branch growth being phase-space suppressed near the soft corner by Vandermonde and measure powers. These are reduced-model computations with oscillation-limited resolution at \(\gamma=0\); whether the left-hand side is controlled on the slice at \(k\ne0\) with \(r^0\ne0\) remains open at full \(N=2\), the \(\gamma\to0^-\) bridge from fixed-\(\gamma<0\) success remains open, and the pure-spatial half of the slice is now ray-free; Problem~E remains open and PROGRAMME-CONDITIONAL.
```

Style conformance: `\(\)` math as in the 054 paragraph; `\epsilon` (not `\varepsilon`) and
`\mathcal R_u`, `\vec r`, `\hat\rho`, `\operatorname`, `\mathrm e` all match the 054
paragraph's macros; ASCII-only; one paragraph; single scoped closing status sentence; no
process language ("commuting-ray alternative", "the displayed limit identity" style
references match 054's own wording).

## Verification scripts

All in this folder; run with `python -I`; saved outputs:

- `slice_ray_r1.py` (8068 B, sha256 a71795701821fe6ced5ec2567b644acf576a1ab91c69105a4b84c75ced64d6c5)
  → `slice_ray_r1.out` (2295 B, sha256 6d96793d761062f5123fda4b22be837c543bca44fc623af4e1c98516928bc810):
  section (1) Cauchy–Binet difference = 0 and \(u=1\) coefficient check (\(r^0,r^1\));
  section (2) \(B\) block, \(\lambda_{\max}\) formula vs sympy eigenvalues (max diff 0),
  sign-lemma samples incl. \(r^0=0\) (\(\lambda_{\max}=0\)) and \(r^0=10^{-3}\), square-difference
  \(=8b^2{r^0}^2\), numeric rank/nullspace in 10 dims, \(r^0=0\) quadratic-form values
  (\(-4.419417=-\cos(\pi/4)b^2\)); section (3) branch series vs closed form (rel err
  \(0,5\cdot10^{-51},1.6\cdot10^{-48}\)), quadrature agreement (0), normalization cross-check
  \(0.1768/\epsilon\) (054, \(\operatorname{Tr}H^2=1\)) vs \(0.0442/\epsilon\) (Pauli factor 2).
- `n2_slice_r1.py` (15230 B, sha256 8d1523d74be8fe47545af7aa35afd68e29f78dab7348654f6ea9e5ad1ae3d42f)
  → `n2_slice_r1.out` (2851 B, sha256 e17a86cf8e9c9c32c60de0da0c9833d0fe79df4db6c5aee0adba68a97116384d):
  E0 normalization (trivial/bare \(=2.0000000000\); factor/bare at \(r^0=10^{-6}\)
  \(=2.0000000000\)); E1 ratios and fits; E2 \(\gamma\) scan and predicted-vs-measured
  saturation; E3 pure-spatial carrier proxy. Grids: \(96\times44\times44\) (coarser for exact
  mode), \(s\)-cap \(\ln(80/\epsilon)\le14\); runtime ~47 s.
- `apply_check.py` (6015 B, sha256 0f57fabba3c56092e463ec060ad7f06942aeb62453fc09ba4d13b77958e447b8):
  report mode → `apply_check_r1.out` (958 B, sha256 03dd4b6ab39567a97595d881d1b4c7a90faae87f1528ad495f2d1587cb05faac):
  pins True/True, 054-marker 1, 055-marker 0, anchor count 1, insert ASCII, no cite/ref/label,
  expected realized size 540236. `--copy` mode → `apply_copy_r1.out` (1318 B, sha256
  dcd5c40f63803d9b56fefa191d9f758d6e8bdc1be121a95cadf38ae1e5d859c8): applied to NEW copy
  `C:/Users/redgi/tmp/055_apply_r1` (left in place for the gatekeeper/author; the script
  refuses to run again while it exists and refuses paths inside the repository):
  appH-after 540236 B, CRLF 3209, bare-LF 0, sha256 c6ab08f319fefee3267ee98cfbcbd9805032c1e901d55b8bad1587f6515ff1af;
  bib and `namcg-book7.tex` untouched.
- Build of the modified copy (`build_check_r1.out`, 361 B, sha256 0688c14a5d92340822326014526146b69fbf6c30d042fc44f151ecc51a0cb588):
  two `pdflatex -interaction=nonstopmode -halt-on-error namcg-book7.tex` passes in the copy
  (figs/, frontmatter/*.tex and namcg-book7.bbl also copied): exit 0/0, 359 pages, no `!`
  errors, no multiply-defined, pass-2 undefined-reference count 0. (The copy dir contains the
  aux/pdf build artifacts; the repo was never built.)

## Decisions Taken

1. Factorized branch surrogate ("factor" mode) as the main finite-\(\epsilon\) insertion, with
   exact Taylor-mode cross-check at \(\epsilon\ge0.1\): the direct Taylor insertion overflows
   float64 partial sums at small \(\epsilon\) (maxterm \(>10^3\) already at \(\epsilon=0.1\)
   for \(r^0=2\)), so it cannot probe the \(\epsilon\to0\) ladder; the surrogate is validated
   against the exact mode at \(\epsilon\ge0.1\) and structurally at \(r^0\to0\) (ratio
   \(\to\operatorname{Tr} I=2\) to \(10^{-10}\)). Favors the derivation: it is the only mode
   that reaches \(\epsilon=3\cdot10^{-3}\). Rejected: reporting only \(\epsilon\ge0.1\) exact
   results; analytic continuation of the Taylor series (no justification).
2. Report same-grid modulus RATIOS of \(Z_\epsilon\) only, never absolute \(|Z_\epsilon|\), at
   \(u=0,\gamma=0\): the absolute values at small \(\epsilon\) are dominated by
   oscillation-resolution artifacts; ratios on identical grids cancel the grid-dependent
   polynomial prefactors. The insert states "oscillation-limited resolution". Rejected:
   claiming converged absolute \(|Z_\epsilon|\) (unsound).
3. Hörmander-type domination-theorem literature lead abandoned: could not verify a specific
   applicable statement; no citation is used anywhere. Rejected: citing unverified literature.
4. Kept the insert's exponents in the exact \(N=2\) \(O_k=2\cos(\rho_X/2)\) normalization
   (denominator 16), matching the manuscript's \(\rho_X\) convention, with the code/ray
   normalization difference (Pauli factor 2) documented here and in `slice_ray_r1.out`.
5. Included E3 (pure-spatial carrier proxy) as supporting numerics for the ray-free
   pure-spatial half; kept it out of the manuscript paragraph (it is a proxy, not \(O_k\)).

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step is derived; the slice window stays
open; the package is model-level evidence plus structural narrowing inside the 054 class.

## Status-label recommendation

Derived current critical-path set from the agenda/ledger (ch17 criterion A, B, C, D1, E, F,
G-derived, N; H, I, J optional): unchanged by this package. Problem E stays
OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. No label changes proposed.

## Author decision needed

None.

## Remaining open step

Ranked avenues (orchestrator may queue follow-ups):

1. Analytic LHS control on the slice at \(r^0\ne0\) for the FULL \(N=2\) integral: prove a
   transverse domination lemma implementing the observed phase-space suppression (vanishing
   powers of the Vandermonde/Pfaffian \((\det\mathcal G)^4\) and Jacobian near each rank-one
   ray, uniformly in \(\epsilon\)); the numerics identify the corner and the power range
   (\(\Lambda^5\)–\(\Lambda^8\)) as the target shape of the lemma.
2. Uniform-in-\((\epsilon,\gamma)\) domination for the slice window (full rank-2): given the
   pointwise divergence of C, formulate and attempt an integrated domination inequality on
   the reduced chart first, then lift; the E2 numerics (no obstruction down to
   \(|\gamma|=0.05,\epsilon=3\cdot10^{-3}\)) say the attempt is live, not settled.
3. Extension beyond the commuting-sector reduction: Gaussian bound for non-commuting modes
   around the commuting manifold plus the \(k<14\) Pfaffian window, to carry the reduced-model
   control to the full \(N=2\) slice integral.
4. Non-factorized exact insertion at small \(\epsilon\) by resummation (currently only
   \(\epsilon\ge0.1\)); would upgrade the surrogate numerics.
5. Explicitly NOT attempted (rank 3): regulator-class and \(N\ge3\) extensions of the slice
   statement.

## Special instructions for the gatekeeper

- Re-run both scripts with `python -I` and diff against the saved `.out` files (deterministic;
  `n2_slice_r1.py` is seeded/fixed grids, ~50 s).
- Re-derive by hand: the Cauchy–Binet identity; the \(B\) block \((1/\sqrt2)[[(r^0)^2,-r^0r],
  [-r^0r,-r^2]]\) and the \(\lambda_{\max}\) sign lemma (the \(8(r^0)^2r^2\) square-difference
  is the whole proof); the branch closed form (erf cancellation) and both exponent formulas;
  the consistency of the \(16\epsilon\) and \(8c\epsilon\) normalizations.
- The anchor literal in `apply_check.py` uses single-backslash raw byte strings: the anchor
  count must be exactly 1 in the current tree (it is; a duplicate `\paragraph{Status.}
  Remains Assumption` context exists in other sections but not with the three-CRLF prefix —
  the script counts it and prints 1). `--copy` mode refuses to re-run over the existing
  `C:/Users/redgi/tmp/055_apply_r1`; use a fresh DIR if needed.
- Must NOT be asserted: that the slice window is closed; that the full-\(N=2\) LHS is
  controlled; that the \(\gamma\to0^-\) bridge is derived; that the reduced-chart results are
  results for the full integral; that the pure-spatial ray-freeness settles the LHS for
  \(r^0=0\) beyond the commuting-ray class (E3 is a proxy).
- Check EOL hygiene of the realized copy (bare-LF must be 0, CRLF 3209) and that the insert
  introduces no `\cite`, `\ref` or `\label`.
- Numerical claims in the insert trace to `n2_slice_r1.out` lines 2–21 and
  `slice_ray_r1.out` lines 21–31; the "0.75 and 2.2" interval covers E2 gam=-0.2 min 0.747
  and gam=0 max 2.1574; "tends to 2 ... down to 3e-3" covers 1.9998/1.9999 (r0=1) and
  1.9993/1.9998 (r0=2).
