# Proposal 066-bw-diamond-scope-correction, round 3

## Change list r2 → r3

| review-r2 finding | Severity | Action in r3 |
|---|---|---|
| 1. General-sector sentence (baseline L42–45) is stale after F1. It also omits the state that any modular operator needs. | major | New edit **F9**: the gatekeeper's snippet, applied verbatim. |
| 2. Doubled "here" in F3 | minor, optional | **Not applied.** F3 is kept exactly as in r2. See Decisions Taken. |

F0–F8 are unchanged from r2, byte for byte. `apply_check_066_r3.py` checks this: it re-derives the r2 result hash
`b8155af3…` by the chain baseline → r1 → r2, then applies F9. r2 files are left in place, and the new script and
output have new names.

## Result

The result is unchanged from r2, which the gatekeeper confirmed.
- appH L30–31 is a prior-claim error. It misattributes the diamond modular result to Bisognano–Wichmann, which is
  a wedge theorem. It also extends the result to a sector containing the massive radial mode m_σ.
- The geometric diamond result is Hislop–Longo's, for the free massless scalar.
- The K_0 Weyl-symbol identification, the half-sided-inclusion step and the √δΘ estimates are marked "not
  derived".

F9 brings the General-sector paragraph into line with this. The half-sided-inclusion construction is now
conditional there too. The text also names the cyclic and separating state, which Tomita–Takesaki theory requires
for any modular operator; this is a standard prerequisite, not a new NAMCG assumption. "From matrix data alone" is
removed. No status, priority or completion label changes.

## Target and status

Unchanged. Problem A is OPEN, CRITICAL PATH for the matrix-derived label, and PROGRAMME-CONDITIONAL; appH L16–20
and ch17 L378 agree. The original target (ch17 L377–392) is `ass:dictionary`, with Hilbert space, Weyl map,
continuum limit and order-by-order error. This package is a correction plus a scoping of the evidence, not progress
on A.

## Source reading

Digest + targeted reads. I read review-r2.md in full. I re-read the baseline General-sector paragraph and the F9
result, at r3-patched L59–74.

The baselines were re-verified with sha256sum and inside the script:
- appH: 624232 bytes, c2dac013…558b5c;
- bib: 29781 bytes, 28fdd7f8…a64d.

The baselines are unchanged; the author's commit 6fb263e touched only the proposal folder. No full scan here; the
orchestrator runs it separately, per the gatekeeper's 3(b)/(c) ruling.

## Research and reasoning

See r1 §§1–5 and the r2 K_0 section; they are unchanged. F9 adds no new mathematics. It records two facts:
- the half-sided-inclusion step is not derived, here as in the free case (F1);
- a modular operator Δ of (𝓜, Ω) is defined only for a cyclic and separating vector Ω, through the closure of
  S: xΩ ↦ x*Ω, so algebraic matrix data alone do not fix it.

This applies the rule "a commutator-to-derivative identity does not determine the state, subsystem algebra, modular
Hamiltonian or MI" to the text.

## Claim classification

As in r2, with one addition. In the general sector, the existence of a half-sided inclusion and of its modular
operator is **unresolved**, now marked as such. The existence of the modular operator is conditional on a cyclic and
separating state, which is a standard **established** prerequisite.

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`

Apply **F0–F7 exactly as in proposal-r2.md**, unchanged, plus F9 below. F8 is the bib edit. All edits are in the
Problem A section. The "Ledger label." and "Missing step." paragraphs, the headings and all labels are untouched.

**F9** (General sector, baseline L43–45). The paragraph's first line, "For a non-quadratic Hamiltonian, or for a
slowly varying", is kept. So is everything from "modular Hamiltonian of a causal diamond if and only if …" on.

OLD:
```latex
\(\Theta=\Theta_0+\delta\Theta\), the same algebraic construction yields
a well-defined modular operator of a half-sided inclusion from matrix
data alone. That operator is a candidate modular Hamiltonian. It is the
```
NEW:
```latex
\(\Theta=\Theta_0+\delta\Theta\), the same algebraic construction would
yield, if it generates a half-sided inclusion (a step not derived here,
as in the free case) and given a cyclic and separating state, a
modular operator built from matrix data. That operator would be a
candidate modular Hamiltonian. It is the
```

Final appH result: 625606 bytes, sha256
`fa12e54a83a05061177e2289b83be59c1007118b57f3c799d9e8685049ce29f7`. CRLF = LF = 3400, no bare LF, no BOM. The
chain baseline → r1 (173ab97b…) → r2 (b8155af3…) → F9 is byte-identical to the direct list F0–F7 + F9.

### `bib/namcg.bib`

**F8** is unchanged from r1/r2. It adds `HislopLongo1982`. Result: 30159 bytes, sha256
`4315a89553cb97405af89604f1e43c9e5e0237fa5b7be0439431d042677a6060`, CRLF = LF = 1006.

### Labels, keys and stale passages

- No new labels or citations beyond r2.
- F9 adds no `\ref`.
- No further stale passages were found within Problem A. In the r3 result, "half-sided" occurs only twice: in F1
  (L47) and in F9 (L62), and both are conditional. The Missing-step paragraph refers to "the algebraic inclusion
  generated by K_0" as the object still to be identified. That states a missing step and is correct as written.

## Verification scripts

- `apply_check_066_r3.py <repo> <outdir>` writes `apply_check_066_r3_output.txt`. It runs in report-only mode, and
  it builds backslashes with `chr(92)`. It asserts that the out-dir is outside the repo. It checks:
  - the baseline hashes;
  - the r1 and r2 chain hashes;
  - each OLD string occurs exactly once before and each NEW string exactly once after, for every r1 edit, every r2
    delta, D9 (F9) and every direct edit F0–F9;
  - the chain result equals the direct result;
  - CRLF only and no BOM.

  It reports ALL CHECKS PASS. Output dir:
  `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\out066r3`.
- `moyal_K0_symbol_066.py` and `lattice_modular_profile_066.py`, with their outputs, are unchanged.
- The earlier rounds' scripts and outputs are kept, including the `*.r1` files and `apply_check_066_r2.py` with its
  output.

## Decisions Taken

- **F9 is applied verbatim** as the gatekeeper's snippet. It is required, and it favours the IR/full-GR route by
  stating precisely the missing ingredients of the general sector: the inclusion step and the state.
- **The optional F3 rewording is not applied.** F3 stays "which is not derived here (in a norm not specified
  here)". The gatekeeper judged it correct, and the orchestrator asked that F0–F8 stay unchanged. Changing F3 would
  reopen an already-accepted edit for a cosmetic gain only. Rejected alternative: "which is not derived here and
  whose norm is not specified".

## Milestone assessment

M3: correction of a materially false prior claim (PRIOR-CLAIM-ERROR) in author-committed text, from commit
6aa4490. The gatekeeper confirmed it, provisional pending the full scan. It is not a breakthrough.

## Status-label recommendation

The critical-path set is A, B, C, D1, E, F, G-derived and N. No label is affected. Problem A stays OPEN / CRITICAL
PATH / PROGRAMME-CONDITIONAL.

The report-only ch17/appH Problem A definitional mismatch is carried from r1, with the quotes and options there.
I recommend aligning appH with ch17. That is an author scope decision, and no edit is proposed.

## Author decision needed

Only the ch17/appH Problem A definitional mismatch. No edit is proposed.

## Remaining open step

Unchanged from r2:
- (1) define H_quad and determine which charge the K_0 symbol equals;
- (2) derive the half-sided-inclusion step, in the free and the general sectors, for a specified cyclic and
  separating state;
- (3) derive the δΘ estimate in a specified norm.

Ranked avenues: wedge reformulation; operator-level definition of K_0/H_quad (within-core forks (i) and (iii)); the
IR theory below m_σ; small-diamond error control; Maxwell/fermion diamond results.

## Special instructions for the gatekeeper

- Check that F9 matches your snippet verbatim, and that F0–F8 are byte-identical to r2. The script checks the r2
  chain hash `b8155af3…`.
- A full scan is still required before a plain ACCEPT; the orchestrator runs it.
- Integration ordinal: 64.

## Build result

r3 scratch build in a fresh directory outside the repo, using the r3-patched appH and bib. Their hashes, fa12e54a… and 4315a895…, were confirmed in the build copy. Sequence: pdflatex, bibtex, pdflatex, pdflatex.

- All exit codes 0.
- 0 bibtex warnings.
- 0 undefined or multiply-defined lines in the final log.
- `HislopLongo1982` is present in the .bbl.
- 380 pages.

The log is in `scratch_build_066_r3_output.txt`. The build copy stays in the session scratchpad, since no rm -rf was run.
