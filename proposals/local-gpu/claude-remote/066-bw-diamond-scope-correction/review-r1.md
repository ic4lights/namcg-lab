VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR, RESEARCHER-DECISION | PROGRESS: first | OPEN: 0/3

## Verdict
The central correction holds: the merged sentence crediting Bisognano–Wichmann with the diamond modular Hamiltonian of "the free theory" is materially false. Three things in the corrected paragraph still overclaim and must be fixed before a plain ACCEPT. (1) The new "Hence" sentence merges the wedge and diamond generators into one charge. (2) The half-sided-inclusion sentence still asserts "exactly H_D" with no source. (3) The retained claim about the Weyl symbol of K_0, which the lemma rests on, is unsupported, and a direct Moyal check does not reproduce it. A full scan is also required (ruling below).

## Source reading
Digest + targeted reads. This is not a full scan.
- `python scripts/make_digest.py --check` printed `DIGEST CURRENT`. head b9c417e, `dirty-chapters: yes` from the uncommitted 064/065 integrations, which is expected.
- Read in full:
  - appH L1–110 (Problem A: ledger label, lemma, general sector, missing step; start of Problem B);
  - ch17 L340–399 (Problem A and E entries);
  - ch03 L780–835 (`sec:ch3-scales`, `eq:scales`, the radial Higgs row, `eq:scale-ineq`);
  - appB L110–150 (`sec:appB-BW`, `eq:appB-BW`);
  - ch02 L436–456; ch06 L55–75 and L140–160 (`eq:HD-boost`);
  - bib L260–285; `namcg-book7.tex` L154–156 (`\nocite{*}`).
- Greps: `delta\Theta`, `Bisognano|Hislop|half-sided|Wiesbrock|Borchers`, `H_{\mathrm{quad}}`, `status-A|Free/Poisson`, radius notation.
- No unreadable repository files.

**Scan ruling (CLAUDE.md 3(c)).** E6 changes the text "is a lemma in this sector" to "is a lemma for that massless scalar part of this sector". E1 restricts the region and field class of the cited theorem. Together they narrow the stated scope of a claimed result in the ledger section of a critical-path problem. I rule this a change to a **scope statement** under 3(c). A full scan of every `chapters/**/*.tex` file is therefore required before a plain ACCEPT. Rule 3(b) independently requires one, because this verdict carries M3, a milestone trigger. I did not attempt the scan. Until the scan is done, the M3 determination and any later ACCEPT are provisional. If integration order allows, the split-pass scan can double as the ordinal-65 scan. Targeted grep found only one external reference to `sec:status-A` (ch06 L68), and it does not rely on the diamond claim.

## Claim under review
- **Claim.**
  - appH L30–31 ("By the Bisognano–Wichmann theorem this charge is the modular Hamiltonian of the causal diamond of the free theory") is false. Bisognano–Wichmann is a wedge theorem. The diamond result is Hislop–Longo, for the free massless scalar. The quadratic sector of the manuscript contains massive modes.
  - The bounds O(R√‖δΘ‖) at L36 and L54 are underived and uncited.
- **Proposed fix.** Edits E1–E6 plus bib entry B1.
- **Original target (ch17 L377–392).** Derive Assumption `ass:dictionary`, [X̂_μ,Φ] ↔ iΘ_{μν}D^νΦ plus higher-derivative corrections, specifying the Hilbert space, Weyl map, continuum limit and error at each order in Θ.
- **Current labels, verbatim.**
  - appH L16–20: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. The general matrix-to-modular map remains unproved. A scope-limited Presentation-B model may retain Assumption~\ref{ass:dictionary} and claims no derivation from the matrix model."
  - ch17 L378: "OPEN; CRITICAL PATH for the matrix-derived label."
  - The two sources agree. The package changes no label.

## Checks performed
- **Provenance.**
  - `git log -S` on the BW sentence and on `sqrt{\|\delta\Theta\|}` both return only 6aa4490.
  - `git show` gives: ic4lights, 2026-11-05, message "1", appH only (+49/−18). Confirmed.
  - `delta\Theta` occurs only at appH L36, L43 and L54. Confirmed.
  - `H_{\mathrm{quad}}` is defined nowhere in `chapters/`; this is new information.
- **Re-run of apply_check_066.py** (output to the scratchpad, not the proposal folder). Result: ALL CHECKS PASS.
  - Baselines match: appH 624232 bytes, c2dac013…558b5c; bib 29781 bytes, 28fdd7f8…a64d.
  - Each OLD string occurs once; no NEW string occurs beforehand.
  - Results match the proposal: appH 625157 bytes, 173ab97b…7e945, CRLF = LF = 3393; bib 30159 bytes, 4315a895…6060, CRLF = LF = 1006; no BOM.
  - I read the patched passage in full. The bib diff is exactly the new entry.
- **Re-run of lattice_modular_profile_066.py.** Output is byte-identical to the stored file. It is an illustration only: a 1D free-fermion chain, not the continuum scalar. Not relied on.
- **Scratch build.** Not re-run by me. The stored log reports pdflatex/bibtex exits 0, no undefined or multiply-defined references, `HislopLongo1982` in the .bbl, and 380 pages.
- **Labels.** `sec:appB-BW` (appB L118) and `sec:ch3-scales` (ch03 L790) each exist once. No new labels. No process language in the patched text. No status-label edits.
- **Literature.**
  - **BW 1976.** I could not fetch the eScholarship 0sf4t33q preprint (CloudFront 403), so I did not read Theorem 1 or eqs. (45)–(46) myself. I did verify the following:
    - doi.org/10.1063/1.522898 redirects to pubs.aip.org, which lists Bisognano and Wichmann, "On the duality condition for quantum fields", J. Math. Phys. 17(3) 303–321 (1976). This matches the existing bib entry.
    - The publisher abstract covers general boson/fermion fields, complex Lorentz transformations related to CPT, and duality conditions.
    - Secondary confirmation that the BW result is the wedge theorem: Longo–Morsella, arXiv:2012.00565, full text read. "If W is a wedge region, there is an important model independent result [6] … rescaled boost unitary transformations leaving W globally invariant." Their [6] is BW 1975, J. Math. Phys. 16, 985. The same text says that for other regions the modular group "in general … has no geometric description."
    - The wedge content of the 1976 paper specifically is therefore supported by its abstract and secondary sources. It is not independently verified from the primary text. This is adequate for the attribution E1 makes.
  - **Hislop–Longo.**
    - Crossref (api.crossref.org/works/10.1007/BF01208372) gives: Hislop and Longo, "Modular structure of the local algebras associated with the free massless scalar field theory", Commun. Math. Phys. 84(1) 71–85, March 1982. The bib entry B1 matches in every field, and the DOI is genuine.
    - The UKY Scholars abstract says the double-cone modular group of the free massless scalar is implemented by conformal (generalized fractional linear) transformations.
    - Longo–Morsella write: "In the free massless QFT, the geometric description of the double cone vacuum modular group was derived in [18]", where [18] is Hislop–Longo.
    - E1's statement is verified at abstract level plus a secondary source.
  - **Massive case.** The Longo–Morsella errata say their massive analysis had a gap and was removed. This supports E1's cautious "no such geometric identification is used here", which makes no non-geometricity claim.
- **Independent check of the retained K_0 symbol claim (supports Finding 3).** Take the Moyal convention [x̂_μ,x̂_ν] = iΘ_{μν}. Then [x̂_ν,f] = iΘ_{νρ}∂^ρ f and tr(x̂_μ ⋆ g) = ∫x_μ g. Reading H_quad as an algebra element with symbol h:

  K_0 = ½Θ^{-1μν}∫x_μ iΘ_{νρ}∂^ρ h = (i/2)∫x_μ∂^μ h.

  The step uses Θ^{-1μν}Θ_{νρ} = δ^μ_ρ. The result is a dilatation-type weighting, which integrates by parts to a multiple of ∫h. It is not the antisymmetric boost weighting x^0∂_i − x^i∂_0, and not the diamond conformal Killing vector. This is a check of the retained claim under its most natural reading, not a proof that it is false: H_quad is undefined, and another reading might differ.

## Findings
1. **Major. E1, final sentence ("Hence the charge is the modular Hamiltonian of the wedge for the free theory, and of the causal diamond only for its free massless scalar part").**
   - Finding: the sentence assigns one charge to two different modular Hamiltonians. The wedge boost generator and the diamond conformal Killing generator are different operators. The single "boost/diamond Noether charge" of L28 cannot be both.
   - Reason: "Hence" does not follow from the two preceding sentences, which concern two different generators. It also adds an unqualified new claim that the charge is the wedge modular Hamiltonian.
   - Required action: make the identification conditional on which generator the symbol equals (see the corrected snippet).
2. **Major. L32–33, unchanged ("The positive spectral subspace therefore generates the half-sided inclusion whose modular operator is exactly H_D").**
   - Finding: after E1 and E6, "therefore … exactly H_D" still stands unscoped and unsourced. E6's restricted lemma depends on it.
   - Reason: no reference or derivation exists in the repository. Grep finds no Wiesbrock, Borchers or Araki–Zsido source. "The positive spectral subspace generates a half-sided inclusion" is not a standard construction as stated. A correction package that rewrites this lemma cannot leave its next inferential step overclaiming.
   - Required action: scope it to the massless diamond case and mark it as not derived or sourced (snippet below). A derivation can follow in a later package.
3. **Major. L28 retained, and the lemma as a whole ("has Weyl symbol equal to the classical boost/diamond Noether charge").**
   - Finding: the identification is neither derived nor sourced, and H_quad is defined nowhere in the manuscript. The Moyal evaluation above gives a dilatation-type weighting, not a boost or diamond-CKV weighting.
   - Reason: the corrected lemma, including E6's "is a lemma for that massless scalar part", rests on this identification. This may be a second prior-claim error. I do not assert that it is one, because the operator is undefined.
   - Required action: either (a) define H_quad and give the symbol computation showing which charge K_0 equals, with the index contraction made explicit, or (b) mark the identification as not derived. Option (b) is in the snippet.
4. **Minor. E2 and the L54 display.**
   - Finding: defining R as "the diamond radius" adds a second symbol for a quantity that ch06 and appB call ℓ. In appH, R is also used for other radii and for curvature.
   - Required action: use ℓ in both places. This needs one new edit, E7, on the display line `=O\bigl(R\sqrt{\|\delta\Theta\|}+\|H_{\mathrm{int}}\|\bigr)`.
5. **Minor. E2/E3 wording.**
   - Finding: "unproved estimate" is acceptable; "conjectured" would classify it more precisely. Keeping the estimate is better than deleting it: it records the author's target, and E5 already states that it controls at most the difference from an unproven candidate.
   - Note: for unbounded modular generators, the norm in ‖σ_t^fluct − σ_t^free‖ is not specified. The researcher may add "in a norm not specified here".
   - Required action: optional wording; not blocking.
6. **Minor, pre-existing, not in the edits. L38 ("the conditional free/Poisson content already noted above").** Nothing above it in the section notes this content. Optional cleanup in the same revision.

## Scope of what is established
- **Established (correction).**
  - Bisognano–Wichmann gives the wedge vacuum modular group as rescaled boosts, model-independently. That includes massive free fields.
  - The geometric diamond (double-cone) modular group is established for the free massless scalar by Hislop–Longo, verified at abstract level plus a secondary source.
  - The L30–31 sentence is false as written. It misattributes the diamond result to BW, and it extends that result to a "free theory" whose quadratic sector contains the massive radial mode m_σ ∼ √λ v (ch03 `sec:ch3-scales`). Reading "free theory" as "a massless sector" does not rescue it: the misattribution remains, and the lemma's sector is not massless.
  - This confirms a PRIOR-CLAIM-ERROR in author-committed text (6aa4490). That is trigger M3, provisional pending the required full scan.
- **Unresolved, and the package correctly does not claim them:** the δΘ estimate; the half-sided-inclusion step; the K_0 symbol identification.
- **Problem A** remains "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL." The package is neither DERIVED nor PROGRAMME-CONDITIONAL progress on A. It narrows existing evidence.
- **Avenues that could still help the IR / full-GR derivation**, ranked by my judgement:
  1. **Wedge formulation of the Problem A modular map** (researcher's avenue 2). BW is mass-independent; the cost is connecting to the diamond-based first law.
  2. **First establish what K_0 actually is** (Finding 3). Whether the modular route works at all depends on it.
  3. **IR theory below m_σ after integrating out σ** (avenue 3). Here the conformal-sector content decides whether a Hislop–Longo-type result applies. Massless free Maxwell is not covered by HL.
  4. **Small-diamond ℓ ≪ 1/m_σ error control** (avenue 1). This is hard: the published massive-ball result was withdrawn because of a gap.
  5. **Free massless Maxwell/fermion diamond results** (avenue 4). Literature not checked.
- **Report-only item.** The ch17/appH definitional mismatch (ch17 defines A as the IR dictionary; appH frames it as a "matrix-to-modular map") is real, and the researcher quoted both texts accurately. It is a scope/definition question for the author. No edit is proposed, and it does not affect this verdict.

## Recommended disposition
Revise (round 2), then run the full scan (3(b)/(c)) before any plain ACCEPT.

**RESEARCHER-DECISION.** Should the paragraph keep the heading "(lemma)"?
- (a) Keep "lemma" and supply derivations of the K_0 symbol identity and the half-sided-inclusion step in this or a following package. This is more valuable for A if achievable.
- (b) Mark both steps as not derived and make "lemma" conditional on them, as in the snippet below. This is accurate now.

Either is acceptable. Neither changes a Problem A status, priority or completion label.

## Corrected snippet
No new physics; it only scopes existing claims. Extra assumptions: none. It implements option (b).

Replace this text from patched E1/E6:

```latex
mass \(m_\sigma\) of Section~\ref{sec:ch3-scales}. Hence the charge
is the modular Hamiltonian of the wedge for the free theory, and
of the causal diamond only for its free massless scalar part. The
positive spectral subspace therefore generates the half-sided inclusion
whose modular operator is exactly \(H_D\). The map
\((\hat X,\Phi)\mapsto H_D\) is a lemma for that massless scalar part
of this sector, defined from
```

with:

```latex
mass \(m_\sigma\) of Section~\ref{sec:ch3-scales}. Hence the charge
is a vacuum modular Hamiltonian only where it coincides with one of
these generators: the wedge boost charge, for the free theory, or the
diamond conformal Killing charge, for its free massless scalar part.
Which of these charges the Weyl symbol of \(K_0\) equals, and for
which \(H_{\mathrm{quad}}\), is not derived here. Nor is the statement
that, in the diamond case, the positive spectral subspace generates a
half-sided inclusion whose modular operator is \(H_D\). Given these
two steps, the map \((\hat X,\Phi)\mapsto H_D\) is a lemma for that
massless scalar part of this sector, defined from
```

E2 (replacing the proposed NEW):

```latex
\(\Theta\). Its error under fluctuations of \(\Theta\) is not derived
here; the scaling \(O(\ell\sqrt{\|\delta\Theta\|})\), with \(\ell\) the
diamond radius, is an unproved estimate.
```

E7 (new; the L54 display line):

OLD: `=O\bigl(R\sqrt{\|\delta\Theta\|}+\|H_{\mathrm{int}}\|\bigr)`

NEW: `=O\bigl(\ell\sqrt{\|\delta\Theta\|}+\|H_{\mathrm{int}}\|\bigr)`

E3–E5 and B1: acceptable as proposed. Re-run apply_check against the same baselines, and re-run the scratch build.

Relevant paths:
- C:\Users\redgi\Projects\namcg-lab\proposals\066-bw-diamond-scope-correction\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (L22–61)
- C:\Users\redgi\Projects\namcg-lab\bib\namcg.bib (L267–275)
- Re-run outputs: C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\ac066\ (patched copies) and C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\lat066.txt

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR, RESEARCHER-DECISION | PROGRESS: first | OPEN: 0/3
