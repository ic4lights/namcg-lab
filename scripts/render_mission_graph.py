#!/usr/bin/env python
"""Render reports/graph/mission-graph.yaml (schema v2) as a fully linked decision map.

Decision-map rule: NOTHING floats - every artifact in the manifest is wired into
the flow.
 - qm foundation nodes: boxes at the left emitting their symbols_out as circles
   (grey "emits" links); circles carry the kind-styled edges into consumers.
 - premises (assumptions/inputs): diamonds wired (purple dotted) to every node
   listed in their used_by.
 - gaps: red MISSING-TARGET nodes placed just upstream of what they block, with
   red dash-dot edges into exactly the targets named in the manifest.
 - namcg/ir problems and conditional theorems: stage columns at minimal
   derivation depth (required/conditional edges only, cycle-guarded topological
   longest path, compacted); each stage header says what the column accomplishes
   and why it sits there.
 - gr criterion items: rightmost column; gr.complete (if present) one further.
Blocked propagation: a node is BLOCKED if named in gaps, a gap symbol is in its
symbols_in, or a required edge comes from an open/blocked node (fixed point);
+open-input if only conditional edges come from open/blocked sources. supports
edges never block and never add derivation depth.
Usage: render_mission_graph.py MANIFEST.yaml OUT.png
"""
import sys, textwrap
import yaml
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Polygon

OPEN_STATES = {"open-critical", "open-optional", "goal"}
COL = {"foundation": "#dfe8f5", "open-critical": "#fde2e2", "open-optional": "#fff2cc",
       "closed-conditionally": "#e2f2e2", "derived": "#b8e6b8", "goal": "#eeeeee"}
KIND = {"required": ("#1f2937", "-", 1.5, 0.80), "conditional": ("#b36b00", "--", 1.2, 0.75),
        "supports": ("#8a8a8a", ":", 1.0, 0.60)}
PREM_C, GAP_C = "#6a1b9a", "#cc0000"
BW, BH, XS, YS = 3.0, 1.5, 4.3, 1.95
XQ, XC, XP, XG = 0.0, 0.8, 1.3, 1.75  # qm boxes, circles, premises, gap strip (x units of XS)


def main(inp, out):
    m = yaml.safe_load(open(inp, encoding="utf-8"))
    nodes = {n["id"]: n for n in m["nodes"]}
    edges = m["edges"]
    gaps = m.get("gaps", [])
    gapsyms = {g["symbol"]: g for g in gaps}
    prem = m.get("inputs", [])
    rm = m.get("render_math", {})
    disp = rm.get("displays", {})
    order = {n["id"]: k for k, n in enumerate(m["nodes"])}

    # ---- blocking propagation (fixed point)
    blocked, openinput = {}, {}
    for g in gaps:
        for b in g["blocks"]:
            blocked.setdefault(b, []).append("gap: " + g["symbol"])
    for n in nodes.values():
        for s in n["symbols_in"]:
            if s in gapsyms and "gap: " + s not in blocked.get(n["id"], []):
                blocked.setdefault(n["id"], []).append("gap: " + s)
    ch = True
    while ch:
        ch = False
        for e in edges:
            if e["kind"] not in ("required", "conditional"):
                continue
            f, t = nodes[e["from"]], nodes[e["to"]]
            if t["layer"] == "qm" or f["layer"] == "qm":
                continue
            src_open = f["state"] in OPEN_STATES or f["id"] in blocked
            if not src_open or t["state"] == "foundation":
                continue
            if e["kind"] == "required":
                tag = "upstream " + f["id"]
                if tag not in blocked.setdefault(t["id"], []):
                    blocked[t["id"]].append(tag)
                    ch = True
            else:
                if t["id"] not in blocked and f["id"] not in openinput.get(t["id"], []):
                    openinput.setdefault(t["id"], []).append(f["id"])

    # ---- layering of namcg + ir: required/conditional only; Kahn topological
    # order so mid-layer cycles cannot inflate ranks; compacted to stages.
    mid = [n for n in nodes.values() if n["layer"] in ("namcg", "ir")]
    midids = {n["id"] for n in mid}
    dedges = [(e["from"], e["to"]) for e in edges
              if e["kind"] in ("required", "conditional") and e["from"] in midids and e["to"] in midids]
    adj, indeg = {i: [] for i in midids}, {i: 0 for i in midids}
    for f, t in dedges:
        adj[f].append(t)
        indeg[t] += 1
    ind, ready = dict(indeg), sorted([i for i in midids if indeg[i] == 0], key=lambda i: order[i])
    topo = []
    while ready:
        i = ready.pop(0)
        topo.append(i)
        for t in sorted(adj[i], key=lambda j: order[j]):
            ind[t] -= 1
            if ind[t] == 0:
                ready.append(t)
        ready.sort(key=lambda j: order[j])
    seen = set()
    for i in sorted(midids, key=lambda i: order[i]):
        if i not in seen:
            topo.append(i)
            seen.add(i)
    rank = {i: 0 for i in midids}
    for i in topo:
        for t in adj[i]:
            rank[t] = max(rank[t], rank[i] + 1)
    dense = {v: k for k, v in enumerate(sorted(set(rank.values())))}
    layer = {i: dense[rank[i]] for i in midids}
    nmid = max(layer.values()) + 1

    # ---- columns: stages 2..nmid+1, gr next, gaps just upstream of first target
    gr = [n for n in nodes.values() if n["layer"] == "gr"]
    gridids = {n["id"] for n in gr}
    gcol = {}  # node id -> x column (in XS units)
    for i in midids:
        gcol[i] = 2 + layer[i]
    G = nmid + 2
    gritems = [n["id"] for n in gr if n["id"] != "gr.complete"]
    final = "gr.complete" if "gr.complete" in nodes else None
    for i in gritems:
        gcol[i] = G
    if final is not None:
        gcol[final] = G + 1
    gapids = {}
    gapedge = []
    for g in gaps:
        gid = "gap:" + g["symbol"]
        tg = [b for b in g["blocks"] if b in gcol]
        if not tg:
            continue
        c = min(gcol[b] for b in tg) - 1
        gcol[gid] = c if c >= 2 else XG
        gapids[gid] = g
        for b in tg:
            gapedge.append((gid, b))

    # ---- vertical ordering: barycentre sweeps over stage/gap/gr columns
    cols = {}
    for i, c in gcol.items():
        cols.setdefault(c, []).append(i)
    for c in cols:
        cols[c].sort(key=lambda i: order.get(i, 999))
    maxr = max(len(v) for v in cols.values())
    pos = {}
    adjc = {i: set() for i in gcol}
    for f, t in dedges:
        adjc[f].add(t)
        adjc[t].add(f)
    for e in edges:  # supports edges also help ordering (no depth, but keep neighbours close)
        f, t = e["from"], e["to"]
        if f in adjc and t in adjc:
            adjc[f].add(t)
            adjc[t].add(f)
    for f, t in gapedge:
        adjc[f].add(t)
        adjc[t].add(f)

    def place():  # each column centred on the same vertical mid-line
        for c, ids in cols.items():
            top = (maxr - 1) / 2.0 * YS
            start = top - (len(ids) - 1) / 2.0 * YS
            for r, i in enumerate(ids):
                pos[i] = (c * XS, start - r * YS)

    for it in range(8):
        place()
        keys = sorted(cols, reverse=(it % 2 == 1))
        for c in keys:
            ids = cols[c]

            def bary(i):
                ys = [pos[j][1] for j in adjc[i] if abs(pos[j][0] - pos[i][0]) > 0.5]
                return sum(ys) / len(ys) if ys else pos[i][1]
            ids.sort(key=lambda i: (bary(i), order.get(i, 999)))
    place()

    # ---- qm boxes, symbol circles (emitted by qm boxes), premise diamonds
    qmids = [n["id"] for n in m["nodes"] if n["layer"] == "qm"]
    qsyms = [(s, nid) for nid in qmids for s in nodes[nid]["symbols_out"]]
    ytop_col = max(pos[i][1] for i in gcol)
    ybot_col = min(pos[i][1] for i in gcol)
    span = (ytop_col - ybot_col) + BH
    for r, i in enumerate(qmids):  # qm boxes centred vertically
        pos[i] = (XQ * XS, (len(qmids) - 1) / 2.0 * 3.1 - r * 3.1)
    cons = {}  # circle -> consumers
    for e in edges:
        f, t = e["from"], e["to"]
        if nodes[f]["layer"] == "qm":
            for s in e["symbols"]:
                key = s.split(" -> ")[0].strip()
                if key in nodes[f]["symbols_out"]:
                    cons.setdefault(("sym", key), []).append(t)
    def cir_bary(key):
        ys = [pos[c][1] for c in cons.get(key, []) if c in pos and nodes[c]["layer"] != "qm"]
        return sum(ys) / len(ys) if ys else 0
    qsyms.sort(key=lambda so: cir_bary(("sym", so[0])))
    for k, (s, nid) in enumerate(qsyms):
        y = ytop_col + BH / 2 - k * span / max(1, len(qsyms) - 1)
        pos["sym:" + s] = (XC * XS, y)
    pcons = {}
    for i in prem:
        pcons[i["symbol"]] = [u for u in i["used_by"] if u in nodes]
    premlist = sorted(prem, key=lambda i: (sum(pos[u][1] for u in pcons[i["symbol"]] if u in pos) /
                                           max(1, len([u for u in pcons[i["symbol"]] if u in pos]))
                                           if any(u in pos for u in pcons[i["symbol"]]) else 0,
                                           i["symbol"]))
    for k, i in enumerate(premlist):
        y = ytop_col + BH / 2 - k * span / max(1, len(prem) - 1)
        pos["pre:" + i["symbol"]] = (XP * XS, y)

    # ---- figure
    last = (G + 1) if final is not None else G
    xmin, xmax = -3.0, last * XS + BW / 2 + 1.2
    ymin = min(pos[i][1] for i in pos) - BH / 2 - 1.6
    ymax = max(pos[i][1] for i in pos) + BH / 2 + 3.4
    fig_w, fig_h = (xmax - xmin) * 0.60, (ymax - ymin) * 0.63
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=110)
    ax.set_aspect("auto")
    renderer = fig.canvas.get_renderer()
    warns = {"hard": 0, "soft": 0}
    boxes = {}
    for i in set(gcol) | set(qmids):
        x, y = pos[i]
        boxes[i] = (x - BW / 2, y - BH / 2, x + BW / 2, y + BH / 2)

    def seg_hits(p, q, r):
        x0, y0, x1, y1 = r
        for k in range(1, 14):
            t = k / 14
            x = p[0] + (q[0] - p[0]) * t
            y = p[1] + (q[1] - p[1]) * t
            if x0 + .06 < x < x1 - .06 and y0 + .06 < y < y1 - .06:
                return True
        return False

    def anchor(i, ox):
        x, y = pos[i]
        if i in boxes:
            return (x + BW / 2, y) if ox > x else (x - BW / 2, y)
        return (x + 0.45, y) if ox > x else (x - 0.45, y)

    def curve(p0, p1):
        dx = (p1[0] - p0[0]) * 0.42
        c0, c1 = (p0[0] + dx, p0[1]), (p1[0] - dx, p1[1])
        pts = []
        for k in range(25):
            t = k / 24.0
            mt = 1 - t
            x = mt**3 * p0[0] + 3 * mt**2 * t * c0[0] + 3 * mt * t**2 * c1[0] + t**3 * p1[0]
            y = mt**3 * p0[1] + 3 * mt**2 * t * c0[1] + 3 * mt * t**2 * c1[1] + t**3 * p1[1]
            pts.append((x, y))
        return pts

    side_n, ncurves = {}, [0]

    def fit_math(t, i):
        fs = 8.0
        while True:
            t.set_fontsize(fs)
            bb = t.get_window_extent(renderer=renderer).transformed(ax.transData.inverted())
            if (bb.width <= BW - 0.12 and bb.height <= BH * 0.42) or fs <= 4.5:
                break
            fs -= 0.5
        if bb.width > BW - 0.12 or bb.height > BH * 0.42:
            warns["hard"] += 1
            print("WARN BOX-OVERFLOW (math clamped at 4.5pt)", i)

    def wire(a, b, color, ls, lw, alpha, z=1):
        ox, oy = pos[b]
        same = abs(pos[a][0] - ox) < 0.6 and (a in boxes and b in boxes)
        if same:  # same column: route as a side loop on the right
            k = (pos[a][1] + oy) / 2
            n = side_n.get(round(k, 2), 0)
            side_n[round(k, 2)] = n + 1
            xr = pos[a][0] + BW / 2
            off = 0.5 + 0.22 * (n % 3)
            p0, p3 = (xr, pos[a][1]), (xr, oy)
            c0, c1 = (xr + off * 1.7, pos[a][1]), (xr + off * 1.7, oy)
            pts = []
            for j in range(25):
                t = j / 24.0
                mt = 1 - t
                pts.append((mt**3 * p0[0] + 3 * mt**2 * t * c0[0] + 3 * mt * t**2 * c1[0] + t**3 * p0[0],
                            mt**3 * p0[1] + 3 * mt**2 * t * c0[1] + 3 * mt * t**2 * c1[1] + t**3 * p3[1]))
        else:
            pa = anchor(a, ox)
            pb = anchor(b, pos[a][0])
            pts = curve(pa, pb)
        ncurves[0] += 1
        xs_, ys_ = zip(*pts)
        ax.plot(xs_, ys_, color=color, ls=ls, lw=lw, alpha=alpha, zorder=z)
        ax.annotate("", xy=pts[-1], xytext=pts[-2], zorder=z,
                    arrowprops=dict(arrowstyle="-|>", color=color, ls="solid", lw=lw,
                                    shrinkA=0, shrinkB=0, alpha=min(1, alpha + 0.2)))
        for u, v in zip(pts[:-1], pts[1:]):
            for j, r in boxes.items():
                if j not in (a, b) and seg_hits(u, v, r):
                    warns["hard"] += 1
                    print("WARN wire-through-node", a, "->", b, "via", j)

    # ---- wires: qm box -> circles -> consumers; premises -> consumers; gaps -> blocks
    for nid in qmids:
        for s in nodes[nid]["symbols_out"]:
            wire(nid, "sym:" + s, "#557799", "-", 0.9, 0.65)
    for e in edges:
        f, t = e["from"], e["to"]
        color, ls, lw, al = KIND[e["kind"]]
        if nodes[f]["layer"] == "qm":
            for s in e["symbols"]:
                key = s.split(" -> ")[0].strip()
                if key in nodes[f]["symbols_out"]:
                    wire("sym:" + key, t, color, ls, lw, al)
        else:
            wire(f, t, color, ls, lw, al)
    for i in prem:
        for u in pcons[i["symbol"]]:
            wire("pre:" + i["symbol"], u, PREM_C, ":", 0.9, 0.5)
    for gid, t in gapedge:
        wire(gid, t, GAP_C, "-.", 1.6, 0.85)

    # ---- QM foundation boxes
    for nid in qmids:
        n = nodes[nid]
        x0, y0, x1, y1 = boxes[nid]
        ax.add_patch(FancyBboxPatch((x0, y0), BW, BH, boxstyle="round,pad=0.02,rounding_size=0.1",
                                    fc=COL["foundation"], ec="#3a5a7a", lw=1.4, zorder=3))
        ax.text(x0 + 0.08, y1 - 0.06, "FOUNDATION (QM)", fontsize=5.8, va="top", color="#3a5a7a", zorder=4)
        ax.text(x0 + 0.08, y1 - 0.25, "\n".join(textwrap.wrap(n["title"], 34)[:3]), fontsize=6.3,
                va="top", weight="bold", zorder=4)
        t = ax.text((x0 + x1) / 2, y0 + BH * 0.30, n["math"][0]["tex"], fontsize=7.5, ha="center",
                    va="center", zorder=4)
        fit_math(t, i=nid)

    # ---- circles (symbols emitted by the QM boxes)
    for s, nid in qsyms:
        x, y = pos["sym:" + s]
        ax.add_patch(Circle((x, y), 0.45, fc=COL["foundation"], ec="#3a5a7a", lw=1.0, zorder=3))
        sm = rm.get("symbols", {}).get(s, {})
        ax.text(x, y, sm.get("math", s), ha="center", va="center", fontsize=8.5, zorder=4)
        ax.text(x, y - 0.58, textwrap.shorten(s, 26), ha="center", va="top", fontsize=5, color="#3a5a7a",
                zorder=4, bbox=dict(boxstyle="square,pad=0.12", fc="white", ec="none", alpha=0.7))

    # ---- premise diamonds (wired into the flow)
    for i in prem:
        x, y = pos["pre:" + i["symbol"]]
        ax.add_patch(Polygon([(x - 0.5, y), (x, y + 0.45), (x + 0.5, y), (x, y - 0.45)],
                             fc="#f3e5f5", ec=PREM_C, lw=1.2, zorder=3))
        pm = rm.get("premises", {}).get(i["symbol"], {})
        halo = dict(boxstyle="square,pad=0.12", fc="white", ec="none", alpha=0.75)
        ax.text(x - 0.65, y + 0.10, i["symbol"], fontsize=5.8, va="bottom", ha="right",
                color=PREM_C, weight="bold", zorder=4, bbox=halo)
        ax.text(x - 0.65, y - 0.06, textwrap.shorten(pm.get("math", pm.get("note", i["kind"])), 30),
                fontsize=5.2, va="top", ha="right", color="#555", zorder=4, bbox=halo)

    # ---- gap nodes: missing targets, wired into what they block
    for gid, g in gapids.items():
        x, y = pos[gid]
        x0, y0, x1, y1 = boxes[gid]
        ax.add_patch(FancyBboxPatch((x0, y0), BW, BH, boxstyle="round,pad=0.02,rounding_size=0.1",
                                    fc="#fdeaea", ec=GAP_C, lw=1.6, ls="--", zorder=3))
        ax.text(x0 + 0.08, y1 - 0.06, "MISSING TARGET (gap)", fontsize=5.8, va="top", color=GAP_C, zorder=4)
        ax.text(x0 + 0.08, y1 - 0.25, "\n".join(textwrap.wrap(g["symbol"], 30)[:2]), fontsize=6.3,
                va="top", weight="bold", color="#8b0000", zorder=4)
        ax.text(x0 + 0.08, y0 + 0.42, "\n".join(textwrap.wrap(g.get("note", ""), 44)[:3]), fontsize=4.9,
                va="bottom", color="#666", zorder=4)

    # ---- derivation / GR boxes (gap boxes drawn above)
    for i in gcol:
        if i in gapids:
            continue
        n = nodes[i]
        x0, y0, x1, y1 = boxes[i]
        bl = i in blocked
        oi = i in openinput
        ec = GAP_C if bl else ("#e69500" if oi else "#333333")
        ax.add_patch(FancyBboxPatch((x0, y0), BW, BH, boxstyle="round,pad=0.02,rounding_size=0.1",
                                    fc=COL[n["state"]], ec=ec, lw=2.0 if (bl or oi) else 1.0,
                                    ls="--" if bl else "-", zorder=3))
        tag = n["state"].upper() + (" | BLOCKED" if bl else (" | +open-input" if oi else ""))
        ax.text(x0 + 0.08, y1 - 0.06, tag, fontsize=5.8, va="top", color="#8b0000" if bl else "#333", zorder=4)
        ax.text(x0 + 0.08, y1 - 0.25, "\n".join(textwrap.wrap(n["title"], 34)[:3]), fontsize=6.3,
                va="top", weight="bold", zorder=4)
        d = disp.get(i, {})
        t = ax.text((x0 + x1) / 2, y0 + BH * 0.26, d.get("math", ""), fontsize=8, ha="center", va="center", zorder=4)
        fit_math(t, i)
        ax.text(x1 - 0.06, y0 + 0.04, d.get("label", ""), fontsize=5.2, ha="right", va="bottom",
                color="#1a237e", zorder=4)
        if bl:
            why = "; ".join(blocked[i])
            ax.text(x0 + 0.08, y0 + 0.16, "BLOCKED: " + textwrap.shorten(why, 52), fontsize=4.8,
                    va="bottom", color=GAP_C, zorder=4)

    # ---- column headers
    ROLE = {"A.map": "A dictionary", "B.ward": "B Ward identity", "C.scalar": "C conformal mode",
            "D1.lorentz": "D1 local Lorentz", "E.sig": "E signature", "F.coeff": "F G_eff coefficients",
            "G.ent": "G boundary entropy", "H.nu": "H nu (optional)", "I.drag": "I drag (optional)",
            "J.ecg": "J ECG (optional)", "N.eft": "N EFT/ghost control", "ch15.lab": "Ch15 laboratory",
            "ir.leff": "IR Lambda_eff (thm:Leff)", "thm.split": "delta-Phi split",
            "thm.locking": "Lorentz locking", "thm.repairII": "composite-metric repair",
            "thm.mT": "m_T = 0", "thm.Geff": "G_eff truncated", "thm.conservation": "stress conservation"}
    NAMED = {
        tuple(sorted(["A.map", "D1.lorentz", "E.sig", "G.ent", "H.nu", "I.drag", "N.eft",
                      "ch15.lab", "thm.locking", "thm.split"])):
            "starting points: the critical targets A, D1, E, G, N fed only by QM symbols and "
            "premises, plus the conditional theorems and optional problems that start here",
        tuple(sorted(["B.ward", "thm.repairII"])):
            "prerequisites closed first: B (Ward identity, after A) and the composite-metric "
            "repair (after Lorentz locking)",
        tuple(sorted(["C.scalar", "thm.Geff", "thm.mT"])):
            "conditional-theorem core: C (conformal mode), m_T = 0 and the truncated G_eff "
            "identity, each needing a stage-1 closure in place",
        tuple(sorted(["F.coeff", "ir.leff"])):
            "the couplings: physical G_eff coefficients (F) and the IR boundary datum "
            "Lambda_eff, downstream of the G_eff identity and the repair",
        tuple(sorted(["J.ecg", "thm.conservation"])):
            "consistency and optional extension: conservation of the total stress, and the "
            "ECG solution family",
    }
    hd = {XQ: "QM foundation", XC: "symbols (emitted)", XP: "premises: every diamond is wired to the nodes that depend on it",
          XG: "missing targets: each red node blocks exactly what the manifest names"}
    for l in range(nmid):
        c = 2 + l
        ids = [i for i in cols[c] if i in midids]
        name = NAMED.get(tuple(sorted(ids)),
                         ", ".join(ROLE.get(i, i) for i in sorted(ids, key=lambda i: order[i])))
        ps = sorted({layer[f] for (f, tt) in dedges if tt in cols[c] and f in midids and layer[f] < l})
        why = ("no upstream stage: fed only by QM symbols and premises"
               if not ps else "needs stage " + (", ".join(str(p + 1) for p in ps)))
        hd[c] = "stage %d: %s (%s)" % (l + 1, name, why)
    hd[G] = "GR criterion items (the Chapter 17 targets every stage feeds)"
    if final is not None:
        hd[G + 1] = "final label"
    ytop = max(pos[i][1] for i in pos) + BH / 2 + 1.8
    for c, t in hd.items():
        ax.text(c * XS, ytop, "\n".join(textwrap.wrap(t, 40)), ha="center", va="top",
                fontsize=7.5, weight="bold", color="#444")

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ytop + 0.4)
    ax.axis("off")
    nopen = sum(1 for n in m["nodes"] if n["state"].startswith("open"))
    ax.set_title("%s  (label: %s; %d nodes, %d open, %d gaps, %d blocked; every artifact wired)" %
                 (m["title"], m["active_label"], len(nodes), nopen, len(gaps), len(blocked)), fontsize=11)
    leg = ("Edges: solid dark = required (blocks if source open); dashed amber = conditional; dotted grey = supports "
           "(helps, never blocks, never adds depth); purple dotted = node depends on premise; red dash-dot = gap blocks "
           "target; thin blue = QM box emits symbol. Boxes: state fill; red dashed border = BLOCKED (gap or required "
           "open/blocked upstream); amber border = +open-input. Stage = minimal derivation depth from QM inputs. "
           "No numerical values are drawn (the manuscript states none for these symbols).")
    fig.text(0.01, 0.004, leg, fontsize=6.5)
    fig.savefig(out, bbox_inches="tight")
    print("RENDERED %s NODES %d EDGES %d BLOCKED %d CURVES %d WARNINGS %d (hard %d, soft %d)" %
          (out, len(nodes), len(edges), len(blocked), ncurves[0],
           warns["hard"] + warns["soft"], warns["hard"], warns["soft"]))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
