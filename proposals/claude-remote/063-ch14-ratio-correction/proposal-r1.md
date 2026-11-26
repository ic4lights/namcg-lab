# Proposal 063-ch14-ratio-correction, round 1

## Result

The claim at `chapters/ch14-dissipation.tex` lines 243-258 is false under the chapter's own definitions. For the working law eq:Fdiss with constant eta (Assumption ass:drag) on a circular Newtonian orbit, P_ent = eta mu G M / d^5 and the Peters power is P_GW = (32/5) G^4 mu^2 M^3 / d^5. Their ratio is

    P_ent / P_GW = (5/32) eta / (G^3 M^2 mu),

which does not depend on d. So the exponent k in eq:ratio is 0, not positive. The ratio does not "grow toward wide separations". The follow-on sentences, which call that growth "an artefact of treating eta as constant" and say suppressing eta "at wide separations" would remove it, describe a growth that does not occur.

The exercise "Energy identity" (lines 363-368) asks for "a separation where the two powers could be comparable for a chosen eta". It inherits the error. Along a Peters inspiral, dU_N/dt = -2 P_GW, so P_ent/|dU_N/dt| = (5/64) eta/(G^3 M^2 mu). That ratio does not depend on d either. For fixed eta, the two powers are comparable at every separation or at none. The correct question asks for eta in terms of the masses, eta ~ (64/5) G^3 M^2 mu.

I checked every reading that could make the claim true. None does (see Research). This is a confirmed PRIOR-CLAIM-ERROR in optional Problem I phenomenology. The proposal corrects the two passages in ch14. No other chapter depends on the false claim. No status, priority or completion label changes.

## Target and status

- **Problem I** ("dynamical origin of the drag"). Appendix H sec:status-I: "Status: OPEN. Priority: OPTIONAL falsifiable phenomenological extension; prerequisite only if drag is claimed as derived or predicted. Completion: PROGRAMME-CONDITIONAL."
- Chapter 17 (ch17:581-594) agrees: "OPEN; OPTIONAL falsifiable phenomenological extension. It becomes critical only if the drag is claimed to be derived or predicted." Also ch17:745-747: "Problems H, I, and J may remain open in a completed derivation within the stated scopes ... Problem I is a prerequisite only if drag is claimed to be derived or predicted." I found no discrepancy between appH and ch17.
- **Original target of Problem I:** derive Gamma_ij(r; l_A, l_B) from microscopic dynamics and a stationary reference state. This package does not address it. It corrects a false phenomenological statement about the assumed working law.
- **Dependencies:** none on the critical path. The corrected passage uses only eq:Peters, eq:Pent, eq:Fdiss and ass:drag in ch14.
- **Classification of this package:** a correction of a merged claim (PRIOR-CLAIM-ERROR, M3 type). It is not a derivation of the target.

## Source reading

Digest + targeted reads.
- `python scripts/make_digest.py --check` printed **DIGEST STALE (head changed)**. HEAD moved with the SME-scout commit d8a07ad, which touches only `reports/`. I did not regenerate the digest, because that writes to `scratch/`, outside my folder. This does not affect the files used here.
- `chapters/ch14-dissipation.tex` was read in full (all 397 lines). It is clean against HEAD.
- Read in full: Problem I in appH (sec:status-I, lines 2929-3059), and ch17:575-600 and 740-752.
- Grepped all `chapters/*.tex` for: `eq:Pent`, `eq:ratio`, `P_{\mathrm{ent}}`, "wide separation", "grow ... toward", `Peters`, `quadrupole`, `chirp`. I listed the files containing "dissipat"/"drag". Then I read the passages that bear on the comparison: ch15:160-175 and 285-298, ch13:405-410, ch11:358-368, ch16:100-115, 210-300 and 335-348.
- Also read: `proposals/062-doubleton-fermion-kernel/scan-p5.md` item 4, `reports/sme-scout-20261108-after60.md` section 5, and the ledger entry at `reports/ledger.md:537`.
- No file was unreadable. This is not a full scan. None is required: the change edits one physics passage and one exercise, and no definition, assumption, scope statement or status passage. Integration ordinal 61 is not a 5th item.

## Research and reasoning

**Definitions used (ch14).**
- eq:Fdiss: F_diss = -eta mu v / d^4.
- ass:drag: "eta >= 0 constant on a given inspiral".
- eq:Pent: P_ent = -F_diss . v = eta mu v^2/d^4.
- eq:Peters: P_GW = (32/5) G mu^2 d^4 Omega^6 <inclination factors>, in quadrupole units (c=1).
- Line 243 states the circular Newtonian orbit: v^2 = GM/d, Omega^2 = GM/d^3.

**Computation.**
- P_ent = eta mu (GM/d)/d^4 = eta mu G M d^-5.
- P_GW = (32/5) G mu^2 d^4 (GM)^3 d^-9 = (32/5) G^4 mu^2 M^3 d^-5.
- Ratio = (5/32) eta/(G^3 M^2 mu). Its d-derivative is 0.
- Dimensions (c=1): [eta] = [F d^4/(mu v)] = L^4/T = L^3, and G M ~ G mu ~ L, so the ratio is dimensionless. The prefactor eta/(G^3 M^2 mu) of the old display was correct. Only the factor (d/GM)^k is wrong, since k = 0.
- For total radiated power, the angle-integrated "inclination factor" is 1. In any case it carries no d-dependence.

**General drag exponent.** For F = -eta mu v/d^n, P_ent ∝ d^-(n+1), so the ratio is ∝ d^(4-n). The ratio grows at wide separations only if n < 4. The undetermined exponent is "falsifiable" per ch14:196-202 and ch16:230-234, so this statement is useful. It also explains how the false sentence could arise: it holds for a drag exponent below 4, not for the stated d^-4 law. Git history gives no help here: the text was introduced in the initial commit 3e2322a.

**Readings checked that might make the claim true (none does).**
1. *eta depends on d or v.* eq:force-PN writes a general eta^mu(d, d-dot). But ass:drag, which defines the law compared in sec:ch14-quad, fixes eta constant on a given inspiral. The sentence itself says "if eta is held fixed". With constant eta, k = 0 exactly.
2. *Non-circular orbit.* The text says "For a circular Newtonian orbit". For eccentric orbits, both orbit-averaged powers get eccentricity factors, but the claim concerns the separation scaling of the circular case.
3. *Different P_GW.* eq:Peters is the quadrupole power as written, and it scales as d^4 Omega^6 ∝ d^-5.
4. *Laboratory distances / the "artefact" sentence.* This sentence explains away a growth that does not happen. It is not an independent reading.

So the negative-result branch ("no change") does not apply.

**Consequence derived for the corrected text (reduced model, leading order).**
- With total loss (1+R) P_GW and R constant, adiabatic circular evolution gives f-dot_GW = (1+R) (96/5) pi^(8/3) (G Mc)^(5/3) f^(11/3), where f = Omega/pi and Mc = mu^(3/5) M^(2/5). The script checks this symbolically against the energy balance with eq:Peters and Kepler.
- Hence the extra loss is the same as a chirp-mass rescaling Mc -> (1+R)^(3/5) Mc in the leading-order frequency evolution.
- I claim this only for the reduced Newtonian/quadrupole model, at leading order. I make no claim about amplitude, higher-order phasing or parameter estimation.

**Entropic-only decay rate (not inserted, recorded for the gatekeeper).** d-dot_ent = -2 eta/d^3, independent of the masses. Fixed eta therefore gives an entropic decay time d^4/(2 eta) that grows at wide separations. It is the comparison with P_GW, not the absolute rate, that is d-independent. This is why I keep the sentence "a sufficiently small eta is required for consistency with Solar-System tests". It is existing text, stays qualitative, and needs no number.

**Literature.**
- Peters-Mathews and the leading-order chirp relation are derived here from eq:Peters and Kepler. No citation is added.
- The SME scout points to the ppE framework (Yunes-Pretorius, arXiv:0909.3328) and to Will's Living Review (arXiv:1403.7377) for PN-order framing ("0PN-relative", "dipole-like ∝ d^-4"). I did not verify these and do not use them. The manuscript text contains no PN-order labels and no citation.

**Other passages checked, unchanged (they do not depend on the false claim).**
- ch14:270-275 (LIGO band: quadrupole remains the default; eta not constrained to be large).
- ch16:220-221 ("Expected if eta is negligible at those separations"). This reads as eta differing between regimes or systems, which ass:drag allows, since it constrains eta only "on a given inspiral". Not false.
- ch16:258 (inspiral-time deviation "only a bound on eta"). Still true. The degeneracy makes it, if anything, a weaker bound.
- ch16:289-290 and ch15:169, 292 (ch15 points to sec:ch14-quad for "the regime in which quadrupole losses dominate". That pointer stays valid: the corrected section says the comparison is set by eta and the masses).
- ch13:405-410, ch11:358-368.
- appH and ch17 Problem I entries contain no ratio claim.

## Claim classification

| Claim | Class |
|---|---|
| P_ent/P_GW = (5/32) eta/(G^3 M^2 mu), independent of d, for eq:Fdiss with constant eta and eq:Peters on circular Newtonian orbits | established derivation (within the stated reduced model) |
| Old statement "positive power of d ... grow toward wide separations" | false (PRIOR-CLAIM-ERROR) |
| For F ∝ v/d^n the ratio ∝ d^(4-n) | established derivation (same model) |
| dU_N/dt = -2 P_GW along a Peters inspiral; comparability at eta ~ (64/5) G^3 M^2 mu | established derivation (same model) |
| Leading-order f-dot multiplied by 1+R, equivalent to Mc -> (1+R)^(3/5) Mc | established derivation (reduced model, leading-order adiabatic circular evolution only) |
| eq:Fdiss itself, the value of eta, whether eta differs between regimes | phenomenological input / unresolved (Problem I) |
| "a sufficiently small eta is required for consistency with Solar-System tests" | existing qualitative statement, retained, not quantified |
| PN-order labels from the SME scout | not independently verified; not used |

## Proposed changes

One file: `chapters/ch14-dissipation.tex`. Full OLD/NEW strings, hashes and CRLF checks are in `edit-ch14-dissipation.md`. The authoritative strings are in `apply_check.py`.

- Baseline: 16520 bytes, sha256 `d6883ca33d0cebd7e78162cdc0b49e0faffac9ac07bd986119ca4a09a3872d36`, 397 CRLF, 0 bare LF/CR, no BOM, no trailing whitespace.
- Result: 17336 bytes, sha256 `b1fefa684669f0315e705061a9efd84c732eca741e687b9f3a88977f2f976dd2`, 411 CRLF, 0 bare LF/CR, no BOM, no trailing whitespace.

**Block 1** (sec:ch14-quad). Replaces lines 243-258, from "For a circular Newtonian orbit, \(v^2=\Geff M/d\) and" through "Solar-System tests." (OLD unique). The surrounding text is kept: eq:Peters, eq:Pent, and the following "The intended domain of~\eqref{eq:Fdiss} is:" list and LIGO paragraph.

```latex
For a circular Newtonian orbit, \(v^2=\Geff M/d\) and
\(\Omega^2=\Geff M/d^3\), so both powers fall as \(d^{-5}\) and
\begin{equation}
  \label{eq:ratio}
  \frac{P_{\mathrm{ent}}}{P_{\mathrm{GW}}}
  \;\sim\;
  \frac{5}{32}\,
  \frac{\eta}{\Geff^3 M^2\mu},
\end{equation}
up to the inclination factors in~\eqref{eq:Peters}. With \(\eta\)
constant on a given inspiral, as in Assumption~\ref{ass:drag}, this
ratio does not depend on \(d\): the working law singles out no
separation at which the entropic channel overtakes the quadrupole
channel, and the comparison is fixed by \(\eta\) and the masses.
Because both losses have the same dependence on \(d\), and hence on
the orbital frequency, the extra loss multiplies the leading-order
quadrupole frequency evolution by the constant factor
\(1+P_{\mathrm{ent}}/P_{\mathrm{GW}}\). At that order it is
degenerate with a rescaling of the chirp mass
\(\mathcal M=\mu^{3/5}M^{2/5}\) to
\((1+P_{\mathrm{ent}}/P_{\mathrm{GW}})^{3/5}\mathcal M\).
For a drag falling as \(d^{-n}\) the same computation gives a ratio
proportional to \(d^{4-n}\); a ratio that grows toward wide
separations would require \(n<4\), which
Assumption~\ref{ass:drag} does not adopt. This book does not
calculate whether \(\eta\) differs between regimes, and a
sufficiently small \(\eta\) is required for consistency with
Solar-System tests.
```

**Block 2** (sec:ch14-exercises, exercise 3 "Energy identity"). This edits an exercise. It replaces lines 367-368 (OLD unique). Lines 363-366 are kept.

```latex
    inspiral, show that their ratio does not depend on \(d\), and
    find the value of \(\eta\), in terms of the masses, at which the
    two powers are comparable. For which drag exponents would the
    ratio depend on separation?
```

**Labels and macros.**
- Labels verified: `eq:ratio` (1 occurrence, kept; no references to it in `chapters/`), `eq:Peters` (1), `ass:drag` (1). No new labels are added.
- Macros: `\Geff` is already used in this passage. `\mathcal M` is local, and the manuscript has no prior "chirp" usage, so there is no conflict.
- This changes no assumption, definition, scope statement or status passage. Assumption ass:drag is untouched.

**Stale passages elsewhere:** none. See the list in Research.

## Verification scripts

- `verify_ratio.py` -> `verify_ratio_output.txt` (sympy) checks:
  - the circular-orbit P_GW and P_ent, and that their ratio is (5/32) eta/(G^3 M^2 mu) with zero d-derivative;
  - the general exponent d^(4-n);
  - dU_N/dt = -2 P_GW, and the eta values at which the powers are comparable;
  - d-dot_ent = -2 eta/d^3;
  - that f-dot equals (1+R) times the leading-order chirp formula with Mc = mu^(3/5) M^(2/5);
  - a dimension bookkeeping line, written by hand.
- `apply_check.py <repo_root> [out]` -> `apply_check_output.txt` checks:
  - uniqueness of each OLD string, and each NEW string's count before and after;
  - baseline and result bytes and sha256;
  - CRLF, bare LF/CR, BOM and trailing whitespace;
  - label counts.

  It writes the result only to the optional output path; it never writes into the repository.
- Scratch build: a repo copy in the scratchpad (`build063a`, without `.git`, `proposals`, `reports`), with the edited ch14, built with two `pdflatex -interaction=nonstopmode -halt-on-error namcg-book7.tex` passes. The result is in `build_output.txt`.

## Decisions Taken

- **Correct rather than reinterpret.** The alternative reading, eta depending on d, would contradict ass:drag ("constant on a given inspiral"). I rejected it.
- **Keep the label eq:ratio and the prefactor, and give its factor 5/32.** This is the smallest change. Dropping the display would remove a correct, useful result.
- **Add the d^(4-n) sentence.** The exponent is explicitly undetermined and falsifiable (ch14:196-202, ch16:230-234). The sentence states exactly when the old claim would hold, so it is not lost information.
- **Add the leading-order chirp-mass degeneracy.** It is derived in the reduced model, it replaces the removed (false) observational distinction, and it bears on ch16's "only a bound on eta". I did not add PN-order labels or citations, because those are not independently verified. Alternative rejected: omit it. That would leave the corrected section silent on what d-independence implies.
- **Leave ch16:220-221 unchanged.** "at those separations" is compatible with eta differing between systems, which ass:drag permits.
- **Retain the Solar-System sentence.** It is still true (the entropic decay time d^4/(2 eta) bounds eta), and it is existing qualitative text.

## Milestone assessment

M3-type correction of a merged claim (PRIOR-CLAIM-ERROR), confirmed, in optional Problem I phenomenology. It is not a breakthrough and does not touch the critical path. Otherwise routine.

## Status-label recommendation

- Current critical-path set (ch17 criterion and appH): A, B, C, D1, E, F, G-derived, N. H, I and J are optional.
- Affected labels: none. Problem I stays OPEN / OPTIONAL / PROGRAMME-CONDITIONAL.

## Author decision needed

none

## Remaining open step

Problem I's original target is untouched: a microscopic calculation of chi^R_ij and Gamma_ij(r; l_A, l_B), including the longitudinal and transverse components, the exponent and the coefficient. Only that calculation can decide whether n = 4. If n = 4 holds, the drag is a separation-independent fraction of the quadrupole loss and, at leading order, degenerate with the chirp mass. If n < 4, the drag grows relative to the quadrupole loss at wide separations.

## Special instructions for the gatekeeper

- Re-derive k = 0 from eq:Pent and eq:Peters with the circular-orbit relations at ch14:243-244.
- Check that ass:drag fixes eta constant on a given inspiral. That is the hypothesis behind d-independence.
- The chirp-mass sentence is claimed only for the leading-order frequency evolution of the reduced model. It must not be read as a parameter-estimation or waveform statement.
- No PN-order labels or literature claims are introduced.
- Confirm that no other chapter depends on the removed growth claim (my list is in Research).
- Re-run `python verify_ratio.py` and `python apply_check.py <repo_root>`. The baseline sha256 must match `d6883ca3...2d36` before integration.
- No status labels change.
