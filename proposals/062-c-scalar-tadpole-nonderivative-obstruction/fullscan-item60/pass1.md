# item-60 full-scan PASS 1 of 5 — saved verbatim from the scan hand-back, run 2026-11-09
Scope: 16 files (all small appendices + ch01, ch05, ch09, ch15, ch18). Read-only scan agent (gatekeeper type); not a proposal review.

SCAN PASS 1 of 5 — item-60 mandatory full scan. Reading statement: digest + full literal reads of all 16 assigned files (every line read to exhaustion); targeted greps/reads of bib/namcg.bib, namcg-book7.tex macro block, and ch16 title for cross-checks. NOT a full-tree scan (other passes cover the other files).

PER-FILE (bytes / lines / read in full):
C:\Users\redgi\Projects\namcg-lab@gpu\chapters\appL-coupling.tex — 2,549 B / 61 L / yes
...\appF-field-equation.tex — 3,211 B / 93 L / yes
...\appG-sector-entropy.tex — 3,353 B / 67 L / yes
...\appI-gaia-wide.tex — 3,855 B / 83 L / yes
...\appK-endomorphism.tex — 4,133 B / 91 L / yes
...\ch18-epilogue.tex — 4,319 B / 92 L / yes
...\appD-empirical.tex — 4,630 B / 121 L / yes
...\appJ-summary.tex — 5,721 B / 123 L / yes
...\appC-integrator.tex — 7,889 B / 219 L / yes
...\appB-modular.tex — 8,789 B / 213 L / yes
...\appA-seeley-dewitt.tex — 10,303 B / 265 L / yes
...\ch15-numerics.tex — 11,881 B / 330 L / yes
...\appE-rar-bridge.tex — 13,446 B / 308 L / yes
...\ch05-lorentz-decomposition.tex — 16,243 B / 418 L / yes
...\ch01-geometrogenesis.tex — 16,316 B / 385 L / yes
...\ch09-ultraviolet.tex — 16,338 B / 391 L / yes
Total 132,976 B. All 16 confirmed CRLF working-tree line endings (byte-dump; an earlier grep loop was an msys artifact — files are CRLF, consistent with CLAUDE.md).

MECHANICAL
1. MAJOR — appC-integrator.tex L103–104: garbled/unbalanced sentence: "because the Newtonian force is minus the gradient of \(U_{\mathrm{N}}=-\Geff\)-less toy potential \(-G_{\mathrm{toy}}M\mu/d\)". The \Geff macro is embedded inside a math U_N definition mid-phrase; presumably intended "the \Geff-less toy potential U_N = −G_toy M μ/d". Needs smallest-text repair.
2. MAJOR (numerical, see also cross-file #1) — appE-rar-bridge.tex L48 and L221 state ν_√(g_gal)≈1.1. By the manuscript's own definition eq:appD-nu, ν_√(x)=1/(1−e^−√x) with x=g_gal/g_†∈[1.25,1.83] (appI: g_gal=(1.5–2.2)e−10, g_†=1.2e−10) gives 1.35–1.49 (35–49% residual), not ~1.1; 1.1 requires x≈5.7. appI separately says "residual of order 20%" (x≈3.2). Three mutually inconsistent characterizations of the same quantity across appE/appI.
3. appE L219 "Theorem~7.3" and L283 "Assumption~E.1" — hard-coded theorem/assumption numbers where \ref/\autoref is required.
4. Hard-coded chapter pointers throughout (convention requires \ref): appL L6 "Chapters~3--12"; appF L44 "Chapter~11", L87 "Chapter~14"; appG L48 "Chapters~6--7"; appC L5/148/218 "Chapter~15", L162 "Chapter~17"; appB Chapters 6,8,11,12,17 + "Appendix~B"; appA Chapters 5,8,13,17; ch15 "Chapter~16"×3, "Chapter~14", "Chapters~3--15", "Chapter~1", "Exercise~5 of Chapter~14"; appE Chapters 6,12,13; ch05 L340 "(Ch.~10)" + Chapters 3,4,6,7,17; ch01 many; ch09 Chapters 8,10,13,17; appJ L6/28/51/88/104. Pervasive but consistent; record for a future \ref sweep, none wrong as far as I could check.
5. ch01 L321–323 stale attribution: "Chapter~16 restates the whole derivation... Chapter~17 lists what would falsify the framework" — ch16 is titled "Assumptions, Predictions, and Falsifiers" (label ch:falsifiers) and ch17 is the agenda; the falsifier pointer is misattributed. MAJOR (content pointer wrong, not just format).
6. appI: in-text citations "Banik et al. 2024; Pittordis, Sutherland & Shepherd 2025; quality-framework study 2026" have NO \cite keys and NO bib entries — unsourced literature claims.
7. appD: "McGaugh, Lelli & Schombert (2016)" cited in text without \cite despite McGaugh2016 key existing; Lelli2016SPARC bib entry exists but is not cited in appD where the SPARC sample is introduced.
8. Orphaned precise numbers: appD tab:sparc_results χ²=1.695×10⁵ (fixed/free gs), 1.691×10⁵ (MOND), 1.960×10⁶ (baryons), 175 galaxies/3391 points appear ONLY in appD tree-wide; no reproduction script in repo — provenance not verifiable in-repo (not shown wrong). appK: Cassini |γ−1|≲2×10⁻⁵ and torsion-balance sin²θ≲10⁻¹³ uncited (Cassini value standard; sin²θ form unconventional).
9. Tree-wide greps: no TODO/FIXME/chat/process language in chapters/; NO duplicate labels (independent plain-string scan); no undefined \ref/\eqref/\autoref/\pageref originating from my 16 files; all \cite keys in my files resolve in bib/namcg.bib (86 keys).
10. DorauMuch2026 (appB, PRL 136, 2026): future-dated; NOT independently verified. Manuscript's use is appropriately hedged ("prescribed metric... says nothing about the matrix condensate").

AUDIT LIST (a)–(i)
(a) ch05/ch10: ch05 contains polar split Φ^IA=(v+σ)Λ, algebraic split eq:algebraic-split δΦ_μν=¼ηψ+F+T, count table sec:ch5-count (4⊗4=1⊕6⊕9, verified), six Goldstone orbit variables with "(Ch.~10)" pointer (L340), eq:F-split, unitary-gauge removal pointer. Thematic overlap with ch10 (Goldstone locking) is real at the pointer level; ch10 itself is not in my pass so duplication depth is a cross-file suspicion only. Also: ch01 eq:lorentz-split is verbatim identical to ch05 eq:notes-split (duplicated source-note split).
(b) ν-drift: CONFIRMED. One interpolator carries two names — ν_√ (eq:appD-nu) and ν_RAR (eq:appE-RAR) — plus retired ν_exp and ν=1 as a model selector in appD's table. Notation \nu_{\sqrt{}} (empty-brace subscript) renders a bare radical; consistent tree-wide in my files but typographically odd.
(c) static-tail labels: consistent; only appC L166–167 and appE point to eq:I-tail (ch14); no competing tail labels in my files.
(d) Kubo pairs: zero mentions in all 16 files (appear only ch14/appH tree-wide).
(e) α=−16πG_effβ_ECG: exactly 3 tree-wide occurrences as expected (appH:3256, ch09:242, ch13:98); only ch09 in my set. appH:3164 uses κ=+16πG_effβ_ECG (different symbol/sign, Problem J) — recorded, not drift.
(f) ζ collisions: none in my files (only ch04/appH tree-wide).
(g) G vs G_eff: appF eq:appF-Ein (bare G) vs eq:appF-NAMCG (8π\Geff) explicit comparison; appG names G_eff as curvature coefficient of thm:Geff, numerically unfixed; ch01 HBEV "K/8πG" uses bare G — consistent with each scope statement; no contradiction found.
(h) σ/𝓔⁽¹⁾/π^8: σ used both as ch05 radial fluctuation and appB density operator (minor collision); 𝓔⁽¹⁾ absent — appA uses W_E^{(1)} consistently; π^8 absent.
(i) even-subalgebra/θ-closure: no such statements in my 16 files; sole tree occurrence appH L1613 with the "closed under θ" qualifier (outside my pass).

NOTATION COLLISIONS (all locally defined; no in-equation clash found)
γ: six roles across my files — PPN γ (appK/appJ), boost ratio γ≡g_int/g_N (appE eq:appE-efe), Clifford γ^μ (ch05), redshift exponent γ (appL), drag γ (appC ex.5), (ch15 uses η for drag instead — inconsistent drag-symbol choice between ch15 lab (η) and appC ex.5 (γ)).
ξ: non-minimal coupling (appA), healing length (ch01), gauge vector ξ^μ (ch05/appB BW).
κ: surface gravity (appB eq:appB-BW) vs appH κ=16πG_effβ_ECG.
E: endomorphism (appA/appK) vs torsion T^A_μν / frame index E (ch09).
θ: phonon phase (ch01), tilt angle (appK), θ-automorphism (appH, outside set).
ψ: conformal mode — consistent across ch05/appB/appK.

INDEPENDENT RE-DERIVATIONS (checks, not proofs)
appA SDW a₀,a₁,a₂ and proper-time cutoff coefficients −a₀(Λ⁴−μ⁴)/64π², −a₁(Λ²−μ²)/32π², −a₂ln(Λ²/μ²)/32π²: all verified. ch05 4⊗4=1⊕6⊕9; tt-gauge −½η∂·ξ, δψ=2∂·ξ: verified. appE BE identity ν=1+n_BE(√x), small-x limit ν≈x^{−1/2}+½, and "wants γ≈4" at g_N=10⁻¹¹ m/s² (x=0.083→ν≈3.99): verified. ECG 𝒫 in ch09 matches Bueno2016ECG (PRD 94 104005) structure: verified against entry; article not refetched. ch15 toy params (G_toy=36, η=0.006, M=μ=1) consistent with appC exercises; appC's Exercise-3/4 pointers to ch15 verified correct.

CROSS-FILE SUSPICIONS (for other passes / orchestrator)
1. ν_√(g_gal): appE "≈1.1" (×2) vs appI "order 20%" vs definition-implied 35–49% at appI's own g_gal range — one of the three must change.
2. ch01 L321–323 falsifier/agenda attribution (ch16 vs ch17).
3. appI asserts wide binaries are consistent with Newton; bib entry Chae2023WideBinaries (ApJ 952 128) title asserts breakdown of Newton–Einstein standard gravity in wide binaries; appI does not cite it; article not fetched — tension flagged, claim about appI's literature position NOT independently verified.
4. ch01↔ch05 verbatim duplicate split (eq:lorentz-split ≡ eq:notes-split).
5. ch05↔ch10 Goldstone/unitary-gauge overlap depth (ch10 unread in this pass).
6. DorauMuch2026 and Whitler2025JADES entries future-dated; keys exist and are used carefully where read, but not independently verified.

Status-restatement check (record only, not judged): appJ and ch18 problem restatements (A,B,C,D1,E,F,G,N critical; H,I,J optional) match appH ledger conventions and Chapter 17 criterion; appB/appG/appK correctly declare "does not alter the ledger"; no status language in my files exceeds OPEN/PROGRAMME-CONDITIONAL wording.

Files with no noteworthy findings: appG (clean beyond hard-coded pointer), appL (clean beyond hard-coded pointer), appF (clean beyond hard-coded pointers; G/G_eff mapping properly scoped), ch18 (clean beyond hard-coded pointer), appJ (clean beyond hard-coded pointers).
