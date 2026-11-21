VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/1

(Gatekeeper review r2 of the combined 054-055 package, remote/claude, 2026-11-18. The orchestrator saved it here, because the gatekeeper is read-only. The gatekeeper's normalisation check is copied as gk_normcheck_r2.py.)

## Source reading
Digest + targeted reads. The full scan was NOT completed. The digest is CURRENT with dirty-chapters: yes.
What was read instead:
- the whole chapters/ and bib/ diff against HEAD (Problem A L28-87, Problem I L3125-3138, ch14 L227, four bib entries; none of it in E or ch17);
- the Problem E entry in full (appH L1509-1690), ch17 L394-399 and L700-730, and ass:lorentzian (ch04 L321-328);
- a keyword scan of all 30 chapter files (not a reading).
A full scan, or an orchestrator ruling on protocol 3(d), is owed before a final ACCEPT.

## Earlier findings (group3-E.md)
- All closed: 054/1-5, 055/1-2 and the group closers.
- Researcher departures accepted: "below"; "the identity is unresolved"; the Pfaffian-window rewording; the Cauchy-Binet relabel; the end-of-ledger placement.
- 056 change confirmed: only its closer is deleted.
- 057 change confirmed: only the tail is replaced (first 3303 chars identical).
- The moved correction is NOT formula-identical (the /2 on the coefficient was corrected, "in gamma_c" was added, among others). This should have been disclosed.
- Scripts re-run with python -I. Their output matches the stored .out files, check_r2 gives 18 PASS, and the anchors occur once each.

## New findings
1. MAJOR, PRIOR-CLAIM-ERROR (accepted 057 text, now in 055). The soft-mode exponents are a factor 2 too small relative to Definition (A), because Tr(a sigma3/2)^2 = a^2/2 is not carried into Q.
   - Correct values: r0^2/(8 sqrt2 eps); -g^2 r0^2/(4 sqrt2 |gamma|); frozen cos(...)/(8 eps) and g^2 sin(...)/(4|gamma|).
   - Quadrature check: |I| = 7.41732 against the corrected 7.41732 and the stated 6.6667.
   - Q is undefined in the text, and the reduced-model numbers (0.044/eps, eps=3e-3, gamma=-0.2, -0.05) are in model units without saying so.
   - Required: (a), (b), and either (i) convert the numbers or (ii) label them with (c). The same label should cover the eps in [0.01,1] range in 054.
2. minor. E1: the retained "It does not exclude..." now reads ambiguously. Fix with (d).
3. minor. E3 (056) has the same k clash between degree and momentum. Fix with (e).
4. minor. E2/054: the proxy does not show "without bound". Fix with (f).
5. minor. Disclosure only (see above).
6. minor, recommended. E4 (057): the beta inequality points the wrong way at eps > 0. Fix with (g).

## Corrected snippets (anchors verified unique in E2/E3/E4)
(a) In E2/055, replace
`For \(r^0\ne0\) the one-dimensional branch integral \(\int_{\mathbb R}\mathrm e^{-Qa^2}\,2\cos(\gamma_{\mathrm c}|a|)\,\mathrm da=2\sqrt{\pi/Q}\,\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\), \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\) frozen at its value on the Hermitian contour, gives in that frozen-coefficient model (with \(g_{\mathrm{YM}}=1\)) pointwise modulus growth \(\mathrm e^{{(r^0)}^2\cos(3\pi u/4-\pi/4)/(16\epsilon)}\) for the soft temporal mode at \(\gamma=0\), saturating as \(\epsilon\to0^+\) at fixed \(\gamma<0\) to a constant of order \(\mathrm e^{{(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)}\),`
with
`For \(r^0\ne0\) write the soft temporal mode as \(\tilde A_0=a\sigma^3/2\), on which the regulator and the mass give \(\mathrm e^{-Qa^2}\) with \(Q=\tfrac12\mathrm e^{-3\pi\mathrm iu/4}(\epsilon-\mathrm i\gamma/(2g_{\mathrm{YM}}^2))\). The one-dimensional branch integral \(\int_{\mathbb R}\mathrm e^{-Qa^2}\,2\cos(\gamma_{\mathrm c}|a|)\,\mathrm da=2\sqrt{\pi/Q}\,\mathrm e^{-\gamma_{\mathrm c}^2/(4Q)}\), with \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\) frozen at its value on the Hermitian contour, gives in that frozen-coefficient model pointwise modulus growth \(\mathrm e^{{(r^0)}^2\cos(3\pi u/4-\pi/4)/(8\epsilon)}\) for the soft temporal mode at \(\gamma=0\), saturating as \(\epsilon\to0^+\) at fixed \(\gamma<0\) to a constant of order \(\mathrm e^{g_{\mathrm{YM}}^2{(r^0)}^2\sin(3\pi u/4-\pi/4)/(4|\gamma|)}\),`

(b) Replace
`with this contour-dependent coefficient in \(\gamma_{\mathrm c}\) the soft-mode growth exponent at \(\gamma=0\) is \({(r^0)}^2/(16\sqrt2\,\epsilon)\) and the fixed-\(\gamma\) saturation exponent is \(-g_{\mathrm{YM}}^2{(r^0)}^2/(8\sqrt2|\gamma|)\)`
with
`with \(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i(1-u)/8}r^0/2\) the soft-mode growth exponent at \(\gamma=0\) is \({(r^0)}^2/(8\sqrt2\,\epsilon)\) and the fixed-\(\gamma\) saturation exponent is \(-g_{\mathrm{YM}}^2{(r^0)}^2/(4\sqrt2|\gamma|)\)`

(c) Option (ii) only, after confirming that the code's a_k are the Pauli components. Replace
`against the pointwise corner value \(0.044/\epsilon\) at \(r^0=1\))`
with
`against the corner value \(0.044/\epsilon\) at \(r^0=1\) of the same reduced model; in it the soft-mode Gaussian is \(\mathrm e^{-Qa^2}\) with \(Q=\mathrm e^{-3\pi\mathrm iu/4}(\epsilon-\mathrm i\gamma/2)\), twice the \(Q\) above at \(g_{\mathrm{YM}}=1\), and the values of \(\epsilon\) and \(\gamma\) quoted in this sub-block are in that normalisation)`

(d) In the E1 application, replace ` It does not exclude a real-time reading obtained by continuation.` with ` The result above does not exclude a real-time reading obtained by continuation.`

(e) In E3, replace `so the \(k<14\) Pfaffian window applies with the \(k=0\) majorant` with `so the bound along the flat directions applies with polynomial degree \(0\)`, and replace `by dominated convergence within the window` with `by dominated convergence under that bound`.

(f) In E2/054, replace
`grows without bound as \(\epsilon\to0\) (numerical, for a large-radius \(\cosh\) proxy of \(|O_k|\) in a reduced chart, on the sampled range \(\epsilon\in[0.01,1]\); the rank-one corner estimate of the paragraph on the slice bridge band, applied along a ray with \(b_u(\hat\rho;k)\ne0\), gives growth at least like \(\mathrm e^{c/\epsilon}\) up to polynomial factors)`
with
`grows without bound as \(\epsilon\to0\): the rank-one corner estimate of the paragraph on the slice bridge band, applied along a ray with \(b_u(\hat\rho;k)\ne0\), gives growth at least like \(\mathrm e^{c/\epsilon}\) up to polynomial factors (a large-radius \(\cosh\) proxy of \(|O_k|\) in a reduced chart increases on the sampled range \(\epsilon\in[0.01,1]\), numerical)`

(g) Optional. In E4, replace `with \(\beta(\epsilon,\gamma)\ge|\gamma|\sin(3\pi u/4)/(2g_{\mathrm{YM}}^2)\), and the ray region contributes at least` with `with \(\beta(\epsilon,\gamma)\to|\gamma|\sin(3\pi u/4)/(2g_{\mathrm{YM}}^2)\) as \(\epsilon\to0^+\), and in that limit the ray region contributes at least`

## Established / open
- Derived:
  - the N=2 eigenvalue identities;
  - the modulus divergence of the RHS off the slice;
  - existence of the limit by (v);
  - the commuting-ray sign lemma;
  - the fixed gamma<0 extension;
  - the modulus no-go for bridges;
  - u-independence of the true-coefficient exponents (after finding 1).
- Model or numerical: the frozen-coefficient exponents, the surrogate ladder, the cosh proxy.
- Open: the slice at k != 0 with r0 != 0, the gamma -> 0^- bridge, N >= 3, N -> infinity first, and the signature itself.
- Problem E stays OPEN / CRITICAL PATH for the matrix-derived label / PROGRAMME-CONDITIONAL. No label change.

Disposition: researcher r3 applies (a)-(f), and (g) if accepted. Re-review with a full scan follows. E1-E4 are integrated jointly.
