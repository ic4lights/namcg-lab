# fix5_100.py -- sole byte authority for mc100s.py v3. Two independent v2 bugs:
# (1) Zf closed form used WRONG fibre endpoints: a/2+b*(1-u) and a/2-b*u instead of
#     Lambda(u,1)=a/2+w/2 and Lambda(u,0)=a/2-w/2, w=b(1-2u) (correct: q-file form).
#     Zf enters the u-normalisation Cu in consts, so BOTH the reference normalisation and
#     eh_ref were mis-scaled (ratio ~4.6 at M=2), while the direct simulation rows were fine.
# (2) eh_ref recomputed "Cu" from ALREADY-normalised weights (gives 1) and divided by it --
#     harmless but misleading; removed. (3) E[x|bin] reference was evaluated at the bin
#     CENTRE; E[x|u] is strongly convex in u, so z-scores were inflated by O(bin^2*f''/12)
#     binning bias. Replaced by the genuine bin average sum_k wu_k*E[x|u_k] over bin nodes.
import hashlib, pathlib
base = pathlib.Path(__file__).resolve().parent
src = (base / "mc100s.py").read_bytes()
nl = b"\r\n" if b"\r\n" in src else b"\n"
lines = src.split(nl)
def find(pref, nth=0):
    idx = [i for i, l in enumerate(lines) if l.startswith(pref)]
    assert len(idx) >= nth + 1, "prefix %r found %d times" % (pref, len(idx))
    return idx[nth]
i = find(b"    Zf = lambda u:")
assert lines[i+1].startswith(b"         ((a/2+b*(1-u))")
lines[i:i+2] = [b"    wv = lambda uu: b*(1-2*uu)",
                b"    Zf = lambda u: np.where(np.abs(wv(u)) < 1e-13, (a/2)**(-al),",
                b"         ((a/2+wv(u)/2)**(1-al)-(a/2-wv(u)/2)**(1-al))/((1-al)*wv(u)))"]
j = find(b"    Cu = np.sum(wu*phi(um)*Zf(um))", 1)
assert lines[j+1].strip() == b"return E/Cu"
lines[j:j+2] = [b"    return E"]
k = find(b"            ex = float(np.dot(wxq,")
lines[k:k+1] = [b"            sel = (um >= lo) & (um < hi)",
                b"            exb = lambda uu: float(np.dot(wxq, xq*Lf(uu, xq)**(-al))/np.dot(wxq, Lf(uu, xq)**(-al)))",
                b"            ex = float(np.dot(wu[sel], [exb(v) for v in um[sel]]))"]
out = nl.join(lines)
(base / "mc100s.py").write_bytes(out)
print("bytes=%d sha256=%s eol=%s lines=%d"
      % (len(out), hashlib.sha256(out).hexdigest(), "CRLF" if nl == b"\r\n" else "LF", len(lines)))
