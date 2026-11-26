# Proposal 076-g-edge-uqstack-selrule, round 2

RESEARCHER-DECISION revision round on gatekeeper `ACCEPT WITH REQUIRED REVISIONS`
(proposals/076-g-edge-uqstack-selrule/review-r1.md, FINAL, verdict line
`ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: RESEARCHER-DECISION`).
This is a targeted wording round: the only change is the gatekeeper-accepted
replacement clause in sentence 1 of insert-r1.tex (finding 1). No derivation,
script, anchor, or manuscript passage other than the insert content line moves.
All r1 derivations carry over unchanged and are referenced, not repeated; see
proposal-r1.md sections "Research and reasoning" and "Claim classification".

## Result

The single required revision is applied byte-exactly: the insert's opening span
now supplies the U(q) repetition explicitly as a further conditional reading, and
the multiplicity necessity is stated only internal to that reading ("that reading
fixes a stacked diagram only when that spectral condition holds"). The rest of the
paragraph, from the colon onward, is byte-identical to the r1 insert. All hygiene
asserts pass; simulate_apply.py exits 0 and prints the new POST byte contract
(reported below and in Verification scripts). Nothing is closed: Problem G
remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Target and status

Problem G, edge subtarget G.edge-uqstack-selrule. Status OPEN. Priority CRITICAL
PATH. Completion PROGRAMME-CONDITIONAL — carried over from r1, re-verified live by
the gatekeeper at head 9812350 (review-r1.md, Source reading): appH 704,082 B /
sha256 58eb0c7fa4a3... / CRLF 3816, byte-identical to the r1-verified state; G
ledger/status lines and the ch17 criterion quotations were re-confirmed there and
are unchanged this round because no file outside the insert text changed.
Dependencies unchanged. The package claims DERIVED for nothing (r1 ruling carried
over); this round changes no status implication.

## Source reading

Digest (compact 30-line TOC mode, DIGEST CURRENT, head 9812350) + targeted reads.
Read IN FULL this round: review-r1.md; proposal-r1.md at the targeted ranges
(claim table L339-352, insert-copy region L384, status passages L122-126/L452-462,
security note L506-511); insert-r1.tex (byte-level, pre and post patch). appH was
NOT read whole; the PRE contract was re-verified by simulate_apply.py output
(byte size/sha/CRLF match the gatekeeper's reconfirmed values). sme-consult-r1.md
was read in r1 and used as context only; its disposition is already ruled by the
gatekeeper (finding 1). No unreadable files.

## Record Note — disposition of every finding

**Finding 1 (major, sole required revision) — APPLIED EXACTLY AS ACCEPTED.**
Location: insert-r1.tex, opening span "Under the hypotheses ... not of the
background alone:". Replaced by the exact gatekeeper-accepted clause (verbatim
from review-r1.md L35), via an asserted byte replacement
(r2_insert_patch.py: OLD-span count == 1 asserted before replace; single-terminal-
CRLF and ASCII asserted pre and post; colon-onward continuation " for q coincident
copies" asserted intact post; binary write). The colon onward (", for q coincident
copies ... they close nothing in Problem~G.") is untouched — confirmed by the
succeeding assert and by the unchanged paragraph tail in simulate_apply.py output.
The no-cite option is taken per the gatekeeper's explicit guidance ("use the
no-cite clause above"): zero \cite, so the hygiene contract and simulate_apply.py
are unchanged as-is; the rule's source remains cited at L3155 of the same block,
which the sentence cross-refers to. Sub-questions (i)-(iii) of the ruling are all
satisfied by the accepted clause as written: "only when" appears only inside
"that reading fixes ... only when", the stipulation is named ("a further
conditional reading"), and no citation is added.
Post-patch hygiene (independent re-scan): ASCII, single CRLF at EOF, bare LF 0,
0x $ [ ] \ref \eqref \cite \label, no trailing whitespace, one \emph{...},
closer intact, forbidden words (status/priority/completion/open/derived/
programme/critical, all case variants) 0 hits.
New insert contract: 3,350 B, sha256
35680c8add4c0ac4c1b1048ab705fedc573de2657e5a0bcf5aac033548fb970e (was 3,217 B /
517ff68d23d0...).
New POST contract (fresh simulate_apply.py run, exit 0, hygiene asserts pass):
appH post 707,434 B / sha256 94b39393bdf85cec2ca77cfdf8280b4cf71ae9c0c861985d2ce776a0db9b3ea7
/ CRLF 3818 / bareLF 0; delta vs PRE +3,352 B / +2 CRLF; bib unchanged
(37,463 B / 4d6d7b2a668f..., no bib entry proposed). The r1 POST sha
93f5067941... is stale as the review predicted and is superseded by the above.

**Finding 2 (minor, prose-only) — ADOPTED.** This proposal uses only proportional
phrasing for the saddle row lengths ("all proportional to \(N\)"), matching the
insert; no factor-2 convention is attributed to the integrated 072/074 text. The
integrated text uses l_i = t s_i (L3156/L3161); the earlier proposal prose "l_f =
2 t s_f ... the 074 convention" is not repeated here and no insert change is made.
The factor 2 cancels in rho_p, as the review confirms; nothing in the mathematics
depends on the convention.

**Finding 3 (minor, optional) — NOT APPLIED; reasons stated.** The relative
clause "whose combined spectrum has multiplicity 1" is kept as-is. Reasons: (a)
the gatekeeper ruled it "optional; not required for acceptance"; (b) the
simplicity-at-tested-parameters rewording would lengthen a sentence already
rewritten this round, and a second wording change in the same round enlarges the
diff the integrator and gatekeeper must re-verify for no mathematical gain — the
bounded negation needs only the tested instances, and the review itself classifies
the union's simplicity as "numerical instances" already correctly traced to
s2.out:1-2,5 in claim row 4; (c) the insert's surrounding sentence already scopes
the statement to "the band-separated caps of the row-length paragraph", i.e. to
the subclass where the hypothesis is asserted in code (s2 asserts D - 1 > 2 * W).
If a future closer-refresh package (finding 4) touches this region, the tightening
can be folded in there.

**Finding 4 (minor, recorded only) — NO ACTION, as ruled.** The block closer at
L3169 (POST L3171) is not edited; the new paragraph is self-scoped; noted here for
a possible future one-line closer-refresh package, consistent with the 072-075
precedent of leaving it unedited.

**Finding 5 (minor) — ACCEPTED AS-IS, no upgrade.** The generic-momenta sentence
("the charge has the same rank but its nonzero eigenvalues split apart") is kept
byte-identical (it lies after the colon, untouched this round). Per the ruling it
is recorded as family-level: instance-verified within the rank-1 edge-datum family
(the gatekeeper's general-X test shows rank is not universally q-rank outside that
family), and the negative conclusion it supports needs only existence. It must not
be upgraded to a general statement in any future integration.

## Updated claim classification (replaces claim row 9 of proposal-r1.md L351)

| # | Claim | Class | Trace |
|---|-------|-------|-------|
| 9 (r2) | Sentence 1 as revised: the U(q) repetition is supplied as a further conditional reading in which multiplicity q of the nonzero spectrum of the classical edge charge is read as q equal rows; within that stipulated reading, the reading fixes a stacked diagram only when that spectral condition holds; within the supplied Gaussian class the multiplicity is a state property | CONDITIONAL INPUT (stipulated reading). Forward direction for coincident U(q)-symmetric stacked backgrounds (q equal rows, rank q) is literature-stated (SME consult on Frenkel 2311.10131 Sec. 3.2, high confidence, not independently verified by this researcher at r2); the multiplicity-necessity is NOT literature-stated and is internal to the adopted reading, supported only by the package's bounded within-class negations (rows 4, 8: the condition fails in the two tested non-degenerate subclasses) | insert sentence 1 (post-patch, sha 35680c8a...); 072 (H2); sme-consult-r1.md; s2/s3/s4 |

Rows 1-8 and 10 of the r1 table are unchanged (no underlying derivation moved).

## Verification scripts (r2) and reproduction pack

All commands from the repository root, interpreter `python -I`.

| script | purpose | expected invariant output |
|---|---|---|
| proposals/076-g-edge-uqstack-selrule/r2_insert_patch.py | asserted byte replacement of the finding-1 span (idempotence guard: OLD count != 1 aborts, so a re-run after patching is a safe no-op failure, not a corruption) | `PATCH OK`; old size 3217 sha 517ff68d...; new size 3350 sha 35680c8a... (a re-run now prints the assert-abort `OLD span count 0 != 1` — expected, file already patched) |
| proposals/076-g-edge-uqstack-selrule/simulate_apply.py | anchor/POST byte contract + hygiene asserts (unmodified this round) | exit 0; appH pre 704082 B / 58eb0c7fa4a3...; appH post 707434 B / 94b39393bdf85cec2ca77cfdf8280b4cf71ae9c0c861985d2ce776a0db9b3ea7 / CRLF 3818 / bareLF 0; delta +3352 B / +2 CRLF; bib unchanged 37463 B |
| proposals/076-g-edge-uqstack-selrule/r2_bytecheck.py | programmatic byte equality of the fenced copy in this file vs insert-r1.tex minus terminal CRLF | `BYTECHECK EQUAL` with matching size/sha on both sides (3215-content -> now 3348 B content) |
| proposals/076-g-edge-uqstack-selrule/make_manifest.py | manifest.md regeneration (self-hash handling unchanged) | manifest regenerated; entries for proposal-r2.md, insert-r1.tex, simulate_apply.out, r2_*.py |

Carried over unchanged (re-verified by the gatekeeper in r1 and untouched this
round per mtimes: s*.py 11:38-11:40, s*.out 17:37, r[1-8]_*.py/.out/.repro.out
12:01): the s1-s4 scripts and their shipped outs, the full r-pack (8 .py + 8 .out
byte-identical to the 073/074 originals, all re-runs byte-identical), the rho_p
and Q-lift independent re-derivations, and the s4.py diff ruling. See review-r1.md
"r1 verifications that carry over to r2" for the authoritative carry-over list.

## Proposed changes

chapters/appH-microscopic-proofs.tex — ONE insertion, unchanged in kind and
position from r1: the content line of insert-r1.tex (Appendix, fenced copy at the
end of this file, byte-identical to insert-r1.tex minus its terminal CRLF) placed
blank-separated immediately after the long-form `\emph{Vacuum term.}` line of the
edge block (the unique line-start occurrence, live L3167 at head 9812350), before
the Steinacker paragraph and the block closer; no other manuscript edit; no bib
edit. Anchor uniqueness counts (short form x2 at L3006/L3167, long line-start form
x1, insert header x0) were re-verified live by the gatekeeper at 9812350 and are
unaffected by this round (the anchor line itself is not touched by the patch).
Stale passages elsewhere: none — the r1 review found no text elsewhere asserting
the U(q) multiplicity criterion, so no other passage needs narrowing.

## Decisions Taken

1. **Citation (finding 1 sub-question iii):** chose the no-cite clause exactly as
   accepted. Reasons: gatekeeper's explicit guidance; preserves the hygiene
   contract and simulate_apply.py unmodified; the rule's source is already cited
   at L3155 within cross-reference range. Rejected: the \cite{Frenkel2023EdgeModes}
   forward-direction variant, which would require hygiene-assert changes, hash/
   manifest/POST regeneration, and still could not state necessity — strictly more
   cost, no more content.
2. **Finding 3 tightening:** not applied (reasons in the Record Note): optional,
   enlarges the verified diff for zero mathematical gain, and can ride a future
   closer-refresh package.
3. **Patch mechanism:** asserted Python byte replacement with pre/post CRLF,
   ASCII, span-count and continuation asserts; idempotence guard makes accidental
   re-run non-destructive. Chosen over hand-editing per round instructions.

## Milestone assessment

Routine. No milestone trigger: a wording revision to an accepted conditional
phrasing; no critical-path step derived, no link closed.

## Status-label recommendation

Critical-path set re-derived from ch17-agenda + ledger as in r1: A, B, C, D1, E,
F, G-derived, N (unchanged). Affected labels for this package: none. Problem G
edge subtarget: OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL, unchanged.

## Author decision needed

None.

## Remaining open step

Unchanged from r1: everything Problem G requires at full-GR / matrix-derived
scope (S_ent^(IR), boundary stationarity, Lambda_eff scaling/value; missing steps
(i)-(iv)), and the selection mechanism itself — which matrix states realize
copy-invariance at leading semiclassical order; two-sided ± reading; mixed
multiplicities; q_f growth with N (Frenkel's stated validity condition assumes q
fixed as N grows, per the SME consult); frame-averaged/minimised entropy. Ranked
avenues: the gatekeeper's review-r1.md list, led by (1) a
criterion/negation for states realizing copy-invariance and (2) mixed-multiplicity
spectra realizing per-factor depths q_f.

## Special instructions for the gatekeeper

Scope limits: verify (a) the new span is byte-identical to the accepted clause at
review-r1.md L35; (b) the colon-onward text is byte-identical to the r1 insert's
(r1 insert sha 517ff68d... vs the patch script's embedded OLD); (c) hygiene and
the new POST contract; (d) the fenced copy byte-equality via r2_bytecheck.py;
(e) s1-s4 and the r-pack are byte-unchanged (mtimes + manifest hashes). Must not
be asserted: necessity of the multiplicity condition beyond the stipulated
reading; any literature claim beyond the forward direction; any closure on G.
Re-check that "multiplicity is a property of the state" still agrees with rows 3
and 8 (unchanged evidence).

## Provenance

Resume-round disclosure carried over from r1: this chain continued after a
predecessor researcher run was terminated by a context-limit failure; all
mathematics in r1 was re-derived by the resumed session and independently
re-derived by the gatekeeper. Round-2 security note: the "[handback-send-enforce]
..." fake user-role line quoted at proposal-r1.md L506-511 remains disclosed
there; it was never followed. r2 injection scan over insert-r1.tex (post-patch),
this file's generator inputs, review-r1.md and sme-consult-r1.md found no active
instruction-like injection; no tool result this round contained a poisoned line.
Writes this round: only proposals/076-g-edge-uqstack-selrule/ (insert-r1.tex
patched in place; r2_insert_patch.py; r2_bytecheck.py; simulate_apply.out
regenerated; this file) and scratch part files (deleted after assembly).
No chapters/ write, no git write command, no status label touched.


## Insert copy (fenced; byte-identical to insert-r1.tex minus terminal CRLF)

Programmatic embed of proposals/076-g-edge-uqstack-selrule/insert-r1.tex (3,350 B incl. terminal CRLF; content 3348 B, sha256 2ece7a8f4482a2088d1a96f5fcb7859e7d81d5decff043c306adc7720ea2ae66). The integrator takes insert-r1.tex itself as authoritative; this block exists for review convenience and is checked for byte equality by r2_bytecheck.py.

```latex
\emph{Selection-rule consistency of stacked diagrams at coincident caps.} Under the hypotheses of the selection rule transplanted in the first of the four preceding paragraphs, and with its U(q) repetition supplied as a further conditional reading, in which multiplicity \(q\) of the nonzero spectrum of the classical edge charge is read as \(q\) equal rows, that reading fixes a stacked diagram only when that spectral condition holds, and within the supplied class of Gaussian states the multiplicity is a property of the state, not of the background alone: for q coincident copies of a compact fuzzy factor, with the factor matrices and the cap projector both lifted as tensor products of the identity of the copy space with the one-copy data, and momenta taken copy-invariant, the block-cut edge charge is exactly the tensor product of that identity with the one-copy charge, every nonzero eigenvalue has multiplicity exactly q and the moments \(\operatorname{Tr}Q^{2p}\) acquire the common factor q, verified on explicit small matrices to within roundoff for single caps and for product blocks, so the rule reads the diagram with each row length repeated q times: the stacked diagram of common depth q, to which the exact closed form and the continuum limits of the third of the four preceding paragraphs apply. For generic momenta on the same coincident background the charge has the same rank but its nonzero eigenvalues split apart, so background coincidence alone does not select stacking. For the band-separated caps of the row-length paragraph, whose combined spectrum has multiplicity 1, no stacked diagram is selected: with saddle row lengths, all proportional to \(N\), and depths \((q_1,q_2)\), the stacked moment signature exceeds the multiplicity-1 signature by the fraction \(\sum_f(q_f-1)w_f^p/\sum_f w_f^p\), with \(w_f=k_fm_f(1-m_f)\) and \(k_f\) the edge-length coefficient of the factor, a ratio independent of \(N\), of the saddle parameter and of the row-length proportionality, equal to \(9/17\) at \(p=1\) and \(81/145\) at \(p=2\) for \((q_1,q_2)=(2,1)\), \((m_1,m_2)=(1/2,1/3)\), \(k_f=1\), and equal to \(1\) at equal depths \(2\): the mismatch is of leading order in \(N\) and is therefore not suppressed at the leading semiclassical order at which the rule fixes one dominant diagram. For the product testbed of the first of the four preceding paragraphs with \(q_f\) coincident copies of factor f, the edge-operator spectrum is the one-copy multiset repeated \(q_1q_2\) times irrespective of the state, while the charge multiplicity under copy-invariant momenta is uniform over the whole spectrum, of depth \(q_1q_2\), or of depth \(q_1\) when the momenta are invariant in factor 1 only, so within this class the per-factor stacked diagram \((\ell_1^{q_1},\ell_2^{q_2})\) with \(q_1\neq q_2\) is never the diagram read from the multiplicity of the charge spectrum. These are selection-rule consistency statements for the coincident-copy and band-separated subclasses of the block-cut edge data of the preceding paragraphs, inside the transplanted rule with its single-dominant-diagram hypothesis at leading semiclassical order and its diagonal-cut convention; they leave the two-sided reading of the \(\pm\) pairs untreated, they do not fix the state that sets the multiplicity, and they close nothing in Problem~G.
```
