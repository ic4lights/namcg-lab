"""X1b. FLRW-type isotropic torsion ansatz on R x SU(2) / R x R^3 (see x1_isotropic.py). Run: python -I x1b_flrw.py"""
import sympy as sp, itertools
t=sp.symbols('t',real=True); kap,s=sp.symbols('kappa s',real=True)
a=sp.Function('a')(t); al=sp.Function('alpha')(t); be=sp.Function('beta')(t)
eta=sp.diag(s,1,1,1); etai=sp.diag(1/s,1,1,1)
R4=range(4)
def ed(x,f): return sp.diff(f,t) if x==0 else 0
eps=lambda i,j,k: sp.LeviCivita(i,j,k)
C=[[[0]*4 for _ in R4] for _ in R4]
for i in (1,2,3):
  C[0][i][i]=-sp.diff(a,t)/a; C[i][0][i]=sp.diff(a,t)/a
  for j in (1,2,3):
    for k in (1,2,3): C[i][j][k]=kap/a*eps(i-1,j-1,k-1)
W=[[[0]*4 for _ in R4] for _ in R4]
for i in (1,2,3):
  for j in (1,2,3):
    for k in (1,2,3): W[i][j][k]+=al*eps(i-1,j-1,k-1)
  W[i][0][i]+=be; W[i][i][0]-=be
Om=[[[sum(W[x][c][d]*eta[d,b] for d in R4) for c in R4] for b in R4] for x in R4]
T=[[[-C[x][b][c]-Om[x][b][c]+Om[b][x][c] for c in R4] for b in R4] for x in R4]
R=[[[[ed(x,Om[b][c][f])-ed(b,Om[x][c][f])+sum(Om[x][c][d]*Om[b][d][f]-Om[b][c][d]*Om[x][d][f]-C[x][b][d]*Om[d][c][f] for d in R4) for f in R4] for c in R4] for b in R4] for x in R4]
Rup=[[[[sum(eta[c,e]*R[x][b][c][f] for c in R4) for e in R4] for f in R4] for b in R4] for x in R4]
def nT(x,A,b,e): return ed(x,T[A][b][e])+sum(Om[x][A][z]*T[z][b][e]+Om[x][b][z]*T[A][z][e]-Om[x][z][e]*T[A][b][z] for z in R4)
def nR(x,A,b,d,e): return ed(x,Rup[A][b][d][e])+sum(Om[x][A][z]*Rup[z][b][d][e]+Om[x][b][z]*Rup[A][z][d][e]-Om[x][z][d]*Rup[A][b][z][e]-Om[x][z][e]*Rup[A][b][d][z] for z in R4)
B1=sp.Matrix(4,4,lambda b,e: sp.simplify(sum(-etai[x,A]*nT(x,A,b,e) for x in R4 for A in R4)+sum(T[A][b][c]*etai[A,x]*T[x][c][e] for A in R4 for c in R4 for x in R4)+sum(Rup[A][b][A][e] for A in R4)))
print("B1 diagonal:", [sp.factor(B1[i,i]) for i in range(4)], "off-diagonal zero:", all(B1[i,j]==0 for i in range(4) for j in range(4) if i!=j))
for b in R4:
  for d,e in itertools.combinations(R4,2):
    v=sp.simplify(sum(etai[x,A]*nR(x,A,b,d,e) for x in R4 for A in R4)-sum(T[A][b][c]*etai[A,x]*Rup[x][c][d][e] for A in R4 for c in R4 for x in R4))
    if v!=0: print((b,d,e),sp.factor(v))
print('trace T',[sp.simplify(sum(T[A][c][c] for c in R4)) for A in R4])
# LC check: torsion zero?
