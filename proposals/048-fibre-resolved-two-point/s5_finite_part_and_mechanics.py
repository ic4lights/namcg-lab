"""
s5_finite_part_and_mechanics.py (proposal 048). Prints to stdout only; writes nothing.

(A) EH form of the trace-reversed variable: exact, with forms_lib.EH2, for transverse h on a frozen background.
(B) I[X] for dust, source S1, general rho: closed K(tau) by finite parts, against a regulated quadrature.
(C) potentials for general rho, source S1, by finite parts: hhat^{11}/hhat^{00} at large s^2.
(D) the mass dependence that turns S2 into S1.
(E) insert mechanics: ASCII, LF, anchor uniqueness, labels and cites exist, one closing status sentence.
"""
import sys, os, re, random
sys.dont_write_bytecode = True
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', '046-fibre-regime-interpolation'))
from forms_lib import *
import numpy as np
from scipy import integrate
random.seed(4805)

print("(A) EH2 of hhat = h - (1/2) eta t, g-background eta/m^2, cometric perturbations lowered with G; h transverse to q")
ok = True
for trial in range(5):
    m = sp.Rational(random.randint(1, 5), random.randint(1, 3))
    q = sp.Matrix([R(random.randint(-7, 7), 3) for _ in range(4)])
    qu = ETA * q
    # transverse h: build from three vectors orthogonal to q
    vecs = []
    while len(vecs) < 2:
        w = sp.Matrix([R(random.randint(-5, 5), 2) for _ in range(4)])
        qq_ = (qu.T * ETA * qu)[0]
        if qq_ == 0: continue
        w = w - qu * (qu.T * ETA * w)[0] / qq_
        vecs.append(w)
    h = vecs[0] * vecs[1].T + vecs[1] * vecs[0].T
    assert all(sp.simplify(x) == 0 for x in (h * q))
    t = sum(ETA[i, i] * h[i, i] for i in range(4))
    hhat = h - ETA.inv() * t / 2
    gb = ETA / m ** 2; gi = gb.inv()
    Hdown = -gb * hhat * gb
    eh = EH2(gb, Hdown, q)
    q2 = (q.T * ETA * q)[0]
    hh = sum(ETA[i, i] * ETA[j, j] * h[i, j] ** 2 for i in range(4) for j in range(4))
    pred = -q2 * (hh - t ** 2 / 2) / (8 * m ** 6)
    ok = ok and sp.simplify(eh - pred) == 0
print("   EH(hhat) = -(q^2/(8 m^6)) (h.h - t^2/2) exactly at the sampled draws:", ok)

print("\n(B) K(tau): I = (1/4) rho0^2 [1 + (rho-1) K], K = finite part of <((c^2 + r(1-c^2))/(r(1-c^2) - c^2))^2>")
def fp_moments(r):
    th = 1 + r; P = r / th; c0 = np.sqrt(P); at = np.arctanh(c0)
    I1 = -at / c0                                   # PV int_0^1 dc/(c^2-P)
    I2 = -1 / (2 * P * (1 - P)) + at / (2 * P * c0)  # finite part int_0^1 dc/(c^2-P)^2
    return th, P, I1, I2
def K_closed(r):
    th, P, I1, I2 = fp_moments(r)
    # ratio = -(1-r)/th + (2r/th)/(r - th c^2) and 1/(r - th c^2) = -(1/th)/(c^2-P)
    A0 = -(1 - r) / th; A1 = (2 * r / th)
    return A0 ** 2 + 2 * A0 * A1 * (-(1 / th) * I1) + A1 ** 2 * (1 / th ** 2) * I2
def K_reg(r, eps):
    d = lambda c: r * (1 - c * c) - c * c
    n = lambda c: (c * c + r * (1 - c * c)) ** 2
    pts = [np.sqrt(r / (1 + r))]
    f = lambda c: n(c) * (d(c) ** 2 - eps ** 2) / (d(c) ** 2 + eps ** 2) ** 2      # real part of n/(d + i eps)^2
    return integrate.quad(f, 0, 1, points=pts, limit=8000)[0]
for s2 in (1.0, 9.0, 100.0, 1e4):
    r = 1 / s2
    print("   s^2=%-8g K closed = %.6f ; regulated eps=1e-3: %.6f ; eps=1e-4: %.6f" % (s2, K_closed(r), K_reg(r, 1e-3), K_reg(r, 1e-4)))

print("\n(C) potentials, general rho, S1: hbar = hbar_0 + delta, units m=k=1, A=1:  hbar_0^{00} = f/2, hbar_0^{11} = -(1+f)/4;")
print("    delta^{mu nu} = -(rho-1) < ((u.v)^2 + v.v/2) v^mu v^nu/(v.v)^2 > (alpha = -(1/2)[J/v.v + (rho-1)(J.v)v/(v.v)^2], J = Xv)")
def pot(s2, rho_, eps=2e-5):
    r = 1 / s2; pts = [np.sqrt(r / (1 + r))]
    d = lambda c: r * (1 - c * c) - c * c
    re1 = lambda c: d(c) / (d(c) ** 2 + eps ** 2)
    re2 = lambda c: (d(c) ** 2 - eps ** 2) / (d(c) ** 2 + eps ** 2) ** 2
    f = integrate.quad(lambda c: c * c * re1(c), 0, 1, points=pts, limit=8000)[0]
    fa = integrate.quad(lambda c: r * (1 - c * c) * re1(c), 0, 1, points=pts, limit=8000)[0]
    # (u.v)^2 = c^2, v.v/2 = d/2
    d00 = integrate.quad(lambda c: (c * c + d(c) / 2) * c * c * re2(c), 0, 1, points=pts, limit=8000)[0]
    daa = integrate.quad(lambda c: (c * c + d(c) / 2) * r * (1 - c * c) / 2 * re2(c), 0, 1, points=pts, limit=8000)[0]
    h00 = f / 2 - (rho_ - 1) * d00
    B = -fa / 4 - (rho_ - 1) * daa
    tr = -h00 + 2 * B
    return h00 + tr / 2, B - tr / 2
for rho_ in (0.75, 1.25):
    row = []
    for s2 in (100.0, 1e4, 1e6):
        E, Fp = pot(s2, rho_)
        row.append((s2, round(E, 5), round(Fp, 5), round(Fp / E, 5)))
    print("   rho=%.2f (s^2, hhat^00, hhat^11, ratio): %s ; expected hhat^00 -> -rho/4 = %.4f" % (rho_, row, -rho_ / 4))

print("\n(D) S_E = rho_M (gamma dphi dphi + M^2 e^{2 delta} phi^2)/2 with delta = t/(4 m^2), t = eta_mu nu hbar^{mu nu}:")
print("    source of hbar^{mu nu} per rho_M: dphi dphi/2 + (M^2 phi^2) eta_mu nu/(4 m^2).  For dust the two terms are in the ratio u u : eta/2 after normalising eta/m^2 -> G; hence X = T - eta tr T/2 for dust.")
print("    delta = delta phi of the merged paragraph, phi = (1/2) ln(rho/sqrt|g|): delta phi = t/(4 m^2).")

print("\n(E) insert mechanics")
ins_b = open(os.path.join(here, 'appH_insert.tex'), 'rb').read()
print("   bytes", len(ins_b), "ASCII", all(b < 128 for b in ins_b), "CR count", ins_b.count(b'\r'), "BOM", ins_b[:3] == b'\xef\xbb\xbf')
ins = ins_b.decode()
repo = os.path.join(here, '..', '..')
appH = open(os.path.join(repo, 'chapters', 'appH-microscopic-proofs.tex'), encoding='utf-8').read()
anchor = '\\section{Problem G: HBEV}'
print("   anchor count in appH:", appH.count(anchor))
allt = ''
for root, _, files in os.walk(os.path.join(repo, 'chapters')):
    for fn in files:
        if fn.endswith('.tex'): allt += open(os.path.join(root, fn), encoding='utf-8').read()
for lab in re.findall(r'\\ref\{([^}]+)\}', ins):
    print("   ref", lab, "labels found:", allt.count('\\label{' + lab + '}'))
bib = open(os.path.join(repo, 'bib', 'namcg.bib'), encoding='utf-8').read()
for keyset in set(re.findall(r'\\cite\{([^}]+)\}', ins)):
    for key in keyset.split(','):
        print("   cite", key, "entries:", bib.count('{' + key.strip() + ','))
print("   new labels in insert:", re.findall(r'\\label\{([^}]+)\}', ins))
print("   status sentences:", len(re.findall(r'remain open and PROGRAMME-CONDITIONAL', ins)), "; closing line:", ins.rstrip().split('. ')[-1])
print("   paragraphs:", len([p for p in ins.split('\n\n') if p.strip()]))
print("   process-language scan:", [w for w in ('proposal', 'researcher', 'gatekeeper', 'as proposed', 'scout', 'review') if re.search(r'' + w + r'', ins.lower())])
