# Proposal 113 (Problem E, thimble side) verification script.
# Run: python -I t13_thimble_checks.py
# Conventions: A_mu = x^a_mu sigma^a; S_b[h] = -1/4 h^{ma}h^{nb}Tr[C_mn C_ab],
# C_mn=[A_m,A_n]; red(X,h) = ((trG)^2-tr G^2)/8, G_ab = h(x^a,x^b)
# (manuscript L1775 form up to the constant k checked in r1).
import numpy as np
rng = np.random.default_rng(113)
S1 = np.array([[0,1],[1,0]],dtype=complex)
S2 = np.array([[0,-1j],[1j,0]],dtype=complex)
S3 = np.array([[1,0],[0,-1]],dtype=complex)
SG = [S1,S2,S3]
def direct(A,h0):
    C = {}
    for m in range(10):
        for n in range(10):
            if m!=n: C[(m,n)] = A[m]@A[n]-A[n]@A[m]
    keys = list(C); full = 0j
    for (m,n) in keys:
        Cmn = C[(m,n)]
        for (a,b) in keys:
            w = h0[m,a]*h0[n,b]
            if w!=0: full += w*np.trace(Cmn@C[(a,b)])
    return -full/4.0
def red(X,h0):
    G = X@h0@X.T; e1 = np.trace(G)
    return (e1*e1-np.trace(G@G))/8.0
def randX():
    return rng.standard_normal((3,10))+1j*rng.standard_normal((3,10))
def XtoA(X):
    return [sum(X[a,mu]*SG[a] for a in range(3)) for mu in range(10)]
def critres(X,h0):
    G = X@h0@X.T; e1 = np.trace(G)
    return np.max(np.abs(e1*X - G@X))
eta = np.diag([-1.]+[1.]*9); dl = np.eye(10)
def report(tag, passed, extra=""):
    print(f"{tag}: {'PASS' if passed else 'FAIL'} {extra}")
print("BEGIN 113 thimble checks")
# r1: proportionality direct = k*red for h0 = eta, 1, L^T eta L
hens = [eta, dl]
Lr = rng.standard_normal((10,10))+1j*rng.standard_normal((10,10))
hens.append(Lr.T@eta@Lr)
errs=[]; ks=[]
for h0 in hens:
    X=randX(); k=direct(XtoA(X),h0)/red(X,h0); ks.append(k); e=0.0
    for _ in range(3):
        X=randX()
        e=max(e,abs(direct(XtoA(X),h0)-k*red(X,h0))/max(1.0,abs(k*red(X,h0))))
    errs.append(e)
k_eta = ks[0]
report("r1", max(errs)<1e-8, f"k(eta)={k_eta:.6g} errs={[f'{e:.1e}' for e in errs]}")
# r2: critical equation e1 X = G X ; cone and null branch critical, rank-2 not
w = rng.standard_normal(3)+1j*rng.standard_normal(3)
z = rng.standard_normal(10)+1j*rng.standard_normal(10)
Xcone = np.outer(w,z)
Xnull = np.zeros((3,10),dtype=complex)
Xnull[0] = rng.standard_normal(10)+1j*rng.standard_normal(10); Xnull[1] = -1j*Xnull[0]
Xr2 = np.zeros((3,10)); Xr2[0,0]=1.0; Xr2[1,1]=1.0
Xrnd = randX()
vals = [critres(Xcone,eta), critres(Xnull,dl), critres(Xr2,dl), critres(Xrnd,dl)]
r2ok = vals[0]<1e-9 and vals[1]<1e-9 and vals[2]>1e-3 and vals[3]>1e-3
r2b = abs(red(Xcone,eta))<1e-12 and abs(red(Xnull,dl))<1e-12
report("r2", r2ok and r2b, f"critres cone={vals[0]:.1e} null={vals[1]:.1e} rank2={vals[2]:.2f} rand={vals[3]:.2f} S_crit={abs(red(Xcone,eta)):.1e}")
# r3: congruence equivariance of the critical set: (X,eta) ~ (X L^T,(L^T)^-1 eta L^-1)
Xc = Xcone
Lm = np.eye(10)+0.3*(rng.standard_normal((10,10))+1j*rng.standard_normal((10,10)))
Linv = np.linalg.inv(Lm)
h2 = Linv.T@eta@Linv
X2 = Xc@Lm.T
r3ok = critres(Xc,eta)<1e-9 and critres(X2,h2)<1e-6
Xrc = randX(); Xrc2 = Xrc@Lm.T
r3b = critres(Xrc,eta)>1e-3 and critres(Xrc2,h2)>1e-6
report("r3", r3ok and r3b, f"crit cone both={critres(X2,h2):.1e} rand both nonzero")
# r4: H(phi) = Re(i S_b[(e^{i phi}t, x)]) = k_eta*C/4*sin(2 phi), C>=0
Xr = rng.standard_normal((3,10)); t = Xr[:,0].copy(); Xs = Xr[:,1:10]
Gs = Xs@Xs.T; s0 = np.trace(Gs); t0 = t@t
Cval = s0*t0 - t@Gs@t
Xm = Xr.astype(complex).copy(); Xm[:,0]*= np.exp(0.6j)
Hnum = np.real(1j*direct(XtoA(Xm),eta))
pred = k_eta*Cval*np.sin(1.2)/4.0
X0 = Xr.astype(complex)
H0 = np.real(1j*direct(XtoA(X0),eta))
r4ok = abs(Hnum-pred)<1e-8*max(1.0,abs(pred)) and abs(H0)<1e-10 and Cval>=-1e-10
# damping on the clockwise ray phi in (-pi/2,0): H<0 when C>0
Xc2 = Xr.astype(complex).copy(); Xc2[:,0]*= np.exp(-0.7j)
Hcw = np.real(1j*direct(XtoA(Xc2),eta))
report("r4", r4ok and (Hcw<0 if Cval>0 else True), f"C={Cval:.4f} H(0.6)err={abs(Hnum-pred):.1e} H0={H0:.1e} Hcw={Hcw:.4f}")
# r5: Euler identity 4 S = 1/2 sum_a h(x^a, e1 x^a - sum_b G_ab x^b) (quartic)
Xe = randX(); Ge = Xe@eta@Xe.T; e1e = np.trace(Ge)
Vv = e1e*Xe - Ge@Xe
lhs = 4.0*red(Xe,eta); rhs = 0.5*np.einsum('am,mn,an->',Xe,eta,Vv)
report("r5", abs(lhs-rhs)<1e-9*max(1.0,abs(lhs)), f"|4S-sum x dS|={abs(lhs-rhs):.1e}")
print("END 113 thimble checks")
