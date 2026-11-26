VECTORMIN: mode5-deepdig(G,N) | ENGINE: semantic:BAAI/bge-m3@5617a9f61b028005a4858fdac845db406aefb181 + lexical TF-IDF (formula + skeleton channels) | QUERIES: 8 arXiv searches + 9 verbatim blocks | HITS: 24 ranked / 24 verified-cached-records / 0 already-cited / 0 unverified (1 prior-run dup: 2608.05913, run-#2 FBC) | INTERNAL: 20 near-miss rows (10 G, 10 N; 3 G + 1 N self-echoes) + 6-doc skeleton channel | STATUS-EFFECT: none

# Deep dig #3 (mode-5): problems G and N

Order of work per coordinator: prose ranking + mode-2 + mode-4-lexical were flushed to this file
BEFORE the scoped skeleton fetch; the skeleton results are section 7. Nothing here changes any
status, priority or completion classification; every literature item is a pointer to a calculation
that still has to be checked against the ledger's hypotheses.

## 1. Source reading

- `make_digest.py --check` -> DIGEST CURRENT. HEAD 4be1328 (coordinator-corrected); working-tree
  appH sha c39e90f5b3431f81 — unchanged since run #2, no ledger drift. Re-chunk byte-identical vs
  run-#2 backups (`cache/chunks_book_preFBC.json`, `math_atoms_preFBC.json`): 1326 chunks / 10502
  atoms; `emb/chunks_P.npy` reused as-is (one model per index, pinned rev unchanged).
- Current ledger sections (from the file, not from advisory labels): **G** = appH:2766-2786
  (`sec:status-G`); G has NO `\paragraph{Missing step.}` — its missing-step equivalent is
  appH:2775-2778 + Status 2780-2785 + ch17 completion levels + the ch12 remark below.
  **N** = appH:3130-3261 (`sec:status-N`), Missing step at 3145-3154.
- N missing step verbatim (appH:3146-3152): "Derive from the matrix path integral that the graviton
  two-point function has no propagating Ostrogradsky ghost for \(p<\LUV\), for the values of
  \(\alpha\) and \(G_{\mathrm{eff}}\) computed in Problem~F (here \(\alpha\) is the Weyl-squared
  coupling of~\eqref{eq:stelle}, whose \(C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}\) coefficient is
  \(-\alpha/2\); with the continuation convention stated below, \(c_W=-\alpha/2\) in~\eqref{eq:W4};
  it is not any other coupling denoted \(\alpha\) in this book), with the region of those values in
  which it holds stated." Status (appH:3260): "Remains Assumption~\ref{ass:EFT-a2}."
- G verbatim (appH:2775-2778): "The boundary functional of Chapter~12 regulates
  \(\Lambda_{\mathrm{eff}}\) once an infrared entropy density is supplied. The working value
  \(\Lambda_{\mathrm{eff}}=3/L_{\mathrm{IR}}^2\) is a choice consistent with that functional, not a
  derived necessity." Status (2781-2785): "The mechanism is CLOSED CONDITIONALLY under the stated
  boundary entropy; derivation of the infrared entropy density and stationarity from the matrix
  theory is OPEN..."
- ch12:243-265 read IN FULL (G-critical): eq:Leff is dimensionally incomplete (LHS dim 4; eq:Sent-exp
  / eq:BY terms dim 3): "A boundary-to-bulk conversion of mass dimension one, with its normalization
  specified by the boundary geometry and variational prescription, is needed for that step. No such
  conversion is supplied here... Problem~G remains OPEN."
  Ledger observation (change nothing): this material G gap is recorded in ch12, not restated in the
  appH G section; G query blocks therefore include ch12 and ch17 passages alongside appH.
- ch17: G para 474-481; G completion levels 482-495 ("G is DERIVED only when the entropy density and
  stationarity relation are derived from the matrix theory... A scaling selected to reproduce a
  target remains an input."); N para 497-516 ("...derive from the matrix path integral, and not from
  Stelle's action~\eqref{eq:stelle}... A statement valid only for a truncated or imposed expansion
  leaves Assumption~\ref{ass:EFT-a2} in place and yields at most a scope-limited model.");
  items 700-732; label table 88-109.
- Notation pinned: ch09:62 eq:W4, :110-119 eq:stelle, :127-132 alpha<0 note, :140-145 ass:EFT-a2;
  ch12:109-121 eq:SHBEV, :138-156 ass:Sent-density + eq:Sent-exp, :171-179 eq:BY, :184-193
  ass:bdy-EE/eq:bdy-EE, :202-225 thm:Leff/eq:Leff/eq:EFE-Leff; ch08:186-217 thm:Geff, :223-228
  eq:Geff-structure; appA:69 eq:appA-a1, :77-95 eq:appA-a2; appH:3173-3195 (W_C,W_R,L;
  m2^2=-ΥΛ_UV^2/L, Υ:=π/(G_eff W_C Λ_UV^2)=A1/(2W_C); minimally-coupled scalars Υ=10);
  appH:3215-3243 (F(x), Lambert-W zeros, Υ*(0)=π/2, Υ*(δ_W)=δ_W for δ_W≥1, Υ=10 window
  −9.58<δ_W<10; illustrative proper-time integral, not the operator-specific δ_W).
- Read adjacency noted (no action): appH:1330-1350 (D section) matrix-side two-point-function
  sign/pole analysis ("Diagonal invariance alone does not impose t=t'=0 or m'=−m"); appH:235/294/333/381
  (B section) touch HBEV/boundary entropy (B->G dependency per ch17:492-495).

## 2. Corpus

8 arXiv API searches (max_results=60, sortBy=relevance, title+abstract only), themes derived from
the passages above; `cache/arxiv_gn/queries_meta.json`, `corpus.json`; raw Atom responses under
`arxiv_gn/raw/` (fetch script v2: per-query resume; first attempt hit an HTTP 429, retried with
backoff). totalResults / fetched: N1 203/60; N2 109/60; N3 62/60; N4 101/60; N5 17/17; N6 85/60;
G1 107/60; G2 325/60. 432 deduped records; masked title+abstract embedded with the pinned bge-m3
(`emb/corpus_gn_P.npy`, `corpus_gn_keys.json`).
Query blocks (9, verbatim, anchor-verified HEAD/TAIL, `cache/queries_gn.json`): G_workval
appH:2775-2778; G_status appH:2780-2785; G_ch17 ch17:482-495; G_Sent ch12:138-156; G_Leff
ch12:202-225; N_missing appH:3145-3154; N_weyl appH:3156-3184; N_ff appH:3215-3243; N_cond
appH:3245-3257. Pre-fixed ranking rules unchanged (per-problem max-cosine over its blocks, top-12,
tercile bands, no retuning). All hits are cached primary Atom records from export.arxiv.org
(title+abstract read; no full text except section 7's six documents).

## 3. Hits — Problem G

bands hi/mid 0.629/0.624; dist max/med/min 0.6522/0.5274/0.4278. Top-12 span only 0.617-0.652 ->
ordering confidence LOW; bands nominal. None cited in bib/namcg.bib; none a prior-run duplicate.

1. 1603.00112 (0.652 high) Topological induced gravity: G_N and Lambda arise as integration
   constants of field equations in a pregeometry/topological model; FRW solutions. Bearing: adjacent
   to "Lambda_eff not a free choice", but continuum field equations presupposed; supplies neither
   the ch12:256-258 dimension-one conversion nor a matrix-derived density. Does not discharge.
2. 2607.21536 (0.631 high) Non-Hermitian critical fermion chains: residual entropy log(Delta L),
   IR gap sensitivity below finite-size scale; dS RT-surface reading. Bearing: an IR-sensitive
   entanglement-scale datum of the kind ch17:479-480 invites, but in a 1-d critical system;
   supplies no alpha_i normalization for eq:Sent-exp.
3. 0912.4604 (0.631 high) DGP/CFT cosmology: bulk and induced 4D cosmological constants FIXED by
   absence of a conical singularity at the dS horizon; species bound. Bearing: closest retrieved
   analogue of "normalization specified by the boundary geometry" (a regularity condition fixes the
   conversion); hypotheses (brane-world, CFT species, Euclidean regularity) are not Namcg's.
   Candidate input for the researcher; status unchanged.
4. hep-th/0604014 (0.630 high) Induced-gravity brane FRW: effective Friedmann equations; branch
   ex=+1 gives effective Lambda + late acceleration. Bearing: external induced-gravity mechanism —
   per appH:2771-2772 such inputs support at most a scope-limited model.
5. 2409.08198 (0.629 mid) Holographic TTbar entanglement (A)dS3/CFT2: generalized replica method,
   analytic single-interval entropies. Bearing: replica machinery in a different object class.
6. 1602.06505 (0.627 mid) dS4 extremal surfaces vs ghost-CFT entanglement (c=-2): replica
   formulation; negative entropies. Bearing: cautionary sign adjacency only.
7. 1911.09302 (0.626 mid) Large-N entanglement entropy of 2-d Yang-Mills. Different object.
8. 1809.02944 (0.625 mid) Entropy of the spectral action (heat-kernel entropy functional).
   Neighbour of Namcg's own W-EH/appA coefficient bookkeeping; not boundary-entropy density.
9. 2504.01942 (0.624 low) dS entropy on-shell vs off-shell. Adjacent to thm:Leff proof-sketch
   on-shell step; different object.
10. 1311.1685 (0.620 low) Holographic spherical-domain entropies in AdS.
11. hep-th/0003206 (0.618 low) Inflation in higher-derivative induced gravity (action-level).
12. 1503.01766 (0.617 low) Strong-coupling YM entanglement (character methods).

Negative finding (G): no record in the 432 proposes deriving a boundary entanglement-density
expansion of eq:Sent-exp form TOGETHER WITH a dimension-one boundary-to-bulk conversion from a
microscopic quantum-mechanical (matrix) system. G2 territory is dominated by holographic/screen
phenomenology; the ch12 conversion datum has no near neighbour in this corpus.

## 4. Hits — Problem N

bands hi/mid 0.626/0.623; dist max/med/min 0.6830/0.5311/0.4097. Rank-1 separation real, rest
compressed (0.618-0.641). None cited; one prior-run duplicate flagged.

1. 2308.05251 (0.683 high) Anomaly-induced action of Weyl quantum gravity: finite local R^2 term
   from the second Schwinger-DeWitt coefficients of the fourth-order minimal and second-order
   nonminimal metric/ghost/gauge-fixing operators. Bearing: induced higher-derivative coefficient
   machinery for the fluctuation operators OF the Weyl-squared action; Namcg needs the two-point
   function of the composite metric with F-computed couplings. Coefficient-machinery donor; does
   not discharge.
2. 2309.01835 (0.641 high) Starobinsky + (-alpha C^2) on flat FLRW: vector ghosts for alpha>0;
   tensor sector 4 DOF, 2 ghosts; scalar ghost mixed with scalaron; no classical instability
   super-Hubble. Bearing: an alpha-sign -> ghost-content dictionary like N's "region of those
   values" asks for, but derived with the Weyl term as a UV input in the action — Namcg's step is
   that the pole structure FOLLOW from the matrix two-point function. Hypothesis mismatch IS the
   missing step.
3. 2607.00096 (0.630 high) Four-derivative UV-complete QFT on a Krein space: tree positivity via
   hidden ghost parity; counterexample to Ostrogradsky "as usually interpreted in QFT". Bearing:
   a consistent-ghost alternative; Namcg's criterion (ch:geometrogenesis item 6, appH:3153-3154)
   demands no propagating ghost below LUV and ass:EFT-a2 forbids extra diagonalized modes. Pointer
   only; does not discharge.
4. 0911.1168 (0.628 high) Covariant perturbation theory IV: heat kernel and one-loop effective
   action to third order in curvature; complete nonlocal form factors + spectral representations.
   Bearing: method donor for the BV-type form-factor control behind N's fixed-L caveat
   (appH:3215-3243) and Namcg's uncomputed δ_W; hypotheses are continuum curvature expansion.
5. 2005.10293 (0.625 mid) Fakeon unitarization of R+R^2+Weyl^2: ghosts removed as purely virtual
   particles; m_chi>m_phi/4 bound. Presupposes the quadratic action; imports the conclusion.
6. 1302.2336 (0.624 mid) Noncommutative spectral action: experimental bound on Weyl-term
   parameter beta. Phenomenology, not derivation.
7. 2308.11324 (0.624 mid) Quadratic gravity massless / partially-massless limits. Pole-spectrum
   adjacency to Namcg's m2^2, m0^2 display (appH:3188-3195) from the imposed action.
8. 2103.08555 (0.624 mid) Exact solutions of nonlocal gravity (almost-universal spacetimes).
9. 2608.05913 (0.623 low) [prior-dup FBC] Emergent gravitational action from nonlocal TTbar-like
   deformations. No new bearing.
10. 1707.00885 (0.623 low) Higher-spin gauge theory on fuzzy S^4_N. Fuzzy-matrix-geometry
    adjacency; cross-domain pointer only.
11. hep-th/0210006 (0.622 low) Black holes on a brane with induced gravity.
12. 2604.19707 (0.618 low) Unitary quadratic quantum gravity in 4D. Presumes quadratic action.

Negative finding (N): query N5 (graviton two-point/propagator x matrix/emergent/induced/
noncommutative) returned only 17 totalResults and its best hit ranked 11th. No retrieved abstract
performs a graviton two-point-function ghost analysis computed from a matrix path integral with
induced higher-derivative couplings. Reported negative, not an obstruction proof.

## 5. Mode-2 internal near-miss (bge-m3 P channel, reused index; no literature claims)

G (own appH section excluded): 1.000 ch17:482-495, 1.000 ch12:138-156, 1.000 ch12:202-225 are
self-echoes of the query blocks' own sources. Then 0.784 ch01:279-283 (HBEV overview); 0.772
appJ:75-77 ("infrared boundary entropy density and stationarity derived from the matrix..." —
limits NOT obtained); 0.753 ch12:253-277 (the dimensional-status remark); 0.751 appJ:50-57; 0.728
ch02:186-191 (boundary terms not optional); 0.700 appB:173-180 (boundary vs diamond entropy —
functional distinction bearing on G); 0.694 ch12:227-241 (thm:Leff proof sketch). No unconnected
partial calculation for G: every close passage is already cross-linked to G. The book's own nearest
neighbour to G's missing step is the ch12 remark itself.

N (own appH section excluded): 0.745 ch17:497-516 (self-echo); 0.722 ch09:108-132 (eq:stelle,
Ostrogradsky-as-veto); 0.714 appH:1873-1910 / 0.714 appH:2518 / 0.704 appH:2610 (F-section
conditional statements — N's stated dependence on F); 0.713 appH:317-322 / 0.711 appH:383 / 0.707
appH:427 (B cone-log coefficient / mode statements — B feeds W_C, A1 traces); 0.707 ch02:362-371
(SDW one-loop sketch); 0.707 appA:213-219 (weighted fibre trace N0 — enters Υ=10). Dependency
adjacencies, not missing links (appH:3148 already routes N through F). Duplicate-pair pass
(pre-fixed 0.90 threshold, run #1) carries over unchanged: chunks byte-identical.

## 6. Mode-4 lexical formula channel (TF-IDF over normalized LaTeX; LEXICAL, not semantic)

Targets G.SentExp ch12:146-153, G.BY ch12:171-179, G.Leff ch12:214-221, N.WL appH:3173-3177,
N.m2 appH:3188-3195, N.Fx appH:3229-3232. Results are intra-book and mostly symbol-co-occurrence:
- G.SentExp 0.565 ch12:355 (exercise S_ent=alpha0 LUV^3); rest repeated alpha0 LUV^3 / S_ent tokens.
- G.BY 0.539 ch12:350 (K^{ij}-Kh^{ij}); then T_bdy / h_ij pi^{ij} tokens.
- G.Leff 0.655 five sites carrying exactly S_ent^{(IR)} (ch12:271, ch16:226, ch16:357, ch17:476,
  ch17:663); next 0.348.
- N.WL 0.370 appH:1974, 0.325 appH:1999, 0.306 appH:2693, 0.284 appH:256 — the 1/32pi^2 heat-kernel
  coefficient skeleton; book-wide the nearest formula family to N's W_C/c_W display is Namcg's OWN
  F-section Weyl-term displays.
- N.m2 0.415/0.381/0.361/0.360 all appH same-section neighbours of the target (own-line exclusion
  covers only 3188-3195) — line-boundary artifacts, disclosed.
- N.Fx best 0.231: matches are the bare symbol delta_W — small-symbol artifact; no formula-level
  twin of F(x) exists inside the book.

## 7. Skeleton channel (mode-4 stage b; scoped: 6 NEW donor docs, LaTeXML alttext, alpha-strip;
fetched BEFORE was not allowed — run only after the section 3-6 flush)

Docs (all NEW; FBC-dup excluded): 2308.05251, 2309.01835, 2308.11324, 2604.19707 (N-side),
1603.00112, 1809.02944 (G-side). Raw HTML cached under `cache/arxiv_gn/html/`; formula counts
496/1189/840/276/275/419; output `cache/skeleton_gn.json`. Scores are LEXICAL skeleton n-gram
cosines on alpha-stripped LaTeX (variables -> wildcard '*'), per-channel, never averaged with
prose scores. Artifact disclosure: alpha-stripping collapses tensor identity (R_{\mu\nu\rho\sigma}
and C_{\mu\nu\rho\sigma} become the same wildcard skeleton) and short skeletons inflate cosines;
several top pairs below are flagged degenerate/boilerplate on that basis.

- `identity-twin` (with explicit ambiguity flag): the contracted-square skeleton
  *_{\mu\nu\rho\sigma}*^{\mu\nu\rho\sigma} at cos 0.931 recurs in all three quadratic-gravity
  donors (2309.01835, 2308.11324, 2604.19707) and matches manuscript atoms ch08:121
  (R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} inside the SDW a2 expansion), ch08:404, and
  ch17:507 / appH:3149 (C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma} in the N paragraph / missing step).
  Same contraction form; alpha-strip cannot tell Riemann^2 from Weyl^2 — compared hypotheses,
  not merged meanings: donors put the term in the action, Namcg has it as an induced coefficient.
- `notation-collision` HAZARD: 1809.02944's "\zeta(\cdot)" skeleton (spectral zeta) at 0.763 vs
  appH:1440 \zeta(y), which in NAMCG is a NULL LORENTZ VECTOR (\zeta\cdot y=\zeta\cdot\zeta=0,
  D section), not a zeta function. Also 1809.02944 "\mathrm{Tr}_{*}(*)=\mathrm{Tr}_{*}(*)" skeleton
  vs appH:2070 F_{ab}(Rp)=F_{ab}(p) (homogeneity/invariance statement) — same shape, different
  kind. Flagged for the gatekeeper; no meaning transfer.
- Convention check (clean): 2604.19707 "\eta_{\mu\nu}=\mathrm{diag}(-,+,+,+)" vs appH:2338
  diag(-,+,+,+,+), appH:887, ch02:32 (all (−,+,+,+)); "\hbar=* =1" vs ch12:244 units. No sign-
  convention collision found between these donors and the manuscript's pinned conventions.
- `representation-match` (weak): 1809.02944 "*=2*+1" vs appH:1531 N=2j+1 (fuzzy-sphere su(2)
  multiplet dimension) — spectral-multiplicity adjacency only.
- Degenerate small-skeleton pairs (disclosed, NOT interpreted): "*_{\mu\nu}=*_{\mu\nu}" 0.918/0.739
  vs appH:2140 G^{\mu\nu}=K^{\mu\nu}, ch07:85/172 h_{\mu\nu}=T_{\mu\nu}; "*=1,2,3" index ranges;
  "\zeta(*)", "*^{*}" token fragments.
- Negative (load-bearing): no donor full text contains a pole/resolvent-denominator skeleton
  resembling Namcg's propagator factors k^2(1-32\pi G_eff c_W k^2), k^2(1+96\pi G_eff c_R k^2)
  (appH:3183-3184) or F(x)=1-(x/\Upsilon)(\ln(1/x)+\delta_W) (appH:3229) above the 0.25 floor in
  these six documents. The form-factor-zero/Lambert-W structure of the N conditional paragraph has
  no full-text structural twin among the top-ranked N donors.

## 8. Direction memos and conjecture-candidates (advice for the researcher only; classification
per CLAUDE rule 6; confined to this file; nothing below is a result or a status)

### G memo
Ranked donors: 0912.4604 (regularity fixes constants) > 2607.21536 (IR-sensitive entropy scale) >
1603.00112 (constants as integration constants) > 1809.02944 (spectral-action entropy).
Obstructions found: none of the corpus supplies the ch12:256-258 dimension-one conversion; the
G-side literature operates with boundary models (the ledger's G-model territory). Dictionary gap:
no domain-X object maps to Namcg's "conversion normalization fixed by boundary geometry AND
variational prescription"; 0912.4604's Euclidean conical regularity is the closest but fixes a
number, not a conversion derived from a density.
CC-G1 (conjecture; mechanism by construction). (i) Missing step discharged if true: derivation of
the infrared entropy density and stationarity from the matrix theory (appH:2781-2785) together with
the conversion needed by ch12:256-258, so that Lambda_eff follows rather than being chosen
(appH:2777-2778; ch17:490-491). (ii) Its own hypotheses: the Problem-B replica construction
extends to a family of cone geometries over the actual boundary \partial M with deficit
2\pi(1-1/n); the n-derivative at n=1 of the resulting matrix-theory partition-function ratio
defines a boundary functional \Phi[\partial M] of mass dimension +1 whose normalization is fixed
by the boundary geometry and the ass:bdy-EE stationarity condition; large-tube limit exists. (iii)
Nearest donors: 0912.4604 (conical-regularity condition fixes bulk+induced constants) and
2409.08198 (generalized replica method); both differ by assuming brane/CFT or holographic-CFT
settings and by fixing constants rather than constructing \Phi from a microscopic density. (iv)
Classification: conjecture (mechanism by construction). (v) A proof must establish an explicit
\Phi with dimension +1 and pinned normalization, the derived ass:bdy-EE relation, and that
\Lambda_eff=3/L_{IR}^2 (or whatever value) FOLLOWS — none of which the donors do. If the ladder
result were merely a scaling consistent with the target, ch17:490-491 keeps it an input.

### N memo
Ranked donors: 2308.05251 (SDW coefficients of quadratic-gravity fluctuation operators) >
2309.01835 (alpha-sign -> ghost dictionary) > 0911.1168 (form factors to cubic curvature) >
2607.00096 (consistent-ghost alternative). Obstructions: every ghost/pole paper examined places the
quadratic terms in the action (the donor hypothesis Namcg must replace); the N5 matrix-side query
is a reported near-vacuum. Dictionary gap: no domain-X object for "matrix-path-integral graviton
two-point function with induced coefficients"; closest internal object is appH:1330-1350 (D-side
quadratic-form pole/sign analysis), which the book already knows.
CC-N1 (conjecture). (i) Missing step discharged if true: a derivation from the matrix path integral
that the graviton two-point function has no propagating Ostrogradsky ghost for p<LUV for the
F-computed (alpha, G_eff), with the region stated (appH:3146-3152); it would retire the fixed-L
truncation caveat at appH:3215ff and ass:EFT-a2's retained status at appH:3260 (STATUS-LANGUAGE
NOTE: description of what the ledger says would follow, not a proposal to change any label).
(ii) Its own hypotheses: flat background; one-loop; the fluctuation operator about the locked-block
background admits a Barvinsky-Vilkovisky-type proper-time representation; the truncation-
controlled F(x) approximates the exact inverse two-point function for |k|<LUV; the F outputs
(A1, W_C) are the ones entering \Upsilon=A1/(2W_C). Under these, the claim is that the ledger's
zero-free criterion (no zero of F in |x|<1 iff \Upsilon>\Upsilon*(\delta_W), \Upsilon*(0)=\pi/2,
appH:3236-3243) reduces N to TWO computable numbers: \Upsilon (already a Problem-F ratio) and
\delta_W (the logarithmic small-proper-time constant of the traced fluctuation semigroup, currently
the illustrative integral at appH:3233-3243, not operator-specific). (iii) Nearest donors:
2308.05251 (second Schwinger-DeWitt coefficients for the fourth-order minimal and second-order
nonminimal operators of Weyl gravity via heat-kernel Green functions) and 0911.1168 (all cubic
form factors); both differ because their operators are continuum metric/ghost/gauge-fixing
operators and neither addresses a sub-cutoff zero-free region. Internal skeleton channel: no full-
text twin of F(x) exists (section 7 negative). (iv) Classification: conjecture (mechanism by
construction). (v) A proof must establish: (a) the BV representation for Namcg's discrete
fluctuation operator; (b) \delta_W computed from the locked-block spectrum with the continuation
convention of appH:3160ff; (c) truncation-error control in |k|<LUV — that (c) is exactly what
distinguishes a derived result from "a statement valid only for a truncated or imposed expansion"
(ch17:514-516).
Obstruction note (not a candidate): 2309.01835's super-Hubble "formal ghosts, no classical
instability" pattern and 2607.00096's Krein-space positivity are routes to weakening N's demand;
both contradict Namcg's own criterion wording (item 6, no propagating ghosts) and ass:EFT-a2, so
they are alternatives to state, not inputs to N as written.
Cross-run: CC-N1 consumes Problem-F outputs; run-#2 CC-F1 (product-background a1/area reduction of
W_R/W_X functionals) is stated for product backgrounds, so applying it to the flat-background CC-N1
requires the flat case as a specialisation — a dependency, no collision. Run-#1 CC-D2 (F-vector
branches = ghost Casimir re-indexing) bears on the SIGN of W_C, hence on which side of the
G_eff W_C>0 tachyon branch (appH:3196) the criterion lands; CC-D2 remains neither strengthened nor
weakened by this run. CC-G1 and run-#2 CC-B1 address different data (B's replica tip coefficient vs
G's conversion functional); per ch17:492-495 B's derivation is a prerequisite of G, so no overlap
and no substitution.

## 9. Reproducibility

Scripts: `scratch/vector/{pin_queries_gn,arxiv_fetch_gn(v2),build_embed_gn,rank_gn,mode2_gn,mode4_gn,skeleton_gn}.py`;
cache: `scratch/vector/cache/{queries_gn.json, arxiv_gn/{queries_meta.json,corpus.json,raw/,html/},
rank_gn.json, mode2_gn.json, mode4_gn.json, skeleton_ids_gn.json, skeleton_gn.json}`;
`index_meta.json` updated with the run-#3 record. Same pinned bge-m3 rev; one model per index;
CPU torch (fine for this scale). Known artifacts (unchanged lineage): norm-regex `\(\\` alternation
(mode4), small-symbol inflation, line-boundary neighbours (disclosed inline). arXiv 429 on first
attempt handled by backoff; no query result fabricated or re-tuned.
