# simulate_apply_083.py  READ-ONLY splice simulation for proposal 083.
# Splices insert-r1.tex plus one CRLF immediately before the G-side Vacuum term
# header, after asserting the live PRE pins and the unique 082-tail anchor.
# Performs no write to any repository file.
# Run: python -I proposals/083-g-moments-aoddsector/simulate_apply_083.py  (repo root)
import hashlib
CRLF = bytes([13, 10])
LF = bytes([10])
APP = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/083-g-moments-aoddsector/insert-r1.tex"
b = open(APP, "rb").read()
ins = open(INS, "rb").read()
PRE = (731183, "956070afcd26fc1c8ffd040ca2d8bb8340467de79117bd0a10d782b6dd062c52")
assert len(b) == PRE[0], ("PRE size", len(b))
assert hashlib.sha256(b).hexdigest() == PRE[1], "PRE sha"
pin = rb"they do not by themselves recover the effective-dimension lower bound of the moment map, say nothing about whether true block-row profiles concentrate, do not fix the state that sets \(W\) and \(g\), leave the missing steps (i)-(iv) of the Missing step paragraph unchanged, and they close nothing in Problem~G."
assert b.count(pin) == 1, "pin count"
end = b.index(pin) + len(pin)
vac = b.index(rb"\emph{Vacuum term.}", end)
assert b[end:vac] == CRLF + CRLF, ("gap", b[end:vac])
post = b[:vac] + ins + CRLF + b[vac:]
assert len(post) == len(b) + len(ins) + 2
assert post.count(rb"\emph{Odd-sector map of the non-centred Gaussian rank-one edge charge.}") == 1
assert post.count(rb"\emph{Vacuum term.}") == 2
print("PRE OK size %d sha8 %s" % (len(b), hashlib.sha256(b).hexdigest()[:8]))
print("POST size %d sha8 %s CRLF %d bareLF %d" % (
    len(post), hashlib.sha256(post).hexdigest()[:8],
    post.count(CRLF), post.count(LF) - post.count(CRLF)))
print("close-idiom count PRE %d POST %d" % (
    b.count(rb"close nothing in Problem~G."),
    post.count(rb"close nothing in Problem~G.")))
print("no write performed")
