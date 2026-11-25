_src=open('gk125_verify.py').read().split("t=symbols('t'); RES=[]")[0]
exec(_src)
X=(symbols('th'),symbols('ph')); t=symbols('t')
met=Matrix.diag(1,sin(X[0])**2)
gi,G,Ric=geo(met,2)
k2=[cos(X[1]),-sin(X[0]) and -sin(X[1])*cos(X[0])/sin(X[0])]
L=lie(met,k2,2)
print("k2 =",k2)
print("Lie:",[[simplify(L[a,b]) for b in range(2)] for a in range(2)])
print("box+Ric:",[simplify(a+b) for a,b in zip(box(G,gi,k2,2),ricv(gi,Ric,k2,2))])
print("dF:",[simplify(v) for v in dFt(met,L,2,t)])
