# item-60 full-scan PASS 2 of 5 — saved verbatim from the scan hand-back, run 2026-11-09
Scope: 12 main-text chapters (ch02, ch03, ch04, ch06, ch07, ch08, ch10, ch12, ch13, ch14, ch16, ch17). Read-only scan agent (gatekeeper type); not a proposal review.

SCAN PASS 2 (item-60 full scan) — complete literal read of all 12 assigned files. Digest was CURRENT (tree-hash d7b5c53dfa8cc1f7, dirty-chapters: yes). No writes made.

PER-FILE READS (all under C:\Users\redgi\Projects\namcg-lab@gpu\chapters\; bytes = on-disk, lines = file line count):
- ch02-preliminaries.tex — 23,615 B / 583 L — read in full: yes
- ch03-matrix-action.tex — 36,967 B / 916 L — read in full: yes
- ch04-vierbein-emergence.tex — 19,141 B / 442 L — read in full: yes
- ch06-entanglement-equilibrium.tex — 20,170 B / 458 L — read in full: yes
- ch07-massless-tensor.tex — 20,136 B / 476 L — read in full: yes
- ch08-heat-kernel.tex — 17,190 B / 411 L — read in full: yes
- ch10-lorentz-locking.tex — 20,005 B / 451 L — read in full: yes
- ch12-hbev.tex — 16,679 B / 400 L — read in full: yes
- ch13-cores-galaxies.tex — 16,631 B / 400 L — read in full: yes
- ch14-dissipation.tex — 16,520 B / 398 L — read in full: yes
- ch16-falsifiers.tex — 16,725 B / 362 L — read in full: yes
- ch17-agenda.tex — 39,519 B / 791 L — read in full: yes
Targeted audit reads (not scan-pass files): ch05-lorentz-decomposition.tex (full, for audit (a)); ch10:320-369; ch09-ultraviolet.tex (grep window); appH-microscopic-proofs.tex (targeted greps/windows at 2444-2450, 2459-2481 excerpts, 2665-2669, 3034-3069, 3217, 3243-3260 — appH itself scanned by other passes).

MECHANICAL:
1. Label existence: one tree-wide grep verified every \ref/\eqref in my 12 files resolves to a defined \label (incl. eq:stelle/eq:W4 ch09:111/62, ass:sqrt-mod appE:155, prop:allowed-drag/eq:four-force/thm:conservation ch11:230/191/116, app:seeley-dewitt appA, app:field-eq appF, eq:Uent-def ch06:295, ass:local-lorentz/prop:B-torsion-free ch10:56/238, def:vierbein/def:composite-metric ch04:117/156, ass:aux-metric/eq:Smatrix/eq:Smicro/eq:V ch03:88/143/221/241, ass:laplace ch08:92, eq:W-EH ch08:210, eq:Leff ch12:216, eq:f-reg/eq:nu-sqrt ch13:84/265, eq:ECG/eq:S-ECG/ass:ECG/ass:EFT-a2 ch09, eq:Z-sigma ch17:246). No undefined refs found. Digest: "duplicate labels: none" — consistent.
2. Hard-coded numbers in prose (style violations, no \ref): ch02:490 "Theorem~2"; ch02:107 "Chapter~10"; ch08:338-350 table "Ch.~17"/"Ch.~9"; ch10:347 self-referential "(Ch.~10)"; ch16:214 "Theorems~7.3--12.4"; ch16:275 "Theorem~7.3"; ch16:267 "Appendix~D". These are fragile under renumbering.
3. No TODO/FIXME/chat language found in my 12 files.
4. ch08:1 `\chapter[Heat kernel and $\Geff$]{...}` — macro defined in namcg-book7.tex:53-56 preamble before chapter inclusion; legal (moving argument contains expandable math). OK.

AUDIT LIST (a)-(i):
(a) RESOLVED. ch10 does NOT re-derive the polar/algebraic split; it references eq:polar/eq:linear-frame/eq:vev-is-frame/eq:Phi-transform (ch05). Duplication depth = ONE verbatim-duplicated bookkeeping table: ch05:332-357 ≡ ch10:334-364 (plus duplicated lead-in sentence), including the self-referential "removable in unitary gauge (Ch.~10)" at ch10:347 pointing at its own chapter. Both tables use F_{μν} for Goldstone orbit angles — collides with the field-strength F^{CD}(B) used in ch10's own torsion analysis.
(b) ν-drift CONFIRMED. ch13:255 and ch16:208 both assert ν_√(g_gal)≈1.1, but the manuscript's own eq:nu-sqrt (ch13:265, ν=1/(1−e^{−√(g/g_s)})) at g_gal≈2.2e-10 with default g_s=g_†=1.20e-10 (ch13:271, \cite{McGaugh2016}) gives 1.348. ch16:212 "a surviving γ≈1.4 is not explained by that saturation" also conflicts: saturation at that g gives ≈1.35, close to 1.4. Isolated ch16 γ≈4 at g=10⁻¹¹ is consistent with the definition (ν≈1.005→ slope ≈4 ✓). g_gal≈2.2e-10 (ch13:253) is uncited — orphaned precise number.
(c) static-tail labels: ch14 eq:I-tail (159) restates ch06 eq:I-falloff with the same c_{p_*}; cross-referenced, not contradictory. Recorded.
(d) Kubo pairs: ch14 eq:linear-response (122), eq:Gamma-kubo (133) ↔ appH:3034-3068 "Conditional Kubo formulation" — conventions IDENTICAL (χ^R=(i/ħ)θ⟨[δF,δF]⟩, δH=−δr·δF, Γ=lim_{ω↓0}Imχ^R_{(ij)}/ω; appH adds ℓ_A,ℓ_B arguments). No sign/factor mismatch. ch14 Γ=ημ/d⁴ (172) consistent with eq:Fdiss (188). Minor wording ambiguity only: ch14's kernel-definition sentence could mislead on the source sign; appH's δH=−δr·δF is explicit.
(e) RESOLVED: α=−16πG_effβ_ECG identical at ch09:242, ch13:98, appH:3256. ch13:98 r_*∼|αM|^{1/5} matches appH:3260 and the appH tail −216αM²/r⁶ (appH:3243+). NEW tension: ch13:91 r₀³=2β_ECG M requires [β_ECG]=L² while r_*⁵=αM requires [α]=L⁴, i.e. [β_ECG]=L⁴ in the same G=1 units — inconsistent dimensions for the same β_ECG between the two model formulae. Both are flagged model/non-derived in text (ch09:251, ch13), and eq:stelle's C² coupling α_Weyl is disambiguated at ch17:506-510 — record only.
(f) ζ collisions, ch04 side + appH: ch04 ζ^μ = coordinate/diffeomorphism shift (340-354); appH:471 ζ = Hamiltonian vector field (same meaning, consistent); appH:1440 ζ(y) null fibre vector (ζ·y=ζ·ζ=0); appH:2446 ζ = scalar metric-perturbation amplitude (δg=ζh, w=−ζ²/16πG_eff); appH:2459-2624 ζ∈ℝ² Landau/centre variable with d²ζ measure. ≥4 distinct meanings in appH alone; each locally disambiguated — notation watch, no contradiction found.
(g) G↔G_eff: \Geff used consistently in ch12 (eq:GHY-again 92, eq:SHBEV 117, eq:BY 174, eq:EFE-Leff 211, eq:Leff 216); no bare-G-where-G_eff-demanded found in my 12 files; ch17 Problem F passages consistent.
(h) 𝓔⁽¹⁾ and π⁸: NO occurrences anywhere in chapters/ (multiple grep patterns: \mathcal{E}^{1}, ^{\langle1\rangle}, π^8, π^{8} — zero hits). 𝓔-family collision recorded: 𝓔^{μν} Euler–Lagrange (ch02:236-237) vs 𝓔^A_{μI} (ch04:47,122) vs 𝓔_{μν}[h] linearized-Einstein operator (ch07, appH:2446-2450). No 𝓔⁽¹⁾/π⁸ notation to watch in current text.
(i) even-subalgebra/θ: no even-subalgebra closure statements in chapters; sole hit appH:2667 "orientation-even part of the mixed term" (scope qualifier in Problem B/F hypotheses). Report-only.

NOTATION:
- Z-family: eq:Z-sigma (ch17:246) resolves the ch08 forward reference; chain re-derived end-to-end: V=Nλv²σ², Z=2N−3/(4πG_effv²)=2N(1−3M_P²/(Nv²)), V''=2Nλv², m²=V''/Z, β=2M_P²/(Zv²)=M_P²/(Nv²−3M_P²) — all correct.
- ψ=8σ/v (eq:repairII-trace, ch17) consistent with ch05 ψ trace and ch10 unitary-gauge usage. √−g R=6(∂Ω)² up to total derivative re-derived ✓.
- β/β_K, β_ECG, β (functional-integrability in ch17 chain) — three β's, locally scoped; record.

CROSS-FILE FINDINGS:
1. MAJOR (mathematical error), ch14:243-253 eq:ratio: substituting the chapter's OWN stated circular-orbit inputs v²=G_eff M/d, Ω²=G_eff M/d³ into eq:Peters (230) and eq:Pent (238): P_GW=(32/5)G_eff⁴M³μ²/d⁵, P_ent=ημG_effM/d⁵ ⇒ P_ent/P_GW=(5/32)η/(G_eff³M²μ) exactly — the d-dependence cancels, k=0. The sentence "with a positive power of d that makes the ratio grow toward wide separations if η is held fixed" is FALSE for the stated assumptions; the following paragraph's caveat ("artefact of treating η as constant") presupposes a growth that the displayed assumptions do not produce. The prefactor η/(G_eff³M²μ) itself is correct (dimensionless in geometrized units). Required action: correct the prose/exponent or state that k=0 for Keplerian orbits (ratio constant in d; growth requires a different Ω(r)/v(r) input).
2. ch12:243-265 dimensional-incompleteness remark of eq:Leff ("RHS has mass dimension three... Problem G remains OPEN") is consistent with ch08 coefficient map; no contradiction.
3. ch17 status restatements vs Appendix H ledger convention (recorded, not judged): B "CRITICAL PATH; OPEN" (123), C (140), D (330) + D2 model note (344), A "OPEN; CRITICAL PATH for the matrix-derived label" (378), E (395), F (404), G "CRITICAL PATH; mechanism CLOSED CONDITIONALLY, derivation OPEN" (475), N "CRITICAL PATH for the matrix-derived label; OPEN" (498), H (521)/I (582)/J (597) OPTIONAL; completion criterion sec:ch17-done (700-732) lists A,B,C,D1,E,F,G-derived,N — matches the standing Chapter 17 snapshot; vocabulary OPEN / CLOSED CONDITIONALLY / DERIVED / PROGRAMME-CONDITIONAL used consistently. ch16:133 "frame existence is part of Problem D1" matches criterion. ch16 falsifier list is consistent with ch13 ν and ch14 η bounds except the ν≈1.1 item (see audit b) and inherits no ch14-ratio claim (ch16 does not repeat the growth statement).
4. ch16:325 G_toy=36 cross-refs ch15 — consistent.
5. Re-verified pre-compaction independent checks: ch03 Moyal −i/24 term ✓; ch03 toy R̃ and R[g_ρ] ✓; ch04 Schwinger–DeWitt expansion ✓; ch07 FP ghost block + divergence identity ✓; ch08 heat-kernel integrals term-by-term ✓; ch10 prop:B-torsion-free (traced 4τ_C=0; (⋆+γ⁻¹)(−⋆+γ⁻¹)=(1+γ⁻²)𝕀) ✓; prop:goldstone-count 6=6 ✓; ch02 Weyl trace ✓.

CITATIONS: bib entries exist in bib/ for McGaugh2016 (PRL 117, 201101), Cardy2013MI (JPA 46, 285402), Bertotti2003 (Nature 425, 374) — standard/real; DorauMuch2026 (PRL 136(9), 2026) future-dated — NOT independently verified. Cardy2013 attribution of p_*=2 in 3+1 dims is consistent with standard small-region CFT MI scaling (not externally re-derived).

Unreadable files: none. Full scan statement: all 12 assigned files read byte-complete; other chapters covered by the other four scan passes plus my targeted audit reads above.
