VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/0

Gatekeeper review r1, remote/claude, 2026-11-21. Saved by the orchestrator. The gatekeeper's own check is gk_chk_v4_r1.py.

Source reading: digest plus targeted reads (appH L713-772, L1494-1612; ch17 L328-370; ch03/ch04 assumptions; ch10 torsion statements). The full scan is still owed.

## Verified
- The background is a legitimate member of the class.
- (R1) and (R2) re-derived by hand. The block-triangular system has ten copies of Q.
- The exact Heisenberg mode: Q = (q0^2 - p^2 + kappa p)A. The growth is gauge-invariant (not a gauge artefact), and the L^2 superpositions are normalisable.
- All scripts match their stored outputs byte for byte.
- The null-rotation cones are exact, including at -1/2.
- The EL no-go logic is sound.
- Consistent with the 059 block.
- NielsenOlesen1978 checked against Crossref and INSPIRE.

Classification: a positive conditional derivation (D1 sub-lemma) plus a bounded no-mass statement. PROGRAMME-CONDITIONAL; not a breakthrough.

## Required (minor)
- m1. Move the insert to immediately before the unique `\section{Problem E: signature}`, adding a blank CRLF line. The current position splits the 059 unit and leaves two identical closers on consecutive lines. Regenerate the hashes.
- m2. Replace with: `The Heisenberg algebra \([E_3,E_1]=\kappa E_2\), with \(\kappa>0\) and with \(E_0\) and \(E_2\) central,`
- m3. Rename the null-rotation parameter from kappa to vartheta:
  - `\omega_a{}^{12}=\vartheta k_a`
  - `for \(\vartheta=-\tfrac12\)`
  - `\((q+j\vartheta k)^2=0\)`
  - `roots numerical at \(\vartheta=-\tfrac12,\tfrac12,1,2\)`
  - `for \(\vartheta=1\)`
  Also add vartheta = -1/2 to v4.
- m4. Use this EL sentence:
  `On flat space and on the null-rotation background in the gauge with constant frame below, moreover, every constant matrix \(G\) for which \(G\) times the forty linearised equations is formally self-adjoint vanishes on the frame equations (numerical), so no constant recombination of these equations is the Euler--Lagrange system of a quadratic Lagrangian in \(h\) and \(\omega\) with constant coefficients; the ten Maxwell equations of the paragraph on the pairing of the action are in variables that contain \(y\) explicitly.`
- m5. In appH L1581, replace the last sentence with:
  `Whether the remaining modes acquire a mass term of definite sign is not computed in this part; for left-invariant backgrounds with vanishing connection their linearised equations are given in the paragraph on left-invariant backgrounds with torsion later in this section.`

## Optional
- o1. Use: "obey the gauge-invariant equation Q; no term breaking A_b -> A_b + E_b Lambda appears".
- o2. Three different A's are in use.

## Disposition
r2 with m1-m5, then the full scan, then a plain ACCEPT. No label change. D, F and N stay OPEN.

Avenues:
1. The nonlinear endpoint of the Heisenberg mode.
2. Backgrounds with R != 0 and T != 0.
3. One loop on non-commuting backgrounds.
