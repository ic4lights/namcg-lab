# Manifest - proposal 117-d1-state-measure-construction, round 1

Working tree at proposal time: branch `local/gpu`;
`chapters/appH-microscopic-proofs.tex` baseline sha1
`28f3a0d2401efc1c65b53a99a5968cdcb70fed7d`, size 834663 B (the item-116
integrated canonical POST). `python -I scripts/make_digest.py --check` printed
`DIGEST CURRENT` at task start (digest head 8b9ff393).

## Folder contents (sha1, size, role)

| file | sha1 | bytes | role |
|---|---|---|---|
| `proposal-r1.md` | `2ffe61497fefa51597f2381555f28983355ee3e4` | 30536 | the proposal (round 1) |
| `insert-d1-state-measure.tex` | `b514e44a19ee627f0aab4ac3d4f69bc052506154` | 4597 | PAYLOAD: one blank CRLF line + one paragraph line + CRLF; ASCII; no `\label`, no `\cite`; regenerable byte-identically |
| `gen_payload_117.py` | `15c8fdfa9e94adc6ac091c8c43b1dd703a5a3e9c` | 7544 | payload generator + byte scan + fragment-join absorb assertion |
| `out-gen-r117p.txt` | `f857858754132d615e2190b6de8e4bc7fb2d62e4` | 127 | generator run record: `bytes 4597 ... PAYLOAD SCAN OK` |
| `verify_r117.py` | `0a240ba72deb13ea739167a84d49aefbd24410e9` | 17965 | sympy/numpy verification pack, seed 117, 31 checks |
| `out-r117.txt` | `93e39fa192243effe67356d1205e13c24ba95a3d` | 2943 | recorded green run: `PASS 31 FAIL 0`, `ALL CHECKS DONE 117` |
| `cert-r117p.py` | `f1d27bb269400870851745af29474efed0e814c6` | 4931 | two-pass out-of-repo compile certificate (splices payload + amendment into a copy) |
| `out-cert-r117p.txt` | `e7a1aaf27d3f8001f9d74cf58ce0f948e9ee7b40` | 423 | certificate record: baseline/amended/POST lines, `rc1=0 rc2=0 errlines=0 outw=True undefrefs_pass2=0`, `CERT PASS` |
| `_scan_macro_join.py` | `91ccfb2caabd6d4519f7e43be032bc6fb3133513` | 1252 | macro-token audit of the payload (caught the `\proptoe` absorb bug) |

Note (payload revision): an earlier 4596-byte payload draft (`f028d8d5...`)
FAILED the compile certificate with `! Undefined control sequence` at
`l.1715` (fragment-join macro absorption, `\propto`+`e` -> `\proptoe`); the
generator was fixed (boundary space, three `\lvert...\rVert` -> `\lVert...\rVert`
delimiter corrections, durable join assertion) and the payload above
(`b514e44a...`, 4597 B) is the certificate-passing artifact. The superseded
draft was never integrated and exists nowhere in the tree.

## Manuscript anchor (Edit B) and amendment (Edit A)

- Anchor line (must occur exactly once; verified count 1 in the baseline):
  `\section{Problem E: signature}` - at byte offset 281406 of the baseline.
- Anchor pre-context (last bytes before it, byte-verified):
  `...h3-relate}; and Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg} remain assumed, so Problem~D remains OPEN and PROGRAMME-CONDITIONAL.\r\n`
  (no blank line between the 116 paragraph and the anchor).
- Edit A (stale clause in the integrated 116 paragraph; verified count 1 in
  the baseline): replace
  `no state of the matrix theory and no integration measure is constructed`
  by
  `no state of the matrix theory is constructed (the Euclidean Gibbs measure of the paragraph below is a Presentation-B probe measure, not a matrix-theory state)`
  (+87 bytes).
- Join convention (115 form, payload carries the leading separator and no
  trailing blank line): `data.replace(ANCHOR, PAYLOAD + CRLF + ANCHOR, 1)`.

## Expected integration arithmetic (recompute against the CURRENT tree)

- baseline appH: `28f3a0d2401efc1c65b53a99a5968cdcb70fed7d` / 834663
- after Edit A: `a38d4e293806a09f7fc5072a273ae49f62100590` / 834750 (+87)
- POST (after Edit B): `7e0546a425c16b55e30f2513a228efd836c120b8` / 839349
  (= 834750 + 4597 + 2), produced and compiled green (two passes, zero
  undefined references) by `cert-r117p.py` in an out-of-repo copy.

## Landing note for the integrator

Apply Edit A first, then Edit B, in the current tree (recount both anchor and
amendment strings against it before editing; if the tree has moved off
`28f3a0d2...`, recompute the arithmetic - the payload itself is unchanged).
Apply no other change to `appH-microscopic-proofs.tex`; no other file changes.
Then `python scripts/build_check.py` and `python scripts/make_digest.py`.
Expected diff: one in-line clause replacement + one inserted paragraph
(balanced blank line from the payload's leading CRLF).

No files outside this proposal folder were created or modified by this run.
