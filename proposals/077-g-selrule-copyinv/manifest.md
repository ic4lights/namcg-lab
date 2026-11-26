# manifest.md — 077-g-selrule-copyinv (round 3, researcher #3, 2026-11-17)

Run all scripts from the repository root as `python -I proposals/077-g-selrule-copyinv/<script>`.
sha8 = first 8 hex of sha256 of the file AS SHIPPED in this folder (script/out hashes
computed 10:44 local; the debug_s5_lemma1.out hash was appended 10:49 after its run.
manifest.md and findings-r1.md are the two record files themselves; their hashes are not
listed here - self-referential by construction, and reported in the chat handback).

## Scripts (current, canonical)

| script | sha8 | what it checks | exit | verdict | re-run |
|---|---|---|---|---|---|
| s1_typicality_exact.py | 4e8b8ad6 | exact mult-q tiling is measure-zero (0/6000 iid draws, nu>0.1) and first-order fragile (nu ~ 0.81 t); edge-row null cone realizes tiling exactly (nu 1.084e-15) | 0 | PASS | python -I proposals/077-g-selrule-copyinv/s1_typicality_exact.py |
| s2_universality_N.py | 917ac53b | leading-order tiling universality in the iid Gaussian class: D~N^-1/2 (slopes -0.461), U_2-1~N^-1 (-0.965); copy-tempered (1,1.6) control holds O(1) violation (D 0.39-0.41, slope -0.036); fixed-q window D<0.25,U_2<0.05 at N=400, q in {2..10} | 0 | PASS (round-3b grid, see grid note below) | python -I proposals/077-g-selrule-copyinv/s2_universality_N.py |
| s2b_qwindow.py | 4eebfb72 | rank-factorized z-path equivalence (z0 1e-12, z1 ratios 1.003/0.978); extended fixed-q window N ~ q^2 up to q=32 (slopes ~ -0.5), along-q growth to q=64 at N=1024; U_2 levels printed per point | 1 | FAIL (GENUINE FINDING: U_2 = 0.0859 at (q=4,N=64) and 0.0549 at (q=4,N=128) exceed the 0.05 level; all N >= 16q^2 points pass; NOT a bug - threshold kept unchanged) | python -I proposals/077-g-selrule-copyinv/s2b_qwindow.py |
| s3_criterion_blockdiag.py | c6138fcd | block-diagonal (coherence-free) class: equal scales tau -> D decays (slope -0.448); tempered tau=(1,1.6) -> persistent O(1) D (slope -0.090); fully correlated copies -> D exactly 0; partial correlation interpolates | 0 | PASS | python -I proposals/077-g-selrule-copyinv/s3_criterion_blockdiag.py |
| s4b_gram_mixture_fixed.py | a59637bf | Gram-concentration criterion, corrected per-event defect statistic: iid defect decays (slope -0.302); CV-0.4 lognormal scale mixture stays > 0.5 (0.77-0.81, slope -0.015) | 0 | PASS | python -I proposals/077-g-selrule-copyinv/s4b_gram_mixture_fixed.py |
| s5_gram_and_q2_exact.py | 08e83e0f | exact lemmas: rank <= 2q factorization Q~ = -2i(U R^+ - R U^+), reduced 2q x 2q pencil T (symbolic charpoly identities + numeric 1e-14); Lemma 2 exact mult-2 criterion: Im(alpha_1)=Im(alpha_2) AND \|w_perp,1\|^2=\|w_perp,2\|^2, Re alpha invisible | 0 | PASS | python -I proposals/077-g-selrule-copyinv/s5_gram_and_q2_exact.py |
| s6_imalpha.py | 32e2f1e2 | Im-alpha column of the exact criterion is subleading: \|alpha\|/\|w_perp\| slope -0.527, rel-dev slope -0.903 (quadratic), D_exact 0.1317->0.0536 (slope -0.436, never at tiling level), U_2-1 slope -0.901 | 0 | PASS (round-3 window fix for the quadratic rel-dev decay; numbers unchanged by the edit - same seed, same table) | python -I proposals/077-g-selrule-copyinv/s6_imalpha.py |
| debug_conventions.py | 6b89217a | pins the R copy-block convention: conv B (R_xy = w_xy) exact 7.87e-14 vs conv A 3.55e+01; T real to 1.72e-15; nz spectrum match 4.44e-15; old-s5 block formula non-Hermitian 5.29e+00 | 0 | PASS (all pins hold) | python -I proposals/077-g-selrule-copyinv/debug_conventions.py |
| debug_s5_lemma1.py | 7dce9221 | HISTORICAL bug-record only: numeric twin of the OLD s5 (round 1) Qs/C0 conventions; both C0 variants fail against that OLD Qs (dev 0.37 / 2.07). NOT part of the current evidence chain (current s5 passes at 1e-14; debug_conventions Part 2 supersedes it) | 0 | record (numbers document the superseded construction, do not use as evidence) | python -I proposals/077-g-selrule-copyinv/debug_s5_lemma1.py |

## Support files

| file | sha8 | role |
|---|---|---|
| s1_typicality_exact.out | 79d342dc | current out (byte-equal to .det.out and to the superseded .out.new) |
| s2_universality_N.out | 7469a471 | round-3b PASS out (N=400, q<=10, 5 events in (b); (a)+(control) byte-equal to researcher #1 run) |
| s2_universality_N.out.r1-fail | 183ba3f8 | researcher #1 full-grid run (q<=16 dense): complete tables, failed only the sT mis-window |
| s2_universality_N.out.r3a-N200 | 93bf0513 | round-3a N=200 test run: D(q=10) 0.2639 vs 0.1869 at N=400 (~sqrt(2) shift) documenting why the (b) grid reduction had to restore N=400 |
| s2b_qwindow.out | 51aa0f68 | current out incl. per-point U_2 medians (the 0.0859/0.0549 identification) |
| s3_criterion_blockdiag.out | 4562707e | current out |
| s4_gram_and_mixtures.out | 70571366 | SUPERSEDED lineage: ends in Traceback (s4(b) pooled-median fragility; replaced by s4b) |
| s4_oldscript_repro.out | 70571366 | byte-identical rerun of the superseded s4 (documents that the old "PASS" claim was a crash) |
| s4b_gram_mixture_fixed.out | 6194df6f | current out |
| s5_gram_and_q2_exact.out | 9a04f362 | current out |
| s6_imalpha.out | 525f0828 | current out (post round-3 window fix; identical numbers to pre-fix run) |
| debug_conventions.out | 394b727c | convention pins output |
| debug_s5_lemma1.out | baa4c256 | bug-record output |
| s1_typicality_exact.det.out | 79d342dc | determinism re-run, BYTE-IDENTICAL to .out |
| s3_criterion_blockdiag.det.out | 4562707e | determinism re-run, BYTE-IDENTICAL to .out |
| s4b_gram_mixture_fixed.det.out | 6194df6f | determinism re-run, BYTE-IDENTICAL to .out |
| s5_gram_and_q2_exact.det.out | 9a04f362 | determinism re-run, BYTE-IDENTICAL to .out |
| s2_run_status.txt | 543c0f32 | appended exit codes. Note: the `S2 EXIT=1` line (10:26:25) is the ORCHESTRATOR's wrapper echo reacting to this researcher's taskkill of the orphaned round-2 s2 process (PID 20036), not a separate run |

## Lineage note (researcher #1 originals vs patches)

- Researcher #1 (2026-11-16 evening, round 1): s1, s2 (`.round1.bak` = pre-round-2 state),
  s3, s4 (superseded), s5 (`s5...round1.bak`), s2b (`s2b...round1.bak`). s4's out and
  s4_oldscript_repro.out both end in a Traceback; the old "PASS s4" outs were crashes.
- `patch_round2.py` (5137366c): asserted string patches of s2/s5/s2b for round 2
  (z0 eigvals vs eigvalsh misuse; s5 symbolic size; s2(b) qualitative claim rewrite).
- `patch_round2b.py` (67e043b0): round-2b patches producing the `.bak2` chain
  (s5 symbolic Qs construction, s2b eigvals bound, s6 (c) threshold 0.3 -> 0.01 + slopes).
- `s4b_gram_mixture_fixed.py`: replacement for s4(b) (per-event concentration defect
  statistic); s4 kept on disk as crash lineage only.
- Researcher #2 died twice on API context while the round-2 s2 rerun ran as orphan PID
  20036 (killed by researcher #3 at 10:26, 8.64 GB, 0 output bytes - stdout is
  block-buffered when redirected, so the 0-byte .out.new never indicated no progress;
  the dense qN=5200/6400 blocks at N=400, q>=13 were the memory blowup).
- Researcher #3 (round 3): `s2_universality_N.py.round2.bak` (2d2691c1) = state at kill;
  round-3 edits to s2: (i) line-buffered stdout; (ii) (b) assert mis-window fixed - the
  first `all(-0.9<s<-0.25 for s in (sD,sT))` applied the D-window to the U_2 slope whose
  own print expects ~-1 and which is separately bounded (-1.6,-0.5) in the SAME assert
  (the r1 run's sT=-0.965 failed only this mis-window); (iii) GRID: (b) N=400,q<=16 ->
  test at N=200 (r3a) -> final N=400, q-grid capped {2,3,4,5,6,8,10}, events 8->5
  (dense qN<=4000 blocks fit the memory budget; q=13,16 window coverage moved to s2b's
  z-path, distribution-equivalence verified there). s2b: `.bak3` (b3a02705) pre-report
  edit adding per-point U_2 medians to the (a) print (REPORTING ONLY, no threshold
  change). s6: `.bak3` (201af1b1) pre-fix state; rel-dev window (-0.8,-0.25) ->
  (-1.6,-0.5) because rel-dev = sqrt(1+x^2)-1 = x^2/2 is QUADRATIC in the
  \|alpha\|/\|w_perp\| ratio (measured slopes -0.527 and -0.903, i.e. slope ~ 2x); the
  quadratic window is the script's own O(1/N) physics, and a slope ~0 or ~-1/2 would
  still fail; data/thresholds otherwise untouched, numbers byte-unchanged after the fix.

## Grid note (s2)

Round-3b (b)-section runs N=400 with q in {2,3,4,5,6,8,10} and 5 events (was N=400,
q up to 16, 8 events). Sections (a) and (a-control) are UNCHANGED and byte-reproduce the
researcher #1 run. The r1 full q<=16 dense numbers are preserved in
`s2_universality_N.out.r1-fail` (D(q=16)=0.1994, U_2=0.0151) and the q>10 window is now
carried by s2b (N=1024, q<=64; N~q^2 window to q=32).

## Hygiene

`__pycache__` removed. `hashes_current.txt` (self-referential empty-hash artifact, the
076 review finding-1 phantom class) deleted after use. No manuscript files touched by
any researcher in this chain; all writes confined to this folder.

## Round-2 appendix (2026-11-17, proposal round 2, gatekeeper review-r1 findings 1-7; wording only)

Evidence UNCHANGED: all 9 script hashes and all evidence `.out` hashes above recomputed
before and after the round-2 work - byte-identical (determinism confirmed; the only
changed evidence-pack file is `insert-r1.tex`). `insert-r1.tex`: file sha8 3947273c ->
55e69809 (55e69809a713...), content 5,185 -> 5,633 B, content sha256 71747ef4...; the
five wording replacements are listed in `patch_r2.py` / `insert-r2-diff.md` (gatekeeper
findings 1-5 and 7; no script touched, s4b comment left as-is by decision).

New round-2 helpers: `verify_r2_clauses.py` (ba63f710) / `verify_r2_clauses.out`
(4b509c1c): checks the corrected 1-based D formula == shipped code statistic (dev 0),
the tiled-spectrum vanishing and the round-1 formula's off-by-one, the U_2 equal-moduli
identity and the closed form 4 rho^2(rho^2+n)/(2 rho^2+n)^2 (dev 3.3e-16), the {-s,-s,
-s,s} counterexample (U_2 = 0, D > 0), the s4b mixture CVs (variance multiplier 0.98,
std multiplier 0.428), and the s2b q=32 grid = {4096, 8192}; `patch_r2.py` (5ed11863) /
`patch_r2.out` (5f9e69aa): applies and re-verifies the patch + hygiene.
Contract re-run: `simulate_apply_077.r2.out` (02bb045f): PRE pins UNCHANGED (appH
707,434 / 94b39393bdf8 / CRLF 3818 / bareLF 0; bib 37,463 / 4d6d7b2a668f); POST 713,071 B /
sha256 3f7e48564a9dc844... / CRLF 3820 / bareLF 0 / delta +5,637 B / +2 CRLF; body line
3169, anchor line 3171; ALL ASSERTS PASS. `normalize_insert.r2.out` (70c399b2) is the
round-2 normalization (no-op: file already one line + terminal CRLF).

Auxiliary outs not in the r1 manifest (gatekeeper finding 6; housekeeping/reporting,
NOT part of the mathematical evidence chain): `final_check.out` (828bc852),
`linenum_check.out` (507cab97), `patch_linenum_fix.out` (2351651f), `verify_quoted.out`
(3f400ab3), `verify_quoted2.out` (8dd970fd). Stale citations corrected: the r1 proposal's
`simulate_apply_077.out` hash d5d45dc6 predates the 11:16 patch regeneration - the r1
on-disk file is `simulate_apply_077.out` (be5e146f); both r1 contract outs (be5e146f,
normalize_insert.out 0fdfdf1f) describe the ROUND-1 insert bytes and are superseded by
the .r2 outs for the round-2 insert.
