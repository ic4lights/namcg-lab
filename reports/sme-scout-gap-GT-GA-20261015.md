SME-SCOUT: 9 routes | TOP: gauge-parameter dependence of the induced TT form (off-shell ambiguity proportional to background EOM) with the all-modes Einstein-structure test; field content that cancels the rho^2 X weight (fermions or torsion-coupled scalars); gauge-sector entropy ambiguity (Casini-Huerta-Rosabal / Donnelly-Wall edge modes) as a fixing principle | EMERGENCE-RISK: low

Saved verbatim from the independent SME agent (mode 1, gap resolution) for the G_T != G_A gap of proposal 015. Advisory only.

# Gap-resolution scout for G_T != G_A (Problem B, proposal 015 r1)

Advisory only. I wrote no derivations or files.

**Reading mode:** digest and targeted reads. I read proposal 015 r1 in full, `reports/sme-route-B-DorauMuch-20261015-1052.md` in full, and the "Gap resolution" instruction in `.claude/agents/sme.md`. I did not read the manuscript chapters and did not re-run the 015 scripts. I did not read `review-r1.md`; I took its confirmation of the arithmetic from the coordinator's message.

## 0. What the gap is, and what 015's own numbers imply

- **Size in scalar units.** One minimally coupled scalar has c = 1/6 in 015's units. The shortfall of 4 in c is therefore 24 scalar units, independent of N_s. Any mechanism has to reproduce that number.
- **Direction.** To restore G_T = G_A, either lower c_A by 4 or raise c_T by 4. The excess is the non-curvature term rho^2 X. It is bounded on the cover, so the replica (I) does not see it.
- **Structural point, derived by me from 015's table (not stated in 015).**
  - The curvature term has eigenvalues (-1/4, -1/4, -3/4) on the three modes. X has (1, 1, 1).
  - Write the induced form as a*rho R + b*rho^2 X, with a = N_tot/6 and b = 1.
  - A pure Einstein term needs the ratio (third mode)/(TT mode) = 3. That holds only if b = 0.
  - With b = 1 the ratio is (1 - N_tot/8)/(1 - N_tot/24), which is not 3. The induced form is therefore not of Einstein form on the delta-rho != 0 mode either.
  - So "G_T" is defined only through the TT modes. Any real fix must remove or reinterpret X. A shift of the R coefficient alone cannot restore Einstein structure on the third mode.
  - This gives the researcher a cheap diagnostic: does a candidate fix make the three-mode ratio equal 3?
- **Wald-type rule.** A bounded non-curvature term gives zero Wald/Iyer-Wald entropy. A mismatch of this type is therefore expected for any action with terms beyond rho R. It is generic, not exotic. The sub-lemmas below test whether X is physical; they do not question the cone computation. This is my own general reading, not a verified citation.

## Ranking

| Rank | Mechanism | Could close 2 Lambda^2/pi? | Sign | Feasibility | Emergence |
|---|---|---|---|---|---|
| 1 | Gauge-parameter / off-shell dependence of the induced form (section 1) | Possibly, as an EOM-proportional ambiguity of b | Not known in advance | Medium-high | Preserved |
| 2 | Field content: fermions or torsion-coupled scalars cancelling X (section 2) | Yes if tuned; the size is a free parameter | Needs a negative net X weight | Medium | Preserved |
| 3 | Gauge-sector entropy ambiguity: Casini-Huerta-Rosabal centre choice, Donnelly-Wall edge modes (section 3) | Shifts c_A only by a non-universal boundary-local amount | Either | Medium-low | Preserved |
| 4 | Index structure: Levi-Civita versus coframe holonomy, Kabat term in the LC basis (section 4) | Changes c_A; not a closure by itself | Negative (lowers c_A) | Medium | Preserved |
| 5 | Singular-cone choice (II) of 015 (section 5) | Only at N_tot = 16, wrong sign | Negative | Low | Preserved |
| 6 | Ghost-weighted entropy (section 6) | Probably inert on the area side | None | Medium-low | Preserved |
| 7 | Moyal corrections, Phi-a mixing | Not scouted | Unknown | Unknown | Preserved |
| 8 | Tree-level term of 014 (section 7) | No: order p^0, not p^2 | None | Low | Preserved |
| 9 | Log terms (section 8) | No: different power of Lambda | None | Low | Preserved |

## 1. Gauge-parameter dependence versus gauge-invariant entropy (top target)

- **Why it applies.** 015 itself notes that the off-shell quadratic form is gauge dependent. The standard background-field statement is that gauge-parameter dependence of the one-loop effective action is proportional to the classical equations of motion of the background. The TT modes of Theta_bar + eps T are a background fluctuation, and they are not on shell in general. So rho^2 X on the TT modes may be partly an EOM-proportional, gauge-dependent piece, and the Feynman-gauge value b = 1 may be a gauge artefact.
- **Literature.**
  - Donnelly-Wall (1506.05792, footnote 1, read in the full text): in the 't Hooft family the regulators can be adjusted so the contact term is independent of the gauge parameter. This suggests a universal gauge-invariant content alongside a gauge-dependent naive coefficient.
  - Nielsen, arXiv:1109.2699, and de Alwis, arXiv:2511.12864: seen only as search-result summaries, not opened ("not independently verified"). They concern gauge independence of the Vilkovisky-DeWitt effective action.
  - I found no paper computing the gauge-parameter dependence of the induced Newton constant in this setting.
- **Sub-lemma for the researcher.**
  1. Generalise the 005 operator to a 't Hooft-type family with parameter alpha, keeping Laplace type through a Stueckelberg scalar if possible. State the hypothesis class explicitly.
  2. Compute b(alpha), the coefficient of rho^2 X on the TT modes.
  3. Evaluate the TT form on the classical EOM of the tree-level Poisson-limit action: is it equivalent to a pure Einstein term modulo EOM?
  4. Report whether the gap is alpha-independent.
- **NAMCG objects.** The EOM of the Poisson-limit action (014 and Problem-C material, tree-level kernel M), the sector table, a non-minimal gauge fixing, and a specified off-shell background.
- **Emergence.** Preserved.
- **Feasibility.** Medium-high for the Laplace-type 't Hooft extension. Non-Laplace gauges are a separate, harder task.
- **Value.** Either outcome is useful. A robust, alpha-independent gap hardens the no-go against the gauge relaxation. An EOM-proportional b reduces B to an on-shell statement, which is a conditional sharpening.

## 2. Field content that cancels the connection-sector excess

- **Mechanism.** The gap is exactly the net rho^2 X weight. Sectors that contribute to X with the opposite sign change b without altering the cone term of bounded sectors.
  - Fermions: the square of a Dirac operator has a heat-kernel endomorphism with torsion-squared terms, and the loop sign is opposite to the bosonic one.
  - Torsion-coupled scalars: an extra scalar with E = E_s + xi_X X, xi_X negative.
  - The R-part of a fermion adds to c_A and c_T equally. Solodukhin counts a Dirac field as 2 scalars in N = N_0 + 2 N_{1/2}; this is taken from the earlier route map and 015, which read eqs. 318-320, and I did not re-read it. The gap closes if and only if the total rho^2 X weight vanishes. That fixes the content and is independent of N_s.
- **Sign needed.** A negative net X weight equal in size to the connection sector's +1.
- **Cross-check.** The condition b = 0 also restores Einstein structure on the third mode (section 0). A fix that closes the TT gap but leaves the three-mode ratio different from 3 is not a real resolution.
- **IKKT context (partly verified).** A web search returned Steinacker, "One-loop effective action and emergent gravity on quantum spaces in the IKKT matrix model", arXiv:2303.08012, JHEP 05 (2023) 129. I read the search snippet only. It says the EH term arises at one loop for M^{3,1} x K with maximal supersymmetry and fuzzy extra dimensions, with the Newton constant set by the KK scale. These statements are not independently verified.
  - In supersymmetric settings the quadratic divergence typically cancels through the supertrace, so the Lambda^2 coefficient c_A could itself vanish. The comparison would then move to a different coefficient (KK scale or log-sensitive terms).
  - If the researcher cancels X with fermions, the comparison must be re-posed for the surviving coefficient. This is a hypothesis-class change that has to be stated; it is not a within-class closure.
- **NAMCG objects.** The fermionic operator in the Poisson limit (Dirac operator built from the coframe with torsion), its endomorphism trace, and the cone term for spinors. In the coframe basis there is no Levi-Civita holonomy, as for a^mu.
- **Emergence.** Preserved. The content is matter-like and the metric stays G.
- **Feasibility.** Medium. The a_1 coefficient of the torsionful Dirac square is a standard computation. What fermion content NAMCG may include is a scope question for the author.
- **Standing.** Closure by content is tuning, hence a conditional sharpening. It becomes a genuine result only if the cancellation follows from a symmetry or a structural property of the matrix action.

## 3. Edge modes (Donnelly-Wall) and boundary-local entropy ambiguity (Casini-Huerta-Rosabal)

Verified sources:

- **Donnelly-Wall, arXiv:1506.05792.** Read: abstract, introduction and footnotes in the full text.
  - They KK-reduce Maxwell onto a 2D base. The geometric entropy is that of scalars, constant fluxes and a contact term whose leading divergence was found by Kabat.
  - The complete contact term is "one negative scalar degree of freedom confined to the entangling surface".
  - It agrees with a statistical entropy that includes edge modes.
  - The contact term traces to the non-minimal Ric coupling in the spin-1 Laplacian, and they argue it cannot be read as a Wald entropy.
- **Donnelly-Wall, arXiv:1206.5831 (PRD 86, 064042).** Abstract only. The negative term depends on the treatment of infrared modes and arises from mishandled zero modes. In a gauge-invariant reduced-phase-space quantisation the gauge-field contribution is positive, finite and equal to entanglement entropy.
- **Casini-Huerta-Rosabal, arXiv:1312.1183 (PRD 89, 085012).** Abstract only. Gauge constraints obstruct tensor-product factorisation. Algebras with trivial centre correspond to partial gauge fixings. The entropy depends on that choice, with ambiguities local on the region's boundary.
- **Kabat, hep-th/9503016 (Nucl. Phys. B 453, 281).** Abstract only. For spin 0 and 1/2 black-hole entropy equals entanglement entropy. For spin 1 they differ by a horizon contact term.

**Mapping onto the gap.**

- **Magnitude.** The Donnelly-Wall term is one negative scalar's worth, about 1/6 in c-units, if the statement carries to order Lambda^2. The gap is 4, i.e. 24 scalar units. One edge-mode term cannot reproduce it. This comparison is mine; the papers do not relate the two.
- **Structure.** The Kabat/Donnelly-Wall term comes from a curvature coupling (Ric) in E. In 015's variables the fibre index is internal, so there is no such term. The NAMCG gap comes from the non-curvature X. The standard edge-mode mechanism therefore does not address the same term.
- **Real relevance.** The centre-choice ambiguity shifts the entropy by a boundary-local, non-universal amount. So 015's c_A for the gauge sector is not an unambiguous entropy.
  - If one adopted "choose the algebra so that G_A = G_T", equality would become a selection rule on the gauge algebra. That is weaker than a derivation.
  - Sub-lemma: determine which centre choices and edge-mode sets are admissible for the matrix gauge algebra, and whether any gives a shift of the required form (c_A lowered by 4). This touches Problem A.
- **Sign.** Either.
- **Emergence.** Preserved.
- **Feasibility.** Medium-low. It depends on Problem A and is not a bounded computation.

## 4. Levi-Civita versus coframe holonomy (Kabat term in another basis)

- **Fursaev-Miele, hep-th/9605153 (Nucl. Phys. B 484, 697).** Abstract only. Heat kernels for spin 1/2 and 1 on cones resemble the scalar case. Spin 2 and 3/2 show a discrepancy attributed to broken local translational isometries. This supports 015's treatment of the internal-index vector as scalar-like.
- **Where the Kabat term returns.** In 015's torsion-basis column the scalar sector has Q = 1/4 per component, so the four-component connection sector has trace Q_v = 1. That is a curvature coupling of Kabat type. The choice between a Weitzenboeck frame (flat, torsionful, no holonomy) and the Levi-Civita frame (index rotated around the surface) is then physical. In the Levi-Civita frame the Kabat term appears and the ghost-weighted count changes.
- **Sub-lemma.** Redo the replica entropy for the connection sector with the fibre index identified with the tangent index through the coframe. Report c_A for the Levi-Civita-rotated and Weitzenboeck-rotated cases. State which one the tensor block h = T uses, since a^mu is a target-space index and the identification is a choice.
- **Sign and size.** The gauge-field contact term is negative (Donnelly-Wall), so it lowers c_A. Its size is O(1) scalar unit, not 24, so it cannot close the gap alone.
- **Emergence.** Preserved if the frame is the emergent coframe. At risk only if the index is silently tied to eta.
- **Feasibility.** Medium; the rotation structure is standard.

## 5. The singular cone choice (II)

- 015 finds c_A(II) = -c_A(I)/2 in every sector, so c_A(II) = -N_tot/12.
- Setting c_T = N_tot/6 - 4 equal to -N_tot/12 gives N_tot = 16. This is my own numerology, not a claim in 015.
- It is not a resolution. The sign is negative (015 says (II) is not claimed physical), it holds at one N_tot only, and the c_T matching uses rho R[g_rho] eigenvalues while the (II) coefficient is stated in R_G terms, so the comparison would need a conversion I have not checked.
- I record it only so the coincidence does not surprise the researcher. Emergence preserved; feasibility low.

## 6. Ghost-weighted entropy

- The vector plus ghosts contribute (4/6 - 2/6) = 1/3 to c_A, which is two scalars, matching two physical polarisations. Donnelly-Wall note ghosts cancel the unphysical components in the partition function (seen in the paper text). So the area-side ghost weighting is probably not the source of the gap. The gap lives in X, which the ghosts do not carry. Rated low.
- Whether the weighted sum is a physical entropy is the centre-choice question of section 3.

## 7. Tree-level term of 014

- 015 says the 014-class tree-level response is degree 0 in h, so it cannot supply or cancel a p^2 mismatch. Low. Its only role is indirect: it fixes the EOM needed in section 1.

## 8. Log terms

- Log terms multiply a different power of the cutoff and cannot cancel a Lambda^2 mismatch. They matter only after renormalisation, where G_A = G_T would become a statement about a_2 coefficients. That is a different problem. Low.

## Conflicts and constraints to respect

- Do not retune a free coupling to make G_T = G_A and call it derived (CLAUDE.md rule 3: no closure by supplied input). A cancellation by content is a condition, not a derivation.
- State Feynman-gauge dependence explicitly until section 1 is done.
- Karczmarek-Sabella-Garnier, arXiv:1310.8345 (abstract-level only, via the earlier route map): the area-law premise for matrix regions is not guaranteed. This is a standing risk for any c_A here.

## Most promising mechanism and ranking rationale

1. **Gauge-parameter dependence (section 1)**, tested with the three-mode Einstein-structure criterion. It is cheap and decides whether the 2 Lambda^2/pi gap is physical or an off-shell artefact. Either outcome is a sharpening.
2. **Field content with b = 0 (section 2).** It is the only route that restores Einstein structure on all modes, and it gives a precise condition on content. It stays conditional unless a symmetry forces the cancellation. Supersymmetry may remove c_A itself (Steinacker line, not independently verified), which changes the comparison.
3. **Centre-choice ambiguity of the gauge-sector entropy (section 3)**, together with the frame choice of section 4. It shows c_A is itself ambiguous for the gauge sector. The edge-mode contact term has the wrong size to close the gap alone.

## Emergence

Risk is low. All routes keep the metric as the emergent G. Emergence would be violated only by supplying the missing coefficient from an external G, from S = A/4, or by tying the fibre index to eta. Each should be refused.

## Literature checked

Verified by fetching the arXiv record:

- Donnelly, Wall, arXiv:1506.05792: abstract, introduction and footnotes read in the full-text PDF. I did not read the dimension-specific value of the contact term in d = 4 or its precise relation to the heat-kernel coefficient.
- Donnelly, Wall, arXiv:1206.5831, PRD 86, 064042: abstract only.
- Kabat, hep-th/9503016, Nucl. Phys. B 453, 281: abstract only.
- Larsen, Wilczek, hep-th/9506066, Nucl. Phys. B 458, 249: abstract only. It states that renormalising Newton's constant makes the entropy finite and equal to its semiclassical value; that the conical geometric entropy depends on curved-space couplings for scalars; and that fermion and gauge-field determinants are closely related to non-minimally coupled scalars.
- Casini, Huerta, Rosabal, arXiv:1312.1183, PRD 89, 085012: abstract only.
- Fursaev, Miele, hep-th/9605153, Nucl. Phys. B 484, 697: abstract only.

Not independently verified (search-result summaries only, not opened):

- Steinacker, arXiv:2303.08012 (JHEP 05 (2023) 129), cited in section 2.
- Nielsen, arXiv:1109.2699; de Alwis, arXiv:2511.12864.
- Teleparallel/torsion Wald-entropy papers that the search returned (arXiv:1912.08811, 2203.13914, 2007.10721). They are pointers only. I found no direct Wald-entropy calculation for torsion-squared Poincare-gauge terms.
- Solodukhin, Living Rev. Rel. 14, 8 (arXiv:1104.3712): the contact-term relation and the "Dirac = 2 scalars" count are taken from the earlier route map and 015, not re-read by me.

I found no published paper on this specific mismatch (rho^2 X from an internal-index connection sector in a Poisson-limit matrix model). As far as this search goes, that part is open in the literature.

Relevant files: C:\Users\redgi\Projects\namcg-lab\proposals\015-entropy-action-identity\proposal-r1.md; C:\Users\redgi\Projects\namcg-lab\reports\sme-route-B-DorauMuch-20261015-1052.md.
