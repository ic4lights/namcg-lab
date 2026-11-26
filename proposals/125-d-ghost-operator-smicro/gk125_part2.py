_src=open('gk125_verify.py').read().split("t=symbols('t'); RES=[]")[0]
exec(_src)
t=symbols('t'); RES=[]
# ---- GK4: flat polar counterexample, xi = x d_x --------------------------
X=(symbols('r'),symbols('ph')); r,ph=X
mP=Matrix.diag(1,r**2)
giP,GP,RP=geo(mP,2)
xiP=[r*cos(ph)**2,-sin(ph)*cos(ph)]   # x d_x in polar
bx=box(GP,giP,xiP,2)
rv=ricv(giP,RP,xiP,2)
dvp=sum(diff(xiP[a],X[a]) for a in range(2))+sum(GP[(a,b,a)]*xiP[b] for a in range(2) for b in range(2))
gd=[simplify(sum(giP[mu,a]*diff(simplify(dvp),X[a]) for a in range(2))) for mu in range(2)]
hP=lie(mP,xiP,2)
dF=dFt(mP,hP,2,t)
log("GK4 polar: div xi = %s ; graddiv = %s ; box = %s ; Ric.xi = %s"%(simplify(dvp),gd,bx,rv))
okz=all(z(v) for v in bx) and all(z(v) for v in rv) and all(z(v) for v in gd)
okd=all(not z(a-b) for a,b in zip(dF,[0,0]))
exp=[2*sin(ph)**2/r, 2*sin(2*ph)/r**2]
okm=all(z(a-b) for a,b in zip(dF,exp))
log("GK4 polar: tensorial-zero %s ; dF nonzero and matches proposal values: %s"%(okz,okm))
if not okm: log("GK4 dF = %s"%dF)
RES.append(okz); RES.append(okm)
# Cartesian same data
X=(symbols('x'),symbols('y'))
mC=Matrix.diag(1,1); giC,GC,RC=geo(mC,2)
hC=lie(mC,[X[0],0],2)
dFc=dFt(mC,hC,2,t)
log("GK4 cartesian: dF = %s"%dFc); RES.append(all(z(v) for v in dFc))
# chart-dependence witness: h polar vs transform of h cartesian
# ---- GK5: background-subtracted F~ ---------------------------------------
# (a) flat polar, Gbar nonzero: dF~(x d_x) must be 0 = box+Ric
dFt1=dFtilde(mP,hP,2,t,GP)
log("GK5a flat-polar dFtilde(x d_x) = %s"%dFt1); RES.append(all(z(v) for v in dFt1))
# (b) S^2, general xi(u,v): dF~ = box + Ric exactly
X=(symbols('th'),symbols('ph'))
met=Matrix.diag(1,sin(X[0])**2)
gi,G,Ric=geo(met,2)
u,v=Function('u')(*X),Function('v')(*X)
h=lie(met,[u,v],2)
dFt2=dFtilde(met,h,2,t,G)
bx2=box(G,gi,[u,v],2); rv2=ricv(gi,Ric,[u,v],2)
okb=all(z(a-b-c) for a,b,c in zip(dFt2,bx2,rv2))
log("GK5b S2 general xi: dFtilde == box+Ric exactly: %s"%("PASS" if okb else "FAIL")); RES.append(okb)
# (c) and the BARE dF differs from box+Ric by GT only:
dFb=dFt(met,h,2,t)
gt=GT(gi,G,h,2)
okc=all(z(a-b-c-g) for a,b,c,g in zip(dFb,bx2,rv2,gt))
log("GK5c S2 general xi bare: dF == box+Ric+GT: %s"%("PASS" if okc else "FAIL")); RES.append(okc)
print("GK PART2: %d/%d PASS"%(sum(RES),len(RES)))
