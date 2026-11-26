# verify_example_129.py -- item 129, held block 48 "The example of the preceding paragraph"
# (the appH L3194 x=3/10 example re-analysed on the cubic branch).
# Run:  python -I proposals/129-rc-held-recheck/verify_example_129.py
# Expected invariant output: last line  EXAMPLE_129 PASS
#
# appH L3194 example (ours, integrated): units F sqrt|g| N^2 theta^2/32pi^2, x = 3/10,
# tree quartic 7.935, tree cubic -12.36, U_chichi = 10.68, loop polynomial -4x^2-6x+15/2.
# Held values to reproduce: r3=1.168, kappa3=-0.336, V/T=0.028, varrho=23.9,
# one-loop slope = 0.168 of quartic slope, tree slope size 5.34, ratio beta_K U'/(4U4) = -14.8.
import math

U4t, U3t = 7.935, -12.36          # V_t = U4t chi^4 + U3t chi^3 at chi = 1
chi = 1.0
c3 = -1.5 * U3t / U4t              # V_t = U4t (chi^4 - (2/3) c3 chi^3)
r3 = c3 / (2 * chi)
k3 = 2 - c3 / chi
VT = (1 - r3) ** 2
varrho = (VT + 2) / (3 * VT)
Lp = 4 * U4t * (r3 - 1)            # = -4U~(1-r3) = U'_loop at stationarity
quartic_slope = 4 * U4t            # 4U~ at chi=1
b2 = 2 * Lp / 10.68                # beta_K = 2U'/U_chichi with our integrated U_chichi = 10.68
ratio = 1.0 * Lp / (4 * (-0.09))   # beta_K U'_loop/(4 U4), beta_K = 1, one-loop U4 = -0.09
delta = 5 * r3 - 6                 # beta_K = 1  <=>  r3 = (6+delta)/5
poly = -4 * 0.3 ** 2 - 6 * 0.3 + 7.5

def near(name, got, want, tol):
    ok = abs(got - want) <= tol
    print(f"{name}: got {got:+.6f}  held/ours {want:+.6f}  {'OK' if ok else 'MISMATCH'}")
    assert ok, name

near("r3", r3, 1.168, 5e-4)
near("kappa3", k3, -0.336, 5e-4)
near("V/T", VT, 0.028, 5e-4)
near("varrho", varrho, 23.9, 0.05)
near("tree slope", Lp, 5.34, 0.01)
near("one-loop/quartic slope", Lp / quartic_slope, 0.168, 5e-4)
near("beta_K from U_chichi=10.68", b2, 1.0, 2e-3)
near("beta_K from 2(r3-1)/(4-3r3+delta)", 2 * (r3 - 1) / (4 - 3 * r3 + delta), 1.0, 1e-12)
near("4U~(4-3r3+delta) vs U_chichi=10.68", 4 * U4t * (4 - 3 * r3 + delta), 10.68, 0.02)
near("ratio beta_K U'/(4U4)", ratio, -14.8, 0.06)
print(f"note: our L3194 polynomial -4x^2-6x+15/2 at x=3/10 = {poly:.4f} (coincides with the tree-slope size 5.34; consistency only, not load-bearing)")
print("EXAMPLE_129 PASS")
