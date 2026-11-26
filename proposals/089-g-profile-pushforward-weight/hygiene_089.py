import hashlib
p = 'proposals/089-g-profile-pushforward-weight/insert-body.txt'
body = open(p, 'rb').read().replace(b'\r\n', b'\n').rstrip(b'\n')
out = 'proposals/089-g-profile-pushforward-weight/insert-r1.tex'
open(out, 'wb').write(body + b'\r\n')
raw = open(out, 'rb').read()
txt = raw.decode('utf-8')
c = {}
c['bytes'] = len(raw)
c['CRLF'] = raw.count(b'\r\n')
c['bareLF'] = raw.count(b'\n') - c['CRLF']
c['lines'] = txt.rstrip('\r\n').count('\n') + 1
c['emph'] = txt.count('emph')
c['dollar'] = txt.count('$')
c['brack'] = txt.count('[') + txt.count(']')
c['cite'] = txt.count(chr(92)+'cite')
c['ref'] = txt.count(chr(92)+'ref')
c['eqref'] = txt.count(chr(92)+'eqref')
c['label'] = txt.count(chr(92)+'label')
c['lp'] = txt.count('\(')
c['rp'] = txt.count('\)')
c['emdash'] = txt.count('—')
c['close_idiom'] = txt.count('they close nothing in Problem~G.')
low = txt.lower()
banned = ['status', 'priority', 'completion', 'open', 'critical', 'programme', 'derived']
c['banned'] = {w: low.count(w) for w in banned if low.count(w) > 0}
c['nonascii'] = sorted(set(hex(ord(ch)) for ch in txt if ord(ch) > 127))
c['sha256'] = hashlib.sha256(raw).hexdigest()
for k, v in c.items():
    print(k, '=', v)
ok = (c['dollar'] == 0 and c['brack'] == 0 and c['cite'] == 0 and c['ref'] == 0
      and c['eqref'] == 0 and c['label'] == 0 and c['emph'] == 1 and c['lp'] == c['rp']
      and c['close_idiom'] == 1 and c['bareLF'] == 0 and not c['banned'] and c['lines'] == 1)
print('HYGIENE', 'PASS' if ok else 'FAIL')
