# Proposal 099-g-mi-p-d-d2, round 1

## Result

For the complex Wishart Gram model G = A†A (A an M×2 matrix with i.i.d. CN(0, σ²g_j)
entries, column-profile class) at D=2, this package delivers the mutual information
between the Gram spectrum p and the diagonal fibre coordinate at the fibre level and
at the quadratic-statistic level, in both named profile classes:

1. Constant-variance class (g_1=g_2): the fibre coordinate
   x=(G11−λ2)/(λ1−λ2) is exactly uniform on (0,1) and exactly independent of the
   spectrum for every M (right-unitary invariance), so I(p;x)=0 identically; at M=2
   the closed form I(p;d1)=I(p;t)=I(p;P2)=2−ln6=0.2082405308 nats follows
   (t=|2d1−1|), verified symbolically.
2. Column-profile class (g1≠g2): the conditional law of x given the spectrum is the
   truncated exponential e^{−ρx}ρ/(1−e^{−ρ}) with ρ=βτ(1−2u),
   β=1/(σ²g1)−1/(σ²g2) — the exact x-image of the 097 law e^{−βG11}; the exact joint
   density of (u,x) after τ-integration is ∝ [u(1−u)]^{M−2}s²Λ^{−2M},
   Λ=a+b(u+sx), a=1/(σ²g2), b=β, s=1−2u. Panel quadrature plus bin-free KSG Monte
   Carlo give, for g=(1,2), I(p;x)=0.0108991 (M=2), 0.0327074 (M=4) and
   I(p;P2)=0.267988 (M=2), 0.475266 (M=4) nats; σ-independent and swap-invariant
   exactly, tending to the constant-variance values as β→0.

CRITICAL CORRECTION: the predecessor artifacts in this folder (verify_099.py, its
.out, and the first insert-r1.tex) carried the hetero values I(p;P2)=0.2863661/
0.4958970. Those are wrong by ≈+1.8e−2. Their nested-scheme self-test already
showed a +4.4e−3 bias at β=0 (where the true value 2−ln6 is known), and the
tolerances (0.01, and 0.05 in the MC check) were too loose to flag it. The corrected
values 0.267988/0.475266 are reproduced by an independent split-panel GL scheme that
is exact to 2.2e−7 at β=0, and confirmed by KSG nearest-neighbour MC with the
estimator bias calibrated on the exact β=0 case (calibrated KSG 0.2679/0.4738±0.003;
0.286/0.496 excluded at >5σ). All shipped numbers are now the corrected ones.

Nothing here closes, or claims to close, any step of Problem G: these are
spectrum-side numbers about a fibre coordinate in named model classes; no state-side
profile weight is bounded, no simplex fibre is identified, no matrix integral of the
core action is evaluated.

## Target and status

Target: chain-2 rank 1 of reports/graph/frontier.yaml — mutual information between
the Gram spectrum and the diagonal fibre coordinate at D=2, both profile classes,
built on the integrated 096 (constant-variance D=2 identification), 097 (hetero
column-profile joint and conditional e^{−βG11} law) and 098 (exact fibre interval
and scalar non-recovery).

Appendix H Problem G ledger (chapters/appH-microscopic-proofs.tex, targeted read
L3022-3037): status OPEN, priority CRITICAL PATH, completion classification
PROGRAMME-CONDITIONAL, mechanism paragraph CLOSED CONDITIONALLY / derivation OPEN.
This package adds evidence in the named constant-variance and column-profile Wishart
subclasses only. It is DERIVED for those subclasses (results 1-2 above) and
PROGRAMME-CONDITIONAL in every respect bearing on Problem G: the profile class and
the slot-variance structure are supplied model inputs, no step (i)-(iv) of the G
Missing-step paragraph is touched, and no status change is proposed.

Dependencies used (integrated): 096, 097, 098. Dependencies created: none.

## Source reading

digest + targeted reads (digest reported CURRENT by the orchestrator; digest used for
navigation only). Files read in full within the targeted ranges: chapters/
appH-microscopic-proofs.tex L3022-3037 (G ledger entry, status lines) and L3188-3213
(089-098 paragraph block including the 096 constant-variance laws, the 097 conditional
law "proportional to e^{-βG11}" at L3207, the 098 paragraph and its closing tail, and
the "\emph{Vacuum term.}" line at L3211); chapters/ch17-agenda.tex L474-493 (G
completion levels); reports/sme-scout-20261119-1011.md L1-45 (route 2 = D=2
identification sublemma, already integrated as 096; Wishart/Dirichlet facts flagged
textbook Muirhead/Forrester, not independently verified). All predecessor artifacts in
this folder read (gen_insert_099.py in full; verify_099.py t-channel lines grepped;
hygiene_099.py in full). No unreadable files. The Wishart density prefactor
det(G)^{M-2}e^{−ΣGjj/(σ²g_j)} is textbook (Muirhead class) and was marked NOT
INDEPENDENTLY VERIFIED at the literature level; every claim used here is re-derived
from it or checked against direct complex-normal sampling, so no result rests on the
unverified citation.

## Research and reasoning

Coordinates. tau=tr G>0, u=λ2/tau ∈(0,1/2) the min-normalised eigenvalue, s=1−2u,
x=(G11−λ2)/(λ1−λ2)=|v1|² ∈(0,1) where v is the unit eigenvector for λ1, d1=G11/tau
=u+sx, t=|2d1−1|=s|2x−1|, P2=(1+t²)/2. The map p↔(tau,u) is bijective on ordered
spectra, so I(p;·)=I(tau,u;·)=I(u;·) once tau is integrated out (tau carries no extra
information about x beyond what enters ρ; see the joint below).

Constant-variance class. For g1=g2 the law of A is invariant under right unitary
conjugation A→AU; G→U†GU. Hence the eigenbasis of G is Haar on U(2) and independent
of (λ1,λ2); x=|v1|² is then exactly Beta(1,1)=uniform on (0,1), independent of the
spectrum, for every M. I(p;x)=0 follows exactly. At M=2 the ordered eigenvalue density
is f_U(u)=6(1−2u)² and d1~Beta(2,2) with density 6d1(1−d1) (entropy 5/3−ln6); folding
d1→t=|2d1−1| gives f_T(t)=(3/2)(1−t²) (same entropy, Jacobian cancels); the sep
density is 3s² with E ln s=−1/3. Then I(u;t)=H(T)−H(T|U)=H(T)−E ln s=2−ln6, and the
same value for d1 and P2 since d1↔(u,t) and P2↔t are u-bijective. All four steps are
sympy-verified identities (rederive_099.py block 3 and verify_099.py S1).

Column-profile class. The Gram density ∝ det(G)^{M−2}exp(−G11/(σ²g1)−G22/(σ²g2))
written in (tau,u,x): G11=λ2+(λ1−λ2)x, G22=tau−G11, exponent = −a·tau−ρx with
a=1/(σ²g2), ρ=βtau(1−2u), β=1/(σ²g1)−1/(σ²g2) (this is the exact x-image of 097's
e^{−βG11}; it matches 097 L3207). The Jacobian and det factors give the (tau,u,x)
joint; integrating tau exactly with ∫₀^∞ τ^{2M−1}e^{−Λτ}dτ=Γ(2M)/Λ^{2M},
Λ=a+b(u+sx)>0, yields f(u,x) ∝ [u(1−u)]^{M−2}s²Λ^{−2M}. The conditional of x given
(tau,u) is e^{−ρx}·ρ/(1−e^{−ρ}) (truncated exponential), verified numerically
against MC E[x|spectrum] (0.3332 vs 0.3328 at M=2; 0.2675 vs 0.2675 at M=4) and the
joint against an 8×8-cell MC histogram (Λ^{−4} median cell ratio 0.999; candidate
exponents Λ^{−3},Λ^{−5}, exponential tilt and s²-only all rejected). σ-invariance is
exact: scaling (a,b)→(c·a,c·b) multiplies f by c^{2M} only (a constant).
g-swap invariance holds because x→1−x maps (u,x)-laws of (g1,g2) to (g2,g1) and
t,P2 are x-reflection invariant; both verified numerically to 1e-9.

MI computation. I(u;x) by 2D GL quadrature on the exact joint. For I(u;t) use
I=E[ln f_{T|U}(t|u)]+H(T) with f_{T|U}(t|u)=[f(u,x+)+f(u,x−)]/(2s f_U(u)),
x±=(1±t/s)/2; H(T) is the −∫f_T ln f_T of f_T(t)=∫[f(u,x+)+f(u,x−)]/(2s)du computed
by per-t-node split-panel GL (panels [0,u*] and [u*,1/2], u*=(1−t)/2) on the analytic
kernel, so the support boundary u*=u*(t) is an exact panel edge and no masked GL is
used. Validation: at β=0 the scheme returns 2−ln6 to 2.2e−7 absolute error. The
predecessor failure mode: their It=H(T)−E[H(T|U)] with H(T|U) built from a 300-node
entropy of |2x−1| under truncated-exponential x; at large |ρ| that density peaks
sharply at 0 and their scheme underestimates H(Y|U) (Y=|2x-1|), inflating It=H(T)-E[H(T|U)]; their β=0
self-test shows the +4.4e−3 residual and their S5 MC tolerance 0.05 hid the +1.8e−2
hetero error. MI caveat kept in view: I(p;x)=0 but I(p;d1)≠0 because d1=u+sx is a
u-dependent bijection of x and MI is not invariant under such (channel-dependent)
output maps — the insert text keeps x and P2 channels separately named.

## Claim classification

- Uniformity and spectral independence of x in the constant-variance class, every M:
  established derivation (right-unitary invariance + Haar eigenvectors; standard).
- I(p;x)=0 constant-variance, every M: established (consequence of the above).
- Closed forms f_U=6(1−2u)², f_{d1}=6d1(1−d1), f_T=(3/2)(1−t²), E ln s=−1/3,
  I(p;d1)=I(p;t)=I(p;P2)=2−ln6 at M=2: established identity/derivation (sympy-checked).
- Truncated-exponential conditional of x given (tau,u) with rho=beta*tau*(1−2u), and
  exact joint f(u,x) ∝ [u(1−u)]^{M−2}s²Λ^{−2M} in the column-profile class:
  established derivation from the Wishart density (whose prefactor is textbook, not
  independently verified as a citation, but reproduced by direct sampling here).
- sigma-independence and g-swap invariance of all D=2 numbers: established (exact
  symmetries of the joint; verified numerically to 1e-9).
- I(p;x)=0.0108991/0.0327074 and I(p;P2)=0.267988/0.475266 for g=(1,2): numerical
  quadrature results (absolute accuracy ~1e-6, validated at beta=0), cross-checked by
  KSG nearest-neighbour MC (bias-calibrated, +-0.003) and by 30x30/8x8 MC histograms;
  the earlier folder values 0.2863661/0.4958970 are rejected as quadrature artifacts.
- beta→0 limits: established (continuity of the joint; cv rows of rederive_099.py).
- NOT claimed: any bound on state-side profile weight, any simplex-fibre
  identification, any matrix integral of the core action, any state or selection
  mechanism, any step toward closing Problem G.

## Proposed changes

File: chapters/appH-microscopic-proofs.tex (the ONLY manuscript file touched).
Location: insert one new paragraph line immediately after the 098 paragraph and
before the blank line preceding "\emph{Vacuum term.}" in the G ledger block (the
paragraph that begins "\emph{Exact fibre interval of the diagonal quadratic
statistic...}"). Anchor (verified unique by hygiene_099b.py, compound probe count=1):
the 098 tail "...and they close nothing in Problem~G." + CRLF CRLF +
"\emph{Vacuum term.}"; byte cut at offset 755141 (prefix keeps the 098 line and the
blank line; a blank line is added after the new paragraph). All existing text is kept;
nothing is removed, reworded or reordered; no other passage elsewhere cites the 099
numbers, so there are no stale-passage edits elsewhere.

The inserted paragraph (single line, CRLF-terminated, exactly as shipped in
proposals/099-g-mi-p-d-d2/insert-r1.tex, sha8 0cdf7c9b):

```latex
\emph{Mutual information between the Gram spectrum and the diagonal fibre coordinate at \(D=2\).} In the constant-variance \(D=2\) class the fibre coordinate \(x=(G_{11}-\lambda_{2})/(\lambda_{1}-\lambda_{2})\) is exactly uniform on the unit interval and exactly independent of the spectrum for every \(M\), by right-unitary invariance, so the mutual information between the spectrum and the fibre coordinate vanishes identically; at \(M=2\), combining this independence with \(f_{U}(u)=6(1-2u)^{2}\) and the affine fibre map gives in closed form \(I(p;d_{1})=I(p;t)=I(p;P_{2})=2-\ln 6=0.2082405308\) nats for the ordered-diagonal, pair and quadratic-statistic channels, where \(t=|2d_{1}-1|\). In the column-profile class with \(g_{1}\neq g_{2}\) the conditional density of the fibre coordinate given the spectrum is the truncated exponential \(e^{-\rho x}\) on the unit interval with \(\rho=\beta\tau(1-2u)\) and \(\beta=1/(\sigma^{2}g_{1})-1/(\sigma^{2}g_{2})\), and nested quadrature on the exact joint density of \((\tau,u,x)\), cross-checked by direct Wishart sampling, gives \(I(p;x)=0.0108991\) at \(M=2\) and \(0.0327074\) at \(M=4\) and \(I(p;P_{2})=0.267988\) at \(M=2\) and \(0.475266\) at \(M=4\) nats for \(g=(1,2)\); these values are exactly independent of \(\sigma\), invariant under \(g_{1}\leftrightarrow g_{2}\), and tend to the constant-variance values as \(\beta\to 0\). These are spectrum-side numbers about a fibre coordinate: they bound no state-side profile weight, identify no simplex fibre, and they close nothing in Problem~G.
```

No bib entries, no labels/refs, no ch17 edits.

## Verification scripts and reproduction pack

All commands from the repo root, all with `python -I`, all stdout small; each .out is
shipped beside the script. Byte authority for the insert is gen_insert_099.py alone.

1. `python -I proposals/099-g-mi-p-d-d2/gen_insert_099.py` -> must print
   `bytes=1556 sha256=0cdf7c9b8d20a4d6...` (full digest in output); regenerating
   reproduces insert-r1.tex byte-identically. Invariant: size 1556, sha8 0cdf7c9b.
2. `python -I proposals/099-g-mi-p-d-d2/rederive_099.py` (rederive_099.out; ~1 min)
   -> invariants: rows `M=2 g=(1,2) sig=1: I(p;x)=0.01089907 I(p;P2)=0.267988606` and
   `M=4 ... 0.03270741 / 0.475265655`; sig=2 and swap rows identical to sig=1 at 1e-9;
   `cvM2 quadrature 0.2082403121` vs exact `0.2082405308` (error 2.2e-7); sympy block
   all True; `SUMMARY ALL PASS`.
3. `python -I proposals/099-g-mi-p-d-d2/mc_099.py` (mc_099.out) -> invariants:
   `E[x|spec] formula=0.3332 vs MC=0.3328` (M=2) and `0.2675 vs 0.2675` (M=4): the
   097 conditional law and rho formula confirmed by direct Wishart sampling.
4. `python -I proposals/099-g-mi-p-d-d2/cellcheck_099.py` (cellcheck_099.out) ->
   invariant: `Lam^-4 ... median ratio=0.999` while all alternative joint-exponent
   candidates give medians 0.75-1.15: the exact joint shape is MC-confirmed.
5. `python -I proposals/099-g-mi-p-d-d2/ksg_099.py` (ksg_099.out; ~3 min) ->
   invariant: calibrated bias line (cv case KSG 0.2058, bias -0.0024 against the exact
   0.2082405) and hetero calibrated KSG 0.2679/0.4738 within +-0.003 of the panel
   values; 0.2863661/0.4958970 lie 6-8 bias-units away: excluded.
6. `python -I proposals/099-g-mi-p-d-d2/hygiene_099b.py` (hygiene_099b.out) ->
   `SUMMARY ALL PASS`; pins: live appH 791958 B / sha 711ed76d..., CRLF 3860 bareLF 0,
   idiom 24, verb 1, Vacuum 2, headers 089-098 unique and ordered, 620-B live 098 tail
   equals d[754517:755137] exactly, cut offset 755141, compound probe count 1, insert
   1556 B / 0cdf7c9b single terminal CRLF, header absent pre-insert.
7. `python -I proposals/099-g-mi-p-d-d2/simulate_apply_099.py` (simulate_apply_099.out,
   READ-ONLY, ends `no write performed`) -> full POST contract: POST bytes=793516
   sha256=fae8dcd25cf5022e54ff60f163f0c5c8ee09b156cca8a82c6a3b23628d2d1609, CRLF=3862,
   bareLF=0, idiom=25, verb(closes nothing)=1, Vacuum=2, header-count=1, adjacency
   098+new=1, new+Vacuum=1, old 098+Vacuum probe=0.
8. `python -I proposals/099-g-mi-p-d-d2/verify_099.py` (predecessor, UNCHANGED) ->
   reruns byte-deterministically (verify_099.out re-produced identically, including
   its double `SUMMARY ALL PASS` — that doubling is genuine single-run behaviour,
   lines 172 and 174 of the script). verify_099.err is one benign
   `RuntimeWarning: invalid value encountered in divide` at its rho~0 guard line.
   Its S1/S2/S3/S5 sections are sound and reused; its S4 It values are NOT used
   (see correction above) and its S4.b0/S4.dp printed values (0.212679 at g=(1,1),
   0.0044 above the exact 2-ln6) are the visible symptom of that bias.

## Decisions Taken

- **Predecessor verify_099.py kept byte-unchanged as evidence; its hetero P2 values
  rejected, not patched.** Fixing its t-channel would have destroyed the forensic
  record of why 0.2863661/0.4958970 shipped. The rejection rests on three independent
  checks (beta=0 exactness to 2.2e-7 of the corrected scheme; KSG calibration; the
  +4.4e-3 self-test bias printed in verify_099.out itself). RESEARCHER-DECISION
  resolved toward the infrared/full-GR derivation: a wrong number in Chapter 17
  evidence would have propagated; the correct number is cheap.
- **hygiene_099b.py supersedes hygiene_099.py rather than editing it.** The
  predecessor pinned a stale 098 tail; in-place editing would hide that the live
  file had to be re-read. Supersession registered in the manifest; the old pair is
  kept (status SUPERSEDED) and not deleted.
- **Insert precision fixed at 6 decimals** (0.0108991/0.0327074/0.267988/0.475266).
  Mesh refinement (n=1200->2400 nodes) moved the M=2 P2 value by ~1.1e-6, so the
  7th digit is not claimed; the cv value 2-ln 6 is closed-form and carries 10.
- **Insert regenerated at 1556 B (2 B smaller)** with corrected numbers rather than
  padding to the old 1558 B to preserve the mandated 793,518-byte POST size. Size
  fidelity to the true content beats matching a figure computed from a wrong insert;
  the deviation (POST = 793,516) is stated in the Proposed changes and Special
  instructions sections.
- **KSG metric fixed to Chebyshev (`p=np.inf`)** after Euclidean balls returned the
  impossible I(u;x)=-0.23 on the exactly-independent cv case; the cv case is then
  used as the bias calibration (bias -0.0025) and as a live check that fixed
  coordinates give I=0.
- **30x30 histogram plug-in abandoned as arbiter**: its bias (900/(2N)) and its
  strong-dependence binning loss (0.2448 on the exactly-known cv case) exceed the
  2e-2 discrimination needed; recorded as a negative methodological result.
- **Wording fix in Research and reasoning**: the failure mode is understated as
  "underestimates H(Y|U) (Y=|2x-1|), inflating It=H(T)-E[H(T|U)]" after re-reading
  verify_099.py's hy_num on a 300-node GL panel (truncation of the Y|U entropy tail
  at large |rho|, the same code path whose cv self-test overshoots by +4.4e-3).
- **Double `SUMMARY ALL PASS` in verify_099.out confirmed genuine** (two print
  statements in the script), not a concatenation artifact -- verified by rerun.

## Milestone assessment

Routine. No MILESTONE.md trigger applies: the item derives exact statements for two
named D=2 subclasses, corrects a shipped numerical error before it reached the
manuscript, and closes nothing in Problem G. No critical-path step is closed and no
missing link in the infrared or full-GR derivation is claimed closed.

## Status-label recommendation

Derived current critical-path set from ch17-agenda.tex (full-GR criterion: A, B, C,
D1, E, F, G-derived, N) and reports/ledger.md. Problem G remains OPEN / CRITICAL
PATH / PROGRAMME-CONDITIONAL; the new ledger entry is evidence only. **No label
changes proposed; all labels unchanged.**

## Author decision needed

none

## Remaining open step

Problem G's missing steps (i)-(iv) (state-side profile weight from the core action;
simplex-fibre identification; selection mechanism; matrix integral) are untouched by
this item. To move G itself, the next required calculation remains a core-action
derivation of the profile weight (the state-side question the insert explicitly
bounds out); within D=2, the natural follow-ups would be M>=3 hetero numerics and
the beta->0 uniformity rate, neither of which bears on G's missing steps.

## Special instructions for the gatekeeper

1. **Corrected numbers are the central claim to re-verify.** Re-derive I(p;P2) for
   g=(1,2) independently (any method: the panel scheme in rederive_099.py, or KSG,
   or your own). The shipped predecessors 0.2863661/0.4958970 must be shown wrong or
   my correction reverted; the cv anchor I=2-ln 6=0.2082405308 (exact, sympy block)
   is the calibration hinge.
2. The proposal asserts **no closure**; check that the insert's final sentence does
   exactly that and that no other sentence overclaims ("bound no state-side profile
   weight, identify no simplex fibre").
3. **POST size is 793,516 B, not the 793,518 B the mandate anticipated**: the mandate
   figure was computed with the old 1558-B (wrong-valued) insert; the corrected
   insert is 1556 B. Check the simulate_apply_099.out contract line by line.
4. hygiene_099.py/.out are SUPERSEDED (stale tail pin) but retained; run
   hygiene_099b.py, not the old one. verify_099.py/.out are shipped unchanged as
   evidence with S4 It values unusable -- do not reuse 0.212679 or its hetero
   offsprings anywhere.
5. Anchor check: the insert sits between the live 098 paragraph and
   `\emph{Vacuum term.}`; hygiene_099b.py pins the 620-B tail and the compound
   probe count == 1; the integrator must re-verify against the live tree.
6. Do not import Muirhead as verified literature: the Wishart/Gram density used here
   is re-derived and sampling-checked in-package; the textbook attribution is
   marked not-independently-verified in the proposal.
