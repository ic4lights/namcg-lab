SME-CONSULT: answered

Advisory only, no verdict. Line numbers refer to the arXiv TeX sources as I downloaded them. Searches are scoped: a failed search is reported as such and is not evidence of absence.

## Short answers
1. **Null spectrum and Jordan structure.** I found no published statement of Jordan or double-zero structure.
   - The triangular linear system that implies it is published, in Furuta et al. and in Sakai 2017. The 8 + 2·6 split follows from Furuta's equations in one step (hand check below).
   - Published actions and norm statements on this class do exist. The sentence "no action defined on the class" is too strong as a statement about the literature.
2. **Lorentzian non-compact fibre.** Yes at the formal level, so "Lorentzian SO(3,1) reading" should not sit in an "added here" list. Domains are untreated in everything I read.
3. **"Not very successful".** No reason is given at that sentence, but the same paper gives its objections to the differential-operator expansion later on. I found no published no-go. hep-th/0602210 and hep-th/0604103 are not no-gos, and both impose their torsion-type constraints by hand.

## Q1. Null spectrum, norm or action on the first-order class

### Searches
- INSPIRE citation lists read in full: HKK (103 citers), Furuta (27), hep-th/0602210 (15), hep-th/0604103 (11).
- INSPIRE full-text queries within HKK citers:
  - "double pole": 0 hits.
  - "Jordan": 2 hits, neither on this topic by title (1911.03162, hep-th/0510252). Not opened for that term.
  - "negative norm": 7 hits. "torsion" and "ghost": 8 hits.
- WebSearch (extended): nothing on double poles or dipoles in this class.
- **Result: searched these, found no statement of double zeros or Jordan chains for torsion modes.** Full-text indexing is incomplete; for example, a Furuta-citers "ghost" query returned only Konishi 1301.0508.

### What exists

**Triangular linear system**
- **Furuta et al., hep-th/0611093, L823-879, L1807-1856.**
  - The equations are ∂^a f_ab^μ = j_b^μ and ∂^a F_ab^cd = J_b^cd.
  - J starts at quadratic order, while j has a term linear in ∂S'. So S' obeys a Maxwell-type equation at linear order and sources h. This is block-triangular.
  - The physical components h_i^μ and S'_i^cd are listed, with h_i^0, S'_i^0j, S'_i^01 called negative-norm. Double zeros are not mentioned.
- **Sakai, 1709.02588 (Nucl. Phys. B925, 195), Eq. EOM_prin, L725-730.** Same structure from the Poisson limit: □f + ∂ω·M = 0 and □ω − ∂∂·ω = 0. He then restricts to metricity and T = 0.

**Hand spot-check (mine, not published)**
- For physical S'_i at null q, Furuta's j reduces to j_i^μ = q_c S'_i^{cμ}.
- For each of the 2 transverse i, the map from a 2-form to q_c S^{cμ} has rank 3 at d = 4. The total rank is 6.
- This gives 6 chains S' → h, with each block's determinant going as (q²)². The remaining 2 h modes and 6 S' modes (those with q_c S^{cμ} = 0) are simple, which makes 8.
- This reproduces the proposal's and the gatekeeper's 8 simple + 6 double exactly.
- The trace term in j is along q_b and looks removable by the gauge condition. It adds no double zero by my argument, which is hand-level only.
- **Novelty consequence:** the explicit split is unstated in what I read, but it is a short corollary of published equations. It is not a new structural discovery.

**Statements bearing on the zero-norm and chain structure**
- Sakai 2017, L1100: quadratic-curvature actions are "forth-order in terms of the metric but second-order in terms of the spin connection". This is the closest published qualitative remark I found. It is not about double zeros as such.
- Ho-Kawai-Steinacker, L943: in the fibre-less minimal model, zero-norm c_i^+ are "orthogonal to all state vectors" and decouple.
- My reading, not published: in the fibre class, h_i^μ ∝ q^μ lies in the image of j, so it is a chain tail. That decoupling argument is not automatically available there.

**Norm or action on the class**
- **Hanada, hep-th/0606163 (PTP 115, 1189), L459-612.** Heat-kernel regulated action.
  - Result: S ∝ ∫ R_abcd R^abcd at leading order, Euclidean Spin(n).
  - The paper says this "does not give the Einstein-Hilbert action", the regulator breaks higher-spin gauge symmetry, and it depends on the background.
- **Sakai 2017, L609-621.** Semi-classical action ∫dq G̃² over x, p, g, t, Euclidean.
- **Matsuo-Tomino-Wen-Zeze, 0807.1186 (JHEP 11, 088), Appendix Eq. idn3.** Tr[∇,∇]² written with torsion ignored. L379 notes the traces formally diverge and assumes a suitable regulator.
- **Isono-Tomino, 0911.1769 (PRD 81, 084049), L98, L614.** The equation "seems difficult to derive by a variation of any gravitational Lagrangian", and no quantisation rule for e and ω is known. They note "an anxiety about negative norm states". L107 and L181 rotate the equations to Lorentzian. This is the closest torsion-focused follow-up, classical only.
- **Asano-Steinacker, 2112.08204, footnote at L3161-3170.** In HKK "the absence of ghosts has not been established".
- **Steinacker, 1910.00839, L1256-1258.** HKK has "excessive dof and the associated ghost issues", citing Sakai 2019.
- **Sakai, 1905.10067 (NPB 949).** Removes "positivity-violating" parts by higher-spin gauge symmetry plus posed generalised torsion-free conditions. It does not analyse torsion modes as dynamical.

**Bearing on Furuta's mass-generation idea**
- Sakai 2017, L928-1062. Results are for g-independent, first-order fields in the semi-classical limit, Euclidean signature.
  - Without supersymmetry, one-loop masses go with the Spin(D) Casimir. The vielbein also gets a mass ("quite bad news", L1003).
  - For IIB (d = 10, factor (d−2) − 2^{[d/2]−κ} = 0) all these fields remain massless.
- So at this order, in that setting, loops do not lift the modes in IIB. This is in tension with the published assumptions below:
  - higher-spin masses are assumed in Asano-Kawai-Tsuchiya (L876);
  - a higher-spin mass gap is assumed in Ho-Kawai-Steinacker (L1343).
- That calculation did not treat independent torsion modes.

**General context, abstracts only**
- Bender-Mannheim, 0804.4190: the equal-frequency Pais-Uhlenbeck Hamiltonian becomes a Jordan-block operator.
- Bender-Mannheim, 0807.2607: the supposed ghosts disappear in a PT-symmetric treatment.
- Together these support not attaching a ghost reading to a double zero without a specified inner product.
- Standard algebra, my spot-check: if an operator is self-adjoint for a nondegenerate form, a chain's eigenvector is neutral, because ⟨v,v⟩ = ⟨(A−λ)w,v⟩ = ⟨w,(A−λ)v⟩ = 0. This presumes a form exists; none is derived here.

## Q2. Lorentzian version with non-compact fibre

**Published, formally:**
- **Asano-Kawai-Tsuchiya, 1205.1468 (IJMPA 27, 1250089), L109-121, L178-235, L384-417, L536-538, L841, L897-898.** This is the explicit case.
  - "we assume that M has the Lorentzian signature", with principal Spin(D−1,1) bundle.
  - C^∞(E_prin) ≅ Γ(E_reg), with the regular representation and the Clebsch-Gordan reading.
  - Haar measure, group delta function, divergent γ = δ_gg, and V_G "the volume of the fiber Spin(D−1,1)".
  - The Peter-Weyl theorem is invoked. The trace is handled by citing Hanada's heat kernel.
  - It does not discuss non-compactness: a grep for "non-compact" and "noncompact" finds nothing.
- **Matsuo et al., 0807.1186, L193 and footnote, L926-936.** G = Spin(1,d) with V_reg = ⊕_r d_r V_r, then explicitly broken to Spin(d) × R for BFSS.
- **Hanada-Kawai-Kimura, hep-th/0602210, L939-941, L1037-1052.** Explicit d = 2 example, principal Spin(1,1) bundle over a Lorentzian N=(1,1) superspace. It uses the real exponential representation R^⟨s⟩(φ) = e^{2sφ}, with O_01 = ¼∂_φ.
- **Sakai 2017, L191.** "Spin(D−1,1) (or Spin(D) in Euclidean case)", one clause. All his analysis is Euclidean (L245).

**Euclidean by stated choice:**
- Hattori-Mizuno-Tsuchiya, 2410.13414, L162-168.
- Hattori-Seko-Tsuchiya, 2606.24577 (PTEP 2026), with embeddings into Euclidean space at L2605. Its regularisation is on Kähler manifolds with Spin or Spin^c fibre. Haar is normalised to ∫dg = 1 (L280), which is the compact case.

**Domains:** searched these sources, found no treatment.

**Concerns these papers do not address (standard mathematics, my remarks; I did not fetch a reference):**
- L²(G) for non-compact G decomposes by a Plancherel direct integral, not Peter-Weyl.
- The vector-representation entries u_a^b are unbounded multipliers on L²(G). This is unlike Spin(n).
- Hanada's heat kernel uses a sign-definite Σ O_ab² in Spin(n). Its Lorentzian use, as cited in Asano-Kawai-Tsuchiya, is not justified in what I read.
- Sakai's "positive mass squared" from the Casimir relies on Spin(D). His Lorentzian footnote (L425) concerns the section 2 analysis only.

## Q3. "Not very successful" and no-go status

### What the paper says
- **Ho-Kawai-Steinacker, 2509.06646v2 (JHEP 02 (2026) 070), L153.** "So far, this does not appear to have been very successful \cite{HKK}". This is the only \cite{HKK} in the source, with no reason attached.
- **Reasons the same paper gives for differential-operator expansions** (linking them to the L153 sentence is my inference):
  1. **Negative norm, L723-724.** Components a_0^i and a_i^0 need 2(d−1) gauge parameters, while diffeomorphisms supply d.
  2. **Divergent trace, L945-982.** The naive action is UV divergent. tr(A exp(εBox)) violates cyclicity. Regularising the operators gives a nonlocal action.
  3. **Summary, L1329-1335.** "the time component of each tensor field has a negative norm"; the expansion is "highly singular in the ultraviolet"; "no clear correspondence" between the bilocal and tensor inner products; both action and inner product are UV divergent.

These are shown for the fibre-less a_μ^ν∂_ν truncation. The paper does not analyse the O_cd sector.

### The paper's own resolution
- A constraint, not a fibre: A_μ|k=0⟩ = 0 (L798), which reduces diffeomorphisms to volume-preserving diffeomorphisms (L822-825). It assumes a higher-spin mass gap (L1343).
- The surviving spin-two sector has no spin connection in this minimal model. Its local rotation content is not established there.
- It runs in the opposite direction to the fibre route. Ho-Kawai-Steinacker also claim positivity in the bilocal planar sector (L684-689, L1327-1328).

### Others
- Steinacker, 2601.08031, L256-257: such backgrounds "do not lead to a local action without further regularization".
- Steinacker, 2002.02742, L302-304: HKK "formally leads to the Einstein equations. However this is not quite borne out here".

### No-go status
Searched the citation lists and full-text queries above and found no published no-go theorem for this interpretation. The published concerns are stated difficulties, not theorems.

### hep-th/0602210 (PTP 115, 1003)
- On torsion modes:
  - The constraints are imposed as an ansatz "to eliminate the fields that are unnecessary" (L943-945).
  - They are shown sufficient in d = 4: "it is unclear whether or not they are necessary" (L1545-1549).
  - Fit to 10D is unclear (L1754-1758).
  - The action "is not bounded from below" (L1760-1762).
- Furuta's discussion (L1747-1757) reads this as suggesting a constraint can be found. It is not a derivation of one from the matrix integral, and it changes the matrix space.
- On sources: it contains the supermultiplet only, with R_ab^ac = 0 stated in super-Riemann form (L1517-1519). I saw no external matter.

### hep-th/0604103 (JHEP 06, 010)
- Free, flat, linear, Euclidean.
- On torsion-type modes:
  - Tracelessness and field-strength constraints are imposed (L987-1009).
  - It warns that "viewed from the matrix model, field strengths should be introduced as independent degrees of freedom" and may "propagate as asymmetric tensor fields" (L1024-1027).
- Nothing on sources.
- Sakai 2019 disagrees on the spin-s content: "not the Fronsdal field" (abstract, and L499).

### Sources at T ≠ 0
- Furuta's R_ab = (3−d)∂_a∂_bφ is the torsion source (L722-725).
- Sakai 2017, L1106: it is "still unclear whether it mediates the real gravitational interaction".

## Facts bearing on the review text (the gatekeeper decides)
- **R21, "With no action defined on the class".** Regulated or semi-classical actions are published (Hanada, Sakai, Matsuo). Scoping would be needed to "no action is used here" or similar.
- **R21 and R20.** Isono-Tomino, Asano-Steinacker and Sakai 2017 also bear on the norm or positivity reading, so attribution to Furuta alone is incomplete.
- **Scope list, "Lorentzian SO(3,1) reading".** Prior: Asano-Kawai-Tsuchiya, Matsuo et al., and Spin(1,1) in hep-th/0602210. The remaining gap is domains and non-compactness.
- **Scope list, "fixed-Hilbert-space statement".** hep-th/0602210, L461-465, says that for any M the large-N space "contains a set of matrices which are unitary equivalent" to i∇_(a). Only the explicit |det e|^{-1/2} conjugation may be additional; I did not search for that specifically.
- **R25, "without a reason given at that point".** True as scoped. The reasons at L723-724, L945-982 and L1329-1335 are in the same paper and bear directly on the sentence.
- **Open avenue 1.**
  - The "quantum corrections" branch has a published one-loop result in the T = 0, g-independent setting (Sakai 2017).
  - The "constraint" branch has 0602210 (imposed) and the Ho-Kawai-Steinacker constraint (fibre-less).
  - Sakai 2017's fibre section keeps only T = 0 fields by assumption, and says metricity "does not seem to be obtained naturally" (L1098).
- **Emergence.**
  - Sakai's and Asano-Kawai-Tsuchiya's framing is a "given" manifold.
  - hep-th/0602210 L523-525 states "we do not fix M", which fits the surviving form in your ruling. This is the formal statement, not a derivation of selection.

## What I read and how
- **TeX source read in full:**
  - hep-th/0604103.
- **TeX source, substantial targeted reads:**
  - hep-th/0602210 (L1-700, L780-800, L932-960, L1030-1089, L1320-1345, L1465-1562, L1680-1790).
  - 1709.02588 (L70-259, L395-434, L560-1115).
  - 2509.06646 (L132-168, L634-1049, L1303-1354).
  - 1205.1468 (L90-359, L530-545, L836-925).
  - hep-th/0611093 (L640-974, L1695-1856; your scratchpad copy).
  - hep-th/0606163 (L447-616).
  - 0911.1769 (L77-181, L612-620, plus equations to L330).
- **TeX source, targeted passages only:**
  - 2410.13414 (L130-180, L1273-1329).
  - 2606.24577 (L113-115, L245, L280, L2589-2626).
  - 1905.10067 (abstract and intro, L499-512).
  - 0807.1186 (L193, L276-290, L375-382, L486-506, L896-945).
- **Grep or citation context only:**
  - 2112.08204, 1910.00839, 2002.02742, 2601.08031, 2608.09598, 1911.03162, 1610.09844, 2005.13936, 1301.0508.
  - Downloaded, but no specific claim taken from the source text: 2609.40183, 2512.03161, 0802.2782, hep-th/0703021, 1708.00734.
- **Other:**
  - hep-th/0508211: grep only (Haar, heat kernel, propagation lines).
  - PoS(CORFU2025)367 (10.22323/1.509.0367): abstract and first page via PDF text. It is a regularisation proceeding, with no torsion or spectrum content on those pages.
  - Bibliographic data for the journal references above: INSPIRE API.
  - 0804.4190 and 0807.2607: arXiv API abstracts only.

## Not independently verified or not read
- **Sakai PhD thesis, Kyoto 2020** (doi:10.14989/doctor.k22243): record only, not read. It may contain more on torsion or the principal bundle.
- **Kawai, "Curved space-times in matrix models", PTPS 171, 99 (2007):** record only; publisher returned 403. Not read.
- **Remaining citers of HKK:** titles only.
- **Plancherel and unboundedness remarks:** standard mathematics, not checked against a fetched reference.
- **The trace-term and chain-tail remarks in Q1:** my own, hand-level, unpublished.

## Process note
- One tool round issued two reads in parallel, against the serial rule.
- Downloads went only to `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\sme50`.
- No repository file was changed. `git status` showed the same three entries as at the start.
