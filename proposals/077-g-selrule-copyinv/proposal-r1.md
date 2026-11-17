# Proposal 077-g-selrule-copyinv, round 1

- **Target:** frontier edge `G.selrule-copyinv` (reports/graph/frontier.yaml, rank 1, state was untried,
  chain 2): a criterion or bounded negation for which matrix-state ensembles realize **copy-invariance of
  the momenta at leading semiclassical order** — the avenue 076 review-r2 ranked first ("converts C1's
  existence into selection"). Passage ownership for this chain: appH-microscopic-proofs.tex L3022-3172.
- **Problem:** G (HBEV / infrared boundary entropy), `chapters/appH-microscopic-proofs.tex`, Problem G
  section beginning L3022.
- **Scope:** full-GR / matrix-derived per `chapters/ch17-agenda.tex` (Problem G paragraph L470-500;
  G-derived completion item L720-732): the criterion requires A, B, C, D1, E, F, G-derived, N.
- **Date:** 2026-11-17. **Round:** 1. **Originator:** researcher #3 (model: sonnet, orchestrator
  allocation — recorded deviation from the standing fable allocation after two fable context-deaths on
  this item; the gatekeeper adjudicates the package on its mathematics).
- **Source reading:** digest + targeted reads (below). `chapters/appH-microscopic-proofs.tex` was never
  read whole.

## Result

For the rank-one edge-datum family of `q` coincident copies under the (H1') diagonal lifts of the
integrated 076 paragraph, this package (a) **reduces the copy-tiling question exactly**: the coincident
edge charge factorizes as Q~ = -2i(UR^† - RU^†) with rank ≤ 2q, its nonzero spectrum is that of an
explicit 2q×2q pencil (symbolic coefficient identity at q=2; nonzero spectra numerically identical to
2.31e-14 / 2.66e-14 at (q,N)=(2,5)/(3,4)); (b) **solves the q=2 criterion exactly**: double-pair (mult-2)
spectrum iff Im(alpha_1)=Im(alpha_2) AND ||w_perp,1||²=||w_perp,2||², with Re(alpha) invisible in the
deciding coefficients; (c) shows **exact tiling is measure-zero and first-order fragile** in Gaussian
ensembles (0/6000 draws; violation ratio 0.7865-0.8137 in the perturbation size; the set nonempty — an
explicit null-cone perturbation tiles to 1.084e-15); (d) establishes, **numerically and at leading
semiclassical order only**, that matched-scale iid Gaussian classes realize copy-invariance with rates
D=O(N^-1/2), U_2=O(1/N), uniform through q=O(N^1/2) tested to q=64 (with the pinned exceptions of
finding C11: U_2<0.05 fails at exactly (q,N)=(4,4q²),(4,8q²), values 0.0859/0.0549); and (e) gives
**bounded negations**: copy-tempered (1,1.6) and CV-0.4 lognormal-mixture classes retain O(1)
leading-order violation, and between the two exact q=2 conditions only the norm equality has
leading-order teeth (the Im-alpha condition is subleading, failing only at the exact-spectrum level).

**Nothing is DERIVED for the critical path.** Neither the general-q criterion nor the negation is a
theorem; the package is bounded, largely numerical evidence **PROGRAMME-CONDITIONAL** for Problem G, and
it touches none of G's missing steps (i)-(iv). One manuscript insert is proposed: a single
scope-limited paragraph after the 076 paragraph, zero new citations, zero new labels.

## Target and status

Exact current status, re-read live from the manuscript (not from the ledger snapshot):

- appH L3026-3029 (Problem G ledger): "Status: OPEN. Priority: CRITICAL PATH. Completion:
  PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and G-external support at most a scope-limited
  model; G remains OPEN and neither satisfies the matrix-derived criterion."
- appH L3120-3130 (Missing step), verbatim essentials: closing the matrix-derived criterion for
  Problem G requires (i) a derivation, not a retained dictionary, of the identification between a
  Presentation-A boundary cut and ∂M under which the cut entropy becomes the local density
  eq:Sent-exp; (ii) the interacting condensate sector of eq:Smatrix, the cubic term, matter and
  non-Gaussian ground-state correlations carrying the alpha_1/alpha_2 structures; (iii) a derivation of
  the stationarity condition eq:bdy-EE of Assumption ass:bdy-EE; and (iv) the mass-dimension-one
  boundary-to-bulk conversion recorded in the dimensional status remark of Chapter ch:hbev, without
  which eq:Leff stays schematic. **This package addresses none of (i)-(iv).**
- Dependency: the integrated 076 paragraph at appH L3167 (072-076 stack) — it proved the block-cut
  multiplicity statements for coincident copies *assuming* copy-invariant momenta under (H1') lifts.
  This package converts that assumption into evidence about **which state ensembles actually realize it
  at leading order** (and which provably do not, within tested classes).
- Classification of this package: **PROGRAMME-CONDITIONAL bounded evidence**. DERIVED: nothing.

## Source reading

Digest mode: compact digest `scratch/digest.md` (head 1cdca82; appH file hash 94b39393bdf8; 30 files;
dirty-chapters: no). Live PRE pins re-verified this round and match the digest: appH 707,434 B /
sha256 prefix 94b39393bdf8 / CRLF 3818 / 0 bare LF; bib/namcg.bib 37,463 B / prefix 4d6d7b2a668f.
Read IN FULL or in the listed ranges: appH L3015-3180 (Problem G section: ledger L3025-3029, missing
step L3119-3130, Row length paragraph L3147, 072 paragraph L3153, 073 L3161, 074 L3163, 075 L3165,
076 L3167, Vacuum-term paragraph L3169, block closer L3171); ch17-agenda.tex L470-500 and L720-732;
this folder's `manifest.md`, `findings-r1.md` and every shipped `.out`; 076's `proposal-r2.md` and
`review-r2.md` in full; `reports/ledger.md` last 30 lines; `reports/graph/frontier.yaml` L125-169 and
L427-428. `chapters/appH-microscopic-proofs.tex` (707 KB) was read ONLY in targeted ranges and by
byte/line searches; no repo file >150 KB was read whole. Previous rounds on this target: none (this is
round 1; the evidence phase was recorded in `manifest.md`/`findings-r1.md`).

## Research and reasoning

**Setup.** Same ensembles as the shipped scripts: su(2) irrep dim N, cap rank M=N/2, Theta = cap
projector, 3 flavors, coincident lifts X~=I_q⊗X, Theta~=I_q⊗Theta, iid standard complex-Gaussian
Hermitian momenta unless stated; block-cut edge charge Q~ in the rank-one edge-datum family. Two
statistics measure mult-q tiling of the signed nonzero spectrum e_1≤...≤e_(2q): the relative gap
D = max_k(e_((k+1)q-1) - e_(kq)) / max_k|e_k| and the fourth-moment signature excess
U_2 = Tr Q~^4 / (2q (Tr Q~^2/(2q))^2) - 1; both vanish iff the spectrum is q-fold tiled by the
one-copy multiset (U_2 exactly: by power-mean equality; D: by sorted-multiset comparison). These are
definitions introduced by the insert, not pre-existing manuscript objects.

**(i) Exact reduction (Lemma 1).** With U = I_q⊗u and R the qN×q edge-row block, the charge map gives
Q~ = -2i(UR^† - RU^†) identically, hence rank Q~ ≤ 2q and, by the standard Sylvester-type argument for
products of rectangular blocks applied to the companion pencil, the nonzero characteristic polynomial of
Q~ equals that of T = -2i[[C0^†, Z0], [-I_q, -C0]], C0 = U^†R, Z0 = R^†R (a 2q×2q matrix). Verified:
FULL charpoly identity exactly at q=2, N=2 (the only tested case of equal sizes); symbolic
top-coefficient (nonzero-charpoly) identities at q=2 with N=2,3; nonzero-spectrum deviations 2.31e-14
(q=2,N=5) and 2.66e-14 (q=3,N=4); T real to 1.72e-15. Convention pinned by direct test: R_xy = w_xy
(conv B) matches the full charge to 7.87e-14 while the transpose convention fails at 3.55e+01.
**Consequence:** the tiling question becomes a 2q×2q eigenvalue question for the whole ensemble, which
is what makes the large-q, large-N window scan (s2b z-path) possible. Classification: established
identity (factorization) + standard linear-algebra reduction, numerically verified at tested sizes; the
insert states the "full charpoly only when sizes coincide" caveat explicitly.

**(ii) Exact q=2 criterion (Lemma 2).** For q=2 block-diagonal pairs the charpoly coefficients in t are
t^1: 4·rho and t^0: -4·rim² - 4·rre² (rho, rim, rre the Im/Re row data): Re(alpha) is invisible in the
deciding coefficients, each row contributes the pair -2·Im(alpha) ± 2·(Im²alpha + ||w_perp||²)^(1/2) —
which is exactly the appH Row-length formula (L3147) — and the pair is a genuine double pair (mult-2
tiling) **iff** Im(alpha_1)=Im(alpha_2) AND ||w_perp,1||²=||w_perp,2||². Symbolic coefficients +
numeric verification (s5). Established at q=2; **no such closed form is claimed or expected-proofed for
q>2** (stated as a caveat in the insert).

**(iii) Exactness is not typical, but nonempty.** 0/6000 iid draws tile exactly (generic violation
median 0.6868, min 0.1190); along generic perturbation directions the violation is linear (ratio
0.7865/0.8134/0.8112/0.7865 plateau over t=1e-4..1e-1) — first-order fragile, codim ≥ 1. The set is
nonempty: the (H1') copy-invariant momenta themselves (076: Q~=I_q⊗Q gives exact tiling) and an explicit
edge-row null-cone perturbation with violation 1.084e-15 (charge-block residual 1.252e-15,
|dQ~|=2.331e-14) while the generic t=1 deviation is D=0.4886. Established numerical facts for the tested
absolutely-continuous ensemble.

**(iv) Leading-order universality.** Coincident iid, q=2: D = 0.2986/0.2120/0.1415/0.1176 at
N=50/100/200/400 (slope -0.461); U_2 = 0.1027/0.0484/0.0223/0.0143 (slope -0.965) — the printed (a)
column labelled T_2 *is* the excess statistic (the script stores T2-1; cosmetic label, disclosed).
Fixed-q windows: s2(b) at N=400, q∈{2,3,4,5,6,8,10} (round-3b reduced grid; 5 events): D 0.0986-0.1898,
U_2 0.0113-0.0155, inside the script thresholds; the dense round-1 grid q≤16 at N=400 (8 events,
preserved in `s2_universality_N.out.r1-fail`) gives D 0.0992-0.1994, U_2 0.0132-0.0160 — no O(1) growth
(the round-1 "breakdown at q ~ N^(1/3)" claim is refuted). s2b z-path (the 2q-pencil from (i)):
full-vs-reduced spectrum dev 1.59e-12/1.02e-12, median-D ratios 1.003/0.978 — the reduction is
distributionally sound; along N ~ q²..16q², q=4..32: D slopes -0.531/-0.499/-0.509/-0.496; along q at
N=1024 to q=64: D ≤ 0.1351 with along-q exponent 0.093, U_2 ≈ 0.006. **Pinned exception (the recorded
finding):** the U_2 < 0.05 level holds at all tested (a)/(b) points with N ≥ 16q² and fails at exactly
(q,N)=(4,64)=(4,4q²) with 0.0859 and (4,128)=(4,8q²) with 0.0549; all others ≤ 0.0253; within q=4 the
decay 0.0859→0.0549→0.0184 has slope ≈ -1.09 (consistent with O(1/N)); z0/z1 pass so the miss is a
genuine finite-N level, not a normalization artifact. The s2b script is left FAIL as the finding's
carrier (threshold unchanged by design). Conditional numerical results: within iid complex-Gaussian
matched-scale ensembles, fixed coincident geometry, tested ranges (Frenkel 2311.10131 fixed-q validity
respected: no claim beyond q = O(N^1/2) tested, growth beyond untested).

**(v) Bounded negations and condition ranking.** Copy-tempered (1,1.6) on the same coincident geometry:
D = 0.4147/0.4113/0.3946 at N=120/240/480 (slope -0.036), U_2 = 0.2226/0.2126/0.2003 (slope -0.076) —
an O(1) inter-copy scale mismatch keeps the violation O(1): the leading-order **negation** for
mismatched-scale classes. Block-diagonal independent per-copy class (s3): equal scales slope -0.448
(leading-order tiling), (1,1.6) slope -0.090 with D ≥ 0.242 at N=480 (persistent O(1)); fully
correlated copies (a.s.-equal momenta) sit at D = 0 exactly (the 076 C1 mechanism); partial correlation
interpolates monotonically (D at N=480: 0.0662/0.0825/0.0254/0.0074 for c=0/0.5/0.9/0.99). Gram
concentration of edge rows (s4b, corrected per-event defect): iid decays (0.4759/0.3920/0.3130, slope
-0.302 — inside the window but not the ~-1/2 of the charge-level statistic, disclosed), CV-0.4 lognormal
mixture stays at 0.8070/0.7732/0.7908 (slope -0.015), all > 0.5 — the concentration criterion fails at
leading order for scale mixtures, matching the charge-level negations. Im-alpha subleadingness (s6):
|alpha|/||w_perp|| slope -0.527, the exact-tiling distance decays only as N^-1/2 and never reaches the
tiling level (min 0.054, slope -0.436, vs the 1e-12 tiling threshold), while U_2 slope -0.901: equalizing
norms never reaches exact tiling — the Im(alpha) equality fails, and it fails only at the exact-spectrum
level. Conditional numerical results within the stated classes.

**Comparison with the original target.** The edge asked for a criterion/negation for state realization
of copy-invariance at leading semiclassical order. Delivered: an exact criterion only at q=2 (general q
stays open); sufficient-condition evidence with rates for matched-scale iid classes; bounded negations
for mismatched-scale and mixture classes; measure-zero/fragility for exactness. The exact leading-order
picture: *at leading semiclassical order, tiling of the charge ensemble is the generic behavior for
matched-scale concentrating ensembles and fails at O(1) for scale-mismatched ensembles; exact finite-N
tiling is a thin (measure-zero) set containing the identity-lift family.* Not a theorem at general q;
the criterion/negation pair is therefore **bounded, not closed**.

## Claim classification

- Insert definitions (D, U_2): notation, exact by definition; vanishing-at-tiling is an exact
  observation (power-mean equality for U_2; sorted multiset comparison for D).
- (i) factorization + pencil reduction: **established identity/derivation** (rank bound is algebraic;
  charpoly reduction standard), numerically verified at tested sizes; conv B pinned numerically.
- (ii) q=2 exact criterion: **established derivation at q=2**; general q: **unresolved**.
- (iii) measure-zero, fragility, nonempty null cone: **established numerical facts** for the tested iid
  Gaussian product ensemble at tested N, q.
- (iv) universality rates, window extents, the two pinned U_2 failures: **conditional results
  (numerical)** within iid complex-Gaussian matched-scale ensembles and the tested grids; z-path
  equivalence conditional (numerical).
- (v) negations (tempered, mixture), Gram criterion, Im-alpha subleadingness: **conditional results
  (numerical)** within the stated classes; the a.s.-equal-copy D=0 instance is an **established exact
  instance** (076 C1 mechanism).
- Single-dominant-diagram caveat: carried as an **input** from the transplanted rule (as in 072-076),
  restated in the insert's scope clause; not re-examined here.
- All rates/levels quoted in the insert: **not analytic results**; proofs beyond tested sizes and
  ensembles are **unresolved**.

## Mandatory disclosures

1. **s2 round-3b grid reduction:** section (b) runs N=400 with q capped to {2,3,4,5,6,8,10}, 5 events
   (was q≤16, 8 events); (a)/(a-control) are unchanged and byte-reproduce the researcher #1 run. Dense
   q≤16 numbers preserved in `s2_universality_N.out.r1-fail` (sha8 183ba3f8); q>10 coverage moved to the
   s2b z-path. The manifest's "D(q=10) 0.1869 at N=400" is from `out.r1-fail` (dense, 8 events), NOT
   from the shipped r3b out (which gives 0.1774); the two differ by seed-stream/event count, both cited
   where used.
2. **r3a artifact:** `s2_universality_N.out.r3a-N200` documents the N=200 test run but its header prints
   "(b) N=400" — a hardcoded print string at that revision (reporting-only; the historical run is not
   reproducible from the current scripts, which set N=400).
3. **s6 window fix (round 3):** the rel-dev assert window (-0.8,-0.25) → (-1.6,-0.5), because rel-dev is
   quadratic in the small ratio (measured slopes -0.527 vs -0.903); data/thresholds otherwise untouched;
   table byte-unchanged after the fix (out sha8 525f0828, same seed).
4. **s2 (b) assert mis-window fix (round 3):** the first assert applied the D slope window to the U_2
   slope; the researcher #1 "FAIL" (out.r1-fail) was only this mis-window (sT=-0.965 is outside the
   D-window, inside its own (-1.6,-0.5) bound).
5. **s4 supersession:** the round-1 s4 out ends in a Traceback (pooled-median fragility); the earlier
   "PASS s4" claim was a crash misread by researcher #1. `s4_oldscript_repro.out` is byte-identical
   (70571366). The shipped evidence is `s4b_gram_mixture_fixed.py` (per-event defect statistic).
6. **Convention pins:** conv B (R_xy=w_xy) 7.87e-14 vs conv A 3.55e+01; T real to 1.72e-15; nz-spectrum
   match 4.44e-15; the OLD round-1 s5 block formula was non-Hermitian (max|Q-Q^H| = 5.29e+00) and is
   superseded; `debug_s5_lemma1.py` is a historical bug record, NOT evidence.
7. **Cosmetic column label:** in s2 sections (a)/(a-control) the column printed "T_2" stores T2-1 — the
   U_2 excess exactly as the insert defines it; in (b) the excess is printed explicitly as "U_2=T_2-1".
8. **s2b FAIL is by design:** threshold kept; s2b's own D threshold is D<0.5 (the 0.25 level belongs to
   s2(b)); the insert quotes no D-level claim from s2b and presents the U_2 result only with the pinned
   exceptions. The threshold assert stays failing; this is the recorded finding, never a pass.
9. **Process lineage:** researchers #1 and #2 died on API context; the orphaned round-2 s2 process (PID
   20036, 8.64 GB, 0 output bytes — stdout was block-buffered) was killed by researcher #3 at 10:26; the
   "S2 EXIT=1" line in `s2_run_status.txt` is the orchestrator wrapper echo of that kill, not a run.
10. **Rounding in the insert:** 2.3e-14/2.7e-14 for s5's 2.31e-14/2.66e-14; 1.6e-12 for s2b z0's
    1.59e-12 (worst case); all other values verbatim from the shipped outs.

## Evidence map (claim → script → sha8 → out → re-run from repo root)

All re-runs: `python -I proposals/077-g-selrule-copyinv/<script>` (exit codes as marked). Hashes are
first 8 hex of sha256 of the file as shipped in this folder (independently recomputed this round; all
manifest hashes matched).

| claim | script (sha8) | out (sha8) | exit / verdict |
|---|---|---|---|
| (i) factorization, pencil, Lemma 2 | s5_gram_and_q2_exact.py (08e83e0f) | .out + .det.out byte-identical (9a04f362) | 0 PASS |
| (i) conventions | debug_conventions.py (6b89217a) | .out (394b727c) | 0 PASS |
| (iii) measure-zero, fragility, null cone | s1_typicality_exact.py (4e8b8ad6) | .out = .det.out (79d342dc) | 0 PASS |
| (iv) universality + rates + controls | s2_universality_N.py (917ac53b) | .out r3b (7469a471); r1-fail dense (183ba3f8); r3a (93bf0513, artifact note 2) | 0 PASS |
| (i)+(iv) z-path, windows, U_2 finding | s2b_qwindow.py (4eebfb72) | .out (51aa0f68) | 1 FAIL **by design** (finding C11; z0/z1 internally PASS) |
| (v) block-diagonal criterion, negation | s3_criterion_blockdiag.py (c6138fcd) | .out = .det.out (4562707e) | 0 PASS |
| (v) Gram criterion + mixture negation | s4b_gram_mixture_fixed.py (a59637bf) | .out = .det.out (6194df6f) | 0 PASS |
| (v) Im-alpha subleadingness | s6_imalpha.py (32e2f1e2) | .out (525f0828) | 0 PASS (post-window-fix) |
| byte contract / insert hygiene | simulate_apply_077.py (cf27ac3a) | simulate_apply_077.out (d5d45dc6) | 0 ALL ASSERTS PASS |
| insert normalization | normalize_insert.py (cf561a59) | normalize_insert.out (0fdfdf1f) | 0 |

Determinism: s1/s3/s4b/s5 `.det.out` byte-identical to `.out` (round-3 from-scratch re-runs). Insert
file on disk: 5,187 B (one 5,185 B content line + terminal CRLF), file sha8 3947273c, content sha256
prefix b7e1460eddd00c10cf25ab2e5ace0764780e32f2435a783cefac19c371a3ebf6.

## Proposed changes

**One file: `chapters/appH-microscopic-proofs.tex` — one insertion, no other edits, no deletions.**

- **Anchor (unique line-start long form):** `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}`
  — verified occurs exactly once, at L3169; the short form `\emph{Vacuum term.}` occurs twice
  (L3006 and L3169) and is NOT the anchor. The insert goes **immediately after the integrated 076
  paragraph (L3167)** and **before** the Vacuum-term paragraph, blank-line separated on both sides
  (same method the 072-076 inserts used).
- **Preceding kept text (boundary, quoted exactly):** the 076 paragraph L3167 ends with the unique
  sentence (occurs once): "These are selection-rule consistency statements for the coincident-copy and
  band-separated subclasses of the block-cut edge data of the preceding paragraphs, inside the
  transplanted rule with its single-dominant-diagram hypothesis at leading semiclassical order and its
  diagonal-cut convention; they leave the two-sided reading of the \(\pm\) pairs untreated, they do not
  fix the state that sets the multiplicity, and they close nothing in Problem~G." That paragraph, the
  Vacuum-term paragraph, the block closer L3171 and everything else are kept unchanged.
- **No stale passages elsewhere:** "copy-invarian" occurs in `chapters/**/*.tex` only at appH L3167
  (two occurrences, both in the 076 paragraph) — nothing conflicts with or needs rewording for this
  insert.
- **Hygiene (mechanically asserted by `simulate_apply_077.py`):** ASCII-only; zero occurrences of
  `\ref`, `\eqref`, `\cite`, `\label`, `$`, `[`, `]` in the insert (zero-cite ruling of the 076
  review-r2 — cross-references are descriptive: "the selection-rule paragraph above", "the Row length
  paragraph"); zero occurrences of the words status/priority/completion/open/derived/programme/critical
  in any case; exactly one `\emph{}` run (the header); ends with the single scoped status clause. No new
  bib entries; `bib/namcg.bib` untouched.
- **Byte contract (re-verified live; `simulate_apply_077.py` rebuilds POST in memory):** PRE appH
  707,434 B / sha 94b39393bdf8... / CRLF 3818 / bare LF 0 → POST **712,623 B / sha 789c668f0b4a... /
  CRLF 3820 / bare LF 0**, delta +5,189 B = content 5,185 + 2×2 B blank lines; +2 CRLF. New paragraph
  occupies POST line 3169; the Vacuum-term line moves 3169 → 3171. The integrator must re-pin against
  the live tree (another chain may have moved text).

The insert (single paragraph, file `proposals/077-g-selrule-copyinv/insert-r1.tex`, one content line):

```latex
\emph{State realization of copy-invariant momenta at leading semiclassical order.} Write \(\widetilde Q\) for the block-cut edge charge of \(q\) coincident copies of a compact factor under the lifts of the selection-rule paragraph above, \(\widetilde X=\mathbf 1_q\otimes X\) and \(\widetilde\Theta=\mathbf 1_q\otimes\Theta\), and list its nonzero eigenvalues as \(e_1\le\cdots\le e_{2q}\) in the rank-one edge-datum family, where it has at most \(2q\) of them: tiling of this spectrum by the one-copy multiset is measured by the relative gap \(D=\max_k(e_{(k+1)q-1}-e_{kq})/\max_k|e_k|\) and the fourth-moment signature excess \(U_2=\operatorname{Tr}\widetilde Q^{4}/(2q(\operatorname{Tr}\widetilde Q^{2}/(2q))^{2})-1\), which vanish at tiling. The charge factorizes exactly as \(\widetilde Q=-2\mathrm i(UR^\dagger-RU^\dagger)\) with \(U=\mathbf 1_q\otimes u\) and \(R\) the \(qN\times q\) edge-row block, and its nonzero characteristic polynomial is exactly that of the explicit \(2q\times2q\) pencil \(-2\mathrm i\left(\begin{smallmatrix}C_0^\dagger&Z_0\\-\mathbf 1_q&-C_0\end{smallmatrix}\right)\) with \(C_0=U^\dagger R\), \(Z_0=R^\dagger R\): the coefficient identity is symbolic at \(q=2\), with full characteristic-polynomial agreement when the two sizes coincide, and the nonzero spectra agree to \(2.3\times10^{-14}\) at \((q,N)=(2,5)\) and \(2.7\times10^{-14}\) at \((3,4)\) (numerical). For \(q=2\) block-diagonal pairs the criterion is exact: the spectrum is a double pair if and only if \(\operatorname{Im}\alpha_1=\operatorname{Im}\alpha_2\) and \(\|w_{\perp,1}\|^{2}=\|w_{\perp,2}\|^{2}\), \(\operatorname{Re}\alpha\) being invisible in the coefficients that decide it, and each row contributes the pair \(-2\operatorname{Im}\alpha\pm2(\operatorname{Im}^{2}\alpha+\|w_\perp\|^{2})^{1/2}\) of the Row length paragraph (symbolic and numerical; no such reduction is established for \(q>2\)). Within Gaussian momenta exact tiling is not typical and is fragile: none of \(6000\) independent draws tiles exactly, along a generic direction the violation is linear in the perturbation with ratio between \(0.7865\) and \(0.8137\) over four decades, and exact tiling is realized only on thin families, the copy-invariant momenta of the identity above and an edge-row null-cone perturbation (violation \(1.084\times10^{-15}\)). At leading semiclassical order in \(N\) the violation of tiling is generically small: for independent standard complex Gaussian momenta with equal per-copy variance, at \(q=2\), \(D\) takes the values \(0.2986,0.2120,0.1415,0.1176\) at \(N=50,100,200,400\) (slope \(-0.461\)) and \(U_2\) the values \(0.1027,0.0484,0.0223,0.0143\) (slope \(-0.965\)); fixed-\(q\) grids along \(N\sim q^{2}\) to \(16q^{2}\) through \(q=32\) give slopes \(-0.531,-0.499,-0.509,-0.496\) and, along \(q\) at \(N=1024\) up to \(q=64\), \(D\le0.1351\) with exponent \(0.093\) in \(q\) (numerical, on the reduced pencil, whose spectrum agrees with the full charge to \(1.6\times10^{-12}\) and whose medians agree to ratios \(1.003\) and \(0.978\)); the signature level \(U_2<0.05\) holds at all tested points with \(N\ge16q^{2}\) and fails at exactly the two smallest-\(N\) points \((q,N)=(4,4q^{2})\) and \((4,8q^{2})\), with values \(0.0859\) and \(0.0549\) (numerical). Outside the matched-scale class the violation stays \(O(1)\): per-copy variance scales \((1,1.6)\) on the same coincident geometry give \(D=0.4147,0.4113,0.3946\) at \(N=120,240,480\) and \(U_2=0.2226,0.2126,0.2003\), with slopes \(-0.036\) and \(-0.076\); in the block-diagonal class with independent per-copy momenta, equal scales decay with slope \(-0.448\) while scales \((1,1.6)\) hold slope \(-0.090\) and \(D\ge0.242\) at \(N=480\), a.s.-equal copies sitting at \(D=0\) exactly; and the Gram concentration defect of the edge rows decays (slope \(-0.302\)) for matched iid data yet stays at \(0.8070,0.7732,0.7908\) (slope \(-0.015\)) for a lognormal scale mixture of coefficient of variation \(0.4\). Between the two conditions of the exact \(q=2\) criterion, only the norm equality has leading-order teeth: at matched iid scales \(|\alpha|/\|w_\perp\|\) decays as \(N^{-1/2}\) (slope \(-0.527\)), the signature excess as \(1/N\) (slope \(-0.901\)), while the distance to exact tiling decays only as \(N^{-1/2}\) and never reaches the tiling level (minimum \(0.054\), slope \(-0.436\)), so the \(\operatorname{Im}\alpha\) condition fails below leading order, at the level of exact spectra only (numerical). These are leading-order state-realization statements for the rank-one edge-datum family of coincident copies, numerical at every rate quoted and exact only for the factorization, the pencil reduction and the \(q=2\) criterion, inside the transplanted rule with its single-dominant-diagram hypothesis at leading semiclassical order and its diagonal-cut convention; they bound which of the tested Gaussian, tempered and mixture ensembles realize copy-invariance at leading order, they do not supply the criterion or the negation for general \(q\), general states or the two-sided reading of the \(\pm\) pairs, they do not fix the selection rule itself, and they close nothing in Problem~G.
```

## What is not established (and must not be asserted from this package)

- The criterion/negation is **not closed for general q**: Lemma 2 is exact only at q=2; the insert says
  so.
- All rates, windows and levels are **numerical within the tested ensembles** (iid complex-Gaussian
  Hermitian momenta, fixed coincident cap geometry, matched scales unless stated; the tempered,
  block-diagonal, correlated and lognormal-mixture classes as tested). No proof of the concentration /
  rank-reduction statements beyond tested sizes; the necessity direction of the Gram-concentration
  criterion is not established (only the concentration-consistency direction tested).
- Growth beyond q = O(N^{1/2}) untested; q>64 dense regime untested (Frenkel 2311.10131 fixed-q validity
  respected by every claim).
- The **two-sided reading of the ± pairs**, mixed multiplicities / q_f growth, and frame-averaged or
  minimised entropy are untouched (the 076 closer caveat carries).
- Nothing here derives the block-cut selection rule itself, the (H1') lift hypothesis, or any of Problem
  G's missing steps (i)-(iv); G stays OPEN with its current labels; no re-labeling is proposed.
- The relation from "the charge ensemble tiles to leading order for generic matched-scale ensembles" to
  the actual NAMCG ensemble's state-selection mechanism is **not bridged**.

## Decisions Taken

1. **Zero `\cite`/`\ref`/`\eqref` in the insert** (076 review-r2 ruling): cross-references are
   descriptive phrases matching established paragraph headers ("the selection-rule paragraph above",
   "the Row length paragraph"). Rejected: `\ref`-based anchors (would add labels to a paragraph that
   needs none and enlarge the merge surface).
2. **Anchor choice:** unique line-start long-form Vacuum-term line at L3169 (076 precedent), not the
   076-closer sentence as anchor text — the closer tail "they close nothing in Problem~G." occurs 4× in
   appH (073-076 closers) and cannot anchor an edit; the long Vacuum form occurs exactly once.
3. **s2b kept FAIL as the finding carrier** with the corrected claim "U_2<0.05 holds at all tested
   points with N≥16q²; fails only at (q,N)=(4,4q²),(4,8q²)"; the threshold was NOT loosened. Rejected:
   retuning the 0.05 level to manufacture a pass (would hide the finite-N structure the finding records).
4. **Insert quotes s2b only through the corrected U_2 statement**; no D-level claim from s2b (its own D
   threshold is D<0.5, not the s2(b) 0.25 level).
5. **Header** "State realization of copy-invariant momenta at leading semiclassical order." verified
   absent from the manuscript (0 occurrences) and unique.
6. **ASCII-only values as verbatim triples/ranges** (e.g. "between 0.7865 and 0.8137") instead of
   en-dash ranges; all numbers verbatim from shipped outs (rounding disclosure 10).
7. **Single-paragraph insert** (no paragraph split): one scope clause, one closer, minimal text — the
   package is one contiguous bounded statement.
8. Rounding to two significant figures for the three deviations (disclosure 10) to avoid implying
   precision of the random seeds; rejected: verbatim 2.31e-14 (keeps text honest but longer; no claim
   turns on it).

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step is derived; the package is bounded
PROGRAMME-CONDITIONAL evidence with two exact sub-lemmas (q=2 scope) and pinned numerical negations.

## Status-label recommendation

Derived from live sources: ch17 full-GR criterion requires A, B, C, D1, E, F, G-derived, N (H, I, J
optional within stated scopes); Appendix H G labels re-quoted above (OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL). **Affected labels: none** — no changes proposed, and none warranted by this
package.

## Author decision needed

None. (No core change, no scope change, no label change is proposed or required to integrate the insert.)

## Remaining open step

To close G.selrule-copyinv as a criterion/negation theorem: (a) the exact mult-q tiling criterion for
general q (beyond the q=2 coefficient mechanism); (b) proof-level statements of the pencil-reduction
universality and Gram-concentration bounds beyond tested ensembles/grids (incl. necessity); (c) growth
beyond q = O(N^{1/2}); (d) extension to the two-sided ± reading and mixed multiplicities, and the bridge
to the NAMCG ensemble's state-selection (and then the frame-averaged entropy). Problem G's own missing
steps (i)-(iv) are untouched by this package.

## Special instructions for the gatekeeper

- **Re-run commands** (repo root, `-I`): every row of the evidence map; expected exits 0 PASS for
  s1/s2/s3/s4b/s5/s6/debug_conventions/normalize_insert/simulate_apply_077, and **exit 1 FAIL for
  s2b_qwindow — by design**, it is the recorded finding C11 carrier; do NOT "fix" it and never present
  its U_2 result as passing. `debug_s5_lemma1.py` exits 0 but is a historical bug record, not evidence.
- **Reproduce the byte contract**: `python -I proposals/077-g-selrule-copyinv/simulate_apply_077.py`
  must print PRE 707434/94b39393bdf8/3818/0, POST **712623 B / sha 789c668f0b4a... / CRLF 3820 /
  bareLF 0 / delta +5189 B / +2 CRLF**, body line 3169, anchor line 3171, `ALL ASSERTS PASS` —
  provided the tree is still at the PRE pins (the integrator must re-pin if another chain integrated
  first; the anchor is a content string, robust to unrelated line moves, but line numbers in this
  proposal refer to the PRE tree at 1cdca82).
- **Verify every number in the insert against the shipped `.out` files**; note the three roundings
  (disclosure 10) and the T_2-column-excess convention (disclosure 7) before flagging mismatches.
- Do not treat the four pre-existing "close nothing in Problem~G" closer occurrences as duplicates; this
  insert adds a fifth (established idiom).
- The `r3a` out's "(b) N=400" header is a reporting artifact of that historical run (disclosure 2).
- Assert the hygiene scans yourself (ASCII, 1 content line + terminal CRLF, zero `$ [ ] \ref \eqref
  \cite \label`, zero forbidden words, single `\emph`).
- Scope limits to enforce in review: no closure language for Problem G anywhere; the insert's q>2 caveat
  must survive integration.

## Provenance

Source reading: **digest + targeted reads** (never read appH whole; no repo file >150 KB read whole;
digest head 1cdca82, appH digest hash matched live pins). All writes confined to
`proposals/077-g-selrule-copyinv/`. No git write command was run. **No injection occurrences this
session** (no "[handback-send-enforce]"-class fake user turns; no SubagentHandback demand observed; the
referenced tool does not exist and would not be called).
