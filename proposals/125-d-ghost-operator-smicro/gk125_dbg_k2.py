import sys; sys.path.insert(0,'.')
from sympy import symbols, Function, Matrix, simplify, sin, cos, diff
exec(open('gk125_verify.py').read().split("t=symbols('t'); RES=[]")[0])
X=(symbols('th'),symbols('ph')); t=symbols('t')
met=Matrix.diag(1,sin(X[0])**2)
gi,G,Ric=geo(met,2)
for i,k in enumerate([[0,1],[-sin(X[1]),-cos(X[0])*cos(X[1])/sin(X[0])],[cos(X[1]),-sin(X[0])*cos(X[1])/sin(X[0])]]):
    L=lie(met,k,2); Ls=[[simplify(L[a,b]) for b in range(2)] for a in range(2)]
    br=[simplify(a+b) for a,b in zip(box(G,gi,k,2),ricv(gi,Ric,k,2))]
    dF=dFt(met,L,2,t)
    print("K%d Lie:"%i,Ls); print("K%d box+Ric:"%i,br); print("K%d dF:"%i,[simplify(v) for v in dF])
