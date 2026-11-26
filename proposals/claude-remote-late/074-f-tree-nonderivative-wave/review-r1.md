VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3

Gatekeeper r1 review, remote/claude, 2026-11-22. Saved by the orchestrator.

Source reading: digest + targeted reads (appH L2640-2669, L2829-2888, L2977-3122, L548-556, L700-712, L1880-1886; ch17 C, F; ch03 eq:Smatrix). The full scan is owed under 3(c).

## Verified
- All scripts reproduce, including the full s2. apply_and_build: pre 29ac2a63, post 55c14afc, 420 pp, clean.
- Re-derived independently:
  - channel realisation (sigma1 = -eps, direction y0 y0);
  - degree argument, valid at finite N (the bilinear is a SUPPLIED input, L2651; the matter fields must vanish at the background);
  - localisation identity (unique, removes the ambiguity);
  - level-one values;
  - singlet sector (eigenvalues 6 and -2, stationary value vartheta varpi/2m^2, a maximum).
- Placement and closer OK.

## Findings
- M1 MAJOR: the identity (L3107-3113) works at equal weights with a pointwise elimination of all fibre harmonics. Neither realisation computed here is shown to be that profile, and the two give different tree forms. So the insert and E1-E3 overclaim that the item is settled for the identity. Fix: replacement text.
- M2 MAJOR: on the level-one amplitude, +3varpi/(m^4 k^2) is positive and dominates at small k. "Yukawa sign available only via the singlet" is not established; restrict the claim to "no positive constant at q=0".
- M3 MAJOR: the leading symbol's -3varpi/m^2 is not in the displays L3051/3055/3111 (phase average of the induced density alone). State this.
- m1: rename E_a (field equation) to \mathsf E_a, and say L in "normalisation" is the identity's constant L.
- m2: T_tree = 0 in every channel follows from E=0 (covered by the replacement).
- m3: "supplied bilinear term"; "with the matter fields at their vanishing background".
- m4: E3 should keep the item, qualified.
- m5: in the singlet sector, say the positive value comes from extremising over a direction with negative non-derivative term (eigenvalue -2, curvature -4).
- m6: correct the overclaims in proposal-r1 Results 2 and 3.

## Replacement texts (verbatim)
Channel paragraph. Replace "Hence \(T_{\mathrm{tree}}=C_{\mathrm{tree}}=0\) in this realisation: ... do not cancel the tadpole of \(U_4\) in this channel." with:
Hence \(T_{\mathrm{tree}}=C_{\mathrm{tree}}=0\) in this realisation. That \(T_{\mathrm{tree}}=0\) holds in every realisation, since the background is stationary, so the tree terms do not cancel the tadpole of \(U_4\) in any channel; that \(C_{\mathrm{tree}}=0\) is a property of this realisation, on which the other entries of the identity of the preceding paragraph, obtained with the background torsion held, are not computed.

After "...the two realisations do not have the same tree form." add:
These values are for the level-one profile \(\hat q\cdot T\). The identity of the preceding paragraph is stated at equal weights with all fibre harmonics eliminated at each fibre point; on that profile \(\langle\mathsf w\cdot L(\mathsf w)\rangle\) contains the fibre derivatives of \(L\) and is not computed. The reduced form of the paragraph on the response of the scale of \(K\) is the phase average of the induced density alone, so the term \(-3\varpi/m^2\) of the leading symbol of the tree form is not among the terms of the displays of the two preceding paragraphs.

Consequence paragraph. Replace with:
\emph{Consequence.} On the two realisations of the channel along \(y^\mu y^\nu\) computed here the tree terms supply no positive constant at \(q=0\): they vanish on the rescaling, and on the level-one amplitude the leading symbol adds a negative constant and the non-derivative term is positive but of order \(k^{-2}\), whose effect on the static response at small \(k\), where the frozen base point is not controlled, is not determined. The tree non-derivative term therefore depends on the fibre profile of the wave, and its value on the profile of the identity of the preceding paragraph is not computed. A positive constant at \(q=0\) of tree strength is obtained here only on the singlet sector, at the stationary value over the \(\sigma_1\)-neutral singlet, whose own non-derivative term is negative; the identity of the preceding paragraph, written for the channel along \(y^\mu y^\nu\), does not contain it.

Scope sentence:
- after "They do not compute" insert "the tree non-derivative terms on the profile of the equal-weight elimination,";
- replace "with the bilinear term" with "with the supplied bilinear term and the matter fields at their vanishing background".

E1:
The terms that cancel the tadpole of \(U_4\) at \(q=0\), any term with the same fibre dependence and the tree non-derivative terms on the profile of the equal-weight elimination are not computed (for two other realisations of this channel see the paragraph on the tree non-derivative terms below), and a long-range form needs them or \(\hat U\to0\);

E2:
the part of the first term with the fibre flux, at first and at second order, and the tree non-derivative terms of the wave on the profile of the equal-weight elimination, which the leading symbol of the tree form drops, none of which is computed (on two other realisations of this channel the tree terms supply no positive constant; paragraph on the tree non-derivative terms below).

E3:
the term of \(U_2\) proportional to \(W_R\), the tree non-derivative terms on the profile of the equal-weight elimination, higher loops or the fibre Laplacian

## Scope
- Exact: the localisation identity; L(kappa T); eigenvalues {6,-2}; one-component flatness at finite N; T_tree = 0 in every channel.
- Conditional: C_tree = 0 on the rescaling; the level-one value; the singlet value.
- Open: the identity's own profile; which channel/singlet is selected; the loop items.
- Classification: a derivation-grade partial computation that shows the realisation dependence. Not a breakthrough. C, F, N stay OPEN.
- Avenues:
  1. the identity's own profile (non-pointwise elimination, including the fibre-derivative part of L);
  2. the singlet kinetic matrix plus the matter coupling;
  3. one-loop profiles on the rescaling;
  4. the L3113 loop items;
  5. other bilinear weights / cubic on M.

## Disposition
r2 with the texts above plus m1-m6. Then the full scan. Do not integrate r1.
