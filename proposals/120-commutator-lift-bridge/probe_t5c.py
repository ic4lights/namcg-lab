# probe_t5c.py - diagnostic (no changes to verify_r120.py): execs the verify prefix
# (artifact checks + T2..T5b), then times the T5c region step by step with wrapped
# helpers to find the real cost. Run: python -I -u -B probe_t5c.py
import io
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(HERE, "verify_r120.py"), "r").read().splitlines(True)
ks = [i for i, l in enumerate(src) if l.strip().startswith("Bs1 = brackets_full(Phi_q")]
ke = [i for i, l in enumerate(src) if "T5c-teeth" in l]
assert len(ks) == 1 and len(ke) >= 1, "region anchors %d/%d" % (len(ks), len(ke))
k, e = ks[0], ke[0] + 3

G = {"__name__": "probe", "__file__": os.path.join(HERE, "verify_r120.py")}
t0 = time.time()
exec(compile("".join(src[:k]), "verify_prefix", "exec"), G)
print("PREFIX DONE t=%.1fs" % (time.time() - t0), flush=True)


def timed(f, name):
    def w(*a, **kw):
        t = time.time()
        r = f(*a, **kw)
        print("T %-14s %.2fs lenargs=%s" % (name, time.time() - t, [len(x) if hasattr(x, "__len__") and not isinstance(x, (str, int)) else x for x in a][:3]), flush=True)
        return r
    return w


for fn in ["star", "D2op", "simplify_sym", "polymat", "xhat_sym", "brackets_full", "lift_from_B", "mats_eq"]:
    G[fn] = timed(G[fn], fn)

for lbl in ["Bs1", "Bs2", "L1", "L2"]:
    t = time.time()
    if lbl == "Bs1":
        G["Bs1"] = G["brackets_full"](G["Phi_q"], G["Asym"], G["ThN"], G["n"])
    elif lbl == "Bs2":
        import sympy as sp
        G["Phi_q2"] = G["madd"](G["Phi_q"], [((0, 0, 0, 0), sp.Symbol("ss", complex=True) * sp.eye(G["n"]))])
        G["Bs2"] = G["brackets_full"](G["Phi_q2"], G["Asym"], G["ThN"], G["n"])
    elif lbl == "L1":
        G["L1"] = G["lift_from_B"](G["Bs1"], G["ThN"], G["n"])
    else:
        G["L2"] = G["lift_from_B"](G["Bs2"], G["ThN"], G["n"])
    print("STEP %s t=%.1fs" % (lbl, time.time() - t), flush=True)

t = time.time()
eqs = [G["mats_eq"](a, b, G["n"]) for a, b in zip(G["Bs1"], G["Bs2"])]
print("STEP mats_eq all=%s t=%.1fs" % (all(eqs), time.time() - t), flush=True)
t = time.time()
z = (G["L2"] == G["L1"]) or (G["sp"].simplify(G["L2"] - G["L1"]) == 0)
print("STEP L2eqL1 struct=%s final=%s t=%.1fs" % (G["L2"] == G["L1"], z, time.time() - t), flush=True)
print("PROBE DONE", flush=True)
