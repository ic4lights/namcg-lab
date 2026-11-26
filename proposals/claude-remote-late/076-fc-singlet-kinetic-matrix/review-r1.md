VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1
Gatekeeper r1 review, remote/claude, 2026-11-22. Saved by the orchestrator.

Source reading: digest + targeted reads (appH L3002-3165, L548-566, L700-714, L1905-1912; ch17 C, F). The full scan is owed under 3(c)/(d).

## Verified
- s1 and s2 reproduce. apply_and_build: pre 8aed4519, post deec6c35, 426 pp, clean.
- Re-derived by hand:
  1. The Taylor form and R formula; the kinetic matrix; no first-order static term (antisymmetric divergence along y0).
  2. Source charges: 3 on T-4PT for all beta_K. The yy channel alone does not solve the static equations.
  3. The Schur complement r/(2 - lambda q^2), equal to r/2 at q=0 (relies on H_n, which is stated).
  4. Isotropy and the ratio (1-beta)/(1+beta). No long-range claim.
  5. The chi criterion; A cancels.
  6. The bound. det M(0) = -r(2mu+r). Under H_K+, exactly one positive root, with healthy residue sign. General entries give the constant mu - (b-r)^2/(nu-2r). Fierz-Pauli form 4m^4 q^2(3eps1^2 + 2eps1 eps_y): indefinite.
  7. E2 is accurate.
  8. Placement and closer OK.

## Findings
1. MAJOR, E1 (L3138): the new text drops hypothesis H_K+. Replace the E1 new text with:
(on two other realisations of this channel the tree terms supply no positive constant, and on the singlet sector, for a positive-definite kinetic matrix of the singlets, they supply one only together with a static pole of the tachyonic sign in the neutral singlet; paragraphs on the tree non-derivative terms and on the kinetic matrix of the static scalar singlets below)
2. minor: zeros of det M vs poles of the response.
   - Replace "the static response has exactly one further pole, at \(q^2>0\), of the tachyonic sign" with "the static form has exactly one further zero, at \(q^2>0\), at which the response to any source not orthogonal to its null vector has a pole of the tachyonic sign".
   - Replace "a static response without a pole at \(q^2\ge0\) needs" with "a static form without a zero at \(q^2\ge0\) needs".
3. minor: replace "through \(U'_{\mathrm{loop}}\) and \(U_{\chi\chi}\), the tree data of \(K\)" with "through \(U'_{\mathrm{loop}}\) and \(U_{\chi\chi}\), the tree and one-loop data of \(K\)".
4. Procedural: full scan.

## Scope
- Exact: the frozen-symbol kinetic matrix, and the charges (with a supplied coupling).
- Conditional on H_n: the q=0 constant and the chi criterion.
- Bounded no-go under H_K+.
- Nothing DERIVED. C, F, N OPEN.

Avenues:
1. Relax H_K+ (the one-loop induced singlet kinetic matrix; EH-type, indefinite).
2. The yy loop entries (mu > 0 necessary).
3. A non-frozen profile.
4. General b, nu (low value).
5. A derived beta_K.

Consequential enough to integrate once revised.

## Disposition
r2 with Findings 1-3 verbatim, then the full scan.
