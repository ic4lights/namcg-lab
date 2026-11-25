# Proposal 126-d1-lorentz, round 2

Round-2 revision responding to proposals/126-d1-lorentz/review-r1.md (verdict ACCEPT WITH REQUIRED REVISIONS; Findings 1(i)-(iii), 2, 3, 4, 5, 6 are payload edits, Finding 7 is proposal-text only). The round-1 record (proposal-r1.md) and all v1/v2 payload, generator, splice and certificate bytes are preserved unmodified as the auditable prior versions.

## Result (round 2)

Payload v3 applies exactly the six clause-level edits required by review-r1 and no other bytes. (1) The missing S=0 step is now explicit: after "vanishes identically" the chain records that the S-sector of the class retains the so(3,1) bracket and that so(3,1) is perfect, which forces S_cd=0; the triviality conclusion is qualified to realizations "whose S-sector retains the so(3,1) bracket, with anti-Hermitian S"; and the hypothesis list gains "and with the S-sector bracket retained". The conclusion is therefore no longer falsifiable by the central-scalar datum S_cd = i*lambda_cd*I with all other class data zero, which satisfies the two class relations and the weak adjoint-only condition but not bracket retention (review-r1 Finding 1). (2) The N=infinity clause carries a prose pointer to the standard lemma already recorded in the conjugate-coordinate analysis under Problem E (appH L1931; no label exists there, so a prose pointer is the correct form; no overlap or novelty claim is made in either direction). (3) The grammar defect "over with" is repaired to "over \(\mathcal A=\mathbb C\)". (4) The flat-model centralizer is \(\mathbb R\mathbb I\) plus the nilpotent span, matching the real 5x5 ambient algebra and the rational computation of script B R6. (5) The byte-identical repetition of the item-120 closer is replaced by the book's own variant formula at the same scope: "nothing in this paragraph closes any of Problem~D, Problem~D1 or Problem~A." (6) The inner-automorphism clause is quantified to what script B R4 verified: "for one rotation and one boost generator at \(t=1\), exact exponentials". The Finding-7 H3 parenthetical is corrected in this document; the generator asserts its absence from the v3 bytes. Artifacts: payload-126-v3.txt, 4,915 B, sha1 fb89da16df60f08b595e3fb0df71ce577e05fb61; regenerated splice appH-spliced-126-v3.tex, 880,023 B, sha1 123108d4a94723be1dbad752883125baac940fe4 (POST 880,023 = 875,106 + 4,915 + 2, independently recomputed); fresh item-108 certificate on the v3 bytes (out-cert-126-v4.txt: two pdflatex passes exit 0, 0 error lines, 0 undefined references, 0 multiply-defined, 196 undefined citations = baseline, all clause probes passing in the spliced region). No mathematics is new: the content is the round-1 conditional unitarity obstruction, now with the bracket-retention input stated where it is used, plus the two exact relaxed finite-N models and the F1 sign correction.

## Target and status

Problem D1 (within sec:status-D; the Problem D ledger at appH L763-808 records Status OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; no separate Problem D1 ledger line exists). Original target (Chapter 17 D1 item): derive the local SO(3,1), the locked frame and its non-degeneracy from the matrix construction. This package is conditional evidence, not a closure: it derives no SO(3,1) from the matrix algebra or the condensate, constructs neither the locked frame nor its non-degeneracy (Assumptions ass:frame-lock and ass:nondeg stay assumptions), closes none of Problem D, D1 or A, and changes no status, priority or completion label.

## Source reading

digest + targeted reads (round-2 revision with no new mathematics; the protocol 3(a) full scan was discharged for the review pass on 2026-11-25, reports/full-scan-2026-11-25.md, at the same appH baseline). Read in full this pass: review-r1.md (requirements document); payload-126-v2.txt; make_payload_126.v2.py (pin/anchor/hygiene guard regions); appH L1725-1742 live (the nine D1 closers, the anchor sentence at L1740, the closer variant formula at L1731, the L1717 formula); appH L1931 live (the standard-lemma sentence and its so(4,1) conjugate-coordinate application verified verbatim); proposal-r1.md L170-189 (H1-H5 with the Finding-7 parenthetical at L183-184); out-gk126r2-notes.md T-READ/VP lines; out-cert-126-v3.txt (stage recipe); manifest.md and journal.md histories.

## Review findings and dispositions

| # | Severity | Disposition in payload v3 | Verification |
|---|----------|---------------------------|--------------|
| 1(i)-(iii) | major | S=0 step inserted in the chain; conclusion qualified by bracket retention; hypothesis list extended | diff segments r1a/r1b/r1c; PDF probes "is perfect, this forces" x1, "retains the" x2, "realization of the two class relations whose" x1, "with constant coefficients and with the" x1 |
| 2 | major | prose pointer added after "requires \(N=\infty\)": "(the general statement recorded in the conjugate-coordinate analysis under Problem~E; the application here is to the \(\mathcal S\)-sector of the class)" | no label at L1931 (checked live), prose form; probes "analysis under Problem" x1, "application here is to the" x1; no overlap/novelty claim |
| 3 | minor | "of the class over with \(\mathcal A=\mathbb C\)" -> "of the class over \(\mathcal A=\mathbb C\)" | probe context "of the class over A = C"; "over with" x0 in the spliced paragraph (2 whole-book hits are pre-existing unrelated text, recorded in the certificate) |
| 4 | minor | "\(\mathbb C\mathbb I\) plus" -> "\(\mathbb R\mathbb I\) plus" (real model, matches the rational-nullspace computation of script B R6) | PDF context "is RI plus the nilpotent"; "CI plus" x0 |
| 5 | minor | closer replaced by "nothing in this paragraph closes any of Problem~D, Problem~D1 or Problem~A." (book variant formula at appH L1731; same problem list; no status labels) | old closer 1x whole-file (the item-120 anchor only); "closes any of Problem" x1; generator dup-closer guard fires on the v2 object (control) |
| 6 | minor | "(rotation and boost generators, at \(t=1\), exact exponentials)" -> "(for one rotation and one boost generator at \(t=1\), exact exponentials)" | probe "one rotation and one boost" x1 |
| 7 | minor (proposal-only) | H3 parenthetical corrected in this document (see "Finding 7 correction"); never in payload v2, asserted absent from v3 | generator guard badh3-absent, CTRL-FIRED |

Non-blocking note recorded from review-r1 Finding 4: verify_126_B_flat5.py docstring line 19 and the R6 print labels are stale relative to the corrected centralizer claim (they read "span{1}" / "= C + nilpotent" where the corrected centralizer is span{1, D}); the executable checks are correct; the script bytes are left untouched.

## The six payload edits (v2 -> v3, exact bytes)

Eight byte-level replacements (Finding 1 is three of them); each old string was asserted to occur exactly once in the v2 bytes; no other bytes change.

```
r1a old: therefore vanishes identically, and the first relation then forces
r1a new: therefore vanishes identically; because the \(\mathcal S\)-sector of the class retains the \(\mathfrak{so}(3,1)\) bracket and \(\mathfrak{so}(3,1)\) is perfect, this forces \(\mathcal S_{cd}=0\), and the first relation then forces
r1b old: realization of the two relations with anti-Hermitian \(\mathcal S\) is trivial
r1b new: realization of the two class relations whose \(\mathcal S\)-sector retains the \(\mathfrak{so}(3,1)\) bracket, with anti-Hermitian \(\mathcal S\), is trivial
r1c old: Hypotheses: the two relations at face value with constant coefficients, finite \(N\),
r1c new: Hypotheses: the two class relations at face value with constant coefficients and with the \(\mathcal S\)-sector bracket retained, finite \(N\),
r2  old: a unitary realization requires \(N=\infty\), and non-unitary
r2  new: a unitary realization requires \(N=\infty\) (the general statement recorded in the conjugate-coordinate analysis under Problem~E; the application here is to the \(\mathcal S\)-sector of the class), and non-unitary
r3  old: of the class over with \(\mathcal A=\mathbb C\)
r3  new: of the class over \(\mathcal A=\mathbb C\)
r4  old: \(\mathbb C\mathbb I\) plus
r4  new: \(\mathbb R\mathbb I\) plus
r5  old: : this paragraph closes none of Problem~D, Problem~D1, or Problem~A.
r5  new: : nothing in this paragraph closes any of Problem~D, Problem~D1 or Problem~A.
r6  old: (rotation and boost generators, at \(t=1\), exact exponentials)
r6  new: (for one rotation and one boost generator at \(t=1\), exact exponentials)
```

No numeral token is added beyond occurrences of \(\mathfrak{so}(3,1)\) already present in the payload; every numeral in v3 traces to the verified scripts or the round-1 re-derivations (rule 7).

## Payload diff v2 -> v3

@ @DIFF@ @

## Payload v3 (embedded verbatim from disk bytes)

@ @PAYLOAD@ @
