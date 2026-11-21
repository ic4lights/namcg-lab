# Local re-review r1 (remote/claude, 2026-11-18): group C / F / H / I / N

Source reading: digest + targeted reads. No full scan claimed.

## 062 block 2 (appH L3018, "Trace-channel tadpole ... q=0"): AWRR, M3 PRIOR-CLAIM-ERROR (OPEN 0/1)
The determinant-profile identities are verified (ratio 4, q*^2 = 1/2 L sum T_i, the magnitudes).
MAJOR: the text uses the L2974 rigidity, which needs \bar h^{11} negligible, in the pure-trace channel, where that does not hold.
- Replace "so with the recorded terms a background flat at \(q=0\) has \(q_*^2=0\)" with:
  so, for recorded terms that carry \(\sqrt{|g|}\) alone in this channel (\(U_4\); \(U_2\) and the first term only if \(\vartheta\) is held fixed under the wave, since the rigidity recorded above needs \(\bar h^{11}\) negligible and \(\bar h=(t/4)\bar g\) is not negligible along \(y\)), a background flat at \(q=0\) has \(q_*^2=0\)
- Replace "the candidate that could supply the required \(\mathcal M\) without cancelling its own tadpole is the response of the fibre levels to \(\bar h\) in \(v^M-2\sigma^M\), which is recorded as not computed" with:
  the candidates that could supply the required \(\mathcal M\) without cancelling their own tadpole are the terms that depend on \(\vartheta\), the \(\vartheta\)-linear part of \(U_2\) and the fibre levels in \(v^M-2\sigma^M\), and their response depends on how \(\vartheta\) moves with the wave

069 overlap: the text inherits the 049 setting (V=T, c=mu=0 operators on K). It neither repeats nor contradicts the cubic-Hessian error. When 069 is integrated, its c=mu=0 qualifier must also cover L3018/L3020, and its anchor must be re-verified.

## 064 (appH L3020, "Trace-channel response of the fibre part"): AWRR, M3 PRIOR-CLAIM-ERROR (OPEN 0/1)
MAJOR: the displayed tadpole and quadratic formulas are computed on B, the bracket of the Y display. Y is d/d ln chi of the density, not the density.
- The true density level factor is (15/4) th^2 E(D) - th c_J/D + c_J^2/D^2, where E is log-divergent with regulator s_Lambda.
- The true extra tadpole is th(15 th D E - 2 c_J)/(8D), and the quadratic part is th(75 th D E - 8 c_J)/(64D). Both are regulator-dependent.
- The levelwise sign claim is not about T or M.
Required (researcher r2):
- Restate the coefficients either as the t-response of Y, or as density coefficients with s_Lambda stated.
- Remove the sign claim.
- Delete the ds/s sentence.
- Write "Take as response hypothesis that ..." for the contraction rule.
What survives: the first term depends on vartheta, so it is not a sqrt|g|-alone term.
Fix 062 and 064 together, because they take opposite implicit positions on whether vartheta moves with the wave.

## 066 (Problem H, appH L3263-3300): AWRR (OPEN 0/1)
MAJOR: the exponential-linear form holds only to first order.
- Replace "so the single-ladder response ... as anticipated in Chapter~\ref{ch:agenda}." with:
  so to first order in \(g_{\mathrm N}\) the single-ladder response of the conditional lemma takes the form \(1/(1-e^{-b-c\,g_{\mathrm N}})\), the retired exponential-linear family \eqref{eq:appE-exp} at \(\alpha=e^{-b}\) and scale \(1/c\): a linear gap feeds a linear argument into the exponential, as anticipated in Chapter~\ref{ch:agenda}. At every order the conditional lemma decides: the target holds if and only if \(\Delta k=\sqrt{g_{\mathrm N}/g_s}\), which is not analytic at \(g_{\mathrm N}=0\), so no gap analytic in the source strength reproduces it.
- Append " at first order" to the paragraph title.
Minor:
- L3284: the remainder is O(x^{3/2}).
- L3289: qualify "exactly displaced state" with "displacement implemented by a unitary of the local algebra or its commutant".

## 063 (Problem I, appH L3436-3448): ACCEPT
Verified: the weighted-Bohr identity, the toy spectra and the labels. Optional: "(as functions in the Poisson limit)".

## 067 (Problem N, appH L3745-3828): AWRR, M3 PRIOR-CLAIM-ERROR (OPEN 0/1)
MAJOR (L3766-3768, which belongs to 067): the OS framing is wrong.
- Replace "the Euclidean measures ... at finite \(N\), and" with:
  the Euclidean measures of Section~\ref{sec:status-E} give the reflected pairing a strictly negative value on every \(\theta\)-odd invariant polynomial at finite \(N\), so a \(\theta\)-stable test algebra on which it is nonnegative is \(\theta\)-even; since these measures carry no positive-time subalgebra, this is not a failure of the positivity of \cite{OsterwalderSchrader1973,OsterwalderSchrader1975} in its positive-time form and neither supplies nor excludes a Hamiltonian bounded below; and
Minor:
- L3814: replace "conditional on the truncated identity or, for the zero-location statements, on the remainder bound" with "conditional on the truncated identity and, for the zero-location statements applied to a completed kernel \(F+R\), on the remainder bound of the preceding paragraph,".
- L3756: add the momentum/spin decomposition to the hypotheses.
- L3812-3813: remove the doubled blank line.
Verified: the delta-shift identity, the zero at x=0.9088996 (c=1.2), min|F| = 0.822025 on |x|=1, and the spectral sum.

## Group summary
- The erroneous 049 statements are still in the tree at L2978, L2992, L3012 and L3014. Local 069 has to fix them.
- The E-section OS framing at L1617 (title) and L1652-1654 is covered in group3-E.md (060).
- Label changes: none.
