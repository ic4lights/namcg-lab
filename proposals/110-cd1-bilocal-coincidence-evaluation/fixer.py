NL = chr(10)
t = open('patch_r2.py','rb').read().decode('utf-8')
pairs = [
 ("""      'decomposes as (profile) + (radial e_rs) + (mixed e-w) + the',""",
  """      '   decomposes as (profile) + (radial e_rs) + (mixed e-w) + the',"""),
 ("""      "anticommutator connector (`run_induced.out`). The item-109 draft claims")""",
  """      "   anticommutator connector (`run_induced.out`). The item-109 draft claims")"""),
 ("""      'decomposes as (profile) + (radial e_rs) + (radial-gradient x e) +',""",
  """      '   decomposes as (profile) + (radial e_rs) + (radial-gradient x e) +',"""),
 ("""      '(mixed e-w) + the anticommutator connector',""",
  """      '   (mixed e-w) + the anticommutator connector',"""),
 ("""      "(`run_induced.out`, corrected r2 identity in R6). The item-109 draft claims"))""",
  """      "   (`run_induced.out`, corrected r2 identity in R6). The item-109 draft claims"))"""),
]
for o,n in pairs:
    assert t.count(o) == 1, o[:50]
    t = t.replace(o,n)
open('patch_r2.py','wb').write(t.encode('utf-8'))
dry = t.replace("""    assert n == 1, ('COUNTFAIL', n, old[:70])""",
                """    print(n, repr(old[:40]))""")
dry = dry.replace("""open('proposal-r2.md','wb').write""", """open('DRYOUT.md','wb').write""")
assert dry != t
open('dry.py','wb').write(dry.encode('utf-8'))
print('FIXER OK')
