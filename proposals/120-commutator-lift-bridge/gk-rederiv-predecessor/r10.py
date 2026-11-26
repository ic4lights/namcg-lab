import sympy as sp, random
random.seed(5)
zz=sp.Matrix(2,2,lambda i,j: sp.Symbol("z%d_%d"%(i,j),complex=True))
zzd=sp.Matrix(2,2,lambda i,j: sp.Symbol("c%d_%d"%(i,j),complex=True))
zl=[zz[i,j] for i in range(2) for j in range(2)]; dl=[zzd[i,j] for i in range(2) for j in range(2)]
CJ={}; CJ.update({zl[k]:dl[k] for k in range(4)}); CJ.update({dl[k]:zl[k] for k in range(4)})
cJ=lambda e: sp.expand(e.xreplace(CJ))
ss=sp.Symbol("ss",complex=True); ssc=sp.Symbol("cc",complex=True)
Pw=zz; Pd=zzd.T
trP=Pw.trace(); trPd=Pd.trace(); trP2=(Pw*Pw).trace(); trPd2=(Pd*Pd).trace(); trX=(Pd*Pw).trace()
w1=sp.expand((Pw**4).trace()); w2=sp.expand((Pw**3*Pd).trace()); w3=sp.expand((Pw*Pw*Pd*Pd).trace()); w4=sp.expand((Pw*Pd*Pw*Pd).trace())
QUAR=[sp.expand((w1+cJ(w1))/2), sp.expand((w1-cJ(w1))/(2*sp.I)),
 sp.expand((w2+cJ(w2))/2), sp.expand((w2-cJ(w2))/(2*sp.I)),
 w3,w4,sp.expand(w2*cJ(w2)),
 sp.expand(trX*(trP2+trPd2)/2), sp.expand(trX*(trP2-trPd2)/(2*sp.I)),
 sp.expand(trX*trP*trPd), sp.expand(trP*trPd*trP*trPd),
 sp.expand((trP**4+cJ(trP**4))/2), sp.expand((trP**4-cJ(trP**4))/(2*sp.I)),
 sp.expand((trP2*trPd2+cJ(trP2*trPd2))/2),
 sp.expand((trP**2*trP2+cJ(trP**2*trP2))/2), sp.expand((trP**2*trP2-cJ(trP**2*trP2))/(2*sp.I))]
SH={}; SH.update({zl[0]:zl[0]+ss, zl[3]:zl[3]+ss, dl[0]:dl[0]+ssc, dl[3]:dl[3]+ssc})
print('family len', len(QUAR))
# numeric exact-integer rows: variables: z entries + c entries + (ss,cc) as (1,0),(0,1),(1,1),(i,0)
def val(expr, zp, cp, s, sb):
    d={}
    d.update({zl[k]: zp[k] for k in range(4)}); d.update({dl[k]: cp[k] for k in range(4)})
    d[ss]=s; d[ssc]=sb
    return sp.nsimplify(expr.xreplace(d))
rows=[]
for trial in range(40):
    zp=[random.randint(-5,6) for _ in range(4)]; cp=[random.randint(-5,6) for _ in range(4)]
    # complex-ify: treat z = a + i b with independent a,b: use two point sets and take re/im of combination? Use exact: z real + i*zimg via linearity is messy; instead take zp, cp as gaussians in Z[i]: evaluate with z = a + I*b via substitution into exprs with numeric complex:
    zc=[complex(random.randint(-5,6),random.randint(-5,6)) for _ in range(4)]
    cc=[complex(random.randint(-5,6),random.randint(-5,6)) for _ in range(4)]
    d0={}; d0.update({zl[k]:zc[k] for k in range(4)}); d0.update({dl[k]:cc[k] for k in range(4)})
    for s,sb in [(1,0),(0,1),(1,1),(1j,0),(0,1j)]:
        d1=dict(d0); d1.update({zl[0]:zc[0]+s, zl[3]:zc[3]+s, dl[0]:cc[0]+sb, dl[3]:cc[3]+sb})
        row=[]
        for q in QUAR:
            dv=complex(q.xreplace(d1))-complex(q.xreplace(d0))
            row.extend([dv.real,dv.imag])
        rows.append(row)
M=sp.Matrix(rows).applyfunc(lambda e: sp.nsimplify(e, rational=False))
M=M.applyfunc(lambda e: sp.Rational(str(round(float(e),6))) if e.__class__.__name__=='Float' else e) if False else M
Mr=sp.Matrix([[sp.Rational(int(round(float(x)*10**6)),10**6) if not sp.nsimplify(x).is_zero and isinstance(x,(float,)) else x for x in r] for r in M.tolist()]) if False else M
# do exact integer arithmetic instead: redo with gaussian integer points and exact arithmetic
rows2=[]
for trial in range(25):
    zq=[complex(random.randint(-4,5),random.randint(-4,5)) for _ in range(4)]
    cq=[complex(random.randint(-4,5),random.randint(-4,5)) for _ in range(4)]
    for s,sb in [(1,0),(0,1),(1,1),(1j,0),(0,1j),(-2,3j)]:
        row=[]
        for q in QUAR:
            d0={**{zl[k]:zq[k] for k in range(4)},**{dl[k]:cq[k] for k in range(4)}}
            d1={**{zl[k]:zq[k] for k in range(4)},**{dl[k]:cq[k] for k in range(4)},zl[0]:zq[0]+s,zl[3]:zq[3]+s,dl[0]:cq[0]+sb,dl[3]:cq[3]+sb}
            dv=sp.simplify(q.xreplace(d1)-q.xreplace(d0))
            row.extend([sp.re(dv),sp.im(dv)])
        rows2.append(row)
M2=sp.Matrix(rows2)
k2=M2.T.nullspace()
print('exact Gaussian-integer nullity:', len(k2))
for v in k2[:6]:
    print([sp.nsimplify(x) for x in v.T])
