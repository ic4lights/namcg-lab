VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: flat | OPEN: 0/1

## Verdict
F10 is applied verbatim and closes the r3 finding. F0–F9 and the bib are unchanged. The researcher reported two further stale sentences, S1 and S2, without applying them, and both are valid.
- S1 is a necessity claim that my own r2 snippet introduced, and it is not established.
- S2 implies that the symbol matching was done in the quadratic sector.

Both need fixing before a plain ACCEPT. I have re-read all of Problem A, and nothing else remains: with S1 and S2 applied verbatim below and nothing else changed, the package is ready for a plain ACCEPT conditional on the full scan.

## Source reading
- Digest + targeted reads; this is not a full scan.
- `python scripts/make_digest.py --check` printed `DIGEST CURRENT`. HEAD is 3051c1d, and that commit touches only the proposal folder (4 files).
- `dirty-chapters: yes` reflects the uncommitted 064/065 changes to appH and bib, which is expected. The manuscript working tree still matches the baselines.
- I read in full the r4-patched Problem A section (L12–96): Ledger label, Free/Poisson, General sector and Missing step. I also read the r3→r4 diff and the r4 build log.
- Scan ruling is unchanged: CLAUDE.md 3(b) and 3(c) both require a full scan before any plain ACCEPT or integration. I did not perform one.

## Claim under review
- The package is unchanged from r1–r3. It corrects appH L30–31: Bisognano–Wichmann (BW) is a wedge result, and the diamond result is Hislop–Longo's, for the free massless scalar.
- It marks as not derived:
  - the K_0 symbol identification;
  - the half-sided-inclusion step;
  - the cyclic and separating state;
  - the √δΘ estimates.
- The lemma and the General-sector diamond claim become conditional.
- Original target (ch17 L377–392): Assumption `ass:dictionary`, with Hilbert space, Weyl map, continuum limit, and error at each order in Θ.
- Current status, verbatim from appH L16–20: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. The general matrix-to-modular map remains unproved. A scope-limited Presentation-B model may retain Assumption~\ref{ass:dictionary} and claims no derivation from the matrix model." The package changes no label.

## Checks performed
- **apply_check_066_r4.py**, re-run report-only into `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk066r4`: ALL CHECKS PASS.
  - Baselines match.
  - The baseline→r1→r2→r3 chain reproduces every earlier hash.
  - F0–F10 each find their OLD text once and their NEW text once afterwards.
  - The chain result equals the direct application.
  - appH: 625774 B, c5bf9be4f7c9b51218be4000dcdd5273ebf3cfa3e125d0a5fe90299e443075b3 (also confirmed with my own `sha256sum`), CRLF = LF = 3402, no bare LF, no BOM.
  - bib: 30159 B, 4315a895…6060, CRLF = LF = 1006.
- **My r3→r4 diff:** a single hunk at L65–70, which is F10 exactly as in my r3 snippet. `cmp` shows the bib is identical to r3.
- **Build log** (the researcher's; I did not re-run it): all steps exit 0, no undefined or multiply-defined references, `HislopLongo1982` is in the .bbl, 380 pages.
- **Anchors for S1 and S2:** each OLD below occurs exactly once in the r4 result. The S1 text comes from the F1 NEW lines; the S2 text comes from F10's last line plus two baseline lines.
- **Full re-read of Problem A**, sentence by sentence:
  - Ledger label: consistent.
  - F0: "is taken here …". The parenthetical "Moyal = Poisson for degree ≤ 2" is a correct standard fact: the Moyal series truncates when one argument is at most quadratic.
  - BW sentence: correct. "For free fields with or without mass" is narrower than BW's actual range but not false.
  - Hislop–Longo sentence: correct.
  - "Hence … only where …": stale, see S1.
  - The not-derived sentences and the conditional lemma: consistent.
  - F2 and F7: consistent.
  - F9 and F10: consistent.
  - "That matching has not been performed for …": stale, see S2.
  - The estimate display and F4/F5: consistent. "Free modular flow … identified with the diamond … only for its free massless scalar part" refers to the vacuum flow of the free theory, which Hislop–Longo identify.
  - Missing step: a target statement, so consistent.
  - Nothing else is stale.

## Findings
1. **Major. S1, Free/Poisson paragraph, r4 L39–40.**
   - Text: "Hence the charge is a vacuum modular Hamiltonian only where it coincides with one of these generators".
   - Finding: this asserts a necessary condition, namely that a charge which is a vacuum modular Hamiltonian must coincide with the wedge boost charge or the diamond conformal Killing charge. That is not established. For a massive or otherwise non-conformal diamond, H_D exists but no geometric form is known. K_0 could in principle equal it without matching either generator. The sentence therefore implicitly asserts non-geometric massive flow, which the package must not claim.
   - Origin: my r2 snippet. This is a reviewer error, not the researcher's.
   - Required action: insert "known to be", as the researcher proposed; exact text below.
2. **Minor, required. S2, General sector, r4 L70–72 (pre-existing).**
   - Text: "That matching has not been performed for higher-order, interacting, or fluctuating-\(\Theta\) terms and is not a routine specialisation of the free-field result."
   - Finding: by listing only those cases, the sentence implies that the matching was performed in the quadratic sector. F0/F1 now say the Weyl-symbol identification is not derived even there. The phrase "the free-field result" also refers to a result that is now conditional.
   - Required action: use the exact text below. It follows the researcher's proposal, but replaces "(see above)" with an explicit pointer and "result" with "case".

No other findings. All findings from r1 (1–6), r2 (1) and r3 (1) are closed and re-verified.

## Scope of what is established
Unchanged.
- **Established (correction; PRIOR-CLAIM-ERROR confirmed; M3, provisional until the full scan):**
  - The L30–31 sentence misattributes the diamond result to BW and overstates its range.
  - BW gives the wedge result for any mass.
  - Hislop–Longo give the geometric diamond modular group of the free massless scalar.
- **Conditional computation:** under the Moyal-element reading of H_quad, K_0 carries the dilatation weighting (i/2)x·∂h.
- **Unresolved, and now marked as such:** the K_0 symbol identification; the half-sided-inclusion step; the state; the δΘ estimates; and sufficiency of vector-field matching outside sectors known to have a geometric diamond modular flow.
- **Not claimed:** that massive diamond modular flow is non-geometric. S1 enforces this.
- Problem A stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
- **Ranked avenues** (unchanged):
  1. wedge reformulation;
  2. an operator-level definition of H_quad, then redo the K_0 symbol computation via forks (i) or (iii);
  3. the IR theory below m_σ;
  4. small-diamond error control;
  5. Maxwell and fermion diamond results.
- **Author item (report only):** the ch17/appH Problem A definitional mismatch.

## Recommended disposition
Revise (r5): apply S1 and S2 verbatim, keep F0–F10 and the bib unchanged, and re-run apply_check and the scratch build. Problem A has now been fully re-read, and I find nothing further. If r5 applies exactly S1 and S2, I will issue a plain ACCEPT conditional on the full scan.

**PROGRESS** is rated "flat" strictly by count: one major closed (r3 F10), one major opened (S1). S1 came from my own r2 snippet. The researcher closed every earlier finding, opened none, and found S1 and S2 independently. The remaining work is two fully specified verbatim substitutions. If the stop rule is triggered, I recommend the orchestrator's digest tell the author that the item is mechanically one step from ACCEPT.

## Corrected snippet
Neither change adds new physics or new assumptions. Apply both to the r4 result, keeping CRLF line endings.

**S1** (Free/Poisson):

OLD:
```latex
mass \(m_\sigma\) of Section~\ref{sec:ch3-scales}. Hence the charge
is a vacuum modular Hamiltonian only where it coincides with one of
```
NEW:
```latex
mass \(m_\sigma\) of Section~\ref{sec:ch3-scales}. Hence the charge
is known to be a vacuum modular Hamiltonian only where it coincides
with one of
```

**S2** (General sector):

OLD:
```latex
elsewhere that recovery is not known to suffice. That matching has
not been performed for higher-order, interacting, or fluctuating-\(\Theta\)
terms and is not a routine specialisation of the free-field result. The
```
NEW:
```latex
elsewhere that recovery is not known to suffice. That matching has
not been performed, even in the quadratic sector, where the Weyl-symbol
identification above is not derived; for higher-order, interacting, or
fluctuating-\(\Theta\) terms it would not be a routine specialisation of
the free-field case. The
```

Relevant paths:
- C:\Users\redgi\Projects\namcg-lab\proposals\066-bw-diamond-scope-correction\proposal-r4.md
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (Problem A, baseline L12–70)
- C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk066r4\ (r4-patched copies)

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: flat | OPEN: 0/1
