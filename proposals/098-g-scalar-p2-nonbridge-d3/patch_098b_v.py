# patch_098b_v.py - appends V6 (two-angle patch level-set curve tracing) block to verify_098.py before SUMMARY.
# Run from repo root. First application used a grid-band cluster count with too-tight eps (reverted);
# this is the applied version: predictor-corrector tracing of one P2 level set with mod-permutation net counts.
D = "proposals/098-g-scalar-p2-nonbridge-d3/"
p = D + "verify_098.py"
s = open(p).read()
anchor = 'print("SUMMARY "'
i = s.find(anchor)
assert i > 0 and s.count(anchor) == 1, "anchor"
assert "V6" not in s, "already applied"
V6 = '''# V6 two-angle patch: rank-2 diagonal map, and one P2 level set traced as a curve of distinct diagonals
def dpatch(lamv, c1, s1, c2, s2):
    l1, l2, l3 = lamv[:3]
    a = l1 * s1 * s1 + l2 * c1 * c1
    return (l1 * c1 * c1 + l2 * s1 * s1, a * c2 * c2 + l3 * s2 * s2, a * s2 * s2 + l3 * c2 * c2)

def v6_grads(lamv, th, ph, tau):
    c1, s1, c2, s2 = np.cos(th), np.sin(th), np.cos(ph), np.sin(ph)
    h = 1e-6
    ch, sh = np.cos(h), np.sin(h)
    d0 = dpatch(lamv, c1, s1, c2, s2)
    da = dpatch(lamv, c1 * ch - s1 * sh, s1 * ch + c1 * sh, c2, s2)
    db = dpatch(lamv, c1, s1, c2 * ch - s2 * sh, s2 * ch + c2 * sh)
    q0 = sum(d * d for d in d0)
    g0 = (sum(d * d for d in da) - q0) / h / tau**2
    g1 = (sum(d * d for d in db) - q0) / h / tau**2
    j00 = (da[0] - d0[0]) / h
    j01 = (da[1] - d0[1]) / h
    j10 = (db[0] - d0[0]) / h
    j11 = (db[1] - d0[1]) / h
    return q0 / tau**2, g0, g1, j00 * j11 - j01 * j10

def v6_case(lamv, tag, nd):
    th = np.linspace(0, 2 * np.pi, 900, endpoint=False)
    C1, C2 = np.meshgrid(np.cos(th), np.cos(th))
    S1, S2 = np.meshgrid(np.sin(th), np.sin(th))
    tau = float(sum(lamv))
    p2, g0, g1, detJ = v6_grads(lamv, C1, C2, tau)
    gmag = np.sqrt(g0 * g0 + g1 * g1)
    reg = (np.abs(detJ) > 1e-5) & (gmag > 1e-5)
    chk(tag + " rank2 region", reg.mean() > 0.15, "frac %.3f" % reg.mean())
    ipk = np.unravel_index(np.argmax(np.where(reg, np.minimum(np.abs(detJ), gmag), -1.0)), detJ.shape)
    t0, f0 = th[ipk[0]], th[ipk[1]]
    lev = p2[ipk]
    chk(tag + " interior level", p2.min() + 1e-6 < lev < p2.max() - 1e-6,
        "lev %.5f in [%.5f, %.5f]" % (lev, p2.min(), p2.max()))
    t, f = t0, f0
    steps, cols = [], []
    for k in range(400):
        p2k, g0k, g1k, _ = v6_grads(lamv, t, f, tau)
        nrm = np.hypot(g0k, g1k)
        tx, ty = g1k / nrm, -g0k / nrm
        t = t + 0.02 * tx
        f = f + 0.02 * ty
        for _ in range(3):
            p2c, g0c, g1c, _ = v6_grads(lamv, t, f, tau)
            g = g0c * g0c + g1c * g1c
            if g < 1e-12:
                break
            t = t - (p2c - lev) * g0c / g
            f = f - (p2c - lev) * g1c / g
        d = dpatch(lamv, np.cos(t), np.sin(t), np.cos(f), np.sin(f))
        row = list(d) + ([lamv[3]] if nd == 4 else [])
        cols.append(np.sort(row))
        steps.append((t, f))
    arr = np.stack(cols)
    dev = max(abs(v6_grads(lamv, t, f, tau)[0] - lev) for t, f in steps)
    for dl in (0.02, 0.008):
        keys = np.unique(np.round(arr / dl).astype(np.int64), axis=0)
        if dl == 0.02:
            n1 = len(keys)
        else:
            chk(tag + " level clusters", len(keys) >= 30 and len(keys) >= 1.5 * n1 and dev < 1e-6,
                "n 0.020 -> %d, n 0.008 -> %d, leveldev %.1e" % (n1, len(keys), dev))

v6_case((3.0, 1.0, 0.2), "V6 D3", 3)
v6_case((3.0, 1.0, 0.2, 0.7), "V6 D4", 4)
'''
s = s[:i] + V6 + s[i:]
open(p, "w", newline="").write(s)
print("V6-APPENDED")
raise SystemExit(0)
