import sympy as sp
from sympy import Rational as Q
from itertools import product

X = sp.symbols('x1:5', real=True)

def eta3():
    # 't Hooft symbols (self-dual): eta^i_{ab}=eps_{iab}, eta^i_{a4}=delta_{ia}, eta^i_{4b}=-delta_{ib}
    out = []
    for i in range(3):
        M = sp.zeros(4, 4)
        for a in range(3):
            for b in range(3):
                M[a, b] = sp.LeviCivita(i, a, b)
            M[a, 3] = 1 if a == i else 0
            M[3, a] = -1 if a == i else 0
        out.append(M)
    return out

def etabar():
    out = []
    for i in range(3):
        M = sp.zeros(4, 4)
        for a in range(3):
            for b in range(3):
                M[a, b] = sp.LeviCivita(i, a, b)
            M[a, 3] = -1 if a == i else 0
            M[3, a] = 1 if a == i else 0
        out.append(M)
    return out

def pf4(w):
    return w[0, 1]*w[2, 3] - w[0, 2]*w[1, 3] + w[0, 3]*w[1, 2]

def hodge(w):
    # (*w)_{mn} = 1/2 eps_{mnrs} w_{rs}
    H = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            s = 0
            for r in range(4):
                for t in range(4):
                    s += sp.LeviCivita(m, n, r, t)*w[r, t]
            H[m, n] = s/2
    return H

def inv_antisym(w):
    # w * (-(*w)/Pf) = 1  (verified in checks)
    P = pf4(w)
    return -hodge(w)/P
