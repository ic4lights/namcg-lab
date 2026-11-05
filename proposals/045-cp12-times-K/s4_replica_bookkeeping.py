"""
s4_replica_bookkeeping.py  (proposal 045)

Bookkeeping of the K-dependent two-derivative coefficients (units c of the merged Problem-B paragraphs: a scalar
component has c = 1/6 and the flat-cone area coefficient 1/6, 1/G = c/2pi with Lambda^2 replaced by the
proper-time integrals W_R, W_X of the merged product-background paragraph) on the six physical level-one
polarisations of CP^{1,2} x K, at the frozen-fibre leading symbol, and comparison with the area coefficient of
the three ledger replicas.

Inputs:
  * c = W_R c_s + W_X c_X, with c_s, c_X the generalised eigenvalues of the scalar a_1 form and of the index
    form relative to the Einstein-Hilbert form of the fibre-averaged metric (s2);
  * averaged-frame reading (s2, exact at every sampled point): c_X = -2, c_s = 1/6 on the five traceless
    polarisations; c_X = 1, c_s = -5/24 on the trace polarisation;
  * trace reading (s2, case (5,3), q = (3/7,1/2,-2/3,1/5)): generalised eigenvalues read from s2_forms_exact.out.txt
    (no ratio W_R : W_X gives a single coefficient; s2);
  * cone values in c units per unit of the scalar density (1/6 fixed-state and periodic, -1/12 smooth) and per
    unit of the vector-normalised index density X (-2 fixed-state, 0 periodic, 0 smooth), from the merged
    product-background paragraph (Dirac index cone -1 per Dirac field for the antiperiodic gluing, index density
    (1/2) X per Dirac field), with the cone in the base at every fibre point (fibre a spectator).
"""
import sympy as sp, re, os
WR, WX = sp.symbols('W_R W_X', real=True)
R = sp.Rational
out = []
def P(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)

cone_s = {'fixed-state': R(1, 6), 'periodic': R(1, 6), 'smooth': -R(1, 12)}
cone_X = {'fixed-state': -2, 'periodic': 0, 'smooth': 0}
cA = {k: cone_s[k] * WR + cone_X[k] * WX for k in cone_s}
P("area coefficient c_A (finite parts; the first-term terms of order Lambda^2 and log, and the first-term fibre-flux part, not included):")
for k, v in cA.items(): P("   %-12s c_A = %s" % (k, v))

P("\naveraged-frame reading:")
cT5 = R(1, 6) * WR - 2 * WX
cTtr = -R(5, 24) * WR + 1 * WX
P("   five traceless polarisations: c_T =", cT5, "   (single coefficient; -2 W_X > 0 since W_X < 0; W_R of no fixed sign)")
P("   trace polarisation:           c_T =", cTtr)
for k, v in cA.items():
    P("   %-12s c_A - c_T: five traceless %s ; trace polarisation %s" % (k, sp.simplify(v - cT5), sp.simplify(v - cTtr)))

P("\ntrace reading (fibre average of the pointwise densities), case (5,3), q = (3/7,1/2,-2/3,1/5):")
txt = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 's2_forms_exact.out.txt')).read()
blk = txt.split("base (y0,y4) = (5,3), chirality 1, ell = 4, q = [3/7, 1/2, -2/3, 1/5]")[1].split("base (y0,y4)")[0]
cx = eval(re.search(r"IX2 / EH on the five traceless polarisations: (\[.*?\])", blk).group(1))
cs = eval(re.search(r"SC2 / EH on the five traceless polarisations: (\[.*?\])", blk).group(1))
cx = [float(x) for x in cx]; cs = [float(x) for x in cs]
P("   index part alone (W_R = 0): c_T / W_X on the five traceless polarisations =", cx)
P("   fixed-state mixed-term gap (c_A - c_T) / W_X =", [round(-2 - x, 6) for x in cx], " (vanishes on none; signs differ)")
P("   scalar part alone (W_X = 0): c_T / W_R =", cs, " against c_A / W_R = 1/6 (fixed-state, periodic), -1/12 (smooth)")
open(__file__.replace('.py', '.out.txt'), 'w').write("\n".join(out) + "\n")
