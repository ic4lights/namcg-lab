# simulate_apply_084.py  READ-ONLY splice simulation for proposal 084.
# Splices insert-r1.tex plus one CRLF immediately before the G-side Vacuum term
# header, after asserting the live PRE pins and the unique 083-tail anchor.
# Performs no write to any repository file.
# Run: python -I proposals/084-g-moments-coupledmixed/simulate_apply_084.py  (repo root)
import hashlib
CRLF = bytes([13, 10])
LF = bytes([10])
APP = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/084-g-moments-coupledmixed/insert-r1.tex"
b = open(APP, "rb").read()
ins = open(INS, "rb").read()
PRE = (733361, "c35bfed009668845a5ff313e0a35b3f48374cbc843ed85e9d4fedb2a936cedfd")
assert len(b) == PRE[0], ("PRE size", len(b))
assert hashlib.sha256(b).hexdigest() == PRE[1], "PRE sha"
pin = rb"The mean, the variance and the slot shifts are inputs of the named state class, they do not fix the state that sets \(W\) and \(g\), leave the missing steps (i)-(iv) of the Missing step paragraph unchanged, and they close nothing in Problem~G."
assert b.count(pin) == 1, "pin count"
end = b.index(pin) + len(pin)
vac = b.index(rb"\emph{Vacuum term.}", end)
assert b[end:vac] == CRLF + CRLF, ("gap", b[end:vac])
post = b[:vac] + ins + CRLF + b[vac:]
assert len(post) == len(b) + len(ins) + 2
assert post.count(rb"\emph{Induced coupling of the imaginary-part and slot data of the rank-one Gaussian edge charge.}") == 1
assert post.count(rb"\emph{Vacuum term.}") == 2
assert post.count(CRLF) == b.count(CRLF) + 2 and post.count(LF) - post.count(CRLF) == 0
print("PRE OK size %d sha8 %s" % (len(b), hashlib.sha256(b).hexdigest()[:8]))
print("POST size %d sha8 %s CRLF %d bareLF %d" % (
    len(post), hashlib.sha256(post).hexdigest()[:8],
    post.count(CRLF), post.count(LF) - post.count(CRLF)))
print("close-idiom count PRE %d POST %d" % (
    b.count(rb"close nothing in Problem~G."),
    post.count(rb"close nothing in Problem~G.")))
print("insert bytes %d sha8 %s" % (len(ins), hashlib.sha256(ins).hexdigest()[:8]))
print("no write performed")
