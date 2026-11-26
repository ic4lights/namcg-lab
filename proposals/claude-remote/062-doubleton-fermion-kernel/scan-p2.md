**Scan note, ordinal-60 full scan, pass 2 of 5 (gatekeeper, read-only)**

**Range read and hash**
- I read `C:\Users\redgi\Projects\namcg-lab\proposals\062-doubleton-fermion-kernel\appH_insert.tex` in full, all 10 lines.
- I read `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex` lines 1101–2200, every line, in consecutive chunks: 1101–1220, 1221–1380, 1381–1440, 1441–1481, 1482–1521, 1522–1561, 1562–1591, 1592–1626, 1627–1746, 1747–1896, 1897–2056 and 2057–2200.
- Working file confirmed: 599923 bytes, sha256 82ab236415a5fbbea02be7ceb6eebc791e560eef4a7e589cb25be2cf9ffa279c, 3313 lines.
- For targeted checks I also read ch17-agenda.tex L390–411 (Problems E and F), confirmed that `ass:lorentzian` exists (ch04 L322), and checked `bib/namcg.bib` and the proposal's `bib_entries.bib`.

**Findings**
1. **L1622, note.** `\paragraph{Status.}` occurs six times in appH (L505, 1622, 2824, 3043, 3160, 3303). The insert must go before the L1622 one, which is the only one in Problem E (L1482–1624), directly after the 061 closing line at L1620 and its blank line at L1621. A search on the bare string is not unique, so place it by line or with its context.
2. **No line (bib), minor, integration prerequisite.** The insert cites four keys that are not yet in `bib/namcg.bib`: MartinDussaud2019, MackTodorov1969, Todorov2019 and FioresiYuncken2024. They are in `proposals/062-.../bib_entries.bib` and must be appended at integration, or the build will show undefined citations. MantaSteinacker2025 is already in the bib.
3. **L1609–1620 (061) against the 062 insert: no conflict.**
   - "The preceding paragraph" in 062 resolves to 061.
   - 062's identity c⁻¹D₋D₊ = C₅ − C₄ − 2X, with X = ½(C₄^tot − C₄ − 3/2), is exactly 061's c(C₅ − C₄^tot + 3/2) (L1612), carried to so(4,1) ⊃ so(3,1) as 061 allows at L1618.
   - 4J_L² = C₄ ± 2iP and B = 1 + C₄ − (A+1)² = ∓2iP re-check by hand. 061's normalisation (3 on the vector) is consistent with C₄ = k² − p² − 1.
   - W timelike, c > 0, γ = 3c matches 060 (L1601) and 061 (L1618).
   - 061's sentence "whether their fermion form has a normalisable kernel is not decided here" (L1618) stays true, since "here" scopes it to that paragraph.
   - 061's conditional "If the fermion forms … are non-degenerate … separates them" stays correctly conditional. 062 says the hypothesis holds only "in that sense" (HS class, smooth vectors, doubletons) and explicitly does not establish the one-loop separation (no bounded inverse, Pfaffian at N = ∞ undefined). Nothing becomes stale or false.
4. **L1609–1620 (061) and 062 together, minor, symbol clashes.** None is blocking; each is defined locally:
   - **X:** 062's X = σ·J_L sits in the same section as the contour matrices X_ν (L1529–1586).
   - **P:** 062's P = J·K clashes with the regulator matrix P (L1552–1569).
   - **K:** 062 uses both the boosts \vec K and "the factor K" (transverse) in one paragraph, and 061 also uses K for the propagator (L1618).
   - **n:** n labels V_n = Sym^n ℂ⁴ in 061 but the doubleton \mathcal H_n in 062.
   - **H_n, J_L, D_±:** there is no real clash. \mathcal H_n and H = LᵀhL use different fonts; vector J_L and lowercase j_L are consistent; \mathcal D_± differs from \mathcal DΦ (L1182) and from the Dirac \mathcal D outside this range.
5. **L1595 and L1605 (060), note.** 𝖪 is the kinetic tensor. The phrase "𝖪 the tensor written γ^{μν} there" refers to Steinacker2026Weak's notation and is disambiguated explicitly, so there is no clash with the mass γ.
6. **Status lines, none.**
   - L1486 ("Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL.") matches ch17 L395 ("OPEN; CRITICAL PATH for the matrix-derived label").
   - L1629 (F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL.") matches ch17 L404.
   - Every E-block closing line in the range (L1480, 1510, 1527, 1549, 1562, 1573, 1586, 1607, 1620) keeps E open and Assumption `ass:lorentzian` retained. The 062 closing line ("Problem E stays open with Assumption retained") agrees.
   - Consecutive closing status lines (061, then 062, then the Status paragraph) follow the section's established house style. Note only.
7. **Labels and refs, none.** The insert adds no `\label`. Its only `\ref` is `ass:lorentzian`, which resolves. I saw no duplicate or undefined labels in the range on reading; this is not a build check.
8. **PRIOR-CLAIM-ERROR, none found** in L1101–2200, including 059–061. On reading, the claims are scoped to their stated classes. I did not re-derive the numerical claims of 059–061 in this pass; I only scanned them for consistency and overreach.
9. **Process or chat language, none** in the range or in the insert.

**Does anything block integrating 062?**
No. The only prerequisite is that the four bib entries from `bib_entries.bib` are appended to `bib/namcg.bib` and that the insert goes at the Problem E `\paragraph{Status.}` (L1622), not at another Status anchor.
