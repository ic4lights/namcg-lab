# Manifest 118-presentation-a-potential-selection (stage C, 2026-11-23)

Baseline state: branch `local/gpu`, HEAD `8b9ff39`; `chapters/appH-microscopic-proofs.tex`
sha1 `ce91063fddcaa5599429519f4bc2c478e0d919e8`, 839337 B (re-counted at stage C start;
matches the dispatch pin). All Python run with `python -I -B`. No files outside this
proposal folder (and `scratch/118/`) were written; no git write commands were run.

## 1. Pin table (sha1 / bytes)

Current active files:

| file | sha1 | bytes | note |
|---|---|---|---|
| proposal-r1.md | `4a6fa455daa2a6dd3da8f9ca9c8cf694688dd90b` | 48887 | r1 + `## Pins addendum (stage C)` appended at end |
| verify_r118_r2.py | `5950fbff30b64fb66ed3813c3fbb39bd6180b632` | 25297 | re-pinned, N12 COVERAGE string fix (see 1a) |
| out-r118r2.txt | `756bd4a8c4f757902dc2a031ef0925a7633964a5` | 2844 | re-pinned raw capture (see 1b) |
| insert-potential-selection-r1.tex | `bbe4e535dd31c76a82ea89ff1b20980eb979f9bf` | 4024 | manuscript-bound payload (P2) |
| gen_payload_118.py | `bba66dd1aeae1d2aa43c08e5d0560ce3038f8f78` | 9426 | payload generator (P3) |
| out-gen-r118p.txt | `2886358184477365ec1786c9debd1172ff73ef2a` | 1040 | two generator runs, tails identical |
| cert-r118p.py | `b711792287c81887574084b770900bc037533c41` | 4938 | compile certificate (P4) |
| out-cert-r118p.txt | `4cd73d864fa7fe0e3fe08c1c9e498229f8f13f77` | 352 | CERT PASS capture (see 5) |

Superseded / historical pins:

| file | sha1 | bytes | status |
|---|---|---|---|
| verify_r118.py | `c2a6bcf98a5e9a55398976879747495af7503c94` | 16868 | round-1 pack, kept unmodified |
| out-r118.txt | `0d95d699c0fb890408fef1de54bb3d432c8037fe` | 823 | round-1 output (records C3 FAIL, C5 NameError), kept |
| verify_r118_r2.py (pre-fix) | `9fb20e50fc198ae8912377bdb4a8893363087a9a` | 25294 | superseded by `5950fbff...` (string-only fix, 1a) |
| out-r118r2.txt (stage A pin) | `0ba8a0d7ec87325aeeaedac5a2d024dd5c0cfb3b` | 3132 | hand-edited: carried a trailing 291 B N11 sentence the script never printed; SUPERSEDED |
| scratch/118/rerun-stageb.txt | `4627add7038ac3be739069ffb24fa31891d35775` | 2841 | stage-B re-run, pre-typo-fix; SUPERSEDED |
| proposal-r1.md (pre-append) | `818f9ac8f6c289ba45c9de670019eea3746fe9ad` | 47153 | the first 47153 bytes of the current proposal-r1.md hash to this value (verified by python at stage C): append-only integrity proven |

Scratch captures (stage C): `scratch/118/rerun-c1.txt` = `scratch/118/rerun-c2.txt` =
`756bd4a8c4f757902dc2a031ef0925a7633964a5` (2844 B, byte-identical pack runs);
`scratch/118/payload-run1.tex` = `bbe4e535dd31c76a82ea89ff1b20980eb979f9bf` (first generator run).

### 1a. verify_r118_r2.py fix (the only edit)
Single string literal on the N12 COVERAGE print (line 521): `det 8c3^3(c3+4c2s)` ->
`det 16 c3^3 (c3+4c2s)`, matching the asserted value `16*c3**3*(c3 + 4*c2s)` (line 435) and the
hand determinant `(2c3)^3 (2c3+8c2) = 16 c3^3 (c3+4c2)`. No check logic touched; byte delta +3.

### 1b. Pack reproducibility (P1)
`python -I -B verify_r118_r2.py` run twice, redirected to `scratch/118/rerun-c1.txt` and
`rerun-c2.txt`: exit 0 both; `cmp` byte-identical; 13 `PASS` lines (C1, C2, C3r, C4, C5r, C6,
C7, C8, C9, C10, N11, N12, N13); tail `TOTAL 13/13 PASS` / `ALL CHECKS DONE 118`. The capture
overwrote `out-r118r2.txt`, replacing the hand-edited `0ba8a0d7.../3132` pin (stage-B disclosed
discrepancy resolved by re-pin, option (a) of the stage-B dispatch note).

## 2. Anchor and reference-label verification (live tree, stage C)

- Splice anchor `\section{Problem E: signature}` in appH: count 1, byte offset 286080; the bytes
  immediately before it end the integrated 117 paragraph (`...PROGRAMME-CONDITIONAL.\r\n\r\n`).
- `\label{...}` definition counts in `chapters/*.tex` (grep -rc, one definition per label, all in
  `chapters/ch03-matrix-action.tex`): `eq:V` 1, `eq:Smatrix` 1, `ass:dictionary` 1,
  `eq:vacuum-manifold` 1, `sec:ch3-relate` 1, `eq:Phi-eom` 1. No duplicate labels; all six are the
  only cross-references used by the payload; the payload contains no `\label` and no `\cite`.

## 3. Payload and hygiene (P2/P3)

`gen_payload_118.py` rebuilds `insert-potential-selection-r1.tex` byte-exactly from 50 FRAGS
(49 joins). Join check: macro-absorption regex `\\[A-Za-z]+$` at every join (a fragment ending in
`\macro` must not be followed by a letter) - NOTE: the 117 r2 generator used `r'\\\\[A-Za-z]+$'`,
which matches a DOUBLED backslash and was vacuous on single-backslash LaTeX; corrected here so the
check bites, and it passes. Regeneration idempotence: second run asserts on-disk bytes == rebuilt
bytes BEFORE writing; both runs `PAYLOAD SCAN OK`, exit 0; `out-gen-r118p.txt` holds both runs.

Hygiene scan (verbatim from `out-gen-r118p.txt`, identical in both runs):
`bytes 4024 CR 2 LF 2 CRLF 2 loneCR 0 loneLF 0 tab 0 nonASCII 0 ctrl 0 endsCRLF True BOM False
backslash-ws 0 \( 41 \) 41 braces 27/27`; forbidden `\label`/`\cite` absent; the six required
label strings present; macro tokens `['Delta','Phi','Theta','cos','dagger','det','emph','eqref',
'lambda','mathbb','mathcal','mathrm','ne','ref','sigma','sum','varepsilon']`, UNKNOWN: `[]`.
Payload structure: leading CRLF blank line + ONE `"\emph{Constraint results on the
Presentation-A selection of Equation~\eqref{eq:V}.} ..."` line + trailing CRLF; no trailing blank
line; ASCII only; signature/conventions untouched (no metric statements made; SO(3,1) not
mentioned - nothing contradicts the manuscript conventions).

## 4. POST pins (P4/P5)

Canonical splice `data.replace(ANCHOR, PAYLOAD + b"\r\n" + ANCHOR, 1)`:
- size 843363 = 839337 (baseline) + 4024 (payload) + 2 (join), recomputed independently;
- sha1 `c24902b31abafc126a7e59485f2b706d2f2b17d4`, computed independently by a standalone python
  one-shot on the live tree BEFORE the certificate ran, then hard-asserted by `cert-r118p.py`
  before any compile.

## 5. Certificate (P4)

`python -I -B cert-r118p.py` (temp copy of the working tree minus `.git/scratch/proposals/reports`,
`namcg-book7.bbl` included and asserted, root PDF excluded):
`rc1=0 rc2=0 errlines=0 outw=True undefrefs_pass2=0`,
`undefrefs-touching-package-labels=0`, `CERT PASS`, exit 0 (full capture `out-cert-r118p.txt`).
Hard asserts precede CERT PASS: baseline pin, anchor count/offset, payload pin/structure, POST
size+sha1, zero `! ` lines, `Output written`, zero undefined refs at pass 2, zero undefined refs
whose messages match the six spliced labels (`eq:V'` etc. with trailing quote - no prefix collision).

## 6. Parameter coverage (consolidated from the pinned pack COVERAGE lines, `out-r118r2.txt`)

- C1,C2,C4,C6,C7,C8,C9,C10: check code identical to round 1 (C6-C10 first fully executed in r2);
  ranges: C1 symbolic generic lambda,v>0 with N=4 exact, N=7 mismatch tooth, explicit N=6; C2 40
  random complex 4x4, h=1e-6, seeded RNG 118; C4 symbolic n in {3,4,5} + 60 random integer momenta,
  theta in (-0.15,0.15); C6 200 random 4x4 + rectangular 4x3; C7 400 random simplex points tau=4 +
  six (a,b) region scans; C8 eps=0.3, 60000 simplex points, t-grid 200001; C9 200 random lambda in
  (0.01,10), v in (0.01,5); C10 60/200 random unitaries.
- C3r: SOS identity symbolic generic nonzero (c4,c2s); 18-point closed sign grid, nine regions incl.
  c4=0 rows and hilltop tooth; 60 random Mexican-hat minima.
- C5r: dims at (n,d) in {(2,1),(2,2),(2,3),(2,4),(3,4),(4,1),(4,2),(4,4)} vs partitions into at most
  n parts; CH teeth; kernel span at n=4,d=2; bifundamental teeth.
- N11: 11 bounded-class points, 51^4 full-grid minima vs s formula; 11 face-restricted minima vs w
  formula; Delta identity/positivity/face-gap; 3 w != s teeth; 3 unbounded teeth.
- N12: symbolic Hessian eigenvalues 2c3 (x3), 2c3+8c2s, det 16 c3^3 (c3+4c2s) [typo fixed, 1a];
  strata k=1,2,3; Delta symbolic; eq:V slice Delta = lambda v^4/4, V_vac = 0, s = v^2; monotonicity;
  corridor nonexistence.
- N13: exp(-theta E) exact entries; three channel phases pairwise distinct, flat at theta=0;
  1-cos = theta^2 p^2/8 + O(theta^4).

## 7. Payload claim -> proposal tier table

| payload passage | proposal result | tier (rule 6) |
|---|---|---|
| two quartic invariants, Tr X^2 = sum sigma_i^4 non-negative, family c3..c0 | R4 (D4 pairing argument, C5r/C6/C10 teeth) | established at checked points + self-contained argument; family-as-Presentation-A-content CONDITIONAL on stated field content + quartic truncation (stated in payload) |
| eq:V = exact slice (lambda/4, 0, -lambda v^2/2, lambda v^4), c0 = lambda v^4 = sum of four squares | R1 (C1, C9) | established identity (symbolic) |
| vacuum-manifold stationarity, gradient (lambda/2) Phi (X - v^2 I) = eq:Phi-eom term | R2 (C2; vacuum subloop definitional, disclosed) | established derivation |
| Hessian eigenvalues, strict convexity = bounded region, unique vacuum s, face inf (0,w,w,w), Delta formula > 0 | R5 (N11, N12) | established derivation |
| slice s = v^2, Delta = lambda v^4/4 re-derived as slice of family theorem; w != s off slice | R6 (N12), R5 teeth | established derivation; "re-derived, not superseded" wording kept |
| channel factors pairwise distinct, flat degeneracy, 1-cos = Theta^2 p^2/8 + O(Theta^4), no parameter absorbs phases, Theta^2 truncation reading | R7 (C4, N13) | established from the live star product; selection-bearing reading CONDITIONAL on dictionary scope; stated as constraint, not selection |
| eps (Tr X)^4 - Tr X^2 bounded with rank-1 global min on det=0, value -1/(4 eps) | R8 (C8) | established counterexample |
| Scope sentence: assumptions kept assumed; "constrained but not derived-closed"; closes no problem | disclosures of `proposal-r1.md` | honest-status text, no tier |

## 8. Stage provenance

- Split chain A/B/C after TWO researcher-agent deaths to API context limits (documented in
  `proposal-r1.md` Provenance). Stage A finished the verification pack to 13/13; stage B did the
  source reads and `proposal-r1.md`; stage C (this) re-pinned the pack, authored payload,
  generator, certificate, manifest, and appended the pins addendum.
- Three check-bug adjudications (all CHECK-code bugs, no claim weakened): C3 -> C3r (sign-table:
  Mexican-hat iff c4>0, c2<0, full nine-region classification); C5 -> C5r (NameError + wrong
  expected dimensions p(d) -> partitions into at most n parts); N11 r2b (`grid_min` axis-0 stack
  vs axis-(-1) reduce -> fixed `np.stack(axis=-1)`, tolerances/points/teeth unchanged).
- Stage C adjudications: (i) N12 COVERAGE prose typo `8c3^3` -> `16 c3^3` fixed (code was always
  16; the printed value now matches the asserted value); (ii) `out-r118r2.txt` re-captured raw
  (supersedes the hand-edited 0ba8a0d7/3132 and the 4627add7/2841 stage-B capture);
  (iii) 117-form join-absorb regex found vacuous and corrected (section 3); (iv) one patch
  attempt on proposal-r1.md double-encoded CRLF in the ADDED block; corrected, and the intact
  pre-append integrity was then PROVEN by hashing the first 47153 bytes to the pre-append pin
  818f9ac8.../47153 (no pre-existing byte was changed); (v) payload uses `Problem~D`, `Problem~D1`,
  `Problem~A` forms re-grepped in the live tree, closes nothing and states no status label.

## 9. Special instructions for the gatekeeper

- Reproduce the pack: from this folder `python -I -B verify_r118_r2.py > out.txt 2>&1` (few
  minutes); expect 13 PASS lines, `TOTAL 13/13 PASS`, `ALL CHECKS DONE 118`, and byte-identity
  with `out-r118r2.txt`.
- Reproduce the payload: `python -I -B gen_payload_118.py` (delete nothing; second run asserts
  byte-identity). Reproduce the certificate: `python -I -B cert-r118p.py` (compiles in a temp
  copy; ends `CERT PASS`).
- Must NOT be asserted from the payload: that eq:V or any slice is derived from eq:Smatrix; that
  the Moyal vertex computes fluctuation vertices beyond the recorded constant-Theta check scope;
  that the L1711 threshold is superseded rather than re-derived; any closure or label change for
  D, D1, A. The dictionary (ass:dictionary), the field content and the quartic truncation remain
  assumed; the selection is CONSTRAINED, not derived-closed.

## 10. Record corrections 2026-11-23 (review-r1 findings 1-2, no payload/manuscript consequence)

- Superseded original preserved byte-for-byte before editing: `proposal-r1-superseded-F1F2.md`
  sha1[:12] 4a6fa455daa2, size 48887 (matches the pinned pre-edit record).
- F1 (D7 parenthetical): `x = (1/(2eps), 0, 0, 0)` -> `x = (1/sqrt(2 eps), 0, 0, 0)` (coordinate is
  tau = 1/sqrt(2 eps), since tau^2 = 1/(2 eps); at eps = 0.3 the old point gives -0.46296, not
  -1/(4 eps) = -0.83333). R8(a) text and the payload were already correct.
- F2 (D5 face minimizer): `y^2 = -c1/(2(c3 + k c2))` -> `sigma^2 = w^2 = -c1/(2(c3 + k c2))`
  (y is the x_i = sigma_i^2 coordinate, dimensionally sigma^2 = w^2; the payload's
  `w^2 = -c1/(2(c3+3c2))` was already correct).
- proposal-r1.md: old sha1[:12] 4a6fa455daa2 / 48887 B -> new b6c55d51a73f / 48902 B; all other bytes unchanged
  (two literal replacements, counts 1 each). No integrated text or payload was touched.
