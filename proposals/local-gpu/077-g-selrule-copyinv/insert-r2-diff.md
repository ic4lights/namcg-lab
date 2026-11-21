# insert-r2 diff — 077-g-selrule-copyinv, round 2 (wording-only, applied by patch_r2.py)

File: `proposals/077-g-selrule-copyinv/insert-r1.tex` (single content line + terminal CRLF; name unchanged).
OLD = round-1 bytes (content sha256 b7e1460eddd00c10..., 5,185 B, file sha8 3947273c).
NEW = round-2 bytes (content sha256 71747ef46bf68649..., 5,633 B, file sha8 55e69809).
Every OLD clause below occurred exactly once in the round-1 insert (asserted by patch_r2.py);
nothing else changed. All checks: `verify_r2_clauses.out` (ALL CHECKS PASS).

## Replacement 1 (findings 1 + 2, mandatory)

OLD:
```
tiling of this spectrum by the one-copy multiset is measured by the relative gap \(D=\max_k(e_{(k+1)q-1}-e_{kq})/\max_k|e_k|\) and the fourth-moment signature excess \(U_2=\operatorname{Tr}\widetilde Q^{4}/(2q(\operatorname{Tr}\widetilde Q^{2}/(2q))^{2})-1\), which vanish at tiling.
```
NEW:
```
tiling of this spectrum by the one-copy multiset is measured by the relative gap \(D=\max_{k=1,2}\bigl(e_{kq}-e_{(k-1)q+1}\bigr)/\max_j|e_j|\), which vanishes at tiling, and by the fourth-moment signature excess \(U_2=\operatorname{Tr}\widetilde Q^{4}/(2q(\operatorname{Tr}\widetilde Q^{2}/(2q))^{2})-1\), which vanishes exactly when the nonzero eigenvalues have equal modulus (in particular at a tiling by the symmetric multiset \(\{-\varepsilon,\varepsilon\}\)), and at a generic tiling measures the \(\operatorname{Im}\alpha\) shift, decaying as \(O(1/N)\) below the leading order in the matched-scale ensembles tested (numerical).
```
Notes. (i) D formula = the gatekeeper's corrected snippet, verified equal to the shipped
code statistic (`e[k*q+q-1]-e[k*q]` on the sorted array, k=0,1, denominator `np.abs(e).max()`
over the 2q nonzero eigenvalues): 1-based `e_{kq}-e_{(k-1)q+1}` ↔ 0-based `e[k*q-1]-e[(k-1)*q]`;
deviation 0.0 on 600 random spectra q=2,3,4 and 0 on 200 tiled spectra, while the round-1
formula read 1-based never vanishes on a tiled spectrum (verify_r2_clauses.out A1/A2).
(ii) U_2 clause = gatekeeper's corrected content; "which vanish at tiling" was false for U_2
at a generic tiling (identity-lift check B1: D_code = 0 but U_2 > 0, matching
(t_-^2-t_+^2)^2/(t_-^2+t_+^2)^2 = 4ρ²(ρ²+n)/(2ρ²+n)² to 3.3e-16; {-s,-s,-s,s}: U_2 = 0, D = 2
> 0 — B3; symmetric tiling: U_2 = 0 — B4).
(iii) ONE deviation from the gatekeeper's snippet wording: the snippet's em-dashes
("— in particular ... —") are replaced by parentheses, because the insert must be ASCII-only
(appendH contains no `---` either, so no LaTeX em-dash idiom is being broken); and the tail
reads "decaying as \(O(1/N)\) below the leading order **in the matched-scale ensembles tested
(numerical)**" instead of the snippet's bare "decaying as \(O(1/N)\) below the leading order"
— the 1/N decay is the s2/s6 numerical observation (slopes -0.965/-0.901), not an exact
identity, so it is scoped and marked (numerical) in the same sentence rather than in a
sentence whose other assertions are exact definitions.

## Replacement 2 (finding 3)

OLD:
```
to \(16q^{2}\) through \(q=32\) give slopes
```
NEW:
```
to \(16q^{2}\) through \(q=16\) and to \(8q^{2}\) at \(q=32\) give slopes
```
Verified: s2b_qwindow.out section (a) grids {4:[64,128,256], 8:[256,512,1024],
16:[1024,2048,4096], 32:[4096,8192]}; CAP_N=8192 default (source line 201-204); slopes
-0.531/-0.499/-0.509/-0.496 unchanged (the q=32 slope is a two-point fit — disclosed).

## Replacement 3 (finding 4)

OLD:
```
for a lognormal scale mixture of coefficient of variation \(0.4\)
```
NEW:
```
for a lognormal per-copy scale mixture whose standard-deviation multipliers have coefficient of variation \(0.43\)
```
Verified: s4b applies `diag(sqrt(t1),sqrt(t2))` with t = exp(N(-σ²/2,σ)), σ² = ln(1.96)
(source lines 102, 113-114): CV(t) = √(e^σ²−1) = 0.9798 (variance multiplier),
CV(√t) = √(e^{σ²/4}−1) = 0.4280 (std multiplier; empirical 0.9790/0.4278). The
gatekeeper's alternative wording "coefficient of variation 0.43 of the per-copy variance
scale" would attach 0.43 to the wrong scale (the variance multiplier's CV is 0.98), so the
second option it offered ("parametrize explicitly" — here: name the multiplier the 0.43
belongs to) was used. s4b left untouched (its docstring "CV-0.4" is script text, not
manuscript text; decision: leave scripts byte-unchanged).

## Replacement 4 (finding 5)

OLD:
```
and exact tiling is realized only on thin families,
```
NEW:
```
and exact tiling is observed, in the tested classes, only on thin families,
```

## Replacement 5 (finding 7)

OLD:
```
at matched iid scales \(|\alpha|/\|w_\perp\|\) decays
```
NEW:
```
at matched iid scales \(|\alpha|/\|w\|\) decays
```
Verified: s6 `dA` = mean|α| / mean‖w‖ with the FULL row vector w (source lines 88-90; the
‖w‖/‖w⊥‖ ratio → 1 since |α|/‖w⊥‖ → 0 as N^{-1/2}, slope unchanged at -0.527). `w` is the
row vector of the Row length paragraph already invoked descriptively in the same insert.

## Hygiene re-scan (patch_r2.py, and independently simulate_apply_077.r2.out)

ASCII-only; one content line + terminal CRLF; 0 × `\ref \eqref \cite \label $ [ ]`;
0 × status/priority/completion/open/derived/programme/critical (any case); exactly one
`\emph{}`; ends "they close nothing in Problem~G."; stale round-1 strings
(`\max_k(e_{(k+1)q-1}-e_{kq})`, `which vanish at tiling`, `through \(q=32\) give`,
`variation \(0.4\)`, `is realized only on thin`) each occur 0 times.
