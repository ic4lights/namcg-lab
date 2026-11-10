# Proposal 064-f-fibre-level-response-q0-trace, round 1

## Result

P1 (central). The recorded item "the response of the fibre levels to \(\bar h\) in
\(v^M-2\sigma^M\) ... is not computed" (appH L2797; named by the 062 paragraph at L2825 as the
surviving candidate \(\mathcal M\)-provider) is computed for one channel component: the pure-trace
\(q=0\) wave \(\bar h_{\mu\nu}=(t/4)\bar g_{\mu\nu}\) of the 062 set of paragraphs, under the frozen
symbol and equal-weights hypotheses of that set plus the stated response hypothesis (the fibre
coordinate \(y\) and \(m\) held, the contraction \(y\cdot y\) taken in the fluctuated metric). The
response does NOT vanish. Within that class the wave moves exactly one datum,
\(\vartheta=\coth^2\tau=-y\cdot y/m^2\) (anchored L2698, L2718): \(\vartheta\to(1+t/4)\vartheta\)
exactly, while \(\mu_J\), \(c_J=J(J+1)\), \(M_A^2=\chi^2\mu_A^2\) and
\(\mathcal D=M_A^2+\mu_J\) do not move. Consequences derived per level, for both recorded level
summands of the first term (L2793/2795): beyond the determinant profile of 062 there is an extra
tadpole and an extra quadratic part, for the recorded bracket
\(B=\tfrac{15\vartheta^2}{4\mathcal D}-\tfrac{\vartheta c_J}{\mathcal D^2}+\tfrac{2c_J^2}{\mathcal D^3}\)
equal to \(\vartheta(15\vartheta\mathcal D-2c_J)/(8\mathcal D^2)\) and
\(\vartheta(75\vartheta\mathcal D-8c_J)/(64\mathcal D^2)\), and for the \(\mathrm ds/s\) proper-time
summand \(S=\tfrac{15\vartheta^2}{4\mathcal D^2}-\tfrac{2\vartheta c_J}{\mathcal D^3}+\tfrac{6c_J^2}{\mathcal D^4}\)
equal to \(\vartheta(15\vartheta\mathcal D-4c_J)/(8\mathcal D^3)\) and
\(\vartheta(75\vartheta\mathcal D-16c_J)/(64\mathcal D^3)\); each pair is levelwise positive when
\(15\vartheta\mathcal D>4c_J\) (which implies both quadratic sign conditions). The extra parts do not
run along the 062 fixed profile with ratio \(T/\mathcal M=4\): e.g. the bracket-form extra ratio is
\((75\vartheta\mathcal D-8c_J)/(8(15\vartheta\mathcal D-2c_J))\), so the 062 cancellation argument
does not bind them. The \(\vartheta\)-linear part of \(U_2\) (L2779) responds as \((1+t/4)^3\) against
the profile \((1+t/4)^2\). What is NOT established: the sign and magnitude of the full
\(\mathcal M\) (the sums over \(A\) and \(J\le n\) at the cut-off \(\mathcal D\gg\vartheta\) are not
performed), the response of the flux insertions and weights, and the Yukawa-versus-tachyon
comparison, which stays convention-bound (the ratio \(\sqrt{|g|}m^8/2\) of L2825, re-derived in
script A6). Problem F stays OPEN.

P2 (bookkeeping). What P1 retires: the recorded item at L2797 "The response of the fibre levels to
\(\bar h\) ... is not computed", and the corresponding clause of the 062 closer at L2825 ("they do
not compute the fibre-level response"), each only for the pure-trace \(q=0\) channel component just
computed. What P1 does NOT retire: no item of the Problem F "Missing step." block (L1653-1660, the
gauge-fixed operator/heat-kernel \(a_1,a_2\) programme), no item of the Chapter 17 Problem F target
(ch17 L403-412), the remaining not-computed items inside the 062 closer (loop kinetic term of
\(\chi\), second-order non-derivative terms at \(\chi^2\lesssim\vartheta\), rotating class, higher
loops), or the other components of the fibre-level response (non-trace channels, flux-insertion and
weight response). No ledger or agenda passage is edited; the retirement is recorded only inside the
scoped closer of the new conditional paragraph.

## Target and status

Problem F (`sec:status-F`, appH L1641+). Current recorded status, re-read this round at L1644-1647:
Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result:
treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN. Chapter 17 (L403-412): "CRITICAL PATH;
OPEN", target: evaluate the weighted \(a_1\) and curvature-linear \(a_2\) on the locked block with a
stated scheme. Dependencies: the locked block, ghost operators, radial-mode threshold, continuation,
counterterm scheme. This package is PROGRAMME-CONDITIONAL evidence inside the static-response
chain of the same Problem (the 062 non-derivative sector), advancing one recorded missing item for
one channel component. It DERIVES nothing on the critical path end-to-end. Status labels: unchanged
by this proposal (the `simulate_apply.py` run certifies the Status/Priority/Completion block
byte-identical). Critical-path set re-derived from ch17 and the ledger snapshot: A, B, C, D1, E, F,
G-derived, N. Discrepancy flag: the L1653-1660 missing-step block describes the heat-kernel route,
while the 062/L2825 chain pursues the reduced-\(t\)-form \(\mathcal M\); both are recorded under F,
and this package belongs to the second; no silent conflation is made here.

## Source reading

digest + targeted reads. Files read in full at the relevant ranges: appH L1641-1660 (F ledger),
L2640-2657 (factorisation), L2691-2698 (fibre-constant class, \(\vartheta=\coth^2\tau\)), L2718
(\(\vartheta=-y\cdot y/m^2\) off \(y^i=0\)), L2775-2781 (potential \(U_4,U_2\), static-channel
rigidity), L2783-2797 (\(\beta_K\), fibre flux level form, not-computed item), L2809-2825 (reduced
\(t\)-form, vacuum term, \(V=T\)/equal-weights, consequence, closer, 062 paragraph); ch17 L38,
L403-412, L653-680 (F criterion and agenda items); proposals/062 (proposal rounds and review) read
before compaction. reports/sme-scout-20261109-*.md skimmed for routes (no route imported). No
unreadable files.

## Research and reasoning

Setting. The 062 paragraph (L2825) proves that every \(q=0\) density term of the form
\(W_i\sqrt{|g|}\) in the trace channel runs along the single profile
\(\sqrt{|g+h|}=\sqrt{|g|}(1+t/2+t^2/16+O(t^3))\), with \(T_i=-\sqrt{|g|}W_i/2\),
\(\mathcal M_i=-\sqrt|g|W_i/8\) (continuation \(S_E=-S_L\)), ratio \(T_i/\mathcal M_i=4\), and
\(q_*^2=\tfrac12L\sum_iT_i\); it then names the fibre-level response in \(v^M-2\sigma^M\) as the
only candidate that could supply \(\mathcal M\) without cancelling its own tadpole. The first term of
the factorisation is not a \(\sqrt{|g|}\)-alone term: on the level form (L2787-2797) it is
\(\sqrt{|g|}\) times a level sum whose summand depends on \(\vartheta\).

Hypotheses (all stated in the inserted paragraph or inherited from the 062 set): (H1) equal weights,
\(V=T\), frozen symbol, product background, one loop (062 list, L2825); (H2) pure-trace channel
\(\bar h=(t/4)\bar g\) at \(q=0\) (062 convention; the pure-trace channel is part of the 062
statement because the profile sign is direction-dependent); (H3) response hypothesis: \(y\) and
\(m\) held, the contraction in \(\vartheta=-y\cdot y/m^2\) taken in the fluctuated metric, so
\(\vartheta\to(1+t/4)\vartheta\) exactly, while \(\mu_J,c_J,M_A^2,\mathcal D\) are frozen;
(H4) the weights \((2J+1)2M_A^2\) and the flux insertions (\(P(\Xi)\) traces, Plancherel density)
carry no additional \(h\)-dependence at this order (the level form itself holds with the cross term
dropped, L2797, "what carries over is their order"); (H5) the recorded corrections of relative order
\(s\) and \(s\vartheta\) (L2793) are not treated.

Derivation (script sections A1-A8, all symbolic identities, run twice byte-identical):
- A1: \((1+t/4)^2=1+t/2+t^2/16\) (062 profile re-check).
- A2: \(\vartheta(t)=(1+t/4)\vartheta_0\) exactly; the background fibre-constant value
  \(\tfrac{15}4\vartheta^2F\sqrt{|g|}/16\pi^2\) (L2781) then responds as \((1+t/4)^4\), not the
  determinant profile — the first quantitative departure from the 062 class.
- A3: the \(\mathrm ds/s\) integral of the recorded integrand average \(s^2[\tfrac{15}4\vartheta^2-
  s\vartheta c_J+s^2c_J^2]\) gives \(S=15\vartheta^2/(4\mathcal D^2)-2\vartheta c_J/\mathcal D^3+
  6c_J^2/\mathcal D^4\); \(\mathcal D^4S\) is positive definite (quadratic form in
  \(X=\vartheta\mathcal D\), \(Y=c_J\): \(\tfrac{15}4X^2-2XY+6Y^2\), discriminant \(-86Y^2\)); the
  recorded bracket form \(\tfrac{15\vartheta^2}{4\mathcal D}-\tfrac{\vartheta c_J}{\mathcal D^2}+
  \tfrac{2c_J^2}{\mathcal D^3}\) (L2795) differs by one power of \(\mathcal D\) per term; both are
  carried through because the measure of the recorded closed form is not restated at L2795 (the two
  forms agree in structure and sign conditions, so no result depends on the choice).
- A4: response \(F_1(t)=\sqrt{|g|}(1+t/4)^2S((1+t/4)\vartheta)\): \(t\)-coefficient
  \((2S_0+\vartheta S')/4=S_0/2+\vartheta S'/4\) (profile part + extra tadpole
  \(\vartheta(15\vartheta\mathcal D-4c_J)/(8\mathcal D^3)\)); \(t^2\)-coefficient
  \((2S_0+4\vartheta S'+\vartheta^2S'')/32=S_0/16+(4\vartheta S'+\vartheta^2S'')/32\) (profile part
  + extra quadratic \(\vartheta(75\vartheta\mathcal D-16c_J)/(64\mathcal D^3)\)); sign conditions
  levelwise; ratio extra-\(\mathcal M\)/extra-\(T=(75X-16Y)/(8(15X-4Y))\ne 1/4\) profile value.
- A5: same computation for the bracket form: extras \(\vartheta(15\vartheta\mathcal D-2c_J)/(8\mathcal D^2)\)
  and \(\vartheta(75\vartheta\mathcal D-8c_J)/(64\mathcal D^2)\) (identity checks \(8\mathcal D^2
  \cdot T_{\rm extra}/\vartheta=15X-2Y\), \(64\mathcal D^2\cdot M_{\rm extra}/\vartheta=75X-8Y\)).
- A6: re-derivation of the 062 link identities (ratio 4; \(q_*^2=2\mathcal{ML}=\tfrac12L\sum T_i\);
  \(q_b^2=12\hat U\chi^2/(m^2(\hat V+2\hat T))\); \(U_4\)-only \(q_*^2=6\sqrt{|g|}\hat U\chi^2m^6/
  (\hat V+2\hat T)\); ratio \(\sqrt{|g|}m^8/2\); \(q_*^2-q_b^2=(\sqrt{|g|}m^8/2-1)q_b^2\)) - these
  confirm the bookkeeping the new result must fit into.
- A7: the exact \(P(\Xi)\) identities of L2787-2795 re-checked (residual 0; principal-series
  conjugation), since the first-term integrand \(|P(\Xi_+)-2|^2\ge0\) is the non-negativity the
  response computation sits on.
- A8: brute-force expansion of the \(t\)-dependent proper-time integral matches the coefficient
  split of A4.

Reconciliation with L2781 ("where \(\bar h^{11}\) is negligible \(U_4\), \(U_2\) and the
fibre-constant part of \(Y\) carry \(\sqrt{|g|}\) alone"): that statement is proved there for the
static channel at large \(\tau\) with \(\bar h^{11}\) negligible. The pure-trace wave has
\(\bar h_{\mu\nu}=(t/4)\bar g_{\mu\nu}\), which is not negligible along \(y\), so \(\delta\vartheta
eq0\) there and the L2781 rigidity does not apply to it; conversely the new result does not claim
anything for the static-channel components with \(\bar h^{11}\) negligible. The insert carries a
one-sentence version of this reconciliation so the two recorded statements cannot be read as
contradictory.

Comparison with the original target: the F target (ch17 L403-412: weighted \(a_1\) and
curvature-linear \(a_2\) with stated scheme) is untouched by this package; what advanced is the
062/L2825 chain: the sole surviving \(\mathcal M\)-provider is now shown present at the level form
with computed per-level structure and sign conditions, and the class in which the 062 no-go holds
is now exactly delimited ("terms carrying \(\sqrt{|g|}\) alone"). The magnitude question
(\(q_*^2\) vs \(q_b^2\)) remains convention-bound (A6), so the Yukawa/tachyon alternative is still
open, not settled in either direction.

## Claim classification

- Determinant profile \((1+t/4)^2\); \(\vartheta(t)=(1+t/4)\vartheta_0\) under H2/H3; the \(S\)
  integral and both coefficient splits; both extra-part formulas; the sign conditions; the A6 link
  identities; the A7 identities: established (symbolic derivations, `derive_r1.py`).
- Applicability to the first term of the matrix-model density: conditional on H1-H5 (frozen symbol,
  channel convention, frozen weights and flux insertions, leading level form). In particular the
  \(\vartheta\)-linear \(U_2\) response as \((1+t/4)^3\) is conditional on the recorded \(U_2\)
  display (L2779) and H3.
- "The response does not vanish in the pure-trace \(q=0\) channel": conditional result under
  H1-H5 (not a theorem about the full fluctuation problem).
- Non-negativity of the level summands: established for the two recorded forms (A3, A7; also
  recorded at L2797).
- Sums over \(A,J\le n\); sign/magnitude of the full \(\mathcal M\); flux-insertion and weight
  response; corrections of relative order \(s,s\vartheta\); non-trace channels: unresolved.
- Yukawa vs tachyon ordering: unresolved, convention-bound (input-dependent on \(m,\sqrt{|g|}\)).

## Proposed changes

File: `chapters/appH-microscopic-proofs.tex` — one insertion only, at the end of the Problem F body,
immediately after the 062 paragraph (L2825) and before `\section{Problem G: HBEV}` (L2827).
Anchor (occurs exactly once, verified in `simulate_apply.out`): the anchor text is
"and give no Cassini or Newtonian comparison. Problems~C, F and~N remain open and
PROGRAMME-CONDITIONAL." — the closing sentence of the 062 paragraph; the insertion is appended after
that sentence as a new paragraph (spliced with a `\r\n\r\n` separator; the anchor sentence itself and
everything else in the file are unchanged). What is kept: the entire L2825 paragraph verbatim, the
L2797 not-computed sentence (historical record, not edited), the L2781 rigidity sentence, the F
status block (L1641-1660, certified byte-identical, block sha256 20eb96d656dd3296b4f580919c1c9f5d97d83c91ccf6b6c32bb9a476ac86dd4e).
The full inserted text is `insert-r1.tex` (3980 bytes, sha256
43038fded3efaaf1f85325a18a9b37610c46236a44ced1c7ccc08558507475c7, LF-only, single paragraph, no
`display` split needed, so no `%---SPLIT---%` marker; no `\ref`, `\eqref`, `\label` or `\cite` added
— verified by inspection; textual cross-references "the fibre-flux display", "the potential display"
point to the unlabelled displays at L2795 and L2777-2780). Stale passages elsewhere: none found; the
closer of the insert matches the existing scoped-closer convention of the same block. One splice
block.

No changes to `bib/namcg.bib` (no new citations), `chapters/ch17-agenda.tex`, or any status passage.

Predicted post-state after the integrator applies `insert-r1.tex` (from `simulate_apply.out`):
582,706 bytes; sha256 dd0bea7780757e51d9677d38130d0425dc38cd54538d85f14f26f23f97bdcf4a; CRLF 3435
(= 3433 + 2 separator + 0 in the insert body, the insert body being one line); bare LF 0.
Pre-state certified unchanged at read time: 578,723 bytes, sha256
5b5fc2650f05d95dce7fb7a4ed96ca282b946dbf7a3b3d2e368331b65638a631, CRLF 3433, bare LF 0.

## Verification scripts

All under this proposal folder, run with `python -I` (each run twice, outputs byte-identical):
- `derive_r1.py` (7071 B, sha256 1d17c85cad83752fa3bd60d514a5e18a5f283569172040bac06e59c9a6eb77a6)
  -> `derive_r1.out` (3641 B, sha256 6ccfd36ef2f1213d22d8696b9a6a291af1247fcfcee2eee2fa1d39f866a2d3b0):
  sections A1-A8 above; every printed check True, False-count 0.
- `simulate_apply.py` (3315 B, sha256 bcbd5b13ab5d91d138bb61205fd0c3b3b8a174c8a49f5ca1407ace36923eb2e6)
  -> `simulate_apply.out` (1312 B, sha256 4db49b18682a771ce3ed82c8b525ed4f71879ea5cd318ed4bd01b78d45b2a035):
  read-only splice simulation; asserts the certified pre-state, anchor count 1, insert LF-only,
  computes the predicted post-state, asserts prefix/suffix byte-preservation and byte-identity of a
  900-byte window from `\label{sec:status-F}` containing the Status/Priority/Completion passage. It
  never writes to `chapters/`.

## Decisions Taken

- Chose the computed branch of P1 over the alternative conjecture that the fibre-level response
  vanishes: the level form makes \(\vartheta\) (a metric contraction) a datum of the first term, so
  a pure-trace wave necessarily moves it; the vanishing route was rejected after derivation, not by
  assumption.
- Rejected a route through a homogeneous scaling \(\lambda\) of the class with a residual \(K\)-level
  response \(M_A^2\to(1+t/4)M_A^2\): it conflates internal-coordinate scaling with a metric wave and
  gave a picture-dependent sign; the \(\vartheta\)-carried derivation stays inside the frozen-symbol
  class of 062 and is the one submitted.
- Deferred the truncation/heat-kernel benchmark route (scout recommendation, and it would require
  Alternate-scope labelling): not needed for P1 and it would mix scopes.
- Recorded both level-summand forms (L2795 bracket and the \(\mathrm ds/s\) proper-time summand)
  because the measure of the recorded closed form at L2795 is not restated there; the result is
  invariant in structure between them, and the insert states both with their own extra-part formulas
  rather than silently choosing one.
- Included the L2781 reconciliation sentence in the insert (routine notation/scope choice, favouring
  consistency of the manuscript record).
- P2 handled as prose inside the insert closer only; deliberately did not touch the L2797
  not-computed sentence or the L1653-1660 missing-step block.

## Milestone assessment

Routine / bounded advance. No MILESTONE.md trigger: no critical-path step is derived end-to-end; the
result is a conditional sub-lemma closing one recorded missing item for one channel component, with
the F target and the magnitude alternative still open.

## Status-label recommendation

None. Critical-path set re-derived from ch17 (L403-412 and the criterion list) and the ledger
snapshot: A, B, C, D1, E, F, G-derived, N. F stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; the
insert adds no status label and the simulation certifies the status block byte-identical. Expected
label changes: none.

## Author decision needed

None. (Report-only, not part of this package: a prior round noted the `Kabat1995` bib entry pages
"281-299" against the commonly cited 281-302; not re-verified this round, no bib edit proposed.)

## Remaining open step

To take this chain further: (i) perform the sums \(\sum_A\sum_{J\le n}(2J+1)2M_A^2(\cdot)\) of the
extra tadpole and extra quadratic parts at the cut-off \(\mathcal D\gg\vartheta\) on an explicit
\(K\) (e.g. \(S^2_N\)), and compare the resulting \(\mathcal M\) against \(q_b^2\) in a stated
convention (the \(\sqrt{|g|}m^8/2\) factor is convention-bound); (ii) compute the response of the
flux insertions (\(P(\Xi)\) factors, Plancherel measure, cross term) to the wave, which H4 froze;
(iii) the corrections of relative order \(s\), \(s\vartheta\) and the \(\chi^2\lesssim\vartheta\)
second-order non-derivative terms; (iv) the F target itself: weighted \(a_1\) and curvature-linear
\(a_2\) on the locked block with stated ghost operators and scheme (ch17 L403-412), still untouched.

## Special instructions for the gatekeeper

- Re-run `python -I derive_r1.py`; every check must print True, False-count 0, and
  `derive_r1.out` must match byte-for-byte. The A5 normalization is now
  \(64\mathcal D^2\cdot M_{\rm extra}/\vartheta=75X-8Y\) (a prior draft of the script had an
  \(64\mathcal D^3\)-labelled check with an extra factor 32; the corrected identities are the ones
  shipped and reflected in the insert).
- Re-derive the \(\vartheta\) response against L2718 (\(\vartheta=-y\cdot y/m^2\) off \(y^i=0\)) and
  check the reconciliation with L2781 (the insert's claim is only for the pure-trace channel, where
  \(\bar h^{11}\) is not negligible).
- The insert must not be read or asserted as: the sign of the full \(\mathcal M\); a decision between
  the Yukawa threshold and the tachyonic pole; any closure of F or label change; a statement about
  the static channel with \(\bar h^{11}\) negligible.
- Splice checks: anchor unique (count 1); pre-state 578,723 B / 5b5fc265... / CRLF 3433 / bare LF 0;
  predicted post-state 582,706 B / dd0bea7780757e51d9677d38130d0425dc38cd54538d85f14f26f23f97bdcf4a /
  CRLF 3435 / bare LF 0; status-F 900-byte window sha 20eb96d656dd3296b4f580919c1c9f5d97d83c91ccf6b6c32bb9a476ac86dd4e
  unchanged. Every number in the insert either appears in appH L2775-2825 or is derived in
  `derive_r1.py`.
- No citations are added; nothing in `bib/` may change on this package. No new `\ref`/`\label`.
