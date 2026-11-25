GK127 ROUND-2 RE-REVIEW JOURNAL (protocol 5)
================================================

== N2-0 HASH GATE (live bytes, 2026-11-25) ==
review-r1.md            f76ebc655433be2135c8baafa5efd2d5f3a5731a 16525 B MATCH (pin f76ebc655433)
payload-P1.txt          8df7a7f42a971892dec26c4e80ad9d18884b1786   871 B MATCH (frozen r1)
payload-P2.txt          e30a1cd68ed607c1d6f51782039464697225b2e3  3043 B MATCH (frozen r1)
payload-P1-r2.txt       6dd693e2cf0b918cce8b0b7912dbab015203411b  1010 B MATCH
payload-P2-r2.txt       73aca8c862ec837c0fcd439abc4e330ea71eded4  3050 B MATCH
journal.md              ef90e7863ceae4ad908fa2e3f67c7f259ceed8f7 11202 B MATCH
verify_dict_sign_127.py 19af147f499c1ea19fc2f8a96da4b37b88998ea9  9814 B MATCH = r1 pin -> r1 results INHERIT (repro pass R2: 30/30 byte-identical; NOT re-run)
verify_anchors_127.py   574b460be50269c730af7323e5f0d4de7c685a0c  1891 B MATCH = r1 pin -> r1 results INHERIT (repro pass R3: 7/7 live bytes; NOT re-run)
make_payload_127.r2.py  9a32332e0eff6e8f9d96b89337e46e0555aef192  3483 B hashed; NOTE: this hash is NOT recorded inside journal.md (R2-REVISION block names the generator but pins only its inputs/outputs); generator is not an ACCEPTed object; my N2-1 reproduces the transform independently from review-r1.md strings, so no pin exposure.
appH (live)             123108d4a94723be1dbad752883125baac940fe4 880023 B MATCH baseline
ch03 (live)             78afd166ccdcde9eed21651b8799effbc743149a 36967 B MATCH pin 78afd166ccdc (wc -c 36967; final bytes "...here." no trailing newline, pre-existing)
scan-checklist-passA.txt 1360d9db54d7 / passB.txt 521338cc148b: 3(c) full scan completed for this package at the baseline above (inherited; re-hashed at r1 verdict pass).
Split-pass journals inherited (NOT re-run, NOT claimed as mine): out-gk127-math-notes.md (math, 20/20 own-sympy), out-gk127-repro-notes.md (repro+cert r1: 30/30 + 7/7 byte-identical, teeth fired, r1 cert tree gk127r_cert_a, PDF 065770405580/3298982). The r2 revision touches only payload prose in the two pinned spans; no mathematics changed -> math verdict inherits.
HASH GATE: PASS (all pins match).

== N2-1 BYTE DIFF P1-r2 vs P1 AND P2-r2 vs P2 (script gk127r2_t1.py, python -I, exit 0) ==
Method: the four replacement strings were extracted FROM review-r1.md BYTES by regex
(marker lines 'old string (must occur exactly once):' / 'new string:', 2-space-indented
payload lines), never transcribed: R1_OLD 139 B, R1_NEW 278 B, R2_OLD 35 B, R2_NEW 42 B
(CR stripped from captures; a first-pass regex that captured the CR is the script-history
note, corrected before any verdict-relevant run).
R1/P1: count(R1_OLD in payload-P1.txt) == 1; mechanical replace reproduces payload-P1-r2.txt
BYTE-IDENTICAL (hash pin 6dd693e2cf0b/1010 verified inside the check); reverse replace
(count(R1_NEW in r2) == 1) reproduces the r1 bytes exactly -> the ONLY difference is the
pinned span; raw diff region r1[287:400] -> r2[287:539], delta +139 B, single contiguous
region equal to the pinned span minus its own shared affixes.
R2/P2: count(R2_OLD) == 1; forward build == payload-P2-r2.txt byte-identical (pin
73aca8c862ec/3050); reverse == r1 bytes; diff region r1[2526:2526] -> r2[2526:2533], +7 B,
single contiguous insertion.
r1 files UNCHANGED (P1 8df7a7f42a97/871, P2 e30a1cd68ed6/3043 re-hashed inside the script).
r2 hygiene: ASCII, CR count 0, trailing LF present, LF line counts 1 (P1-r2) and 2 (P2-r2).
TASK1: PASS.

== N2-2 CURE CHECK AGAINST THE MANUSCRIPT (protocol 5 re-verification of my r1 F2 findings) ==
Live reads this task: ch03 L172-205 (def:matrix-coords-ext in full), L355-365 (ass:dictionary
anchor neighborhood), appH L4020-4030 (anchor head + tail of the 124 realization paragraph),
payload-P1-r2.txt and payload-P2-r2.txt in full.
R1 CURED: def:matrix-coords-ext live text defines "the induced tensor g_{alpha beta}" and
"the operator tensor K^{mu nu}=theta^{alpha mu} g_{alpha beta} theta^{beta nu}, which is the
kinetic tensor of a fluctuation" - it displays the INDUCED tensor, never g^(0). Revised P1 now
reads "...to the background-form K^(0)-sandwich of the kinetic tensor of
Definition~\ref{def:matrix-coords-ext} (the induced tensor g_{alpha beta} of the definition
replaced by g^(0)_{alpha beta}), which is congruent to g^(0)_{mu nu}...". The attribution no
longer claims the definition displays the g^(0)-form; it names the definition's own phrase
("kinetic tensor", "induced tensor") and states the replacement explicitly. Accurate.
P1 still inserts after the anchor sentence "...not an established result." (live L361, kept
verbatim) and before the LUV sentence (live L362, kept verbatim), same assumption environment.
R2 CURED: escape clause now "costs: complex (anti-)self-dual \(\Theta\)". Internally
consistent with the same paragraph's body "(ii) ... over the complex numbers the equation for
g^(0)=eta is solved exactly by the (anti-)self-dual class" and with the inherited math-pass
exact solution set (c = +/- i u). "(anti-)self-dual" is manuscript-conformant usage (appH F-
section and F-adjacent paragraphs, e.g. L338 "self-dual or anti-self-dual", L342 self-dual/
anti-self-dual parts). AppH context read for the wording.
F1-note / F3-note remain proposal-prose-only: counts in BOTH r2 payload files - "exhaustive" 0,
"t^2" 0, "charact" 0. (r1 findings F1, F3 stay non-blocking; no payload revision needed or made.)
Rule 3 discipline in r2 bytes: "Status" 0, "priority"/"Priority" 0, "completion" 0,
"closed"/"closes"/"solve"/"RESOLVED" 0; P2-r2 retains "(not closure)" (head), "Problems~A
and~N remain open", "none of this derives the datum", "no status label changes"; "D1" 0,
"Problem~G" 0; the sole Problem-D/F mentions are "the recorded Problem-D and Problem-F
consumption" (overturn-cost clause), asserting nothing about D/D1/G status. Nothing in the r2
bytes changes any status, priority or completion label; nothing closes D, D1, A, N or G.
AppH insertion context: anchor head unique at live L4027; preceding live paragraph (124
realization) pins "the kinetic-sign content of Assumption~\ref{ass:dictionary}" as a recorded
input and closes "they close nothing in Problem~N" - P2-r2's "kinetic-sign input of the
sublemma hypotheses recorded above" and "the Presentation-B realization above consumes no
transfer and is unaffected" point at exactly that record. Context intact at live bytes.
Label spot-check (this task): eq:dictionary 1x (ch03); ass:lorentzian, eq:Smatrix, eq:Smicro,
eq:NC, eq:g-from-e, app:status, ass:dictionary, def:matrix-coords-ext - 8 pattern hits over
appH/ch03/ch04, each defined (uniqueness of the full label set inherited from math pass label
hygiene; compile-time 0-undefined re-checked by the fresh cert, N2-4).
N2-2: PASS (R1 cured, R2 cured, F1/F3 notes unaffected, no label/closure violation).

== N2-3 POST RECOMPUTE, INDEPENDENT (script gk127r2_t3.py, python -I, exit 0) ==
External copies of LIVE bytes (re-hashed first: ch03 78afd166ccdc/36967, appH
123108d4a947/880023 - MATCH). Canonical recipe data.replace(anchor, payload_crlf+anchor, 1),
payload_crlf = raw LF -> CRLF (adds 1 B/line; r2 pc1 1011 B, pc2 3052 B).
Anchor uniqueness at live bytes: ch03 LUV line ('  \(\LUV\) remains the cutoff of the
derivative expansion.' + CRLF) 1x; declared ch03 anchor sentence 1x; appH head
'\paragraph{The named completion class and the remainder bound.}' 1x.
RECIPE SELF-TEST: applying the recipe to the frozen r1 payloads reproduces the inherited r1
POST files byte-identically (ch03 sha1_12 9031f6cf469c, appH 639e0fce81a2 - both MATCH the
repro pass R4/R5 pins), so my anchor/layout choice equals the inherited splice layout: the
payload line sits between the anchor sentence line and the LUV line (ch03) and immediately
before the head line with the preceding blank line kept (appH).
r2 POST (independently computed from live bytes):
  ch03: 37,978 B / 917 lines, sha1_12 9b1de0928d53  -> PIN 37,978/917 PASS
  appH: 883,075 B / 4,146 lines, sha1_12 6839a5cab30e -> PIN 883,075/4,146 PASS
Checks per POST: pure insertion (delete inserted block reproduces PRE exactly); payload
CRLF block present exactly once; pure CRLF (LF count == CRLF count); join asserts pass.
POST files written to %TEMP%\gk127r2_post\{ch03-spliced.tex,appH-spliced.tex} for the cert.
Note: ch03 PRE line count 916 (final line unterminated, pre-existing), POST 917 = PRE+1.
N2-3: PASS (no divergence; proceed to cert).

== N2-4 FRESH ITEM-108 CERTIFICATE OF THE r2 SPLICES ==
Tree: %TEMP%\gk127r2_cert_a (NEW; gk127r_cert_a untouched; nothing deleted). Staged from the
CURRENT working tree: namcg-book7.tex (hash MATCHES working tree), namcg-book7.bbl, bib/,
figs/, chapters/ (*.tex; no .aux staged), frontmatter/ (*.tex; no .aux). Staged spliced files
re-hashed equal to N2-3 POSTs: ch03 9b1de0928d53, appH 6839a5cab30e.
pdflatex -interaction=nonstopmode -halt-on-error namcg-book7.tex x2 from tree root:
pass1 exit 0 (444 pp), pass2 exit 0 (450 pp).
Log scans: '^!' count 0 in pass1.stdout, pass2.stdout and namcg-book7.log. Final (pass-2) log:
'undefined' (case-insensitive, refs AND citations) 0, 'multiply' 0. No first-pass aux noise in
final log.
pdftotext probes (whitespace-flattened, probe.txt 1,115,154 B):
  P1 phrases x1 EXACTLY: 'sharpens to a no-go'; 'independent datum of the dictionary';
    r2-SPAN 'the kinetic tensor of Definition'; r2-SPAN 'of the definition replaced by'.
  P2 phrases x1 EXACTLY: 'Kinetic-sign content of Assumption';
    'a datum, free in sign for every class member'; r2-SPAN 'with costs: complex';
    r2-SPAN 'complex (anti-)self-dual'; 'self-dual class' (body clause of same paragraph) x1.
  Negatives: OLD R1 misattributed clause regex 'of Definition <num> , which is congruent' x0
    (rendered form now 'Definition 3.4 (the induced tensor ...', comma form absent);
    OLD P2 list wording 'complex self-dual' x0 AT ITS LOCATION and document-wide (substring
    'self-dual' x61 legitimately: F-section and adjacent paragraphs; '(anti-)self-dual' x4
    including the two P2 occurrences); nonsense control 'ZZQQXNONSENSESTRINGZZQQX' x0;
    '??' x0.
Junction reads (PDF text): P1 '...not an established result. Within the quadratic transfer
class...' same paragraph, new attribution clause renders '...to the background-form K = Theta
g(0) Theta of the kinetic tensor of Definition 3.4 (the induced tensor g of the definition
replaced by g(0)), which is congruent to g(0)...'; P2 tail '...Escapes outside the class, with
costs: complex (anti-)self-dual (contradicts Equation (3.2) and the hermiticity of Definition
3.4)...' and typesets cleanly into '\paragraph' head 'The named completion class and the
remainder bound.' as a new paragraph - no merge defect. (pdftotext page-header artifact inside
a P1 sentence is a page-boundary extraction artifact, not a typeset defect.)
CERT: PASS. PDF sha1_12 b3f391aecbe7 (b3f391aecbe7cf9f43a1d6964fdf9d1158a3d1ae), 3,299,086 B,
450 pages. NOTE: differs from the r1 cert PDF (065770405580/3,298,982) by the R1/R2 text only
(+104 B text growth plausible at typeset size); r1 tree left intact per no-delete policy.
N2-4: PASS.

== N2-5 VERDICT + CLOSURE ==
Wrote review-r2.md: sha1_12 06e2c78be621, 11,512 B, 148 lines, ASCII, CRLF, line 1:
  Verdict: ACCEPT | MILESTONE: trigger-2 | FLAGS: F1-note;F3-note;hyg-LF;gen-hash-note | PROGRESS: improving | OPEN: 0/4
R1/R2 CURED (byte-exact mechanical reproduction from review-r1.md strings; single contiguous
diff regions; hygiene); F1/F3 notes proposal-prose-only confirmed; rule 3 clean; POST pins
independently recomputed and PASS (recipe self-test reproduced inherited r1 POST hashes);
fresh item-108 certificate PASS on tree gk127r2_cert_a (PDF b3f391aecbe7/3,299,086/450 pp).
r1 payload files re-hashed unchanged at close. Live chapters re-hashed at close: ch03
78afd166ccdc/36967, appH 123108d4a947/880023 - UNTOUCHED (this pass wrote only inside
proposals/127-n-dict-kinetic-sign/ and %TEMP%\{gk127r2_post,gk127r2_cert_a}; trees left in
place per no-delete policy).
STATUS: complete | TASKS DONE: N2-0..N2-5 | VERDICT: ACCEPT | MILESTONE reading: trigger-2
(with author-decision A-E / trigger-5 stop noted) | OPEN: 0 blocking / 4 nonblocking.
