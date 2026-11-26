GK127 REPRO+CERT PASS JOURNAL (pass 2/3)
================================================

== R1 HASH GATE ==
verify_dict_sign_127.py 19af147f499c1ea19fc2f8a96da4b37b88998ea9 9814 B MATCH
verify_anchors_127.py   574b460be50269c730af7323e5f0d4de7c685a0c 1891 B MATCH
payload-P1.txt          8df7a7f42a971892dec26c4e80ad9d18884b1786 871 B MATCH
payload-P2.txt          e30a1cd68ed607c1d6f51782039464697225b2e3 3043 B MATCH
proposal-r1.md          4f6853dbb5385010deba82ef58b243f10f559d7c 33885 B MATCH
appH baseline           123108d4a94723be1dbad752883125baac940fe4 880023 B MATCH (live file)
NOTE: script compare line printed spurious MISMATCH for appH (12-char prefix vs full-sha1 expected string); full sha1 and size verified equal.
HASH GATE: PASS - all 6 match.

== R1 CLAIMED (from proposal-r1.md L285-347, targeted read) ==
P1 anchor (ch03-matrix-action.tex, ass:dictionary, unique A1): sentence ending
  "...this is a matching condition, not an established result." (live L361);
  insert immediately after, same paragraph. CLAIMED: payload = ONE new source
  line, 871 B, ASCII, no CR; POST = PRE + 1 lines; inserted region grows by
  exactly the payload bytes after the integrator CRLF conversion.
P2 anchor (appH, unique A3): head line \paragraph{The named completion class
  and the remainder bound.} (live L4027); insert immediately before it, after
  the preceding blank line. CLAIMED: payload = TWO new source lines, 3043 B,
  ASCII, no CR; POST = PRE + 2 lines; same byte-growth claim.
verify_dict_sign_127.py CLAIMED 30 checks all PASS (capture-verify-r1.txt).
verify_anchors_127.py CLAIMED 7 checks all PASS (capture-anchors-r1.txt).
Proposals says no compile certificate shipped; integrator certificate required.
Payload files inspected (gatekeeper): P1 871 B last4=7d292e0a CR=0 LF=1;
P2 3043 B last4=74292e0a CR=0 LF=2. Both end bare LF (no CR).
NOTE: CLAIMED byte-growth wording is loose: LF->CRLF conversion adds 1 B per
line (P1 +1, P2 +2); to be recomputed independently in R4.
== R2 VERIFY_DICT_SIGN_127 ==
Capture files hash-gated first: capture-verify-r1.txt 1901293f1aa3 1709 B MATCH;
capture-anchors-r1.txt b6791076b165 379 B MATCH.
Copied verify_dict_sign_127.py to Temp/gk127r_ext/v127.py, ran python -I, exit 0.
Full output captured to scratch/gk127r_verify127.txt: sha1_12 1901293f1aa3,
1709 B - BYTE-IDENTICAL to capture-verify-r1.txt (diff 0 lines). 30 PASS / 0 FAIL.
TEETH: mutated copy v127_mut.py, single change K = -TH^T eta TH (sign flip in
core K construction, line 27). Run exit 1; 5 checks FAIL: S1c, S2a, S2c, S5a,
S5b; summary line 'FAILURES: 5 of 30'. Core guards fire on broken math.
TEETH: FIRED. Proposal copy untouched (mutation ran only on external copy).
== R3 VERIFY_ANCHORS_127 ==
Script ROOT is relative '../../chapters/' resolved from CWD; built external tree
Temp/gk127r_anch2 with chapters/ = byte-copies of CURRENT live bytes
(ch03 sha1_12 78afd166ccdc 36967 B; appH sha1_12 123108d4a947 880023 B,
live appH re-hash MATCHES baseline). Live==copy verified for both.
Run python -I from gk127r_anch2/a/b: exit 0, 7/7 PASS (A1-A7), output
sha1_12 b6791076b165 379 B - BYTE-IDENTICAL to capture-anchors-r1.txt.
TEETH: defaced ch03 copy (anchor sentence replaced by ZZZ) in the same tree:
A1 FAILs, exit 1 -> script really reads file bytes; anchors checked against
current bytes, not baked-in counts. Copy restored equal to live afterwards.
NOTE: gk127r_anch (first attempt, bad relative depth) left in place, unused.
== R4 INDEPENDENT POST ACCOUNTING ==
Payloads verbatim-in-proposal: P1 x1, P2 x1 (as claimed).
Raw payload newlines: P1 871 B last4 7d292e0a, 1 LF, 0 CR; P2 3043 B last4
74292e0a, 2 LF, 0 CR. HYGIENE FLAG: raw payload files are bare-LF (no CR).
Proposals assigns CRLF conversion to the integrator. Bare LF in spliced .tex
would survive pdflatex and would NOT trip git diff --check whitespace rules,
but violates the repo CRLF convention; with the declared CRLF conversion the
spliced files are PURE CRLF (verified: LF count == CRLF count in both POSTs).
Canonical recipe replace(anchor, payload+anchor, 1), payload LF->CRLF converted
(pc1 872 B, pc2 3045 B, both end CRLF; anchor blank line outside replacement):
P1 ch03 anchor line (L361, 75 B incl CRLF, unique). PRE 36967 B / 916 lines
(splitlines; final line has NO terminator, 915 CRLF). POST 37839 B
(added 872 = 871+1 CR), 917 lines = PRE+1. CLAIMED lines PASS; CLAIMED byte
wording 'grows by exactly the payload bytes' is off by the per-line CR
(+872/+3045 actual). P1 join verified: payload sits between anchor line and
'  \(\LUV\) remains the cutoff' - same paragraph, proposal text order kept.
P2 appH head line unique. PRE 880023 B / 4144 lines. POST 883068 B
(added 3045 = 3043+2 CR), 4146 lines = PRE+2. PASS. Join: blank line before
payload preserved; payload last line directly followed by head line (no blank
between payload and \paragraph head) - matches declared 'immediately before'.
POST files: gk127r_post/ch03-spliced.tex sha1_12 9031f6cf469c;
gk127r_post/appH-spliced.tex sha1_12 639e0fce81a2; both PURE CRLF.
Live files clean: ch03 and appH have zero bare LF, zero lone CR.
POST: P1 PASS, P2 PASS (lines per CLAIMED; byte deltas recomputed above).
== R5 COMPILE CERTIFICATE (item-108 rule) ==
Tree: Temp/gk127r_cert_a (new; single tree). Staged from CURRENT working tree:
namcg-book7.tex, namcg-book7.bbl (built bibliography, needed by 2-pass build),
bib/, figs/, chapters/ (full), frontmatter/ *.tex (needed by \include). No .aux
staged. R4 spliced files copied over staged ch03/appH; staged hashes re-verified
(9031f6cf469c / 639e0fce81a2 MATCH R4 POSTs).
pdflatex -interaction=nonstopmode -halt-on-error x2 from tree root:
pass1 exit 0 (444 pp), pass2 exit 0 (450 pp).
Scans: ^! lines 0 in pass1.stdout, pass2.stdout, namcg-book7.log.
Pass-2 log (final): 0 undefined (case-insens: refs AND citations), 0 multiply.
pass1.stdout carries 1634 first-pass undefined warnings - expected (no aux on
first pass), fully cleared by pass 2. Citation-undefined: 0 in final log.
pdftotext probes (whitespace-flattened, 1,071,967 B): P1 phrases 'sharpens to a
no-go', 'independent datum of the dictionary', 'Within the quadratic transfer
class' each EXACTLY 1; P2 phrases 'Kinetic-sign content of Assumption',
'a datum, free in sign for every class member', 're-datuming whose sign content'
each EXACTLY 1 (live-source grep: each 0 outside payloads; uppercase-K form
checked case-sensitively against lowercase live occurrence). Absent-string
control 'ZZQQXNONSENSESTRINGZZQQX': 0 -> pipeline distinguishes present/absent.
Defect probes: '??' 0; 'LaTeX Error' 0.
Junction reads (PDF text): P1 '...not an established result. Within the
quadratic transfer class...' same paragraph, before \LUV sentence, as declared;
P2 payload ends and run-in head 'The named completion class and the remainder
bound.' typesets correctly as new paragraph immediately after - no merge defect
from the blank-line-free join.
CERT: PASS. pdf sha1_12 065770405580, 3298982 B, 450 pages. Pass exits 0/0.

== R6 CLOSURE ==
REPRO-PASS STATUS: complete | TASKS DONE: R1,R2,R3,R4,R5 | VERIFY127: 30/30,
matches capture yes (byte-identical, sha1_12 1901293f1aa3) | VERIFYANCHORS:
7/7, live-bytes yes (run against hash-verified live-byte copies; defaced-copy
teeth FAILed A1) | TEETH: fired (K sign flip -> 5 core checks FAIL, exit 1;
anchors deface -> A1 FAIL) | POST: P1 pass, P2 pass (+872 B/+1 line; +3045 B/
+2 lines; POST 37839/917 and 883068/4146) | EOL: bare-LF flag (raw payload
files 0 CR; spliced POSTs pure CRLF after declared integrator conversion) |
CERT: PASS gk127r_cert_a, pdf sha1_12 065770405580 / 3298982 B, pass exits 0/0 |
FLAGS: (1) raw payloads bare-LF - integrator must CRLF-convert (proposal
assigns this; without it spliced .tex has bare LF: survives pdflatex and
git diff --check but breaks CRLF convention); (2) proposal byte-growth wording
'exactly the payload bytes' off by per-line CR (actual +872/+3045); line-count
claims exact; (3) live ch03 last line has no terminator (pre-existing, splice
mid-file, unaffected); (4) Temp/gk127r_anch first-attempt tree left unused
(no-delete policy); (5) no status/label changes made or endorsed; verdict pass
follows separately.
