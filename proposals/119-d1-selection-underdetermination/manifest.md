# Manifest 119-d1-selection-underdetermination (round 2, 2026-11-23)

Branch `local/gpu`; no git write commands run; no files outside this proposal folder modified in
round 2 (round-1 section 4 records the separately assigned 118-folder fixes). All Python run
`python -I -B`. Baseline re-verified live before byte work AND again at manifest time (round-2
byte session): `chapters/appH-microscopic-proofs.tex` working bytes sha1[:12] `2ed53c7778c1`,
843649 B; anchor `\section{Problem E: signature}` count 1 at byte offset 290106 (unchanged);
in-memory POST reconstruction asserted below. Inputs read: `dispatch-r2.md` (spec), `review-r1.md`
(verdict ACCEPT WITH REQUIRED REVISIONS; `484736e8c8f0`/17539), `review-r1-addendum.md`
(`c8621a1e0549`/2190; spec-neutral: restates F-1/F-2/F-3 as implemented, retracts its own
appended-line determinism artifact, verdict unchanged).

## 1. File pins (sha1 / bytes)

| file | sha1 | bytes |
|---|---|---|
| proposal-r2.md | `824ba35e90f69b8d68901293665d4a6e9089ba3b` | 28037 |
| proposal-r1.md | `a9316eba486e1356f30665d5587417a7aaa1f1ff` | 23535 |
| proposal-r1-superseded-r1.md | `a9316eba486e1356f30665d5587417a7aaa1f1ff` | 23535 |
| insert-overdetermination-r1.tex | `c085c19cba683ff3aa832ac36a1c6b7075ba8d63` | 5191 |
| insert-overdetermination-r1-superseded-r1.tex | `3b4c2d0794a96a9cccac5fae79f797e595342cd4` | 4704 |
| gen_payload_119.py | `2242d21eacc5c63181bbd9c4448f672fb49fac1d` | 8291 |
| gen_payload_119-superseded-r1.py | `15cbff8eb70f3eedbc3463ab40f27f9d2b83ee94` | 7804 |
| cert-r119p.py | `2de50b85d266a6bcd691db2185a82ce3e9a8989e` | 4555 |
| verify_r119.py | `c3e02350e4ec2da45009ca4eadfd9295c104b086` | 23292 |
| out-r119.txt | `009de59d50acc04af0247dc057e94277f13a72d4` | 6476 |
| out-r119-r2.txt | `009de59d50acc04af0247dc057e94277f13a72d4` | 6476 |
| out-r119-run1-fail.txt | `19f92196bf46cdc57bf3f4fd041509d447de7219` | 6272 |
| out-cert-r119p.txt | `e87ae59a3c4a4b57a540ac4dc1bcd996ef75386d` | 393 |
| out-cert-r119p-r2.txt | `d2411624a9bb67a8e0925925d7283127d73d231b` | 421 |
| notes.md | `6fbc2d9b88f7f1e9086b3a4b69f6b71450967933` | 12257 |
| review-r1.md | `484736e8c8f0133a5ad7d69002935d0e05d7fc0f` | 17539 |
| review-r1-addendum.md | `c8621a1e0549d971e20c8017a9b1f32d645386a8` | 2190 |
| dispatch-r2.md | `cc5e98c9decaf2b44c4e60a794aade9e80e0ff54` | 2932 |
| manifest.md | bb432f4b923fba52e989991da113ac8299f2dfd1 | (self, rule below) |

Self-hash rule (round 2, made length-explicit): the sha1 in the manifest.md row is that of the
manifest file with its own 40-hex cell content replaced by the exact 40-byte literal token
SELF40TOKEN_ followed by 28 zeros (token and hex are both 40 bytes, so all other bytes are
unaffected). Recheck: read manifest.md, replace the hex in the manifest.md row cell with that
40-byte token, hash, compare to the cell.

## 2. Supersession ledger (old -> new, round 2)

| artifact | old sha1[:12] / bytes | new sha1[:12] / bytes | reason |
|---|---|---|---|
| insert-overdetermination-r1.tex | `3b4c2d0794a9` / 4704 | `c085c19cba68` / 5191 | apply review-r1 F-1 (`>=` + equality double-ray clause; strict `<` window), F-2 option (a) (displayed system labeled u(4) `(A_G,B_G)=(4,0)`; su(4) channel data stated outside the pairing), F-3 (shift clause scoped to commutator-type lifts; eq:Smicro lift and dictionary bridge stated NOT shift-covariant); old bytes preserved byte-for-byte as insert-overdetermination-r1-superseded-r1.tex |
| gen_payload_119.py | `15cbff8eb70f` / 7804 | `2242d21eacc5` / 8291 | generator patched to emit the round-2 payload (four byte-exact line replacements); old preserved as gen_payload_119-superseded-r1.py |
| cert-r119p.py | `27ce6d10200f` / 4560 | `2de50b85d266` / 4555 | hard pins updated to the round-2 payload pin and POST; POST sha1 now printed in full; structure and asserts unchanged |
| proposal-r1.md | `a9316eba486e` / 23535 (kept) | round text = proposal-r2.md `824ba35e90f6` / 28037 | round-1 text NOT edited (new-round-file rule); pre-round copy proposal-r1-superseded-r1.md created per dispatch supersession instruction (byte-identical, same pin) |
| proposal-r2.md | `8aa711e2232f` / 27569 (draft, same session) | `824ba35e90f6` / 28037 | guarded fixes before first pin: beta-clause renderings v4 -> v_4 to match payload; capture procedure documented; identity statement set to confirmed |
| notes.md | `087475daf03a` / 6899 -> `fe9147ac6e45` / 10677 -> `6fbc2d9b88f7` / 12257 | | Round 2 section appended; byte repair: the 0x0D at 9452 of the middle state was a backslash eaten as a CR escape by a prior python-string append (corrupted an Assumption-ref mention), restored to a literal backslash byte-for-byte, asserted count 1; file now 0 CR bytes; final round-2 section appended |
| manifest.md | `6ca77c4b7203` (r1 file; its self-cell `1d18781c772c`) | this file | full round-2 re-pin |

## 3. Pins

- Payload artifact: `insert-overdetermination-r1.tex`, 5191 B, sha1[:12] `c085c19cba68`
  (full `c085c19cba683ff3aa832ac36a1c6b7075ba8d63`). Purely additive at the anchor; CRLF-terminated,
  ASCII, no BOM, zero `\label`, zero `\cite`; final rule-3 scope sentence unchanged from r1.
- POST (spliced appH): 848842 B = 843649 + 5191 + 2, full sha1
  `9e0b198af2c3c7f11454980ec6df2e875fbb80ef` (reconstructed in memory from the live tree at
  manifest time and asserted equal to the generator printout and cert PRE-COMPILE pins).
- Verifier: `verify_r119.py` UNCHANGED in round 2 (F-2 option (a); F-5 waived wording alignment).
  Raw capture `out-r119-r2.txt` (new): 6476 B `009de59d50acc04af0247dc057e94277f13a72d4`,
  `cmp` exit 0 against `out-r119.txt` (byte-identical; same interpreter and script), exit code 0
  (`VERIFY-EXIT=0` preserved in the job wrapper log), ends `TOTAL 62/62 PASS` /
  `ALL CHECKS DONE 119`. Capture integrity: the run wrapper had appended its own 14-byte
  `VERIFY-EXIT=0` status line (file 6490 B); after `cmp -n 6476` proved the verifier prefix
  byte-identical to `out-r119.txt`, that appended line was removed by `head -c 6476` truncation -
  no verifier byte was added, changed, or deleted; raw stdout redirect otherwise untouched.
  A 0-byte `err-verify-r2.log` (stderr sink) was removed.
- Generator: run twice, byte-identical (`GEN OK 119`); join-guard positive control (injected
  dangling `\secti`) fires and negative control passes inside both runs; hygiene asserts pass
  (CR=LF, ends CRLF, ASCII, no tab/BOM/dollar, no `\label`/`\cite`, brace and paren-math balance);
  live baseline pins asserted; POST independently reconstructed.
- Certificate (`cert-r119p.py`, fresh out-of-repo temp tree from tracked working bytes minus root
  PDF and reports/, plus working bbl; 2945 files; tree removed after): `out-cert-r119p-r2.txt` -
  `PRE-COMPILE PINS OK: baseline 2ed53c7778c1/843649, anchor 1, payload c085c19cba68/5191,
  POST 848842 9e0b198af2c3c7f11454980ec6df2e875fbb80ef`, `PASS 1: rc=0`, `PASS 2: rc=0`, zero
  exclamation error lines, zero undefined/multiply-defined references, PDF 3231928 B,
  `CERT PASS`, `CERT-EXIT=0`.
- Labels used by the payload, each verified to occur exactly once book-wide this round:
  eq:Smatrix, eq:Smicro, eq:V, sec:ch3-relate, ass:dictionary, eq:LUV-def. (eq:dictionary verified
  unique but referenced via Assumption ass:dictionary, which contains it; not referenced directly.)
- Trace macro: payload uses `\operatorname{Tr}` (manuscript-dominant: 88x in appH vs `\Tr` 2x;
  preamble `namcg-book7.tex` L104 defines `\Tr` as `\operatorname{Tr}`, so the gatekeeper snippets
  are the same macro; dispatch said match the manuscript).

## 4. Excluded directory

`__pycache__/` (stale, created by an early pre-`-B` interpreter invocation; deletion blocked by
the permission hook). Not referenced by any artifact; reproduction commands use `-I -B` and
create no cache.

## 5. 118-folder record fixes (round-1 assigned secondary task; unchanged in round 2)

- `proposals/118-presentation-a-potential-selection/proposal-r1-superseded-F1F2.md` (new):
  byte-for-byte copy of the original r1, sha1[:12] `4a6fa455daa2`, 48887 B.
- `proposals/118-presentation-a-potential-selection/proposal-r1.md`: F1 D7
  `x = (1/(2eps), 0, 0, 0)` -> `x = (1/sqrt(2 eps), 0, 0, 0)`; F2 D5
  `y^2 = ...` -> `sigma^2 = w^2 = ...` (one occurrence each; review-r1 findings 1-2).
  Old `4a6fa455daa2`/48887 -> new `b6c55d51a73f`/48902.
- `proposals/118-presentation-a-potential-selection/manifest.md`: section 10 appended
  (supersession + F1/F2 old/new pins); now `8df4f47c7d19`/13057.

## 6. Reproduction (from this folder)

1. `python -I -B verify_r119.py`  ->  `TOTAL 62/62 PASS`, `ALL CHECKS DONE 119`; stdout must be
   byte-identical to `out-r119-r2.txt`.
2. `python -I -B gen_payload_119.py` (twice; second asserts byte-identity)  ->
   `payload bytes: 5191  sha1[:12]: c085c19cba68`,
   `POST: 848842 (= 843649 + 5191 + 2)  full sha1: 9e0b198af2c3c7f11454980ec6df2e875fbb80ef`,
   `GEN OK 119`.
3. `python -I -B cert-r119p.py`  ->  `PRE-COMPILE PINS OK ...`, `CERT PASS`, `temp tree removed`.


## Addendum 2026-11-23 (chain 120 stage 2)

Record-only addendum appended by the chain-120 stage-2 agent (byte append; nothing above
altered).

Census correction superseding the "Trace macro" line above (manifest.md line 85) and
proposal-r2.md lines 54 and 237. Verified 2026-11-23 with
proposals/120-commutator-lift-bridge/census_trace120.py: pre-integration appH
(843649-byte baseline reconstructed by exact removal of the integrated 119 block from
live 9e0b198af2c3/848842): \operatorname{Tr} 138, \mathrm{Tr} 25, standalone \Tr 2;
live post-integration: 156 / 25 / 2 (119 payload contributes 18 \operatorname{Tr}).
The "\Tr 2x" figure is confirmed (two "\Tr\rho_D^n", appH lines 3235/3250 in live
bytes); "88x" for \operatorname{Tr} was wrong (138) and the \mathrm{Tr} category (25)
was omitted. The register decision (\operatorname{Tr} in payloads) is unaffected and
strengthened.

Also recorded: (i) a second escape artifact in notes.md line 123 (LF + "ewcommand",
same class as the documented 0x0D repair above), documentation-only; (ii)
scratch/119/out-s7-m1.txt (ccfc557ff99d / 808 B) is stale relative to its script per
the chain-120 stage-1 audit, record-only.

Pin changes caused by this addendum pair: notes.md 6fbc2d9b88f7/12257 -> the post-append
pin recorded in proposals/120-commutator-lift-bridge/manifest.md (chain 120 folder),
this manifest 5e3e09090733/8999 -> own new pin likewise recorded there (a file cannot
contain its own post-hash).
