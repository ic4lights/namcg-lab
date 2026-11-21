# Local re-review r1 (remote/claude, 2026-11-18): group E (signature)

Group verdict: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | OPEN: 0/3
Source reading: digest + targeted reads (appH L1570, L1580-1831, L3760-3772; ch17 L394-399, L721-722). No full scan claimed.

## 053-lorentzian-integral-limit-order: ACCEPT
- Local and gpu 053 r3 give byte-equivalent manuscript text (appH_insert and bib_additions identical after line-ending normalisation). Nothing was dropped.
- Local E1 is present at L1570.

## 056-slice-lhs-full-n2-bridge: ACCEPT
- sup over the range = sqrt(2+sqrt2) at theta=1; c0(u) is re-derived.

## 057-gamma-zero-bridge-slice-u-third: ACCEPT
- Gamma0(1/3) = 0.0883883; the fixed gamma<0 extension is a valid derivation.
- Its PRIOR-CLAIM-ERROR on 055 has to be fixed in 055's own paragraph.

## 054-nonpolynomial-observables-lorentzian-n2: AWRR (OPEN 0/1)
1. MAJOR (L1610 vs this branch's L1680-1717). As written, the text suggests the opposite of the proved limit in (v) of the linear-contour paragraph.
   - Replace "there is no analyticity strip and no non-polynomial extension of the limit statement at \(\gamma=0\) off that slice, within the hypothesis class" with "the displayed identity has no analyticity strip in \(k\) and no non-polynomial extension at \(\gamma=0\) off that slice, within the hypothesis class".
   - Insert after "...contours \(\mathcal R_u\), \(\epsilon\to0^+\) last.": "This concerns the right-hand side of the displayed identity and the modulus route, not the existence of the limit: by (v) of the paragraph on linear contours that mix the indices, at \(N=2\) the limit of \(\langle O_k\rangle_\epsilon\) exists and equals \(F_{\mathrm E}(\mathrm e^{\mathrm i\pi/4}k^\mu k_\mu)\) for every real spacelike \(k\) and for every \(k\) with \(\Lambda^{\mathrm T}k\) real on \(\mathcal R_{u'}\), \(0<u'<2/3\), although for some of these \(k\) the commuting-ray contribution grows."
2. minor (L1608, the sentence appended to 053). Replace it with: "The next paragraph sharpens this at \(N=2\), \(\gamma=0\), regulator (A) and the contours \(\mathcal R_u\): the right-hand side diverges in modulus for every nonzero real \(k\) and every \(k\) off one slice, it is unresolved on that slice, and the failure is absent at fixed \(\gamma<0\)."
3. minor (L1610). Replace "numerically like \(\mathrm e^{c(k,u)/\sqrt\epsilon}\) on the sampled range" with "(numerical on the sampled range \(\epsilon\in[0.01,1]\); the rank-one corner estimate of the paragraph on the slice bridge band gives growth at least like \(\mathrm e^{c/\epsilon}\) up to polynomial factors)".
4. minor. Replace "(numerical)" after "extends to \(O_k\) for every \(k\in\mathbb C^{10}\)" with "(derived in the paragraph on the \(\gamma\to0^-\) link below)".
5. minor. Replace "\(\rho_X^2=k^\mu k^\nu\mathcal G_{\mu\nu}\)" with "\(\rho_X^2=\sum_{a=1}^{3}(k^\mu A^a_\mu)^2\)".

## 055-anti-wick-slice-nonzero-k: AWRR, M3 PRIOR-CLAIM-ERROR (OPEN 0/1)
1. MAJOR (L1612). The exponents use gamma_c frozen at its u=0 value. With the R_u coefficient the exponents are independent of u, and the "divergence as gamma->0^-" is an artefact. The script ladder uses a frozen factorised surrogate.
   - Replace "\(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\), gives pointwise modulus growth" with "\(\gamma_{\mathrm c}=\mathrm e^{3\pi\mathrm i/8}r^0/2\) frozen at its value on the Hermitian contour, gives in that frozen-coefficient model (with \(g_{\mathrm{YM}}=1\)) pointwise modulus growth".
   - Replace "In the reduced \(N=2\) integral (regulator (A), contours \(\mathcal R_u\), \(\epsilon\to0^+\) last) with this insertion at pure temporal slice momenta," with "In the reduced \(N=2\) integral (regulator (A), contours \(\mathcal R_u\), \(\epsilon\to0^+\) last) with the factorized surrogate of this insertion along the soft temporal mode, coefficient frozen as above, at pure temporal slice momenta (the exact insertion, evaluated at \(u=0\) for \(\epsilon\ge0.1\) only, gives ratios between \(2.0\) and \(4.1\)),".
2. minor (process language). Replace "the pure-spatial half of the slice is now ray-free" with "the pure-spatial half of the slice has no commuting ray with growth".

## 060-rp-n2-invariant-failure: AWRR (OPEN 0/1)
1. MAJOR (OS framing). Every theta-invariant weight fails on theta-odd functions, and OS positivity is imposed on a positive-time subalgebra. 1 + y0 y1 has a positive pairing.
   - L1651-1655: replace "do not satisfy the reflection positivity of~\cite{OsterwalderSchrader1973,OsterwalderSchrader1975} on the invariant polynomial algebra: the failure sits on" with "are not reflection positive on the full invariant polynomial algebra taken as a \(\theta\)-stable test algebra, a stronger condition than that of~\cite{OsterwalderSchrader1973,OsterwalderSchrader1975}, which is imposed on observables supported at positive time, a subalgebra not preserved by \(\theta\) and without a canonical analogue for a zero-dimensional integral; the same holds for every \(\theta\)-invariant nonnegative weight with a \(\theta\)-odd test function not vanishing almost everywhere. The negative values sit on".
   - L1657: replace "and every invariant mixing time and space under \(\theta\) is excluded from any reconstruction from these measures." with "and no nonzero \(\theta\)-odd invariant lies in any set of test functions on which the reflected pairing is nonnegative."
   - L1570: replace "The positivity taken from field theory already fails on the finite-\(N\) invariant algebra of the Euclidean model: the paragraph" with "On the finite-\(N\) invariant algebra of the Euclidean model, taken as a \(\theta\)-stable test algebra, the reflected pairing is not positive: the paragraph".
   - L1570: replace "; the large-\(N\) field-theory statement remains untested." with "; the positive-time positivity of the large-\(N\) field theory is not tested by this."
2. minor (L1634). Replace "with \(M_{0i}=0\) at any \(N\); constant" with "with \(M_{0i}=0\) at any \(N\), an auxiliary bosonic Euclidean weight that does not appear on that right-hand side; constant".
3. minor (L1570). Replace "with the content above" with "with the fermion content of~\cite{IKKT1997}".

## Group-wide
- Six consecutive "Problem~E remains open and PROGRAMME-CONDITIONAL" closing sentences (L1608-1675) should be reduced to one.
- Outside this group: L3766 repeats the OS framing and needs the same rescoping as 060 finding 1.
- Label changes: none. Problem E stays OPEN / CRITICAL PATH for the matrix-derived label / PROGRAMME-CONDITIONAL.
