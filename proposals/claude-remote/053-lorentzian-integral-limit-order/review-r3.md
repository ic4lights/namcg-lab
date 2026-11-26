VERDICT: ACCEPT | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/0

## Verdict
The insert is exactly r2 plus S7, S7 is correct in context, and both anchors are unique on the new baseline. The expected output bytes, the copy build and the record all check out. On my ruling below, the scan requirement is met. No byte needs to change.

## Scan ruling
**Ruling: the scan requirement under CLAUDE.md 3(b) (M3) and 3(c) (E1 changes a scope sentence) is met. It rests on the ordinal-50 full-scan record plus a byte-verified, fully read delta. I did not do a full scan and claim none.**

The basis, all recomputed by me:
- **Scanned state is unchanged in the chapters.** `git diff 46cf967 d3e4cb7 -- chapters bib` is empty, so the chapter bytes behind review-r1 and review-r2 equal d3e4cb7.
- **Only appH changed in the chapters.** `git diff --stat d3e4cb7 HEAD -- chapters bib` touches only `appH-microscopic-proofs.tex` and `namcg.bib`. The other 29 chapter files are unchanged, and the tree is clean.
- **The appH changes are exactly two.** My difflib comparison of the d3e4cb7 appH blob with the working appH gives:
  - three replace hunks at d3 L17-18, L22-31 and L34-39 (working L17-18, L22-61 and L64-70), all inside Problem A;
  - one insert hunk at d3 L1423 (working L1454-1480), which is the 052 block.
- **The 052 block is byte-identical to the reviewed one.** I applied only the insert hunk to d3e4cb7 and converted to CRLF. The result is 519811 bytes, sha256 `f3d20921...1285`. That is the input of review-r2, which review-r1 tied to the ordinal-50 scan (content-hash 717cadc85cf88f78).
- **Digest.** `make_digest --check` prints DIGEST CURRENT, `dirty-chapters: no`, chapters-hash `060976c0e8e7218c`. So 3(d) does not apply.
- **Ordinal.** By the ledger, ordinal 50 was 052, so this item is ordinal 51. It is not a 5th item.

What I read for the delta:
- the whole Problem A hunk (appH L12-71);
- appH L1-11;
- every chapter line that cites Problem A, `sec:status-A` or `ass:dictionary`, found by grep: ch03 L237, L340-412 (the assumption and rem:ch3-moyal-check), L543, L602, L848; ch06 L62-70, L130, L198, L205, L384; ch07 L280; ch16 L32, L86, L121, L131, L308, L356; ch17 L100, L128, L370-392, L660-712; ch18 L40-66; appB L110-150 (BW section).

The Problem A text cites none of this package's labels (`ass:lorentzian`, `eq:Smatrix`, `sec:status-E`) or keys. It says nothing on signature, contours or the Lorentzian integral, so E1 and E2 cannot go stale against it. This ruling does not lapse unless a chapter byte outside these two verified changes differs at integration. The integrator's input-hash check enforces that.

## Source reading
Digest + targeted reads, with the scan record above. Not a full scan. No unreadable files.

Also read:
- appH L1482-1497 (all of Problem E);
- ch17 L394-399;
- the S7 paragraph in context (insert L2, L4, L6, L10, L14);
- review-r1 (scan section), review-r2 in full, proposal-r3 in full;
- `apply_check.py` head;
- ledger ordinals.

## Claim under review
- **Target:** Problem E, derive Lorentzian signature. Appendix H verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature." Status paragraph: "Remains Assumption~\ref{ass:lorentzian}." Ch17: "OPEN; CRITICAL PATH for the matrix-derived label."
- **Package:** unchanged from r2 apart from S7. It is a PROGRAMME-CONDITIONAL sharpening and does not derive the target.

## Checks performed
My own script is `gk53r3/bytes.py` in the scratchpad. It parses review-r2 raw and reads the `apply_check.py` literals by AST, without executing them.

1. **S7 bytes.**
   - The S7 old string is 195 bytes and the new string is 316 bytes. Both hashes match review-r2.
   - The old string occurs once in `appH_insert.r2.tex` (10645 bytes, `5d0d4538...3aef`).
   - r2 with S7 applied equals `appH_insert.tex` exactly: 10766 bytes LF, `e5562f76...d15009`, ASCII, 0 CR. The CRLF form is 10783 bytes, `bab65e95...4285`.
   - `diff` shows only line 14, inside the S7 span.
2. **S7 in context.**
   - **mu range.** The insert's R_1 is A_0 = e^{-3 pi i/8} At_0 and A_i = e^{pi i/8} At_i. With A_mu = e^{pi i/8} At_mu for mu = 1..d+1, the model's A_0 = -i A_{d+1} gives e^{-3 pi i/8} At_{d+1}, which is R_1 with At_{d+1} = At_0. My sympy check: difference 0, and the old mu = 0 reading is off by a ratio of i. `s7_check_r3.py` agrees.
   - **p = 4.** "for p=4, the Pfaffian there" matches the limit display at insert L10, Pf M(-i At_0, At_i) on R_1, and the bosonic-only identification with 2501.17798 is now restricted to p = 0.
   - G1 and G2 are closed.
3. **Re-anchoring.** OLD (337 bytes, `145590c5...`), NEW (653 bytes, `7f9d628d...`) and ANCHOR (61 bytes, `a7c77412...`) are byte-equal to `apply_check.r2.py`.
   - In appH `c0f9462f...6bba777` (521477 bytes, CRLF 3186, 0 bare LF), E1 old occurs once at L1478 and the anchor once at L1495.
   - The NEW text and the insert are not already present.
   - **My outputs:**

     | File | Size | sha256 | CRLF | Bare LF |
     |---|---|---|---|---|
     | appH | 532576 | `7a75554e...6aaa` | 3203 | 0 |
     | bib | 25976 | `a651fe60...c42b` | 867 | 0 |

     Both equal the expected values. The bib input is `09ac48a5...a3aa`, 24258 bytes, the same as in r2.
   - The researcher's `apply_check_r3_copy.out` agrees.
4. **Build.**
   - I copied all tracked files into the scratchpad `gk53r3/tree` and installed my two outputs there.
   - pdflatex, bibtex, pdflatex, pdflatex: all exit 0. 357 pages, 0 undefined, 0 multiply defined, 0 BibTeX warnings, no rerun warning on the last pass.
   - All four new keys are in the `.bbl` and `.aux`.
   - No trailing whitespace in the insert or the bib additions.
   - The repository afterwards: hashes unchanged, HEAD `567c0c4`, `git status` clean.
5. **Record.** proposal-r3 covers everything review-r2 asked for:
   - S7 and its hashes;
   - a note on the digest regeneration, with the staleness resolved (L28-29);
   - new expected values, plus an `EXPECT` table that enforces the input-hash precondition;
   - the new output file `apply_check_r3.out` in place of the regenerated r2 one, which is acceptable on the new baseline.

   It adds no mathematical claim. The two new rows (052 block identical; the Problem A edits do not bear on this package) are verified above.
6. **Other checks.**
   - No labels changed. `ass:lorentzian`, `eq:Smatrix` and `sec:status-E` are each defined once.
   - Problem E stays OPEN, with one scoped closing status sentence ("Problem~E remains open and PROGRAMME-CONDITIONAL.").
   - Assumption ass:lorentzian stands.
   - Emergence is kept: eta on matrix indices is a retained input, and no metric is made fundamental.
   - No process language.
   - I did not run `apply_s7_r3.py`, `apply_check.py` or the numerics scripts. Their mathematics was verified in r1 and r2 and is unchanged.

## Findings
None. G1 and G2 from review-r2 are closed by S7. F1-F6 were closed earlier.

## For the author: Problem A edits (not findings against this package; no edits proposed)
- **A1.** The text says "By the Bisognano–Wichmann theorem this charge is the modular Hamiltonian of the causal diamond of the free theory". BW covers wedges, and appB L144 says "exact for free fields in Rindler space". A geometric modular flow for diamonds is a conformal (massless) result, not a general free-field one. As written the attribution is broader than the theorem. Not independently checked against the literature here.
- **A2.** The paragraph headed "(lemma)" has no derivation or citation in the passage, and the bound O(R sqrt||delta Theta||) has no source there. Compare appH L4-6 ("does not convert any open problem into a lemma"). The label is still OPEN, so there is no status-label conflict.
- **A3.** "already noted above" now has no antecedent, because the deleted paragraph (the reference to rem:ch3-moyal-check) was what it pointed to. The new text no longer mentions the metric-matching obstruction for real constant Theta (ch03 L400ff) while claiming exactness at constant Theta.
- **A4.** K_0 is defined with tr(...). As written that is a scalar, not an operator, unless tr means a partial trace.
- **A5.** The text uses a Unicode en dash; the manuscript convention is `--` (appB L117).
- **Chapter 17.** The status label and missing step still say OPEN and retain ass:dictionary. This is consistent with ch17 L377-391 and criterion item 1 (L701), and the sector statement does not claim to meet item 1.

## Scope of what is established
- **Proved at N = 2:**
  - the eps -> 0 limit, with rate;
  - Pf = c_P (det G)^4 and the Cauchy-Binet bound;
  - k < 14 sharp for the modulus;
  - regulator independence and SO(9,1) invariance of the limit;
  - the gamma statements;
  - Definition C equality for gamma <= 0, with a convergence factor removed last and a non-vanishing partition function, for invariant O. The weight is e^{-S_E}, with the Pfaffian on R_1 for p = 4; for p = 0 this is the CNT model under the rotation for mu = 1..d+1.
- **Proved at any N:** the fixed-eps contour identity for u < 2/3, and non-integrability on R_1 at fixed eps.
- **Conditional for N >= 3:** the same limit and corollaries, on Lemma D and on Z_E != 0 for ratios.
- **Numerical:** the tables and the S4 checks.
- **Unresolved:** the gap with the 2501.17798 plots; Definition C at N >= 3.
- **Classification:** PROGRAMME-CONDITIONAL. Problem E is still OPEN. No signature is derived, and ass:lorentzian is not discharged. Not stated: N -> infinity first, fixed gamma > 0, degree >= 14 beyond the numerics, non-polynomial O, C_{mu nu lambda} != 0, a fermion mass.
- **PRIOR-CLAIM-ERROR, narrow:** the 052 sentence is overbroad. Its first clause is false in the limit (proved at N = 2, conditional for N >= 3), and its second is unsupported. E1 corrects it, and M3 applies. Under the directive this does not stop integration. Not a breakthrough.

**Obstruction classes (bounded):**
- *Limit class:* traceless SU(N) at finite N; IKKT content supplied; eq:Smatrix with C = 0 and no matter; polynomial O of degree < 14; a positive definite quadratic regulator; eps -> 0 first; gamma <= 0, or gamma -> 0 with gamma/eps bounded.
- *Definition C class:* N = 2, d >= 4, invariant O, gamma <= 0, a convergence factor.

**Open avenues, ranked:**
1. Non-polynomial observables at N = 2 (Tr e^{ik.A}, timelike k first).
2. N -> infinity taken first, starting from a controllable model.
3. C_{mu nu lambda} != 0.
4. Fixed gamma > 0 at N = 2. This is a deformation, so rule 3 scopes it.
5. Definition C at N >= 3, and the gap with 2501.17798.

A fermion mass is also open, as a deformation.

## Recommended disposition
Integrate as-is. The specification is the one in review-r2, with the r3 hashes:
- **appH.**
  - Require input 521477 bytes, `c0f9462fd2c6daf7e1b085250ea9f4bc7d45f605b93afc21857950bb796ba777`.
  - E1: replace OLD with NEW in place, once, at L1478.
  - E2: insert the CRLF form of `appH_insert.tex` (10783 bytes, `bab65e95...4285`) immediately before `\paragraph{Status.}\r\nRemains Assumption~\ref{ass:lorentzian}.`, which occurs once, at L1495.
  - Output: 532576 bytes, `7a75554ef8cb7efe0e4c5cd3c53d6a9c4ffd2a9149e6ff29c7e8e067bb7f6aaa`.
- **bib.**
  - Require input 24258 bytes, `09ac48a5a1157723a766f1aa118081b1c3f5ec4c928158ba3d0c43a80a90a3aa`.
  - Append `\r\n` and then the CRLF form of `bib_additions.bib` (1716 bytes, `981eb00f...f458`).
  - Output: 25976 bytes, `a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b`.
- **Both:** 0 bare LF afterwards. Do not re-normalise anything else. Stop if either input hash differs.

## Corrected snippet
None needed.

Process: all tool calls were serial, no background job was started, and nothing was written in the repository. Scratch files are in C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk53r3. The build tree is C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk53r3\tree.

Relevant files:
- C:\Users\redgi\Projects\namcg-lab\proposals\053-lorentzian-integral-limit-order\proposal-r3.md
- C:\Users\redgi\Projects\namcg-lab\proposals\053-lorentzian-integral-limit-order\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\053-lorentzian-integral-limit-order\apply_check.py
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex
- C:\Users\redgi\Projects\namcg-lab\bib\namcg.bib
