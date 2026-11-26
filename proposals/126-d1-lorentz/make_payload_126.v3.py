# make_payload_126.v3.py -- round-2 payload for chain 126 (review-r1 ACCEPT WITH REQUIRED
# REVISIONS). Reads payload-126-v2.txt from disk (pin-asserted) and applies EXACTLY the six
# clause-level edits required by review-r1 Findings 1(i)-(iii), 2, 3, 4, 5, 6; no other bytes
# change. v2 bytes (b9ebeba71fe9/4447) and make_payload_126.v2.py (e996ca20baad/7417) are the
# preserved prior version and are never edited. Every hygiene/join guard carries an injected
# positive control (CTRL-FIRED lines); a CTRL-DEAD line is a hard failure.
# Recipe (same as v2, review-verified): spliced = live.replace(ANCHOR, ANCHOR + PAYLOAD + CRLF, 1),
# i.e. anchor sentence + CRLFCRLF, then payload + join CRLF. The canonical
# replace(anchor, payload+anchor) is the WRONG object (review-r1, Splice section).
# Run from the proposals folder: python -I make_payload_126.v3.py <repo-root>
import hashlib
import re
import sys

REPO = sys.argv[1] if len(sys.argv) > 1 else "."
APP = REPO + "/chapters/appH-microscopic-proofs.tex"
PIN = "76d862968c31d78fffc665f72aaf60d40c90367a"
V2PIN = "b9ebeba71fe933b1048dbcd2a0ec4f46d89c54dd"
ANCHOR = (b"supplied: this paragraph closes none of Problem~D, Problem~D1, or Problem~A."
          b"\r\n\r\n")
CLOSER = b"this paragraph closes none of Problem~D, Problem~D1, or Problem~A."
BADH3 = b"only the adjoint action needs to be a homomorphic image"
REFSET = {b"eq:Smatrix", b"ass:frame-lock", b"ass:nondeg"}

v2 = open("payload-126-v2.txt", "rb").read()
assert hashlib.sha1(v2).hexdigest() == V2PIN, "payload v2 pin drift"

REPL = [
    # Finding 1(i): insert the missing S=0 step (bracket retention + perfection)
    ("r1a", br"therefore vanishes identically, and the first relation then forces",
            br"therefore vanishes identically; because the \(\mathcal S\)-sector of the class"
            br" retains the \(\mathfrak{so}(3,1)\) bracket and \(\mathfrak{so}(3,1)\) is perfect,"
            br" this forces \(\mathcal S_{cd}=0\), and the first relation then forces"),
    # Finding 1(ii): qualify the conclusion by the bracket-retention premise
    ("r1b", br"realization of the two relations with anti-Hermitian \(\mathcal S\) is trivial",
            br"realization of the two class relations whose \(\mathcal S\)-sector retains the"
            br" \(\mathfrak{so}(3,1)\) bracket, with anti-Hermitian \(\mathcal S\), is trivial"),
    # Finding 1(iii): extend the hypothesis list clause
    ("r1c", br"Hypotheses: the two relations at face value with constant coefficients, finite \(N\),",
            br"Hypotheses: the two class relations at face value with constant coefficients and"
            br" with the \(\mathcal S\)-sector bracket retained, finite \(N\),"),
    # Finding 2: prose pointer to the standard lemma recorded under Problem E (no label exists)
    ("r2", br"a unitary realization requires \(N=\infty\), and non-unitary",
            br"a unitary realization requires \(N=\infty\) (the general statement recorded in"
            br" the conjugate-coordinate analysis under Problem~E; the application here is to"
            br" the \(\mathcal S\)-sector of the class), and non-unitary"),
    # Finding 3: grammar, delete "with"
    ("r3", br"of the class over with \(\mathcal A=\mathbb C\)",
            br"of the class over \(\mathcal A=\mathbb C\)"),
    # Finding 4: real centralizer in the real 5x5 model
    ("r4", br"\(\mathbb C\mathbb I\) plus",
            br"\(\mathbb R\mathbb I\) plus"),
    # Finding 5: variant closer, same scope, book variant formula (appH L1731)
    ("r5", br": this paragraph closes none of Problem~D, Problem~D1, or Problem~A.",
            br": nothing in this paragraph closes any of Problem~D, Problem~D1 or Problem~A."),
    # Finding 6: quantifier matching script B R4 (one rotation, one boost, t=1)
    ("r6", br"(rotation and boost generators, at \(t=1\), exact exponentials)",
            br"(for one rotation and one boost generator at \(t=1\), exact exponentials)"),
]

p = v2
for name, old, new in REPL:
    assert p.count(old) == 1, "old string not unique for " + name
    p = p.replace(old, new, 1)
for name, old, new in REPL:
    assert p.count(new) == 1, "new string not exactly once for " + name
    assert v2.count(new) == 0, "no-op replacement " + name
PAY = p
assert len(PAY) == len(v2) + sum(len(n) - len(o) for _, o, n in REPL), "length bookkeeping"

# ---------- hygiene guards (each with an injected positive control) ----------
def g_ascii(x): assert x.decode("ascii", "strict") is not None
def g_bom(x): assert not x.startswith(b"\xef\xbb\xbf")
def g_bareLF(x): assert b"\n" not in x.replace(b"\r\n", b"")
def g_bareCR(x): assert b"\r" not in x.replace(b"\r\n", b"")
def g_term(x): assert x.endswith(b"\r\n") and not x.endswith(b"\r\n\r\n")
def g_brace(x):
    d = 0
    for c in x:
        d += (c == 123) - (c == 125)
        assert d >= 0
    assert d == 0
def g_dollar(x): assert x.count(b"$") % 2 == 0
def g_nolabel(x): assert b"\\label" not in x
def g_nocite(x): assert b"\\cite" not in x
def g_refs(x):
    m = re.findall(rb"\\(?:eqref|ref)\{([^{}]*)\}", x)
    assert len(m) == 3 and set(m) == REFSET, "ref set drift"
def g_badh3(x): assert BADH3 not in x
def g_nooverwith(x): assert b"over with" not in x
def g_nocI(x): assert br"\(\mathbb C\mathbb I\)" not in x
def g_nooldcloser(x): assert CLOSER not in x
def g_nooldquant(x): assert br"(rotation and boost generators, at \(t=1\)" not in x

CTRL = 0
def prod_and_ctrl(name, g, bad, sample=None):
    global CTRL
    g(PAY if sample is None else sample)
    try:
        g(bad)
        print("CTRL-DEAD " + name); sys.exit(1)
    except Exception:
        CTRL += 1
        print("CTRL-FIRED " + name)

prod_and_ctrl("ascii", g_ascii, PAY + b"\xe9")
prod_and_ctrl("bom", g_bom, b"\xef\xbb\xbf" + PAY)
prod_and_ctrl("bareLF", g_bareLF, PAY + b"\n")
prod_and_ctrl("bareCR", g_bareCR, PAY + b"\r")
prod_and_ctrl("term", g_term, PAY + b"\r\n")
prod_and_ctrl("brace", g_brace, PAY + b"{")
prod_and_ctrl("dollar", g_dollar, PAY + b"$")
prod_and_ctrl("nolabel", g_nolabel, PAY + b"\\label{x}")
prod_and_ctrl("nocite", g_nocite, PAY + b"\\cite{x}")
prod_and_ctrl("refs", g_refs, PAY + b"\\ref{ass:bogus}")
prod_and_ctrl("badh3-absent", g_badh3, PAY + BADH3)
prod_and_ctrl("no-over-with", g_nooverwith, PAY + b"over with")
prod_and_ctrl("no-CI", g_nocI, PAY + br"\(\mathbb C\mathbb I\)")
prod_and_ctrl("no-old-closer", g_nooldcloser, PAY + CLOSER)
prod_and_ctrl("no-old-quantifier", g_nooldquant, PAY + br"(rotation and boost generators, at \(t=1\)")
print("HYGIENE-OK PAYLOAD-V3-BYTES", len(PAY))
print("PAYLOAD-V3-SHA1", hashlib.sha1(PAY).hexdigest())

# ---------- splice guards (each with an injected positive control) ----------
b = open(APP, "rb").read()
def g_pin(y): assert hashlib.sha1(y).hexdigest() == PIN
def g_anchor(y): assert y.count(ANCHOR) == 1
def g_dupcloser(sp): assert sp.count(CLOSER) == 1, "closer duplicated in splice"
def g_joinlen(sp): assert len(sp) == len(b) + len(PAY) + 2, "join length"
def g_contains(sp): assert sp.count(ANCHOR) == 1 and sp.count(PAY) == 1

prod_and_ctrl("appH-pin", g_pin, b + b"%", sample=b)
prod_and_ctrl("anchor-unique", g_anchor, b + ANCHOR, sample=b)
spliced = b.replace(ANCHOR, ANCHOR + PAY + b"\r\n", 1)
wrong = b.replace(ANCHOR, PAY + ANCHOR, 1)            # canonical-wrong object, control only
spliced_v2 = b.replace(ANCHOR, ANCHOR + v2 + b"\r\n", 1)  # v2 object, dup-closer control only
prod_and_ctrl("joinlen", g_joinlen, wrong, sample=spliced)
prod_and_ctrl("dup-closer", g_dupcloser, spliced_v2, sample=spliced)
for g in (g_joinlen, g_contains):
    g(spliced)
assert g_dupcloser(spliced) is None
assert len(wrong) == len(b) + len(PAY), "wrong-recipe is a different object (expected lengths differ)"

open("payload-126-v3.txt", "wb").write(PAY)
open("appH-spliced-126-v3.tex", "wb").write(spliced)
print("CTRL-FIRED-TOTAL", CTRL)
print("PRE", len(b), "POST", len(spliced), "DELTA", len(spliced) - len(b))
print("EXPECTED-POST", len(b) + len(PAY) + 2, "MATCH", len(spliced) == len(b) + len(PAY) + 2)
print("SPLICED-SHA1", hashlib.sha1(spliced).hexdigest())
print("ANCHOR-COUNT-SPLICED", spliced.count(ANCHOR), "CLOSER-COUNT-SPLICED", spliced.count(CLOSER))
print("MAKE-OK")
