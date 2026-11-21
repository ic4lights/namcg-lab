# Proposal 072-g-edge-resum-dominant-rep, round 1

## Result

Within the dominant-representation class of the Appendix H 065 block (compact fuzzy factor,
positive contraction, leading semiclassical order with one representation), the fixed-frame
non-additivity excess recorded there as mismatch (3) is shown to be **selection-independent**:
on the exact product-fuzzy-sphere edge testbed (067-remote lineage), the edge-charge moment data
that a Frenkel-type selection rule consumes are additive over the two factors up to one corner
eigenvalue whose relative weight is $O(1/N)$, while the hook-content additivity defect of the
selected two-row diagram at the edge-data saddle $\ell_i=t\,s_i$ grows linearly in $N$
($\Delta/N=0.520906$ at $t=1$, $N=3200$). The rank dependence of mismatch (2) also survives at
the saddle ($\partial\log\dim/\partial\log M = 0.8111\,|\mu|$ at $N=3200$). This is a
conditional sharpening of the structure adjacent to item (iii) of the 065 bearing paragraph; it
closes nothing. Problem G remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Target and status

- Problem: **G** (sector entropy / edge density), Appendix H ledger entry at
  `chapters/appH-microscopic-proofs.tex` L3026-3027, quoted from the digest status-line index:
  "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope
  results: G-model and ..." The G ledger entry itself was **not read in full** under this
  round's read budget; the gatekeeper should verify the quotation against L3026-3027.
- The evidence block this package edits sits inside G's section, at L3133-3155 (the 065-remote
  bounded no-go for the compact-fuzzy-factor sent-density model). Its hypothesis class: compact
  fuzzy factor, positive contraction, single projector at fixed frame (deformed sphere and two
  caps), leading semiclassical order with one dominant representation, Gaussian states.
- This package addresses **only the representation-selection status of mismatch (3)** of that
  block (the fixed-frame non-additivity excess $\approx \ell_1\log\frac{M_1+M_2}{M_1}
  +\ell_2\log\frac{M_1+M_2}{M_2}$). Mismatches (1)-(2) and the G missing steps (i)-(iv) recorded
  in the G entry are **not touched**.
- Nothing is DERIVED toward G's original target; the package is an internal sharpening of an
  existing bounded negative result. No dependency of any critical-path target changes.

## Source reading

Digest + targeted reads. Digest status: `DIGEST CURRENT`, recorded head `eb8fc7d`
(compact, `dirty-chapters: no`). This round was resumed after a stop: the first pass of round 1
halted at `DIGEST STALE (head changed)` (the author's commit eb8fc7d postdated the digest); the
orchestrator regenerated the digest and re-dispatched. The byte pins were already exact at the
first pass, so no manuscript content moved between passes.

Read in full this round: `scratch/digest.md`; appH L3003-3008 and L3133-3156 (offset/limit
only — the file was never read whole); `s1.out`, `s2.out`, `s3.out` and their reproductions;
the three evidence scripts; `proposals/claude-remote/067-product-sphere-edge/` listing and the
first 40 lines of `e1_edge_operator_output.txt`;
`proposals/068-j-spherical-reduction-consistency/simulate_apply.py` (template);
`reports/sme-scout-20261115-1409.md` lines 13-23 plus grep context (the SME-verified citation
record for 2311.10131). Grep-verified in `bib/namcg.bib`: `Frenkel2023EdgeModes` absent;
`FlissFrenkelHartnollSoni2025` present once at L1197 (`@article`). Not read (budget): the full
G ledger entry, ch17 G passage, the 065 proposal files, prior rounds (none exist for 072).

## Claim

**CONDITIONAL SHARPENING** of the G (iii)-adjacent structure: mismatch (3) of the 065 block is
upgraded from "a statement at fixed frame, not about the minimised entropy of a block of rank
$M_1+M_2$" to "**selection-independent within the stated dominant-representation class**": for
the product-block geometry, feeding the exact edge-moment data through the class's own
selection logic (Frenkel's dominant-diagram rule transplanted to the block cut, rows at the
edge-data saddle) does not remove the excess — it survives at scale $\Theta(N)$. Mismatches (1)
and (2) are untouched; G missing steps (i)-(iv) are untouched; **Problem G remains OPEN,
CRITICAL PATH, PROGRAMME-CONDITIONAL. No closure by scope. No label change proposed.**

Provenance of the literature input: arXiv:2311.10131 [hep-th], Alexander Frenkel (solo author),
"Entanglement Edge Modes of General Noncommutative Matrix Backgrounds", v1 2023-11-16, 35
pages, no revisions, no withdrawal, no journal reference — record-level and full-text verified
by the SME agent on 2026-11-15 (`reports/sme-scout-20261115-1409.md` L12-20, read directly this
round). Per that report: the entropy object is the $\sum_r p_r\log\dim r$ piece of the edge
reduced density matrix (its eq. (41)); the dominant Young diagram is selected at leading
semiclassical order by moments of the edge charge (its eqs. (10) and (61)), one row per
disconnected component of the cut; the paper's "resummation" is the UV/IR normal-mode
resummation into the kinetic coupling $\kappa_{ij}$ ($O(C/N)$ errors), **not** an edge-entropy
resummation; and the diagonal-cut vs block/projector-cut comparison is named open by the
author. **The researcher did not independently re-fetch the paper**; these facts are used as
record- and full-text-verified by the SME report and are marked as such, not independently
verified. The insertion in this package cites the paper only for the selection rule and states
its transposition to the block cut as a transplant.

## Central derivation

Setup (the 067-remote product testbed, re-derived independently in `s1_moment_decomposition.py`
from the 067 `su2`/`config` machinery and the 067-proven per-site eigenvalue formula):
$X^I$ on $\mathbb C^N\otimes\mathbb C^N$ are the two deformed fuzzy-sphere factors
$(A_1J)^a\otimes\mathbf 1$ and $\mathbf 1\otimes(A_2J)^a$; $\Theta=\Theta_1\otimes\Theta_2$ is
the tensor product of two interval (cap) spectral projectors of ranks $M_1,M_2$;
$E=\sum_I\Theta X^I\bar\Theta X^I\Theta$; $k_f$ is the factor contraction of $A_f$,
$s_f^2=k_fM_f(N-M_f)$. The 067 run (`e1_edge_operator_output.txt`, read this round) proves
diagonality for gap-free $\Omega$ (dev $\le 2.84\times10^{-14}$), $s^2=\operatorname{Tr}E
=\tfrac12\operatorname{Tr}(\Theta\Box\Theta)$, the closed forms $s^2=M_2s_1^2+M_1s_2^2$ and
$T=(M_2-1)s_1+(M_1-1)s_2+\sqrt{s_1^2+s_2^2}$, and rank $M_1+M_2-1$ (dev $\le1.4\times10^{-14}$).

**Lemma 1 (exact edge spectrum and moment decomposition; `s1`).** For $2\le M_1,M_2\le N-2$,
the nonzero spectrum of $E$ is exactly the multiset
$$\{\,s_1^2\ \times(M_2-1),\qquad s_2^2\ \times(M_1-1),\qquad s_1^2+s_2^2\ \times 1\,\},$$
hence $\operatorname{Tr}E^p=(M_2-1)s_1^{2p}+(M_1-1)s_2^{2p}+(s_1^2+s_2^2)^p$ for all $p\ge1$,
and $\operatorname{rank}E=M_1+M_2-1$. *Reasoning:* the 067 per-site formula is additive over
the two factor directions for gap-free $\Omega$; each interior boundary site of the rectangle
$\Omega$ carries exactly one factor's single-factor boundary value ($s_1^2$ or $s_2^2$), and
the two sides of the rectangle meet at exactly one corner site carrying both — counting gives
$(M_2-1)+(M_1-1)+1=M_1+M_2-1$ edge sites, and the $p{=}1$ sum reproduces 067's
$\operatorname{Tr}E=M_2s_1^2+M_1s_2^2$ and 067's $T$ (a second independent cross-check, since
$T$ is the sum of square roots of the same multiset). *Verification:* 12 random cases
$N\in\{6,9,12\}$ (seed 72001): max addrel deviation $2.111\times10^{-16}$ (identity (b) vs
(a) spectra), max kronecker/site/spectral deviation $1.421\times10^{-14}$, rank deviation $0$
(exact). Classification: **conditional** (the gap-free rectangle combinatorics of the
067-proven formula) + **numerically verified** at exact finite $N$.

**Lemma 2 (exact hook-content closed form for the two-row defect; `s2`).** For the
two-row diagram $(\ell_1,\ell_2)$, $\ell_1\ge\ell_2\ge1$, define the additivity defect
$$\Delta(M_1,M_2;\ell_1,\ell_2):=\log\dim_{U(M_1+M_2)}(\ell_1,\ell_2)
-\log\dim_{U(M_1)}(\ell_1)-\log\dim_{U(M_2)}(\ell_2).$$
By the hook-content formula $\dim_M(\text{rows})=\prod_{(r,c)}(M+c-r)/h(r,c)$, the content
factors of row 1 and row 2 give the two products below and the hook products telescope to
$(\ell_1+1)/(\ell_1-\ell_2+1)$, giving the closed form
$$\Delta=\sum_{c=1}^{\ell_1}\log\frac{M_1+M_2-1+c}{M_1-1+c}
+\sum_{c=1}^{\ell_2}\log\frac{M_1+M_2-2+c}{M_2-1+c}
-\log\frac{\ell_1+1}{\ell_1-\ell_2+1}.$$
*Verification:* the underlying rational identity was checked with exact `Fraction` arithmetic
on 1155 cases ($7\times5\times11\times3$ grid of $(M_1,M_2,\ell_2,\ell_1)$): **0 failures**;
the hook-telescoping product and the rank-derivative identity
$\partial\log\dim/\partial\log M=\sum_{(r,c)}M/(M+c-r)$ (the (ii)-formula of L3151) were checked
symbolically (sympy). Grid survey ($M\le40$, $\ell_i\le(M_1+M_2)/2$): $\Delta>0$ with minimum
$4.054651\times10^{-1}$ at $(M_1,M_2,\ell_1,\ell_2)=(2,2,1,1)$ — where the closed form gives
exactly $\log 2+\log\frac32-\log 2=\log\frac32$, hand-checked. **Honest negative:** $\Delta$ is
NOT monotone in $\ell_2$; the minimum of the increment is
$\Delta(\ell_1,\ell_2{+}1)-\Delta(\ell_1,\ell_2)=-6.657482\times10^{-1}$ at
$(2,24,13,12)$ — hand-checked: the increment there is $\log\frac{37}{36}-\log 2=-0.6656$. The
mechanism is the hook-correction term $-\log\frac{\ell_1+1}{\ell_1-\ell_2+1}$ as $\ell_2\to\ell_1$.
A supplementary monotone comparison $T_1\ge T_2$ (the two row products at shifted ranks) passed
576/576 exact-rational cases (informational). Classification: closed form **established**
(exact identity, finite case grid); positivity **grid-survey numerical** (not proved for all
partitions); non-monotonicity **established by counterexample**.

**Proposition (selection-independence at the edge-data saddle; `s3`).** Hypothesis class
(stated, not derived): (H1) the 067 product testbed with block rank $M=M_1+M_2$,
$M_f=m_fN$; (H2) leading semiclassical order with one dominant representation — the 065 class —
with the diagram selected by $U(M)$-invariant moments of the edge datum via Frenkel's rule
(one row per disconnected component; rows fixed by edge-charge moments, his eqs. (10)/(61)),
transplanted to the block cut as the 2311.10131 author himself leaves open; (H3) the saddle
rows $\ell_i=t\,s_i$, $t$ fixed as $N\to\infty$ (the 065 row-length relation
$\langle\ell^2\rangle=4s^2W$, $t=2\sqrt W$); (H4) two-row diagrams (the rule's output for a
two-component block on this testbed).

Statements, all within (H1)-(H4):
1. *Selection data are additive up to a corner mode of relative weight $O(1/N)$.* By Lemma 1
   the only non-additive term of $\operatorname{Tr}E^p$ ($p\ge2$) is the corner power
   $(s_1^2+s_2^2)^p$; the relative corner correction
   $\delta_p:=\bigl((s_1^2+s_2^2)^p-s_1^{2p}-s_2^{2p}\bigr)/\operatorname{Tr}E^p$ (computed
   with the full Lemma-1 multiset) decreases as $1/N$: at $p=2$, $(m_1,m_2)=(\tfrac12,\tfrac13)$,
   $N\,\delta_2 = 2.3943\to 2.4396$ for $N=100\to3200$. Small finite-$N$ values:
   $N{=}6$ $(4,2)$: $2.5\times10^{-1}$ ($p{=}2$), $5.0\times10^{-1}$ ($p{=}3$);
   $N{=}9$ $(4,6)$: $1.6304\times10^{-1}$, $3.6523\times10^{-1}$;
   $N{=}12$ $(10,5)$: $8.9457\times10^{-2}$, $1.9769\times10^{-1}$.
2. *The defect is extensive at the saddle.* $M_1=M_2=N/2$, $k_1=k_2=1$:
   $\Delta/N = 0.520906$ at $t=1$, $N=3200$ (increasing sequence
   $0.4827\to0.5209$, $N=100\to3200$); $t=0.5$: $0.294133$; $t=2$: $0.860434$.
   **Honest shortfall:** the ratio $\Delta/\text{(naive form }
   \ell_1\log(1{+}M_2/M_1)+\ell_2\log(1{+}M_1/M_2)\text{)}$ stabilises near
   $0.7515$ at $t=1$, $N=3200$ (increasing, still drifting up), i.e. the naive
   L3151 "about" form overcounts the exact defect by $\sim25\%$ at $t=1$; the ratio is
   $0.8487$ at $t=0.5$ and $0.6207$ at $t=2$ — the deficit is not a uniform constant.
   Four small product cases at $t=1$ (rows sorted $(\max,\min)$ of $(s_1,s_2)$) are all
   positive: $(6,4,2)$ rows $(3,3)$: $\Delta=1.8124$, leading $4.5122$; $(9,4,6)$ $(4,4)$:
   $2.7758/5.7085$; $(12,10,5)$ $(6,4)$: $4.7260/6.8272$; $(12,8,3)$ $(6,5)$: $4.8451/8.4071$.
   Combining 1 and 2: the selection input varies from the additive one by $O(1/N)$ relative,
   while the defect at the selected saddle is $\Theta(N)$ — an $O(N^2)$ separation between
   the scale of the selection data's cross-factor distortion and the scale of the defect.
3. *The (ii)-type rank dependence survives at the saddle.*
   $\partial\log\dim/\partial\log M=\sum_{(r,c)}M/(M+c-r)$ at the $t{=}1$ saddle diagram of $U(N)$
   gives $2595.6$ against $|\mu|=3200$ at $N=3200$: ratio $0.8111$ (sequence $0.8143, 0.8118,
   0.8111$). **Honest negative:** the ratio is $0.81$, not $1$ — the $|\mu|$-saturation of
   L3151 requires $M\gg\ell$, which the saddle ($\ell\propto N$) does not satisfy; the rank
   term survives with a reduced coefficient at the tested fractions.

*Conclusion (conditional, class-restricted):* within (H1)-(H4), the mismatch-(3) excess is not
an artefact of the fixed probe diagram of L3151 — the diagram class that the selection rule
itself points to carries the same extensive non-additivity. Classification: 1 and the
numerical content of 2 and 3, **conditional + numerically verified** at exact finite $N$ /
scaling sequences; the transfer of the selection rule to the block cut, the identification of
the dominant diagram with the saddle rows, and any claim that the true minimised entropy of
the block has this defect are **conjecture/transplanted input**, outside what is established.
The $O(N^2)$-separation argument for "no diagram in the class absorbs the defect" is a
**mechanism/argument**, not a proof (no optimisation over diagrams is performed).

## Evidence (verification scripts and reproduction)

All scripts live in `proposals/072-g-edge-resum-dominant-rep/` (absolute path:
`C:/Users/redgi/Projects/namcg-lab@gpu/proposals/072-g-edge-resum-dominant-rep/`).
Reproduction commands (run from the repo root) and expected invariant outputs:

```
python -I proposals/072-g-edge-resum-dominant-rep/s1_moment_decomposition.py
python -I proposals/072-g-edge-resum-dominant-rep/s2_hook_content.py
python -I proposals/072-g-edge-resum-dominant-rep/s3_saddle_residual.py
python -I proposals/072-g-edge-resum-dominant-rep/simulate_apply.py
```

- `s1_moment_decomposition.py` (numpy, seed 72001): rebuilds the 067 edge operator on the
  product factor and checks (a) diagonality + 067 per-site formula, (b) the Lemma-1 multiset,
  (c) the moment identity $p=1..5$, (d) rank and $\operatorname{Tr}E$, (e) the direction-wise
  split $E=E_1+E_2$ against the single-factor interval edge diagonals.
  Expected: `max addrel deviation: 2.111e-16`, `max kroneck/site/spec deviation: 1.421e-14`,
  `max rank deviation: 0.000e+00`, last line `PASS s1`. Reproduced (this round):
  `PASS s1`, all values as saved.
- `s2_hook_content.py` (exact `Fraction` + sympy): Lemma-2 closed form, telescoping product,
  rank-derivative identity, positivity and monotonicity surveys, $T_1\ge T_2$ check.
  Expected: `exact rational identity: 1155 checks, 0 failures`, `exact identity: OK`,
  `hook-ratio symbolic: OK`, `derivative symbolic: OK`,
  `grid min Delta ... 4.054651e-01 at (2, 2, 1, 1)`,
  `grid min Delta(l1,l2+1)-Delta(l1,l2): -6.657482e-01 at (2, 24, 13, 12)`,
  `T1 vs T2 ...: 576 of 576`, last line `PASS s2`. Reproduced.
- `s3_saddle_residual.py` (float, exact closed forms): saddle $N$-scaling, corner-mode
  fractions, finite-$N$ cases at $t=1$, saddle rank ratio.
  Expected key lines: `t=1.0 N= 3200 l= 1600 Delta/N=0.520906 leading/N=0.693147
  ratio=0.751508`, `N= 3200 m1=1/2 m2=1/3 p=2  delta_p/TrE^p = 7.6237e-04  (xN = 2.4396)`,
  `N= 3200 rows=(1600,1600)  sum M/(M+c-r)=2595.6  |mu|=3200  ratio=0.8111`, last line
  `PASS s3` (plus asserts that all $\Delta>0$ in section (3)). Reproduced.
- `simulate_apply.py`: byte-contract simulation (below). Reproduced; stdout saved as
  `simulate_apply.out`.

Reproduction evidence for round 1: `s1.repro.out`, `s2.repro.out`, `s3.repro.out` are fresh
runs of the shipped scripts made this round and are **byte-identical** to the saved
`s1.out`, `s2.out`, `s3.out` (identical sha256, see Manifest). The shipped `.out` files were
never overwritten. Tool output is a check, not a proof: Lemma 1's exactness claim is a
combinatorial argument (above), and the $\Theta(N)$ scaling is a sequence trend at $N\le3200$,
not a proved limit.

**Honest negatives (recorded, not smoothed):** (i) $\Delta$ is not monotone in $\ell_2$
(counterexample $-0.666$ at $(2,24,13,12)$, mechanism = hook correction as $\ell_2\to\ell_1$);
(ii) $\Delta$ / naive-leading ratio $\approx0.75$, not $1$, and still drifting at $N=3200$;
(iii) saddle rank ratio $0.8111$, not $1$; (iv) the corner fraction is tested up to $N=3200$
at $p=2$ (smaller finite-$N$ cases at $p=3$ only); (v) no optimisation over diagrams is
performed — "selection-independence" is stated for the saddle-class restriction only.

## Proposed text and byte contract

**Manuscript change (one file, `chapters/appH-microscopic-proofs.tex`): purely additive
insertion, no deletions, no edits to existing text.**

- Anchor (long form, verified count == 1):
  `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}` (paragraph at L3153).
  The short form `\emph{Vacuum term.}` occurs **twice** (L3006 and L3153) — grep-verified this
  round; `simulate_apply.py` asserts both counts and uses the line-start-anchored long form.
- Boundary quoted: insertion goes after the end of the "Bearing on
  Assumption~\ref{ass:Sent-density}" paragraph (last words: "... rests on
  Assumption~\ref{ass:dictionary} and Problem~D.", L3151) and immediately before the
  `\emph{Vacuum term.}` paragraph (first words: "The abstract of~\cite{Steinacker2023} states
  that the vacuum energy there does not act as a cosmological constant but stabilises the brane
  structure at one loop."). All existing sentences, including the block closer at L3155
  ("These statements are for a compact factor ... Problem~G remains open and
  PROGRAMME-CONDITIONAL."), are kept unchanged; the inserted closer is scoped to the inserted
  paragraph and does not contradict or re-edit L3155.
- The paragraph text is `insert-r1.tex` (LF, ASCII, 3243 B, 7 lines). It uses no `\ref`,
  `\eqref` or `\label` (so no new label obligations; the two citation keys are the only
  external references: `Frenkel2023EdgeModes` once — new, from `bib_additions.bib` — and
  `FlissFrenkelHartnollSoni2025` once — pre-existing, `bib/namcg.bib` L1197, grep-verified).
- Stale passages elsewhere: none identified; the insertion makes no claim that changes any
  other passage. No ch17 edit.
- Bibliography (append-only, `bib/namcg.bib`): `bib_additions.bib` (CRLF, 360 B) appends the
  one `@misc` entry with fields taken exactly from the SME-verified record (solo author, title,
  eprint 2311.10131, hep-th, year 2023, note records v1/16-Nov-2023/35 pages/no revisions/no
  journal reference). No DOI/journal field is supplied because the SME record-level check found
  none.

**Byte contract.** PRE pins (measured this round, match the orchestrator pins exactly):
appH 692,406 B, sha256 `531a1e5b4127c7966c69b5dcaa3b776764df8324b1f64d246539ba1525fc2388`,
CRLF 3802, bareLF 0; bib 37,103 B, sha256
`44ef152d2bb17364d29b83a9780dec90d8ca76ecb1804985dd40e082d46e3a81`, CRLF 1230, bareLF 0.
POST (from `simulate_apply.out`, exit 0):
appH 695,658 B, sha256 `a41055028eb6a93e04d4ca509f335f8ca285ead761845137cd01aac7432550c4`,
CRLF 3810, bareLF 0; bib 37,463 B, sha256
`4d6d7b2a668fdaa64663e624b3f296d833c3bbcaa06a74ec5012a7f494ce0de6`, CRLF 1239, bareLF 0.
Arithmetic cross-checks: $695{,}658-692{,}406=3252$ = insert body (3242 B) $+\,7$ CRLF
conversions $+\,2$ paragraph-break CRLF; $37{,}463-37{,}103=360$ = `bib_additions.bib`;
CRLF deltas $+8$ and $+9$ match. The simulator is READ-ONLY (binary reads, in-memory
replacement, no writes; asserts anchor counts and POST anchor counts 2/1, insert ASCII/LF/no
dollar/no `$`-math/no labels/no `\ref`, bib ends `}\r\n`).

## Open items (explicitly NOT closed)

- Mismatch (1) — factor-edge vs $\partial M$ of def:HBEV: untouched by this package; G
  missing-step (i) remains open regardless of this sharpening.
- G missing steps (ii)-(iv): untouched.
- Rank dependence beyond the dominant class ($|\mu|\log M$ with general $\mu$, frame-averaged
  or minimised entropies): open; this package only evaluates the rank-derivative formula at
  two-row saddle diagrams.
- $\ell_2$-monotonicity mechanism of $\Delta$: open (counterexample given; no structural
  explanation proved; positivity of $\Delta$ is a grid survey, not a theorem over partitions).
- Minimisation over frames, two-sided diagrams, the full minimised entropy of a rank-$M_1+M_2$
  block, the $O(C/N)$ errors of the selection rule, and the $p_r\log p_r$ piece of the edge
  entropy: all outside this package.
- Transplanting Frenkel's selection rule from diagonal cuts to block/projector cuts (named
  open by the author): used as hypothesis (H2), not derived.

## Decisions Taken

- "insertion anchor corrected by the orchestrator from `\emph{Vacuum term.}` (count 2,
  L3006+L3153) to the long form (count 1, L3153)" — recorded verbatim; both counts
  re-verified by `simulate_apply.py` before and after the simulated insertion.
- No `\ref` to Problem G's ledger label: the neighbouring L3155 closer uses plain text
  "Problem~G"; the insert mirrors that convention instead of introducing a label dependency
  under the budget that forbade reading the G label. Rejected: `\ref{prob:G}`-style (label not
  verified this round).
- Insert cites `Frenkel2023EdgeModes` once (selection rule only) and
  `FlissFrenkelHartnollSoni2025` once (leading-order entropy class), matching L3151's framing;
  rejected a second Frenkel mention (the resummation/UV-IR content is not used here).
- Bibliography entry typed `@misc` with `eprint`/`archivePrefix`/`primaryClass` and a `note`
  carrying the record-verified version facts; rejected `@article` with invented journal fields
  (none verified).
- The insert's corner-mode sentence states the $O(1/N)$ fraction against $\operatorname{Tr}E^p$
  directly (matching `s3`'s full-multiset computation); rejected a wording tying it to
  "one-row values", which the script does not compute.
- Stopped the first pass at `DIGEST STALE` per the round's gate instead of regenerating the
  digest (digest regeneration is orchestrator-exclusive); continued after the orchestrator
  refreshed it. Recorded here because it is visible in the folder history.

## Milestone assessment

Routine. No milestone trigger believed to apply: no critical-path step is derived; the package
sharpens the hypothesis class of an existing bounded negative result adjacent to G(iii).

## Status-label recommendation

No label changes (expected and actual: unchanged). Current critical-path set re-derived from
the digest status-line index (appH L16/L151/L525/L692/L1584/L1837/L3026/L3596; ch17 L123/L140/
L330/L378/L395/L404/L475/L498/L740): A, B, C, D1, E, F, G, N all remain OPEN / CRITICAL PATH,
PROGRAMME-CONDITIONAL. G (appH L3026-3027) is unaffected by this package. Caveat: within the
read budget only the digest status-line index, not the full ledger entries, was read.

## Author decision needed

None.

## Remaining open step

To close the original target (G's edge-density derivation for the stated programme) one would
still need: an identification of a factor edge with $\partial M$ of the emergent spacetime
(mismatch 1 / step (i)); a derivation — not a transplant — of the dominant-diagram selection
for the block/projector cut from the matrix integral, including the frame average and
minimisation of FlissFrenkelHartnollSoni2025; control of the $O(C/N)$ and $p_r\log p_r$
omissions; and the identification of the length $s$ with the metric length of
eq:g-from-e (mismatch, step (iii)). This package reduces the selection-related uncertainty in
one bounded class: within the dominant-representation class on the product block, the
fixed-frame excess cannot be removed by re-choosing the diagram at the edge-data saddle.

## Special instructions for the gatekeeper

- Verify the two anchor counts (short 2, long 1) against the live tree before integrating; the
  integrator must re-anchor regardless (another chain may move L-numbers).
- Re-run the four commands in the Evidence section; check every number quoted here against the
  fresh outputs (the `.repro.out` files must come out byte-identical to `.out` again).
- Check the bib entry against the SME report lines 12-17 (record-verified fields only; do not
  add a journal/DOI unless independently verified against the arXiv record).
- What must NOT be asserted in review or downstream text: that the excess is selection-
  independent outside the stated class (H1)-(H4); that the minimised entropy of the block has
  been computed or bounded; that Frenkel's paper contains a product-sphere entropy formula or a
  block-cut selection rule (it names the cut comparison open); that G or mismatch (1)/(2) or
  G(i)-(iv) are advanced. The insert paragraph itself must be checked to preserve all of this.
- Re-derive the two hand-checks quoted (log(3/2) at (2,2,1,1); log(37/36)−log 2 at (2,24,13,12))
  and the Lemma-1 $p{=}1$ consistency with 067's two closed forms.

## Manifest

See `manifest.md` (generated after this file; contains bytes + sha256 + line endings for every
file in the folder, including this one; `manifest.md` necessarily omits its own hash).
File roles: `proposal-r1.md` (this file), `insert-r1.tex` (manuscript text),
`bib_additions.bib` (append-only entry), `simulate_apply.py` / `simulate_apply.out`
(byte contract), `s1_moment_decomposition.py`/`s2_hook_content.py`/`s3_saddle_residual.py`
(evidence scripts), `s1.out`/`s2.out`/`s3.out` (saved evidence),
`s1.repro.out`/`s2.repro.out`/`s3.repro.out` (round-1 reproduction, byte-identical to saved).
