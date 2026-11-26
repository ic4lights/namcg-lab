"""
065 s4: row length of the cap edge irrep on the round fuzzy sphere X^a = nu J^a for Gaussian momentum states.

Scalar proxy state: each of the three momentum matrices Pi^a is an independent Hermitian Gaussian with covariance
f(l) on the spin-l subspace of Mat_N (l <= Lam, the coarse-graining of arXiv:2408.05274 Eq. (3.11)), 0 above.
With X^a_{SS'} = c^a |u)(v| (s2), sum_a |c^a|^2 = s^2 = nu^2 M(N-M)/2, and s3, the classicalised row length is
ell = 2|w_perp|, so  <ell^2> = 4 s^2 W_perp,  W_perp = sum_{j<M, j != M-1} <|Pi_{M j}|^2>.
Checks:
 (i) sum_j <|Pi_{ij}|^2> over a full row equals (1/N) sum_l (2l+1) f(l) for every row i (Schur; exact);
 (ii) W_perp as a function of M (latitude of the cap) and Lam;
 (iii) f(l) = nu l / 2 (Gaussian ground state of frequencies nu|omega_l| ~ nu l, the state of 2408.05274) gives
       <ell^2> -> nu^3 Lam^3 M(N-M)/(3N), the value implied by Eq. (3.14) [eqn:cap-ee] of 2408.05274;
 (iv) f(l) = kappa_l / 4 with kappa_l = l(l+1) (square root of a Gaussian weight exp(-1/2 sum kappa x^2)) gives
       a different power of Lam: W_perp -> Lam^4 / (16N).
Output to stdout only.
"""
import numpy as np
import scipy.sparse as sp

def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    jm = jp.conj().T
    return [(jp + jm) / 2, (jp - jm) / (2j), j3]

def offset_spectra(N):
    J = su2(N)
    I = sp.identity(N, format='csr', dtype=complex)
    C = None
    for Ja in J:
        A = sp.csr_matrix(Ja)
        ad = sp.kron(A, I) - sp.kron(I, A.T)
        C = ad @ ad if C is None else C + ad @ ad
    C = C.tocsr()
    spec = {}
    for k in range(-(N - 1), N):
        # entries (r, c) with r - c = k ; row-major index r*N + c
        if k >= 0:
            idx = [(i + k) * N + i for i in range(N - k)]
        else:
            idx = [i * N + (i - k) for i in range(N + k)]
        sub = C[idx][:, idx].toarray()
        lam, V = np.linalg.eigh((sub + sub.conj().T) / 2)
        l = np.rint((-1 + np.sqrt(1 + 4 * np.clip(lam.real, 0, None))) / 2).astype(int)
        assert np.allclose(l * (l + 1), lam.real, atol=1e-6)
        spec[k] = (idx, l, np.abs(V) ** 2)
    return spec

def entry_var(spec, N, f, Lam):
    """D[(r,c)] = sum_{l<=Lam} f(l) <E_rc, P_l E_rc>"""
    D = np.zeros((N, N))
    for k, (idx, l, W2) in spec.items():
        wts = np.where(l <= Lam, f(l), 0.0)
        vals = W2 @ wts
        for t, ii in enumerate(idx):
            D[ii // N, ii % N] = vals[t]
    return D

import sys
for N in (160, 400):
  spec = offset_spectra(N)
  print('N =', N)
  nu = 1.0
  f_gs = lambda l: nu * l / 2.0
  f_sq = lambda l: l * (l + 1) / 4.0
  for name, f, Lams in (('ground-state f = nu l/2', f_gs, (4, 8, 12, 16)), ('sqrt-measure f = l(l+1)/4', f_sq, (4, 8, 12, 16))):
      print('state:', name)
      for Lam in Lams:
          D = entry_var(spec, N, f, Lam)
          row = D.sum(axis=1)
          schur = sum((2 * l + 1) * f(l) for l in range(Lam + 1)) / N
          dev = np.abs(row - schur).max() / schur
          line = '  Lam=%2d  (i) row sums vs Schur value: max rel dev %.1e |' % (Lam, dev)
          assert dev < 1e-9
          for M in (N // 8, N // 4, N // 2, 3 * N // 4):
              Wp = D[M, :M].sum() - D[M, M - 1]
              ell2 = 4 * (nu ** 2 * M * (N - M) / 2) * Wp
              if f is f_gs:
                  ref = nu ** 3 * Lam ** 3 * M * (N - M) / (3 * N)
                  line += ' M=%3d: ell^2/[nu^3 Lam^3 M(N-M)/3N]=%.4f' % (M, ell2 / ref)
              else:
                  ref = Lam ** 4 / (16 * N)
                  line += ' M=%3d: W_perp/[Lam^4/16N]=%.4f' % (M, Wp / ref)
          print(line)

  # exponent fits in Lam at M = N/2
  print('power of Lam in W_perp at M=N/2 (fit over Lam = 8..16):')
  for name, f in (('ground-state', f_gs), ('sqrt-measure', f_sq)):
      Ls = np.arange(8, 17)
      Ws = []
      for Lam in Ls:
          D = entry_var(spec, N, f, Lam)
          M = N // 2
          Ws.append(D[M, :M].sum() - D[M, M - 1])
      p = np.polyfit(np.log(Ls), np.log(Ws), 1)[0]
      print('  %s: exponent %.3f' % (name, p))
print('DONE s4')

# larger cut-offs at N = 400 (Lam/N <= 0.1): local exponents and ratios at M = N/2
N = 400
spec = offset_spectra(N)
M = N // 2
print('N = 400, M = N/2, Lam = 20..40: ratios and local exponent d ln W_perp / d ln Lam')
for name, f, refL in (('ground-state', lambda l: l / 2.0, lambda L: L ** 3 / (6 * N)),
                      ('sqrt-measure', lambda l: l * (l + 1) / 4.0, lambda L: L ** 4 / (16 * N))):
    Ls = np.array([20, 24, 28, 32, 36, 40])
    Ws = np.array([(lambda D: D[M, :M].sum() - D[M, M - 1])(entry_var(spec, N, f, L)) for L in Ls])
    loc = np.diff(np.log(Ws)) / np.diff(np.log(Ls))
    print('  %s: W_perp/ref =' % name, ' '.join('%.4f' % (w / refL(L)) for w, L in zip(Ws, Ls)),
          '| local exponents', ' '.join('%.3f' % e for e in loc))
print('DONE s4 (extended)')
