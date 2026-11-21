# manifest — 073-g-edge-rowshift (round 2)

Round 2: wording-only revision per review-r1.md finding 1; s1-s5 not re-run (math unchanged).

Digest state (round 1, historical): `python scripts/make_digest.py --check` -> `DIGEST CURRENT`;
compact digest, head eb8fc7d7713fd5a87a02fb7aeae75d5945088a42, tree-hash 46f71ab2676074dd,
chapters-hash 4917763564864af7, dirty-chapters: yes (the integrated, author-uncommitted 072
text - expected). appH digest hash prefix a41055028eb6 matches the live PRE pin.

Reproduction (round 1, historical record; `python -I` from the repository root, stdout
redirected, then `cmp`):

    cmp s1.out s1.repro.out  -> IDENTICAL
    cmp s2.out s2.repro.out  -> IDENTICAL
    cmp s3.out s3.repro.out  -> IDENTICAL
    cmp s4.out s4.repro.out  -> IDENTICAL
    cmp s5.out s5.repro.out  -> IDENTICAL
    simulate_apply.py re-run -> output byte-identical (deterministic)

Round 2: the gatekeeper independently re-ran all six commands (round 1 review, Checks A) with
byte-identical results; after the finding-1 insert wording fix, `simulate_apply.py` was re-run
and printed the PRE pins exactly (appH 695,658 B /
a41055028eb6a93e04d4ca509f335f8ca285ead761845137cd01aac7432550c4 / CRLF 3810 / bareLF 0;
bib 37,463 B / 4d6d7b2a668fdaa64663e624b3f296d833c3bbcaa06a74ec5012a7f494ce0de6 /
CRLF 1239 / bareLF 0); anchor assertions passed (script exit 0).

Byte contract (from the round-2 `simulate_apply.out`): appH PRE 695,658 B /
a41055028eb6a93e04d4ca509f335f8ca285ead761845137cd01aac7432550c4 / CRLF 3810 / bareLF 0;
appH POST 697,839 B / 437df96e4be9a5428840c42308fa770c5bc9c3e8aa39c0a03bab672d9e0f111c /
CRLF 3812 / bareLF 0 (round-1 POST 697,767 B / ff90a68aa93a... superseded by the corrected
insert); bib unchanged PRE = POST 37,463 B /
4d6d7b2a668fdaa64663e624b3f296d833c3bbcaa06a74ec5012a7f494ce0de6 / CRLF 1239 / bareLF 0.
Anchor counts live: `\emph{Vacuum term.}` x2 (never used), long form x1, line-start long x1.

Files (bytes / sha256), computed after finalization (round 2):

    insert-r1.tex                          2179  5722f69e6bd67ac99eeb7fa028e7b164c683c9d9325fe5cb28387a6f954d3c8a
    proposal-r1.md                        36021  20b723c4aad607f55453ad848381be11a82d59e101b8be586b6cf6910e1d6f6f
    review-r1.md                          19305  db16aef844d4c426bdeb5a26d08b121e87a45f02448a4174c6b82189cd69c0a7
    simulate_apply.py                      3975  0ee730257d7acfa6efe5543b391fec0b0d6a33fbb9201e0ae01125a03dbc208a
    simulate_apply.out                     1171  129298392aec1ad6ebab122781835b2e2acf8104165223c00c7948cb443f117b
    s1_moment_decomposition.py             5866  070a465212048c4a56e98a4a363f863ecd859aa83baa2ff8bbd0b47c281a8404
    s1.out                                 1236  5b978bd092e5e46d6428d8f9a9ceb0ff2503f06bcb16db13fbebfede1888d942
    s1.repro.out                           1236  5b978bd092e5e46d6428d8f9a9ceb0ff2503f06bcb16db13fbebfede1888d942
    s2_hook_content.py                     5538  748b5cf9c65aee73dd4f254438b04f59dddc63896209ca468f309048002cf80e
    s2.out                                  352  25270a2dffaf8810983ae518be9613e8ab5c37aef307caddc434bf51ec00d14d
    s2.repro.out                            352  25270a2dffaf8810983ae518be9613e8ab5c37aef307caddc434bf51ec00d14d
    s3_saddle_residual.py                  4455  c3859b761a9f1fa2ae645ffaf4a5aa14be3b0f07dfbf911e9ccf569bd4ae82fe
    s3.out                                 2777  8ed8ab308f3b70e5690f06f1119ef96eea56414098e9bd17f311a63792029ce1
    s3.repro.out                           2777  8ed8ab308f3b70e5690f06f1119ef96eea56414098e9bd17f311a63792029ce1
    s4_uniform_rowshift.py                 8298  cd1aec5c0b4ff9e037217dc7885bc1a5bd80af35e7f97ceed0b1953de814b501
    s4.out                                  700  c50c909c84eae4763d6c97133e9fdf6bf2527ec3b79db3ddaedeffa11ee5e4ee
    s4.repro.out                            700  c50c909c84eae4763d6c97133e9fdf6bf2527ec3b79db3ddaedeffa11ee5e4ee
    s5_scaling_and_breakdown.py            9825  c24c3de0fab4fb74b6134cf92121cc8150b8718dcb0dbffc1611f97b12eab849
    s5.out                                 4210  7c2075d2c5151dc9b409f28cf552b179599690663219d03e01312d216ebb897d
    s5.repro.out                           4210  7c2075d2c5151dc9b409f28cf552b179599690663219d03e01312d216ebb897d

No bib_additions.bib (no bibliography change proposed). insert-r1.tex is CRLF, ASCII-only,
one paragraph + terminating CRLF. proposal-r1.md includes the byte-frozen script hashes above;
re-hash it if the proposal text changes. The round-1 hashes of the three changed files were
insert-r1.tex 2107 / 622f862e43e1..., proposal-r1.md 35129 / 9d63b9b984c1..., and
simulate_apply.out 1171 / 6802e6aea747... (superseded by the round-2 values above).
