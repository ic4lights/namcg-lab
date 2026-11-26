# --- I2: pure connector at O(l): eta w_r antisymmetric
def sym(M):
    return sp.simplify((M + M.T) / 2)
def antisym(M):
    return sp.simplify((M - M.T) / 2)

ok2 = all(sym(eta*w[r-1]) == sp.zeros(4) for r in range(1, 5))
ck("I2 sym(eta w_r) = 0 (O(l) connector pure gauge)", ok2)

# --- I3: d_s w_r pieces antisymmetric
ok3 = all(sym(eta*dw[(r, s)]) == sp.zeros(4)
          for r in range(1, 5) for s in range(1, 5))
ck("I3 sym(eta d_s w_r) = 0 (derivative part stays antisymmetric)", ok3)

# --- I4: soldering-type connector from {w_r, w_s} at O(l^2), generic nonzero
symm = sym(eta*(w[0]*w[1] + w[1]*w[0]))
ck("I4a sym(eta{w1,w2}) nonzero generically (soldering at O(l^2))",
   symm != sp.zeros(4))
print("I4 sym(eta{w1,w2}) sample nonzero entries:",
      [(i, j, symm[i, j]) for i in range(4) for j in range(4)
       if symm[i, j] != 0][:3])
num = symm.subs({R('w1', 0): 1, R('w2', 3): 1})
ck("I4b explicit: w1 = boost-x generator, w2 = rot generator, nonzero sym",
   any(num[i, j] != 0 for i in range(4) for j in range(4)))
# abelian single-generator subcase: w2 = c*w1 -> sym(eta{w1,w2}) = 2c sym(eta w1^2)
c1c = sp.symbols('c1c')
symab = sp.simplify(sym(eta*(w[0]*w[0])) * 2 * c1c)
sub12 = {}
for k in range(6):
    subsym = {R('w2', k): c1c*R('w1', k)}
symm_ab = symm.subs({R('w2', k): c1c*R('w1', k) for k in range(6)})
ck("I4c abelian subcase sym(eta{w,w}) nonzero (K_x^2 term)",
   symm_ab.subs({R('w1', 0): 1}) != sp.zeros(4))
