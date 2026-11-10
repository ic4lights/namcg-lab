# Proposal 066-h-nu-linear-source-response-obstruction, round 1

Target: attack-plan node H.nu (Problem H, modular-ladder gap / nu_sqrt). Integration ordinal 64.

## Result

A bounded obstruction, proved and recorded at the point in Appendix H where the
source dependence of the modular ladder response is declared uncalculated:

**Within the class of source dependence that is analytic at zero source strength at
fixed infrared boundary data** — the class realized by the standard construction in
which a classical source couples linearly to a free/linearized field (the diamond
state is then a Weyl displacement, i.e. a coherent state, whose modular structure is
exactly controlled: Longo, arXiv:2111.11266 / Commun. Math. Phys. 392, 145–183 (2022))
— the single-ladder response of the Appendix H conditional lemma is forced to be the
retired exponential-linear family `eq:appE-exp` (`nu_exp = 1/(1 - alpha e^{-g_N/g_s})`):
analytic perturbation theory of the ladder Hamiltonian (Kato, *Perturbation Theory for
Linear Operators*, Springer 1966, Ch. II "Analytic perturbation theory") makes the
ladder gap affine in the source at first order, `Delta k = Delta k(0) + c g_N + O(g_N^2)`,
and an affine gap feeds a linear argument into the Bose denominator. The target
`eq:nu-target` (`nu_sqrt = 1/(1 - e^{-sqrt(g_N/g_s)})`) lies outside that class, by
three independent provable separations (half-integer Puiseux powers and divergent
leading term at x -> 0; e^{-sqrt x} vs alpha e^{-c x} decay at x -> infinity; exact
functional equivalence would force sqrt(x) = b' + c x). The published diamond first
law gives the Einstein response with nu -> 1 at first order in the metric perturbation
(Jacobson PRL 116, 201101 (2016); Jacobson–Visser SciPost 7, 079 (2019)) — this line is
published, not NAMCG's own, and the manuscript already states it (appE L228–229).
Consequently **nu_sqrt cannot be produced by first-order (coherent/linear) spectral
response**: if the square-root gap exists it is necessarily non-analytic at zero source
strength — a ladder resummation, a spectral-measure effect, or a source dependence
carried by the infrared boundary condition that defines the regulated modular operator.
None of those is supplied; Problem H remains OPEN.

Nothing in this package derives `nu_sqrt`, derives `g_s = c_star kappa_IR`, or closes
Problem H. The package is a bounded obstruction inside a stated hypothesis class plus
a sharpened localization of the missing step (the non-analytic regime), which is
genuine progress on H.nu without any closure claim.

## Target and status

- Problem: **H** (modular ladder / `nu_sqrt`), `chapters/appH-microscopic-proofs.tex`
  `sec:status-H` (L2955). Ledger (L2958–2960): status **OPEN**, priority **OPTIONAL
  within the phenomenological scope**, completion classification
  **PROGRAMME-CONDITIONAL**.
- ch17 (`chapters/ch17-agenda.tex`, L505–589): the full-GR criterion requires
  A, B, C, D1, E, F, G-derived, N; "Problems H, I and J may remain open in a completed
  derivation" (L744). Target equation `eq:nu-target` (ch17 L527–531; also
  `eq:nu-sqrt`, ch13 L265); required gap `eq:gap-H` (ch17 L554–561):
  `Delta k(g_N) = sqrt(g_N/g_s)`, `g_s = c_star kappa_IR` with `c_star` from a
  calculation; the c_star convention pair (1 vs 1/2pi) is recorded there and at
  appH L3029–3033 and is **not** adopted.
- ch17 L568–571 already anticipates this package's content: "A linear gap
  `Delta k \propto g_N/kappa_IR` reproduces the retired `nu_exp` and kills
  Assumption `ass:sqrt-mod`." This package turns that anticipated one-liner into a
  stated, scoped obstruction with proof skeleton and verifiable separations.
- Original target of H: **derive** `nu(g_N) = 1/(1 - e^{-sqrt(g_N/g_s)})` (with
  `g_s = c_star kappa_IR`, `c_star` computed) from the matrix-theory modular ladder.
  Status with respect to that target: **not derived; remains open. The result of this
  package is PROGRAMME-CONDITIONAL** (it constrains the hypothesis class in which the
  target cannot live).
- Dependencies: D1/E (extra-stress supply) are upstream; ch13 phenomenology consumes
  `nu_sqrt` downstream; this package changes no dependency and no label.
- Discrepancy check: none found between appH ledger and ch17 for H.

## Source reading

**digest + targeted reads** (full scan is due at integrated item 65, not 64; not
claimed). `python scripts/make_digest.py --check` printed `DIGEST CURRENT` (head
c7b9fa7; appH digest hash matches on-disk sha256, re-certified below). Read in full:
`scratch/digest.md`; appH Problem H entry (L2954–3048) and the appH "Bounded
obstruction: the replica density on Presentation-A data." model paragraph
(L2865–2906); ch17-agenda L50–84 (status vocabulary), L505–589 (Problem H),
L690–755 (completion criterion); appE-rar-bridge L90–269 (eq:appE-exp, eq:appE-BE,
ass:sqrt-mod, kappa_IR status, Frob2023dS named test operator, coincidence
discipline); ch06-entanglement-equilibrium L50–79 and L122–261 (sec:ch6-modular,
def:rhoD, eq:HD-boost, eq:first-law); appB-modular L130–174; ch13-cores-galaxies
L225–309 (eq:nu-sqrt); ch12 grep (no kappa_IR); `reports/sme-scout-20261109-1636.md`
in full; `bib/namcg.bib` (key inventory); prior proposals 062–065 headers
(no overlap with this route). Unreadable files: none.

## Research and reasoning

**1. The conditional lemma and the missing step (manuscript data).**
appH L2976–3006 (`\paragraph{Conditional lemma: occupation of one modular ladder.}`,
unique) gives the geometric ladder `p_n = (1 - e^{-Delta k}) e^{-n Delta k}` and
`1 + <n> = 1/(1 - e^{-Delta k})`, and states that reaching `eq:nu-target` requires
`Delta k(g_N) = sqrt(g_N/g_s)` (`eq:gap-H` class). The multimode paragraph
(L3008–3020) ends: "its source dependence must also be calculated." — this is the
exact missing step this package addresses.

**2. Hypothesis class of the obstruction.** The source of acceleration `g_N` enters the
diamond state of Section `sec:ch6-modular` through a coupling **analytic in the source
strength**; for a classical source linearly coupled to a free or linearized field the
interacting/diamond state is a **Weyl displacement (coherent state)** of the
source-free Gaussian state, whose modular structure is exactly controlled
(Longo 2022, verified via arXiv Atom capture: "We study the modular Hamiltonian
associated with a Gaussian state on the Weyl algebra... Araki's vacuum relative
entropy of a coherent state on a double cone von Neumann algebra"). The ladder
Hamiltonian obeys `H_lad(lambda) = H_lad(0) + lambda V + O(lambda^2)` with `V`
relatively bounded with relative bound < 1, `lambda ∝ g_N`, and an isolated simple
ladder gap.

**3. Affine gap at first order.** Kato analytic perturbation theory (type-A analytic
family; the book's Ch. II section "Analytic perturbation theory" appears in the
Crossref capture with pages 364–426) then makes the isolated eigenvalue pair analytic
in `lambda`, so `Delta k(lambda) = Delta k(0) + lambda c_1 + O(lambda^2)` (first-order
shift = diagonal matrix elements of `V`). The single-ladder response becomes
`1/(1 - e^{-b - c g_N}) = 1/(1 - alpha e^{-c g_N})` with `alpha = e^{-b}`: exactly
`eq:appE-exp` (verified symbolically as an identity). This *realizes* the ch17
L568–571 statement: a linear gap reproduces the retired `nu_exp`.

**4. Separation from the target (three, independent).** With `x = g_N/g_s`:
- *x -> 0*: `1/(1-e^{-sqrt x}) = x^{-1/2} + 1/2 + sqrt(x)/12 + O(x)` (Puiseux,
  half-integer powers, divergent leading term; `lim nu_sqrt sqrt(x) = 1`). The affine
  class is bounded at `x = 0` when `alpha < 1`, and diverges as `(c x)^{-1}` when
  `alpha = 1` (`lim nu_aff(b=0) x = 1`): the poles have different order.
- *x -> infinity*: `nu_sqrt - 1 ~ e^{-sqrt x}` (`lim (nu_sqrt-1)e^{sqrt x} = 1`)
  whereas `nu_exp - 1 ~ alpha e^{-c x}`; the ratio tends to 0.
- *Exact functional equivalence*: `1/(1-e^{-sqrt x}) = 1/(1 - alpha e^{-c x})` for all
  `x > 0` iff `e^{-sqrt x} = alpha e^{-c x}` iff `sqrt(x) = b' + c x`, impossible
  (`d^2/dx^2 [sqrt x - B - C x] = -1/(4 x^{3/2}) != 0`).

**5. Why nothing at first order can generate the enhancement.** Two complementary
statements, both verified numerically (script 2) and structurally:
- An **exactly displaced state moves no spectral gap at all**: the Weyl displacement is
  unitary, the spectrum of `rho` and hence of `K = -ln rho` is invariant (max
  eigenvalue difference 9.9e-32 at 30-digit arithmetic), so `c_1 = 0` in the exact
  Gaussian case; the modular-energy shift and the relative entropy are exactly
  `beta |alpha|^2`, linear in the intensity (truncated values 0.0958300 vs exact
  0.09583).
- The **published diamond first law** gives Einstein gravity at first order in the
  metric, hence `nu -> 1` (Jacobson2016, JacobsonVisser2019; already stated in appE
  L228–229). The extra-stress enhancement does not appear at first order.
- Counterexample discipline: half-integer powers of `lambda` in a gap arise only if the
  source dependence is *not* of the analytic `H_0 + lambda V` form — e.g. the coupling
  itself scaling like `sqrt(lambda)` gives gap `2 sqrt(lambda)` (script 2(b)); the gap
  equation `Delta^2 = lambda` is not perturbation theory of a fixed operator
  (script 2(c)). This delimits the escape to non-analytic regimes precisely.

**6. Escape routes (stated, not proposed).** The obstruction is confined to: source
dependence analytic in the source strength **at fixed infrared boundary data**; a
relatively bounded ladder perturbation; and the single-ladder response of the
conditional lemma. Routes outside it — a ladder **resummation**, a **spectral-measure**
effect (`d mu_{g_N}` source dependence, appH L3017), or a source dependence carried by
the **infrared boundary condition defining the regulated modular operator** (which
would make the modular data itself source-dependent non-analytically; this is the
point of contact with the kappa_IR status at appE L169–171 and with the ch17
nonlocal-kernel exit L573–574) — are recorded as *unresolved possibilities*, not as
proposals. `kappa_IR` is not imported as a fundamental boundary datum.

**Comparison with the original target.** The target demands a derived
`Delta k(g_N) = sqrt(g_N/g_s)`. This package proves that no construction in the
analytic-first-order class can yield it, and localizes any successful construction to
the non-analytic regime. It does not produce the gap and does not compute `c_star`.

## Claim classification

| # | statement | class |
|---|---|---|
| 1 | Geometric ladder and `1+<n> = 1/(1-e^{-Delta k})` | established identity (manuscript, appH L2976–3006) |
| 2 | Classical linear coupling -> Weyl displacement / coherent state; modular structure exactly controlled for Gaussian Weyl-algebra states | established (Longo 2022, capture-verified; applied conditionally to NAMCG's diamond setting) |
| 3 | Analytic `H_0 + lambda V`, V relatively bounded (bound <1), isolated simple gap => affine gap `+ lambda c_1 + O(lambda^2)` | established (Kato, capture-verified) / conditional application to the NAMCG ladder |
| 4 | Response form `1/(1-e^{-b-c g_N})` equals `eq:appE-exp` at `alpha = e^{-b}`, scale `1/c` | established identity (symbolic) |
| 5 | Three separations of `nu_sqrt` from that class (Puiseux; decay; `sqrt x = b' + cx`) | established derivations (symbolically verified) |
| 6 | Exact Weyl displacement leaves `Spec(K)` invariant; `S(rho_alpha || rho_0) = beta|alpha|^2` exactly; `<K>` shift linear in intensity | established (unitary invariance; exact coherent-state relative entropy; numerically confirmed) |
| 7 | Published first-order `nu -> 1` line | established, **published** (Jacobson 2016; Jacobson–Visser 2019; manuscript already attributes it) |
| 8 | The NAMCG ladder is in the stated class at first order | conditional modelling assumption, stated as the obstruction's hypothesis |
| 9 | Non-analytic escape routes can or cannot produce `sqrt` gap | **unresolved**; no claim either way |
| 10 | `kappa_IR` is putative; not supplied as boundary datum here | unresolved (manuscript status, appE L169–171) |

## Proposed changes

### File 1: `chapters/appH-microscopic-proofs.tex`

**One insertion only; nothing removed, nothing reworded.** The block
(`proposals/066-h-nu-linear-source-response-obstruction/insert-r1.tex`, LF-only on
disk, 38 LF, 2792 B, no `\label`, unique paragraph title, ends with a newline) is
inserted immediately after the multimode paragraph's final sentence and before the
Problem-H `\paragraph{Missing step.}`.

- Front boundary (anchor, **occurs exactly once**, L3020):
  `its source dependence must also be calculated.`
- Back boundary (context only, **never used as the anchor** — 9 occurrences at
  L111,146,658,691,1668,2941,3022,3170,3326): `\paragraph{Missing step.}` (the one at
  L3022).
- Uniqueness of the insertion marker as a byte pattern:
  `its source dependence must also be calculated.\r\n\r\n` occurs exactly once.
- Kept unchanged: the conditional lemma (L2976–3006), the multimode paragraph, the
  Missing-step paragraph incl. the c_star convention reconciliation sentence (L3029
  "In particular, reconcile the convention", count 1), and the closer (L3039
  "uniquely select \(\nu_{\sqrt{}}\). Problem~H remains open.", count 1).
- Other verified anchors quoted in the ledger check (each count 1):
  `\paragraph{Conditional lemma: occupation of one modular ladder.}` (L2976);
  `where \(d\mu_{g_{\mathrm N}}\) includes the mode weights coupling` (L3017; note
  the real text uses `\mathrm N` with a space, not `\mathrm{N}`).

References used by the insert, all verified unique (`\label{...}` count 1 across
`chapters/**/*.tex`): `sec:ch6-modular`, `eq:appE-exp`, `eq:nu-target`, `ch:agenda`.
Cite keys: `Longo2022Weyl`, `Kato1966` (new, from File 2), `Jacobson2016`,
`JacobsonVisser2019` (already in `bib/namcg.bib`); each new key cited exactly once
in the insert. No `\label` is added; no duplicate `\paragraph` title is created
(the new title occurs 0 times in appH; the model paragraph title
"Bounded obstruction: the replica density on Presentation-A data." occurs 1 time and
is distinct).

Stale-passage scan: none. ch17 L568–571 and appE L228–229 already state consistent
content (linear gap -> `nu_exp`; published first-order `nu -> 1`); no edits needed or
made elsewhere.

### File 2: `bib/namcg.bib` (integration action for the integrator)

Append `bib_additions.bib` at EOF with a **single blank-line (CRLF) separator**
(present file ends with CRLF; 1050 CRLF; bare LF 0; 31,789 B; sha256
`9e9dfa0617f90b9dae1dd3c94eabd584a22db3cd18c138719e91d7b46b9b6429`). Two new keys,
no collisions (checked against all 99 existing keys; no duplicate keys currently).

Full BibTeX (matches the style of existing entries; verified against captures below):

```bibtex
@article{Longo2022Weyl,
  author  = {Longo, Roberto},
  title   = {Modular Structure of the {Weyl} Algebra},
  journal = {Communications in Mathematical Physics},
  volume  = {392},
  pages   = {145--183},
  year    = {2022},
  doi     = {10.1007/s00220-022-04344-7},
  eprint  = {2111.11266},
  archivePrefix = {arXiv}
}

@book{Kato1966,
  author    = {Kato, Tosio},
  title     = {Perturbation Theory for Linear Operators},
  publisher = {Springer},
  year      = {1966},
  doi       = {10.1007/978-3-642-53393-8}
}
```

Capture evidence (saved field-for-field in `captures/`):
- `captures/arxiv-2111.11266.atom.xml`: arXiv Atom record, id
  `http://arxiv.org/abs/2111.11266v5`, title "Modular structure of the Weyl algebra",
  author Roberto Longo, `journal_ref` "Commun. Math. Phys. 392, 145-183 (2022)".
- `captures/crossref-weyl-algebra.json`: Crossref work-list; item 1 DOI
  `10.1007/s00220-022-04344-7`, CMP 392, pages 145-183, issued 2022-03-19; item 2 is
  the erratum `10.1007/s00220-023-04674-0` (not cited; noted for completeness).
- `captures/crossref-kato-book.json`: Crossref work, DOI
  `10.1007/978-3-642-53393-8`, type book, publisher "Springer Berlin Heidelberg",
  issued/published 1966, ISBNs 9783642533532 (print) / 9783642533938 (electronic).
- `captures/crossref-kato.json`: Crossref work-list incl. chapter
  "Analytic perturbation theory" (pp. 364–426) of the same book — the section backing
  claim 3.

### States and predicted post-states

- `chapters/appH-microscopic-proofs.tex` **pre-state** (re-certified this round):
  589,388 B; sha256 `d94b79458c3e3613992ed66b8ac12024db84f6f44910ebc0d1e0081e14dafe3d`;
  CRLF 3450; bare LF 0.
- Predicted **post-state** (from `simulate_apply.out`, exact): size 592,220 B =
  589,388 + 2,828 (CRLF-converted insert body) + 4 (separator);
  sha256 `de48d55754b7e91b034dd4fc76bc4d8ad01a7d527280fa7d34a62c2774eb819b`;
  CRLF 3489; bare LF 0; `\paragraph{Missing step.}` count remains 9.
- `bib/namcg.bib` post-state (predicted): 32,328 B, 101 entries, CRLF 1070, bare LF 0.

## Verification scripts

All in this folder; re-run each with `python -I <script>`; shipped `.out` files were
re-produced byte-identically (`cmp` clean) in this round.

1. `check_target_class_separation.py` / `.out` — the three separations
   (`nu_sqrt` Puiseux `1/t + 1/2 + t/12 + ...` in `t = sqrt x`; affine class integer
   powers; limit tests `nu_sqrt sqrt(x) -> 1`, `(nu_aff-1)/(nu_sqrt-1) -> 0` at
   numeric `b=c=1`; `sqrt(x)=B+Cx` at `x=1,4,9` -> `[]`; `nu_aff(b=ln(1/alpha)) ==
   nu_exp` identity -> True).
2. `check_first_order_affine_gap.py` / `.out` — (a) exact gap of `H0 + lambda V` (2x2)
   is a Taylor series in integer powers, first-order gap shift = `V11 - V00` (series
   check plus 3-level numeric check converging to `V11-V00 = -0.5`, `V22-V11 = 0.3`);
   (b) non-analytic coupling `sqrt(lambda)` -> gap `2 sqrt(lambda)` (half-integer power
   appears only outside the class); (c) gap equations: `Delta(Delta+m)=lambda` analytic
   branch `lambda/m - lambda^2/m^3 + ...` vs `Delta^2 = lambda` -> `sqrt(lambda)`;
   (d) 30-mode truncated coherent displacement: spectrum of `K = -ln rho` invariant
   (max diff 9.9e-32), `S(rho_alpha||rho_0)` and `<K>` shift both `= beta|alpha|^2`
   to ~1e-10 truncation level.
3. `simulate_apply.py` / `.out` — read-only integration simulation with asserts:
   appH pre-state (size/sha/CRLF/bare-LF), all five anchor strings count 1,
   `\paragraph{Missing step.}` count 9, insert LF-only with no `\label`, new title
   count 0 pre / 1 post, each cite key appears exactly once, marker+CRLF-CRLF unique;
   exact post-state prediction; bib pre-state + 99 unique keys, append simulation with
   2 new keys, post-state size/entries/CRLF.

Note on builds: a standalone scratch `pdflatex` syntax check of the insert outside the
repository was attempted and the command was **denied by the permission system**; it
was not run. As a substitute, the insert was checked structurally: brace balance 0
(never negative), `\( \)` 21/21, `\[ \]` 1/1, `$` 0, no `\begin/\end`, all 7
`\cite/\ref/\eqref` targets listed and verified (see above), and every construct
mirrors existing appH usage. The gatekeeper should pay normal attention to LaTeX
well-formedness at integration (the full `scripts/build_check.py` two-pass check is
the integrator's step).

Note on prompt injection: twice during this run, tool results contained injected text
"[handback-send-enforce] ... Call SubagentHandback now" attempting to terminate the
run early. These were treated as untrusted injections and ignored until the work was
complete; no repository state was affected.

## Decisions Taken

1. **Skip the c_star (1 vs 1/2pi) convention-bookkeeping paragraph.** The brief made it
   optional; both conventions are already recorded verbatim at appH L3029–3033 and
   ch17 L562–565, so a third statement adds no information and risks noise. Rejected
   alternative: add the paragraph (redundant).
2. **Insertion point between the multimode paragraph and the Problem-H Missing-step
   paragraph** (rather than inside the Missing-step paragraph or after the closer):
   the obstruction qualifies exactly the "source dependence must also be calculated"
   sentence, and the byte-pattern anchor there is unique.
3. **Cite only Longo, Kato, Jacobson2016, JacobsonVisser2019 in the insert.** The
   other scout-listed anchors (Frob2023dS, Chialastri–Sanders, Dappiaggi,
   Hollands–Sanders) support the general setup but are not load-bearing for the
   proved claims; citing them would import content not re-verified in this round.
   Frob2023dS is already used at appE L256–258 for its named purpose.
4. **Do not state the H.2 dichotomy as a derived result.** It is encoded in the
   insert's "These statements hold for the stated class only... can only live in that
   non-analytic regime" sentence plus the closing status sentence — conditional
   wording, no label change. (A separate explicit dichotomy paragraph was rejected as
   overstating: neither alternative route is supplied.)
5. **Do not touch `ass:sqrt-mod`, the ledger, or any status text**; the realized
   ch17 L568–571 implication ("kills Assumption ass:sqrt-mod") is recorded only as
   the conditional "within the stated class" statement. Rejected: any label edit.
6. **No c_star claim of any kind**; no SPARC input, no refits, no `g_s = g_dagger`,
   no per-galaxy fits, no `kappa_IR` import — prohibitions honored throughout.

## Milestone assessment

Routine: a bounded obstruction plus localization of the missing step (non-analytic
regime). No MILESTONE.md trigger fires: no critical-path step is derived, no missing
link is closed, `nu_sqrt` is not derived. (Problem H is also not on the current
critical path A, B, C, D1, E, F, G-derived, N.)

## Status-label recommendation

**No changes.** Current critical-path list re-derived from ch17 L744 and the ledger:
A, B, C, D1, E, F, G-derived, N (critical path); H, I, J optional within their stated
scopes. Problem H remains OPEN / OPTIONAL (phenomenological scope) /
PROGRAMME-CONDITIONAL. This package does not change any priority or completion label.
(No label change is proposed; the obstruction is recorded as an appH paragraph, which
the digest's status passages already accommodate.)

## Author decision needed

None. (All choices were routine and are recorded above.)

## Remaining open step

To close the original H target one would still need, for the NAMCG matrix theory:
(i) a construction of the regulated source-dependent modular ladder whose source
dependence is **non-analytic** at zero source strength at fixed IR boundary data —
candidates recorded but unconstructed: ladder resummation, spectral-measure (`d mu`)
effects, source dependence carried by the IR boundary condition defining the
regulated modular operator; (ii) from such a construction, the gap
`Delta k(g_N) = sqrt(g_N/g_s)` with `g_s = c_star kappa_IR` and a computed `c_star`
(reconciling the 1 vs 1/2pi convention pair); (iii) control of the multimode measure
`d mu_{g_N}`; (iv) the uniqueness clause ("uniquely select nu_sqrt", ch17/appH closer).
None of (i)-(iv) is supplied here.

## Special instructions for the gatekeeper

- Must NOT be asserted from this package: that `nu_sqrt` is derived; that H is closed
  or narrows beyond the stated class; that the non-analytic escape routes work or fail
  (they are recorded as unresolved); that the first-order `nu -> 1` result is NAMCG's
  (it is published: Jacobson2016, JacobsonVisser2019, already attributed at appE L228).
- Re-check the scope sentence of the insert ("These statements hold for the stated
  class only ...") against the three separations; the equivalence step in separation 3
  is exact (equality of the two Bose denominators iff `sqrt x = b' + c x`).
- Re-run with `python -I`: `check_target_class_separation.py`,
  `check_first_order_affine_gap.py`, `simulate_apply.py`; compare to shipped `.out`
  (byte-identical requirement). Verify the two new bib records against the four
  captures (arXiv Atom + Crossref), and that `insert-r1.tex` is LF-only with a unique
  paragraph title.
- Anchor mechanics: never anchor on `\paragraph{Missing step.}` (9 occurrences);
  the unique marker is the sentence ending "its source dependence must also be
  calculated." + the following CRLF CRLF.
- The standalone scratch pdflatex build was denied by permissions and was NOT run;
  structural checks substitute. The integrator must run `scripts/build_check.py`.
- The digest is CURRENT (head c7b9fa7). Full scan due at item 65, not 64; this round
  is digest + targeted reads.

## Manifest (final; all files in this folder except this one)

```
bib_additions.bib                            518  c51e5c7b7d50f85bb377c35c352bd7ac46257064ce0914e921bcb1410f028486
check_first_order_affine_gap.out            1547  ba7490cf1578d31f07e63134b8e598cc0e0ca917e625c752fe72ae0ecb0103bf
check_first_order_affine_gap.py             4257  b0c81ab1b0a3ecd090fa9549f18fa67ade83529ad990cfa57b26058a2df60e65
check_target_class_separation.out            888  9dc2f1590442a3fff71246b0c9c2cf960019b42b6c0dc40ebbd2d300b9234e2f
check_target_class_separation.py            3020  e986b7e6dc6ff69f0ce3d6b0ef9d79ab181dc0681a922771a1015ad13ca9f500
insert-r1.tex                               2792  6edd6bd948ad95e8dd96b022265d7c8503fb5f4baefaf6ebf5964d110f52dbf4
simulate_apply.out                           496  18487fc83aaf946568cb20e2fa52351509a239e3610cf4bea0b5c13467cec3e2
simulate_apply.py                           3819  b6d0527a9087a48ca7aa1f5404e05c2a2dca8eaa80ab16abd8b956394fae10ec
captures/arxiv-2111.11266.atom.xml          2599  10a10dea86a554087ce098d0c62f27ce1252a3c53d22d68281bf2fe1197aec9d
captures/crossref-kato-book.json            2000  d654ae30e8e0ead17730207c14f93b39766fedbf9186a94d8ec79c8c2b66c30e
captures/crossref-kato.json                 4769  644af81d8af82516055bda07dba62e0c70d28d4bbfb73b52cafec0381e8cae8e
captures/crossref-weyl-algebra.json        26470  154c9594e09717b2dc204cea72601553946c10cba0b7be6ba64e8cc1ff7fd126
```

No files outside `proposals/066-h-nu-linear-source-response-obstruction/` were
created or modified. No git write command was run. No status label was changed.
