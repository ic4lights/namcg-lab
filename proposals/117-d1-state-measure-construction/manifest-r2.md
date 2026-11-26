# Manifest - proposal 117-d1-state-measure-construction, round 2

SUPERSEDES `manifest.md` (round 1, sha1 `7f73f7922ef57e43fdeecd0a0b7b5682fd89cbb8`,
4346 B), which is kept untouched as the round-1 audit record.

Working tree at proposal time: branch `local/gpu`;
`chapters/appH-microscopic-proofs.tex` baseline sha1
`28f3a0d2401efc1c65b53a99a5968cdcb70fed7d`, size 834663 B (the item-116
integrated canonical POST); re-verified at round-2 artifact creation (also:
Edit A string count 1; anchor `\section{Problem E: signature}` count 1 at byte
offset 281406). `python -I scripts/make_digest.py --check` printed
`DIGEST CURRENT` at task start (digest head 8b9ff393).

Round-2 scope: gatekeeper verdict ACCEPT WITH REQUIRED REVISIONS (one blocking
finding). FINDING 1 (blocking): the payload (v) soft-event display was not
volume-balanced (false for Vol<1); repaired by gatekeeper option (a) - the left
side is the spacetime-INTEGRATED defect volume, exactly what the r1 Sect. 5
derivation proves. FINDING 2 (minor, proposal text only): Sect. 2 tube bound
now carries the non-negative tube kinetic term. The payload delta vs r1 is
EXACTLY the (v)-sentence replacement; all r1 artifacts are kept untouched.

## Round-2 artifacts (sha1, size, role)

| file | sha1 | bytes | role |
|---|---|---|---|
| `proposal-r2.md` | `d1438082f2f7c9df84a6082617c09bf8ad958f45` | 37756 | THE PROPOSAL (round 2); regenerable byte-exactly by `patch_r2.py` (asserted on re-run: `REPRODUCED byte-exactly`) |
| `insert-d1-state-measure-r2.tex` | `51010545179a3d3609826aefa0f6c1fa84182ae4` | 4585 | PAYLOAD (Edit B): one blank CRLF line + one paragraph line + CRLF; ASCII; no `\label`, no `\cite`; = r1 payload with EXACTLY the (v)-sentence byte replacement (delta -12) |
| `r2_blocks.txt` | `e7acdc961567d48f5da4abdf3f3a33b3d4519660` | 10094 | the 18 round-2 replacement blocks (`@(` = open-math, `@)` = close-math, every other `@` illegal, asserted) |
| `patch_r2.py` | `678cf923d33d1493502a57786ff9c347d2d37672` | 4397 | regenerates `proposal-r2.md` byte-exactly from pinned `proposal-r1.md` bytes + `r2_blocks.txt`; guard-asserted line ranges, global invariants (`PASS 35 FAIL 0` x2, old POST sha1 record count 1, 2 inherited non-ASCII bytes, 2 inherited lone CRs, 0 control bytes) |
| `gen_payload_117_r2.py` | `6e0a45e1375dcaacfb29d1f9587782c29a949ee3` | 10699 | r2 payload generator: byte replacement on pinned r1 bytes (count-1 assert, reverse-substitution identity) + FRAGS rebuild with join-absorb assertion + full byte/macro scans |
| `out-gen-r117r2p.txt` | `ddfa1fed36f4db28b045fad22ca6de298ed96273` | 448 | generator run record: `v-replacement applied count 1 (delta -12)`, `r2 sha1 51010545... size 4585`, `PAYLOAD SCAN OK` |
| `verify_r117_r2.py` | `ca3c584696c45a26bddce84f5fae9419a553a69a` | 20724 | 31 r1 checks (same seed/arms) + N16 block on the repaired (v) display at genuine Vol != 1 |
| `out-r117r2.txt` | `18da13ed6b1fbe3fb1cc5ba0340bcfe38b98fab9` | 3428 | recorded green run: `PASS 35 FAIL 0` / `ALL CHECKS DONE 117R2`, exit 0; re-run at artifact creation reproduced this file byte-identically |
| `cert-r117r2p.py` | `d4b041360d99f45afa29e172a6e789936e6e2979` | 6570 | two-pass out-of-repo compile certificate, both edits, hard pins: baseline `28f3a0d2.../834663`, anchor byte 281406, Edit-A intermediate `a38d4e29.../834750`, r1->r2 (v) reconstruction re-asserted at runtime, POST size `834750+4585+2` |
| `out-cert-r117r2p.txt` | `98e16b249e09eb4c1e655c85ab6a262a95d34603` | 507 | certificate record: `rc1=0 rc2=0 errlines=0 outw=True undefrefs_pass2=0`, `undefrefs-touching-package-labels=0`, POST `ce91063f...` size 839337, `CERT PASS` |
| `diff-r1-r2.txt` | `b3024c48862bab1dac8420ec03e6c113ef3014cf` | 12694 | audit aid: unified line diff proposal-r1 -> proposal-r2 (visual region check of all 18 replacements); NOT an integration artifact |

## Round-1 artifacts kept untouched (substitution base / audit)

| file | sha1 | bytes |
|---|---|---|
| `proposal-r1.md` | `2ffe61497fefa51597f2381555f28983355ee3e4` | 30536 |
| `insert-d1-state-measure.tex` | `b514e44a19ee627f0aab4ac3d4f69bc052506154` | 4597 |
| `gen_payload_117.py` | `15c8fdfa9e94adc6ac091c8c43b1dd703a5a3e9c` | 7544 |
| `out-gen-r117p.txt` | `f857858754132d615e2190b6de8e4bc7fb2d62e4` | 127 |
| `verify_r117.py` | `0a240ba72deb13ea73167a84d49aefbd24410e9` | 17965 |
| `out-r117.txt` | `93e39fa192243effe67356d1205e13c24ba95a3d` | 2943 |
| `cert-r117p.py` | `f1d27bb269400870851745af29474efed0e814c6` | 4931 |
| `out-cert-r117p.txt` | `e7a1aaf27d3f8001f9d74cf58ce0f948e9ee7b40` | 423 |
| `_scan_macro_join.py` | `91ccfb2caabd6d4519f7e43be032bc6fb3133513` | 1252 |
| `manifest.md` | `7f73f7922ef57e43fdeecd0a0b7b5682fd89cbb8` | 4346 |

Byte-reconstruction proof (payload): `gen_payload_117_r2.py` asserts
`r2 = r1.replace(OLD_SENT, NEW_SENT, 1)` with `count(OLD_SENT) == 1` in r1 and
reverse substitution recovering the r1 bytes byte-exactly (so the ONLY payload
delta is the (v) sentence); `cert-r117r2p.py` re-asserts the identity at
runtime before compiling.

N16 teeth (the blocking finding, both directions): repaired display holds at
Vol=1/4 (B=1..16, e.g. B=16: 0.1690<=0.3594) and Vol=4 (2.7048<=5.7503); the
r1 normalized display FAILS at Vol=1/64, beta=64 (P=1.0000 > 0.3801) while the
repaired one holds there (0.0156<=0.3801).

Option (a) rationale (recorded as Decision 8): the r1 Sect. 5 derivation
(Markov on the one-point law, integrate in x, `\int\mathcal V\le S_E`) already
derives exactly the un-normalized chain, so option (a) restores volume balance
without touching the derivation or any payload numeral, and is true for every
Vol>0; option (b) (Vol^-1 through both RHS terms) divides by Vol<1, inflates
the RHS, and changes no conclusion.

## Round-2 patch audit note (for the gatekeeper)

The first round-2 generation had an off-by-one at `patch_r2.py` REPS entry 16
(range 389-390 instead of 390-391), which deleted the Decision-3 continuation
line "literally true and points to the new paragraph." and left a duplicate of
the old Decision-4 rate line. Caught by the line-region audit recorded in
`diff-r1-r2.txt`; the entry was corrected to (390, 391), `proposal-r2.md`
regenerated, and every replacement region re-audited line-by-line against
`proposal-r1.md`. The intermediate 37778 B `proposal-r2.md`
(`fa20e443ae0c521fab491ae91deb0b554f80ee9f`) was deleted; no integrated text,
proposal or script references it.

## Expected integration arithmetic (recompute against the CURRENT tree)

- baseline appH: `28f3a0d2401efc1c65b53a99a5968cdcb70fed7d` / 834663
- after Edit A: `a38d4e293806a09f7fc5072a273ae49f62100590` / 834750 (+87)
- POST (after Edit B): `ce91063fddcaa5599429519f4bc2c478e0d919e8` / 839337
  (= 834750 + 4585 + 2), produced and compiled green (two passes, zero
  undefined references, zero undefined refs touching package labels) by
  `cert-r117r2p.py` in an out-of-repo copy.
- Anchor `\section{Problem E: signature}`: count 1, byte offset 281406 in the
  baseline (281493 after Edit A); anchor pre-context: no blank line between
  the 116 paragraph and the anchor (byte-verified).
- Join convention (115 form; payload carries the leading separator and no
  trailing blank line): `data.replace(ANCHOR, PAYLOAD + CRLF + ANCHOR, 1)`.

## Landing note for the integrator

Apply Edit A first, then Edit B, in the current tree; USE THE ROUND-2 PAYLOAD
`insert-d1-state-measure-r2.tex` (`51010545...`, 4585 B) - do NOT apply the
round-1 payload. Recount both the anchor and the Edit A amendment string
against the current tree before editing; if the tree has moved off
`28f3a0d2...`, recompute the arithmetic (the payload bytes are unchanged).
Apply no other change to `appH-microscopic-proofs.tex`; no other file changes.
Then `python scripts/build_check.py` and `python scripts/make_digest.py`.
Expected diff: one in-line clause replacement + one inserted paragraph
(balanced blank line from the payload's leading CRLF).

No files outside this proposal folder were created or modified by this run.
