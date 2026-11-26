import time
import hashlib

F = "C:/Users/redgi/Projects/namcg-lab@gpu/proposals/120-commutator-lift-bridge/"


def eol(path):
    d = open(path, "rb").read()
    return "\r\n" if b"\r\n" in d else "\n"


p5 = open(F + "insert-commutator-lift-r1.tex", "rb").read().decode("utf-8")
frags = [
    "no quadratic shift-invariant term exists",
    "the \\(X\\)-free shift-invariant sector is one-dimensional, spanned by "
    "\\(W_1=\\operatorname{Tr}([\\Phi,\\Phi^\\dagger])^2\\)",
    "so this lone quartic locks nothing",
]
offs = [p5.find(f) for f in frags]
names = ["payload", "gen", "cert", "verify_r120", "preR4"]
files = ["insert-commutator-lift-r1.tex", "gen_payload_120.py", "cert-r120p.py",
         "verify_r120.py", "verify_r120-preR4.py"]
pins = []
for n, f in zip(names, files):
    b = open(F + f, "rb").read()
    pins.append("%s %s/%d" % (n, hashlib.sha1(b).hexdigest()[:12], len(b)))
pinstr = "; ".join(pins)

R4 = [
    "",
    "## R4 (triage, 2026-11-23)",
    "",
    "Root-cause triage of the 4 fails in out-r120-rerun1.txt (49/53). Probes: probe_r4_triage.py",
    "(modes fast/heavy) and probe_r4_triage2.py (modes p1/heavy2); captures probe-r4-fast.txt,",
    "probe-r4-heavy.txt (right-nullspace, superseded) and probe-r4-heavy2.txt. Three shared",
    "check-side defects fixed via patch_r4_verify.py: (a) nulltest() used the RIGHT nullspace",
    "(monomial space) instead of the LEFT nullspace Mx.T (family-combination space), so the old",
    "T6f pass was vacuous; (b) SH shifted all four entries (Phi -> Phi + s*J_all-ones) instead of",
    "the shift of the claim, Phi -> Phi + s*I (diagonal only; matches the passing T6e and the",
    "frame mode phi_0*I); (c) the W1 word was miswritten as 2w4 - w3 - w2 - cJ(w2); the identity",
    "W1 = Tr(C^dag C) = 2 Tr(P Pd P Pd) - 2 Tr(P^2 Pd^2) with C = [Phi,Phi^dag] was verified",
    "numerically (P0, 5 matrices) and symbolically (P2: to_ri(2w4-2w3) - W2 == 0).",
    "",
    "T6f (was PASS vacuously; re-scoped). True statement now checked: the quadratic",
    "shift-invariant subspace of the 6-dim conjugation-invariant family is EXACTLY 3-dimensional,",
    "spanned by 2TrX - TrPhi TrPhidag, 2Re TrPhi^2 - Re(TrPhi)^2, 2Im TrPhi^2 - Im(TrPhi)^2 (the",
    "invariants of the traceless part Phi~ = Phi - (TrPhi/2) I; heavy2 left-null dim 3, basis",
    "matches), and the Tr X direction alone is shift-variant. Capture: probe-r4-heavy2.txt.",
    "",
    "T6g (FAIL; check-side bugs a,b,c plus GENUINE payload finding). With a,b,c fixed, heavy2",
    "gives the shift-invariant subspace of the 16-element QUAR family at n=2 EXACTLY",
    "4-dimensional (W1 direction w4 - w3 plus three further traceless-part invariants), not",
    "1-dimensional; expected value set to truth (dim 4 + W1 direction in span).",
    "",
    "T6h (FAIL; check-side). Corrected word identity per (c): expectation to_ri(2w4 - 2w3) == W2",
    "verified True symbolically (probe-r4-fast.txt P2); old form False (P0/P2).",
    "",
    "T7c (FAIL; check-side). The old code applied U2g = [[al,be],[-conj(be),conj(al)]] WITHOUT",
    "imposing U^dag U = I (U^dag U = (|al|^2+|be|^2) I), so preservation failed for generic",
    "al,be (P1: nonzero). Truth checked instead, exactly: general U(2) via real parameters",
    "a1..a4 gives (U2 Phi)^dag (U2 Phi) = norm * Phi^dag Phi (P1' identity True), so the",
    "normalized U preserves X; teeth: the unscaled matrix does not preserve X when norm != 1",
    "(P1 second line True).",
    "",
    "## R4 findings - GENUINE: payload paragraph 5 false as stated (payload bytes unchanged this",
    "round: insert-commutator-lift-r1.tex 343226e27ebf/5138 kept intact). Affected fragments",
    "(utf-8 byte offsets in payload file):",
]
for o, f in zip(offs, frags):
    R4.append("[%d] %s" % (o, f))
R4 += [
    "Both statements are false under the established shift notion Phi -> Phi + s I: quadratic",
    "shift-invariant conjugation-invariants DO exist (the three traceless-part invariants above)",
    "and the quartic shift-invariant sector of the checked family is 4-dim, not spanned by W1",
    "alone. Minimal corrected wording for the supersession dispatch:",
    "(A) 'no quadratic shift-invariant term exists' -> 'no shift-invariant term is a function of",
    "X at quadratic order, X itself being shift-variant'; (B) 'at quartic order the X-free",
    "shift-invariant sector is one-dimensional, spanned by W1 = Tr([Phi,Phi^dag])^2 (checked at",
    "matrix sizes 2,3 over the conjugation-invariant families)' -> 'at quartic order the",
    "shift-invariant sector of the checked conjugation-invariant family is four-dimensional,",
    "spanned by W1 = Tr([Phi,Phi^dag])^2 and three invariants of the traceless part",
    "Phi~ = Phi - (TrPhi/2) I (checked at matrix size 2)' - the verifier MARK string",
    "W_1=\\operatorname{Tr}([\\Phi,\\Phi^\\dagger])^2 is preserved; (C) 'so this lone quartic locks",
    "nothing' -> 'so this quartic locks nothing'. The paragraph-6 W(X)-channel argument uses only",
    "W1 not-a-function-of-X (T7, PASS) and is unaffected. Pins after R4: " + pinstr,
    "",
]
with open(F + "verify_repair_log.txt", "a", encoding="utf-8", newline="") as log:
    log.write(eol(F + "verify_repair_log.txt").join(R4))

PB = [
    "",
    "## Triage r1 (49/53) - 2026-11-23, R4",
    "- T6f: check-side vacuous pass (right-nullspace + all-entries shift map); truth: quadratic shift-invariant subspace = 3-dim traceless-part span, Tr X direction shift-variant; re-scoped (probe-r4-heavy2.txt).",
    "- T6g: check-side bugs (transpose, shift map, W1 word) PLUS genuine payload defect: quartic shift-invariant sector of the n=2 family is 4-dim (W1 direction + 3 traceless-part invariants), not 1-dim spanned by W1 (probe-r4-heavy2.txt).",
    "- T6h: check-side wrong word identity; true identity W1 = 2Tr(P Pd P Pd) - 2Tr(P^2 Pd^2) = Tr(C^dag C), verified symbolically and numerically (probe-r4-fast.txt P0/P2).",
    "- T7c: check-side missing unitarity normalization (U^dag U = (|al|^2+|be|^2)I); true statement (U2 Phi)^dag(U2 Phi) = norm Phi^dag Phi verified exactly with real-parameter U(2) plus non-normalized teeth (probe-r4-fast.txt P1; p1 run True).",
    "",
]
with open(F + "pr1_partB.md", "a", encoding="utf-8", newline="") as pb:
    pb.write(eol(F + "pr1_partB.md").join(PB))

ST = [
    "GENUINE-FIX-REQUIRED: T6f,T6g (payload paragraph 5 false as stated: quadratic-term claim and 1-dim sector claim; see verify_repair_log.txt R4 findings for minimal corrected wording + byte offsets)",
    "R4 check-side patches applied: verify_r120.py 4d751ac4afb8/39745 (preR4 copy verify_r120-preR4.py 6d72f26fbfd7/37603); payload untouched 343226e27ebf/5138",
    "rerun2 launched " + time.strftime("%Y-%m-%d %H:%M") +
    " (background bado20en1); expected next step: orchestrator assembles when out-r120-rerun2.txt ends with TOTAL x/x PASS + ALL CHECKS DONE 120 + RC=0, after payload paragraph-5 supersession per R4 findings",
]
with open(F + "STATUS120.txt", "w", encoding="utf-8", newline="") as s:
    s.write("\r\n".join(ST) + "\r\n")
print("offsets:", offs)
print(pinstr)
print("DONE writes")
