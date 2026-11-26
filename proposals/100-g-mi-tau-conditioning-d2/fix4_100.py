# fix4_100.py -- sole byte authority for rederive_100.py v2. v1 bug found by isolation:
# Itau_u returned nan for |b(1-2u)| ~ 1e-18..1e-6. Cause: 1-mp.e**(-w*t) suffers full
# cancellation when w*t < 10^-dps at tanh-sinh nodes (t ~ 10^-23), giving q=0 exactly and
# log(q)=-inf -> 0*(-inf)=nan; the guard only removed w<1e-18. Fix: compute q in log-space
# with mp.expm1 (accurate for tiny arguments), and stabilize Nq = Gamma(al-1)(L0^{1-al}-
# L1^{1-al}) as L1^{1-al}*expm1((1-al)*ln(L0/L1)) * Gamma(al-1) (same cancellation). Zc(u)
# gets the identical expm1 form. I(p2;x) values were already unaffected (verified: v1
# rederive I(p2;x) agrees with the numpy pipeline to 3e-8).
import hashlib, pathlib
base = pathlib.Path(__file__).resolve().parent
src = (base / "rederive_100.py").read_bytes()
nl = b"\r\n" if b"\r\n" in src else b"\n"
lines = src.split(nl)
def find(pref):
    idx = [i for i, l in enumerate(lines) if l.startswith(pref)]
    assert len(idx) == 1, "prefix %r found %d times" % (pref, len(idx))
    return idx[0]
i = find(b"    Zc = lambda u:")
assert "else Lam" in lines[i+1].decode()
lines[i:i+2] = [b"    Zc = lambda u: (Lam(u,0)**(1-al)*mp.expm1((1-al)*mp.log(Lam(u,1)/Lam(u,0)))",
                b"                    / ((1-al)*b*(1-2*u)) if abs(b*(1-2*u)) > mp.mpf('1e-18') else Lam(u,mp.mpf('0.5'))**(-al))"]
j = find(b"    def Itau_u(u):")
k = find(b"        return htau - al")
lines[j:k+1] = [
    b"    def Itau_u(u):",
    b"        w = abs(b*(1-2*u)); L0 = a/2 - w/2; L1 = a/2 + w/2",
    b"        if w < mp.mpf('1e-18'):",
    b"            return mp.mpf(0)",
    b"        lnNq = mp.log(mp.gamma(al-1)) + (1-al)*mp.log(L1) + mp.log(mp.expm1((1-al)*mp.log(L0/L1)))",
    b"        lq = lambda t: (al-2)*mp.log(t) + mp.log(-mp.expm1(-w*t)) - L0*t - lnNq",
    b"        htau = -mp.quad(lambda t: mp.e**lq(t)*lq(t), [0, 1, mp.inf])",
    b"        EL = mp.quad(lambda x: pX(u, x)*mp.log(Lam(u, x)), [0, 1])",
    b"        return htau - al - mp.log(mp.gamma(al)) - (1-al)*mp.digamma(al) + EL",
]
out = nl.join(lines)
(base / "rederive_100.py").write_bytes(out)
print("bytes=%d sha256=%s eol=%s lines=%d"
      % (len(out), hashlib.sha256(out).hexdigest(), "CRLF" if nl == b"\r\n" else "LF", len(lines)))
