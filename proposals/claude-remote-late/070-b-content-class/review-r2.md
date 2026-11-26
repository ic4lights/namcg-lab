VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

Gatekeeper r2 review, remote/claude, 2026-11-19. Saved here by the orchestrator.

Source reading: digest + targeted reads. Covered appH L154-531, appH L2780-2802 and ch17 L115-137. The full scan (ordinal 65, and 3(d)) is still owed.

## Checks
- s1-s3 re-run: outputs identical; S1 PASS.
- apply_build_r2:
  - pre hash 5106f993..., post hash 7e9f6760... (702343 B);
  - anchor and companion phrase are each unique;
  - 401 pp, 0 undefined.
- Re-derived by hand:
  - the four content identities;
  - c_T - c_W(0) = -4 kappa_X for every content;
  - the required term -(4kappa_X+n_D), which equals -4kappa_X at n_D=0 (matches 065) and -2 at (6,2);
  - the (6,2) ledger: tensor side 0, c_A = 2 is the Dirac excess, not removable by the Lambda^2 contacts;
  - the mass-shift formulas.
- Product-class quotation against L2780-2802: correct.
- 065 consistency: no duplication.
- Placement and the L437 companion edit ("at the end of this section" -> "later in this section"): ENDORSED as the smallest consistent option.
- Status sentence: compliant. sec:status-F resolves.
- S1 FAIL disclosure: verified against commits 20741cb and 7efe824.

## r1 findings
M1, M2 and m1-m5: all closed.

## New findings
- m-a, minor, REQUIRED. In "Sectors with a scale", replace
  `For this formal shift the comparison at this content is thus not vacuous only for a split spectrum, where it reduces to the two sums \(\mathsf S_n\) and \(\mathsf S_\kappa\).`
  with
  `For this formal shift the comparison at this content is thus, for the periodic gluing, not vacuous only for a split spectrum, where it reduces to the two sums \(\mathsf S_n\) and \(\mathsf S_\kappa\); for the fixed-state replica it keeps the Dirac term for every spectrum.`
  Reason: at a common mass the fixed-state comparison is c_A - c_T = 2f, which is not 0. The faulty wording was the gatekeeper's own r1 snippet.
- m-b, minor, recommended, proposal file only. The nsimplify mechanism is misdescribed: nsimplify(Rational) is the identity. Restate it as nsimplify applied to a non-Rational intermediate.
- m-c, optional. Replace "the family \(L_r\) of the paragraph on covariant variables reduces to \(L_0\)" with "the family \(L_r\) of the paragraph on covariant variables, with \(\kappa_X\) taken over the whole content, reduces to \(L_0\)".

## Disposition
- r3: apply m-a (+ m-b; m-c optional) and regenerate the post hash.
- Then the full scan, then a plain ACCEPT.
- No label change. Problem B stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- Bounded no-go: within the stated class, G_A = G_T is 0 = 0 or 2 != 0, which fixes no Newton constant.
