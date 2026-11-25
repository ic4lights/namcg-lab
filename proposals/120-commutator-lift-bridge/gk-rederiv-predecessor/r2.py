import sympy as sp
x=sp.symbols('x1:9',real=True)
z=[x[k]+sp.I*x[k+4] for k in range(4)]
ZB=sp.symbols('u1:9',complex=True)
Pm=sp.Matrix([[z[0],z[1]],[z[2],z[3]]])
Pdb=sp.Matrix([[ZB[0],ZB[2]],[ZB[1],ZB[3]]])
X=Pdb*Pm
s,sb=sp.symbols('s sb',complex=True)
def tr(M): return sp.expand(sp.simplify(M.trace()))
TRP=tr(Pm); TRPd=tr(Pdb)
QUAD=[sp.expand(q) for q in [tr(X), tr(X*X), TRP**2, TRPd**2, TRP*TRPd, tr(Pdb*Pdb)]]
def dshift(F):
    Fs=F.subs({z[k]:z[k]+s for k in range(4)}).subs({ZB[k]:ZB[k]+sb for k in range(4)})
    return sp.Poly(sp.expand(Fs-F),s,sb)
mons=[(1,0),(0,1),(1,1),(2,0),(0,2)]
def shiftM(Fs):
    rows=[]
    for F in Fs:
        d=dshift(F)
        rows.append([d.coeff_monomial(s**a*sb**b) if (a,b) in d.monoms() else 0 for a,b in mons])
    return sp.Matrix(rows)
Mq=shiftM(QUAD)
print('quad M',Mq.shape,'rank',Mq.rank(),'left-null dim',len(Mq.T.nullspace()))
t=X-(tr(X)/2)*sp.eye(2)
g1=sp.expand(2*tr(X)-TRP*TRPd)
g2=sp.expand((TRP**2+TRPd**2)/2)
g2b=sp.expand((TRP**2-TRPd**2)/(2*sp.I))
g3=sp.expand(tr(t*t))
g4=sp.expand(tr((Pm-t).adjoint() if False else (Pdb-(TRPd/2)*sp.eye(2))*(Pm-(TRP/2)*sp.eye(2))))
for g,nm in [(g1,'2TrX-TrPTrPd'),(g2,'ReTrP^2'),(g2b,'ImTrP^2'),(g3,'Tr t^2'),(g4,'Tr td t')]:
    print(nm,'shift-inv:',dshift(g).is_zero,'| in family span?')
# express g1,g2,g2b in family basis
def coords(g,basis):
    # solve linear combo of QUAD = g by matching polynomial coeffs
    v=sp.Poly(sp.expand(g),*list(z)+list(ZB),domain='EX') if False else None
    A=[];b=[]
    monset=sp.Add(*[sp.sympify(1)])
    # coefficient vector over generators of R[z,zbar]: use Groebner-free: sample? do linear solve on coeffs dict
    gd=sp.Poly(sp.expand(g),*([e for e in z]+[e for e in ZB]))
    rows=[];rhs=[]
    for q in basis:
        qd=sp.Poly(sp.expand(q),*([e for e in z]+[e for e in ZB]))
        rows.append(qd)
    # manual: substitute numeric random points
    import random
    random.seed(3)
    pts=[]
    while len(pts)<6:
        pt={**{z[i]:complex(random.randint(-5,5),random.randint(-5,5)) for i in range(4)},
             **{ZB[i]:complex(random.randint(-5,5),random.randint(-5,5)) for i in range(4)}}
        pts.append(pt)
    M=sp.Matrix([[sp.N(q.subs(p)) for q in basis] for p in pts]).applyfunc(lambda e: complex(e))
    y=[complex(sp.N(g.subs(p))) for p in pts]
    Ms=sp.Matrix([[ [complex(sp.N(q.subs(p).as_real_imag()[0]),),0] for q in basis] for p in pts])
    return None
print('Tr X alone shift-variant:', not dshift(QUAD[0]).is_zero)
# intersection with X-functions span{TrX,TrX2,(TrX)^2}: any shift-inv combo? solve c0..c2 shift-invariant
MX=shiftM([QUAD[0],QUAD[1],QUAD[2]])
print('X-span left-null dim (expect 0):',len(MX.T.nullspace()))
