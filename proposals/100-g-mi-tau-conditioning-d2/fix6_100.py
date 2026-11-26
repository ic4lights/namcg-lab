# fix6_100.py -- sole byte authority for mc100s.py v4. v3 normalization bug (found by direct
# check: sum(wu)=0.75 != 1): consts returned the RAW GL weights divided by Cu instead of the
# density weights raw*phi*Zf/Cu, so consts' "wu" was not f_u(u)du. Consequences: eh_ref was
# misweighted (returned E_true*C-ish, -0.7467 vs -0.2239) and the bin reference was missing
# the bin-probability normalization. Fixes: consts returns proper density weights; eh_ref
# uses the conditional density Lambda^-al/Zf(u) for x|u (times density weights); bin
# reference divided by bin probability sum(wu[sel]).
import hashlib, pathlib
base = pathlib.Path(__file__).resolve().parent
src = (base / "mc100s.py").read_bytes()
nl = b"\r\n" if b"\r\n" in src else b"\n"
lines = src.split(nl)
def find(pref):
    idx = [i for i, l in enumerate(lines) if l.startswith(pref)]
    assert len(idx) == 1, "prefix %r found %d times" % (pref, len(idx))
    return idx[0]
i = find(b"    return a, b, al, Zf, phi, (um, wu/Cu)")
lines[i] = b"    return a, b, al, Zf, phi, (um, wu*phi(um)*Zf(um)/Cu)"
j = find(b"    pdfux = phi(um)[:, None]*lam**(-al)")
lines[j] = b"    pdfux = lam**(-al)/Zf(um)[:, None]"
k = find(b"            ex = float(np.dot(wu[sel],")
lines[k] = b"            ex = float(np.dot(wu[sel], [exb(v) for v in um[sel]])/wu[sel].sum())"
out = nl.join(lines)
(base / "mc100s.py").write_bytes(out)
print("bytes=%d sha256=%s eol=%s lines=%d"
      % (len(out), hashlib.sha256(out).hexdigest(), "CRLF" if nl == b"\r\n" else "LF", len(lines)))
