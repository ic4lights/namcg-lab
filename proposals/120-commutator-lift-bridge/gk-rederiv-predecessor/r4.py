import sympy as sp, random
# FAST exact-integer sampling route for quadratic (6-dim family) and quartic (21 products)
random.seed(120)
def evalfam(pts):
    rows=[]
    return rows
import itertools
# symbolic invariant values at random integer (z,zbar independent integer) points
def Fvals(z, zb):
    # z, zb: lists of 4 ints, independent
    P=[[z[0],z[1]],[z[2],z[3]]]; Pd=[[zb[0],zb[2]],[zb[1],zb[3]]]
    def mm(A,B): return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],[A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
    X=mm(Pd,P); X2=mm(X,X)
    trP=z[0]+z[3]; trPd=zb[0]+zb[3]
    trX=X[0][0]+X[1][1]; trX2=X2[0][0]+X2[1][1]
    Pdd=mm(Pd,Pd); t=[v- (trX*sp.Rational(1,2) if i in(0,3) else 0) for i,v in enumerate([X[0][0],X[0][1],X[1][0],X[1][1]])]
    tt=[v- (trX/2 if i in(0,3) else 0) for i,v in enumerate([X[0][0],X[0][1],X[1][0],X[1][1]])]
    t=[[tt[0],tt[1]],[tt[2],tt[3]]]
    t2=mm(t,t)
    return [trX, trX2, trP**2, trPd**2, trP*trPd, Pdd[0][0]+Pdd[1][1]], (trX, t2[0][0]+t2[1][1])
QUADNAMES=['TrX','TrX2','(TrP)^2','(TrPd)^2','TrP*TrPd','Tr(Pd^2)']
def shiftrows(Ffn, nf, sshift):
    # returns rows: for each sampled point and each (s,sb,ssb) direction, values of F(Phi+sI)-F(Phi)
    rows=[]
    for trial in range(60):
        z=[random.randint(-6,6) for _ in range(4)]
        zb=[random.randint(-6,6) for _ in range(4)]
        v0=Ffn(z,zb)
        ss=complex(random.randint(-3,3),0) if True else 0
        # s real=1:
        for s,sb in [(1,0),(0,1),(1,1),(2,3)]:
            z2=[zi+s for zi in z]; zb2=[zi+sb for zi in zb]
            v1=Ffn(z2,zb2)
            rows.append([sp.expand(a-b) for a,b in zip(v1,v0)])
    return sp.Matrix(rows)
M=shiftrows(lambda z,zb: Fvals(z,zb)[0], 6, None)
k=M.nullspace()
print('quad: M rank', M.rank(), 'kernel dim', len(k))
for v in k: print(' kernel vec', [x for x in v.T])
# quartic: all products qi qj of quad family + extra words
def Qvals(z,zb):
    q,_=Fvals(z,zb)
    out=[]
    for i in range(6):
        for j in range(i,6):
            out.append(sp.expand(q[i]*q[j]))
    return out
MQ=shiftrows(lambda z,zb: Qvals(z,zb), 21, None)
kQ=MQ.nullspace()
print('quartic products-21: rank', MQ.rank(), 'kernel dim', len(kQ))
# check W1 in kernel: W1 in terms of family: W1 = 2Tr(PPdPPd) - 2Tr(P^2 Pd^2): evaluate W1 at sample points and check linear dependence with kernel of shift-matrix of Qvals+[W1]
def W1val(z,zb):
    P=[[z[0],z[1]],[z[2],z[3]]]; Pd=[[zb[0],zb[2]],[zb[1],zb[3]]]
    def mm(A,B): return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],[A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
    C=[[-1,-1],[-1,-1]]
    PPd=mm(P,Pd); PdP=mm(Pd,P)
    C=[[PPd[0][0]-PdP[0][0],PPd[0][1]-PdP[0][1]],[PPd[1][0]-PdP[1][0],PPd[1][1]-PdP[1][1]]]
    C2=mm(C,C)
    return C2[0][0]+C2[1][1]
def QW(z,zb): return Qvals(z,zb)+[W1val(z,zb)]
MW=shiftrows(lambda z,zb: QW(z,zb), 22, None)
kW=MW.nullspace()
print('quartic21+W1: kernel dim', len(kW))
# is W1 independent of the products family? check rank of value-matrix (no shift): values at points
rowsV=[]
for trial in range(40):
    z=[random.randint(-6,6) for _ in range(4)]; zb=[random.randint(-6,6) for _ in range(4)]
    rowsV.append(Qvals(z,zb))
MV=sp.Matrix(rowsV)
rowsW=[]
for trial in range(40):
    z=[random.randint(-6,6) for _ in range(4)]; zb=[random.randint(-6,6) for _ in range(4)]
    rowsW.append(Qvals(z,zb)+[W1val(z,zb)])
MW2=sp.Matrix(rowsW)
print('W1 in span of products family?', MV.rank()==MW2.rank(), 'ranks', MV.rank(), MW2.rank())
