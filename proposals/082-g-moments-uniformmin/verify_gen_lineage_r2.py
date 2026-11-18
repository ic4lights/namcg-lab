"""082 r2 read-only lineage proof: applying the gen_simulate_r2.py substitution
set in memory to the frozen simulate_apply_082.py reproduces the shipped
simulate_apply_082_r2.py byte-for-byte. Writes nothing.
Run: python -I proposals/082-g-moments-uniformmin/verify_gen_lineage_r2.py"""
import hashlib
import sys
sys.path.insert(0, 'proposals/082-g-moments-uniformmin')
import gen_simulate_r2 as G

src = open(G.SRC, 'r', encoding='utf-8', newline='').read()
for o in (G.B_OLD, G.I_OLD, G.S_OLD, G.D_OLD, G.C_OLD):
    assert src.count(o) == 1, o[:30]
out = src.replace(G.B_OLD, G.B_NEW).replace(G.I_OLD, G.I_NEW)
out = out.replace(G.S_OLD, G.S_NEW).replace(G.D_OLD, G.D_NEW)
out = out.replace(G.C_OLD, G.C_NEW)
ob = out.encode('utf-8')
disk = open(G.DST, 'rb').read()
print('LINEAGE OK equal' if ob == disk else 'LINEAGE FAIL')
print('transformed %d B sha8 %s; on-disk %d B sha8 %s'
      % (len(ob), hashlib.sha256(ob).hexdigest()[:8],
         len(disk), hashlib.sha256(disk).hexdigest()[:8]))
