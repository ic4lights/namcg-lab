"""Algebraic structure of the contact-completed log coefficient at (N_s,n_D)=(6,2), tested at RANDOM closed omega = dA (generic, non-chiral, J != 0).
 s24   = 029 assembly (direct sector sum, including the geometric R_Sigma, W pieces)         [24 pi units]
 CB    = log cross term of Q=1/4 uniform E_delta on the eight bosonic components (6 scalars, 4 vector, -2 ghosts), E_delta = -pi (1-n) d_S
 COm   = tr_V(J Omega^v_12)           (curvature delta of the connection bundle, J = rotation in the internal normal plane)
 claims: s24 + CB = -tau ;  COm = tau (so(4) representation theory) ; hence s24 + CB + COm = 0 for ANY Poisson bivector."""
import sys, random
import sympy as sp
from common import *
import jetlib as jl
from jetlib import Jet
import sector_data as S
use_gaussian(3)
def random_A_jets(seed, deg=4):
    random.seed(seed)
    A = []
    for mu in range(4):
        d = {}
        import itertools
        for mon in itertools.product(range(deg + 1), repeat=4):
            if 1 <= sum(mon) <= jl.N + 1:
                if random.random() < 0.5:
                    d[mon] = Q(random.randint(-3, 3), random.randint(1, 3))
        A.append(Jet({k: v for k, v in d.items() if not jl.isz(v)}))
    return A
for seed in range(int(sys.argv[1]) if len(sys.argv) > 1 else 3):
    A = random_A_jets(seed)
    # add a constant background omega_bar so that Pf != 0
    wb = jl.mm  # placeholder to avoid unused import warning
    w = omega_from_A(A)
    base = [[Q(0), Q(2), Q(1), Q(0)], [Q(-2), Q(0), Q(0), Q(1)], [Q(-1), Q(0), Q(0), Q(3)], [Q(0), Q(-1), Q(-3), Q(0)]]
    w = [[w[m][n] + Jet.const(base[m][n]) for n in range(4)] for m in range(4)]
    d = S.run_jets(w)
    R, Rii, Rj, e = d['R'], d['Rii'], d['Rijij'], d['e']
    W = Rj - Rii + R/3
    trEv = -d['trEv_G']; trEf = -d['trEf_G']
    Rsig = R - 2*Rii + Rj
    s24 = sp.Rational(8, 6)*R - (4*e + trEv) + R - trEf - d['tau'] - Rj - Rsig + 2*W
    CB_sectors = (-R + 6*e) + (-(R + sp.Rational(3, 2)*d['trEv_G']))           # scalars+ghosts , vector
    COm = d['trJOm_v']
    print('seed', seed, ' e-R/6=', sp.simplify(e - R/6), ' J!=0 generic')
    print('   s24 + CB + tau           =', sp.simplify(s24 + CB_sectors + d['tau']), ' (claim 0)')
    print('   COm - tau                =', sp.simplify(COm - d['tau']), ' (claim 0)')
    print('   total s24 + CB + COm     =', sp.simplify(s24 + CB_sectors + COm))
    print('   Hodge-distribution total =', sp.simplify(s24 + (-R + 6*e) + (-(R + 3*d['trN_EG'])) + COm), ' (differs from uniform when tr_N E_G != tr E_G/2)')
    sys.stdout.flush()
