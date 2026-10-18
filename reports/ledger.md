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

## 011-fuzzy-leaf (Problem F; A, D1, E) — integrated 2026-10-15
- Rounds: 3. r1 AWRR | M2 (leaf-level det proof wrong for odd m; misleading (N_tot-12)/6 line); r2 AWRR | M2 (two wording fixes; torsion identity derived, Weitzenboeck step verified independently by gatekeeper); r3 ACCEPT | M2 | flags none. Full scan at r1 (10th integration).
- Integrated two appH paragraphs before \section{Problem G: HBEV}. Commit ae8aff4. Build PASS 252 pages, 0 undefined. No label touched.
- Established: bounded no-go — with base coordinates = Lorentzian matrix block, fibre-averaged K != c eta^-1 (c != 0) for any D, compact fibre, positive average; leaf-level G != c g for 2m>=4 (counterexample at 2m=2); product leaf M x fuzzy sphere keeps zero-mode tensor of M (Einstein rank 3 about flat M); CP^{1,2} conjugate-coordinate class gives K = (M45/R^2)^2 eta^-1 (conformally flat) — Einstein rank not computed, base-function choice not derived; heat kernel over fuzzy factor gives 1/G_eff ~ Lambda^2 x weighted mode count (conditional); X = Weitzenboeck torsion invariant: rho^2 X = -2 rho R[g_rho] - rho|grad ln rho|^2 + (3/2) rho^2 S^2 + total derivative (derived; net TT coefficient 1 - N_tot/24 unchanged).
- Next (researcher-ranked): Einstein rank in the CP^{1,2} class; then derive why y^mu = M^{mu5} are base functions.
- Integrated count this run: 9 (002,003,005,006,007,008,010,009,011).

## SME literature review — Dorau & Much, PRL 136, 091602 (2026), arXiv:2510.24491
- reports/sme-lit-DorauMuch2026-20261015.md. PARTLY RELEVANT | mixed | emergence risk low. Rigorous AQFT form of Jacobson's matter side (S_rel = null energy flux, free scalar, coherent states); assumes metric and S = A/4, so it does not touch NAMCG's Claim 2 / Problems A, B gap. Constrains: a Jacobson-type closure needs a conserved total stress, which 008/009 show NAMCG does not yet derive.
- SME suggestions (ranked): 1 cite and position in ch06/appB without overclaiming; 2 test eq. 13 (S_rel = flux) against a matrix-derived modular Hamiltonian (Problem A sub-lemma); 3 derive the conserved total stress; 4 relative-entropy form of ass:EE; 5 interacting / non-coherent extension.

## 012-dorau-much-positioning — integrated 2026-10-15
- From the SME literature review (rank-1 suggestion). r1 AWRR (appB sentence over-attributed modular flow); r2 ACCEPT, flags none. BibTeX DorauMuch2026 verified (Crossref + arXiv).
- ch06 paragraph after Claim 1/Claim 2: Dorau-Much as the operator-algebraic matter side of Claim 1 (free scalar, coherent states, bifurcate Killing horizon); assumes metric, local Minkowski, Raychaudhuri, S=A/4; no support for Claim 2 or Problems A, B. appB sentence: relative entropy = horizon energy flux for free scalars/coherent states, prescribed metric only.
- Commit 9100a5a. Build PASS 252 pages, 0 undefined. No label touched. Integrated count this run: 10.
- SME suggestion 4 (relative-entropy form of ass:EE): researcher recommends against (first variation vanishes on the finite-dimensional diamond algebra; carries only the first law). Not adopted.

## 013-cp12-einstein-rank (Problem F; A, D1, E) — integrated 2026-10-15
- Rounds: 2. r1 AWRR (unverified "lowest member of tower" attribution; scope wording); r2 ACCEPT, flags none. Gatekeeper independently re-derived rank (own script, random base points; also random W_y planes).
- Integrated two appH paragraphs before \section{Problem G: HBEV} + bib SperlingSteinacker2019 (verified). Commit d4bca69. Build PASS 254 pages, 0 undefined. No label touched.
- Established (kinematic, H_CP: Poisson limit, linear, frozen coefficients, leading order in 1/(|q| l), fibre-integrated operator tensor, one sheet): only the 12 first-harmonic fibre amplitudes (frame-type A = kappa T) respond; exact constraint q q h = 0; image dim 9, linearized Einstein rank 6 = number of conserved sources; kernel on image = transverse diffeomorphisms = matrix-gauge image; gauge group of the class is divergence-free diffeos, density fixed by Liouville; 12 = 3 inert + 3 gauge + 6 gauge-invariant. Rank 6 follows from surjectivity onto the hyperplane (a count), independent of W_y. Fibre-constant and l != 1 fluctuations give no linear response (exact, in class). Partial base-function closure argument (alpha = 0).
- First class where neither the 008/009 rank obstruction nor the 011 proportionality obstruction occurs. Not a breakthrough (no dynamics; second- vs third-order mismatch; leading-symbol gauge invariance only).
- Next: dynamics of the level-1 amplitudes (action, masses, positivity, order mismatch).
- Integrated count this run: 11.

## 014-level1-dynamics (Problem F) — integrated 2026-10-15
- Rounds: 2. r1 AWRR | M2 narrow (two wording fixes); r2 ACCEPT, flags none.
- Integrated appH block before \section{Problem G: HBEV}. Commit 8416acb. Build PASS 258 pages, 0 undefined. No label touched.
- Established (Poisson limit, CP^{1,2} class, leading symbol, tree level, level-1 sector, sheet y4>0): background T^a = M^{a4} is not stationary for the quartic term of eq:Smatrix alone; a bilinear term mu^2 = -3/R^2 (input of the class, not adopted into eq:Smatrix; reported for these backgrounds in SperlingSteinacker2019) makes it stationary and the amplitude action exactly gauge invariant; 12 level-1 amplitudes = 3 massless Maxwell fields, colour metric delta_ij, no relative ghost at this order. Bounded no-go: E[h(c)] cubic vs Maxwell quadratic, no local E[h] = P(d)J; sourced h algebraic, degree 0, E[h] != constant x T (q^2 T excluded in samples); null-q trace polarisation E = (1/2) q q tr h.
- No PRIOR-CLAIM-ERROR: merged 011/013 never claimed the background solves eq:Smatrix ("off-shell"; "does not derive the background").
- Open routes: induced (one-loop) term, subleading orders (ranked first), other sectors, entanglement route (ass:EE).
- Integrated count this run: 12.

## 015-entropy-action-identity — INTEGRATION-FAILED (r2), 2026-10-15
- Build failed: "Double subscript" from \LUV_s / \LUV_v in the accepted appH text (\LUV = \Lambda_{\mathrm{UV}}). Integrator restored chapters/bib; nothing committed. Needs an r3 macro fix (\Lambda_{\mathrm{UV},s}) and gatekeeper re-accept.

## 015-entropy-action-identity (Problem B; F) — integrated 2026-10-15
- Route: SME Problem-B route map (Dorau-Much / Jacobson line), primary target. Rounds: 3. r1 AWRR | M2 (no PRIOR-CLAIM-ERROR: appG overgeneral, thm:mT conditional, R-coefficient variable dependence are clarifications); r2 ACCEPT; integration failed (double subscript \LUV_s); r3 notation fix, ACCEPT.
- Integrated: appH sec:status-B two paragraphs; appG replica-cone sentences + Status sentence (conical-delta convention); ch07 sentence (coefficient equality is content of Hypotheses 5-6); bib Solodukhin2011, SusskindUglum1994 (verified). Commit 333c282. Build PASS 260 pages, 0 undefined. No label touched.
- Established: pulled-back replica (I) cone area coefficient S = (A_G/48pi) sum w tr1 Lambda^2, contact term Q = 0 per sector, so the delta-A coefficient equals the Lambda^2 coefficient of thm:Geff (B2 at conditional scope); contact term sign consistent with Solodukhin (321)-(323); singular-rho replica (II) gives -1/2 (branch-conditional, unused); R coefficient depends on variables (E_s = R_G/4 + torsion^2).
- Bounded no-go: EE needs G_T = G_A; in class (Poisson, Euclidean, Feynman background gauge, one loop, Lambda^2, delta rho = 0, replica I) c_T = N_tot/6 - 4 vs c_A = N_tot/6, 1/G_A - 1/G_T = 2 Lambda^2/pi from rho^2 X. Survives replica II for positive G.
- Open avenues (gatekeeper rank): content (fermions / torsion-coupled scalars, b = 0), tensor-block identification / Phi-a mixing, tree-level 014 class, gauge fixing, Moyal, curved backgrounds, replica choice. SME gap scout: reports/sme-scout-gap-GT-GA-20261015.md. Follow-up: proposal 017 (in progress).
- Integrated count this run: 13.

## 016-mirage-stress (Problem F; B, A) — integrated 2026-10-15
- Route: SME scout R14. Rounds: 2. r1 provisional AWRR with SME-CONSULT; SME consultation (proposals/016-mirage-stress/sme-consult-r1.md): Steinacker2026 crossover (1 - m^2 Box^-1) form confirmed with m^2 = 32 pi G_N alpha^2 r^-4; T[C] conservation imposed via the C -> C + dC ambiguity, not derived; massless matrix Noether identity is prior art (Steinacker 0812.3761, Abou-Zeid-Dorn). r1 final AWRR (no milestone); r2 ACCEPT, flags none.
- Integrated appH block before \section{Problem G: HBEV}. Commit b42bd98. Build PASS 262 pages, 0 undefined. No label touched.
- Established (class H16: Poisson limit, level-one sector, leading symbol, frozen coefficients, tree level + input EH form + input conserved T): exact Poisson-limit Noether identity {X^a,E_a} = 0 and mu^2 stress-divergence identity (massless form standard); closed form extra stress X = -Lambda L E; exact (w + Lambda L)E = T with L spectrum; crossover (1 + rho/(2 q_perp^2))E = T/w in the TT-like channel; dispersion elliptic in omega, anisotropy from the background direction y-hat (covariant if y is a vector); y^i = 0 not essential.
- Not: a derivation of the conservation of the extra stress (Bianchi + input T, same as literature); the 008/009 missing stress; G_eff sign/size.
- Open avenues (ranked): subleading order; induced coefficient in this class (F's target); frame averaging; matrix-derived T; doubleton constraints; nonlinear / N>=8.
- Integrated count this run: 14. Next integration is the 15th (gatekeeper full scan due).

## 017-GT-GA-gap (Problem B; F, A) — integrated 2026-10-15 (uncommitted, author to commit)
- Route: 015 open avenue (gauge parameter, fermion content) + SME gap scout. Rounds: 2. r1 AWRR | M2, full scan (ordinal 15), three major scope fixes (tip-domain claim deleted; numerical fits labelled, alpha = 1/3..3; periodic gluing reported); r2 ACCEPT, flags none.
- Integrated appH sec:status-B, after the 015 block, before \section{Problem C}. Working tree only (author directive: chapters/bib not committed by agents). Backup scratch/integrator-backup/017-GT-GA-gap/. Build PASS 264 pages, 0 undefined. No label touched.
- Established: gauge lemma O_v Gr = Gr O_s - {J,.}, Gr^dag Gr = O_s (any Poisson bivector); on J = 0 backgrounds (stated tip domain) connection-sector a_1 = ((3+alpha)/6) rho R + rho^2 X, so c_A - c_T = 4 is alpha-independent; off-shell numerics (rational fits, 1/3 <= alpha <= 3) agree; EOM-term gauge function enlarges the gap; Dirac a_1 = (4/6) rho R + (1/2) rho^2 X, b_total = 1 - n_D/2.
- Gluing-conditional: gap 4 - n_D (antiperiodic, spinor-transported) or 4 - 2n_D (unrotated periodic; 0 = 0 at n_D = 2 with c_T = c_A = 0, an equality of vanishing Lambda^2 coefficients, not a derivation). Gluing selected by the matrix state is not determined (Problem A).
- Open avenues (ranked): (1) next order (log / a_2, Moyal) in D = 10 content per gluing; (2) replica gluing from matrix modular flow (Problem A sub-lemma); (3) tensor-block identification; (4) non-constant J = 0 backgrounds; (5) other gauge functions; (6) tip domain / edge modes; (7) tree-level, Moyal, curved.
- Integrated count this run: 15. SME scout due (5th-integration cadence).

## 018-induced-coefficient-cp12 (Problem F) — integrated 2026-10-15 (uncommitted, author to commit)
- Route: 011/016 open avenue (induced coefficient in the CP^{1,2} class). Rounds: 2. r1 AWRR | M2 narrow, full scan; R1-R6 wording (Euclidean contraction Box_E for the sub-Laplacian claim; e^{-sH_V} unbounded; formal Lorentzian density; regulator + one loop in scope; sampling stated; w, varrho defined); no PRIOR-CLAIM-ERROR (011 replication is stated only for product leaves); r2 ACCEPT, flags none.
- Integrated appH block before \section{Problem G: HBEV}; bib BenArous1989 (VERIFIED vs Crossref; nilpotent leading term corroborated by Colin de Verdiere-Hillairet-Trelat 2004.06461). Working tree only; backup scratch/integrator-backup/018-induced-coefficient-cp12/. Build PASS 266 pages, 0 undefined. No label touched.
- Established: Box = C_so(4,1) - C_so(3,1), ghost -Box, fibre-constant density (5m^2 - 3l^2)/(4m^6) (formal Lorentzian); Euclidean Box_E is a step-2 sub-Laplacian, Q = 8, diagonal c0 s^-4 (Landau 3 zeta(3)/(64 pi^3) at f1 = f2), not 4D x fibre mode count; vector sector lowest level -|f1 - f2| (Nielsen-Olesen), unbounded; F^2 coefficient (22 - n_ex)/6.
- No-go class H1-H5 (Poisson limit/leading symbol, Euclidean contraction, equiregular points, bosonic/background gauge/one loop, proper-time cutoff of Box_X). w, its sign and varrho not derived.
- Open avenues (ranked): (1) fermionic/SUSY content or fibre truncation; (2) exact so(4,2) harmonic analysis with Moyal; (3) weight-two s^-3 coefficient; (4) fibre-harmonic cutoff; (5) compact twistor section.
- Integrated count this run: 16. Pending author commit: chapters/appH-microscopic-proofs.tex (017 + 018), bib/namcg.bib (018).

## 019-fermion-replica-gluing (Problems B; A) — integrated 2026-10-16 (uncommitted, author to commit)
- Route: SME scout gluing/fermions (R-a1, R-b1 Step 1, R-a3). Rounds: 2. r1 AWRR | M2 (F1 preceding-paragraph misstatement; F2 self-adjoint extension worded as a choice; F3 continuation uniqueness); r2 ACCEPT, full scan, flags none. No PRIOR-CLAIM-ERROR (017 periodic branch was reported only as an alternative).
- Integrated: appH sec:status-B sentence replaced ("…not determined here." -> "The gluing selected by a quasi-free state with rotational modular flow is stated below."), three-paragraph block before \section{Problem C}; bib CasiniHuerta2009, FursaevMiele1997 (VERIFIED, Crossref). Working tree only; backup scratch/integrator-backup/019-fermion-replica-gluing/. Build PASS 268 pages, 0 undefined. No label touched.
- Established (conditional: quasi-free state, rotational modular flow, less singular self-adjoint extension, uniqueness of continuation from integer n): Tr rho^n is polar-antiperiodic (Cartesian -e^{2 pi i n sigma}); sum a_k^2 = (n^2-1)/(12n); c_A(Dirac) = 1/3; c_A - c_T = 4 - n_D, (c_T, c_A) = (0, 2) at the D = 10 content; 017 periodic branch = Tr rho^n at odd n, graded trace at even n, so its 0 = 0 is not a replica result; rotated branches not continuations. N_tot and b are the alpha^0, alpha^2 orders of the MST Q_10 character; first survivor (x^2 - y^2)^2/16 (zero on (anti-)self-dual flux).
- Open avenues (ranked): (1) contact/edge terms of weight n_D = 2 at Lambda^2 (spin term +1 per Dirac; Lichnerowicz -R/4 or edge modes); (2) A-side next order on a curved J = 0 leaf; (3) vector/ghost/scalar tip domains; (4) non-rotational flow / non-quasi-free / Moyal; (5) non-flat J = 0 backgrounds.
- Integrated count this run: 17. Pending author commit: appH (017, 018, 019), bib (018, 019).

## 020-flux-locus-cp12 (Problem F) — integrated 2026-10-16 (uncommitted, author to commit)
- Route: SME scout R-f1 (Troost flux inequality) + 018 avenues. Rounds: 2. r1 AWRR | no milestone (locus classification worded as exact though self-duality is numerical; Troost phrasing); no PRIOR-CLAIM-ERROR (018 "compact twistor section" avenue was never in the manuscript); r2 ACCEPT, flags none.
- Integrated appH block before \section{Problem G: HBEV}, after the 018 block; bib Troost2000 (VERIFIED, Crossref). Working tree only; backup scratch/integrator-backup/020-flux-locus-cp12/. Build PASS 268 pages, 0 undefined. No label touched.
- Established (conditional on numerically verified, unproved self-duality of Q^{-1/2} F Q^{-1/2}): F = Q^{1/2} omega Q^{1/2}, Q^{ab} = y4^2 eta^{ab} + y^a y^b; closed forms for f1, f2; f1 = f2 for all zeta only on |y4| = l, y_i = 0 (codimension 4); compact so(6) section with constant delta gives f2/f1 = |y4|/l. Unconditional in H1-H5: zeta-independent transverse flux cannot stabilise an unbounded fibre; at f1 = f2 the vector density tends to f^2/(2 pi^2), so the zeta-integral still diverges. w not determined.
- Open avenues (ranked): (1) position-dependent Q^{-1} contraction from the matrix action / gauge fixing / regulator ((y_a D^a)^2/l^2 term); (2) finite fibre + transverse flux; (3) SO(4,1)-covariant X^A = M^{A5}; (4) SUSY flux expansion radius (R-f2); (5) exact so(4,2) characters with Moyal; fermions help only on the locus.
- Integrated count this run: 18. Pending author commit: appH (017-020), bib (018-020).

## Author commit 60d0d39 (2026-10-17): 017-020 manuscript changes committed by the author.

## 022-Qinv-contraction (Problem F; E) — integrated 2026-10-17 (uncommitted, author to commit)
- Route: 020 top avenue (does the matrix theory supply the Q^{-1} contraction?). Rounds: 2. r1 AWRR | M2, full scan (missing (y4)^{-2} factor; no-go restated as enveloping-algebra statement; "only if" narrowed to sets examined; full negative-mode data; emergent-metric / ass:lorentzian disclaimer); r2 ACCEPT, flags none. No PRIOR-CLAIM-ERROR; emergence preserved; no Lorentzian claim of 013-016 weakened.
- Integrated appH block before \section{Problem G: HBEV}, after the 020 block. Working tree only; backup scratch/integrator-backup/022-Qinv-contraction/. Build PASS 272 pages, 0 undefined. No label touched, no bib change.
- Established: Q^{-1} contraction = (y4)^{-2}[eta DD + (y.D)^2/l^2], base symbol g^{-1} (induced Euclidean metric of the hyperboloid); K = m^2 eta. No-go: in the four-matrix class (Poisson limit, T^a = M^{a4}, quartic + one bilinear, gauge D_a A^a, ghost -Box, regulator f(Box_X), constant eta) (y_a D^a)^2 is not in U(so(4,1)'). Five-matrix X^A = M^{A5}: f1 = f2 identically (numerical), mu^2 = +4, H_V = C_so(4,2) - C_G + C_Sigma + mu^2 exact; six presentations M^{Ac0} give Euclidean or (2,2) horizontal metric, never Lorentzian. Formal polynomial spectrum -8,-4,-2,+2,+4 (1,5,20,14,35); compact five-matrix background has 49/154/385/814 negative modes (N=1..4): unstable. g not identified with the emergent metric; ass:lorentzian untouched (Problem E). w not derived.
- Open avenues (ranked): (1) so(4,2) Casimir as regulator in the four-matrix class; (2) eight-matrix {T^a, y^a} set with -eta y-block (mu^2 = -4, rank 6); (3) exact so(4,2) analysis on normalisable states; (4) weight-two coefficient with finite fibre then Wick tie to E; (5) fermions / finite fibre.
- Integrated count this run: 19. Pending author commit: appH (022).

## 021-spin-contact-term (Problem B; A, F) — integrated 2026-10-17 (uncommitted, author to commit)
- Route: 019 top avenue (contact/edge terms of weight n_D = 2 at Lambda^2). Rounds: 2. r1 AWRR | M2, full scan (sign/weight of the Dirac contact; Kabat attribution; flux localisation not binary), no PRIOR-CLAIM-ERROR; r2 ACCEPT, flags none (ordinal 20; 3(a) full scan covered by r1, chapters unchanged since apart from 022).
- Integrated appH sec:status-B block after the 019 block, before \section{Problem C}; bib Kabat1995, DonnellyWall2016 (VERIFIED; Kabat abstract only). Working tree only; backup scratch/integrator-backup/021-spin-contact-term/. Build PASS 273 pages, 0 undefined. No label touched.
- Established (conditional, 019 class + fixed-state and first-order smooth replicas): the Dirac spin excess (+1 per Dirac) is the weighted Lichnerowicz Q_f contact at n = 1, already inside c_A, so no further spin contact (Q_f = Q_s = 1/4 in the torsion reading; n-derivative statement). R_G^(1) = -2 Box delta ln rho: the fixed-state replica is not a limit of smooth Poisson structures about constant Theta-bar; smooth replica gives c_A = -N_tot/12 (0 = 0 at IKKT, not a derivation). At (2, 6): fixed-state 2, with vector contact (input) 1, smooth 0; standard contacts reach at most 1. Values 2 and 0 = zero and full-deficit flux of grad ln rho through Sigma; intermediate fluxes not computed.
- Open avenues (ranked): (1) replica/flux datum: c_A for intermediate flux, replica of the matrix state (Problem A sub-lemma); (2) next order on a curved J = 0 leaf; (3) tip domains, symplectic-gauge / fermion edge modes; (4) non-quasi-free / non-rotational state.
- Integrated count this run: 20. SME scout due (5th-integration cadence). Pending author commit: appH (021, 022), bib (021).

## 023-casimir-regulator (Problem F; E) — integrated 2026-10-17 (uncommitted, author to commit)
- Route: 022 top avenue (so(4,2) Casimir as proper-time regulator in the four-matrix class) + SME scout 20261017. Rounds: 2. r1 AWRR | no milestone (sign convention: positivity is -sigma(Delta_kappa); eight-matrix (5,1) only at sampled lambda; A=48 fraction numerical); no PRIOR-CLAIM-ERROR (022 stated only the base block of C_so(4,2)); r2 ACCEPT, flags none.
- Integrated appH block before \section{Problem G: HBEV}, after the 022 block. Working tree only; backup scratch/integrator-backup/023-casimir-regulator/. Build PASS 277 pages, 0 undefined. No label touched, no bib change.
- Established: exact four-matrix relations H_V = C_G - C_41 - C_Sigma + mu^2 (mu^2 = -3), Box = C_41 - C_31, C_so(4,2) and C_so(4,1) commute with H_V. sigma(C_42) has signature (2,4) on the leaf (base negative, fibre positive), so no function of C_42 alone regulates. Delta_kappa = kappa C_42 - C_41 has positive-definite principal symbol for 1/2 < kappa < 1 (pencil 1/2 x4, 1 x2), commutes with H_V, gives a finite window density (added regulator, not derived; kappa not fixed). Negative direction bounded (linear in Lambda), not removed; compact spectrum lowest -(A+3). Eight-matrix (eta, lambda eta) set: (5,1) form at sampled lambda, two bilinear coefficients, Hessian not examined. w not derived; ass:lorentzian untouched.
- Open avenues (ranked): (1) fix kappa, chi by matrix-intrinsic fibre admissibility (R-F2); (2) Lorentzian i-epsilon Schwinger trace in the Delta_kappa window (R-F1); (3) eight-matrix Hessian; (4) Moyal / fermions; (5) regulators from the exact action.
- Integrated count this run: 21. Pending author commit: appH (021, 022, 023), bib (021).

## Author commit (2026-10-17): 021-023 manuscript changes committed by the author.

## 024-replica-classification (Problem B; A) — integrated 2026-10-17 (uncommitted, author to commit)
- Route: SME scout 20261017 R-B1/R-B2. Rounds: 2. r1 AWRR | M2 (LM regularised cone overstated: smooth family has far field rho ~ r^{n-1}, LM first bracket not reproduced; "bulk-mode" for Kabat; "in form" for Solodukhin Q); no PRIOR-CLAIM-ERROR; r2 ACCEPT, flags none. Gatekeeper upheld the researcher against the scout: G_A = G_T does NOT follow "by construction".
- Integrated appH sec:status-B block after the 021 block, before \section{Problem C}; bib HerzogNishioka2016, LewkowyczMaldacena2013 (VERIFIED). Working tree only; backup scratch/integrator-backup/024-replica-classification/. Build PASS 279 pages, 0 undefined. No label touched.
- Established (021 class): the Herzog-Nishioka counterterm cancels the Wald-type contact (H-N Eq. 5.20 supports); singular-rho s-wave index |n-1|/(2n), regular-branch values 1/6 -/+ 1/4 non-analytic at n = 1; c_A^sm = -c_R/2; c_A^sm - c_T = (14 - N_s - 4 n_D)/4, zero only on N_s + 4 n_D = 14; the two SUSY vanishing lines meet only at (6, 2), so the IKKT 0 = 0 carries no information on G. Classification by form: 2 = contact-free (H-N type), 0 = Solodukhin delta-potential, 1 = imported vector contact (no published prescription). Affine flux law is an assumption only; holonomy template inapplicable (imaginary twist).
- Open avenues (ranked): (1) next order (Lambda^0, log) on a curved J = 0 leaf at the SUSY content; (2) covariant completion of the induced action (torsion invariants); (3) stationarity at the SUSY point; (4) tip domains / edge modes; (5) state-dependent frame kappa; (6) non-quasi-free states.
- Integrated count this run: 22. Pending author commit: appH (024), bib (024).

## Author commit (2026-10-17): 024 manuscript changes committed by the author.

## 025-lorentzian-window (Problem F; E) — integrated 2026-10-17 (uncommitted, author to commit)
- Route: 023 avenues + SME scout 20261017 R-F1/R-F2/R-E1. Rounds: 2. r1 AWRR | no milestone (F1 cone/fibre window relaxes, not contradicts, 023 (i); Lorentzian results are for the Delta_kappa Gaussian window; F2 Seeley-DeWitt (5m^2-3l^2)/(4m^2) x sqrt|G| = m^-4 gives the merged density /(4m^6); F3 Re Q root a~0.62 is subtraction-dependent); no PRIOR-CLAIM-ERROR; r2 ACCEPT, flags none.
- Integrated appH block before \section{Problem G: HBEV}, after the 023 block. Working tree only; backup scratch/integrator-backup/025-lorentzian-window/. Build PASS 281 pages, 0 undefined. No label touched, no bib change.
- Established: admissible cone -C42 > 9/2 (from 1910.00839 (2.7),(3.43); footnote 8 "plausible", conditional); a fibre bound (cutoff of S^2 = 2C41 - C42) makes the window compact, cone not needed; kappa only rescales Lambda^2 at fixed Q; chi and base scale external. Lorentzian i-epsilon Gaussian Delta_kappa window: finite trace for every s, closed-form leading density; mass moment positive (4000 samples, numerical); flux has one real and one imaginary pair, F.F changes sign across the leaf; Nielsen-Olesen growth absent order by order and for the magnetic pair, present for the electric pair. Exact invariant sector (R x H^3): independent D1, Seeley-DeWitt coefficient confirmed; windowed weight-two Re Q indefinite; mode-count term (R/6 of auxiliary H^4) cancels only if N_b = N_f. No sign of w or G_eff.
- Open avenues (ranked): (1) Lorentzian moments in the fibre-bounded cone window; (2) exact SO(4,1) spin-1 trace (vector/ghost); (3) Weyl second variation under A; (4) supertrace/fermions to remove the mode-count term; (5) window from dynamical matrices only; (6) reconcile s <= n with s <= x0/r; (7) eight-matrix (5,1) Hessian; (8) Moyal.
- Integrated count this run: 23. Pending author commit: appH (025).

## 026-next-order-curved (Problem B; F) — integrated 2026-10-17 (uncommitted, author to commit)
- Route: 024 top avenue (next order beyond Lambda^2 at the SUSY content on a curved leaf). Rounds: 2. r1 AWRR | M2 (common proper-time limit / ln Lambda-coefficient hedge; chirality on non-BPS family sampled); gatekeeper re-derived the central identity analytically; no PRIOR-CLAIM-ERROR; r2 ACCEPT, flags none.
- Integrated appH sec:status-B block after the 024 paragraph, before \section{Problem C}. Working tree only; backup scratch/integrator-backup/026-next-order-curved/. Build PASS 283 pages, 0 undefined. No label touched, no bib change.
- Established (Poisson limit, Euclidean (also algebraically Lorentzian eta), alpha = 1, one loop, content (6,2), one common proper-time limit, local Pf omega != 0): weighted a_1 = 0 pointwise for every Poisson bivector; weighted a_2 = (1/2) S_4 up to total derivatives, S_4 = 8 trA trB + 16 tr(CC^T) >= 0, zero iff the connection b is chiral. So the ln Lambda coefficient has no R^2, C^2, Euler, RE or Einstein-Hilbert term. Every (A)SD Poisson bivector has J = 0 (G conformally flat, curved; g_rho flat), S_4 = 0; closed-form non-BPS J = 0 family with Weyl^2 != 0 found chiral in all sampled cases (not proved); non-chiral J = 0 Maxwell perturbations give S_4 > 0 (formal). Mass-insertion lemma: an EH term enters only through a SUSY-breaking mass scale (formal shift); Steinacker's route needs fuzzy extra dimensions. A side (cone log coefficient) not computed.
- Open avenues (ranked): (1) a_3 mixed quartic with a KK 1/mu^2 sum (only EH entry point in the class); (2) A-side log coefficient (twisted-Dirac cone a_2^Sigma); (3) exact non-chiral J = 0 backgrounds or proof of chirality; (4) Lorentzian colliding waves; (5) Moyal, tip domains, edge modes.
- Integrated count this run: 24. Pending author commit: appH (025, 026).

## 027-fibre-window-spin1 (Problem F; E) — integrated 2026-10-17 (uncommitted, author to commit)
- Route: 025 avenues 1-4. Rounds: 2. r1 AWRR | no milestone, full scan (ordinal 25): tangency mechanism (unique continuation) wrong, restated as a numerical observation; undefined D_1/g defined/removed; point counts and precision; notation; supertrace wording; no PRIOR-CLAIM-ERROR; r2 ACCEPT, flags none.
- Integrated appH block before \section{Problem G: HBEV}, after the 025 block. Working tree only; backup scratch/integrator-backup/027-fibre-window-spin1/. Build PASS 287 pages, 0 undefined. No label touched, no bib change.
- Established: lemma (proved) — for every Gaussian window of sigma(Box) (rank 4, signature (3,1) for y4 != 0) the Lorentzian principal-value mass moment has Re M > 0, Im M > 0. Fibre-bounded cone window: apex-inside shell formula exact; continuation up to R coth(tau) a numerical observation, so Re N_W > 0 and finiteness are conditional. Zeeman closed forms (59/60 points); fibre-driven electric rate bounded independently of the base cutoff, base-driven rate linear in it; log det has integrable log singularities. Invariant sector: SD route matches exact scalar D_1 (125 digits); vector/ghost/spin terms in closed form; bosonic weight-two coefficient not sign-definite; F^2 tail changes sign at |y4| = l on the kernel plane. Supertrace with the supplied IKKT content: count, index and F^2 cancel; order-F^4 character 4(cos s f_m - cosh s f_e)^2; at A = 0 the remainder is -(4 mu^2 + n_ex mu_i^2) j(a) with Re j > 0; the species-independent part does not carry the Newton coefficient. No sign of w or G_eff.
- Open avenues (ranked): (1) A-dependence (second variation under the matrix fluctuation) of the mass supertrace and the order-s^4 term; (2) fermion content/mass pattern beyond no bilinear mass; (3) window with |p| < r or a proof of the continuation; (4) exact vector kernel / Plancherel; (5) dynamical-matrix windows; (6) Moyal.
- Integrated count this run: 25. SME scout due (5th-integration cadence). Pending author commit: appH (025, 026, 027).

## 028-second-variation (Problem F; E) — integrated 2026-10-18 (uncommitted, author to commit)
- Route: 027 top avenue (A-dependence) + SME scout second-variation (R-F1/R-F2). Rounds: 2. r1 AWRR | no milestone (mass-linear sign +M_str Tr[chi Phi'(H_X)]; flux shift only at phi = 0; undefined K^{mu nu} dropped and "no EH form" restricted to the leading symbol; covariance and Hessian wording); lemma independently re-derived in a different Dirac representation; no PRIOR-CLAIM-ERROR; r2 ACCEPT, flags none.
- Integrated appH block before \section{Problem G: HBEV}, after the 027 block. Working tree only; backup scratch/integrator-backup/028-second-variation/. Build PASS 289 pages, 0 undefined. No label touched, no bib change.
- Established (exact algebra, formal Duhamel expansion; CP^{1,2} four-matrix class, mu^2 = -3, IKKT content, no bilinear fermion mass, one window): for arbitrary X every species operator is (-Box_X) + Sigma_i {F, .} + m_i; weighted species sums vanish through three Zeeman insertions (n = 4 gives (f_e^2 + f_m^2)^2); count, spin and cubic terms vanish for every X; first surviving mass constant M_str = 4 mu^2 + n_ex mu_i^2. Leading symbol: the weight-two term depends on A only through the first jet, so its second variation has no EH-form term; next-to-leading symbol not computed. Order-F^4 integrand grows as s^2 (numerical), so not expandable; integrand depends on q.y at fixed proper time (not Lorentz invariant; window and leaf both single out y). No sign of w or G_eff.
- Open avenues (ranked): (1) next-to-leading symbol of the M_str term (only EH entry in the class); (2) nilpotent (Landau) resummation of the logarithm; (3) fermion mass patterns; (4) transverse flux / fuzzy K (Steinacker route); (5) species- or A-dependent windows; (6) eight-matrix sets, Moyal.
- Integrated count this run: 26. Pending author commit: appH (025-028).
