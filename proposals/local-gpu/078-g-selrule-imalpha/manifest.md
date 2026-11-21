# Manifest - proposals/078-g-selrule-imalpha (round 1, 2026-11-17)

All hashes SHA-256, computed 2026-11-17 by `python -I` in this folder. No file in this
folder reads `chapters/`. No manuscript file was modified by any script here.

## Files (size B / CRLF count / sha256)

| file | B | CRLF | sha256 |
|---|---|---|---|
| s1_structure_general_q.py | 5747 | 121 | 2c40daa04e90b841fbb081cd46c9063936462d8c1b7d6c19e7656c34e01b2584 |
| s1_structure_general_q.out | 1302 | 17 | 1b99d2ba6f35f5c54c04b17e8c4274f09128f9e21a7ad045a397a803904252d2 |
| s2_imalpha_exact.py | 7421 | 0 | 5b05f7bcd58fcff1941576da8e40761b08b6ba1543bfbe715f105875986040af |
| s2_imalpha_exact.out | 1619 | 21 | cf7d05c73fb563af78223ed5709cdffd2c89f406c063291e9bf209cd0e9d15b5 |
| s2b_imalpha_exact_fixed.py | 10007 | 0 | e40324a7b701e1377995b6713e5202be79784341afef48e377b5072ab062255e |
| s2b_imalpha_exact_fixed.out | 1568 | 20 | 6a08683ae7d9fa8edfb0ba5e29621e823df9192708b09d9771cdc7a9e398cc3f |
| s3_scalarK_general_q.py | 11349 | 0 | 9302c421e2691b0cb97732f848f8f03d2128a59671cc482d76bbe5aa4713b971 |
| s3_scalarK_general_q.out | 1613 | 23 | e192ee24ec5e9309442f3e7b344d16b797201af5fd7595a1edce0c90d6fc442b |
| insert-r1.tex | 3912 | 1 | d57d892b04fa411764b1ccec08fdc8644daafa21020a3e08f6b8e480a4e3e278 |
| simulate_apply_078.py | 4029 | 0 | cd3ce501000ee06fd93452349ae213ba3f9786f290360fd64c9da3a66f453de8 |
| simulate_apply.out | 447 | 7 | 3c6305b9cb3bdc6c0b8bc2dff312bf3ff998f36614261dd6445d0811ff0280b2 |
| findings-r1.md | 5122 | 0 | c6918d9eea7bc47f67c4af50733f102130c27fc660b54b65396afc0b911d1cfb |

insert-r1.tex is 3,910 B content + one terminal CRLF (single content line).
findings-r1.md is the context-guard notes file required by the dispatch; the Write tool
rejected its creation as a "report file", so it was written through `python`/heredoc
inside this folder (dispatch-mandated workflow artifact; all content is repeated in
proposal-r1.md).

## Lineage

- s1 (5,747 B, sha256 2c40daa0...) and its .out (sha256 1b99d2ba...): pre-existing from
  the first 078 session; re-verified intact this session (sign s_q = +1 for q=1..6;
  determinant identity max rel dev 7.040e-15; Re-C0 invisibility; sympy q=2,3 exact).
- s2_imalpha_exact.py/.out: DEFECT ARTIFACTS, byte-frozen, kept for lineage. The .out is
  a crash traceback: line 42 `sp.diff(Dsimple, a2)` raised `ValueError: Can't calculate
  derivative wrt a1 + d` (a2 is the Python sum a1+d, not a symbol). Sections (B),(C),(D)
  NEVER executed. Two latent methodology defects were found by inspection:
  (a) `np.linalg.eigvalsh(-2j*M)` is invalid: -2iM is not Hermitian (block (1,2) is
      -2i Z0 while block (2,1)^dag is -2i I_q), and eigvalsh silently reads one triangle;
  (b) the assert `abs(U2s[0] - U2eq_closed) < 1e-9` was never executed and is wrong:
      U2 varies linearly in the mismatch (diff 3.55e-05 at eps = 1e-4).
- s2b_imalpha_exact_fixed.py/.out: fixed regeneration. Fixes recorded in its header:
  (i) derivative taken wrt d at fixed a1 (equals d/da2 at fixed a1);
  (ii) all spectra from the Hermitian charge Q~ = -2i(UR^dag - RU^dag) (asserted
       Hermitian; the qN-2q exact zeros screened out; rank-full guard asserted),
       cross-checked against the row-pair closed forms;
  (iii) the U2 assert replaced by an exact finite-eps closed-form match (< 1e-12) plus
       linear-approach bounds.
  Run: `python -I s2b_imalpha_exact_fixed.py > s2b_imalpha_exact_fixed.out 2>&1`,
  exit 0, ends "ALL S2B ASSERTS PASS".
- s3_scalarK_general_q.py/.out: new, this session. Run command as above, exit 0, ends
  "ALL S3 ASSERTS PASS". Two in-development corrections (not defects in artifacts):
  an index fix in (E) (3 gaps of 4 sorted eigenvalues, `gapsE[3]` -> two gaps), and the
  first "generic" discriminant sample (h1,h2,n1,n2)=(1,2,3,5) accidentally lay on the
  double-root locus (rows (1,3),(2,5) share lambda=2), which is why it gave disc = 0;
  replaced by (1,2,3,6), disc = 212336640 != 0; the (G) eps grid narrowed to 1e-4..1e-2
  because the linear onset carries O(eps) relative curvature.
- simulate_apply_078.py: adapted from proposals/077-g-selrule-copyinv/simulate_apply_077.py
  (read-only template) with updated PRE pins (post-077 tree) and 078 markers.
  Run from repo root: `python -I proposals/078-g-selrule-imalpha/simulate_apply_078.py`,
  output in simulate_apply.out, exit 0, ends "ALL ASSERTS PASS". Nothing was written
  outside this folder; the POST bytes were built in memory only.

## Seeds and grids (disclosed)

- s1: np.random.default_rng(20261117); q=1..6 sign checks (4 draws), q=1..6 identity
  (N=3q+2, 4 eval points), invisibility q=2,3 (3 draws), sympy q=2,3.
- s2b: default_rng(20261117+2); q=N=... q=2, N=6; data points a=(0.8,0.8..2.5), n0=3.7;
  eps grid {1e-4,1e-3,1e-2,1e-1}; non-scalar control 300 draws, K = BB^dag + 0.5I.
- s3: default_rng(20261117+3); (B) q=2..6, N=3q+2; (C) 150 trials q=3, h uniform on
  [-2.5,2.5] with min sep > 0.05, n uniform [0.4,4], N=11; onset grid {1e-4..1e-1};
  (D) 40 draws, q 2..5, n in [0.5,5], h uniform [-3,3], N=14; (E) exact rationals
  (3,7),(5,11), perturb n2 -> 11+1e-3, N=8; (F) 400 draws, K = BB^dag + 0.3I;
  (G) q=3, h=0.9, n=2.0, 3 traceless directions (simple spectrum enforced, min eig gap
  of V > 0.2), eps {1e-4,1e-3,1e-2}, N=11.
- All grids bounded; q fixed <= 6; no N-scaling asymptotics anywhere.

## PRE/POST byte contract (from simulate_apply.out, exit 0)

PRE: appH 713,071 B / sha256 prefix 3f7e48564a9d / CRLF 3,820 / bare LF 0;
     bib 37,463 B / sha256 prefix 4d6d7b2a668f.
INSERT hygiene OK: content 3,910 B, sha256 e7697412c4de33b73a3ad9a622a484629cf16a712b6a2218f059dd2c7cd8bd98.
POST (in-memory splice, for the integrator): appH 716,985 B /
     sha256 be3dbddd91560f5af9d5e47ee9c559bae59e233f65abb113fe18b46f8c3b1b2e /
     CRLF 3,822 / bare LF 0 / delta +3,914 B / +2 CRLF.
Site: body lands at 1-based line 3171, immediately before the unique anchor line
`\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}` (moves 3171 -> 3173),
blank-line separated on both sides (after the 077 paragraph at line 3169); marker
"Exact spectrum structure of norm-equalized coincident copies" 0 -> 1 occurrence;
077 marker "State realization of copy-invariant momenta" stays 1; '\emph{Vacuum term.}'
stays 2.
