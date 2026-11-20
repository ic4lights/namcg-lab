# Manifest, proposal 090, round 1 (regenerated after round-1 review addendum)

Manuscript file touched by the proposed integration: `chapters/appH-microscopic-proofs.tex` only.

## Splice contract (verified by simulate_apply_090.py against the current tree)
- PRE appH: size 752790, sha256 4b5213160fab6154dbefcdaaf5795501eebed9add432b910660ef2b4e62068d6, CRLF 3842.
- Tail-pin (count 1): `close nothing in Problem~G.\r\n\r\n\emph{Vacuum term.}` on paragraph line 3191;
  the phrase `the matrix integral itself is not evaluated here` has count 1 (L3191).
- Insert: `insert-r1.tex`, one paragraph, CRLF-terminated, 3735 bytes, sha256 first 8 hex 3a6a69c4;
  new paragraph lands at line 3193, `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}` moves to line 3195.
- POST appH: size 756527, sha256 31149f6250ec834adaac83903a6a492ee7c987f1b4ce0ca9abcf1d930ad6ac1c,
  CRLF 3844, no lone LF; byte identity outside the splice window asserted by the script.
- Hygiene (hygiene_090.py, PASS): no `$`, no `[`/`]`, no \cite/\ref/\eqref/\label macros, no `\=`,
  no accents inside math, ASCII only, control-byte-free, single CRLF-terminated line, one \emph,
  balanced \( \) (53/53), closer `it closes nothing in Problem~G.` count 1, banned-word map empty,
  header `Fixed-trace beta deformation` count 1 in insert and 0 in PRE appH.
- Smoke (smoke_compile_090.py, SMOKE GATE OK, run from the repository root; build dir is the
  in-folder `scratch_latex/`): positive control article+amsmath,amssymb compiles (rc 0, no error
  lines, no undefined control sequence); negative control (first \lvert byte-surgered to \lvertz
  in memory only) fails as required (rc 1, `! Undefined control sequence`). The insert itself is
  untouched by the negative control (asserted on the shipped bytes).

## Verification scripts (re-run: `python -I proposals/090-g-interaction-induced-simplex-profiles/<script>`
from the repository root; all .out files shipped)
- s1_pushforward.py: Jacobian of E = tau*p is tau^(D-1) (D=2,3 exact); exact separation of the
  fixed-trace weight into (pure-tau law) x (simplex kernel); tau-law integral sigma^k Gamma(k),
  k = D a + beta D(D-1)/2; profile kernel independent of sigma.
- s2_stationarity_D2.py: closed form u* = sqrt(beta/(beta+2(a-1))); residual 0; curvature
  -(2a+beta-2)^2/(a-1) (D2_FACTOR_CHECK: 0); onset 1/sqrt(2(a-1)); tail a-1; a=1 vertex-only.
- s2b_stationarity_D3.py: D=3 stationary profiles a=2, beta in {0.2,1,5,20} (residuals <= 7e-28);
  Euler multiplier identity mismatch 0; sqrt-onset slopes 0.4856..0.5; a=1 mismatch = 3 beta.
- s2c_D4_and_gridmax.py: D=4 profile a=2, beta=1 (residual 1.6e-29); D=3 grid argmax within
  0.0016 < h = 0.00415 of the stationary root.
- s3_limits_normalization.py: Z2(a=1) = 1/(beta+1) -> 1; Z2 beta-form 4^(1-a) B((beta+1)/2, a)/2
  (12-digit checks); face point (3+sqrt3)/6 of t(1-t)(2t-1) (the a=2, beta=1 face density; the
  script label prefix A1 is a misnomer); small-beta slope log(2t-1); Z3(a=1) = 0.4007 at beta=0.05
  trending to flat 0.5; kernel 0 at barycenter, positive at the chamber profile. Shipped version is
  FIXED (v3 had a wrong inner integration limit letting x3 < 0); .out matches the shipped script.
- s4_mc_weighted_mean.py: E_w[max p_i] 0.628843 (MC, seed 20261119, N=4e5) vs 0.628941 (grid 1000);
  E_w[sum p_i^2] 0.499830 vs 0.499997 at a=2, beta=1. Shipped version is FIXED (v2 double-counted
  the Dirichlet base factor); bug recorded in the script header.
- simulate_apply_090.py: READ-ONLY splice rehearsal; prints the PRE/POST contract; SIMULATE OK.
- hygiene_090.py / smoke_compile_090.py: audits described above; PASS / OK printed in the .out files.

## Inventory (all files except this manifest, which self-references)
| file | bytes | sha256[0:8] |
|---|---|---|
| hygiene_090.out | 268 | ffdff856 |
| hygiene_090.py | 1938 | 187617dc |
| insert-r1.tex | 3735 | 3a6a69c4 |
| proposal-r1.md | 25242 | 9090a9b9 |
| s1_pushforward.out | 295 | c745375f |
| s1_pushforward.py | 1473 | 23a43f76 |
| s2_stationarity_D2.out | 569 | 84d81357 |
| s2_stationarity_D2.py | 1333 | bc9e9481 |
| s2b_stationarity_D3.out | 650 | f1a0e5f8 |
| s2b_stationarity_D3.py | 1731 | 08e15f60 |
| s2c_D4_and_gridmax.out | 240 | 75956a8a |
| s2c_D4_and_gridmax.py | 1772 | aeea4a3a |
| s3_limits_normalization.out | 536 | d747e30d |
| s3_limits_normalization.py | 2592 | 2424f8f4 |
| s4_mc_weighted_mean.out | 201 | 66fd6fc0 |
| s4_mc_weighted_mean.py | 1299 | 8aa33fad |
| scratch_latex/smoke090.log | 6727 | e2006d9f |
| scratch_latex/smoke090.tex | 3820 | 7f610b2f |
| scratch_latex/smoke090neg.log | 6016 | d4727355 |
| scratch_latex/smoke090neg.tex | 3821 | 06541ba9 |
| simulate_apply_090.out | 404 | 86bfd2bb |
| simulate_apply_090.py | 1758 | 1c0e1de2 |
| smoke_compile_090.out | 99 | cbdb27ee |
| smoke_compile_090.py | 1817 | 9393d0f4 |
