import hashlib, re
# Hygiene audit of insert-r1.tex, per the 089 r3 template. Run from the repository root.
P = 'proposals/090-g-interaction-induced-simplex-profiles/'
raw = open(P + 'insert-r1.tex', 'rb').read()
assert len(raw) == 3735 and hashlib.sha256(raw).hexdigest()[:8] == '3a6a69c4'
B = bytes([92])
assert raw.endswith(b'\r\n')
body = raw[:-2]
assert b'\r' not in body and not [c for c in body if c < 32] and body + b'\r\n' == raw
txt = raw.decode('utf-8'); low = txt.lower()
c = dict(bytes=len(raw), CRLF=raw.count(b'\r\n'), bareLF=raw.count(b'\n') - 1,
         emph=txt.count('emph'), dollar=txt.count('$'),
         brack=txt.count('[') + txt.count(']'))
for k in ('cite', 'ref', 'eqref', 'label'): c[k] = raw.count(B + k.encode())
c['bs_eq'] = raw.count(B + b'=')
c['lp'] = raw.count(B + b'('); c['rp'] = raw.count(B + b')')
c['accInMath'] = sum(sp.count(B + bytes([q])) for sp in re.findall(B + b'\((.*?)' + B + b'\)', raw, re.S) for q in b"=^`'~.")
c['close'] = txt.count('it closes nothing in Problem~G.')
c['banned'] = {w: low.count(w) for w in 'status priority completion open critical programme derived'.split() if w in low}
c['nonascii'] = sorted(set(hex(ord(ch)) for ch in txt if ord(ch) > 127))
hdr = 'Fixed-trace beta deformation'
c['hdr_in_insert'] = txt.count(hdr)
c['hdr_in_appH_PRE'] = open('chapters/appH-microscopic-proofs.tex', 'rb').read().count(hdr.encode())
print(c)
ok = (c['dollar'] == 0 and c['brack'] == 0 and c['cite'] == 0 and c['ref'] == 0 and c['eqref'] == 0
      and c['label'] == 0 and c['emph'] == 1 and c['lp'] == c['rp'] and c['close'] == 1
      and c['bareLF'] == 0 and c['CRLF'] == 1 and not c['banned'] and c['bs_eq'] == 0
      and c['accInMath'] == 0 and c['nonascii'] == [] and c['hdr_in_insert'] == 1
      and c['hdr_in_appH_PRE'] == 0)
# no frozen prior rounds exist for 090 (round 1); header-uniqueness audited against current PRE appH.
print('HYGIENE', 'PASS' if ok else 'FAIL')
