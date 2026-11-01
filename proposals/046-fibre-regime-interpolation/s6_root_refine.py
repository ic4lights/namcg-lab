"""s6_root_refine.py (proposal 046, round 3; review-r2 finding 3).

s4_window_scan.py reports as M* the left endpoint of a grid bracket of ratio 10^(1/40), not a root.  This script solves
    f(M) = W_B(M) lambda_L + (1 + 24 L/c)/M^2 = 0,    W_B = W1 beta_X,
by brentq inside each bracket and compares with the table of review-r2.md.  The term 24 L/c is s4's -4 (L/c) lambda_P with
lambda_P = -6.

Inputs taken from s4 and not retyped: the functions cJJ_closed and W_index are compiled from the source of
s4_window_scan.py with ast (the module itself is not imported, since importing it reruns s4 and rewrites its output);
lambda_L is read from the saved s4_window_scan.out.txt; the grid is s4's; coth^2 tau = 25/9 at the base point (5,3).

The script compares and reports. It does not adjust anything to fit.  Uniqueness of the zero is tested by the sign changes
on s4's grid only, so it is a grid statement and not a proof.
"""
import ast, os, re
import numpy as np
from scipy.optimize import brentq

here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 's4_window_scan.py'), encoding='utf-8').read()
tree = ast.parse(src)
want = {'cJJ_closed', 'W_index'}
nodes = [nd for nd in tree.body if isinstance(nd, ast.FunctionDef) and nd.name in want]
assert {nd.name for nd in nodes} == want
ns = {'np': np}
exec(compile(ast.Module(body=nodes, type_ignores=[]), 's4_window_scan.py', 'exec'), ns)
W_index = ns['W_index']

s4out = open(os.path.join(here, 's4_window_scan.out.txt'), encoding='utf-8').read()
lamL = float(re.search(r'lambda_L = (-?[0-9.]+)', s4out).group(1))
coth2 = 25.0 / 9.0
mu = lambda J: J * (J + 2)
grid = np.logspace(-3, 3, 241)
LCS = (0.0, 1.0, 10.0)

out = []
def P(*a):
    line = " ".join(str(x) for x in a)
    print(line)
    out.append(line)

P("inputs: lambda_L = %.6f (saved s4 output), coth^2 tau = 25/9 = %.6f, spectrum mu_J = J(J+2), grid = s4's (241 points, 1e-3 to 1e3)" % (lamL, coth2))
P("W_index reproduces the s4 check lines:")
for M, n in ((0.1, 30), (3.0, 30)):
    W1, b = W_index(M, mu, n)
    P("   M = %g, n = %d: W1 = %.6f, beta_X = %.6f" % (M, n, W1, b))

def WB(M, n):
    W1, b = W_index(M, mu, n)
    return W1 * b

def solve(n):
    """for one n: returns {L/c: (number of grid sign changes, M*, beta_X, coth^2/M*, left grid endpoint, residual)}"""
    wb = np.array([WB(M, n) for M in grid])
    res = {}
    for Lc in LCS:
        f_grid = wb * lamL + (1 + 24 * Lc) / grid ** 2
        sc = np.where(np.sign(f_grid[:-1]) != np.sign(f_grid[1:]))[0]
        f = lambda M: WB(M, n) * lamL + (1 + 24 * Lc) / M ** 2
        k = sc[0]
        Ms = brentq(f, grid[k], grid[k + 1], xtol=1e-13, rtol=1e-13)
        b = W_index(Ms, mu, n)[1]
        res[Lc] = (len(sc), Ms, b, coth2 / Ms, grid[k], f(Ms))
    return res

allres = {n: solve(n) for n in range(2, 301)}

P("\n(1) the nine s4 rows: left grid endpoint as s4 prints it, and the root")
P("   n    L/c   M*(s4 grid)  M*(root)    beta_X(root)  coth^2/M*(s4 grid)  coth^2/M*(root)  residual f(M*)")
for n in (2, 30, 300):
    for Lc in LCS:
        c, Ms, b, t, g, r = allres[n][Lc]
        P("   %-4d %-5g %-12.4g %-11.5f %-13.5f %-19.4g %-16.5f %.1e" % (n, Lc, g, Ms, b, coth2 / g, t, r))

printed = {
    0.0: dict(M=(0.2194, 0.6724), b=(0.3925, 0.7185), t=(4.131, 12.66)),
    1.0: dict(M=(1.1301, 5.0875), b=(0.51999, 0.9288), t=(0.546, 2.458)),
    10.0: dict(M=(3.6276, 30.762), b=(0.52001, 0.97425), t=(0.0903, 0.7657)),
}
def digits(x):
    s = repr(x)
    return len(s.split('.')[1]) if '.' in s else 0

def table(ns_, title, compare):
    P("\n" + title)
    ok = True
    for Lc in LCS:
        rows = [allres[n][Lc] for n in ns_]
        nz = sorted(set(r[0] for r in rows))
        Ms = [r[1] for r in rows]; bs = [r[2] for r in rows]; ts = [r[3] for r in rows]
        mono = all(Ms[i + 1] < Ms[i] for i in range(len(Ms) - 1))
        i0, i1 = int(np.argmin(Ms)), int(np.argmax(Ms))
        P("   L/c = %-4g: sign changes per n %s; M* decreasing in n: %s" % (Lc, nz, mono))
        P("      M*        %.6f (n=%d) to %.6f (n=%d)" % (Ms[i0], ns_[i0], Ms[i1], ns_[i1]))
        P("      beta_X    %.6f (n=%d) to %.6f (n=%d)" % (min(bs), ns_[int(np.argmin(bs))], max(bs), ns_[int(np.argmax(bs))]))
        P("      coth^2/M* %.6f (n=%d) to %.6f (n=%d)" % (min(ts), ns_[int(np.argmin(ts))], max(ts), ns_[int(np.argmax(ts))]))
        if compare:
            for key, vals in (('M', Ms), ('b', bs), ('t', ts)):
                lo, hi = printed[Lc][key]
                got = (round(min(vals), digits(lo)), round(max(vals), digits(hi)))
                match = got == (lo, hi)
                ok = ok and match
                P("      review table %-2s (%s, %s), rounded root values (%s, %s): %s" % (key, lo, hi, got[0], got[1], 'MATCH' if match else 'DIFFERENT'))
    return ok

review_ns = list(range(2, 61)) + list(range(65, 301, 5))
ok = table(review_ns, "(2) the review's sample: n = 2..60 and every 5th n up to 300 (%d values)" % len(review_ns), True)
P("\n   review table reproduced at the printed digits: %s" % ok)

all_ns = list(range(2, 301))
table(all_ns, "(3) every integer n from 2 to 300 (%d values), which is the range the insert states" % len(all_ns), False)

P("\n(4) the inequalities printed in the insert, every integer 2 <= n <= 300")
r0 = [allres[n][0.0] for n in all_ns]
r1 = [allres[n][Lc] for n in all_ns for Lc in (1.0, 10.0)]
checks = [
    (r"0.21 <= M* <= 0.68 (L/c = 0)", all(0.21 <= r[1] <= 0.68 for r in r0)),
    (r"coth^2/M* >= 4.1 (L/c = 0)", all(r[3] >= 4.1 for r in r0)),
    (r"1.1 <= M* <= 31 (L/c = 1, 10)", all(1.1 <= r[1] <= 31 for r in r1)),
    (r"0.51 <= beta_X <= 0.98 (L/c = 1, 10)", all(0.51 <= r[2] <= 0.98 for r in r1)),
    (r"exactly one sign change on the grid, all n and L/c", all(allres[n][Lc][0] == 1 for n in all_ns for Lc in LCS)),
]
for name, v in checks:
    P("   %-55s %s" % (name, v))

P("\n(5) the values printed before review-r2 replacement (d), against the roots")
old = [
    (r"M* <= 0.67 (L/c = 0)", all(r[1] <= 0.67 for r in r0)),
    (r"coth^2/M* >= 4.2 (L/c = 0)", all(r[3] >= 4.2 for r in r0)),
    (r"M* <= 30 (L/c = 1, 10)", all(r[1] <= 30 for r in r1)),
    (r"0.52 <= beta_X <= 0.97 (L/c = 1, 10)", all(0.52 <= r[2] <= 0.97 for r in r1)),
]
for name, v in old:
    P("   %-55s %s" % (name, v))

open(os.path.join(here, 's6_root_refine.out.txt'), 'w', newline='\n').write("\n".join(out) + "\n")
