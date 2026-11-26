# Manifest, proposals/098-g-scalar-p2-nonbridge-d3 (round 1, completed 2026-11-19)
SHA-256 computed from the live bytes on disk at completion. This manifest lists every file in the folder; no self-line.

## Live artifacts (the package as dispatched to the gatekeeper)
- `proposal-r1.md` 24,843 B sha256 264c1f0c67e61f895d5d35cdb69ba01241f1b7859b78d3396348976a42de0543 - the proposal (completed this round; prior session's truncation finished; two Result sentences corrected).
- `insert-r1.tex` 5,786 B sha256 af7c45b903f21dca4d0c8cd8d5b0fe275400fca0ad5e48e7d6bcd863d8aba4b5 - the manuscript insertion, one content line + terminal CRLF, pure ASCII.
- `gen_insert_098.py` 7,304 B sha256 3f7191b3da7367ded8a8a6082d84a2f37f61805e6491edcdf0a33d928ab3b67c - regeneration authority for insert-r1.tex (reproduces it byte-identically; all wording patches folded in).
- `verify_098.py` 9,148 B sha256 105c2412f26bb010fb6b2fef27690d4643eb9bad146f84f2207ad3be5ad16847 - numerical backing V0-V6, seed 20261119, read-only.
- `verify_098.out` 1,104 B sha256 a68279ededd6a3d76cf34dc88a6e4460b5b212943988e72c596011d690b0973b - shipped stdout of verify_098.py (final run; ends SUMMARY ALL PASS).
- `hygiene_098.py` 3,598 B sha256 b23f18dfa4a237d49cc075d1f8c677351d5d45121b07546e27eae7a31ac71aec - insert byte battery + appH PRE pins + PIN probes, read-only.
- `hygiene_098.out` 640 B sha256 2413185ef1960bdffc3d8daade2512b9563ad30a90daa04f727b0081407ad550 - shipped stdout (byte-unchanged through the round; ends SUMMARY ALL PASS).
- `simulate_apply_098.py` 2,614 B sha256 e15c573de2bcaa8624ec0bf3d7480f5ff873d61150728086cd1a26dd11037d13 - read-only in-memory splice and POST contract asserts.
- `simulate_apply_098.out` 134 B sha256 811335764cf2229addd269e0d9b9000d3922d3786bf07e64eb0a33080c29af22 - shipped stdout: POST 791,958 B sha256 711ed76dd238a995ed77c597d0717b5045cff53b4a0837c9b03469d7c172a3fb, CRLF 3,860, bareLF 0, SUMMARY ALL PASS.

## Used one-shot byte-surgery patch scripts (applied; re-run trips their uniqueness guards)
- `patch_098_v.py` 2,664 B sha256 70a6efbf857156ad11f9c235b30bb67890a783c492f234f558bdd037001ffe9e - prior session; replaced the V3 doubling block and the V4 block in verify_098.py (applied before this round).
- `patch_098_insert.py` 1,042 B sha256 65203a6b24c8b710f3dad1c73d29eaac9e55b7c5990ea8b6faeaba6929002270 - prior session (written, not run); run this round: folded the block-local D>3 clause into gen_insert_098.py.
- `patch_098b_insert.py` 1,877 B sha256 1b936f0e2dc24e607482213c21cb7df2b5ac329ded88ac4ed02e70668fb511d2 - this round: the three precision fixes (level-set scope; Vandermonde attribution; D=2 profile-class attribution) into gen_insert_098.py.
- `patch_098b_v.py` 3,520 B sha256 1c80b63a19194e3089bb331b7b7d345731e1ff3bde6602e1326d8d0c73e34a8d - this round: appended the V6 curve-tracing block to verify_098.py. Disclosed: this file's first version used a grid-band cluster count with an eps too small to sample the level band (V6 reported 1 cluster, chk FAIL); it was stripped from verify_098.py and this predictor-corrector version is what is applied.

## Byte contract (PRE/POST)
PRE appH (live, unmodified by this package): 786,170 B / sha256 691af35303cf46fadcb38b9e0f4a455a54e14fa65adf5e553c0e8839fdfc6e41 / CRLF 3,858 / bareLF 0 / noun idiom 23. Insert 5,786 B. POST (in simulate only): 791,958 B / sha256 711ed76dd238a995ed77c597d0717b5045cff53b4a0837c9b03469d7c172a3fb / CRLF 3,860 / bareLF 0 / idiom 24 / verb "closes nothing" 1 / "\emph{Vacuum term.}" 2 / new header 1. PIN: full 648-B 097 tail (offset 748,701) + CRLFCRLF + line-initial Vacuum header, compound unique; cut 749,353.

## Security note
No instruction-like embedded directives were encountered in any file or tool output processed by this package other than the usual YAML/manuscript prose; all such text was treated as data.
