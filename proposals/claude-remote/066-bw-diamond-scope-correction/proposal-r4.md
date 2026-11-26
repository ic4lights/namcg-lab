# Proposal 066-bw-diamond-scope-correction, round 4

## Change list r3 → r4

| review-r3 finding | Severity | Action in r4 |
|---|---|---|
| 1. The General-sector sentence "It is the modular Hamiltonian of a causal diamond if and only if …" is stale after E1/F1. | major | New edit **F10**: the gatekeeper's snippet, applied verbatim to the r3 result. It is kept as a separate edit after F9 rather than folded into it, so F9 stays byte-identical. |

- F0–F9 and the bib edit F8 are unchanged byte for byte. `apply_check_066_r4.py` checks this by re-deriving the r1, r2 and r3 hashes in a chain.
- The orchestrator asked for one more read of the whole Problem A section. It found **two further sentences** that the corrections have made stale or overclaiming. They are **reported below with proposed replacements and not applied**, as instructed.

## Result

The result is unchanged from r1–r3, and the gatekeeper confirmed it.
- appH L30–31 is a prior-claim error: it misattributes the diamond modular result to Bisognano–Wichmann, a wedge theorem.
- It also overstates the range of that result to a sector that contains the massive radial mode m_σ.
- The geometric diamond result is Hislop–Longo's, and it holds for the free massless scalar.
- The K_0 symbol identification, the half-sided-inclusion step and the δΘ estimates are marked as not derived.

F10 turns the General-sector biconditional into a sufficient condition. That condition holds only in sectors whose diamond modular flow is known to be geometric. F10 asserts no non-geometricity. No label changes.

## Target and status

Unchanged. Problem A is OPEN, CRITICAL PATH for the matrix-derived label, and PROGRAMME-CONDITIONAL. The original target is in ch17 L377–392 (`ass:dictionary` with error control). This package is a correction plus scoping of evidence.

## Source reading

Digest + targeted reads.
- Read review-r3.md in full.
- Re-read the whole r3-patched Problem A section, L12–92 of the r3 result: Ledger label, Free/Poisson, General sector, Missing step.
- Baselines re-checked with sha256sum and in the script. They are unchanged:
  - appH: 624232 bytes, c2dac013…558b5c.
  - bib: 29781 bytes, 28fdd7f8…a64d.
- No full scan. The orchestrator runs it separately.

## Research and reasoning

There is no new mathematics. F10 records that matching the semi-classical symbol to the geometric vector field is known to be sufficient only where the diamond modular flow is geometric. Among free fields, that is the massless scalar (Hislop–Longo). The "only if" direction of the old biconditional presupposed geometricity, which is not established outside such sectors.

### Further stale sentences (reported only, not applied)

**S1. Free/Poisson paragraph, r4 result L40–43.**

Current text:
> Hence the charge is a vacuum modular Hamiltonian only where it coincides with one of these generators: the wedge boost charge, for the free theory, or the diamond conformal Killing charge, for its free massless scalar part.

- **Problem:** "only where" is a necessity claim.
- For a massive free field it states that the diamond conformal-Killing charge is *not* the diamond vacuum modular Hamiltonian. In other words, it asserts that the massive diamond modular flow is non-geometric.
- Every round has kept that claim out of the text ("no such geometric identification is used here"). F10 now makes the same distinction explicitly ("not known to suffice").
- So S1 is in mild tension with F10.
- This wording came from the r1-review snippet (F1). The fix is a two-word insertion.

Proposed replacement. OLD occurs once in the r4 result; checked with CRLF preserved.
```latex
mass \(m_\sigma\) of Section~\ref{sec:ch3-scales}. Hence the charge
is a vacuum modular Hamiltonian only where it coincides with one of
```
NEW:
```latex
mass \(m_\sigma\) of Section~\ref{sec:ch3-scales}. Hence the charge
is known to be a vacuum modular Hamiltonian only where it coincides with one of
```
Line lengths may be re-wrapped. The content change is the insertion of "known to be".

**S2. General sector, r4 result L70–72. This is pre-existing text that the corrections have made stale.**

Current text:
> That matching has not been performed for higher-order, interacting, or fluctuating-Θ terms and is not a routine specialisation of the free-field result.

- **Problem:** the sentence implies the matching *has* been performed for the quadratic terms.
- After F0/F1, the Weyl-symbol identification of K_0 is "not derived here" even in the quadratic sector.
- In addition, the Moyal-element reading of H_quad gives a dilatation weighting, not a boost or diamond charge (`moyal_K0_symbol_066.py`).

Proposed replacement. OLD occurs once in the r4 result.
```latex
That matching has
not been performed for higher-order, interacting, or fluctuating-\(\Theta\)
terms and is not a routine specialisation of the free-field result. The
```
NEW:
```latex
That matching has
not been performed, even in the quadratic sector (see above); for
higher-order, interacting, or fluctuating-\(\Theta\) terms it is not a
routine specialisation of the free-field result. The
```

**Checked and not stale:**
- **Ledger label:** consistent.
- **"(Moyal bracket reduces exactly … degree ≤ 2)":** true as background to the "taken here" premise.
- **"Mutual information follows from the Araki formula":** a general definition via Araki relative entropy, and conditional through F7.
- **The "free modular flow … only for its free massless scalar part" parenthetical:** correct. It concerns the free vacuum flow, which Hislop–Longo identify.
- **Missing step:** a target statement.
- **The section title "matrix-to-modular map":** this is the ch17/appH definitional item for the author and is not stale text.

## Claim classification

As in r3, with one change. For the general sector, "vector-field matching suffices for the diamond modular Hamiltonian" is now **conditional**. It is established only where the diamond modular flow is geometric (Hislop–Longo for the free massless scalar), and **unresolved** elsewhere. Non-geometricity of the massive diamond modular flow is **not claimed**. S1 would remove the remaining implicit claim of it.

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`

- Apply **F0–F9 exactly as in proposal-r3.md** (F0–F7 are listed in proposal-r2.md, F9 in proposal-r3.md).
- Then apply **F10**. F10's OLD text contains F9's NEW last line, so F10 must be applied after F9. Its OLD text occurs once in the r3 result.

**F10** (General sector). OLD:
```latex
candidate modular Hamiltonian. It is the
modular Hamiltonian of a causal diamond if and only if the
semi-classical symbol of \(K_0\) is shown to recover the geometric
boost/diamond vector field of the emergent geometry. That matching has
```
NEW:
```latex
candidate modular Hamiltonian. It would be the modular Hamiltonian of
a causal diamond if the semi-classical symbol of \(K_0\) were shown to
recover the geometric boost/diamond vector field of the emergent
geometry, in a sector whose diamond modular flow is known to be
geometric (for free fields, the massless scalar part cited above);
elsewhere that recovery is not known to suffice. That matching has
```

**Final appH result**
- 625774 bytes.
- sha256 `c5bf9be4f7c9b51218be4000dcdd5273ebf3cfa3e125d0a5fe90299e443075b3`.
- CRLF = LF = 3402. No bare LF, no BOM.
- The chain baseline → r1 (173ab97b…) → r2 (b8155af3…) → r3 (fa12e54a…) → F10 gives a byte-identical result to the direct sequence F0–F10.

### `bib/namcg.bib`

F8 is unchanged and adds `HislopLongo1982`.
- 30159 bytes.
- sha256 `4315a89553cb97405af89604f1e43c9e5e0237fa5b7be0439431d042677a6060`.
- CRLF = LF = 1006.

Labels and keys: F10 adds no `\ref` or `\cite`. Nothing new beyond r2.

## Verification scripts

- `apply_check_066_r4.py <repo> <outdir>` writes `apply_check_066_r4_output.txt`.
  - Report-only. It builds backslashes with `chr(92)` and asserts that the out-dir is outside the repo.
  - It checks the baselines, the r1/r2/r3 chain hashes, and that every OLD occurs exactly once before and every NEW exactly once after, for each edit. That covers r1 E1–E5/B1, r2 D0–D5, r3 D9, r4 D10, and the direct F0–F10 and F8.
  - It also checks that chain equals direct, CRLF only, and no BOM.
  - Result: ALL CHECKS PASS (25 edit checks).
  - Output directory: `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\out066r4`.
- The S1/S2 anchors were each checked to occur once in the r4 result, with an inline count reading under `newline=''`. They are not applied.
- Earlier-round scripts and outputs are kept unchanged: the `*.r1` files, `apply_check_066_r2.py`, `apply_check_066_r3.py`, the Moyal check and the lattice illustration.

## Decisions Taken

- **F10 applied verbatim as a separate edit after F9, not folded in.** This keeps F9 byte-identical to the already-reviewed r3 text and keeps the chain auditable. Rejected alternative: merging F9 and F10, which the review allowed but which would change F9's reviewed OLD/NEW pair.
- **S1 and S2 reported, not applied**, per the orchestrator's instruction to apply nothing beyond F10. I recommend applying both in round 5, or in the integrator's accepted text, if the gatekeeper agrees.
  - Both narrow claims toward what is established.
  - Neither adds physics or touches a label.
  - S1 removes an implicit non-geometricity claim that F10 itself avoids.

## Milestone assessment

M3: correction of a materially false prior claim (PRIOR-CLAIM-ERROR) in author-committed text from commit 6aa4490. The gatekeeper has confirmed it, provisional pending the full scan. It is not a breakthrough.

## Status-label recommendation

The critical-path set is A, B, C, D1, E, F, G-derived and N. No label is affected. Problem A stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

The ch17/appH Problem A definitional mismatch is carried as report only. The quotes are in proposal-r1.md.

## Author decision needed

Only the ch17/appH Problem A definitional mismatch. No edit is proposed.

## Remaining open step

Unchanged:
1. Define H_quad and find which charge K_0 equals.
2. The half-sided-inclusion step, in both sectors, with a specified cyclic and separating state.
3. The δΘ estimate in a specified norm.

Ranked avenues:
1. Wedge reformulation.
2. Operator-level K_0/H_quad, via in-core forks (i) and (iii).
3. The IR theory below m_σ.
4. Small-diamond error control.
5. Maxwell and fermion diamond results.

## Special instructions for the gatekeeper

- Verify that F10 matches your snippet verbatim and that F0–F9 and F8 are byte-identical to r3. The script checks the r3 chain hash `fa12e54a…`.
- Decide on S1 and S2. They are reported only and are not in the r4 result hash. If you require them, round 5 will add them verbatim.
- A full scan is still required before a plain ACCEPT.
- Integration ordinal: 64.

## Build result

The r4 scratch build ran in a fresh directory outside the repo, with the r4-patched appH and bib. Their hashes, c5bf9be4… and 4315a895…, were confirmed in the build copy. The sequence was pdflatex, bibtex, pdflatex, pdflatex.

- All exit codes were 0.
- bibtex reported 0 warnings.
- The final log has 0 undefined or multiply-defined lines.
- `HislopLongo1982` is present in the .bbl.
- The PDF has 380 pages.

The log is in `scratch_build_066_r4_output.txt`. The build copy remains in the session scratchpad, because no rm -rf was run.
