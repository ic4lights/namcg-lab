VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1

Source-reading basis (verbatim, as directed): "split scan: helper passes read all 30 chapters/**/*.tex files in full (passes 1-2 appH L1-2000/L2001-3939, pass 3 = 11 app* files, passes 4a/4b/4c = ch01-05/06-11/12-18; all returned clean: 0 dangling cross-refs centrally checked, 0 duplicate labels, byte-clean CRLF); this verdict pass = digest + targeted reads + scan reports." `python scripts/make_digest.py --check` printed `DIGEST CURRENT` in this session (head 23266972cd07..., dirty-chapters: no).

## Verdict
The manuscript payload's five claims are each independently re-derived and true, and the four reproduction batteries re-run byte-identically; however the proposal's own record contains one false "exactly" identity (I7) and the battery check that certifies it is tautological (both sides omit the same nonzero term), so the package returns for a record/battery correction even though the pinned payload text itself needs no change.

## Claim under review
Proposal 110, round 1: inside the posited locked sector (ass:frame-lock, eq:polar data with SO(3,1)-valued Λ, frame eq:vev-is-frame, dressed connection eq:dressed-omega), evaluate the item-109 bilocal composite eq:bilocal-frame-op: (1) coincidence value G(x,x) = (1+σ/v)²η_{IJ}e^I_μe^J_ν; (2) O(ℓ²) path coefficient = (area)·F, F = ∂_ρw_σ−∂_σw_ρ−[w_ρ,w_σ] in the printed transport ordering (ab/2 triangle, ab/6 parabola); (3) O(ℓ) symmetric sector connector-free, connector-quadratic soldering ½(1+σ/v)²sym(η{w_ρ,w_σ}) at ρ≠σ; (4) det identity, O(g⁺) right-action example, SO(η) non-invariance. Target: Problem C Missing-step input (i). `Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL.` (appH L532-536, quoted verbatim); ch17 L139-140 "CRITICAL PATH; OPEN" — both re-read and unchanged. Classification per rule 6: conditional in-hypothesis evaluations / derivation-grade inputs, NOT a closure; C, D, D1 stay OPEN. The proposal claims this correctly.

## Checks performed
- Pins: proposal sha1 a8a6efff... ✓, payload sha1 2cca5842... ✓ (compile cert at this sha stands; no recompile), all 8 script + 4 .out shas ✓.
- Battery re-runs (documented invocation, from the proposal folder):

| script(s) | recorded sha | my result | byte-identical to stored .out |
|---|---|---|---|
| check_path_curvature{,_part2,_part3} | 2145e16e/8aef4877/679a0ded | ALL PASS | yes (7da3445d) |
| check_locked_coincidence | c0f0bbda | ALL PASS | yes (9177127b) |
| check_right_isometry | 5496fbc6 | ALL PASS | yes (23281c81) |
| check_induced_expansion{,_part2,_part3} | c857d4f0/8950ff46/4035bdf7 | ALL PASS | yes (32b37018) |

- Independent re-derivations (fresh scratch `scratch/gk110_s1,s2,s2b,s3*.py`, not the researcher's code):
  - P1: solved dV/ds = (εM₀+sε²M₁)V by RK4 with generic noncommuting 3×3 data; V(1) − [I+εM₀+½ε²(M₁+M₀²)] scales ε³ (7.4e-5→7.2e-8) — left-multiplication transport reproduces eq:bilocal-frame-expansion exactly through O(ℓ²), ordering `w_ρw_σ` as printed ✓.
  - P2/parabola: corrected RK4 for L-path vs chord and parabola vs chord; the O(ε²) coefficient converges (dev ∝ ε: 0.604/0.246/0.062) to (ab/2)[(B₂₁−B₁₂)−[C₁,C₂]] with B_{ρμ}=∂_μw_ρ, i.e. F₁₂ = ∂₁w₂−∂₂w₁−[w₁,w₂] − the payload's −[w,w] sign in the printed ordering — and ab/6 for the parabola ✓. Right-ordered composition gives dw + [w,w] and the same coincidence series (hand check) — ordering-sensitivity statement correct.
  - R4: symbolic factorization (ΛE)^Tη(ΛE) − E^T(Λ^TηΛ)E = 0 for fully generic 4×4 Λ (so the drop holds for all Λ, not only the 2-parameter boost-rotation subfamily), plus exp(so(η)) 6-parameter instance (max dev 1e-14) and vacuum η at σ=0, e=I ✓. Normalization chains: Φ=(v+σ)Λe with G=v^{-2}Φ^TηΦ gives (1+σ/v)² E^TηE; script absorbs v^{-1} into Φ consistently.
  - R3: hand proof so(η) closure (X^Tη=−ηX ⇒ [X,Y]^Tη=−η[X,Y]) and (ηF)^T=−ηF ✓.
  - R5: det multiplicativity + reproduced script values (−1, −44100, 0; O=D⁻¹BD hand-verified entrywise, 9/8, 1/2 ✓); O(g⁺) right action on column index preserves G, SO(η) right action does not ✓ — 109 sentence correct as printed, do-not-edit instruction respected.
  - R6: **direct differentiation** of G=fηUE (product f·η·U·E with so(η) w, general e-profile and radial data) gives the mixed coefficient sym(∂₁∂₂G|₀) = [claimed I7 target] **plus** sym((1+a)(a₁ηe₂+a₂ηe₁)), which is generically nonzero (S1: claimed=False, claimed+extra=True). The connector-quadratic (w²) part is exactly ½(1+a)²sym(η{w₁,w₂}) and the O(ℓ) symmetric coefficient is connector-free — both payload claims hold; I2/I3/I5/I5b verified true; I6 follows from R3.
- Anchor contract (count-only python on live appH, sha 0d10fd46... not matching the digest prefix d37cbf70046a in the task text, but the file has 3939 lines and both anchors count 1): HEAD=1, TAIL=1, joined=1; insertion point is exactly between "…sign fixed by the transport convention). " and "The representation content is admissible…" at L732 ✓.
- Labels: `eq:bilocal-coinc-locked` 0 occurrences; all five `\eqref` labels exist exactly once (ch04:62,91,161; appH:712; ch10-lorentz-locking:133 — note the file is `ch10-lorentz-locking.tex`, the proposal's "ch10" is right); repo label count 597 ✓; insertion is LF-only (integrator converts to CRLF per its own note); signature, SO(3,1), no hard-coded chapter numbers, no process language, no status/priority wording ✓. Problem C status passages (appH L529-556, L754) read in full; unchanged by the package. ch17 L139-157 read in full; untouched. Dependency passages eq:VEV/ass:frame-lock/eq:Phi-transform (ch03 L248-289), eq:polar/eq:vev-is-frame (ch04), eq:g-from-e/ass:nondeg (ch04 L152-175), eq:dressed-omega (ch10 L125-140) read in full ✓.
- Not verified by me: the compile cert itself (accepted on the matching payload sha per instructions).

## Findings
1. **Major — proposal Result 3 / R6 (I7) and `check_induced_expansion.py` G2 + `check_induced_expansion_part3.py` tgt7.** The claimed identity "the symmetric part of the mixed coefficient ∂_ρ∂_σG|₀ (ρ≠σ) is exactly F_{ρσ}η + F₀sym(ηE_{ρσ}) + F₀sym(η(w_ρe_σ+w_σe_ρ)) + sym(F_ρηw_σ+F_σηw_ρ) + ½F₀sym(η{w_ρ,w_σ})" is **false for off-vacuum radial-gradient data (a_r=∂_rσ|₀≠0)**: the true coefficient contains in addition `sym((1+σ/v)(a_ρ η e_σ + a_σ η e_ρ))` (S1 ground truth). The battery's `G2` omits `Fd1[r]*eta*Ed1[s] + Fd1[s]*eta*Ed1[r]` from the product rule and tgt7 omits it too, so I7 "ALL PASS" certifies a tautology. The dropped term is linear in w, so the **payload text (what would be integrated) is unaffected** — it claims only the connector-quadratic part and the O(ℓ) statement, both true — and Decisions 2's phrase "sigma-gradient x w and e x w cross terms" already gestures at the incompleteness but omits this term. Required action: in the proposal text add the missing term to Result 3 / R6 (I7) (or restrict I7 to a_r=0 data and say so), add `+ Fd1[r]*eta*Ed1[s] + Fd1[s]*eta*Ed1[r]` to `G2` and `+ sym(Fd1[r]*eta*Ed1[s] + Fd1[s]*eta*Ed1[r])` to `tgt7`, re-run, and store the new outputs/shas. No payload change.
2. **Minor — proposal "Anchor contract"**: stated HEAD/TAIL byte lengths 43/81 do not match the actual strings (41/66 chars); occurrence counts are correct and verified 1/1/1. Fix the bookkeeping numbers (the integrator asserts counts, not lengths).
3. **Minor — proposal R2 body**: "where B_{mu nu} = d_mu w_nu(0)" has the indices swapped relative to the script's convention comment (`w_rho = C_rho + B_{rho mu} x^mu`, i.e. B_{ρμ}=∂_μw_ρ) under which "F_12 = B21−B12−[C1,C2]" is correct. The checks and payload are fine; fix the sentence.
4. **Minor — proposal Source reading** says the digest was STALE at researcher run start; in this review pass it is DIGEST CURRENT at head 23266972. No conflict; recorded for provenance.

## Scope of what is established
- Established (conditional-identity tier, derived under the explicitly posited locked-polar/locked-frame hypotheses with the posited dressed connection): the coincidence formula eq:bilocal-coinc-locked; the loop/area coefficient and its ordering-sensitivity (for any w with linearized data at the basepoint, general noncommuting); the η-antisymmetry of ηF and of ηw, η∂w; the connector-quadratic soldering coefficient ½(1+σ/v)²sym(η{w_ρ,w_σ}) at ρ≠σ; det identity, O(g⁺) right-action ambiguity example, SO(η) non-invariance. These hold as algebra within the hypotheses; none requires the I7 correction.
- False-as-written (must be corrected in the record before acceptance): the "exactly" full symmetric O(ℓ²) mixed-coefficient decomposition (Finding 1). Corrected form in "Corrected snippet".
- Open, unchanged: Problem C (operator, kinetic coefficient, mixing, couplings, pole mass, ass:gap-psi), D1 (connection specification), D (local Lorentz derivation), inputs (ii) G_eff (F) and (iii) constraint structure. Still OPEN: yes. DERIVED: only the scoped identities above; PROGRAMME-CONDITIONAL unchanged; nothing closed by scope (rule 3 respected by the package).
- Open avenues this package keeps alive: the w² soldering term gives a concrete O(ℓ²) metric-sector functional of w once D1 specifies it; the O(ℓ³) transport term and the second-variation/bilinear fluctuation of G named in "Remaining open step" remain the natural routes to an action/fluctuation operator for G (Missing-step (iii)).

## Recommended disposition
Revise (round 2): correct the proposal I7 text, fix the two battery lines, re-run the induced battery, fix the two bookkeeping numbers; keep the pinned payload byte-identical (its compile cert then still applies) and integrate the unchanged payload text. If the researcher prefers, restricting I7 to a_r=0 in the text and adding one caveat sentence is an equally valid minimal fix. Milestone assessment (routine) and status-label recommendation (none) are correct and I concur; MILESTONE.md trigger 3 does not fire (the error is internal to this proposal's record, not a merged claim; item 109's integrated sentences were each re-checked and stand).

## Corrected snippet
No physics needed. Record-level corrections only (payload untouched):
- Proposal I7/Result 3 identity becomes, with F_r = (1+σ/v)·∂_rσ|₀ and F₀ = (1+σ/v)²,
  sym(∂_ρ∂_σG|₀) = F_{ρσ}η + F₀ sym(ηE_{ρσ}) + F₀ sym(η(w_ρe_σ+w_σe_ρ)) + sym(F_ρηw_σ + F_σηw_ρ) + ½F₀ sym(η{w_ρ,w_σ}) + sym(F_ρηe_σ + F_σηe_ρ).
- `check_induced_expansion.py`, G2 dict: add `+ Fd1[r]*eta*Ed1[s] + Fd1[s]*eta*Ed1[r]`.
- `check_induced_expansion_part3.py`, tgt7: add `+ sp.simplify(sym(Fd1[r]*eta*Ed1[s] + Fd1[s]*eta*Ed1[r]))`.
(S1 confirms the corrected right-hand side equals the directly differentiated ground truth exactly, and the payload's narrower claims survive unchanged.)

Observations (non-blocking): (i) the L5/N=6 counter-scope example yields G₆ = diag(1,2,1,1), a positive-definite composite over a degenerate locked block — adequate for the stated square-frame bookkeeping; correctly kept out of the manuscript. (ii) The 109 sentence "only modulo the right action of the orthogonal group of g⁺" is true as L6 verifies; the usual internal-index (left) O(η)/local-Lorentz redundancy coexists with it — read "only" as "in addition to local Lorentz"; no edit recommended. (iii) L2 verifies the coset drop for a 2-parameter Λ family; my generic-Λ factorization closes that gap formally for all Λ with Λ^TηΛ=η.

END REVIEW 110 r1