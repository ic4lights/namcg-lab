VECTORMIN: mode5-deepdig(A,D1,E) | ENGINE: semantic:BAAI/bge-m3@5617a9f61b028005a4858fdac845db406aefb181 (prose) + lexical TF-IDF (formula channel) | QUERIES: 8 (arXiv, all in interrupted stage; no new queries this run) | HITS: 36 ranked / 33 verified-cached-record / 2 already-cited / 0 unverified | INTERNAL: 30 near-miss + 7 dup pairs + 8 formula-channel findings | STATUS-EFFECT: none

# Mode-5 deep dig — problems A, D1, E (resumed run)

Started 2026-11-08 12:40. **Supersedes the interrupted 11:39 run**
(`reports/vector/vector-mining-mode1-20261108-1139.md`, MiniLM index; its
`cache/rank_out.json` is cross-model and NOT used). Resume constraints honoured: no new
arXiv queries; the 173-record cached corpus is the corpus; the **full-text skeleton
channel is DEFERRED, not saturated** (0 full-text docs); the 10,502 math atoms are
indexed only through the lexical formula channel. Mid-run correction (recorded, not
hidden): the prose masking regex initially swallowed non-math environments
(`tabular`/lists) collapsing 155 chunks to `<MATH>`; the chunker was fixed to a math-env
allowlist, those chunks re-embedded (same pinned model), all stages re-run; pre-fix
numbers in this file are the corrected ones. Corpus rows and query blocks were unaffected.

## Source reading

`scripts/make_digest.py --check`: DIGEST CURRENT; 30 files; chapters-hash 078490eebb054d6a;
appH hash c39e90f5b343... (= coordinator's post-integration-57 sha256); dirty-chapters:
no; no duplicate labels. Digest + targeted reads; no full-manuscript scan claimed.
Read in full: appH Problem A section L12-118 (free lemma L22-39, K0 at L26; general
sector L41-61, bound L52-55; 058 Weyl-data L63-109, product law L78; missing step
L111-118); Problem D ledger+missing step L644-687; 059 D blocks (class relation
L1442-1448; ghost/label/pairing L1464-1528; finite-N toy L1530-1531; locked-frame
composite L1533-1534); Problem E L1536-1581 (ledger L1539-1547; integrals L1549-1568;
Stokes band L1570; bridge L1573; status L1578-1579); appH L2734-2745 (Problem F
"Explicit K", fuzzy-sphere closed spectra). ch17 L325-410 (D/D1 329-370; A 377-392; E
394-399), L640-734 (order; finished items A 701-703, D1 712-717, E 718-719).
Definitions: ch03:264-271 (ass:frame-lock), ch03:345-362 (ass:dictionary, eq:dictionary),
ch03:371-401 (constant-Theta Moyal-check remark), ch04:170-175 (ass:nondeg),
ch04:321-328 (ass:lorentzian), ch10:56 (ass:local-lorentz).
Query blocks (verbatim; pinned in `scratch/vector/cache/queries_ade.json`): A_missing
appH:111-118; A_058close 103-109; A_freelemma 22-39; A_general 41-61; D_class 1442-1448;
D_locked 1533-1534; D_status 647-651+674-687; D_toy 1530-1531; E_stokes 1570; E_bridge
1573; E_status 1539-1547+1578-1579.

## Corpus

8 arXiv title+abstract queries (max_results 60), 173 deduped records cached in
`scratch/vector/cache/arxiv_ade/corpus.json` (+`queries_meta.json`):
A1 modular Hamiltonian+causal diamond+matrix/emergent/NC -> 2; A2 Bisognano-Wichmann +
deformation/NC/variable/generalization -> 24; A3 "half-sided modular inclusion" -> 20;
D1 matrix model + local Lorentz/vierbein/tetrad -> 9; D2 fuzzy sphere +
Laplacian/Yang-Mills + spectrum -> 5; E1 Lorentzian + signature/path integral +
emergent/matrix/Euclidean -> 431 total/60 fetched; E2 thimbles + complex action/
oscillatory/fermions -> 48; X1 NCG + modular + spectral triple/Tomita -> 5.
Cached Atom records (title+abstract) count as primary verification per coordinator
instruction; all 173 ids resolve; no non-resolving near-duplicate ids found.
Reproducibility: `scratch/vector/{chunk_book,arxiv_fetch_ade,build_embed_ade,patch_emb,
rank_ade,mode2_scan,mode4_lex,mode4_refocus}.py`; `scratch/vector/index_meta.json`
(model id + revision 5617a9f6..., dim 1024, channels, pre-fixed thresholds/rules).

## MODE 1 — external ranking (COMPLETE)

Channel P (bge-m3). Aggregation per problem: MAX cosine over the problem's query blocks
(pre-fixed). Bands (pre-fixed): terciles of each problem's own top-12 scores; full
173-record distribution given so the compressed range is visible. "cited" = arXiv id
(version-stripped) matches an `eprint` in `bib/namcg.bib`. Each line = verified record /
what its own record says it proves / why it does not by itself discharge the ledger's
stated missing step. No score below is progress on any problem; all are pointers to
calculations that still have to be checked against the ledger's hypotheses.

Problem A (max 0.622, median 0.494, min 0.409):
1 0.622 high | 2002.00018 | new — all-order Lorentzian formula for half-space/Rindler modular Hamiltonians of Euclidean-source states. Fixed-background QFT: metric and region precede K; no matrix generator, so not A's pre-metric identification.
2 0.619 high | 2503.18036 | new — proves K1⊂K2 for half-sided modular inclusions iff spectral-subspace inclusions of the positive one-parameter generators hold. Nearest formal neighbour to "identify inclusions via generators"; its generators are already modular data of standard subspaces; A needs an algebraic generator shown to BE H_D.
3 0.608 high | 2111.03172 | new — explicit deformed half-sided modular inclusions; relative-commutant triviality criterion (algebra localized at infinity). Closest "variable-structure" modular construction here; fixed chiral QFT, no matrix Hamiltonian.
4 0.600 high | 2501.02998 | new — non-local modular flows across deformed null cuts in the relativistic vacuum; vacuum/background assumed; regions deformed, not generating data.
5 0.589 mid | 2509.13401 | new — explicit causal-diamond vacuum density matrix in asymptotically flat gravity (soft effective action). Direction reversed vs A: metric input, K output.
6 0.579 mid | hep-th/9511216 | new — modular-covariance conditions generalizing Bisognano-Wichmann for nets; assumes wedge-local algebras with geometric action.
7 0.576 mid | 1006.4726 | new — algebraic Haag theorem: net fixed by double-cone algebras on one hyperplane (split + geometric modular action). Method pointer (modular data -> model rigidity); geometric modular action is precisely what A must derive.
8 0.575 mid | 2505.15941 | new — Einstein-as-hydrodynamics with density matrix per causal diamond (⟨K⟩, fluctuations). Metric fundamental, K derived — opposite of A.map's required direction.
9 0.575 low | 2503.09644 | new — zeta zeros via Majorana in Rindler space; off-topic near-miss.
10 0.573 low | 0806.1940 | new — Borchers relations for braid sectors: modular objects give boost/translation reps WITHOUT full BW geometric action; closest "modular structure from axioms alone" item here; no matrix model.
11 0.572 low | 2508.21062 | new — modular-twisted product for scrambling on Leutheusser-Liu half-sided inclusions; semiclassical background assumed.
12 0.567 low | 1607.04205 | new — CP^{N-1} thimbles; relevant to E, not A.
A-flag (key question): across all 173 records, **no paper matches an algebraic K-0-type
generator built from a matrix Hamiltonian to a causal-diamond modular Hamiltonian without
a pre-existing metric** — near hits assume the metric (1,4,5,6,8,11) or use
already-modular data in fixed backgrounds (2,3,7,10). Negative finding; search breadth is
8 title/abstract queries only, not a novelty proof.

Problem D1 (max 0.637, median 0.533, min 0.429):
1 0.637 high | 2503.18036 | new — (recurs) generator/spectral-subspace inclusion; recurrence is shared vocabulary with D_status, not shared content.
2 0.626 high | hep-th/0508211 | **already cited** — curved spaces described by matrices; confirms adjacency of the D toy to existing citations; no new input.
3 0.625 high | 1704.01336 | new — antiunitary representations and modular theory survey; relevant to structure-group/signature readings; no class-selection result.
4 0.625 high | 2503.09644 | new — off-topic (Rindler zeta).
5 0.624 mid | hep-th/0303119 | new — U(2)⊗U(2) matrix model: vierbein in Y_mu, spin connection in X_mu; Einstein equations from theta->0. Strongest dictionary/method donor for D1 (vierbein+connection as separate matrix data); their theta is NC deformation; no equivariant-class selection; the class relation is not their object.
6 0.623 mid | 1006.4726 | new — (recurs) net rigidity; geometric-modular hypotheses.
7 0.621 mid | hep-th/0606163 | **already cited** — Steinacker finite-matrix covariant derivative on curved space: closest existing anchor to the finite-N class/ghost machinery; the ledger does not show 𝔻_a/ghost equal to its operator.
8 0.619 mid | 1004.3009 | new — general-linear matrix model -> Weyl kinetic operator on 3+1D lattice; neighbour to (7,3) kinetic signature and to E; no local-Lorentz selection.
9 0.618 low | hep-th/0204078 | new — matrix model with manifest general-coordinate invariance mixing so(9,1) and u(N); structural predecessor for D1 connection content; 10D large-N, mechanism not selection.
10 0.614 low | 2111.03172 | new — (recurs).
11 0.612 low | 2509.13401 | new — (recurs).
12 0.609 low | 2203.13124 | new — Rényi log corrections; off-topic.
Note: the D2 fuzzy-sphere records did not reach D1's top-12; the internal appH:2740 twin
(mode 4 below) currently outperforms the external corpus for the ghost-spectrum question
at this query breadth.

Problem E (max 0.642, median 0.527, min 0.428):
1 0.642 high | 2501.03752 | new — Lorentzian-signature fluctuations from Wick rotation in foliated asymptotic safety (ADM RG). Signature-as-fluctuation, but no contour family, no matrix model, no gamma->0- bridge.
2 0.626 high | 2406.06635 | new — hybrid Euclidean-Lorentzian universe with transition point; phenomenological; no error-controlled contour statement.
3 0.616 high | 2503.18036 | new — (recurs; vocabulary).
4 0.607 high | 0806.4239 | new — emergent Lorentzian signature + scalar gravity model; closest to E's emergence framing; condensed-matter-like mechanism, not R_u analysis.
5 0.604 mid | gr-qc/9802057 | new — bijective maps between classes of Euclidean and Lorentzian metrics (covector-product construction). Metric-level signature dictionary; NAMCG's signature sits in the kinetic e-combination — `notation-collision` watch on any "signature map" phrasing.
6 0.604 mid | hep-th/0002050 | new — non-perturbative Lorentzian path integral (causal triangulations) with unique Wick rotation per geometry; assumed uniqueness stands opposite to E's band obstruction.
7 0.603 mid | 2111.03172 | new — (recurs).
8 0.602 mid | 2603.29287 | new — Schwinger-model theta-vacuum entanglement; off-topic (theta vocabulary).
9 0.599 low | 1607.04205 | new — CP^{N-1}+fermions Lefschetz-thimble analysis beyond Gaussian (bions, complex saddles): nearest method donor to E's Stokes/contour machinery; QM not the matrix-model action; no analogue of delta>lambda_*eps; transfers technique, not statements.
10 0.598 low | 2002.11700 | new — twisted spectral triple inducing Euclidean->Lorentzian transition (fermionic action); NAMCG has no spectral triple; dictionary would be research work.
11 0.597 low | 2505.00112 | new — Lorentzian dispersion from Euclidean scalar-tensor background; dispersion-level, not measure/signature-level.
12 0.596 low | 2212.10127 | new — expanding spacetime in a large-N limit of the LORENTZIAN type IIB matrix model (Lorentz-invariant mass term, complex Langevin). Adjacent to E's IKKT-type sign problem; their fix changes the model rather than bridging gamma->0-.
Cross-cutting: 6 records recur in two problems' top-12; with medians 0.49-0.53 the bands
are ranks within top-12, not evidence tiers.
## MODE 2 — internal prose scan (COMPLETE; bge-m3 P channel; no literature claim)

(a) Near-misses to query blocks, excluding the problem's own appH section (top rows;
full 10 in `cache/mode2_scan.json`). Reading these is for the researcher; possible
partial-calculation candidates flagged [P]:
A: 0.703 ch08-heat-kernel:283-285 (heat kernel on g^(0) vs ass:aux-metric, near the
pre-metric theme); 0.692 appK-endomorphism:71-82 ("What is not shown": completed a1/a2
evaluation on the locked 4x4 block) [P]; 0.681 ch03:593-606 (symbol action does not
construct Phi); 0.679 ch03:371-401 constant-Theta Moyal-check remark (conditional) [P];
0.677 appH:2855-2866 (Problem H missing step: regulated modular operator, weak field);
0.673 appE-rar-bridge:256-265 (de Sitter diamond modular Hamiltonian used as gap test).
D1: 0.774 ch17:329-370 (own agenda passage; expected); 0.761 appH:15-20, 0.760
appH:2769-2773, 0.754 appH:1584-1588 (other problems' ledger-label boilerplate); 0.748
appH:427 (Problem B Moser variables for symplectic leaves) [P]; 0.755 ch18:81-88 and
0.754 ch17:675-683, 0.751 ch17:734-742 (alternate-scope D2 statements).
E: 0.859 ch17:394-399 (own agenda E passage); 0.795/0.770/0.760/0.759 ledger-label
boilerplate (appH:15-20, N:3133-3135, F:1584-1588, G:2769-2773) — vocabulary, not
content; no near-miss above 0.74 carries E-specific mathematics outside the E section.
(b) Duplicate pairs, threshold cosine >= 0.90 pre-fixed, chunks >= 200 chars: 7 pairs
(all reported): 1.000 ch05-lorentz-decomposition:327-330 = ch10-lorentz-locking:334-337
and 1.000 ch05:332-357 = ch10:339-364 — VERBATIM cross-chapter duplication (component
counts of the algebraic split; read and confirmed identical) — gatekeeper duplication
risk; 0.923 appA-seeley-dewitt:110-160 ~ ch08-heat-kernel:30-49; 0.921 appH:2569 ~
appH:2582; 0.914 appH:663-672 ~ ch10:291-307 (D missing-step region vs locking chapter);
0.914 appH:1584-1588 ~ appH:2769-2773 (ledger boilerplate); 0.900 appH:2474 ~
appH:2509. Internal observations only; no status implication.

## MODE 4 — internal formula channel (COMPLETE; LEXICAL TF-IDF, not semantic)

TF-IDF over normalized LaTeX (char/token n-grams 2..4, df-weighted, cosine), 7 target
formula spans vs 10,502 math atoms of all `chapters/**/*.tex` (`cache/mode4_lex.json`;
exact-atom refocus pass excluding own-line atoms in `cache/mode4_refocus.json`). bge-m3
is not formula-aware so the spec's token-level fallback is used; never averaged with the
prose channel. External formula ranking and full-text skeletons: DEFERRED this run.
1 `identity-twin (candidate)` — ghost spectrum `{l(l+1):0<=l<=N-1}` (appH:1531, D toy) vs
  Problem F fuzzy-sphere closed spectra "vector l(l−1), l(l+1)+2, (l+1)(l+2); spinor l²,
  (l+1)²" (appH:2740): top-3 0.539/0.418/0.386, all at 2740. Different operators (ad²
  ghost on End(C^N) vs F fluctuation operator); connection, if any, for the researcher.
2 `isolated` — ghost operator `Σ_i ad²_{X_i}/ħ_eff²` itself: best non-own atom 0.312.
3 `isolated` — Weyl product law appH:78: best non-own 0.408 = its own remainder bound
  appH:83; nothing else in book.
4 `no notation collision` — class relation appH:1444-1447 matches only inside the D
  section (0.572 @1531; 0.519 @1499; 0.509 @1458); 𝔻,𝕋,𝕽,𝕊,𝔽 consistently used.
5 `duplicate (same-section)` — c0(u) identical at appH:1570 and 1573 (1.000); Γ0(u)↔c0(u)
  0.746 from shared numerator. Consistency note.
6 `isolated` — Stokes band δ>λ_*ε (appH:1570): only artifacts (`R_*`,`m_*` at
  ch14:280, 0.451 — shared subscript-star; verified by reading the atoms).
7 `isolated` — K0 = ½Θ⁻¹ᵘᵛ tr(X̂_μ[X̂_ν,H_quad]) (appH:25-27): best non-own 0.245; the
  bound O(R√‖δΘ‖+‖H_int‖) matches only appH:36 (0.526, same section).
8 `artifact` — `2l+1` best hit `\(2+1\)` ch06:326 (0.565): shared n-grams; not a twin.

## Consolidation (mode-5) — direction memos; conjecture-candidates are advice only

### Problem A — matrix-to-modular map
Ranked donors: 2503.18036 (generator-spectral criterion), 2111.03172 (relative-commutant
triviality), 2002.00018 (interaction modular H), 1006.4726 (modular-data rigidity);
internal: ch03:371-401 (constant-Θ Moyal check), appK:71-82, appH:2855-2866.
Obstructions: every donor presupposes either the metric or already-modular data (the
central A obstruction, visible as a corpus-wide negative); the book's own Weyl-data and
bound paragraphs give no spectral handle on H_D.
Dictionary gaps: sigma_t^fluct (appH:52) <-> standard-subspace one-parameter group;
K0 <-> "generator of positive group" of 2503.18036; triviality of relative commutants in
the matrix-net — never stated in book.
CC-A1 (conjecture; hypotheses: (i) matrix-net vacuum GNS with cyclic separating vector for
the diamond algebra; (ii) sigma_t from K0 extends to a positive one-parameter group with
standard-subspace data; (iii) a matrix-localized-at-infinity subalgebra implementing the
2111.03172 triviality criterion): reframe the missing step as two checkable claims —
spectral-subspace inclusion for the constructed algebras (2503.18036 criterion) plus
relative-commutant triviality — instead of a direct generator-to-H_D identity.
Differs from donors: they start from modular data; here (ii) IS the hard content.
A proof must establish the standard-subspace construction the donors assume; nothing here
closes A.
CC-A2 (conjecture; hypotheses: constant-Θ Moyal realization per ch03:371-401; free
quadratic H_quad; half-space/diamond limit of 2002.00018 applicable): candidate check —
first-order source variation of 2002.00018's modular Hamiltonian on the free vacuum
should match the first-order H_int variation of K0 up to the O(Θ^{3/2}) and O(R√‖δΘ‖+
‖H_int‖) allowances (appH:52, 81-83). A mismatch would constrain the dictionary; a match
is a consistency check at matching order, not closure.
Strongest donor: 2503.18036. Candidates: 2.

### Problem D1 — class selection
Ranked donors: hep-th/0303119 (vierbein/connection split in matrices), hep-th/0606163
(cited; finite-N covariant derivative), hep-th/0204078 (coordinate-invariant matrix
model), 1004.3009 (kinetic operator); internal: appH:2740 twin; ch10:291-307 (near
D-missing-step prose).
Obstructions: no external item formulates selection of an equivariant class by matrix
dynamics; the ghost/class machinery is isolated in-book (mode 4 items 2,4); Elitzur-type
locked-frame reading (appH:1533-1534) presupposes the connection content D1 needs.
Dictionary gaps: 𝕋,𝕽,𝔽 vs matrix structure constants + O(ħ_eff) corrections; Y_mu/X_mu
split vs ass:frame-lock composites; no in-book or corpus object for "the matrix equation
selects the class".
CC-D1 (mechanism; hypotheses: vacuum expectation of Phi admits a block decomposition
identifying frame and connection blocks as in hep-th/0303119; large-N expansion with
ħ_eff->0; ass:nondeg on the two-point composite): candidate claim — the class relation
coefficients 𝕋,𝕽,𝔽 are the O(1) and O(ħ_eff) structure-constant data of that block
decomposition, so D1 reduces to showing the matrix eom annihilate the 𝔽-slot on-shell.
Differs: their model imposes the split; NAMCG must derive selection. A proof must supply
the selection mechanism neither the donor nor the toy (appH:1530-1531) gives.
CC-D2 (conjecture; hypotheses: fuzzy-sphere vacuum with Λ^i=J^i and radius-one X_i per
appH:2734-2745 and 1531; both operators act on End(C^N) in the adjoint): candidate lemma
— the F-section vector branches l(l−1), l(l+1)+2, (l+1)(l+2) (appH:2740) are the ghost
Casimir values C_l = l(l+1) (appH:1531) re-indexed under the j⊗1 Clebsch-Gordan
decomposition (C_{l-1}, C_l+2, C_{l+1}); an operator identity, not just spectral overlap,
would connect the D toy to the F counting. Donor is internal + standard su(2) theory;
what a proof must add is the operator identity and the multiplicity map. If false, it is
a `notation-collision` hazard for the gatekeeper.
Strongest donor: hep-th/0303119. Candidates: 2.

### Problem E — Lorentzian signature
Ranked donors: 1607.04205 (thimbles beyond Gaussian), 2212.10127 (Lorentzian IIB
large-N with regulator), 2501.03752 (signature fluctuation), hep-th/0002050 (unique Wick
rotation contrast case), gr-qc/9802057 (metric-level signature maps; notation-collision
watch).
Obstructions: nothing in the corpus addresses a gamma->0- bridge at fixed quadratic data;
the E band statement δ>λ_*ε and λ_*=√(2+√2) are isolated in-book (mode 4 item 6); E's
top internal near-misses are all boilerplate (mode 2), so the E section is
mathematically unconnected to the rest of the book at prose level.
Dictionary gaps: R_u contour family <-> Lefschetz thimbles of a 2-parameter quadratic+
corner truncation; Pfaffian k<14 window <-> nowhere treated in corpus records.
CC-E1 (mechanism; hypotheses: action truncated to the quadratic terms of appH:1566-1573
plus the (r⁰)² corner terms; complexification in (ε,γ)): candidate computation — redo the
Stokes-band derivation with multi-parameter thimble technology (1607.04205-style) to test
whether δ>λ_*ε is the exact Stokes locus of the truncated model and whether the corner
exponents c0(u), Γ0(u) are thimble-invariant; a donor gives no λ_*; a proof must derive
the constant itself.
Strongest donor: 1607.04205. Candidates: 1 (a second E candidate was not supported by
any ladder result at this depth; stated plainly rather than forced).

## What this is not

Every number above is a similarity between embeddings or a token-overlap between LaTeX
strings. None of it removes a dependence on any NAMCG assumption, discharges any missing
step, or changes any status, priority or completion classification: the ledger's missing
steps remain missing proofs, not missing nearest neighbours. The cited records state what
their own abstracts state; comparison against the ledger's hypotheses is the researcher's
and gatekeeper's work. The full-text skeleton channel was not run, so method-level
transfer claims (CC-E1, CC-D1) rest on abstracts plus the manuscript's own text only.
