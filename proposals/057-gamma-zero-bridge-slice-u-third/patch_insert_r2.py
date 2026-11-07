# Proposal 057 r2, script 4: single byte-span substitution implementing gatekeeper
# finding 1 in appH_insert.tex. Idempotent: re-running detects the patched state and
# writes nothing. The r1 state is preserved in appH_insert.r1.tex.
import hashlib
old = (r"the fixed-\(\gamma\) saturation exponent is \(-{(r^0)}^2/(8\sqrt2|\gamma|)")
new = (r"the fixed-\(\gamma\) saturation exponent is \(-g_{\mathrm{YM}}^2{(r^0)}^2/(8\sqrt2|\gamma|)")
T = "appH_insert.tex"
R1 = "appH_insert.r1.tex"
sha = lambda b: hashlib.sha256(b).hexdigest()
r1 = open(R1, "rb").read()
assert sha(r1) == "a7f80bea2d3546fb60ba168acdf6f5f980b37790412f19ceae9392b24b7db022" and len(r1) == 4017, "r1 copy pin broken"
cur = open(T, "rb").read()
if cur.count(old.encode()) == 0 and cur.count(new.encode()) == 1:
    print("already patched (idempotent); file unchanged")
    print("current size", len(cur), "sha256", sha(cur))
elif cur.count(old.encode()) == 1:
    out = cur.replace(old.encode(), new.encode(), 1)
    assert out.count(new.encode()) == 1 and out.count(old.encode()) == 0
    open(T, "wb").write(out)
    print("patched")
    print("pre  size", len(cur), "sha256", sha(cur))
    print("post size", len(out), "sha256", sha(out))
    print("inserted bytes:", len(new.encode()) - len(old.encode()))
else:
    raise SystemExit("unexpected clause counts: old=%d new=%d" % (cur.count(old.encode()), cur.count(new.encode())))
