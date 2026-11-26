# Proposal 103-g-moments-nonproduct-measures, round 1

## Result

A DERIVED member family of correlated (non-product) gaussian slot pushforward
laws is established at D=2 with exact moment data at D=3: the pushforward
density of the simplex coordinate under a correlated two-slot complex gaussian
law is the closed form f(p) = (g1 g2 - |rho|^2) b / (b^2 - c^2)^{3/2},
b = g2 p + g1 (1 - p), c = 2|rho| sqrt(p(1-p)), obtained by integrating the slot
phases to a modified-Bessel factor and applying the ray integral
int_0^inf tau e^{-b tau} I_0(c tau) dtau = b/(b^2-c^2)^{3/2}; it reduces at
rho = 0 to the integrated 089 product density. Inside the family: at equal
variances the weight is strictly peaked at the barycenter (height
1/sqrt(1-r^2), coincidence window eps/sqrt(1-r^2) + O(eps^3), E[s2] < 2/3 for
every r>0); at unequal variances (1,2) the vertex maximum destabilizes at
|rho|^2 = 1/3 (normalized coherence 0.408248290463863) and the argmax moves
into the interior (0.09909 at |rho| = 0.7, grid-recorded). This is a
CONDITIONAL DERIVATION CLASS: the coherence rho and variances are inputs of the
named family; the repository does not by itself supply where the slot
correlations come from; the bifurcation is a selection MECHANISM within the
conditional family, NOT profile selection by the core. Nothing in Problem G is
closed.

## Target and status

- Problem G: Status: OPEN. Priority: CRITICAL PATH. Completion:
  PROGRAMME-CONDITIONAL (appH Missing step paragraph L3119-3131, missing steps
  (i)-(iv), read this round; unchanged by this package).
- Frontier edge G.moments-nonproduct-measures (chain 2 head post-33, "untried"
  before this package, co-rank 2 order 1 per the frontier excerpt): attempted,
  partially supplied. Required symbols obtained: a non-product slot joint law
  (slot side) and its induced profile-pushforward weight (D=2 closed form; D=3
  via moments only). Required symbols NOT obtained: the joint law on
  slot-simplex x FRAME space (frame measure not entered) and non-degeneracy
  along the 088 kernel directions (not assessed). Classification of this
  package on the edge: ATTEMPTED-OPEN.

## Source reading

digest + targeted reads. Read in full: the three surviving .py files and the
three surviving .out files; appH L3119-3131, L3191 (089 paragraph), L3221
(block closer). Scripted 110-byte prefix listing of L3185-3221 plus
ordinal-cross-reference scans of L3185-3221 and L3223-3309 (prefixes/offsets
only). Frontier context via scratch/103_frontier_excerpt.txt (frontier.yaml not
read). Live appH contract re-asserted: 801632 B / sha256-16 e37ca5385996df34 /
CRLF 3868 / bareLF 0 / no BOM.

## Research and reasoning

Complete route statement, verbatim .out evidence, rule-6 classification per
claim, bounded-class relation, OPEN list and reproduction pack: see
`findings.md` (sections 2-7). Summary of the relation to recorded bounded
edges: the 089 fibre-integration bound is stated for the class of PRODUCT slot
laws (independent squared slot magnitudes each fixed by s^2 times the slot
variance); every member derived here has dependent squared magnitudes (the
I_0(2|rho| sqrt(E1 E2)/det) factor is absent iff rho = 0), so the derivation
lies OUTSIDE that class and yields a property impossible inside it (a strictly
non-flat pushforward at equal variances, versus the flat product-class weight
at uniform input): EVASIVE of the 089 product-class bound, as a matter of class
fact. What is inherited: the same fibre map, and the family is indexed by input
labels (g1, g2, rho) - reading f as a profile weight re-imports those labels,
so the 089 structural obstruction ("no weight beyond the supplied profile data")
is relocated from (g) to (g, rho), not defeated; the 088 audit gap (core-
produced profile-space weight supplied by nothing upstream) is untouched. The
equal-coherence members are relabelling-invariant with unique barycenter
maximum - exactly the 090 orbit-rigidity alternative, not a counterexample;
the unequal-variance members realize the label-asymmetry escape branch only
within the named family. No Gram-spectrum/fibre (094-101) claim is made.
Literature: no citations introduced; no external sources relied on.

## Claim classification

See findings.md section 4 (per claim: established / conditional / numerical
check / input / unresolved / mechanism). Headline: closed forms, monotonicity,
threshold slope at (1,2), moment identities = established (symbolic +
high-precision quadrature, MC cross-checks); the "interior maximum exists iff"
and the general-g threshold form = NOT asserted in the manuscript text (the iff
needs unimodality, the general form is verified only at (1,2)); the slot
correlations = input; core derivation of the family = unresolved.

## Proposed changes

Single file, single pure insertion, no existing text replaced or edited.

File: chapters/appH-microscopic-proofs.tex
Passage anchor: immediately after the paragraph beginning
"\emph{Exact conditional diagonal law at D=3.}" (L3217, item 101, measured line
length 2846 B, line-initial offset 761965 in live bytes) and before
"\emph{Vacuum term.}" (L3219). Quoted boundary: preceding line begins
"\emph{Exact conditional diagonal law at D=3.} Let $\lambda_{1}>\lambda_{2}>\lamb..."
and ends "...close nothing in Problem~G."; next line begins "\emph{Vacuum term.}".
What is kept: every existing byte; the insert is added between the blank line
after L3217 and the Vacuum-term paragraph.

Anchor choice (Decisions Taken): the orchestrator-offered slots after L3191 and
after L3197 are NOT pure-insertion-safe - the scripted scan shows downstream
ordinal references ("the preceding paragraph" at L3193; "seventh/third/tenth
preceding" at L3199; "fourth/third" L3203; "fourth/second/third/sixth" L3205;
L3207, L3209, L3211, L3215) that an insertion at either slot would silently
re-point; the insertion after L3217 breaks no ordinal (verified across
L3185-3221 and L3223-3309) and remains inside the approved span "after the
integrated 102 paragraph and before the block closer", adjacent to the
measures-side discussion rather than after the citation-type Vacuum-term note.
The inserted paragraph references neighbours by title fragments only
("Pushforward weights paragraph", "flat-Dirichlet statistics paragraph",
"fixed-trace beta-deformation paragraph", "variational-rigidity paragraph",
"Missing step paragraph"), never by ordinals, so it is insertion-robust.

Inserted text (the exact bytes of insert-r1.tex, 4205 B, sha8 1bd7af30, one
CRLF-terminated line, ASCII-only):

```latex
\emph{Coherence-induced non-product slot laws and their profile pushforward weights at \(D=2\).} Within a named correlated two-slot gaussian law, with slots \(w_{1},w_{2}\) complex gaussian of mean zero and prescribed covariance \(\mathbb{E}\,w_{i}w_{j}^{*}=\Sigma_{ij}\) with diagonal entries \(g_{1},g_{2}>0\) and coherence \(\rho=\Sigma_{12}\) at \(g_{1}g_{2}>\lvert\rho\rvert^{2}\): writing \(E_{i}=\lvert w_{i}\rvert^{2}\) and \(\Delta=g_{1}g_{2}-\lvert\rho\rvert^{2}\), the joint density of \(E_{1},E_{2}\) is proportional to \(e^{-(g_{2}E_{1}+g_{1}E_{2})/\Delta}I_{0}(2\lvert\rho\rvert\sqrt{E_{1}E_{2}}/\Delta)\), the slot phases contributing the modified Bessel factor \(I_{0}\), so the squared slot magnitudes are dependent; and for the simplex coordinate \(p=E_{1}/(E_{1}+E_{2})\) the pushforward density is exact at \(D=2\): \(f(p)=\Delta b/(b^{2}-c^{2})^{3/2}\) with \(b=g_{2}p+g_{1}(1-p)\) and \(c=2\lvert\rho\rvert\sqrt{p(1-p)}\), by the ray integral \(\int_{0}^{\infty}\tau e^{-b\tau}I_{0}(c\tau)\,d\tau=b/(b^{2}-c^{2})^{3/2}\); the density is normalized on \(0<p<1\), depends on the coherence only through \(\lvert\rho\rvert\), and at \(\rho=0\) reduces exactly to the exponential product-slot density \(g_{1}g_{2}/(g_{2}p+g_{1}(1-p))^{2}\) of the Pushforward weights paragraph. Three structural facts are exact. At equal variances, with normalized coherence \(r=\lvert\rho\rvert/\sqrt{g_{1}g_{2}}\), the density is exactly \((1-r^{2})/(1-4r^{2}p(1-p))^{3/2}\), strictly increasing in \(p(1-p)\): its maximum is unique at the barycenter \(p=1/2\) with value \(1/\sqrt{1-r^{2}}\) against the vertex values \(1-r^{2}\), the coincidence window obeys \(\mathbb{P}(\lvert 2p-1\rvert<\varepsilon)=\varepsilon/\sqrt{1-r^{2}}+O(\varepsilon^{3})\), and \(\mathbb{E}(p^{2}+(1-p)^{2})<2/3\), below the flat-simplex value recorded in the flat-Dirichlet statistics paragraph, for every \(r>0\); coherence thus peaks, at equal slot variances, a weight that is flat at uniform input for the exponential product-slot law. At unequal variances the relabelling symmetry is broken by the input labels and the maximum bifurcates from a vertex to the interior: at \((g_{1},g_{2})=(1,2)\) the right-derivative at \(p=0^{+}\) of \(\log f\) is \(6\lvert\rho\rvert^{2}-2\), the vertex maximum destabilizes at \(\lvert\rho\rvert^{2}=1/3\), i.e. normalized coherence \(\lvert\rho\rvert/\sqrt{g_{1}g_{2}}=0.408248290463863\), and fine-grid argmax tables record an interior maximum near \(p=0.099\) at \(\lvert\rho\rvert=0.7\). The joint Laplace transform of the squared magnitudes is \(\det(I+T\Sigma)^{-1}\) for diagonal \(T\), and the contingency-table complex-wick formula gives exact mixed moments: \(\mathbb{E}[E_{1}E_{2}]=g_{1}g_{2}+\lvert\rho\rvert^{2}\) at \(D=2\), and \(\mathbb{E}[E_{1}E_{2}E_{3}]=1+3t^{2}+2t^{3}\) at \(D=3\) for equicorrelated unit-variance slots, whose profile statistics shift toward uniformity relative to the flat Dirichlet values; the ray formula reproduces exactly the product-class closed density at diagonal covariance at \(D=2\) and \(D=3\). The named family is non-product at finite slot number, its squared slot magnitudes being dependent, so it lies outside the product slot class of the recorded fibre-integration bound; the equal-coherence members are relabelling-invariant and their unique maximum is the barycenter, consistent with the orbit-rigidity alternative recorded in the fixed-trace beta-deformation paragraph, while the unequal-variance members realize, within the named family, a selection mechanism driven by input label asymmetry. The coherence and the variances are inputs of the named family, supplied by nothing upstream in the core; the frame measure is not entered, and non-degeneracy along the kernel directions of the variational-rigidity paragraph is not assessed. These statements are exact-formula, monotonicity and bifurcation statements for the named correlated gaussian slot family, with \(D=3\) moment identities checked by Monte Carlo; they derive no slot law from the core action, they supply no state and no selected profile, they leave the missing steps (i)-(iv) of the Missing step paragraph unchanged, and they close nothing in Problem~G.
```

Stale passages elsewhere: none identified; no replacements.

## Verification scripts

Folder: proposals/103-g-moments-nonproduct-measures/
- s1_wick_pushforward_D2.py/.out, s2_selection_bifurcation.py/.out,
  s3_generalD_checks.py/.out (surviving derivation/check scripts, re-run
  verified; reproduction invariants in findings.md section 7).
- hygiene_103.py / hygiene_103.out: HYGIENE PASS (exit 0). Confirms: ASCII-only,
  no BOM, single CRLF-terminated line, balanced delimiters, no \ref/\label/
  \eqref, every backslash macro used occurs in appH (counts printed), closing
  idiom "they close nothing in Problem~G." exactly once, no ordinal paragraph
  references.
- simulate_apply_103.py / simulate_apply_103.out: SIMULATION PASS (exit 0).
  PRE asserts 801632 B / e37ca5385996df34 / CRLF 3868 / bareLF 0 / no BOM;
  header prefix "\emph{Exact conditional diagonal law at D=3.}" count 1,
  line-initial at offset 761965, line 2846 B; PIN (line + CRLF + blank CRLF)
  = 2850 B, count 1; bytes at cut = "\emph{Vacuum term.}"; payload = insert
  (4205 B, sha8 1bd7af30) + blank-CRLF = 4207 B; POST = 805839 B, sha256-16
  21163962e4f7f514, CRLF 3870, bareLF 0, PIN still unique; POST written only to
  scratch/103_sim_post.tex.

Reproduction pack (commands + expected invariants): findings.md section 7.

## Decisions Taken

1. Anchor after L3217 instead of the orchestrator-suggested after-L3191 /
   after-L3197 slots: pure insertion at the suggested slots silently corrupts
   the ordinal chain (scripted scan evidence in findings.md 6.8); after-L3217
   is ordinal-safe on both sides (checked to L3309), inside the approved span,
   and topically adjacent to the measures/pushforward discussion. Rejected:
   after-L3219 (would place a measures paragraph after a citation note with no
   benefit); renumbering downstream ordinals (not pure insertion, forbidden).
2. The insert claims only the symbolically verified threshold at (g1,g2)=(1,2)
   and records the global switch numerically; the printed "iff" and the
   general-g threshold form are kept out of manuscript text (findings.md 6.2,
   6.3). Rejected: importing the printed iff as a derived statement.
3. All numbers in the insert are taken from the .out files (rule 7); no
   literature citations added.
4. s2 docstring/outputs mismatch resolved in favour of the .out values
   (re-derived independently; findings.md 6.1).

## Milestone assessment

Routine. No MILESTONE.md trigger is claimed: this is a conditional member
family, not a critical-path step derived from the matrix theory; it does not
supply a core-produced profile-space weight.

## Status-label recommendation

No label change proposed. Current critical-path set re-derived from the Missing
step paragraph and the frontier excerpt (chain 2 head G.moments-nonproduct-
measures, dispatchable, was "untried"): this package makes the edge
attempted-open in its own record terms, but I propose no status, priority or
completion-classification edit anywhere.

Author decision needed: none.

## Remaining open step

To move G.moments-nonproduct-measures toward its original target one still
needs: (a) a derivation of a correlated (non-product) slot law from the core
action or a derived core state - the coherence must become an output, not an
input; (b) the joint law on slot-simplex x frame space and its induced profile
weight (frame factor untouched here); (c) non-degeneracy of the induced weight
along the 088 kernel directions; (d) the D=2 general-D pushforward density and
the general-g threshold proof (beyond the moments established here). Within the
named family, (i) unimodality of f at unequal variances (closing the printed
"iff") and (ii) the symbolic general-g vertex threshold are cheap sub-lemmas a
later round could close.

## Special instructions for the gatekeeper

1. Verify the insert against the .out files only (rule 7): every number in the
   paragraph appears in s1/s2/s3 .out (0.408248290463863, 0.09909->0.099 as
   "near 0.099", 6*r**2-2, 1/3, 2/3, 1+3t^2+2t^3, eps/sqrt(1-r^2),
   1/sqrt(1-r^2), 1-r^2, (1,2)).
2. Check first: the anchor-safety scan (findings.md 6.8) - if you find any
   cross-reference outside L3185-L3309 that an insertion after L3217 would
   break, the insert must move to after L3219 (ordinal-safe by the same scan)
   with no text change.
3. What must NOT be asserted on integration: that the core produces correlated
   slots or a selected profile; that the 089 bound is refuted (it is evaded by
   class extension, its scope statement stands); that the bifurcation selects a
   profile outside the named family; any status change to Problem G or its
   missing steps (i)-(iv).
4. Re-run the three scripts (fixed seeds; byte-stable outputs) and the two
   gate scripts; re-check PIN count 1 and bytes-at-cut against the live tree
   before splicing (another chain may have moved the text).
5. The paragraph's "the recorded fibre-integration bound" refers to the
   integrated 089 paragraph's product-class statement; verify the wording
   matches the current L3191 class clause ("the wider class of product slot
   laws in which the squared slot magnitudes are independent and the law of
   each is fixed by \(s^{2}\) times the slot variance").
6. Known tolerances: MC numbers are consistency checks at the stated sample
   sizes; the insert's Monte-Carlo-dependent clauses are phrased as "recorded"
   / "checked by Monte Carlo" accordingly.
