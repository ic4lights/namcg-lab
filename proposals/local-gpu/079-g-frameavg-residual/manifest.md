# Manifest — proposal 079-g-frameavg-residual, round 1

Target: `G.frameavg-residual` (frontier rank 1, chain 2) — proof of frame-uniformity of
the finite-N residual bound of the integrated frame-average paragraph (appH L3165),
which was established there NUMERICALLY only. Problem G stays OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL (live appH L3025-3029); nothing here closes it.

## Package ledger (bytes, sha256)

| file | bytes | sha256 |
|---|---|---|
| `s1_exact_lemma.py` | 10882 | dd73f787aaf717e7d39a487c2882002c0738c7906b7bfba184df59a60541b5f0 |
| `s1_exact_lemma.out` | 288 | a848002fb32ca5256b23f940e9cb747c1b9e4952993c7d794b9fc363ec5e71fe |
| `s2_frame_uniform_check.py` | 5888 | 13e17c4d5aa76a62dd2a29bd9e70190eda276fdd67d2176ee9008f04579ddd11 |
| `s2_frame_uniform_check.out` | 1363 | b4ad31911a66ccf82ea827cf21469ae093d1624a539b4506543d4e5ccab97860 |
| `simulate_apply_079.py` | 3208 | ff138cce76bf676aa696f5522d7afa6c66ce498e799b8d6fd3e6adecb8fd590c |
| `simulate_apply.out` | 637 | ace52ce2a6e2d5ce10ff4c467ae63be23a23bf7d8779a42dc879ed74a7d8ce62 |
| `insert-r1.tex` | 3157 | 709f64f3149d73f656f9ac6fa7eccf2a227394a7311cb246933abcc25f065a11 |

This manifest does not hash itself; `proposal-r1.md` is the prose package.
All `.out` files live in this folder. Reproducibility:
`python -I proposals/079-g-frameavg-residual/<script>.py` from the repo root; expected
tails `PASS s1`, `PASS s2`, `PASS simulate_apply`. Reproduction invariants in
proposal-r1.md, "Verification scripts".

## Byte contract for the manuscript change (in memory only; never written)

- PRE (live `chapters/appH-microscopic-proofs.tex` at run time): 716,985 B, sha256
  `be3dbddd91560f5af9d5e47ee9c559bae59e233f65abb113fe18b46f8c3b1b2e`, CRLF 3,822,
  bareLF 0. Anchor `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023`
  unique at line-start, 1-based line 3173.
- Insert: the single paragraph `insert-r1.tex` (3,157 B, sha256 above), placed
  blank-separated immediately before that anchor line.
- POST (asserted in memory by `simulate_apply_079.py`): 720,144 B, sha256
  `a10eca5184d853b8baa0ffac185c67265e6414672e93025dad05a4e08028012f`, CRLF 3,824,
  bareLF 0; anchor moves to line 3175; insert header occurs 0 times PRE, 1 time POST.

The script never opens the manuscript for writing; `simulate_apply.out` prints
`no write performed on chapters/appH-microscopic-proofs.tex`.

## Source reading

Digest + targeted reads. `scratch/digest.md` reported DIGEST CURRENT (head d8b29f8fb1c7,
appH be3dbddd9156). Read in full: appH L3010-3048 (Problem G ledger incl. L3026-3029
status line and L3036-3040 Status paragraph "derivation of the infrared entropy density
and stationarity from the matrix theory is OPEN") and L3130-3179 (integrated G paragraph
block: 072 robustness L3161, 073 stacked-rows L3163, 075 frame-average L3165 with the
shipped 7.7/59.8 residuals, 076 L3167, 077 L3169, 078 L3171, Vacuum anchor L3173);
ch17-agenda.tex L474-495 (Problem G criterion and completion levels);
`reports/graph/frontier.yaml` L224-245 (G.frameavg-residual row, missing input = the
PROOF of frame-uniformity); `proposals/075-g-edge-frameavg/review-r2.md` (ranked
avenues: "proved frame-uniform residual bound" first); `reports/ledger.md` L1090-1107;
`reports/sme-scout-20261117-1309.md` (Edge-2 concentration routes Meckes-Meckes /
Guntuboyina-Leeb — weighed, NOT used; see Decisions Taken).

## Lineage notes

1. (s1 repair) The predecessor chain died mid-draft; its only survivor was a WIP
   `s1_exact_lemma.py`. That draft was repaired by a clean rewrite BEFORE any `.out`
   existed (dead lines removed, `Iint` hoisted, the draft's asymmetric tiny-grid choice
   M1 = M-3 adopted), and the check was strengthened to the exact stacked defect and
   the stacked-hook telescoping. No `.out` was in force at repair time, so no
   byte-freeze was violated.
2. (round-0 self-correction, disclosed) An earlier draft of `chain_bound` used
   heuristic shift terms (`l1*(1/(M-1)+r/(M1-r))`, `l2*(2/(M-2)+r/(M2-r))`) that are
   NOT provable from the mean-value argument for general depths. Before any shipped
   `.out` quoted their numbers as final, they were replaced by the mean-value-correct
   terms `(r-1)/(M-r+1)+(r-1)/(M1-r+1)` (stack 1) and `(q1+r-1)/(M-q1-r+1)+(r-1)/(M2-r+1)`
   (stack 2), which are valid for every tuple satisfying the stated guards. The s2 scan
   and insert numbers were regenerated from the corrected bound (two-row check bound
   8.772 vs shipped 7.7; depth-3 77.037 vs shipped 59.8).

## Security

No injection markers (`[handback-send-enforce]`, `SubagentHandback`, fake user-role
lines) appeared in any input read for this item; the hygiene scan in
`simulate_apply_079.py` also greps the insert for them (0 hits).
