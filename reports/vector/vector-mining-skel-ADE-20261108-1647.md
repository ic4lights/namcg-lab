VECTORMIN: mode1b-skel+formula(A,D1,E) | ENGINE: semantic:BAAI/bge-m3@5617a9f61b028005a4858fdac845db406aefb181 (P-channel index REUSED, not re-embedded; BOTH channels run this session are LEXICAL TF-IDF: alpha-strip skeleton channel + normalized-LaTeX formula channel; scores per channel, never averaged, never comparable across channels) | QUERIES: 0 new arXiv API queries (directive: corpus exists); 8 donor full-text fetches = 8380 alttext formulas; 18 named manuscript formula targets (17 skeleton, 18 formula); 2 structural probes (K0-twin, inclusion-chain) | HITS: 0 NEW literature records — all 8 donors are run-#1 cached export.arxiv.org Atom records (verified primary in run #1); 0 already-cited-vs-bib among them (run-#1 check carried); 0 unverified | INTERNAL: targeted 18-target skeleton pass + generic donor->book pass (6335 rows ≥ floor, 2586 degenerate-flagged, 1181 both-sides-substantive) + inclusion/K0 probes + external formula channel 18×6 | STATUS-EFFECT: none

# Deep dig #1b — deferred external skeleton + mode-4 external formula channels for A / D1 / E

This run closes the run-#1 gap stated as "full-text skeleton DEFERRED, not saturated" for the A/D1/E
problems (run #1 report, `reports/vector/vector-mining-deepdig-ADE-20261108-1240.md`). Two lexical
external channels were built against the 8 donor full texts of run #1's A/D1/E corpus, and one explicit
structural question was answered (inclusion chain / K0 twin). No prose (P-channel) query was re-embedded:
the pinned bge-m3 index is unchanged and was not touched (one model per index).

**Status context (observation only, nothing changed here):** A remains OPEN, CRITICAL PATH for the
matrix-derived label, PROGRAMME-CONDITIONAL (appH:15-20); D remains OPEN, CRITICAL PATH (appH:647-651),
with D1 as its agenda-level sub-item (ch17; D1 references at appH:797, 950, 1534); E remains OPEN with
status "Remains Assumption~\ref{ass:lorentzian}." (appH:1578-1579). Every finding below is candidate
input for the researcher; statuses, priorities and completion classifications are untouched.

## 0. Discipline, drift checks, disclosures

- `python scripts/make_digest.py --check` -> `DIGEST CURRENT` (20261108-1614, rebuilt after the run-#4
  report writes). HEAD `4be1328`; `git diff HEAD -- chapters/` empty.
- appH hash provenance: raw-bytes sha1 `defdf09936bb6881132f97ddfd013fdcc8230314`; the ledger hash quoted
  in the coordinator brief ("c39e90f5…") is the digest's **sha256** of the same unchanged file (run-#1
  index_meta record). Different algorithm, same content — reported, not acted on.
- atoms-cache guard asserted at runtime in both scripts: `math_atoms.json` sha1
  `0fd705e37b64382f27778ea05957ed8f7e9f49d1` (unchanged since the run-#4 re-chunk; 10502 atoms). All 18
  named target indices were runtime-asserted against `(file, anchor-line)`.
- `cache/rank_ade.json` does not exist on disk (run #1 stored ranking in `cache/rank_ade.json`? — it is
  not in the cache directory). Donor set therefore = coordinator list, cross-checked against the run-#1
  report's ranked tables (all 8 are run-#1 ranked donors). Disclosed; nothing substituted.
- All 8 donor HTML fetched from `https://arxiv.org/html/<id>` (ar5iv fallback configured but never needed,
  including for the two hep-th ids). Raw bytes cached for audit.
- Unescape convention: **SINGLE** `html.unescape` for BOTH 1b sub-passes (skeleton and formula), so 1b rows
  are internally comparable; run-#4's generic skeleton pass used a double unescape — cross-run skeleton
  comparison is by construction only, never numeric identity.
- Formula-channel gram recipe is byte-identical to run-#4's internal formula channel (`norm_latex`,
  token n-grams 2..4, df≥2) **including its known `(` + `\` deletion artifact** (visible below as
  "Atilde", "P{-1})", "Osigma^2)") — preserved deliberately for comparability with run-#1/#4 formula
  numbers, and every score that depends on such a mangled string is flagged artifact, not interpreted.
  Deviation from run #4: queries here are the named **atoms** (verified indices), not re-extracted line
  spans; for displays the atom latex is the whole `\[...\]` block, so the query content is the same text.
- Channel-weighting bug disclosure: the first skeleton implementation computed idf per-side (manuscript
  vs donor) and produced cosines > 1; the bug was found and fixed (joint df) **before any number was
  recorded**; no pre-fix number appears anywhere in this report. A sparse-vocab-index bug was fixed in
  the same pre-recording phase.
- Bash safety-classifier outage at the start of this run (same pattern as run #4); recovered on retry;
  read-only work was interleaved while waiting.
- Skeleton target set = 17 named formulas; the formula channel adds `D1.TR` (appH:1477) as an 18th query
  because it is the vierbein/spin-connection split display named in the brief.

## 1. Query blocks (verbatim manuscript text, single-line start anchors from the atoms cache)

Ledger missing-step context (A, appH:111-118, quoted in run #1 and re-read this run):
> "An error-controlled identification of the algebraic inclusion generated by K_0 (or of
> [\hat X,\Phi]) with the modular Hamiltonian H_D of a causal diamond, or with the mutual-information
> functional U_ent[I(A:B)], that holds for the general (non-quadratic) matrix model before the
> composite metric is defined ..."

Named formula targets (each is the full atom text at the anchor):

| tag | anchor | verbatim |
|---|---|---|
| A.K0 | appH:25 | `K_0=\frac12\Theta^{-1\mu\nu}\operatorname{tr}\bigl(\hat X_\mu[\hat X_\nu,H_{\mathrm{quad}}]\bigr)` |
| A.bound | appH:52 | `\|\sigma_t^{\mathrm{fluct}}-\sigma_t^{\mathrm{free}}\| =O\bigl(R\sqrt{\|\delta\Theta\|}+\|H_{\mathrm{int}}\|\bigr)` |
| A.Weyl | appH:78 | `\([\widehat W_v,\widehat W_w]=2\mathrm i\sin(\tfrac{\theta}{2}\sigma(v,w))\,\widehat W_{v+w}\)` |
| A.assoc | appH:97 | `\([\Theta,\Theta]^{abc}\partial_af\,\partial_bg\,\partial_ch\)` |
| D1.classrel | appH:1444 | `[\mathcal S_{cd},\mathbb D_a]=\eta_{ad}\mathbb D_c-\eta_{ac}\mathbb D_d,\qquad [\mathbb D_a,\mathbb D_b]=-\mathsf T_{ab}{}^c\mathbb D_c+\tfrac12\mathsf R_{ab}{}^{cd}\mathcal S_{cd}+\mathsf F_{ab},` |
| D1.mateq | appH:1453 | `\bigl(-\mathbb D^a\mathsf T_{ab}{}^e+\mathsf T_{ab}{}^c\mathsf T^a{}_c{}^e+\mathsf R_{ab}{}^{ae}\bigr)\mathbb D_e+\tfrac12\bigl(\mathbb D^a\mathsf R_{ab}{}^{de}-\mathsf T_{ab}{}^c\mathsf R^a{}_c{}^{de}\bigr)\mathcal S_{de}+\bigl(\mathbb D^a\mathsf F_{ab}-\mathsf T_{ab}{}^c\mathsf F^a{}_c\bigr),` |
| D1.pair | appH:1466 | `S_2=\frac1{2g_{\mathrm{YM}}^2}\,\eta^{ab}\mathrm{Tr}\bigl(A_a(\mathcal EA)_b\bigr),\qquad (\mathcal EA)_b(m,m')=Q\cdot Q\,A_b(m,m')-Q_b\,Q^aA_a(m,m'),` |
| D1.TR | appH:1477 | `\mathsf T_{ab}{}^c=F_{ab}{}^c+y_gF_{ab}{}^{gc},\qquad\mathsf R_{ab}{}^{cd}=F_{ab}{}^{cd},` |
| D1.maxwell | appH:1481 | `\mathcal E^{(2)}{}_b{}^{de}=\partial^aF_{ab}{}^{de},\qquad \mathcal E^{(1)}{}_b{}^e+y_g\mathcal E^{(2)}{}_b{}^{ge}=-\partial^aF_{ab}{}^e,\qquad 2\mathcal E^{(3)}{}_b=\partial_c\mathcal E^{(1)}{}_b{}^c-\eta_{bg}\mathcal E^{(2)}{}_c{}^{gc}.` |
| D1.comp | appH:1493 | `\begin{pmatrix}O(\sigma^2)&\varkappa\\\varkappa&O(\sigma^2)\end{pmatrix},\qquad \varkappa=-\frac{\sigma}{\sqrt2}\sqrt{v^g\mathsf G_{gh}v^h}\,\bigl(1+O(\sigma^2)\bigr),` |
| D1.refl | appH:1519 | `\bigl\langle\phi_r{}^g(y)\,\phi_s{}^h(y')\bigr\rangle=g_{\mathrm{YM}}^2\,\mathcal V\,\delta_{rs}\,\mathsf G_{gh}\,\frac1{4\pi^2|y-y'|^2},` |
| D1.su2 | appH:1531 | `\([X_i,X_j]=\mathrm i\hbar_{\mathrm{eff}}\varepsilon_{ijk}X_k\)` |
| D1.spec | appH:1531 | `\(\{l(l+1):0\le l\le N-1\}\)` |
| E.contour | appH:1552 | `\(A_0=\mathrm e^{-3\pi\mathrm iu/8}\tilde A_0\)` |
| E.limit | appH:1557 | `\lim_{\epsilon\to0^+}I_\epsilon[O]=\mathrm e^{7\pi\mathrm i(N^2-1)/4}\int\mathrm d\tilde A\;O\bigl(\mathrm e^{-3\pi\mathrm i/8}\tilde A_0,\mathrm e^{\pi\mathrm i/8}\tilde A_i\bigr)\operatorname{Pf}\mathcal M(-\mathrm i\tilde A_0,\tilde A_i)\,\mathrm e^{-S_{\mathrm E}(\tilde A)},` |
| E.lamstar | appH:1570 | `\(\lambda_*=\sqrt{2+\sqrt2}\)` |
| E.c0 | appH:1570 | `\(c_0(u)=\sin^2(3\pi(1-u)/8){(r^0)}^2/(16\cos(3\pi u/4))>0\)` |
| E.Gamma0 | appH:1573 | `\(\Gamma_0(u)=g_{\mathrm{YM}}^2\sin^2(3\pi(1-u)/8){(r^0)}^2/(8\sin(3\pi u/4))>0\)` |

## 2. Corpus

- 0 new arXiv API queries. Donor ids and records are the run-#1 cached Atom records
  (`scratch/vector/cache/arxiv_ade/corpus.json`, 173 records; all 8 ids present, titles verified in run #1).
- Full texts (this run): `2503.18036` 1005 formulas, `2111.03172` 1022, `2002.00018` 774,
  `hep-th/0303119` 584, `1704.01336` 3539, `1004.3009` 356, `1607.04205` 952, `2212.10127` 148
  = **8380** alttext formulas. Raw HTML under `scratch/vector/cache/arxiv_ade/html/`;
  id list `scratch/vector/cache/skeleton_ids_ade.json`.
- Scripts (re-runnable): `scratch/vector/skel_ade_fetch.py` (fetch), `scratch/vector/skeleton_ade.py`
  (targeted + generic + probes), `scratch/vector/mode4_ade_ext.py` (formula channel).
  Outputs: `cache/skeleton_ade_targeted.json`, `cache/skeleton_ade.json`, `cache/skeleton_ade_probe.json`,
  `cache/mode4_ade_ext.json`. Reproducibility record in `scratch/vector/index_meta.json` (run1b) and
  `cache/run1b_hashes_r1.txt` / `_r2.txt`.

## 3. Skeleton channel, TARGETED pass (OFFICIAL numbers)

Method (identical to run-#4 targeted): alpha-strip (`\commands`, numerals, greek kept; single Latin
letters -> `*` runs collapsed), TF-IDF token n-grams 2..4, joint df≥2 (manuscript atoms + donor
skeletons), cosine, pre-fixed floor 0.25. Fragment/degenerate rows are disclosed with their token counts
and NOT interpreted.

Best cosine per target against the 8380 donor skeletons, and per-donor maxima:

| target | best overall | above floor? | per-donor maxima (2503 / 2111 / 2002 / 0303119 / 1704 / 1004 / 1607 / 2212) |
|---|---|---|---|
| A.K0 | 0.152 | no | .083 / .152 / .060 / .084 / .115 / .053 / .082 / .063 |
| A.bound | 0.250 | fragment only (1704#2487 `\|\xi\|=1`, 3-token) | .206 / .249 / .135 / .107 / .250 / .068 / .061 / .038 |
| A.Weyl | 0.206 | no | .190 / .147 / .097 / .080 / .206 / .069 / .116 / .069 |
| A.assoc | 0.139 | no | .065 / .065 / .088 / .039 / .065 / .139 / .116 / .040 |
| D1.classrel | 0.166 | no | .164 / .164 / .164 / .164 / .164 / .164 / .166 / .164 |
| D1.mateq | 0.212 | no | .132 ×6 / .212 (1607, fragment `e^{i}{}_{a}`) / .132 |
| D1.pair | 0.152 | no | .145 / .126 / .080 / .120 / .152 / .087 / .079 / .049 |
| D1.maxwell | 0.285 | fragment only (1607#715 `E^{(1)}`, 3-token) | .102 / .088 / .142 / .089 / .107 / .088 / .285 / .088 |
| D1.comp | 0.152 | no | .075 / .072 / .067 / .088 / .083 / .152 / .086 / .067 |
| D1.refl | 0.114 | no | .094 / .103 / .096 / .094 / .095 / .103 / .107 / .114 |
| D1.su2 | 0.203 | no | .118 / .203 / .099 / .102 / .181 / .131 / .099 / .099 |
| D1.spec | 0.345 | fragments only (2002#771/#736 `(b+1)`, 5-token) | .180 / .107 / .345 / .152 / .191 / .226 / .050 / .059 |
| E.contour | 0.112 | no | .067 / .080 / .081 / .042 / .081 / .080 / .046 / .112 |
| E.limit | 0.116 | no | .116 / .096 / .081 / .045 / .093 / .096 / .069 / .077 |
| E.lamstar | 0.161 | no | .076 / .128 / .076 / .043 / .161 / .128 / .102 / .086 |
| E.c0 | 0.102 | no | .057 / .065 / .102 / .057 / .091 / .065 / .073 / .067 |
| E.Gamma0 | 0.128 | no | .084 / .108 / .106 / .057 / .128 / .080 / .071 / .068 |

Reading stated plainly: at skeleton level, **every named A/D1/E formula is isolated or fragment-level**
against these eight donor full texts. The only rows at/above 0.25 attach to micro-fragments
(`‖ξ‖=1`, `E^{(1)}`, `(b+1)`) and are disclosed as artifacts, not findings. Structural relative worth
recording without a score claim: the closest K0-family skeleton in hep-th/0303119 is
`* _ { \mu \nu } = [ * _ { \mu } , * _ { \nu } ] - * \theta _ { \mu \nu } ^ { - 1 }` at 0.084 — their
noncommutativity-parameter/commutator relation, a *different object* from the book's
`K_0=\frac12\Theta^{-1\mu\nu}\operatorname{tr}(\hat X_\mu[\hat X_\nu,H_{\mathrm{quad}}])`, and far below floor.

## 4. Explicit probes (answered as found)

Question put by the coordinator: does any donor full text contain a skeleton twin of the
**modular-inclusion chain** or of the **K0 generator identity**?

- **K0 twin: NO.** Best skeleton cosine 0.152 (below the 0.25 floor); best formula-channel cosine 0.206
  and every formula-channel top row for A.K0 is a micro-document (`H_{1},H_{2},H_{3}`, `(H_{1},H_{2})`
  from the 1704.01336 survey). No donor full text displays a generator built as
  (inverse-Poisson tensor) × trace(X [X, H]).
- **Inclusion chain: the donors have them; the book does not (at display-skeleton level).**
  `\subset`-bearing donor skeletons: 2503.18036 = 112 (family e.g. `(H,U_{1})\subset(H,U_{2})`),
  2111.03172 = 58 (family e.g. `\mathcal{M}_{t}\subset\mathcal{M}_{s}`), 1704.01336 = 1, others 0.
  The manuscript contains exactly **3** atoms whose skeleton contains `\subset`:
  appH:1440 `\(\mathfrak{so}(3,1)\subset\mathfrak{so}(4,1)\)`,
  appH:1443 `\([\hat X_a,\mathcal A]\subset\mathcal A\)`,
  appH:2338 `\(y^\perp\subset\mathbb R^{1,4}\)` — none is a nested inclusions-of-von-Neumann-algebras
  or one-parameter-group chain. Both probe directions (inclusion-family donors -> book; book `\subset`
  atoms -> donors) return only degenerate small-atom pairings (best 0.401: the 7-token book atom
  `so(3,1)⊂so(4,1)` vs the 2-token donor skeleton `\mathfrak { * }`; inclusion-direction best 0.343
  `(H,U_1)⊂(H,U_2)` vs book atom `\(c_W,c_R,c_{\mathrm{GB}}\)`).
  **Conclusion as found: negative in both directions — the book's inclusion statements (including the
  A-section half-sided-inclusion discussion) exist only in prose, never as a displayed skeleton.**
  This is a structural observation about notation density in the manuscript; it is NOT a statement
  that any inclusion chain is proved, derivable, or disproved.

## 5. Skeleton channel, GENERIC pass (secondary)

8380 donor skeletons -> best manuscript atoms, floor 0.25: 6335 rows; 2586 flagged degenerate (<6 tokens
on either side). Restricting to both-sides-substantive (≥12 tokens): 1181 rows; top rows:

| cos | donor -> book atom | note |
|---|---|---|
| 0.642 | 1704.01336#2663 -> appH:2460/2477/2608 `\(\mathbb{CP}^{1,2}\)` | name-level, tiny book atom |
| 0.613 | 1607.04205#142 -> ch08:293 / ch03:77 / appH:1088 `\(g^{(0)}_{\mu\nu}\)` | symbol-level only |
| 0.609 | 1704.01336#1174 -> appH:2409 `\(Q^{-1/2}F_{ab}Q^{-1/2}\)` | donor is `S=S^{-1}=\Delta_{V}^{-1/2}J_{V}^{-1}=J_{V}^{-1}(J_{V}\Delta_{V}^{-1/2}J_{V}^{-1})`; inverse-conjugation pattern; F-region atom, outside A/D1/E scope — pointer for gatekeeper awareness only |
| 0.578/0.556/0.529 | 1004.3009#308 -> appH:2615/2632/2659 `\(T^{ab\mu}=\eta^{a\mu}y^b-\eta^{b\mu}y^a\)` etc. | donor alttext is `\Delta_{x^{A\mu}y^{A\mu}}` — the match is a superscript-pattern degeneracy, NOT an angular-momentum twin; disclosed |
| 0.551 | 1004.3009#298 -> appH:2309 `\(p^{\mu}T_{\mu\nu}=0\)` | donor is `p_{\mu}p_{\nu}\eta^{\mu\nu}=0`; different equation, same token family |
| 0.545 | 1704.01336#3512 -> appH:2070 `\(F_{ab}(Rp)=F_{ab}(p)\)` | G-region |
| 0.535 | 1704.01336#1174 -> appH:2413 `\(Q^{-1/2}FQ^{-1/2}\)` | as above |
| 0.517 | hep-th/0303119#227 -> appH:2140 `\(G^{\mu\nu}=K^{\mu\nu}\)` | symbol-level |

Generic rows are dominated by shared small-atom superscript/symbol patterns and land mostly in F/G-region
book atoms, not in the A/D1/E sections under mining. No generic row constitutes a calculation; none is
interpreted beyond pattern disclosure.

## 6. Mode-4 EXTERNAL FORMULA channel (per-channel; never averaged with P or skeleton)

18 named atoms vs 8380 donor formula strings (normalized LaTeX; gram recipe of run-#4 internal channel).
Class label per hit = one of `identity-twin / notation-collision / representation-match / method-donor`
(plus `artifact` for mangled/micro-document rows). No hit is an identity-twin.

| target | top non-artifact rows | class | what the donor row is, and the gap |
|---|---|---|---|
| A.K0 | 1704.01336#1801 `H_{1},H_{2},H_{3}` (0.206), `(H_{1},H_{2})` family | artifact | no external counterpart of the K0 generator identity |
| A.bound | 2111.03172#955 `\|\sigma_{t}(L^{*})Q_{n}^{\perp}\Psi_{A^{*}}\|` (0.195), #950 (0.182) | method-donor (weak) | 2111.03172 bounds norms of modular-group expressions against projections; the book bounds a state-restriction difference by `R\sqrt{\|\delta\Theta\|}+\|H_{\mathrm{int}}\|`. Different objects, different hypotheses; supplies only a hint that norm-estimate scaffolding of that shape exists in the modular-theory literature |
| A.Weyl | 1704.01336#1384 `h(v,w):=(v,w)+i(v,Cw)` (0.364), #1253 `h(v,w):=\langle v,w\rangle=(v,w)+i\omega(v,w)` (0.359), #1255 `\omega(v,w)=(v,Cw)` (0.354), #2988 `W(v)W(w)=e^{-i\,\mathrm{Im}\langle v,w\rangle/2}W(v+w)` (0.182) | **representation-match** | the survey's one-particle Weyl-system data (complex inner product / symplectic form / Weyl phase) vs the book's finite-dimensional 't Hooft pair with phase `2\mathrm i\sin(\tfrac{\theta}{2}\sigma(v,w))`. Same *kind* of structure (Weyl system over a symplectic pair), different phase law (exponential of Im pairing vs bounded sine of the lattice 2-cocycle) and different hypotheses (abstract regular one-particle space vs N×N unitaries). Hypotheses compared, meanings NOT merged |
| A.assoc | 1004.3009#214 `\partial_{0}` etc. | artifact | associator skeleton isolated externally |
| D1.classrel | hep-th/0303119#577 `[\gamma_{ab},\gamma_{cd}]=2\eta_{ad}\gamma_{bc}+\eta_{bc}\gamma_{ad}-\eta_{ac}\dots` (0.325), #578 anticommutator (0.321), #165 `M_{ab}=-\frac12\epsilon_{abcd}M_{cd}` (0.257), #170 `N_{ab}=+\frac12\epsilon_{abcd}N_{cd}` (0.245) | **representation-match** | the same donor's Clifford/Lorentz-generator η-contraction algebra and its self-dual/anti-self-dual (M,N) split vs the book's `[\mathcal S_{cd},\mathbb D_a]` / `[\mathbb D_a,\mathbb D_b]` with coefficient fields `\mathsf T,\mathsf R,\mathsf F`. Donor generators are c-number/Clifford objects; the book's are operator-valued derivations. Index-skeleton resemblance only |
| D1.TR | hep-th/0303119 `M_{ab}`/`N_{ab}`/`\gamma_{ab}` single-symbol rows (0.24-0.29) | artifact | no external twin of the `\mathsf T=F+y_gF,\ \mathsf R=F` split display |
| D1.pair / D1.mateq / D1.comp / D1.refl | `\eta^{ab}` (0.223), `\gamma_{ab}` (0.243), 1607.04205#433 `\mathcal{K}_{\sigma'}` (0.356, artifact via pmatrix mangle), 1704.01336#3330 `\langle\xi,\eta\rangle_{D}=\int\overline{\xi(x)}\eta(y)\,dD(x,y)` (0.133) | artifact; D1.refl row = representation-match (weak) | the survey defines an inner product from a positive two-point kernel dD(x,y) — conceptually adjacent to the book's reflected two-point function but far below any claim threshold |
| D1.su2 | 1704.01336#981 `\mathfrak{aff}(\mathbb R)` (0.195), `X_{\mu}` fragments | artifact | no su(2)/fuzzy-sphere spectrum donor exists in this donor set |
| D1.spec | `P{-1\})=0` (0.366, brace-mangle artifact), 2002.00018#476 `\{100,101,110,111\}` (0.274) | artifact | the book's `\{l(l+1):0\le l\le N-1\}` has no external twin among these 8 donors (CC-D2's comparators were book-internal: appH:2740 vs appH:1531) |
| E.contour | 2212.10127#107 `\pi/8` (0.146) | notation-collision (low confidence) | both sides rotate a contour by a rational multiple of π; the donor's π/8 is a fixed complex-Langevin/parameter rotation in Lorentzian type IIB, not the book's u-dependent contour weights. Symbol-level watch only |
| E.limit | `\mathcal{A}(\mathcal{O})\subset\mathcal{A}(\tilde{\mathcal{O}})` 2111.03172#13 (0.123) | artifact | below floor; noted because it is an inclusion row seen through the second channel — consistent with §4: no book-side twin |
| E.lamstar / E.c0 / E.Gamma0 | 1704.01336 `\sqrt{D}`, `\sqrt{2}Pv` rows (0.16-0.22); 2002.00018#439 `(3,4,5)` (0.128) | artifact | the Stokes-band data (λ\*, c0(u), Γ0(u)) is isolated in BOTH external channels |

## 7. Notation-collision hazards for the gatekeeper (symbol-level, low confidence, no score claims)

1. **σ-family**: book `O(\sigma^2)` compression expansion (appH:1493-1496) vs `1004.3009` Pauli-σ basis
   labels `f_d=i^{d_0}(\sigma^1)^{d_1}\dots` vs `1607.04205` thimble labels `σ, σ'` in
   `\tau_\sigma,\ \phi_R=-(\sigma+1)\pi`. Three unrelated σ families meet in this corpus.
2. **𝓔^{(1)}**: book's linearized-EOM slots `\mathcal E^{(1,2,3)}` (appH:1481) vs `1607.04205`
   `E^{(1)}=E^{(1)}_{\rm pert}+E^{(1)}_{\rm bion}` (energy of a bion sector). Different objects, same label family.
3. **π/8**: book contour phases `e^{-3\pi\mathrm iu/8}`, `e^{\pi\mathrm i/8}` (appH:1552, 1557) vs
   `2212.10127` fixed rotation angle `\pi/8`. Coincidental symbol adjacency, different roles.

None of these is evidence of anything except that the same glyphs recur across unrelated literatures.
They are listed so that any future citation pairing checks the definitions first.

## 8. Cross-run consistency (run #1 candidates; strengthened / weakened / untouched — none forced)

- **CC-A1** (reframe the A missing step as a spectral-subspace-inclusion criterion + relative-commutant
  triviality, donors 2503.18036 / 2111.03172): **untouched.** The skeleton channel confirms the donors'
  inclusion apparatus exists at display level (112 + 58 `\subset` skeletons, incl. `(H,U_1)⊂(H,U_2)`
  and `\mathcal M_t⊂\mathcal M_s` — concrete target notation for the reframe) and equally confirms the
  book currently states its inclusions only in prose. Neither fact supplies or blocks the step.
- **CC-A2** (first-order source variation of the 2002.00018 modular Hamiltonian vs first-order
  H_int variation of K0): **strengthened as a necessity, not as progress.** A.K0 now has no twin in
  EITHER external channel (skeleton 0.152, formula 0.206 both below/at fragment level) and run #1's
  internal channel gave 0.245 — the comparison CC-A2 proposes cannot be shortcut by citation; it must
  be constructed. The 2111.03172 norm-fragment rows (§6, A.bound) are weak method-donor adjacency for
  that construction. Candidate status unchanged: conjecture.
- **CC-D1** (𝕋, 𝕽, 𝔽 as O(1)/O(ħ_eff) structure-constant data of the hep-th/0303119 block
  decomposition): **strengthened as dictionary availability.** The same donor now shows explicit
  formula rows for its self-dual/anti-self-dual split (`M_{ab}=-\tfrac12\epsilon_{abcd}M_{cd}`,
  `N_{ab}=+\tfrac12\dots`, 0.245-0.257) and η-type generator algebra (0.32-0.33) — the candidate's
  proposed correspondence (their (M,N,γ) slots <-> the book's 𝕊/𝔻 slots and coefficient fields) has a
  visible source-side vocabulary. What differs remains what always differed: they decompose
  c-number/Clifford Lorentz generators; the book needs the coefficients of operator-valued derivations
  to satisfy its class relations on shell. Candidate status unchanged (mechanism/conjecture).
- **CC-D2** (F-section vector branches vs the su(2) Casimir tower at appH:1531 re-indexed):
  **untouched.** No su(2)-spectrum computation exists among these 8 donors (D1.spec rows are artifacts);
  CC-D2's comparators are book-internal, and run-#2's conclusion carries.
- **CC-E1** (redo the Stokes-band derivation with 1607.04205-style multi-parameter thimble technology):
  **untouched.** λ\*, c0(u), Γ0(u) are isolated in both external channels; no thimble paper in the set
  computes anything with these coefficients. The transfer remains method-level advice exactly as stated
  in run #1.

**No new `conjecture-candidate` is supported by this ladder run.** The honest output of two external
full-text channels on eighteen named formulas is a set of negatives plus two representation-match
pointers; forcing a new candidate here would be a rule violation, so none is filed.

## 9. Reproducibility record (run-#4 lesson applied)

- Every official number in this report is produced by a file-persisted script
  (`skeleton_ade.py`, `mode4_ade_ext.py`), runtime-guarded on the atoms-cache sha1 and on target
  (file, line) anchors — no heredoc-only passes this run.
- Both scripts were executed twice; the four JSON outputs are **byte-identical** across reruns:
  sha1 targeted `3fb0f2a573178b25e57b76d1e6a38fcb94e8af3a`, generic
  `c633115b329db0378592b7a854c4dcb9a8cbbf34`, probe `bfa156547ffa08b421a9e654a02934b201fd8c15`,
  formula `36fcb3203a30bc040e96b963767001c2677584cf` (`cache/run1b_hashes_r1.txt` / `_r2.txt`).
- Two implementation bugs (per-side idf; sparse vocab indexing) were caught by a cosine>1 sanity signal
  and fixed BEFORE the official run; the buggy runs produced no recorded numbers.
- `scratch/vector/index_meta.json` carries the full run1b record (engine pinned, 0 new API queries,
  fetch counts, single-unescape convention, hash guards); prior run records preserved.
- Engine note: the pinned bge-m3 index was NOT re-embedded or queried this run; both channels are
  lexical TF-IDF, which is stated in the machine line. CPU-only .venv (torch 2.15.0+cpu); no installs.

## 10. What this is not

Nothing in this report changes the status of any problem. A skeleton-channel negative (no twin of K0,
no twin of an inclusion chain) does not mean the A missing step is unproveable, and a
representation-match pointer (the 1704.01336 Weyl-system data; the hep-th/0303119 self-dual split) does
not mean those papers' results apply to NAMCG's hypotheses — they prove statements about their own
objects, quoted from their own records, under their own hypotheses. Vector and skeleton proximity are
similarity, not derivation: the ledger's missing step (the error-controlled identification of the
algebraic inclusion generated by K_0 with H_D of a causal diamond, for the general non-quadratic matrix
model, before the composite metric is defined — appH:111-118) remains exactly as stated, and these
items are candidate inputs for the researcher, to be re-derived by the gatekeeper if they are ever used.
