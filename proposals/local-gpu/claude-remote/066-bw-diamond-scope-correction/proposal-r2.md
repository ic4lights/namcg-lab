# Proposal 066-bw-diamond-scope-correction, round 2

## Change list r1 → r2

| Finding (review-r1) | Severity | Action in r2 | Edit id (direct list) |
|---|---|---|---|
| 1. The "Hence" sentence merges the wedge and diamond generators | major | Replaced by the gatekeeper's option-(b) snippet. The charge is a vacuum modular Hamiltonian only where it coincides with the wedge boost charge (free theory) or the diamond conformal-Killing charge (free massless scalar part). | F1 |
| 2. Half-sided-inclusion sentence: "exactly H_D", unsourced | major | Scoped to the diamond case and marked "not derived here" (snippet). The lemma is made conditional on it ("Given these two steps …"). | F1 |
| 3. The K_0 Weyl-symbol claim is unsupported (gatekeeper Moyal check gives dilatation weighting) | major | RESEARCHER-DECISION resolved as option (b); see Decisions Taken. Snippet adopted. In addition, L28 "has Weyl symbol equal to" becomes "is taken here to have Weyl symbol equal to", so the claim is not asserted as fact before it is declared underived. The Moyal check was reproduced in `moyal_K0_symbol_066.py`. | F0, F1 |
| 4. R → ℓ (diamond radius, as in ch06/appB) | minor | E2 now uses ℓ. New edit E7 changes R → ℓ in the L54 display. | F2, F6 |
| 5. Wording / norm | minor | "unproved estimate" kept. Added "(in a norm not specified here)" to E3. | F3 |
| 6. L38 "already noted above" | minor | Cleanup: "This records the conditional free/Poisson content of Problem~A; it remains dependent on the free-field theorems cited above and on the two steps not derived here." | F7 |
| Full-scan ruling (3(b)/(c)) | — | Accepted. Per the orchestrator, the full scan runs separately before integration. | — |

E4 and E5 (now F4 and F5) and B1 (now F8) are unchanged from r1. The r1 scripts and outputs are kept as
`apply_check_066.py.r1`, `apply_check_066_output.txt.r1` and `scratch_build_066_output.txt.r1`.

## Result

This round makes no change to the core finding of r1, which the gatekeeper confirmed.
- appH L30–31 ("By the Bisognano–Wichmann theorem this charge is the modular Hamiltonian of the causal diamond of
  the free theory") is false. It misattributes the result and overstates its range.
- Bisognano–Wichmann (BW) is a wedge theorem for general Wightman fields, massive included.
- The geometric double-cone modular flow is Hislop–Longo, proved for the free massless scalar.
- The lemma's quadratic sector contains the massive radial mode m_σ.

Round 2 also scopes the two remaining unsupported steps of the free/Poisson lemma. These are the K_0
Weyl-symbol identification and the half-sided-inclusion step. Both are now explicitly "not derived here". The map
(X̂,Φ)↦H_D is a lemma only conditional on them, and only for the free massless scalar part. The √δΘ estimates are
marked unproved, with ℓ as the diamond radius and the norm unspecified.

A new symbolic check (`moyal_K0_symbol_066.py`) confirms the gatekeeper's computation. On the Moyal plane, for a
generic quadratic symbol h, the integrand of K_0 = ½Θ^{-1μν}tr(x̂_μ[x̂_ν,h]_⋆) equals (i/2)x^μ∂_μh pointwise.
That is a dilatation-type weighting, not the boost weighting x⁰∂₁h − x¹∂₀h.

No status, priority or completion label changes.

## Target and status

Unchanged from r1.
- Problem A, `sec:status-A`: OPEN; CRITICAL PATH for the matrix-derived label; PROGRAMME-CONDITIONAL. appH L16–20
  and ch17 L378 agree.
- Original target (ch17 L377–392): derive `ass:dictionary` with Hilbert space, Weyl map, continuum limit and error
  at each order in Θ.
- This package corrects a materially false claim and scopes evidence. It is not progress on A.

## Source reading

Digest + targeted reads. In addition to r1, I read `review-r1.md` in full, including:
- the gatekeeper's Moyal check;
- the scope ruling;
- the literature checks: Crossref for Hislop–Longo, and AIP/doi for BW 1976, which verify the DOI
  10.1063/1.522898 the gatekeeper resolved.

Baseline re-verified by `apply_check_066_r2.py`: appH 624232 bytes / c2dac013…558b5c; bib 29781 bytes /
28fdd7f8…a64d. These are unchanged, so the author has not committed changes to these files since r1. The
appH-internal structure (L22–61) is the one quoted in r1.

## Research and reasoning

r1 §§1–5 stand: source verification, the verdict on the sentence, the δΘ bound, and the no-go fork avenues. The
additions follow.

### K_0 symbol (Finding 3)

Moyal plane, [x̂_μ,x̂_ν] = iΘ_{μν}. Then [x̂_ν, f]_⋆ = iΘ_{νρ}∂^ρ f exactly for any f, since the Moyal series
truncates on a linear function. With tr ↦ ∫ and ∫ f⋆g = ∫ fg:

K_0 = ½Θ^{-1μν}∫x_μ(iΘ_{νρ}∂^ρh) = (i/2)∫x_μ∂^μh.

- The contraction Θ^{-1μν}Θ_{νρ} = δ^μ_ρ is independent of signature conventions.
- `moyal_K0_symbol_066.py` implements the exact Moyal product in d = 2 for a generic quadratic h, with six free
  coefficients. The integrand x_μ⋆[x_ν,h]_⋆ contracted with ½Θ^{-1μν} equals (i/2)x·∂h identically.
- It is not proportional to the boost weighting for generic h.
- Integrated over the plane, x·∂h = ∂·(xh) − d·h, which is a multiple of ∫h up to boundary terms. That is a
  multiple of the Hamiltonian itself, not a boost or conformal-Killing charge.

**Classification.** This is an established computation under the reading "H_quad = an algebra element with Weyl
symbol h, tr = Moyal trace". It is not a disproof of L28: H_quad is defined nowhere in `chapters/`, and another
reading could differ. For example, H_quad might be a superoperator on fluctuation fields, or tr might be a partial
trace with a different index placement.

**Fork (directive 2026-10-15).** Which readings could make the symbol a boost charge?
- (i) An index structure Θ^{-1}_{μν} x^μ … with the commutator acting on a stress-tensor density rather than on h
  itself. This needs a definition of H_quad as a field-space operator.
- (ii) Replacing Θ^{-1} by an antisymmetric boost generator ω^{μν}: ½ω^{μν}∫x_μ∂_νh is a boost weighting.
  However, ω is then a supplied geometric datum, not matrix data.
- (iii) A partial trace over internal indices only, leaving a spacetime-local density.

None was derivable within this package without first defining H_quad. Ranked follow-up:
1. Define H_quad and redo the symbol computation (i).
2. The wedge reformulation (r1 avenue 2), which needs only a boost charge.

### Option choice

See Decisions Taken.

## Claim classification

- BW: the wedge modular group consists of rescaled boosts, for general Wightman fields (massive included).
  **Established** (primary preprint Theorem 1, read in r1; abstract and secondary sources verified by the
  gatekeeper).
- Hislop–Longo: geometric (conformal) double-cone modular group for the free massless scalar. **Established**
  (abstract level plus a secondary source).
- The appH L30–31 sentence is false or overbroad. **Established** (correction).
- K_0 with H_quad read as a Moyal element h gives the (i/2)x·∂h weighting. **Established computation, conditional
  on that reading.**
- The K_0 symbol equals a boost or diamond charge. **Unresolved** (now marked not derived).
- The half-sided inclusion has modular operator H_D. **Unresolved** (now marked not derived).
- The δΘ estimates. **Unresolved** (marked unproved; norm unspecified).
- Massive diamond modular flow is non-geometric. **Not claimed.**
- The lattice profile. **Illustration only.**

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`: final direct OLD→NEW list against the baseline

All edits are in `\section{Problem A: matrix-to-modular map}`, paragraphs "Free/Poisson sector (lemma)" and
"General sector". The "Ledger label." and "Missing step." paragraphs, the headings and all labels are untouched.
Each OLD occurs exactly once in the baseline, and each NEW exactly once in the result. Line breaks are CRLF.

**F0** (L28). The rest of the sentence is kept.

OLD:
```latex
has Weyl symbol equal to the classical boost/diamond Noether charge
```
NEW:
```latex
is taken here to have Weyl symbol equal to the classical boost/diamond
Noether charge
```

**F1** (L30–34). This replaces the BW sentence, the half-sided-inclusion sentence and the head of the lemma
sentence. L35 "matrix operators before any composite metric, exact at constant" is kept.

OLD (the en-dash is U+2013):
```latex
degree \(\le 2\)). By the Bisognano–Wichmann theorem this charge is the
modular Hamiltonian of the causal diamond of the free theory. The
positive spectral subspace therefore generates the half-sided inclusion
whose modular operator is exactly \(H_D\). The map
\((\hat X,\Phi)\mapsto H_D\) is a lemma in this sector, defined from
```
NEW:
```latex
degree \(\le 2\)). For a Rindler wedge, the Bisognano--Wichmann
theorem~\cite{BisognanoWichmann1976} identifies the vacuum modular
Hamiltonian with \(2\pi\) times the boost generator that fixes the
wedge (Section~\ref{sec:appB-BW}), for free fields with or without
mass. For a causal diamond (double cone), the identification of the
vacuum modular flow with the conformal Killing flow of the diamond is
established for the free massless scalar field~\cite{HislopLongo1982},
through conformal covariance. No such geometric identification is
used here for massive free fields, such as the radial mode with the
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

**F2** (L36).

OLD:
```latex
\(\Theta\), with error \(O(R\sqrt{\|\delta\Theta\|})\) under fluctuations.
```
NEW:
```latex
\(\Theta\). Its error under fluctuations of \(\Theta\) is not derived
here; the scaling \(O(\ell\sqrt{\|\delta\Theta\|})\), with \(\ell\) the
diamond radius, is an unproved estimate.
```

**F7** (L37–39).

OLD:
```latex
Mutual information follows from the Araki formula. This makes explicit
the conditional free/Poisson content already noted above; it remains
dependent on the free-field theorem.
```
NEW:
```latex
Mutual information follows from the Araki formula. This records the
conditional free/Poisson content of Problem~A; it remains dependent on
the free-field theorems cited above and on the two steps not derived
here.
```

**F3** (L50–52). The display opening `\[` is kept.

OLD:
```latex
terms and is not a routine specialisation of the free-field result. The
bound
\[
```
NEW:
```latex
terms and is not a routine specialisation of the free-field result. The
estimate, which is not derived here (in a norm not specified here),
\[
```

**F6** (E7, L54).

OLD:
```latex
=O\bigl(R\sqrt{\|\delta\Theta\|}+\|H_{\mathrm{int}}\|\bigr)
```
NEW:
```latex
=O\bigl(\ell\sqrt{\|\delta\Theta\|}+\|H_{\mathrm{int}}\|\bigr)
```

**F4** (L56–58). Unchanged from r1's E4.

OLD:
```latex
controls the difference from the free modular flow (itself identified
with the diamond only in the constant-\(\Theta\) quadratic sector); it
does not control
```
NEW:
```latex
would control the difference from the free modular flow (itself
identified with the diamond only in the constant-\(\Theta\) quadratic
sector, and there only for its free massless scalar part); it would
not control
```

**F5** (L59–60). Unchanged from r1's E5. The final "Hamiltonian." is kept.

OLD:
```latex
of the general theory. The error bound therefore controls the
difference from an unproven candidate, not from the diamond modular
```
NEW:
```latex
of the general theory. Even if derived, the estimate would therefore
control only the difference from an unproven candidate, not from the
diamond modular
```

**Result:** appH 625504 bytes, sha256 `b8155af307c5d8840405d2bb8e4d3e1b5217316d1fcf555f398839c9ce82394e`.
CRLF = LF = 3398, no bare LF, no BOM. The chain baseline → r1 (hash 173ab97b…, confirmed) → r2 deltas D0–D5
gives a byte-identical result to the direct list F0–F7.

### `bib/namcg.bib`

**F8** = r1's B1, unchanged: insert `HislopLongo1982` after `BisognanoWichmann1976`. The full BibTeX is in r1 and
in the script; Crossref was re-verified by the gatekeeper. Result: 30159 bytes, sha256
`4315a89553cb97405af89604f1e43c9e5e0237fa5b7be0439431d042677a6060`, CRLF = LF = 1006.

### Labels and keys

- `sec:appB-BW` and `sec:ch3-scales` each exist once.
- No new labels.
- New citation `HislopLongo1982`; existing citation `BisognanoWichmann1976`.
- ℓ as the diamond radius matches ch06/appB usage (`eq:HD-boost` context, appB L134–141).

### Stale passages elsewhere

None. The BW statements in ch02 L443–444, ch06 L149–151 and appB L119–144 are about wedges ("Rindler space") and
are correct. The gatekeeper found that the only external reference to `sec:status-A` (ch06 L68) does not rely on
the diamond claim.

## Verification scripts

- `apply_check_066_r2.py <repo> <outdir>` → `apply_check_066_r2_output.txt`. Report-only. It builds backslashes
  with `chr(92)` and asserts that the out-dir is outside the repo. It checks:
  - the baseline hashes;
  - the r1 result hashes via the r1 edits;
  - for each r2 delta and each direct edit, OLD exactly once before and NEW exactly once after;
  - chain == direct;
  - CRLF only and no BOM.

  Status: ALL CHECKS PASS (21 edit checks). Output dir:
  `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\out066r2b`.
- `moyal_K0_symbol_066.py` → `moyal_K0_symbol_066_output.txt`. The exact Moyal-product check of the K_0
  integrand (Finding 3).
- `lattice_modular_profile_066.py` → `lattice_modular_profile_066_output.txt`. Unchanged; illustration only.
- r1 files kept: `apply_check_066.py.r1`, `apply_check_066_output.txt.r1`, `scratch_build_066_output.txt.r1`.
  `apply_check_066.py` (the r1 script) is also left in place unchanged.
- Scratch build: see "Build result" below.

## Decisions Taken

**RESEARCHER-DECISION (review-r1, Findings 1–3): option (b).** The lemma is made conditional on the two steps,
using the gatekeeper's snippet plus the F0 rewording of L28.

Reasons:
- (a) would require deriving the K_0 symbol identity. Under the only reading the manuscript supports, my symbolic
  check confirms that this gives a dilatation weighting (i/2)x·∂h, not a boost or diamond charge. H_quad is
  undefined, so (a) cannot be completed now without first defining a new object. Defining it is a change to the
  core content of the lemma and needs its own package.
- (a) would also require deriving the half-sided-inclusion step. That needs Wiesbrock/Borchers-type
  half-sided-modular-inclusion input for which the repository has no source.
- Keeping "(lemma)" in the heading with the conditional sentence is accurate: the paragraph states exactly what
  the lemma would be, given the two steps.

Option (b) favours the IR / full-GR derivation more than (a)-by-assertion. It isolates the missing ingredient (the
operator-level definition of the K_0 charge) as the concrete next target, rather than leaving a claim that
silently fails.

Rejected:
- (a) now, which is not derivable;
- deleting the lemma, which would lose the correct wedge statement usable by the wedge-reformulation avenue.

Other routine choices:
- F0 added, so L28 does not assert as fact what F1 declares underived.
- Norm phrase added (optional Finding 5).
- L38 cleanup done (optional Finding 6).
- ℓ adopted for the radius (Finding 4).

## Milestone assessment

M3: correction of a materially false prior claim in author-committed text (commit 6aa4490), confirmed by the
gatekeeper. It is provisional pending the full scan, which the orchestrator runs separately. Not a breakthrough.

## Status-label recommendation

The critical-path set at full-GR / matrix-derived scope is A, B, C, D1, E, F, G-derived and N (ch17 and appH).
Affected labels: none. Problem A stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

### Separate item (report only, carried from r1, confirmed by the gatekeeper)

The ch17/appH definitional mismatch for Problem A: ch17 L377–392 defines A as the infrared dictionary with error
control, while appH L12/L17–18/L63–69 frames it as a "matrix-to-modular map". The verbatim quotes and options are in
proposal-r1.md. I recommend option (i): align appH with ch17, treating the modular map as one route. This is an
author scope decision. No edit.

## Author decision needed

Only the ch17/appH Problem A definitional mismatch (above). No edit is proposed.

## Remaining open step

- Problem A, original target: OPEN, unchanged.
- In the free/Poisson lemma, three steps remain:
  - (1) define H_quad and compute which charge the K_0 symbol equals. Under the Moyal-element reading it is the
    dilatation weighting, so a different operator definition is needed for a boost charge;
  - (2) derive or source the half-sided-inclusion step;
  - (3) derive the δΘ estimate in a specified norm, e.g. via a Connes-cocycle bound on the relative modular
    generator.
- Ranked follow-up avenues:
  1. wedge reformulation;
  2. defining K_0 and H_quad;
  3. the IR theory below m_σ;
  4. small-diamond error control;
  5. Maxwell/fermion diamond results.

## Special instructions for the gatekeeper

- Verify that F1 is your snippet verbatim apart from its first line. The first line is E1's last line,
  "mass \(m_\sigma\) of Section~\ref{sec:ch3-scales}. Hence the charge", kept as in your snippet.
- F0 is a new edit beyond your snippet: L28 "has Weyl symbol equal to" becomes "is taken here to have Weyl symbol
  equal to". Check that it is consistent with the F1 sentence "Which of these charges … is not derived here".
- Re-run `moyal_K0_symbol_066.py`. It reproduces your Finding-3 computation exactly in d = 2.
- Do not assert that L28 is false. H_quad is undefined; the computation is conditional on the Moyal-element
  reading.
- The full scan is required before a plain ACCEPT, per your ruling. The orchestrator runs it separately.
- Integration ordinal: 64.

## Build result

r2 scratch build in a fresh directory outside the repo, with the r2-patched appH and bib (hashes b8155af3… and 4315a895… confirmed in the build copy). Sequence: pdflatex, bibtex, pdflatex, pdflatex. All exit codes 0; 0 bibtex warnings; 0 undefined or multiply-defined lines in the final log; `HislopLongo1982` present in the .bbl; 380 pages. Output in `scratch_build_066_r2_output.txt`. The build copy stays in the session scratchpad (no rm -rf was run).
