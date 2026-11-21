# 070 — Peters attribution citation completion (ch14) + El-Badry catalogue reference (report-only)

Package type: citation-completion / prior-attribution gap. No Problem object. No status, priority or
completion label is touched, proposed or implied. No derivation is originated or altered; every equation in
the touched passages stays byte-identical.

Origin: vector-miner mode-6 run 2026-11-13 (congruence mining against 066/069 and recent author merges);
findings 1 and 2 of its report, re-verified in-tree by the orchestrator. Author instruction 2026-11-13:
"apply actionable findings".

## Finding and evidence

`chapters/ch14-dissipation.tex` L226-227 attributes eq:Peters to "the Peters--Mathews power" with no
`\cite`; `bib/namcg.bib` contains no Peters key (grep: only "Mem. Acad. St. Petersbourg" matches
"Peters"). This is the only externally-named formula in the section without a citation.

Primary records, verified independently by the orchestrator via Crossref API on 2026-11-13 (record level
only; equation content of those papers not read):

- Peters, P. C. and Mathews, J., "Gravitational Radiation from Point Masses in a Keplerian Orbit",
  Physical Review 131, 435-440 (1963), DOI 10.1103/physrev.131.435.
- Peters, P. C., "Gravitational Radiation and the Motion of Two Point Masses", Physical Review 136 (4B),
  B1224-B1232 (1964), DOI 10.1103/physrev.136.b1224.

The displayed 32/5 form with inclination average matches the orbit-averaged quadrupole power convention of
the 1964 paper; the 1963 paper carries the underlying point-mass quadrupole formula. Citing both is the
standard attribution. The ApJ 138 (1963) 470 record sometimes cited for the orbit-averaged power did NOT
resolve in either the miner's or this package's searches and is NOT used here (unverified).

## Edits to apply (E1, E2)

### E1 — chapters/ch14-dissipation.tex (pre-edit sha256 b1fefa684669f0315e705061a9efd84c732eca741e687b9f3a88977f2f976dd2, 17336 B)

OLD (L226-227, single hit):

    The Isaacson flux of the tensor block for a weak, slow binary is
    the Peters--Mathews power

NEW:

    The Isaacson flux of the tensor block for a weak, slow binary is
    the Peters--Mathews power~\cite{PetersMathews1963,Peters1964}

No other line changes. eq:Peters itself is untouched.

### E2 — bib/namcg.bib (pre-edit sha256 36931b9313266d619003b6a42af882dda2ab825d22551055cd124eb1527e2761, 36511 B; equals the post-066 hash recorded in the ledger)

Append after the final entry `FlissFrenkelHartnollSoni2025` (end of file, after the closing `}`), matching
the file's existing entry style:

    @article{PetersMathews1963,
      author  = {Peters, P. C. and Mathews, J.},
      title   = {Gravitational Radiation from Point Masses in a {Keplerian} Orbit},
      journal = {Physical Review},
      volume  = {131},
      pages   = {435--440},
      year    = {1963},
      doi     = {10.1103/physrev.131.435}
    }

    @article{Peters1964,
      author  = {Peters, P. C.},
      title   = {Gravitational Radiation and the Motion of Two Point Masses},
      journal = {Physical Review},
      volume  = {136},
      number  = {4B},
      pages   = {B1224--B1232},
      year    = {1964},
      doi     = {10.1103/physrev.136.b1224}
    }

Label hygiene: grep confirms `Peters` keys and `\cite{Peters` are currently absent from bib/ and
chapters/; no duplicate bib keys.

## E3 — El-Badry catalogue reference: REPORT-ONLY, author decision (no edit in this package)

`chapters/appI-gaia-wide.tex:32-33` names "the public El-Badry et al.\ Gaia DR3 wide-binary catalogue" with
no `\cite` and no bib key. Record-level resolution performed:

- The canonical El-Badry wide-binary catalogue paper is El-Badry, Rix & Heintz, "A million binaries from
  Gaia eDR3: sample selection and validation of Gaia parallax uncertainties", MNRAS 506, 2269-2295 (2021),
  DOI 10.1093/mnras/stab323 (verified via Crossref). It is an **eDR3**-based catalogue.
- No El-Badry **DR3**-era wide-binary catalogue paper surfaced in two Crossref searches (2026-11-13). The
  miner's earlier candidate DOI 10.1093/mnras/stac3140 resolves to an unrelated paper.
- The quality cuts quoted at appI:34-35 (RUWE<1.3, fractional parallax error <0.06, separations 2-30 kAU)
  are the only such statements in the manuscript; no other passage pins the data release.

Because the text says DR3 and the only verified catalogue paper is eDR3-based, attaching
`\cite{ElBadryRixHeintz2021}` to the current wording would risk a false provenance attribution. Options for
the author: (i) cite the 2021 paper and change "Gaia DR3" to "Gaia eDR3"; (ii) keep "DR3" and supply the
DR3-era record if one exists under the author's knowledge (not found here); (iii) leave uncited. This
package deliberately does not guess.

## Report-only side notes (no edits)

- bib `BisognanoWichmann1976` lists pages "303"; the Crossref primary record is 303-321 (minor completeness;
  066 miner finding). Author decision.
- La Piana & Morsella, "The fermionic massless modular Hamiltonian", CMP 406 (2025) 81, arXiv:2405.07888,
  DOI 10.1007/s00220-025-05253-1 (record verified by miner): free massless FERMION double-cone modular
  Hamiltonian. Relevant only if Problem A/appB wording is read as "only the free massless scalar has an
  explicit diamond modular Hamiltonian". No text proposed.

## Verification plan

1. OLD blocks single-hit pre-patch (done by integrator grep before edit).
2. Post-patch: grep `\cite{PetersMathews1963,Peters1964}` present at ch14:227; keys unique in bib; no
   duplicate bib keys.
3. `python scripts/build_check.py`: PASS expected; bibtex resolves both new keys; 0 undefined/multiply-defined.
4. CRLF preserved, UTF-8 no BOM (all three files confirmed CRLF/no-BOM pre-edit).

## Classification

Established primary records (Crossref-verified at metadata level). Attribution gap fix only; no physics
content claimed, no equation re-derived. The equation-vs-paper content match is the manuscript's existing
claim, unchanged by this package.
