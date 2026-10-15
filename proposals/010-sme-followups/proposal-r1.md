# Proposal 010-sme-followups, round 1

## Result
Three small follow-ups from the SME review (reports/sme-auto-20261014-1520-20261014-2054.md).
- A: a one-clause wording change in ch09, so the sign statement names its dependence on the added curvature-continuation convention at the point of use.
- B: appK's conclusion "confined to the conformal mode; no transverse-traceless response" does not use the word "linear". But it is not protected against the term that the 006 correction left open (an F-linear term proportional to tr(S E_0)). Its stated reason ("proportional to g_{mu nu}") is also asserted without derivation. Minimal scoping text (two sentences) is proposed. Nothing else in appK relies on the superseded claim.
- C: no summary of the 003 Lemma 2 / scaffold no-go or of the 008 obstruction exists in ch01, ch16 or ch17 that omits hypotheses. No edit proposed.
No label, status or priority is touched. There is no new mathematics, no new number and no citation.

## Target and status
Bookkeeping and scoping follow-ups. Problems touched: N (item A; Appendix H sec:status-N, critical path, OPEN) and the appK laboratory-field heat-kernel note (not a critical-path problem; its Status section says it does not alter the ledger). Statuses are as in Appendix H and Chapter 17 and are unchanged. Discrepancies found: none. The text is PROGRAMME-CONDITIONAL scoping only; nothing is derived or closed.

## Source reading
Digest + targeted reads (digest CURRENT, chapters-hash e8f8d69487f4f2db). Read: ch09 L113-131; appH sec:status-N L2191-2230 (Missing step and the continuation-convention paragraph); appK-endomorphism.tex in full; ch16 L40-50, L83-106, L130-140; grep of ch01/ch16/ch17 for scaffold, no-go, obstruction, Poisson, emergent-op, Lemma; the SME report; the 002 and 006 reviews. This is not a full scan.

## Research and reasoning
A. The ch09 sentence (L129-131) says Section sec:status-N "records that a truncated induced Weyl term has this sign when G_eff and the weighted Weyl trace are positive". In appH (L2209-2211 and the paragraph from L2227) the identification c_W = -alpha/2 is stated "with the continuation convention", and the curvature invariants are "continued without change of sign (an added convention)". So the sign statement is conditional on that convention. I use the 002 gatekeeper's optional wording and add the name of the convention.

B. Structure of appK:
- sec:a1-null: delta a_1 = 0 from tr S = 0. Correct, with a_1 = tr(R/6 - E).
- sec:a2: the first F F term is quadratic; then the conformal-mode conclusion.
- sec:constraints: Cassini and EP bounds on a hand-introduced mixing of psi with a laboratory scalar. These are independent of a_2.
- sec:not-shown and sec:appK-status: the Status speaks only of the a_1 linear coupling and of the constraints on residual mixing.
- The labels app:heat_kernel_mixing, sec:a1-null, sec:a2, sec:constraints, sec:not-shown and sec:appK-status are not cited from any other chapter (grep over chapters/*.tex), so no cross-file consequence.

Within appK the only conclusion drawn from the a_2 discussion is the conformal-mode confinement. By eq:appA-a2 the F-linear part of a_2 is xi F_ab tr(S^ab E_0). The -(1/6) R tr E part vanishes by tr S = 0. The tr(S E_0) term is not excluded by anything in the manuscript (006 review-r1, A2). Its metric variation, if non-zero, has no reason to be proportional to g_{mu nu}. So the confinement conclusion is valid at most for the quadratic term alone, and the text should say so.

The sentence "variation ... produces a contribution proportional to g_{mu nu}" is also given without derivation for the quadratic term. A quantity quadratic in a field strength generally has a Maxwell-type metric variation, F_{ma}F_n^a - (1/4) g F^2, whose traceless part is non-zero. Whether tr(S S) F F gives a pure-trace variation depends on how the indices of F_{alpha beta} are tied to the metric, and appK does not specify this. I do not claim the sentence is false; I claim it is asserted, not shown. The proposed text marks it as such instead of removing it.

The Status section says only that "the linear coupling of a laboratory field strength to a_1 vanishes for antisymmetric generators". That is still accurate as worded, since it concerns a_1 only. No edit.

C. Search results:
- ch01: no scaffold lemma, no-go, Poisson or four-matrix text.
- ch16: ass:emergent-op appears in the claims list (L43-47), the inventory row (L94) and L134-135 ("a premise of Theorem Geff that Problem F must discharge"). These state the assumption, not Lemma 2 or the 008 result, so no hypothesis is omitted. The inventory row for ass:aux-metric ("g^(0) is a scaffold") is likewise a label, not a no-go summary.
- ch17: no occurrence of scaffold, no-go, four-matrix, Poisson or emergent-op. "Lemma" hits are the unrelated lem:msigma and lem:psi-sigma.
So there is nothing to scope. If a future ch01 or ch17 summary is added, it must carry the hypothesis list of the 003 and 008 statements.

## Claim classification
- A wording: conditional on the added convention (established as recorded in appH sec:status-N).
- B: delta a_1 = 0 is an established algebraic fact. The F-linear tr(S E_0) term not being excluded is an established gap (006). Conformal-only confinement is unresolved/unshown, conditional on stated assumptions.
- C: negative search result (established by grep).

## Proposed changes

### 1. chapters/ch09-ultraviolet.tex (item A)
Anchor (occurs once; spans L129-131): "the graviton; Section~\ref{sec:status-N} records that a truncated / induced Weyl term has this sign when \(G_{\mathrm{eff}}\) and the / weighted Weyl trace are positive." Verified: "induced Weyl term has this sign" occurs once in chapters/; `\label{sec:status-N}` exists once (appH L2191). Replace only those lines (the end of the paragraph); everything before stays.

```latex
the graviton; Section~\ref{sec:status-N} records that a truncated
induced Weyl term has this sign, under the curvature-continuation
convention stated there, when \(G_{\mathrm{eff}}\) and the
weighted Weyl trace are positive.
```

### 2. chapters/appK-endomorphism.tex (item B)
Anchor (occurs once; spans L43-45; the sentence breaks across lines at "The / coupling"): "The coupling is therefore confined to the conformal mode. No transverse-traceless response is generated at this order." Keep the preceding sentences ("The first non-vanishing correction ... quadratic in the laboratory field. Variation of the resulting effective action with respect to the metric produces a contribution proportional to \(g_{\mu\nu}\)."). Replace the two anchor sentences with:

```latex
For the quadratic term, if its metric variation has this form, the
coupling is confined to the conformal mode and generates no
transverse-traceless response. This statement does not cover a term
linear in \(F_{\alpha\beta}\) proportional to
\(\operatorname{tr}(S^{\alpha\beta}E_0)\), which is not excluded by
\(\operatorname{tr}S^{\alpha\beta}=0\) alone, and the proportionality to
\(g_{\mu\nu}\) is not derived here.
```
No label or \ref is added. The Status section is unchanged.

### 3. ch01, ch16, ch17 (item C)
No change.

## Verification scripts
None; there is no new algebra. Checks done by grep: the ch09 phrase occurs once; sec:status-N is defined once (appH); the appK sentence occurs once; the appK labels are not referenced elsewhere.

## Decisions Taken
- A: used the 002 gatekeeper's wording, extended with the name of the convention. It is the shortest wording that names the dependence and does not repeat the convention in ch09.
- B: scope rather than delete, since the conclusion may well hold for the quadratic term. The 006 gatekeeper's optional clause is used, plus a "not derived" caveat on the g_{mu nu} proportionality. Rejected: deleting the conformal-mode conclusion (loses a possibly correct statement); no edit (leaves an unprotected conclusion).
- C: no edit, because no offending summary exists. Rejected: adding a preventive caveat to ch01 (nothing to scope).

## Milestone assessment
Routine.

## Status-label recommendation
None. The critical-path set (A, B, C, D1, E, F, G-derived, N) and all labels are unchanged.

## Author decision needed
None.

## Remaining open step
For appK: derive the metric variation of the quadratic a_2 term for the actual index structure of F_{alpha beta} S^{alpha beta} on the locked block, and evaluate tr(S^{alpha beta} E_0) there (part of Problem F's heat-kernel evaluation). For N: the added continuation convention remains an input; Problem N is otherwise unaffected.

## Special instructions for the gatekeeper
Check that the ch09 edit only adds the clause and yields no stronger sign claim. Check that the appK replacement does not assert the conformal-only conclusion unconditionally and does not claim the linear term is non-zero (only that it is not excluded). Item C is a negative search; re-run the grep over ch01/ch16/ch17 if desired.
