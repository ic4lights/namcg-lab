# Proposal 007-N-formfactor-citation, round K=1

## Result
Adds one citation, Barvinsky and Vilkovisky, Nucl. Phys. B 333 (1990) 471-511, to the uncited statement in the Problem N block of `chapters/appH-microscopic-proofs.tex` (`sec:status-N`). The statement is that the one-loop action at second order in curvature is nonlocal with momentum-dependent form factors. The citation is for nonlocality and form factors only. The decay of the Weyl form factor at `sk^2 >> 1` stays an explicit assumption ("assuming that ..."), and nothing is cited for it. No mathematics and no status are touched.

## Target and status
Problem N, `sec:status-N`. I did not re-derive the status, priority or classification, because the change is bibliographic and touches no label. Original target and dependencies are unchanged. The result is a bibliographic correction, neither DERIVED nor PROGRAMME-CONDITIONAL. It follows the follow-up from proposal 002 review-r2 finding 8 and `proposals/004-author-questions` Q3.

## Source reading
Digest plus targeted reads. I read the Problem N passage at appH lines 2092-2111 and the `bib/namcg.bib` neighbours around Stelle1977. I did not do a full scan. This is a one-token change that alters no definition, scope or status.

## Research and reasoning
Record check (Crossref API query, 2026-10-14):
- Title: "Covariant perturbation theory (II). Second order in the curvature. General algorithms".
- Authors: A. O. Barvinsky, G. A. Vilkovisky.
- Journal: Nuclear Physics B, vol. 333, issue 2, March 1990, pages 471-511.
- DOI: 10.1016/0550-3213(90)90047-H. Crossref returned it in lowercase, `10.1016/0550-3213(90)90047-h`; DOIs are case-insensitive.

My first guessed DOI ending `90258-X` returned "Resource not found". It was wrong and is discarded; the DOI above is the one the Crossref bibliographic search returned.

Scope of support: the paper builds the heat-kernel and effective action at second order in curvature as nonlocal form factors. I have not read the full text, and I rely on the title and my knowledge of the paper. I cite it only for "nonlocal form factors at second order in curvature". The decay of the Weyl form factor at large `sk^2` is not claimed from this source. That keeps the "assuming that" clause intact.

Key check: `grep` finds no `Barvinsky`, `Vilkovisky` or `BarvinskyVilkovisky1990` in `bib/` or `chapters/`. The key is free. The anchor is unique (grep count 1 for the sentence, with the line break). The only `\cite` command uses are other keys, so no label conflicts arise. A `\cite` adds no `\label`.

## Claim classification
- Second-order one-loop action is nonlocal with form factors: established in the literature (the record is verified, the content is from the abstract/title and not independently read in full).
- Weyl form factor decays for `sk^2 >> 1`: unchanged, an assumption (conditional).

## Proposed changes
File `bib/namcg.bib` (for the integrator, after the Stelle1977 entry):

```bibtex
@article{BarvinskyVilkovisky1990,
  author  = {Barvinsky, A. O. and Vilkovisky, G. A.},
  title   = {Covariant perturbation theory ({II}). Second order in the curvature. General algorithms},
  journal = {Nuclear Physics B},
  volume  = {333},
  pages   = {471--511},
  year    = {1990},
  doi     = {10.1016/0550-3213(90)90047-H}
}
```

File `chapters/appH-microscopic-proofs.tex`, inside `sec:status-N`. Anchor (occurs once, spanning a line break): "At second order in curvature the one-loop action / is nonlocal, with momentum-dependent form factors; assuming that". The change replaces only `form factors;` with `form factors~\cite{BarvinskyVilkovisky1990};`. The rest stays, including "assuming that the Weyl form factor decays when \(sk^2\gg1\)".

```latex
is nonlocal, with momentum-dependent form factors~\cite{BarvinskyVilkovisky1990}; assuming that
```

Stale passages elsewhere: none.

## Verification scripts
None needed. The checks were a Crossref query, a grep for the key and a grep for the anchor, as described above.

## Decisions Taken
Cite narrowly for nonlocal form factors, following the 004 Q3 recommendation. The alternative, placing the cite after the decay clause, is rejected because it would imply support for the decay assumption.

## Milestone assessment
Routine.

## Status-label recommendation
None. No labels are affected.

## Author decision needed
None.

## Remaining open step
None for this item. The decay assumption and all of Problem N's own open steps are unchanged.

## Special instructions for the gatekeeper
Check that the cite does not support decay. Re-check the DOI against Crossref. Check that the key is unused. The PDF page range 471-511 is from Crossref, and I did not check the PDF.
