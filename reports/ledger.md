# NAMCG-Lab running ledger

## 002-auto-target (Problem N) — 2026-10-14
- Problem: N (control of the effective expansion / no spin-2 ghost below Lambda_UV).
- Claim: within the truncated identity of thm:Geff (flat background, vacuum term removed, common limits, added curvature-continuation convention) the induced Weyl term gives m_2^2 = -Upsilon Lambda_UV^2/L with Upsilon = pi/(G_eff W_C Lambda_UV^2) (=10 for minimal scalars, a_1-only G); in the leading-log form-factor model F, no zero in |k^2|<Lambda_UV^2 iff Upsilon > Upsilon_*(delta_W) (Upsilon_*(0)=pi/2; numerical converse).
- Rounds: 2. Verdicts: r1 ACCEPT WITH REQUIRED REVISIONS (PRIOR-CLAIM-ERROR, AUTHOR-DECISION); r2 ACCEPT (PRIOR-CLAIM-ERROR, AUTHOR-DECISION; PROGRESS improving).
- Final: ACCEPT with flags -> NOT INTEGRATED (run-cycle step d: flags require author). Commit: not integrated.
- Proved: C^2/E_GB/R^2 decomposition, spin-2/spin-0 quadratic forms, pole masses and residue signs, Lambert zero formula, Upsilon_*(0)=pi/2, Upsilon_*(d)=d for d>=1. Conditional: c_W, c_R, Upsilon=A_1/(2W_C), Upsilon=10. Model/numerical: disc criterion, Upsilon_* table, window -9.58<delta_W<10. Open: W_C, A_1, G_eff, delta_W for locked block; |k|~Lambda_UV control; matrix derivation. N stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- Milestone: none (gatekeeper). Run stopped on flags. Fixed-L "no-go" (M2) route withdrawn in r2 as an artefact of the fixed-L form; do not resubmit it.
- Author items: (9) appK-endomorphism.tex:17 a_1 sign opposite to eq:appA-a1/eq:a0a1 (non-load-bearing); (10) alpha overloaded, N target wording ambiguous; optional Barvinsky-Vilkovisky 1990 bib entry.

## 003-auto-target (Problem F; consequences for C, B, D1) — 2026-10-14
- Claim: on the fixed flat scaffold the displayed Presentation-B action induces no Einstein-Hilbert/Fierz-Pauli term for the composite metric (Lemma 1 at one loop with A_mu fixed; Lemma 2 to all loop orders under scaffold-rotation-invariant regulator/gauge fixing/vacuum), so G_eff comes entirely from the assumed emergent-background operator; the final inference of prop:scaffold (ch08) is false.
- Rounds: 1. Verdict: r1 ACCEPT WITH REQUIRED REVISIONS | M3, M2 | PRIOR-CLAIM-ERROR, AUTHOR-DECISION | PROGRESS first.
- Final: NOT INTEGRATED. Run stopped at r1 on confirmed M3 (MILESTONE.md: wrong merged claim stops the loop immediately). Revisions (findings 1-3 major, 4-8 minor) not yet made.
- Proved: Hessian structure + Lemma 1 (scaffold proper-time regulator, A_mu fixed); conformal-mode counterexample to prop:scaffold's final sentence; psi-T orthogonality at tree level; Lemma 2 (flat scaffold, rotation-preserving regulator and gauge fixing, invariant vacuum, h a fixed linear image of Phi). Conditional: Delta Z = 3 lambda/(4 pi^2) (A_mu fixed, s_max -> infinity). Not covered: A_mu-integrated theory, Theta-dependent regulators, curved scaffolds, Presentation A, Weinberg-Witten applicability. F, C, B, D stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- Milestone: M3 (prop:scaffold final inference wrong; ch05 psi dd T clause false, non-load-bearing), M2 (no-go for loop-generated composite-metric EH/FP in the scaffold-symmetric class).
- Author items: prop:scaffold form (proposition vs remark/assumption) and ch16 inventory; structural ingredient tying derivative and tangent indices; stale passages ch04 Ex.7 L418-423, ch08 L56-58, appG L19-29.
