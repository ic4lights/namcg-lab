import hashlib
APP = 'chapters/appH-microscopic-proofs.tex'
INS = 'proposals/089-g-profile-pushforward-weight/insert-r1.tex'
PIN = ('they establish a stationarity identity and variational rigidity within the named class, '
       'they supply no state, no selection mechanism and no weight on profile space, they do not fix '
       'the state that sets \\(W\\), \\(g\\), \\(s\\) or the frame \\(u\\), they leave the missing steps '
       '(i)-(iv) of the Missing step paragraph unchanged, and they close nothing in Problem~G.')
b = open(APP, 'rb').read()
ins = open(INS, 'rb').read()
print('PRE size=%d sha256=%s CRLF=%d bareLF=%d'
      % (len(b), hashlib.sha256(b).hexdigest(), b.count(b'\r\n'), b.count(b'\n') - b.count(b'\r\n')))
assert len(b) == 748814
assert hashlib.sha256(b).hexdigest() == 'ecb67a25a2881d35c27d3db0a482e06fff8c0ccba790f5a1db4cf3d593df6749', 'PRE MOVED'
assert b.count(b'\r\n') == 3840 and b.count(b'\n') == 3840
assert b.count(PIN.encode()) == 1, 'PIN count != 1'
i = b.find(PIN.encode())
vt = b.find(r'\emph{Vacuum term.}'.encode(), i)
assert vt > 0
gap = b[i + len(PIN):vt]
print('PIN at offset %d; gap PIN-end..Vacuum = %r' % (i, gap))
assert gap == b'\r\n\r\n', 'gap not exactly CRLFCRLF'
pre_close = b.count('they close nothing in Problem~G.'.encode())
new = b[:vt] + ins + b'\r\n' + b[vt:]
assert len(new) == len(b) + len(ins) + 2
post_crlf = new.count(b'\r\n')
post_bare = new.count(b'\n') - post_crlf
print('POST size=%d sha256=%s CRLF=%d bareLF=%d'
      % (len(new), hashlib.sha256(new).hexdigest(), post_crlf, post_bare))
print('close-idiom %d -> %d ; new-header count %d ; Vacuum-term count %d'
      % (pre_close, new.count('they close nothing in Problem~G.'.encode()),
         new.count('Pushforward weights on the profile simplex'.encode()),
         new.count(r'\emph{Vacuum term.}'.encode())))
assert new[vt:vt + len(ins)] == ins and new[vt - 4:vt] == b'\r\n\r\n'
assert new[vt + len(ins):vt + len(ins) + 20] == b'\r\n' + rb'\emph{Vacuum term.'  # one added spacer CRLF then the displaced Vacuum header
assert new[vt + len(ins) + 20:] == b[vt + 18:]  # bytes outside the insertion window are byte-identical (size delta = len(ins)+2 checked above)
assert post_bare == 0 and post_crlf == 3842
print('SIMULATION OK (read-only; no repository file written)')
