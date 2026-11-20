# fix_100.py -- sole byte authority for mi_tau_100q.py from mi_tau_100p.py.
# Line-prefix surgery (each prefix verified unique). Five fixes:
# (1) h(): p-file branch algebra wrong -- small-r branch used r/(1-e^-r) (= e^r *
#     true r/(e^r-1)); big-r branch r*e^-r omitted /(1-e^-r). Correct stable form
#     rq = r*e^-r/(1-e^-r). So the p-file assert detected a real h() bug.
# (2) line-36 self-test constants -> mpmath-dps30 values of the FIXED h.
# (3)+(4) route-B KL: f(tau|u) ~ tau^(2M-1)(e^-L0t-e^-L1t)/N with
#     N = Gamma(2M)(L0^-2M-L1^-2M)/|w|; the p-file used the 2M-2 normalisation
#     gammaln(al-1)+log|(L0^(1-al)-L1^(1-al))/w|. With that correction the
#     (al-1)(psi(al)-ln L) terms cancel and KL = -al + al*Lmin/L - Elnq + lnNu.
# (5) Elnq row: float() dropped -- np.sum(...,1) is a per-x vector, not a scalar;
#     shape (nu,nx) matches Lm and lnNu[:,None].
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
k = find(b"    lnNu = gammaln(al-1)")
lines[k] = (b"    lnNu = gammaln(al)+np.log(np.maximum(((a/2-Wv/2)**(-al)-"
            b"(a/2+Wv/2)**(-al))/Wv, 1e-300))")
m = find(b"    KL = (al-1)*np.log(Lm)")
lines[m] = b"    KL = -al+al*(a/2-Wv[:, None]/2)/Lm+lnNu[:, None]-Elnq"
p = find(b"    Elnq = np.array([float(")
lines[p] = (b"    Elnq = np.array([np.sum(wt*np.log(np.maximum(-np.expm1("
            b"-Wv[i]*zt/Lm[i, :, None]), 1e-300)), 1) for i in range(nu)])")
out = nl.join(lines)
(base / "mi_tau_100q.py").write_bytes(out)
print("bytes=%d sha256=%s eol=%s lines=%d"
      % (len(out), hashlib.sha256(out).hexdigest(), "CRLF" if nl == b"\r\n" else "LF",
         len(lines)))
