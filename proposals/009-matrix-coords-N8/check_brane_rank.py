"""
Linear response of the Poisson-limit operator metric to D matrix coordinates (4D symplectic brane in R^{1,D-1}).
Chart y with constant reference Poisson bivector theta (Tr -> int d^4y, so rho_y = const). Background data at a point (WKB):
induced metric gbar (Lorentzian), second fundamental forms II^i_{mu nu}, i=1..D-4 (normal modes), constant theta.
Operator inverse metric K = theta^T g theta, G = K^{-1}.
Perturbation delta x^I = A^I e^{i p.y}, A = xi^mu d_mu xbar + phi_i n_i  (D real amplitudes; the factor i absorbed in xi):
   delta g = p (.) (gbar xi) - 2 sum_i phi_i II^i,   a(.)b = a b^T + b a^T      [tangent: Lie derivative; normal: Weingarten]
   delta G = - G (theta^T delta g theta) G.
Gauge: Hamiltonian xi = theta^T p gives delta G = p (.) (G xi) = linearised G-diffeo.
Quantities: rank of the response map; dim(Im + Diff_G) - 4 = rank of the linearised Einstein operator of G on Im
(E annihilates Diff_G; max 6 = dim of conserved sources p^mu T_{mu nu}=0).  II either generic or K-traceless (normal part of
tree-level equation of motion  K^{mu nu} II^i_{mu nu} = 0).  Exact rational arithmetic.
"""
import sympy as sp, random
random.seed(21)
R = lambda: sp.Rational(random.randint(-5,5), random.randint(1,3))
eta = sp.diag(-1,1,1,1)
def rand_theta():
    while True:
        t=[R() for _ in range(6)]
        T=sp.Matrix([[0,t[0],t[1],t[2]],[-t[0],0,t[3],t[4]],[-t[1],-t[3],0,t[5]],[-t[2],-t[4],-t[5],0]])
        if T.det()!=0: return T
def rand_g():
    while True:
        A=sp.Matrix(4,4,lambda i,j:R())
        if A.det()!=0: return A.T*eta*A
def rand_sym():
    S=sp.zeros(4,4)
    for i in range(4):
        for j in range(i,4): S[i,j]=S[j,i]=R()
    return S
idx=[(i,j) for i in range(4) for j in range(i,4)]
vec=lambda h: [h[i,j] for (i,j) in idx]
def tomat(v):
    h=sp.zeros(4,4)
    for c,(i,j) in enumerate(idx): h[i,j]=h[j,i]=v[c]
    return h
odot=lambda a,b: a*b.T+b*a.T
def lin_einstein(h,gb,p):
    gi=gb.inv(); hu=gi*h; tr=hu.trace(); pu=gi*p; p2=(p.T*pu)[0]; ph=h*pu; pph=(pu.T*h*pu)[0]
    Ric=sp.Matrix(4,4,lambda a,b: sp.Rational(1,2)*(-ph[b]*p[a]-ph[a]*p[b]+p2*h[a,b]+p[a]*p[b]*tr))
    return Ric-sp.Rational(1,2)*gb*(-pph+p2*tr)
def run(D, mode):
    th=rand_theta(); g=rand_g(); p=sp.Matrix([R() for _ in range(4)])
    K=th.T*g*th; G=K.inv(); Ki=K  # K^{mu nu}
    IIs=[]
    for _ in range(D-4):
        S=rand_sym()
        if mode=="traceless":
            S=S-(sum(K[i,j]*S[i,j] for i in range(4) for j in range(4))/sum(K[i,j]*G[i,j] for i in range(4) for j in range(4)))*G
            assert sum(K[i,j]*S[i,j] for i in range(4) for j in range(4))==0
        if mode=="flat": S=sp.zeros(4,4)
        IIs.append(S)
    dG=lambda dg: -G*(th.T*dg*th)*G
    modes=[]
    for k in range(4):
        xi=sp.zeros(4,1); xi[k]=1
        modes.append(dG(odot(p,g*xi)))
    for S in IIs: modes.append(dG(-2*S))
    xiH=th.T*p
    gauge=dG(odot(p,g*xiH)); diffH=odot(p,G*xiH)
    gauge_ok=(gauge==diffH)
    Diff=[vec(odot(p,G*sp.Matrix([1 if i==k else 0 for i in range(4)]))) for k in range(4)]
    Im=[vec(m) for m in modes]
    rkIm=sp.Matrix(Im).rank()
    rkSum=sp.Matrix(Im+Diff).rank()
    # direct Einstein rank
    E=[vec(lin_einstein(m,G,p)) for m in modes]
    rkE=sp.Matrix(E).rank()
    return gauge_ok,rkIm,rkSum-4,rkE
print("D  mode       Hamiltonian-gauge=Diff_G | rank(Im) | dim(Im+Diff)-4 | rank E on Im   (max 6)")
for mode in ("flat","generic","traceless"):
    for D in range(4,12):
        a,b,c,d=run(D,mode)
        print("%2d %-9s %s | %d | %d | %d"%(D,mode,a,b,c,d))
