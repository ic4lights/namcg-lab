VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/1

## Verdict
F1–F7 are applied and the mathematics is unchanged and sound as a conditional result. The LaTeX block has one transcription defect that must be fixed before integration: a literal TAB character stands where `\tau` should begin, in the first occurrence of `\tau_\Omega`.

## Source reading
Digest plus targeted reads; no full scan. The digest is stale because the tree is dirty, which is expected. I read in full:
- `proposals/029-cone-log-coefficient/proposal-r2.md`
- `proposals/029-cone-log-coefficient/appH_insert.tex`
- `proposals/029-cone-log-coefficient/review-r1.md`, which I wrote in round 1
- the `flat_landau_ab.py` output
- the `sec:status-B` anchor region of `chapters/appH-microscopic-proofs.tex`

The round-1 derivation checks stand and I did not redo them. These were the Z_n decomposition, the Landau–Aharonov–Bohm constants, the 24πσ assembly, the self-dual example, and Eq. (70) and a = 11/360 of Solodukhin2011.

## Claim under review
Conditional structural result for Problem B (with A and F). It computes the A-side logarithmic coefficient at (N_s, n_D) = (6, 2) for the fixed-state replica. On the rotation-invariant self-dual example the result is σ_log = R_Σ/(12π), against the T-side zero of 026.

Appendix H label for B, verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-order identity is established, but the stationarity condition for the tensor block is not derived." Chapter 17 lists A, B, C, D1, E, F, G-derived and N as the critical set. No label change is proposed.

## Checks performed
I checked the r2 LaTeX block against the r1 findings by direct reading.

- **F1: applied.** The block now says:
  - the difference is "as coefficients, for the fixed-state replica on these backgrounds";
  - it is "not about G_eff";
  - the smooth replica gives zero on both sides;
  - the state selection is not derived;
  - contact and edge-mode terms "could cancel the difference".
- **F2: applied.** The block uses the convention-free spin term γ¹²Ω₁₂ of (γD)², with Ω₁₂ = [D₁,D₂]. The `-σ₃2πaδ` wording is gone from the block. τ_Ω is defined with the same Ω₁₂.
- **F3: applied.** The block uses τ_Ω and σ_log throughout. Neither clashes with the 024 `\mathcal T` or the 026 `\mathcal S_4`. The one exception is the defect below.
- **F4: applied.** R_ii, R_ijij and R_Σ are defined, with R_Σ = R − 2R_ii + R_ijij for totally geodesic Σ.
- **F5: applied.** The block cites "a = 11/360 … Equation (275) of Solodukhin2011, after Duff; not re-derived here" and lists it as an input in paragraph 2.
- **F6: applied.** The block has a single closer, "Problem B remains open and PROGRAMME-CONDITIONAL."
- **F7: applied.** I re-ran `flat_landau_ab.py`. The last line now prints −S₂ and matches `tot`, for N = 2..5 (−1/8, −2/9, −5/16, −2/5). The line states that the attractive-channel assignment is an input checked by hand.
- **Nothing else changed.** The 24πσ formula, the self-dual statements and the scope paragraph read as in r1. The only differences from r1 are the F1–F6 edits.
- **Anchor.** The substring "no logarithmic coefficient of the cone (area) side" occurs exactly once in `chapters/appH-microscopic-proofs.tex`. It ends the 026 paragraph, and `\section{Problem C…}` follows. The anchor is unique and correct.
- **Labels and citations.** The block adds no `\label` and no `\ref`. The `\cite` key `Solodukhin2011` already exists. No label is duplicated.
- **Emergence.** G, ρ and b are built from Θ, so spacetime stays emergent.

**The `appH_insert.tex` and `proposal-r2.md` LaTeX blocks match** apart from this defect, which is present in both.

## Findings

**1. Major (text-integrity, a one-character fix). Location: `appH_insert.tex` and the proposal-r2 LaTeX block, first occurrence of `\tau_\Omega`.**
- Finding: `grep` and `od -c` show a literal TAB (0x09) followed by `au_\Omega`. This is the text `\(<TAB>au_\Omega=\operatorname{tr}(\gamma^{12}…`. The `\t` of `\tau` was swallowed as a tab escape. The displayed formula and the sentence "so that … −τ_Ω" use the correct `\tau_\Omega`; only the defining occurrence is corrupted.
- Reason: if integrated, the definition would typeset as "a u_Ω" with no τ, or fail to build. τ_Ω would then be used in the displayed formula without being defined, and the definition of the load-bearing symbol would be wrong.
- Required action: replace the tab with a backslash, so the text reads `\(\tau_\Omega=\operatorname{tr}(\gamma^{12}\Omega^{f}_{12})\)`. After the fix, confirm that `grep -P '\t'` finds no tabs in the insert. The CRLF line endings must be preserved on integration, as `CLAUDE.md` requires. The working-tree `appH` currently has zero tab characters, so the corrected block must introduce none.

## Known caveat: stale symbols in the research text
The research text of r2 still uses the old symbols 𝒯 and 𝒮 and the old Dirac sign wording. The r2 changelog item F2 flags this explicitly. Only the LaTeX block enters the manuscript, and the changelog says that the research text keeps old names and that the intermediate Dirac sign was convention-dependent while the final formula −½S₂ tr(γ¹²Ω₁₂) is convention-free. This does not affect acceptance. The proposal body is the evidence record. I ask only that the final round-3 text carry the same changelog note.

## Scope of what is established
- **Established.** The Z_n flavour-vortex decomposition for the fixed-state replica. The flat-model constants, with Σ_k B₃(k/n) = 0. The Dirac Ω weight −½S₂ tr(γ¹²Ω₁₂). The symbolic assembly of 24πσ_log, given the two literature inputs.
- **Conditional.**
  - **Class:** the fixed-state replica with regular ρ and the less singular Dirac extension; antiperiodic gluing; totally geodesic Σ; one loop, α = 1, Yukawas dropped; one common proper-time limit; Eq. (70) and a = 11/360 taken as inputs.
  - **Identity not proved:** the claim (3/2)X′ − τ_Ω = 2R_Σ is checked at three points of one self-dual example and is not proved.
  - **Mismatch:** the resulting mismatch with the T-side zero is therefore conditional. It says nothing about G_eff or the matrix state.
- **Open avenues, ranked.** These are as in r1 and the proposal's own list.
  1. Edge-mode and contact terms (the Kabat vector contact, Dirac edge modes). This is the most likely site of cancellation.
  2. A Weitzenböck-type proof of the identity on self-dual backgrounds, and evaluation on the non-BPS family.
  3. The log analogue of the intermediate-flux replica, and the smooth replica's own log coefficient.
  4. An independent spindle-spectra check of the Dirac sign and geometric part.
  5. Relaxing the totally geodesic hypothesis.
  6. The rotated-gluing vector branch.
  7. The a₃ Kaluza–Klein route.
- Problem B stays OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL. There is no breakthrough and no label change.

## Recommended disposition
Fix the tab in `appH_insert.tex` and in the proposal block (Finding 1). The orchestrator may then integrate the corrected block as ordinal 27 without a further derivation round. Nothing needs re-deriving, since the fix is a transcription correction with no new physics. If the integrator verifies the repaired text by `grep -P '\t'` and a clean `build_check.py`, I regard this verdict as converted to ACCEPT for exactly the text below.

## Corrected snippet
Only this phrase changes. The rest of the block is accepted as it stands in `appH_insert.tex` and `proposal-r2.md`, and no extra assumption is needed.

Replace
`\(<TAB>au_\Omega=\operatorname{tr}(\gamma^{12}\Omega^{f}_{12})\)`
with
`\(\tau_\Omega=\operatorname{tr}(\gamma^{12}\Omega^{f}_{12})\)`

What would be accepted, once repaired and inserted after the 026 paragraph and before `\section{Problem C…}`:
- the `\paragraph{Cone logarithmic coefficient at …(conditional; not closure).}` paragraph;
- the following scope paragraph, ending "Problem~B remains open and PROGRAMME-CONDITIONAL."
