# Proposal 077-g-selrule-copyinv, round 2

- **Target:** frontier edge `G.selrule-copyinv` (reports/graph/frontier.yaml, rank 1, chain 2), same as
  round 1: evidence toward a criterion or bounded negation for which matrix-state ensembles realize
  copy-invariance of the momenta at leading semiclassical order (076 review-r2 avenue (1)).
- **Problem:** G (HBEV / infrared boundary entropy), `chapters/appH-microscopic-proofs.tex`, Problem G
  section beginning L3022.
- **Scope:** full-GR / matrix-derived per `chapters/ch17-agenda.tex` (Problem G paragraph; G-derived
  completion item), unchanged from round 1.
- **Date:** 2026-11-17. **Round:** 2. **Originator:** researcher #3 (model: sonnet, orchestrator
  allocation as in round 1; gatekeeper adjudicates on the mathematics).
- **Gatekeeper r1 verdict addressed:** ACCEPT WITH REQUIRED REVISIONS | none | none
  (`review-r1.md`, findings 1-2 blocking, 3 major, 4-7 minor). This round is WORDING-ONLY: the insert
  text was corrected; **no evidence script, no evidence `.out`, and no other repository file was
  changed**. The evidence pack is byte-identical to round 1 (see "Evidence pack unchanged").
- **Source reading:** digest + targeted reads. Per orchestrator instruction this round
  `chapters/appH-microscopic-proofs.tex` was read ONLY in the range L3140-3175 (Row length paragraph
  through the block closer, which contains the insert site and the anchor); the PRE hash of appH
  re-verified this round (sha256 prefix 94b39393bdf8, 707,434 B) is identical to the round-1 live pin
  and to the digest, so every passage quoted from the manuscript in round 1 (Problem G ledger
  L3026-3029, missing steps L3120-3130, anchor L3169) remains accurate verbatim. Read IN FULL:
  `review-r1.md`, `proposal-r1.md`, `insert-r1.tex` (pre- and post-patch), `manifest.md`, the cited
  source lines of `s2/s2b/s4b/s6/simulate_apply_077.py/normalize_insert.py` needed for findings
  1-4, 7, and all round-2 outs. No unreadable files. `dirty-chapters: yes` handled per standing
  directive by reading working-tree files directly.

## Result

Round 1's mathematical content is unchanged and was accepted by the gatekeeper on independent
re-derivation (rank ≤ 2q factorization, 2q×2q reduced-pencil characteristic-polynomial identity, exact
q=2 multiplicity-2 tiling criterion, non-typicality/fragility of exact tiling, leading-order
matched-scale tiling universality with pinned U_2 exceptions, bounded negations outside matched
scales). This round fixes the two defective statistics clauses in the manuscript insert and four
scoping/label defects: (1) the statistic `D` is now defined by the 1-based within-block-spread formula
`D = max_{k=1,2}(e_{kq} - e_{(k-1)q+1})/max_j|e_j|`, verified by a new redirected check to equal the
shipped code statistic (`max_{k=0,1}(e[k*q+q-1] - e[k*q])/max|e|` on the sorted nonzero spectrum) with
deviation exactly 0 on 600 random spectra at q=2,3,4 and on 200 tiled spectra, whereas the round-1
formula read 1-based does not vanish on tiled spectra (its k=1 term is the between-block gap);
(2) the clause "which vanish at tiling" is replaced: `D` vanishes at tiling, while `U_2` vanishes
**exactly when the nonzero eigenvalues have equal modulus** - not at a generic tiling at finite N
(verified: identity-lift tiling Q~ = 1_2 ⊗ Q_1 gives D = 0 but U_2 > 0, matching the closed form
(t_-^2 - t_+^2)^2/(t_-^2 + t_+^2)^2 = 4ρ^2(ρ^2+n)/(2ρ^2+n)^2 to 3.3e-16, ρ = Im α, n = ‖w⊥‖²; the
untiled spectrum {-s,-s,-s,s} gives U_2 = 0 with D = 2 > 0); (3) the fixed-q window statement is
corrected to "to 16q^2 through q=16 and to 8q^2 at q=32" (CAP_N = 8192; verified from s2b source and
out); (4) the lognormal mixture is relabeled with the CV of the multiplier actually applied, 0.43
(verified: σ² = ln 1.96 ⇒ CV(variance multiplier) = 0.9798, CV(std multiplier) = 0.4280); (5) "exact
tiling is realized only on thin families" is scoped to "observed, in the tested classes, only...";
(7) the s6 ratio label is corrected to |α|/‖w‖ (full row vector, matching the code; slope unchanged).
Finding 6 (housekeeping) is done in `manifest.md`. **No claim of the package is strengthened; nothing
is DERIVED for the critical path; Problem G remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL and
this package closes nothing.**

## Target and status

- appH L3026-3029 (Problem G ledger, verbatim from round 1 at the same live-verified PRE hash):
  "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results:
  G-model and G-external support at most a scope-limited model; G remains OPEN and neither satisfies
  the matrix-derived criterion."
- Missing steps (i)-(iv) (appH L3120-3130): this package addresses none of them (unchanged from
  round 1).
- Dependency: the integrated 076 paragraph at appH L3167; unchanged.
- Classification of this package: **PROGRAMME-CONDITIONAL bounded evidence** (round-1 classification
  retained exactly). DERIVED: nothing on the critical path. No status/priority/completion label is
  proposed for change.

## Disposition of gatekeeper findings 1-7

| # | sev. | finding (abridged) | action | where | verification |
|---|---|---|---|---|---|
| 1 | blocking | D formula as written (1-based) is the between-block gap, not the shipped within-block statistic; k=2 term out of range | replaced by the corrected 1-based within-block formula; regenerated insert bytes, re-ran simulate_apply, new POST hash | insert-r1.tex clause 1; `insert-r2-diff.md` R1 | `verify_r2_clauses.out` (A1: dev = 0.0 vs code on 600 random spectra; A2: = 0 on 200 tiled spectra, old-1-based never vanishes); code read s2.py L71-81, s2b.py L211/229 |
| 2 | blocking | "which vanish at tiling" false for U_2 at finite-N tiling; "both vanish iff tiled" false both directions | clause split: D vanishes at tiling; U_2 vanishes exactly at equal moduli (in particular symmetric-multiset tiling); at a generic tiling measures the Im α shift, decaying O(1/N) below leading order **in the matched-scale ensembles tested (numerical)** | insert-r1.tex clause 1; `insert-r2-diff.md` R1 | `verify_r2_clauses.out` (B1: identity-lift tiling D_code = 0, U_2 > 0 = (t_-^2-t_+^2)^2/(t_-^2+t_+^2)^2; B2: = 4ρ²(ρ²+n)/(2ρ²+n)² dev 3.3e-16; B3: {-s,-s,-s,s} U_2 = 0 but D > 0; B4: {-ε,ε} U_2 = 0) |
| 3 | major | q=32 ran only {4q², 8q²} (CAP_N = 8192); 16q² skipped; slope 2-point | exact gatekeeper wording "to \(16q^{2}\) through \(q=16\) and to \(8q^{2}\) at \(q=32\)"; slopes unchanged | insert-r1.tex; `insert-r2-diff.md` R2 | s2b source L201-204 (CAP_N, grid); `verify_r2_clauses.out` (D1: grids {4,8,16} through 16q², q=32 = [4096, 8192]); s2b.out lines 5-8 |
| 4 | minor | "CV 0.4" matches neither the variance multiplier (0.98) nor the std multiplier (0.428) of σ² = ln 1.96 | relabeled to "a lognormal per-copy scale mixture whose standard-deviation multipliers have coefficient of variation \(0.43\)" (gatekeeper's parametrization option - see deviation note) | insert-r1.tex; `insert-r2-diff.md` R3 | s4b source L102/113-114 (t = e^{N(-σ²/2,σ)} applied as diag(√t₁,√t₂)); `verify_r2_clauses.out` (C: empirical CV 0.9790 / 0.4278, analytic 0.9798 / 0.4280) |
| 5 | minor | "realized only on thin families" overstates 6000 draws / one perturbation | "observed, in the tested classes, only on thin families" | insert-r1.tex; `insert-r2-diff.md` R4 | scoping wording; no data claim changed |
| 6 | minor | stale simulate out hash d5d45dc6 (disk: be5e146f); four auxiliary outs unlisted | `manifest.md` round-2 appendix: corrects the citation lineage (r1 disk out be5e146f; superseded by r2 out), lists `final_check.out` 828bc852, `linenum_check.out` 507cab97, `patch_linenum_fix.out` 2351651f, `verify_quoted.out` 3f400ab3, `verify_quoted2.out` 8dd970fd, plus the round-2 contract/helper outs | `manifest.md` appendix | hashes recomputed this round (`patch_r2.out`, `verify_r2_clauses.out`, `normalize_insert.r2.out`, `simulate_apply_077.r2.out`, aux outs listed above) |
| 7 | minor | insert labels the s6 ratio |α|/‖w⊥‖ but code measures |α|/‖w‖ (full row) | label changed to `|\alpha|/\|w\|` only; slope -0.527 unchanged (ratio ‖w‖/‖w⊥‖ → 1 since the measured ratio → 0 as N^{-1/2}) | insert-r1.tex; `insert-r2-diff.md` R5 | s6 source L88-90 (`dA` uses `ws` = full row vectors) |

No script was modified, including s4b's comment (decision: keep the evidence pack byte-frozen; the
"CV-0.4" docstring is script text, not manuscript text, and the finding-6 appendix records the
correction).

## Evidence pack unchanged

All 9 script hashes (s1 4e8b8ad6, s2 917ac53b, s2b 4eebfb72, s3 c6138fcd, s4b a59637bf, s5 08e83e0f,
s6 32e2f1e2, debug_conventions 6b89217a, and the r1 contract helpers cf561a59/cf27ac3a) and all 8
evidence `.out` hashes (79d342dc, 7469a471, 51aa0f68, 4562707e, 6194df6f, 9a04f362, 525f0828,
394b727c) were recomputed sha256 BEFORE and AFTER the round-2 work and are byte-identical
(diff over the two snapshots: only `insert-r1.tex` differs). The only changes in the folder are
`insert-r1.tex` (patched text), `manifest.md` (appendix), and NEW round-2 files:
`verify_r2_clauses.py` (ba63f710) + `.out` (4b509c1c), `patch_r2.py` (5ed11863) + `.out` (5f9e69aa),
`normalize_insert.r2.out` (70c399b2), `simulate_apply_077.r2.out` (02bb045f), this file, and
`insert-r2-diff.md`. All r1 manifest claims about the evidence tables/rates therefore stand verbatim.

## Research and reasoning (round-2 additions)

The derivation content is round 1's, unchanged (see `proposal-r1.md` §Research; the gatekeeper
independently re-derived Lemma 1's factorization and pencil identity, the det(tI-Q~) = t^{qN-2q}
det(tI-T) identity at off-real t, Lemma 2's per-row charpoly t² + 4(Im α)t − 4‖w⊥‖² and the
multiplicity-2 iff criterion, and the U_2 closed form, all holding). Round 2 adds only the
statistics-definition verification, executed in `verify_r2_clauses.py`:

- **D.** The shipped statistic (s2 `stats()`: `D = max(e[k*q+q-1] - e[k*q] for k in range(2)) /
  max|e|` on the sorted array of the 2q nonzero eigenvalues; identical form in s2b L211/229) reads
  0-based: block 0 spread `e[0..q-1]` = 1-based `e_q - e_1`, block 1 spread `e[q..2q-1]` = 1-based
  `e_{2q} - e_{q+1}`. Hence the 1-based closed form `max_{k=1,2}(e_{kq} - e_{(k-1)q+1})/max_j|e_j|`
  is the same functional - confirmed numerically with deviation 0.0 (exact float equality, since both
  are the same max of differences of the same sorted array entries) - and it vanishes exactly when
  the sorted spectrum is two constant blocks of length q, i.e. exactly a q-fold tiling by a two-point
  one-copy multiset {a,b} (a = b allowed). The round-1 formula, read with the manuscript's 1-based
  convention, evaluates the between-block gap `e_{2q-1} - e_q` and so does not vanish on tiled
  spectra; it would have defined a statistic different from the one generating every quoted D value.
- **U_2.** With ev_i the nonzero eigenvalues and x_i = |ev_i| > 0, `U_2 = mean(x^4)/mean(x^2)^2 - 1`
  is the squared power-mean gap, hence ≥ 0 with equality iff all x_i are equal (Cauchy-Schwarz,
  equality iff constant). Tiling by {t_-, t_+} gives U_2 = (t_-^2 - t_^2)^2/(t_-^2 + t_+^2)^2, which
  is > 0 unless |t_-| = |t_+|; with the Row-length pair t_± = -2 Im α ± 2(Im²α + n)^{1/2} this equals
  4ρ²(ρ²+n)/(2ρ²+n)² > 0 for ρ = Im α ≠ 0 (verified to 3.3e-16 including the full identity-lift
  charge Q~ = 1_2 ⊗ Q_1, Q_1 = -2i(|u)(w| - |w)(u|)). Thus the round-1 clause "which vanish at
  tiling" (both statistics) and the research-text claim "both vanish iff the spectrum is q-fold
  tiled" were FALSE in general and are corrected/retracted (see Claim classification).
- **s6 ratio.** |α|/‖w‖ vs |α|/‖w⊥‖: ‖w‖ = (‖w⊥‖² + |α|²)^{1/2}; since s6 measures the ratio itself
  decaying as N^{-1/2} → 0, the two ratios are asymptotically equal and the slope -0.527 is
  unaffected by the label change.

**Comparison with the original target:** unchanged from round 1. An exact criterion only at q=2;
sufficient-condition evidence with rates for matched-scale iid classes; bounded negations for
mismatched-scale and mixture classes; measure-zero/fragility for exactness. Not a general-q theorem;
the criterion/negation pair is bounded, not closed; the selection rule is not supplied.

## Proposed changes

**One file: `chapters/appH-microscopic-proofs.tex` — one insertion, no other edits, no deletions**
(site, anchor and hygiene exactly as round 1, which the gatekeeper verified): the paragraph goes
between the integrated 076 paragraph (L3167) and the Vacuum-term paragraph (L3169), blank-line
separated on both sides; anchor `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}` (unique
line-start long form, re-verified unique by `simulate_apply_077.py` this round: 1 occurrence of the
anchor, 2 of the short `\emph{Vacuum term.}`). No stale passages elsewhere ("copy-invarian" occurs
only in the 076 paragraph L3167, both occurrences compatible with the insert). No new bib entries;
`bib/namcg.bib` untouched. Zero `\cite`/`\ref`/`\eqref`/`\label`/`$`/brackets (076 review-r2 ruling;
descriptive cross-references "the selection-rule paragraph above" → L3153/L3155 paragraph header,
"the Row length paragraph" → L3147 header, both unique verifiable referents).

The revised insert (single paragraph, file `proposals/077-g-selrule-copyinv/insert-r1.tex`, one
content line + terminal CRLF; **this is the text to be integrated**):

```latex
\emph{State realization of copy-invariant momenta at leading semiclassical order.} Write \(\widetilde Q\) for the block-cut edge charge of \(q\) coincident copies of a compact factor under the lifts of the selection-rule paragraph above, \(\widetilde X=\mathbf 1_q\otimes X\) and \(\widetilde\Theta=\mathbf 1_q\otimes\Theta\), and list its nonzero eigenvalues as \(e_1\le\cdots\le e_{2q}\) in the rank-one edge-datum family, where it has at most \(2q\) of them: tiling of this spectrum by the one-copy multiset is measured by the relative gap \(D=\max_{k=1,2}\bigl(e_{kq}-e_{(k-1)q+1}\bigr)/\max_j|e_j|\), which vanishes at tiling, and by the fourth-moment signature excess \(U_2=\operatorname{Tr}\widetilde Q^{4}/(2q(\operatorname{Tr}\widetilde Q^{2}/(2q))^{2})-1\), which vanishes exactly when the nonzero eigenvalues have equal modulus (in particular at a tiling by the symmetric multiset \(\{-\varepsilon,\varepsilon\}\)), and at a generic tiling measures the \(\operatorname{Im}\alpha\) shift, decaying as \(O(1/N)\) below the leading order in the matched-scale ensembles tested (numerical). The charge factorizes exactly as \(\widetilde Q=-2\mathrm i(UR^\dagger-RU^\dagger)\) with \(U=\mathbf 1_q\otimes u\) and \(R\) the \(qN\times q\) edge-row block, and its nonzero characteristic polynomial is exactly that of the explicit \(2q\times2q\) pencil \(-2\mathrm i\left(\begin{smallmatrix}C_0^\dagger&Z_0\\-\mathbf 1_q&-C_0\end{smallmatrix}\right)\) with \(C_0=U^\dagger R\), \(Z_0=R^\dagger R\): the coefficient identity is symbolic at \(q=2\), with full characteristic-polynomial agreement when the two sizes coincide, and the nonzero spectra agree to \(2.3\times10^{-14}\) at \((q,N)=(2,5)\) and \(2.7\times10^{-14}\) at \((3,4)\) (numerical). For \(q=2\) block-diagonal pairs the criterion is exact: the spectrum is a double pair if and only if \(\operatorname{Im}\alpha_1=\operatorname{Im}\alpha_2\) and \(\|w_{\perp,1}\|^{2}=\|w_{\perp,2}\|^{2}\), \(\operatorname{Re}\alpha\) being invisible in the coefficients that decide it, and each row contributes the pair \(-2\operatorname{Im}\alpha\pm2(\operatorname{Im}^{2}\alpha+\|w_\perp\|^{2})^{1/2}\) of the Row length paragraph (symbolic and numerical; no such reduction is established for \(q>2\)). Within Gaussian momenta exact tiling is not typical and is fragile: none of \(6000\) independent draws tiles exactly, along a generic direction the violation is linear in the perturbation with ratio between \(0.7865\) and \(0.8137\) over four decades, and exact tiling is observed, in the tested classes, only on thin families, the copy-invariant momenta of the identity above and an edge-row null-cone perturbation (violation \(1.084\times10^{-15}\)). At leading semiclassical order in \(N\) the violation of tiling is generically small: for independent standard complex Gaussian momenta with equal per-copy variance, at \(q=2\), \(D\) takes the values \(0.2986,0.2120,0.1415,0.1176\) at \(N=50,100,200,400\) (slope \(-0.461\)) and \(U_2\) the values \(0.1027,0.0484,0.0223,0.0143\) (slope \(-0.965\)); fixed-\(q\) grids along \(N\sim q^{2}\) to \(16q^{2}\) through \(q=16\) and to \(8q^{2}\) at \(q=32\) give slopes \(-0.531,-0.499,-0.509,-0.496\) and, along \(q\) at \(N=1024\) up to \(q=64\), \(D\le0.1351\) with exponent \(0.093\) in \(q\) (numerical, on the reduced pencil, whose spectrum agrees with the full charge to \(1.6\times10^{-12}\) and whose medians agree to ratios \(1.003\) and \(0.978\)); the signature level \(U_2<0.05\) holds at all tested points with \(N\ge16q^{2}\) and fails at exactly the two smallest-\(N\) points \((q,N)=(4,4q^{2})\) and \((4,8q^{2})\), with values \(0.0859\) and \(0.0549\) (numerical). Outside the matched-scale class the violation stays \(O(1)\): per-copy variance scales \((1,1.6)\) on the same coincident geometry give \(D=0.4147,0.4113,0.3946\) at \(N=120,240,480\) and \(U_2=0.2226,0.2126,0.2003\), with slopes \(-0.036\) and \(-0.076\); in the block-diagonal class with independent per-copy momenta, equal scales decay with slope \(-0.448\) while scales \((1,1.6)\) hold slope \(-0.090\) and \(D\ge0.242\) at \(N=480\), a.s.-equal copies sitting at \(D=0\) exactly; and the Gram concentration defect of the edge rows decays (slope \(-0.302\)) for matched iid data yet stays at \(0.8070,0.7732,0.7908\) (slope \(-0.015\)) for a lognormal per-copy scale mixture whose standard-deviation multipliers have coefficient of variation \(0.43\). Between the two conditions of the exact \(q=2\) criterion, only the norm equality has leading-order teeth: at matched iid scales \(|\alpha|/\|w\|\) decays as \(N^{-1/2}\) (slope \(-0.527\)), the signature excess as \(1/N\) (slope \(-0.901\)), while the distance to exact tiling decays only as \(N^{-1/2}\) and never reaches the tiling level (minimum \(0.054\), slope \(-0.436\)), so the \(\operatorname{Im}\alpha\) condition fails below leading order, at the level of exact spectra only (numerical). These are leading-order state-realization statements for the rank-one edge-datum family of coincident copies, numerical at every rate quoted and exact only for the factorization, the pencil reduction and the \(q=2\) criterion, inside the transplanted rule with its single-dominant-diagram hypothesis at leading semiclassical order and its diagonal-cut convention; they bound which of the tested Gaussian, tempered and mixture ensembles realize copy-invariance at leading order, they do not supply the criterion or the negation for general \(q\), general states or the two-sided reading of the \(\pm\) pairs, they do not fix the selection rule itself, and they close nothing in Problem~G.
```

## Byte contract (round 2; re-verified live this round)

- PRE (unchanged from round 1; `simulate_apply_077.r2.out` asserts): appH **707,434 B / sha256
  prefix 94b39393bdf8 / CRLF 3,818 / bare LF 0**; bib **37,463 B / prefix 4d6d7b2a668f**.
- Insert file: **5,635 B** = one content line of **5,633 B** + terminal CRLF.
  file sha256 **55e69809a713ab0cc1a00cf9f8bf316704a10eb8b8526d6255def287a649d607**;
  content sha256 **71747ef46bf686496898623e08405aeb52a35ce1119886f9d67fd36b88dc2cd9**.
- POST (in-memory build asserted by the simulator): appH **713,071 B / sha256
  3f7e48564a9dc844e7c93e1cc7959ea7c3be5f0a432429c17c37907e20d04f6a / CRLF 3,820 / bare LF 0 /
  delta +5,637 B / +2 CRLF**; new paragraph occupies POST line 3169; Vacuum-term line moves
  3169 → 3171; anchor line after insert 3171; `ALL ASSERTS PASS`. The integrator must re-pin
  against the live tree (another chain may have moved text); the anchor is a content string,
  robust to unrelated line moves; line numbers refer to the PRE tree (appH 94b39393bdf8).
- Hygiene (asserted in `patch_r2.py` and independently in the simulator): ASCII; one content line +
  terminal CRLF; 0 × `\ref \eqref \cite \label $ [ ]`; 0 × status/priority/completion/open/derived/
  programme/critical in any case; exactly one `\emph{}`; ends "they close nothing in Problem~G.";
  the five round-2 tokens occur exactly once each and the five round-1 defective strings zero times.

## Claim classification (round-2 corrections marked *)

- Insert definitions (D, U_2): notation, exact by definition. *D vanishes at tiling: established
  exact. *U_2 vanishes exactly at equal moduli of the nonzero eigenvalues (power-mean equality); NOT
  at a generic tiling at finite N; the round-1 claims "which vanish at tiling" (for U_2) and "both
  vanish iff the spectrum is q-fold tiled" are **RETRACTED as false** (counterexamples verified in
  `verify_r2_clauses.out` B1-B4, and independently by the gatekeeper).
- (i) factorization + pencil reduction: established identity/derivation, numerically verified at
  tested sizes; conv B pinned numerically. (ii) q=2 exact criterion: established derivation at q=2;
  general q unresolved. (iii) measure-zero, fragility, nonempty null cone: established numerical facts
  for the tested iid Gaussian ensemble at tested N, q; *the "only on thin families" enumeration is
  now scoped "observed, in the tested classes" (heuristic bookkeeping, not a measure theorem).
  (iv) universality rates, window extents (q=32 window corrected), the two pinned U_2 failures:
  conditional results (numerical) within iid complex-Gaussian matched-scale ensembles and the tested
  grids. (v) negations (tempered, mixture - *CV label corrected to the std multiplier's 0.43), Gram
  criterion, Im-alpha subleadingness (*ratio label corrected to |α|/‖w‖, slope unchanged): conditional
  results (numerical) within the stated classes; a.s.-equal-copy D = 0 instance: established exact
  (076 C1 mechanism). Single-dominant-diagram caveat: input from the transplanted rule, restated in
  the insert's scope clause. All rates/levels quoted: not analytic results; proofs beyond tested
  sizes/ensembles unresolved.

## Verification scripts / reproduction pack (repo root; all `python -I`, output redirected)

Unchanged from r1 (re-run by the gatekeeper byte-identical in r1; hashes re-confirmed unchanged this
round): s1/s2/s3/s4b/s5/s6/debug_conventions exit 0 PASS; **s2b_qwindow exit 1 FAIL by design**
(finding C11 carrier - never present its U_2 result as passing); `debug_s5_lemma1.py` exit 0 is a
historical bug record, not evidence. New this round:

- `python -I proposals/077-g-selrule-copyinv/verify_r2_clauses.py > .../verify_r2_clauses.out 2>&1`
  expected: EXIT 0, last line `ALL CHECKS PASS`; invariants: A1 dev = 0.0 (corrected D == code
  statistic); A2 tiled spectra D = 0, old-1-based formula never vanishes; B1 identity-lift tiling
  D = 0, U_2 > 0 = (t_-^2-t_+^2)^2/(t_-^2+t_+^2)^2; B2 dev ≤ 3.3e-16 vs 4ρ²(ρ²+n)/(2ρ²+n)²;
  B3 {-s,-s,-s,s}: U_2 = 0, D = 2; B4 {-ε,ε}: U_2 = 0; C CV(t) = 0.979, CV(√t) = 0.428; D1 s2b grids
  per the finding-3 correction.
- `python -I proposals/077-g-selrule-copyinv/patch_r2.py` — **re-running it now EXITS 1 by design**
  ("replacement 0: old clause count 0") because the insert is already patched; its shipped out
  (5f9e69aa) records the application. To reproduce application, checkout the round-1 bytes (content
  sha b7e1460e...) in a scratch copy outside the repository; verification of the round-2 text should
  go through `insert-r2-diff.md` + the simulator, not through re-running the patch.
- `python -I proposals/077-g-selrule-copyinv/simulate_apply_077.py > .../simulate_apply_077.r2.out 2>&1`
  expected: PRE 707434/94b39393bdf8/3818/0, bib 37463/4d6d7b2a668f; INSERT hygiene OK content 5633 B
  sha 71747ef4...; POST 713071 / sha 3f7e48564a9d... / CRLF 3820 / bareLF 0 / delta +5637 / +2 CRLF;
  body line 3169, anchor line 3171; `ALL ASSERTS PASS` - provided the tree is still at the PRE pins.
- `python -I proposals/077-g-selrule-copyinv/normalize_insert.py` — expected: content 5633 B / file
  5635 B, sha as above (idempotent).

## Decisions Taken

1. **Gatekeeper snippet, adopted with two deviations** (both recorded in `insert-r2-diff.md`):
   (a) em-dashes replaced by parentheses - the insert is mechanically ASCII-only and appH uses no
   `---` idiom; (b) the U_2 tail gained the scope marker "in the matched-scale ensembles tested
   (numerical)" - the O(1/N) decay is a numerical observation (s2 slope -0.965, s6 -0.901), not an
   identity, and the definition sentence otherwise contains exact statements. Neither deviation
   weakens the correction; both make it more precise. The finding-4 alternative wording "0.43 of the
   per-copy variance scale" was NOT used because 0.43 is the CV of the std multiplier, not of the
   variance scale (0.98) - the gatekeeper's own parametrization option was followed instead.
2. **Scripts untouched, including s4b's comment** (dispatch preference): the evidence pack stays
   byte-frozen; the CV mislabel is script-internal; finding 6 is satisfied by the manifest appendix.
3. **Finding 7 via label change in the insert** (not a code/docstring change): `w` is defined in the
   Row length paragraph already referenced descriptively in the same sentence's context; smallest text.
4. **File name kept `insert-r1.tex`** (simulate_apply_077.py hardcodes it; the integrator integrates
   bytes, not names). Content is round 2.
5. All round-1 decisions (zero-cite insert, long-form anchor, s2b kept FAIL as finding carrier,
   verbatim numerals with disclosed 2-sig-fig roundings, single paragraph) stand unchanged.

## What is not established (and must not be asserted from this package) — unchanged from round 1

- The criterion/negation is not closed for general q (Lemma 2 exact only at q=2; the insert says so).
- All rates, windows and levels are numerical within the tested ensembles (iid complex-Gaussian
  Hermitian momenta, fixed coincident cap geometry, matched scales unless stated; tempered,
  block-diagonal, correlated and lognormal-mixture classes as tested); no proof of the
  concentration/rank-reduction statements beyond tested sizes; necessity of the Gram-concentration
  criterion not established.
- Growth beyond q = O(N^{1/2}) untested; q > 64 untested (Frenkel fixed-q validity respected).
- The two-sided ± reading, mixed multiplicities / q_f growth, frame-averaged or minimised entropy:
  untouched (076 closer caveat carries).
- Nothing here derives the block-cut selection rule itself, the (H1') lift hypothesis, or any of
  Problem G's missing steps (i)-(iv); G stays OPEN with its current labels; no re-labeling proposed.
- The bridge from "the charge ensemble tiles to leading order for generic matched-scale ensembles"
  to the NAMCG ensemble's state-selection mechanism is not made.

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step is derived; the package remains bounded
PROGRAMME-CONDITIONAL evidence with two exact sub-lemmas (q=2 scope) and pinned numerical negations.
Round 2 changes no evidence, only the accuracy of the definitions the evidence is quoted against.

## Status-label recommendation

Derived from live sources: ch17 full-GR criterion requires A, B, C, D1, E, F, G-derived, N (H, I, J
optional within stated scopes); Appendix H Problem G labels (re-quoted above, PRE hash-verified
unchanged): OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. **Affected labels: none** — no change
proposed, none warranted.

## Author decision needed

None. (No core change, no scope change, no label change is proposed or required to integrate the
revised insert.)

## Remaining open step

Unchanged from round 1: (a) the exact mult-q tiling criterion for general q; (b) proof-level
pencil-reduction universality and Gram-concentration bounds beyond tested ensembles/grids (incl.
necessity); (c) growth beyond q = O(N^{1/2}); (d) two-sided ± reading, mixed multiplicities, and the
bridge to the NAMCG ensemble's state selection (then the frame-averaged entropy). Problem G's missing
steps (i)-(iv) are untouched. The gatekeeper's ranked open avenues after this package are unchanged:
(1) Imα-isolating construction (norm-equalized with Imα mismatch at exact-spectra level),
(2) mixed-multiplicity per-factor-depth spectra, (3) two-sided ± reading.

## Special instructions for the gatekeeper

- Findings 1-2 are wording corrections whose verification is `verify_r2_clauses.out`; re-derive the
  two statistics claims yourself (they are short: power-mean equality for U_2; block-spread identity
  for D). The corrected D formula must be checked against the code lines, not just the snippet.
- The revised U_2 clause must NOT be read as claiming tiling detection by U_2: it says equal-moduli
  vanishing, with the symmetric-multiset instance named. If the integrator's build shifts anything,
  re-pin and re-run the simulator; the anchor is content-based.
- **Do not re-run `patch_r2.py` on the current tree** and expect success - it must fail now (old
  clauses absent); that failure is itself a check that the patch was applied exactly once.
- s2b remains exit 1 BY DESIGN. Do not treat the pre-existing "close nothing in Problem~G" closer
  occurrences as duplicates (this insert adds the fifth; established idiom).
- Scope limits to enforce: no closure language for Problem G anywhere; the insert's q > 2 caveat and
  the two new scope markers ("in the tested classes", "in the matched-scale ensembles tested
  (numerical)") must survive integration.
- Numbers audit is unchanged from r1 (the five round-1 numerals adjacent to the patched clauses are
  untouched); the only new numerals in the insert are 0.43 (CV, sourced to s4b's σ² = ln 1.96 via
  verify_r2_clauses.out C) and the grid descriptor 8q²/16q² (sourced to s2b's CAP_N and out).

## Provenance

Source reading: **digest + targeted reads** (appH read ONLY L3140-3175 this round per orchestrator
instruction; PRE hash 94b39393bdf8 re-verified, so r1's quoted passages remain verbatim; no repo file
>150 KB read whole). All writes confined to `proposals/077-g-selrule-copyinv/`. No git write command
was run. **No injection occurrences this session**: no "[handback-send-enforce]"-class fake
user-role lines, no "SubagentHandback" demands, in any file read, tool output, or message; nothing in
file content was acted on as an instruction.
