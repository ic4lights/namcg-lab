SME-SCOUT: 10 routes | TOP: B:Lorentz-Noether (Jacobson-Mohd eqs 46-49) / Elgood-Ortin eq (6.1)-(6.2) entropy density for the independent so(3,1) bundle connection, with Omega treated both as independent and as composite in the leaf; F:spectral channel decomposition with transverse/ghost cancellation (Hattori-Itakura-Ozaki 2001.06131 eqs 65, 70, 76-78) plus Bastianelli et al 2507.15943 eqs 4.20, 4.28-4.33 as the analytic-continuation template; B:classify the surviving R_Sigma/Weyl residue as Euler-type (topological after integration) versus Weyl-type, using Jacobson-Mohd Sec V.2 | EMERGENCE-RISK: low

(Saved verbatim by the orchestrator; the SME agent is read-only. Advice only. No derivations, no manuscript text.)

# SME scout: torsion/connection entropy assignment (B) and spectral vector sector (F)

## Summary (10 lines)
1. The cleanest published precedent for "entropy of a non-Riemannian invariant of an independent or torsionful connection" is the Lorentz-Lie Noether-charge construction: Jacobson-Mohd 1507.01054 eqs (46)-(49) for first-order gravity, and Elgood-Meessen-Ortin 2012.14892 eq (6.1)-(6.2) for the torsionful R_(-)^2 (Yang-Mills-type) term of the heterotic action.
2. In both, the entropy density is the binormal contraction n^{ab} with dL/dR^{ab} of the connection, taken with a Lorentz momentum map. It is not a Levi-Civita Riem derivative. This is the structure behind tau_Omega, so it supports the gatekeeper's "variable-independent Iyer-Wald" avenue.
3. A Wald-type term linear in Omega_12 cannot by itself supply a Weyl-tensor coefficient 2 kappa_X. Two questions must be separated: Omega as independent field, or Omega as a composite of the leaf data.
4. Hung-Myers-Smolkin 1101.5813 is a standing no-go: bare Wald is not the entanglement entropy in general. Dong 1310.5713 and Camps 1310.6659 add K^2 terms with d^2L/dRdR. These vanish on totally geodesic Sigma, so they cannot rescue a mismatch at the 029-031 hypotheses.
5. The only published "torsion enters the log term" result, Dordevic-Gocanin 2602.12197, is a heuristic substitution R -> R^(RC) with no replica derivation. The authors call it hard to justify. Treat it as a caution, not support.
6. Holst terms drop out of the entropy (Jacobson-Mohd Sec V.2, eq 52; Durka 1111.0961). Euler terms give chi(Sigma). This points to the R_Sigma-proportional residue being topological after integration. That is a question to test, not a result.
7. F: the structure 2[cosh + cos] and the ghost cancellation are in Hattori-Itakura-Ozaki 2001.06131 eqs (65)-(70). The Nielsen-Olesen tachyon contour is explicitly left open by those authors (eqs 76-78).
8. Zeta and heat-kernel definitions of Im W differ (Pioline-Troost hep-th/0501169 eqs 85-90 versus eq 68). The vacuum choice must be stated.
9. No IKKT-specific treatment of the electric-field Zeeman vector instability was found for 2024-2026. Newton-constant progress beyond earlier scouts: none found (Frenkel-Hartnoll 2301.01325 is the nearest, 2023).
10. Emergence risk: low for all routes. Every route uses a connection or bundle curvature built from matrix data, never a background metric.

## 0. Reading mode and trust
- Repository: digest + targeted reads. I read ledger entries 028-032 in full, the head of proposals/033-log-content-scan/review-r1.md (verdict, claim, checks), and the openings of the five earlier scouts. I read no chapter files.
- Literature: each ID below was opened live on its arXiv abstract page, or on an arXiv/ar5iv HTML page. The fetch tool paraphrases, so equation numbers are as reported by the tool. Re-open each paper before quoting an equation in the manuscript.
- "Abstract only" means I read the abstract page. "Text (partial)" means I read an HTML page, in some cases only the first ~100k characters.
- Not read at all: any paper marked "not independently verified" below.
- Not repeated from earlier scouts: Casini-Huerta/Fursaev-Miele gluing; Steinacker-Tran and Manta-Steinacker-Tran character supertrace; Troost locus; Larsen-Wilczek; Herzog-Nishioka; Jing-Niu-Xian; Donnelly-Wall/CHR edge modes; Solodukhin 1104.3712 eq (70).

## 1. Literature results by requested topic

### 1.1 Entropy functionals with torsion or an independent connection

| Paper | Read | What it gives (relevant to B) |
|---|---|---|
| Jacobson-Mohd, PRD 92, 124010, arXiv:1507.01054 | Abstract + text (partial) | First/second-order orthonormal frame formalism. Entropy is the Noether charge of diffeo + local Lorentz (Lorentz-Lie derivative). Eqs (46)-(49): S = (2pi/hbar) oint Qhat^K, Q^K = (i_xi omega - lambda_xi)^{ab} ^ dL/dR^{ab}, with Qhat^K = -kappa n^{ab} ^ dL/dR^{ab} for a regular frame. Sec V.1 on torsion: torsionful solutions can exist for Lovelock in D>4, with known examples having vanishing Noether charge. A general torsion contribution is left open. Sec V.2, topological terms: Holst drops out (eq 52, since the binormal is orthogonal to the surface), Euler gives chi(Sigma), Pontryagin gives 0. Nieh-Yan not discussed. |
| Elgood-Meessen-Ortin (authors per my recollection, not confirmed on the page I opened), arXiv:2012.14892 | Abstract + text (partial) | Heterotic action, first order in alpha'. Entropy eq (6.1): the R^(0)_(-)^{ab} n_ab term sits beside the Einstein term. Torsionful curvature squared, a Yang-Mills-type term in the Lorentz connection Omega_(-) = omega - H/2, contributes (alpha'/2) e^{-2phi} *R_(-)^{ab} n_ab. The Lorentz Chern-Simons piece enters as a Lorentz-covariant momentum map Pi_n with d Pi_n = R_(-)^{ab} n_ab (eq 6.2). The naive replacement Omega n is not covariant (eq 7.3). Closest published analogue of tr Omega^2 for a non-Levi-Civita connection. |
| Coincident GR, arXiv:2203.13914 | Text (partial) | Wald entropy with an independent torsion-free connection: Thm III.8, eq (61), S = 2pi oint X^{cd} b_{cd}. Appendix E extends the Noether charge to torsionful connections (I did not read the appendix). Remark III.16: non-metricity does not enter the entropy density directly in their solution. The 2pi versus 1/(2pi) prefactor between eqs (61) and (78) is unreconciled, so check normalisation. |
| Dordevic-Gocanin, arXiv:2602.12197 | Abstract + text | Holographic EE in 5D Chern-Simons gravity with torsion: replace R_Sigma by its Riemann-Cartan value. This gives a log term proportional to torsion squared (eqs 18, 21, 22, 32). No replica method. The authors say the prescription is "hard to justify" in general and that the RC functional lacks the right extremal surface (eqs 29-31). The only 2026 result on torsion and EE log terms. |
| Durka, arXiv:1111.0961 | Abstract | First-order Noether charges with Holst and topological terms. No Immirzi dependence except AdS-Taub-NUT. |
| Dong 1310.5713; Camps 1310.6659 | Abstract | General Riemann-dependent L: Wald plus extrinsic-curvature terms with d^2L/dRdR. Reduces to Jacobson-Myers for Lovelock. |
| Hung-Myers-Smolkin 1101.5813 | Abstract | Wald's formula does not in general give the entanglement entropy. Lovelock prescription depends on the intrinsic curvature of the surface. |
| Lewkowycz-Maldacena 1304.4926 | Abstract | Smooth-replica argument behind Dong/Camps. |
| Tachikawa hep-th/0611141 | Abstract | Wald entropy with gravitational Chern-Simons terms. Standard reference for non-covariant-looking terms needing extra care. |
| Frolov-Fursaev hep-th/9703178; Frolov-Fursaev-Zelnikov hep-th/9607104 | Abstract | Induced-gravity BH entropy versus UV-divergent entanglement entropy: they differ by a Noether-charge surface term Q for non-minimally coupled fields. This is the same kind of gap as sigma_fs + C_b + C_Omega in 031. |
| Puntigam-Soleng gr-qc/9604057 | Abstract | Einstein-Cartan strings: delta-valued curvature (disclination) and torsion (dislocation) are distinct defect types. Relevant to the uniform versus Hodge distribution of Omega_delta in 031. |
| Shapiro hep-th/0103093 | Abstract | Review of torsion, heat-kernel/a_2 and anomalies with torsion. Goldthorpe/Obukhov/Nieh-Yan a_2 computations are named in the search summary only (not independently verified). |

Not found, after several queries (arXiv API plus WebSearch):
- A published Dong/Camps functional with torsion or an independent connection.
- A replica or conical computation of the log coefficient with torsion.
- Any statement that torsion-squared or Nieh-Yan terms contribute to EE.
- The Dirac log-coefficient anomaly with torsion.

### 1.2 Spectral, zeta and Schwinger definitions with unstable modes

| Paper | Read | Content |
|---|---|---|
| Hattori-Itakura-Ozaki, arXiv:2001.06131 | Text (partial, first ~100k characters) | Gluon proper-time representation. Lorentz-index trace gives 2[cosh(2v a s) + cos(2v b s)], eq (65). Longitudinal and transverse pieces with the ghost subtracted, eqs (70a,b). Zeeman-shifted Landau spectra, eqs (72)-(75). Vacuum persistence as a sum over Landau levels via poles, Sec III.3 eqs (52), eq (79)-(80) for gluons. Longitudinal gluon and ghost cancel; the Im part comes only from transverse modes. Nielsen-Olesen tachyon: closing the contour above gives a suppressed result (eq 77); closing below with continuation to negative mass squared gives a growing result (eq 78). The authors say eq (78) seems more sensible but they have no clear mathematical reason, and they list it as open. The text is inconsistent on the tachyon mass between Secs IV.2 and IV.3 (-\|v b\| versus -\|v a\|). |
| Bastianelli-Fecit-Miccichè, arXiv:2507.15943 | Text (partial) | Massive charged spin-1 worldline. Eq (4.20): Euclidean Lagrangian with bracket [1 - 2cosh(2qTK+) - 2cos(2qTK-)] over sinh(qTK+) sin(qTK-). Electric case, eqs (4.28)-(4.33): poles at T = -i pi n/(qE), n>=1, with n=0 excluded (fn 10). Im L = (3/16pi^3)(qE)^2 sum (-1)^{n+1} e^{-m^2 pi n/(qE)}/n^2, rate three times scalar. Defined by analytic continuation. No spectral definition. No Nielsen-Olesen or pure-magnetic discussion, though the structure shows K+ = B, K- = 0 for pure B. |
| Nikishov, hep-th/0104019 | Abstract | W boson g=2: for E only, Bogoliubov coefficients are polarisation independent and equal to scalar; with collinear E and H, aligned spin gives m^2 -> m^2 +/- 2eH. A spectral (in/out) definition exists for E-only. |
| Pioline-Troost, hep-th/0501169 | Text (partial) | Zeta definition W = -zeta'(0). B -> e^{i theta}E continuation, eq (84). Sub/supercritical split by sign of w~(0), eqs (85)-(89). Im W from a density of states, eq (90): two saddles with actions 2pi(E +/- Delta). The Schwinger-time result (eq 68) has only one saddle. Quote: the two are "equally valid, but for different choices of vacua and boundary conditions." |
| Fucci, 1105.5624 | Abstract | Real and imaginary parts of the Hurwitz zeta function at imaginary argument, via polylogarithms. Useful for closed forms. |
| Cho, hep-th/0301013 | Abstract | Argues colour-reflection invariance excludes the tachyon from the loop. Contested; gauge-theory specific. |
| Vercauteren-Verschelde, 0712.0570; Kondo, 1309.2337 | Abstracts | Dynamical gluon mass or a functional RG argument removes the Nielsen-Olesen imaginary part. Non-perturbative; not a one-loop definition. |
| Muramatsu, arXiv:2605.03611 | Abstract | IIB matrix model: supersymmetry-constrained nontrivial backgrounds are (anti-)self-dual and require Euclidean signature. |
| Anagnostopoulos et al., arXiv:2604.19836 | Abstract | Complex Langevin on Lorentzian IIB with supersymmetric deformation: (3+1)D expanding space. |

IKKT-specific: I found no 2024-2026 paper that treats the constant-electric-field vector Zeeman growth or a Nielsen-Olesen mode in the Steinacker-type one-loop calculation. This is a negative result from the search and may not be exhaustive. Battista-Steinacker 2310.11126 and the JHEP02(2025)031 paper were seen only through search summaries: not independently verified.

### 1.3 Newton constant or entanglement-area relations in matrix models
- Beyond the earlier scouts I found nothing that derives G_N from entanglement in IKKT-type models.
- The nearest results are older or only adjacent:
  - Frenkel-Hartnoll 2301.01325 (abstract): Gauss-law entanglement near a fuzzy sphere gives an area law with coefficient set by an emergent Maxwell coupling, not by a Newton constant.
  - Allouche-Dou 2609.10027 (abstract): scalar phi^4 on fuzzy spaces; the interaction gives a non-area bulk entropy and an IR-sensitive zero mode. A caution about what "area" means on fuzzy leaves, not a G result.
- Steinacker's review 2609.08955 is already known from earlier scouts.
- NAMCG's A-versus-T comparison is ahead of the matrix-model literature on this specific point.

## 2. Route map for B: Weyl/torsion entropy assignment

Framing, using the 033 review: the T-side coefficient has tr Omega^2 equal to twice its Levi-Civita value, giving a Weyl term 2 kappa_X. The replica side uses the Wald cross-term rule on the metric Riemann tensor only.

### B-R1 (rank 1). Lorentz-Noether entropy for the bundle connection
- **Papers and equations:** Jacobson-Mohd eqs (46)-(49) and Sec V.1-V.2; Elgood et al eqs (6.1), (6.2), (7.3); Coincident GR eq (61) as the generic independent-connection template.
- **Sub-lemma the researcher could attempt:**
  - Treat the so(3,1) (or so(4)) bundle connection Omega on the leaf as independent.
  - Take as hypotheses the 029-031 Poisson-limit induced action, the kappa_X tr Omega^2 term, totally geodesic Sigma, and a regular frame at Sigma.
  - Form the Lorentz-Lie Noether charge. The expected form is an entropy density kappa_X x (binormal contraction n^{ab} * Omega_{ab}), plus the momentum-map correction.
  - Then compare with tau_Omega in 029.
- **Expected outcome (my forecast):** it reproduces a linear-in-Omega_12 term, i.e. the tau_Omega structure, not a W term. That would show the W coefficient 2 kappa_X is not generated by an independent-connection Wald term. The mismatch would then be a statement about the composite relation Omega = Omega[Theta], which is route R2.
- **Needs from NAMCG:** the local frame-rotation invariance of the induced action, which earlier scouts flagged (R7, the D1 local-Lorentz content), and an explicit statement of which connection is regular at Sigma.
- **No-gos:**
  - The naive Omega n replacement is not covariant (Elgood eq 7.3). Use the momentum map.
  - Hung-Myers-Smolkin: Wald alone is not EE in general.
  - Jacobson-Mohd leave torsion contributions open in general. Their torsion examples have zero charge.
- **Feasibility:** medium-high. **Value:** conditional sharpening; it removes the "Wald rule assigns nothing" objection or turns it into a clean obstruction.

### B-R2 (rank 2). Composite Omega: chain rule through the leaf versus independent delta support
- **Idea:** if Omega is a function of the metric data on the leaf, the entropy assignment depends on whether the replica deforms Omega with its own delta (031: uniform versus Hodge distribution) or only through the metric. This is the same choice that separates dislocation from disclination defects (Puntigam-Soleng).
- **Sub-lemma:** state the variable-dependence as a precise dictionary: which distributional content of Omega_delta (equivalently, which torsion-delta) makes the replica side equal the T side, and whether that content is forced by the matrix structure (the 2-form Theta^{12}, Theta^{34} frame) or is a free choice.
- **Reuse:** 031's E_delta, Omega_delta forms; Elgood eq (6.1) as the independent-connection benchmark; Frolov-Fursaev's Noether-term logic (the induced-versus-entanglement difference is a surface Noether charge).
- **No-gos:** 031 already found the normal-block (Hodge) distribution gives a nonzero sum for J != 0, so the distributional choice is physical. Avoid fitting it to the target.
- **Feasibility:** medium. **Value:** if forced by the matrix model, this is a genuine step; if not, it is a documented ambiguity.

### B-R3 (rank 3). Euler versus Weyl decomposition of the residue
- **Observation for the researcher to test, not a derived result:** Jacobson-Mohd Sec V.2 say the Euler term contributes chi(Sigma) and is connection-independent after integration, and Holst/Pontryagin do not contribute.
- 029 reports sigma_log = R_Sigma/(12 pi) on the self-dual family. 031 found proportionality only where g = 2 R_Sigma.
- **Sub-lemma:** decide whether the persistent R_Sigma-proportional piece is an Euler-class integral (then topological, tied to the a-type coefficient, and independent of the choice of SO(2) connection on TSigma) or a genuine non-topological density. The two cases need different fixes.
- **Reuse:** Solodukhin 1104.3712 eq (70) (already in the manuscript), Jacobson-Mohd eq (52) and the Euler-term discussion.
- **Feasibility:** high for the classification. **Value:** conditional, but it prevents a wasted search for a local W counterterm.

### B-R4. Dong/Camps with independent-connection second derivatives
- **Idea:** include d^2L/dOmega dR mixed terms times K^2.
- **Constraint:** all K^2 terms vanish on totally geodesic Sigma, the 029-031 hypothesis. Only useful for the open avenue "non-geodesic Sigma".
- **Feasibility:** low now, medium later. **Value:** conditional.

### B-R5. Torsion-substitution heuristic
- **Idea:** the Dordevic-Gocanin R -> R^(RC) rule as a template for the log term with torsion-squared.
- **Constraint:** unjustified, no replica derivation; CS gravity in 5D. Do not cite as support. At most it motivates testing R-> R^(RC) as an ansatz that B-R1/R2 must reproduce or refute.
- **Feasibility:** high effort-to-value ratio is poor. **Value:** low.

### Constraints for all B routes
- Hung-Myers-Smolkin no-go: the Wald formula is not the EE in general; use Dong/Camps corrections or the smooth-replica statement.
- Holst and Pontryagin terms contribute nothing; Euler contributes topologically (Jacobson-Mohd Sec V.2). Do not expect a Nieh-Yan type torsion-squared term to carry the Weyl coefficient.
- Frolov-Fursaev: induced-gravity entanglement and BH entropy differ by a Noether surface term Q for non-minimally coupled fields. Any mismatch assigned to "contact terms" needs this accounting.
- Normalisation: Coincident GR eqs (61) versus (78) differ by 2pi versus 1/(2pi); compare conventions before importing.

## 3. Route map for F: spectral vector sector

### F-R1 (rank 1). Zeeman-channel decomposition with ghost/longitudinal cancellation
- **Papers and equations:** Hattori-Itakura-Ozaki 2001.06131 eqs (65), (70a,b), (72)-(75), (79)-(80); Nikishov hep-th/0104019 (in/out Bogoliubov definition).
- **Sub-lemma:**
  - Diagonalise the vector Zeeman matrix on the CP^{1,2} class into channels with shifts lambda +/- 2 f_B (real) and lambda +/- 2i f_E (imaginary).
  - Subtract the ghost contribution as in eq (70a), so the longitudinal channel is removed.
  - Define each remaining channel as a scalar-type determinant with shifted mass, via a spectral sum.
  - Test whether the exponentially growing cosh-type term is then absent from the physical channel sum, as it is for Im W in 2001.06131.
- **Expected form:** a finite set of scalar-type Landau/Hurwitz sums (Fucci 1105.5624 for closed forms), with no residual e^{+2 f s} integrand.
- **Needs from NAMCG:** a precise statement of whether the IKKT bosonic fluctuation operator in the 028 class has the ghost structure of a gauge theory (two ghost scalar-type fields). The 032 "mass-linear" term should be matched channel by channel.
- **No-gos:**
  - The Nielsen-Olesen tachyonic channel has no unique contour (2001.06131 eqs 76-78; the authors call it open).
  - A pure E-field has no real Zeeman shift (Nikishov), whereas NAMCG's rule has +/- 2i f_E; check which description applies on the leaf (a non-collinear (a,b) mixture is not covered by Nikishov).
- **Feasibility:** medium. **Value:** conditional sharpening; a genuine step for F only if the tachyon channel is also fixed.

### F-R2 (rank 2). Euclidean analytic continuation with Schwinger-pole prescription
- **Papers and equations:** Bastianelli et al 2507.15943 eqs (4.20), (4.28)-(4.33) and footnote 10 (n=0 pole excluded); Pioline-Troost eqs (84)-(90) (zeta definition) versus eq (68) (Schwinger time).
- **Sub-lemma:** put the 032 leaf result into the form (4.20) with K+ and K- identified with the two flux invariants. Note the Euclidean convergence region needs m^2 > q K+. NAMCG's mu^2 = -3 is outside it, so one needs analytic continuation in m^2 (Hurwitz form), not a contour fix.
- **No-go to respect:** Pioline-Troost: zeta and Schwinger-time Im parts differ (extra saddle at negative proper time; vanishing at threshold). The vacuum (in-out versus Euclidean/instanton) must be stated, and the answer is definition dependent.
- **Feasibility:** medium. **Value:** conditional.

### F-R3. Positive-mass or non-perturbative completion
- **Idea:** dynamical mass or condensate removing the tachyon (Vercauteren-Verschelde 0712.0570, Kondo 1309.2337); Cho's colour reflection argument (hep-th/0301013).
- **Constraint:** non-perturbative or contested; none is an IKKT result. Equivalent in spirit to the Pauli-Sakharov completion route already listed in 030/032. Would enter as a new input, not a derivation.
- **Feasibility:** low as a derivation. **Value:** low-conditional.

### F-R4. Euclidean/self-dual signature constraint
- Muramatsu 2605.03611 argues the IIB matrix model with nontrivial supersymmetric backgrounds forces (anti-)self-dual, Euclidean configurations. If this applies to the CP^{1,2} class, the Lorentzian iEps contour is the wrong definition and the Euclidean zeta definition (F-R2) is natural. Verified only at abstract level. Check whether its hypotheses cover the NAMCG class before using it.
- **Value:** conditional guidance, not a computation.

### F-R5. Next-to-leading symbol with exact [W_a, Y]
- No direct literature mapping. The Hattori et al paper's Landau-level machinery (eqs 43-50) provides the exact-in-flux structure on which a derivative expansion could be built. This stays an in-house computation.

### Constraints for all F routes
- The electric-field Im part is not a unique functional: the heat-kernel and zeta definitions differ (Pioline-Troost).
- The Nielsen-Olesen contour is genuinely open in the literature (2001.06131 eqs 76-78).
- Bastianelli's spin-1 bracket is for a massive Proca-type particle; the NAMCG massless/tachyonic content with ghosts differs in counting. Match the bracket to the 028 field content before reusing eq (4.20).

## 4. Ranked list (10 routes)
1. B-R1 Lorentz-Noether entropy for the bundle connection (feasibility medium-high; conditional sharpening).
2. F-R1 Zeeman-channel decomposition with ghost cancellation (medium; conditional sharpening).
3. B-R3 Euler versus Weyl classification of the residue (high feasibility; classification).
4. B-R2 composite versus independent delta support (medium; potentially genuine).
5. F-R2 Euclidean analytic continuation (medium; conditional).
6. F-R4 signature constraint check (high feasibility; guidance).
7. B-R4 Dong/Camps with non-geodesic Sigma (low now).
8. F-R5 NLO symbol with [W_a, Y] (in-house).
9. F-R3 non-perturbative mass (low).
10. B-R5 torsion-substitution heuristic (low).

None of these is a breakthrough route to G_eff on its own. B-R1 or B-R2 would be a genuine step only if they fix the sign or value of the A-side coefficient.

## 5. Notes on emergence
- B-R1 and R2 use only the bundle connection and frame data obtained from the matrix leaf. Treating Omega as independent is a bookkeeping device for the entropy functional, not a fundamental field. Keep it explicit that the independent-connection variable is auxiliary.
- F routes are spectral statements about the matrix fluctuation operator. No background metric is introduced.

## 6. Unverified or limited items
- Elgood-Meessen-Ortin author list: not confirmed on the abstract page I opened.
- Coincident GR (2203.13914) Appendix E: not read.
- Castro et al 1405.2792, Miao-Guo 1411.5579, Hung-Myers-Smolkin details: abstract/listing only.
- Goldthorpe, Obukhov, Nieh-Yan a_2 with torsion: named in a search summary only; not independently verified.
- Battista-Steinacker 2310.11126 and JHEP02(2025)031: seen through search summaries only.
- Equation numbers are as returned by the fetch tool's paraphrase. Re-open before citing.

## 7. Files
- Repository files read: /c/Users/redgi/Projects/namcg-lab/reports/ledger.md (028-032), /c/Users/redgi/Projects/namcg-lab/proposals/033-log-content-scan/review-r1.md (head), and the five previous scouts in /c/Users/redgi/Projects/namcg-lab/reports/.
