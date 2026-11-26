## Scan note, pass 2 of 5 (ordinal-55 full scan, CLAUDE.md 3(a))

**File.** `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex`, working tree. The size is 561466 bytes and the sha256 is ea5c753b0f01a3a92e426435f747fa464521980f609ab330f4a432868daba1f5, so both are confirmed. The file has 3255 lines.

**Range read.** I read every line of L1101–2200 in consecutive chunks: 1101–1200, 1201–1350, 1351–1481, 1482–1526, 1527–1571, 1567–1686, 1687–1846, 1847–2026 and 2027–2200. Problem E (L1482–1566) I read line by line. I also read `C:\Users\redgi\Projects\namcg-lab\proposals\057-mass-plane-class\appH_insert.tex` in full first.

**Supporting checks (read-only).**
- No `\label` is duplicated across `chapters/**/*.tex`.
- `ass:lorentzian` is defined once (ch04 L322).
- `\mathfrak C` and `M_\gamma` occur only in Problem E (L1530–1562).
- ch17 L394–399 for Problem E reads "OPEN; CRITICAL PATH for the matrix-derived label". This agrees with appH L1486–1489 ("Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL.").

### Findings

**1. The 057 cross-references resolve once the insert sits immediately before L1564.**
- "two preceding paragraphs" means L1551 (regulator fixes the class) and L1529 (linear contours that mix the indices). Both use Definition (A), and L1554 introduces the mass term and M_γ. Resolves.
- "(i) of the preceding paragraph" means L1554. It defines ε+iγ' = |·|e^{iφ}, ℓ = a+ib, the identity (ε+iγ')h = M_γ − 2εℓℓ^T, the contour A_0 = e^{iπ/8}X_0, A_i = e^{−3πi/8}X_i, and the inertia argument for γ ≤ 0. Resolves.
- "(ii) of the paragraph on linear contours that mix the indices" means L1538: at most one β outside (−π/2, π/2) and at most one outside (0, π), so at least eight β lie in (0, π/2). L1554 cites the same fact the same way. Resolves.
- The cited 053 sentence is L1502: "For fixed γ>0 the admissible u closes like ε/γ as ε→0, and nothing is stated." Resolves.
- 057's closing reference to "the paragraph on the regulated Lorentzian integral" for γ→0 first, or γ/ε bounded, matches L1502 ("also holds for γ→0 with γ/ε bounded above").
- 057's "conditions used for the Stokes arguments above" matches the path hypotheses of L1558 (iii).

**2. Nothing in 053–056 becomes stale or false once 057 follows.** Each "no statement about fixed γ>0" line is a local scope disclaimer for its own paragraph, and 057 also decides no limit at fixed γ>0 ("not decided"). The lines checked:
- L1478 ("for a fixed positive mass, no such relation is stated")
- L1502
- L1508 (Definition (C), γ>0 not treated; 057 also excludes (C))
- L1510
- L1527
- L1549
- L1554 ("For fixed γ>0 it fails"). This refers to the inertia argument. 057 keeps that contour and only shows it is not path-connected, so there is no conflict.
- L1562

None of these conflicts with the signature (−,+,+,+) / η = diag(−1,1,…,1), Definitions (A)/(B)/(C), the contours R_u, the mass term S_γ with γ' = γ/2g², the Wick rotation, or `ass:lorentzian`. I spot-checked 057 (i): sin(Θ−2φ) ≥ 0 with Θ ∈ (−π, π) and 2φ ∈ (0, π) gives Θ ∈ [2φ, π) or Θ ∈ (−π, 2φ−π]. That is correct. For φ ≤ 0 the lower interval is empty, also correct.
- Severity: note.

**3. Status lines are consistent.**
- E: L1486–1489, L1510, L1527, the L1564–1565 Status paragraph ("Remains Assumption~\ref{ass:lorentzian}") and 057's closing sentence all agree with ch17.
- F: L1571–1574 ("Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL…") agrees with ch17 L403 ("CRITICAL PATH; OPEN").
- The "Problems … remain open (and PROGRAMME-CONDITIONAL)" closers at L1161, 1214, 1256, 1310, 1375, 1414, 1453, 1480, 1652, 1694, 1752, 1780, 1821, 1896, 1934 and 2112 make no closure claim and change no label.
- Severity: none.

**4. Symbol reuse (minor or note; locally defined, no ambiguity in context).**
- Θ: 057 uses Θ(E) for a plane-angle function. It is also used for the c-number Θ_{ab} (L1402, L1440, Problem D) and the Poisson bivector Θ^{μν} (L2085, L2114ff., Problem F). These are different sections and 057 defines Θ explicitly, so this is a note.
- v and κ: 057 (iii) rebinds v (real vector in Im h_∞ = −κvv^T) and κ ≥ 0. Under "keep the notation of the two preceding paragraphs" these collide with v = Λ^{-1}e_0 at L1554 and the momentum κ at L1547. 057 redefines both explicitly at the point of use, so this is minor and not blocking.
- σ_1, σ_2 (057) versus the Pauli σ^a at L1500/L1530. Note.
- \mathcal J: \mathcal J_λ at L1424 (Problem D derivation) versus \mathcal J(κ) at L1519 (Problem E). This reuse predates 057 and 057 does not use \mathcal J. The threshold function J(m²; …) at L1718 uses a different glyph. Note.
- F_{\mathrm E}, \mathcal R_u, \mathfrak C and M_γ are used consistently, with no clash.

**5. PRIOR-CLAIM-ERROR.** I found no materially false or overbroad merged claim in L1101–2200.

**6. Process language.** I found none. "We have not reproduced this" (L1120) and "The reading adopted here" (L1476) are first-person scholarly wording, not process language. Note.

### Integration of the 057 insert
Nothing in L1101–2200 blocks integrating the 057 insert immediately before the Problem E `\paragraph{Status.}` at L1564. Its internal references resolve, and no earlier E block becomes false or stale. If desired, a later editorial pass could rename 057's rebound v and κ (minor).
