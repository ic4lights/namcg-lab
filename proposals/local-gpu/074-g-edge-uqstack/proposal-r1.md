# Proposal 074-g-edge-uqstack, round 1

Recovery round: the computations (scripts `s1_uq_closedform.py`, `s2_uq_scaling.py`,
`s3_uq_boxmin.py` and their `.out` files, and the reproduction pack `r1..r5`) are those left on
disk by the prior researcher for this target, who died to an API error before writing the package.
Nothing was redesigned. This round independently re-ran every script (fresh `python -I` runs from
the repository root, byte-compared against every shipped `.out`: all identical), verified the
x=0 hook-term fix named in the prior agent's last message (attribution and evidence below),
wrote the manuscript insert, the read-only simulator, and this proposal.

## Result

Within the 072 dominant-representation hypothesis class (H1)-(H4), inherited verbatim, and on the
same product fuzzy-sphere testbed defect, the two-row fixed-frame excess is extended to
**stacked-row diagrams**: with \(M=M_1+M_2\), depths \(1\le q_f\le M_f\) and rows
\(\ell_1\ge\ell_2\ge0\), let
\(\Delta_{q_1,q_2}:=\log\dim_{U(M)}(\ell_1^{q_1},\ell_2^{q_2})-\log\dim_{U(M_1)}(\ell_1^{q_1})-\log\dim_{U(M_2)}(\ell_2^{q_2})\)
(\((q_1,q_2)=(1,1)\) with \(\ell_2\ge1\) is the integrated two-row defect \(\Delta\)). Established /
derived-with-numerically-checked-constants / numerical, in the sense detailed in the classification
section:

1. **Closed form (established derivation + exact-rational verification).** \(\exp\Delta_{q_1,q_2}\)
   equals
   \(\prod_{r=1}^{q_1}\prod_{c=1}^{\ell_1}\frac{M+c-r}{M_1+c-r}\cdot
   \prod_{r=1}^{q_2}\prod_{c=1}^{\ell_2}\frac{M-q_1+c-r}{M_2+c-r}\cdot
   \prod_{r=1}^{q_1}\prod_{c=1}^{\ell_2}\frac{\ell_1-c+q_1-r+1}{\ell_1-c+q_1+q_2-r+1}\):
   content factors per box of the two stacks (second stack with shifted content \(M-q_1\)), times a
   hook correction of \(q_1\ell_2\) ratios (the column height of the union exceeds that of
   \((\ell_1^{q_1})\) by \(q_2\) over the first \(\ell_2\) columns; the second stack's hooks cancel
   exactly - derivation below). Verified in exact rational arithmetic on 17,856 cases, 0 failures;
   cross-checked on the \((q_1,q_2)=(1,1)\) subgrid against the integrated 072 two-row closed form
   on 2,268 cases, 0 failures (`s1`). Positivity: \(\Delta_{q,0}>0\) for \(\ell_1\ge1\) is
   established analytically (every factor \(>1\)); on the generic-rank grid (\(M_1,M_2\ge2\),
   \(q_1+q_2<M_1+M_2\)) the sampled minimum is \(0.200670695=\log(11/9)\) at
   \((M_1,M_2,\ell_1,\ell_2,q_1,q_2)=(9,2,1,0,1,0)\); degenerate zeros exist at rank-one corners
   (e.g. \((1,1,1,1,1,1)\) gives \(\Delta=0\)).
2. **Linear-in-depth continuum limit and additivity (derived limit; numerical tables).** At fixed
   \(M_f/N\to m_f\), \(\ell_f/N\to u_f\) and fixed depths, \(\Delta_{q_1,q_2}/N\to
   q_1\bigl[G(m_1+m_2,u_1)-G(m_1,u_1)\bigr]+q_2\bigl[G(m_1+m_2,u_2)-G(m_2,u_2)\bigr]\) with the
   073 paragraph's \(G(m,u)=(m+u)\log(m+u)-m\log m-u\) (Riemann-sum derivation below; depth shifts
   and hook factors contribute \(O(q\log\ell_1)\) to \(\Delta\), subleading at fixed depth).
   Numerically (`s2`): \(\Lambda(1/2,1/2)=0.523248144\) (asserted against the 072/073 value);
   symmetric saddle \(\Delta_q/N = 0.520906 / 1.037902 / 1.551490\) at \(N=3200\),
   \(q=1,2,3\), each below \(q\Lambda\) with residual \(N(q\Lambda-\Delta_q/N)=7.50/27.50/58.41\)
   (i.e. \(O(q\log N)\)-consistent); the \(q=1\) value reproduces the shipped 072/073 reference
   0.520906 exactly; unequal depths agree with \((q_1+q_2)g\) to the residual size:
   \((q_1,q_2)=(2,1)\): 0.780448 vs 0.784872 (diff \(-0.00442\)); \((1,3)\) and \((3,1)\):
   1.040208 vs 1.046496 (diff \(-0.00629\)), \(N=3200\). Single-stack removal at
   \(m_1=1/2,m_2=1/3\), \(N=1600\): \(\Delta_{q,0}/(qN)=0.188909/0.188979/0.189049\), i.e. \(q\)
   times the integrated one-row value 0.188909 (the 073 paragraph's printed 0.189) to within
   \(2\times10^{-4}\) uniformly in \(q\le3\).
3. **Uniform residual bound (coded constant, numerically verified).** \(\lvert\Delta_{q_1,q_2}-
   N(q_1g_1+q_2g_2)\rvert\le B\) with
   \(B=q_1(2K_1+\log(\ell_1+1)+2)+q_2(2K_2+2)+q_1q_2(\log(\ell_2+2)\text{ form: }\log(\ell_1+2)+2)+q_1(q_1+q_2)\),
   \(K_1=\log\frac{M}{M_1-q_1}\), \(K_2=\log\frac{M-q_1}{\max(M_2-q_2,1)}\), holds on all 400
   sampled stacks (seed 20261115; depths \(\le3\), \(M_f\in[100,2000]\)); worst signed margin
   \(-8.863544\) at \((M_1,M_2,\ell_1,\ell_2,q_1,q_2)=(604,259,177,170,1,0)\) (`s3` section 1).
   Hence \(O(1)\)-per-`N`-normalised uniformity: the error in \(\Delta_{q_1,q_2}\) is
   \(O(q\log\ell_1)\) at fixed fractions.
4. **Box minima and unchanged breakdown (numerical, exhaustive at N=400).** At the symmetric
   saddle (\(N=400\), \(\ell_1=\ell_2=200\)) the exhaustive minimum of \(\Delta_{q,q}\) over valid
   diagrams with \(|\ell_i'-\ell_i|\le C\) is attained at the far diagonal corner \((200-C,200-C)\)
   for \(q\in\{1,2,3\}\), \(C\in\{1,5,10,20,40,80\}\) (min/N at \(C=80\): 0.333902/0.649680/0.951233;
   asserted \(>0.3\,qN\)); along \(C=cN\) the minimum stays positive through \(c=0.4975\)
   (min/N \(\ge0.001727\), attained first at \((1,1)\)) and is 0 at \(C=200=c/2\cdot N\), attained
   at the trivial diagram \((0,0)\) (`s3` sections 2-3; assertion `best == 0.0 and arg == (0,0)`).
   This is the same combinatorial breakdown boundary as for two rows (073: \((0,0)\in B_C\iff
   C\ge\ell_1\)); note "attained at" - the enumeration reports the first-encountered minimizer and
   does not exclude ties.
5. **x=0 hook-term fix (verification outcome).** The prior researcher's last message - "the prefix
   missed the x=0 hook term present when l1=l2. Fixing the accumulation to start at x=0" - refers
   to `s3_uq_boxmin.py` only: `make_delta` builds the hook prefix `F` with the accumulation
   starting at `j = 0` (line 43, comment "includes x = 0"), so `F[l1] - F[l1-l2]` includes the
   \(x=l_1-\ell_2=0\) term exactly when \(\ell_1=\ell_2\); the direct double-sum `delta_ref`
   (the formula of result 1) always included it, and `s3` asserts prefix-vs-direct agreement to
   \(10^{-10}\) at five points including \((2\ell,0)\) and diagonal points. `s1`/`s2` use direct
   double sums only and were never prefix-based, so they are unaffected. **Shipped-output
   provenance verified:** fresh byte-for-byte re-runs of the three current scripts reproduce
   `s1.out`, `s2.out`, `s3.out` exactly (table in the verification section), so every shipped
   output post-dates the fix.

Net effect on the ledger evidence: the selection-independence excess (072) and its
row-perturbation robustness (073) are shown to persist for stacked-row diagrams of fixed depth,
scaling linearly in the depth and additively across the two factors, uniformly \(\Theta(N)\) away
from the \(C=\ell_1\) combinatorial boundary. This is a conditional, class-restricted extension.
It closes nothing. Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL, untouched.

## Target and status

- Target: frontier edge `G.edge-uqstack` (`reports/graph/frontier.yaml` L143-149), the 072
  gatekeeper's ranked follow-up avenue (2), quoted there verbatim: "U(q)-stack q-repeated-rows
  diagram class" [src: proposals/072-g-edge-resum-dominant-rep/review-r1.md 'Scope of what is
  established'; ledger:1054]. The frontier records the missing input as "the defect computation on
  the U(q)-stack class and its selection-rule consistency": this package supplies the defect
  computation for the two-stack equal-length subclass at fixed depths; the selection-rule
  consistency is NOT addressed (Remaining open step).
- Problem G ledger, appH L3025-3029, re-read live this round (offset/limit), verbatim: "Status:
  OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results:
  G-model and G-external support at most a scope-limited model; G remains OPEN and neither
  satisfies the matrix-derived criterion." Unchanged by this package; no label, priority or
  completion classification is touched anywhere.
- Chapter 17 criterion passage, ch17 L474-495, re-read live (first and last lines verbatim):
  "\paragraph{Problem G: infrared boundary entropy.} \emph{CRITICAL PATH; mechanism CLOSED
  CONDITIONALLY, derivation OPEN.} Evaluate \(S_{\mathrm{ent}}^{\mathrm{(IR)}}\) on an explicit
  cosmological or large-tube boundary and produce a candidate \(\Lambda_{\mathrm{eff}}\)
  from~\eqref{eq:Leff}. [...] The required entropy density is the one in
  Assumption~\ref{ass:Sent-density}, derived by the replica construction from the matrix theory,
  and boundary stationarity Assumption~\ref{ass:bdy-EE} must likewise be derived rather than
  retained." Nothing in this package moves that criterion.
- Character of the result: DERIVED is NOT claimed. Everything is conditional within the 072
  hypothesis class (H1)-(H4) and concerns the testbed defect \(\Delta_{q_1,q_2}\); the
  identification of the defect with the fixed-frame excess of the leading-order entropy is
  inherited from 065/072/073 unchanged. Unlike the two-row defect, the stacked-row class is NOT
  claimed to be what the selection rule outputs - it is a robustness class (see Decisions and
  Remaining open step).

## Source reading

digest + targeted reads. `scratch/digest.md` in full (compact; head eb8fc7d; appH digest hash
437df96e4be9 - matches the live PRE pin measured this round; dirty-chapters: yes = the
integrated, author-uncommitted 072+073 text, as stated by the orchestrator). Targeted appH reads
with offset/limit only (file never read whole): L3022-3042 (Problem G section: ledger label +
Status paragraph), L3153-3165 (the 065 block tail: 072 paragraph incl. its scoped closer L3159,
the integrated 073 paragraph L3161, the Vacuum-term paragraph L3163, and the block closer L3165).
Targeted ch17 reads: L474-495 (Problem G criterion + G completion levels) after grep; grep lines
666 and 726 (criterion list items "Problem~G: derive \(S_{\mathrm{ent}}^{\mathrm{(IR)}}\)..." and
"Problem~G-derived: ...") noted, full item text not needed for this package. Full reads:
`proposals/073-g-edge-rowshift/proposal-r1.md` sections Result / Target and status / Source
reading / Claim classification / Proposed changes (incl. byte contract) / Verification scripts /
Decisions Taken (targeted, not the middle derivations); `proposals/073-g-edge-rowshift/manifest.md`
in full; `proposals/073-g-edge-rowshift/simulate_apply.py` in full (template); the three 074
`s*.py` scripts in full; `r1..r5*.py` not re-read: they are byte-identical copies of 073's
`s1..s5*.py` (sha256 compared, table below), so 073's full round-1 read covers them. Skims:
`s1.out`, `s2.out`, `s3.out` in full; `r*.out` / `r*.repro.out` (byte-identical to 073's shipped
outputs and to fresh re-runs). Unreadable files: none.

## Context: quoted source passages (the passage this insert extends)

072 closer (appH L3159, kept): "These statements are for the product background with the block of
the union at fixed frame, two-row diagrams and the saddle class \(\ell_i=t\,s_i\); they are not a
minimisation over frames, they do not give monotonicity of the excess in \(\ell_2\) (minimum
increment \(\Delta(\ell_1,\ell_2+1)-\Delta(\ell_1,\ell_2)=-0.666\) at
\((M_1,M_2,\ell_1,\ell_2)=(2,24,13,12)\), numerical), they leave items (i)-(iii) of the preceding
paragraph unchanged, and they close nothing in Problem~G."

073 paragraph header (appH L3161, kept): "\emph{Robustness of the fixed-frame excess to bounded
row perturbations.} Under the same hypotheses, the two-row defect \(\Delta\) of the preceding
paragraph admits a uniform description under perturbations of the row lengths of the saddle
diagram: ..." (full sentence read live; defines \(\Lambda(u_1,u_2)\) and \(G(m,u)\), the box
statements, and the 0.189 one-row value).

Insertion seam - boundary after (appH L3163, kept, occurs exactly once; short form
`\emph{Vacuum term.}` occurs twice and is never used as anchor): "\emph{Vacuum term.} The
abstract of~\cite{Steinacker2023}".

## Research and reasoning

### Class definition (precise)

Fix \(M_1,M_2\ge1\), depths \(1\le q_f\le M_f\) (\(q_f=0\) in the code denotes a trivial/omitted
stack), rows \(\ell_1\ge\ell_2\ge0\), \(M=M_1+M_2\). Union diagram \(\lambda=(\ell_1^{q_1},
\ell_2^{q_2})\vdash q_1\ell_1+q_2\ell_2\); factor diagrams \(\lambda_f=(\ell_f^{q_f})\).
\(\Delta_{q_1,q_2}:=\log\dim_{U(M)}(\lambda)-\log\dim_{U(M_1)}(\lambda_1)-\log\dim_{U(M_2)}
(\lambda_2)\), \(\dim\) the hook-content dimension. The `s1` exact-identity grid: \(M_1,M_2\in
\{1,\dots,9\}\), \((q_1,q_2)\in\{0,\dots,3\}^2\) with \(q_f\le M_f\) and \(q_1+q_2\ge1\),
\(\ell_1\in\{0,\dots,6\}\), \(0\le\ell_2\le\ell_1\), excluding the inconsistent degeneracies
(\(q_1=0\) with \(\ell_1>0\) or \(\ell_2>0\); \(q_2=0\) with \(\ell_2>0\)) - 17,856 asserted
cases. Nontrivial checked cases have \(q_1\ge1\); the \(q_1=0\) family is vacuous in this
parameterization.

### Closed form: derivation

Write \(\dim_{U(M)}(\mu)=\prod_{(r,c)\in\mu}(M+c-r)/h_\mu(r,c)\), \(h_\mu(r,c)=\mu_r-c+\#\{r':\mu_{r'}\ge c\}-r+1\).
Compare factor-by-factor between \(\lambda\) and the pair \((\lambda_1,\lambda_2)\):

- Content factors. Rows \(r\le q_1\) of \(\lambda\) are the rows of \(\lambda_1\) (same row index
  \(r\)): ratio \((M+c-r)/(M_1+c-r)\). Rows \(q_1+r'\) (\(r'=1..q_2\)) of \(\lambda\) correspond
  to row \(r'\) of \(\lambda_2\), and the union row index is shifted by \(q_1\): ratio
  \((M-q_1+c-r')/(M_2+c-r')\). This gives the \(q_1\ell_1+q_2\ell_2\) content factors.
- Hook factors. For a box of \(\lambda_1\) at \((r,c)\), \(r\le q_1\): the union column height is
  \(q_1+q_2\) iff \(c\le\ell_2\) and \(q_1\) otherwise, while the separate height is \(q_1\). The
  hook differs only for \(c\le\ell_2\): \(h_\lambda=(\ell_1-c)+(q_1+q_2)-r+1\) vs
  \(h_{\lambda_1}=(\ell_1-c)+q_1-r+1\); since hooks sit in the denominator, each contributes the
  ratio \(h_{\lambda_1}/h_\lambda=(\ell_1-c+q_1-r+1)/(\ell_1-c+q_1+q_2-r+1)<1\): the \(q_1\ell_2\)
  hook factors.
- For a box of \(\lambda_2\) at row \(r'\): in the union the row index is \(q_1+r'\) and the
  column height is \(q_1+q_2\) (rows \(1..q_1\) all have length \(\ell_1\ge\ell_2\ge c\)); so
  \(h_\lambda=(\ell_2-c)+(q_1+q_2)-(q_1+r')+1=(\ell_2-c)+q_2-r'+1=h_{\lambda_2}\): the second
  stack's hooks cancel **identically**. This is the structural reason the correction is confined
  to the first stack.

The product of the three factor families equals \(\exp\Delta_{q_1,q_2}\) exactly. `s1` checks
this identity in exact `Fraction` arithmetic on the grid above (17,856 cases, 0 failures) and
against the 072 two-row closed form (2,268 cases, 0 failures). All factors are strictly positive
on the grid (denominators positive because \(M_f\ge q_f\)).

### Continuum limit: derivation

Take \(M_f=m_fN\) (up to \(o(N)\)), \(\ell_f=\lfloor u_fN\rfloor\), \(q_f\) fixed. Each content
sum is a Riemann sum: \(\sum_{c=1}^{\ell_f}\log\frac{M_f'+c-r}{M_f+c-r} =
N\int_0^{u_f}\log\frac{m_1+m_2+u}{m_f+u}\,du+O(\log\ell_f)\) per row \(r\) (summand monotone in
\(u\); the \(r\)-shifts and endpoint corrections are \(O(1)\) per row since the summand is
bounded on compact fractions, \(O(\log \ell_f)\) worst case near \(u=0\) as in 073's treatment),
and \(\int_0^{u}\log\frac{m_1+m_2+v}{m_f+v}\,dv=G(m_1+m_2,u)-G(m_f,u)\) because
\(\partial_u G(m,u)=\log(m+u)\). The hook factors: \(\log\frac{\ell_1-c+q_1-r+1}{\ell_1-c+q_1+q_2-r+1}
=-\log(1+\frac{q_2}{\ell_1-c+q_1-r+1})=O(1/\ell_1)\) per factor, \(q_1\ell_2\) factors, total
\(O(q_1q_2\,\ell_2/\ell_1)=O(q_1q_2)\) - \(o(N)\) at fixed depth. Summing rows: \(\Delta_{q_1,q_2}/N
\to q_1g_1+q_2g_2\) with \(g_f=G(m_1+m_2,u_f)-G(m_f,u_f)\). The uniform residual bound stated in
result 3 is the coded bookkeeping form of this comparison (Riemann comparison plus explicit
shift/hook accounting, constants collected as \(B\)); its coded form on the \(q\)-grid is
verified numerically (400 samples, worst margin \(-8.863544\)), in the same status class as 073's
"coded constant checked numerically".

Consistency anchors (`s2`): \(q=1\) reproduces the shipped 072/073 value 0.520906 at \(N=3200\);
\(\Lambda(1/2,1/2)=0.523248144\) (same assert as 072/073); \(\Delta_{1,0}/N=0.188909\) reproduces
the 073 printed 0.188909 (m=(1/2,1/3), N=1600). The unequal-depth tables show the finite-\(N\)
residuals have the predicted \(O(q\log N)\) size.

### Positivity

\(\Delta_{q,0}>0\) for \(\ell_1\ge1\): every factor of the two content families is \(>1\) strictly
(the hook family is empty when \(\ell_2=0\)); denominator positivity from \(M_1\ge q_1\). For
\(\ell_2\ge1\) the hook ratios are \(<1\) and no closed-form positivity proof was closed; the
sampled generic-rank grid minimum is \(0.200670695\) (analytically \(\log(11/9)\), the
single-content-factor case \((9,2,1,0,1,0)\)), degenerate rank-one zeros exist. Classified
numerical (grid), general case open.

### Box minima and breakdown

Protocol (`s3`, \(N=400\), \(\ell_1=\ell_2=200\)): exhaustive enumeration of valid
\((\ell_1',\ell_2')\) with \(\max|\ell_i'-\ell_i|\le C\), \(\ell_2'\le\ell_1'\), over
\(C\in\{1,5,10,20,40,80\}\) and \(q\in\{1,2,3\}\); assertions: argmin \(=(200-C,200-C)\) (first
point of the ascending scan - so: the minimum is attained at the far corner and no enumerated
point is smaller; ties are not excluded), value \(>0.3\,qN\). Along \(C=cN\): values printed at
\(C\in\{40,80,120,160,199\}\), asserted \(>0\); at \(C=200\) the value is exactly \(0.0\) with
first argmin \((0,0)\) (assert). Positivity for all intermediate \(c\le0.4975\) follows from these
prints by monotonicity of the box in \(C\) (larger box, smaller-or-equal min). The \(C=200\)
entry of \((0,0)\) is the same combinatorics as 073's \((0,0)\in B_C\iff C\ge\ell_1\);
\(\Delta_{q,q}(0,0)=0\) vacuously (empty diagram, empty products).

### Cross-protocol verification of the prefix fix

`s3` asserts `abs(delta(a,b) - delta_ref(...)) < 1e-10` at \((200,200),(197,193),(160,160),(400,200),(400,0)\)
for each \(q\), i.e. prefix (with x=0 term) vs the direct sum of the closed form, on and off the
diagonal. Combined with the byte-exact re-runs, the x=0 fix is verified in place and reflected in
all shipped outputs.

### s3 section-2 printed "corner/N" column: known cosmetic artifact (reported, not edited)

`sec2.append((C, best, best/N, corner/N, arg))` then prints `row[3]/N` - a double division: the
column headed `corner/N` in `s3.out` is actually \(\mathrm{corner}/N^2\) (e.g. the printed
0.001303 at \(q=1,C=1\) is \(0.521219/400\); the correct \(\mathrm{corner}/N=0.521219\) computed
here from the same formula line, and \(\approx0.996\,\Lambda(1/2,1/2)\), consistent with the
far-corner being near the saddle). **No assertion uses `corner`** (the asserts are
`arg==(l-C,l-C)`, `best>0.3*q*N`, `best>0`, and the exact-zero check); this proposal and the
insert cite no corner-column value. Scripts left byte-frozen so the reproduction stays exact;
gatekeeper can confirm the artifact by reading `s3_uq_boxmin.py` lines 139-145.

### Comparison with the original target

The 072 review avenue asked for the "U(q)-stack q-repeated-rows diagram class" defect computation.
Supplied: the exact closed form and its continuum asymptotics for the two-stack equal-length
subclass \((\ell_1^{q_1},\ell_2^{q_2})\) at fixed depths, with linear-in-depth scaling, additivity
across stacks, uniform residual bound, box robustness and unchanged breakdown. Not supplied: any
statement that the *selected* diagram is of this form (selection-rule consistency for stacks -
frontier's second missing input), and general (non-equal-row) multi-row partitions. The
two-row-only restriction (072 H4) is thereby widened **for the defect computation only**: every
robustness statement of 072/073 survives stacking to depth \(\le3\), with the excess multiplied
by the depth. Mismatch (1) (factor-edge vs dM) and Problem G missing steps (i)-(iv) are untouched
by the package, exactly as for 072/073.

### Literature

No new citations; no `bib/` change proposed. The U(q)-stack diagram class is named in
arXiv:2311.10131 (Frenkel) per the 072 gatekeeper review (`frontier.yaml` L144 and L194 record the
review's verification of that reference); **not independently re-verified this round** - the
package imports no result from it (the insert carries no citation; the class is defined intrinsically
by its hook-content defect).

## Claim classification

1. **Established identity/derivation:** the stacked-row closed form (hook-content comparison
   above, including the exact cancellation of the second stack's hooks; plus 17,856 exact-rational
   checks); \(\Delta_{q,0}>0\) for \(\ell_1\ge1\); pointwise and fraction-uniform
   \(\Delta_{q_1,q_2}/N\to q_1g_1+q_2g_2\) (Riemann-sum derivation); positivity/monotonicity of
   \(G\)-combinations \(\Lambda\)-type profile (inherited from 073, same \(G\)); box-min
   \(\Theta(N)\) for fixed and \(o(N)\) boxes *given* the uniform residual bound (as 073);
   breakdown combinatorics \((0,0)\in B_C\iff C\ge\ell_1\) (inherited from 073) and
   \(\Delta(0,0)=0\) vacuity; positivity of box minima for intermediate \(c\) from the printed
   points by box monotonicity.
2. **Conditional under (H1)-(H4) (072 class), and only as a statement about the testbed defect:**
   the whole package; the stacked-row class is a robustness class, not a selection-rule output.
3. **Numerically verified (reproduced this round; finite; supports but does not prove the general
   case):** the closed-form grid (17,856) and 072-reduction cross-check (2,268); the coded
   uniform residual bound on 400 sampled stacks (worst margin \(-8.863544\)); the scaling tables
   (\(N\le3200\), depths \(\le3\)); unequal-depth additivity to the residual size; the
   \(\Delta_{q,0}/(qN)\) agreement with 0.189 to \(2\times10^{-4}\); generic-rank grid positivity
   min 0.200670695.
4. **Finite-grid / enumeration-only (general case unproved):** strict positivity for
   \(\ell_2\ge1\) and general \(q\); far-corner attainment of the box minimum at \(N=400\)
   (\(q\le3\), \(C\le80\)) and its value - uniqueness of the minimizer not tested (scan returns
   first); the exact-zero minimum at \(C=200\) exhaustive at \(N=400\) only; the printed
   breakdown sequence for the enumerated \(c\)-values.
5. **Conjecture / inherited input (unchanged from 072/073):** the block-cut transplant of the
   selection rule; that the saddle diagram is the selected diagram; any statement about the
   minimised block entropy. This package adds no new conjectures, but note the *new* subclass
   itself is unmotivated as a selection output: no claim is made that selected diagrams have
   stacked rows.
6. **Mechanism/argument (unchanged character):** the physical reading of the box minimum as the
   excess the fixed saddle data force; depth-linearity as the statement that each additional
   repeated row layer contributes the same per-layer excess to leading order.

## Proposed changes

File `chapters/appH-microscopic-proofs.tex` only. No `bib/` change (no citation is load-bearing).
No ch17 change. No label/status/priority touch. No equation moved or renumbered.

**Anchor** (the 073 integration point; the new paragraph sits between the 073 paragraph L3161 and
the Vacuum-term paragraph L3163):

- Boundary before (kept verbatim): the 073 paragraph L3161 ends "...and they concern perturbations
  of the selected diagram at fixed saddle data, not the selection of the diagram itself."
- Boundary after (kept verbatim, occurs exactly once, live-asserted count = 1; the short form
  `\emph{Vacuum term.}` occurs twice and is never used as anchor):
  `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}` (L3163).
- Anchor used by `simulate_apply.py`: `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}`
  with the leading CRLF (line-start form). Live counts in this round's run: short 2, long 1,
  line-start 1; the new paragraph's header occurs 0 times pre-insert.

**What is inserted** (one new paragraph, CRLF file `insert-r1.tex`, 2,984 B incl. its terminal
CRLF, sha256 9eae941be5ba496bde7273dd539e0bddae51e8ee080afdef624c41bad38014e3; the fenced line
below is byte-equal to the file's single line; longer than 073's 2,179 B because the closed form
and three separate numerical claims each carry their own qualifier):

```latex
\emph{Extension of the fixed-frame excess to stacked-row diagrams.} Under the same hypotheses, the comparison of the two preceding paragraphs extends to diagrams whose rows form two stacks of equal length: for \(\ell_1\ge\ell_2\ge0\) and depths \(1\le q_f\le M_f\), let \(\Delta_{q_1,q_2}\) be the difference of \(\log\dim\)'s between \(U(M_1+M_2)\) at the diagram with \(q_1\) rows \(\ell_1\) and \(q_2\) rows \(\ell_2\), and the stacked diagrams \((\ell_1^{q_1})\) of \(U(M_1)\) and \((\ell_2^{q_2})\) of \(U(M_2)\). The multiplicative defect \(\exp\Delta_{q_1,q_2}\) is a product of \(q_1\ell_1+q_2\ell_2\) content factors, \((M+c-r)/(M_1+c-r)\) on the first stack and \((M-q_1+c-r)/(M_2+c-r)\) on the second, times \(q_1\ell_2\) hook ratios \((\ell_1-c+q_1-r+1)/(\ell_1-c+q_1+q_2-r+1)\) (the hooks of the first stack exceed those of \((\ell_1^{q_1})\) by \(q_2\) over its first \(\ell_2\) columns, those of the second stack are unchanged), with \(M=M_1+M_2\): an exact identity, checked in rational arithmetic on 17,856 cases and reducing to the two-row closed form above in 2,268 cases at \(q_1=q_2=1\); the defect is strictly positive on the sampled grid with \(M_1,M_2\ge2\), \(q_1+q_2<M_1+M_2\), minimum \(0.201\) (numerical). At fixed \(M_f=m_fN\), fixed fractions \(u_f=\ell_f/N\) and fixed depths, \(\Delta_{q_1,q_2}/N\) converges to \(q_1\bigl[G(m_1+m_2,u_1)-G(m_1,u_1)\bigr]+q_2\bigl[G(m_1+m_2,u_2)-G(m_2,u_2)\bigr]\) with the preceding paragraph's \(G\), the error in \(\Delta_{q_1,q_2}\) of order \(q\log(\ell_1+1)\) uniformly in \(N\) at fixed fractions (numerical, 400 sampled stacks at depths \(\le3\), worst residual slack \(8.9\)); the limit is linear in depth and additive across stacks, equal to \(q\Lambda(1/2,1/2)=0.523\,q\) at the symmetric saddle (\(\Delta_{q,q}/N=0.5209,1.0379,1.5515\) at \(N=3200\), \(q=1,2,3\), numerical), while at \(m_1=1/2\), \(m_2=1/3\) the single-stack value \(\Delta_{q,0}/(qN)\) agrees with the one-row value \(0.189\) above to within \(2\times10^{-4}\) for \(q\le3\) at \(N=1600\) (numerical). The box-minimum and breakdown statements of the preceding paragraph carry over: at the symmetric saddle, \(N=400\), the exhaustive minimum of \(\Delta_{q,q}\) over valid diagrams with \(|\ell_i'-\ell_i|\le C\) is attained at the far diagonal corner for \(q\le3\) (\(\min/N=0.334,0.650,0.951\) at \(C=80\), \(q=1,2,3\)) and, along \(C=cN\), stays positive up to \(c=0.4975\) (\(\min/N\ge0.0017\)) and vanishes at \(c=1/2\), attained at the trivial diagram - the same boundary as for two rows (numerical, exhaustive over the box). These statements are for the stacked-row hook-content defect of the product testbed within the same dominant-representation class as the two preceding paragraphs, with the rows restricted to two stacks of equal length and depths held fixed as \(N\to\infty\); they concern the defect of the stacked diagrams at fixed saddle data, not the selection of stacked diagrams, and they close nothing in Problem~G.
```

**What is kept:** everything else in the file, including the 072 paragraph L3153-3159, the 073
paragraph L3161, and both closers (L3159 and the block closer L3165), unchanged. The insert
contains no `\ref`, `\eqref`, `\label`, `$`, `\cite`, display math, and no Status/Priority/
Completion wording.

**Byte contract** (from `simulate_apply.out` run this round; live re-verification by the
integrator is mandatory - other chains may have moved the text): appH PRE 697,839 B / sha256
437df96e4be9a5428840c42308fa770c5bc9c3e8aa39c0a03bab672d9e0f111c / CRLF 3,812 / bareLF 0
(asserted in the script; equals the current digest's appH hash 437df96e4be9); POST 700,825 B /
sha256 50f12c8131819f513ff37d5149529ba616063578b04510891a6b7f1d43b8f25e / CRLF 3,814 / bareLF 0;
delta +2,986 B = insert body 2,982 B + 4 (paragraph line terminator + blank separator line; the
insert file is 2,984 B including its own terminal CRLF); CRLF delta +2; bareLF delta 0. bib
unchanged: PRE = POST = 37,463 B / sha256
4d6d7b2a668fdaa64663e624b3f296d833c3bbcaa06a74ec5012a7f494ce0de6 / CRLF 1,239 / bareLF 0.

**Insert number sources** (all from this folder's verified `.out` files or existing manuscript
text; insert roundings listed): 17,856 and 2,268 (`s1.out` exact counts); 0.201 (`s1.out`
0.200670695, = log(11/9) analytically); 0.523 (`s2.out` Lambda(1/2,1/2) = 0.523248144);
0.5209/1.0379/1.5515 (`s2.out` 0.520906/1.037902/1.551490 at N=3200); "agrees with the one-row
value \(0.189\) above to within \(2\times10^{-4}\)" (`s2.out` 0.188909/0.188979/0.189049 vs
manuscript 0.189: max deviation 9.1e-5 vs printed, 1.4e-4 vs unrounded 0.188909); "worst residual
slack \(8.9\)" (`s3.out` worst margin -8.863544); 0.334/0.650/0.951 (`s3.out` 0.333902/0.649680/
0.951233 at C=80); 0.0017 (`s3.out` min/N = 0.001727 at C=199, q=1); 400 samples and depths
\(\le3\) (`s3.out`); "0.189 above" and "the two-row closed form above" are the integrated values
at L3161 and L3156.

**Stale passages elsewhere:** none requiring edits. Same note as 073's (mirrored): the block
closer L3165 enumerates the 065-block scope for the paragraphs above it; read as covering all of
them it would understate this insert's scope (which stacks rows to fixed depth beyond the saddle
class) - under-coverage is conservative and the insert states its own scope, so no text edit is
proposed.

## Verification scripts

All in this folder; reproduce with `python -I` from the repository root, stdout redirected:

- `python -I proposals/074-g-edge-uqstack/s1_uq_closedform.py` -> exact-rational closed form +
  072 reduction + positivity grids. Expected invariants: `PASS s1`; `cases 17856  exact-identity
  failures 0`; `cases 2268  failures 0`; strict-positivity min `0.200670695` at
  `(9, 2, 1, 0, 1, 0)`; nontrivial-grid min 0 at `(1, 1, 1, 1, 1, 1)`; `negative-count 0`.
- `python -I proposals/074-g-edge-uqstack/s2_uq_scaling.py` -> continuum scaling / depth
  linearity / additivity tables. Expected: `PASS s2`; `Lambda(1/2,1/2) = 0.523248144`;
  `t=1 N= 3200 q=1 Delta_q/N=0.520906`; `Delta_{1,0}/N = 0.188909`; `Delta_{2,0}/N = 0.377957`;
  `Delta_{3,0}/N = 0.567146`; unequal-depth lines 0.780448 / 1.040208.
- `python -I proposals/074-g-edge-uqstack/s3_uq_boxmin.py` (seconds) -> residual bound, box
  minima, breakdown. Expected: `PASS s3`; `worst (|resid|-bound) -8.863544 at (604, 259, 177,
  170, 1, 0)`; `q=1 boxmin C= 80 min/N=0.333902`; `q=1 breakdown C=200 (c=0.5000) min/N=0.000000
  arg=(0, 0)` (and the q=2,3 analogues). NOTE: the section-2 column headed `corner/N` prints
  corner/N^2 (cosmetic artifact, no assertion uses it - see Research and reasoning).
- Reproduction pack (byte-identical copies of the integrated 072/073 scripts, renamed `r1..r5`):
  `python -I proposals/074-g-edge-uqstack/r1_moment_decomposition.py` ... `r5_scaling_and_breakdown.py`.
  Expected: identical to the shipped `073` outputs: `PASS` lines; s4-form worst slack 1.816865;
  s5-form worst residual-minus-bound -6.163; Lambda 0.523248; min/N 0.495256 at C=100, N=3200;
  c=0.50 min 0.0 at (0,0); Delta(l1,0)/N = 0.188909.
- `python -I proposals/074-g-edge-uqstack/simulate_apply.py` -> read-only byte contract;
  expected appH post 700,825 B / sha 50f12c81... / CRLF 3814 / bareLF 0; bib post == pre.

Reproduction performed this round (fresh `python -I` runs from the repository root, stdout
redirected, `cmp` byte-comparison; exit code 0 for every script):

    cmp s1.out <fresh run>              -> IDENTICAL
    cmp s2.out <fresh run>              -> IDENTICAL
    cmp s3.out <fresh run>              -> IDENTICAL
    cmp r{i}.out <fresh run>, i=1..5    -> all IDENTICAL
    cmp r{i}.repro.out <fresh run>      -> all IDENTICAL
    cmp r{i}.out r{i}.repro.out         -> all IDENTICAL
    r{i}*.py sha256 == 073 s{i}*.py     -> all IDENTICAL (prefix hashes 070a4652, 748b5cf9,
                                            c3859b76, cd1aec5c, c24c3de0 match 073's manifest)
    r{i}.out == 073 s{i}.out            -> all IDENTICAL
    simulate_apply.py re-run x2         -> output byte-identical (deterministic)

Consequence: the shipped `s3.out` (mtime equal to its script) and all other outputs post-date the
x=0 fix - byte-for-byte reproducibility is the mechanical proof, since the current scripts produce
them exactly.

## Decisions Taken

1. **x=0 fix: verified by re-run, no edit.** The prior agent's message was ambiguous about which
   script the fix touched. Attribution by code inspection: only `s3_uq_boxmin.py` had a prefix
   accumulation (comment "includes x = 0" at the F-array loop); `s1`/`s2` are direct sums.
   Provenance: byte-exact fresh reproduction of every shipped `.out` (table above) proves the
   outputs post-date the fix. Rejected alternatives: regenerating outputs (nothing to regenerate -
   they already match), editing the scripts (no defect found post-fix; the in-script prefix-vs-
   direct asserts cover the diagonal where the x=0 term lives).
2. **s3 corner-column artifact: reported, not edited.** Fixing the print would change `s3.py` and
   force re-freezing outputs the gatekeeper has not yet seen changed; the artifact is cosmetic
   (diagnostic column only, no assertion, no cited number) and now documented, so the frozen
   scripts are kept (mirrors 073's decision 5 style).
3. **Insert wording "is attained at" / "vanishes at ..., attained at the trivial diagram".** The
   enumeration returns the first-encountered minimizer (ascending scan) and cannot exclude ties;
   "sits at / vanishes exactly at" would assert uniqueness of the minimum/zero beyond evidence
   (positivity of \(\Delta\) for \(\ell_2\ge1\) is grid-only). Rejected: keeping stronger wording.
4. **No manuscript citation.** The U(q)-stack naming (arXiv:2311.10131 per 072 review) is not
   load-bearing in the insert: the class is defined intrinsically. Citing would import a
   dependency the derivation does not use and repeat 073's rejected option.
5. **Anchor = long-form Vacuum-term line (line-start form), CRLF ASCII insert** - same decisions
   as 073 (items 2-3 there), re-justified: it is the live integration point and keeps adjacency to
   072/073; the short-form `\emph{Vacuum term.}` occurs twice (fibre-point paragraph L~3005 region
   and L3163) and was not used.
6. **Depth range stated honestly as fixed-depth (\(\le3\) numerical, \(q_f\) fixed in the
   limit).** Depth-growing-with-\(N\) regimes are outside the derivation (the hook term is \(o(N)\)
   only at fixed depth); no claim is stretched to \(q=q(N)\).
7. **Recovery scope:** no target, class, method or anchor change relative to the scripts on disk;
   the math content is as left by the prior researcher, verified by re-run.

No decision above changes any label, scope or core assumption; none affects emergence of
spacetime.

## Milestone assessment

Routine. No MILESTONE.md trigger applies: no critical-path step is derived, no missing link is
closed without supplied inputs; this is a conditional, class-restricted extension of 072/073 with
honest boundaries.

## Status-label recommendation

Derived from the current ledger + digest status lines this round: critical path = A (L16), B
(L151), C (L525), D (L692), E (L1584), F (L1837), G (L3026-3029: OPEN, CRITICAL PATH,
PROGRAMME-CONDITIONAL), N (L3606); H, I, J OPTIONAL (L3171, L3297, L3442). Affected labels: none.
This package changes no status, priority or completion classification; Problem G stays
OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

To close the original `G.edge-uqstack` target fully one would still need: (a) the **selection-rule
consistency** named in the frontier entry - an argument (within the 072 transplant hypothesis or
beyond it) that the diagram selected by the moment rule for the block of the union can carry
stacked rows (currently the class is a robustness subclass only); (b) strict positivity of
\(\Delta_{q_1,q_2}\) for \(\ell_2\ge1\) and general ranks (currently analytic only for
\(\ell_2=0\), numerical on the grid min 0.200670695); (c) far-corner attainment of the box minimum
beyond exhaustive \(N=400\) and uniqueness of minimizers (ties untested); (d) the stated uniform
residual bound constant proved in closed form at general \(q\) (currently: Riemann-comparison
derivation of the \(O(q\log\ell_1)\) order + coded form verified on 400 samples); (e)
depth-growing \(q(N)\) regimes; (f) everything remains conditional on (H1)-(H4) and the testbed
identification of the defect with the fixed-frame excess. For Problem G itself nothing changes:
missing steps (i)-(iv), mismatches (1)-(2), the frame average, two-sided diagrams, the minimised
block entropy, the E<->Q moment identification and the \(p_r\log p_r\) piece all remain as 072's
review left them (avenues (3)-(5) of that review unchanged in priority; avenue (2) is now mapped
for the two-stack equal-length subclass at fixed depth).

## Special instructions for the gatekeeper

- Scope limits: do not let any sentence be read as (i) any statement about the *selection* of a
  stacked diagram (the insert says so explicitly; frontier's selection-rule-consistency input is
  NOT supplied), (ii) any statement about the minimised block entropy, the frame average, or
  Problem G's missing steps, (iii) uniqueness of box minimizers or of the zero at \(C=200\)
  ("attained at", first-encountered argmin), (iv) depth-growing-with-\(N\) claims (fixed depths
  only, numerics at depths \(\le3\)), (v) general multi-row partitions (only the two-stack
  equal-length subclass).
- Re-derive, in order: the hook-comparison closed form (the crux is that the second stack's hooks
  cancel identically - union row index \(q_1+r'\), column height \(q_1+q_2\)); the Riemann-sum
  limit with \(\partial_uG(m,u)=\log(m+u)\); the \(O(q_1q_2)\) size of the hook contribution;
  \(\Delta_{q,0}>0\) factor-by-factor; \(0.200670695=\log(11/9)\) at the reported grid point;
  the x=0 term: the union-diagram hook at \(\ell_1=\ell_2\), column \(c=\ell_2\), i.e. \(x=0\).
- Re-run all commands in the Verification scripts section and the `cmp` table; re-check the s3
  corner-artifact claim against `s3_uq_boxmin.py` lines 139-145 (one-line print inspection).
- Re-verify the anchor and byte contract against the live tree before integration (other chains
  may have moved the seam; PRE pins quoted above were measured live this round, digest head
  eb8fc7d, appH digest hash 437df96e4be9).
- No bibliography change; no label touched; if you want the corner-column print fixed, that must
  be a script edit in a later round with re-frozen hashes - this round ships the frozen scripts.
