VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
The r2 insert is exactly the r1 insert with the seven required replacements F1–F7 applied verbatim and nothing else changed. I re-checked every changed claim and it holds, and the r1 core mathematics was already verified, so the package can be integrated as a bounded no-go plus an N=2 pointwise lemma. No label changes.

## Source reading
- **Digest + targeted reads. Not a full scan.**
- `make_digest.py --check` printed DIGEST CURRENT at HEAD 87e35d9. `git status --short` is clean.
- appH is still 540605 bytes, sha256 e67297cd3066e3f4795ed81875d5075dfec3fe98ba5a8d8feb0bfcb733e134d7, so it is byte-identical to the file I read in r1. My r1 full reads still apply:
  - appH L1480–1534: the Problem E ledger label, the 053 and 054 blocks, and the Status paragraph;
  - ch17 L394–399 and L710–726;
  - ch04 L316–334 (`ass:lorentzian`, defined once at L322).
- This round I also read in full: `proposal-r2.md` (by diff against r1), `appH_insert.tex` (r2), `appH_insert.r1.tex`, `apply_r2_edits.txt` and `apply_check.txt`.
- **Scan ruling:**
  - CLAUDE.md 3(b) asks for a full scan before a milestone verdict that triggers a milestone digest. Under the author's directive M2 is non-stopping and triggers no milestone digest, so 3(b) is not triggered.
  - 3(c) does not apply: no definition, assumption, scope or status passage changes, and `\mathfrak C` is a new local symbol with no clash in `chapters/`.
  - 3(d) does not apply: the digest is current and the chapters are clean.
  - Ordinal 53 is not a 5th-item scan; that one is due at 55.
  - So this ACCEPT carrying M2 rests on digest + targeted reads. No full scan was done and none is claimed.

## Claim under review
- **Problem E.** Appendix H, verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature." Chapter 17, verbatim: "OPEN; CRITICAL PATH for the matrix-derived label." The two agree.
- **Original target:** derive Lorentzian signature rather than retain `ass:lorentzian`.
- **The package's claim.** It applies to linear contours A=ΛX with Λ∈GL(10,C), Definition (A), γ=0 and ε→0 taken first at fixed N.
  - The damping set is C=C_0∪(−C_0).
  - No path of contours with h in the closure of C joins the two classes.
  - Bounded Fourier modes with h∈C_0 have k·k in the 054 sector at every N.
  - At N=2: V=F_E(e^{iπ/4}q^Th^{-1}q) on C_0, and the pointwise limit F_E(e^{iπ/4}k·k) exists for every real spacelike k.
  - Contours with h in −C_0 reach real timelike k but are not joined to the Hermitian contour.

## Checks performed
- **Diff r1 → r2 of the insert.**
  - My script (scratchpad `r2chk.py`) applies the exact r1 replacement strings for F1–F7 to `appH_insert.r1.tex`. Each old string occurs once, and the result is byte-identical to the r2 `appH_insert.tex`: 9880 bytes, sha256 348d7656781e69f871e3a8fa95efc24343d2f4c4714303b5c2d022b13fc0cbbe.
  - Nothing else in the insert changed. It is ASCII with LF only, and "ledger label" no longer occurs.
  - `apply_r2_edits.txt` agrees: each old and new string has count 1.
- **apply_check.py**, re-run in report mode, gives output identical to `apply_check.txt`:
  - baseline 540605 bytes, e67297cd…34d7;
  - anchor 61 bytes, count 1, line 1529;
  - insert CRLF form 9901 bytes, 4b16928cf1f2425981bd829a293c02d5918a3d0a9221e0bd9d6f3ef5a57cb15d;
  - result 550508 bytes, 01a3bf55a888ea30f4f3182358877b4ba6db5ac6237f2b7fff7e06093277d7a9, CRLF 3242, bare LF 0.
  - These match the coordinator's claimed hashes.
- **F1 (normalisation and the Step 5 ratio), re-derived.**
  - W(h,0) contains Tr 1=2, while F_E(0)=2 because F_E is normalised by the partition function without the trace.
  - So V=2W(h,q)/W(h,0) gives V(e^{iπ/4}I,q)=⟨Tr e^{iq·X}⟩_E=F_E(|q|²), as required.
  - In (v), I_ε[Tr e^{ik·A}] tends to c·W(h(1),q) and I_ε[1] tends to c·W(h(1),0)/2, with the same constant c=c_P det Λ(1)^3. The ratio is 2W/W(h,0)=V, as in proposal Step 5 r2.
  - W(·,0)≠0 on C_0 is unaffected.
  - `mc_check.py` already used this normalisation (mean(w·O)/mean(w)), so no number changes.
- **F2.** The closing statement is now restricted to h∈C_0. That is consistent with (iv), where −C_0 gives F_E(−e^{iπ/4}k·k).
- **F3 (the −C_0 example), re-derived.**
  - Λ=diag(1, e^{2πi/3}) gives h=diag(−1, e^{4πi/3}). Then −h=diag(1, e^{iπ/3}), with phases 0 and π/3 and pair sums π/3 and 2π/3, which lie in (0,π). So h∈−C_0.
  - The damping is Im(h_00h_ii)=sin(π/3)>0 and Im(h_iih_jj)=sin(2π/3)>0.
  - For k=κδ_0 the vector q=(κ,0,…) is real and the mode is bounded. Then q^Th^{-1}q=−κ², and V=F_E(−e^{iπ/4}(−κ²))=F_E(e^{iπ/4}κ²).
  - The Hermitian contour has h=Λ(0)^TηΛ(0) with Λ(0) real. Its Re h has 9 positive eigenvalues, so it lies in the closure of C_0 and not of −C_0. By (ii), no path with h in the closure of C joins the two.
  - The proposal's Result item 2 now matches.
- **F4.** The third-index argument is the one I verified in r1: β'_max<π, β'_min>−π/2 and a spread below π. It gives arg(k·k)∈(−π,π/2) and k·k≠0.
- **F5.** The closing sentence no longer repeats 054's "Problem~E keeps its ledger label". It is one scoped sentence.
- **F6.** "zero components of T^{-T}q" is the correct object.
- **F7.** The piecewise C¹ requirement suits Stokes' theorem, and the explicit path in (v) is smooth.
- **Core results.** These are unchanged from r1, where I verified them by hand, by my own script and by re-running `lemma_checks` and `path_check`. They are not repeated here:
  - Step 0;
  - Lemma 1, including the n≥3 requirement and the n=2 counterexample;
  - Lemma 2;
  - Step 3 at every N via C^(N)⊂C;
  - the Step 4 identity theorem;
  - the Step 5 construction, including my own boosted-k check (min eig Re Λ^TΛ>0 for small u).
- **Other.**
  - The scratch build (361 pages, 0 undefined references, 0 multiply defined labels) is reported by the researcher. I did not rebuild; the build is the integrator's step.
  - No citations were added. Finsler, Calabi and Brickman remain absent from the insert and are marked "not independently verified" in the proposal.
  - There is no process language, and the only reference is `\ref{ass:lorentzian}`, which exists.

## Findings
none. Each r1 finding is re-verified and closed:
- F1 (major), normalisation: closed.
- F2 (major), −C_0 overstatement: closed.
- F3–F7 (minor): closed.

## Scope of what is established
- **Exact:**
  - S_b=σ_2(X^ThX)/4g² at N=2;
  - damping ⇔ (P) at N=2, and C^(N)⊂C;
  - the normal form C=C_0∪(−C_0) (n≥3);
  - disjoint closures on invertible h;
  - the η-adjacent class is C_0.
- **Bounded no-go (every N).** Its hypothesis class is linear contours A=ΛX with Λ∈GL(10,C), the damping condition Re iS_b≤−cS_E, h∈C_0 and a bounded mode Tr e^{ik·A}. Then k·k lies in (−π,π/2), so real causal k≠0 is unreachable.
  - This is not a statement about all linear contours: −C_0 contours reach real timelike k with value F_E(e^{iπ/4}κ²), but they are disconnected from the Hermitian contour within the closure of C.
- **Proved at N=2** (using 053's N=2 flat-direction bound and 054 (iv)):
  - the value formula on C_0;
  - the pointwise ε→0 limit for every real spacelike k, independent of the regulator and of boosts.
- **Classification:** a PROGRAMME-CONDITIONAL sharpening and an M2 bounded no-go that settles 054's open "off-axis / index-mixing" route for linear contours. It is not a BREAKTHROUGH: η is put into S_b by hand and no signature is derived. Problem E stays OPEN, CRITICAL PATH for the matrix-derived label, PROGRAMME-CONDITIONAL.
- **Open relaxations, ranked by promise:**
  1. Paths that keep Re iS_b≤0 but leave the closure of C. Real h of any signature has Re iS_b=0, so the admissible set is strictly larger. Since −C_0 already reaches real timelike k, a regulator-admissible path from the Hermitian contour to −C_0 is the sharpest open question.
  2. Non-linear (thimble) contours at real causal k, N=2.
  3. Direct oscillatory analysis of the real timelike or null pointwise limit at N=2. The Step 6.4 power count is heuristic only.
  4. N→∞ taken first.
  5. (iv) and (v) at N≥3, which needs an independent general-h version of 053's bound.
  6. γ≠0 and Definitions (B) and (C).
  7. Osterwalder–Schrader (OS) reflection positivity.

  None of these derives signature while η is an input.

## Recommended disposition
Integrate as-is:
- insert the CRLF form of `C:\Users\redgi\Projects\namcg-lab\proposals\055-index-mixing-contours\appH_insert.tex` immediately before the unique anchor at appH L1529, followed by one blank line;
- expected result: 550508 bytes, 01a3bf55a888ea30f4f3182358877b4ba6db5ac6237f2b7fff7e06093277d7a9;
- then run `python scripts/build_check.py`.

The ledger entry should record that this M2 ACCEPT rests on digest + targeted reads, under the 3(b) ruling above, and that the ordinal-55 full scan is still due.

## Corrected snippet
None needed.

VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0
