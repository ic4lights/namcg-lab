"""X1. Explored avenue: isotropic ansaetze (recorded in the proposal, not in the insert).
(a) flat frame, w_i = alpha J_i + beta K_i, w_0 = 0 (the most general SO(3)-invariant constant connection);
(b) FLRW-type frame on R x SU(2) (kappa != 0) or R x R^3 (kappa = 0), scale factor a(t), with
    isotropic alpha(t), beta(t).  Prints the first and second brackets (s = eta_00).
Run: python -I x1_isotropic.py"""
import sympy as sp, itertools
al,be,ga,de=sp.symbols('alpha beta gamma delta',real=True)
s=sp.symbols('s')  # eta00 sign
eta=sp.diag(s,1,1,1); etai=eta.inv()
R4=range(4)
def eps3(i,j,k): return sp.LeviCivita(i,j,k)
# W[a][c][d] = w_a^{cd}
W=[[[0]*4 for _ in R4] for _ in R4]
for i in (1,2,3):
  for j in (1,2,3):
    for k in (1,2,3):
      W[i][j][k]+= al*eps3(i-1,j-1,k-1)
  W[i][0][i]+=be; W[i][i][0]-=be
Om=[[[sum(W[a][c][d]*eta[d,b] for d in R4) for c in R4] for b in R4] for a in R4]
T=[[[ -Om[a][b][c]+Om[b][a][c] for c in R4] for b in R4] for a in R4]
R=[[[[sum(Om[a][c][d]*Om[b][d][f]-Om[b][c][d]*Om[a][d][f] for d in R4) for f in R4] for c in R4] for b in R4] for a in R4]
Rup=[[[[sum(eta[c,e]*R[a][b][c][f] for c in R4) for e in R4] for f in R4] for b in R4] for a in R4]
def nT(x,a,b,e): return sum(Om[x][a][z]*T[z][b][e]+Om[x][b][z]*T[a][z][e]-Om[x][z][e]*T[a][b][z] for z in R4)
def nR(x,a,b,d,e): return sum(Om[x][a][z]*Rup[z][b][d][e]+Om[x][b][z]*Rup[a][z][d][e]-Om[x][z][d]*Rup[a][b][z][e]-Om[x][z][e]*Rup[a][b][d][z] for z in R4)
B1=sp.Matrix(4,4,lambda b,e: sp.expand(sum(-etai[x,a]*nT(x,a,b,e) for x in R4 for a in R4)+sum(T[a][b][c]*etai[a,x]*T[x][c][e] for a in R4 for c in R4 for x in R4)+sum(Rup[a][b][a][e] for a in R4)))
print('B1=',sp.simplify(B1))
B2={}
for b in R4:
  for d,e in itertools.combinations(R4,2):
    v=sp.expand(sum(etai[x,a]*nR(x,a,b,d,e) for x in R4 for a in R4)-sum(T[a][b][c]*etai[a,x]*Rup[x][c][d][e] for a in R4 for c in R4 for x in R4))
    if v!=0: B2[(b,d,e)]=sp.factor(v)
print('B2=',B2)
print('trace T', [sp.simplify(sum(T[a][c][c] for c in R4)) for a in R4])
