# manifest — 074-g-edge-uqstack (round 1, recovery write-up)

Recovery round: scripts/outputs on disk are the prior researcher's; this round verified them
(all re-run fresh, all byte-identical), attributed the x=0 fix, and wrote insert-r1.tex,
proposal-r1.md, simulate_apply.py/.out and this manifest. No script was edited.

Digest state: `scratch/digest.md` read in full this round; compact digest, head
eb8fc7d7713fd5a87a02fb7aeae75d5945088a42, tree-hash 46f71ab2676074dd, chapters-hash
35e0794d296de6b7, appH file-hash prefix 437df96e4be9 - matches the live PRE pin measured this
round (697,839 B / 437df96e...); dirty-chapters: yes (the integrated, author-uncommitted 072+073
text - expected).

x=0 verification outcome: the fix ("accumulation to start at x=0") is in
`s3_uq_boxmin.py` only (`make_delta`, F-prefix loop starting at `j = 0`, comment
"includes x = 0"); `s1`/`s2` use direct double sums and were never prefix-based. The shipped
`s1.out`, `s2.out`, `s3.out` are byte-identical to fresh re-runs of the current scripts
(commands and cmp results in proposal-r1.md, Verification scripts section), so all shipped
outputs POST-DATE the fix; `s3` additionally self-checks prefix-vs-direct agreement (1e-10) at
diagonal and off-diagonal points.

Known cosmetic artifact (documented, NOT edited; no assertion and no cited number uses it):
the s3.out section-2 column headed "corner/N" prints corner/N^2 (double division at the print
of sec2 rows; correct corner/N at q=1,C=1 is 0.521219 = printed 0.001303 x 400, approx
0.996*Lambda(1/2,1/2)). Scripts left byte-frozen.

Reproduction (this round; `python -I` from the repository root, stdout redirected, exit 0 each,
then `cmp`):

    cmp s1.out fresh-run   -> IDENTICAL
    cmp s2.out fresh-run   -> IDENTICAL
    cmp s3.out fresh-run   -> IDENTICAL
    cmp r{i}.out fresh-run and r{i}.repro.out fresh-run   -> IDENTICAL for i=1..5
    cmp r{i}.out r{i}.repro.out                           -> IDENTICAL for i=1..5
    r{i}*.py and r{i}.out == 073's s{i}*.py and s{i}.out  -> IDENTICAL (sha256 table below
        matches 073's manifest hashes; r1 070a4652..., r2 748b5cf9..., r3 c3859b76...,
        r4 cd1aec5c..., r5 c24c3de0...)
    simulate_apply.py re-run x2 -> output byte-identical (deterministic)

Byte contract (from `simulate_apply.out`, run this round; live re-verification by the integrator
is mandatory). Anchor: line-start long form CRLF +
`\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}`; live anchor counts: short
`\emph{Vacuum term.}` x2, long x1, line-start long x1; new header
`\emph{Extension of the fixed-frame excess to stacked-row diagrams.}` x0 pre, x1 post.
appH PRE 697,839 B / 437df96e4be9a5428840c42308fa770c5bc9c3e8aa39c0a03bab672d9e0f111c /
CRLF 3812 / bareLF 0. appH POST (expected on integration, same tree) 700,825 B /
50f12c8131819f513ff37d5149529ba616063578b04510891a6b7f1d43b8f25e / CRLF 3814 / bareLF 0;
delta +2,986 B (= insert body 2,982 + 4), CRLF +2, bareLF 0. bib unchanged PRE = POST =
37,463 B / 4d6d7b2a668fdaa64663e624b3f296d833c3bbcaa06a74ec5012a7f494ce0de6 / CRLF 1239 /
bareLF 0. Insert `insert-r1.tex`: single ASCII line + one terminating CRLF (bareLF 0).

Files (bytes / sha256), computed after finalization (this manifest excludes itself):

    insert-r1.tex                          2984  9eae941be5ba496bde7273dd539e0bddae51e8ee080afdef624c41bad38014e3
    proposal-r1.md                        39362  59fef2e2b4c007438826656066f11b707bd51c1a878b6794cdf1e54d46bebdd7
    r1.out                                 1236  5b978bd092e5e46d6428d8f9a9ceb0ff2503f06bcb16db13fbebfede1888d942
    r1.repro.out                           1236  5b978bd092e5e46d6428d8f9a9ceb0ff2503f06bcb16db13fbebfede1888d942
    r1_moment_decomposition.py             5866  070a465212048c4a56e98a4a363f863ecd859aa83baa2ff8bbd0b47c281a8404
    r2.out                                  352  25270a2dffaf8810983ae518be9613e8ab5c37aef307caddc434bf51ec00d14d
    r2.repro.out                            352  25270a2dffaf8810983ae518be9613e8ab5c37aef307caddc434bf51ec00d14d
    r2_hook_content.py                     5538  748b5cf9c65aee73dd4f254438b04f59dddc63896209ca468f309048002cf80e
    r3.out                                 2777  8ed8ab308f3b70e5690f06f1119ef96eea56414098e9bd17f311a63792029ce1
    r3.repro.out                           2777  8ed8ab308f3b70e5690f06f1119ef96eea56414098e9bd17f311a63792029ce1
    r3_saddle_residual.py                  4455  c3859b761a9f1fa2ae645ffaf4a5aa14be3b0f07dfbf911e9ccf569bd4ae82fe
    r4.out                                  700  c50c909c84eae4763d6c97133e9fdf6bf2527ec3b79db3ddaedeffa11ee5e4ee
    r4.repro.out                            700  c50c909c84eae4763d6c97133e9fdf6bf2527ec3b79db3ddaedeffa11ee5e4ee
    r4_uniform_rowshift.py                 8298  cd1aec5c0b4ff9e037217dc7885bc1a5bd80af35e7f97ceed0b1953de814b501
    r5.out                                 4210  7c2075d2c5151dc9b409f28cf552b179599690663219d03e01312d216ebb897d
    r5.repro.out                           4210  7c2075d2c5151dc9b409f28cf552b179599690663219d03e01312d216ebb897d
    r5_scaling_and_breakdown.py            9825  c24c3de0fab4fb74b6134cf92121cc8150b8718dcb0dbffc1611f97b12eab849
    s1.out                                  328  a0f5fee2ba50d14bfb5887204ddc237d18e26a675496847f3a6a308ca7d58ff2
    s1_uq_closedform.py                    5735  10b8c4be35a324d4a237986a811d4041bd72a4e0ab73c5742d0d8515ab292b07
    s2.out                                 1439  81588edbcc7927d2b421b3695cda211ecc310ee1dc91838723a955c2acb71195
    s2_uq_scaling.py                       3774  d9fce04dc1035e0f1c2623abc7fb72b7d5d33511be258b0a1a299244b41aef7e
    s3.out                                 2438  2243f6420e52ae5b612d2818f3bc8db3fcea00585dfb397a44219b5003440534
    s3_uq_boxmin.py                        6210  7990ae853a039eda8f8f9a048d29406465bfad3606cb755b464a2b75748f9cd0
    simulate_apply.py                      3967  370e21b031422726d3583c1ebcc366c905486906fda6118340d38328c7b6c4f5
    simulate_apply.out                     1171  2e3df8061548014aa6eab6fd81afaf89693cd7fb28af23b5a3a2d0f258157ba1

No bib_additions.bib (no bibliography change proposed). proposal-r1.md contains the insert
paragraph fenced byte-equal to insert-r1.tex's single line (verified programmatically); re-hash
this manifest's entries if any file changes (proposal-r1.md hash is the post-splice value).
