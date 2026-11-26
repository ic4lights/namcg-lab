# patch_098_v.py - replaces the V3 doubling block and the V4 block in verify_098.py. One-shot. Run from repo root.
D = "proposals/098-g-scalar-p2-nonbridge-d3/"
s = open(D + "verify_098.py").read()

a0 = "# doubling-ratio non-atomicity at midrange level a\n"
a1 = 'chk("V3 doubling ratio", 1.1 < r1 < 2.4, "ratio %.2f" % r1)\n'
i0, i1 = s.find(a0), s.find(a1)
assert 0 <= i0 < i1
newV3 = (
    "# mass-per-width at the median halves scales: bounded above and below => no atom\n"
    "am = np.median(p2b)\n"
    "def mpw(h):\n"
    "    return np.mean((p2b > am - h) & (p2b <= am + h)) / (2 * h)\n"
    "w1, w2, w3 = mpw(0.02), mpw(0.005), mpw(0.00125)\n"
    'chk("V3 mass-per-width bounded", 0.4 < w2 / w1 < 2.5 and 0.4 < w3 / w2 < 2.5,\n'
    '    "w %.1f %.1f %.1f" % (w1, w2, w3))\n'
)
s = s[:i0] + newV3 + s[i1 + len(a1):]

b0 = "# V4 D=2 hetero: conditional law"
b1 = 'chk("V4b uniform contrast", abs(predU - pred) > 30 * se, "unif %.5f tilt %.5f" % (predU, pred))\n'
j0, j1 = s.find(b0), s.find(b1)
assert 0 <= j0 < j1
newV4 = (
    "# V4 D=2 hetero batched: P2 conditional on spectrum = pushforward of exp(-beta G11) via P2=2x^2-2x+1\n"
    "M2, D2 = 4, 2\n"
    "gpr2 = np.array([1.0, 2.0]); beta = 1 / 1.0 - 1 / 2.0  # sigma=1\n"
    "acc = []\n"
    "for rep in range(8):\n"
    "    A = (rng.standard_normal((375000, M2, D2)) + 1j * rng.standard_normal((375000, M2, D2))) / np.sqrt(2) * np.sqrt(gpr2)\n"
    "    G = gram(A)\n"
    "    t = np.real(np.trace(G, axis1=-2, axis2=-1))\n"
    "    p = evals(G) / t[..., None]\n"
    "    band2 = (np.abs(t - 4.0) < 0.3) & (np.abs(p[:, 0] - 0.65) < 0.012)\n"
    "    x = np.real(G[:, 0, 0]) / t\n"
    "    acc.append(2 * x[band2]**2 - 2 * x[band2] + 1)\n"
    "p2b2 = np.concatenate(acc); nb2 = len(p2b2)\n"
    "emp = p2b2.mean(); se = p2b2.std() / np.sqrt(nb2)\n"
    "# quadrature prediction at band-center spectrum tau=4, lam=(2.6,1.4): x in [0.35,0.65]\n"
    "xs = np.linspace(0.35, 0.65, 20001)\n"
    "w = np.exp(-beta * (xs * 4.0))\n"
    "pred = np.trapezoid(w * (2 * xs**2 - 2 * xs + 1), xs) / np.trapezoid(w, xs)\n"
    "z = (emp - pred) / se\n"
    'chk("V4 tilt scalar pred", nb2 > 1500 and abs(z) < 4.0, "n=%d emp %.5f pred %.5f z %.1f" % (nb2, emp, pred, z))\n'
    "# V4b no atom and full support: 10 equal-width bins on the fibre interval image, each >= 5 counts\n"
    "lo, hi = 0.5, 2 * 0.35**2 - 2 * 0.35 + 1\n"
    "h2, _ = np.histogram(p2b2, bins=10, range=(lo, hi))\n"
    'chk("V4b bins nonzero", h2.min() >= 5, "min count %d" % h2.min())\n'
)
s = s[:j0] + newV4 + s[j1 + len(b1):]
open(D + "verify_098.py", "w", newline="").write(s)
print("V-BLOCKS PATCHED")
raise SystemExit(0)
