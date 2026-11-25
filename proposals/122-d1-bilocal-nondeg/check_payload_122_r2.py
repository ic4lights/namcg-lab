# Item 122 r2 independent verifier: payload byte invariants on the NEW bytes,
# verbatim wording presence (review 122 r1 findings 2-3) and old-wording
# absence, independent POST recompute from live appH with the canonical splice
# replace(anchor+CRLFCRLF, anchor+CRLFCRLF+payload+CRLF, 1), wrong-zone variant
# hash check, and the exact heat-kernel spectrum values for the finding-4
# record fix. Reads only; writes nothing. All backslash strings are built from
# BB to keep this file free of escape sequences. Run: python -I (repo root).
import hashlib
import math
import os
import re

B = chr(92)
BB = B.encode("ascii")
ROOT = "C:/Users/redgi/Projects/namcg-lab@gpu"
D = ROOT + "/proposals/122-d1-bilocal-nondeg"
CRLF = chr(13).encode("ascii") + chr(10).encode("ascii")
CR = chr(13).encode("ascii")
LF = chr(10).encode("ascii")


def sha(b):
    return hashlib.sha1(b).hexdigest()


pay = open(D + "/payload-122.tex", "rb").read()
pre = open(ROOT + "/chapters/appH-microscopic-proofs.tex", "rb").read()
prev = open(D + "/preview-appH-spliced.tex", "rb").read()

fails = []


def chk(name, cond):
    print("%-46s %s" % (name, "OK" if cond else "FAIL"))
    if not cond:
        fails.append(name)


def lone(b, byte, other, before):
    n = 0
    for i, x in enumerate(bytearray(b)):
        if x != byte:
            continue
        if before:
            if i == 0 or b[i - 1:i] != other:
                n += 1
        else:
            if i == len(b) - 1 or b[i + 1:i + 2] != other:
                n += 1
    return n


chk("pure ASCII", all(x < 128 for x in bytearray(pay)))
chk("zero lone LF", lone(pay, LF[0], CR, True) == 0)
chk("zero lone CR", lone(pay, CR[0], LF, False) == 0)
chk("ends exactly one CRLF", pay.endswith(CRLF) and pay.count(CR) == 1 and pay.count(LF) == 1)
chk("not CR-CR-LF terminated", not pay.endswith(CR + CRLF))
chk("zero label / cite tokens", pay.count(BB + b"label") == 0 and pay.count(BB + b"cite") == 0)

refpat = BB + BB + b"(?:eq)?ref" + BB + b"{([^}]+)" + BB + b"}"
refs = set(re.findall(refpat, pay))
white = {b"ass:nondeg", b"ass:frame-lock", b"eq:V", b"eq:vev-is-frame", b"eq:vacuum-manifold", b"eq:Smicro"}
chk("refs exactly six whitelisted", refs == white)
alls = b""
for f in os.listdir(ROOT + "/chapters"):
    if f.endswith(".tex"):
        alls += open(ROOT + "/chapters/" + f, "rb").read()
chk("refs all resolve in chapters/", all(alls.count(BB + b"label{" + m + b"}") >= 1 for m in white))

new_ii = (b"If the carrier is finite and the link-variable assembly makes the carrier transport operator "
          b"unitary -- matrix link variables and exactly unitary fuzzy Wilson lines (transport as a unitary "
          b"superoperator on the finite carrier), path-ordered exponentials of anti-Hermitian fibre "
          b"connections, for which " + BB + b"(" + BB + b"sigma_{" + BB + b"min}=1" + BB + b")"
          b" exactly and uniformly in the carrier size -- then " + BB + b"(w=1" + BB + b")")
chk("finding-2 verbatim wording present", new_ii in pay)
new_iii = (b"with fibre-wise equality on radial fibres " + BB + b"(" + BB + b"Phi=" + BB + b"rho" + BB
           + b",U" + BB + b") (and operator equality when " + BB + b"(" + BB + b"rho" + BB + b") is constant)")
chk("finding-3 verbatim wording present", new_iii in pay)
chk("old (ii) wording absent", b"transporter matrix is unitary" not in pay)
chk("old (iii) wording absent", b"with equality on radial fibres" not in pay)

ANCHOR = (b"remains the upstream input that gates what any Presentation-B measure can be cited as; "
          b"Assumptions~" + BB + b"ref{ass:frame-lock} and~" + BB + b"ref{ass:nondeg} remain assumed, "
          b"so Problem~D remains OPEN and PROGRAMME-CONDITIONAL.")
chk("anchor count 1 in live appH", pre.count(ANCHOR + CRLF + CRLF) == 1)
post = pre.replace(ANCHOR + CRLF + CRLF, ANCHOR + CRLF + CRLF + pay + CRLF, 1)
chk("recomputed POST == generator preview bytes", post == prev)
chk("POST = PRE + PAY + 2", len(post) == len(pre) + len(pay) + 2)
print("PRE  %d  PAY %d  POST %d" % (len(pre), len(pay), len(post)))
print("POST-SHA1-12 %s  PAYLOAD-SHA1-12 %s" % (sha(post)[:12], sha(pay)[:12]))
wrong = pre.replace(ANCHOR + CRLF + CRLF, pay + CRLF + ANCHOR + CRLF + CRLF, 1)
chk("wrong-zone variant same size", len(wrong) == len(post))
chk("wrong-zone variant hashes differently", sha(wrong) != sha(post))

s2 = 0.15 * 0.15
for n in (32, 64, 128, 256):
    print("exact exp(-s^2 n^2 / 4)  s=0.15  n=%3d : %.3g" % (n, math.exp(-s2 * n * n / 4.0)))

if fails:
    print("CHECK-FAILURES:", fails)
    raise SystemExit(1)
print("CHECK-FAILURES: 0 (none)")
