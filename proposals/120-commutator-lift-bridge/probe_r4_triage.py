import sys
import sympy as sp

mode = sys.argv[1] if len(sys.argv) > 1 else "fast"


def cmat(n, tag):
    R = sp.Matrix(n, n, lambda i, j: sp.Symbol("R" + tag + str(i) + str(j), real=True))
    Ii = sp.Matrix(n, n, lambda i, j: sp.Symbol("I" + tag + str(i) + str(j), real=True))
    return R + sp.I * Ii


def Cfun(M):
    return sp.expand(M * M.adjoint() - M.adjoint() * M)


def Wfun(M):
    C = Cfun(M)
    return sp.expand((C.adjoint() * C).trace())


Phi2 = cmat(2, "a")
W2 = Wfun(Phi2)

zz = sp.Matrix(2, 2, lambda i, j: sp.Symbol("z" + str(i) + str(j), complex=True))
zzd = sp.Matrix(2, 2, lambda i, j: sp.Symbol("c" + str(i) + str(j), complex=True))
zl = [zz[i, j] for i in range(2) for j in range(2)]
dl = [zzd[i, j] for i in range(2) for j in range(2)]
CJ = {}
CJ.update({zl[k]: dl[k] for k in range(4)})
CJ.update({dl[k]: zl[k] for k in range(4)})


def cJ(e):
    return sp.expand(e.xreplace(CJ))


ss = sp.Symbol("ss", complex=True)
ssc = sp.Symbol("cc", complex=True)
VS10 = zl + dl + [ss, ssc]
SHall = {}
SHall.update({zl[k]: zl[k] + ss for k in range(4)})
SHall.update({dl[k]: dl[k] + ssc for k in range(4)})
SHdia = {}
SHdia.update({zl[0]: zl[0] + ss, zl[3]: zl[3] + ss, dl[0]: dl[0] + ssc, dl[3]: dl[3] + ssc})


def polyvec(expr, smap=None):
    sm = {}
    sm.update({zl[k]: VS10[k] for k in range(4)})
    sm.update({dl[k]: VS10[4 + k] for k in range(4)})
    sm[ss] = VS10[8]
    sm[ssc] = VS10[9]
    return sp.Poly(sp.expand(expr).xreplace(sm), *VS10)


def nulltest(family, SH):
    rows = [polyvec(sp.expand(q.xreplace(SH) - q)) for q in family]
    mons = sorted(set().union(*[set(r.monoms()) for r in rows]))
    Mx = sp.Matrix(len(rows), len(mons), lambda i, j: rows[i].coeff_monomial(mons[j]))
    return Mx.nullspace()


Pw = zz
Pd = zzd.T
trP = Pw.trace()
trPd = Pd.trace()
trP2 = (Pw * Pw).trace()
trPd2 = (Pd * Pd).trace()
trX = (Pd * Pw).trace()
w1 = sp.expand((Pw ** 4).trace())
w2 = sp.expand((Pw ** 3 * Pd).trace())
w3 = sp.expand((Pw * Pw * Pd * Pd).trace())
w4 = sp.expand((Pw * Pd * Pw * Pd).trace())
QUAD = [sp.expand(trX), sp.expand((trP2 + trPd2) / 2), sp.expand((trP2 - trPd2) / (2 * sp.I)),
        sp.expand(trP * trPd), sp.expand((trP * trP + trPd * trPd) / 2),
        sp.expand((trP * trP - trPd * trPd) / (2 * sp.I))]
QUAR = [sp.expand((w1 + cJ(w1)) / 2), sp.expand((w1 - cJ(w1)) / (2 * sp.I)),
        sp.expand((w2 + cJ(w2)) / 2), sp.expand((w2 - cJ(w2)) / (2 * sp.I)),
        w3, w4, sp.expand(w2 * cJ(w2)),
        sp.expand(trX * (trP2 + trPd2) / 2), sp.expand(trX * (trP2 - trPd2) / (2 * sp.I)),
        sp.expand(trX * trP * trPd), sp.expand(trP * trPd * trP * trPd),
        sp.expand((trP ** 4 + cJ(trP ** 4)) / 2), sp.expand((trP ** 4 - cJ(trP ** 4)) / (2 * sp.I)),
        sp.expand((trP2 * trPd2 + cJ(trP2 * trPd2)) / 2),
        sp.expand((trP ** 2 * trP2 + cJ(trP ** 2 * trP2)) / 2),
        sp.expand((trP ** 2 * trP2 - cJ(trP ** 2 * trP2)) / (2 * sp.I))]
W1c = sp.expand(2 * w4 - 2 * w3)
W1bug = sp.expand(2 * w4 - w3 - w2 - cJ(w2))

if mode == "fast":
    # P0: numeric word-identity triage (T6h)
    def Wnum(M):
        C = M * M.conjugate().transpose() - M.conjugate().transpose() * M
        return sp.expand((C.conjugate().transpose() * C).trace())

    Ms = [sp.Matrix([[1, 2 * sp.I], [3 - sp.I, -1]]), sp.Matrix([[0, 5], [0, 0]]),
          sp.Matrix([[1 + sp.I, 2], [2 * sp.I, 3 - sp.I]]), sp.Matrix([[1, 0], [0, 2]]),
          sp.Matrix([[1, 2], [0, 1]])]
    for k, M in enumerate(Ms):
        P = M
        Pdx = M.conjugate().transpose()
        _w2 = sp.expand((P * P * P * Pdx).trace())
        _w3 = sp.expand((P * P * Pdx * Pdx).trace())
        _w4 = sp.expand((P * Pdx * P * Pdx).trace())
        lhs = 2 * _w4 - 2 * _w3
        rhs = Wnum(M)
        chkv = sp.expand(2 * _w4 - _w3 - _w2 - sp.conjugate(_w2))
        print("P0", k, "2w4-2w3==W1:", sp.simplify(lhs - rhs) == 0,
              "buggyform==W1:", sp.simplify(chkv - rhs) == 0, flush=True)

    # P1: T7c normalized unitary (real-parameter U(2))
    a1, a2, a3, a4 = sp.symbols("a1 a2 a3 a4", real=True)
    al = a1 + sp.I * a2
    be = a3 + sp.I * a4
    U2g = sp.Matrix([[al, be], [-sp.conjugate(be), sp.conjugate(al)]])
    norm = a1 ** 2 + a2 ** 2 + a3 ** 2 + a4 ** 2
    U = (1 / sp.sqrt(norm)) * U2g
    Pg = cmat(2, "g")
    d1 = sp.expand((U * Pg).adjoint() * (U * Pg) - Pg.adjoint() * Pg)
    print("P1 normalized-U X-preserving:", all(x == 0 for x in d1), flush=True)
    d0 = sp.expand((U2g * Pg).adjoint() * (U2g * Pg) - Pg.adjoint() * Pg)
    print("P1 unnormalized-U nonzero (as verifier coded):", not all(x == 0 for x in d0), flush=True)

    # P2: symbolic T6h identity in real/imag form
    SMR = {}
    SMR.update({zl[(2 * i + j)]: Phi2[i, j] for i in range(2) for j in range(2)})
    SMR.update({dl[(2 * i + j)]: sp.conjugate(Phi2[i, j]) for i in range(2) for j in range(2)})

    def to_ri(e):
        return sp.expand(e.xreplace(SMR))

    print("P2 corrected 2w4-2w3 identity:", sp.expand(to_ri(W1c) - W2) == 0, flush=True)
    print("P2 buggy-word identity:", sp.expand(to_ri(W1bug) - W2) == 0, flush=True)

    # P3: shift maps
    print("P3 W1c inv scalar shift:", sp.expand(W1c.xreplace(SHdia) - W1c) == 0, flush=True)
    print("P3 W1c inv all-ones shift:", sp.expand(W1c.xreplace(SHall) - W1c) == 0, flush=True)
    ns4d = nulltest(QUAD, SHdia)
    print("P3 QUAD null dim scalar-shift:", len(ns4d), flush=True)
    for v in ns4d:
        print([str(x) for x in v.T.tolist()[0]], flush=True)
    ns4a = nulltest(QUAD, SHall)
    print("P3 QUAD null dim all-ones shift:", len(ns4a), flush=True)
    # traceless-part invariants outside family: span membership + invariance
    F1 = sp.expand((trP2 - trP * trP / 2) * cJ(trP2 - trP * trP / 2))
    F2 = sp.expand((trX - trP * trPd / 2) ** 2)
    print("P3 F1=|TrPhi~^2|^2 inv:", sp.expand(F1.xreplace(SHdia) - F1) == 0, flush=True)
    print("P3 F2=(TrPhi~dag Phi~)^2 inv:", sp.expand(F2.xreplace(SHdia) - F2) == 0, flush=True)
    nsF = nulltest([F1, F2], SHdia)
    print("P3 F1,F2 both null (dim2):", len(nsF) == 2, flush=True)
    q4 = QUAR[13] - QUAR[14] + QUAR[10] / 4
    print("P3 F1 == QUAR13-QUAR14+QUAR10/4:", sp.expand(F1 - q4) == 0, flush=True)
    sys.exit(0)

if mode == "heavy":
    ns = nulltest(QUAR + [W1c], SHdia)
    print("P4 QUAR+W1c scalar-shift null dim:", len(ns), flush=True)
    for v in ns:
        print([str(x) for x in v.T.tolist()[0]], flush=True)
    nsa = nulltest(QUAR + [W1c], SHall)
    print("P4b QUAR+W1c all-ones null dim:", len(nsa), flush=True)
    print("ALL PROBE DONE", flush=True)
