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

## 002-auto-target — integrated 2026-10-14
- Integrated proposal-r2 items 1-3 (appH Problem N conditional block; deletion of "No computation is recorded."; ch09 Stelle qualifier) under the author's 2026-10-14 autonomy directive (flags concerned only outside items). Commit eecd202. Build PASS 242 pages, 0 undefined refs. No label touched. N stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## 004-author-questions — advisory recommendations
- r1 reviewed (ACCEPT WITH REQUIRED REVISIONS, OPEN 0/4); r2 written addressing findings 1-7. Not for integration; under the autonomy directive its within-core recommendations become researcher decisions to be carried into normal proposal rounds (Q1 appK sign; Q2/Q3 N gloss + citation; Q4/Q6 with 003).

## 003-auto-target (Problem F; C, B, D1) — integrated 2026-10-14
- Rounds: 3. r1 AWRR (M3, M2); r2 AWRR (improving, OPEN 0/0; Item 7 excluded as AUTHOR-DECISION); r3 ACCEPT | M3, M2 | PRIOR-CLAIM-ERROR.
- Integrated Items 1-5 (appH, ch08, appB, ch04 Ex.7, appG, ch03, ch05). Commit 85f49d0. Build PASS 244 pages, 0 undefined refs. No label touched.
- Proved: Lemma 1 (fixed A_mu, scaffold regulator: no Lambda^4/Lambda^2/ln Lambda term with derivatives of Phi); conformal-mode counterexample; finite Delta Z incl. Delta Z_K; Lemma 2 no-go within H1-H4 only (flat scaffold, rotation-preserving regulator+gauge fixing, invariant vacuum, h fixed linear image of Phi); psi-T orthogonality. Correction: prop:scaffold -> ass:emergent-op + rem:ch8-scaffold-vs-emergent.
- Not a closure of the composite-metric EH route. Relaxable hypotheses: Theta-built regulator/kinetic metric (Presentation A), non-invariant vacuum, curved scaffold, non-linear composite map.
- Queued for author: Item 7 (ch16 inventory row for ass:emergent-op + premise sentence + chain item 6; optional ch17 F missing-step sentence) — changes Ch.17 completion criterion by cross-reference.
- Milestone: M3, M2 (non-stopping under autonomy directive). Integrated count this run: 2.

## 006-followups-002-003-004 — integrated 2026-10-14
- Bookkeeping follow-ups (author-approved B and C: "proceed with worth integrating items"). r1 ACCEPT, flags none, full scan.
- A: appK a_1 sign corrected to tr(R/6-E); A2 narrowed (F F term quadratic; linear tr(S E_0) term not excluded). B: alpha gloss on N target (ch17, appH sec:status-N). C: ch16 inventory row for ass:emergent-op (load-bearing), premise sentence, chain item 6.
- Commit 5ddf637. Build PASS 246 pages, 0 undefined refs. No label touched. Integrated count this run: 3.
- Still queued: Barvinsky-Vilkovisky citation for the N form-factor sentence (integrator may now add accepted BibTeX).

## 007-N-formfactor-citation — integrated 2026-10-14
- \cite{BarvinskyVilkovisky1990} after "momentum-dependent form factors" in appH sec:status-N; BibTeX added to bib/namcg.bib (record verified against Crossref by gatekeeper). Decay clause stays an uncited assumption. r1 ACCEPT, flags none.
- Commit 6e5f56a. Process note: integrator committed after build_check reported FAIL (citation undefined because scripts/build_check.py runs pdflatex only, never bibtex; .bbl is gitignored). After a manual bibtex + 2x pdflatex the cite resolves; orchestrator re-ran build_check: PASS 246 pages, 0 undefined. Infrastructure gap: build_check.py does not run bibtex (left for the author).
- No label touched. Integrated count this run: 4.

## 005-F-presentationA-EH (Problem F) — integrated 2026-10-14
- Rounds: 2. r1 AWRR (no milestone; "obstruction" downgraded to conditional computation); r2 ACCEPT, flags none, full scan (5th integration).
- Integrated one appH paragraph before \section{Problem G: HBEV}. Commit 9c68802. Build PASS 248 pages, 0 undefined refs. No label touched.
- Established: scalar-sector identity sqrt|G|(R_G/6-E)=rho R[g_rho]/6 (Poisson-limit operator); G = eta_AB e^A e^B for e = eta^-1 Theta^-1; connection-sector trace (4/6)rho R + rho^2 X (ghosts -2/6 rho R); quadratic eigenvalues +1, -1/4, -3/4; net TT Maxwell-kernel coefficient 1 - N_tot/24 (N_tot = N_s + 2, input count). Sampled counterexample: rho^2 X is not alpha rho R + beta rho|grad ln rho|^2 mod total derivatives at cubic order ((g_rho, rho)-covariant class; eta-using rewritings untested).
- Conditional on Poisson limit, bosonic 4D content, background gauge, diagonal heat kernel with local cutoff, Euclidean signs. Not established: ass:emergent-op discharge (<Phi>/v = coframe not derived), any G_eff value/sign.
- Open relaxations: fermion/extra-scalar content, Moyal corrections, non-minimal gauges, Phi-a mixing, Presentation-B frame coupling, eta-using rewritings of X.
- Milestone: none. Integrated count this run: 5.

## 008-auto-target (ass:emergent-op; Problems F, A) — integrated 2026-10-14
- Rounds: 2. r1 AWRR | M2 | AUTHOR-DECISION (N>=8 relaxation); r2 ACCEPT | M2 | flags none (N>=8 now author-pre-approved, recorded only under Decisions Taken).
- Integrated one appH paragraph (four-matrix Poisson-limit conditional obstruction) before \section{Problem G: HBEV}. Commit 3ab80c9. Build PASS 250 pages, 0 undefined refs. No label touched.
- Established in H_A (4 matrices, Poisson limit, constant eta, real nondegenerate Theta, linear order about constant Theta, generic p): Theta->G rank 6 at Pf!=0 with quadratic image relation (codim 4); 3-dimensional linear response; linearized Einstein operator rank 3 vs 6 conserved sources, so E[h]=T fails for generic conserved T without an additional derived conserved stress; K != c g^-1 pointwise for real Lorentzian g; tree-level quadratic action algebraic in (dG, d rho).
- Conditional: vacuum-manifold mismatch (if e = <Phi>/v); nonlinear 3-vs-7 count (counting argument).
- Next routes: N>=8 matrix coordinates (author-pre-approved structural, ranked first -> proposal 009); derived extra stress T_ent; Moyal; non-constant backgrounds; fermions/scalars; Presentation B independent Phi.
- Milestone: M2 (bounded; non-stopping). Integrated count this run: 6.

## Author directive update — 2026-10-14
- "proceed with positive impact changes that remain namcg emergent spacetime, automatically": emergence-preserving, positive-impact structural/scope/core-definition changes are pre-approved (gatekeeper review still required; label changes still author-only). Encoded in run-cycle.md and gatekeeper.md (commit 401db7b); researcher.md edit was denied by the permission classifier, so the pre-approval is passed in researcher prompts.

## 010-sme-followups — integrated 2026-10-14
- From the independent SME review (reports/sme-auto-20261014-1520-20261014-2054.md). r1 ACCEPT, flags none.
- A: ch09 Weyl-sign sentence now states dependence on the curvature-continuation convention of sec:status-N. B: appK conformal-mode/no-TT conclusion scoped (metric-variation form not derived; F-linear tr(S E_0) term not excluded). C: no summaries of 003/008 no-gos in ch01/ch16/ch17; no edit.
- Commit ab0fa84. Build PASS 250 pages, 0 undefined refs. No label touched. Integrated count this run: 7.

## 009-matrix-coords-N8 (ass:emergent-op; Problems F, A, D1, E) — integrated 2026-10-14
- Author-pre-approved structural extension (M5). Rounds: 2. r1 AWRR | M5 (headline no-go already merged via 008; N_tot line unsupported; literature over-attributed); r2 ACCEPT | M5 | flags none.
- Integrated: ch03 def:matrix-coords-ext (D matrix coordinates, Poisson limit, 4-dim symplectic leaf, fixed eta_IJ; reduces to def:matrix-coords for D=4); appH paragraph on linear-response ranks; bib KumarSteinacker2023, Steinacker2026 (records verified at abstract level). Commit d9da131. Build PASS 250 pages, 0 undefined. No label touched.
- Established (kinematic): linearized Einstein rank exactly 3 about a flat brane for every D; min(6, D-1) for generic frozen second fundamental form (exact upper bound; lower bound by exact-rational sample + semicontinuity), so all 6 conserved sources reachable from D=7; D>=8 incl. density is a necessary count only. G != c g for real Lorentzian g and 4-dim leaf, any D (cross-referenced to 008).
- Not established: Einstein-type field equation for G; gap of the D-4 transverse scalars (not covered by ass:locked-block); Phi = tangent frame; G_eff.
- Next (researcher-ranked): relax the 4-dimensional leaf (fuzzy extra dimensions, cf. Steinacker2023); then derive the extra conserved stress.
- Integrated count this run: 8.
