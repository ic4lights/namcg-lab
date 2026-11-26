# Proposal 012-dorau-much-positioning, round 1

## Result
A literature-positioning insertion, no new mathematics. Dorau and Much (PRL 136, 091602; arXiv:2510.24491) is cited as a rigorous operator-algebraic form of the matter side of Claim 1 (Jacobson-type step): for a free real scalar field, vacuum versus coherent excitations, on a bifurcate Killing horizon, the Araki relative entropy equals the null energy flux. The text states that the paper assumes the metric, local Minkowski, the Raychaudhuri equation and S = A/4, so it does not support Claim 2 and does not derive the emergent-metric area term (Problems A and B). Bibliographic record verified (below). No labels change.

## Target and status
Not a Problem-level target; a positioning/citation package bearing on Problems A and B (both OPEN, CRITICAL PATH per the current ledger and Chapter 17 criterion; re-read `chapters/appH-microscopic-proofs.tex` sections `sec:status-A`, `sec:status-B`). Classification of this package: literature citation, PROGRAMME-CONDITIONAL context only; it closes nothing and changes no status, priority or classification.

## Source reading
Digest + targeted reads (digest CURRENT, hash 0e5c23a767a66a2f): SME report `reports/sme-lit-DorauMuch2026-20261015.md` in full; ch06 lines 30-60 and 128-145; appB lines 115-150; appH lines 12-100 (Problems A, B, area-term paragraph). Not a full scan.

## Research and reasoning
Bibliographic verification (done by me):
- Crossref, DOI 10.1103/lmq8-nsty: title "From Quantum Relative Entropy to the Semiclassical Einstein Equations"; authors Philipp Dorau, Albert Much; Physical Review Letters, vol. 136, issue 9, article number 091602; issued 2026-03-02; accepted 2026-02-09; CC BY 4.0. Matches the SME.
- arXiv abs page 2510.24491: same title, authors, DOI link; submitted 2025-10-28, v3 posted 2026-03-03; abstract matches the Crossref abstract.
- Paper content: I could not extract text from the PDF (compressed streams). I read the arXiv HTML v3 via the fetch tool, which returns a model-generated digest rather than verbatim text. That digest agrees with the SME report on every point used below: free real minimally coupled scalar; Hadamard quasifree state with coherent excitations; Minkowski vacuum in the Rindler case; S_rel(omega_0||omega_phi) given by the energy flux across the horizon (a U-weighted integral of the stress component along the Killing field); local Minkowski approximation by the equivalence principle; Raychaudhuri equation used; Bekenstein-Hawking relation assumed to relate flux to area variation (alpha = 8 pi then natural); local conservation fixes the trace part and an integration constant Lambda; relative-entropy formula does not hold for noncoherent states (extension expected, not shown); leading-order only. The explicit equation, including its sign convention, I did not independently verify, so the proposed text quotes no formula. Not independently verified: the paper's derivations (eqs. 10-13), the PRL text versus v3, and the paper's own references (Kay-Wald, Summers-Verch, Casini, Araki, etc.).

Positioning logic against the manuscript:
- ch06 Claim 1 is stated as "assumes a metric and a quantum field". The paper is of exactly that type, so it is accurate to cite it as a refinement of the matter side only.
- appB states the Bisognano-Wichmann identification is "exact for free fields in Rindler space" and not claimed for the matrix potential. The paper's free-field result is consistent with that and adds a rigorous modular-flow statement for general bifurcate Killing horizons in the free scalar case (per the SME and the HTML digest; the Summers-Verch/Kay-Wald attribution is the paper's, not independently verified). The appB sentence should therefore only say the free-field case is treated rigorously there, not that anything about the matrix potential follows.
- Over-attribution guards: no claim that the paper derives Einstein equations without inputs; no claim about G_eff (alpha is free until S = A/4 is imposed); no claim about interacting fields, non-coherent states, or emergent metrics.

SME suggestion 4 (relative-entropy form of ass:EE), assessment only. For the finite-dimensional diamond algebra of Definition `HD-SD` (ch06), S_D is a well-defined von Neumann entropy, so the type-III motivation does not apply at the level of the matrix model. For states rho and sigma on a fixed algebra, S(rho||sigma) = Delta<H_sigma> - Delta S, and its first-order variation about sigma vanishes identically; the "stationarity" content is then the first law dS = d<H>, which Appendix H already records as the fixed-algebra identity that does not imply dS_D = 0 and does not contain the area term (the area term comes from varying the algebra, which relative entropy of two states on one algebra does not address). Hence a relative-entropy restatement does not obviously preserve the content of Claim 2 and may trivialise it. Conclusion: not recommended as an assumption rewrite; at most a remark.

## Claim classification
- Paper's relative-entropy = flux result (free scalar, coherent states, bifurcate Killing horizon): established in the literature as the authors' claim; not independently verified by me.
- Paper's gravity step: conditional on metric, local Minkowski, S = A/4, Raychaudhuri; stated by the authors as leading-order argument.
- Statement "does not support Claim 2 / does not derive emergent-metric area term": established from the paper's stated inputs.
- Relevance as a consistency target for Problem A in the free, coherent, Rindler regime: conjecture/suggestion (not in the proposed text).
- Suggestion-4 assessment: reasoning, not established beyond the finite-dimensional observation above.

## Proposed changes

### bib/namcg.bib (integrator adds; key `DorauMuch2026` verified unused by grep in bib/, chapters/, proposals/)
```bibtex
@article{DorauMuch2026,
  author  = {Dorau, Philipp and Much, Albert},
  title   = {From Quantum Relative Entropy to the Semiclassical {Einstein}
             Equations},
  journal = {Physical Review Letters},
  volume  = {136},
  number  = {9},
  pages   = {091602},
  year    = {2026},
  doi     = {10.1103/lmq8-nsty},
  eprint  = {2510.24491},
  archivePrefix = {arXiv}
}
```

### chapters/ch06-entanglement-equilibrium.tex
Anchor (occurs once, verified): the sentence ending the paragraph "...pretend that Claim~2 has been derived from the path integral of / Chapter~3 with the same status as Claim~1." Insert a new paragraph immediately after it, before `\begin{assumption}[Microscopic entanglement equilibrium]`. Nothing existing is removed.

```latex
A recent operator-algebraic treatment~\cite{DorauMuch2026} gives a
rigorous form of the matter side of Claim~1 for a free real scalar
field: on a bifurcate Killing horizon, the relative entropy between
the vacuum and a coherent excitation equals the null energy flux
across the horizon. Its passage to the Einstein equation takes the
metric, a local Minkowski approximation, the Raychaudhuri equation
and the relation \(S=A/4\) as inputs. It therefore belongs to
Claim~1, and it is restricted to free fields and coherent states. It
does not support Claim~2 and does not derive an area term for the
emergent metric; that is the content of Problems~A and~B in
Appendix~\ref{sec:status-A}--\ref{sec:status-B}.
```
Issue: `\ref{sec:status-A}--\ref{sec:status-B}` yields section numbers "H.1--H.2"-style; acceptable. If the gatekeeper prefers, replace the last clause by "see Chapter~\ref{ch:agenda}". Labels verified to exist: `sec:status-A` (appH line 13), `sec:status-B` (line 42), `ch:agenda` (ch17 line 2).

### chapters/appB-modular.tex
Anchor (occurs once, verified; file uses CRLF): `theorem for the full matrix potential~\eqref{eq:V}.` at the end of section `sec:appB-BW`. Append after it:

```latex
For free scalar fields and coherent states, the modular flow on
a bifurcate Killing horizon and the identification of the relative
entropy with the horizon energy flux are treated rigorously
in~\cite{DorauMuch2026}. That result is for a prescribed metric and
says nothing about the interacting matrix condensate.
```
Labels verified: `eq:V` (ch03 line 241), `sec:appB-BW`. The sentence "modular flow ... rigorously" rests on the paper's abstract (modular theory, relative entropy = flux) and the SME report; the Summers-Verch/dilation detail is deliberately omitted because I did not verify it.

Stale passages elsewhere: none found; no other passage cites the paper (grep for DorauMuch returned nothing). Status line: none added (no label touched); the inserted text explicitly states what is not claimed.

## Verification scripts
None (no calculation). Verification was by Crossref API, arXiv abs page, arXiv HTML v3 digest, and greps for anchors/labels.

## Decisions Taken
- Placed the citation in ch06 (Claim 1 context) and one sentence in appB, rather than appH, since the request was positioning and appH ledger paragraphs are for problem-level evidence.
- Omitted the explicit relative-entropy formula and the Summers-Verch/Kay-Wald attributions because I could not verify sign conventions or attribution from verbatim text.
- Did not touch ass:EE; suggestion 4 assessed only.

## Milestone assessment
Routine.

## Status-label recommendation
None. Critical-path list unchanged (A, B, C, D1, E, F, G-derived, N per the current criterion); no label affected.

## Author decision needed
None.

## Remaining open step
- Problems A and B are unchanged: a matrix-derived modular Hamiltonian and the emergent-metric area term remain to be derived.
- Possible later (separate) sub-lemma for Problem A: test whether a matrix-derived H_D reproduces S_rel = flux for a free scalar on the emergent background in the free, coherent, Rindler regime. Consistency target only, valid only if the emergent (not scaffold) metric is used.
- Suggestion 4 (relative-entropy ass:EE): recommendation is not to rewrite the assumption; at most add a remark that on the finite-dimensional diamond algebra S(rho||sigma) = Delta<H> - Delta S has vanishing first variation at sigma, so the relative-entropy form carries only the fixed-algebra first law and not the area term. A later package may record this remark inside the Problem B ledger section after a normal gatekeeper round.
- The Jacobson-type step in NAMCG also needs a derived conserved total stress (the paper uses local conservation to fix the trace part); that is the existing 008/009 issue.

## Special instructions for the gatekeeper
- Check that the inserted text does not read as support for Claim 2 or for G_eff.
- Re-check the Crossref/arXiv record yourself; the paper body was seen only through a fetch-tool digest and the SME's page images, not verbatim by me.
- Confirm the `\ref{sec:status-A}--\ref{sec:status-B}` rendering is acceptable or substitute `Chapter~\ref{ch:agenda}`.
- No chapter files were edited; text above is for the integrator only upon ACCEPT.
