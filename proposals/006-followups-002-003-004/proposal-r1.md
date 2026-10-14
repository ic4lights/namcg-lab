# Proposal 006-followups-002-003-004, round 1

## Result

A bookkeeping package of three separable follow-ups to accepted proposals 002, 003 and 004. It derives nothing new for any critical-path target and changes no status, priority or completion label.

- **A (routine).** Sign correction in `appK-endomorphism.tex` so that the displayed `a_1` agrees with `eq:appA-a1`; optional A2 wording fix ("linear" to "quadratic").
- **B (author-approved).** A pure notation gloss identifying the `alpha` in Problem N's target with the Weyl-squared coupling of `eq:stelle`.
- **C (author-approved).** `ass:emergent-op` entered in the ch16 inventory as load-bearing, with the premise sentence and the rewritten chain item 6.

Why bundled: all three are reviewed follow-ups of accepted 002/003/004 (003 review-r2 finding 5 and 004 recommendations-r2 Q1/Q2), each already checked by a gatekeeper in an earlier review, and each is a text-only edit of at most a few lines. Each is separable: A, B and C touch disjoint passages and none depends on another. The integrator may apply any subset.

## Target and status

No problem is targeted for closure. Statuses (read in `chapters/appH-microscopic-proofs.tex`, `sec:status-N` L2015-2019, and ch17): N is OPEN / CRITICAL PATH for the matrix-derived label / PROGRAMME-CONDITIONAL. F is likewise OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. The critical-path set per ch17 `sec:ch17-done` is A, B, C, D1, E, F, G-derived, N; H, I, J optional. No discrepancy found between ch17 and Appendix H for N and F. Items B and C touch ch17 or ch16, which bear on the completion criterion, hence the author approval below.

**Author approval (recorded).** On 2026-10-14 the orchestrator relayed that the author was told items B and C need author approval, and the author replied: "proceed with worth integrating items". This is recorded as explicit author approval for items B and C as scoped here (B a notation gloss only; C the ch16 inventory row, premise sentence and chain-item-6 rewrite, with no label change). It is not approval of any label, priority, status or scope change, and none is made.

## Source reading

Digest + targeted reads (digest status DIGEST CURRENT, chapters-hash 196b7f142fde8bc9, as stated by the orchestrator; not a full scan). Read in full: `proposals/004-author-questions/recommendations-r2.md`; `proposals/003-auto-target/proposal-r2.md` Item 7 and `review-r2.md` finding 5; `appK-endomorphism.tex`; ch16 L20-170; ch17 L440-515, L648-660, L715-735; appH `sec:status-N` L2014-2139 and `sec:status-F` L1630-1648; ch08 L180-200; ch09 `eq:W4`, `eq:stelle` neighbourhood; appA `eq:appA-O`, `eq:appA-a1`, `eq:appA-a2`. I did not re-read the 004 `review-r1.md` (its corrected gloss is carried in recommendations-r2 Q2, which states it).

## Research and reasoning

### A. appK sign
- `eq:appA-O`: `O = -g^{mu nu} D_mu D_nu + E`. `eq:appA-a1`: `a_1 = tr_V(R/6 - E)`. appK L14-18 uses the same operator form `Delta = -D^mu D_mu + E` and writes `a_1 = tr(E) - (1/6) R dim`, the exact negative. Established by direct comparison.
- The conclusion `delta a_1 = 0` uses only `tr S^{ab} = 0` and is sign independent. No other file references appK's labels `sec:a1-null`, `sec:a2` (grep).
- **A2.** appK L38-39 says "The first non-vanishing correction linear in the laboratory field appears in `a_2` and is proportional to `F F`", under the section title "Quadratic appearance in `a_2`". `eq:appA-a2` contains `(1/2) tr E^2 - (1/6) R tr E`. With `E = E_0 + xi F_{ab} S^{ab}` the terms linear in F are `xi F_{ab} tr(S^{ab} E_0)` (from `E^2`, cross term) and `-(1/6) R xi F_{ab} tr S^{ab}`. The second vanishes by `tr S = 0`. The first is not shown to vanish by `tr S = 0` alone: it vanishes if `tr(S^{ab} E_0) = 0`, which depends on E_0 and is not established in the manuscript. So the precise statement is: the quantity proportional to `F_{mu nu}F^{mu nu}` is quadratic in F, and appK's text already claims only that this is the first non-vanishing term proportional to `F F`. To keep A2 accurate, the replacement states quadratic dependence and does not assert that no linear term exists beyond the `tr S = 0` cases. (This corrects the shorthand in recommendations-r2 Q1b, which attributed the vanishing of the whole linear term to `tr S = 0` alone.) The `a_2` statement itself is the manuscript's and is not recomputed. Status of A2: wording correction of non-load-bearing text, established as a comparison.

### B. alpha gloss
- Facts (re-grepped): `eq:stelle` (ch09) has `-(alpha/2) C^2`; `eq:W4` (ch09) has `+c_W C^2`; hence `c_W = -alpha/2` (established algebra) conditional on the continuation convention. appH `sec:status-N` (integrated from proposal 002) states "with `S_E=-iS_L` as in Appendix `app:seeley-dewitt`, and with curvature invariants continued without change of sign (an added convention)" and "`alpha = -2c_W` and `beta = 2c_R` in `eq:stelle`". So the label `sec:status-N` now contains the convention, resolving the caveat in recommendations-r2 Q2.
- Other uses of `alpha` in the book (ECG coupling, Fierz-Pauli parameter, `nu_exp`, a per-galaxy fit parameter) are listed in recommendations-r2 Q2; I re-grepped ch17 and found `alpha` at L506, L572, L626, L655, L727; L572 and L626 are the fit parameter (galactic), which is the ambiguity the gloss disambiguates.
- **Placement.** The defining statement of N's target is ch17 L497-513 (the `\paragraph{Problem N}`), with the same wording repeated in appH L2030-2033 (Missing step). L655 and L727 are restatements ("using the alpha and G_eff of Problem F"; "computed in Problem F") that refer back to the same symbol. Minimal placement: gloss once at ch17 L506 and once at appH L2032, where the symbol is first introduced in each file's N entry; leave L655 and L727 untouched (a gloss at L727 would be a second edit inside the completion criterion without adding information; if the author wants it, the same parenthesis applies verbatim). Both glosses are parentheticals inserted after "Problem~F"; the sentence otherwise unchanged. They add no requirement: they say which symbol the target already names.
- Scope check: the gloss does not replace `alpha` by `Upsilon`, does not restate N in `c_W, c_R` (that would add the spin-0 pole), and adds no hypothesis. N's target, status, priority and classification are unchanged.

### C. ch16 inventory, premise sentence, chain item 6
- Facts: `ass:emergent-op` is defined exactly once (ch08 L288, integrated with 003). The ch16 inventory table L81-106 does not list it. The ch16 sentence L127-130 lists "targets of critical-path Problems A, E and N" for `ass:dictionary`, `ass:lorentzian`, `ass:EFT-a2` and says "frame existence is part of Problem D1". Chain item 6 (ch16 L43-46) refers to `thm:Geff` without the operator premise; `thm:Geff` itself (ch08 L186-) begins "For specified gauge-fixed operators", and `ass:emergent-op` is what the manuscript (appH L1636-1644) records as the ingredient that must be assumed or discharged by Problem F.
- The inserted sentence does not add F to "Problems A, E and N" (that sentence concerns targets of three specific assumptions); a separate sentence states the new premise, which leaves the existing list intact.
- Effect on the completion criterion: ch17 defines the Completed-derivation label (L91-96, as quoted in 003 review-r2 finding 5) as one where no load-bearing assumption of ch16 remains assumed in the chain. A new load-bearing row therefore enlarges that class by one by cross-reference. This is the author-approved effect. F's own target ("computed from the specified operators; G_eff is not an input", ch17 L718-719) already requires the operator to be specified, and `ass:emergent-op` says what that specification must be on the emergent metric. No label changes.
- **Optional ch17 F missing-step sentence: omitted.** The ch17 F Missing step (L457-471) already says the Hessian is "an input to, not a specification of, these operators", and appH `sec:status-F` (L1636-1644) records that F includes discharging `ass:emergent-op`. A further ch17 sentence would add no information and would be an extra edit of the completion criterion; the draft from 003 proposal-r2 ("Stale passages elsewhere") is therefore not carried forward.

Literature: none used, none cited. The Barvinsky citation (004 Q3) is excluded as instructed (it needs a `bib/` edit and stays with the author).

## Claim classification

- A: `appK` sign now differs from `eq:appA-a1`: established (comparison). Corrected formula: established identity.
- A2: statement that `F F` dependence is quadratic: established; absence of other linear terms: not claimed (see reasoning).
- B: `c_W = -alpha/2`: established algebra, conditional on the added continuation convention; gloss is notation only.
- C: `ass:emergent-op` is an input assumption (not derived); classifying it load-bearing: author-approved classification; Theorem `thm:Geff` is conditional on it.
- No claim in this package is a derivation for a critical-path problem.

## Proposed changes

All `.tex` files use CRLF; the integrator normalises. All `\ref` labels below exist exactly once (checked by `verify_anchors_labels.py`): `eq:appA-a1`, `eq:stelle`, `eq:W4`, `ch:ultraviolet` (not used in the final snippets), `sec:status-N`, `app:seeley-dewitt`, `thm:Geff`, `ass:emergent-op`, `ass:laplace`. No new labels are introduced.

### A. `chapters/appK-endomorphism.tex`

Anchor (occurs once, L14-18): "On a Laplace-type operator \(\Delta=-D^\mu D_\mu+E\) the first Seeley--DeWitt coefficient is" followed by the `equation` with `a_1=\operatorname{tr}(E)-\frac16 R\,\dim.` Replace the lead-in's final words and the displayed line; the rest of the section is kept.

```latex
On a Laplace-type operator \(\Delta=-D^\mu D_\mu+E\) the first
Seeley--DeWitt coefficient, in the convention of~\eqref{eq:appA-a1}, is
\begin{equation}
  a_1=\operatorname{tr}\Bigl(\tfrac16 R-E\Bigr)
     =\tfrac16 R\,\dim-\operatorname{tr}(E).
\end{equation}
```

A2 (optional, include with A). Anchor (once, L38-39): "The first non-vanishing correction linear in the laboratory field appears in \(a_2\) and is proportional to \(F_{\mu\nu}F^{\mu\nu}\)." Replace this sentence only; the following sentences ("Variation of the resulting effective action ...") are kept.

```latex
The first non-vanishing correction proportional to
\(F_{\mu\nu}F^{\mu\nu}\) appears in \(a_2\) and is quadratic in the
laboratory field.
```

### B. Problem N target gloss

(i) `chapters/ch17-agenda.tex`, `\paragraph{Problem N}` (L503-507). Anchor (once): "function has no propagating Ostrogradsky ghost for \(p<\LUV\), for the values of \(\alpha\) and \(G_{\mathrm{eff}}\) computed in Problem~F, with the region of those values in which it holds stated. The target is no stronger". Replace "computed in Problem~F, with the region" by the following; everything else is kept.

```latex
computed in Problem~F (here \(\alpha\) is the Weyl-squared coupling
of~\eqref{eq:stelle}, whose \(C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}\)
coefficient is \(-\alpha/2\); with the continuation convention of
Section~\ref{sec:status-N}, \(c_W=-\alpha/2\) in~\eqref{eq:W4}; it is
not any other coupling denoted \(\alpha\) in this book), with the region
```

(ii) `chapters/appH-microscopic-proofs.tex`, `\paragraph{Missing step}` of `sec:status-N` (L2030-2033). Anchor (once): "function has no propagating Ostrogradsky ghost for \(p<\LUV\), for the values of \(\alpha\) and \(G_{\mathrm{eff}}\) computed in Problem~F, with the region of those values in which it holds stated. This is the requirement". Same replacement of "computed in Problem~F, with the region", with the clause "with the continuation convention of Section~\ref{sec:status-N}" changed to "with the continuation convention stated below" (the paragraph is inside `sec:status-N`):

```latex
computed in Problem~F (here \(\alpha\) is the Weyl-squared coupling
of~\eqref{eq:stelle}, whose \(C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}\)
coefficient is \(-\alpha/2\); with the continuation convention stated
below, \(c_W=-\alpha/2\) in~\eqref{eq:W4}; it is not any other coupling
denoted \(\alpha\) in this book), with the region
```

Not edited: ch17 L655 and L727 (restatements; the symbol is fixed by L506). No change to the scope, status, priority or completion classification of N. Stale-text check: the gloss adds no sentence that contradicts ch09 L128-130 or the `sec:status-N` formulas.

### C. `chapters/ch16-falsifiers.tex`

(a) Inventory row. Anchor (once): `\ref{ass:laplace} & setup & infrared operator is Laplace type \\`. Insert after it (rows kept in place):

```latex
\ref{ass:emergent-op} & load-bearing & fluctuations propagate on the
  emergent metric \\
```

(b) Premise sentence. Anchor (once): "and frame existence is part of Problem~D1. An assumption may remain in a scope-limited model, but that does not derive or close the corresponding problem." Insert after "Problem~D1." and before "An assumption may remain":

```latex
Assumption~\ref{ass:emergent-op} is a premise of
Theorem~\ref{thm:Geff} that Problem~F must discharge.
```

(c) Chain item 6. Anchor (once, L43-46): "The Euclidean curvature coefficient obeys the conditional, truncated heat-kernel identity of Theorem~\ref{thm:Geff}; physical matching requires specified operators, weights, thresholds, continuation, and scheme (Problem~F)." Replace with (enumerate indentation to be matched by the integrator):

```latex
The Euclidean curvature coefficient obeys the conditional,
        truncated heat-kernel identity of Theorem~\ref{thm:Geff} for
        operators built on the emergent metric
        (Assumption~\ref{ass:emergent-op}); physical matching requires
        specified operators, weights, thresholds, continuation, and
        scheme (Problem~F).
```

Stale passages elsewhere (not edited): the ch08 "What has been computed" status-table cell for `thm:Geff` ("conditional on specified sectors and scheme") could add "and on Assumption ass:emergent-op"; ch04 L270-272 and ch01 L59-60 optional qualifiers; ch17 F missing step (omitted, see above). I did not re-verify these locations this round.

## Verification scripts

`proposals/006-followups-002-003-004/verify_anchors_labels.py`, output `verify_anchors_labels.out.txt`: whitespace/CRLF-normalised check that each quoted anchor occurs exactly once in `chapters/` (all eight report 1) and that the labels `eq:appA-a1`, `eq:stelle`, `eq:W4`, `ch:ultraviolet`, `sec:status-N`, `app:seeley-dewitt`, `thm:Geff`, `ass:emergent-op`, `ass:laplace` are each defined once. Nothing computed; no build run (no scratch build was made).

## Decisions Taken

1. Gloss placed at ch17 L506 and appH L2032 only, not L655/L727: smallest text that fixes the symbol at its defining statements; rejected: glossing all four occurrences (extra edits of the completion criterion without new information), replacing alpha by Upsilon (narrows the target), restating in `c_W, c_R` (adds the spin-0 pole).
2. Optional ch17 F sentence omitted: the F target and appH `sec:status-F` already carry the requirement; the sentence would be an extra edit of the completion criterion.
3. A2 included in a corrected form (quadratic wording only), because the 004 shorthand ("linear term vanishes by tr S = 0") is not established for the `tr(S E_0)` cross term.
4. Barvinsky citation excluded per instruction.

## Milestone assessment

Routine (bookkeeping, sign/wording corrections, notation gloss). Trigger 3 considered: the appK sign error is in non-load-bearing text ("sign corrections to non-load-bearing text" is listed as non-milestone). Trigger 4 not triggered: no status, priority or classification change; C enlarges the load-bearing inventory by one assumption with explicit author approval, no problem label changes.

## Status-label recommendation

None. N, F and all other critical-path problems stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL (critical-path set from ch17 `sec:ch17-done`: A, B, C, D1, E, F, G-derived, N).

## Author decision needed

None beyond the approval recorded above for B and C.

## Remaining open step

Nothing here advances N or F. N still requires the matrix-path-integral derivation of the absence of an Ostrogradsky ghost for `p < Lambda_UV` at the `alpha`, `G_eff` computed in F; F still requires the specified operators and discharge of `ass:emergent-op`.

## Special instructions for the gatekeeper

- Verify the sign of A against `eq:appA-O`/`eq:appA-a1`, and my narrowing of A2 (is `tr(S^{ab}E_0)` established to vanish anywhere? I claim not, so only quadratic wording is used).
- Confirm B is a pure gloss: no new requirement, no scope change; check `sec:status-N` really contains the convention clause quoted and `alpha = -2c_W`.
- Confirm C does not edit ch17, adds only the approved row/sentence/rewrite, and that "load-bearing" classification is within the recorded approval.
- The approval quote is the orchestrator's relay; it covers B and C only.
- Do not accept any claim that these edits close or advance N or F.
