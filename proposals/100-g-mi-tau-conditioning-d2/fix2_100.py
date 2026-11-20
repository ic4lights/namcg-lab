# fix2_100.py -- supersedes fix_100.py; sole byte authority for mi_tau_100q.py (v2) from mi_tau_100p.py.
# Line-prefix surgery. Fixes, each re-derived:
# (1) h(): p-file branch algebra wrong (small branch r/(1-e^-r), big branch missing
#     /(1-e^-r)). Correct stable truncated-exp entropy: -ln r + ln(1-e^-r) + 1 - r e^-r/(1-e^-r).
# (2) self-test constants: mpmath-dps30 values h(3) = -0.3068685590845791.
# (3) Gamma-posterior z-quadrature: scipy roots_genlaguerre overflows at n>=200 (NaN Eh);
#     replaced by Gauss-Legendre on z in [0,60] with weight exp((al-1)ln z - z - lnGamma(al)).
# (4) lnNu (route B): f(tau|u) = tau^(al-2)(e^-L0tau-e^-L1tau)/Nq, Nq = Gamma(al-1)*(L0^(1-al)-
#     L1^(1-al)) -- the 1/|w| in f(tau|u) cancels against the x-integral normalisation (checked
#     two ways: marginalising Gamma(2M,Lambda(x)) over f(x|u), and integrating e^-tau*Lambda directly).
#     So lnNu = gammaln(al-1)+ln(L0^(1-al)-L1^(1-al)) with NO /|w| (the p-file's /Wv was the
#     route-B bug) and with a small-W series branch lnD = ln(al-1)-al*ln(a/2)+lnW.
# (5) Elnq row: drop float() -- np.sum(...,1) is per-x vector; shape (nu,nx) matches Lm.
# p-file KL line (32) is already the exact E_Gamma[ln p - ln q] and is KEPT untouched.
import hashlib, pathlib
base = pathlib.Path(__file__).resolve().parent
src = (base / "mi_tau_100p.py").read_bytes()
nl = b"\r\n" if b"\r\n" in src else b"\n"
lines = src.split(nl)
def find(pref):
    idx = [i for i, l in enumerate(lines) if l.startswith(pref)]
    assert len(idx) == 1, "prefix %r found %d times" % (pref, len(idx))
    return idx[0]
i = find(b"    le = np.where(big")
assert lines[i+1].startswith(b"    rq = np.where(big")
assert lines[i+2].startswith(b"    return np.where(r < 1e-6")
lines[i:i+3] = [b"    return np.where(r < 1e-6, -(r**2)/24.0 + (r**4)/960.0,"
                b" np.log(emr) - np.log(r) + 1.0 - r*er/emr)"]
j = find(b"    assert abs(h(1e-3)")
lines[j] = (b"    assert abs(h(1e-3)+(1e-3)**2/24) < 1e-12 and "
            b"abs(h(2e-4)+(2e-4)**2/24) < 1e-14 and abs(h(3.)+0.3068686) < 5e-7")
q = find(b"    zt, wt = roots_genlaguerre")
lines[q] = (b"    wz, zz = gl(nt, 0, 60); zt = zz;"  # gl returns (weights, nodes)!"
            b" wt = wz*np.exp((al-1)*np.log(zt)-zt-gammaln(al))")
k = find(b"    lnNu = gammaln(al-1)")
lines[k] = (b"    with np.errstate(divide='ignore'):"
            b"        lnNu = gammaln(al-1)+np.where(Wv > 1e-6,"
            b" np.log((a/2-Wv/2)**(1-al)-(a/2+Wv/2)**(1-al)),"
            b" np.log(al-1)-al*np.log(a/2)+np.log(Wv))")
p = find(b"    Elnq = np.array([float(")
lines[p] = (b"    Elnq = np.array([np.sum(wt*np.log(np.maximum(-np.expm1("
            b"-Wv[i]*zt/Lm[i, :, None]), 1e-300)), 1) for i in range(nu)])")
out = nl.join(lines)
(base / "mi_tau_100q.py").write_bytes(out)
print("bytes=%d sha256=%s eol=%s lines=%d"
      % (len(out), hashlib.sha256(out).hexdigest(), "CRLF" if nl == b"\r\n" else "LF",
         len(lines)))
