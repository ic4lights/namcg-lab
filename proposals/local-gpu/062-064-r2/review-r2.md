VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: PRIOR-CLAIM-ERROR (gpu-line text only) | PROGRESS: improving | OPEN: 0/2

Gatekeeper review r2, remote/claude, 2026-11-21. Saved by the orchestrator.

Source reading: digest + targeted reads (appH C L548-712, F L1821-1842 and L2949-3046; ch17 C, F, order and criterion). No full scan.

## Checks
- verify_r2 identical. apply_and_build_r2: pre a7f1492a, post 112b485c, clean build.
- Re-derived and VERIFIED:
  - point 1, channel along y^mu y^nu; the group4 062-M3 objection dissolves;
  - point 2, identity, phase average and convention chain; (L/2m^4)U_4 = -q_b^2;
  - point 3, q_*^2|_chi < 0;
  - point 5, vartheta resolution;
  - point 6, density coefficients, which agree with group4.
- The sample does NOT support a sign change: at s_Lambda D = 3 the exact value is positive, and the crossings lie outside the validity range.
- Block C checked against ch17.
- Earlier findings: group4 062-b2 M3 closed; 064 M3 closed; group2 062-b1 applied.
- Ruling on 3(c): block C restates a critical-path target in a Missing step, so it is a scope statement and 3(c) APPLIES. A full scan is required.

## Findings
1. MAJOR: the obstruction's list omits the tree non-derivative terms of the wave (appH L2998, L2947). Fix with F1 and F2.
2. MAJOR: the "change of sign with s_Lambda" rests on a point outside the truncation's validity. Fix with F3 and F4.
3. minor: F5 (coefficients of sigma_1).
4. minor: F6 (q^2 below m_chi^2).
5. minor: C1, follow the ch17 wording.
6. optional: "vartheta-dependent coefficients"; note that at stationarity the sign of U-hat does not decide the first pole.
7. PRIOR-CLAIM-ERROR ruling: gpu-accepted 062 block 2 is WRONG. It counts U_4 twice, mixes parametrisations, and the claim "pole at q^2=q_b^2" is false. No impact on this branch, because the text is not in chapters/ or main. It matters only if the author merges the gpu-line appH, which must NOT carry that paragraph.

## Corrected snippets (verbatim)
F1: replace `and the tree term carries \(\rho_M\), which does not respond at fixed \(\chi\).` with `and the tree potential \(\rho_MV_{\mathrm t}/g^2\) carries \(\rho_M\), which does not respond at fixed \(\chi\).`

F2: replace `within the recorded content these are the second-order parts of \(U_2\) and of the fibre-constant part of the first term, and the part of the first term with the fibre flux, at first and at second order, none of which is computed.` with `within the recorded content these are the second-order parts of \(U_2\) and of the fibre-constant part of the first term, the part of the first term with the fibre flux, at first and at second order, and the tree non-derivative terms of the wave, which the leading symbol of the tree form drops, none of which is computed.`

F3: replace `, whose value and sign depend on \(s_\Lambda\), and that of \(U_2\) exceeds it by \(p\,U_2\);` with `, whose value depends on \(s_\Lambda\) through \(E_1\), the bracket at each level being positive exactly when \(E_1(s_\Lambda\mathcal D)>2c_J/15\vartheta\mathcal D\), and that of \(U_2\) exceeds it by \(p\,U_2\sigma_1\);`

F4: replace `The identity at a stationary background is exact for these forms, the density of the first term is exact for the level form at the stated limit, and the change of sign with \(s_\Lambda\) is numerical at sampled values.` with `The identity at a stationary background is exact for these forms, and the density of the first term is exact for the level form at the stated limit.`

F5: replace `exceeds the profile of \(\sqrt{|g|}\) by \(-p\,(` with `exceeds the profile of \(\sqrt{|g|}\) by \(\sigma_1\) times \(-p\,(`; and replace `the response of \(Y\) is finite, with the summand` with `the coefficient of \(\sigma_1\) in the response of \(Y\) is finite, with the summand`.

F6: replace `With the exchange of \(\chi\) of the preceding paragraph, the denominator` with `With the exchange of \(\chi\) of the preceding paragraph, for \(q^2\) below \(m_\chi^2\), the denominator`.

C1: replace `the gauge-fixed quadratic scalar operator` with `the full quadratic scalar operator`; and replace `and its pole mass as a derived output,` with `and its pole mass, or a ratio \(m_\psi/v\), as a derived output,`.

## Classification
A consistency correction plus a bounded obstruction that redirects C/F to named computable items. Not a missing-step derivation. Do not spawn further edges ahead of D1.

Avenues, best first:
1. tree non-derivative terms of the wave;
2. fibre-level and flux response in the yy channel;
3. second-order U_2 / first term;
4. V != T;
5. third-term q_b^2;
6. fix p.

No label change. C, F and N stay OPEN.

## Disposition
Researcher r3 with F1-F6 and C1, then the 3(c) full scan, then plain ACCEPT.
