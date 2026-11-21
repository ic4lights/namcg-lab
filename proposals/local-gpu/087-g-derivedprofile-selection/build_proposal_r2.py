# Round-2 proposal driver: regenerates proposal-r2.md from proposal-r1.md by
# assert-guarded span replacement (F1-F4 register, provenance fixes, r2 byte
# contract). Deterministic: refuses to write unless proposal-r1.md sha8 and
# review-r1.md sha8 match the round-2 pins and every anchor count is 1.
import hashlib, sys
sys.stdout.reconfigure(errors="replace")
D = "proposals/087-g-derivedprofile-selection/"
NL = chr(10)
BS = chr(92)
Q = chr(34)
LAMEQ = BS + "(lambda^{+}" + BS + ")"
SIGP = BS + "(Sigma_{" + BS + "pi}" + BS + ")"
src = open(D + "proposal-r1.md", "rb").read()
rev = open(D + "review-r1.md", "rb").read()
assert len(src) == 28875 and hashlib.sha256(src).hexdigest()[:8] == "2ae709c0"
assert len(rev) == 17057 and hashlib.sha256(rev).hexdigest()[:8] == "3a5d4486"
buf = src.decode("utf-8")

def rep(old, new, tag):
    global buf
    assert buf.count(old) == 1, (tag, buf.count(old))
    buf = buf.replace(old, new, 1)

def span(a1, a2, new, tag):
    global buf
    assert buf.count(a1) == 1 and buf.count(a2) == 1, tag
    i, j = buf.find(a1), buf.find(a2)
    assert 0 <= i < j
    buf = buf[:i] + new + buf[j + len(a2):]

# 1. title
rep("# Proposal 087-g-derivedprofile-selection, round 1",
    "# Proposal 087-g-derivedprofile-selection, round 2", "title")
# 2. Result (iv) corrected definition (F1)
span("(iv) a stiffness tie", "**without moving the locus**.",
     "(iv) a stiffness tie `E_pi Gamma >= lam+ W^2 (1/D_eff - 1/D)` with `lam+`" + NL +
     "the least eigenvalue of `Sigma_pi` on profiles of mean zero - the least" + NL +
     "nonzero eigenvalue exactly when the coincidence graph is connected, and" + NL +
     "strictly positive exactly in the connected case - and mixtures" + NL +
     "`((1-eps) delta_{e1} + eps Haar)` degenerate the stiffness" + NL +
     "(`lam+ = eps/(D+1)`) **without moving the locus**.", "result-iv")
# 3. S1 phase provenance (F2)
rep("(200 exact rational cases checked).",
    "(200 exact rational cases checked; the phase-independence of Gamma is" + NL +
    "structural - Gamma involves u only through the weights q_i = ||u_i||^2 -" + NL +
    "and the explicit complex-frame phase check (100 exact complex frames with" + NL +
    "genuine phases) was performed independently by the gatekeeper in" + NL +
    "review-r1, not by the shipped s1 script, whose header comment claiming" + NL +
    "that check was corrected in round 2 with stdout re-verified unchanged).",
    "s1-prov")
# 4. S2 bounds provenance (F2)
span("Var_q(g) <= ||g - c 1||^2 / 2 for any constant c, 4000 random",
     "attained at half-half weights.",
     "Var_q(g) <= ||g - c 1||^2 / 2 for any constant c (provenance: 4000" + NL +
     "random cases checked in floating point at 1e-12 tolerance - not exact" + NL +
     "rational checks; the bounds themselves are derivations: Popoviciu for" + NL +
     "the first, and for the second a^2 + b^2 >= (a-b)^2/2 with c = gbar, the" + NL +
     "constant 1/2 sharp at D = 2 with half-half weights), worst sampled" + NL +
     "ratio 1/2.", "s2-prov")
# 5. Round 2 corrections register (before Target and status)
R2 = (
 "## Round 2 corrections" + NL + NL +
 "Review-r1 verdict: ACCEPT WITH REQUIRED REVISIONS (review-r1.md 17,057 B" + NL +
 "/ sha8 3a5d4486). Findings mapped to exact round-2 actions (all round-2" + NL +
 "artifacts live in this folder; r1 files kept unmodified as audit trail" + NL +
 "except the two comment-only script fixes noted below):" + NL + NL +
 "- F1 (blocking; stiffness tie false as written for disconnected" + NL +
 "  coincidence graphs). (i) build_insert_r2.py, a byte-surgery copy of" + NL +
 "  build_insert_087.py, replaces the defective clause (at byte offset 2244" + NL +
 "  of the script source) with the gatekeeper-corrected clause and changes" + NL +
 "  the output filename span only (round-trip asserts prove the two spans" + NL +
 "  are the whole diff; 5,460 to 5,558 B / sha8 8f25bc1c). It regenerates" + NL +
 "  insert-r2.tex, 5,378 B / sha256" + NL +
 "  5e692fbca8984cd552047b38ba52a35df63409f4df4333795ffbbe4af31fc3a6" + NL +
 "  (sha8 5e692fbc): vs insert-r1.tex (5,280 / 3fc233c9, kept unmodified" + NL +
 "  and superseded) the diff is a single changed span - common prefix" + NL +
 "  2,233 B, common suffix 3,008 B, 39 B of r1 replaced by 137 B (+98 B)." + NL +
 "  Clause text: " + Q + "where " + LAMEQ + " is the least eigenvalue of" + NL +
 "  " + SIGP + " on profiles of mean zero, the least nonzero eigenvalue" + NL +
 "  exactly when the coincidence graph is connected and strictly positive" + NL +
 "  exactly in the connected case," + Q + ". (ii) Result item (iv) above" + NL +
 "  corrected to the same definition. (iii) s4_selection_content.py header" + NL +
 "  comment fixed in place (assert-guarded byte surgery, 4,456 to 4,555 B /" + NL +
 "  sha8 d0981d8e); stdout re-run byte-identical to the shipped .out" + NL +
 "  (53fcf550), so the .out stays valid. Hygiene re-run on the new insert" + NL +
 "  bytes (hygiene_087_r2.py): overall PASS, numeral set identical to r1" + NL +
 "  (the clause adds no numerals)." + NL +
 "- F2 (minor; provenance). S2 below now states the s2.4 bounds are" + NL +
 "  floating-point checks at 1e-12 tolerance with the true derivation" + NL +
 "  stated; S1 below now records that the phase-independence is structural" + NL +
 "  (Gamma involves u only through q) and that the explicit complex-frame" + NL +
 "  check with 100 exact complex frames is the independent gatekeeper" + NL +
 "  re-derivation in review-r1, not shipped s1 code; the s1_variance_graph.py" + NL +
 "  comment making the overclaim was fixed in place (assert-guarded byte" + NL +
 "  surgery, 5,769 to 5,854 B / sha8 92f019ae), stdout re-run byte-identical" + NL +
 "  to the shipped .out (dba73a0c)." + NL +
 "- F3 (minor; forward-pin hazard; no insert-text action). Recorded in the" + NL +
 "  BYTE CONTRACT below and in Special instructions: post-integration the" + NL +
 "  full 085-closer PIN counts 2; every future chain-2 anchor must re-pin to" + NL +
 "  the 087 closer unique tail " + Q + "they classify the locus over frame" + NL +
 "  laws rather than selecting the profile" + Q + ". Frontier-row note for" + NL +
 "  the integrator." + NL +
 "- F4 (minor; manifest self-hash staleness). No action on r1 artifacts;" + NL +
 "  manifest_r2.md carries no self-hash line." + NL + NL +
 "Round-2 source reading: review-r1.md read in full; targeted re-reads of" + NL +
 "every quoted span; appH windows L3026-3029, L3119-3130, L3173-3189" + NL +
 "re-checked against the live pinned bytes; live appH pins (739,096 B /" + NL +
 "sha256 31b345ed... / CRLF 3,836 / bareLF 0) re-verified before and after" + NL +
 "every run this round; digest not used. No other mathematical claim" + NL +
 "changed: all r1 derivations, scripts, closed forms, the exact example and" + NL +
 "all scoped disclaimers are carried forward unchanged (the gatekeeper" + NL +
 "independently re-derived them in full)." + NL + NL)
assert buf.count("## Target and status") == 1
buf = buf.replace("## Target and status", R2 + "## Target and status", 1)
# 6. Source reading r2 note
rep("review itself" + NL + "requested.",
    "review itself" + NL + "requested." + NL + NL +
    "Round-2 addendum (this round): review-r1.md read in full; targeted" + NL +
    "re-reads of every span quoted in the review; the three appH targeted" + NL +
    "windows re-checked against the live pinned bytes; live pins re-verified" + NL +
    "before and after every run; digest not used.", "sr-r2")
# 7. Anchor paragraph insert size
rep("(5,280 B, content + terminal CRLF, single content",
    "(5,378 B, content + terminal CRLF, single content", "anchor-size")
# 8. BYTE CONTRACT paragraph
span("BYTE CONTRACT (authoritative", "nil, build mandatory) and refresh the digest.",
     "BYTE CONTRACT (authoritative, round 2, from simulate_apply_087_r2.py" + NL +
     "re-run this round). PRE: 739,096 B / sha256" + NL +
     "31b345ed5e957910bacd3c02ebae87edfbeb5f0effa77c98149f6eafc2a2679d / CRLF" + NL +
     "3,836 / bareLF 0 (live, re-verified before and after every run this" + NL +
     "round). Insert: insert-r2.tex, 5,378 B / sha8 5e692fbc (full sha256" + NL +
     "5e692fbca8984cd552047b38ba52a35df63409f4df4333795ffbbe4af31fc3a6)," + NL +
     "regenerated byte-identically by build_insert_r2.py; single content line" + NL +
     "+ terminal CRLF; hygiene PASS (hygiene_087_r2.py). POST: **744,476 B /" + NL +
     "sha256 e7736a56230f80eff3c3325c519eda797d2f3b7a1a77c4f785451d51b79df75b" + NL +
     "/ CRLF 3,838 / bareLF 0 / close-idiom count 14 (was 13, +1) / new" + NL +
     "header " + Q + "Measure dependence of the frame-averaged decoupling" + NL +
     "locus" + Q + " count 1 / " + BS + "emph{Vacuum term.} count 2" + NL +
     "unchanged**; POST size = PRE + 5,378 + 2. Boundary invariants asserted" + NL +
     "by the script: PIN followed by CRLFCRLF (085 separation kept);" + NL +
     "CRLFCRLF immediately before the new header; the insert terminal CRLF" + NL +
     "followed by the appended CRLF before the Vacuum line. SUPERSEDED" + NL +
     "CONTRACTS - do not integrate against either: the round-1 contract POST" + NL +
     "744,378 / 38db6497... (valid only for the superseded insert-r1.tex" + NL +
     "bytes, void once the F1 clause fix is applied) and the shipped" + NL +
     "defective simulator POST 744,376 / d65eb64f (same-line splice defect)." + NL +
     "Forward-pin note (F3): after integration the full-085-closer PIN" + NL +
     "counts 2; re-anchor any later chain-2 edit to the 087 closer unique" + NL +
     "tail " + Q + "they classify the locus over frame laws rather than" + NL +
     "selecting the profile" + Q + ". After integration: run" + NL +
     "python scripts/build_check.py (insert adds no macros, no refs: build" + NL +
     "risk nil, build mandatory) and refresh the digest.", "bytecontract")
# 9. Verification intro sentence
rep("All six shipped scripts were re-run this" + NL + "round",
    "Every shipped script (round-1 set, with round-2 comment-only fixes to" + NL +
    "the s1/s4 .py files noted below, whose stdout re-ran byte-identical) was" + NL +
    "re-run this round", "verintro")
# 10. build_insert bullet
span("- build_insert_087.py - regenerates insert-r1.tex",
     "prints " + Q + "insert bytes 5280" + Q + ".",
     "- build_insert_r2.py - round-2 generator: byte-surgery copy of" + NL +
     "  build_insert_087.py with only the F1 clause span and the output" + NL +
     "  filename span changed (round-trip assert); regenerates insert-r2.tex" + NL +
     "  5,378 B / sha8 5e692fbc. Invariant: prints " + Q + "insert bytes" + NL +
     "  5378" + Q + ". The round-1 pair build_insert_087.py / insert-r1.tex" + NL +
     "  (5,280 / 3fc233c9) is kept unmodified as the superseded audit" + NL +
     "  artifact.", "build-bullet")
# 11. s1/s4 bullet notes
rep("Invariants: four " + Q + "OK" + Q + " lines + " + Q + "S1 DONE" + Q + ".",
    "Invariants: four " + Q + "OK" + Q + " lines + " + Q + "S1 DONE" + Q + "." + NL +
    "  Round-2 note: header comment fixed (phase provenance, review F2);" + NL +
    "  stdout re-verified byte-identical, .out valid.", "s1-bullet")
rep("Invariants: " + Q + "E_pi Gamma = 0 exactly" + Q + ", " + Q + "S4 DONE" + Q + ".",
    "Invariants: " + Q + "E_pi Gamma = 0 exactly" + Q + ", " + Q + "S4 DONE" + Q + "." + NL +
    "  Round-2 note: header comment lam+ definition fixed (review F1);" + NL +
    "  stdout re-verified byte-identical, .out valid.", "s4-bullet")
# 12. append r2 bullets after the fix bullet
rep("ends " + Q + "no write performed" + Q + ".",
    "ends " + Q + "no write performed" + Q + "." + NL +
    "- hygiene_087_r2.py / hygiene_087_r2.out - hygiene_087.py logic" + NL +
    "  pointed at insert-r2.tex: overall PASS, 5,378 B; numeral set" + NL +
    "  identical to r1." + NL +
    "- simulate_apply_087_r2.py / .out - round-2 authoritative splice (the" + NL +
    "  r1 fix script pointed at insert-r2.tex, the hardcoded 5,280 header" + NL +
    "  offset generalized to len(ins), header comment marked round 2;" + NL +
    "  assert-guarded copy): PRE pins, POST 744,476 / e7736a56... / CRLF" + NL +
    "  3,838 / bareLF 0 / close-idiom 14 / header 1 / Vacuum 2; three" + NL +
    "  boundary probes; ends " + Q + "no write performed" + Q + ". The r1" + NL +
    "  fix script and .out are kept unmodified (they encode the void" + NL +
    "  round-1 contract, audit trail).", "sim-bullet")
# 13. Decisions items 6-7
rep("specific to the 084 gaussian slot law.",
    "specific to the 084 gaussian slot law." + NL +
    "6. (Round 2, routine) Adopted the F1 clause form that redefines lam+" + NL +
    "   as the least eigenvalue of Sigma_pi on the mean-zero profile subspace" + NL +
    "   (inequality true for every pi) over the alternative of prepending" + NL +
    "   " + Q + "in the connected case," + Q + " and keeping the least-nonzero" + NL +
    "   definition: the chosen form keeps the single stated inequality valid" + NL +
    "   for every pi, which matches the surrounding text that discusses" + NL +
    "   disconnected measures in the same breath; the definition clause" + NL +
    "   records the equivalence in the connected case, so no information is" + NL +
    "   lost. Rejected: dropping the inequality (loses the quantitative tie" + NL +
    "   the block uses to separate stiffness from locus)." + NL +
    "7. (Round 2, routine) Applied the s4 and s1 comment fixes in place by" + NL +
    "   assert-guarded byte surgery with stdout re-verified byte-identical" + NL +
    "   against the shipped .out files, rather than registering notes only:" + NL +
    "   the round-trip asserts plus the byte-identical re-runs prove the" + NL +
    "   scripts are otherwise untouched, which is stronger provenance than" + NL +
    "   a note.", "decisions")
# 14. Special instructions item 2
span("2. Do NOT integrate against the shipped simulate_apply_087.py output",
     "after the pin with gap CRLFCRLF.",
     "2. Do NOT integrate against the shipped simulate_apply_087.py output" + NL +
     "   (POST 744,376 / d65eb64f: same-line splice defect) nor against the" + NL +
     "   round-1 contract (POST 744,378 / 38db6497...: valid only for the" + NL +
     "   superseded insert-r1.tex bytes, void after the F1 clause fix)." + NL +
     "   Integrate against simulate_apply_087_r2.py (POST 744,476 / sha256" + NL +
     "   e7736a56230f80eff3c3325c519eda797d2f3b7a1a77c4f785451d51b79df75b /" + NL +
     "   CRLF 3,838 / bareLF 0). Re-pin before splicing: if the tree moved," + NL +
     "   recompute; the full-085-closer tail pin must count 1" + NL +
     "   pre-integration (F3: post-integration it counts 2 - re-anchor to" + NL +
     "   the 087 closer unique tail), and the G-side Vacuum term must be the" + NL +
     "   next " + BS + "emph{Vacuum term.} after the pin with gap CRLFCRLF.",
     "spec-item2")
out = buf.encode("utf-8")
open(D + "proposal-r2.md", "wb").write(out)
print("proposal-r2.md", len(out), hashlib.sha256(out).hexdigest())
