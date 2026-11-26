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

```
difflib SequenceMatcher character-level opcodes, payload-126-v2.txt -> payload-126-v3.txt
v2 sha1 b9ebeba71fe933b1048dbcd2a0ec4f46d89c54dd 4447 B ; v3 sha1 fb89da16df60f08b595e3fb0df71ce577e05fb61 4915 B
DELETE old[129:134] new[129:129]
  BEFORE: ...the two relations of the class over << with>>  \(\mathcal A=\mathbb C\) at finite...
  AFTER : ...the two relations of the class over <<>>  \(\mathcal A=\mathbb C\) at finite...
INSERT old[1171:1171] new[1166:1330]
  BEFORE: ...ctor therefore vanishes identically <<>> , and the first relation then force...
  AFTER : ...ctor therefore vanishes identically <<; because the \(\mathcal S\)-sector of the class retains the \(\mathfrak{so}(3,1)\) bracket and \(\mathfrak{so}(3,1)\) is perfect, this forces \(\mathcal S_{cd}=0\)>> , and the first relation then force...
INSERT old[1309:1309] new[1468:1474]
  BEFORE: ...inite-\(N\) realization of the two  <<>> relations with anti-Hermitian \(\ma...
  AFTER : ...inite-\(N\) realization of the two  <<class >> relations whose \(\mathcal S\)-sect...
INSERT old[1318:1318] new[1483:1555]
  BEFORE: ...\) realization of the two relations <<>>  with anti-Hermitian \(\mathcal S\)...
  AFTER : ...lization of the two class relations << whose \(\mathcal S\)-sector retains the \(\mathfrak{so}(3,1)\) bracket,>>  with anti-Hermitian \(\mathcal S\)...
INSERT old[1353:1353] new[1590:1591]
  BEFORE: ... with anti-Hermitian \(\mathcal S\) <<>>  is trivial, a unitary realization ...
  AFTER : ... with anti-Hermitian \(\mathcal S\) <<,>>  is trivial, a unitary realization ...
INSERT old[1408:1408] new[1646:1799]
  BEFORE: ...ry realization requires \(N=\infty\ <<>> ), and non-unitary \(\mathcal S\) i...
  AFTER : ...ry realization requires \(N=\infty\ <<) (the general statement recorded in the conjugate-coordinate analysis under Problem~E; the application here is to the \(\mathcal S\)-sector of the class>> ), and non-unitary \(\mathcal S\) i...
INSERT old[2169:2169] new[2560:2568]
  BEFORE: ... the label Lorentz matrix exactly ( <<>> rotation and boost generators, at \...
  AFTER : ... the label Lorentz matrix exactly ( <<for one >> rotation and one boost generator at...
INSERT old[2181:2181] new[2580:2584]
  BEFORE: ...orentz matrix exactly (rotation and <<>>  boost generators, at \(t=1\), exac...
  AFTER : ...atrix exactly (for one rotation and << one>>  boost generator at \(t=1\), exact ...
DELETE old[2197:2199] new[2600:2600]
  BEFORE: ...actly (rotation and boost generator <<s,>>  at \(t=1\), exact exponentials), t...
  AFTER : ...ne rotation and one boost generator <<>>  at \(t=1\), exact exponentials), t...
REPLACE old[2554:2555] new[2955:2956]
  BEFORE: ...bb D_a\) on that span is \(\mathbb  <<C>> \mathbb I\) plus the nilpotent \(\o...
  AFTER : ...bb D_a\) on that span is \(\mathbb  <<R>> \mathbb I\) plus the nilpotent \(\o...
INSERT old[3939:3939] new[4340:4346]
  BEFORE: ...ruction above. Hypotheses: the two  <<>> relations at face value with consta...
  AFTER : ...ruction above. Hypotheses: the two  <<class >> relations at face value with consta...
INSERT old[3989:3989] new[4396:4448]
  BEFORE: ...ce value with constant coefficients <<>> , finite \(N\), no state, no dynami...
  AFTER : ...ce value with constant coefficients << and with the \(\mathcal S\)-sector bracket retained>> , finite \(N\), no state, no dynami...
INSERT old[4379:4379] new[4838:4849]
  BEFORE: ...frame-lock} and~\ref{ass:nondeg}):  <<>> this paragraph closes none of Probl...
  AFTER : ...frame-lock} and~\ref{ass:nondeg}):  <<nothing in >> this paragraph closes any of Proble...
INSERT old[4401:4401] new[4871:4872]
  BEFORE: ...ss:nondeg}): this paragraph closes  <<>> none of Problem~D, Problem~D1, or P...
  AFTER : ...: nothing in this paragraph closes  <<a>> ny of Problem~D, Problem~D1 or Prob...
REPLACE old[4402:4405] new[4873:4874]
  BEFORE: ...s:nondeg}): this paragraph closes n <<one>>  of Problem~D, Problem~D1, or Probl...
  AFTER : ...nothing in this paragraph closes an <<y>>  of Problem~D, Problem~D1 or Proble...
DELETE old[4430:4431] new[4899:4899]
  BEFORE: ...loses none of Problem~D, Problem~D1 <<,>>  or Problem~A.
...
  AFTER : ...closes any of Problem~D, Problem~D1 <<>>  or Problem~A.
...
SEGMENT-COUNT 16
```

## Payload v3 (embedded verbatim from disk bytes)

PAYLOAD-EMBEDDED-SHA1 fb89da16df60f08b595e3fb0df71ce577e05fb61 BYTES 4915 EMBED-MATCHES-PAYLOAD True
(the disk file is exactly the single line below plus one CRLF terminator)
```
\emph{Finite matrix size: a unitarity obstruction and two exact algebraic realizations.} Take the two relations of the class over \(\mathcal A=\mathbb C\) at finite matrix size \(N\), keeping the \(*\)-structure on \(\mathcal S_{cd}\) (anti-Hermiticity). For anti-Hermitian \(A\) one has \(\operatorname{tr}(\operatorname{ad}_A\operatorname{ad}_A)=-\lVert\operatorname{ad}_A\rVert_{\mathrm{HS}}^2\le0\), so every matrix Lie algebra of anti-Hermitian matrices has negative-semidefinite Killing form; \(\mathfrak{so}(3,1)\) is simple with indefinite Killing form (in the vector representation \(\operatorname{tr}(\operatorname{ad}_{J_{12}}\operatorname{ad}_{J_{12}})=-4\) and \(\operatorname{tr}(\operatorname{ad}_{K_1}\operatorname{ad}_{K_1})=+4\)). The adjoint action of the \(\mathcal S\)-sector of the class is a homomorphic image of \(\mathfrak{so}(3,1)\) formed by anti-Hermitian endomorphisms of the matrix space; a homomorphic image of a simple Lie algebra is either \(0\) or an isomorphic copy, and the latter would make the Killing form both negative-semidefinite and indefinite: the adjoint action of the \(\mathcal S\)-sector therefore vanishes identically; because the \(\mathcal S\)-sector of the class retains the \(\mathfrak{so}(3,1)\) bracket and \(\mathfrak{so}(3,1)\) is perfect, this forces \(\mathcal S_{cd}=0\), and the first relation then forces \(\mathbb D_a=0\) (its label map has rank \(4\)). Hence the only finite-\(N\) realization of the two class relations whose \(\mathcal S\)-sector retains the \(\mathfrak{so}(3,1)\) bracket, with anti-Hermitian \(\mathcal S\), is trivial, a unitary realization requires \(N=\infty\) (the general statement recorded in the conjugate-coordinate analysis under Problem~E; the application here is to the \(\mathcal S\)-sector of the class), and non-unitary \(\mathcal S\) is unavoidable in any finite-\(N\) Lorentzian data of the class; this is why the compact fibres used elsewhere in this section are not obstructed. With the \(*\)-structure relaxed, two exact realizations show that the relations are consistent at finite \(N\) with the Lorentzian \(\eta\) contraction. (i) \(5\times5\) real matrices, \(\mathbb D_a=E_{a4}\) and \(\mathcal S_{cd}\) the standard affine lift of the vector representation, \((\mathcal S_{cd})^{\mu}{}_{\nu}=\delta^{\mu}_{c}\eta_{d\nu}-\delta^{\mu}_{d}\eta_{c\nu}\): both relations hold exactly with \(\mathsf T=\mathsf R=\mathsf F=0\); the inner automorphism \(\mathrm e^{\mathcal S}\mathbb D_a\mathrm e^{-\mathcal S}\) reproduces the label Lorentz matrix exactly (for one rotation and one boost generator at \(t=1\), exact exponentials), the finite-\(N\) form of the identity of the class that local rotations are matrix gauge transformations; the ghost operator \([\hat X^a,[\hat X_a,\cdot\,]]\) vanishes on \(\operatorname{span}\{\mathbb I,\mathcal S,\mathbb D\}\); and the centralizer of the adjoint action of the \(\mathbb D_a\) on that span is \(\mathbb R\mathbb I\) plus the nilpotent \(\operatorname{span}\{\mathbb D_a\}\) (all products zero), whose spectrum is a point: at \(N=5\) no base manifold sits inside the fibre algebra. (ii) \(4\times4\) complex matrices, \(\mathbb D_a=\gamma_a\) the Lorentzian Clifford generators (\(\gamma_0\) anti-Hermitian, \(\gamma_i\) Hermitian) and \(\mathcal S_{cd}=\tfrac14[\gamma_c,\gamma_d]\): both relations hold exactly with \(\mathsf T=\mathsf F=0\) and \(\mathsf R_{ab}{}^{cd}=4(\delta_a^c\delta_b^d-\delta_b^c\delta_a^d)\), and the contracted matrix identity holds exactly, \([\mathbb D^a,[\mathbb D_a,\mathbb D_b]]=\mathsf R_{ab}{}^{ae}\mathbb D_e=12\,\mathbb D_b\), i.e. \(\mathrm{Ric}_b{}^e=-12\,\delta_b{}^e\) under the identity \(\mathsf R_{ab}{}^{ae}=-\mathrm{Ric}_b{}^e\) of the matrix equation; the sign of \(\mathcal S_{cd}\) is forced, by the first relation (48 exact checks) and independently by this contraction. The operator \([\mathbb D^a,[\mathbb D_a,\cdot\,]]\) on \(\operatorname{End}(\mathbb C^4)\), the class ghost operator up to the sign of \(\hat X_a=\mathrm i\mathbb D_a\) at \(N=4\), has kernel the scalars and eigenvalues \(12,8,16,4\) on the vector, bivector, pseudoscalar and axial sectors of the \(16\) Dirac bilinears, which close under both adjoint actions with rational constants; its mixed \(*\)-structure is forced by the obstruction above. Hypotheses: the two class relations at face value with constant coefficients and with the \(\mathcal S\)-sector bracket retained, finite \(N\), no state, no dynamics, no reference to Equation~\eqref{eq:Smatrix}, no matter content, no selection; these are consistency and obstruction results at the algebraic level, they derive no \(\mathrm{SO}(3,1)\) from the matrix algebra or the condensate, and they construct neither the locked frame nor its non-degeneracy (Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg}): nothing in this paragraph closes any of Problem~D, Problem~D1 or Problem~A.
```

## Proposed changes (manuscript)

One insertion, into chapters/appH-microscopic-proofs.tex. Anchor (verified exactly 1x in the live base at 76d862968c31.../875,106): the sentence ending "...remains supplied: this paragraph closes none of Problem~D, Problem~D1, or Problem~A." at the end of L1740 (item-120 paragraph), followed by a blank line and then \section{Problem E: signature}. The payload is inserted as a separate paragraph between that sentence and the section command, via the recipe

```
live.replace(ANCHOR, ANCHOR + payload_v3 + CRLF, 1),
ANCHOR = "supplied: this paragraph closes none of Problem~D, Problem~D1, or Problem~A." + CRLFCRLF
```

giving POST 880,023 = 875,106 + 4,915 + 2 (independently recomputed from live bytes; LEN-CHK and RECIPE-CHK True). The canonical form replace(anchor, payload+anchor) is the WRONG object (880,021 bytes, payload before the anchor sentence; review-r1, Splice section). Everything existing is kept: no sentence is removed or replaced, the item-120 anchor sentence stays, and the new paragraph's variant closer leaves the old closer at exactly 1 whole-file occurrence (the anchor). Stale passages elsewhere: none - the D1 paragraph is new to this chain; payload-126.txt (v1) and payload-126-v2.txt (v2) were never integrated and must not be (superseded; preserved on disk for audit).

## Verification scripts and reproduction pack

All commands run from proposals/126-d1-lorentz with the repo root as argument; captures persisted in this folder.

| script | re-run command | expected invariant output |
|--------|----------------|---------------------------|
| make_payload_126.v3.py | python -I make_payload_126.v3.py "<repo>" | exit 0; 19 CTRL-FIRED, 0 CTRL-DEAD; CTRL-FIRED-TOTAL 19; PAYLOAD-V3-BYTES 4915; PAYLOAD-V3-SHA1 fb89da16df60f08b595e3fb0df71ce577e05fb61; PRE 875106 POST 880023; EXPECTED-POST 880023 MATCH True; SPLICED-SHA1 123108d4a94723be1dbad752883125baac940fe4; ANCHOR-COUNT-SPLICED 1; CLOSER-COUNT-SPLICED 1; MAKE-OK |
| independent POST/recipe recompute | python -I -c "b=open('<repo>/chapters/appH-microscopic-proofs.tex','rb').read(); p=open('payload-126-v3.txt','rb').read(); s=open('appH-spliced-126-v3.tex','rb').read(); A=b'supplied: this paragraph closes none of Problem~D, Problem~D1, or Problem~A.\r\n\r\n'; print(len(b),len(p),len(s), len(b)+len(p)+2==len(s), s==b.replace(A,A+p+b'\r\n',1), b.count(A), s.count(A))" | 875106 4915 880023 True True 1 1 |
| cert_stage_126.r2.py + 2x pdflatex -interaction=nonstopmode -halt-on-error namcg-book7.tex in the staged tree | see out-cert-126-v4.txt | STAGE-OK with staged-appH hash assert; PASS1/PASS2 exit 0; log '^!' 0; undefined References 0; multiply-defined 0; undefined Citations 196 (baseline, bibtex not run); pdf 3,197,586 B; probes PROBE-RESULT-SCOPED ALL-OK |

Guard controls (the run-hazard rule that every hygiene/join guard needs an injected positive control): ascii, bom, bareLF, bareCR, single-CRLF-terminator, braces, dollar-parity, zero-\label, zero-\cite, ref-set-exactly-{eq:Smatrix, ass:frame-lock, ass:nondeg}, bad-H3-parenthetical-absent, "over with"-absent, blackboard-CI-absent, old-closer-absent, old-quantifier-absent, appH-pin, anchor-unique, join-length (control: the canonical-wrong splice), closer-duplication (control: the v2 splice - the Finding-5 defect itself is the injected sample). Every control prints CTRL-FIRED; a vacuous guard prints CTRL-DEAD and aborts.

Round-1 scripts verify_126_A_nogo.py (aa8135e0299f7ed1801e9c49dc214136b84c21a2, 7,068 B), verify_126_B_flat5.py (b87f28eeedc38d0798bf09ec6d74494ae52505d9, 7,913 B), verify_126_C_spinor.py (52f7204c5443ad4308fe58309243931987a010c8, 12,328 B): bytes untouched; re-executed by the review pass with ALL-PASS and outputs byte-identical to out-A-run4.resume.txt (b75bb07c1f65...), out-B-run4.resume.txt (46396df66b2c...), out-C-run3.resume.txt (8a58011ca975...). The v3 edits change no numeral, so every quantity those scripts check is untouched by this revision. Frozen: proposals/123-f-coeff-locked-block/verify_ghost_op_123.py never run (author order). The repository itself was never built; the certificate ran in the external staged copy.

## Claim classification (round-2 restatement)

- Established identity/derivation (unchanged from round 1): tr(ad_A ad_A) = -||ad_A||^2_HS for anti-Hermitian A; Killing numbers -4 (rotation) and +4 (boost) in the vector representation; a homomorphic image of a simple Lie algebra is 0 or a copy; ad S = 0 for the class's S-sector adjoint action; D = 0 from the first relation (rank-4 label map, non-degenerate eta in dimension 4); both exact finite-N models and every model-tied identity and eigenvalue (relations with the stated T/R/F, R_ab^{ae} D_e = 12 D_b, Ric = -12 delta via the L1630 identity, kernel and eigenvalues 12, 8, 16, 4 of the N=4 operator, the 48-check sign forcing, the centralizer shape of script B R6 over the rationals, the one-rotation/one-boost inner-automorphism identity at t=1); the F1 sign correction.
- Conditional theorem under H1-H5 (H5 a disclosed reading hypothesis, non-load-bearing): the only finite-N realization of the two class relations whose S-sector retains the so(3,1) bracket, with anti-Hermitian S, is trivial; the bracket-retention input is now explicit in the payload chain, conclusion and hypothesis list. The corollaries ("unitary realization requires N = infinity"; "non-unitary S unavoidable at finite N of the class") inherit exactly this conditionality. Weak adjoint-only closure does NOT force the conclusion: the central-scalar datum S_cd = i*lambda_cd*I with all other class data zero satisfies both relations and falsifies the unqualified sentence (review-r1 Finding 1) - this is the mathematical content of the Finding-7 correction below.
- Standard lemma, not claimed new: finite-N Hermitian representations of a non-compact simple Lie algebra are trivial; recorded at appH L1931 (verified live this pass) and applied there to the five-index so(4,1) conjugate-coordinate algebra. The payload points to it in prose; the present application (the S-sector of the D1 first-order class) is a distinct specialization, and neither overlap nor novelty is claimed for the lemma itself.
- Models: exact algebraic consistency witnesses under explicit relaxations (drop H2: flat 5x5 real affine; drop *-unitarity and read over C: the 4x4 spinor model); verified computations, closing nothing.
- Unresolved: any derivation of SO(3,1), the locked frame, or its non-degeneracy from the matrix construction - the D1 target itself.

## Finding 7 correction (proposal text; never payload)

proposal-r1.md, H3, L182-184 read: "Note the formulation avoids the central-extension ambiguity of a literal \(\mathcal S\mapsto\) matrices homomorphism claim (journal T4): only the adjoint action needs to be a homomorphic image." The final clause is wrong: it admits exactly the central-scalar datum that falsifies the unqualified triviality conclusion (review-r1 Findings 1 and 7), and it is inconsistent with Research B step 6, which states the strong closure actually used. Corrected H3 statement used from round 2 on: the S-sector is assumed to RETAIN the bracket, \([\mathcal S_X,\mathcal S_Y]=\mathcal S_{[X,Y]}\) (strong closure; Research B step 6). Together with ad S = 0 this makes each S central, forces \(\mathcal S_{[X,Y]}=0\), and perfection of so(3,1) then forces S = 0 - the step payload v3 now spells out. The central-extension remark survives only as the observation that the weak adjoint-action formulation, while sufficient for ad S = 0, cannot deliver S = 0; the strong retention assumption is precisely what a central two-form ambiguity would violate, and no literal "S maps by a homomorphism" claim stronger than bracket retention is needed or made. The bad parenthetical never appeared in payload v2 and its absence from payload v3 is asserted by the generator (guard badh3-absent, CTRL-FIRED).

## Remaining open step

Unchanged by this revision: D1 (derive local SO(3,1), the locked frame and its non-degeneracy from the matrix construction) stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. This package derives a conditional obstruction (triviality under H1-H5 with bracket retention, H5 disclosed and non-load-bearing) and two exact models under explicit relaxations; it supplies no premise the target needs and closes nothing. Ranked open avenues (review-r1): (1) drop H2 - non-anti-Hermitian (mixed-*) S is what finite-N Lorentzian data of the class forces, with the flat model as the witness that the relations then hold exactly; (2) release H1 - unitary fibres at N = infinity; (3) relax the H5 reading - class relations with nonzero S survive when the coefficient algebra is not C; (4) adjoint-action-only closure (central-S datum) - logically admissible, least promising.

## Decisions Taken

- Adopted the review's Required-action wording for all six payload edits. Where mathematically equivalent wording was permitted: the Finding-5 closer follows the book's own variant formula at appH L1731 ("nothing in this paragraph closes ...") with the identical problem list (D, D1, A) and no status labels; the Finding-2 pointer mirrors the review's own description of the recorded lemma and claims neither overlap nor novelty.
- Finding 7 (researcher decision): delete and replace the weak-closure parenthetical with the strong bracket-retention statement per Research B step 6, because the weak form admits the central-scalar counterexample and would make the payload conclusion false on its stated premises; the alternative (rewording the parenthetical to keep weak closure) was rejected as it preserves a false claim.
- The generator reads payload-126-v2.txt from disk (pin-asserted) and applies the eight byte replacements, so v3 is provably v2 plus exactly the prescribed edits (each old string asserted unique; each new string asserted exactly-once and absent from v2); retyping the body was rejected for silent-drift risk.
- Rejected: adding a label or \eqref at appH L1931 - no label exists there, editing another part of appH is outside this single-insertion package, and the review prescribed the prose form.
- Rejected: whole-book-count defect probes - the string "over with" occurs twice in unrelated pre-existing book text (ch02 exercises note; an appendix passage); defect probes are scoped to the spliced paragraph and the two hits are recorded in the certificate so a future whole-book count cannot mis-fire.
- Certificate: fresh external tree C:/Users/redgi/AppData/Local/Temp/build126_cert_v4_12620 (new name, kept, outside the repo; repository never built, never written outside this folder).

## Milestone assessment

Routine: a round-2 revision package with no new mathematics; no MILESTONE.md trigger applies (the mathematical scope is the bounded conditional obstruction plus two exact models that review-r1 classified as non-milestone; the Chapter 17 D1 criterion is untouched).

## Status-label recommendation

Unchanged for every label. Critical-path list re-derived from the current Chapter 17 criterion and Appendix H: A, B, C, D1, E, F, G-derived and N (H, I, J optional within their stated scopes). D1 stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; no label, priority or completion-classification edit is proposed or made.

## Author decision needed

None.

## Special instructions for the gatekeeper

- Scope of this package: payload v3 + splice + certificate + this document. Do not integrate v1 or v2 objects (preserved bytes: payload-126.txt 7e6ed4cd6c83/4,361; payload-126-v2.txt b9ebeba71fe9/4,447; generators v1 d2826812c80a, v2 e996ca20baad/7,417).
- Anchor and recipe: ANCHOR = "supplied: this paragraph closes none of Problem~D, Problem~D1, or Problem~A." + CRLFCRLF, unique at appH L1740; insertion recipe live.replace(ANCHOR, ANCHOR + payload_v3 + CRLF, 1); expect POST 880,023 = 875,106 + 4,915 + 2; the canonical replace(anchor, payload+anchor) form is the wrong object (880,021). appH must still be 76d862968c31d78fffc665f72aaf60d40c90367a / 875,106 B at integration time.
- Re-checks suggested: re-run make_payload_126.v3.py (expect 19 CTRL-FIRED, 0 CTRL-DEAD, MAKE-OK) and the independent POST one-liner; confirm each of the six finding edits appears exactly once in the v3 bytes and the Finding-7 parenthetical phrase is absent; confirm the difflib segments account for all and only the eight replacements; confirm the central-scalar datum does not satisfy the qualified conclusion's premises (it fails bracket retention unless lambda = 0, since so(3,1) is perfect).
- The certificate need not be re-run unless bytes change; out-cert-126-v4.txt carries the full probe table, the scoped-resolution note for the two pre-existing whole-book "over with" hits, and the baseline citation count.
- Must not be asserted anywhere in the integrated text: any closure (of D, D1 or A), any derivation of SO(3,1) from the matrix algebra or the condensate, any novelty for the Problem E lemma, or any unqualified triviality sentence without the bracket-retention premise.
- Script B's stale docstring line 19 / R6 print labels (review-r1 Finding 4 side note) are script-internal and byte-preserved; the executable checks are correct.
