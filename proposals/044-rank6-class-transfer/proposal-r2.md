# Proposal 044-rank6-class-transfer, round 2

This round addresses `review-r1.md` (ACCEPT WITH REQUIRED REVISIONS). The r1 block is saved as `appH_insert_r1.tex`. `appH_insert.tex` is now the r2 block: 11763 bytes, produced by `apply_r2.py`. Every old string was checked to occur exactly once before it was replaced. Only the reviewer's snippets were applied, plus the closing-scope rewording the reviewer asked for.

All r1 sections not changed below stand as written in `proposal-r1.md`. Three corrections to r1 apply throughout:

- **No brane no-go.** The r1 "bending no-go" (r1 claim 12, Result item 6, and Milestone) is withdrawn.
  - The fourth-order term is the product of the induced d'Alembertian symbol and the tree kinetic symbol p·𝖪p, with 𝖪 = θᵀgθ the kinetic tensor. It can be removed by a local field redefinition, and it vanishes on the tree mass shell.
  - The order-p² part was not compared with EH(ĝ). So a common G_T on the transverse polarisations is neither established nor excluded.
  - The positive brane sub-result stands: the scalar part is exactly ρ·EH(ĝ), and the rank is min(6, D−1).
- **G_A ≠ G_T is generic, not forced.** It depends on unfixed replicas (Problem A) and on the undressed, off-shell quadratic form.
  - The periodic gap 4W_X is nonzero for W_X ≠ 0.
  - The smooth gap vanishes only if W_R = 16W_X, a condition on K that is not excluded.
  - The fixed-state gap is a cutoff-dependent first-term contribution plus 2W_X from the mixed term. The first-term contribution consists of a Λ² term and a log term ∝ Tr H₀ᴷ, neither computed.
  - With the merged dressed density, the mixed-term part of the fixed-state gap vanishes. That density is an input of Assumption local-lorentz and is not derived.
- **Milestone: none.** M2 is no longer claimed. The fuzzy-KK route, CP^{1,2}×K, the dressed route and non-product backgrounds all remain open.

## Findings and how they were applied

1. **Brane "no single G_T" (major).** Replaced by snippet 4. The kinetic tensor is renamed 𝖪 (`\mathsf K`) in the bending term `(p\cdot g^{-1}p)(p\cdot\mathsf Kp)` and in the new sentence. There is no second occurrence of `(p\cdot K\,p)` in the r1 block, so the brane sentence had only that one K to rename. The closing scope sentence was reworded minimally (see below).
2. **Fixed-state "finite part" (major).** Applied as snippet 2, with the first-term Λ² and log terms marked as not computed. The periodic and smooth gaps are now phrased as conditions.
3. **Dressed route (moderate).** Applied as snippet 3 (both parts): "part 2W_X … from the mixed term", plus the conditional dressed-density remark citing `Assumption~\ref{ass:local-lorentz}`. That label is defined exactly once, in `ch10-lorentz-locking.tex`.
4. **Title.** Changed to `(conditional; not closure)`.
5. **Steinacker.** Now reads "corresponds structurally …". The normalisations and the sign convention are stated as not compared, and the axial torsion is identified as the axion there.
6. **CP^{1,2} role assignment.** Applied as snippet 6. The roles of the two families follow Section 7 of Steinacker2023 and are not asserted independently.
7. **Fuzzy K not a solution.** Applied as snippet 8 in the scope sentence.
8. **Generic, not forced.** Covered by the snippet-2 wording ("does not vanish", "vanishes only if").
9. **Null mode.** Applied as snippet 7: "nonzero as a tensor …, although its quadratic invariants vanish on a single null wave."

Exact final closing scope sentence:
"These statements are for the Poisson limit on \(M\), one loop, the content stated, a fuzzy space \(K\) that is not required to solve the equations of motion, product backgrounds without mixed flux, the orientation-even part of the mixed term, the replicas of Section~\ref{sec:status-B} with the hypotheses stated there, and, for the transverse-mode check, frozen coefficients at one background point."

The final status sentence is unchanged: "Problems~B and~F remain open and PROGRAMME-CONDITIONAL."

## Claim classification changes

- **Claim 8** (replica gaps): conditional, and the gap is generic rather than forced. The fixed-state first-term terms (Λ² and log) are not computed.
- **Claim 12** (bending): reclassified as established at frozen coefficients. The fourth-order term equals the product of the induced d'Alembertian symbol and the tree kinetic symbol. The order-p² comparison is unresolved, and there is no no-go.
- **New claim 17** (dressed density gives c_Tᵉˣᵗ = W_R/6 − 2W_X, so the mixed-term gap vanishes): conditional on Assumption local-lorentz (an input).

## Checks

- **Byte check** (`apply_r2.out.txt`): 11763 bytes; 0 TAB, 0 CR, 0 non-ASCII, 0 control characters other than LF. Braces, `\(`/`\)` and `\[`/`\]` are all balanced.
- **Mechanics** (`s5_insert_mechanics.out.txt`):
  - one `\paragraph`, no `\label`;
  - refs `ass:local-lorentz`, `ch:vierbein-emergence` and `sec:status-B` each defined once;
  - cites IKKT1997, Steinacker2023 and SperlingSteinacker2019 each present in the bib;
  - the anchor `\section{Problem G: HBEV}` is unique.
- **Scratch compile of the current tree** (`compile_check.out.txt`): 317 pages baseline, 321 with the insert. Exit codes are all 0, with 0 undefined references, 0 undefined citations and 0 multiply defined labels. CRLF was preserved and the scratch directory removed.
- **No changed calculation.** All r1 scripts and outputs stand.

## Milestone assessment
None. This is not a breakthrough.

## Status-label recommendation
None. B and F remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Author decision needed
None.

## Remaining open step (ranked, per the review)
1. CP^{1,2} (finite fibre) × K: the Dirac index density on the six level-one modes, and whether they source axial torsion.
2. The dressed route: compute the first-term Λ² and log excess and its replica dependence.
3. The first-term cone with the full s0ᴷ(s).
4. The sign of W_R and the ratio W_R/W_X for an explicit K.
5. Non-product backgrounds.
6. The brane transverse sector at order p².
7. The orientation-odd mixed term.

## Special instructions for the gatekeeper
- Diff `appH_insert_r1.tex` against `appH_insert.tex`. The only changes should be the eleven replacements in `apply_r2.py`.
- The integrator converts the block to CRLF.
